# Sets a piece back at true size using a clean plate (the same frame with the piece removed by the model): aligns the plate to the
# original and matches its tone, takes the piece and its shadow from the difference between them, and pastes them at scale s,
# centred on (ncx, ncy). The plate is used only inside the piece's old footprint, so the rest of the frame stays the original.
# Usage: replate.py <raw-orig> <raw-plate> <raw-out> <s> <ncx> <ncy> <sx> <sy> <seed-hue-lo> <seed-hue-hi> <seed-reach>
#   sx, sy = shadow reach toward the lower right; seed hue = OpenCV hue range of the piece's stones or metal (S > 100), which
#   marks the piece so that nothing else the plate redrew is taken for it; seed reach = how far the piece runs past its seeds (px)
import sys, cv2, numpy as np
#   optional: synth <cast> <contact> = a shadow drawn from the piece's own outline instead of the measured one (use it when the
#   plate redrew nearby shadows, so the measured difference is not the piece's alone), e.g. synth 0.22 0.30
a = sys.argv; src, pl, dst, s = a[1], a[2], a[3], float(a[4]); ncx, ncy, sx, sy, hlo, hhi, reach = map(int, a[5:12])
#   optional: ringfit <band-width> = take a ring's band as an ellipse through its stones, band-width in stone sizes (e.g. 1.6)
SYNTH = "synth" in a; CAST, CONTACT = (float(a[a.index("synth") + 1]), float(a[a.index("synth") + 2])) if SYNTH else (0, 0)
RINGFIT = "ringfit" in a; BANDW = float(a[a.index("ringfit") + 1]) if RINGFIT else 0
#   optional: hand cx cy w h ang icx icy iw ih iang = the ring's outline as an outer ellipse minus an inner one (cv2.ellipse terms)
HAND = [float(v) for v in a[a.index("hand") + 1:a.index("hand") + 11]] if "hand" in a else None
NOSHADOW = "noshadow" in a
#   optional: close r = also close the piece's mask by r px, for polished links whose inner walls mirror a dark ground
CLOSE = int(a[a.index("close") + 1]) if "close" in a else 0
NOCREAM = "nocream" in a                                                 # with hand: keep evenly darkened ground out of the piece
D = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/perf/colour"
A = cv2.imread(f"{D}/raw/{src}.png").astype(np.float32); P = cv2.imread(f"{D}/raw/{pl}.png").astype(np.float32)
if P.shape != A.shape: P = cv2.resize(P, (A.shape[1], A.shape[0]), interpolation=cv2.INTER_CUBIC)
h, w = A.shape[:2]
disk = lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))
blur = lambda m, sg: cv2.GaussianBlur(m.astype(np.float32), (0, 0), sg)
lum = lambda Z: Z @ np.array([0.114, 0.587, 0.299], np.float32)
def comps(m, keep):
    n, lab, st, _ = cv2.connectedComponentsWithStats(m.astype(np.uint8)); return np.isin(lab, [i for i in range(1, n) if keep(st[i])]).astype(np.uint8)
# 0. the piece's seeds: its stones or metal by colour, the biggest cluster
hsv = cv2.cvtColor(A.astype(np.uint8), cv2.COLOR_BGR2HSV)
seed = ((hsv[..., 0] >= hlo) & (hsv[..., 0] <= hhi) & (hsv[..., 1] > 100) & (hsv[..., 2] > 25)).astype(np.uint8)
seed = cv2.morphologyEx(seed, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
if HAND:                                                                   # the outline drawn by hand is the authority on where the piece is
    e = HAND; band = np.zeros_like(seed)
    cv2.ellipse(band, ((e[0], e[1]), (e[2], e[3]), e[4]), 1, -1); cv2.ellipse(band, ((e[5], e[6]), (e[7], e[8]), e[9]), 0, -1)
    seed = (band > 0) & (((hsv[..., 1] < 60) & (hsv[..., 2] > 110)) | (seed > 0)); seed = seed.astype(np.uint8)
    RZ = cv2.dilate(band, disk(30))
else:
    n, lab, st, _ = cv2.connectedComponentsWithStats(cv2.dilate(seed, disk(40)))
    seed = seed * (lab == 1 + int(np.argmax(st[1:, 4]))).astype(np.uint8)
    RZ = cv2.dilate(seed, disk(reach))                                     # where the piece can be
# 1. align: the integer shift that best matches the frame away from the piece, then tone-match
far = cv2.dilate(RZ, disk(220)) == 0
la, lp = lum(blur(A, 1.5))[::2, ::2], lum(blur(P, 1.5))[::2, ::2]; fm = far[::2, ::2]
best = None
for ty in range(-8, 9):
    for tx in range(-8, 9):
        sh = np.roll(np.roll(lp, ty, 0), tx, 1); e = np.abs(la - sh)[fm].mean()
        if best is None or e < best[0]: best = (e, tx, ty)
resp, tx, ty = best[0], 2 * best[1], 2 * best[2]
P = cv2.warpAffine(P, np.float32([[1, 0, tx], [0, 1, ty]]), (w, h), borderMode=cv2.BORDER_REFLECT)
diff0 = np.abs(A - P).sum(-1)
bad = cv2.dilate((blur(diff0, 3) > 45).astype(np.uint8), disk(40))
ratio = np.where(bad[..., None] > 0, np.nan, blur(A, 25) / np.maximum(blur(P, 25), 1))
q = 8; small = cv2.resize(np.nan_to_num(ratio, nan=1.0), (w // q, h // q), interpolation=cv2.INTER_AREA)
msk = cv2.resize(bad, (w // q, h // q), interpolation=cv2.INTER_NEAREST)
g = np.stack([cv2.inpaint(np.clip(small[..., c] * 100, 0, 255).astype(np.uint8), msk, 6, cv2.INPAINT_TELEA).astype(np.float32) / 100 for c in range(3)], -1)
Pt = P * blur(cv2.resize(g, (w, h), interpolation=cv2.INTER_CUBIC), 20)
# 2. the piece and its shadow from the difference
d = np.abs(A - Pt).sum(-1); dl = lum(A) / np.maximum(lum(Pt), 4)
if HAND: seed = (seed & (blur(d, 1.2) > 40)).astype(np.uint8)          # a neutral ground looks like silver: keep only what the plate lacks
hsvP = cv2.cvtColor(np.clip(Pt, 0, 255).astype(np.uint8), cv2.COLOR_BGR2HSV)
cream = lambda X: (X[..., 1] > 40) & (X[..., 2] > 170) & (X[..., 0] >= 10) & (X[..., 0] <= 40) & (not NOCREAM)   # petal or paper, never the piece
                                                                           # (nocream: off for gold, whose highlights are cream too)
Vf = hsv[..., 2].astype(np.float32); sd = np.sqrt(np.maximum(blur(Vf * Vf, 2.0) - blur(Vf, 2.0) ** 2, 0))
lit = (lum(A) > lum(Pt) + 15) & (sd < 22) & (seed == 0) & (hsv[..., 1] < 60)  # light through the piece onto the ground, never saturated metal or stone
piece_like = ((sd > 16) | (lum(A) < lum(Pt) - 25) | (seed > 0)) & ~lit      # busy as pave, darker (stones), or its own colour
rr = blur(A, 1.5) / np.maximum(blur(Pt, 1.5), 4); rm = rr.mean(-1)
shadowlike = (rm > 0.4) & (rm < 0.985) & (np.abs(rr - rm[..., None]).max(-1) < 0.035) & (sd < 16)   # evenly darkened, smooth: a shadow
if HAND:                                                                   # a ring's outline drawn by hand: outer ellipse minus its opening
    G = ((blur(d, 1.2) > 25) & (band > 0) & ~cream(hsv) & ~(shadowlike if NOSHADOW else False) & ~lit).astype(np.uint8) | (seed & band & ~lit)
elif RINGFIT:                                                              # a ring: its band follows an ellipse through the stones
    n2, lab2, st2, cen2 = cv2.connectedComponentsWithStats(seed)
    pts = np.float32([cen2[i] for i in range(1, n2) if st2[i][4] > 150]); size = np.median([max(st2[i][2], st2[i][3]) for i in range(1, n2) if st2[i][4] > 150])
    (ex, ey), (ea, eb), ang = cv2.fitEllipse(pts)
    band = np.zeros_like(seed); cv2.ellipse(band, ((ex, ey), (ea, eb), ang), 1, int(round(size * BANDW)))
    G = ((blur(d, 1.2) > 28) & (band > 0) & ~cream(hsv)).astype(np.uint8) | seed
else:
    G = ((blur(d, 1.2) > 60) & (RZ > 0) & ~cream(hsv) & piece_like & ~shadowlike).astype(np.uint8)
G = cv2.morphologyEx(G, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) | seed
n, lab, st, _ = cv2.connectedComponentsWithStats(cv2.morphologyEx(G, cv2.MORPH_CLOSE, disk(6)))
keep = [i for i in range(1, n) if (seed[lab == i] > 0).any()]               # only parts that hold the piece's own stones or metal
G = cv2.morphologyEx(np.isin(lab, keep).astype(np.uint8), cv2.MORPH_CLOSE, disk(6))
if CLOSE: G = cv2.morphologyEx(G, cv2.MORPH_CLOSE, disk(CLOSE))           # dark inner walls that mirror the ground go with the metal
hull = np.zeros_like(G); cv2.fillPoly(hull, [cv2.convexHull(np.argwhere(G > 0)[:, ::-1].astype(np.int32))], 1)
Gd = cv2.dilate(G | hull, disk(14)); Z = np.zeros_like(G)                   # the whole outline, the ring's opening included
for t in np.linspace(0, 1, 9): Z |= cv2.warpAffine(Gd, np.float32([[1, 0, t * sx], [0, 1, t * sy]]), (w, h))
Z &= cv2.dilate(RZ, disk(40))
# plus everything the old piece darkened or lit around it, wherever it lies (its shadow, its bounced light)
touched = ((blur(dl, 4) < 0.975) | (blur(dl, 4) > 1.03)).astype(np.uint8)
n3, lab3, st3, _ = cv2.connectedComponentsWithStats(touched)
near = cv2.dilate(Gd, disk(10)) > 0
Z |= cv2.dilate(np.isin(lab3, [i for i in range(1, n3) if (near & (lab3 == i)).any()]).astype(np.uint8), disk(16)) & cv2.dilate(Z, disk(90))
Zf = blur(cv2.dilate(Z, disk(10)), 8)[..., None]
k = np.clip((0.975 - blur(dl, 2.0)) / 0.05, 0, 1)                         # real shadow only, not noise between the two renders
same = cream(hsv) == cream(hsvP)                                           # shadow only where both show the same surface
R = np.where((Z > 0) & same & (G == 0), 1 - (1 - np.minimum(1, blur(dl, 2.0))) * k, 1)
R = np.minimum(R, np.where(G > 0, 1, R))[..., None]
Gf = blur(G, 0.9)[..., None]
# inside the footprint, the plate's broad tone follows the original plaster around it (the model paints the gap a shade off)
Zm = (Zf[..., 0] > 0.02).astype(np.uint8); q = 4
lowA = cv2.resize(blur(A, 10), (w // q, h // q), interpolation=cv2.INTER_AREA)
tgt = np.stack([cv2.inpaint(np.clip(lowA[..., c], 0, 255).astype(np.uint8), cv2.resize(cv2.dilate(Zm, disk(8)), (w // q, h // q), interpolation=cv2.INTER_NEAREST), 8, cv2.INPAINT_TELEA) for c in range(3)], -1).astype(np.float32)
tgt = blur(cv2.resize(tgt, (w, h), interpolation=cv2.INTER_CUBIC), 6)
Pm = Pt * np.clip(tgt / np.maximum(blur(Pt, 10), 4), 0.8, 1.25)
base = A * (1 - Zf) + Pm * Zf                                              # the original, with the plate only where the piece was
# 3. back at scale s, centred on (ncx, ncy)
ys, xs = np.nonzero(G); cx, cy = xs.mean(), ys.mean()
if ncx < 0: ncx, ncy = cx, cy                                             # a negative centre keeps the piece where it is
M = np.float32([[s, 0, ncx - s * cx], [0, s, ncy - s * cy]])
pre = lambda m: blur(m, 0.45 / s) if s < 0.8 else m
warp = lambda m, b: cv2.warpAffine(m, M, (w, h), flags=cv2.INTER_LINEAR, borderValue=b)
Gs = warp(pre(Gf[..., 0]), 0)[..., None]; As = warp(pre(A), 0)
if SYNTH:                                                                  # the piece's own outline casts its shadow, light from the upper left
    Ws = (xs.max() - xs.min()) * s; g0 = Gs[..., 0]
    sh = lambda m, fx, fy: cv2.warpAffine(m, np.float32([[1, 0, fx * Ws], [0, 1, fy * Ws]]), (w, h))
    Rs = ((1 - CAST * blur(sh(g0, 0.07, 0.06), 0.04 * Ws)) * (1 - CONTACT * blur(sh(g0, 0.012, 0.014), 0.012 * Ws)))[..., None]
else:
    Rs = warp(pre(R[..., 0]), 1.0)[..., None]
out = base * Rs; out = out * (1 - Gs) + As * Gs
cv2.imwrite(f"{D}/raw/{dst}.png", np.clip(out, 0, 255).astype(np.uint8))
ys2, xs2 = np.nonzero(Z); bx0, by0, bx1, by1 = max(0, xs2.min() - 60), max(0, ys2.min() - 60), min(w, xs2.max() + 60), min(h, ys2.max() + 60)
viz = A.copy(); viz[G > 0] = (0, 0, 255); viz[(Z > 0) & (G == 0)] = viz[(Z > 0) & (G == 0)] * 0.6 + np.array([255, 0, 0]) * 0.4
pair = np.concatenate([viz[by0:by1, bx0:bx1], np.full((by1 - by0, 10, 3), 255, np.float32), out[by0:by1, bx0:bx1]], 1)
cv2.imwrite(f"{D}/view/{dst}_ba.jpg", cv2.resize(pair, (pair.shape[1] // 2, (by1 - by0) // 2)).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 90])
print(dst, "shift", round(tx, 1), round(ty, 1), "resp", round(resp, 3), "piece px", int(G.sum()), "centre", round(cx), round(cy), "->", ncx, ncy, "scale", s)
