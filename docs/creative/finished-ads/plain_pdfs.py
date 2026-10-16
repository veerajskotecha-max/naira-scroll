# Builds the plain-image PDFs for Claude Design: every photograph made in this round with no copy on it, plus the store's own
# listing photos, each on its own page with a caption band (piece, price, frame, and the listing-check verdict), after a brand-kit
# page (the deck's wordmarks, palette and type, and the layout of the account's best ad). Files are split to stay under 14.5 MB,
# the artifact's limit for one file being 15 MB. Frames come from the contact sheet's data (<scratchpad>/sheet/index.html).
# Usage: plain_pdfs.py <outdir>     writes <outdir>/*.pdf and <outdir>/plain.json (what each PDF holds, for the page)
import glob, io, json, os, re, sys
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab import rl_config
rl_config.useA85 = 0

HERE = os.path.dirname(os.path.abspath(__file__)); CRE = os.path.normpath(f"{HERE}/..")
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
FONTS = f"{SPB}/c4/fonts"
for n, f in [("Velista", f"{HERE}/brand/Velista.ttf"), ("Jost", f"{FONTS}/Jost-Regular.ttf"), ("JostMed", f"{FONTS}/Jost-Medium.ttf"),
             ("CormIt", f"{FONTS}/Cormorant-Italic.ttf"), ("Corm", f"{FONTS}/Cormorant-Regular.ttf")]:
    pdfmetrics.registerFont(TTFont(n, f))
INK, PAPER, BLUSH, SAGE, PEACH, CORAL, MUTE = (HexColor(h) for h in ("#1A1614", "#FBF8F3", "#FFF8F5", "#99B4AE", "#F2C4B6", "#F0A08F", "#6E625A"))
LIMIT = 14.5e6; PW = 1200; CAP = 230; LONG = 2000

def jpg(path, long=LONG, q=84):
    im = Image.open(path).convert("RGB"); k = long / max(im.size)
    if k < 1: im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=q, optimize=True, progressive=False); return b.getvalue(), im.size

def tracked(c, text, font, size, x, y, track=0.2, color=INK):
    c.setFillColor(color); c.setFont(font, size)
    for ch in text:
        f = font if ch != "₹" else "Corm"; c.setFont(f, size); c.drawString(x, y, ch); x += pdfmetrics.stringWidth(ch, f, size) + track * size
    return x

def wrap(text, font, size, width):
    out, cur = [], ""
    for wd in text.split():
        t = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width: cur = t
        else: out.append(cur); cur = wd
    return out + ([cur] if cur else [])

def sheet_frames():
    s = open(f"{SPB}/sheet/index.html", encoding="utf-8").read()
    data = json.loads(re.search(r"const DATA = (\{.*?\});\n", s, re.S).group(1).replace("<\\/", "</"))
    return data["frames"]

def plate_path(f):
    return f"{SPB}/{f['tag']}/plates/{f['id']}.png"

STATUS = {"keep": "READY FOR ADS · KEEPER", "pass": "READY FOR ADS", "fail": "REFERENCE ONLY · FAILS THE LISTING CHECK",
          "scene": "A SET WITH NO PIECE IN IT · FOR COMPOSITES", "wait": "READY FOR ADS · COMPOSITE OF THE REAL LISTING PHOTO"}

def brand_page(c):
    c.setPageSize((PW, 1700)); c.setFillColor(BLUSH); c.rect(0, 0, PW, 1700, stroke=0, fill=1)
    tracked(c, "NAIRA PETITE  ·  BRAND KIT FOR THE ADS", "JostMed", 16, 72, 1620, 0.24, MUTE)
    for k, (f, bg) in enumerate([("logo_sage.png", BLUSH), ("logo_white.png", SAGE), ("logo_ink.png", PAPER)]):
        y = 1450 - k * 150; c.setFillColor(bg); c.rect(72, y - 20, 520, 130, stroke=0, fill=1)
        c.drawImage(ImageReader(f"{HERE}/brand/{f}"), 112, y + 4, 440, 98, mask="auto")
    c.setFillColor(INK); c.setFont("Corm", 22)
    for i, ln in enumerate(["The wordmark: sage on blush, white on sage, or black.", "In the ads it is black on light photographs and",
                            "white on dark ones: the sage reads about 2:1 on a photo.", "The tulip is the I. Keep clear space of its height;",
                            "never under 120 px wide in an ad."]):
        c.drawString(640, 1530 - i * 32, ln)
    for k, (name, hx) in enumerate([("Sage", "#99B4AE"), ("Blush", "#FFF8F5"), ("Peach", "#F2C4B6"), ("Coral", "#F0A08F"), ("Ink", "#1A1614"), ("Paper", "#FBF8F3")]):
        x = 72 + k * 176; c.setFillColor(HexColor(hx)); c.setStrokeColor(HexColor("#D9CFC8")); c.rect(x, 940, 150, 150, stroke=1, fill=1)
        tracked(c, name.upper(), "JostMed", 14, x, 910, 0.2); tracked(c, hx, "Jost", 14, x, 888, 0.12, MUTE)
    c.setFillColor(INK); c.setFont("Velista", 88); c.drawString(72, 740, "ALMOST EDIBLE.")
    c.setFont("CormIt", 40); c.drawString(72, 684, "cubic zirconia, not candy.")
    c.setFillColor(INK); c.rect(72, 640, 64, 2, stroke=0, fill=1)
    tracked(c, "PRISM RIVIÈRE · 18 CM · CUBIC ZIRCONIA", "JostMed", 18, 72, 608, 0.24)
    c.rect(72, 520, 300, 64, stroke=0, fill=1); tracked(c, "SHOP THE BRACELET", "JostMed", 19, 100, 545, 0.22, PAPER)
    c.setFont("Corm", 22); c.setFillColor(INK)
    spec = ["Headline: Velista capitals, about 100 px on a 1080 px ad, 2 lines at most.",
            "Correction: Cormorant Garamond italic, lowercase, about 40 px.",
            "Spec line: Jost Medium capitals, 18 px, 0.24 em tracking, listing facts only.",
            "CTA: ink button with paper type (Feed only; Stories use Meta's own sticker).",
            "Price, with the wordmark signing off above it, bottom right.",
            "Grounds: the photo, full bleed; on busy feet, the deck's blush paper band."]
    for i, ln in enumerate(spec): c.drawString(72, 450 - i * 34, ln)
    win = f"{SPB}/img_stockplan/img_001.jpg"
    if os.path.exists(win):
        c.drawImage(ImageReader(win), 760, 230, 360, 450); tracked(c, "THE ACCOUNT'S BEST AD · 10 SALES", "JostMed", 13, 760, 205, 0.2, MUTE)
    c.showPage()

def cover(c, title, sub, lines):
    c.setPageSize((PW, 1700)); c.setFillColor(PAPER); c.rect(0, 0, PW, 1700, stroke=0, fill=1)
    c.drawImage(ImageReader(f"{HERE}/brand/logo_sage.png"), 72, 1520, 330, 74, mask="auto")
    tracked(c, "PLAIN IMAGES FOR CLAUDE DESIGN  ·  OCTOBER 2026", "JostMed", 16, 72, 1450, 0.24, MUTE)
    c.setFillColor(INK); c.setFont("Velista", 84); y = 1330
    for ln in wrap(title.upper(), "Velista", 84, PW - 144): c.drawString(72, y, ln); y -= 84
    c.setFont("CormIt", 34); y -= 20
    for ln in wrap(sub, "CormIt", 34, PW - 144): c.drawString(72, y, ln); y -= 44
    c.setFont("Corm", 24); y -= 30
    for ln in lines:
        for w in wrap(ln, "Corm", 24, PW - 144): c.drawString(72, y, w); y -= 32
        y -= 8
    c.showPage()

def photo_page(c, data, size, cap):
    w, h = size; ih = round(PW * h / w); c.setPageSize((PW, ih + CAP))
    c.setFillColor(PAPER); c.rect(0, 0, PW, ih + CAP, stroke=0, fill=1)
    c.drawImage(ImageReader(io.BytesIO(data)), 0, CAP, PW, ih)
    tracked(c, cap["status"], "JostMed", 15, 48, CAP - 44, 0.22, CORAL if cap["status"].startswith("REFERENCE") else HexColor("#5F7B74"))
    piece, _, name = cap["title"].partition(" · ")          # Velista has no middle dot: the frame's name follows in italic
    c.setFillColor(INK); c.setFont("Velista", 40); c.drawString(48, CAP - 96, piece.upper())
    if name: c.setFont("CormIt", 32); c.drawString(48 + pdfmetrics.stringWidth(piece.upper(), "Velista", 40) + 18, CAP - 96, name.lower())
    tracked(c, cap["meta"], "Jost", 15, 48, CAP - 128, 0.16, MUTE)
    c.setFont("CormIt", 22); c.setFillColor(INK); y = CAP - 160
    for ln in wrap(cap["line"], "CormIt", 22, PW - 96)[:3]: c.drawString(48, y, ln); y -= 26
    c.showPage()

PIECES = {"toggle": "Toggle Link Chain", "woven": "Woven Gold Hoops", "heart": "Heartbead Bracelet", "prism": "Prism Rivière Bracelet"}
PIECES.update({k: v["title"] for k, v in json.load(open(f"{CRE}/edition-one/build/frames.json"))["pieces"].items()})

def build(outdir):
    os.makedirs(outdir, exist_ok=True)
    frames = [f for f in sheet_frames() if os.path.exists(plate_path(f))]
    PIECE_ORDER = ["prism", "toggle", "woven", "heart", "e1h", "e1b"]
    def key(f): return (PIECE_ORDER.index(f["sec"]) if f["sec"] in PIECE_ORDER else 9, f["piece"], f["n"])
    ready = sorted([f for f in frames if f["st"] in ("keep", "pass", "wait", "scene")], key=key)
    ref = sorted([f for f in frames if f["st"] == "fail"], key=key)
    groups = [("Ready for ads", "Every photograph that passed the listing check, best first by piece. Build ads from these.", ready),
              ("Reference only", "Photographs that failed the listing check: wrong stone count or order, a face, or the wrong scale. "
               "Kept for the record; do not build ads from them.", ref)]
    # the store's own listing photos: the plain truth of every piece
    listing = []
    for folder, pieces in [(f"{CRE}/concept-camps/build/refs", None), (f"{CRE}/edition-one/build/refs", None)]:
        for d in sorted(glob.glob(f"{folder}/*/")):
            for p in sorted(glob.glob(f"{d}*.jpg")):
                listing.append(dict(path=p, piece=os.path.basename(d.rstrip("/")), name=os.path.basename(p)))
    made = []
    def caption_frame(f):
        verdict = f.get("line") or ""
        meta = f"{f['price']}  ·  {f['code']}  ·  {f['aspect']}  ·  {f['w']}×{f['h']} px" + (f"  ·  ad score {f['score']}" if f.get("score") else "")
        return dict(status=STATUS.get(f["st"], f["st"].upper()), title=f"{f['piece']} · {f['name']}", meta=meta, line=verdict)
    def write(prefix, title, sub, items, pagefn):
        pages = [pagefn(it) for it in items]; total = sum(len(p[0]) for p in pages)
        n = max(1, -(-int(total) // int(LIMIT - 1.8e6))); target = total / n
        chunks, cur, size = [], [], 0
        for it, pg in zip(items, pages):
            if cur and size + len(pg[0]) > target * 1.04 and len(chunks) < n - 1: chunks.append(cur); cur, size = [], 0
            cur.append((it, pg)); size += len(pg[0])
        chunks.append(cur)
        for part, chunk in enumerate(chunks, 1):
            fn = f"{outdir}/Naira-Plain-{prefix}-{part}.pdf"; c = canvas.Canvas(fn); c.setTitle(f"Naira Petite · {title} · part {part}")
            if part == 1 and prefix.startswith("1"): brand_page(c)
            tally = {}
            for it, pg in chunk: tally[pg[2]["title"].split(" · ")[0]] = tally.get(pg[2]["title"].split(" · ")[0], 0) + 1
            cover(c, f"{title}, part {part} of {len(chunks)}", sub, ["In this part:"] + [f"{k}: {v}" for k, v in tally.items()])
            for it, (data, wh, cap) in chunk: photo_page(c, data, wh, cap)
            c.save(); mb = os.path.getsize(fn) / 1e6
            made.append(dict(file=os.path.basename(fn), title=f"{title}, part {part} of {len(chunks)}", count=len(chunk), mb=round(mb, 1),
                             ids=[it.get("id") or it.get("name") for it, _ in chunk])); print(os.path.basename(fn), len(chunk), f"{mb:.1f} MB")
    def frame_page(f):
        data, wh = jpg(plate_path(f)); return data, wh, caption_frame(f)
    def listing_page(l):
        data, wh = jpg(l["path"], long=1800, q=86)
        return data, wh, dict(status="THE STORE'S OWN LISTING PHOTO", title=PIECES.get(l["piece"], l["piece"]), meta=l["name"], line="")
    write("1-Ready", groups[0][0], groups[0][1], ready, frame_page)
    write("2-Reference", groups[1][0], groups[1][1], ref, frame_page)
    write("3-Listing", "Listing photos", "The store's own product photos, for plain ads and controls.", listing, listing_page)
    json.dump(dict(pdfs=made, ready=[f["id"] for f in ready], reference=[f["id"] for f in ref], listing=[l["name"] for l in listing]),
              open(f"{outdir}/plain.json", "w"), indent=1, ensure_ascii=False)

if __name__ == "__main__":
    build(sys.argv[1])
