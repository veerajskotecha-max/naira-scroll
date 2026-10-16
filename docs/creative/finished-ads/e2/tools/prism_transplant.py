# Puts the Prism Rivière stones into the bracelet's strict three-colour repeat by transplanting real stones of the wanted colour
# from elsewhere on the same chain (rotated and scaled to the target's place), so facets and light stay photographic.
# Usage: prism_transplant.py SRC.png OUT.png SPEC.json   SPEC: {"stones": [[x,y],...] in chain order, "cur": "...", "tgt": "...",
# "half": 38, "feather": 3}. Halos, claws and the ground are untouched outside each stone's square.
import cv2, json, sys, numpy as np
src, dst, S = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3]))
a = cv2.imread(src); out = a.copy(); P = [tuple(p) for p in S["stones"]]; n = len(P); cur, tgt = S["cur"], S["tgt"]
half, fe = S.get("half", 38), S.get("feather", 3)
def frame(i):
    p, q = P[max(i - 1, 0)], P[min(i + 1, n - 1)]; v = np.array(q, float) - np.array(p, float)
    return np.degrees(np.arctan2(v[1], v[0])), np.linalg.norm(v) / (2 if 0 < i < n - 1 else 1)
yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
for i in range(n):
    if cur[i] == tgt[i]: continue
    donors = [j for j in range(n) if cur[j] == tgt[i] and tgt[j] == cur[j]]
    j = min(donors, key=lambda d: abs(d - i))
    ai, si = frame(i); aj, sj = frame(j)
    M = cv2.getRotationMatrix2D(P[j], S.get("rot", 1.0) * (ai - aj), si / sj * S.get("grow", 1.06))   # rotate/scale about the donor ...
    M[:, 2] += np.array(P[i], float) - np.array(P[j], float)       # ... then move it onto the target stone
    warped = cv2.warpAffine(a, M, (a.shape[1], a.shape[0]), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)
    th = np.radians(ai); dx, dy = xx - P[i][0], yy - P[i][1]
    u = dx * np.cos(th) + dy * np.sin(th); v = -dx * np.sin(th) + dy * np.cos(th)
    d = np.maximum(np.abs(u), np.abs(v))
    hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV).astype(np.float32)
    core = (np.abs(u) < half * 0.8) & (np.abs(v) < half * 0.8)
    ring = ((xx - P[i][0]) ** 2 + (yy - P[i][1]) ** 2 < (half * 1.4) ** 2)
    hs = np.median(hsv[..., 0][core & (hsv[..., 1] > 40)])
    dh = np.abs(((hsv[..., 0] - hs + 90) % 180) - 90)
    old = ring & (((hsv[..., 1] > S.get("min_sat", 24)) & (dh < 35)) | core)          # the old stone's own pixels, so no fringe survives
    old = cv2.morphologyEx(old.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    old = cv2.dilate(old, np.ones((5, 5), np.uint8)).astype(np.float32)
    m = cv2.GaussianBlur(old, (0, 0), fe * 0.7)[..., None]
    out = (out * (1 - m) + warped * m).astype(np.uint8)
    print(f"stone {i+1}: {cur[i]}->{tgt[i]} from stone {j+1}")
cv2.imwrite(dst, out)
