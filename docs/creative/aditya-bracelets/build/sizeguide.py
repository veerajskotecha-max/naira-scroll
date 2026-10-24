# Draws the store's bracelet size-guide card (1600x1600, the live <handle>-size-guide.jpg format): a gold bar for the
# bracelet length on a 0-24 cm ruler, the wrist range it fits (length minus 1.5-2.5 cm), and the house footer lines.
# Usage: sizeguide.py OUTDIR "Title" length_cm [adjust_min adjust_max] ...  (reads products from ../shopify/listing.json if no args)
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__))
VEL = os.path.join(H, "../../finished-ads/brand/Velista.ttf"); J = lambda w: os.path.join(H, f"fonts/Jost-{w}.ttf")
BG, INK, GREY, GOLD, SAGE = (244, 235, 226), (28, 23, 18), (118, 109, 100), (153, 118, 52), (153, 180, 175)
NOLIG = ["-liga", "-dlig", "-calt", "-swsh"]
X0, PX = 200, 50                                    # ruler origin and pixels per cm (0-24 cm across x 200-1400)
def spaced(d, xy, text, font, fill, track, anchor="l"):
    w = sum(d.textlength(c, font=font) for c in text) + track * (len(text) - 1)
    x = xy[0] - (w / 2 if anchor == "m" else w if anchor == "r" else 0)
    for c in text:
        d.text((x, xy[1]), c, font=font, fill=fill); x += d.textlength(c, font=font) + track
def fmt(v): return f"{v:g}"
def card(title, length, adjust=None):
    im = Image.new("RGB", (1600, 1600), BG); d = ImageDraw.Draw(im)
    spaced(d, (800, 91), "SIZE GUIDE", ImageFont.truetype(J(500), 27), GOLD, 7.5, "m")
    tf = ImageFont.truetype(VEL, 65)
    while d.textlength(title.upper(), font=tf, features=NOLIG) > 1320: tf = ImageFont.truetype(VEL, tf.size - 2)
    d.text((800, 170), title.upper(), font=tf, fill=INK, anchor="mm", features=NOLIG)
    lo, hi = (adjust or (length, length))
    xa, xb = X0 + lo * PX, X0 + hi * PX
    if adjust: d.rounded_rectangle((X0 - 8, 742, xb + 8, 759), radius=9, fill=GOLD); d.rectangle((xa, 742, xb, 759), fill=BG); \
        d.rounded_rectangle((X0 - 8, 742, xa, 759), radius=9, fill=GOLD); [d.rectangle((x, 746, x + 10, 755), fill=GOLD) for x in range(int(xa) + 6, int(xb) - 4, 22)]
    else: d.rounded_rectangle((X0 - 8, 742, xb + 8, 759), radius=9, fill=GOLD)
    lab = f"{fmt(lo)}–{fmt(hi)} cm" if adjust else f"{fmt(length)} cm"
    d.text((xb, 707), lab, font=ImageFont.truetype(J(500), 44), fill=GOLD, anchor="ms" if not adjust else "rs")
    d.rectangle((X0, 818, 1400, 820), fill=INK)
    for i in range(0, 49):
        x = X0 + i * 25; y1 = 856 if i % 10 == 0 else 843 if i % 2 == 0 else 831
        d.rectangle((x - 1, 818, x, y1), fill=INK)
    lf = ImageFont.truetype(J(400), 30)
    for cm in range(0, 25, 2):
        d.text((X0 + cm * PX, 898), str(cm), font=lf, fill=GREY, anchor="ms")
    d.text((X0 + 24 * PX + 19, 898), "cm", font=lf, fill=GREY, anchor="ls")
    w0, w1 = lo - 2.5, hi - 1.5
    d.rectangle((X0 + w0 * PX, 993, X0 + w1 * PX, 1031), fill=SAGE)
    d.text((X0 + (w0 + w1) / 2 * PX, 1085), f"fits wrists {fmt(w0)}–{fmt(w1)} cm", font=ImageFont.truetype(J(400), 33), fill=INK, anchor="ms")
    d.text((201, 1234), "Measure around your wrist bone; allow 1.5–2.5 cm for an easy fit.", font=ImageFont.truetype(J(300), 30), fill=GREY, anchor="ls")
    big = (f"Adjustable {fmt(lo)}–{fmt(hi)} cm · fits wrists about {fmt(w0)}–{fmt(w1)} cm" if adjust
           else f"{fmt(length)} cm · fits wrists about {fmt(w0)}–{fmt(w1)} cm")
    bf = ImageFont.truetype(J(400), 54)
    while d.textlength(big, font=bf) > 1280: bf = ImageFont.truetype(J(400), bf.size - 2)
    d.text((163, 1383), big, font=bf, fill=INK, anchor="ls")
    d.text((161, 1444), "Measurements are approximate, give or take 1 mm.", font=ImageFont.truetype(J(300), 27), fill=GREY, anchor="ls")
    spaced(d, (1432, 1481), "NAIRA PETITE", ImageFont.truetype(J(500), 22), GOLD, 7.0, "r")
    return im
if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    L = json.load(open(os.path.join(H, "../shopify/listing.json")))
    for p in L:
        im = card(p["title"], p["length_cm"], tuple(p["adjust_cm"]) if p.get("adjust_cm") else None)
        im.save(f"{out}/{p['handle']}-size-guide.jpg", quality=92); print(p["handle"])
