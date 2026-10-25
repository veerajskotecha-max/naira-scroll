# 25 Oct size fix for the Bougainvillea Vine Bracelet: the owner found the flowers about 30% bigger in the photos than
# on the piece. Measured against Aditya's photos (flower span over the joints, the small flowers and the vine spacing)
# the centre flower drew about 1.3x too big everywhere and the small flowers about 1.2x too big on the wrist; on the
# plinth the small flowers already match. Shrinking by edit does not work with the model (it redraws the piece), so this
# warps the approved takes without credits: an as-rigid-as-possible (moving least squares, similarity) warp where each
# flower scales about its own centre, the joints and leaves next to it slide inward with it so the vine stays joined,
# and everything else (the other flowers, the clasp, the plinth edges, the hand) is pinned in place. Only the bare
# stems and the plain plaster or skin around the flower stretch to fill the gap. Writes out/<key>.png.
# Usage: retouch.py [KEY ...]
import sys, os, numpy as np, cv2
H = os.path.dirname(os.path.abspath(__file__)); O = f"{H}/out"

def ring(c, r, n, a0=0.0):
    return [(c[0] + r * np.cos(a0 + 2 * np.pi * k / n), c[1] + r * np.sin(a0 + 2 * np.pi * k / n)) for k in range(n)]

def controls(spec):
    """spec items: ("scale", c, R, s[, Ry]) a flower; ("pts", c, s, [points]) more points of that flower;
    ("move", c, r, dx, dy, s) a joint or leaf that slides and scales by s; ("pin", [points]) points held in place."""
    src, dst = [], []
    for it in spec:
        if it[0] == "scale":
            _, c, R, s = it[:4]; ry = it[4] if len(it) > 4 else R
            pts = [c] + [(c[0] + (x - c[0]), c[1] + (y - c[1]) * ry / R) for f in (0.4, 0.75, 1.0) for x, y in ring(c, R * f, 12)]
            src += pts; dst += [(c[0] + s * (x - c[0]), c[1] + s * (y - c[1])) for x, y in pts]
        elif it[0] == "pts":  # extra points that scale with a flower, e.g. its tip prongs and just beyond them
            _, c, s, pts = it
            src += list(pts); dst += [(c[0] + s * (x - c[0]), c[1] + s * (y - c[1])) for x, y in pts]
        elif it[0] == "move":
            _, c, r, dx, dy, s = it
            pts = [c] + ring(c, r, 6)
            src += pts; dst += [(c[0] + dx + s * (x - c[0]), c[1] + dy + s * (y - c[1])) for x, y in pts]
        else:
            src += list(it[1]); dst += list(it[1])
    return np.array(src, np.float64), np.array(dst, np.float64)

def mls(shape, src, dst, box, alpha=1.0, fade=60):
    """Inverse similarity MLS: for each output pixel, where to sample the source. dst points receive src content."""
    h, w = shape[:2]; x0, y0, x1, y1 = box
    gy, gx = np.mgrid[y0:y1, x0:x1].astype(np.float64); v = gx + 1j * gy
    q = dst[:, 0] + 1j * dst[:, 1]; p = src[:, 0] + 1j * src[:, 1]
    Sw = np.zeros_like(gx); Sq = np.zeros_like(v); Sp = np.zeros_like(v); Sqp = np.zeros_like(v); Sqq = np.zeros_like(gx)
    for qi, pi in zip(q, p):
        wi = 1.0 / (np.abs(v - qi) ** (2 * alpha) + 1e-6)
        Sw += wi; Sq += wi * qi; Sp += wi * pi; Sqp += wi * np.conj(qi) * pi; Sqq += wi * abs(qi) ** 2
    qs, ps = Sq / Sw, Sp / Sw
    a = (Sqp - Sw * np.conj(qs) * ps) / (Sqq - Sw * np.abs(qs) ** 2 + 1e-9)
    sv = a * (v - qs) + ps; d = sv - v
    # fade the displacement to zero at the box edge, so the warp is exactly the identity outside the box
    fx = np.clip(np.minimum(gx - x0, x1 - 1 - gx) / fade, 0, 1); fy = np.clip(np.minimum(gy - y0, y1 - 1 - gy) / fade, 0, 1)
    f = fx * fy; f = f * f * (3 - 2 * f); d *= f
    mx = np.tile(np.arange(w, dtype=np.float32), (h, 1)); my = np.tile(np.arange(h, dtype=np.float32)[:, None], (1, w))
    mx[y0:y1, x0:x1] += d.real.astype(np.float32); my[y0:y1, x0:x1] += d.imag.astype(np.float32)
    return mx, my

def warp(img, spec, box, alpha=1.0):
    src, dst = controls(spec)
    mx, my = mls(img.shape, src, dst, box, alpha)
    return cv2.remap(img, mx, my, cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)

# plinth heroes: the centre flower scales to 0.76, its joints slide in 43px and shrink a little, the leaf pairs slide in 18px
def tips(c, pts, out=20):
    """each prong and a point out beyond it along the ray from the flower centre"""
    res = []
    for x, y in pts:
        d = np.hypot(x - c[0], y - c[1]); res += [(x, y), (x + (x - c[0]) * out / d, y + (y - c[1]) * out / d)]
    return res

PLINTH = [("scale", (923, 1175), 193, 0.76, 178),
          ("pts", (923, 1175), 0.76, tips((923, 1175), [(825, 1012), (1020, 1012), (830, 1335), (1015, 1335)])),
          ("move", (702, 1170), 30, 43, 0, 0.88), ("move", (1145, 1175), 32, -43, 0, 0.88),
          ("move", (502, 1130), 40, 18, 0, 1.0), ("move", (580, 1215), 45, 18, 0, 1.0),
          ("move", (1290, 1150), 45, -18, 0, 1.0), ("move", (1367, 1212), 42, -18, 0, 1.0),
          ("pin", [(312, 1100)] + ring((312, 1100), 85, 8) + [(1531, 1112)] + ring((1531, 1112), 85, 8)),
          ("pin", [(760, 860), (850, 845), (925, 845), (1000, 845), (1090, 860), (640, 900), (1210, 905)]),
          ("pin", [(923, 905), (650, 960), (1200, 975), (600, 1400), (800, 1470), (923, 1480), (1050, 1470), (1250, 1420)]),
          ("pin", [(400, 1404), (550, 1447), (700, 1489)])]
# Fuchsia wrist, across the forearm: against the arm width (about 420px here) every flower drew about 1.35x too big.
# The centre flower and the lower small flower scale to 0.74; the joints shrink to 0.85 and follow the centre flower in;
# the upper small flower sits on the arm's silhouette, foreshortened: it and its leaf shrink to 0.9 and slide in a little.
W1F = [("scale", (1022, 1481), 63, 0.74),
       ("pts", (1022, 1481), 0.74, tips((1022, 1481), [(1045, 1424), (1078, 1470), (964, 1490), (999, 1537)], 12)),
       ("move", (982, 1428), 13, 9, 12.6, 0.85), ("move", (1068, 1540), 15, -9.6, -12.3, 0.85),
       ("move", (962, 1420), 18, 7, 10, 0.9), ("move", (965, 1385), 30, 4, 6, 0.9),
       ("move", (1111, 1578), 18, 0, 0, 0.85), ("move", (1107, 1620), 18, 0, 0, 0.85),
       ("scale", (1180, 1670), 45, 0.74),
       ("pin", [(1115, 1423), (928, 1539), (1182, 1555), (1038, 1645), (1257, 1622), (1103, 1718), (1240, 1572), (1140, 1735),
                (1035, 1310), (900, 1468), (930, 1330), (1150, 1360), (900, 1600), (1000, 1760), (1280, 1700)])]
# Fuchsia wrist from above: against the wrist (about 480px between the small flowers) the flowers drew about 1.3x too big,
# the centre flower scales to 0.77 and its joints follow it in; the two small flowers sit on the wrist's edges and scale
# to 0.82, with their leaf pairs sliding toward them, so the extra length goes into the bare stems by the joints.
W2F = [("scale", (818, 1524), 68, 0.77),
       ("pts", (818, 1524), 0.77, tips((818, 1524), [(832, 1459), (881, 1503), (756, 1537), (804, 1587)], 12)),
       ("move", (742, 1463), 13, 10, 10, 0.85), ("move", (884, 1587), 12, -11, -11, 0.85),
       ("move", (687, 1409), 22, -5, -2, 0.9), ("move", (695, 1457), 22, -5, -2, 0.9),
       ("move", (922, 1638), 22, 0.5, 5, 0.9), ("move", (913, 1690), 24, 0.5, 5, 0.9),
       ("scale", (615, 1405), 44, 0.82), ("scale", (930, 1767), 46, 0.82),
       ("pin", [(901, 1452), (735, 1596), (750, 1378), (630, 1482), (978, 1608), (858, 1712), (683, 1346), (547, 1464),
                (998, 1708), (862, 1826), (556, 1337), (880, 1840), (1010, 1500), (620, 1640), (800, 1360)])]
# Violet wrist: about 470px between the small flowers; the centre flower scales to 0.75, the small ones to 0.82
W3F = [("scale", (1086, 1382), 70, 0.75, 77),
       ("pts", (1086, 1382), 0.75, tips((1086, 1382), [(1089, 1307), (1154, 1349), (1149, 1423), (1087, 1457), (1021, 1426), (1026, 1344)], 12)),
       ("move", (1018, 1334), 12, 15, 9.5, 0.85), ("move", (1160, 1432), 13, -16, -10, 0.85),
       ("move", (970, 1287), 20, -5.5, -4.3, 0.9), ("move", (972, 1326), 20, -5.5, -4.3, 0.9),
       ("move", (1212, 1458), 20, 6, 3.7, 0.9), ("move", (1221, 1505), 20, 6, 3.7, 0.9),
       ("scale", (918, 1265), 40, 0.82), ("scale", (1303, 1535), 43, 0.82),
       ("pin", [(1146, 1296), (1026, 1468), (1014, 1244), (928, 1368), (964, 1199), (872, 1331), (856, 1222), (1259, 1420),
                (1173, 1543), (1349, 1469), (1257, 1601), (1310, 1602), (1000, 1420), (1180, 1330), (1370, 1580)])]
# macros: no wrist or loop to read size from, so the flower comes in only as far as Aditya's close-up allows: it spans
# about 4.9 joints there against 5.7 here, so 0.84; the joints follow it in, the leaf pairs go about 40% as far
M8 = [("scale", (915, 1148), 375, 0.84, 350),
      ("pts", (915, 1148), 0.84, tips((915, 1148), [(733, 803), (1133, 820), (713, 1470), (1100, 1500)], 30)),
      ("move", (483, 1129), 62, 59, 0, 0.92), ("move", (1367, 1179), 75, -61, 0, 0.92),
      ("move", (133, 1029), 78, 25, 0, 1.0), ("move", (262, 1217), 88, 25, 0, 1.0),
      ("move", (1688, 1142), 98, -25, 0, 1.0), ("move", (1800, 1300), 60, -25, 0, 1.0),
      ("pin", [(100, 700), (400, 720), (700, 700), (1000, 700), (1300, 700), (1600, 720), (1800, 700), (300, 850), (1550, 880),
               (200, 1680), (600, 1790), (1000, 1890), (1400, 1990), (700, 1650), (1150, 1650), (400, 1450), (1500, 1450)])]
M9 = [("scale", (925, 1133), 441, 0.84, 400),
      ("pts", (925, 1133), 0.84, tips((925, 1133), [(700, 733), (1151, 740), (700, 1522), (1151, 1529)], 30)),
      ("move", (406, 1139), 78, 71, 0, 0.92), ("move", (1455, 1155), 82, -71, 0, 0.92),
      ("move", (122, 1267), 98, 30, 0, 1.0), ("move", (40, 1000), 45, 30, 0, 1.0), ("move", (1760, 1105), 98, -30, 0, 1.0),
      ("pin", [(100, 640), (400, 640), (925, 600), (1400, 640), (1700, 640), (250, 850), (1600, 850),
               (200, 1800), (600, 1888), (1000, 1976), (1400, 2064), (700, 1700), (1150, 1700), (300, 1500), (1600, 1500)])]
FIX = {"A8_Hs": ("A8_H", [(PLINTH, (380, 885, 1470, 1500))]),
       "A9_Hs": ("A9_H2", [(PLINTH, (380, 885, 1470, 1500))]),
       "A8_W1s": ("A8_W1", [(W1F, (880, 1300, 1300, 1780))]),
       "A8_W2s": ("A8_W2", [(W2F, (520, 1300, 1040, 1880))]),
       "A9_W1s": ("A9_W1", [(W3F, (840, 1180, 1390, 1630))]),
       "A8_Ms": ("A8_M", [(M8, (0, 640, 1856, 2000))]), "A9_Ms": ("A9_M", [(M9, (0, 560, 1856, 2100))])}  # the Violet hero is an edit of the Fuchsia one, same geometry

if __name__ == "__main__":
    keys = sys.argv[1:] or list(FIX)
    for k in keys:
        src, passes = FIX[k]; img = cv2.imread(f"{O}/{src}.png")
        for spec, box in passes: img = warp(img, spec, box)
        cv2.imwrite(f"{O}/{k}.png", img); print(k, "from", src)
