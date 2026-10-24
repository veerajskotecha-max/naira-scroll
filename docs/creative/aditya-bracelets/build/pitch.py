# Samples a photo along a traced centreline and finds the stone pitch by autocorrelation.
# Usage: pitch.py IMAGE "x,y x,y ..." MODE  (MODE: blue|green|bright|sat)  [xoff,yoff]
import sys, numpy as np
from PIL import Image
img, pts, mode = sys.argv[1], sys.argv[2], sys.argv[3]
off = tuple(map(int, sys.argv[4].split(','))) if len(sys.argv) > 4 else (0, 0)
a = np.asarray(Image.open(img).convert('RGB')).astype(float)
P = np.array([tuple(map(float, p.split(','))) for p in pts.split()]) + np.array(off)
seg = np.sqrt(((P[1:] - P[:-1]) ** 2).sum(1)); L = seg.sum()
n = int(L)
cum = np.concatenate([[0], np.cumsum(seg)])
t = np.linspace(0, L, n)
xs = np.interp(t, cum, P[:, 0]); ys = np.interp(t, cum, P[:, 1])
def samp(x, y):
    x0, y0 = int(round(x)), int(round(y))
    win = a[max(0, y0 - 2):y0 + 3, max(0, x0 - 2):x0 + 3].reshape(-1, 3)
    return win.mean(0)
S = np.array([samp(x, y) for x, y in zip(xs, ys)])
r, g, b = S[:, 0], S[:, 1], S[:, 2]
if mode == 'blue': s = b - r
elif mode == 'green': s = g - (r + b) / 2
elif mode == 'bright': s = (r + g + b) / 3
else: s = S.max(1) - S.min(1)
s = s - np.convolve(s, np.ones(61) / 61, mode='same')
s = (s - s.mean()) / (s.std() + 1e-9)
ac = np.correlate(s, s, mode='full')[len(s) - 1:]; ac /= ac[0]
lo, hi = 12, 120
k = lo + int(np.argmax(ac[lo:hi]))
# refine with parabola
if 1 <= k < len(ac) - 1:
    y0, y1, y2 = ac[k - 1], ac[k], ac[k + 1]; k = k + 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2 + 1e-12)
peaks = sorted(range(lo, hi), key=lambda i: -ac[i])[:5]
print(f"path {L:.0f}px  pitch {k:.1f}px  stones~{L / k:.1f}  ac={ac[int(round(k))]:.2f}  top lags {peaks}")
