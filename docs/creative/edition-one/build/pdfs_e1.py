# Builds the Edition One PDF for Claude Design: cover, what the ad data says, the board, then one verified photograph per page at
# full resolution, then the next shoot. Reuses the fonts and drawing helpers of the concept-camps builder.
# Usage: pdfs_e1.py <final_e1.json> <outdir>
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "concept-camps", "build"))
import pdfs as base
from pdfs import tracked, para, wrap, bg, footer, jpeg, PW, PH, IMG_H, INK, MUTE, CREAM, FORMAT
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image

SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/e1"
ORDER = ["aqua", "quatrefoil", "cluster", "halo", "verdant", "riviere", "papillon", "torsade", "dome", "square", "bow"]   # ₹ high to low
DATA = [
    ("1.44×", "ROAS of concept statics, against 0.57× for plain statics (Meta, lifetime, 108 ads, ₹1.59 lakh)"),
    ("10 of 10", "ad sets where concept beat plain on outbound click-through, side by side"),
    ("1.63×", "Prism Rivière concept ads: 12 of the 16 concept sales. Pieces over ₹2,000 pay back"),
    ("1.79×", "concept statics in the Instagram 4:5 Feed; Stories 1.36×; Reels lose money for statics"),
]
RULES = [
    "Make the piece the punchline of a visual pun that reads in the thumbnail. Food and candy worked best (\"Almost edible\").",
    "Lead with the ₹2,000+ pieces: Aqua Heart, Quatrefoil, Prism Cluster, Baguette Halo, Verdant.",
    "Light, pastel and cream grounds only; the dark plinth look returned 0.49×.",
    "4:5 Feed first, Stories second. Pair each headline with a plain-spoken correction and a real number.",
    "Run every crazy frame against a plain craft close-up of the same piece, in the same ad set, and judge on cost per purchase.",
]

def cover(c, D, final):
    bg(c)
    tracked(c, "NAIRA PETITE  ·  EDITION ONE  ·  OCTOBER 2026", "JostMed", 16, 60, PH - 80, 0.22)
    c.setFillColor(INK); c.setFont("Velista", 104); c.drawString(60, PH - 230, "Crazy Camps")
    y = para(c, "Eleven pre-order pieces. One everyday object wears each one. Every photograph checked against its listing.",
             "CormIt", 40, 60, PH - 300, PW - 120, 1.25)
    items = [it for k in ORDER for it in final.get(k, [])][:6]
    cols, gx = 3, 24; cw = (PW - 120 - gx * (cols - 1)) / cols; top = y - 40
    for i, it in enumerate(items):
        p = jpeg(f"{SP}/plates/{it['file']}", f"{SP}/jpg/{it['file'].rsplit('.',1)[0]}_t.jpg", 85, 700)
        im = Image.open(p); w, h = im.size; th = cw * h / w
        x = 60 + (i % cols) * (cw + gx); yy = top - (i // cols) * (th + 70)
        c.drawImage(ImageReader(p), x, yy - th, cw, th)
        tracked(c, f"{D['pieces'][it['camp']]['title'].upper()}", "Jost", 11, x, yy - th - 22, 0.12, INK)
        c.setFont("CormIt", 20); c.setFillColor(INK); c.drawString(x, yy - th - 48, it["copy"])
    footer(c, "BUILT FOR CLAUDE DESIGN  ·  EVERY PHOTOGRAPH IS ON ITS OWN PAGE AT FULL RESOLUTION", f"{sum(len(v) for v in final.values())} VERIFIED")
    c.showPage()

def data_page(c):
    bg(c)
    tracked(c, "WHAT THE AD DATA SAYS", "JostMed", 16, 60, PH - 80, 0.25, MUTE)
    c.setFillColor(INK); c.setFont("Velista", 54); c.drawString(60, PH - 150, "Crazy wins, mostly")
    y = para(c, "Naira's own Meta account, every jewellery ad to 12 Oct 2026, spend-weighted and corrected for nine friends-and-family "
                "orders. Concept-led ads beat plain ones, but the lead rests on one image and the data is thin: treat it as direction.",
             "Corm", 24, 60, PH - 200, PW - 120, 1.35)
    y -= 30
    for big, txt in DATA:
        c.setFillColor(INK); c.setFont("Velista", 60); c.drawString(60, y - 50, big)
        para(c, txt, "Corm", 22, 360, y - 22, PW - 420, 1.3); y -= 120
    y -= 10
    tracked(c, "RULES FOR THESE CAMPS", "JostMed", 13, 60, y, 0.25, MUTE); y -= 38
    for r in RULES:
        y = para(c, "·  " + r, "Corm", 22, 60, y, PW - 120, 1.3) - 10
    footer(c, "SOURCE: AD_PERFORMANCE.MD IN THE REPO", "NAIRA PETITE")
    c.showPage()

def board(c, D, final):
    items = [it for k in ORDER for it in final.get(k, [])]
    for start in range(0, len(items), 12):
        bg(c)
        tracked(c, "THE BOARD", "JostMed", 16, 60, PH - 80, 0.25, MUTE)
        c.setFillColor(INK); c.setFont("Velista", 54); c.drawString(60, PH - 150, "Edition One")
        chunk = items[start:start + 12]
        cols, gx, gy, top = 4, 22, 92, PH - 200
        cw = (PW - 120 - gx * (cols - 1)) / cols
        rows = (len(chunk) + cols - 1) // cols
        ch_max = (top - 90 - gy * rows) / max(rows, 1)
        y = top
        for r in range(rows):
            row = chunk[r * cols:(r + 1) * cols]; rh = 0
            for i, it in enumerate(row):
                p = jpeg(f"{SP}/plates/{it['file']}", f"{SP}/jpg/{it['file'].rsplit('.',1)[0]}_t.jpg", 85, 700)
                im = Image.open(p); w, h = im.size; tw = cw; th = tw * h / w
                if th > ch_max: th = ch_max; tw = th * w / h
                c.drawImage(ImageReader(p), 60 + i * (cw + gx) + (cw - tw) / 2, y - th, tw, th); rh = max(rh, th)
            for i, it in enumerate(row):
                x = 60 + i * (cw + gx)
                tracked(c, D["pieces"][it["camp"]]["title"].upper(), "Jost", 11, x, y - rh - 22, 0.1, INK)
                c.setFont("CormIt", 18); c.setFillColor(INK); c.drawString(x, y - rh - 46, it["copy"])
                tracked(c, f"{FORMAT[it['aspect']].upper()}  ·  {it['score']:.1f}", "Jost", 10, x, y - rh - 66, 0.1, MUTE)
            y -= rh + gy
        footer(c, "NAIRA PETITE", "THE BOARD")
        c.showPage()

def photo(c, D, it):
    bg(c)
    path = jpeg(f"{SP}/plates/{it['file']}", f"{SP}/jpg/{it['file'].rsplit('.',1)[0]}.jpg", 90)
    im = Image.open(path); w, h = im.size
    dw = PW; dh = PW * h / w
    if dh > IMG_H: dh = IMG_H; dw = IMG_H * w / h
    c.drawImage(ImageReader(path), (PW - dw) / 2, PH - dh, dw, dh)
    P = D["pieces"][it["camp"]]
    by = PH - IMG_H - 70
    tracked(c, f"{P['title'].upper()}  ·  {it['name'].upper()}  ·  {FORMAT[it['aspect']].upper()}  ·  {w}×{h}px", "JostMed", 14, 60, by, 0.14)
    c.setFillColor(INK); c.setFont("CormIt", 40); c.drawString(60, by - 60, it["copy"])
    tracked(c, f"VERIFIED AGAINST LISTING  ·  AD SCORE {it['score']:.1f}/10", "Jost", 12, PW - 60, by, 0.14, MUTE, "right")
    tracked(c, f"₹{P['price']:,}  ·  SKU {P['sku']}  ·  PRE-ORDER", "Jost", 12, PW - 60, by - 52, 0.14, MUTE, "right")
    c.showPage()

def next_page(c, D, final):
    bg(c)
    tracked(c, "NEXT SHOOT", "JostMed", 16, 60, PH - 80, 0.25, MUTE)
    c.setFillColor(INK); c.setFont("Velista", 54); c.drawString(60, PH - 150, "Still to make")
    y = para(c, "Pieces still short of four verified frames, with the ideas planned for the next credits. Scale is the usual reason a "
                "frame fails: the generator draws jewellery about 1.5 times too big next to a prop, so each prompt now asks for a smaller "
                "piece to land at true size.", "Corm", 22, 60, PH - 200, PW - 120, 1.35) - 20
    plan = json.load(open(f"{HERE}/frames.json"))["camps"]
    for k in ORDER:
        have = len(final.get(k, []))
        if have >= 4: continue
        P = D["pieces"][k]
        tracked(c, f"{P['title'].upper()}  ·  ₹{P['price']:,}  ·  {have} OF 4 VERIFIED", "JostMed", 12, 60, y, 0.14, INK)
        y = para(c, plan[k]["idea"], "Corm", 19, 60, y - 26, PW - 120, 1.3) - 16
        if y < 120: break
    footer(c, "NAIRA PETITE", "EDITION ONE")
    c.showPage()

def main():
    final = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True); os.makedirs(f"{SP}/jpg", exist_ok=True)
    D = json.load(open(f"{HERE}/frames.json"))
    for k, items in final.items():
        for it in items: it["camp"] = k
    pdf = f"{out}/Naira-Edition-One-Crazy-Camps.pdf"
    c = canvas.Canvas(pdf, pagesize=(PW, PH)); c.setTitle("Naira Petite · Edition One · Crazy Camps")
    c.setAuthor("Naira Petite"); c.setSubject("Verified ad photographs for Claude Design")
    cover(c, D, final); data_page(c); board(c, D, final)
    for k in ORDER:
        for it in final.get(k, []): photo(c, D, it)
    next_page(c, D, final)
    c.save(); print(pdf, round(os.path.getsize(pdf) / 1e6, 1), "MB")

if __name__ == "__main__":
    main()
