# 25 Oct sizing fix: brings the worn photos that read too big down to the listed size, without asking the model again
# (plain shrink edits came back unchanged and blended composites redrew the piece large). Writes out/<key>.png.
#  pinch: liquify-style, the ellipse around the piece scales by s about its centre and eases back to 1 by K x the ellipse,
#         so a chain stays joined to the piece; used where the chain is attached at the sides or a bail.
#  squeeze: a bracelet band narrows across its width, along the arm (unit vector a), about its own centreline (a cubic
#         through the points, read off a GrabCut mask); the skin either side eases back by K x the half-width and the warp
#         fades out past the band's ends, so the band keeps its length round the wrist and the arm's outline does not move.
#  cut:   the piece is cut out (GrabCut), the area is clone-stamped with plain skin or hair from a donor offset and the
#         piece is pasted back scaled about its top (the bail or the piercing); used for drops that hang from one point.
# J02 and J11 came from Higgsfield instead: J02_W1c blended the cut composite, J11_W1qp pinches the on-rim take J11_W1q.
# Usage: retouch.py [KEY ...]
import sys, os, numpy as np, cv2
H = os.path.dirname(os.path.abspath(__file__)); O = f"{H}/out"
PINCH = {  # key: (source take, centre, half-axes, scale, K)
 "J01_W1p": ("J01_W1", (950, 1305), (62, 108), 0.60, 2.4), "J03_W1p": ("J03_W1", (971, 1485), (56, 54), 0.65, 2.6),
 "J05_W1p": ("J05_W1e2", (866, 1493), (66, 40), 0.65, 2.6), "J07_W1p": ("J07_W1", (939, 1495), (78, 104), 0.60, 2.4),
 "J08_W1p": ("J08_W1", (972, 1387), (72, 72), 0.70, 2.6), "J11_W1qp": ("J11_W1q", (682, 422), (84, 82), 0.70, 1.7),
 # 26 Oct, Aditya's photo of the Lumière ring lying on a palm (IMG_6847): the oval is about 8 x 6 mm, about 10 x 6.5 here.
 "J15_W1p": ("J15_W1", (920, 1177), (58, 58), 0.82, 2.4),
 # 27 Oct, Solitaire Drop Huggies: the worn stone drew about 0.56 of the hoop's height; the supplier photo and the hero say 0.37.
 "J19_W1p": ("J19_W1", (1025, 615), (30, 30), 0.66, 2.4), "J19_W2p": ("J19_W2", (1175, 650), (36, 36), 0.66, 2.4),
 # 27 Oct, Lotus Pear Drop Studs: the worn earring drew about 24 mm (W1) and 28 mm (W2) against a 58 mm ear; the card says 17 mm.
 "J20_W1p": ("J20_W1", (684, 553), (62, 102), 0.72, 3.0), "J20_W2p": ("J20_W2", (972, 515), (66, 120), 0.63, 3.0)}
SQUEEZE = {  # key: (source take, centreline points, span (the band's two ends), arm axis, half-width, scale, K)
 # 27 Oct, Watch Link Strap Bracelet: the worn band drew about 12.5 to 13 mm across a 55 mm wrist (about 108 and 103 px
 # across 490 and 443 px); the supplier card says about 9 mm.
 "J21_W1s": ("J21_W1", [(1254, 1468), (1197, 1485), (1155, 1522), (1120, 1558), (1090, 1593), (1063, 1625), (1039, 1660),
                        (1018, 1700), (1001, 1745), (998, 1770)], [(1292, 1416), (968, 1792)], (0.759, 0.651), 62, 0.72, 2.3),
 "J21_W2s": ("J21_W2", [(590, 1350), (632, 1320), (662, 1323), (694, 1332), (725, 1346), (754, 1365), (786, 1379), (815, 1399),
                        (842, 1422), (873, 1442), (904, 1466), (929, 1492), (949, 1514), (964, 1535)], [(568, 1365), (985, 1600)],
             (-0.556, 0.831), 60, 0.70, 2.3)}
CUT = {  # key: (source take, piece box, fill box, donor offset, anchor, scale)
 "J16_W1d": ("J16_W1r2", (955, 1372, 1002, 1555), (944, 1376, 1016, 1572), (120, 0), (977, 1373), 0.58),
 "J17_W1d": ("J17_W1h2", (760, 462, 805, 688), (754, 472, 812, 700), (-45, 0), (783, 468), 0.72)}
# swap: the stud in the worn take drew both hearts as pave; the packshot's own stud (one heart-cut stone per heart, the
# same way round) is cut out, scaled to the worn stud's size and set in its place on a clean lobe.
SWAP = {  # key: (worn take, packshot take, packshot stud box, worn fill box, donor offset, worn stud centre, scale)
 "J06_W1s": ("J06_W1e2", "J06_He", (980, 1035, 1370, 1290), (1086, 468, 1160, 522), (76, 0), (1122, 496), 0.165)}

def pinch(img, c, a, s, K):
    h, w = img.shape[:2]; cx, cy = c; ax, ay = a
    rin = np.linspace(0, K * 1.5, 6000); u = np.clip((rin - 1) / (K - 1), 0, 1); u = u * u * (3 - 2 * u)
    rout = np.where(rin <= 1, s, s + (1 - s) * u) * rin
    gy, gx = np.mgrid[0:h, 0:w].astype(np.float32); dx, dy = gx - cx, gy - cy
    ro = np.sqrt((dx / ax) ** 2 + (dy / ay) ** 2)
    ri = np.where(ro >= K, ro, np.interp(ro, rout, rin)).astype(np.float32)
    f = np.where(ro > 1e-6, ri / np.maximum(ro, 1e-6), 1 / s).astype(np.float32)
    return cv2.remap(img, cx + dx * f, cy + dy * f, cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)

def squeeze(img, pts, span, a, hw, s, K, fade=60):
    h, w = img.shape[:2]; a = np.float32(a) / np.linalg.norm(a); b = np.float32([-a[1], a[0]])
    P = np.float32(pts); o = P.mean(0); tp, up = (P - o) @ b, (P - o) @ a
    cu = np.polyfit(tp, up, min(3, len(P) - 1)); ts = (np.float32(span) - o) @ b; t0, t1 = ts.min(), ts.max()
    gy, gx = np.mgrid[0:h, 0:w].astype(np.float32); X, Y = gx - o[0], gy - o[1]
    t, u = X * b[0] + Y * b[1], X * a[0] + Y * a[1]
    d = u - np.polyval(cu, np.clip(t, tp.min(), tp.max())).astype(np.float32)
    rin = np.linspace(0, K * 1.5, 6000); e = np.clip((rin - 1) / (K - 1), 0, 1); e = e * e * (3 - 2 * e)
    rout = np.where(rin <= 1, s, s + (1 - s) * e) * rin
    r = np.abs(d) / hw; ri = np.where(r >= K, r, np.interp(r, rout, rin))
    z = np.clip(np.maximum(t0 - t, t - t1) / fade, 0, 1); sh = (np.sign(d) * ri * hw - d) * (1 - z * z * (3 - 2 * z))
    return cv2.remap(img, (gx + sh * a[0]).astype(np.float32), (gy + sh * a[1]).astype(np.float32), cv2.INTER_LANCZOS4,
                     borderMode=cv2.BORDER_REFLECT)

def grab(img, box):
    h, w = img.shape[:2]; x0, y0, x1, y1 = box; pad = 40
    X0, Y0, X1, Y1 = max(0, x0 - pad), max(0, y0 - pad), min(w, x1 + pad), min(h, y1 + pad)
    m = np.zeros((Y1 - Y0, X1 - X0), np.uint8)
    cv2.grabCut(img[Y0:Y1, X0:X1].copy(), m, (x0 - X0, y0 - Y0, x1 - x0, y1 - y0), np.zeros((1, 65)), np.zeros((1, 65)), 6, cv2.GC_INIT_WITH_RECT)
    pm = np.where((m == 1) | (m == 3), 255, 0).astype(np.uint8)
    pm = cv2.morphologyEx(cv2.morphologyEx(pm, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    piece = np.zeros((h, w), np.uint8); piece[Y0:Y1, X0:X1] = pm
    return piece

def cut(img, box, fillbox, donor, anchor, s, src=None, at=None):
    # src/at: paste the piece cut from another image (src, its box) with its box centre landing on "at" in img
    h, w = img.shape[:2]; f32 = img.astype(np.float32)
    piece = grab(src if src is not None else img, box)
    fx0, fy0, fx1, fy1 = fillbox; fill = np.zeros((h, w), np.uint8); fill[fy0:fy1, fx0:fx1] = 255
    d = cv2.warpAffine(f32, np.float32([[1, 0, -donor[0]], [0, 1, -donor[1]]]), (w, h), borderMode=cv2.BORDER_REFLECT)
    rim = cv2.dilate(fill, np.ones((21, 21), np.uint8)) & ~fill
    ys, xs = np.nonzero(rim); diff = f32[ys, xs] - d[ys, xs]   # match colour and shading to the rim with a fitted plane
    coef, *_ = np.linalg.lstsq(np.c_[xs, ys, np.ones_like(xs)].astype(np.float32), diff, rcond=None)
    gy, gx = np.mgrid[0:h, 0:w]; d += (gx[..., None] * coef[0] + gy[..., None] * coef[1] + coef[2]).astype(np.float32)
    soft = cv2.GaussianBlur(fill, (0, 0), 6).astype(np.float32)[..., None] / 255
    base = f32 * (1 - soft) + d * soft
    ax, ay = anchor; M = np.float32([[s, 0, ax - s * ax], [0, s, ay - s * ay]])
    if src is not None:  # scale about the source box centre, then move that centre to "at"
        cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
        M = np.float32([[s, 0, at[0] - s * cx], [0, s, at[1] - s * cy]])
    srcf = (src if src is not None else img).astype(np.float32)
    a = cv2.warpAffine(cv2.GaussianBlur(piece, (3, 3), 0).astype(np.float32) / 255, M, (w, h))
    sh = cv2.GaussianBlur(cv2.warpAffine(a, np.float32([[1, 0, 1.5], [0, 1, 2.5]]), (w, h)), (0, 0), 2.5) * 0.3 if src is not None else \
         cv2.GaussianBlur(cv2.warpAffine(a, np.float32([[1, 0, 3], [0, 1, 6]]), (w, h)), (0, 0), 5) * 0.28
    base = base * (1 - sh[..., None]); wp = cv2.warpAffine(srcf, M, (w, h), flags=cv2.INTER_AREA)
    return (base * (1 - a[..., None]) + wp * a[..., None]).clip(0, 255).astype(np.uint8)

if __name__ == "__main__":
    keys = sys.argv[1:] or list(PINCH) + list(SQUEEZE) + list(CUT) + list(SWAP)
    for k in keys:
        if k in PINCH: src, *args = PINCH[k]; res = pinch(cv2.imread(f"{O}/{src}.png"), *args)
        elif k in SQUEEZE: src, *args = SQUEEZE[k]; res = squeeze(cv2.imread(f"{O}/{src}.png"), *args)
        elif k in CUT: src, *args = CUT[k]; res = cut(cv2.imread(f"{O}/{src}.png"), *args)
        else:
            src, donor_take, box, fillbox, don, at, s = SWAP[k]
            res = cut(cv2.imread(f"{O}/{src}.png"), box, fillbox, don, at, s, src=cv2.imread(f"{O}/{donor_take}.png"), at=at)
        cv2.imwrite(f"{O}/{k}.png", res); print(k, "from", src)
