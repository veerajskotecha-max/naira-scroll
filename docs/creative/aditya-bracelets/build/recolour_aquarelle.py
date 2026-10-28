# Aquarelle Rivière Bracelet (ADT06) in White and Pink, 27 Oct 2026: the owner asked for the same fine line in white and in
# pink (Aditya's photo shows the pink one: the same gold four claw cups, pale rose stones). The four approved Lavender photos
# (hero, worn, worn close, macro) become each colour's photos with only their stones changed, so the line, its size and the
# model stay exactly as in the other colours. A pixel counts as stone by its CIELab hue (the lavender's facets run from violet
# at 290 degrees round to rose at 20, apart from the gold, skin, saffron camisole and plaster at 40 and up) and chroma; in the
# worn frames only a box around the bracelet is touched, which keeps the lips and nails as they were.
#  - White: as recolour_white.py, the tint goes and the stone bodies' lightness is mapped by rank onto a clear stone's, so
#    every facet and glint stays where it was. The clear stones take the warm white of Rivière Classique's (ADT04) stones in
#    the same room light, and the faint lilac on their near-white facets goes too: within a few pixels of a stone, every
#    pixel that is not gold, plaster or skin (warm hues) is neutralised, whatever its chroma.
#  - Pink: as recolour_carre.py, each stone pixel moves to the target colour keeping its shading relative to the stones' median.
# Usage: python3 -I recolour_aquarelle.py  -> ../exports/aquarelle-riviere-bracelet-08..11.jpg (White), -12..15.jpg (Pink)
import os
import numpy as np, cv2
from PIL import Image

H = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.join(H, "../exports")
SRC = {"H": 4, "W1": 5, "W2": 6, "M": 7}                  # the Lavender exports
BOX = {"H": None, "W1": (470, 800, 940, 1160), "W2": (420, 900, 740, 1170), "M": None}
FIRST = {"White": 8, "Pink": 12}
STONE_HUE, HALF = 335, 47                                   # the lavender's facets: 288 to 22 degrees in full, none past 276 or 34
SMALL = [30, 48, 74, 87, 94, 99, 100]                       # clear stone lightness at the 1, 5, 25, 50, 75, 95, 99.5 percentiles
HERO = [38, 56, 80, 90, 95, 99, 100]                        # the hero's shaded far side reads smoky at SMALL
LARGE = [32, 42, 64, 82, 92, 98.5, 100]                     # Rivière Classique's macro facets bottom out near L 38
CLEAR = {"H": HERO, "W1": SMALL, "W2": SMALL, "M": LARGE}
NEUTRAL = (3.0, 6.0)                                        # a*, b* of a clear stone: Rivière Classique's read (4, 8) on highlights
PINK = (72, 21, 354, 0.75)                                  # target stone body: L, C, hue, lightness contrast (the soft pink of Aditya's photo)


def _ramp(x, a, b):
    return np.clip((x - a) / (b - a), 0, 1)


def recolour(path, box, colour, clear):
    rgb = np.asarray(Image.open(path).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab); L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.hypot(A, B); hue = (np.degrees(np.arctan2(B, A)) + 360) % 360
    dh = ((hue - STONE_HUE + 180) % 360) - 180
    hw = 1 - _ramp(np.abs(dh), HALF, HALF + 12)
    reg = np.ones_like(L)
    if box:
        reg = np.zeros_like(L); x0, y0, x1, y1 = box; reg[y0:y1, x0:x1] = 1; reg = cv2.GaussianBlur(reg, (0, 0), 6)
    w_ab = _ramp(C, 3, 9) * hw * reg; w_l = cv2.GaussianBlur(_ramp(C, 7, 14) * hw * reg, (0, 0), 0.8)
    core = ((C > 7) & (np.abs(dh) < HALF) & (reg > 0.5)).astype(np.uint8)
    near = cv2.GaussianBlur(cv2.dilate(core, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))).astype(np.float32), (0, 0), 1.5)
    warm = _ramp(C, 4, 9) * ((hue > 34) & (hue < 120))      # gold, plaster and skin keep their colour
    w_ab = cv2.GaussianBlur(np.maximum(w_ab, near * (1 - warm) * reg), (0, 0), 0.8)
    body = w_l > 0.5
    out = lab.copy()
    if colour == "White":
        Ln = np.interp(L, np.percentile(L[body], [1, 5, 25, 50, 75, 95, 99.5]), clear)
        out[..., 0] = L * (1 - w_l) + Ln * w_l
        out[..., 1] = A * (1 - w_ab) + NEUTRAL[0] * w_ab; out[..., 2] = B * (1 - w_ab) + NEUTRAL[1] * w_ab
    else:
        Lm, Cm = np.median(L[body]), np.median(C[body]); Lt, Ct, ht, k = PINK
        L2 = np.clip(Lt + (L - Lm) * k, 4, 98)
        C2 = np.clip(Ct * (C / Cm) ** 0.8, 0, 70)
        h2 = np.radians(ht + dh * 0.3 * hw)                   # near-white facets take the pink's own hue
        out[..., 0] = L * (1 - w_l) + L2 * w_l
        out[..., 1] = A * (1 - w_ab) + C2 * np.cos(h2) * w_ab; out[..., 2] = B * (1 - w_ab) + C2 * np.sin(h2) * w_ab
    res = np.clip(cv2.cvtColor(out, cv2.COLOR_Lab2RGB), 0, 1)
    return Image.fromarray((res * 255 + 0.5).astype(np.uint8)), int(body.sum())


if __name__ == "__main__":
    for colour, first in FIRST.items():
        for n, (view, i) in enumerate(SRC.items()):
            img, px = recolour(f"{EXP}/aquarelle-riviere-bracelet-0{i}.jpg", BOX[view], colour, CLEAR[view])
            dst = f"{EXP}/aquarelle-riviere-bracelet-{first + n:02d}.jpg"; img.save(dst, quality=92, optimize=True, progressive=True)
            print(os.path.basename(dst), colour, view, "stone px", px)
