# Removes the stray second chain end at the left of C34 attempt 2 by inpainting the gold and its shadow off the canvas,
# then adds back canvas grain so the patch does not read smooth.
import sys
import numpy as np, cv2
src, out, prev = sys.argv[1:4]
im = cv2.imread(src)
x0, x1, y0, y1 = 150, 372, 1462, 1562
box = im[y0:y1, x0:x1].astype(np.float32)
b, g, r = box[..., 0], box[..., 1], box[..., 2]
lum = (r + g + b) / 3
canvas_lum = np.median(lum[:10, :60])
gold = (r > 70) & (g / np.maximum(r, 1) > 0.42) & ((r - b) > 45)            # warm metal, not the pale canvas
dark = (lum < canvas_lum - 45) & ~((g / np.maximum(r, 1) < 0.35) & (r > 60))  # its shadow, not the red glove
mask = np.zeros(im.shape[:2], np.uint8)
mask[y0:y1, x0:x1] = ((gold | dark) * 255).astype(np.uint8)
mask = cv2.dilate(mask, np.ones((7, 7), np.uint8))
glove = np.zeros(im.shape[:2], np.uint8)                                      # never inpaint over or next to the glove
glove[y0:y1, x0:x1] = (((g / np.maximum(r, 1) < 0.35) & (r > 60)) * 255).astype(np.uint8)
mask[cv2.dilate(glove, np.ones((9, 9), np.uint8)) > 0] = 0
fixed = cv2.inpaint(im, mask, 9, cv2.INPAINT_TELEA)
noise = cv2.GaussianBlur(np.random.default_rng(3).normal(0, 5, im.shape[:2]).astype(np.float32), (0, 0), 0.8)
m = cv2.GaussianBlur(mask.astype(np.float32) / 255, (0, 0), 2)[..., None]
fixed = np.clip(fixed.astype(np.float32) + noise[..., None] * m, 0, 255).astype(np.uint8)
cv2.imwrite(out, fixed, [cv2.IMWRITE_JPEG_QUALITY, 95])
cv2.imwrite(prev, cv2.resize(fixed[1350:1650, 80:560], (960, 600)), [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imwrite(prev.replace(".jpg", "_mask.jpg"), cv2.resize(mask[1350:1650, 80:560], (480, 300)))
