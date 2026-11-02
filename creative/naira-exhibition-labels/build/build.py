"""Flat-price labels for the exhibition table, on A4: FLAT ₹999 and FLAT ₹1,299, each in light sage and in light blush.

Two print files, four sheets each (₹999 sage, ₹999 blush, ₹1,299 sage, ₹1,299 blush):
  horizontal  one table sign 198 x 90 mm, four tray strips 99 x 50 mm, nine small strips 66 x 31.7 mm
  mixed       one table sign 198 x 90 mm, two squares 99 x 99 mm (fit a 4 inch square stand),
              two tray strips 102 x 48 mm, four minis 48 x 48 mm
Labels share cut lines, so a cut a little off never leaves a white edge, and the ground runs 3 mm past the
outer cut line. Print at 100 % (actual size), cut along the hairlines.

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

INK = "#3F5B52"                      # deep sage, for type on both light grounds
COLOURS = {
    "sage": dict(name="light sage", ground="#CFDFD9", ink=INK, letters="#4A6A60", flower="#D07A62", line="rgba(63,91,82,.36)"),
    "blush": dict(name="light blush", ground="#F9E1D8", ink=INK, letters="#4A6A60", flower="#C86F58", line="rgba(63,91,82,.34)"),
}
PRICES = ["₹999", "₹1,299"]
M = 6                    # outer cut line, mm from the paper edge
BLEED = 3                # ground beyond the outer cut line
W, H = 198, 285          # the block inside the outer cut line
S3 = 95 / 3              # three rows of small strips in the last 95 mm
# (kind, x, y, w, h) in mm from the outer cut line's top-left corner
LAYOUTS = {
    "horizontal": [("sign", 0, 0, 198, 90)]
                  + [("strip", x, y, 99, 50) for y in (90, 140) for x in (0, 99)]
                  + [("small", x, 190 + r * S3, 66, S3) for r in range(3) for x in (0, 66, 132)],
    "mixed": [("sign", 0, 0, 198, 90),
              ("square", 0, 90, 99, 99), ("square", 99, 90, 99, 99),
              ("strip", 0, 189, 102, 48), ("strip", 0, 237, 102, 48),
              ("mini", 102, 189, 48, 48), ("mini", 150, 189, 48, 48), ("mini", 102, 237, 48, 48), ("mini", 150, 237, 48, 48)],
}


def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def face(fam, file, weight=400, style="normal", rng=None):
    fmt, mime = ("truetype", "font/ttf") if file.endswith(".ttf") else ("woff2", "font/woff2")
    r = f"unicode-range:{rng};" if rng else ""
    return (f"@font-face{{font-family:'{fam}';src:url(data:{mime};base64,{b64(FONTS / file)}) format('{fmt}');"
            f"font-weight:{weight};font-style:{style};font-display:block;{r}}}")


def logo(w, c):
    px = py = 65
    vw, vh = LOGO["width"] - 2 * px, LOGO["height"] - 2 * py
    return (f"<svg class='logo' style='width:{w}mm;height:{w * vh / vw:.2f}mm' viewBox='{px} {py} {vw} {vh}'>"
            f"<path d='{LOGO['letters']}' fill='{c['letters']}' fill-rule='evenodd'/>"
            f"<path d='{LOGO['flower']}' fill='{c['flower']}' fill-rule='evenodd'/></svg>")


def caps(text, pt, ls, extra=""):
    # letter-spacing also follows the last letter; the matching left padding keeps the word centred
    return f"<div class='caps' style='font-size:{pt}pt;letter-spacing:{ls}em;padding-left:{ls}em;{extra}'>{text}</div>"


def price(p, pt, extra=""):
    return f"<div class='price' style='font-size:{pt}pt;{extra}'>{p}</div>"


def italic(text, pt, extra=""):
    return f"<div class='it' style='font-size:{pt}pt;{extra}'>{text}</div>"


def col(x, y, w, h, *inner):
    return f"<div class='col' style='left:{x:g}mm;top:{y:g}mm;width:{w:g}mm;height:{h:g}mm'>{''.join(inner)}</div>"


def split(w, h, c, p, inset, lw, logo_w, flat_pt, price_pt, it_pt=None, gap=1.5):
    """Horizontal label: the logo on the left, a hairline, then FLAT and the price."""
    rx = inset + lw + 2 * gap
    right = [caps("FLAT", flat_pt, .6), price(p, price_pt, "margin-top:.4mm")]
    if it_pt:
        right.append(italic("any piece here.", it_pt))
    return "".join([f"<div class='frame' style='inset:{inset}mm'></div>",
                    col(inset, inset, lw, h - 2 * inset, logo(logo_w, c)),
                    f"<div class='vrule' style='left:{inset + lw + gap:g}mm;top:{h * .24:.2f}mm;height:{h * .52:.2f}mm'></div>",
                    col(rx, inset, w - inset - rx, h - 2 * inset, *right)])


def label(kind, w, h, c, p):
    if kind == "sign":
        return "".join([
            "<div class='frame' style='inset:4mm'></div>",
            col(4, 4, 72, 82, logo(46, c), caps("DEMI-FINE JEWELLERY", 6.2, .34, "margin-top:4.6mm"),
                "<div class='rule' style='width:10mm;margin:3.4mm 0 3mm'></div>",
                "<div class='web' style='font-size:8pt'>nairaflore.com</div>"),
            "<div class='vrule' style='left:78mm;top:17mm;height:56mm'></div>",
            col(80, 4, 114, 82, caps("FLAT", 12.5, .62), price(p, 100, "margin-top:1.2mm"),
                italic("any piece here.", 17, "margin-top:1mm"))])
    if kind == "square":
        return "".join([
            "<div class='frame' style='inset:3.5mm'></div>",
            col(3.5, 3.5, 92, 92, logo(38, c), caps("FLAT", 9, .6, "margin-top:7mm"), price(p, 62, "margin-top:.6mm"),
                italic("any piece here.", 12.5, "margin-top:.4mm"),
                "<div class='web' style='font-size:6.4pt;margin-top:5.2mm'>nairaflore.com</div>")])
    if kind == "strip":
        return split(w, h, c, p, 3, 36, 27, 7, 46, 9.5)
    if kind == "small":
        return split(w, h, c, p, 2.2, 21, 17, 5.4, 26, gap=1)
    if kind == "mini":
        return "".join([
            "<div class='frame' style='inset:2.5mm'></div>",
            col(2.5, 3, 43, 43, logo(24, c), caps("FLAT", 6, .6, "margin-top:3.2mm"), price(p, 33, "margin-top:.2mm"))])
    raise ValueError(kind)


def merge(segs):
    """Join overlapping or touching collinear segments: {pos: [(a, b), ...]} -> [(pos, a, b), ...]."""
    out = []
    for pos, spans in segs.items():
        spans = sorted(spans)
        a, b = spans[0]
        for x, y in spans[1:]:
            if x <= b + 1e-6:
                b = max(b, y)
            else:
                out.append((pos, a, b)); a, b = x, y
        out.append((pos, a, b))
    return out


def cut_lines(cells, c):
    """A hairline on every cut, run out into the bleed wherever it meets the edge of the block."""
    hs, vs = {}, {}
    for _, x, y, w, h in cells:
        for yy in (y, y + h):
            hs.setdefault(round(yy, 3), []).append((x, x + w))
        for xx in (x, x + w):
            vs.setdefault(round(xx, 3), []).append((y, y + h))
    lines = []
    for y, a, b in merge(hs):
        a, b = (a - BLEED if a <= 0 else a), (b + BLEED if b >= W else b)
        lines.append((M + a, M + y, M + b, M + y))
    for x, a, b in merge(vs):
        a, b = (a - BLEED if a <= 0 else a), (b + BLEED if b >= H - 1e-6 else b)
        lines.append((M + x, M + a, M + x, M + b))
    body = "".join(f"<line x1='{a:.3f}' y1='{b:.3f}' x2='{e:.3f}' y2='{f:.3f}'/>" for a, b, e, f in lines)
    return f"<svg class='cuts' viewBox='0 0 210 297'><g stroke='{c['line']}' stroke-width='0.09' fill='none'>{body}</g></svg>"


def sheet(layout, c, p):
    cells = LAYOUTS[layout]
    labs = "".join(f"<div class='lab {k}' style='left:{M + x:.3f}mm;top:{M + y:.3f}mm;width:{w:.3f}mm;height:{h:.3f}mm'>"
                   f"{label(k, w, h, c, p)}</div>" for k, x, y, w, h in cells)
    ground = (f"<div class='ground' style='left:{M - BLEED}mm;top:{M - BLEED}mm;width:{W + 2 * BLEED}mm;"
              f"height:{H + 2 * BLEED}mm;background:{c['ground']}'></div>")
    return f"<section class='page' style='color:{c['ink']};--line:{c['line']}'>{ground}{labs}{cut_lines(cells, c)}</section>"


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
FONT_CSS = None


def html(layout):
    global FONT_CSS
    FONT_CSS = FONT_CSS or "".join([face("Velista", "Velista.ttf"), face("Rupee", "Laila-300-r.woff2", 400, rng="U+20B9"),
                                    face("JostF", "Jost-400.woff2", 400), face("JostF", "Jost-500.woff2", 500),
                                    face("CormI", "CormorantGaramond-300i.woff2", 400, "italic")])
    pages = "".join(sheet(layout, COLOURS[k], p) for p in PRICES for k in ("sage", "blush"))
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>NAIRA PETITE · Flat price labels · {layout}</title>"
            f"<style>{FONT_CSS}{CSS}</style></head><body>{pages}</body></html>")


CHECK = """() => {
  const mm = 96 / 25.4, bad = [];
  document.querySelectorAll('.lab').forEach((lab, i) => {
    const L = lab.getBoundingClientRect();
    const inset = parseFloat(lab.querySelector('.frame').style.inset) * mm, pad = 1.2 * mm;   // keep 1.2 mm inside the frame
    lab.querySelectorAll('.caps, .price, .it, .web, .logo').forEach(e => {
      const r = e.getBoundingClientRect();
      if (r.left < L.left + inset + pad || r.right > L.right - inset - pad || r.top < L.top + inset + pad || r.bottom > L.bottom - inset - pad)
        bad.push([i, lab.className, e.className.baseVal || e.className, (r.width / mm).toFixed(1) + 'x' + (r.height / mm).toFixed(1)]);
    });
  });
  const fonts = [...document.fonts].filter(f => f.status !== 'loaded').map(f => f.family + ' ' + f.weight);
  return {labels: document.querySelectorAll('.lab').length, bad, fonts};
}"""


async def render():
    OUT.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=CHROME)
        for layout in LAYOUTS:
            src = D / f"labels-{layout}.html"
            src.write_text(html(layout))
            pg = await b.new_page()
            await pg.goto(src.as_uri(), wait_until="networkidle")
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(400)
            print(layout, "check:", json.dumps(await pg.evaluate(CHECK)))
            tmp = OUT / f"{layout}.tmp.pdf"
            await pg.pdf(path=str(tmp), prefer_css_page_size=True, print_background=True)
            await pg.close()
            pdf = OUT / f"naira-flat-price-labels-{layout}-A4.pdf"
            doc = fitz.open(tmp)
            doc.set_metadata({"title": f"Naira Petite · Flat price labels · {layout} · A4", "author": "Naira", "creator": "Naira",
                              "producer": "Naira", "keywords": "Naira, Naira Petite, exhibition, price labels, flat 999, flat 1299",
                              "subject": "FLAT ₹999 and FLAT ₹1,299 in light sage and light blush: pages 1-2 ₹999, pages 3-4 ₹1,299"})
            doc.save(pdf, garbage=4, deflate=True)
            tmp.unlink()
            doc = fitz.open(pdf)
            for i, page in enumerate(doc):
                page.get_pixmap(dpi=90).save(OUT / f"preview-{layout}-p{i + 1}.png")
            print(" ", pdf.name, len(doc), "pages", round(pdf.stat().st_size / 1e3), "kB")
        await b.close()


if __name__ == "__main__":
    asyncio.run(render())
