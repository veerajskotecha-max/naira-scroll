# The three colour-camp standees (APRICOT, SAGE, LILAC) as the back-wall posters, 24 × 36 in.
# The 4 × 6 ft standee PDFs (122 × 182.6 cm, from ../colour-camps) are already 2:3, so each is placed at half size
# (x 0.4997, y 0.5008 — a 0.2% stretch nobody can see) on an exact 24 × 36 in page, vector intact. Before that, patches are
# laid over what has changed since September, matched to the original type by measuring each old line:
#   · Brushed Gold Huggies is now ₹999 (was ₹1,099) — the sticker price is repainted (raster patch, the sticker is glossy)
#   · the Sage QR was ivory on green, which phones misread: redrawn dark on an ivory tile
#   · no "waterproof" claims: the Apricot taped strip, the Sage and Lilac footers, the Lilac side facts
#   · "gold" is always "gold-tone": the Heartbead and Granule Dome spec lines (Sage)
#   · the 12 cm stand base (now 6 cm) carries a quiet line: NAIRA PETITE · SOFTLY, SLOWLY, WORN.
# Usage: <venv>/bin/python standees_print.py -> <scratchpad>/stall/out/Naira-Stall-back-<n>-<camp>-24x36in.pdf (+ jpg, preview)
import io, os, subprocess, sys
import numpy as np, cv2, segno
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
SRC = f"{SP}/stall/pdf/print"; OUT = f"{SP}/stall/out"; WORK = f"{SP}/stall/work/standees"
MONO = f"{SP}/stall/fonts/JetBrainsMonowght400.ttf"; JOST = f"{SP}/cat/fonts/Jost[wght].ttf"
pdfmetrics.registerFont(TTFont("JBMono", MONO))
DPI = 400; K = DPI / 72
CAMPS = [("A-apricot", 1, "apricot"), ("B-sage", 2, "sage"), ("C-lilac", 3, "lilac")]

def render(pdf, box):
    """box in pt (x0, y0, x1, y1), top-left origin -> RGB array at DPI"""
    x0, y0, x1, y1 = box
    base = f"{WORK}/r"
    subprocess.run(["pdftoppm", "-r", str(DPI), "-x", str(int(x0 * K)), "-y", str(int(y0 * K)), "-W", str(int((x1 - x0) * K)),
                    "-H", str(int((y1 - y0) * K)), "-png", "-singlefile", pdf, base], check=True)
    return np.asarray(Image.open(base + ".png").convert("RGB")).astype(int)

def measure(pdf, box):
    """bg colour, ink colour and the ink extent (pt, page coords) of one line of text inside box"""
    a = render(pdf, box); h, w, _ = a.shape
    edge = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    bg = np.median(edge, axis=0)
    d = np.abs(a - bg).sum(2); ink = d > 60
    rows = ink.any(1); runs = []; st = None
    for i, v in enumerate(list(rows) + [False]):          # keep only the line of text nearest the box's middle
        if v and st is None: st = i
        if not v and st is not None: runs.append((st, i)); st = None
    mid = h / 2; r0, r1 = min(runs, key=lambda r: 0 if r[0] <= mid < r[1] else min(abs(r[0] - mid), abs(r[1] - mid)))
    ink[:r0] = False; ink[r1:] = False
    ys, xs = np.where(ink)
    far = a[d >= np.percentile(d[ink], 70)]
    col = np.median(far, axis=0)
    x0, y0 = box[0], box[1]
    return dict(bg=bg, ink=col, left=x0 + xs.min() / K, right=x0 + (xs.max() + 1) / K, top=y0 + ys.min() / K, base=y0 + (ys.max() + 1) / K)

def mono_fit(cap_pt, extent_pt, text):
    """font size from cap height, letter spacing from the line's ink width"""
    f = ImageFont.truetype(MONO, 1000); cap = f.getbbox("H")[3] - f.getbbox("H")[1]
    fs = cap_pt / (cap / 1000)
    plain = pdfmetrics.stringWidth(text, "JBMono", fs)
    lsb = f.getbbox(text[0])[0] / 1000 * fs; rsb = (f.getlength(text[-1]) - f.getbbox(text[-1])[2]) / 1000 * fs
    ls = (extent_pt + lsb + rsb - plain) / max(1, len(text) - 1)
    return fs, ls, lsb

def rgb(c): return tuple(float(v) / 255 for v in c)

class Patcher:
    def __init__(self, pdf):
        self.pdf = pdf; r = PdfReader(pdf); p = r.pages[0]
        self.W, self.H = float(p.mediabox.width), float(p.mediabox.height)
        self.buf = io.BytesIO(); self.c = canvas.Canvas(self.buf, pagesize=(self.W, self.H))

    def line(self, box, old, new, cover=None, x=None, base=None, m=None):
        """replace one line of mono text: measure `old` inside box, cover it, set `new` in the same face, size and spacing"""
        m = m or measure(self.pdf, box)
        fs, ls, lsb = mono_fit(m["base"] - m["top"], m["right"] - m["left"], old)
        c = self.c; cx0, cy0, cx1, cy1 = cover or (m["left"] - 4, m["top"] - 6, m["right"] + 4, m["base"] + 6)
        c.setFillColorRGB(*rgb(m["bg"])); c.rect(cx0, self.H - cy1, cx1 - cx0, cy1 - cy0, stroke=0, fill=1)
        t = c.beginText(); t.setFont("JBMono", fs); t.setCharSpace(ls); t.setFillColorRGB(*rgb(m["ink"]))
        t.setTextOrigin((x if x is not None else m["left"]) - lsb, self.H - (base if base is not None else m["base"])); t.textOut(new); c.drawText(t)
        return m, fs, ls

    def image(self, im, box):
        x0, y0, x1, y1 = box; p = f"{WORK}/patch-{abs(hash(box)) % 99991}.png"; im.save(p)
        self.c.drawImage(p, x0, self.H - y1, x1 - x0, y1 - y0, mask="auto")

    def done(self):
        self.c.showPage(); self.c.save(); self.buf.seek(0); return PdfReader(self.buf).pages[0]

def apricot(P):
    # the taped strip, redrawn on its own geometry (apricot.py, 4 ft stand): coral band 1.2 W wide, 1.8u tall, rotated -1.6°
    Wpx, Hpx = 4611, 6901; u = Wpx / 100; fx, fy = P.W / Wpx, P.H / Hpx
    base_h = 12 * 96 / 2.54; qr = min(max(.15 * Wpx, 8 * 96 / 2.54), 12 * 96 / 2.54); tick = 1.8 * u
    tyk = Hpx - base_h - (qr + 2.4 * u) - tick - 1.2 * u
    cx, cy, w, h = .5 * Wpx * fx, (tyk + tick / 2) * fy, 1.2 * Wpx * fx, tick * fy
    fs = tick * .40 * fx; ls = .24 * fs
    c = P.c; c.saveState(); c.translate(cx, P.H - cy); c.rotate(1.6)
    c.setFillColorRGB(*rgb((224, 121, 90))); c.rect(-w / 2 - 3, -h / 2 - 2, w + 6, h + 4, stroke=0, fill=1)
    t = c.beginText(); t.setFont("JBMono", fs); t.setCharSpace(ls); t.setFillColorRGB(*rgb((255, 248, 245)))
    capH = 0.73 * fs; t.setTextOrigin(-w / 2, -capH / 2); t.textOut("SURGICAL STAINLESS STEEL · 18K GOLD TONE · NAIRA PETITE · " * 9); c.drawText(t)
    c.restoreState()
    # Brushed Gold Huggies sticker: ₹1,099 -> ₹999. The whole sticker is redrawn with the standee's own PLU drawing
    # (base.plu_svg, minus its drop shadow, which stays from the original) at the size and centre fitted to the old one.
    box = (560, 3940, 1000, 4250)
    a = render(P.pdf, box).astype(np.uint8); ri = a.astype(int)
    coral = (ri[..., 0] > 185) & (ri[..., 1] > 85) & (ri[..., 1] < 175) & (ri[..., 2] > 55) & (ri[..., 2] < 160) & (ri[..., 0] - ri[..., 2] > 70)
    n, lab, st, _ = cv2.connectedComponentsWithStats(coral.astype(np.uint8), 8)
    big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    hull = cv2.convexHull(np.argwhere(lab == big)[:, ::-1].astype(np.int32))
    (ex, ey), (ea, eb), _ = cv2.fitEllipse(hull)
    cx_pt, cy_pt = box[0] + ex / K, box[1] + ey / K
    rx_css = max(ea, eb) / 2 / K / .75
    w = rx_css / (.5 - 4 / 260) * 1.015      # a touch larger, so no edge of the old sticker shows
    sticker_png(w, cx_pt / .75 - box[0] / .75, cy_pt / .75 - box[1] / .75, (box[2] - box[0]) / .75, (box[3] - box[1]) / .75, f"{WORK}/sticker.png")
    P.image(Image.open(f"{WORK}/sticker.png"), box)

def plu_svg(w, price_txt, top_txt, bot_txt, code, col, ink):
    """base.plu_svg from the colour-camp standees, without the drop-shadow ellipse"""
    k = w / 260; h = w * 0.72; rx, ry = w / 2 - 4 * k, h / 2 - 4 * k; cx, cy = w / 2, h / 2; u = f"{code}{int(w)}"
    return f'''<svg width="{w:.1f}" height="{h:.1f}" viewBox="0 0 {w:.1f} {h:.1f}" style="overflow:visible;display:block">
<defs><path id="pt{u}" d="M {cx-rx*0.78:.1f},{cy+2*k:.1f} A {rx*0.78:.1f},{ry*0.74:.1f} 0 0,1 {cx+rx*0.78:.1f},{cy+2*k:.1f}"/>
<path id="pb{u}" d="M {cx-rx*0.80:.1f},{cy-4*k:.1f} A {rx*0.80:.1f},{ry*0.80:.1f} 0 0,0 {cx+rx*0.80:.1f},{cy-4*k:.1f}"/>
<linearGradient id="gl{u}" x1="0" y1="0" x2="0.6" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".30"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{col}"/>
<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx-9*k:.1f}" ry="{ry-9*k:.1f}" fill="none" stroke="{ink}" stroke-width="{1.6*k:.2f}" stroke-opacity=".85"/>
<text font-family="JetBrains Mono" font-size="{w*0.052:.1f}" letter-spacing="{2.4*k:.1f}" fill="{ink}"><textPath href="#pt{u}" startOffset="50%" text-anchor="middle">{top_txt}</textPath></text>
<text x="{cx:.1f}" y="{cy+w*0.07:.1f}" text-anchor="middle" font-family="Jost" font-weight="600" font-size="{w*0.20:.1f}" fill="{ink}">{price_txt}</text>
<text font-family="JetBrains Mono" font-size="{w*0.046:.1f}" letter-spacing="{1.8*k:.1f}" fill="{ink}"><textPath href="#pb{u}" startOffset="50%" text-anchor="middle">{bot_txt}</textPath></text>
<text x="{cx:.1f}" y="{cy+ry*0.58:.1f}" text-anchor="middle" font-family="JetBrains Mono" font-size="{w*0.040:.1f}" letter-spacing="{1.5*k:.1f}" fill="{ink}" fill-opacity=".8">PLU {code}</text>
<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="url(#gl{u})"/>
</svg>'''

def sticker_png(w, cx, cy, pw, ph, out):
    svg = plu_svg(w, "₹999", "NAIRA PETITE · APRICOT", "BRUSHED HUGGIES · 12MM", "14776", "#E0795A", "#FFF8F5")
    page = (f"<!doctype html><html><head><meta charset='utf-8'><style>@font-face{{font-family:'JetBrains Mono';src:url('file://{MONO}')}}"
            f"@font-face{{font-family:Jost;src:url('file://{JOST}');font-weight:100 900}}html,body{{margin:0;background:transparent}}</style></head>"
            f"<body><div style='position:absolute;left:{cx - w / 2:.2f}px;top:{cy - .36 * w:.2f}px;transform:rotate(-8deg)'>{svg}</div></body></html>")
    open(f"{WORK}/sticker.html", "w").write(page)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{round(pw)},height:{round(ph)}}},deviceScaleFactor:{K * .75}}});"
          f"await p.goto('file://{WORK}/sticker.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);"
          f"await p.screenshot({{path:'{out}',omitBackground:true}});await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True, env=dict(os.environ, NODE_PATH="/opt/node-tools/node_modules"))

def sage(P):
    P.line((700, 4725, 1700, 4795), "WATERPROOF · SURGICAL STAINLESS STEEL", "SURGICAL STAINLESS STEEL · 18K GOLD TONE")
    P.line((645, 2552, 1560, 2612), "6MM STEEL BEADS · GOLD TOGGLE · 15MM HEART", "6MM STEEL BEADS · GOLD-TONE TOGGLE · 15MM HEART")
    P.line((1283, 3737, 2240, 3796), "16.8 × 15.7MM DOME · GOLD GRANULATION · NO STONES", "16.8 × 15.7MM DOME · GOLD-TONE GRANULATION · NO STONES")
    # the QR was ivory on green, which most phone cameras will not read: an ivory tile with green modules, as on Apricot
    # and Lilac, over the old code's footprint (x 310-663, y 4645-4999 px at 150 ppi on the 24 × 36 in page)
    sx, sy = P.W / 1728 * .48, P.H / 2592 * .48; pad = 16
    x0, y0, x1, y1 = (310 - pad) * sx, (4645 - pad) * sy, (663 + pad) * sx, (4999 + pad) * sy
    c = P.c; c.setFillColorRGB(*rgb((245, 244, 237))); c.roundRect(x0, P.H - y1, x1 - x0, y1 - y0, 13 * sx, stroke=0, fill=1)
    q = segno.make("https://nairaflore.com/?utm_source=stall", error="m"); mx = q.matrix; n = len(mx)
    m = (x1 - x0) / (n + 3); qx, qy = x0 + 1.5 * m, y0 + 1.5 * m
    c.setFillColorRGB(*rgb((31, 58, 49)))
    for r, row in enumerate(mx):
        for k, v in enumerate(row):
            if v: c.rect(qx + k * m, P.H - (qy + (r + 1) * m), m * 1.002, m * 1.002, stroke=0, fill=1)

def lilac(P):
    m1 = measure(P.pdf, (2685, 1408, 2990, 1476))            # WATERPROOF
    m2 = measure(P.pdf, (2685, 1468, 3220, 1536))            # SURGICAL STAINLESS
    m3 = measure(P.pdf, (2685, 1527, 2990, 1594))            # STEEL
    m4 = measure(P.pdf, (2685, 1587, 3100, 1656))            # RHODIUM PLATED
    cover = (2680, m1["top"] - 8, 3230, m4["base"] + 10)
    P.line(None, "WATERPROOF", "SURGICAL STAINLESS", cover=cover, x=m1["left"], base=m1["base"], m=m1)
    P.line(None, "STEEL", "STEEL", cover=(0, 0, 0, 0), x=m1["left"], base=m2["base"], m=m3)
    P.line(None, "RHODIUM PLATED", "RHODIUM PLATED", cover=(0, 0, 0, 0), x=m1["left"], base=m3["base"], m=m4)
    P.line((660, 4548, 1660, 4612), "WATERPROOF · SURGICAL STAINLESS STEEL", "SURGICAL STAINLESS STEEL")

def band_text(page_w, colour_rgb, text="NAIRA PETITE  ·  SOFTLY, SLOWLY, WORN."):
    """the stand base (bottom 170 pt at 24 × 36 in) with one quiet line, as an overlay at final size"""
    b = io.BytesIO(); c = canvas.Canvas(b, pagesize=(1728, 2592))
    pdfmetrics.registerFont(TTFont("JostM", f"{SP}/c4/fonts/Jost-Medium.ttf"))
    fs = 22; ls = .42 * fs; w = pdfmetrics.stringWidth(text, "JostM", fs) + ls * (len(text) - 1)
    t = c.beginText(); t.setFont("JostM", fs); t.setCharSpace(ls); t.setFillColorRGB(*colour_rgb)
    t.setTextOrigin((1728 - w) / 2, 170 / 2 - fs * .35); t.textOut(text); c.drawText(t)
    c.showPage(); c.save(); b.seek(0); return PdfReader(b).pages[0]

def main():
    os.makedirs(WORK, exist_ok=True); os.makedirs(f"{OUT}/previews", exist_ok=True)
    for key, n, name in CAMPS:
        pdf = f"{SRC}/{key}-4x6ft.pdf"; P = Patcher(pdf)
        {"A-apricot": apricot, "B-sage": sage, "C-lilac": lilac}[key](P)
        over = P.done(); page = PdfReader(pdf).pages[0]; page.merge_page(over)
        out = PageObject.create_blank_page(width=1728, height=2592)
        out.merge_transformed_page(page, Transformation().scale(1728 / P.W, 2592 / P.H))
        out.merge_page(band_text(1728, (1.0, 0.973, 0.96)))
        w = PdfWriter(); w.add_page(out); w.add_metadata({"/Title": f"Naira Petite stall poster - {name} - 24 x 36 in"})
        dst = f"{OUT}/Naira-Stall-back-{n}-{name}-24x36in"
        with open(dst + ".pdf", "wb") as f: w.write(f)
        subprocess.run(["pdftoppm", "-r", "150", "-jpeg", "-jpegopt", "quality=92", "-singlefile", dst + ".pdf", dst], check=True)
        subprocess.run(["pdftoppm", "-scale-to-x", "600", "-scale-to-y", "900", "-jpeg", "-singlefile", dst + ".pdf",
                        f"{OUT}/previews/Naira-Stall-back-{n}-{name}-24x36in"], check=True)
        print(dst + ".pdf")

if __name__ == "__main__":
    main()
