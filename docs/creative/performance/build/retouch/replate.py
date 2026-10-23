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
NOCREAM = "nocream" in a
NOTOUCH = "notouch" in a
#   optional: fill a = fill enclosed holes in the piece's mask smaller than a px (clear stones), never the opening of a loop
FILL = int(a[a.index("fill") + 1]) if "fill" in a else 0
#   optional: anchor ax ay = scale about this point (raw px), e.g. where a standing ring touches the ground, so it stays grounded
ANCHOR = tuple(map(float, a[a.index("anchor") + 1:a.index("anchor") + 3])) if "anchor" in a else None
#   optional: seedbox x0 y0 x1 y1 = look for the piece's seeds only inside this box (raw px), when a prop shares its colour
SEEDBOX = tuple(map(int, a[a.index("seedbox") + 1:a.index("seedbox") + 5])) if "seedbox" in a else None
#   optional: cut x1 y1 x2 y2 ... ; = a polygon (raw px, ended by ';') that is never the piece nor
#   replaced, e.g. a deep contact shadow or a prop beside it
CUT = None
if "cut" in a:
    i0 = a.index("cut") + 1; i1 = a.index(";", i0); v = list(map(int, a[i0:i1])); CUT = np.int32(list(zip(v[0::2], v[1::2])))
#   optional: solid = an opaque piece (plain metal, no clear stones): its pale smooth highlights are metal, never light through it
SOLID = "solid" in a
#   optional: seeddiff = keep only seeds the plate lacks, when a gold prop (a clutch frame) sits by the piece
SEEDDIFF = "seeddiff" in a
#   optional: cluster r = seeds within 2r px of each other count as one piece (default 40), for a piece whose pale parts leave gaps
CLUSTER = int(a[a.index("cluster") + 1]) if "cluster" in a else 40
#   optional: zone x1 y1 x2 y2 ... ; = a polygon (raw px) also replaced by the plate, e.g. the far tail of a long old shadow
XZONE = None
if "zone" in a:
    j0 = a.index("zone") + 1; j1 = a.index(";", j0); vz = list(map(int, a[j0:j1])); XZONE = np.int32(list(zip(vz[0::2], vz[1::2])))
#   optional: band r = whatever lies within r px of the piece's gold walls is the piece: soft, out-of-focus
#   clear stones in box settings, which would otherwise read as light through the stones
BAND = int(a[a.index("band") + 1]) if "band" in a else 0
#   optional: grabcut = refine the piece's outline by colour and edges (GrabCut), seeded by its strong metal as surely the piece and
#   by the plaster the plate matches as surely not: for pale metal whose highlights and warm shadows colour thresholds confuse
GRABCUT = "grabcut" in a
#   optional: shadowcut <rm> <dev> = never the piece where the frame is darker than the plate by more than rm (a ratio) and evenly
#   so (colour ratio spread under dev): a deep shadow on a dark ground, which the metal never is
SHCUT = tuple(map(float, a[a.index("shadowcut") + 1:a.index("shadowcut") + 3])) if "shadowcut" in a else None

#   optional: softshadow r = smooth the measured shadow over r px (median, then blur), where the plate redrew the plaster's pores
#   under the old shadow, so the measured shadow is speckled with them
SOFT = int(a[a.index("softshadow") + 1]) if "softshadow" in a else 0                                                 # with hand: keep evenly darkened ground out of the piece
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
if SEEDBOX: sb = np.zeros_like(seed); sb[SEEDBOX[1]:SEEDBOX[3], SEEDBOX[0]:SEEDBOX[2]] = 1; seed = seed * sb
if CUT is not None: cmask = np.zeros_like(seed); cv2.fillPoly(cmask, [CUT], 1); seed[cmask > 0] = 0
if HAND:                                                                   # the outline drawn by hand is the authority on where the piece is
    e = HAND; band = np.zeros_like(seed)
    cv2.ellipse(band, ((e[0], e[1]), (e[2], e[3]), e[4]), 1, -1); cv2.ellipse(band, ((e[5], e[6]), (e[7], e[8]), e[9]), 0, -1)
    seed = (band > 0) & (((hsv[..., 1] < 60) & (hsv[..., 2] > 110)) | (seed > 0)); seed = seed.astype(np.uint8)
    RZ = cv2.dilate(band, disk(30))
else:
    n, lab, st, _ = cv2.connectedComponentsWithStats(cv2.dilate(seed, disk(CLUSTER)))
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
if HAND or SEEDDIFF: seed = (seed & (blur(d, 1.2) > 40)).astype(np.uint8)   # a neutral ground looks like silver: keep only what the plate lacks
hsvP = cv2.cvtColor(np.clip(Pt, 0, 255).astype(np.uint8), cv2.COLOR_BGR2HSV)
cream = lambda X: (X[..., 1] > 40) & (X[..., 2] > 170) & (X[..., 0] >= 10) & (X[..., 0] <= 40) & (not NOCREAM)   # petal or paper, never the piece
                                                                           # (nocream: off for gold, whose highlights are cream too)
Vf = hsv[..., 2].astype(np.float32); sd = np.sqrt(np.maximum(blur(Vf * Vf, 2.0) - blur(Vf, 2.0) ** 2, 0))
lit = (lum(A) > lum(Pt) + 15) & (sd < 22) & (seed == 0) & (hsv[..., 1] < 60)  # light through the piece onto the ground, never saturated metal or stone
piece_like = ((sd > 16) | (lum(A) < lum(Pt) - 25) | (seed > 0)) & ~lit      # busy as pave, darker (stones), or its own colour
if BAND:
    inband = cv2.dilate(seed, disk(BAND)) > 0
    lit = lit & ~inband; piece_like = piece_like | inband
if SOLID:                                                                  # opaque metal: its own saturated colour or brighter than the plate, never a shadow
    lit = np.zeros_like(lit); Hh, Ss = hsv[..., 0], hsv[..., 1]
    piece_like = (seed > 0) | (lum(A) > lum(Pt) + 8) | ((Ss > 75) & (Hh >= hlo) & (Hh <= hhi))
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
if GRABCUT:
    Au = np.clip(A, 0, 255).astype(np.uint8); db = blur(d, 1.2); Sv, Vv = hsv[..., 1].astype(int), hsv[..., 2].astype(int)
    zone = cv2.dilate(seed, disk(reach)) > 0
    gm = np.full((h, w), cv2.GC_BGD, np.uint8); gm[zone] = cv2.GC_PR_BGD
    gm[zone & (db > 60) & ~((lum(A) < lum(Pt)) & (Sv < 90))] = cv2.GC_PR_FGD           # differs from the plate and is not a pale shadow
    gm[zone & (db < 30) & (cv2.dilate(seed, disk(4)) == 0)] = cv2.GC_BGD                 # the plaster exactly as the plate has it
    dev = np.abs(rr - rm[..., None]).max(-1)                                            # how unevenly it differs from the plaster
    strong = ((seed > 0) & (((dev > 0.11) & (rm > 0.5)) | (lum(A) > lum(Pt) + 5))).astype(np.uint8)   # metal, never its warm shadow
    gm[zone & (rm < 0.8) & (dev < 0.1) & (lum(A) < lum(Pt) - 20) & (cv2.dilate(strong, disk(5)) == 0)] = cv2.GC_BGD    # its shadow:
                                                                                         # the plaster evenly darkened, warm bounce allowed
    gm[cv2.erode(strong, disk(3)) > 0] = cv2.GC_FGD                                     # strong metal
    gm[zone & (Vv > 246) & (db > 60) & (cv2.dilate(strong, disk(30)) > 0)] = cv2.GC_FGD  # its brightest highlights
    ys0, xs0 = np.nonzero(zone); r0 = (xs0.min(), ys0.min(), xs0.max() - xs0.min() + 1, ys0.max() - ys0.min() + 1)
    sub = (slice(r0[1], r0[1] + r0[3]), slice(r0[0], r0[0] + r0[2])); g2 = gm[sub].copy()
    bg_, fg_ = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(Au[sub], g2, None, bg_, fg_, 6, cv2.GC_INIT_WITH_MASK)
    G = np.zeros_like(G); G[sub] = ((g2 == cv2.GC_FGD) | (g2 == cv2.GC_PR_FGD)).astype(np.uint8)
n, lab, st, _ = cv2.connectedComponentsWithStats(cv2.morphologyEx(G, cv2.MORPH_CLOSE, disk(6)))
keep = [i for i in range(1, n) if (seed[lab == i] > 0).any()]               # only parts that hold the piece's own stones or metal
G = cv2.morphologyEx(np.isin(lab, keep).astype(np.uint8), cv2.MORPH_CLOSE, disk(6))
if CLOSE: G = cv2.morphologyEx(G, cv2.MORPH_CLOSE, disk(CLOSE))           # dark inner walls that mirror the ground go with the metal
if SHCUT:                                                                  # never within a few px of its metal or its lit stones
    dv_ = np.abs(rr - rm[..., None]).max(-1); keep_ = cv2.dilate(((seed > 0) | (lum(A) > lum(Pt) + 10)).astype(np.uint8), disk(6)) > 0
    G[(rm < SHCUT[0]) & (dv_ < SHCUT[1]) & ~keep_] = 0
    G = G & cv2.dilate(cv2.erode(G, disk(6)), disk(12))                        # no thin rims of half-lit shadow away from the body
    n5, lab5, st5, _ = cv2.connectedComponentsWithStats(G); G = np.isin(lab5, [i for i in range(1, n5) if (seed[lab5 == i] > 0).any() and st5[i][4] > 400]).astype(np.uint8)
if FILL:                                                                   # clear stones show the ground through them: fill their small holes
    n4, lab4, st4, _ = cv2.connectedComponentsWithStats((G == 0).astype(np.uint8))
    G = (G | np.isin(lab4, [i for i in range(1, n4) if st4[i][4] < FILL and st4[i][0] > 0 and st4[i][1] > 0 and st4[i][0] + st4[i][2] < w and st4[i][1] + st4[i][3] < h])).astype(np.uint8)
if CUT is not None: G[cmask > 0] = 0

hull = np.zeros_like(G); cv2.fillPoly(hull, [cv2.convexHull(np.argwhere(G > 0)[:, ::-1].astype(np.int32))], 1)
Gd = cv2.dilate(G | hull, disk(14)); Z = np.zeros_like(G)                   # the whole outline, the ring's opening included
for t in np.linspace(0, 1, 9): Z |= cv2.warpAffine(Gd, np.float32([[1, 0, t * sx], [0, 1, t * sy]]), (w, h))
Z &= cv2.dilate(RZ, disk(40 + max(sx, sy))) if HAND else cv2.dilate(RZ, disk(40))   # the shadow may run past the outline
# plus everything the old piece darkened or lit around it, wherever it lies (its shadow, its bounced light)
touched = ((blur(dl, 4) < 0.975) | (blur(dl, 4) > 1.03)).astype(np.uint8)
n3, lab3, st3, _ = cv2.connectedComponentsWithStats(touched)
near = cv2.dilate(Gd, disk(10)) > 0
if not NOTOUCH:                                                            # (notouch: when a prop sits close, rely on the shadow reach alone)
    Z |= cv2.dilate(np.isin(lab3, [i for i in range(1, n3) if (near & (lab3 == i)).any()]).astype(np.uint8), disk(16)) & cv2.dilate(Z, disk(90))
if XZONE is not None: xz = np.zeros_like(Z); cv2.fillPoly(xz, [XZONE], 1); Z |= xz
if CUT is not None: Z[cv2.dilate(cmask, disk(12)) > 0] = 0                 # the prop stays exactly as shot
Zf = blur(cv2.dilate(Z, disk(10)), 8)[..., None]
k = np.clip((0.975 - blur(dl, 2.0)) / 0.05, 0, 1)                         # real shadow only, not noise between the two renders
same = cream(hsv) == cream(hsvP)                                           # shadow only where both show the same surface
R = np.where((Z > 0) & same & (G == 0), 1 - (1 - np.minimum(1, blur(dl, 2.0))) * k, 1)
if SOFT:                                                                   # (the piece itself left out of the smoothing, so no halo)
    out_ = (G == 0).astype(np.float32); Re = cv2.medianBlur((np.clip(np.where(G > 0, 1.0, R), 0, 1) * 255).astype(np.uint8), 2 * SOFT + 1).astype(np.float32) / 255
    R = np.where(G > 0, R, np.minimum(1, blur(Re * out_, SOFT) / np.maximum(blur(out_, SOFT), 1e-3)))
R = np.minimum(R, np.where(G > 0, 1, R))[..., None]
Gf = blur(G, 0.9)[..., None]
# inside the footprint, the plate's broad tone follows the original plaster around it (the model paints the gap a shade off)
Zm = (Zf[..., 0] > 0.02).astype(np.uint8); q = 4
lowA = cv2.resize(blur(A, 10), (w // q, h // q), interpolation=cv2.INTER_AREA)
tgt = np.stack([cv2.inpaint(np.clip(lowA[..., c], 0, 255).astype(np.uint8), cv2.resize(cv2.dilate(Zm, disk(8)), (w // q, h // q), interpolation=cv2.INTER_NEAREST), 8, cv2.INPAINT_TELEA) for c in range(3)], -1).astype(np.float32)
tgt = blur(cv2.resize(tgt, (w, h), interpolation=cv2.INTER_CUBIC), 6)
gl = blur(np.clip(lum(tgt) / np.maximum(lum(blur(Pt, 25)), 4), 0.9, 1.1), 30)   # brightness only, broad and gentle: never a colour shift
Pm = Pt * gl[..., None]
base = A * (1 - Zf) + Pm * Zf                                              # the original, with the plate only where the piece was
# 3. back at scale s, centred on (ncx, ncy)
ys, xs = np.nonzero(G); cx, cy = xs.mean(), ys.mean()
if ncx < 0: ncx, ncy = cx, cy                                             # a negative centre keeps the piece where it is
M = np.float32([[s, 0, ncx - s * cx], [0, s, ncy - s * cy]])
if ANCHOR: M = np.float32([[s, 0, ANCHOR[0] * (1 - s)], [0, s, ANCHOR[1] * (1 - s)]])   # or scale about the point it stands on
pre = lambda m: blur(m, 0.45 / s) if s < 0.8 else m
warp = lambda m, b: cv2.warpAffine(m, M, (w, h), flags=cv2.INTER_LINEAR, borderValue=b)
Gs = warp(pre(Gf[..., 0]), 0)[..., None]; As = warp(pre(A * Gf), 0)              # premultiplied: no ground leaks into its edge
if SYNTH:                                                                  # the piece's own outline casts its shadow, light from the upper left
    Ws = (xs.max() - xs.min()) * s; g0 = Gs[..., 0]
    sh = lambda m, fx, fy: cv2.warpAffine(m, np.float32([[1, 0, fx * Ws], [0, 1, fy * Ws]]), (w, h))
    Rs = ((1 - CAST * blur(sh(g0, 0.07, 0.06), 0.04 * Ws)) * (1 - CONTACT * blur(sh(g0, 0.012, 0.014), 0.012 * Ws)))[..., None]
else:
    Rs = warp(pre(R[..., 0]), 1.0)[..., None]
out = base * Rs; out = out * (1 - Gs) + As
cv2.imwrite(f"{D}/raw/{dst}.png", np.clip(out, 0, 255).astype(np.uint8))
cv2.imwrite(f"{D}/raw/{dst}_G.png", (G * 255).astype(np.uint8)); cv2.imwrite(f"{D}/raw/{dst}_Z.png", (Z * 255).astype(np.uint8))
ys2, xs2 = np.nonzero(Z); bx0, by0, bx1, by1 = max(0, xs2.min() - 60), max(0, ys2.min() - 60), min(w, xs2.max() + 60), min(h, ys2.max() + 60)
viz = A.copy(); viz[G > 0] = (0, 0, 255); viz[(Z > 0) & (G == 0)] = viz[(Z > 0) & (G == 0)] * 0.6 + np.array([255, 0, 0]) * 0.4
pair = np.concatenate([viz[by0:by1, bx0:bx1], np.full((by1 - by0, 10, 3), 255, np.float32), out[by0:by1, bx0:bx1]], 1)
cv2.imwrite(f"{D}/view/{dst}_ba.jpg", cv2.resize(pair, (pair.shape[1] // 2, (by1 - by0) // 2)).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 90])
print(dst, "shift", round(tx, 1), round(ty, 1), "resp", round(resp, 3), "piece px", int(G.sum()), "centre", round(cx), round(cy), "->", ncx, ncy, "scale", s)
