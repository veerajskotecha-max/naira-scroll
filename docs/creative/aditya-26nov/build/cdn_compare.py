# Downloads every gallery image of the 26 Nov drafts back from the Shopify CDN and compares it with the local file it was
# made from (export or size card), matched by alt text; also fetches the size card the description links. A pass is a mean
# pixel difference under 3 of 255 at 322x400, with no other export closer.
# Usage: python3 -I cdn_compare.py PRODUCTS_QUERY_JSON EMPTY_DOWNLOAD_DIR   (a saved Admin products query: handle, title,
#        descriptionHtml, media(first: 20) { nodes { alt ... on MediaImage { image { url } } } })
import json, os, re, subprocess, sys
from PIL import Image, ImageChops, ImageStat
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "..")
L = {p["handle"]: p for p in json.load(open(f"{R}/shopify/listing.json"))}; EMAP = json.load(open(f"{H}/export_map.json"))
def get(url, dst): return subprocess.run(["curl", "-sS", "-L", "-o", dst, "-w", "%{http_code}", url], capture_output=True, text=True).stdout.strip()
def diff(a, b):
    A = Image.open(a).convert("RGB").resize((322, 400)); B = Image.open(b).convert("RGB").resize((322, 400))
    return sum(ImageStat.Stat(ImageChops.difference(A, B)).mean) / 3
q, dl = sys.argv[1], sys.argv[2]; os.makedirs(dl, exist_ok=True)
allx = [f"{R}/exports/{f}" for f in sorted(os.listdir(f"{R}/exports"))]
bad = 0
nodes = json.load(open(q)); nodes = nodes.get("data", nodes)
for n in nodes["products"]["nodes"]:
    p = L.get(n["handle"])
    if not p: continue
    want = {f"{p['title']} — {alt}": f"{R}/exports/{EMAP[slot]}" for slot, alt in p["images"] if slot in EMAP}
    want[f"Size guide — {p['title']}"] = f"{R}/cards/{p['handle']}-size-guide.jpg"
    for i, m in enumerate(n["media"]["nodes"], 1):
        exp = want.get(m["alt"]); url = (m.get("image") or {}).get("url")
        dst = f"{dl}/{n['handle']}-{i:02d}.jpg"; code = get(url, dst) if url else "no-url"
        if code != "200" or not exp or not os.path.exists(exp):
            bad += 1; print(f"BAD {n['handle']} #{i} alt={m['alt']!r} http {code}"); continue
        d = diff(dst, exp); others = [diff(dst, c) for c in allx if c != exp]
        ok = d < 3 and all(o > 3 * max(d, 1) for o in others); bad += not ok
        print(f"{'OK ' if ok else 'BAD'} {n['handle']} #{i} {os.path.basename(exp)} diff {d:.2f}" + (f" next {min(others):.1f}" if others else ""))
    m = re.search(r'<img src="([^"]+)"', n.get("descriptionHtml") or "")
    if m:
        code = get(m.group(1), f"{dl}/{n['handle']}-desc-card.jpg"); ok = code == "200"
        if ok: d = diff(f"{dl}/{n['handle']}-desc-card.jpg", f"{R}/cards/{p['handle']}-size-guide.jpg"); ok = d < 3
        bad += not ok; print(f"{'OK ' if ok else 'BAD'} {n['handle']} description size guide http {code}" + (f" diff {d:.2f}" if code == "200" else ""))
print("FAILURES:", bad)
