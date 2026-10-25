# Downloads every listing image and size guide of the Aditya jewellery drafts from the Shopify CDN and compares each with
# the local export it was made from (matched by alt text to its listing.json position).
# Usage: cdn_compare.py PRODUCTS_QUERY_JSON EMPTY_DOWNLOAD_DIR  -> one OK/BAD line per image, then the failure count.
# PRODUCTS_QUERY_JSON is a saved Admin API products query (handle, title, media alt + image url).
import json, sys, subprocess, os
from PIL import Image, ImageChops, ImageStat
H = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(H, "..")
q, dl = sys.argv[1], sys.argv[2]
L = {p["handle"]: p for p in json.load(open(f"{root}/shopify/listing.json"))}; sg = json.load(open(f"{root}/shopify/sizeguide_urls.json"))
def get(url, dst): return subprocess.run(["curl", "-sS", "-o", dst, "-w", "%{http_code}", url], capture_output=True, text=True).stdout.strip()
def diff(a, b):
    A = Image.open(a).convert("RGB").resize((322, 400)); B = Image.open(b).convert("RGB").resize((322, 400))
    return sum(ImageStat.Stat(ImageChops.difference(A, B)).mean) / 3
allx = sorted(f"{root}/exports/{f}" for f in os.listdir(f"{root}/exports"))
bad = 0
for n in json.load(open(q))["data"]["products"]["nodes"]:
    p = L.get(n["handle"])
    if not p: continue
    want = {f"{p['title']} — {alt}": i for i, (_, alt) in enumerate(p["images"], 1)}
    for m in n["media"]["nodes"]:
        pos = want.get(m["alt"]); exp = f"{root}/exports/{n['handle']}-{pos:02d}.jpg" if pos else None
        dst = f"{dl}/{n['handle']}-{pos or 0:02d}.jpg"; code = get(m["image"]["url"], dst)
        d = diff(dst, exp) if code == "200" and exp else None
        o = min((diff(dst, c), os.path.basename(c)) for c in allx if c != exp) if d is not None else None
        ok = d is not None and d < 3 and o[0] > 3 * max(d, 1); bad += not ok
        print(f"{'OK ' if ok else 'BAD'} {n['handle']:30s} #{pos} http {code}  diff {d:.2f}  next-nearest {o[1]} {o[0]:.1f}" if d is not None else f"BAD {n['handle']} alt {m['alt']!r} http {code}")
for h, url in sg.items():
    dst = f"{dl}/{h}-size-guide.jpg"; code = get(url, dst)
    d = diff(dst, f"{root}/shopify/sizeguides/{h}-size-guide.jpg") if code == "200" else None
    ok = d is not None and d < 3; bad += not ok
    print(f"{'OK ' if ok else 'BAD'} size guide {h:30s} http {code}  diff {d:.2f}" if d is not None else f"BAD size guide {h} http {code}")
print("FAILURES:", bad)
