# Contact sheet of plates: one row per product, its five formats in order. Usage: sheet.py <out.jpg> <handle> [<handle> ...]
import os, sys
from PIL import Image, ImageDraw, ImageFont
PERF = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FMTS = ["rhyme", "silk", "worn", "quiet", "play"]; TW, TH, PAD = 270, 480, 10
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

def main(out, *keys):
    sheet = Image.new("RGB", (5 * (TW + PAD) + PAD, len(keys) * (TH + 40 + PAD) + PAD), (236, 232, 226)); d = ImageDraw.Draw(sheet)
    for r, k in enumerate(keys):
        y = PAD + r * (TH + 40 + PAD)
        for c, f in enumerate(FMTS):
            x = PAD + c * (TW + PAD); p = f"{PERF}/plates/{k}-{f}.jpg"
            if os.path.exists(p): sheet.paste(Image.open(p).convert("RGB").resize((TW, TH)), (x, y + 30))
            else: d.rectangle([x, y + 30, x + TW, y + 30 + TH], outline=(180, 170, 160), width=2); d.text((x + 10, y + 240), "missing", fill=(140, 120, 110), font=F)
            d.text((x, y + 4), f"{k[:22]} · {f}", fill=(40, 30, 25), font=F)
    sheet.save(out, quality=86)

if __name__ == "__main__":
    main(*sys.argv[1:])
