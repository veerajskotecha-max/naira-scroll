# Exports approved shots to Shopify listing files: 1288x1600 JPEG (the live listing size), optional tighter crop for
# small rings, and a red-stone hue correction for the ruby huggies/necklace so the set matches the bracelet.
import json, os, sys
import numpy as np
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
CROP = {"N07_H": 0.62, "N08_H": 0.62, "N18_H": 0.66, "N19_H": 0.66}   # centre-crop fraction for small rings
CENTRE = {"N07_H": (0.5, 0.40), "N08_H": (0.5, 0.40), "N18_H": (0.5, 0.42), "N19_H": (0.5, 0.42)}
DEEPEN = {"N23_H", "N23_W1", "N23_W2", "N23_M", "N22_W1", "N22_W2", "N22_M", "N22_H", "N19_H", "N19_W1", "N19_M"}
def deepen_red(im):
    a = np.asarray(im).astype(np.float32) / 255.0
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx = a.max(-1); mn = a.min(-1); sat = (mx - mn) / (mx + 1e-6)
    pink = (r > 0.35) & (sat > 0.45) & (b > g) & (r > b)          # magenta/raspberry stone pixels only
    k = np.clip((b - g) * 2.2, 0, 1) * pink
    a[..., 2] = b - k * (b - g) * 0.85                               # pull blue down toward green: raspberry -> ruby
    a[..., 0] = r * (1 - 0.06 * k)
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
WARM = {"N09_G"}                                                     # pale champagne gold -> the set's warm yellow gold
def warm_gold(im):
    a = np.asarray(im).astype(np.float32) / 255.0
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx = a.max(-1); mn = a.min(-1); sat = (mx - mn) / (mx + 1e-6)
    k = np.clip((sat - 0.24) / 0.1, 0, 1) * ((r >= g) & (g >= b))     # saturated warm metal only, not the cream ground
    a[..., 2] = b * (1 - 0.14 * k)
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
def export(key, src, dst):
    im = Image.open(src).convert("RGB")
    if key in DEEPEN: im = deepen_red(im)
    if key in WARM: im = warm_gold(im)
    w, h = im.size
    f = CROP.get(key, 1.0)
    if f < 1.0:
        cx, cy = CENTRE[key]; cw, ch = w * f, h * f
        x0 = min(max(cx * w - cw / 2, 0), w - cw); y0 = min(max(cy * h - ch / 2, 0), h - ch)
        im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch)))
    im = im.resize((1288, 1600), Image.LANCZOS)
    im.save(dst, quality=92, optimize=True, progressive=True)
if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for k in sys.argv[2:]:
        export(k, f"{H}/out/{k}.png", f"{out}/{k}.jpg"); print(k)
