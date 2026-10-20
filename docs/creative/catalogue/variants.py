# Works out which colour each picked photo shows (from the store's alt text) so each card links to that variant and
# shows its price. Alt text comes from two saved Admin API pages; the third page's colours are listed by hand below.
import json, re, sys
SRC = sys.argv[1]; DUMPS = sys.argv[2:]
alt = {}
for f in DUMPS:
    for p in json.load(open(f))["data"]["products"]["nodes"]:
        for im in p["images"]["nodes"]:
            alt[im["url"].split("/files/")[-1].split("?")[0]] = im["altText"] or ""
PAGE3 = {"baguette-eternity-band": "Emerald", "baguette-huggies": "Ruby", "tubogas-dome-ring": "Gold", "petal-flower-studs": "Gold",
         "droplet-open-cuff": "Gold", "chain-drop-dome-ring": "Gold", "watch-link-ring": "Gold", "mesh-band-ring": "Gold"}
byh = {p["handle"]: p for p in json.load(open(f"{SRC}/products.json"))["products"]}
rows = json.load(open(f"{SRC}/products_pick.json"))
def colour(r, kind, pos):
    p = byh[r["handle"]]; im = p["images"][pos - 1]
    a = alt.get(im["src"].split("/files/")[-1].split("?")[0], "")
    m = re.match(r"[^,—]+,\s*([^—]+?)\s+—", a)
    if m: return m.group(1).strip()
    return PAGE3.get(r["handle"]) if kind == "worn" else None
for r in rows:
    p = byh[r["handle"]]; vs = [v for v in p["variants"] if v.get("available")] or p["variants"]
    for kind in ("worn", "alt"):
        pos = r.get(kind) if kind == "alt" else (r["worn"] or 1)
        if not pos: continue
        c = colour(r, kind, pos); v = None
        if c: v = next((v for v in vs if v["title"] == c or v["title"].startswith(c + " /") or v["title"].startswith(c + " ·")), None)
        v = v or vs[0]
        r[kind + "_colour"] = c; r[kind + "_variant"] = v["title"]; r[kind + "_price"] = int(float(v["price"]))
        r[kind + "_url"] = f"https://www.nairaflore.com/products/{p['handle']}" + (f"?variant={v['id']}" if len(p["variants"]) > 1 else "")
    r["price"] = r["worn_price"]; r["url"] = r["worn_url"]
json.dump(rows, open(f"{SRC}/products_pick.json", "w"), indent=1, ensure_ascii=False)
for r in rows:
    if r.get("worn_colour") or r.get("alt_colour"): print(r["n"], r["handle"], "|", r.get("worn_colour"), r["worn_variant"], r["worn_price"], "| alt:", r.get("alt_colour"), r.get("alt_variant"))
