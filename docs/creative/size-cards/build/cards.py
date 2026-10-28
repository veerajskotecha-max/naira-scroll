# Draws the size-guide cards in ../cards.json (28 Oct 2026: the live listings that had none) in the store's three house
# formats, using the existing generators so the cards match the live ones:
#   photo     ../../aditya-jewellery/build/sizeguide.py photo(): the listing photo in a panel with measurement bars;
#   bracelet  ../../aditya-bracelets/build/sizeguide.py card(): the length on a 0-24 cm ruler and the wrists it fits;
#   necklace  necklace() below, after the live necklace card (Serpentine Whisper Chain): a neck and shoulders outline with
#             the house reference lengths, 36 to 60 cm, and the piece's own length(s) drawn in gold.
# Usage: cards.py  -> ../out/<handle>-size-guide.jpg
import importlib.util, json, math, os
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(H)
def load(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
SGJ = load("sgj", os.path.join(C, "../aditya-jewellery/build/sizeguide.py"))
SGB = load("sgb", os.path.join(C, "../aditya-bracelets/build/sizeguide.py"))
OUTLINE, REF, LABEL = (150, 141, 131), (205, 196, 186), (128, 119, 110)
CX, TOP = 590, 440                                          # the outline's centre line and the base of the neck
REFS = {36: "choker", 40: "base of the neck", 45: "collarbone", 50: "mid-chest", 60: "matinee"}
def y_of(cm): return 493 + (cm - 36) * 22                  # the live card's spacing: 40 cm at y 581, 45 at 691, 60 at 1021
def a_of(cm):                                                # half-width of each length's loop, read off the live card
    pts = [(36, 85), (40, 106), (45, 126), (50, 150), (60, 198)]
    for (c0, a0), (c1, a1) in zip(pts, pts[1:]):
        if cm <= c1: return a0 + (a1 - a0) * (cm - c0) / (c1 - c0)
    return pts[-1][1]
def bezier(p0, p1, p2, p3, n=40):
    return [tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t ** 2 * c + t ** 3 * d for a, b, c, d in zip(p0, p1, p2, p3))
            for t in (i / n for i in range(n + 1))]
def loop(d, cm, end_dx, end_y, fill, width):
    # one length as an ellipse whose ends sit at (CX +- end_dx, end_y), widest a_of(cm) across, lowest at y_of(cm)
    a, yb = a_of(cm), y_of(cm); th = math.acos(min(end_dx / a, 0.99)); s = math.sin(th)
    cy = (end_y + yb * s) / (1 + s); b = yb - cy; deg = math.degrees(th)
    d.arc((CX - a, cy - b, CX + a, cy + b), -deg, 180 + deg, fill=fill, width=width)
def necklace(title, lengths, line, note):
    im = Image.new("RGB", (1600, 1600), SGJ.BG); d = ImageDraw.Draw(im); SGJ.head(d, title)
    for s in (1, -1):                                        # neck, shoulders and collarbones, mirrored about CX
        X = lambda x: CX + s * (x - CX)
        d.line([(X(521), 248), (X(516), 420)], fill=OUTLINE, width=3)
        d.line([(X(x), y) for x, y in bezier((516, 420), (470, 448), (170, 478), (108, 600))] + [(X(96), 1130)], fill=OUTLINE, width=3)
        d.line([(X(270), 511), (X(555), 498)], fill=REF, width=3)
    d.arc((CX - 85, 455 - 38, CX + 85, 455 + 38), 0, 180, fill=REF, width=3)   # 36 cm, the choker line at the neck
    for cm in (40, 45, 50, 60):                              # the reference loops, faint, rising behind the collar
        loop(d, cm, 0.75 * a_of(cm), 470, REF, 3)
    lf, gf = ImageFont.truetype(SGJ.J(400), 31), ImageFont.truetype(SGJ.J(500), 46)
    for cm in lengths:                                       # the piece itself, in gold, its ends at the neck
        yb = y_of(cm); loop(d, cm, 72, 423, SGJ.GOLD, 11)
        for x in range(CX + 40, 1125, 14): d.ellipse((x - 1.6, yb - 1.6, x + 1.6, yb + 1.6), fill=SGJ.GOLD)
        d.text((1150, yb), f"{cm:g} cm", font=gf, fill=SGJ.GOLD, anchor="lm")
    for cm, name in REFS.items():                            # reference labels, unless a gold one sits there
        if all(abs(y_of(cm) - y_of(c)) > 52 for c in lengths):
            d.text((1150, y_of(cm)), f"{cm} cm · {name}", font=lf, fill=LABEL, anchor="lm")
    SGJ.foot(d, line, note); return im
if __name__ == "__main__":
    spec = json.load(open(os.path.join(C, "cards.json"))); os.makedirs(os.path.join(C, "out"), exist_ok=True)
    for c in spec["cards"]:
        if c["kind"] == "photo":
            im = SGJ.photo(c["title"], dict(c, path=os.path.join(C, c["path"])))
        elif c["kind"] == "bracelet":
            im = SGB.card(c["title"], c["length"], None, c["note"])
        else:
            im = necklace(c["title"], c["lengths"], c["line"], c["note"])
        im.save(os.path.join(C, "out", f"{c['handle']}-size-guide.jpg"), quality=92); print(c["handle"], c["kind"])
