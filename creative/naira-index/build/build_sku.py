"""
NAIRA PETITE — The Petite Index: every jewellery listing (55) on one A4 sheet.

8 x 8 grid: four family title tiles (two cells wide) + 55 product tiles + one QR tile = 64 cells.
In-stock pieces first within each family (by price), then sold-out pieces, faded and tagged.
BLEED=3 makes the print master (216 x 303 mm, content offset by the bleed).
"""
import json, os, sys
from pathlib import Path
from PIL import Image
import segno

K = Path(__file__).resolve().parent
SCR = K.parent
CAMP = SCR / "camp"
sys.path.insert(0, str(CAMP / "studio"))
import base

BLEED = float(os.environ.get("BLEED", "0"))
IMG = K / "crops"; IMG.mkdir(exist_ok=True)
SKU = json.load(open(K / "skus.json"))
FOCUS = json.load(open(SCR / "catalogue" / "grid_focus.json"))

INK, INK_SOFT, MUTED, CORAL_DEEP = "#1C1C1C", "#3D3530", "#6B615A", "#B8604A"
PAGE = "#FCF8F3"

# image per listing: the catalogue's plinth choice for in-stock pieces, a chosen plinth shot for sold-out ones
CAT_ODD = {
    "heartbead-bracelet": "raw/heartbead-bracelet/shop1.jpg", "halo-curve-ring": "raw/halo-curve-ring/shop2.jpg",
    "woven-gold-hoops": "raw/woven-gold-hoops/shop1.jpg", "bold-nocturne-chain": "raw/bold-nocturne-chain/shop2.jpg",
    "prism-riviere-bracelet": "raw/prism-riviere-bracelet/shop3.jpg", "blush-cluster-ring": "raw/blush-cluster-ring/shop1.jpg",
    "star-point-band": "raw/star-point-band/shop2.jpg", "toggle-link-chain": "raw/toggle-link-chain/shop1.jpg",
    "verdant-eternity-band": "raw/verdant-eternity-band/shop3.jpg", "bold-nocturne-bracelet": "raw/bold-nocturne-bracelet/shop1.jpg",
    "pearl-legacy-necklace": "raw/pearl-legacy-necklace/shop1.jpg",
}
SOLD_PICK = {"dewdrop-bezel-necklace": 2, "lumiere-oval-necklace": 2, "lumiere-oval-bracelet": 0, "petite-pearl-chain": 4,
             "marquise-layering-set": 0, "clover-charm-necklace": 0, "triple-dawn-cuff": 0, "riviere-of-light-bracelet": 0,
             "pearl-reverie-bracelet": 0, "baguette-eclat-bracelet": 1, "first-light-set": 1, "cushion-halo-ring": 1,
             "blush-station-bracelet": 3, "baroque-bloom-cuff": 1, "molten-bloom-hoops": 0, "serpentine-whisper-chain": 1,
             "riviere-eternal-necklace": 0}
SKU_FOCUS = {}  # per-listing (fx, fy, zoom) overrides for this sheet
if (K / "sku_focus.json").exists():
    SKU_FOCUS = json.load(open(K / "sku_focus.json"))


def src(h):
    if h in SOLD_PICK:
        return K / "img" / f"{h}_{SOLD_PICK[h]}.jpg"
    if h == "pearl-drop-studs":
        return Path(json.load(open(SCR / "catalogue" / "raw_index.json"))["pearl-drop-studs:48dc"]["path"])
    if h in CAT_ODD:
        return CAMP / CAT_ODD[h]
    return CAMP / "shop" / h / "0.jpg"


def crop(path, w, h, fx, fy, zoom, key):
    out = IMG / f"{key}_{fx:g}_{fy:g}_{zoom:g}.jpg".replace(".", "p", 3)
    out = IMG / (out.stem.replace(".", "p") + ".jpg")
    if not out.exists():
        im = Image.open(path).convert("RGB"); W, H = im.size; ar = w / h
        cw, ch = (H * ar, H) if W / H > ar else (W, W / ar); cw, ch = cw / zoom, ch / zoom
        cx = min(max(fx * W, cw / 2), W - cw / 2); cy = min(max(fy * H, ch / 2), H - ch / 2)
        c = im.crop((round(cx - cw / 2), round(cy - ch / 2), round(cx + cw / 2), round(cy + ch / 2)))
        tw = round(w / 25.4 * 300)
        if c.width > tw:
            c = c.resize((tw, round(tw / ar)), Image.LANCZOS)
        c.save(out, "JPEG", quality=90, subsampling=0, optimize=True)
    return f"crops/{out.name}"


def T(text, x, y, cls, w=None, extra=""):
    ww = f"width:{w}mm;" if w is not None else ""
    return f"<div class='abs {cls}' style='left:{x}mm;top:{y}mm;{ww}{extra}'>{text}</div>"


def logo(x, y, w, mode="brand"):
    L = base._LOGO; px = py = 65
    vw, vh = L["width"] - 2 * px, L["height"] - 2 * py
    a, b = {"brand": (base.LOGO_SAGE, base.LOGO_BLUSH), "ink": (INK, INK)}[mode]
    return (f"<svg class='abs' style='left:{x}mm;top:{y}mm;width:{w}mm;height:{w * vh / vw:.2f}mm' viewBox='{px} {py} {vw} {vh}'>"
            f"<path d='{L['letters']}' fill='{a}' fill-rule='evenodd'/><path d='{L['flower']}' fill='{b}' fill-rule='evenodd'/></svg>")


def qr(url, x, y, size):
    q = segno.make(url, error="m"); n = q.symbol_size(border=0)[0]
    d = "".join(f"M{c} {r}h1v1h-1z" for r, row in enumerate(q.matrix) for c, v in enumerate(row) if v)
    return (f"<svg class='abs' style='left:{x}mm;top:{y}mm;width:{size}mm;height:{size}mm' viewBox='0 0 {n} {n}' "
            f"shape-rendering='crispEdges'><path d='{d}' fill='{INK}'/></svg>")


def metal(tags):
    if "Rose Gold Tone" in tags: return "rose"
    if "Two Tone" in tags: return "two"
    if any(t.startswith("Rhodium") for t in tags): return "rhodium"
    return "gold"


DOT = {"gold": "background:#C9A55C", "rhodium": "background:#A7AAAF", "rose": "background:#D69C86",
       "two": "background:linear-gradient(90deg,#A7AAAF 50%,#C9A55C 50%)"}


def inr(n):
    return base.inr(n)


FAMILIES = [("Earrings", "EARRINGS", "#F3D9CF", ""), ("Ring", "RINGS", "#D5E0D8", ""),
            ("Necklace", "NECKLACES", "#EEE2C8", ""), ("Bracelet", "BRACELETS &amp; SET", "#F6E3DC", "")]

# ---- geometry -------------------------------------------------------------------------------
X0, GW, COLS, GAP = 9, 192, 8, 2.4
CW = (GW - (COLS - 1) * GAP) / COLS            # 21.9 mm
Y0, ROWS = 40.5, 8
RH = (287.5 - Y0 - (ROWS - 1) * GAP) / ROWS     # row pitch without gap
IH = RH - 9.2                                   # image height; 9.2 mm of type under it

cells, parts = [], []
for fam, label, colour, _ in FAMILIES:
    hs = [h for h, p in SKU.items() if p["type"] == fam or (fam == "Bracelet" and p["type"] == "Jewellery Set")]
    hs.sort(key=lambda h: (not SKU[h]["available"], SKU[h]["type"] == "Jewellery Set", SKU[h]["price"], SKU[h]["title"]))
    cells.append(("label", fam, label, colour, hs))
    cells += [("item", h) for h in hs]
cells.append(("qr",))

i = 0
for c in cells:
    span = 2 if c[0] == "label" else 1
    if i % COLS + span > COLS:      # never needed with this count, kept as a guard
        i += COLS - i % COLS
    r, col = divmod(i, COLS)
    x, y = X0 + col * (CW + GAP), Y0 + r * (RH + GAP)
    if c[0] == "label":
        _, fam, label, colour, hs = c
        w = 2 * CW + GAP
        ins = sum(SKU[h]["available"] for h in hs)
        lo, hi = min(SKU[h]["price"] for h in hs), max(SKU[h]["price"] for h in hs)
        parts.append(f"<div class='abs' style='left:{x}mm;top:{y}mm;width:{w}mm;height:{RH}mm;background:{colour}'></div>")
        parts.append(T(f"<span class='lab-n'>{len(hs):02d}</span>", x + 3, y + 2.6, "", extra="line-height:1"))
        parts.append(T(label, x + 3, y + RH - 14.2, "lab-t", w=w - 6))
        parts.append(T(f"{ins} in stock{f' &nbsp;·&nbsp; {len(hs) - ins} sold out' if len(hs) - ins else ''}<br>{inr(lo)} to {inr(hi)}",
                       x + 3, y + RH - 8.3, "lab-s", w=w - 6))
    elif c[0] == "item":
        h = c[1]; p = SKU[h]
        fx, fy, z = SKU_FOCUS.get(h, FOCUS.get(h, (0.5, 0.45, 1.2)))
        sold = not p["available"]
        parts.append(f"<img class='ph{' sold' if sold else ''}' src='{crop(src(h), CW, IH, fx, fy, z, h)}' "
                     f"style='left:{x}mm;top:{y}mm;width:{CW}mm;height:{IH}mm' alt=''>")
        if sold:
            parts.append(T("SOLD OUT", x + 1.2, y + 1.2, "chip"))
        parts.append(T(p["title"], x, y + IH + 1.1, "nm", w=CW))
        parts.append(T(f"<span class='dot' style='{DOT[metal(p['tags'])]}'></span>{p['sku']}", x, y + RH - 2.75, "sku", w=CW))
        parts.append(T(inr(p["price"]), x + CW, y + RH - 2.95, "pr" + (" muted" if sold else ""), extra="transform:translateX(-100%)"))
    else:
        parts.append(qr("https://nairaflore.com", x + (CW - 15) / 2, y + 1.6, 15))
        parts.append(T("Shop every piece<br>at nairaflore.com", x + CW / 2, y + 18.6, "qrcap", extra="transform:translateX(-50%);text-align:center"))
    i += span

n_all = len(SKU); n_in = sum(p["available"] for p in SKU.values())
legend = "".join(f"<span class='lg'><span class='dot' style='{DOT[k]}'></span>{t}</span>" for k, t in
                 (("gold", "18k gold coated"), ("rhodium", "Rhodium coated"), ("rose", "Rose gold coated"), ("two", "Two-tone")))
head = "".join([
    logo(X0, 10.2, 30),
    T("NAIRA PETITE &nbsp;·&nbsp; THE COMPLETE LISTING &nbsp;·&nbsp; 1 OCTOBER 2026", X0 + GW, 11.2, "folio", extra="transform:translateX(-100%)"),
    T("<span class='disp'>THE PETITE INDEX</span><span class='it'>&nbsp; every piece, on one page.</span>", X0, 19.6, "title"),
    T(f"{n_all} listings &nbsp;·&nbsp; {n_in} in stock &nbsp;·&nbsp; {n_all - n_in} sold out", X0 + GW, 21.2, "meta", extra="transform:translateX(-100%)"),
    T(legend, X0 + GW, 27.6, "legend", extra="transform:translateX(-100%)"),
    f"<div class='abs' style='left:{X0}mm;top:35.6mm;width:{GW}mm;border-top:0.25pt solid {INK};opacity:.28'></div>",
    T("Prices in Indian rupees as listed on nairaflore.com on 1 October 2026. Sold-out pieces may return; ask us on WhatsApp "
      "+91 95615 57935, Monday to Saturday, 10 am to 7 pm IST.", X0, 290.3, "fine", w=150),
    T("[ 18k gold coated &nbsp;·&nbsp; rhodium coated ]", X0 + GW, 290.3, "fine", extra="transform:translateX(-100%);letter-spacing:.06em;white-space:nowrap"),
])

CSS = f"""
@page {{ size:{210 + 2 * BLEED}mm {297 + 2 * BLEED}mm; margin:0 }}
* {{ margin:0; padding:0; box-sizing:border-box }}
body {{ -webkit-print-color-adjust:exact; print-color-adjust:exact }}
.page {{ position:relative; width:{210 + 2 * BLEED}mm; height:{297 + 2 * BLEED}mm; overflow:hidden; background:{PAGE}; color:{INK} }}
.trim {{ position:absolute; left:{BLEED}mm; top:{BLEED}mm; width:210mm; height:297mm }}
.abs {{ position:absolute }}
img.ph {{ position:absolute; display:block; object-fit:cover }}
img.ph.sold {{ opacity:.42; filter:grayscale(.35) }}
.disp {{ font-family:'Velista',Georgia,serif; font-size:19pt; letter-spacing:.012em }}
.it {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:14pt; color:{INK_SOFT} }}
.title {{ white-space:nowrap; line-height:1 }}
.folio {{ font-family:'JostF',sans-serif; font-weight:500; font-size:5.6pt; letter-spacing:.24em; color:{MUTED}; white-space:nowrap }}
.meta {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:7.2pt; letter-spacing:.05em; color:{INK_SOFT}; white-space:nowrap }}
.legend {{ font-family:'JostF',sans-serif; font-weight:400; font-size:6.2pt; color:{INK_SOFT}; white-space:nowrap; display:flex; gap:4mm }}
.lg {{ display:inline-flex; align-items:center }}
.dot {{ display:inline-block; width:1.55mm; height:1.55mm; border-radius:50%; margin-right:1mm; vertical-align:-0.1mm; flex:none }}
.lab-n {{ font-family:'CormI',Georgia,serif; font-style:italic; font-size:24pt; color:{INK} }}
.lab-t {{ font-family:'Velista',Georgia,serif; font-size:12.5pt; letter-spacing:.02em; white-space:nowrap }}
.lab-s {{ font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:5.6pt; line-height:1.45; letter-spacing:.03em; color:{INK_SOFT} }}
.nm {{ font-family:'JostF',sans-serif; font-weight:400; font-size:5.55pt; line-height:1.18; color:{INK}; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden }}
.sku {{ font-family:'JostF',sans-serif; font-weight:400; font-size:4.9pt; letter-spacing:.03em; color:{MUTED}; white-space:nowrap; display:flex; align-items:center }}
.pr {{ font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:5.8pt; color:{INK}; white-space:nowrap }}
.pr.muted {{ color:{MUTED}; font-weight:400 }}
.chip {{ font-family:'JostF',sans-serif; font-weight:500; font-size:4.3pt; letter-spacing:.16em; color:{CORAL_DEEP}; background:{PAGE}; padding:.5mm .9mm; white-space:nowrap }}
.qrcap {{ font-family:'JostF',sans-serif; font-weight:400; font-size:5.2pt; line-height:1.35; color:{INK_SOFT}; white-space:nowrap }}
.fine {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:5.4pt; line-height:1.4; color:{MUTED} }}
"""
CORM_FULL = ("@font-face{font-family:'CormI';src:url(data:font/woff2;base64,"
             + base.b64(SCR / "fonts" / "cormorant-garamond-latin-300-italic.woff2")
             + ") format('woff2');font-style:italic;font-weight:400;font-display:block}")
html = (f"<!doctype html><html><head><meta charset='utf-8'><title>NAIRA PETITE · The Petite Index</title>"
        f"<style>{base.fonts_css()}{CORM_FULL}{CSS}</style></head><body><section class='page'><div class='trim'>"
        f"{head}{''.join(parts)}</div></section></body></html>")
(K / ("index-bleed.html" if BLEED else "index.html")).write_text(html)
print("cells", len(cells), "listings", n_all, "in stock", n_in, "row pitch", round(RH, 2), "image", round(CW, 2), "x", round(IH, 2))
