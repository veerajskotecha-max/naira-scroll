# Builds the owner's review page (../review/): listings.json (names, prices, copy, flags) + frames.json (each listing's
# approved photos, variant by variant) + ../cards (size cards) + the owner's screenshot crop for each piece (../refs).
# Writes ../review/img/<handle>-NN.jpg (800x1000 for the photo strip and the zoom), ../review/img/<handle>-size.jpg,
# ../review/img/<handle>-src.jpg, and the page's data block in ../review/index.html.
# Usage: python3 -I review.py
import json, os, re, unicodedata
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "../review"); IMG = os.path.join(R, "img"); os.makedirs(IMG, exist_ok=True)
L = json.load(open(os.path.join(H, "listings.json"))); F = json.load(open(os.path.join(H, "frames.json")))
NOT = json.load(open(os.path.join(H, "not_shot.json")))
CHK = json.load(open(os.path.join(H, "checks.json"))) if os.path.exists(os.path.join(H, "checks.json")) else {}
def handle(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower(); return re.sub(r"[^a-z0-9]+", "-", t).strip("-")
SHOT = {"H": "Hero", "E": "Earrings", "W1": "Worn", "W2": "Worn close", "M": "Macro"}
def label(key, vname):
    m = re.match(r"[A-Z]\d+[a-z]*_([A-Z]+\d?)", key); s = SHOT.get(m.group(1), m.group(1)) if m else key
    return f"{vname} · {s}" if vname else s
def save(src, dst, size=(800, 1000), fit="cover"):
    im = Image.open(src).convert("RGB")
    if fit == "cover":
        w, h = im.size; dx, dy = round(w * 0.015), round(h * 0.015); im = im.crop((dx, dy, w - dx, h - dy)).resize(size, Image.LANCZOS)
    else:
        im.thumbnail(size, Image.LANCZOS)
    im.save(dst, quality=84, optimize=True, progressive=True)
listings = []
for x in L:
    h = handle(x["title"]); fr = F.get(x["id"], {}); images = []; n = 0
    for vname, keys in fr.items():
        for key in keys:
            n += 1; dst = f"img/{h}-{n:02d}.jpg"; save(os.path.join(H, "out", key + ".png"), os.path.join(R, dst))
            images.append({"src": dst, "alt": f"{x['title']}{', ' + vname if vname else ''}: {label(key, '')}", "label": label(key, vname), "kind": "photo"})
    card = os.path.join(H, "../cards", f"{h}-size-guide.jpg")
    if os.path.exists(card):
        dst = f"img/{h}-size.jpg"; save(card, os.path.join(R, dst), (1000, 1000), "contain")
        images.append({"src": dst, "alt": f"Size guide for {x['title']}", "label": "Size card", "kind": "size"})
    ref = os.path.join(H, "../refs", f"{x['id']}_full.jpg")
    if os.path.exists(ref):
        dst = f"img/{h}-src.jpg"; save(ref, os.path.join(R, dst), (800, 800), "contain")
        images.append({"src": dst, "alt": f"Your screenshot of {x['title']}", "label": "Your screenshot", "kind": "source"})
    opt = x["option"]
    variants = ([{"name": v, "sku": s, "units": x["units"]} for v, s in opt[1]] if opt else [{"name": "One style", "sku": x.get("sku", h.upper()[:3]), "units": x["units"]}])
    listings.append({"id": x["id"], "title": x["title"], "handle": h, "type": x["type"], "price": x["price"], "compare": x["compare"],
                     "margin": x.get("margin", ""), "cost": x.get("cost", "not given"), "variants": variants, "intro": x["intro"], "tip": x["tip"],
                     "details": x["details"], "src": x["src"], "code": x["code"], "flags": x["flags"], "checks": CHK.get(x["id"], []), "images": images})
meta = json.load(open(os.path.join(H, "review_meta.json")))
data = {"listings": listings, "notes": meta["notes"], "how": meta["how"], "notshot": NOT}
page = open(os.path.join(R, "index.html")).read()
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = re.sub(r'(<script id="data" type="application/json">)(.*?)(</script>)', lambda m: m.group(1) + blob + m.group(3), page, count=1, flags=re.S)
open(os.path.join(R, "index.html"), "w").write(page)
print(len(listings), "listings,", sum(len(l["images"]) for l in listings), "images")
