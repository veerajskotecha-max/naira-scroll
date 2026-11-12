# Stone-only recolours for the 7 Nov Albyluxe pieces, a copy of ../../albyluxe-31oct/build/recolour.py: the stones in the approved
# photos become the other colours the owner asked for, so the piece, its size, the light and the model stay identical.
#   Interlocked Baguette Trio Ring (L10) and Zigzag Gem Eternity Ring (L14): the green stones become Red or White (clear);
#   Duet Emerald-Cut Cuff (L09): the pink emerald-cut becomes Clear or Aqua (SOURCE "pink": the pink stone sits at CIELab hue
#   about 340-30 degrees, away from the gold, skin and camisole at 40-100, so the same hue-window method picks it alone).
# The green stone sits at CIELab hue 120-200 degrees with clear chroma; gold, skin, plaster, hair and the saffron camisole sit
# below 100, so a hue window picks the stone alone. In worn frames only pixels within about 80px of the stone change.
# A colour keeps each pixel's shading relative to the stone's median; Clear (and White) maps lightness by rank onto a clear stone's.
# Macro frames (<SKU>_M) use macro_weights instead: the whole stone outline, dark facets included, and the glow on the plaster.
# Usage: python3 -I recolour.py STEM:COLOUR[:SOURCE[:X0,Y0,X1,Y1]] ...  (the box limits the change to the stone, where lips or skin come near its hue)  (out/<STEM>.png -> out/<STEM>_<colour>.png; SOURCE green (default) or pink)
import os, sys
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "out")
# 12 Nov (../corrections.md): red is the supplier's darker, softer ruby (C about 36-39, was 52); aqua the supplier's sky blue (L 60, C 15,
# hue 241; was a lighter, greener turquoise).
TARGET = {"red": (32, 42, 30, 0.9), "aqua": (60, 15, 241, 0.7)}
CLEAR = [40, 62, 84, 92, 97, 99.5, 100]
CLEAR_WORN = [25, 45, 70, 85, 94, 98.5, 100]   # many small stones on the hand read grey or milky on the narrower curve
NEUTRAL = (0.8, 2.0)

def ramp(x, a, b): return np.clip((x - a) / (b - a), 0, 1)
SRC = "green"
BOX = None
def boxmask(shape):
    if BOX is None: return 1.0
    m = np.zeros(shape, np.float32); x0, y0, x1, y1 = BOX; m[y0:y1, x0:x1] = 1
    return cv2.GaussianBlur(m, (0, 0), 6)
def hwin(h):                                   # the source stone's hue window, soft-edged
    if SRC == "pink":
        d = np.abs(((h - 5 + 180) % 360) - 180); return 1 - ramp(d, 26, 36)     # our pink stone: median hue 15, chroma 23
    return ramp(h, 105, 122) * (1 - ramp(h, 215, 232))
def load(p):
    rgb = np.asarray(Image.open(p).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab); A, B = lab[..., 1], lab[..., 2]
    return lab, lab[..., 0], np.hypot(A, B), (np.degrees(np.arctan2(B, A)) + 360) % 360
def save(lab, p):
    rgb = np.clip(cv2.cvtColor(lab.astype(np.float32), cv2.COLOR_Lab2RGB), 0, 1); Image.fromarray((rgb * 255 + 0.5).astype(np.uint8)).save(p)

def weights(L, C, h, worn):
    hw = hwin(h) * boxmask(h.shape)
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
    core = ((C > 12) & (hwin(h) * boxmask(h.shape) > 0.9)).astype(np.uint8)
    n, lbl, st, _ = cv2.connectedComponentsWithStats(core, 8)
    big = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    pts = cv2.findNonZero((lbl == big).astype(np.uint8))
    hull = np.zeros(L.shape, np.uint8); cv2.fillConvexPoly(hull, cv2.convexHull(pts), 1)
    if SRC == "pink":
        # 12 Nov (../corrections.md): the pink stone's centre carries warm, low-chroma peach that the hue window missed (a peach patch was
        # left in Clear and Aqua), and the 41px growth reached the gold wall and claws (grey or teal specks): grow the hull 5px only, take
        # warm low-chroma pixels inside it too, and keep anything clearly gold out
        region = cv2.dilate(hull, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))).astype(np.float32)
        gold = ramp(C, 24, 28) * ramp(h, 52, 58) * (1 - ramp(h, 100, 106))
        glow = ramp(C, 3, 8) * hwin(h)                                    # outside the stone only its own pink glow (never the cream plaster)
        greenish = np.maximum(glow, (1 - ramp(C, 22, 28)) * ramp(h, 28, 32) * (1 - ramp(h, 56, 60)) * ramp(C, 2, 5))
    else:
        region = cv2.dilate(hull, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41))).astype(np.float32)
        gold = ramp(C, 12, 18) * ramp(h, 40, 50) * (1 - ramp(h, 92, 102)) * ramp(L, 30, 40)
        greenish = ramp(C, 3, 8) * ramp(h, 95, 105) * (1 - ramp(h, 228, 242)); glow = greenish
    dark = 1 - ramp(L, 22, 35)
    w_in = region * (1 - gold) * np.maximum(greenish, dark)
    far = cv2.GaussianBlur(cv2.dilate(hull, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (301, 301))).astype(np.float32), (0, 0), 40)
    w_out = (1 - region) * far * glow * (1 - gold)
    return [cv2.GaussianBlur(w.astype(np.float32), (0, 0), 1.2) for w in (w_in, w_out)] + [hull.astype(bool)]

def recolour_macro(stem, colour):
    lab, L, C, h = load(os.path.join(OUT, stem + ".png")); w_in, w_out, hull = macro_weights(L, C, h)
    stone = hull & (w_in > 0.6); lab2 = lab.copy(); A, B = lab[..., 1], lab[..., 2]
    if colour in ("clear", "white"):
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

MANY = ("L10_", "L14_")       # many stones in the macro too: the whole-frame method, not the one-stone outline of macro_weights

def stone_weights(L, C, h):
    # 12 Nov, for the many-stone rings (L10, L14): the 7 Nov weights left olive rims, half-green back holes and near-black flecks.
    # Now each green stone's core is taken whole: its convex hull, grown 4px, and inside it every pixel that is not gold changes,
    # green at any strength (hue 85-240 at chroma 3 and up, which catches rims and out-of-focus stones) or dark (its darkest facets).
    # Silver rails and white highlights (bright and colourless) stay as they are.
    core = ((C > 12) & (hwin(h) * boxmask(h.shape) > 0.9)).astype(np.uint8)
    n, lbl, st, _ = cv2.connectedComponentsWithStats(core, 8); region = np.zeros(L.shape, np.uint8)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] < 4: continue
        cv2.fillConvexPoly(region, cv2.convexHull(cv2.findNonZero((lbl == i).astype(np.uint8))), 1)
    region = cv2.dilate(region, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))).astype(np.float32)
    gold = ramp(C, 12, 18) * ramp(h, 40, 50) * (1 - ramp(h, 100, 110))
    bright = ramp(L, 68, 78) * (1 - ramp(C, 4, 8))
    greenish = ramp(C, 3, 6) * ramp(h, 80, 90) * (1 - ramp(h, 235, 245)); dark = 1 - ramp(L, 38, 48)
    w = cv2.GaussianBlur((region * (1 - gold) * (1 - bright) * np.maximum(greenish, dark)).astype(np.float32), (0, 0), 0.8)
    return w, region > 0

def recolour(stem, colour):
    if "_M" in stem and not stem.startswith(MANY): return recolour_macro(stem, colour)
    lab, L, C, h = load(os.path.join(OUT, stem + ".png"))
    if stem.startswith(MANY): w_l, _ = stone_weights(L, C, h); w_ab = w_l
    else: w_ab, w_l = weights(L, C, h, "_W" in stem)
    core = w_l > 0.6; lab2 = lab.copy()
    if colour in ("clear", "white"):
        curve = CLEAR_WORN if (stem.startswith(MANY) and "_W" in stem) else CLEAR      # the dark facets go through the curve too: no black flecks
        Ln = np.interp(L, np.percentile(L[core], [1, 5, 25, 50, 75, 95, 99.5]), curve)
        lab2[..., 0] = L * (1 - w_l) + Ln * w_l
        lab2[..., 1] = lab[..., 1] * (1 - w_ab) + NEUTRAL[0] * w_ab; lab2[..., 2] = lab[..., 2] * (1 - w_ab) + NEUTRAL[1] * w_ab
    else:
        Lt, Ct, ht, k = TARGET[colour]; Lm, Cm = np.median(L[core]), np.median(C[core])
        L2 = np.clip(Lt + (L - Lm) * k, 4, 98); C2 = np.clip(Ct * (C / Cm) ** 0.6, 0, 80)
        if stem.startswith(MANY): C2 = np.maximum(C2, 0.5 * Ct)                               # a dark facet is a dark red, never grey
        lab2[..., 0] = L * (1 - w_l) + L2 * w_l
        lab2[..., 1] = lab[..., 1] * (1 - w_ab) + C2 * np.cos(np.radians(ht)) * w_ab
        lab2[..., 2] = lab[..., 2] * (1 - w_ab) + C2 * np.sin(np.radians(ht)) * w_ab
    save(lab2, os.path.join(OUT, f"{stem}_{colour}.png")); return int(core.sum())

if __name__ == "__main__":
    for a in sys.argv[1:]:
        stem, colour, *s = a.split(":"); SRC = s[0] if s else "green"
        BOX = tuple(int(v) for v in s[1].split(",")) if len(s) > 1 else None
        print(stem, colour, SRC, BOX or "", "stone px", recolour(stem, colour))
