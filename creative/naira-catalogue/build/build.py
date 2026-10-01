"""
NAIRA PETITE — The Catalogue, Volume One (A4, 10 pages).

Pages: 1 cover · 2 about · 3–6 four themed camps · 7–10 price list by family (+ ordering on 10).
Images are cropped here from the Higgsfield originals and Shopify photos to the exact placed size at
300 dpi (never upscaled), so the PDF carries print-resolution JPEGs and nothing heavier.
"""
import io, json, os, re, sys, base64
from pathlib import Path
from PIL import Image
import segno

C = Path(__file__).resolve().parent
SCR = C.parent
CAMP = SCR / "camp"
sys.path.insert(0, str(CAMP / "studio"))
import base  # fonts + logo vector + palette

IMG = C / "img"; IMG.mkdir(exist_ok=True)
BLEED = float(os.environ.get("BLEED", "0"))   # mm; 3 for the print master
OUT = C / "out"; OUT.mkdir(exist_ok=True)
LIB = json.load(open(CAMP / "library.json"))
RAW = json.load(open(C / "raw_index.json"))

CREAM, PAPER, BLUSH, BLUSH_MID = "#F4F0E8", "#FBF5F0", "#FBEDE9", "#F2CFC4"
INK, INK_SOFT, MUTED = "#1C1C1C", "#3D3530", "#6B615A"
SAGE_DEEP, CORAL_DEEP = "#5E7A70", "#B8604A"
SAGE_GROUND, RED_GROUND = "#9CB1A5", "#4B191A"


# ---- images ---------------------------------------------------------------------------------
def crop(src, w, h, fx=0.5, fy=0.5, zoom=1.0, key=None):
    """Crop `src` to the w:h (mm) aspect around (fx, fy) with optional zoom, at <= 300 dpi."""
    key = key or Path(src).stem
    name = f"{key}_{w:g}x{h:g}_{fx:g}_{fy:g}_{zoom:g}".replace(".", "p") + ".jpg"
    out = IMG / name
    if not out.exists():
        im = Image.open(src).convert("RGB")
        W, H = im.size
        ar = w / h
        cw, ch = (H * ar, H) if W / H > ar else (W, W / ar)
        cw, ch = cw / zoom, ch / zoom
        cx = min(max(fx * W, cw / 2), W - cw / 2)
        cy = min(max(fy * H, ch / 2), H - ch / 2)
        c = im.crop((round(cx - cw / 2), round(cy - ch / 2), round(cx + cw / 2), round(cy + ch / 2)))
        tw = round(w / 25.4 * 300)
        if c.width > tw:
            c = c.resize((tw, round(tw / ar)), Image.LANCZOS)
        c.save(out, "JPEG", quality=90, subsampling=0, optimize=True)
    return f"img/{name}"


def hf(key):
    return RAW[key]["path"]


def photo(src, x, y, w, h, fx=0.5, fy=0.5, zoom=1.0, key=None, extra=""):
    if BLEED:
        r, b = x + w >= 209.99, y + h >= 296.99
        if x <= 0.01: x, w = x - BLEED, w + BLEED
        if r: w += BLEED
        if y <= 0.01: y, h = y - BLEED, h + BLEED
        if b: h += BLEED
    return (f"<img class='ph' src='{crop(src, w, h, fx, fy, zoom, key)}' "
            f"style='left:{x}mm;top:{y}mm;width:{w}mm;height:{h}mm;{extra}' alt=''>")


# ---- type & marks ---------------------------------------------------------------------------
def T(text, x, y, cls, w=None, extra="", tag="div"):
    ww = f"width:{w}mm;" if w is not None else ""
    return f"<{tag} class='abs {cls}' style='left:{x}mm;top:{y}mm;{ww}{extra}'>{text}</{tag}>"


def logo(x, y, w, mode="brand", anchor="left"):
    L = base._LOGO
    letters, flower = {"brand": (base.LOGO_SAGE, base.LOGO_BLUSH), "ink": (INK, INK),
                       "cream-blush": (PAPER, base.LOGO_BLUSH), "ink-blush": (INK, base.LOGO_BLUSH),
                       "sage": (SAGE_DEEP, base.LOGO_BLUSH)}[mode]
    px, py = 65, 65
    vw, vh = L["width"] - 2 * px, L["height"] - 2 * py
    h = w * vh / vw
    if anchor == "center":
        x -= w / 2
    return (f"<svg class='abs' style='left:{x}mm;top:{y}mm;width:{w}mm;height:{h:.2f}mm' viewBox='{px} {py} {vw} {vh}'>"
            f"<path d='{L['letters']}' fill='{letters}' fill-rule='evenodd'/><path d='{L['flower']}' fill='{flower}' fill-rule='evenodd'/></svg>")


def qr(url, x, y, size, color=INK):
    q = segno.make(url, error="m")
    n = q.symbol_size(border=0)[0]
    path = []
    for r, row in enumerate(q.matrix):
        for c, v in enumerate(row):
            if v:
                path.append(f"M{c} {r}h1v1h-1z")
    return (f"<svg class='abs' style='left:{x}mm;top:{y}mm;width:{size}mm;height:{size}mm' viewBox='0 0 {n} {n}' "
            f"shape-rendering='crispEdges'><path d='{''.join(path)}' fill='{color}'/></svg>")


def leaf(which, x, y, w, rot=0, op=0.3):
    p = base.LEAVES[which]
    return (f"<img class='abs' src='data:image/png;base64,{base.b64(p)}' "
            f"style='left:{x}mm;top:{y}mm;width:{w}mm;transform:rotate({rot}deg);opacity:{op}' alt=''>")


def rule(x, y, w, color=INK, op=0.25):
    return f"<div class='abs' style='left:{x}mm;top:{y}mm;width:{w}mm;height:0;border-top:0.25pt solid {color};opacity:{op}'></div>"


def inr(n):
    return base.inr(n)


def folio(n, color=MUTED, left="NAIRA PETITE &nbsp;·&nbsp; THE CATALOGUE &nbsp;·&nbsp; MMXXVI", lx=14):
    return (T(left, lx, 286.2, "folio", extra=f"color:{color}") +
            T(f"{n:02d}", 196, 286.2, "folio", extra=f"color:{color};transform:translateX(-100%)"))


# ---- product data ---------------------------------------------------------------------------
def material(h):
    tags = LIB[h].get("tags") or []
    if "Rose Gold Tone" in tags:
        metal = "Rose gold coated"
    elif "Two Tone" in tags:
        metal = "Rhodium coated, gold heart"
    elif any(t.startswith("Rhodium") for t in tags):
        metal = "Rhodium coated"
    else:
        metal = "18k gold coated"
    stones = [s for s, t in (("pearl", "Pearl"), ("cubic zirconia", "Cubic Zirconia")) if t in tags]
    bits = [metal] + stones
    if "Waterproof" not in tags:
        bits.append("keep dry")
    return " · ".join(bits)


ODD = {  # products whose first Shopify photo is off-grid (model, red ground, logo): use a plinth/cream shot
    "heartbead-bracelet": CAMP / "raw/heartbead-bracelet/shop1.jpg",
    "halo-curve-ring": CAMP / "raw/halo-curve-ring/shop2.jpg",
    "woven-gold-hoops": CAMP / "raw/woven-gold-hoops/shop1.jpg",
    "bold-nocturne-chain": CAMP / "raw/bold-nocturne-chain/shop2.jpg",
    "prism-riviere-bracelet": CAMP / "raw/prism-riviere-bracelet/shop3.jpg",
    "blush-cluster-ring": CAMP / "raw/blush-cluster-ring/shop1.jpg",
    "pearl-drop-studs": None,  # Higgsfield still life on the plinth
    "star-point-band": CAMP / "raw/star-point-band/shop2.jpg",
    "toggle-link-chain": CAMP / "raw/toggle-link-chain/shop1.jpg",
    "verdant-eternity-band": CAMP / "raw/verdant-eternity-band/shop3.jpg",
    "bold-nocturne-bracelet": CAMP / "raw/bold-nocturne-bracelet/shop1.jpg",
    "pearl-legacy-necklace": CAMP / "raw/pearl-legacy-necklace/shop1.jpg",
}
FOCUS = {}  # per-product (fx, fy, zoom) for the grid crop; filled from grid_focus.json if present
if (C / "grid_focus.json").exists():
    FOCUS = {k: tuple(v) for k, v in json.load(open(C / "grid_focus.json")).items()}


def grid_src(h):
    if h == "pearl-drop-studs":
        return hf("pearl-drop-studs:48dc")
    if h in ODD:
        return ODD[h]
    return CAMP / "shop" / h / "0.jpg"


def card(h, x, y, w, ih):
    fx, fy, z = FOCUS.get(h, (0.5, 0.45, 1.15))
    p = LIB[h]
    return (photo(grid_src(h), x, y, w, ih, fx, fy, z, key=f"g_{h}") +
            T(p["title"], x, y + ih + 2.6, "pname", w=w) +
            T(material(h), x, y + ih + 6.6, "pmat", w=w) +
            T(inr(p["price"]), x, y + ih + 10.4, "pprice", w=w))


def by_type(t):
    hs = [h for h, p in LIB.items() if p["type"] == t]
    return sorted(hs, key=lambda h: (LIB[h]["price"], LIB[h]["title"]))


# ---- pages ----------------------------------------------------------------------------------
pages = []

# 1 · cover
pages.append(("cover", CREAM, "".join([
    logo(105, 15.5, 46, "brand", anchor="center"),
    T("DEMI-FINE JEWELLERY &nbsp;·&nbsp; THE CATALOGUE", 105, 28.4, "eyebrow center"),
    photo(hf("baroque-pearl-lariat:eeed"), 14, 36, 182, 213, fx=0.47, fy=0.52, key="cover"),
    T("<span class='disp'>SOFTLY, SLOWLY,</span><span class='it' style='margin-left:2.6mm'>worn.</span>", 105, 254, "covertitle center"),
    rule(14, 278.6, 182, INK, 0.22),
    T("VOLUME ONE &nbsp;·&nbsp; FESTIVE MMXXVI", 14, 282.2, "folio", extra=f"color:{INK_SOFT}"),
    T("NAIRAFLORE.COM", 196, 282.2, "folio", extra=f"color:{INK_SOFT};transform:translateX(-100%)"),
])))

# 2 · about
counts = {t: len(by_type(t)) for t in ("Earrings", "Ring", "Necklace", "Bracelet")}
prices = [p["price"] for p in LIB.values()]
FAMILY = [("Earrings", "EARRINGS", "pearl-point-studs"), ("Ring", "RINGS", "chevron-whisper-ring"),
          ("Necklace", "NECKLACES", "heartline-paperclip-necklace"), ("Bracelet", "BRACELETS", "prism-riviere-bracelet")]
fam = []
for i, (t, label, h) in enumerate(FAMILY):
    x = 14 + i * (cw_fam := (182 - 3 * 5) / 4 + 5)
    fx, fy, z = FOCUS.get(h, (0.5, 0.45, 1.15))
    fam.append(photo(grid_src(h), x, 177, cw_fam - 5, 58, fx, fy, z, key=f"fam_{h}"))
    fam.append(T(f"<span class='num-big'>{counts[t]}</span><span class='label'>{label}</span>", x, 238.5, "stat"))
pages.append(("about", PAPER, "".join([
    T("ABOUT NAIRA", 14, 16, "eyebrow"),
    T("<span class='disp'>HERE YOUR STORY IS<br>HAND-STITCHED</span><br><span class='it'>into every thread.</span>", 14, 24, "h2", w=110),
    T("Naira is an Indian couture house: soft tailoring, pressed flowers and the long quiet of an Indian afternoon. "
      "Every outfit is hand-finished and made to measure in our atelier, one at a time.", 14, 56, "body", w=102),
    T("Naira Petite is the house’s demi-fine jewellery. The same soul in a smaller object: pieces made to be worn "
      "every day, light enough to forget you have them on, and finished to keep their colour.", 14, 76.5, "body", w=102),
    T("[ 18k gold coated &nbsp;·&nbsp; rhodium coated ]", 14, 99, "matline"),
    photo(CAMP / "raw/pearl-legacy-necklace/shop2.jpg", 126, 16, 70, 88, fx=0.5, fy=0.52, key="box"),
    T("The Naira box, in blush.", 126, 106.5, "caption"),
    rule(14, 117, 182),
    T("THE PETITE PROMISE", 14, 122, "eyebrow"),
    T("<span class='label'>HYPOALLERGENIC</span><br>Gentle on every ear, wrist and finger. True of every piece in these pages.", 14, 130, "small", w=56),
    T("<span class='label'>TARNISH-FREE</span><br>Made to stay gold, through work, travel and the wedding season.", 77, 130, "small", w=56),
    T("<span class='label'>WATERPROOF</span><br>Shower, swim, sweat. Daily wear and water are fine.", 140, 130, "small", w=56),
    T("All but three pieces are tarnish-free and waterproof as well. The Pearl Legacy Necklace, the Baroque Shell "
      "Bracelet and the Verdant Drop Earrings would rather be kept dry; they are marked in the price list.", 14, 152.5, "fine", w=182),
    rule(14, 164, 182),
    T("THE PETITE COLLECTION", 14, 169, "eyebrow"),
    "".join(fam),
    T(f"{len(LIB)} pieces in stock as this catalogue goes out, from {inr(min(prices))} to {inr(max(prices))}. "
      "The four camps follow on pages 03 to 06, and the full price list runs from page 07 to page 10.", 14, 255, "small", w=150),
    folio(2),
])))

# 3 · camp I — the long afternoon
pieces1 = [("toggle-link-chain", ""), ("pearl-blossom-earrings", ""), ("halo-curve-ring", ""), ("baroque-pearl-lariat", "on the cover")]


def piece_list(items, x, y, w, color=INK, mcolor=MUTED):
    rows = []
    for h, note in items:
        p = LIB[h]
        n = p["title"] + (f" <span class='it-s'>({note})</span>" if note else "")
        rows.append(f"<div class='pl'><span>{n}</span><span class='pl-p'>{inr(p['price'])}</span></div>")
    return T("".join(rows), x, y, "plist", w=w, extra=f"color:{color};--m:{mcolor}")


pages.append(("camp1", CREAM, "".join([
    photo(hf("toggle-link-chain:ed86"), 0, 0, 118, 297, fx=0.6, fy=0.5, key="c1hero"),
    T("CAMP I", 126, 16, "eyebrow"),
    T("<span class='disp'>THE LONG<br>AFTERNOON</span>", 126, 23, "h1"),
    T("<span class='it'>light through a cotton blind.</span>", 126, 47.5, "h3"),
    T("Cream cotton, slow hours and gold that warms to the skin. The pieces for a whole day: put on with the first "
      "coffee, still there at the last light.", 126, 59, "body", w=70),
    photo(hf("pearl-blossom-earrings:b5f9"), 126, 90, 70, 74, fx=0.5, fy=0.44, zoom=1.1, key="c1a"),
    photo(hf("halo-curve-ring:c39c"), 126, 168, 70, 74, fx=0.42, fy=0.36, zoom=1.15, key="c1b"),
    piece_list(pieces1, 126, 249, 70),
    folio(3, left="NAIRA PETITE &nbsp;·&nbsp; MMXXVI", lx=126),
])))

# 4 · camp II — sage
pieces2 = [("pearl-point-studs", ""), ("bold-nocturne-chain", ""), ("ribbon-bow-earrings", ""),
           ("silver-drop-earrings", ""), ("verdant-drop-earrings", "")]
pages.append(("camp2", SAGE_GROUND, "".join([
    T("CAMP II", 14, 16, "eyebrow", extra=f"color:{INK}"),
    T("<span class='disp'>SAGE</span>", 14, 22, "h1 big"),
    T("<span class='it'>gold, pearl and a cardamom pod.</span>", 14, 41, "h3"),
    T("Our one cool note. Gold and pearl laid on sage paper, the green of a monsoon leaf, and a single green "
      "stone to answer it.", 118, 22.5, "body", w=78, extra=f"color:{INK}"),
    photo(hf("pearl-point-studs:e387"), 14, 56, 120, 150, fx=0.5, fy=0.42, key="c2hero"),
    photo(hf("bold-nocturne-chain:a524"), 140, 56, 56, 72, fx=0.5, fy=0.5, zoom=1.0, key="c2a"),
    photo(hf("ribbon-bow-earrings:4665"), 140, 134, 56, 72, fx=0.45, fy=0.45, zoom=1.05, key="c2b"),
    photo(hf("silver-drop-earrings:9004"), 14, 212, 57, 66, fx=0.47, fy=0.5, zoom=1.0, key="c2c"),
    photo(hf("verdant-drop-earrings:e9c4"), 77, 212, 57, 66, fx=0.55, fy=0.45, zoom=1.1, key="c2d"),
    piece_list(pieces2, 140, 213.5, 56, INK, "#2F3D37"),
    folio(4, color="#2F3D37"),
])))

# 5 · camp III — steel & gold
pieces3 = [("textured-gold-hoops", "in the tumbler"), ("woven-gold-hoops", "the tiffin and the king"),
           ("baroque-shell-bracelet", "in the coupe")]
pages.append(("camp3", CREAM, "".join([
    T("CAMP III", 14, 16, "eyebrow"),
    T("<span class='disp'>STEEL &amp; GOLD</span>", 14, 22, "h1 big"),
    T("<span class='it'>from the kitchen shelf.</span>", 14, 41, "h3"),
    T("The steel tumbler, the tiffin, the chessboard after lunch. Everyday Indian steel, and gold made for "
      "every day.", 118, 22.5, "body", w=78),
    photo(hf("textured-gold-hoops:7b08"), 14, 56, 58, 118, fx=0.5, fy=0.42, zoom=1.0, key="c3a"),
    photo(hf("woven-gold-hoops:4154"), 76, 56, 58, 118, fx=0.53, fy=0.5, zoom=1.0, key="c3b"),
    photo(hf("woven-gold-hoops:7e9c"), 138, 56, 58, 118, fx=0.55, fy=0.5, zoom=1.0, key="c3c"),
    photo(hf("baroque-shell-bracelet:f701"), 14, 180, 120, 98, fx=0.5, fy=0.45, zoom=1.0, key="c3d"),
    piece_list(pieces3, 140, 181.5, 56),
    T("Steel is the one Indian object on these pages: the tumbler on every kitchen shelf, the tiffin on every desk.",
      140, 236, "fine", w=56),
    folio(5),
])))

# 6 · camp IV — the red room (full bleed)
pieces4 = [("pearl-ribbon-ring", ""), ("heartbead-bracelet", "")]
pages.append(("camp4", RED_GROUND, "".join([
    photo(hf("pearl-ribbon-ring:b275"), 0, 0, 210, 297, fx=0.42, fy=0.5, key="c4hero"),
    T("CAMP IV", 14, 16, "eyebrow", extra=f"color:{PAPER}"),
    T("<span class='disp'>THE RED ROOM</span>", 14, 22, "h1 big", extra=f"color:{PAPER}"),
    T("<span class='it'>lit for the festive table.</span>", 14, 41, "h3", extra=f"color:{PAPER}"),
    photo(hf("heartbead-bracelet:b5f1"), 132, 188, 64, 80, fx=0.45, fy=0.5, zoom=1.0, key="c4a",
          extra=f"outline:1.2mm solid {PAPER};"),
    T("Sealing wax, a red glass, the evening the lamps come out. Two pieces for the festive weeks, and for every "
      "gift between them.", 14, 236, "body", w=100, extra=f"color:{PAPER}"),
    piece_list(pieces4, 14, 254, 100, PAPER, "#E9CFC5"),
    folio(6, color="#E9CFC5"),
])))

# 7 · earrings (4 x 4, feature tile spans two cells)
def grid_page(n, title, line, family, cols, cw, ih, x0, y0, rowh, slots, extra_cells, header_extra="", bg=PAPER, meta_left=False):
    hs = by_type(family)
    lo, hi = min(LIB[h]["price"] for h in hs), max(LIB[h]["price"] for h in hs)
    parts = [T(f"THE COLLECTION &nbsp;·&nbsp; {n - 6:02d}", 14, 16, "eyebrow"),
             T(f"<span class='disp'>{title}</span>", 14, 22, "h1 big"),
             T(f"<span class='it'>{line}</span>", 14, 41, "h3"),
             (T(f"{len(hs)} pieces &nbsp;·&nbsp; {inr(lo)} to {inr(hi)}", 14, 53, "meta") if meta_left else
              T(f"{len(hs)} pieces &nbsp;·&nbsp; {inr(lo)} to {inr(hi)}", 196, 44.5, "meta", extra="transform:translateX(-100%)")),
             header_extra]
    free = [s for s in range(slots) if s not in extra_cells]
    for h, s in zip(hs, free):
        r, c = divmod(s, cols)
        parts.append(card(h, x0 + c * (cw + (182 - cols * cw) / (cols - 1)), y0 + r * rowh, cw, ih))
    parts.append(folio(n))
    return "".join(parts)


cw4 = (182 - 3 * 5) / 4          # 41.75 mm
ear_feature = (photo(hf("baguette-arc-hoops:51e4"), 14 + 2 * (cw4 + 5), 56, 2 * cw4 + 5, 37 + 13, fx=0.5, fy=0.5, zoom=1.0, key="earfeat") +
               T("Baguette Arc Hoops, drawn through pink sand.", 14 + 2 * (cw4 + 5), 56 + 50 + 1.5, "caption-s", w=2 * cw4 + 5))
pages.append(("earrings", PAPER, grid_page(7, "EARRINGS", "fourteen ways to frame a face.", "Earrings", 4, cw4, 37, 14, 56, 57.5, 16, {2, 3}, ear_feature)))

# 8 · rings (hero band + 4 x 3)
ring_hero = photo(hf("verdant-eternity-band:0d46"), 0, 0, 210, 0.1, key="dummy") if False else ""
pages.append(("rings", PAPER, "".join([
    photo(hf("verdant-eternity-band:0d46"), 0, 0, 210, 74, fx=0.55, fy=0.47, zoom=1.0, key="ringhero"),
    T("Verdant Eternity Band, over green ink.", 196, 76.5, "caption-s", extra="transform:translateX(-100%);text-align:right"),
]) + grid_page(8, "RINGS", "for the hand you talk with.", "Ring", 4, cw4, 37, 14, 118, 56.5, 12, set())
    .replace("top:16mm", "top:84mm", 1).replace("top:22mm", "top:90mm", 1).replace("top:41mm", "top:109mm", 1).replace("top:44.5mm", "top:112.5mm", 1)))

# 9 · necklaces (3 cols; on-model feature spans two rows in col 1)
cw3 = (182 - 2 * 6) / 3          # 56.67 mm
neck_feature = (photo(hf("heartline-paperclip-necklace:a18a"), 14, 56, cw3, 2 * 66 - 4 + 13, fx=0.5, fy=0.45, zoom=1.0, key="neckfeat") +
                T("Heartline Paperclip Necklace, worn.", 14, 56 + 2 * 66 - 4 + 13 + 1.5, "caption-s", w=cw3))
pages.append(("necklaces", PAPER, grid_page(9, "NECKLACES", "close to the collarbone.", "Necklace", 3, cw3, 50, 14, 56, 70, 9, {0, 3}, neck_feature)))

# 10 · bracelets + ordering
cw3b = cw3
order = "".join([
    f"<div class='abs' style='left:{-BLEED}mm;top:236mm;width:{210 + 2 * BLEED}mm;height:{61 + BLEED}mm;background:{BLUSH}'></div>",
    logo(14, 246, 38, "brand"),
    T("Made to stay gold.", 14, 258.5, "caption"),
    T("<span class='label'>TO ORDER</span><br>Shop the whole collection at <b>nairaflore.com</b>.<br>"
      "Or WhatsApp us on <b>+91 95615 57935</b>,<br>Monday to Saturday, 10 am to 7 pm IST.", 74, 245, "small", w=86),
    qr("https://nairaflore.com", 172, 244, 24),
    T("nairaflore.com", 184, 269.5, "fine", extra="transform:translateX(-50%);text-align:center"),
    T("Prices in Indian rupees as listed on nairaflore.com on 1 October 2026. Photographs may be enlarged to show detail.",
      14, 279.5, "fine", w=182),
])
brace_care = T("<span class='label'>CARE</span><br>Daily wear and water are fine. Keep each piece dry and in its box "
               "between wears, and put perfume on before your jewellery, not after.", 14 + 2 * (cw3 + 6), 160, "small", w=cw3)
pages.append(("bracelets", PAPER, "".join([
    photo(hf("prism-riviere-bracelet:2513"), 112, 14, 84, 70, fx=0.5, fy=0.47, zoom=1.0, key="bracehero"),
    T("Prism Rivière Bracelet, in the light.", 196, 86, "caption-s", extra="transform:translateX(-100%)"),
]) + grid_page(10, "BRACELETS", "a wrist, quietly.", "Bracelet", 3, cw3, 46, 14, 94, 67, 6, {5}, brace_care, meta_left=True)
    + order))


# ---- html ----------------------------------------------------------------------------------
CSS = f"""
@page {{ size: {210 + 2 * BLEED}mm {297 + 2 * BLEED}mm; margin: 0 }}
* {{ margin:0; padding:0; box-sizing:border-box }}
html, body {{ background:#fff }}
body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact }}
.trim {{ position:absolute; left:{BLEED}mm; top:{BLEED}mm; width:210mm; height:297mm }}
.page {{ position:relative; width:{210 + 2 * BLEED}mm; height:{297 + 2 * BLEED}mm; overflow:hidden; page-break-after:always; break-after:page; color:{INK} }}
.page:last-child {{ page-break-after:auto; break-after:auto }}
.abs {{ position:absolute }}
img.ph {{ position:absolute; display:block; object-fit:cover }}
.center {{ transform:translateX(-50%); text-align:center; white-space:nowrap }}
.disp {{ font-family:'Rupee','Velista',Georgia,serif; font-weight:400; letter-spacing:.012em }}
.it {{ font-family:'Rupee','CormI',Georgia,serif; font-style:italic; font-weight:400 }}
.it-s {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:9.5pt; color:var(--m) }}
.eyebrow {{ font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:6.6pt; letter-spacing:.26em; color:{INK_SOFT}; white-space:nowrap }}
.folio {{ font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:5.9pt; letter-spacing:.24em; white-space:nowrap }}
.covertitle .disp {{ font-size:27pt }}
.covertitle .it {{ font-size:33pt }}
.h1 .disp {{ font-size:27pt; line-height:1.0 }}
.h1.big .disp {{ font-size:34pt; line-height:1.0; white-space:nowrap }}
.h2 .disp {{ font-size:21pt; line-height:1.04 }}
.h2 .it {{ font-size:23pt; line-height:1.15 }}
.h3 .it {{ font-size:17pt; line-height:1.1; white-space:nowrap }}
.body {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:9.2pt; line-height:1.55; color:{INK_SOFT} }}
.small {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:8.2pt; line-height:1.5; color:{INK_SOFT} }}
.small b, .small .label, .label {{ font-weight:500 }}
.label {{ font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:6.6pt; letter-spacing:.24em; color:{INK}; display:inline-block; margin-bottom:1.2mm }}
.fine {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:6.9pt; line-height:1.5; color:{MUTED} }}
.matline {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:8.6pt; letter-spacing:.12em; color:{SAGE_DEEP}; white-space:nowrap }}
.caption {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:11.5pt; color:{INK_SOFT}; white-space:nowrap }}
.caption-s {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:9.6pt; color:{INK_SOFT}; white-space:nowrap }}
.meta {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:7.6pt; letter-spacing:.06em; color:{INK_SOFT}; white-space:nowrap }}
.stat {{ display:flex; align-items:baseline; gap:2.2mm; white-space:nowrap }}
.num-big {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:26pt; line-height:1; color:{INK} }}
.toc {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:7.8pt; line-height:1.62; color:{INK_SOFT} }}
.pname {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:8.2pt; line-height:1.2; color:{INK}; white-space:nowrap; overflow:hidden; text-overflow:ellipsis }}
.pmat {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:6.5pt; line-height:1.2; color:{MUTED}; white-space:nowrap; overflow:hidden; text-overflow:ellipsis }}
.pprice {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:8.6pt; letter-spacing:.02em; color:{INK} }}
.plist {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:8.1pt; line-height:1.4 }}
.plist .pl {{ display:flex; justify-content:space-between; gap:3mm; padding:1.25mm 0; border-top:0.25pt solid currentColor }}
.plist .pl:last-child {{ border-bottom:0.25pt solid currentColor }}
.plist .pl-p {{ font-weight:400; white-space:nowrap }}
"""


CORM_FULL = ("@font-face{font-family:'CormI';src:url(data:font/woff2;base64,"
             + base.b64(SCR / "fonts" / "cormorant-garamond-latin-300-italic.woff2")
             + ") format('woff2');font-style:italic;font-weight:400;font-display:block}")


def html():
    body = "".join(f"<section class='page' id='p-{name}' style='background:{bg}'><div class='trim'>{inner}</div></section>" for name, bg, inner in pages)
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>NAIRA PETITE · The Catalogue · Volume One</title>"
            f"<style>{base.fonts_css()}{CORM_FULL}{CSS}</style></head><body>{body}</body></html>")


if __name__ == "__main__":
    (C / ("catalogue-bleed.html" if BLEED else "catalogue.html")).write_text(html())
    print("pages", len(pages), "images", len(list(IMG.glob('*.jpg'))))
