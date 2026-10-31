# Emerald Station Snake Chain (B02): the buy-book photo shows the two side stations in colour, a rose pink stone on the left and a pale
# champagne yellow one on the right, but the shoot drew both clear. This tints ONLY those two stones, inside an ellipse fitted to each
# stone in each frame (boxes found on gridded crops), keeping every facet's lightness so the cut and sparkle stay; the gold bezels and the
# skin around them carry colour already (CIELab chroma above about 16) and are left alone. Left and right are as the viewer sees them.
# Usage: python3 -I sidestones.py   (out/B02_{H,W1,W2,M}.png -> out/B02_{H,W1,W2,M}_side.png)
import os
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "out")
PINK, CHAMPAGNE = (26, 2), (24, 76)                       # chroma, hue (degrees)
BOXES = {"B02_H": [(548, 848, 617, 912, PINK), (1160, 1225, 1247, 1303, CHAMPAGNE)],
         "B02_M": [(472, 514, 594, 624, PINK), (1480, 1060, 1624, 1184, CHAMPAGNE)],
         "B02_W1": [(618, 1122, 648, 1147, PINK), (1222, 1131, 1251, 1155, CHAMPAGNE)],
         "B02_W2": [(661, 1303, 711, 1344, PINK), (1221, 1266, 1265, 1302, CHAMPAGNE)]}   # x0, y0, x1, y1 of the stone
def ramp(x, a, b): return np.clip((x - a) / (b - a), 0, 1)
for stem, boxes in BOXES.items():
    rgb = np.asarray(Image.open(os.path.join(OUT, stem + ".png")).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab); L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]; C = np.hypot(A, B)
    out = lab.copy()
    for x0, y0, x1, y1, (ct, ht) in boxes:
        ell = np.zeros(L.shape, np.float32)
        cv2.ellipse(ell, (int((x0 + x1) / 2), int((y0 + y1) / 2)), (int((x1 - x0) * 0.47), int((y1 - y0) * 0.47)), 0, 0, 360, 1.0, -1)
        w = cv2.GaussianBlur(ell, (0, 0), 1.5) * (1 - ramp(C, 12, 18))       # the clear stone only, never the gold or skin
        k = ct * (0.45 + 0.55 * (1 - ramp(L, 82, 98))) * (0.7 + 0.3 * ramp(L, 15, 35))   # white highlights and black facets keep less colour
        if ht > 40: k = k * (0.25 + 0.75 * ramp(L, 35, 65))                              # a dark yellow facet reads olive: keep those near grey
        out[..., 0] = out[..., 0] * (1 - w) + (L * 0.96 if ht < 40 else np.minimum(L * 1.03 + 2, 99)) * w
        out[..., 1] = out[..., 1] * (1 - w) + k * np.cos(np.radians(ht)) * w
        out[..., 2] = out[..., 2] * (1 - w) + k * np.sin(np.radians(ht)) * w
        print(stem, (x0, y0, x1, y1), "px", int((w > 0.5).sum()))
    res = np.clip(cv2.cvtColor(out.astype(np.float32), cv2.COLOR_Lab2RGB), 0, 1)
    Image.fromarray((res * 255 + 0.5).astype(np.uint8)).save(os.path.join(OUT, stem + "_side.png"))
