# Local composites for A14 Solitaire Charm Huggies (3 Nov 2026), where Higgsfield drew the pair 1.3 to 1.4x the measured size and its
# shrink edits dropped the square tube.
#  palm: the background-removed pair from the approved packshot (comp/a14_pair_cut.png, cut from out/A14_H_a.png at (570, 620)) pasted
#        onto the empty-palm plate out/N02_Pclean.png (fingers about 100 px, about 16 mm, so 6.25 px per mm) with the hoop at 13 mm
#        (its 455 px height in the cut -> 81 px), turned to lie along the palm, with a soft contact shadow -> out/A14_Pcomp.png
#  worn: the earring in an original worn frame, masked by its difference from a bare-lobe edit of the same frame and by colour (gold
#        or a bright colourless stone, so the lobe's own shading stays behind), is scaled about its
#        piercing point and pasted onto the bare-lobe frame -> out/<key>.png
# Usage: python3 -I comp.py palm | run_palm | unloop | worn SRC BARE OUT X0 Y0 X1 Y1 AX AY SCALE [DARK [LOBE_Y]]
import sys, os
import numpy as np
from PIL import Image, ImageFilter
H = os.path.dirname(os.path.abspath(__file__)); O = lambda k: os.path.join(H, "out", k + ".png")

def palm(angle=-25, centre=(960, 1255), hoop_px=455, hoop_mm=13.0, px_mm=6.25):
    plate = Image.open(O("N02_Pclean")).convert("RGBA"); cut = Image.open(os.path.join(H, "comp", "a14_pair_cut.png")).convert("RGBA")
    s = hoop_mm * px_mm / hoop_px
    cut = cut.resize((round(cut.width * s), round(cut.height * s)), Image.LANCZOS).rotate(angle, resample=Image.BICUBIC, expand=True)
    x, y = centre[0] - cut.width // 2, centre[1] - cut.height // 2
    a = cut.split()[3]
    sh = Image.new("RGBA", cut.size, (60, 35, 20, 0)); sh.putalpha(a.filter(ImageFilter.GaussianBlur(5)).point(lambda v: int(v * 0.38)))
    plate.alpha_composite(sh, (x + 5, y + 7)); plate.alpha_composite(cut, (x, y))
    plate.convert("RGB").save(O("A14_Pcomp")); print("palm", cut.size, (x, y), round(s, 3))

def fill_holes(b):
    """Fill enclosed holes in a boolean mask: flood the background in from the border (4-connected), keep everything else."""
    h, w = b.shape; seen = np.zeros_like(b); stack = [(y, x) for y in (0, h - 1) for x in range(w)] + [(y, x) for x in (0, w - 1) for y in range(h)]
    while stack:
        y, x = stack.pop()
        if 0 <= y < h and 0 <= x < w and not seen[y, x] and not b[y, x]:
            seen[y, x] = True; stack += [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return ~seen

def worn(src, bare, out, box, anchor, scale, thr=38, dark=95, lobe=0):
    A = np.asarray(Image.open(O(src)).convert("RGB")).astype(np.int16); B = np.asarray(Image.open(O(bare)).convert("RGB")).astype(np.int16)
    x0, y0, x1, y1 = box; d = np.abs(A - B).sum(axis=2); m = np.zeros(d.shape, np.uint8)
    hsv = np.asarray(Image.open(O(src)).convert("HSV")).astype(np.int16); hh, ss, vv = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    gold = (hh >= 15) & (hh <= 48) & (ss >= 70) & (vv >= dark)        # PIL hue 0-255; dark: lowest value kept (shadowed gold)
    stone = (vv >= 170) & (ss <= 80)                                   # the clear stone: bright and nearly colourless
    keep = (d > thr) & (gold | stone)
    if lobe:                                   # below the lobe's edge only the earring changed: the difference alone, specks opened away
        below = np.asarray(Image.fromarray(((d > thr + 10) * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))) > 127
        keep[lobe:, :] = below[lobe:, :] | keep[lobe:, :]
    m[y0:y1, x0:x1] = keep[y0:y1, x0:x1] * 255
    m = np.asarray(Image.fromarray(m).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(5)))
    m = fill_holes(m > 127).astype(np.uint8) * 255                     # the stone's darker facets are not skin
    mask = Image.fromarray(m).filter(ImageFilter.GaussianBlur(1.2))
    layer = Image.open(O(src)).convert("RGBA"); layer.putalpha(mask); layer = layer.crop(box)
    ax, ay = anchor[0] - x0, anchor[1] - y0
    w, h = round(layer.width * scale), round(layer.height * scale); layer = layer.resize((w, h), Image.LANCZOS)
    base = Image.open(O(bare)).convert("RGBA"); base.alpha_composite(layer, (round(anchor[0] - ax * scale), round(anchor[1] - ay * scale)))
    base.convert("RGB").save(O(out)); Image.fromarray(m).save(os.path.join(H, "comp", out + "_mask.png")); print("worn", out, (w, h))

def run_palm(angle=-71, centre=(1205, 1265), clover_px=180, clover_mm=10.0, px_mm=6.25):
    """C2 Clover Garland Necklace: the back run of clovers from the approved packshot (comp/c2_run_cut.png, the background-removed crop
    of out/C2_H_a.png at (150, 540)); the front strand and the turn at the left are cut away along a line, the run is scaled to 10 mm
    clovers and laid across the palm of out/N02_Pclean.png from the web of the thumb towards the heel of the hand -> out/C2_Pcomp.png"""
    cut = Image.open(os.path.join(H, "comp", "c2_run_cut.png")).convert("RGBA"); a = np.asarray(cut.split()[3]).copy()
    pts = [(0, 190), (420, 240), (690, 340), (960, 430), (1200, 500), (1510, 600)]
    yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]; line = np.interp(xx, [p[0] for p in pts], [p[1] for p in pts])
    a[(yy >= line) | (xx < 200)] = 0; cut.putalpha(Image.fromarray(a)); cut = cut.crop(cut.getbbox())
    s = clover_mm * px_mm / clover_px
    cut = cut.resize((round(cut.width * s), round(cut.height * s)), Image.LANCZOS).rotate(angle, resample=Image.BICUBIC, expand=True)
    plate = Image.open(O("N02_Pclean")).convert("RGBA"); x, y = centre[0] - cut.width // 2, centre[1] - cut.height // 2
    sh = Image.new("RGBA", cut.size, (60, 35, 20, 0)); sh.putalpha(cut.split()[3].filter(ImageFilter.GaussianBlur(5)).point(lambda v: int(v * 0.4)))
    plate.alpha_composite(sh, (x + 5, y + 7)); plate.alpha_composite(cut, (x, y))
    plate.convert("RGB").save(O("C2_Pcomp")); print("run_palm", cut.size, (x, y), round(s, 3))

def unloop(src="C2_Pf_a", plate="N02_Pclean", out="C2_Pu", grow=3):
    """C2: the blend edits drew the loop hanging below the hand with the clovers' plain gold backs. The blended frame lines up with the
    empty-palm plate it was made from (mean difference about 6 in the background), so the blended frame is kept only on the hand
    (comp/n02_hand_mask.png grown a few pixels) and the plate is used everywhere else: the loop goes and the line ends over the palm's edge."""
    A = Image.open(O(src)).convert("RGB"); B = Image.open(O(plate)).convert("RGB")
    hand = Image.open(os.path.join(H, "comp", "n02_hand_mask.png")).convert("L")
    for _ in range(grow): hand = hand.filter(ImageFilter.MaxFilter(7))
    Image.composite(A, B, hand.filter(ImageFilter.GaussianBlur(4))).save(O(out)); print("unloop", out)

if __name__ == "__main__":
    if sys.argv[1] == "palm": palm()
    elif sys.argv[1] == "run_palm": run_palm()
    elif sys.argv[1] == "unloop": unloop()
    else:
        s, b, o, *n = sys.argv[2:]; n = [float(v) for v in n]
        worn(s, b, o, tuple(int(v) for v in n[0:4]), (n[4], n[5]), n[6], 38, *[int(v) for v in n[7:9]])
