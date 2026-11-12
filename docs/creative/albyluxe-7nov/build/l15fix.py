# Emerald-Cut Bezel Studs (L15), worn frames (../corrections.md, 12 Nov): flower-like clusters of dots sit inside the stone at its cut corners
# (W1 top-right and bottom-right, W2 all four), reading as claws or pave on a stone that is clean to its corners (L15_H is clean). It is
# their DARK dots that read as claws: in those corners every pixel darker than its 7px median is lifted to it (feathered), so the dots go
# and the facets' bright sparkle stays (a plain median there left milky blobs). W2 also has streaky,
# over-sharpened skin on the collarbone and chest: a light edge-keeping smoothing there, on skin only (never the stud, hair or silk).
# Usage: python3 -I l15fix.py -> out/L15_W1f.png, out/L15_W2f.png
import os
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
CORNERS = {"L15_W1": [(770, 526, 787, 545), (786, 580, 804, 600)],
           "L15_W2": [(1142, 502, 1160, 520), (1196, 506, 1216, 538), (1132, 580, 1156, 606), (1178, 578, 1206, 606)]}
for k, boxes in CORNERS.items():
    img = np.asarray(Image.open(os.path.join(H, "out", k + ".png")).convert("RGB"))
    med = cv2.medianBlur(img, 7); m = np.zeros(img.shape[:2], np.float32)
    for x0, y0, x1, y1 in boxes: m[y0:y1, x0:x1] = 1
    Li = img.astype(np.float32).mean(2); Lm = med.astype(np.float32).mean(2)
    m = (cv2.GaussianBlur(m, (0, 0), 1.5) * np.clip((Lm - Li - 3) / 6, 0, 1))[..., None]   # only what is darker than round it
    out = img * (1 - m) + med * m
    if k == "L15_W2":
        f = out.astype(np.float32) / 255; lab = cv2.cvtColor(f, cv2.COLOR_RGB2Lab); C = np.hypot(lab[..., 1], lab[..., 2])
        hue = (np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) + 360) % 360
        skin = ((hue > 38) & (hue < 68) & (C > 14) & (C < 46) & (lab[..., 0] > 32) & (lab[..., 0] < 82)).astype(np.float32)
        skin[:1050] = 0                                                                   # the collarbone and chest only
        skin = cv2.GaussianBlur(cv2.erode(skin, np.ones((7, 7), np.uint8)), (0, 0), 4)[..., None] * 0.6
        sm = cv2.bilateralFilter(out.astype(np.uint8), 9, 18, 6).astype(np.float32)
        out = out * (1 - skin) + sm * skin
    Image.fromarray(np.clip(out, 0, 255).round().astype(np.uint8)).save(os.path.join(H, "out", k + "f.png")); print(k, "->", k + "f")
