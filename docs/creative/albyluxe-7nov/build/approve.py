# Builds the owner's approval page (../approve/index.html, from ../approve/template.html and base.css) and its web-sized photos
# (../approve/img/): every listing in listings.json with its frames (frames.json: id -> {variant name: [frame keys]}, out/<key>.png),
# its size card (../cards/<handle>-size-guide.jpg), the owner's or supplier's photo it was made from, and the checks made on its photos
# (checks.json). Frames not made yet are left out, so the page can be previewed early.
# Usage: python3 -I approve.py
import json, os, re, unicodedata
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(H, "../approve"); IMG = os.path.join(A, "img"); os.makedirs(IMG, exist_ok=True)
L = json.load(open(os.path.join(H, "listings.json")))
F = json.load(open(os.path.join(H, "frames.json"))) if os.path.exists(os.path.join(H, "frames.json")) else {}
CK = json.load(open(os.path.join(H, "checks.json"))) if os.path.exists(os.path.join(H, "checks.json")) else {}
SHOTS = {"H": "Packshot", "W1": "Worn", "W2": "Worn close", "M": "Macro", "P": "In the palm", "He": "Packshot"}
ASSUME = [
    "The baguette ring you asked for in green, white and red is the Interlocked Baguette Trio Ring. The supplier only shows it in green, "
    "so the White and Red photos are the green photos with only the stones recoloured.",
    "From your second set of photos: both blue rings are in (the Aqua Emerald-Cut Band and the Aqua Oval Cocktail Ring), and so are the "
    "two pieces still pending, the Emerald-Cut Bezel Studs and the Charm Chain Duo Ring.",
    "Left out, as you said: the three two-stone rings (a pear and an emerald-cut side by side, in pink and in clear). They are the same "
    "design as the Duet Emerald-Cut Ring that is already on Shopify as a draft (DER-GR, DER-PK, DER-CL).",
    "Prices follow the last Albyluxe batch: studs ₹999, rings ₹999 to ₹1,499, necklaces ₹1,199 to ₹1,299, all with a compare-at price, "
    "and 5 units per variant. Change any number on a card and it saves.",
    "Sizes come from the supplier's photos, measured against an ear, a fingertip or a hand, and from Albyluxe's sheet where it gives one "
    "(the heart necklace and the trio ring). Anything still to confirm with Albyluxe is listed in amber on the card.",
    "Approved pieces go live on all six sales channels in one batch, with their photos, size card, SKUs, stock and copy. If you would "
    "rather see one on Shopify as a draft first, say so in its note.",
]
HOW = ("Every photo was made on Higgsfield with Nano Banana Pro at 2K, with your photo or the supplier's as the only authority on the design. "
       "The packshot came first and was checked against that photo stone by stone; the worn photos and the macro were then made from the "
       "approved packshot and checked for size against the body (an earlobe is about 18mm, a finger about 17mm wide). Where a photo was "
       "right except for one thing, that photo was edited with the one change, so nothing else moved. The palm photo is a cut-out of the "
       "approved packshot laid on a photo of an open palm at its true size (about 6 pixels to the millimetre). Colours the supplier does not show are "
       "recolours of the approved photos that change only the stones.")

def handle(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower(); return re.sub(r"[^a-z0-9]+", "-", t).strip("-")
def save(src, dst, size=(800, 1000), fit="cover"):
    im = Image.open(src).convert("RGB")
    if fit == "cover":
        w, h = im.size; dx, dy = round(w * 0.015), round(h * 0.015); im = im.crop((dx, dy, w - dx, h - dy)).resize(size, Image.LANCZOS)
    else:
        im.thumbnail(size, Image.LANCZOS)
    im.save(dst, quality=82, optimize=True, progressive=True)
def label(key, vname):
    m = re.match(r"L\d+_([A-Z]+\d?)", key); s = SHOTS.get(m.group(1), m.group(1)) if m else key
    return f"{vname} · {s}" if vname else s

out = []
for x in L:
    h = handle(x["title"]); images, n = [], 0
    for vname, keys in F.get(x["id"], {"": [x["id"] + "_H"]}).items():
        for key in keys:
            p = os.path.join(H, "out", key + ".png")
            if not os.path.exists(p): continue
            n += 1; dst = f"img/{h}-{n:02d}.jpg"; save(p, os.path.join(A, dst))
            images.append({"src": dst, "alt": f"{x['title']}{', ' + vname if vname else ''}: {label(key, '')}", "label": label(key, vname), "kind": "photo"})
    card = os.path.join(H, "../cards", f"{h}-size-guide.jpg")
    if os.path.exists(card):
        dst = f"img/{h}-size.jpg"; save(card, os.path.join(A, dst), (1000, 1000), "contain")
        images.append({"src": dst, "alt": f"Size card for {x['title']}", "label": "Size card", "kind": "size"})
    ref = next((os.path.join(H, "../refs", f"{x['id']}_{s}.jpg") for s in ("full", "det") if os.path.exists(os.path.join(H, "../refs", f"{x['id']}_{s}.jpg"))), None)
    if ref:
        dst = f"img/{h}-src.jpg"; save(ref, os.path.join(A, dst), (800, 800), "contain")
        images.append({"src": dst, "alt": f"The photo {x['title']} was made from", "label": "Your photo", "kind": "source"})
    opt = x.get("option")
    variants = [{"name": v, "sku": s} for v, s in opt[1]] if opt else [{"name": "SKU", "sku": x["sku"]}]
    out.append({"id": x["id"], "title": x["title"], "handle": h, "type": x["type"], "price": x["price"], "compare": x["compare"],
                "units": x["units"], "variants": variants, "sizes": x.get("sizes"), "intro": x["intro"], "details": x["details"],
                "tip": x.get("tip", ""), "flags": x["flags"], "checks": CK.get(x["id"], []), "images": images})
data = {"listings": out, "assume": ASSUME, "how": HOW}
page = open(os.path.join(A, "template.html")).read().replace("/*BASE*/", open(os.path.join(A, "base.css")).read(), 1)
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = re.sub(r'(<script id="data" type="application/json">)(.*?)(</script>)', lambda m: m.group(1) + blob + m.group(3), page, count=1, flags=re.S)
open(os.path.join(A, "index.html"), "w").write(page)
print(len(out), "pieces,", sum(len(l["images"]) for l in out), "images,", os.path.getsize(os.path.join(A, "index.html")), "bytes")
