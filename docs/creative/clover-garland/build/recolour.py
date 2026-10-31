# Clover Garland Bracelet in Pink and White, 30 Oct 2026: the owner's photos show the same clover strand in sky blue, pink
# and clear stones. The Sky Blue photos (hero, worn, worn close, macro) become the Pink and White photos with only the petal
# stones changed, so the strand, its size and the model are identical across the three colours.
#  - The blue petals sit at CIELab hue 200 to 250 degrees; the gold, skin, saffron camisole and plaster sit at 40 to 90, so
#    nothing else is touched. The tiny clear centre stones and white glints have little colour and stay as they are.
#  - Pink keeps each pixel's shading relative to the petals' median (as ../../aditya-bracelets/build/recolour_carre.py does)
#    and moves the colour to a soft rose pink read against the blue in the owner's photo.
#  - White loses the tint and maps the petals' lightness by rank onto a clear stone's (as recolour_white.py does there).
# Usage: python3 -I recolour.py FRAME.png ... -> out/<frame>_pink.png and out/<frame>_white.png
import os, sys
import numpy as np, cv2
from PIL import Image

PINK = (68, 24, 8, 0.85)                   # L, C, hue, lightness contrast of the rose-pink petals in the listing light
SMALL = [34, 52, 78, 89, 95, 99, 100]       # clear stone lightness at the petals' 1, 5, 25, 50, 75, 95, 99.5 percentiles
LARGE = [30, 46, 74, 87, 94, 99, 100]       # the macro's large petals
NEUTRAL = (1.0, 2.5)                        # a*, b* of a clear stone in the warm room


def _ramp(x, a, b):
    return np.clip((x - a) / (b - a), 0, 1)


def load(path):
    rgb = np.asarray(Image.open(path).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab)
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    return lab, L, np.hypot(A, B), (np.degrees(np.arctan2(B, A)) + 360) % 360


def save(lab, path):
    rgb = np.clip(cv2.cvtColor(lab.astype(np.float32), cv2.COLOR_Lab2RGB), 0, 1)
    Image.fromarray((rgb * 255 + 0.5).astype(np.uint8)).save(path)


def weights(L, C, h, grow, macro=False):
    # Cyan to violet, wide enough to take the petals' teal edges and lilac glints; the warm scene sits far below 150. In the
    # macro the out-of-focus clovers are blue blurred with gold, which drifts to 110-150, and nothing else there is that hue.
    hw = (_ramp(h, 110, 125) if macro else _ramp(h, 150, 172)) * (1 - _ramp(h, 288, 308))
    # Low thresholds so the macro's out-of-focus clovers, blue blurred into cream, change too; nothing else here is blue.
    w_ab = _ramp(C, 0.6, 2.5) * hw; w_l = _ramp(C, 3, 8) * hw
    # The petals' darkest edge, inside each gold cup, has almost no colour left, so the hue test misses it and it would
    # stay teal-grey. Pixels near a petal that are dark and not gold are taken too; the bright centre stones are not.
    near = cv2.dilate((w_l > 0.5).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * grow + 1,) * 2)) > 0
    gold = (h > 40) & (h < 125) & (C > 10)
    edge = (near & ~gold & (L < 58)).astype(np.float32)
    w_ab, w_l = np.maximum(w_ab, edge), np.maximum(w_l, edge)
    if not macro:   # only near the bracelet, so no faint tint in hair or shadow anywhere else moves
        zone = cv2.dilate((w_l > 0.5).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (81, 81)))
        zone = cv2.GaussianBlur(zone.astype(np.float32), (0, 0), 8)
        w_ab, w_l = w_ab * zone, w_l * zone
    return tuple(cv2.GaussianBlur(w.astype(np.float32), (0, 0), 0.8) for w in (w_ab, w_l))


def pink(path, grow, macro=False):
    lab, L, C, h = load(path); w_ab, w_l = weights(L, C, h, grow, macro)
    if macro:
        # The out-of-focus clovers are near-neutral grey with a little blue, which reads cool beside pink. Dark, colourless
        # pixels next to stone pixels take the pink too; the gold (warm and saturated) and the cream (light) are left alone.
        near = cv2.dilate((w_ab > 0.3).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (51, 51))) > 0
        grey = near & (C < 6) & (L < 80)
        w_ab = np.maximum(w_ab, cv2.GaussianBlur(grey.astype(np.float32), (0, 0), 2) * 0.9)
    core = w_l > 0.6
    Lm, Cm = np.median(L[core]), np.median(C[core])
    Lt, Ct, ht, k = PINK
    L2 = np.clip(Lt + (L - Lm) * k, 4, 98)
    # Out-of-focus petals carry little colour; a floor keeps them reading pink rather than cool grey beside the gold.
    C2 = np.clip(Ct * np.maximum((C / Cm) ** 0.8, 0.5 if macro else 0), 0, 60)
    out = np.stack([L * (1 - w_l) + L2 * w_l, C2 * np.cos(np.radians(ht)), C2 * np.sin(np.radians(ht))], -1)
    lab2 = lab.copy()
    lab2[..., 0] = out[..., 0]
    lab2[..., 1] = lab[..., 1] * (1 - w_ab) + out[..., 1] * w_ab
    lab2[..., 2] = lab[..., 2] * (1 - w_ab) + out[..., 2] * w_ab
    return lab2, int(core.sum())


def white(path, target, grow, macro=False):
    lab, L, C, h = load(path); w_ab, w_l = weights(L, C, h, grow, macro)
    body = w_l > 0.5
    Ln = np.interp(L, np.percentile(L[body], [1, 5, 25, 50, 75, 95, 99.5]), target)
    lab2 = lab.copy()
    lab2[..., 0] = L * (1 - w_l) + Ln * w_l
    lab2[..., 1] = lab[..., 1] * (1 - w_ab) + NEUTRAL[0] * w_ab
    lab2[..., 2] = lab[..., 2] * (1 - w_ab) + NEUTRAL[1] * w_ab
    return lab2, int(body.sum())


if __name__ == "__main__":
    H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "out")
    for path in sys.argv[1:]:
        stem = os.path.splitext(os.path.basename(path))[0]
        macro = stem.endswith("_M"); grow = 14 if macro else 4      # the macro's petals are about 150 px across
        lab, n = pink(path, grow, macro); save(lab, os.path.join(OUT, f"{stem}_pink.png"))
        lab, _ = white(path, LARGE if macro else SMALL, grow, macro); save(lab, os.path.join(OUT, f"{stem}_white.png"))
        print(stem, "petal px", n)
