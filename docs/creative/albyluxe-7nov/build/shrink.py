# Takes a piece (or one part of it) down to its true size in a worn frame where the generator drew it too big, keeping its own light,
# shading and detail. 12 Nov (../corrections.md): retries with ever-stronger size wording brought these pieces down a step at a time but not
# all the way, so the last step is done here, after measuring each against the body:
#   L13 Lattice Lace Ring (W1y, W2y): the lattice was 1.05-1.15 finger widths across and 1.4-1.5 along the finger, where the supplier's
#       worn photo shows about 0.8 by 0.8 (measured across the gaps between the fingers); openwork, so only its wires move.
#   L09 Duet Emerald-Cut Cuff (W1x): the wire is right (2 mm, 14 px) but each stone and its box is about twice its size (9-10 mm against 5):
#       each box shrinks toward the joint where its wire enters, so the wire stays attached.
# How: the part is found inside its box (gold: the surest wires first, hue over 70 and chroma over 30, which no skin reaches, then every
# pixel over hue 64 near them; stones: clear is bright and colourless, pink sits at hue 300-35). The skin under the whole old outline is
# filled from the skin round it (inpainting, so no old shadow or wire is left), its pores and lines copied back from nearby skin, and its colour
# matched to the skin just outside. The part then goes back at F times its size about its anchor, with a soft shadow to the lower right
# (the key light is from camera-left).
# Usage: python3 -I shrink.py KEY OUT PART [PART ...] -> out/OUT.png, where PART is F:x0,y0,x1,y1[:ax,ay][:solid][:poly=x,y,...][:keep=x,y,...]
#        (without an anchor the part shrinks about its own centre; "solid" for stones and solid metal, otherwise openwork wires; poly= traces
#        a solid part's outline by hand where its shadowed walls sit at a skin-like hue; keep= is a polygon left exactly as it is, neither
#        moved nor filled: the wire's collar a stone box hangs from, so the smaller box stays attached)
import os, sys
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))

def masks(I, box, solid):
    f = I / 255; lab = cv2.cvtColor(f, cv2.COLOR_RGB2Lab); C = np.hypot(lab[..., 1], lab[..., 2])
    hue = (np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) + 360) % 360; L = lab[..., 0]
    bx = np.zeros(C.shape, np.uint8); x0, y0, x1, y1 = box; bx[y0:y1, x0:x1] = 1
    seed = ((hue > 70) & (C > 30)).astype(np.uint8) & bx
    if solid: seed |= (((L > 45) & (C < 13)) | (((hue > 300) | (hue < 35)) & (C > 8) & (L > 45))).astype(np.uint8) & bx   # clear, pink
    n, lb, st, _ = cv2.connectedComponentsWithStats(cv2.morphologyEx(seed, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17))))
    core = (lb == 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    reg = np.zeros_like(core); cv2.fillConvexPoly(reg, cv2.convexHull(cv2.findNonZero(core)), 1); reg = cv2.dilate(reg, np.ones((31, 31), np.uint8))
    part = ((((hue > 64) & (C > 20)).astype(np.uint8)) | seed) & reg & bx                   # in a paler light gold comes down to hue 64
    n, lb, st, _ = cv2.connectedComponentsWithStats(cv2.morphologyEx(part, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17 if not solid else 9,) * 2)))
    sil = (lb == 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    cnts, _ = cv2.findContours(sil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE); sil = np.zeros_like(sil); cv2.drawContours(sil, cnts, -1, 1, -1)
    sil &= bx; part &= sil
    if solid:   # a stone box is convex, and its shadowed gold walls sit at a skin-like hue: take the hull of its surest pixels, grown a little
        sil = np.zeros_like(core); cv2.fillConvexPoly(sil, cv2.convexHull(cv2.findNonZero(core)), 1)
        sil = cv2.dilate(sil, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))) & bx
    return sil, (sil if solid else cv2.dilate(part, np.ones((3, 3), np.uint8)) & sil), hue, C, bx

def shrink(I, F, box, anchor=None, solid=False, poly=None, keep_poly=None):
    sil, piece, hue, C, bx = masks(I, box, solid)
    keep = np.zeros_like(bx)
    if keep_poly: cv2.fillPoly(keep, [np.array(keep_poly, np.int32).reshape(-1, 2)], 1)
    if poly:
        sil = np.zeros_like(bx); cv2.fillPoly(sil, [np.array(poly, np.int32).reshape(-1, 2)], 1); piece = sil.copy()
    sil &= 1 - keep; piece &= 1 - keep
    ys, xs = np.nonzero(piece); ax, ay = anchor if anchor else (xs.mean(), ys.mean())
    # 1. the skin under the whole old outline
    fill = cv2.dilate(sil, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21) if poly else (17, 17)))
    if solid:   # a solid piece's contact shadow goes too: skin near it clearly darker than the skin round it (openwork casts none to speak of)
        L = cv2.GaussianBlur(cv2.cvtColor(I / 255, cv2.COLOR_RGB2Lab)[..., 0], (0, 0), 3)          # blurred, so skin grain is not 'shadow'
        near = (cv2.dilate(sil, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41))) > 0) & (fill == 0)
        med = np.median(L[near & ((hue < 63) | (C < 18))]); shadow = (near & (L < med - 6)).astype(np.uint8)
        n, lb, st, _ = cv2.connectedComponentsWithStats(shadow | fill)
        fill = cv2.dilate((lb == np.bincount(lb[fill > 0]).argmax()).astype(np.uint8), np.ones((11, 11), np.uint8))
    fill &= 1 - keep                                                                        # never into what is kept
    img8 = np.clip(I, 0, 255).astype(np.uint8); low = cv2.inpaint(img8, fill, 9, cv2.INPAINT_TELEA).astype(np.float32)
    ring = (cv2.dilate(sil, np.ones((31, 31), np.uint8)) - cv2.dilate(sil, np.ones((9, 9), np.uint8))).astype(bool)
    P = np.stack([xs, ys], 1).astype(np.float64); _, _, Vt = np.linalg.svd(P - P.mean(0), full_matrices=False); u = Vt[0]
    ext = np.ptp((P - P.mean(0)) @ u); best = None
    gold = (((hue > 64) & (C > 25)) | ((hue > 300) | (hue < 35)) & (C > 8)).astype(np.uint8)
    vs = (u, -u, Vt[1], -Vt[1], (u + Vt[1]) / 1.414, (u - Vt[1]) / 1.414, (-u + Vt[1]) / 1.414, (-u - Vt[1]) / 1.414) if solid else (u, -u)
    for v in vs:                                            # pores and lines from nearby skin (a ring's: along the same finger only)
        for r in (1.25, 1.6):
            d = (v * max(ext, 40) * r).round().astype(int); sh = np.roll(np.roll(I, -d[1], 0), -d[0], 1)
            g = (np.roll(np.roll(cv2.morphologyEx(gold, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)), -d[1], 0), -d[0], 1) & fill).sum()
            e = ((cv2.GaussianBlur(sh, (0, 0), 4) - cv2.GaussianBlur(I, (0, 0), 4)) ** 2).sum(2)[ring].mean()
            if solid: e += 1e6 * max(0.0, g / fill.sum() - 0.002)                                 # bare skin first (not the wire, not the other stone)
            if best is None or e < best[0]: best = (e, d, sh)
    _, D, src = best; hf = src - cv2.GaussianBlur(src, (0, 0), 2.5)
    edge = ((cv2.dilate(fill, np.ones((21, 21), np.uint8)) - fill) > 0) & ((hue < 63) | (C < 18))
    em = edge.astype(np.float32); low = low + cv2.GaussianBlur((I - low) * em[..., None], (0, 0), 10) / np.maximum(cv2.GaussianBlur(em, (0, 0), 10), 1e-3)[..., None]
    fm = cv2.GaussianBlur(fill.astype(np.float32), (0, 0), 2.0)[..., None]
    skin = I * (1 - fm) + (low + hf) * fm
    # how much darker the skin seen through openwork was than the fill (its own shade), kept for the smaller piece; solid pieces 0.85
    if solid: shade = 0.85
    else:
        open_ = sil.astype(bool) & ~cv2.dilate(piece, np.ones((3, 3), np.uint8)).astype(bool)
        shade = float(np.clip(np.median(I[open_].mean(1)) / np.median(low[open_].mean(1)), 0.6, 1.0))
    # 2. the piece alone, soft-edged, at F times its size about the anchor, over a soft shadow
    a = cv2.GaussianBlur((piece if not solid else cv2.erode(piece, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7) if poly else (5, 5)))).astype(np.float32),
                         (0, 0), 0.6 if not solid else 0.7)                                  # a traced outline has a margin: only the box moves
    M = np.float32([[F, 0, ax * (1 - F)], [0, F, ay * (1 - F)]]); wh = I.shape[1::-1]
    fs = cv2.warpAffine(I, M, wh, flags=cv2.INTER_AREA); as_ = np.clip(cv2.warpAffine(a, M, wh, flags=cv2.INTER_LINEAR), 0, 1)[..., None]
    Ms = M.copy(); Ms[:, 2] += (3, 4)
    shd = cv2.GaussianBlur(cv2.warpAffine(sil.astype(np.float32), Ms, wh), (0, 0), 3.5)[..., None] * (1 - shade)
    out = skin * (1 - shd); out = out * (1 - as_) + fs * as_
    if solid:   # no halo: round the smaller piece the skin's low-frequency colour is taken from the skin just beyond it
        st_ = cv2.dilate((as_[..., 0] > 0.1).astype(np.uint8), np.ones((5, 5), np.uint8))
        ann = cv2.dilate(st_, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41))) - st_
        outer = ((cv2.dilate(st_, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (71, 71))) - st_ - ann) > 0) & ((hue < 63) | (C < 18)) & (keep == 0)
        om = outer.astype(np.float32); tgt = cv2.GaussianBlur(out * om[..., None], (0, 0), 12) / np.maximum(cv2.GaussianBlur(om, (0, 0), 12), 1e-3)[..., None]
        wa = cv2.GaussianBlur(ann.astype(np.float32), (0, 0), 4)[..., None] * (1 - as_) * (1 - keep[..., None])
        out = out + (tgt - cv2.GaussianBlur(out, (0, 0), 6)) * wa
    print("  part in %s: %d px, anchor (%.0f, %.0f), %.0f px long, texture from (%d, %d), shade %.2f, x%.2f" % (box, piece.sum(), ax, ay, ext, D[0], D[1], shade, F))
    return out

if __name__ == "__main__":
    k, o = sys.argv[1], sys.argv[2]; I = np.asarray(Image.open(os.path.join(H, "out", k + ".png")).convert("RGB")).astype(np.float32)
    print(k, "->", o)
    for p in sys.argv[3:]:
        bits = p.split(":"); F = float(bits[0]); box = tuple(map(int, bits[1].split(",")))
        anchor = tuple(map(float, bits[2].split(","))) if len(bits) > 2 and bits[2][:1].isdigit() else None
        get = lambda k: next((list(map(int, b[len(k) + 1:].split(","))) for b in bits[2:] if b.startswith(k + "=")), None)
        I = shrink(I, F, box, anchor, solid="solid" in bits[2:], poly=get("poly"), keep_poly=get("keep"))
    Image.fromarray(np.clip(I, 0, 255).round().astype(np.uint8)).save(os.path.join(H, "out", o + ".png"))
