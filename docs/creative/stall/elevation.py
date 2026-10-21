# The stall unfolded: left wall, back wall and right wall side by side, each 24 × 36 in poster on its own white
# shell-scheme panel (about 1 m × 2.5 m, aluminium uprights) at true scale, with the table line and a person for scale.
# Usage: elevation.py <out.jpg> <left-1> <left-2> <back-1> <back-2> <back-3> <right-1> <right-2>   (poster JPGs)
#        elevation.py --lineup <out.jpg> <same seven>   -> the seven side by side, large, labelled, in wall order
import sys
from PIL import Image, ImageDraw, ImageFont

PX = 420                                   # px per metre
PANEL_W, PANEL_H = .99, 2.5                # one shell-scheme panel
POSTER_W, POSTER_H = .6096, .9144          # 24 × 36 in
TOP = 2.05                                 # poster top edge from the floor
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def main(out, *posters):
    walls = [("LEFT WALL", posters[0:2]), ("BACK WALL", posters[2:5]), ("RIGHT WALL", posters[5:7])]
    gap = .55; n = sum(len(p) for _, p in walls)
    W = round((n * PANEL_W + (len(walls) - 1) * gap + .4) * PX); H = round((PANEL_H + .75) * PX)
    im = Image.new("RGB", (W, H), "#F4F1EC"); d = ImageDraw.Draw(im)
    f1 = ImageFont.truetype(F, 54); f2 = ImageFont.truetype(F, 34)
    x = .2 * PX; floor = H - .45 * PX
    for name, ps in walls:
        x0 = x
        for p in ps:
            px0, py0 = round(x), round(floor - PANEL_H * PX)
            d.rectangle([px0, py0, px0 + PANEL_W * PX, floor], fill="#FBFBFA", outline="#C9CCCF", width=3)
            pw, ph = round(POSTER_W * PX), round(POSTER_H * PX)
            img = Image.open(p).convert("RGB").resize((pw, ph), Image.LANCZOS)
            ix = round(x + (PANEL_W * PX - pw) / 2); iy = round(floor - TOP * PX)
            d.rectangle([ix + 4, iy + 6, ix + pw + 4, iy + ph + 6], fill="#E2E2E0"); im.paste(img, (ix, iy))
            x += PANEL_W * PX
        # table (75 cm) in front of the wall
        d.rectangle([round(x0 + .15 * PX), round(floor - .75 * PX), round(x - .15 * PX), round(floor)], fill="#E6D6C4", outline="#CDBBA6", width=2)
        d.text((x0, floor + .12 * PX), name, fill="#1A1614", font=f1)
        x += gap * PX
    d.text((.2 * PX, 30), "NAIRA PETITE · STALL WALLS, TO SCALE · posters 24 × 36 in, top edge 2.05 m from the floor · table 75 cm", fill="#6E625A", font=f2)
    im.save(out, quality=90)

LABELS = ["LEFT 1", "LEFT 2", "BACK 1", "BACK 2", "BACK 3", "RIGHT 1", "RIGHT 2"]

def lineup(out, *posters):
    pw, ph, g, wg, m = 720, 1080, 36, 110, 90
    W = 2 * m + 7 * pw + 4 * g + 2 * wg; H = m + ph + 150
    im = Image.new("RGB", (W, H), "#F4F1EC"); d = ImageDraw.Draw(im); f = ImageFont.truetype(F, 34)
    x = m
    for i, (p, lab) in enumerate(zip(posters, LABELS)):
        d.rectangle([x + 5, m + 8, x + pw + 5, m + ph + 8], fill="#E2E0DC")
        im.paste(Image.open(p).convert("RGB").resize((pw, ph), Image.LANCZOS), (x, m))
        d.text((x, m + ph + 34), lab, fill="#1A1614", font=f)
        x += pw + (wg if i in (1, 4) else g)
    im.save(out, quality=90)

if __name__ == "__main__":
    if sys.argv[1] == "--lineup": lineup(*sys.argv[2:])
    else: main(*sys.argv[1:])
