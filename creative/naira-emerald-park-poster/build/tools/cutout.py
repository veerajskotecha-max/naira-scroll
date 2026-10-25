"""photo4_srgb.jpg -> alpha.png / cutout.png: table polygon (minus carpet) + BiRefNet stands + traced bag."""
import sys, cv2, numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
D = Path(sys.argv[1])
im = Image.open(D / "photo4_srgb.jpg").convert("RGB"); W, H = im.size
SS = 4

def poly(pts):
    m = Image.new("L", (W * SS, H * SS), 0)
    ImageDraw.Draw(m).polygon([(x * SS, y * SS) for x, y in pts], fill=255)
    return np.asarray(m.resize((W, H), Image.LANCZOS)).astype(np.float32) / 255

# back edge of the table, left -> right (wall / chairs / person above it)
BACK = [(0, 1060), (238, 1060), (238, 848), (330, 846), (470, 846), (690, 846), (700, 1000), (840, 1000),
        (966, 1000), (972, 882), (1117, 834), (1126, 825), (1195, 810), (1260, 797), (1290, 793), (1291, 781),
        (1310, 779), (1310, 670), (1348, 665), (1370, 743), (1448, 745), (1432, 795), (1468, 791), (1512, 790)]
table = poly(BACK + [(W, H), (0, H)])
bag = poly([(0, 702), (60, 699), (186, 697), (200, 703), (214, 714), (238, 848), (240, 1062), (0, 1062)])

# carpet: dark saturated green, connected to the frame edge, in the lower half
hsv = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2HSV).astype(np.float32)
h, s, v = hsv[..., 0] * 2, hsv[..., 1] / 255, hsv[..., 2] / 255
c = ((h > 70) & (h < 190) & (s > 0.30) & (v < 0.42)).astype(np.uint8)
c[:1000] = 0
c = cv2.morphologyEx(c, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
c = cv2.morphologyEx(c, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(c)
keep = np.zeros_like(c)
for i in range(1, n):
    x, y, w, hh, a = st[i]
    if a > 3000 and (x == 0 or x + w >= W or y + hh >= H): keep[lab == i] = 1
carpet = cv2.GaussianBlur(keep.astype(np.float32), (0, 0), 1.2)

stands = np.asarray(Image.open(D / "mattes" / "full_birefnet.png").convert("L")).astype(np.float32) / 255
box = np.zeros_like(stands); box[640:1250, 200:1000] = 1
stands = stands * box

alpha = np.maximum.reduce([table * (1 - carpet), stands, bag])
alpha = np.clip(alpha, 0, 1)
A = Image.fromarray((alpha * 255).astype(np.uint8))
A.save(D / "alpha.png")
rgba = im.copy(); rgba.putalpha(A); rgba.save(D / "cutout.png")
print("carpet px", int(keep.sum()), "alpha mean", round(float(alpha.mean()), 3))

# chair (dark red) and the orange outfit showing between the necklace stand's teeth
x0, y0, x1, y1 = 800, 650, 978, 1000
sub = hsv[y0:y1, x0:x1]
hh, ss, vv = sub[..., 0] * 2, sub[..., 1] / 255, sub[..., 2] / 255
yy, xx = np.mgrid[y0:y1, x0:x1]
felt = ((xx - 920) / 54.0) ** 2 + ((yy - 872) / 172.0) ** 2 <= 1   # pendants on the felt stay
red = ((((hh < 24) | (hh > 320)) & (ss > 0.42)) & ~felt).astype(np.uint8)
red = cv2.dilate(red, np.ones((3, 3), np.uint8))
red = cv2.GaussianBlur(red.astype(np.float32), (0, 0), 0.8)
alpha[y0:y1, x0:x1] *= (1 - np.clip(red * 1.4, 0, 1))
A = Image.fromarray((np.clip(alpha, 0, 1) * 255).astype(np.uint8))
A.save(D / "alpha.png")
rgba = im.copy(); rgba.putalpha(A); rgba.save(D / "cutout.png")
print("red px removed", int((red > 0.5).sum()))
