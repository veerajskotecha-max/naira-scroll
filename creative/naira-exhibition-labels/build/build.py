"""Flat-price labels for the exhibition table, on A4: FLAT ₹999 (deep sage) and FLAT ₹1,199 (blush), one sheet each.

Every sheet holds nine labels in four sizes, sharing cut lines so a cut a little off never leaves a white edge:
  one table sign 198 x 90 mm, two squares 99 x 99 mm (fit a 4 inch square stand),
  two tray strips 102 x 48 mm, four minis 48 x 48 mm.
The ground runs 3 mm past the outer cut line. Print at 100 % (actual size), cut along the hairlines.

Type: the price is Velista (the PETITE masthead face) with the ₹ from Laila Light, which matches Velista's
contrast; FLAT in tracked Jost; the italic in Cormorant, as on the catalogue and the pop-up posters."""
import asyncio, base64, json, sys
from pathlib import Path
import pymupdf as fitz
from playwright.async_api import async_playwright

D = Path(__file__).resolve().parent
FONTS = D / "fonts"
REPO = Path("/home/user/naira-scroll")
LOGO = json.load(open(REPO / "creative/naira-bag/build/assets/naira-logo-vector.json"))
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else D / "out"
CHROME = "/opt/pw-browsers/chromium"

SHEETS = [
    dict(key="999", price="₹999", ground="#5A766D", ink="#FBF5F0", accent="#FBD3C6",
         letters="#FBF5F0", flower="#FFBDA8", line="rgba(251,245,240,.45)"),
    dict(key="1199", price="₹1,199", ground="#F2CFC4", ink="#4A645B", accent="#4A645B",
         letters="#4A645B", flower="#C27560", line="rgba(74,100,91,.42)"),
]
M = 6                    # outer cut line, mm from the paper edge
BLEED = 3                # ground beyond the outer cut line
# (kind, x, y, w, h) in mm from the outer cut line's top-left corner; the block is 198 x 285
CELLS = [("sign", 0, 0, 198, 90),
         ("square", 0, 90, 99, 99), ("square", 99, 90, 99, 99),
         ("strip", 0, 189, 102, 48), ("strip", 0, 237, 102, 48),
         ("mini", 102, 189, 48, 48), ("mini", 150, 189, 48, 48), ("mini", 102, 237, 48, 48), ("mini", 150, 237, 48, 48)]
W, H = 198, 285


def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def face(fam, file, weight=400, style="normal", rng=None):
    fmt, mime = ("truetype", "font/ttf") if file.endswith(".ttf") else ("woff2", "font/woff2")
    r = f"unicode-range:{rng};" if rng else ""
    return (f"@font-face{{font-family:'{fam}';src:url(data:{mime};base64,{b64(FONTS / file)}) format('{fmt}');"
            f"font-weight:{weight};font-style:{style};font-display:block;{r}}}")


def logo(w, s):
    px = py = 65
    vw, vh = LOGO["width"] - 2 * px, LOGO["height"] - 2 * py
    return (f"<svg class='logo' style='width:{w}mm;height:{w * vh / vw:.2f}mm' viewBox='{px} {py} {vw} {vh}'>"
            f"<path d='{LOGO['letters']}' fill='{s['letters']}' fill-rule='evenodd'/>"
            f"<path d='{LOGO['flower']}' fill='{s['flower']}' fill-rule='evenodd'/></svg>")


def caps(text, pt, ls, extra=""):
    # letter-spacing also follows the last letter; the matching left padding keeps the word centred
    return f"<div class='caps' style='font-size:{pt}pt;letter-spacing:{ls}em;padding-left:{ls}em;{extra}'>{text}</div>"


def price(s, pt, extra=""):
    return f"<div class='price' style='font-size:{pt}pt;{extra}'>{s['price']}</div>"


def italic(text, pt, s, extra=""):
    return f"<div class='it' style='font-size:{pt}pt;color:{s['accent']};{extra}'>{text}</div>"


def label(kind, s):
    if kind == "sign":
        return "".join([
            "<div class='frame' style='inset:4mm'></div>",
            "<div class='col' style='left:4mm;top:4mm;width:72mm;height:82mm'>", logo(46, s),
            caps("DEMI-FINE JEWELLERY", 6.2, .34, "margin-top:4.6mm"),
            f"<div class='rule' style='width:10mm;margin:3.4mm 0 3mm'></div>",
            "<div class='web' style='font-size:8pt'>nairaflore.com</div></div>",
            "<div class='vrule' style='left:78mm;top:17mm;height:56mm'></div>",
            "<div class='col' style='left:80mm;top:4mm;width:114mm;height:82mm'>",
            caps("FLAT", 12.5, .62), price(s, 100, "margin-top:1.2mm"), italic("any piece here.", 17, s, "margin-top:1mm"), "</div>"])
    if kind == "square":
        return "".join([
            "<div class='frame' style='inset:3.5mm'></div>",
            "<div class='col' style='left:3.5mm;top:3.5mm;width:92mm;height:92mm'>", logo(38, s),
            caps("FLAT", 9, .6, "margin-top:7mm"), price(s, 62, "margin-top:.6mm"),
            italic("any piece here.", 12.5, s, "margin-top:.4mm"),
            "<div class='web' style='font-size:6.4pt;margin-top:5.2mm'>nairaflore.com</div></div>"])
    if kind == "strip":
        return "".join([
            "<div class='frame' style='inset:3mm'></div>",
            "<div class='col' style='left:3mm;top:3mm;width:36mm;height:42mm'>", logo(27, s), "</div>",
            "<div class='vrule' style='left:40.5mm;top:11mm;height:26mm'></div>",
            "<div class='col' style='left:42mm;top:3mm;width:57mm;height:42mm'>",
            caps("FLAT", 7, .6), price(s, 46, "margin-top:.4mm"), italic("any piece here.", 9.5, s), "</div>"])
    if kind == "mini":
        return "".join([
            "<div class='frame' style='inset:2.5mm'></div>",
            "<div class='col' style='left:2.5mm;top:3mm;width:43mm;height:43mm'>", logo(24, s),
            caps("FLAT", 6, .6, "margin-top:3.2mm"), price(s, 33, "margin-top:.2mm"), "</div>"])
    raise ValueError(kind)


def cut_lines(s):
    """Hairlines on every cut, run out into the bleed where they reach the edge of the block."""
    x0, y0, b = M, M, BLEED
    segs = [(x0 - b, y0, x0 + W + b, y0), (x0 - b, y0 + H, x0 + W + b, y0 + H),        # top, bottom
            (x0, y0 - b, x0, y0 + H + b), (x0 + W, y0 - b, x0 + W, y0 + H + b)]        # left, right
    for y in (90, 189, 237):                                                              # full-width cuts
        segs.append((x0 - b, y0 + y, x0 + W + b, y0 + y))
    segs.append((x0 + 99, y0 + 90, x0 + 99, y0 + 189))                                   # between the squares
    for x in (102, 150):                                                                  # strips | minis | minis
        segs.append((x0 + x, y0 + 189, x0 + x, y0 + H + b))
    lines = "".join(f"<line x1='{a}' y1='{c}' x2='{e}' y2='{f}'/>" for a, c, e, f in segs)
    return (f"<svg class='cuts' viewBox='0 0 210 297'><g stroke='{s['line']}' stroke-width='0.09' "
            f"fill='none' shape-rendering='geometricPrecision'>{lines}</g></svg>")


def sheet(s):
    labs = "".join(f"<div class='lab {k}' style='left:{M + x}mm;top:{M + y}mm;width:{w}mm;height:{h}mm'>{label(k, s)}</div>"
                   for k, x, y, w, h in CELLS)
    ground = (f"<div class='ground' style='left:{M - BLEED}mm;top:{M - BLEED}mm;width:{W + 2 * BLEED}mm;"
              f"height:{H + 2 * BLEED}mm;background:{s['ground']}'></div>")
    return f"<section class='page' style='color:{s['ink']};--line:{s['line']}'>{ground}{labs}{cut_lines(s)}</section>"


CSS = """
@page { size: 210mm 297mm; margin: 0 }
* { margin:0; padding:0; box-sizing:border-box }
html, body { background:#fff }
body { -webkit-print-color-adjust:exact; print-color-adjust:exact }
.page { position:relative; width:210mm; height:297mm; overflow:hidden; break-after:page }
.page:last-child { break-after:auto }
.ground, .lab, .col, .frame, .vrule { position:absolute }
.cuts { position:absolute; left:0; top:0; width:210mm; height:297mm }
.frame { border:0.3pt solid var(--line) }
.vrule { width:0; border-left:0.3pt solid var(--line) }
.rule { height:0; border-top:0.3pt solid var(--line) }
.col { display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center }
.logo { display:block }
.caps { font-family:'JostF',sans-serif; font-weight:500; line-height:1; white-space:nowrap }
.web { font-family:'JostF',sans-serif; font-weight:400; letter-spacing:.08em; line-height:1; white-space:nowrap }
.price { font-family:'Rupee','Velista',serif; font-weight:400; line-height:.98; white-space:nowrap; letter-spacing:.005em }
.it { font-family:'CormI',serif; font-style:italic; font-weight:400; line-height:1.1; white-space:nowrap }
"""


def html():
    fonts = "".join([face("Velista", "Velista.ttf"), face("Rupee", "Laila-300-r.woff2", 400, rng="U+20B9"),
                     face("JostF", "Jost-400.woff2", 400), face("JostF", "Jost-500.woff2", 500),
                     face("CormI", "CormorantGaramond-300i.woff2", 400, "italic")])
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>NAIRA PETITE · Flat price labels</title>"
            f"<style>{fonts}{CSS}</style></head><body>{''.join(sheet(s) for s in SHEETS)}</body></html>")


CHECK = """() => {
  const mm = 96 / 25.4, bad = [];
  document.querySelectorAll('.lab').forEach((lab, i) => {
    const L = lab.getBoundingClientRect();
    lab.querySelectorAll('.caps, .price, .it, .web, .logo').forEach(e => {
      const r = e.getBoundingClientRect(), pad = 1.2 * mm;   // keep 1.2 mm inside the label's frame inset
      const inset = parseFloat(lab.querySelector('.frame').style.inset) * mm;
      if (r.left < L.left + inset + pad || r.right > L.right - inset - pad || r.top < L.top + inset + pad || r.bottom > L.bottom - inset - pad)
        bad.push([i, lab.className, e.className.baseVal || e.className, (r.width / mm).toFixed(1) + 'x' + (r.height / mm).toFixed(1)]);
    });
  });
  const fonts = [...document.fonts].filter(f => f.status !== 'loaded').map(f => f.family + ' ' + f.weight);
  return {bad, fonts};
}"""


async def render():
    OUT.mkdir(parents=True, exist_ok=True)
    src = D / "labels.html"
    src.write_text(html())
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        pg = await b.new_page()
        await pg.goto(src.as_uri(), wait_until="networkidle")
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(400)
        print("check:", json.dumps(await pg.evaluate(CHECK)))
        tmp = OUT / "labels.tmp.pdf"
        await pg.pdf(path=str(tmp), prefer_css_page_size=True, print_background=True)
        await b.close()
    pdf = OUT / "naira-flat-price-labels-A4.pdf"
    doc = fitz.open(tmp)
    doc.set_metadata({"title": "Naira Petite · Flat price labels · A4", "author": "Naira", "creator": "Naira", "producer": "Naira",
                      "subject": "FLAT ₹999 and FLAT ₹1,199 labels for the exhibition table, nine per sheet in four sizes",
                      "keywords": "Naira, Naira Petite, exhibition, price labels, flat 999, flat 1199"})
    doc.save(pdf, garbage=4, deflate=True)
    tmp.unlink()
    doc = fitz.open(pdf)
    for i, page in enumerate(doc):
        page.get_pixmap(dpi=110).save(OUT / f"preview-p{i + 1}.png")
    print(pdf.name, len(doc), "pages", f"{doc[0].rect.width / 72 * 25.4:.1f} x {doc[0].rect.height / 72 * 25.4:.1f} mm",
          round(pdf.stat().st_size / 1e3), "kB")


if __name__ == "__main__":
    asyncio.run(render())
