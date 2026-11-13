# Finger width by a luminance profile across the finger.
# usage: fw.py FRAME X Y AXIS_DEG [HALF=260] -> prints width in px; writes FRAME_fw_X_Y.jpg with the line
import sys, os, math
import numpy as np
from PIL import Image, ImageDraw
f, x, y, a = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
half = int(sys.argv[5]) if len(sys.argv) > 5 else 260
im = Image.open(f).convert("RGB"); A = np.asarray(im).astype(float)
# perpendicular to the axis
t = math.radians(a + 90); dx, dy = math.cos(t), math.sin(t)
ts = np.arange(-half, half + 1)
xs = np.clip(np.round(x + ts * dx).astype(int), 0, im.width - 1); ys = np.clip(np.round(y + ts * dy).astype(int), 0, im.height - 1)
rgb = A[ys, xs]; L = rgb.mean(axis=1)
r, g, b = rgb[:, 0], rgb[:, 1], rgb[:, 2]
skin = (r > g + 14) & (r > b + 28) & (L < 185)            # warm and not bright white
# smooth the mask with a run filter, then take the run containing the centre
k = 7; sm = np.convolve(skin.astype(float), np.ones(k) / k, mode="same") > 0.5
c = half
if not sm[c]:
    near = np.where(sm)[0]; c = near[np.argmin(abs(near - half))] if len(near) else half
lo = c
while lo > 0 and sm[lo - 1]: lo -= 1
hi = c
while hi < len(sm) - 1 and sm[hi + 1]: hi += 1
w = hi - lo + 1
d = ImageDraw.Draw(im)
d.line([(x + ts[0] * dx, y + ts[0] * dy), (x + ts[-1] * dx, y + ts[-1] * dy)], fill=(0, 120, 255), width=2)
d.line([(x + ts[lo] * dx, y + ts[lo] * dy), (x + ts[hi] * dx, y + ts[hi] * dy)], fill=(255, 0, 0), width=4)
out = os.path.splitext(f)[0] + f"_fw_{int(x)}_{int(y)}.jpg"
im.crop((max(0, int(x) - 400), max(0, int(y) - 400), min(im.width, int(x) + 400), min(im.height, int(y) + 400))).save(out, quality=80)
print(f"{os.path.basename(f)} centre ({x:.0f},{y:.0f}) axis {a:.0f} deg: finger width {w} px  [{lo - half:+d} .. {hi - half:+d}]  -> {out}")
