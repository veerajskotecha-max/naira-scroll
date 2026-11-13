# Evidence image for the Toggle Link Chain's clasp ring (page/img/toggle-link-chain.jpg), 13 Nov 2026.
# Left: the ad reel (nov02.mp4) at frame 439 (14.63 s), the clasp resting on the fingers. The ring outline is fitted with an ellipse
# (cv2.fitEllipse on the gold pixels round the ring); its long axis is the ring's true width, because the ring is round (right) and
# only looks oval here because it is tilted. The link width (30.8 px) is the line the ad-reel agent drew.
# Right: the store's close-up of the clasp (concept-camps/build/refs/toggle/ref-clasp.jpg): a round ring, 408 x 413 px.
# Usage: python3 -I toggle.py <scratchpad>/adreel/frames30/n_0439.jpg <repo>/docs/creative/concept-camps/build/refs/toggle/ref-clasp.jpg <out.jpg>
import math, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont
F = lambda n: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", n)
FB = lambda n: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", n)
reel, ref, out = sys.argv[1:4]

# fit the ring in the reel frame: gold (warm, bright) pixels inside a box round the ring, outer contour, ellipse
im = cv2.imread(reel); x0, y0, x1, y1 = 425, 1255, 590, 1470
hsv = cv2.cvtColor(im[y0:y1, x0:x1], cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (12, 90, 120), (35, 255, 255))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
cs, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
c = max(cs, key=cv2.contourArea); (ex, ey), (ea, eb), eang = cv2.fitEllipse(c)
ex += x0; ey += y0; L, Sh = max(ea, eb), min(ea, eb)
t = math.radians(eang + (90 if eb > ea else 0))      # direction of the long axis
lx, ly = math.cos(t) * L / 2, math.sin(t) * L / 2
print("reel ring ellipse %.0f x %.0f px, aspect %.2f, centre (%.0f, %.0f)" % (L, Sh, Sh / L, ex, ey))
link = math.hypot(238 - 220, 1188 - 1213)
print("link width %.1f px -> ring = %.1f link widths -> %.1f mm at 4 mm links" % (link, L / link, 4 * L / link))

def crop(path, box, s):
    img = Image.open(path).convert("RGB").crop(box); return img.resize((int(img.width * s), int(img.height * s)), Image.LANCZOS)

def seg(d, a, b, col, lab, off=(8, -8)):
    d.line([a, b], fill="black", width=6); d.line([a, b], fill=col, width=3)
    tx, ty = (a[0] + b[0]) / 2 + off[0], (a[1] + b[1]) / 2 + off[1]
    bb = d.textbbox((tx, ty), lab, font=FB(15)); d.rectangle((bb[0] - 3, bb[1] - 2, bb[2] + 3, bb[3] + 2), fill="white"); d.text((tx, ty), lab, fill="black", font=FB(15))

box, s = (150, 1150, 700, 1600), 1.1
A = crop(reel, box, s); d = ImageDraw.Draw(A); P = lambda x, y: ((x - box[0]) * s, (y - box[1]) * s)
seg(d, P(ex - lx, ey - ly), P(ex + lx, ey + ly), "#ff2bd6", "ring %.0f px" % L, (14, -10))
seg(d, P(238, 1188), P(220, 1213), "#00e5ff", "link %.0f px" % link, (12, -16))
B = crop(ref, (0, 0, 900, 780), 0.635); d2 = ImageDraw.Draw(B); Q = lambda x, y: (x * 0.635, y * 0.635)
seg(d2, Q(232, 441), Q(640, 441), "#ff2bd6", "ring 408 px", (-185, -34))
seg(d2, Q(436, 235), Q(436, 648), "#ff2bd6", "413 px", (8, 52))
H = max(A.height, B.height); W = A.width + B.width + 12
sheet = Image.new("RGB", (W, H + 152), "white"); sheet.paste(A, (0, 40)); sheet.paste(B, (A.width + 12, 40))
d3 = ImageDraw.Draw(sheet)
d3.text((6, 10), "Toggle Link Chain: the clasp ring", fill="black", font=FB(19))
foot = ["Left: the ad reel at 14.63 s. The ring looks oval (%.0f x %.0f px) only because it is tilted; its long side is its width." % (L, Sh),
        "Right: the store's close-up of the clasp: the ring is round (408 x 413 px).",
        "The ring is %.1f to %.1f times the chain's link width (%.0f px; 167 px is the ad-reel agent's tighter outline, without the jump ring)." % (167 / link, L / link, link),
        "At the listed 4 mm links that is about %.0f to %.0f mm across." % (4 * 167 / link, 4 * L / link),
        "Against the fingers in the same frame (the ad-reel check): about 18.5 to 26 mm. The listing says about 15 mm."]
for i, line in enumerate(foot): d3.text((6, H + 48 + i * 20), line, fill="black", font=F(14))
sheet.save(out, quality=88); print(out, sheet.size)
