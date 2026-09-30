"""Trace the NAIRA wordmark to vector: sage letters and blush flower as two clean compound paths.
Source: the site's 4000 x 2250 footer PNG. Coordinates are emitted in the pixel space of
assets/naira-logo-brand.png (1772 x 498, 65 px padding) so the vector drops into the same slot."""
import json, time, numpy as np, potrace
from PIL import Image

S = 3                                   # supersample before thresholding: sub-pixel accurate edges
PAD = 65
src = np.asarray(Image.open('src/logo_footer_4000.png').convert('RGBA')).astype(np.float32)
al = src[..., 3]
ys, xs = np.where(al > 8)
x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
crop = src[y0:y1, x0:x1]
h, w = crop.shape[:2]
alpha = crop[..., 3] / 255.0
flower = (crop[..., 0] - crop[..., 2]) > 40
cov = {"letters": np.where(flower, 0.0, alpha), "flower": np.where(flower, alpha, 0.0)}


def fmt(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def pt(p):
    return (p.x / S + PAD, p.y / S + PAD)


out = {}
for name, c in cov.items():
    t = time.time()
    im = Image.fromarray((c * 255).astype(np.uint8)).resize((w * S, h * S), Image.BICUBIC)
    mask = np.asarray(im) > 127
    bm = potrace.Bitmap(~mask)                     # potrace traces the "dark" pixels
    path = bm.trace(turdsize=12, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=1.0,
                    opticurve=True, opttolerance=0.2)
    d = []
    for curve in path:
        sx, sy = pt(curve.start_point)
        d.append(f"M{fmt(sx)},{fmt(sy)}")
        for seg in curve.segments:
            if seg.is_corner:
                cx, cy = pt(seg.c); ex, ey = pt(seg.end_point)
                d.append(f"L{fmt(cx)},{fmt(cy)}L{fmt(ex)},{fmt(ey)}")
            else:
                ax, ay = pt(seg.c1); bx, by = pt(seg.c2); ex, ey = pt(seg.end_point)
                d.append(f"C{fmt(ax)},{fmt(ay)} {fmt(bx)},{fmt(by)} {fmt(ex)},{fmt(ey)}")
        d.append("Z")
    out[name] = "".join(d)
    print(f"{name}: {len(path)} curves, {len(out[name])/1000:.0f} kB path, {time.time()-t:.1f}s")

out["width"], out["height"] = int(w + 2 * PAD), int(h + 2 * PAD)
json.dump(out, open('assets/naira-logo-vector.json', 'w'))
print('canvas', out["width"], out["height"])
