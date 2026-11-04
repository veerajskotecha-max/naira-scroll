# Review sheet for one set: the five Feed cards on top, the five Stories below, each labelled with its key and line.
# Usage: sheet.py layout.json "Set title" out.jpg
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
OUT = f"{SPB}/ads20/out"
FONT = f"{SPB}/c4/fonts/Jost[wght].ttf"

def main():
    lay = json.load(open(os.path.join(HERE, sys.argv[1]))); title = sys.argv[2]; dst = sys.argv[3]
    ads = lay["ads"]; fw, fh = 432, 540; sw, sh = 304, 540; gap = 24; pad = 40
    W = pad * 2 + len(ads) * fw + (len(ads) - 1) * gap
    H = pad + 70 + fh + 60 + sh + 70 + pad
    img = Image.new("RGB", (W, H), (250, 248, 243)); d = ImageDraw.Draw(img)
    f1 = ImageFont.truetype(FONT, 30); f1.set_variation_by_axes([500])
    f2 = ImageFont.truetype(FONT, 17); f2.set_variation_by_axes([400])
    d.text((pad, pad), title, font=f1, fill=(26, 22, 20))
    y0 = pad + 70
    for i, a in enumerate(ads):
        x = pad + i * (fw + gap)
        feed = Image.open(f"{OUT}/{a['key']}_feed.jpg").resize((fw, fh), Image.LANCZOS); img.paste(feed, (x, y0))
        story = Image.open(f"{OUT}/{a['key']}_story.jpg").resize((sw, sh), Image.LANCZOS); img.paste(story, (x + (fw - sw) // 2, y0 + fh + 60))
        label = a["key"].split("_", 2)[-1].replace("_", " ")
        line = (a.get("line") or a.get("feed", {}).get("line") or a.get("name", "")).replace("<br>", " ").replace("₹", "Rs ")
        d.text((x, y0 + fh + 10), label, font=f2, fill=(110, 100, 94))
        d.text((x, y0 + fh + 32), line[:48], font=f2, fill=(26, 22, 20))
    img.save(dst, quality=88); print(dst, img.size)

if __name__ == "__main__":
    main()
