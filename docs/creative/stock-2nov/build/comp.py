# Local composites for A14 Solitaire Charm Huggies (3 Nov 2026), where Higgsfield drew the pair 1.3 to 1.4x the measured size and its
# shrink edits dropped the square tube.
#  palm: the background-removed pair from the approved packshot (comp/a14_pair_cut.png, cut from out/A14_H_a.png at (570, 620)) pasted
#        onto the empty-palm plate out/N02_Pclean.png (fingers about 100 px, about 16 mm, so 6.25 px per mm) with the hoop at 13 mm
#        (its 455 px height in the cut -> 81 px), turned to lie along the palm, with a soft contact shadow -> out/A14_Pcomp.png
#  worn: the earring in an original worn frame, masked by its difference from a bare-lobe edit of the same frame and by colour (gold
#        or a bright colourless stone, so the lobe's own shading stays behind), is scaled about its
#        piercing point and pasted onto the bare-lobe frame -> out/<key>.png
#  stud: as worn, for a stud with an open centre (A15 Pave Open Heart Studs, 3 Nov afternoon): only small enclosed holes in the mask are filled, so
#        the heart's open centre shows the bare-lobe frame behind it.
# Usage: python3 -I comp.py palm [CUT OUT HOOP_PX ANGLE CX CY] | run_palm | unloop | worn SRC BARE OUT X0 Y0 X1 Y1 AX AY SCALE [DARK [LOBE_Y]]
#                           | stud SRC BARE OUT X0 Y0 X1 Y1 AX AY SCALE [DARK [MAXHOLE]]
#                           | hug  SRC BARE OUT X0 Y0 X1 Y1 AX AY SCALE [DARK [LOBE_Y]]   (worn, with specks under 200 px dropped)
#                           | tone SRC OUT DH SK [H0 HR SMAX X0 Y0 X1 Y1]   (B1 Orb Cable Cuff: the gold shifted to the paler yellow of the stock)
import sys, os
import numpy as np
from PIL import Image, ImageFilter
H = os.path.dirname(os.path.abspath(__file__)); O = lambda k: os.path.join(H, "out", k + ".png")

def palm(angle=-25, centre=(960, 1255), hoop_px=455, hoop_mm=13.0, px_mm=6.25, cut_name="a14_pair_cut.png", out="A14_Pcomp"):
    plate = Image.open(O("N02_Pclean")).convert("RGBA"); cut = Image.open(os.path.join(H, "comp", cut_name)).convert("RGBA")
    s = hoop_mm * px_mm / hoop_px
    cut = cut.resize((round(cut.width * s), round(cut.height * s)), Image.LANCZOS).rotate(angle, resample=Image.BICUBIC, expand=True)
    x, y = centre[0] - cut.width // 2, centre[1] - cut.height // 2
    a = cut.split()[3]
    sh = Image.new("RGBA", cut.size, (60, 35, 20, 0)); sh.putalpha(a.filter(ImageFilter.GaussianBlur(5)).point(lambda v: int(v * 0.38)))
    plate.alpha_composite(sh, (x + 5, y + 7)); plate.alpha_composite(cut, (x, y))
    plate.convert("RGB").save(O(out)); print("palm", out, cut.size, (x, y), round(s, 3))

def fill_holes(b):
    """Fill enclosed holes in a boolean mask: flood the background in from the border (4-connected), keep everything else."""
    h, w = b.shape; seen = np.zeros_like(b); stack = [(y, x) for y in (0, h - 1) for x in range(w)] + [(y, x) for x in (0, w - 1) for y in range(h)]
    while stack:
        y, x = stack.pop()
        if 0 <= y < h and 0 <= x < w and not seen[y, x] and not b[y, x]:
            seen[y, x] = True; stack += [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return ~seen

def small_holes(b, box, maxarea):
    """Fill only the enclosed holes of at most maxarea pixels inside box (the stones' dark facets), so a large enclosed opening such as
    the open centre of a heart stays open and shows the bare frame behind it."""
    x0, y0, x1, y1 = box; sub = b[y0:y1, x0:x1].copy(); h, w = sub.shape; lab = np.zeros(sub.shape, np.int32); n = 0
    for sy in range(h):
        for sx in range(w):
            if sub[sy, sx] or lab[sy, sx]: continue
            n += 1; lab[sy, sx] = n; stack = [(sy, sx)]; pts = []; edge = False
            while stack:
                y, x = stack.pop(); pts.append((y, x)); edge |= y in (0, h - 1) or x in (0, w - 1)
                for yy, xx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if 0 <= yy < h and 0 <= xx < w and not sub[yy, xx] and not lab[yy, xx]: lab[yy, xx] = n; stack.append((yy, xx))
            if not edge and len(pts) <= maxarea:
                for y, x in pts: sub[y, x] = True
    out = b.copy(); out[y0:y1, x0:x1] = sub; return out

def largest(b, box):
    """Keep only the largest 8-connected shape of a boolean mask inside box (the earring); stray patches where the bare-lobe edit
    also changed the hair or the skin are dropped."""
    x0, y0, x1, y1 = box; sub = b[y0:y1, x0:x1]; h, w = sub.shape; lab = np.zeros(sub.shape, np.int32); best, n = [], 0
    for sy in range(h):
        for sx in range(w):
            if not sub[sy, sx] or lab[sy, sx]: continue
            n += 1; lab[sy, sx] = n; stack = [(sy, sx)]; pts = []
            while stack:
                y, x = stack.pop(); pts.append((y, x))
                for yy in (y - 1, y, y + 1):
                    for xx in (x - 1, x, x + 1):
                        if 0 <= yy < h and 0 <= xx < w and sub[yy, xx] and not lab[yy, xx]: lab[yy, xx] = n; stack.append((yy, xx))
            if len(pts) > len(best): best = pts
    out = np.zeros_like(b)
    for y, x in best: out[y0 + y, x0 + x] = True
    return out

def drop_specks(b, box, minpart):
    """Drop 8-connected shapes of fewer than minpart pixels inside box (stray specks of hair or skin), keeping the earring's parts."""
    x0, y0, x1, y1 = box; sub = b[y0:y1, x0:x1]; h, w = sub.shape; lab = np.zeros(sub.shape, np.int32); out = np.zeros_like(b); n = 0
    for sy in range(h):
        for sx in range(w):
            if not sub[sy, sx] or lab[sy, sx]: continue
            n += 1; lab[sy, sx] = n; stack = [(sy, sx)]; pts = []
            while stack:
                y, x = stack.pop(); pts.append((y, x))
                for yy in (y - 1, y, y + 1):
                    for xx in (x - 1, x, x + 1):
                        if 0 <= yy < h and 0 <= xx < w and sub[yy, xx] and not lab[yy, xx]: lab[yy, xx] = n; stack.append((yy, xx))
            if len(pts) >= minpart:
                for y, x in pts: out[y0 + y, x0 + x] = True
    return out

def stud_mask(keep, box, maxhole, close=7, cut=9, smooth=9):
    """The band of an open stud, built by shape: close the speckled band, open it to cut the hair strands and skin patches that touch it,
    keep the largest shape, fill it solid, and take away its opening (its one large hole) smoothed, so neither stray patches nor a notched
    inner edge are pasted."""
    x0, y0, x1, y1 = box; f = lambda a, k, op: np.asarray(Image.fromarray(a).filter(op(k)))
    sub = (keep[y0:y1, x0:x1] * 255).astype(np.uint8)
    sub = f(f(sub, close, ImageFilter.MaxFilter), close, ImageFilter.MinFilter)          # close: one solid band
    sub = f(f(sub, cut, ImageFilter.MinFilter), cut, ImageFilter.MaxFilter)              # open: thin attachments go
    full = np.zeros(keep.shape, bool); full[y0:y1, x0:x1] = sub > 127
    band = largest(full, box); solid = fill_holes(band); hole = solid & ~small_holes(band, box, maxhole)
    hs = (hole[y0:y1, x0:x1] * 255).astype(np.uint8)
    hs = f(f(hs, smooth, ImageFilter.MinFilter), smooth, ImageFilter.MaxFilter)          # the opening's edge without notches
    hole[y0:y1, x0:x1] = hs > 127
    return ((solid & ~hole) * 255).astype(np.uint8)

def worn(src, bare, out, box, anchor, scale, thr=38, dark=95, lobe=0, maxhole=None, minpart=0):
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
    if maxhole is None:
        b = fill_holes(m > 127)                                                          # the stone's darker facets are not skin
        m = (drop_specks(b, box, minpart) if minpart else b).astype(np.uint8) * 255
    else: m = stud_mask(keep, box, maxhole)                                             # stud: the heart only, its open centre clean
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

def tone(src, out, dh=9.0, sk=0.8, s0=0.22, s1=0.32, h0=12.0, h1=62.0, hr=6.0, smax=None, box=None):
    """Shift the gold's hue by dh degrees and scale its saturation by sk (B1 Orb Cable Cuff, 3 Nov: Higgsfield drew a warm orange
    gold, hue about 32 deg and saturation about 0.5, where the cuffs in the owner's photo, white balance neutral on the bag, read a
    paler yellow gold of about 40 to 46 deg). The weight ramps in from saturation s0 to s1 and fades at the hue limits, so the cream
    ground (saturation about 0.19) stays as it is."""
    im = Image.open(O(src)).convert("RGB"); hsv = np.asarray(im.convert("HSV")).astype(np.float32)
    h, s = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255
    w = np.clip((s - s0) / (s1 - s0), 0, 1) * np.clip((h - h0) / hr, 0, 1) * np.clip((h1 - h) / 6, 0, 1)
    if smax: w *= np.clip((smax - s) / 0.08, 0, 1)            # worn frames: the saffron camisole is far more saturated than the gold
    if box:                                                   # worn frames: only inside a feathered box round the cuff
        m = Image.new("L", im.size, 0); m.paste(255, tuple(int(v) for v in box))
        w *= np.asarray(m.filter(ImageFilter.GaussianBlur(12))).astype(np.float32) / 255
    hsv[..., 0] = ((h + dh * w) % 360) * 255 / 360; hsv[..., 1] = np.clip(s * (1 - (1 - sk) * w), 0, 1) * 255
    t = np.asarray(Image.fromarray(np.round(hsv).astype(np.uint8), "HSV").convert("RGB")).astype(np.float32)
    k = (w > 0.002)[..., None]                                # pixels outside the gold keep their exact RGB (the HSV round trip is lossy)
    o = np.where(k, t, np.asarray(im).astype(np.float32))
    Image.fromarray(np.round(o).astype(np.uint8)).save(O(out)); print(out, "toned", dh, sk)

if __name__ == "__main__":
    if sys.argv[1] == "palm" and len(sys.argv) > 2:      # palm CUT OUT HOOP_PX ANGLE CX CY
        c, o, hp, ang, cx, cy = sys.argv[2:8]; palm(float(ang), (int(cx), int(cy)), float(hp), cut_name=c, out=o)
    elif sys.argv[1] == "palm": palm()
    elif sys.argv[1] == "hug":                           # hug SRC BARE OUT X0 Y0 X1 Y1 AX AY SCALE [DARK [LOBE_Y]]: worn, specks dropped
        s, b, o, *n = sys.argv[2:]; n = [float(v) for v in n]
        worn(s, b, o, tuple(int(v) for v in n[0:4]), (n[4], n[5]), n[6], 38, *[int(v) for v in n[7:9]], minpart=200)
    elif sys.argv[1] == "stud":                          # stud SRC BARE OUT X0 Y0 X1 Y1 AX AY SCALE [DARK [MAXHOLE]]
        s, b, o, *n = sys.argv[2:]; n = [float(v) for v in n]
        worn(s, b, o, tuple(int(v) for v in n[0:4]), (n[4], n[5]), n[6], 38, int(n[7]) if len(n) > 7 else 95, 0,
             int(n[8]) if len(n) > 8 else 900)
    elif sys.argv[1] == "run_palm": run_palm()
    elif sys.argv[1] == "unloop": unloop()
    elif sys.argv[1] == "tone":                          # tone SRC OUT DH SK [H0 HR SMAX X0 Y0 X1 Y1]: shift the gold hue by DH deg, scale its
        n = [float(v) for v in sys.argv[4:]]              # saturation by SK; on worn frames, from hue H0 (ramp HR), under SMAX, in the box
        kw = dict(h0=n[2], hr=n[3], smax=n[4], box=n[5:9]) if len(n) > 2 else {}
        tone(sys.argv[2], sys.argv[3], n[0], n[1], **kw)
    else:
        s, b, o, *n = sys.argv[2:]; n = [float(v) for v in n]
        worn(s, b, o, tuple(int(v) for v in n[0:4]), (n[4], n[5]), n[6], 38, *[int(v) for v in n[7:9]])
