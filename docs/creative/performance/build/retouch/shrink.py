# Shrinks a piece the model drew too large, in place, on a plain plaster ground: lifts the gold out by colour, rebuilds the
# plaster under it and its old shadows (smooth light from inpainting, pore texture from a clean patch of the same frame, scaled
# to the local light), carries its shadows as a brightness map and pastes piece and shadows back at scale s about their centre.
# Usage: shrink.py <raw-in> <raw-out> <s> <x0> <y0> <x1> <y1> <dx> <dy> <ground: light|red> <shadow-reach-x> <shadow-reach-y>
#   box = the piece and its shadows with a margin; (dx, dy) = offset to a clean patch of the same plaster, for texture;
#   shadow reach = how far the shadows run from the metal, in px, toward the lower right (the light comes from the upper left)
import sys, cv2, numpy as np
src, dst, s = sys.argv[1], sys.argv[2], float(sys.argv[3]); x0, y0, x1, y1, dx, dy = map(int, sys.argv[4:10]); ground = sys.argv[10]
sx, sy = int(sys.argv[11]), int(sys.argv[12])
D = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/perf/colour"
I = cv2.imread(f"{D}/raw/{src}.png").astype(np.float32); A = I[y0:y1, x0:x1].copy(); h, w = A.shape[:2]
hsv = cv2.cvtColor(A.astype(np.uint8), cv2.COLOR_BGR2HSV).astype(int); H, S, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]
if ground == "light":                                             # pale plaster: gold is the only saturated thing
    G = (S > 70) & (H >= 8) & (H <= 32)
    other = (S < 45) & (V > 236)                                  # bright ivory things (cloth, paper) that must not be touched
else:                                                              # red plaster: gold is the only yellow-orange thing
    G = (H >= 7) & (H <= 32) & (V > 70) & (S > 60)
    other = (A[..., 2] - A[..., 1] < 14) & (V < 80)               # neutral black things (silk, lacquer); shadows on red stay red
def comps(m, keep):                                               # the connected parts of a mask that pass keep(stats)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m.astype(np.uint8)); return np.isin(lab, [i for i in range(1, n) if keep(st[i])]).astype(np.uint8)
inside = lambda t: t[0] > 2 and t[1] > 2 and t[0] + t[2] < w - 2 and t[1] + t[3] < h - 2
disk = lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))
blur = lambda m, sg: cv2.GaussianBlur(m.astype(np.float32), (0, 0), sg)
lum = lambda Z: Z @ np.array([0.114, 0.587, 0.299], np.float32)
other = cv2.dilate(comps(other, lambda t: t[4] > 30000), np.ones((9, 9), np.uint8))   # only the big cloth or fan, never a highlight
G = comps(cv2.morphologyEx(G.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8)), lambda t: t[4] > 3000 and inside(t))
G = cv2.morphologyEx(G, cv2.MORPH_CLOSE, disk(8)); G[other > 0] = 0  # highlights, crevices and the opening go with the metal
# the area to rebuild: the metal and the whole of its shadow, smeared toward the lower right
Gd = cv2.dilate(G, disk(45)); O = np.zeros_like(G)
for t in np.linspace(0, 1, 9):
    O |= cv2.warpAffine(Gd, np.float32([[1, 0, t * sx], [0, 1, t * sy]]), (w, h))
O = ((O > 0) & (cv2.dilate(other, disk(25)) == 0)) | (cv2.dilate(G, disk(6)) > 0); O = O.astype(np.uint8)
O[:24], O[-24:], O[:, :24], O[:, -24:] = 0, 0, 0, 0               # fade out before the box edge, never a seam
# smooth light under it: inpaint at quarter size (the other object left out), then blur
q = 4; small = cv2.resize(A, (w // q, h // q), interpolation=cv2.INTER_AREA)
msk = cv2.resize(np.maximum(O, other), (w // q, h // q), interpolation=cv2.INTER_NEAREST)
Ls = cv2.inpaint(np.clip(small, 0, 255).astype(np.uint8), msk, 12, cv2.INPAINT_TELEA).astype(np.float32)
L = blur(cv2.resize(blur(Ls, 2.5), (w, h), interpolation=cv2.INTER_CUBIC), 6)
P = I[y0 + dy:y1 + dy, x0 + dx:x1 + dx]; T = P / np.maximum(blur(P, 8), 1)   # pore texture as a ripple around 1
Of = blur(O, 7)[..., None]
plate = A * (1 - Of) + L * T * Of                                  # the plaster with the piece and its shadows gone
# shadows as a brightness map, pores closed out first so they are not carried; crisp right at the metal
Ac = cv2.morphologyEx(lum(A), cv2.MORPH_CLOSE, disk(5))
Rb = np.minimum(1, blur(Ac, 2.5) / np.maximum(lum(L), 4) + 0.02)[..., None]
R0 = A / np.maximum(L, 4)
Gm = blur(cv2.dilate(G, np.ones((7, 7), np.uint8)), 1.5)[..., None]
R = np.clip(R0 * Gm + Rb * (1 - Gm), 0.05, 1.0); R = 1 - (1 - R) * Of
Gf = blur(G, 0.9)[..., None]
ys, xs = np.nonzero(G); cx, cy = xs.mean(), ys.mean()             # scale about the piece's centre
nw, nh = int(round(w * s)), int(round(h * s)); ox, oy = int(round(cx * (1 - s))), int(round(cy * (1 - s)))
rs = lambda m: cv2.resize(m, (nw, nh), interpolation=cv2.INTER_AREA)
Rs, Gs, As = rs(R), rs(Gf[..., 0])[..., None], rs(A)
out = plate.copy(); reg = out[oy:oy + nh, ox:ox + nw] * Rs; out[oy:oy + nh, ox:ox + nw] = reg * (1 - Gs) + As * Gs
J = I.copy(); J[y0:y1, x0:x1] = out
cv2.imwrite(f"{D}/raw/{dst}.png", np.clip(J, 0, 255).astype(np.uint8))
viz = A.copy(); viz[G > 0] = (0, 0, 255); viz[(O > 0) & (G == 0)] = viz[(O > 0) & (G == 0)] * 0.6 + np.array([255, 0, 0]) * 0.4
cv2.imwrite(f"{D}/view/{dst}_mask.jpg", cv2.resize(viz, (w // 2, h // 2)).astype(np.uint8))
pair = np.concatenate([I[y0:y1, x0:x1], np.full((h, 10, 3), 255, np.float32), J[y0:y1, x0:x1]], 1)
cv2.imwrite(f"{D}/view/{dst}_ba.jpg", pair.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 90])
print(dst, "gold px", int(G.sum()), "centre", round(cx + x0), round(cy + y0), "scale", s)
