# Aqua Oval Cocktail Ring (L18), the macro M (../corrections.md, 12 Nov): small bubble and dust specks inside the stone. Inside the stone's
# outline (its aqua pixels' hull), every tiny dot that stands out from its 9px median by more than 10 levels (up to 8px across, never a long thin line) is replaced by the median
# (facet edges are lines, not dots, and survive). The stone's pale sky blue is then moved to the mint of the other four photos by tone.py L18.
# Usage: python3 -I l18fix.py -> out/L18_Mf.png
import os
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
img = np.asarray(Image.open(os.path.join(H, "out", "L18_M.png")).convert("RGB"))
lab = cv2.cvtColor(img.astype(np.float32) / 255, cv2.COLOR_RGB2Lab); C = np.hypot(lab[..., 1], lab[..., 2]); h = (np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) + 360) % 360
aq = ((h > 150) & (h < 230) & (C > 6)).astype(np.uint8)
n, lbl, st, _ = cv2.connectedComponentsWithStats(cv2.morphologyEx(aq, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8)))
stone = np.zeros_like(aq); cv2.fillConvexPoly(stone, cv2.convexHull(cv2.findNonZero((lbl == 1 + np.argmax(st[1:, 4])).astype(np.uint8))), 1)
stone = cv2.erode(stone, np.ones((15, 15), np.uint8))                                       # inside the bezel only
med = cv2.medianBlur(img, 9); d = np.abs(img.astype(np.int16) - med.astype(np.int16)).max(2)
spk = ((d > 10) & (stone > 0)).astype(np.uint8)
n, lbl, st, _ = cv2.connectedComponentsWithStats(spk); dots = np.zeros_like(spk)
for i in range(1, n):
    x, y, w, hh, a = st[i]
    if a <= 40 and max(w, hh) <= 8 and min(w, hh) >= max(w, hh) / 3: dots[lbl == i] = 1      # a dot, not a facet line
m = cv2.GaussianBlur(cv2.dilate(dots, np.ones((3, 3), np.uint8)).astype(np.float32), (0, 0), 0.8)[..., None]
out = img * (1 - m) + med * m
Image.fromarray(np.clip(out, 0, 255).round().astype(np.uint8)).save(os.path.join(H, "out", "L18_Mf.png")); print("specks", int(dots.sum()), "px")
