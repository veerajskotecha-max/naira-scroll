# Recolours individual Prism stones by matching each pixel's rank in the source stone's value and saturation to the same rank in
# a real reference stone of the wanted colour, with the reference's hue, so facet light and dark stay but the colour is the real
# stone's (no olive yellows from dark aqua facets). Usage: prism_histmatch.py SRC OUT SPEC.json
# SPEC: {"stones": {"name": [x, y, r] or [x, y, rx, ry]}, "jobs": [["name", "ref_name"], ...], "gate": 30, "min_sat": 22}
import cv2, json, sys, numpy as np
src, dst, S = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3]))
a = cv2.imread(src); hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV).astype(np.float32); out = hsv.copy()
yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
def hmean(h):
    ang = h / 180 * 2 * np.pi; return (np.arctan2(np.sin(ang).mean(), np.cos(ang).mean()) % (2 * np.pi)) / (2 * np.pi) * 180
def mask(name):
    g = S["stones"][name]; x, y, rx = g[:3]; ry = g[3] if len(g) > 3 else rx      # [x, y, r] or an ellipse [x, y, rx, ry]
    e = ((xx - x) / rx) ** 2 + ((yy - y) / ry) ** 2; disk = e < 1; core = e < .25
    hs = hmean(hsv[..., 0][core & (hsv[..., 1] > 35)])
    dh = np.abs(((hsv[..., 0] - hs + 90) % 180) - 90)
    return disk & (dh < S.get("gate", 30)) & (hsv[..., 1] > S.get("min_sat", 22)), hs
for name, ref in S["jobs"]:
    m, hs = mask(name); mr, hr = mask(ref)
    for ch in (1, 2):
        sv = hsv[..., ch][m]; rv = np.sort(hsv[..., ch][mr])
        ranks = np.argsort(np.argsort(sv)) / max(len(sv) - 1, 1)
        out[..., ch][m] = rv[(ranks * (len(rv) - 1)).astype(int)]
    dh = ((hsv[..., 0][m] - hs + 90) % 180) - 90
    out[..., 0][m] = (hr + dh * 0.5) % 180
    w = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 1.2)
    for ch in (1, 2): out[..., ch] = hsv[..., ch] * (1 - w) + out[..., ch] * w
    hsv = out.copy(); print("recoloured", name, "like", ref, int(m.sum()), "px")
cv2.imwrite(dst, cv2.cvtColor(np.clip(out, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR))
