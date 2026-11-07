# In-palm size photos (the P frame), as ../../stock-2nov/build/comp.py palm: the background-removed approved packshot (out/<KEY>_rb.png,
# from Higgsfield remove_background) is scaled to its true size and laid on the empty-palm plate (out/plate_palm.png, the 2 Nov plate
# N02_Pclean: fingers about 100 px, about 16 mm, so 6.25 px per mm), turned to lie naturally, with a soft contact shadow -> out/<KEY>_P.png.
# OBJ_PX is a dimension measured in the cut-out, OBJ_MM its true size from listings.json, so the piece lands at its real size on the hand.
# Usage: python3 -I palm.py KEY OBJ_PX OBJ_MM ANGLE CX CY
import os, sys
from PIL import Image, ImageFilter
H = os.path.dirname(os.path.abspath(__file__)); PX_MM = 6.25

def palm(key, obj_px, obj_mm, angle, cx, cy):
    plate = Image.open(os.path.join(H, "out", "plate_palm.png")).convert("RGBA")
    cut = Image.open(os.path.join(H, "out", f"{key}_rb.png")).convert("RGBA")
    bb = cut.getbbox(); cut = cut.crop(bb)
    s = obj_mm * PX_MM / obj_px
    cut = cut.resize((max(1, round(cut.width * s)), max(1, round(cut.height * s))), Image.LANCZOS).rotate(angle, resample=Image.BICUBIC, expand=True)
    x, y = cx - cut.width // 2, cy - cut.height // 2
    a = cut.split()[3]
    sh = Image.new("RGBA", cut.size, (60, 35, 20, 0)); sh.putalpha(a.filter(ImageFilter.GaussianBlur(5)).point(lambda v: int(v * 0.38)))
    plate.alpha_composite(sh, (x + 5, y + 7)); plate.alpha_composite(cut, (x, y))
    plate.convert("RGB").save(os.path.join(H, "out", f"{key}_P.png")); print(key, "P", cut.size, (x, y), round(s, 4))

if __name__ == "__main__":
    k, px, mm, ang, cx, cy = sys.argv[1:7]; palm(k, float(px), float(mm), float(ang), int(cx), int(cy))
