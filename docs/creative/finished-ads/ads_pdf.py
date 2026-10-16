# Builds Naira-Ready-To-Run-Ads.pdf: a cover with every finished ad, then one ad per page at its exact pixel size (1 px = 1 pt),
# then the plain controls (controls.json) to run beside them, for Claude Design or a media buyer. Scores from the newest review.
# Usage: ads_pdf.py <outdir>
import glob, json, os, sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config
from PIL import Image
rl_config.useA85 = 0

HERE = os.path.dirname(os.path.abspath(__file__))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
FONTS = f"{SPB}/c4/fonts"
for n, f in [("Velista", "Velista.ttf"), ("CormIt", "Cormorant-Italic.ttf"), ("Corm", "Cormorant-Regular.ttf"), ("Jost", "Jost-Regular.ttf"), ("JostMed", "Jost-Medium.ttf")]:
    pdfmetrics.registerFont(TTFont(n, f"{FONTS}/{f}"))
PAPER, INK, MUTE = HexColor("#F4F0E8"), HexColor("#1C1C1C"), HexColor("#6B5F57")

def tracked(c, text, font, size, x, y, spacing=0.2, color=INK, align="left"):
    c.setFont(font, size); c.setFillColor(color)
    w = sum(pdfmetrics.stringWidth(ch, font, size) + size * spacing for ch in text) - size * spacing
    x = x - w if align == "right" else x
    for ch in text:
        c.drawString(x, y, ch); x += pdfmetrics.stringWidth(ch, font, size) + size * spacing

def main():
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    ads = json.load(open(f"{HERE}/ads.json"))["ads"]
    reviews = sorted(glob.glob(f"{HERE}/review_r[0-9].json") + glob.glob(f"{HERE}/review_r[0-9][0-9].json"), key=os.path.getmtime)
    sigf = reviews[-1][:-5] + ".sig.json" if reviews else ""
    sig = json.load(open(sigf)) if sigf and os.path.exists(sigf) else {}
    cur = {a["id"]: json.dumps({k: v for k, v in a.items() if k not in ("id", "src")}, sort_keys=True, ensure_ascii=False) for a in ads}
    score = {r["id"]: r["score"] for r in json.load(open(reviews[-1])) if sig.get(r["id"]) == cur.get(r["id"])} if reviews else {}
    pdf = f"{out}/Naira-Ready-To-Run-Ads.pdf"
    c = canvas.Canvas(pdf); c.setTitle("Naira Petite · Ready-to-run ads"); c.setAuthor("Naira Petite")
    PW, PH = 1200, 1700; c.setPageSize((PW, PH)); c.setFillColor(PAPER); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    tracked(c, "NAIRA PETITE  ·  READY-TO-RUN ADS  ·  OCTOBER 2026", "JostMed", 16, 60, PH - 80, 0.22)
    c.setFillColor(INK); c.setFont("Velista", 96); c.drawString(60, PH - 220, "Ready to run")
    c.setFont("CormIt", 30)
    c.drawString(60, PH - 280, f"{len(ads)} finished ads from the keepers, Feed and Stories: the pun, a plain correction and the exact price.")
    cols, gx, gy = 9, 16, 46; cw = (PW - 120 - gx * (cols - 1)) / cols; y = PH - 330
    for i in range(0, len(ads), cols):
        row = ads[i:i + cols]; rh = 0
        for k, a in enumerate(row):
            p = f"{SPB}/ads/out/{a['id']}.jpg"; w, h = Image.open(p).size; th = cw * h / w
            c.drawImage(ImageReader(p), 60 + k * (cw + gx), y - th, cw, th); rh = max(rh, th)
            s = score.get(a["id"]); tracked(c, a["id"] + (f"  ·  {s:.1f}" if s is not None else ""), "Jost", 10, 60 + k * (cw + gx), y - th - 18, 0.1, MUTE)
        y -= rh + gy
    c.showPage()
    for a in ads:
        p = f"{SPB}/ads/out/{a['id']}.jpg"; w, h = Image.open(p).size
        c.setPageSize((w, h)); c.drawImage(ImageReader(p), 0, 0, w, h); c.showPage()
    ctl = [a for a in json.load(open(f"{HERE}/controls.json"))["ads"] if os.path.exists(f"{SPB}/ads/out/{a['id']}.jpg")]
    if ctl:
        c.setPageSize((1080, 1350)); c.setFillColor(PAPER); c.rect(0, 0, 1080, 1350, stroke=0, fill=1)
        tracked(c, "THE CONTROL FOR EACH TEST", "JostMed", 16, 72, 1350 - 90, 0.22, MUTE)
        c.setFillColor(INK); c.setFont("Velista", 72); c.drawString(72, 1350 - 200, "Plain close-ups")
        c.setFont("CormIt", 30)
        for i, line in enumerate(["Run each crazy ad beside the plain close-up of the same", "piece, in the same ad set, and judge on cost per purchase."]):
            c.drawString(72, 1350 - 270 - i * 40, line)
        c.showPage()
        for a in ctl:
            p = f"{SPB}/ads/out/{a['id']}.jpg"; w, h = Image.open(p).size
            c.setPageSize((w, h)); c.drawImage(ImageReader(p), 0, 0, w, h); c.showPage()
    c.save(); print(pdf, round(os.path.getsize(pdf) / 1e6, 1), "MB")

if __name__ == "__main__":
    main()
