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
#                           | garland SRC BARE OUT SCALE X0 Y0 X1 Y1 TOPX TOPY   (C2: the worn clover necklace rebuilt at the bracelet's clover size)
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

def _label(b, minpix):
    """8-connected components of a small boolean mask (BFS); returns lists of (y, x) with at least minpix pixels."""
    h, w = b.shape; lab = np.zeros(b.shape, bool); parts = []
    for sy, sx in zip(*np.nonzero(b)):
        if lab[sy, sx]: continue
        lab[sy, sx] = True; stack = [(sy, sx)]; pts = []
        while stack:
            y, x = stack.pop(); pts.append((y, x))
            for yy in (y - 1, y, y + 1):
                for xx in (x - 1, x, x + 1):
                    if 0 <= yy < h and 0 <= xx < w and b[yy, xx] and not lab[yy, xx]: lab[yy, xx] = True; stack.append((yy, xx))
        if len(pts) >= minpix: parts.append(pts)
    return parts

def _catmull(P, n=40):
    """A Catmull-Rom curve through the points P (k x 2), n samples per span, with its unit tangents."""
    P = np.asarray(P, float); Q = np.vstack([2 * P[0] - P[1], P, 2 * P[-1] - P[-2]]); pts = []
    for i in range(1, len(Q) - 2):
        p0, p1, p2, p3 = Q[i - 1], Q[i], Q[i + 1], Q[i + 2]
        for t in np.linspace(0, 1, n, endpoint=False):
            pts.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    pts.append(P[-1]); C = np.asarray(pts); d = np.gradient(C, axis=0); d /= np.linalg.norm(d, axis=1)[:, None] + 1e-9
    s = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(C, axis=0), axis=1))]); return C, d, s

def garland(src, bare, out, scale, box, top, thr=40):
    """Lay a worn clover necklace back on its bare plate with every clover at `scale` of the size Higgsfield drew it (C2 Clover Garland
    Necklace, 3 Nov: the bracelet's 10 mm clover is about 0.22 of the lip width, the necklace's worn frames drew it at about 0.32).
    The clovers' centres (red stones, merged and labelled at quarter size inside box) are ordered round the U by angle about `top`, a
    point above it, and joined by a Catmull-Rom curve. Each original clover is cut, turned so the curve is level at it, as a link from half
    a pitch before it to half a pitch after, with its mask (its difference from the bare plate, kept to red, gold and clear-stone pixels).
    New links, `scale` times the size, go every scale x pitch along the same curve from the first clover to the last; each uses the
    original link nearest its place on the curve (so the foreshortening and the light round the neck stay), is turned to the curve, and
    gets a soft contact shadow."""
    A = Image.open(O(src)).convert("RGB"); Bimg = Image.open(O(bare)).convert("RGB")
    a = np.asarray(A).astype(np.int16); b = np.asarray(Bimg).astype(np.int16)
    hsv = np.asarray(A.convert("HSV")).astype(np.float32); hh, ss, vv = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255, hsv[..., 2] / 255
    red = ((hh < 14) | (hh > 338)) & (ss > 0.5) & (vv > 0.2)
    gold = (hh >= 26) & (hh <= 56) & (ss >= 0.45) & (vv >= 0.3); clear = (vv >= 0.72) & (ss <= 0.3)
    x0, y0, x1, y1 = box; inside = np.zeros(red.shape, bool); inside[y0:y1, x0:x1] = True
    q = (red & inside)[::4, ::4]; q = np.asarray(Image.fromarray((q * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 127
    parts = [pts for pts in _label(q, 12) if len(pts) >= 40]                                 # specks dropped; partial clovers kept for now
    area = np.array([len(pts) for pts in parts]); full = area >= 0.6 * np.median(area[area >= 150])
    cen = np.array([[np.mean([p[1] for p in pts]) * 4 + 2, np.mean([p[0] for p in pts]) * 4 + 2] for pts in parts])
    size = np.median([max(max(p[1] for p in pts) - min(p[1] for p in pts), max(p[0] for p in pts) - min(p[0] for p in pts)) * 4
                      for pts, f in zip(parts, full) if f])
    order = np.argsort(-np.arctan2(cen[:, 1] - top[1], cen[:, 0] - top[0])); cen, full = cen[order], full[order]   # round the U
    C, D, S = _catmull(cen); ci = [int(np.argmin(np.linalg.norm(C - c, axis=1))) for c in cen]
    fi = [i for i, f in zip(ci, full) if f]                  # the links are cut from whole clovers only; a part-hidden end clover only
    pitch = np.median(np.diff(S[fi])); keep = (np.abs(a - b).sum(axis=2) > thr) & (red | gold | clear) & inside   # marks where the line goes
    bh = np.asarray(Bimg.convert("HSV")).astype(np.float32)[..., 2] / 255
    occl = Image.fromarray(((bh >= 0.28) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))   # hair in the bare plate hides the line
    m = Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))
    m = Image.fromarray((fill_holes(np.asarray(m) > 127) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
    rgba = A.convert("RGBA"); rgba.putalpha(m); Hh = int(size * 1.5); sf = S[fi]
    lp = np.array([np.mean([d for d in (sf[min(k + 1, len(sf) - 1)] - sf[k], sf[k] - sf[max(k - 1, 0)]) if d > 0]) for k in range(len(sf))])
    order_k = sorted(range(len(fi)), key=lambda k: -lp[k]); full_p = float(np.mean(lp[order_k[:3]])); links = []
    for k in order_k:                  # the links are cut from the clovers that face the camera most squarely (largest spacing), and
        if len(links) == 3: break      # only those with a ring stub at BOTH ends, so the chain never breaks
        i = fi[k]; ang = np.degrees(np.arctan2(D[i][1], D[i][0])); cx, cy = C[i]; L = int(lp[k])
        r = rgba.rotate(ang, resample=Image.BICUBIC, center=(cx, cy))                        # PIL turns counter-clockwise: the curve goes level
        link = r.crop((int(cx - L / 2), int(cy - Hh / 2), int(cx - L / 2) + L, int(cy - Hh / 2) + Hh))
        al = np.asarray(link.split()[3]); own = largest(al > 40, (0, 0, al.shape[1], al.shape[0]))   # this clover and the rings joined to it
        own = np.asarray(Image.fromarray((own * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3))) > 127
        al2 = al * own; e = max(3, L // 12)
        if al2[:, :e].max() < 128 or al2[:, -e:].max() < 128: continue
        link.putalpha(Image.fromarray(al2.astype(np.uint8))); links.append((link, L)); link.save(os.path.join(H, "comp", f"{out}_link{len(links)}.png"))
    s0, s1 = S[ci[0]], S[ci[-1]]; spots = [s0]       # step by scale x the local spacing, so the chain recedes up the sides as it did
    while True:
        nxt = spots[-1] + scale * float(np.interp(spots[-1], sf, lp))
        if nxt > s1 + 1e-6: break
        spots.append(nxt)
    base = Bimg.convert("RGBA"); n_new = len(spots); unit = scale
    for t, s_ in enumerate(spots):
        j = int(np.argmin(np.abs(S - s_))); link, L = links[t % len(links)]; ph = float(np.interp(s_, sf, lp)) / full_p   # foreshortening here
        link = link.resize((max(1, round(L * scale * ph)), max(1, round(Hh * scale * (0.85 + 0.15 * ph)))), Image.LANCZOS)
        link = link.rotate(-np.degrees(np.arctan2(D[j][1], D[j][0])), resample=Image.BICUBIC, expand=True)
        x, y = int(round(C[j][0] - link.width / 2)), int(round(C[j][1] - link.height / 2))
        al = np.asarray(link.split()[3]).astype(np.float32) * np.asarray(occl.crop((x, y, x + link.width, y + link.height))).astype(np.float32) / 255
        al[al < 40] = 0                                                                         # no faint scraps at the link's edges
        if al.sum() < 0.35 * np.asarray(link.split()[3]).astype(np.float32).sum(): continue    # mostly behind the hair: left out whole
        al = al * drop_specks(al > 0, (0, 0, al.shape[1], al.shape[0]), 60)                   # no specks left where hair strands cross it
        link.putalpha(Image.fromarray(al.astype(np.uint8)))
        sh = Image.new("RGBA", link.size, (55, 30, 18, 0)); sh.putalpha(link.split()[3].filter(ImageFilter.GaussianBlur(4)).point(lambda v: int(v * 0.32)))
        base.alpha_composite(sh, (x + 2, y + 4)); base.alpha_composite(link, (x, y))
    base.convert("RGB").save(O(out)); m.save(os.path.join(H, "comp", out + "_mask.png"))
    print("garland", out, "clovers", len(cen), "(whole", len(fi), ") ->", n_new, "| clover", round(size), "px -> about", round(size * unit), "| pitch", round(pitch), "->", round(pitch * unit))

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
    elif sys.argv[1] == "garland":                       # garland SRC BARE OUT SCALE X0 Y0 X1 Y1 TOPX TOPY
        n = [float(v) for v in sys.argv[5:]]; garland(sys.argv[2], sys.argv[3], sys.argv[4], n[0], tuple(int(v) for v in n[1:5]), (n[5], n[6]))
    elif sys.argv[1] == "tone":                          # tone SRC OUT DH SK [H0 HR SMAX X0 Y0 X1 Y1]: shift the gold hue by DH deg, scale its
        n = [float(v) for v in sys.argv[4:]]              # saturation by SK; on worn frames, from hue H0 (ramp HR), under SMAX, in the box
        kw = dict(h0=n[2], hr=n[3], smax=n[4], box=n[5:9]) if len(n) > 2 else {}
        tone(sys.argv[2], sys.argv[3], n[0], n[1], **kw)
    else:
        s, b, o, *n = sys.argv[2:]; n = [float(v) for v in n]
        worn(s, b, o, tuple(int(v) for v in n[0:4]), (n[4], n[5]), n[6], 38, *[int(v) for v in n[7:9]])
