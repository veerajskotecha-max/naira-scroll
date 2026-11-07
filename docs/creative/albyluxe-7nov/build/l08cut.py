# Baguette Heart Necklace (L08): the in-palm cut-out. Higgsfield's background remover kept the cube (the pendant lies on its face), so the
# necklace is cut out here: polished gold reads chroma 35+ at gold hue, where the cream backdrop reads 19 and the cube 10; the heart's stones
# are the holes inside its gold rim; specks under 150 px are dropped.  Usage: python3 -I l08cut.py -> out/L08_rb.png
import os
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
im = np.asarray(Image.open(os.path.join(H, "out", "L08_H.png")).convert("RGB")); f = im.astype(np.float32) / 255
lab = cv2.cvtColor(f, cv2.COLOR_RGB2Lab); C = np.hypot(lab[..., 1], lab[..., 2]); h = (np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) + 360) % 360
gold = ((C > 32) & (h > 55) & (h < 100)).astype(np.uint8)
gold = cv2.morphologyEx(gold, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
n, lbl, st, _ = cv2.connectedComponentsWithStats(gold, 8)
keep = np.zeros_like(gold)
for i in range(1, n):
    if st[i, 4] > 150: keep[lbl == i] = 1
filled = keep.copy(); cnts, _ = cv2.findContours(keep, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for c in cnts:
    if cv2.contourArea(c) > 20000: cv2.drawContours(filled, [c], -1, 1, -1)      # only the heart is large enough to have stones inside
a = cv2.GaussianBlur(filled.astype(np.float32), (0, 0), 0.8)
Image.fromarray(np.dstack([im, (a * 255).astype(np.uint8)])).save(os.path.join(H, "out", "L08_rb.png"))
ys, xs = np.nonzero(filled); print("bbox", xs.min(), ys.min(), xs.max(), ys.max(), "px", int(filled.sum()))
