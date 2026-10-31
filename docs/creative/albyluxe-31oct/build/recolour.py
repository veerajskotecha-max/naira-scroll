# Stone-only recolours for the 31 Oct rings, after ../../clover-garland/build/recolour.py: the green stones in the approved
# photos become the other colours the supplier makes, so the ring, its size, the light and the model stay identical.
#   Duet Emerald-Cut Ring (A04): the green emerald-cut becomes Pink (the soft pink in the owner's photo) or Clear (#19);
#   Oval Duet Ring (A05): the emerald-green oval becomes Sapphire Blue, Citrine Yellow or Olive Green (the supplier's four).
# The green stone sits at CIELab hue 120-200 degrees with clear chroma; gold, skin, plaster, hair and the saffron camisole sit
# below 100, so a hue window picks the stone alone. In worn frames only pixels within about 80px of the stone change.
# A colour keeps each pixel's shading relative to the stone's median; Clear maps lightness by rank onto a clear stone's.
# Usage: python3 -I recolour.py STEM:COLOUR ...  (out/<STEM>.png -> out/<STEM>_<colour>.png)
import os, sys
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "out")
TARGET = {"pink": (75, 33, 6, 0.85), "sapphire": (36, 46, 285, 1.0), "citrine": (80, 62, 88, 0.8), "olive": (52, 34, 112, 0.9)}
CLEAR = [40, 62, 84, 92, 97, 99.5, 100]
NEUTRAL = (0.8, 2.0)

def ramp(x, a, b): return np.clip((x - a) / (b - a), 0, 1)
def load(p):
    rgb = np.asarray(Image.open(p).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab); A, B = lab[..., 1], lab[..., 2]
    return lab, lab[..., 0], np.hypot(A, B), (np.degrees(np.arctan2(B, A)) + 360) % 360
def save(lab, p):
    rgb = np.clip(cv2.cvtColor(lab.astype(np.float32), cv2.COLOR_Lab2RGB), 0, 1); Image.fromarray((rgb * 255 + 0.5).astype(np.uint8)).save(p)

def weights(L, C, h, worn):
    hw = ramp(h, 105, 122) * (1 - ramp(h, 215, 232))
    w_ab = ramp(C, 4, 12) * hw; w_l = ramp(C, 8, 16) * hw
    core = (w_l > 0.5).astype(np.uint8)
    # the stone's darkest facets keep little colour: dark, low-chroma pixels right next to the stone go too (not the gold)
    near = cv2.dilate(core, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))) > 0
    gold = (h > 40) & (h < 110) & (C > 12)
    edge = (near & ~gold & (L < 55)).astype(np.float32)
    w_ab, w_l = np.maximum(w_ab, edge), np.maximum(w_l, edge)
    if worn:
        zone = cv2.dilate(core, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (81, 81))).astype(np.float32)
        zone = cv2.GaussianBlur(zone, (0, 0), 8); w_ab, w_l = w_ab * zone, w_l * zone
    return [cv2.GaussianBlur(w.astype(np.float32), (0, 0), 0.8) for w in (w_ab, w_l)]

def recolour(stem, colour):
    lab, L, C, h = load(os.path.join(OUT, stem + ".png")); w_ab, w_l = weights(L, C, h, "_W" in stem)
    core = w_l > 0.6; lab2 = lab.copy()
    if colour == "clear":
        Ln = np.interp(L, np.percentile(L[core], [1, 5, 25, 50, 75, 95, 99.5]), CLEAR)
        lab2[..., 0] = L * (1 - w_l) + Ln * w_l
        lab2[..., 1] = lab[..., 1] * (1 - w_ab) + NEUTRAL[0] * w_ab; lab2[..., 2] = lab[..., 2] * (1 - w_ab) + NEUTRAL[1] * w_ab
    else:
        Lt, Ct, ht, k = TARGET[colour]; Lm, Cm = np.median(L[core]), np.median(C[core])
        L2 = np.clip(Lt + (L - Lm) * k, 4, 98); C2 = np.clip(Ct * (C / Cm) ** 0.6, 0, 80)
        lab2[..., 0] = L * (1 - w_l) + L2 * w_l
        lab2[..., 1] = lab[..., 1] * (1 - w_ab) + C2 * np.cos(np.radians(ht)) * w_ab
        lab2[..., 2] = lab[..., 2] * (1 - w_ab) + C2 * np.sin(np.radians(ht)) * w_ab
    save(lab2, os.path.join(OUT, f"{stem}_{colour}.png")); return int(core.sum())

if __name__ == "__main__":
    for a in sys.argv[1:]:
        stem, colour = a.split(":"); print(stem, colour, "stone px", recolour(stem, colour))
