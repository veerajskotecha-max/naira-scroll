"""Story ground for ad 9: the photo's own paper, extended up and down, with the edge pea removed. Colour comes from a smooth
fit of the surrounding paper; grain comes from a real patch of the same paper (high-pass, mirror-tiled)."""
import numpy as np, cv2
from PIL import Image
IMG = '/tmp/claude-0/-home-user-naira-scroll/3afe135e-ba9d-5fe5-a4de-8088e2e02a7f/scratchpad/ten/img/'
src = np.array(Image.open(IMG + 'n10.png').convert('RGB')).astype(np.float32)
H, W = src.shape[:2]


def grain(img, sigma):
    return img - cv2.GaussianBlur(img, (0, 0), sigma)


def tile(t, h, w):
    t2 = np.concatenate([t, t[:, ::-1]], 1); t2 = np.concatenate([t2, t2[::-1]], 0)
    reps = (h // t2.shape[0] + 1, w // t2.shape[1] + 1, 1)
    return np.tile(t2, reps)[:h, :w]


paper = src[60:560, 40:900]                           # empty pink, top-left (soft focus)
near = src[2030:2296, 260:1060]                       # empty pink, bottom-left (sharp focus)
g_src = grain(near, 6)
x0, x1, y0, y1 = 1080, 1720, 2010, 2304
ring = np.zeros((H, W), bool); ring[y0 - 60:y1, x0 - 60:x1 + 60] = True; ring[y0:y1, x0:x1] = False
ys, xs = np.where(ring)
A = np.stack([np.ones_like(xs), xs, ys, xs * ys, xs ** 2, ys ** 2], 1).astype(np.float64)
gy, gx = np.mgrid[y0:y1, x0:x1]
G = np.stack([np.ones_like(gx), gx, gy, gx * gy, gx ** 2, gy ** 2], -1).astype(np.float64)
fit = np.zeros((y1 - y0, x1 - x0, 3), np.float32)
for c in range(3):
    coef, *_ = np.linalg.lstsq(A, cv2.GaussianBlur(src, (0, 0), 6)[ys, xs, c].astype(np.float64), rcond=None)
    fit[..., c] = (G @ coef).astype(np.float32)
fit += tile(g_src, y1 - y0, x1 - x0)
patch = src.copy(); patch[y0:y1, x0:x1] = fit
m = np.zeros((H, W), np.float32); m[y0 + 20:y1, x0 + 20:x1 - 20] = 1
m = cv2.GaussianBlur(m, (0, 0), 16)[..., None]
clean = np.clip(src * (1 - m) + patch * m, 0, 255)

sc = 1080 / W; ph = round(H * sc)
small = cv2.resize(clean, (1080, ph), interpolation=cv2.INTER_AREA).astype(np.float32)
g_small = grain(cv2.resize(paper, (round(paper.shape[1] * sc), round(paper.shape[0] * sc)), interpolation=cv2.INTER_AREA), 4)
g_near = grain(cv2.resize(near, (round(near.shape[1] * sc), round(near.shape[0] * sc)), interpolation=cv2.INTER_AREA), 4)
canvas = np.zeros((1920, 1080, 3), np.float32); top = 300
canvas[top:top + ph] = small
smooth = cv2.GaussianBlur(small, (0, 0), 4)
tr = cv2.GaussianBlur(smooth[:16].mean(0)[None], (0, 0), sigmaX=24, sigmaY=.1)[0]
br = cv2.GaussianBlur(smooth[-16:].mean(0)[None], (0, 0), sigmaX=24, sigmaY=.1)[0]
gt = tile(g_small, 1920, 1080)
tb = tile(g_near, 2400, 1600)
hh, ww = g_near.shape[:2]
gb = (tb[:1920, :1080] + tb[hh // 2 + 37:hh // 2 + 37 + 1920, ww // 2 + 53:ww // 2 + 53 + 1080]) / np.sqrt(2)
canvas[:top] = tr[None] + gt[:top]
canvas[top + ph:] = br[None] + gb[top + ph:]
for k in range(36):
    a = k / 35
    canvas[top + k] = canvas[top + k] * a + (tr + gt[top + k]) * (1 - a)
    y = top + ph - 36 + k
    canvas[y] = canvas[y] * (1 - a) + (br + gb[y]) * a
Image.fromarray(np.clip(canvas, 0, 255).astype(np.uint8)).save(IMG + 'a9_story.jpg', quality=93)
Image.fromarray(np.clip(canvas[1350:1920], 0, 255).astype(np.uint8)).save(IMG + 'rev_a9bottom.jpg', quality=88)
Image.fromarray(np.clip(canvas[0:520], 0, 255).astype(np.uint8)).save(IMG + 'rev_a9top.jpg', quality=88)
print('ok')
