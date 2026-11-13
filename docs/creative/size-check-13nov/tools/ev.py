# Annotated evidence crops for the size check of the 12 Nov stock video (frames at 6 fps, 1440x1920).
import os
from PIL import Image, ImageDraw, ImageFont
V = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos/all")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evidence")
try: F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
except Exception: F = ImageFont.load_default()
def ev(name, frame, crop, lines, boxes, caption):
    im = Image.open(os.path.join(V, frame + ".jpg")).convert("RGB"); d = ImageDraw.Draw(im)
    for (p, q, col, lab) in lines:
        d.line([p, q], fill=col, width=7)
        for e in (p, q): d.ellipse([e[0] - 8, e[1] - 8, e[0] + 8, e[1] + 8], fill=col)
        d.text(((p[0] + q[0]) / 2 + 12, (p[1] + q[1]) / 2 - 36), lab, fill=col, font=F, stroke_width=3, stroke_fill="white")
    for (b, col, lab) in boxes:
        d.rectangle(b, outline=col, width=6)
        d.text((b[0], b[3] + 6), lab, fill=col, font=F, stroke_width=3, stroke_fill="white")
    im = im.crop(crop)
    w = 900; im = im.resize((w, int(im.height * w / im.width)))
    bar = Image.new("RGB", (w, 70), (250, 247, 242)); ImageDraw.Draw(bar).text((14, 18), caption, fill=(40, 30, 25), font=F)
    c = Image.new("RGB", (w, im.height + 70), "white"); c.paste(im, (0, 0)); c.paste(bar, (0, im.height))
    c.save(os.path.join(OUT, name + ".jpg"), quality=86); print(name, c.size)
B, R, G = (20, 110, 230), (220, 30, 40), (10, 140, 70)
ev("soleil-petal", "0026", (520, 220, 1000, 1700),
   [((633, 1521), (874, 1478), B, "thumb 246 px ~ 21 mm")],
   [((715, 280, 880, 505), R, "flower 165 x 225 px ~ 15-20 mm"), ((652, 1302, 752, 1395), G, "Asscher 100 px ~ 9 mm")],
   "4.2 s: Soleil Petal vs thumb and Asscher pendant")
ev("v-bar-teardrop", "0232", (0, 380, 1440, 1900),
   [((172, 545), (125, 755), B, "keys 19 mm apart"), ((545, 1510), (580, 1690), R, "bar ~18 mm"), ((585, 1675), (740, 1640), R, "bar ~17 mm")],
   [((465, 1695, 590, 1830), R, "pear ~11 x 15 mm")],
   "38.5 s: V-Bar Teardrop on the keyboard (9 px per mm)")
ev("pave-open-heart", "0066", (420, 850, 1300, 1680),
   [((548, 973), (699, 1167), B, "finger 247 px ~ 17.5 mm")],
   [((893, 1183, 1234, 1544), R, "heart ~ 22-24 mm"), ((573, 1289, 907, 1628), R, "")],
   "10.8 s: Pave Open Heart Studs vs index finger")
ev("petite-pear", "0054", (480, 560, 900, 1460),
   [((588, 656), (713, 785), B, "finger ~190 px ~ 17.5 mm")],
   [((723, 1326, 791, 1406), R, "pear ~6 x 7.5 mm")],
   "8.8 s: Petite Pear Solitaire vs index finger")
ev("heart-solitaire-huggies", "0078", (300, 650, 1100, 1250),
   [((446, 756), (463, 950), B, "finger 196 px ~ 17.5 mm")],
   [((573, 860, 745, 1060), R, "hoop ~16.5 mm"), ((735, 805, 815, 900), G, "heart ~7.5 mm")],
   "12.8 s: Heart Solitaire Huggies (opened) vs finger")
ev("clover-garland", "0144", (560, 880, 1060, 1720),
   [((615, 1390), (856, 1390), B, "finger 241 px ~ 17.5 mm")],
   [((800, 1095, 921, 1224), R, "clover ~8.5 mm"), ((813, 945, 932, 1058), R, "")],
   "23.8 s: Clover Garland Necklace (red) vs finger")
ev("bow-and-heart", "0197", (0, 100, 1100, 1150),
   [((305, 240), (278, 549), B, "finger 311 px (above the card)")],
   [((551, 918, 764, 1091), R, "earring ~12-19 mm"), ((805, 869, 960, 1073), R, "")],
   "32.7 s: Bow and Heart earrings: finger is off the card plane")
