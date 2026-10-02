"""
NAIRA PETITE — Exhibition stock log: the Petite Index as a one-page A4 count sheet.

Every jewellery listing (55) with its photograph, name, SKU, metal and price, and write-in boxes for the
storage box number, the quantity at the start, the quantity at the end and the number sold.
White page and hairline rules so it prints cleanly on an office printer and takes pen.
"""
import json, sys
from pathlib import Path
from PIL import Image

K = Path(__file__).resolve().parent
SCR = K.parent
CAMP = SCR / "camp"
sys.path.insert(0, str(CAMP / "studio"))
import base

IMG = K / "log_crops"; IMG.mkdir(exist_ok=True)
SKU = json.load(open(K / "skus_1002.json"))
FOCUS = json.load(open(SCR / "catalogue" / "grid_focus.json"))
SKU_FOCUS = json.load(open(K / "sku_focus.json")) if (K / "sku_focus.json").exists() else {}

INK, INK_SOFT, MUTED, RULE, CORAL_DEEP = "#1C1C1C", "#3D3530", "#6B615A", "#CFC7BE", "#B8604A"

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


def src(h):
    if h in SOLD_PICK:
        return K / "img" / f"{h}_{SOLD_PICK[h]}.jpg"
    if h == "pearl-drop-studs":
        return Path(json.load(open(SCR / "catalogue" / "raw_index.json"))["pearl-drop-studs:48dc"]["path"])
    if h in CAT_ODD:
        return CAMP / CAT_ODD[h]
    return CAMP / "shop" / h / "0.jpg"


def thumb(h, mm):
    """Square crop around the piece (the Index's per-product focus), 600 dpi so it stays crisp on screen and paper."""
    fx, fy, zoom = SKU_FOCUS.get(h) or FOCUS.get(h) or (0.5, 0.45, 1.15)
    out = IMG / f"{h}.jpg"
    if not out.exists():
        im = Image.open(src(h)).convert("RGB"); W, H = im.size
        s = min(W, H) / zoom
        cx = min(max(fx * W, s / 2), W - s / 2); cy = min(max(fy * H, s / 2), H - s / 2)
        c = im.crop((round(cx - s / 2), round(cy - s / 2), round(cx + s / 2), round(cy + s / 2)))
        px = round(mm / 25.4 * 600)
        if c.width > px:
            c = c.resize((px, px), Image.LANCZOS)
        c.save(out, "JPEG", quality=90, subsampling=0, optimize=True)
    return f"log_crops/{out.name}"


def metal(tags):
    if "Rose Gold Tone" in tags: return "rose"
    if "Two Tone" in tags: return "two"
    if any(t.startswith("Rhodium") for t in tags): return "rhodium"
    return "gold"


DOT = {"gold": "background:#C9A55C", "rhodium": "background:#A7AAAF", "rose": "background:#D69C86",
       "two": "background:linear-gradient(90deg,#A7AAAF 50%,#C9A55C 50%)"}
METAL_WORD = {"gold": "gold", "rhodium": "silver", "rose": "rose gold", "two": "two-tone"}


def logo(x, y, w):
    L = base._LOGO; px = py = 65
    vw, vh = L["width"] - 2 * px, L["height"] - 2 * py
    return (f"<svg class='abs' style='left:{x}mm;top:{y}mm;width:{w}mm;height:{w * vh / vw:.2f}mm' viewBox='{px} {py} {vw} {vh}'>"
            f"<path d='{L['letters']}' fill='{base.LOGO_SAGE}' fill-rule='evenodd'/><path d='{L['flower']}' fill='{base.LOGO_BLUSH}' fill-rule='evenodd'/></svg>")


def A(x, y, w, h, inner="", cls="", style=""):
    return f"<div class='abs {cls}' style='left:{x}mm;top:{y}mm;width:{w}mm;height:{h}mm;{style}'>{inner}</div>"


FAMILIES = [("Earrings", "EARRINGS", "#F3D9CF"), ("Ring", "RINGS", "#D5E0D8"),
            ("Necklace", "NECKLACES", "#EEE2C8"), ("Bracelet", "BRACELETS &amp; SET", "#F6E3DC")]


def family(fam):
    hs = [h for h, p in SKU.items() if p["type"] == fam or (fam == "Bracelet" and p["type"] == "Jewellery Set")]
    return sorted(hs, key=lambda h: (not SKU[h]["available"], SKU[h]["type"] == "Jewellery Set", SKU[h]["price"], SKU[h]["title"]))


# ---- geometry (mm) -------------------------------------------------------------------------------
M = 8                                   # page margin
GUT = 6
CW = (210 - 2 * M - GUT) / 2            # column width, 94 mm
TOP = 33.5                              # table top
HEAD_H = 5.2                            # column-header row
FAM_H = 4.6                             # family row
RH = 8.0                                # item row
F = dict(box=13.0, start=11.5, end=11.5, sold=10.0)   # write-in columns, right-aligned in each column
FW = sum(F.values())
PHOTO = RH - 0.9

parts = []


def column(x0, fams):
    y = TOP
    # column header
    fx = x0 + CW - FW
    parts.append(A(x0, y, CW - FW, HEAD_H, "PIECE", "th", "padding-left:10.6mm"))
    for key, label in (("box", "BOX NO."), ("start", "START QTY"), ("end", "END QTY"), ("sold", "SOLD")):
        parts.append(A(fx, y, F[key], HEAD_H, label, "th c"))
        fx += F[key]
    y += HEAD_H
    parts.append(A(x0, y, CW, 0, "", "rule strong"))
    for fam, label, tint in fams:
        hs = family(fam)
        ins = sum(SKU[h]["available"] for h in hs)
        meta = f"{len(hs)} pieces · {ins} in stock online" + (f" · {len(hs) - ins} sold out online" if len(hs) > ins else "")
        parts.append(A(x0, y, CW, FAM_H, f"<span class='fam'>{label}</span><span class='fam-m'>{meta}</span>", "famrow",
                       f"background:{tint}"))
        y += FAM_H
        for h in hs:
            p = SKU[h]
            m = metal(p["tags"])
            sold = "" if p["available"] else "<span class='so'>sold out</span>"
            parts.append(A(x0, y, 1.2, RH, "", "", f"background:{tint}"))
            parts.append(f"<img class='abs ph' src='{thumb(h, PHOTO)}' style='left:{x0 + 2.0}mm;top:{y + 0.45}mm;"
                         f"width:{PHOTO}mm;height:{PHOTO}mm' alt=''>")
            parts.append(A(x0 + 2.0 + PHOTO + 1.6, y, CW - FW - (2.0 + PHOTO + 1.6) - 1.0, RH,
                           f"<div class='nm'>{p['title']}</div>"
                           f"<div class='sk'><i class='dot' style='{DOT[m]}'></i>{p['sku']} · {base.inr(p['price'])}"
                           f"{' · ' + sold if sold else ''}</div>", "cell"))
            fx = x0 + CW - FW
            for key in ("box", "start", "end", "sold"):
                parts.append(A(fx, y, F[key], RH, "", "box"))
                fx += F[key]
            y += RH
            parts.append(A(x0, y, CW, 0, "", "rule"))
    return y


yl = column(M, FAMILIES[:2])
yr = column(M + CW + GUT, FAMILIES[2:])
bottom = max(yl, yr)

# ---- header ---------------------------------------------------------------------------------------
n_in = sum(p["available"] for p in SKU.values())
head = [
    logo(M, 9.2, 30),
    A(M, 18.2, 80, 6, "EXHIBITION STOCK LOG", "title"),
    A(M, 25.4, 86, 5, f"The Petite Index · {len(SKU)} pieces · count in before opening, count again at close · sold = start − end", "sub"),
]
fields = [("EXHIBITION", 102, 9.0, 56), ("DATES", 162, 9.0, 40),
          ("VENUE", 102, 16.6, 56), ("TABLE / STALL", 162, 16.6, 40),
          ("START COUNT BY", 102, 24.2, 56), ("END COUNT BY", 162, 24.2, 40)]
for label, x, y, w in fields:
    head.append(A(x, y, w, 6.2, f"<span class='fl'>{label}</span>", "field"))

# ---- footer ---------------------------------------------------------------------------------------
fy = bottom + 3.2
foot = [
    A(M, fy, 194, 9.5, "", "totals"),
    A(M + 2.5, fy + 1.3, 40, 7, "<span class='fl'>TOTAL PIECES</span>", ""),
    A(M + 44, fy + 1.3, 36, 7, "<span class='fl'>START</span>", "tbox"),
    A(M + 82, fy + 1.3, 36, 7, "<span class='fl'>END</span>", "tbox"),
    A(M + 120, fy + 1.3, 36, 7, "<span class='fl'>SOLD</span>", "tbox"),
    A(M + 158, fy + 1.3, 34, 7, "<span class='fl'>CHECKED BY</span>", "tbox"),
    A(M, fy + 11.2, 194, 4, f"Prices as listed on nairaflore.com on 2 October 2026. “Sold out” means sold out on the website that day; "
      f"log it here if you have it in a box. Metal: <i class='dot' style='{DOT['gold']}'></i>gold "
      f"<i class='dot' style='{DOT['rhodium']}'></i>silver (rhodium) <i class='dot' style='{DOT['two']}'></i>two-tone "
      f"<i class='dot' style='{DOT['rose']}'></i>rose gold.", "fine"),
]

CSS = f"""
@page {{ size: 210mm 297mm; margin: 0 }}
* {{ margin:0; padding:0; box-sizing:border-box }}
html, body {{ background:#fff }}
body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact }}
.page {{ position:relative; width:210mm; height:297mm; overflow:hidden; background:#fff; color:{INK} }}
.abs {{ position:absolute }}
.title {{ font-family:'Velista',Georgia,serif; font-size:17pt; letter-spacing:.02em; white-space:nowrap; line-height:1 }}
.sub {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:6.4pt; color:{MUTED}; white-space:nowrap }}
.field {{ border-bottom:0.35pt solid {INK_SOFT} }}
.fl {{ font-family:'JostF',sans-serif; font-weight:500; font-size:5pt; letter-spacing:.18em; color:{MUTED}; position:absolute; left:0; top:0 }}
.th {{ font-family:'JostF',sans-serif; font-weight:500; font-size:5pt; letter-spacing:.16em; color:{INK_SOFT}; display:flex; align-items:center; white-space:nowrap }}
.th.c {{ justify-content:center; letter-spacing:.1em }}
.rule {{ border-top:0.25pt solid {RULE} }}
.rule.strong {{ border-top:0.6pt solid {INK_SOFT} }}
.famrow {{ display:flex; align-items:center; gap:2.2mm; padding-left:2mm }}
.fam {{ font-family:'JostF',sans-serif; font-weight:500; font-size:5.6pt; letter-spacing:.2em; color:{INK} }}
.fam-m {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:5.4pt; color:{INK_SOFT} }}
img.ph {{ object-fit:cover; border-radius:0.6mm; display:block }}
.cell {{ display:flex; flex-direction:column; justify-content:center; gap:0.35mm; overflow:hidden }}
.nm {{ font-family:'JostF',sans-serif; font-weight:400; font-size:6.5pt; line-height:1.12; color:{INK};
       display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden }}
.sk {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:5.4pt; line-height:1.1; color:{MUTED}; white-space:nowrap }}
.so {{ color:{CORAL_DEEP} }}
.dot {{ display:inline-block; width:1.5mm; height:1.5mm; border-radius:50%; margin-right:0.9mm; vertical-align:-0.1mm }}
.box {{ border-left:0.25pt solid {RULE} }}
.totals {{ border:0.6pt solid {INK_SOFT}; border-radius:1mm }}
.tbox {{ border-bottom:0.35pt solid {INK_SOFT} }}
.fine {{ font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:5.6pt; color:{MUTED}; white-space:nowrap }}
"""


def html():
    body = "".join(head + parts + foot)
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>NAIRA PETITE · Exhibition stock log</title>"
            f"<style>{base.fonts_css()}{CSS}</style></head><body><section class='page'>{body}</section></body></html>")


if __name__ == "__main__":
    (K / "log.html").write_text(html())
    print("rows", len(SKU), "bottom of table", round(bottom, 1), "mm; footer ends", round(fy + 15.2, 1), "mm")
