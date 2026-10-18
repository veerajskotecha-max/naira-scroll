# Builds the "Edition Two Plain Images" artifact: the 26 clean Edition Two ad photographs (no copy on them) at full size, every
# Shopify listing photo for the 34 new pieces at 1288×1600, the wordmarks, and PDFs for Claude Design: a brand-kit page and the
# ad brief, then one photograph per page with a caption band (piece, price, and what to watch for). JPEGs go into the PDFs as they
# are, never re-encoded, and each PDF stays under 14.5 MB (the artifact's limit for one file is 15 MB).
# Sources: e2_ads.json, e2/plates/, e2/plain_notes.json (concept and photo note per plate), ../edition-two-listings/kit/listing.json,
# ../edition-two-listings/exports/ and ../edition-two-listings/shopify/verify_live.json (which pieces are on sale).
# Usage: e2_plain.py     writes <scratchpad>/e2plain/site/ and <scratchpad>/e2plain/publish.json (the files map for each publish)
import base64, json, os, re, shutil
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
import plain_pdfs as P

HERE = os.path.dirname(os.path.abspath(__file__)); CRE = os.path.normpath(f"{HERE}/.."); LST = f"{CRE}/edition-two-listings"
SPB = P.SPB; OUT = f"{SPB}/e2plain"; SITE = f"{OUT}/site"
CAPH = 330; SAGE_INK = HexColor("#5F7B74"); BIN_MB, BIN_FILES = 60e6, 250
TYPES = [("Bracelet", "Bracelets"), ("Ring", "Rings"), ("Earrings", "Earrings"), ("Necklace", "Necklaces")]
TITLE = {"Prism Rivière": "Prism Rivière Bracelet"}

BRIEF = [
    "Use the photographs as they are: never redraw, restyle or resize the jewellery. Every photo names its piece and price, and "
    "flags any fault to work around.",
    "The pieces: 34 new demi-fine pieces, 31 on sale now. Garnet Cable Cuff, Tile Stone Bangle and Birthstone Heart Necklace are "
    "drafts, so make no ads for them yet.",
    "Truth in copy: the metal is plated, so write “18k gold tone” or “silver tone”, never “gold” alone, “solid”, “real” or “pure”. "
    "The stones are cubic zirconia, never “diamond”; Ruby, Emerald and Amethyst are colour names, so write “ruby-red cubic "
    "zirconia”. No “waterproof” claims. Prices in rupees as listed, e.g. ₹1,699. Sizes marked “unconfirmed” "
    "are estimates, so keep them out of the copy.",
    "The hook: an Indian culture rhyme at the piece’s own scale, then a lowercase “X, not Y” correction that states the true "
    "material. The account’s best ad: “Almost edible.” / “cubic zirconia, not candy.”",
    "The layout: headline in Velista capitals, about 100 px on a 1080 px ad and two lines at most; the correction in Cormorant "
    "Garamond italic, lowercase, about 40 px; a spec line in Jost Medium capitals at 0.24 em tracking, listing facts only; on Feed "
    "an ink button with paper type (Stories use Meta’s own sticker); the wordmark signing off above the price, bottom right. "
    "Black wordmark on light photos, white on dark.",
    "Sizes: Feed 4:5 at 1080×1350, keeping 72 px clear at top and bottom. Stories 9:16 at 1080×1920, with no copy in the top "
    "290 px or the bottom 380 px.",
    "Timing: Diwali is 8 November 2026, so stop the diya and kandil ads after it. Rain is off-season for this launch.",
    "Palette: Sage #99B4AE, Blush #FFF8F5, Peach #F2C4B6, Coral #F0A08F, Ink #1A1614, Paper #FBF8F3.",
]

def velista(s):                         # Velista has no middle dot or dashes
    return s.replace("·", "-").replace("–", "-").replace("—", "-")

def size_line(s):                       # the listing kit's size notes, without supplier quantities; estimates marked plainly
    s = re.sub(r" \(3 pcs each[^)]*\)", "", s).replace(" per supplier diagram", "")
    s = re.sub(r" \(confirm(?: length)? on sample\)", " (unconfirmed)", s)
    return re.sub(r"\b([Ll]ength|size) to confirm\b", r"\1 unconfirmed", s)

def rupees(ps):
    lo, hi = min(ps), max(ps)
    return f"₹{lo:,}" if lo == hi else f"₹{lo:,}–{hi:,}"

def thumb(src, dst, w=640):
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src): return
    im = Image.open(src).convert("RGB")
    im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(dst, "JPEG", quality=80, optimize=True, progressive=True)

def plates():
    ads = json.load(open(f"{HERE}/e2_ads.json"))["ads"]; notes = json.load(open(f"{HERE}/e2/plain_notes.json"))
    order = {}                                          # products in the ads' own order, Stories beside their Feed
    for a in ads: order.setdefault(a["spec"].split(" · ")[0], len(order))
    out = []
    for a in ads:
        n = notes[a["plate"]]; src = f"{HERE}/e2/plates/{a['plate']}.jpg"; w, h = Image.open(src).size
        prod = a["spec"].split(" · ")[0]; prod = TITLE.get(prod, prod)
        out.append(dict(g="ad", ok=n["ok"], id=a["plate"], src=src, title=prod, name=f"{n['concept']} · {n['gloss']}", price=a["price"],
                        fmt=a["fmt"], w=w, h=h, tall=a["fmt"] == "9:16", note=n["note"], facts=n["facts"], scene=n["scene"],
                        meta=f"{'Story 9:16' if a['fmt'] == '9:16' else 'Feed 4:5'} · {w}×{h} px",
                        t=f"t/{a['plate']}.jpg", f=f"f/{a['plate']}.jpg", file=f"Naira-E2-{a['plate']}.jpg",
                        rank=(order[a["spec"].split(" · ")[0]], a["fmt"] == "9:16")))
    return sorted(out, key=lambda x: x["rank"])

def products():
    live = json.load(open(f"{LST}/shopify/verify_live.json")); drafts = set(live["draft_no_supplier_quantity"])
    out = []
    for p in json.load(open(f"{LST}/kit/listing.json")):
        if not p.get("handle"): continue
        prices = [v["price"] for v in p["variants"]] or [p["price_inr"]]
        photos = []
        for k, im in enumerate(sorted(p["images"], key=lambda i: i["position"]), 1):
            src = f"{LST}/exports/{im['file']}"; w, h = Image.open(src).size
            desc = im["alt"].split(" — ", 1)[-1]
            photos.append(dict(g="list", id=im["file"], src=src, title=p["title"], name=im.get("variant") or "", line=desc[:1].upper() + desc[1:],
                               meta=f"Photo {k} of {len(p['images'])} · {w}×{h} px", w=w, h=h, tall=False,
                               t=f"l/{im['file']}", f=f"lf/{im['file']}", file=f"Naira-E2-{im['file']}"))
        opts = []                                       # the stone colours are already in the stones line
        for o in (o for o in p["options"] if o != "Stone"):
            vals = list(dict.fromkeys(v["options"][o] for v in p["variants"]))
            opts.append(f"{o}: {', '.join(vals)}" if len(vals) <= 4 else f"{o}: {len(vals)} choices")
        out.append(dict(handle=p["handle"], title=p["title"], type=p["product_type"], price=rupees(prices), sale=p["handle"] not in drafts,
                        code=p["supplier_code"], tagline=p["tagline"], size=size_line(p["size_and_fit"]), stones=p["stones"],
                        options=" · ".join(opts), photos=photos))
    rank = {t: i for i, (t, _) in enumerate(TYPES)}
    return sorted(out, key=lambda p: (rank[p["type"]], not p["sale"], p["title"]))

# ---- PDFs ----
def photo_page(c, it, cap):
    ih = round(P.PW * it["h"] / it["w"]); c.setPageSize((P.PW, ih + CAPH))
    c.setFillColor(P.PAPER); c.rect(0, 0, P.PW, ih + CAPH, stroke=0, fill=1)
    c.drawImage(it["src"], 0, CAPH, P.PW, ih)          # a JPEG path is embedded as it is, at full resolution
    P.tracked(c, cap["status"], "JostMed", 15, 48, CAPH - 44, 0.22, P.CORAL if cap["warn"] else SAGE_INK)
    title = velista(cap["title"].upper()); c.setFillColor(P.INK); c.setFont("Velista", 40); c.drawString(48, CAPH - 98, title)
    if cap["name"]:
        c.setFont("CormIt", 32); c.drawString(48 + pdfmetrics.stringWidth(title, "Velista", 40) + 18, CAPH - 98, cap["name"])
    P.tracked(c, cap["meta"], "Jost", 15, 48, CAPH - 132, 0.16, P.MUTE)
    y = CAPH - 168; c.setFont("CormIt", 22); c.setFillColor(P.INK)
    for ln in P.wrap(cap["line"], "CormIt", 22, P.PW - 96)[:3]: c.drawString(48, y, ln); y -= 26
    y -= 8; c.setFont("Corm", 19); c.setFillColor(P.MUTE)
    for ln in P.wrap(cap["sub"], "Corm", 19, P.PW - 96)[:3]: c.drawString(48, y, ln); y -= 23
    c.showPage()

def ad_cap(it):
    return dict(status="READY FOR ADS" if it["ok"] else "USE WITH CARE · READ THE NOTE", warn=not it["ok"], title=it["title"],
                name=it["name"].replace(" · ", ", "), meta=f"{it['price']}  ·  {it['meta']}  ·  {it['id']}", line=it["note"], sub=it["facts"])

def list_cap(p, it):
    return dict(status=("ON SALE" if p["sale"] else "DRAFT · NOT ON SALE YET, NO ADS") + "  ·  THE STORE’S LISTING PHOTO", warn=not p["sale"],
                title=p["title"], name=it["name"].lower(), meta=f"{p['price']}  ·  {p['code']}  ·  {it['meta']}  ·  {it['id']}",
                line=it["line"], sub=" · ".join(x for x in (p["size"], "Stones: " + p["stones"] if p["stones"] not in ("", "None") else "", p["options"]) if x))

def split(items, size):                 # contiguous parts of near-equal size, each under the limit
    total = sum(size(x) for x in items); n = max(1, -(-int(total) // int(P.LIMIT - 1.5e6))); target = total / n
    parts, cur, s = [], [], 0
    for x in items:
        if cur and s + size(x) > target * 1.04 and len(parts) < n - 1: parts.append(cur); cur, s = [], 0
        cur.append(x); s += size(x)
    return parts + [cur]

def pdfs(ads, prods):
    os.makedirs(f"{SITE}/pdfs", exist_ok=True); made = []
    def write(fn, title, sub, kind, pages, first=None):
        path = f"{SITE}/pdfs/{fn}"; c = canvas.Canvas(path); c.setTitle(f"Naira Petite · {title}")
        if first: first(c)
        tally = {}
        for it, cap in pages: tally[it["title"]] = tally.get(it["title"], 0) + 1
        P.cover(c, title, sub, ["In this file:"] + [f"{k}: {v} photograph{'s' if v > 1 else ''}" for k, v in tally.items()])
        for it, cap in pages: photo_page(c, it, cap)
        c.save(); mb = os.path.getsize(path) / 1e6; assert mb < P.LIMIT / 1e6, (fn, mb)
        made.append(dict(file=fn, title=title, kind=kind, count=len(pages), mb=round(mb, 1))); print(fn, len(pages), f"{mb:.1f} MB")
    def kit(c):
        P.brand_page(c); P.cover(c, "Edition Two: the ad brief", "Read this before making an ad from these photographs.", BRIEF)
    for ok, fn, title, sub, kind in [
            (True, "Naira-E2-1-Ad-photos-ready.pdf", "Edition Two ad photos, ready", "Clean photographs with no copy on them, "
             "ready to build ads from. Each caption names the piece, the price and anything to watch.", "Ad photos"),
            (False, "Naira-E2-2-Ad-photos-use-with-care.pdf", "Edition Two ad photos, use with care", "Clean photographs with a "
             "known fault, named in each caption: crop around it, fix it, or pick a ready photo instead.", "Ad photos")]:
        group = [x for x in ads if x["ok"] == ok]
        write(fn, title, sub, kind, [(x, ad_cap(x)) for x in group], kit if ok else None)
    for t, label in TYPES:
        pages = [(it, list_cap(p, it)) for p in prods if p["type"] == t for it in p["photos"]]
        parts = split(pages, lambda pc: os.path.getsize(pc[0]["src"]))
        for k, part in enumerate(parts, 1):
            tag = f", part {k} of {len(parts)}" if len(parts) > 1 else ""
            write(f"Naira-E2-3-Listing-{label}{f'-{k}' if len(parts) > 1 else ''}.pdf", f"Edition Two listing photos: {label.lower()}{tag}",
                  "The store’s own product photos, the truth to check any ad against. Drafts are marked: no ads for them yet.",
                  "Listing photos", part)
    return made

# ---- page ----
def main():
    for d in ("t", "f", "l", "lf", "brand", "pdfs"): os.makedirs(f"{SITE}/{d}", exist_ok=True)
    ads, prods = plates(), products()
    for it in ads: thumb(it["src"], f"{SITE}/{it['t']}"); shutil.copyfile(it["src"], f"{SITE}/{it['f']}")
    for p in prods:
        for it in p["photos"]: thumb(it["src"], f"{SITE}/{it['t']}"); shutil.copyfile(it["src"], f"{SITE}/{it['f']}")
    marks = [("Naira-wordmark-ink.png", "logo_ink.png", "Black, for light photographs"), ("Naira-wordmark-white.png", "logo_white.png",
             "White, for dark photographs"), ("Naira-wordmark-sage.png", "logo_sage.png", "Sage, on blush paper only")]
    for fn, src, _ in marks: shutil.copyfile(f"{HERE}/brand/{src}", f"{SITE}/brand/{fn}")
    made = pdfs(ads, prods)
    strip = lambda it: {k: v for k, v in it.items() if k not in ("src", "rank", "w", "h")}
    data = dict(ads=[strip(x) for x in ads], products=[dict(p, photos=[strip(x) for x in p["photos"]]) for p in prods],
                types=[dict(key=t, label=l) for t, l in TYPES], pdfs=made, marks=[dict(file=f, line=l) for f, _, l in marks],
                brief=BRIEF, mb=round(sum(p["mb"] for p in made), 1),
                counts=dict(ads=len(ads), ready=sum(x["ok"] for x in ads), listing=sum(len(p["photos"]) for p in prods),
                            pieces=len(prods), sale=sum(p["sale"] for p in prods)))
    b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
    for n in ("logo_sage", "logo_white"):
        im = Image.open(f"{HERE}/brand/{n}.png"); im.resize((480, round(im.height * 480 / im.width)), Image.LANCZOS).save(f"{OUT}/{n}_480.png")
    tpl = open(f"{HERE}/e2_plain_template.html", encoding="utf-8").read()
    page = (tpl.replace("__VELISTA__", b64(f"{HERE}/brand/Velista.ttf")).replace("__WM_LIGHT__", b64(f"{OUT}/logo_sage_480.png"))
               .replace("__WM_DARK__", b64(f"{OUT}/logo_white_480.png")).replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    open(f"{SITE}/index.html", "w", encoding="utf-8").write(page)
    # files map in publish order (page and thumbnails first, so the page works from the first publish), each under 250 files and 60 MB
    paths = ([x["t"] for x in ads] + [it["t"] for p in prods for it in p["photos"]] + [f"brand/{f}" for f, _, _ in marks] +
             [x["f"] for x in ads] + [it["f"] for p in prods for it in p["photos"]] + [f"pdfs/{p['file']}" for p in made])
    paths = list(dict.fromkeys(paths)); bins, cur, s = [], {}, 0
    for p in paths:
        sz = os.path.getsize(f"{SITE}/{p}")
        if cur and (s + sz > BIN_MB or len(cur) >= BIN_FILES): bins.append(cur); cur, s = {}, 0
        cur[p] = {"from": f"{SITE}/{p}"}; s += sz
    bins.append(cur); json.dump(bins, open(f"{OUT}/publish.json", "w"), indent=1)
    print("ads", len(ads), "photos", data["counts"]["listing"], "files", len(paths), "MB", round(sum(os.path.getsize(f"{SITE}/{p}") for p in paths) / 1e6, 1),
          "page KB", round(os.path.getsize(f"{SITE}/index.html") / 1024), "publishes", [(len(b), round(sum(os.path.getsize(f"{SITE}/{p}") for p in b) / 1e6, 1)) for b in bins])

if __name__ == "__main__":
    main()
