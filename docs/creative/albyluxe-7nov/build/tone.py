# Stone tones: moves one stone colour of a piece toward the supplier's (or the owner's) photo, the same way in every frame, so every frame
# matches and a pair stays identical: hue +DH degrees, chroma x SK, lightness +DL, each stone's own shading kept. The weight window is centred
# on the stones' own hue (HC, half-width HW) and needs some colour (chroma over CMIN), so skin, gold and silver are untouched.
#   L04 Lilac Flutter Studs (was l04fix.py): the owner's stones read a cool lavender (CIELab hue about 331, chroma about 15); the 7 Nov tone
#       (window at 300, DH +14) moved them pinker, so on 12 Nov it turns them cooler and a little softer. Measured at the claws, the owner's two
#       upper marquise are the same length, so the near-equal stones in the photos are right.
#   L10 Interlocked Baguette Stack Ring (12 Nov, ../corrections.md): the regenerated frames still draw a brighter green (hue 141-150,
#       chroma about 23) than the supplier's deep blue-green (hue about 155, chroma about 14); the Green variant's frames are toned here.
#       The frames start from different greens, so L10 gives a TARGET (TH, TC) instead of a fixed shift: each frame's stone pixels are moved
#       so their median lands on it. The White and Red variants are recoloured from the untoned frames (recolour.py).
#   L14 Zigzag Gem Eternity Ring (12 Nov): the green reads brighter and more saturated than the supplier's deep emerald: a little darker,
#       softer and bluer (lightness -5, chroma x0.75, hue +5). Red and White are recoloured from the untoned frames.
#   L18 Aqua Oval Cocktail Ring (12 Nov): the macro alone came out pale sky blue (hue about 186) where the supplier's stone and our other
#       four photos are a soft mint (159-167): its stone (after l18fix.py) goes to hue 162, half as strong again.
#   L05 Blush Octagon Studs (12 Nov): the stones lean peach (the remade packshot at hue 45, chroma 23); the owner's is a rosier pink (hue about
#       36, chroma 22): a target, as L10. Its deep orange centre sits at hue 50-58, next to skin, so on frames with skin a box round the studs
#       keeps the window to the stones (KEY:x0,y0,x1,y1).
# Usage: python3 -I tone.py PIECE KEY[:x0,y0,x1,y1] ...   (out/KEY.png -> out/KEY_t.png; the ellipse in the box limits the change to the stone)
import os, sys
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); O = lambda k: os.path.join(H, "out", k + ".png")
P = {"L04": dict(HC=343.0, HW=45.0, DH=-12.0, SK=0.76, DL=-1.0, CMIN=5.0, LMIN=0.0),
     "L10": dict(HC=147.0, HW=40.0, TH=155.0, TC=15.0, DL=0.0, CMIN=6.0, LMIN=0.0),
     "L14": dict(HC=150.0, HW=45.0, DH=+5.0, SK=0.75, DL=-5.0, CMIN=6.0, LMIN=0.0),
     "L18": dict(HC=186.0, HW=40.0, TH=162.0, TC=14.0, DL=0.0, CMIN=3.0, LMIN=0.0),
     "L05": dict(HC=44.0, HW=16.0, TH=36.0, TC=22.0, DL=0.0, CMIN=8.0, LMIN=0.0)}

def lab_of(rgb):
    lab = cv2.cvtColor(rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab); A, B = lab[..., 1], lab[..., 2]
    return lab, np.hypot(A, B), (np.degrees(np.arctan2(B, A)) + 360) % 360

def tone(piece, src, dst, box=None):
    im = Image.open(O(src)); alpha = im.split()[3] if im.mode == "RGBA" else None       # a cut-out keeps its alpha
    q = P[piece]; rgb = np.asarray(im.convert("RGB")); lab, C, h = lab_of(rgb)
    w = (np.clip((C - q["CMIN"]) / 6, 0, 1) * np.clip(1 - np.abs(((h - q["HC"] + 180) % 360) - 180) / q["HW"], 0, 1) ** 0.5
         * np.clip((lab[..., 0] - q["LMIN"]) / 6 + 1, 0, 1))
    if box:   # the ellipse inscribed in the box: a round stud on skin of nearly the same hue keeps the skin round it untouched
        b = np.zeros(C.shape, np.float32); x0, y0, x1, y1 = box
        cv2.ellipse(b, ((x0 + x1) // 2, (y0 + y1) // 2), ((x1 - x0) // 2, (y1 - y0) // 2), 0, 0, 360, 1, -1); w = w * cv2.GaussianBlur(b, (0, 0), 1.5)
    w = cv2.GaussianBlur(w.astype(np.float32), (0, 0), 1.0); m = w > 0.5
    dh, sk = (q["TH"] - np.median(h[m]), q["TC"] / np.median(C[m])) if "TH" in q else (q["DH"], q["SK"])
    h2 = np.radians(h + dh * w); C2 = C * (1 - (1 - sk) * w)
    lab2 = lab.copy(); lab2[..., 0] = np.clip(lab[..., 0] + q["DL"] * w, 0, 100)
    lab2[..., 1] = C2 * np.cos(h2); lab2[..., 2] = C2 * np.sin(h2)
    rgb2 = np.clip(cv2.cvtColor(lab2.astype(np.float32), cv2.COLOR_Lab2RGB), 0, 1)
    out = Image.fromarray((rgb2 * 255 + 0.5).astype(np.uint8))
    if alpha is not None: out.putalpha(alpha)
    out.save(O(dst))
    _, C3, h3 = lab_of((rgb2 * 255 + 0.5).astype(np.uint8))
    print(src, "->", dst, "stone px", int(m.sum()), "hue %.0f -> %.0f, chroma %.1f -> %.1f" % (np.median(h[m]), np.median(h3[m]), np.median(C[m]), np.median(C3[m])) if m.any() else "")

if __name__ == "__main__":
    for a in sys.argv[2:]:
        k, *b = a.split(":"); tone(sys.argv[1], k, k + "_t", tuple(map(int, b[0].split(","))) if b else None)
