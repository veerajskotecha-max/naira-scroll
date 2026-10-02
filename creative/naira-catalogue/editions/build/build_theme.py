"""
NAIRA PETITE — The Catalogue, one camp per edition (A4, 10 pages).

The same ten pages as Volume One (cover · about · four camp pages · four price-list pages), but every
photograph in an edition comes from ONE of the Colour Camps shot in Higgsfield: Apricot, Lilac or Sage.
THEME=apricot|lilac|sage picks the edition; BLEED=3 builds the print master.

Images are cropped here from the Higgsfield originals and Shopify photos to the exact placed size at
<= 300 dpi (never upscaled), so the PDF carries print-resolution JPEGs and nothing heavier.
"""
import json, os, sys
from pathlib import Path
from PIL import Image
import segno

C = Path(__file__).resolve().parent
SCR = C.parent
CAMP = SCR / "camp"
RAWDIR = SCR / "themes" / "raw"
sys.path.insert(0, str(CAMP / "studio"))
import base  # fonts + logo vector + palette

THEME = os.environ.get("THEME", "apricot")
BLEED = float(os.environ.get("BLEED", "0"))   # mm; 3 or 5 for the print masters
SB = max(BLEED, 3.0)                          # full-bleed art always covers at least 3 mm
IMG = C / "img_theme" / THEME; IMG.mkdir(parents=True, exist_ok=True)
LIB = json.load(open(CAMP / "library.json"))
RAW = json.load(open(C / "raw_index.json"))

INK, INK_SOFT, MUTED = "#1C1C1C", "#3D3530", "#6B615A"
CREAM = "#F4F0E8"


# ---- the three camps ----------------------------------------------------------------------------
# Each slot is (image id, fx, fy, zoom): the crop centre as a fraction of the original and a zoom >= 1.
THEMES = {
    "apricot": dict(
        name="Apricot", edition="THE APRICOT EDITION",
        paper="#FCF5EF", ground="#F0C9AC", deep="#A9532B", tint="#F7E1D2", on_ground="#4A2B1D",
        matline="#A9532B", scrim4=(247, 225, 209),
        cover=dict(src="cffca2c2", z=1.0, fx=0.5, fy=0.5, mast="#A9532B", base=100, head="#7A3D20", lines="#4A2A1B",
                   label="#2E180E", roi=(54, 52, 216, 112), box=(56, 64, 210, 112), mode="gold",
                   scrim=(246, 222, 205), scrim_a=0.86, tag="#8E4322",
                   camp="Apricot: raw silk, a halved<br>apricot, an almond and gold.",
                   on_cover=("brushed-gold-huggies", "Up close, page 04"),
                   tagline="ripe silk, warm gold."),
        about=(("6ff006c9", 0.5, 0.42, 1.0), "Heartline Paperclip Necklace, worn."),
        ch1=dict(hero=("fb2e1f88", 0.57, 0.5, 1.0),
                 a=("b7e6edcb", 0.5, 0.46, 1.25), b=("73e4c71f", 0.52, 0.5, 1.35),
                 title="THE APRICOT<br>CAMP", line="silk the colour of the fruit.",
                 body="Raw silk the colour of the fruit, an apricot cut open, an almond from the same tree. Gold sits in "
                      "this colour the way it sits on skin: warm, and a little lit from within.",
                 pieces=["woven-gold-hoops", "ribbon-bow-earrings", "brushed-gold-huggies"]),
        ch2=dict(hero=("fe1b77ea", 0.5, 0.5, 1.0),
                 a=("b26afec3", 0.5, 0.5, 1.0), b=("81e92cbb", 0.55, 0.45, 1.0),
                 c=("772b1d01", 0.5, 0.55, 1.0), d=("5c8e4c48", 0.45, 0.45, 1.0),
                 title="UP CLOSE", line="every strand, every stone.",
                 body="Close enough to count: the plaited wires of the hoops, the brushing on the huggies, four stones in "
                      "each bow, two hearts on the bracelet and nine on the necklace.",
                 pieces=["heartline-paperclip-necklace", "woven-gold-hoops", "ribbon-bow-earrings",
                         "ribbon-bead-bracelet", "brushed-gold-huggies"]),
        ch3=dict(t1=("9f10068d", 0.55, 0.5, 1.0), t2=("8e6cf897", 0.5, 0.47, 1.0), t3=("a4b59b99", 0.55, 0.45, 1.0),
                 wide=("3c740431", 0.5, 0.55, 1.0),
                 title="ON RAW SILK", line="slubbed, warm, unhurried.",
                 body="Dupioni silk with its slubs left in and the light kept low. Each piece laid down on its own, the "
                      "way you would lay them out before choosing.",
                 note="Every piece in these pages is in stock and on nairaflore.com.",
                 pieces=["brushed-gold-huggies", "ribbon-bow-earrings", "ribbon-bead-bracelet", "heartline-paperclip-necklace"]),
        ch4=dict(hero=("68b811fc", 0.5, 1.0, 1.0), inset=("d9e5a99a", 0.45, 0.5, 1.0), inset_at="bottom", inset_y=197, inset_h=74,
                 title="STONE FRUIT", line="where the stone was.", light=False,
                 body="One hoop resting in the hollow where the stone was, the other on the silk beside it. Plaited from "
                      "fine gold wires, light enough for every day.",
                 pieces=["woven-gold-hoops", "ribbon-bead-bracelet"]),
        ear=(("91ead2c7", 0.45, 0.47, 1.0), "Ribbon Bow Earrings, beside an almond."),
        ring=(("c8ea8095", 0.55, 0.52, 1.0), "Woven Gold Hoops, with the fruit."),
        neck=(("e13c241b", 0.5, 0.45, 1.0), "Heartline Paperclip Necklace, worn."),
        brace=(("cbe2406e", 0.5, 0.45, 1.0), "Ribbon Bead Bracelet, worn."),
    ),
    "lilac": dict(
        name="Lilac", edition="THE LILAC EDITION",
        paper="#F8F5F8", ground="#C9B6CB", deep="#5E4A78", tint="#ECE4EF", on_ground="#2E2338",
        matline="#5E4A78", scrim4=(238, 230, 241),
        cover=dict(src="e948577d", z=1.0, fx=0.5, fy=0.5, mast="#4E3C66", base=100, head="#3B2D4E", lines="#33264A",
                   label="#1E1529", roi=(70, 52, 160, 112), box=(72, 70, 158, 112), mode="silver",
                   scrim=(236, 228, 240), scrim_a=0.86, tag="#4E3C66",
                   camp="Lilac: deckled paper, a sprig<br>of lavender, linen and silver.",
                   on_cover=("pearl-blossom-earrings", "Up close, page 04"),
                   tagline="lilac paper, cool silver."),
        about=(("e215782d", 0.5, 0.45, 1.0), "Serpentine Whisper Chain, worn."),
        ch1=dict(hero=("49b4c6c3", 0.52, 0.5, 1.0),
                 a=("7ee84742", 0.5, 0.45, 1.2), b=("33950938", 0.5, 0.52, 1.15),
                 title="THE LILAC<br>CAMP", line="deckled paper, a sprig of lavender.",
                 body="Lilac paper torn by hand, lavender laid across it and linen in the same soft colour. This is the "
                      "camp for silver: rhodium-coated pieces that stay cool and bright.",
                 pieces=["silver-drop-earrings", "pearl-blossom-earrings", "serpentine-whisper-chain-silver"]),
        ch2=dict(hero=("240a53f1", 0.5, 0.5, 1.0),
                 a=("402a29f5", 0.5, 0.5, 1.0), b=("3a7252fd", 0.45, 0.5, 1.0),
                 c=("b12b4b97", 0.4, 0.55, 1.0), d=("8dae0328", 0.5, 0.55, 1.15),
                 title="UP CLOSE", line="every stone in its setting.",
                 body="Close enough to count: three pastel colours in turn, a pearl held low in a circle of stones, "
                      "baguettes running round an open oval, one cushion stone in a four-claw basket.",
                 pieces=["pearl-blossom-earrings", "prism-riviere-bracelet", "silver-drop-earrings",
                         "serpentine-whisper-chain-silver"]),
        ch3=dict(t1=("a1f2270b", 0.5, 0.45, 1.0), t2=("48c15520", 0.45, 0.47, 1.0), t3=("ce24a0a9", 0.5, 0.45, 1.0),
                 wide=("e47cca3a", 0.5, 0.5, 1.0),
                 title="ON PAPER", line="deckled, and torn by hand.",
                 body="Handmade paper with its edges left rough, a sprig of lavender and a slant of afternoon light. "
                      "Each piece laid down on its own.",
                 note="Every piece in these pages is in stock and on nairaflore.com.",
                 pieces=["pearl-blossom-earrings", "silver-drop-earrings", "serpentine-whisper-chain-silver",
                         "prism-riviere-bracelet"]),
        ch4=dict(hero=("2e1c28f6", 0.5, 1.0, 1.0), inset=("02048561", 0.6, 0.5, 1.0), inset_at="bottom",
                 title="LAVENDER", line="the camp’s one note of colour.", light=False,
                 body="Pink, aqua and yellow stones in turn, each in a halo of tiny clear ones. The Prism Rivière, with a "
                      "sprig of lavender laid across it.",
                 pieces=["prism-riviere-bracelet"]),
        ear=(("03c53bd1", 0.5, 0.5, 1.0), "Trio Oval Drop Earrings, from above."),
        ring=(("VIII-L4", 0.55, 0.42, 1.0), "Halo Curve Ring, in lilac light."),
        neck=(("50baf608", 0.5, 0.5, 1.0), "Serpentine Whisper Chain, on deckled paper."),
        brace=(("4a0c8a79", 0.55, 0.5, 1.0), "Prism Rivière Bracelet, worn."),
    ),
    "sage": dict(
        name="Sage", edition="THE SAGE EDITION",
        paper="#F6F6F1", ground="#AFBFA9", deep="#3F5A4C", tint="#E3EAE1", on_ground="#1F2E25",
        matline="#3F5A4C", scrim4=(231, 238, 232),
        cover=dict(src="960a8c9a", z=1.0, fx=0.5, fy=0.5, mast="#F2EFE6", base=104, head="#F2EFE6", lines="#EEF1EA",
                   label="#FFFFFF", roi=(14, 56, 216, 116), box=(16, 84, 210, 116), mode="gold",
                   scrim=(38, 52, 43), scrim_a=0.62, tag="#F2EFE6",
                   camp="Sage: a celadon dish, a sage<br>leaf, linen and gold.",
                   on_cover=("granule-dome-ring", "Up close, page 04"),
                   tagline="celadon, a leaf, gold."),
        about=(("9a343bc1", 0.5, 0.48, 1.0), "Toggle Link Chain, worn."),
        ch1=dict(hero=("25f570f8", 0.42, 0.5, 1.0),
                 a=("5eec97d0", 0.5, 0.5, 1.3), b=("2643190d", 0.5, 0.5, 1.0),
                 title="THE SAGE<br>CAMP", line="a celadon dish, a sage leaf.",
                 body="A dish glazed the green of a sage leaf and crazed with fine lines, and linen in the same quiet "
                      "colour. Against green, gold looks its warmest.",
                 pieces=["verdant-circlet-studs", "chevron-whisper-ring", "toggle-link-chain"]),
        ch2=dict(hero=("a9edf299", 0.5, 0.5, 1.0),
                 a=("345b8934", 0.5, 0.5, 1.0), b=("ea62d7e3", 0.5, 0.5, 1.0),
                 c=("100c8b2b", 0.5, 0.5, 1.0), d=("ec7c57a2", 0.5, 0.5, 1.0),
                 title="UP CLOSE", line="granule by granule.",
                 body="Close enough to see light through the granule dome, the plain rail between two rails of stones, "
                      "the sailor clasp and its bar of stones, a puffed gold heart at the toggle.",
                 pieces=["heartbead-bracelet", "verdant-circlet-studs", "chevron-whisper-ring", "toggle-link-chain",
                         "granule-dome-ring"]),
        ch3=dict(t1=("d0ecca0e", 0.5, 0.48, 1.0), t2=("0ac3824a", 0.5, 0.45, 1.0), t3=("a2b23756", 0.5, 0.45, 1.0),
                 wide=("4dd9a8ca", 0.5, 0.5, 1.0),
                 title="ON CELADON", line="crazed glaze, a cool green.",
                 body="Glaze crazed into a fine net of lines, a sage leaf from the garden, and each piece set down in the "
                      "hollow of the dish.",
                 note="Every piece in these pages is in stock and on nairaflore.com.",
                 pieces=["granule-dome-ring", "verdant-circlet-studs", "chevron-whisper-ring", "heartbead-bracelet"]),
        ch4=dict(hero=("04b753a1", 0.5, 0.5, 1.0), inset=("7d32128c", 0.55, 0.45, 1.0), inset_at="bottom",
                 title="IN THE DISH", line="a heart on a toggle, and a leaf.", light=False,
                 body="Mirror-polished silver beads closed by a gold toggle, with one puffed gold heart. Laid in the "
                      "hollow of the dish, and worn.",
                 pieces=["heartbead-bracelet"]),
        ear=(("24152112", 0.5, 0.5, 1.0), "Verdant Circlet Studs, on celadon."),
        ring=(("7654725d", 0.5, 0.55, 1.0), "Chevron Whisper Ring, up close."),
        neck=(("43ef3c83", 0.5, 0.5, 1.0), "Toggle Link Chain, up close."),
        brace=(("c8196fcf", 0.55, 0.5, 1.0), "Heartbead Bracelet, worn."),
    ),
}
T = THEMES[THEME]
PAPER, GROUND, DEEP, TINT = T["paper"], T["ground"], T["deep"], T["tint"]


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
    return f"img_theme/{THEME}/{name}"


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


def inr(n):
    return base.inr(n)


FOLIO_LEFT = f"NAIRA PETITE &nbsp;·&nbsp; {T['edition']} &nbsp;·&nbsp; MMXXVI"


def folio(n, color=MUTED, left=FOLIO_LEFT, lx=14):
    return (Tx(left, lx, 286.2, "folio", extra=f"color:{color}") +
            Tx(f"{n:02d}", 196, 286.2, "folio", extra=f"color:{color};transform:translateX(-100%)"))


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
FOCUS = {}
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
            Tx(p["title"], x, y + ih + 2.6, "pname", w=w) +
            Tx(material(h), x, y + ih + 6.6, "pmat", w=w) +
            Tx(inr(p["price"]), x, y + ih + 10.4, "pprice", w=w))


def by_type(t):
    hs = [h for h, p in LIB.items() if p["type"] == t]
    return sorted(hs, key=lambda h: (LIB[h]["price"], LIB[h]["title"]))


def piece_list(items, x, y, w, color=INK, mcolor=MUTED):
    rows = []
    for h in items:
        p = LIB[h]
        rows.append(f"<div class='pl'><span>{p['title']}</span><span class='pl-p'>{inr(p['price'])}</span></div>")
    return Tx("".join(rows), x, y, "plist", w=w, extra=f"color:{color};--m:{mcolor}")


# ---- pages ----------------------------------------------------------------------------------
pages = []
CV = T["cover"]


def cover_layers():
    """The masthead sits behind the piece: one crop sized to the bleed gives the background, and the piece is laid back
    over the letters from the same pixels, cut out with a BiRefNet matte (themes/cut/<theme>_birefnet-general.png,
    made with rembg on the 3 mm crop) inside the masthead band. The crop covers at least a 3 mm bleed; for a wider
    bleed the matte is placed back in source pixels and cut to the wider crop, so the cut-out still registers."""
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
    m3 = Image.open(SCR / "themes" / "cut" / f"{THEME}_birefnet-general.png").convert("L")
    b3 = window(216 / 303)
    assert m3.size == (b3[2] - b3[0], b3[3] - b3[1]), (m3.size, b3)
    full = Image.new("L", (W, H), 0); full.paste(m3, (b3[0], b3[1]))
    matte = full.crop(bx)
    pxmm = c.width / pw
    y0 = max(int((CV["base"] - 50 + mb) * pxmm), 0); y1 = int((CV["base"] + 4 + mb) * pxmm)
    a = np.asarray(matte).astype(np.float32) / 255
    a[a < 0.06] = 0
    a = cv2.erode(a, np.ones((3, 3), np.uint8))                      # pull the edge 1 px inside the piece
    a = cv2.GaussianBlur(a, (0, 0), 0.7)
    alpha = (a[y0:y1] * 255).clip(0, 255).astype(np.uint8)
    rgb = np.asarray(c)[y0:y1]
    Image.fromarray(np.dstack([rgb, alpha])).save(IMG / f"cover_fg_{mb:g}.png", optimize=True)
    ft, fh = y0 / pxmm - mb, (y1 - y0) / pxmm
    return (f"<img class='ph' src='img_theme/{THEME}/cover_bg_{mb:g}.jpg' style='left:-{mb:g}mm;top:-{mb:g}mm;"
            f"width:{pw:g}mm;height:{ph:g}mm' alt=''>",
            f"<img class='ph' src='img_theme/{THEME}/cover_fg_{mb:g}.png' style='left:-{mb:g}mm;top:{ft:.3f}mm;"
            f"width:{pw:g}mm;height:{fh:.3f}mm;object-fit:fill' alt=''>")


COVER_BG, COVER_FG = cover_layers()
oc_h, oc_where = CV["on_cover"]
base_y = CV["base"]
sc = ",".join(str(v) for v in CV["scrim"])
pages.append(("cover", PAPER, "".join([
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
    Tx(f"<span class='label' style='color:{CV['label']}'>THE COLLECTION</span><br>{len(LIB)} pieces, from "
       f"{inr(min(p['price'] for p in LIB.values()))}", 92, 236, "coverline", w=50, extra=f"color:{CV['lines']}"),
    Tx(f"<span class='label' style='color:{CV['label']}'>ON THE COVER</span><br>{LIB[oc_h]['title']}, {inr(LIB[oc_h]['price'])}"
       f"<br>{oc_where}", 196, 236, "coverline", w=62, extra=f"color:{CV['lines']};transform:translateX(-100%);text-align:right"),
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
    fam.append(Tx(f"<span class='num-big'>{counts[t]}</span><span class='label'>{label}</span>", x, 238.5, "stat"))
ab_spec, ab_cap = T["about"]
pages.append(("about", PAPER, "".join([
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
    Tx("<span class='label'>HYPOALLERGENIC</span><br>Gentle on every ear, wrist and finger. True of every piece in these pages.", 14, 130, "small", w=56),
    Tx("<span class='label'>TARNISH-FREE</span><br>Made to stay gold, through work, travel and the wedding season.", 77, 130, "small", w=56),
    Tx("<span class='label'>WATERPROOF</span><br>Shower, swim, sweat. Daily wear and water are fine.", 140, 130, "small", w=56),
    Tx("All but three pieces are tarnish-free and waterproof as well. The Pearl Legacy Necklace, the Baroque Shell "
       "Bracelet and the Verdant Drop Earrings would rather be kept dry; they are marked in the price list.", 14, 152.5, "fine", w=182),
    rule(14, 164, 182),
    Tx("THE PETITE COLLECTION", 14, 169, "eyebrow"),
    "".join(fam),
    Tx(f"{len(LIB)} pieces in stock as this catalogue goes out, from {inr(min(prices))} to {inr(max(prices))}. "
       f"The {T['name']} camp follows on pages 03 to 06, and the full price list runs from page 07 to page 10.", 14, 255, "small", w=150),
    folio(2),
])))

# 3 · camp I — the camp itself (tall on-model hero + two still lifes)
c1 = T["ch1"]
pages.append(("camp1", PAPER, "".join([
    slot(c1["hero"], 0, 0, 118, 297, "c1hero"),
    Tx(f"{T['name'].upper()} &nbsp;·&nbsp; I", 126, 16, "eyebrow"),
    Tx(f"<span class='disp'>{c1['title']}</span>", 126, 23, "h1"),
    Tx(f"<span class='it'>{c1['line']}</span>", 126, 47.5, "h3"),
    Tx(c1["body"], 126, 59, "body", w=70),
    slot(c1["a"], 126, 92, 70, 74, "c1a"),
    slot(c1["b"], 126, 170, 70, 74, "c1b"),
    piece_list(c1["pieces"], 126, 251, 70),
    folio(3, left="NAIRA PETITE &nbsp;·&nbsp; MMXXVI", lx=126),
])))

# 4 · camp II — up close, on the camp colour
c2 = T["ch2"]
pages.append(("camp2", GROUND, "".join([
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
])))

# 5 · camp III — the still lifes
c3 = T["ch3"]
pages.append(("camp3", PAPER, "".join([
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
])))

# 6 · camp IV — one still life, full bleed
c4 = T["ch4"]
on4 = PAPER if c4["light"] else INK
sub4 = "#E9DED6" if c4["light"] else INK_SOFT
inset_y = 30 if c4["inset_at"] == "top" else c4.get("inset_y", 188)
inset_h = c4.get("inset_h", 80)
s4 = ",".join(str(v) for v in T["scrim4"])
pages.append(("camp4", GROUND, "".join([
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
])))


# 7 · earrings (4 x 4, feature tile spans two cells)
def grid_page(n, title, line, family, cols, cw, ih, x0, y0, rowh, slots, extra_cells, header_extra="", meta_left=False):
    hs = by_type(family)
    lo, hi = min(LIB[h]["price"] for h in hs), max(LIB[h]["price"] for h in hs)
    parts = [Tx(f"THE COLLECTION &nbsp;·&nbsp; {n - 6:02d}", 14, 16, "eyebrow"),
             Tx(f"<span class='disp'>{title}</span>", 14, 22, "h1 big"),
             Tx(f"<span class='it'>{line}</span>", 14, 41, "h3"),
             (Tx(f"{len(hs)} pieces &nbsp;·&nbsp; {inr(lo)} to {inr(hi)}", 14, 53, "meta") if meta_left else
              Tx(f"{len(hs)} pieces &nbsp;·&nbsp; {inr(lo)} to {inr(hi)}", 196, 44.5, "meta", extra="transform:translateX(-100%)")),
             header_extra]
    free = [s for s in range(slots) if s not in extra_cells]
    for h, s in zip(hs, free):
        r, c = divmod(s, cols)
        parts.append(card(h, x0 + c * (cw + (182 - cols * cw) / (cols - 1)), y0 + r * rowh, cw, ih))
    parts.append(folio(n))
    return "".join(parts)


cw4 = (182 - 3 * 5) / 4          # 41.75 mm
e_spec, e_cap = T["ear"]
ear_feature = (slot(e_spec, 14 + 2 * (cw4 + 5), 56, 2 * cw4 + 5, 37 + 13, "earfeat") +
               Tx(e_cap, 14 + 2 * (cw4 + 5), 56 + 50 + 1.5, "caption-s", w=2 * cw4 + 5))
pages.append(("earrings", PAPER, grid_page(7, "EARRINGS", "fourteen ways to frame a face.", "Earrings", 4, cw4, 37, 14, 56, 57.5, 16, {2, 3}, ear_feature)))

# 8 · rings (hero band + 4 x 3)
r_spec, r_cap = T["ring"]
pages.append(("rings", PAPER, "".join([
    slot(r_spec, 0, 0, 210, 74, "ringhero"),
    Tx(r_cap, 196, 76.5, "caption-s", extra="transform:translateX(-100%);text-align:right"),
]) + grid_page(8, "RINGS", "for the hand you talk with.", "Ring", 4, cw4, 37, 14, 118, 56.5, 12, set())
    .replace("top:16mm", "top:84mm", 1).replace("top:22mm", "top:90mm", 1).replace("top:41mm", "top:109mm", 1).replace("top:44.5mm", "top:112.5mm", 1)))

# 9 · necklaces (3 cols; feature spans two rows in col 1)
cw3 = (182 - 2 * 6) / 3          # 56.67 mm
n_spec, n_cap = T["neck"]
neck_feature = (slot(n_spec, 14, 56, cw3, 2 * 66 - 4 + 13, "neckfeat") +
                Tx(n_cap, 14, 56 + 2 * 66 - 4 + 13 + 1.5, "caption-s", w=cw3))
pages.append(("necklaces", PAPER, grid_page(9, "NECKLACES", "close to the collarbone.", "Necklace", 3, cw3, 50, 14, 56, 70, 9, {0, 3}, neck_feature)))

# 10 · bracelets + ordering
b_spec, b_cap = T["brace"]
order = "".join([
    f"<div class='abs' style='left:{-BLEED}mm;top:236mm;width:{210 + 2 * BLEED}mm;height:{61 + BLEED}mm;background:{TINT}'></div>",
    logo(14, 246, 38, "brand"),
    Tx("Made to stay gold.", 14, 258.5, "caption"),
    Tx("<span class='label'>TO ORDER</span><br>Shop the whole collection at <b>nairaflore.com</b>.<br>"
       "Or WhatsApp us on <b>+91 95615 57935</b>,<br>Monday to Saturday, 10 am to 7 pm IST.", 74, 245, "small", w=86),
    qr("https://nairaflore.com", 172, 244, 24),
    Tx("nairaflore.com", 184, 269.5, "fine", extra="transform:translateX(-50%);text-align:center"),
    Tx("Prices in Indian rupees as listed on nairaflore.com on 1 October 2026. Photographs may be enlarged to show detail.",
       14, 279.5, "fine", w=182),
])
brace_care = Tx("<span class='label'>CARE</span><br>Daily wear and water are fine. Keep each piece dry and in its box "
                "between wears, and put perfume on before your jewellery, not after.", 14 + 2 * (cw3 + 6), 160, "small", w=cw3)
pages.append(("bracelets", PAPER, "".join([
    slot(b_spec, 112, 14, 84, 70, "bracehero"),
    Tx(b_cap, 196, 86, "caption-s", extra="transform:translateX(-100%)"),
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
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>NAIRA PETITE · The {T['name']} Edition</title>"
            f"<style>{base.fonts_css()}{CORM_FULL}{CSS}</style></head><body>{body}</body></html>")


if __name__ == "__main__":
    out = C / ((f"catalogue-{THEME}-bleed.html" if BLEED == 3 else f"catalogue-{THEME}-bleed{BLEED:g}.html") if BLEED else f"catalogue-{THEME}.html")
    out.write_text(html())
    print(THEME, "pages", len(pages), "->", out.name)
