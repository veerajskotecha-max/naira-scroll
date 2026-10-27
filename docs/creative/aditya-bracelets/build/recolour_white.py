# Bougainvillea Vine Bracelet (ADT07) in white, 27 Oct 2026: the owner sent Aditya's photo of the same vine with every
# flower in clear stones and asked for it on Shopify. The four approved Fuchsia photos (hero, worn, worn close, macro, the
# 25 Oct size-fixed takes) become the White photos with only their coloured stones changed, so the vine, its size and the
# model stay exactly as in the other colours.
#  - Tint: every pixel at the stones' hues (magenta through purple to ruby red, CIELab hue 270 to 40 degrees) loses its
#    colour, down to faint tints on highlights and on the claws that reflected the ruby.
#  - Brightness: the stone bodies' lightness is mapped by rank onto a clear stone's (dark facet lines, mostly bright, white
#    sparks), so every facet and glint stays where it was. Small stones get a brighter target than the macro's large petals, and the hero's
#    centre flower brighter still.
# In the worn frames only a box around the bracelet is touched, which keeps the lips, nails and camisole as they were.
# Usage: python3 -I recolour_white.py  -> ../exports/bougainvillea-vine-bracelet-08..11.jpg
import os
import numpy as np, cv2
from PIL import Image

H = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.join(H, "../exports")
SMALL = [30, 48, 74, 87, 94, 99, 100]     # clear stone lightness at the stones' 1, 5, 25, 50, 75, 95, 99.5 percentiles
HERO = [38, 56, 80, 90, 95, 99, 100]      # the hero's centre flower is big enough to read grey at SMALL
LARGE = [22, 35, 64, 82, 92, 98.5, 100]
FRAMES = {1: (None, HERO), 2: ((620, 920, 880, 1230), SMALL), 3: ((370, 920, 700, 1320), SMALL), 4: (None, LARGE)}
NEUTRAL = (1.5, 3.5)                      # a*, b* of the clear stones: a touch of the warm room, like the pavé leaves


def _ramp(x, a, b):
    return np.clip((x - a) / (b - a), 0, 1)


def recolour(path, box, target):
    rgb = np.asarray(Image.open(path).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab); L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.hypot(A, B); hue = (np.degrees(np.arctan2(B, A)) + 360) % 360
    hw = np.where(hue >= 180, _ramp(hue, 268, 282), 1 - _ramp(hue, 30, 42))
    reg = np.ones_like(L)
    if box:
        reg = np.zeros_like(L); x0, y0, x1, y1 = box; reg[y0:y1, x0:x1] = 1; reg = cv2.GaussianBlur(reg, (0, 0), 6)
    w_ab = _ramp(C, 3, 10) * hw * reg; w_l = _ramp(C, 8, 18) * hw * reg
    body = w_l > 0.5
    Ln = np.interp(L, np.percentile(L[body], [1, 5, 25, 50, 75, 95, 99.5]), target)
    out = lab.copy()
    out[..., 0] = L * (1 - w_l) + Ln * w_l
    out[..., 1] = A * (1 - w_ab) + NEUTRAL[0] * w_ab; out[..., 2] = B * (1 - w_ab) + NEUTRAL[1] * w_ab
    res = np.clip(cv2.cvtColor(out, cv2.COLOR_Lab2RGB), 0, 1)
    return Image.fromarray((res * 255 + 0.5).astype(np.uint8)), int(body.sum())


if __name__ == "__main__":
    for i, (box, target) in FRAMES.items():
        img, n = recolour(f"{EXP}/bougainvillea-vine-bracelet-0{i}.jpg", box, target)
        dst = f"{EXP}/bougainvillea-vine-bracelet-{i + 7:02d}.jpg"; img.save(dst, quality=92, optimize=True, progressive=True)
        print(os.path.basename(dst), "from", i, "stone px", n)
