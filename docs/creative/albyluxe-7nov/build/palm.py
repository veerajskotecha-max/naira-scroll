# In-palm size photos (the P frame), as ../../stock-2nov/build/comp.py palm: the background-removed approved packshot (out/<KEY>_rb.png,
# from Higgsfield remove_background) is scaled to its true size and laid on the empty-palm plate (out/plate_palm.png, the 2 Nov plate
# N02_Pclean: fingers about 100 px, about 16 mm, so 6.25 px per mm), turned to lie naturally, with a soft contact shadow -> out/<KEY>_P.png.
# OBJ_PX is a dimension measured in the cut-out, OBJ_MM its true size from listings.json, so the piece lands at its real size on the hand.
# 12 Nov (../corrections.md): the cut-out's edge is shrunk 1 px first (a pale rim from the packshot's cream showed at 4-5x); and for a
# necklace whose cut-out holds only part of its chain (CLIP 1), the chain arms are laid running off the edge of the hand and cut at the
# hand's outline, as if they fall behind it (they used to stop mid-palm with blunt ends).
# ERASE clears parts of a cut-out that would not show with the piece lying in the palm: the Emerald-Cut Bezel Studs' posts stick out
# sideways in the upright packshot, but lying flat they point down into the palm.
# KEY may be OUT:CUT, to lay out/CUT.png (e.g. a toned cut-out, L05:L05_rb_t) and save out/OUT_P.png.
# Usage: python3 -I palm.py KEY OBJ_PX OBJ_MM ANGLE CX CY [CLIP]
import os, sys
import numpy as np, cv2
from PIL import Image, ImageFilter
H = os.path.dirname(os.path.abspath(__file__)); PX_MM = 6.25
ERASE = {"L15": [(878, 980, 962, 1024), (1246, 1056, 1340, 1104)]}     # x0, y0, x1, y1 in out/<KEY>_rb.png

def hand_mask(plate):
    rgb = np.asarray(plate.convert("RGB")).astype(np.float32) / 255; lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab)
    C = np.hypot(lab[..., 1], lab[..., 2]); skin = ((C > 22) & (lab[..., 0] < 82)).astype(np.uint8)          # the cream backdrop is C 9-18
    skin = cv2.morphologyEx(skin, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8)); skin = cv2.morphologyEx(skin, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    return Image.fromarray((cv2.GaussianBlur(cv2.erode(skin, np.ones((5, 5), np.uint8)).astype(np.float32), (0, 0), 1.5) * 255).astype(np.uint8))

def palm(key, obj_px, obj_mm, angle, cx, cy, clip=False):
    plate = Image.open(os.path.join(H, "out", "plate_palm.png")).convert("RGBA")
    key, src = key.split(":") if ":" in key else (key, f"{key}_rb")
    cut = Image.open(os.path.join(H, "out", f"{src}.png")).convert("RGBA")
    for x0, y0, x1, y1 in ERASE.get(key, []): cut.paste((0, 0, 0, 0), (x0, y0, x1, y1))
    bb = cut.getbbox(); cut = cut.crop(bb)
    cut.putalpha(cut.split()[3].filter(ImageFilter.MinFilter(3)))                         # defringe
    s = obj_mm * PX_MM / obj_px
    cut = cut.resize((max(1, round(cut.width * s)), max(1, round(cut.height * s))), Image.LANCZOS).rotate(angle, resample=Image.BICUBIC, expand=True)
    x, y = cx - cut.width // 2, cy - cut.height // 2
    a = cut.split()[3]
    sh = Image.new("RGBA", cut.size, (60, 35, 20, 0)); sh.putalpha(a.filter(ImageFilter.GaussianBlur(5)).point(lambda v: int(v * 0.38)))
    if clip:
        hm = hand_mask(plate)
        for im, dx, dy in ((cut, x, y), (sh, x + 5, y + 7)):
            m = hm.crop((dx, dy, dx + im.width, dy + im.height))
            im.putalpha(Image.fromarray((np.asarray(im.split()[3]).astype(np.float32) * np.asarray(m).astype(np.float32) / 255).astype(np.uint8)))
    plate.alpha_composite(sh, (x + 5, y + 7)); plate.alpha_composite(cut, (x, y))
    plate.convert("RGB").save(os.path.join(H, "out", f"{key}_P.png")); print(key, "P", cut.size, (x, y), round(s, 4), "clipped to the hand" if clip else "")

if __name__ == "__main__":
    k, px, mm, ang, cx, cy = sys.argv[1:7]; palm(k, float(px), float(mm), float(ang), int(cx), int(cy), len(sys.argv) > 7 and sys.argv[7] == "1")
