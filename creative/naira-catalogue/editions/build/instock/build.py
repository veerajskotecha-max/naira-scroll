"""
NAIRA PETITE — The Catalogue, one camp per edition (A4), with every piece in stock.

The cover, About and the four camp pages are the editions of 1 October unchanged (same photographs, same crops).
The price list now carries every Naira Petite piece in stock on nairaflore.com on the day of the build: each family
keeps its opening page and continues on a second page, then comes an index of every piece and a back cover.
Pieces listed for pre-order are left out. THEME=apricot|lilac|sage picks the edition; BLEED=3 or 5 builds a print master.
"""
import math, json, os, re, sys
from pathlib import Path
from PIL import Image
import segno

C = Path(__file__).resolve().parent
ROOT = C.parent
sys.path.insert(0, str(C))
import base  # fonts + logo vector + palette

REPO = base.REPO
OLD = REPO / "creative/naira-catalogue/editions/build/build_theme.py"
exec(re.search(r"THEMES = \{.*?\n\}\n", OLD.read_text(), re.S).group(0))   # the three camps, exactly as before
# the rings hero is now a 66 mm band (was 74): Lilac's crop moves down so the whole ring and its stones stay in frame
_ls, _lc = THEMES["lilac"]["ring"]
THEMES["lilac"]["ring"] = ((_ls[0], _ls[1], 0.52, _ls[3]), _lc)
MATTES = REPO / "creative/naira-catalogue/editions/build/mattes"

THEME = os.environ.get("THEME", "apricot")
BLEED = float(os.environ.get("BLEED", "0"))
SB = max(BLEED, 3.0)
AS_OF = os.environ.get("AS_OF", "26 October 2026")
IMG = ROOT / "img" / THEME; IMG.mkdir(parents=True, exist_ok=True)
LIB = json.load(open(ROOT / "data" / "library.json"))
RAWDIR = ROOT / "data" / "raw"

INK, INK_SOFT, MUTED = "#1C1C1C", "#3D3530", "#6B615A"
T = THEMES[THEME]
PAPER, GROUND, DEEP, TINT = T["paper"], T["ground"], T["deep"], T["tint"]
NUM = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
       12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
       30: "thirty", 40: "forty"}


def words(n):
    return NUM.get(n) or f"{NUM[n // 10 * 10]}-{NUM[n % 10]}"


# ---- images ---------------------------------------------------------------------------------
def raw(i):
    return RAWDIR / f"{i}.png"


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
    return f"img/{THEME}/{name}"


def photo(src, x, y, w, h, fx=0.5, fy=0.5, zoom=1.0, key=None, extra=""):
    if BLEED:
        r, b = x + w >= 209.99, y + h >= 296.99
        if x <= 0.01: x, w = x - BLEED, w + BLEED
        if r: w += BLEED
        if y <= 0.01: y, h = y - BLEED, h + BLEED
        if b: h += BLEED
    return (f"<img class='ph' src='{crop(src, w, h, fx, fy, zoom, key)}' "
            f"style='left:{x}mm;top:{y}mm;width:{w}mm;height:{h}mm;{extra}' alt=''>")


def slot(spec, x, y, w, h, key, extra=""):
    i, fx, fy, z = spec
    return photo(raw(i), x, y, w, h, fx, fy, z, key=f"{key}_{i}", extra=extra)


# ---- type & marks ---------------------------------------------------------------------------
def Tx(text, x, y, cls, w=None, extra="", tag="div"):
    ww = f"width:{w}mm;" if w is not None else ""
    return f"<{tag} class='abs {cls}' style='left:{x}mm;top:{y}mm;{ww}{extra}'>{text}</{tag}>"


def logo(x, y, w, mode="brand", anchor="left"):
    L = base._LOGO
    letters, flower = {"brand": (base.LOGO_SAGE, base.LOGO_BLUSH), "ink": (INK, INK),
                       "cream-blush": (PAPER, base.LOGO_BLUSH), "ink-blush": (INK, base.LOGO_BLUSH),
                       "sage": ("#5E7A70", base.LOGO_BLUSH), "deep": (DEEP, base.LOGO_BLUSH),
                       "cover": (T["cover"]["head"], base.LOGO_BLUSH)}[mode]
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


def rule(x, y, w, color=INK, op=0.25):
    return f"<div class='abs' style='left:{x}mm;top:{y}mm;width:{w}mm;height:0;border-top:0.25pt solid {color};opacity:{op}'></div>"


inr = base.inr
FOLIO_LEFT = f"NAIRA PETITE &nbsp;·&nbsp; {T['edition']} &nbsp;·&nbsp; MMXXVI"


def folio(n, color=MUTED, left=FOLIO_LEFT, lx=14):
    return (Tx(left, lx, 286.2, "folio", extra=f"color:{color}") +
            Tx(f"{n:02d}", 196, 286.2, "folio", extra=f"color:{color};transform:translateX(-100%)"))


# ---- product data ---------------------------------------------------------------------------
def material(h):
    p = LIB[h]
    return " · ".join([p["metal"]] + p["stones"] + ([] if p["waterproof"] else ["<b>keep dry</b>"]))


def price(h):
    p = LIB[h]
    return ("from " if p["from"] else "") + inr(p["price"])


FOCUS = {  # (fx, fy, zoom) for the grid crop where the default would cut the piece
}
DEF_FOCUS = (0.5, 0.45, 1.15)


def card(h, x, y, w, ih, th):
    fx, fy, z = FOCUS.get(h, DEF_FOCUS)
    p = LIB[h]
    ext = f"<span class='pext'>{p['extras']}</span>" if p["extras"] else ""
    return (photo(p["grid"], x, y, w, ih, fx, fy, z, key=f"g_{h}") +
            f"<div class='abs ptext' data-h='{h}' style='left:{x}mm;top:{y + ih + 2.4}mm;width:{w}mm;height:{th}mm'>"
            f"<div class='pname'>{p['title']}</div><div class='pmat'>{material(h)}</div><div class='pprice'>{price(h)}{ext}</div></div>")


def by_type(t):
    hs = [h for h, p in LIB.items() if p["type"] == t]
    return sorted(hs, key=lambda h: (LIB[h]["price"], LIB[h]["title"]))


def piece_list(items, x, y, w, color=INK, mcolor=MUTED):
    rows = []
    for h in items:
        p = LIB[h]
        rows.append(f"<div class='pl'><span>{p['title']}</span><span class='pl-p'>{price(h)}</span></div>")
    return Tx("".join(rows), x, y, "plist", w=w, extra=f"color:{color};--m:{mcolor}")


# ---- pages ----------------------------------------------------------------------------------
pages = []
CV = T["cover"]
N_ALL = len(LIB)
PRICES = [p["price"] for p in LIB.values()]


def cover_layers():
    """The masthead sits behind the piece: the piece is laid back over the letters from the same pixels, cut out with
    the BiRefNet matte made for the 3 mm crop and placed back in source pixels for any wider bleed."""
    import numpy as np, cv2
    im = Image.open(raw(CV["src"])).convert("RGB"); W, H = im.size
    mb = SB
    pw, ph = 210 + 2 * mb, 297 + 2 * mb

    def window(ar):
        z, fx, fy = CV["z"], CV["fx"], CV["fy"]
        cw, ch = (H * ar, H) if W / H > ar else (W, W / ar); cw, ch = cw / z, ch / z
        cx = min(max(fx * W, cw / 2), W - cw / 2); cy = min(max(fy * H, ch / 2), H - ch / 2)
        return (round(cx - cw / 2), round(cy - ch / 2), round(cx + cw / 2), round(cy + ch / 2))

    bx = window(pw / ph)
    c = im.crop(bx)
    c.save(IMG / f"cover_bg_{mb:g}.jpg", "JPEG", quality=92, subsampling=0, optimize=True)
    m3 = Image.open(MATTES / f"{THEME}_birefnet-general.png").convert("L")
    b3 = window(216 / 303)
    assert m3.size == (b3[2] - b3[0], b3[3] - b3[1]), (m3.size, b3)
    full = Image.new("L", (W, H), 0); full.paste(m3, (b3[0], b3[1]))
    matte = full.crop(bx)
    pxmm = c.width / pw
    y0 = max(int((CV["base"] - 50 + mb) * pxmm), 0); y1 = int((CV["base"] + 4 + mb) * pxmm)
    a = np.asarray(matte).astype(np.float32) / 255
    a[a < 0.06] = 0
    a = cv2.erode(a, np.ones((3, 3), np.uint8))
    a = cv2.GaussianBlur(a, (0, 0), 0.7)
    alpha = (a[y0:y1] * 255).clip(0, 255).astype(np.uint8)
    rgb = np.asarray(c)[y0:y1]
    Image.fromarray(np.dstack([rgb, alpha])).save(IMG / f"cover_fg_{mb:g}.png", optimize=True)
    ft, fh = y0 / pxmm - mb, (y1 - y0) / pxmm
    return (f"<img class='ph' src='img/{THEME}/cover_bg_{mb:g}.jpg' style='left:-{mb:g}mm;top:-{mb:g}mm;"
            f"width:{pw:g}mm;height:{ph:g}mm' alt=''>",
            f"<img class='ph' src='img/{THEME}/cover_fg_{mb:g}.png' style='left:-{mb:g}mm;top:{ft:.3f}mm;"
            f"width:{pw:g}mm;height:{fh:.3f}mm;object-fit:fill' alt=''>")


def add(name, bg, inner):
    pages.append((name, bg, inner))


# 1 · cover
COVER_BG, COVER_FG = cover_layers()
oc_h, oc_where = CV["on_cover"]
base_y = CV["base"]
sc = ",".join(str(v) for v in CV["scrim"])
add("cover", PAPER, "".join([
    COVER_BG,
    Tx(f"{T['edition']} &nbsp;·&nbsp; MMXXVI", 14, 13.4, "folio", extra=f"color:{CV['head']}"),
    logo(105, 10.6, 34, "cover", anchor="center"),
    Tx("NAIRAFLORE.COM", 196, 13.4, "folio", extra=f"color:{CV['head']};transform:translateX(-100%)"),
    rule(14, 23, 182, CV["head"], 0.35),
    Tx("THE DEMI-FINE JEWELLERY CATALOGUE", 105, 27.5, "eyebrow center", extra=f"color:{CV['head']}"),
    f"<svg class='abs' style='left:0;top:0;width:210mm;height:297mm' viewBox='0 0 210 297'>"
    f"<text x='12' y='{base_y}' font-family=\"Velista\" font-size='62' textLength='186' lengthAdjust='spacing' fill='{CV['mast']}'>PETITE</text></svg>",
    COVER_FG,
    f"<div class='abs' style='left:-{SB:g}mm;top:178mm;width:{210 + 2 * SB:g}mm;height:{297 + SB - 178:g}mm;background:linear-gradient(to bottom,"
    f"rgba({sc},0) 0%,rgba({sc},{CV['scrim_a'] * 0.75:.2f}) 38%,rgba({sc},{CV['scrim_a']}) 70%,rgba({sc},{CV['scrim_a']}) 100%)'></div>",
    Tx(f"<span class='it'>{CV['tagline']}</span>", 14, 214, "h3", extra=f"color:{CV['tag']}"),
    rule(14, 231, 182, CV["lines"], 0.35),
    Tx(f"<span class='label' style='color:{CV['label']}'>THE CAMP</span><br>{CV['camp']}", 14, 236, "coverline", w=70,
       extra=f"color:{CV['lines']}"),
    Tx(f"<span class='label' style='color:{CV['label']}'>THE COLLECTION</span><br>{N_ALL} pieces in stock,<br>from {inr(min(PRICES))}",
       92, 236, "coverline", w=50, extra=f"color:{CV['lines']}"),
    Tx(f"<span class='label' style='color:{CV['label']}'>ON THE COVER</span><br>{LIB[oc_h]['title']}, {price(oc_h)}"
       f"<br>{oc_where}", 196, 236, "coverline", w=62, extra=f"color:{CV['lines']};transform:translateX(-100%);text-align:right"),
]))

# the price list is laid out first so the About page and the index can quote its page numbers
FAMS = [("Earrings", "EARRINGS"), ("Ring", "RINGS"), ("Necklace", "NECKLACES"), ("Bracelet", "BRACELETS")]
ITEMS = {t: by_type(t) for t, _ in FAMS}
CAP = {"Earrings": 14, "Ring": 12, "Necklace": 7, "Bracelet": 11}       # cards on each family's opening page
CONT = 16                                                              # cards on a continuation page
plan, n = {}, 7
for t, _ in FAMS:
    hs = ITEMS[t]; first, rest = hs[:CAP[t]], hs[CAP[t]:]
    chunks = [first] + [rest[i:i + CONT] for i in range(0, len(rest), CONT)]
    plan[t] = [(n + k, ch) for k, ch in enumerate(chunks)]
    n += len(chunks)
PAGE_OF = {h: pg for t in plan for pg, ch in plan[t] for h in ch}
LAST_LIST, INDEX_PAGE = n - 1, n


def span(t):
    a, b = plan[t][0][0], plan[t][-1][0]
    return f"page {a:02d}" if a == b else f"pages {a:02d} to {b:02d}"


# 2 · about
counts = {t: len(ITEMS[t]) for t, _ in FAMS}
FAMILY = [("Earrings", "EARRINGS", "pearl-point-studs"), ("Ring", "RINGS", "chevron-whisper-ring"),
          ("Necklace", "NECKLACES", "heartline-paperclip-necklace"), ("Bracelet", "BRACELETS", "prism-riviere-bracelet")]
fam = []
for i, (t, label, h) in enumerate(FAMILY):
    x = 14 + i * (cw_fam := (182 - 3 * 5) / 4 + 5)
    fx, fy, z = FOCUS.get(h, DEF_FOCUS)
    fam.append(photo(LIB[h]["grid"], x, 177, cw_fam - 5, 58, fx, fy, z, key=f"fam_{h}"))
    fam.append(Tx(f"<span class='num-big'>{counts[t]}</span><span class='label'>{label}</span>", x, 238.5, "stat"))
n_dry = sum(not p["waterproof"] for p in LIB.values()); n_wp = N_ALL - n_dry
n_hypo = sum(p["hypoallergenic"] for p in LIB.values())
ab_spec, ab_cap = T["about"]
add("about", PAPER, "".join([
    Tx("ABOUT NAIRA", 14, 16, "eyebrow"),
    Tx("<span class='disp'>HERE YOUR STORY IS<br>HAND-STITCHED</span><br><span class='it'>into every thread.</span>", 14, 24, "h2", w=110),
    Tx("Naira is an Indian couture house: soft tailoring, pressed flowers and the long quiet of an Indian afternoon. "
       "Every outfit is hand-finished and made to measure in our atelier, one at a time.", 14, 56, "body", w=102),
    Tx("Naira Petite is the house’s demi-fine jewellery. The same soul in a smaller object: pieces made to be worn "
       "every day, light enough to forget you have them on, and finished to keep their colour.", 14, 76.5, "body", w=102),
    Tx("[ 18k gold coated &nbsp;·&nbsp; rhodium coated ]", 14, 99, "matline"),
    slot(ab_spec, 126, 16, 70, 88, "about"),
    Tx(ab_cap, 126, 106.5, "caption"),
    rule(14, 117, 182),
    Tx("THE PETITE PROMISE", 14, 122, "eyebrow"),
    Tx("<span class='label'>PVD COATED</span><br>18k gold or rhodium bonded to the metal in a vacuum: far harder than plating, "
       "and anti-tarnish. True of every piece in these pages.", 14, 130, "small", w=56),
    Tx(f"<span class='label'>WATERPROOF</span><br>Shower, swim, sweat. True of {n_wp} pieces; the {words(n_dry)} that would "
       f"rather stay dry say <b>keep dry</b> in the price list.", 77, 130, "small", w=56),
    Tx(f"<span class='label'>HYPOALLERGENIC</span><br>Gentle on sensitive ears, wrists and fingers. Listed as hypoallergenic on "
       f"{n_hypo} pieces; ask us about any other.", 140, 130, "small", w=56),
    Tx("Sizes, lengths and stones for every piece are on its page at nairaflore.com. Rings that come in sizes are US sizes; "
       "the size guide is on page " + f"{plan['Ring'][-1][0]:02d}.", 14, 154, "fine", w=182),
    rule(14, 164, 182),
    Tx("THE PETITE COLLECTION", 14, 169, "eyebrow"),
    "".join(fam),
    Tx(f"{N_ALL} pieces in stock as this catalogue goes out, from {inr(min(PRICES))} to {inr(max(PRICES))}. "
       f"The {T['name']} camp follows on pages 03 to 06, the price list runs from page 07 to page {LAST_LIST:02d}, "
       f"and every piece is indexed on page {INDEX_PAGE:02d}.", 14, 255, "small", w=160),
    folio(2),
]))

# 3 · camp I — the camp itself (tall on-model hero + two still lifes)
c1 = T["ch1"]
add("camp1", PAPER, "".join([
    slot(c1["hero"], 0, 0, 118, 297, "c1hero"),
    Tx(f"{T['name'].upper()} &nbsp;·&nbsp; I", 126, 16, "eyebrow"),
    Tx(f"<span class='disp'>{c1['title']}</span>", 126, 23, "h1"),
    Tx(f"<span class='it'>{c1['line']}</span>", 126, 47.5, "h3"),
    Tx(c1["body"], 126, 59, "body", w=70),
    slot(c1["a"], 126, 92, 70, 74, "c1a"),
    slot(c1["b"], 126, 170, 70, 74, "c1b"),
    piece_list(c1["pieces"], 126, 251, 70),
    folio(3, left="NAIRA PETITE &nbsp;·&nbsp; MMXXVI", lx=126),
]))

# 4 · camp II — up close, on the camp colour
c2 = T["ch2"]
add("camp2", GROUND, "".join([
    Tx(f"{T['name'].upper()} &nbsp;·&nbsp; II", 14, 16, "eyebrow", extra=f"color:{T['on_ground']}"),
    Tx(f"<span class='disp'>{c2['title']}</span>", 14, 22, "h1 big", extra=f"color:{T['on_ground']}"),
    Tx(f"<span class='it'>{c2['line']}</span>", 14, 41, "h3", extra=f"color:{T['on_ground']}"),
    Tx(c2["body"], 118, 22.5, "body", w=78, extra=f"color:{T['on_ground']}"),
    slot(c2["hero"], 14, 56, 120, 150, "c2hero"),
    slot(c2["a"], 140, 56, 56, 72, "c2a"),
    slot(c2["b"], 140, 134, 56, 72, "c2b"),
    slot(c2["c"], 14, 212, 57, 66, "c2c"),
    slot(c2["d"], 77, 212, 57, 66, "c2d"),
    piece_list(c2["pieces"], 140, 213.5, 56, T["on_ground"], T["on_ground"]),
    folio(4, color=T["on_ground"]),
]))

# 5 · camp III — the still lifes
c3 = T["ch3"]
add("camp3", PAPER, "".join([
    Tx(f"{T['name'].upper()} &nbsp;·&nbsp; III", 14, 16, "eyebrow"),
    Tx(f"<span class='disp'>{c3['title']}</span>", 14, 22, "h1 big"),
    Tx(f"<span class='it'>{c3['line']}</span>", 14, 41, "h3"),
    Tx(c3["body"], 118, 22.5, "body", w=78),
    slot(c3["t1"], 14, 56, 58, 118, "c3a"),
    slot(c3["t2"], 76, 56, 58, 118, "c3b"),
    slot(c3["t3"], 138, 56, 58, 118, "c3c"),
    slot(c3["wide"], 14, 180, 120, 98, "c3d"),
    piece_list(c3["pieces"], 140, 181.5, 56),
    Tx(c3["note"], 140, 249, "fine", w=56),
    folio(5),
]))

# 6 · camp IV — one still life, full bleed
c4 = T["ch4"]
on4 = PAPER if c4["light"] else INK
sub4 = "#E9DED6" if c4["light"] else INK_SOFT
inset_y = 30 if c4["inset_at"] == "top" else c4.get("inset_y", 188)
inset_h = c4.get("inset_h", 80)
s4 = ",".join(str(v) for v in T["scrim4"])
add("camp4", GROUND, "".join([
    slot(c4["hero"], 0, 0, 210, 297, "c4hero"),
    Tx(f"{T['name'].upper()} &nbsp;·&nbsp; IV", 14, 16, "eyebrow", extra=f"color:{on4}"),
    Tx(f"<span class='disp'>{c4['title']}</span>", 14, 22, "h1 big", extra=f"color:{on4}"),
    Tx(f"<span class='it'>{c4['line']}</span>", 14, 41, "h3", extra=f"color:{on4}"),
    f"<div class='abs' style='left:-{SB:g}mm;top:196mm;width:{210 + 2 * SB:g}mm;height:{297 + SB - 196:g}mm;background:linear-gradient(to bottom,"
    f"rgba({s4},0) 0%,rgba({s4},0.55) 40%,rgba({s4},0.72) 100%)'></div>",
    slot(c4["inset"], 196 - 64 * inset_h / 80, inset_y, 64 * inset_h / 80, inset_h, "c4a", extra=f"outline:1.2mm solid {PAPER};"),
    Tx(c4["body"], 14, 236, "body", w=100, extra=f"color:{sub4}"),
    piece_list(c4["pieces"], 14, 258, 100, on4, sub4),
    folio(6, color=sub4),
]))


# ---- the price list -------------------------------------------------------------------------
cw4 = (182 - 3 * 5) / 4          # 41.75 mm
cw3 = (182 - 2 * 6) / 3          # 56.67 mm


def grid(items, cols, cw, ih, x0, y0, rowh, slots, extra_cells=()):
    free = [s for s in range(slots) if s not in set(extra_cells)]
    assert len(items) <= len(free), (len(items), len(free))
    gap = (182 - cols * cw) / (cols - 1)
    out = []
    for h, s in zip(items, free):
        r, c = divmod(s, cols)
        out.append(card(h, x0 + c * (cw + gap), y0 + r * rowh, cw, ih, rowh - ih - 4.2))
    return "".join(out)


def header(no, title, line, meta, meta_left=False, dy=0):
    return "".join([Tx(f"THE COLLECTION &nbsp;·&nbsp; {no:02d}", 14, 16 + dy, "eyebrow"),
                    Tx(f"<span class='disp'>{title}</span>", 14, 22 + dy, "h1 big"),
                    Tx(f"<span class='it'>{line}</span>", 14, 41 + dy, "h3"),
                    Tx(meta, 14, 53 + dy, "meta") if meta_left else Tx(meta, 196, 44.5 + dy, "meta", extra="transform:translateX(-100%)")])


def fam_meta(t):
    hs = ITEMS[t]
    return f"{len(hs)} pieces &nbsp;·&nbsp; {inr(min(LIB[h]['price'] for h in hs))} to {inr(max(LIB[h]['price'] for h in hs))}"


LINES = {"Earrings": (f"{words(len(ITEMS['Earrings']))} ways to frame a face.", "hoops, drops and studs."),
         "Ring": ("for the hand you talk with.", "stacked, or worn alone."),
         "Necklace": ("close to the collarbone.", "chains to layer, or wear alone."),
         "Bracelet": ("a wrist, quietly.", "cuffs, tennis lines and pearls.")}


def continuation(t, no, title, pg, items, extra_cells=(), extra=""):
    first = plan[t][0][0]
    return "".join([header(no, title, LINES[t][1], f"continued from page {first:02d}"),
                    grid(items, 4, cw4, 37, 14, 56, 57.5, 16, extra_cells), extra, folio(pg)])


# earrings: opening page (4 x 4, the feature photo spans two cells), then the rest
e_spec, e_cap = T["ear"]
pg, items = plan["Earrings"][0]
add("earrings", PAPER, "".join([
    header(1, "EARRINGS", LINES["Earrings"][0], fam_meta("Earrings")),
    slot(e_spec, 14 + 2 * (cw4 + 5), 56, 2 * cw4 + 5, 37 + 13, "earfeat"),
    Tx(e_cap, 14 + 2 * (cw4 + 5), 56 + 50 + 1.5, "caption-s", w=2 * cw4 + 5),
    grid(items, 4, cw4, 37, 14, 56, 57.5, 16, {2, 3}), folio(pg)]))
for pg, items in plan["Earrings"][1:]:
    add("earrings-cont", PAPER, continuation("Earrings", 1, "EARRINGS", pg, items))

# rings: hero band + 4 x 3, then the rest with the size guide in the last free cells
r_spec, r_cap = T["ring"]
pg, items = plan["Ring"][0]
add("rings", PAPER, "".join([
    slot(r_spec, 0, 0, 210, 66, "ringhero"),
    Tx(r_cap, 196, 68.5, "caption-s", extra="transform:translateX(-100%);text-align:right"),
    header(2, "RINGS", LINES["Ring"][0], fam_meta("Ring"), dy=60),
    grid(items, 4, cw4, 37, 14, 116, 56.5, 12), folio(pg)]))
fits = {f: [h for h in ITEMS["Ring"] if LIB[h]["fit"] == f] for f in ("sized", "fixed", "adjustable")}
assert sum(map(len, fits.values())) == len(ITEMS["Ring"])
for k, (pg, items) in enumerate(plan["Ring"][1:]):
    last = k == len(plan["Ring"]) - 2
    guide = ""
    if last:
        free0 = len(items)
        assert free0 <= 13, "the size guide needs the last three cells"
        gx, gy = 14 + (cw4 + 5), 56 + 3 * 57.5
        guide = Tx("<span class='label'>RING SIZES</span><br>"
                   f"{words(len(fits['sized'])).capitalize()} rings come in US sizes, shown beside the price. Inside diameter:<br>"
                   "<span class='sz'>US 5 · 15.7 mm</span><span class='sz'>US 6 · 16.5 mm</span><span class='sz'>US 7 · 17.3 mm</span>"
                   "<span class='sz'>US 8 · 18.1 mm</span><span class='sz'>US 9 · 18.9 mm</span><br>"
                   f"{words(len(fits['fixed'])).capitalize()} are made in one fixed size, also shown beside the price. "
                   f"The other {words(len(fits['adjustable']))} are adjustable and fit most fingers. "
                   "Not sure of your size? WhatsApp us and we will help you measure.",
                   gx, gy + 1, "small guide", w=3 * cw4 + 2 * 5)
    add("rings-cont", PAPER, continuation("Ring", 2, "RINGS", pg, items, {13, 14, 15} if last else (), guide))

# necklaces: 3 columns, the feature spans two rows in the first column; then the rest on the 4-column grid
n_spec, n_cap = T["neck"]
pg, items = plan["Necklace"][0]
add("necklaces", PAPER, "".join([
    header(3, "NECKLACES", LINES["Necklace"][0], fam_meta("Necklace")),
    slot(n_spec, 14, 56, cw3, 2 * 66 - 4 + 13, "neckfeat"),
    Tx(n_cap, 14, 56 + 2 * 66 - 4 + 13 + 1.5, "caption-s", w=cw3),
    grid(items, 3, cw3, 50, 14, 56, 70, 9, {0, 3}), folio(pg)]))
for pg, items in plan["Necklace"][1:]:
    add("necklaces-cont", PAPER, continuation("Necklace", 3, "NECKLACES", pg, items))

# bracelets: hero top right, 4 x 3 with the care note in the last cell; then the rest
b_spec, b_cap = T["brace"]
pg, items = plan["Bracelet"][0]
care = Tx("<span class='label'>CARE</span><br>Put perfume on before your jewellery, not after, and keep each piece in its box "
          "between wears. Pieces marked <b>keep dry</b> would rather stay out of the water.", 14 + 3 * (cw4 + 5), 94 + 2 * 57.5 + 1, "small", w=cw4)
add("bracelets", PAPER, "".join([
    slot(b_spec, 112, 14, 84, 70, "bracehero"),
    Tx(b_cap, 196, 86, "caption-s", extra="transform:translateX(-100%)"),
    header(4, "BRACELETS", LINES["Bracelet"][0], fam_meta("Bracelet"), meta_left=True),
    grid(items, 4, cw4, 37, 14, 94, 57.5, 12, {11}), care, folio(pg)]))
for pg, items in plan["Bracelet"][1:]:
    add("bracelets-cont", PAPER, continuation("Bracelet", 4, "BRACELETS", pg, items))
assert len(pages) == LAST_LIST, (len(pages), LAST_LIST)


FROM_BY = sorted({o for p in LIB.values() for o in p["from_by"]})


# ---- the index ------------------------------------------------------------------------------
def index_col(fams, x, y, w):
    out = []
    for t, label in fams:
        out.append(f"<div class='ix-h'><span>{label}</span><span>{len(ITEMS[t])} &nbsp;·&nbsp; {span(t)}</span></div>")
        for h in ITEMS[t]:
            out.append(f"<div class='ix'><span class='ix-n'>{LIB[h]['title']}{'' if LIB[h]['waterproof'] else ' <i>keep dry</i>'}</span>"
                       f"<span class='ix-p'>{price(h)}</span><span class='ix-g'>{PAGE_OF[h]:02d}</span></div>")
    return Tx("".join(out), x, y, "index", w=w)


add("index", PAPER, "".join([
    Tx("THE COLLECTION &nbsp;·&nbsp; INDEX", 14, 16, "eyebrow"),
    Tx("<span class='disp'>THE INDEX</span>", 14, 22, "h1 big"),
    Tx("<span class='it'>every piece, by family and price.</span>", 14, 41, "h3"),
    Tx(f"{N_ALL} pieces &nbsp;·&nbsp; prices on {AS_OF}", 196, 44.5, "meta", extra="transform:translateX(-100%)"),
    index_col(FAMS[:2], 14, 53, 86), index_col(FAMS[2:], 110, 53, 86),
    Tx("<span class='label'>KEY</span><br><i class='kd'>keep dry</i>&nbsp; would rather stay out of the water; every other piece is waterproof.<br>"
       + (f"from&nbsp; the lowest price, where it changes with the {' or '.join(FROM_BY)}.<br>" if FROM_BY else "")
       + "The last column is the page each piece is on.", 110, 262, "fine key", w=86),
    folio(INDEX_PAGE),
]))

# back cover
add("back", TINT, "".join([
    logo(105, 64, 64, "brand", anchor="center"),
    Tx("<span class='it'>Made to stay gold.</span>", 105, 88, "h3 center"),
    rule(80, 104, 50, INK, 0.3),
    Tx("<span class='label'>TO ORDER</span><br>Shop the whole collection at <b>nairaflore.com</b>.<br>"
       "Or WhatsApp us on <b>+91 95615 57935</b>,<br>Monday to Saturday, 10 am to 7 pm IST.", 105, 112, "small center-block", w=110),
    qr("https://nairaflore.com", 105 - 15, 146, 30),
    Tx("nairaflore.com", 105, 179, "fine center"),
    Tx("<span class='label'>CARE</span><br>Put perfume on before your jewellery, not after, and keep each piece in its box between "
       "wears. Pieces marked <b>keep dry</b> would rather stay out of the shower, the pool and the sea.", 105, 196, "small center-block", w=120),
    Tx(f"Prices in Indian rupees as listed on nairaflore.com on {AS_OF}, for the {N_ALL} pieces in stock that day. "
       "Pieces open for pre-order are not included. Photographs may be enlarged to show detail.", 105, 262, "fine center-block", w=150),
    Tx(FOLIO_LEFT, 105, 286.2, "folio center", extra=f"color:{MUTED}"),
]))


# Chromium rounds a PDF page to whole points. With bleed, round the page up instead, so the trim stays exactly
# 210 x 297 mm at (BLEED, BLEED) and render.py can set the boxes to the millimetre.
PAGE_W, PAGE_H = ((f"{math.ceil((210 + 2 * BLEED) * 72 / 25.4)}pt", f"{math.ceil((297 + 2 * BLEED) * 72 / 25.4)}pt")
                  if BLEED else ("210mm", "297mm"))


# ---- html ----------------------------------------------------------------------------------
CSS = f"""
@page {{ size: {PAGE_W} {PAGE_H}; margin: 0 }}
* {{ margin:0; padding:0; box-sizing:border-box }}
html, body {{ background:#fff }}
body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact }}
.trim {{ position:absolute; left:{BLEED}mm; top:{BLEED}mm; width:210mm; height:297mm }}
.page {{ position:relative; width:{PAGE_W}; height:{PAGE_H}; overflow:hidden; page-break-after:always; break-after:page; color:{INK} }}
.page:last-child {{ page-break-after:auto; break-after:auto }}
.abs {{ position:absolute }}
img.ph {{ position:absolute; display:block; object-fit:cover }}
.center {{ transform:translateX(-50%); text-align:center; white-space:nowrap }}
.center-block {{ transform:translateX(-50%); text-align:center }}
.disp {{ font-family:'Rupee','Velista',Georgia,serif; font-weight:400; letter-spacing:.012em }}
.it {{ font-family:'Rupee','CormI',Georgia,serif; font-style:italic; font-weight:400 }}
.eyebrow {{ font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:6.6pt; letter-spacing:.26em; color:{INK_SOFT}; white-space:nowrap }}
.folio {{ font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:5.9pt; letter-spacing:.24em; white-space:nowrap }}
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
.matline {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:8.6pt; letter-spacing:.12em; color:{T['matline']}; white-space:nowrap }}
.coverline {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:8.6pt; line-height:1.5 }}
.caption {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:11.5pt; color:{INK_SOFT}; white-space:nowrap }}
.caption-s {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:9.6pt; color:{INK_SOFT}; white-space:nowrap }}
.meta {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:7.6pt; letter-spacing:.06em; color:{INK_SOFT}; white-space:nowrap }}
.stat {{ display:flex; align-items:baseline; gap:2.2mm; white-space:nowrap }}
.num-big {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:26pt; line-height:1; color:{INK} }}
.ptext {{ display:flex; flex-direction:column; overflow:hidden }}
.pname {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:8.2pt; line-height:1.18; color:{INK} }}
.pmat {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:6.5pt; line-height:1.25; color:{MUTED}; margin-top:0.5mm }}
.pmat b {{ font-weight:500; color:{T['matline']} }}
.pprice {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:8.6pt; letter-spacing:.02em; color:{INK}; margin-top:auto; white-space:nowrap }}
.pext {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:6.5pt; letter-spacing:.03em; color:{MUTED}; margin-left:1.8mm }}
.plist {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:8.1pt; line-height:1.4 }}
.plist .pl {{ display:flex; justify-content:space-between; gap:3mm; padding:1.25mm 0; border-top:0.25pt solid currentColor }}
.plist .pl:last-child {{ border-bottom:0.25pt solid currentColor }}
.plist .pl-p {{ font-weight:400; white-space:nowrap }}
.guide {{ line-height:1.55 }}
.guide .sz {{ display:inline-block; margin-right:3.2mm; font-weight:400; color:{INK}; white-space:nowrap; font-variant-numeric:tabular-nums }}
.index {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:7.2pt; line-height:1.3; color:{INK_SOFT} }}
.ix-h {{ display:flex; justify-content:space-between; font-weight:500; font-size:6.6pt; letter-spacing:.22em; color:{INK}; padding:3.2mm 0 1.2mm; border-bottom:0.4pt solid {INK} }}
.ix-h:first-child {{ padding-top:0 }}
.ix-h span:last-child {{ letter-spacing:.08em; font-weight:400; color:{MUTED} }}
.ix {{ display:grid; grid-template-columns:1fr auto 7mm; gap:2mm; align-items:baseline; padding:0.34mm 0; border-bottom:0.25pt solid rgba(28,28,28,.14) }}
.key i.kd, .ix-n i {{ font-style:normal; font-size:6pt; letter-spacing:.06em; color:{T['matline']}; margin-left:1mm }}
.key i.kd {{ margin-left:0 }}
.ix-p {{ font-weight:400; color:{INK}; white-space:nowrap; font-variant-numeric:tabular-nums }}
.ix-g {{ text-align:right; color:{MUTED}; font-variant-numeric:tabular-nums }}
"""


def html():
    body = "".join(f"<section class='page' id='p{i + 1:02d}-{name}' style='background:{bg}'><div class='trim'>{inner}</div></section>"
                   for i, (name, bg, inner) in enumerate(pages))
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>NAIRA PETITE · The {T['name']} Edition</title>"
            f"<style>{base.fonts_css()}{CSS}</style></head><body>{body}</body></html>")


if __name__ == "__main__":
    out = ROOT / (f"catalogue-{THEME}-bleed{BLEED:g}.html" if BLEED else f"catalogue-{THEME}.html")
    out.write_text(html())
    print(THEME, "pages", len(pages), "| price list 07 to", f"{LAST_LIST:02d}", "| index", INDEX_PAGE,
          "| per family:", {t: [(pg, len(ch)) for pg, ch in plan[t]] for t, _ in FAMS}, "->", out.name)
    if len(pages) % 4:
        print("WARNING: page count is not a multiple of 4")
