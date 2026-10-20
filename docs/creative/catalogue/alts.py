# Second on-model photos (another angle, a closer crop, or another colour) for the products that have them,
# by product number and image position. Adds "alt" to picks.json and downloads them as <handle>-alt.jpg.
import json, os, sys, urllib.request, concurrent.futures as cf
from PIL import Image
SRC, PICKS = sys.argv[1], sys.argv[2]
ALT = {1:2, 3:7, 6:3, 7:3, 8:3, 9:5, 10:5, 12:3, 14:3, 15:4, 19:5, 20:3, 22:3, 24:3, 36:2, 37:4, 40:5, 42:3, 44:3,
       45:4, 48:3, 51:4, 52:2, 53:5, 56:4, 61:3, 72:3, 77:1, 78:3, 84:3, 85:4}
ALT_CLOSE = {1: 3, 10: 6, 19: 6}   # close-ups in the second photo's colour (crystal, silver, silver)
byh = {p["handle"]: p for p in json.load(open(f"{SRC}/products.json"))["products"]}
rows = json.load(open(f"{SRC}/products_pick.json")); jobs = []
for r in rows:
    a = ALT.get(r["n"]); r["alt"] = a
    if a:
        im = byh[r["handle"]]["images"][a - 1]; jobs.append((im["src"], f"{SRC}/full/{r['handle']}-alt.jpg"))
        if r["n"] in ALT_CLOSE:
            jobs.append((byh[r["handle"]]["images"][ALT_CLOSE[r["n"]] - 1]["src"], f"{SRC}/full/{r['handle']}-altclose.jpg")); r["alt_close"] = ALT_CLOSE[r["n"]]
        vids = im.get("variant_ids") or []
        v = next((v for v in byh[r["handle"]]["variants"] if v["id"] in vids), None)
        r["alt_variant"] = v["title"] if v else None; r["alt_variant_id"] = v["id"] if v else None
def get(j):
    u, f = j
    if not os.path.exists(f):
        with urllib.request.urlopen(u, timeout=120) as resp: open(f, "wb").write(resp.read())
with cf.ThreadPoolExecutor(12) as ex: list(ex.map(get, jobs))
for r in rows:
    if r["alt"]: r["alt_size"] = Image.open(f"{SRC}/full/{r['handle']}-alt.jpg").size
json.dump(rows, open(f"{SRC}/products_pick.json", "w"), indent=1, ensure_ascii=False)
print(len(jobs), "alt photos;", [(r["n"], r["alt_variant"]) for r in rows if r.get("alt_variant")])
