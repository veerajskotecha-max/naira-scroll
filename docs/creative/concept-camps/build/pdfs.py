# Builds one PDF per camp (cover, board, plan, then one verified photograph per page at full resolution) and a master board PDF.
# The photographs are embedded as high-quality JPEGs at their native 2K size so they can be lifted straight into Claude Design.
# Usage: pdfs.py <final.json> <outdir>
import json, os, sys
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab import rl_config
from fontTools.ttLib import TTFont as FTFont
rl_config.useA85 = 0   # embed the JPEG bytes as they are, without ASCII85 inflation

HERE = os.path.dirname(os.path.abspath(__file__))
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/c4"
FONTS = f"{SP}/fonts"
for name, file in [("Velista", "Velista.ttf"), ("Jost", "Jost-Regular.ttf"), ("JostMed", "Jost-Medium.ttf"),
                   ("CormIt", "Cormorant-Italic.ttf"), ("Corm", "Cormorant-Regular.ttf")]:
    pdfmetrics.registerFont(TTFont(name, f"{FONTS}/{file}"))

CMAP = {"Jost": set(FTFont(f"{FONTS}/Jost-Regular.ttf").getBestCmap()), "JostMed": set(FTFont(f"{FONTS}/Jost-Medium.ttf").getBestCmap()),
        "Velista": set(FTFont(f"{FONTS}/Velista.ttf").getBestCmap())}
def face(font, ch):
    # Jost and Velista have no rupee sign; Cormorant does
    return font if font not in CMAP or ord(ch) in CMAP[font] else "Corm"

CREAM, INK, BLUSH, GOLD = HexColor("#F4F0E8"), HexColor("#1C1C1C"), HexColor("#FBEDE9"), HexColor("#B8924A")
MUTE = HexColor("#6E625A")
PW, PH = 1200, 1700          # every page, points; a 4:5 photograph fills 1200 x 1500
IMG_H = 1500
ACCENT = {"toggle": "#D8A9A1", "woven": "#E9C7A8", "heart": "#F0C4BE", "prism": "#A9D9DE"}
PALETTE = {
 "toggle": [("Blush", "#FBEDE9"), ("Dusty rose", "#D8A9A1"), ("Warm ivory", "#F4F0E8"), ("Peach", "#F2CFC4"), ("Gold", "#C9A55C"), ("Ink", "#1C1C1C")],
 "woven":  [("Warm ivory", "#F4F0E8"), ("Blush thread", "#EFC9C0"), ("Peach", "#F2CFC4"), ("Honey wood", "#D9B48A"), ("Gold", "#C9A55C"), ("Ink", "#1C1C1C")],
 "heart":  [("ECG blush", "#F7DCD6"), ("Coral grid", "#E79C82"), ("Warm ivory", "#F4F0E8"), ("Mirror silver", "#C9C9CC"), ("Gold", "#C9A55C"), ("Ink", "#1C1C1C")],
 "prism":  [("Aqua", "#A9D9DE"), ("Soft pink", "#F4C2CC"), ("Butter yellow", "#F3E6A6"), ("Warm ivory", "#F4F0E8"), ("Rhodium", "#D7D9DC"), ("Ink", "#1C1C1C")],
}
FORMAT = {"4:5": "Feed 4:5", "9:16": "Story / Reel 9:16"}

def wrap(c, text, font, size, width):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width: cur = t
        else: lines.append(cur); cur = wd
    if cur: lines.append(cur)
    return lines

def para(c, text, font, size, x, y, width, lead=1.35, color=INK):
    c.setFillColor(color); c.setFont(font, size)
    for ln in wrap(c, text, font, size, width):
        c.drawString(x, y, ln); y -= size * lead
    return y

def tracked(c, text, font, size, x, y, track=0.18, color=INK, align="left"):
    c.setFillColor(color)
    w = sum(pdfmetrics.stringWidth(ch, face(font, ch), size) for ch in text) + track * size * (len(text) - 1)
    if align == "center": x -= w / 2
    elif align == "right": x -= w
    for ch in text:
        f = face(font, ch); c.setFont(f, size)
        c.drawString(x, y, ch); x += pdfmetrics.stringWidth(ch, f, size) + track * size

def jpeg(src, dst, q=90, maxw=None):
    if not os.path.exists(dst):
        im = Image.open(src).convert("RGB")
        if maxw and im.width > maxw: im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
        im.save(dst, quality=q, optimize=True, progressive=False, subsampling=0)
    return dst

def bg(c, color=CREAM):
    c.setFillColor(color); c.rect(0, 0, PW, PH, stroke=0, fill=1)

def footer(c, left, right):
    tracked(c, left, "Jost", 13, 60, 40, 0.16, MUTE)
    tracked(c, right, "Jost", 13, PW - 60, 40, 0.16, MUTE, "right")

def cover(c, camp, D, frames, files, n):
    P, C = D["pieces"][camp], D["camps"][camp]
    bg(c)
    tracked(c, f"NAIRA PETITE  ·  CONCEPT CAMP {n:02d}  ·  OCTOBER 2026", "JostMed", 16, 60, PH - 80, 0.22)
    c.setFillColor(INK); c.setFont("Velista", 104)
    y = PH - 230
    for ln in wrap(c, C["title"], "Velista", 104, PW - 120):
        c.drawString(60, y, ln); y -= 112
    y = para(c, C["line"], "CormIt", 46, 60, y - 10, PW - 120, 1.2)
    tracked(c, f"{P['name'].upper()}   ·   {P['price']}   ·   SKU {P['sku']}   ·   {P['stock']} IN STOCK (SHOPIFY, 15 OCT 2026)",
            "Jost", 15, 60, y - 18, 0.12, MUTE)
    y = para(c, C["idea"], "Corm", 27, 60, y - 80, 560, 1.38)
    # hero photograph on the right
    hero = files[0]
    im = Image.open(hero); w, h = im.size; tw = 500; th = tw * h / w
    c.drawImage(ImageReader(hero), PW - 60 - tw, PH - 470 - th, tw, th)
    # palette
    py = 330
    tracked(c, "PALETTE", "JostMed", 14, 60, py + 120, 0.25, MUTE)
    for i, (nm, hx) in enumerate(PALETTE[camp]):
        x = 60 + i * 180
        c.setFillColor(HexColor(hx)); c.setStrokeColor(HexColor("#D9D2C7")); c.rect(x, py, 150, 90, stroke=1, fill=1)
        tracked(c, nm.upper(), "Jost", 12, x, py - 24, 0.12, INK); tracked(c, hx, "Jost", 12, x, py - 44, 0.12, MUTE)
    tracked(c, "TYPE", "JostMed", 14, 60, 190, 0.25, MUTE)
    para(c, "Velista for names, Jost tracked capitals for prices and labels, Cormorant Garamond italic for the single line. "
            "Tone-on-tone ink. Keep the top 250 px and the bottom reply bar of stories free of text.", "Corm", 22, 60, 158, PW - 120, 1.3)
    footer(c, "BUILT FOR CLAUDE DESIGN  ·  EVERY PHOTOGRAPH IS ON ITS OWN PAGE AT FULL RESOLUTION", f"{len(frames)} VERIFIED FRAMES")
    c.showPage()

def board(c, camp, D, frames, thumbs, title=True):
    C = D["camps"][camp]
    bg(c)
    if title:
        tracked(c, "THE BOARD", "JostMed", 16, 60, PH - 80, 0.25, MUTE)
        c.setFillColor(INK); c.setFont("Velista", 54); c.drawString(60, PH - 150, C["title"])
    cols, gx, gy, top = 4, 22, 70, PH - 200
    cw = (PW - 120 - gx * (cols - 1)) / cols
    rows = (len(frames) + cols - 1) // cols
    ch_max = (top - 90 - gy * rows) / rows
    y = top
    for r in range(rows):
        row = frames[r * cols:(r + 1) * cols]; rh = 0
        for i, f in enumerate(row):
            im = Image.open(thumbs[f["id"]]); w, h = im.size
            tw = cw; th = tw * h / w
            if th > ch_max: th = ch_max; tw = th * w / h
            x = 60 + i * (cw + gx) + (cw - tw) / 2
            c.drawImage(ImageReader(thumbs[f["id"]]), x, y - th, tw, th); rh = max(rh, th)
        for i, f in enumerate(row):
            x = 60 + i * (cw + gx)
            tracked(c, f"{f['id']}  {f['name'].upper()}", "Jost", 11, x, y - rh - 22, 0.1, INK)
            tracked(c, FORMAT[f["aspect"]].upper(), "Jost", 10, x, y - rh - 40, 0.1, MUTE)
        y -= rh + gy
    footer(c, "NAIRA PETITE", "THE BOARD")
    c.showPage()

def plan(c, camp, D, frames, verdicts):
    C = D["camps"][camp]
    bg(c)
    tracked(c, "THE PLAN", "JostMed", 16, 60, PH - 80, 0.25, MUTE)
    c.setFillColor(INK); c.setFont("Velista", 54); c.drawString(60, PH - 150, C["title"])
    y = PH - 230
    cols = [(60, "FRAME"), (150, "CONCEPT"), (560, "FORMAT"), (760, "HEADLINE"), (1040, "CHECK")]
    for x, t in cols: tracked(c, t, "JostMed", 12, x, y, 0.2, MUTE)
    y -= 18; c.setStrokeColor(HexColor("#D9D2C7")); c.line(60, y, PW - 60, y); y -= 34
    for f in frames:
        v = verdicts.get(f["id"], {})
        concept = f.get("concept", f["name"])
        lines = wrap(c, concept, "Corm", 19, 390)
        hl = wrap(c, f["copy"], "CormIt", 21, 260)
        n = max(len(lines), len(hl), 1)
        tracked(c, f["id"], "JostMed", 13, 60, y, 0.1)
        yy = y
        for ln in lines: c.setFont("Corm", 19); c.setFillColor(INK); c.drawString(150, yy, ln); yy -= 24
        tracked(c, FORMAT[f["aspect"]].upper(), "Jost", 11, 560, y, 0.1, MUTE)
        yy = y
        for ln in hl: c.setFont("CormIt", 21); c.setFillColor(INK); c.drawString(760, yy, ln); yy -= 25
        chk = f"PASS {v['score']:.1f}" if v.get("score") is not None else "PASS"
        tracked(c, chk, "Jost", 12, 1040, y, 0.1, INK)
        y -= max(n, 1) * 25 + 22
        c.setStrokeColor(HexColor("#E6DFD4")); c.line(60, y + 12, PW - 60, y + 12); y -= 12
    y -= 30
    tracked(c, "USING THESE PHOTOGRAPHS", "JostMed", 13, 60, y, 0.25, MUTE); y -= 36
    for t in ["Feed ads: 1080 × 1350 (4:5). Stories and Reels: 1080 × 1920 (9:16); keep the top 250 px and the bottom reply bar free of text.",
              "Every photograph leaves calm space for one headline. Set the headline in Cormorant italic, the name in Velista and the price in Jost.",
              "The photographs carry no text, logo or price. Add the wordmark and price in Claude Design, never on top of the piece.",
              "Each frame passed a check against the real listing photos: construction, stones, metal, scale, no face, no text."]:
        y = para(c, "·  " + t, "Corm", 20, 60, y, PW - 120, 1.3) - 8
    footer(c, "EVERY FRAME CHECKED AGAINST THE SHOPIFY LISTING PHOTOS", "NAIRA PETITE")
    c.showPage()

def photo(c, camp, D, f, path, v):
    bg(c)
    im = Image.open(path); w, h = im.size
    if f["aspect"] == "4:5" or w / h > 0.7:
        dw = PW; dh = PW * h / w
        if dh > IMG_H: dh = IMG_H; dw = IMG_H * w / h
    else:
        dh = IMG_H; dw = IMG_H * w / h
    x = (PW - dw) / 2; y = PH - dh
    c.drawImage(ImageReader(path), x, y, dw, dh)
    by = PH - IMG_H - 70
    tracked(c, f"{f['id']}  ·  {f['name'].upper()}  ·  {FORMAT[f['aspect']].upper()}  ·  {w}×{h}px", "JostMed", 14, 60, by, 0.14)
    c.setFillColor(INK); c.setFont("CormIt", 40); c.drawString(60, by - 60, f["copy"])
    chk = "VERIFIED AGAINST LISTING" + (f"  ·  AD SCORE {v['score']:.1f}/10" if v.get("score") is not None else "")
    tracked(c, chk, "Jost", 12, PW - 60, by, 0.14, MUTE, "right")
    tracked(c, D["pieces"][camp]["name"].upper() + "  ·  " + D["pieces"][camp]["price"], "Jost", 12, PW - 60, by - 52, 0.14, MUTE, "right")
    c.showPage()

def main():
    sel = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    D = json.load(open(f"{HERE}/frames.json"))
    idx = {f["id"]: f for f in D["frames"]}
    jdir = f"{SP}/jpg"; os.makedirs(jdir, exist_ok=True)
    order = ["toggle", "woven", "heart", "prism"]
    master_frames = {}
    for n, camp in enumerate(order, 1):
        if camp not in sel: continue
        items = sel[camp]
        frames = [dict(idx[it["id"]], concept=it.get("concept", idx[it["id"]]["name"])) for it in items]
        files = [jpeg(f"{SP}/plates/{it['file']}", f"{jdir}/{it['file'].rsplit('.',1)[0]}.jpg", 90) for it in items]
        thumbs = {it["id"]: jpeg(f"{SP}/plates/{it['file']}", f"{jdir}/{it['file'].rsplit('.',1)[0]}_t.jpg", 85, 700) for it in items}
        verdicts = {it["id"]: it for it in items}
        name = D["pieces"][camp]["name"].replace(" ", "-").replace("è", "e")
        pdf = f"{out}/Naira-Camp-{n:02d}-{D['camps'][camp]['title'].title().replace(' ', '').replace(',', '')}-{name}.pdf"
        c = canvas.Canvas(pdf, pagesize=(PW, PH)); c.setTitle(f"Naira Petite · {D['camps'][camp]['title']} · {D['pieces'][camp]['name']}")
        c.setAuthor("Naira Petite"); c.setSubject("Concept camp: verified ad photographs for Claude Design")
        cover(c, camp, D, frames, files, n); board(c, camp, D, frames, thumbs); plan(c, camp, D, frames, verdicts)
        for f, p in zip(frames, files): photo(c, camp, D, f, p, verdicts[f["id"]])
        c.save(); print(pdf, round(os.path.getsize(pdf) / 1e6, 1), "MB")
        master_frames[camp] = (frames, thumbs, files)
    # master board: cover + one board per camp
    pdf = f"{out}/Naira-Concept-Camps-Board.pdf"
    c = canvas.Canvas(pdf, pagesize=(PW, PH)); c.setTitle("Naira Petite · Concept camps · Board")
    bg(c)
    tracked(c, "NAIRA PETITE  ·  OCTOBER 2026", "JostMed", 16, 60, PH - 80, 0.22)
    c.setFillColor(INK); c.setFont("Velista", 96); c.drawString(60, PH - 220, "Concept Camps")
    y = para(c, "Four in-stock pieces, four ideas, forty photographs. Each one checked against its listing.", "CormIt", 40, 60, PH - 300, PW - 120, 1.25)
    y -= 40
    for n, camp in enumerate(order, 1):
        if camp not in master_frames: continue
        P, C = D["pieces"][camp], D["camps"][camp]
        frames, thumbs, files = master_frames[camp]
        c.setFillColor(HexColor(ACCENT[camp])); c.rect(60, y - 210, 16, 210, stroke=0, fill=1)
        tracked(c, f"CAMP {n:02d}  ·  {P['name'].upper()}  ·  {P['price']}  ·  {P['stock']} IN STOCK", "JostMed", 13, 100, y - 18, 0.14, MUTE)
        c.setFillColor(INK); c.setFont("Velista", 44); c.drawString(100, y - 72, C["title"])
        para(c, C["line"], "CormIt", 26, 100, y - 112, 560, 1.2)
        # three thumbnails
        tx = PW - 60
        for f in reversed(frames[:3]):
            im = Image.open(thumbs[f["id"]]); w, h = im.size; th = 210; tw = th * w / h; tx -= tw
            c.drawImage(ImageReader(thumbs[f["id"]]), tx, y - 210, tw, th); tx -= 14
        y -= 270
    footer(c, "BUILT FOR CLAUDE DESIGN", "ONE PDF PER CAMP FOLLOWS")
    c.showPage()
    for camp in order:
        if camp in master_frames:
            frames, thumbs, files = master_frames[camp]; board(c, camp, D, frames, thumbs)
    c.save(); print(pdf, round(os.path.getsize(pdf) / 1e6, 1), "MB")

if __name__ == "__main__":
    main()
