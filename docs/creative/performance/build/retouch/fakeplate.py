# Makes a free clean plate from the frame itself, for replate.py, where the piece lies on plain plaster: inside a drawn region (the
# piece and its whole shadow, clear of any prop) the plaster is rebuilt as smooth light (inpainted at low resolution from the plaster
# around the region) times pore texture (a clean rectangle of the same plaster, mirrored and tiled, as a ripple around 1).
# Usage: fakeplate.py <raw-in> <raw-out> <tx0> <ty0> <tx1> <ty1> x1 y1 x2 y2 ...   (t* = the clean texture rectangle, raw px)
import sys, cv2, numpy as np
D = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/perf/colour"
src, dst = sys.argv[1], sys.argv[2]; tx0, ty0, tx1, ty1 = map(int, sys.argv[3:7]); v = list(map(int, sys.argv[7:]))
poly = np.int32(list(zip(v[0::2], v[1::2])))
A = cv2.imread(f"{D}/raw/{src}.png").astype(np.float32); h, w = A.shape[:2]
blur = lambda m, s: cv2.GaussianBlur(m.astype(np.float32), (0, 0), s)
M = np.zeros((h, w), np.uint8); cv2.fillPoly(M, [poly], 1)
q = 6; small = cv2.resize(A, (w // q, h // q), interpolation=cv2.INTER_AREA)
ms = cv2.dilate(cv2.resize(M, (w // q, h // q), interpolation=cv2.INTER_NEAREST), np.ones((3, 3), np.uint8))
Ls = cv2.inpaint(np.clip(small, 0, 255).astype(np.uint8), ms, 15, cv2.INPAINT_TELEA).astype(np.float32)
L = blur(cv2.resize(blur(Ls, 3), (w, h), interpolation=cv2.INTER_CUBIC), 10)
C = A[ty0:ty1, tx0:tx1]; C = C / np.maximum(blur(C, 8), 1)                # pores as a ripple around 1
# the ripple laid as a mosaic of random patches of the clean rectangle, feathered into each other, so no pattern repeats
rng = np.random.default_rng(7); ps, st = 144, 96; ch, cw = C.shape[:2]
acc = np.zeros((h, w, 3), np.float32); wsum = np.zeros((h, w), np.float32)
win = np.outer(np.hanning(ps), np.hanning(ps)).astype(np.float32) + 1e-3
ys_, xs_ = np.nonzero(cv2.dilate(M, np.ones((41, 41), np.uint8)))
for y in range(max(0, ys_.min() - ps), min(h, ys_.max() + ps), st):
    for x in range(max(0, xs_.min() - ps), min(w, xs_.max() + ps), st):
        sy, sx = rng.integers(0, ch - ps), rng.integers(0, cw - ps); pt = C[sy:sy + ps, sx:sx + ps]
        if rng.random() < 0.5: pt = pt[:, ::-1]
        y1, x1 = min(h, y + ps), min(w, x + ps)
        acc[y:y1, x:x1] += pt[:y1 - y, :x1 - x] * win[:y1 - y, :x1 - x, None]; wsum[y:y1, x:x1] += win[:y1 - y, :x1 - x]
T = np.where(wsum[..., None] > 0, acc / np.maximum(wsum, 1e-6)[..., None], 1.0)
T = 1 + (T - 1) * 1.15                                                     # feathering softens the pores a little: restore them
Mf = blur(M, 6)[..., None]
P = A * (1 - Mf) + L * T * Mf
cv2.imwrite(f"{D}/raw/{dst}.png", np.clip(P, 0, 255).astype(np.uint8)); print(dst, "region px", int(M.sum()))
