"""thumbs -> quality.json: perceptual hash (dupes), edge-smear score (bad outpaints), thumb size."""
import json, sys, collections
from pathlib import Path
from PIL import Image
import numpy as np
D = Path(sys.argv[1]); T = json.load(open(D / "tagged.json")); out = {}
sizes = collections.Counter()
for x in T:
    p = D / "thumbs" / (x["id"] + ".webp")
    if not p.exists(): continue
    try: im = Image.open(p)
    except Exception: continue
    sizes[im.size] += 1
    g = np.asarray(im.convert("L").resize((9, 8), Image.LANCZOS)).astype(np.float32)
    bits = (g[:, 1:] > g[:, :-1]).flatten()
    ph = int("".join("1" if b else "0" for b in bits), 2)
    a = np.asarray(im.convert("L").resize((96, 120), Image.BILINEAR)).astype(np.float32)
    hg = np.abs(np.diff(a, axis=1)).mean(1)              # per-row horizontal gradient
    band = max(6, int(len(hg) * 0.12)); mid = hg[band:-band].mean() + 1e-3
    smear = float(min(hg[:band].mean(), hg[-band:].mean()) / mid)   # ~0 when top/bottom bands are flat streaks
    out[x["id"]] = {"ph": ph, "smear": round(smear, 3)}
json.dump(out, open(D / "quality.json", "w"))
print("thumb sizes", sizes.most_common(6))
print("smeared (<0.12):", sum(1 for v in out.values() if v["smear"] < 0.12))
# near-duplicate groups
ids = list(out); hs = [out[i]["ph"] for i in ids]
def ham(a, b): return bin(a ^ b).count("1")
dupes = 0; seen = set()
buckets = collections.defaultdict(list)
for i, h in zip(ids, hs): buckets[h >> 48].append((i, h))
for b in buckets.values():
    for k in range(len(b)):
        for j in range(k + 1, len(b)):
            if ham(b[k][1], b[j][1]) <= 4: dupes += 1
print("near-dupe pairs (coarse):", dupes)
