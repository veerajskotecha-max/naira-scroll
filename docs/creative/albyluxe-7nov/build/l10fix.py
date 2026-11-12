# Interlocked Baguette Stack Ring (L10): the 12 Nov worn frame W1x is right (four stripes, the silver band's green baguettes, the wide band's
# spaced rounds), but where the stack turns round the side of the finger, four stones at the end of the square channel, the last baguettes
# and the centre of the last round stone come out WHITE, so they read as clear accent stones (the lock says none). Here those white pixels,
# inside the channel ends only (the silver rails and the gold are outside the boxes), take the green of the same channel's own stones,
# their brightness squeezed into the range of those stones so the facets still show. The glints on the baguettes further in are kept.
# W2y (the close back-of-hand frame) is right but for one stray dark green bar standing across the wide band like an extra baguette: it is
# covered with the band's own gold from just beside it (the band's shading runs along it, so a short shift matches).
# Usage: python3 -I l10fix.py -> out/L10_W1xf.png and out/L10_W2yf.png (then tone.py L10 and recolour.py work from them)
import os
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
BOX = {"squares": (976, 1108, 1017, 1120), "baguettes": (984, 1135, 1019, 1151), "round": (999, 1175, 1009, 1191)}   # x0, y0, x1, y1:
# the stone rows only (the rails' highlights sit just outside); the last round stone is an ellipse inside its box (the gold's glint is beside it)
img = np.asarray(Image.open(os.path.join(H, "out", "L10_W1x.png")).convert("RGB")); f = img.astype(np.float32) / 255
lab = cv2.cvtColor(f, cv2.COLOR_RGB2Lab); C = np.hypot(lab[..., 1], lab[..., 2]); hue = (np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) + 360) % 360
out = lab.copy()
for name, (x0, y0, x1, y1) in BOX.items():
    # the channel's own green stones: the same rows, a little further in
    gy = slice(y0, y1); gx = slice(x0 - 60, x0 + 10); g = (hue[gy, gx] > 110) & (hue[gy, gx] < 200) & (C[gy, gx] > 8)
    La, A, B = lab[gy, gx][..., 0][g], lab[gy, gx][..., 1][g], lab[gy, gx][..., 2][g]
    Lm, Lhi = np.median(La), np.percentile(La, 90)
    w = np.zeros(C.shape, np.float32); s = (slice(y0, y1), slice(x0, x1))
    w[s] = np.clip((lab[s][..., 0] - 50) / 10, 0, 1) * np.clip((14 - C[s]) / 6, 0, 1)
    if name == "round":
        yy, xx = np.mgrid[:C.shape[0], :C.shape[1]]; w *= (((xx - (x0 + x1) / 2) / ((x1 - x0) / 2)) ** 2 + ((yy - (y0 + y1) / 2) / ((y1 - y0) / 2)) ** 2) <= 1
    w = cv2.GaussianBlur(w, (0, 0), 0.6); w[:y0] = 0; w[y1:] = 0; w[:, :x0] = 0; w[:, x1:] = 0
    Lw = np.median(lab[..., 0][w > 0.5]) if (w > 0.5).any() else 80.0
    Ln = np.clip(Lm + 6 + (lab[..., 0] - Lw) * 0.8, Lm - 10, Lhi + 5)   # each white stone keeps its own shading, at the green's brightness
    for c, v in ((0, Ln), (1, np.median(A)), (2, np.median(B))): out[..., c] = out[..., c] * (1 - w) + v * w
    print(name, "white px", int((w > 0.5).sum()), "-> green L %.0f-%.0f a %.1f b %.1f" % (Lm, Lhi, np.median(A), np.median(B)))
rgb = np.clip(cv2.cvtColor(out, cv2.COLOR_Lab2RGB), 0, 1)
Image.fromarray((rgb * 255 + 0.5).astype(np.uint8)).save(os.path.join(H, "out", "L10_W1xf.png"))

# W2y: the stray bar on the wide band, x 1006-1023, y 1099-1141, covered from 16 px to its left (plain band surface), feathered
img = np.asarray(Image.open(os.path.join(H, "out", "L10_W2y.png")).convert("RGB")).astype(np.float32)
x0, x1, y0, y1, dx = 1006, 1023, 1099, 1141, -16
m = np.zeros(img.shape[:2], np.float32); m[y0:y1, x0:x1] = 1; m = cv2.GaussianBlur(m, (0, 0), 1.2)[..., None]
src = np.roll(img, -dx, 1); out = img * (1 - m) + src * m
Image.fromarray(np.clip(out, 0, 255).round().astype(np.uint8)).save(os.path.join(H, "out", "L10_W2yf.png")); print("W2y bar covered")
