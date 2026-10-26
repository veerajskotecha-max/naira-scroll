"""Download the camp originals (Higgsfield raw PNGs) and every Shopify photo of every in-stock piece."""
import json, sys, re, concurrent.futures as cf, urllib.request
from pathlib import Path
W = Path(sys.argv[1]); D = W / "data"
P = json.load(open(D / "products.json"))["products"]
jobs = []
for i, v in json.load(open(D / "raw_map.json")).items():
    jobs.append((v["raw"], D / "raw" / f"{i}.png"))
for p in P:
    if p["vendor"] != "Naira Petite" or "pre-order" in p["tags"] or not any(v["available"] for v in p["variants"]): continue
    for k, im in enumerate(p["images"]):
        u = im["src"]; u = u + ("&" if "?" in u else "?") + "width=1400"
        jobs.append((u, D / "shop" / p["handle"] / f"{k}.jpg"))
def get(j):
    u, out = j
    if out.exists() and out.stat().st_size > 1000: return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=90) as r: out.write_bytes(r.read()); return 1
        except Exception as e: err = e
    print("FAIL", u, err); return 0
with cf.ThreadPoolExecutor(12) as ex: n = sum(ex.map(get, jobs))
print("downloaded", n, "of", len(jobs))
