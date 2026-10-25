# Draws the store's size-guide cards (1600x1600, the live <handle>-size-guide.jpg format) for the pieces in
# ../shopify/listing.json that carry a "sizeguide" spec:
#   ring   the house ring card (Chevron Whisper Ring): inner-diameter circle and the US size boxes, with the sizes an
#          adjustable ring fits filled in;
#   photo  the house photo card (Crystal Pear Ear Cuff, Clover Trio Edit): the approved hero in a panel, with
#          measurement bars and labels. Callouts are in raw frame pixels: ["h", x0, x1, y, label] is a bar across,
#          ["v", y0, y1, x, label(, "left"|"right")] a bar down with its label beside it.
# Necklaces and bracelets have no card yet: their chain lengths are not known.
# Usage: sizeguide.py OUTDIR
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__))
VEL = os.path.join(H, "../../finished-ads/brand/Velista.ttf"); J = lambda w: os.path.join(H, f"../../aditya-bracelets/build/fonts/Jost-{w}.ttf")
BG, INK, GREY, GOLD, RING, LINE = (244, 235, 226), (28, 23, 18), (109, 100, 91), (153, 118, 52), (160, 125, 67), (172, 163, 154)
NOLIG = ["-liga", "-dlig", "-calt", "-swsh"]
SRC = {"J06_H": "J06_He", "J17_H": "J17_Hs"}   # the true-size heroes from the 25 Oct reshoot
US = [("5", "15.7"), ("6", "16.5"), ("6½", "16.9"), ("7", "17.3"), ("8", "18.1"), ("9", "18.9")]
def spaced(d, xy, text, font, fill, track, anchor="l"):
    w = sum(d.textlength(c, font=font) for c in text) + track * (len(text) - 1)
    x = xy[0] - (w / 2 if anchor == "m" else w if anchor == "r" else 0)
    for c in text:
        d.text((x, xy[1]), c, font=font, fill=fill); x += d.textlength(c, font=font) + track
def head(d, title):
    spaced(d, (800, 91), "SIZE GUIDE", ImageFont.truetype(J(500), 27), GOLD, 7.5, "m")
    tf = ImageFont.truetype(VEL, 65)
    while d.textlength(title.upper(), font=tf, features=NOLIG) > 1320: tf = ImageFont.truetype(VEL, tf.size - 2)
    d.text((800, 170), title.upper(), font=tf, fill=INK, anchor="mm", features=NOLIG)
def foot(d, line):
    bf = ImageFont.truetype(J(400), 54)
    while d.textlength(line, font=bf) > 1280: bf = ImageFont.truetype(J(400), bf.size - 2)
    d.text((163, 1383), line, font=bf, fill=INK, anchor="ls")
    d.text((161, 1444), "Measurements are approximate, give or take 1 mm.", font=ImageFont.truetype(J(300), 27), fill=GREY, anchor="ls")
    spaced(d, (1432, 1481), "NAIRA PETITE", ImageFont.truetype(J(500), 22), GOLD, 7.0, "r")
def ring(title, spec):
    im = Image.new("RGB", (1600, 1600), BG); d = ImageDraw.Draw(im); head(d, title)
    lo, hi = spec["fit"]; keys = [u for u, _ in US]; fit = keys[keys.index(lo):keys.index(hi) + 1]
    spaced(d, (800, 442), "INNER DIAMETER", ImageFont.truetype(J(400), 30), GREY, 3.2, "m")
    d.ellipse((523, 493, 1077, 1047), outline=RING, width=17)
    mm = f"{dict(US)[lo]}–{dict(US)[hi]} mm"; mf = ImageFont.truetype(J(500), 50); half = d.textlength(mm, font=mf) / 2 + 28
    for a, b in ((540, 800 - half), (800 + half, 1060)): d.line((a, 770, b, 770), fill=INK, width=3)
    for x in (540, 1060): d.line((x, 752, x, 788), fill=INK, width=3)
    d.text((800, 770), mm, font=mf, fill=INK, anchor="mm")
    bf, sf = ImageFont.truetype(J(500), 32), ImageFont.truetype(J(400), 23)
    for i, (us, m) in enumerate(US):
        x0 = 184 + i * 208; on = us in fit
        if on: d.rectangle((x0, 1149, x0 + 191, 1254), fill=(26, 22, 19))
        else: d.rectangle((x0, 1149, x0 + 191, 1254), outline=LINE, width=2)
        d.text((x0 + 96, 1186), f"US {us}", font=bf, fill=BG if on else INK, anchor="mm")
        d.text((x0 + 96, 1227), f"{m} mm", font=sf, fill=(226, 217, 208) if on else GREY, anchor="mm")
    foot(d, spec["line"]); return im
def photo(title, spec):
    im = Image.new("RGB", (1600, 1600), BG); d = ImageDraw.Draw(im); head(d, title)
    pw, ph = (800, 931) if spec.get("portrait") else (1280, 931); px0, py0 = (1600 - pw) // 2, 288
    cx, cy, cw = spec["crop"]; s = pw / cw; ch = round(ph / s)
    src = Image.open(f"{H}/out/{SRC.get(spec['src'], spec['src'])}.png").convert("RGB")
    im.paste(src.crop((cx, cy, cx + cw, cy + ch)).resize((pw, ph), Image.LANCZOS), (px0, py0))
    X = lambda x: px0 + (x - cx) * s; Y = lambda y: py0 + (y - cy) * s
    lf = ImageFont.truetype(J(500), 42)
    def pill(xc, yc, text):
        w = d.textlength(text, font=lf) + 52
        d.rounded_rectangle((xc - w / 2, yc - 33, xc + w / 2, yc + 33), radius=33, fill=BG)
        d.text((xc, yc + 1), text, font=lf, fill=INK, anchor="mm"); return w
    for c in spec["callouts"]:
        if c[0] == "h":
            _, x0, x1, y, text = c; a, b, yy = X(x0), X(x1), Y(y)
            d.line((a, yy, b, yy), fill=INK, width=4)
            for x in (a, b): d.line((x, yy - 18, x, yy + 18), fill=INK, width=4)
            pill((a + b) / 2, yy - 62, text)
        else:
            _, y0, y1, x, text, *side = c; a, b, xx = Y(y0), Y(y1), X(x)
            d.line((xx, a, xx, b), fill=INK, width=4)
            for y in (a, b): d.line((xx - 18, y, xx + 18, y), fill=INK, width=4)
            w = d.textlength(text, font=lf) + 52
            pill(xx + (w / 2 + 30) * (1 if side and side[0] == "right" else -1), (a + b) / 2, text)
    foot(d, spec["line"]); return im
if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for p in json.load(open(os.path.join(H, "../shopify/listing.json"))):
        sg = p.get("sizeguide")
        if not sg: continue
        (ring if sg["kind"] == "ring" else photo)(p["title"], sg).save(f"{out}/{p['handle']}-size-guide.jpg", quality=92)
        print(p["handle"])
