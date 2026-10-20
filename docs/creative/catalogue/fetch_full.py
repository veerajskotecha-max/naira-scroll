# Downloads the full-size on-model and close-up photo picked for each product, plus product facts for the ads
# (price, variant of the pictured colour, link). Writes <src>/full/<handle>-worn.jpg and -close.jpg and products_pick.json.
import json, os, sys, urllib.request, concurrent.futures as cf
from PIL import Image
SRC, PICKS = sys.argv[1], sys.argv[2]
byh = {p["handle"]: p for p in json.load(open(f"{SRC}/products.json"))["products"]}
picks = json.load(open(PICKS)); jobs = []; rows = []
os.makedirs(f"{SRC}/full", exist_ok=True)
for k in picks:
    p = byh[k["handle"]]; imgs = p["images"]
    wi = imgs[(k["worn"] or 1) - 1]; ci = imgs[k["close"] - 1]
    jobs += [(wi["src"], f"{SRC}/full/{k['handle']}-worn.jpg"), (ci["src"], f"{SRC}/full/{k['handle']}-close.jpg")]
    vids = wi.get("variant_ids") or []
    var = next((v for v in p["variants"] if v["id"] in vids), None) or next((v for v in p["variants"] if v.get("available")), p["variants"][0])
    rows.append(dict(k, price=int(float(var["price"])), variant=var["title"], variant_id=var["id"], options=[o["name"] for o in p.get("options", [])],
                     url=f"https://www.nairaflore.com/products/{p['handle']}" + (f"?variant={var['id']}" if len(p["variants"]) > 1 else ""),
                     tags=p.get("tags", []), body=(p.get("body_html") or "")[:600]))
def get(j):
    u, f = j
    if os.path.exists(f): return
    with urllib.request.urlopen(u, timeout=120) as r: open(f, "wb").write(r.read())
with cf.ThreadPoolExecutor(12) as ex: list(ex.map(get, jobs))
for r in rows:
    for kind in ("worn", "close"):
        im = Image.open(f"{SRC}/full/{r['handle']}-{kind}.jpg"); r[kind + "_size"] = im.size
json.dump(rows, open(f"{SRC}/products_pick.json", "w"), indent=1, ensure_ascii=False)
from collections import Counter
print(len(rows), "products;", Counter(tuple(r["worn_size"]) for r in rows).most_common(6))
