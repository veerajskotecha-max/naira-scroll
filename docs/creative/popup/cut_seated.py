# Usage: python3 -I cut_seated.py  (reads <scratchpad>/pop2/src.jpg and mask_birefnet-portrait.png from cutout.py's rembg run)
# Two layers from the seated stall photo: person.png (her alone) and table.png (trays, boxes and the front of the table),
# so florals can sit between them and hide where the chair was.
import cv2, numpy as np
from PIL import Image
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/pop2"
im = cv2.imread(f"{SP}/src.jpg"); H, W = im.shape[:2]
rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
person = cv2.imread(f"{SP}/mask_birefnet-portrait.png", 0)
edge = [(300, 1352), (440, 1345), (655, 1288), (840, 1238), (990, 1196), (995, 1172), (1060, 1170), (1062, 900), (W, 900)]
table = np.zeros((H, W), np.uint8); cv2.fillPoly(table, [np.array(edge + [(W, H), (300, H)], np.int32)], 255)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV); hh = hsv[..., 0].astype(int)
b, g, r = [im[..., i].astype(int) for i in range(3)]
s, v = hsv[..., 1].astype(int), hsv[..., 2].astype(int)
wall = ((s < 30) & (v > 165)).astype(np.uint8)
n, lab = cv2.connectedComponents((wall & (table > 0)).astype(np.uint8), connectivity=4)
out = cv2.dilate((table == 0).astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)
touch = set(np.unique(lab[out & (lab > 0)])) - {0}
table[np.isin(lab, list(touch)) & (np.arange(H)[:, None] < 1240)] = 0
# wall above and beside the pink jewellery box (darker in shadow)
box = np.zeros((H, W), bool); box[860:990, 1040:W] = True
table[box & (s < 34) & (v > 120) & (v < 235) & ~((r - b) > 18)] = 0
carpet = ((g - r > 22) & (g - b > 6) & (hh > 38) & (hh < 90)).astype(np.uint8)
table[cv2.morphologyEx(carpet, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)) > 0] = 0
table = cv2.GaussianBlur(table, (0, 0), 1.2)
X0, Y0, Y1 = 300, 740, 1900
for name, a in (("person", person), ("table", table)):
    Image.fromarray(np.dstack([rgb, a])[Y0:Y1, X0:]).save(f"{SP}/{name}.png")
p = Image.open(f"{SP}/person.png"); t = Image.open(f"{SP}/table.png")
c = Image.new("RGB", p.size, (40, 32, 28)); c.paste(p, (0, 0), p); c.paste(t, (0, 0), t)
c.resize((560, round(560 * c.height / c.width))).save(f"{SP}/_layers.jpg", quality=86); print(p.size)
