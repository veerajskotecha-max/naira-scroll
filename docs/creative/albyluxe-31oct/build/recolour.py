# Stone-only recolours for the 31 Oct rings, after ../../clover-garland/build/recolour.py: the green stones in the approved
# photos become the other colours the supplier makes, so the ring, its size, the light and the model stay identical.
#   Duet Emerald-Cut Ring (A04): the green emerald-cut becomes Pink (the soft pink in the owner's photo) or Clear (#19);
#   Oval Duet Ring (A05): the emerald-green oval becomes Sapphire Blue, Citrine Yellow or Olive Green (the supplier's four).
# The green stone sits at CIELab hue 120-200 degrees with clear chroma; gold, skin, plaster, hair and the saffron camisole sit
# below 100, so a hue window picks the stone alone. In worn frames only pixels within about 80px of the stone change.
# A colour keeps each pixel's shading relative to the stone's median; Clear maps lightness by rank onto a clear stone's.
# Macro frames (<SKU>_M) use macro_weights instead: the whole stone outline, dark facets included, and the glow on the plaster.
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

def macro_weights(L, C, h):
    # Macro frames show the stone large, with near-black facets that carry almost no colour and a green glow cast on the plaster.
    # Inside the stone's outline (the convex hull of its coloured core, grown 20px) every green or dark pixel that is not gold
    # changes; outside it only the glow's hue changes (lightness kept), fading out within about 150px.
    core = ((C > 12) & (h > 120) & (h < 215)).astype(np.uint8)
    n, lbl, st, _ = cv2.connectedComponentsWithStats(core, 8)
    big = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    pts = cv2.findNonZero((lbl == big).astype(np.uint8))
    hull = np.zeros(L.shape, np.uint8); cv2.fillConvexPoly(hull, cv2.convexHull(pts), 1)
    region = cv2.dilate(hull, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41))).astype(np.float32)
    gold = ramp(C, 12, 18) * ramp(h, 40, 50) * (1 - ramp(h, 92, 102)) * ramp(L, 30, 40)
    greenish = ramp(C, 3, 8) * ramp(h, 95, 105) * (1 - ramp(h, 228, 242)); dark = 1 - ramp(L, 22, 35)
    w_in = region * (1 - gold) * np.maximum(greenish, dark)
    far = cv2.GaussianBlur(cv2.dilate(hull, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (301, 301))).astype(np.float32), (0, 0), 40)
    w_out = (1 - region) * far * greenish * (1 - gold)
    return [cv2.GaussianBlur(w.astype(np.float32), (0, 0), 1.2) for w in (w_in, w_out)] + [hull.astype(bool)]

def recolour_macro(stem, colour):
    lab, L, C, h = load(os.path.join(OUT, stem + ".png")); w_in, w_out, hull = macro_weights(L, C, h)
    stone = hull & (w_in > 0.6); lab2 = lab.copy(); A, B = lab[..., 1], lab[..., 2]
    if colour == "clear":
        Ln = np.interp(L, np.percentile(L[stone], [1, 5, 25, 50, 75, 95, 99.5]), CLEAR)
        lab2[..., 0] = L * (1 - w_in) + Ln * w_in
        a_t, b_t = NEUTRAL[0], NEUTRAL[1]; a_o, b_o = NEUTRAL[0], NEUTRAL[1]
        lab2[..., 1] = A * (1 - w_in - w_out) + a_t * w_in + a_o * w_out
        lab2[..., 2] = B * (1 - w_in - w_out) + b_t * w_in + b_o * w_out
    else:
        Lt, Ct, ht, k = TARGET[colour]; Lm, Cm = np.median(L[stone]), np.median(C[stone])
        L2 = np.clip(Lt + (L - Lm) * k, 4, 98); C2 = Ct * np.clip((C / Cm) ** 0.6, 0.55, 1.6)
        Co = np.minimum(C, Ct)  # the glow keeps its own strength, never more than the stone's
        lab2[..., 0] = L * (1 - w_in) + L2 * w_in
        lab2[..., 1] = A * (1 - w_in - w_out) + C2 * np.cos(np.radians(ht)) * w_in + Co * np.cos(np.radians(ht)) * w_out
        lab2[..., 2] = B * (1 - w_in - w_out) + C2 * np.sin(np.radians(ht)) * w_in + Co * np.sin(np.radians(ht)) * w_out
    save(lab2, os.path.join(OUT, f"{stem}_{colour}.png")); return int(stone.sum())

def recolour(stem, colour):
    if stem.endswith("_M"): return recolour_macro(stem, colour)
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
