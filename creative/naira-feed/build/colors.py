"""thumbs/*.webp -> colors.json: per image, the border (background) colour, overall mean, brightness, and a palette name."""
import json, sys, colorsys
from pathlib import Path
from PIL import Image
import numpy as np
D = Path(sys.argv[1]); T = json.load(open(D / "tagged.json")); out = {}
def name(rgb):
    r, g, b = [v / 255 for v in rgb]; h, s, v = colorsys.rgb_to_hsv(r, g, b); h *= 360
    if v < 0.22: return "black"
    if v < 0.45:
        if s < 0.22: return "charcoal"
        if h < 15 or h >= 330: return "red"
        if h < 70: return "brown"
        if h < 170: return "green"
        if h < 250: return "blue"
        return "lilac"
    if s < 0.08 and v > 0.86: return "white"
    if s < 0.16 and v > 0.62: return "grey" if (h < 20 or h > 300 or 150 < h < 260) and s < 0.06 else "cream"
    if s < 0.22 and v > 0.55: return "cream" if 20 <= h <= 70 else ("blush" if h < 20 or h > 300 else ("sage" if 70 < h < 170 else ("lilac" if 230 < h <= 300 else "grey")))
    if h < 12 or h >= 340: return "red" if s > 0.45 and v < 0.75 else "blush"
    if h < 42: return "apricot" if s > 0.3 else "cream"
    if h < 68: return "gold" if s > 0.3 else "cream"
    if h < 170: return "sage" if s < 0.45 else "green"
    if h < 250: return "blue"
    if h < 300: return "lilac"
    return "pink"
for x in T:
    p = D / "thumbs" / (x["id"] + ".webp")
    if not p.exists(): continue
    try: im = Image.open(p).convert("RGB")
    except Exception: continue
    im.thumbnail((160, 160)); a = np.asarray(im).astype(np.float32); h, w = a.shape[:2]; m = max(4, min(h, w) // 10)
    border = np.concatenate([a[:m].reshape(-1, 3), a[-m:].reshape(-1, 3), a[:, :m].reshape(-1, 3), a[:, -m:].reshape(-1, 3)])
    bg = np.median(border, 0); mean = a.reshape(-1, 3).mean(0)
    sat = (a.max(-1) - a.min(-1)) / (a.max(-1) + 1e-3)
    out[x["id"]] = {"bg": [int(v) for v in bg], "mean": [int(v) for v in mean], "lum": round(float(a.mean() / 255), 3),
                    "sat": round(float(sat.mean()), 3), "pal": name(bg), "w": im.width, "h": im.height}
json.dump(out, open(D / "colors.json", "w"))
import collections; print(len(out), collections.Counter(v["pal"] for v in out.values()).most_common())
