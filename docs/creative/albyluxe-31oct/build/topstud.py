# Pastel Line Drop Earrings (B06): the supplier's top stud is a LILAC cushion, but the shoot drew it pink, the same as the oval
# below it. This recolours ONLY the top cushion in the three frames that show it (the hero's two studs, one in each worn frame),
# inside a small box around each stud, to the house lilac measured on the Pastel Trio Cluster Studs' lilac stone (B05_H: CIELab
# L 70, C 17, hue 325). Each pixel keeps its shading relative to the stud's median, as recolour.py does; gold (hue 40-110) is untouched.
# Usage: python3 -I topstud.py   (out/B06_{H,W1,W2}.png -> out/B06_{H,W1,W2}_lilac.png)
import os
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "out")
LT, CT, HT, K = 67, 17, 323, 0.9
BOXES = {"B06_H": [(696, 548, 88, 89), (1013, 566, 90, 89)], "B06_W1": [(1006, 478, 43, 41)], "B06_W2": [(1148, 495, 55, 55)]}  # x, y, w, h
def ramp(x, a, b): return np.clip((x - a) / (b - a), 0, 1)
for stem, boxes in BOXES.items():
    rgb = np.asarray(Image.open(os.path.join(OUT, stem + ".png")).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab); L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.hypot(A, B); h = (np.degrees(np.arctan2(B, A)) + 360) % 360; hs = (h + 180) % 360 - 180  # signed hue, pink near 0
    box = np.zeros(L.shape, np.float32)
    for x, y, w, hh in boxes:
        box[max(0, y - 10):y + hh + 10, max(0, x - 10):x + w + 10] = 1
    hue = ramp(hs, -45, -32) * (1 - ramp(hs, 18, 28))           # pink window, -32..+18 degrees, soft edges
    wt = cv2.GaussianBlur((ramp(C, 5, 12) * hue * box).astype(np.float32), (0, 0), 0.8)
    core = (wt > 0.6) & (C > 12)
    Lm, Cm = np.median(L[core]), np.median(C[core])
    L2 = np.clip(LT + (L - Lm) * K, 4, 98); C2 = np.clip(CT * (np.maximum(C, 0.1) / Cm) ** 0.6, 0, 60)
    out = lab.copy()
    out[..., 0] = L * (1 - wt) + L2 * wt
    out[..., 1] = A * (1 - wt) + C2 * np.cos(np.radians(HT)) * wt
    out[..., 2] = B * (1 - wt) + C2 * np.sin(np.radians(HT)) * wt
    res = np.clip(cv2.cvtColor(out.astype(np.float32), cv2.COLOR_Lab2RGB), 0, 1)
    Image.fromarray((res * 255 + 0.5).astype(np.uint8)).save(os.path.join(OUT, stem + "_lilac.png"))
    print(stem, "stud px", int(core.sum()), "median L %.0f C %.0f" % (Lm, Cm))
