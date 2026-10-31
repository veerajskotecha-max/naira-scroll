# Builds the owner's final approval page (../final/): every listing marked to ship in listings.json (after the owner's review decisions,
# with their changes made) and every held piece. Writes ../final/img/<handle>-NN.jpg (800x1000, the final listing photos in order),
# -size.jpg, -book.jpg (the buy-book photo) and -src.jpg (the owner's screenshot), a small hero for each held piece, and the page's data
# block in ../final/index.html. Frames remade after the review carry a "New" tag on the page (NEW below).
# Usage: python3 -I final.py
import json, os, re, unicodedata
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "../final"); IMG = os.path.join(R, "img"); os.makedirs(IMG, exist_ok=True)
L = json.load(open(os.path.join(H, "listings.json"))); F = json.load(open(os.path.join(H, "frames.json"))); SK = json.load(open(os.path.join(H, "skus.json")))
SHOTS = {"H": "Hero", "E": "Earrings", "W1": "Worn", "W2": "Worn close", "M": "Macro"}
ALL = {"A12", "A13", "A14", "A15", "A16", "B01", "B11"}                      # every frame remade after the review
NEW = {"A02": {"A02_W1"}, "B04": {"B04_H", "B04_W1", "B04_W2"},
       "A05": {"A05_H_sapphire", "A05_W1_sapphire", "A05_W2_sapphire", "A05_M_sapphire", "A05_W2", "A05_W2_citrine", "A05_W2_olive"},
       "B02": {"B02_H_side", "B02_W1_side", "B02_W2_side", "B02_M_side"}}
HOW = ("The reshoots used the same Higgsfield recipe and model as the first round, with each piece's buy-book photo as the reference and a "
       "rewritten construction lock that names what went wrong: claws not cups, a square huggie, a symmetric heart, a straight bar, stones end "
       "to end, a teardrop hanging point up. New packshots were checked against the buy book before their worn photos and macros were made "
       "from them. Where a photo was right except for one thing (B04's heart size, A16's chain and stone, a second earring at the edge of A15's "
       "macro), the photo itself was edited with that one change, so nothing else moved. A02's worn photo was made from our packshot alone. "
       "The navy Sapphire and B02's pink and champagne side stones are recolours of the approved photos that change only those stones.")

def handle(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower(); return re.sub(r"[^a-z0-9]+", "-", t).strip("-")
def save(src, dst, size=(800, 1000), fit="cover"):
    im = Image.open(src).convert("RGB")
    if fit == "cover":
        w, h = im.size; dx, dy = round(w * 0.015), round(h * 0.015); im = im.crop((dx, dy, w - dx, h - dy)).resize(size, Image.LANCZOS)
    else:
        im.thumbnail(size, Image.LANCZOS)
    im.save(dst, quality=84, optimize=True, progressive=True)
def label(key, vname):
    m = re.match(r"[A-Z]\d+[a-z]*_([A-Z]+\d?)", key); s = SHOTS.get(m.group(1), m.group(1)) if m else key
    return f"{vname} · {s}" if vname else s

ship, held = [], []
for x in L:
    h = handle(x["title"])
    if x["status"] == "hold":
        key = F[x["id"]][next(iter(F[x["id"]]))][0]; dst = f"img/held-{h}.jpg"
        save(os.path.join(H, "out", key + ".png"), os.path.join(R, dst), (600, 750))
        held.append({"id": x["id"], "title": x["title"], "img": dst, "note": x.get("owner_note", ""), "book": x["book"]}); continue
    images, n = [], 0
    for vname, keys in F[x["id"]].items():
        for key in keys:
            n += 1; dst = f"img/{h}-{n:02d}.jpg"; save(os.path.join(H, "out", key + ".png"), os.path.join(R, dst))
            images.append({"src": dst, "alt": f"{x['title']}{', ' + vname if vname else ''}: {label(key, '')}", "label": label(key, vname),
                           "kind": "photo", "isNew": x["id"] in ALL or key in NEW.get(x["id"], set())})
    card = os.path.join(H, "../cards", f"{h}-size-guide.jpg")
    if os.path.exists(card):
        dst = f"img/{h}-size.jpg"; save(card, os.path.join(R, dst), (1000, 1000), "contain")
        images.append({"src": dst, "alt": f"Size guide for {x['title']}", "label": "Size card", "kind": "size",
                       "isNew": x["id"] in ALL | {"B04"} and x["id"] not in ("B01",)})
    hd = SK.get(x["id"], {}).get("ref", "")
    if hd.endswith("_hd") and os.path.exists(os.path.join(H, "../refs", hd + ".jpg")):
        dst = f"img/{h}-book.jpg"; save(os.path.join(H, "../refs", hd + ".jpg"), os.path.join(R, dst), (800, 800), "contain")
        images.append({"src": dst, "alt": f"Buy book photo of {x['title']}", "label": "Buy book photo", "kind": "source"})
    ref = os.path.join(H, "../refs", f"{x['id']}_full.jpg")
    if os.path.exists(ref):
        dst = f"img/{h}-src.jpg"; save(ref, os.path.join(R, dst), (800, 800), "contain")
        images.append({"src": dst, "alt": f"Your screenshot of {x['title']}", "label": "Your screenshot", "kind": "source"})
    opt = x["option"]
    variants = [{"name": v, "sku": s, "units": x["units"]} for v, s in opt[1]] if opt else [{"name": "One style", "sku": x["sku"], "units": x["units"]}]
    ship.append({"id": x["id"], "title": x["title"], "handle": h, "type": x["type"], "price": x["price"], "compare": x["compare"],
                 "variants": variants, "intro": x["intro"], "details": x["details"], "flags": x["flags"], "changes": x.get("changes", []),
                 "owner_note": x.get("owner_note", ""), "images": images})
data = {"listings": ship, "held": held, "how": HOW}
page = open(os.path.join(R, "index.html")).read()
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = re.sub(r'(<script id="data" type="application/json">)(.*?)(</script>)', lambda m: m.group(1) + blob + m.group(3), page, count=1, flags=re.S)
open(os.path.join(R, "index.html"), "w").write(page)
print(len(ship), "to ship,", len(held), "held,", sum(len(l["images"]) for l in ship) + len(held), "images")
