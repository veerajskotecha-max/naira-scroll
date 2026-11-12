# Charm Chain Duo Ring (L16): the worn frame W1 has the two rings right (a finger between them, as the supplier's photo) but SIX charms;
# the edit that was asked to remove one (L16_W1e in edits.py) changed nothing. So the extra charm, the lower of the two pears hanging one under
# the other, is removed here, leaving the supplier's five in order: emerald-cut, pear, emerald-cut, pear, emerald-cut.
# 12 Nov (../corrections.md): the 7 Nov fill (skin copied from a fixed 70 px to the left) left a gold smear where the jump ring hung, a blurred
# chain link and a darker, smoother pear-shaped patch with repeated freckles. Now: the chain is kept out of the mask (CHAIN, gold pixels on its
# path stay untouched); the mask takes the pear, its jump ring and its contact shadow; the skin source is the nearby patch whose surroundings
# match best (searched, never overlapping jewellery), copied with its colour matched to the skin round it, then checked against the skin around it (lightness, grain).
# Usage: python3 -I l16fix.py -> out/L16_W1f.png
import os
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
PEAR = [(850, 1336), (866, 1336), (874, 1352), (880, 1372), (882, 1400), (880, 1428), (870, 1444), (848, 1450), (824, 1446), (812, 1426),
        (810, 1400), (815, 1378), (828, 1362), (842, 1350)]
CHAIN = [(862, 1296), (886, 1296), (887, 1326), (893, 1345), (946, 1462), (908, 1470), (877, 1372), (875, 1350), (870, 1342), (864, 1334), (862, 1318)]   # the chain, its links whole
img = np.asarray(Image.open(os.path.join(H, "out", "L16_W1.png")).convert("RGB"))
lab = cv2.cvtColor(img.astype(np.float32) / 255, cv2.COLOR_RGB2Lab); C = np.hypot(lab[..., 1], lab[..., 2])
hue = (np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) + 360) % 360
jewel = (lab[..., 0] > 58) | ((hue > 62) & (C > 25) & (lab[..., 0] > 35))   # gold and stones: brighter or yellower than the skin (L 38-47, hue 52-57)
chain = np.zeros(img.shape[:2], np.uint8); cv2.fillPoly(chain, [np.array(CHAIN, np.int32)], 1)
chain = (chain.astype(bool) & cv2.dilate(jewel.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)).astype(np.uint8)
m = np.zeros(img.shape[:2], np.uint8); cv2.fillPoly(m, [np.array(PEAR, np.int32)], 1)
m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13)))   # the gold rim, its glow and the contact shadow go too
m[chain > 0] = 0
ring = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))) - m; ring[chain > 0] = 0
ys, xs = np.nonzero(m); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
best = None
for dy in range(-140, 141, 4):
    for dx in range(-160, 161, 4):
        if abs(dx) < 70 and abs(dy) < 90: continue                           # never the skin right beside it (repeats show)
        sy, sx = y0 + dy, x0 + dx
        if sy < 0 or sx < 0 or sy + (y1 - y0) > img.shape[0] or sx + (x1 - x0) > img.shape[1]: continue
        win = np.zeros_like(m); win[sy:sy + (y1 - y0), sx:sx + (x1 - x0)] = (m[y0:y1, x0:x1] | ring[y0:y1, x0:x1])
        if (jewel & win.astype(bool)).any(): continue
        sh = np.roll(np.roll(lab, -dy, 0), -dx, 1)                            # sh[y, x] = lab[y + dy, x + dx]
        d = ((sh - lab) ** 2).sum(2)[ring > 0].mean()
        if best is None or d < best[0]: best = (d, dx, dy)
_, DX, DY = best
src = np.roll(np.roll(img, -DY, 0), -DX, 1).astype(np.float32); I = img.astype(np.float32)
# the source's colour is matched to the skin round the hole only (never to the gold, which a Poisson clone would pull in as a haze):
# the difference on skin pixels of the ring, spread smoothly over the hole (normalised convolution), is added to the source.
skin = ((ring > 0) & ~jewel).astype(np.float32)
num = cv2.GaussianBlur((I - src) * skin[..., None], (0, 0), 14); den = cv2.GaussianBlur(skin, (0, 0), 14)[..., None]
fill = np.clip(src + num / np.maximum(den, 1e-3), 0, 255)
a = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 2.0); a = np.clip(a * 1.6, 0, 1); a[chain > 0] = 0
out = (I * (1 - a[..., None]) + fill * a[..., None]).round().astype(np.uint8)
Image.fromarray(np.ascontiguousarray(out)).save(os.path.join(H, "out", "L16_W1f.png"))
o = cv2.cvtColor(out.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
hp = lambda a: np.abs(a[..., 0] - cv2.GaussianBlur(a[..., 0], (0, 0), 2))
print("source offset", (DX, DY), "fill px", int(m.sum()), "L* fill %.1f ring %.1f" % (o[..., 0][m > 0].mean(), o[..., 0][ring > 0].mean()),
      "grain fill %.2f ring %.2f" % (hp(o)[m > 0].mean(), hp(o)[ring > 0].mean()))
