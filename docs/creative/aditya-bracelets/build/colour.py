# Stone colour corrections applied before export (and to a hero before it is used as a reference).
import numpy as np
from PIL import Image, ImageFilter
def _hsv(a):
    mx = a.max(-1); mn = a.min(-1); d = mx - mn + 1e-6
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) / 6
    s = (mx - mn) / (mx + 1e-6)
    return h, s, mx
def _rgb(h, s, v):
    i = np.floor(h * 6).astype(int) % 6; f = h * 6 - np.floor(h * 6)
    p, q, t = v * (1 - s), v * (1 - f * s), v * (1 - (1 - f) * s)
    out = np.zeros(h.shape + (3,))
    for k, (x, y, z) in enumerate([(v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q)]):
        m = i == k; out[m, 0], out[m, 1], out[m, 2] = x[m], y[m], z[m]
    return out
def deepen_blue(im, vscale=0.70, sboost=1.22):
    """Light cornflower stones -> royal cobalt: lower value and raise saturation on blue stone pixels only (not the cream ground or gold)."""
    a = np.asarray(im.convert("RGB")).astype(np.float64) / 255.0
    h, s, v = _hsv(a)
    m = ((h > 0.54) & (h < 0.70) & (s > 0.22)).astype(np.float64)
    m = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))).astype(np.float64) / 255.0
    v2 = v * (1 - m * (1 - vscale)); s2 = np.clip(s * (1 + m * (sboost - 1)), 0, 1)
    return Image.fromarray((np.clip(_rgb(h, s2, v2), 0, 1) * 255).astype(np.uint8))
