# Review sheet of finished ads: one row per product, its Feed ads then its Story ads. Usage: ads_sheet.py <out.jpg> <handle> ...
import os, sys
from PIL import Image, ImageDraw, ImageFont
PERF = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FMTS = ["rhyme", "silk", "worn", "quiet", "play"]; H, PAD = 430, 6
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)

def main(out, *keys):
    rows = []
    for k in keys:
        ims = [(f"{f} {t}", f"{PERF}/ads/{k}-{f}-{t}.jpg") for t in ("feed", "story") for f in FMTS]
        rows.append([(lab, Image.open(p).convert("RGB")) for lab, p in ims if os.path.exists(p)])
    rows = [[(lab, im.resize((round(im.width * H / im.height), H))) for lab, im in r] for r in rows if r]
    W = max(sum(im.width + PAD for _, im in r) for r in rows) + PAD
    sheet = Image.new("RGB", (W, len(rows) * (H + 26 + PAD) + PAD), (236, 232, 226)); d = ImageDraw.Draw(sheet); y = PAD
    for r in rows:
        x = PAD
        for lab, im in r: sheet.paste(im, (x, y + 22)); d.text((x, y + 2), lab, fill=(40, 30, 25), font=F); x += im.width + PAD
        y += H + 26 + PAD
    sheet.save(out, quality=85)

if __name__ == "__main__":
    main(*sys.argv[1:])
