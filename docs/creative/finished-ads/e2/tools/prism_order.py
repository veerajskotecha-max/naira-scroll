# Recolours generated Prism Rivière stones into the bracelet's strict three-colour repeat, one stone at a time.
# Usage: prism_order.py SRC.png OUT.png SPEC.json  where SPEC = {"stones": [[x, y], ...] in chain order, "cur": "APAY...",
# "tgt": "AYPA...", "par": {"i": [half, hue_gate, min_sat]}, "warm_y": 4, "pink_s": 0.9}. A stone's mask is a square aligned
# with the chain (from its neighbours), gated to the source stone's hue, so halos and the cloth under them keep their colour.
import cv2, json, sys, numpy as np
src, dst, spec = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3]))
a = cv2.imread(src); hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV).astype(np.float32)
C = {i + 1: tuple(p) for i, p in enumerate(spec["stones"])}; CUR, TGT = spec["cur"], spec["tgt"]
PAR = {int(k): v for k, v in spec.get("par", {}).items()}
yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
def sq(i, hs):
    cx, cy = C[i]; p = C.get(i - 1, C[i]); n = C.get(i + 1, C[i]); vx, vy = n[0] - p[0], n[1] - p[1]; L = (vx * vx + vy * vy) ** .5 or 1
    ux, uy = vx / L, vy / L; dx, dy = xx - cx, yy - cy; u = dx * ux + dy * uy; v = -dx * uy + dy * ux
    return (np.abs(u) < hs) & (np.abs(v) < hs)
def hmean(h):
    ang = h / 180 * 2 * np.pi; return (np.arctan2(np.sin(ang).mean(), np.cos(ang).mean()) % (2 * np.pi)) / (2 * np.pi) * 180
st = {}
for i in C:
    m = sq(i, spec.get("probe", 30)) & (hsv[..., 1] > 40); st[i] = (hmean(hsv[..., 0][m]), np.median(hsv[..., 1][m]), np.median(hsv[..., 2][m]))
ref = {c: np.array([st[i] for i in C if CUR[i - 1] == c and TGT[i - 1] == c and i not in spec.get("skip_ref", [])]).mean(0) for c in "APY"}
ref["Y"][0] = (ref["Y"][0] + spec.get("warm_y", 0)) % 180; ref["P"][1] *= spec.get("pink_s", 1.0)
out = hsv.copy()
for i in C:
    s, t = CUR[i - 1], TGT[i - 1]
    if s == t: continue
    hsz, hg, smin = PAR.get(i, spec.get("default", [44, 30, 10]))
    hs, ss, vs = st[i]; ht, stt, vt = ref[t]
    dh = ((hsv[..., 0] - hs + 90) % 180) - 90
    m = (sq(i, hsz) & (np.abs(dh) < hg)).astype(np.float32)
    w = cv2.GaussianBlur(np.clip((hsv[..., 1] - smin) / 22, 0, 1) * m, (0, 0), 1.0)
    Hn = (ht + dh * 0.6) % 180; Sn = np.clip(hsv[..., 1] * stt / max(ss, 1), 0, 255); Vn = np.clip(hsv[..., 2] * vt / max(vs, 1), 0, 255)
    out[..., 0] = np.where(w > 0.05, Hn, out[..., 0]); out[..., 1] = out[..., 1] * (1 - w) + Sn * w; out[..., 2] = out[..., 2] * (1 - w) + Vn * w
res = cv2.cvtColor(out.astype(np.uint8), cv2.COLOR_HSV2BGR)
for i, (x0, y0, x1, y1) in spec.get("restore", {}).items():          # put the original cloth back where a stone's mask spilled
    res[y0:y1, x0:x1] = a[y0:y1, x0:x1]
cv2.imwrite(dst, res); print("recoloured", sum(1 for i in C if CUR[i - 1] != TGT[i - 1]), "stones")
