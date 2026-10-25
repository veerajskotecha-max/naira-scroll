"""cutout.png -> poster/display.png: crop to the table, gentle grade, 2x Lanczos + light sharpen."""
import sys, numpy as np
from pathlib import Path
from PIL import Image, ImageFilter
D = Path(sys.argv[1]); Y0 = 640
c = Image.open(D / "cutout.png").convert("RGBA").crop((0, Y0, 1512, 2016))
rgb = np.asarray(c.convert("RGB")).astype(np.float32) / 255
a = c.getchannel("A")
# tame the specular glare on the two laminated catalogue sheets (paper whites stay below ~0.89)
import cv2
L = rgb.max(-1)
g = np.clip((L - 0.88) / (0.98 - 0.88), 0, 1); g = g * g * (3 - 2 * g)
reg = np.zeros_like(g); reg[1060 - Y0:, 150:1380] = 1
reg = cv2.GaussianBlur(reg, (0, 0), 12)
g = cv2.GaussianBlur(g * reg, (0, 0), 2.0)
w = 1 - np.clip(g * 1.6, 0, 1)
num = cv2.GaussianBlur(rgb * w[..., None], (0, 0), 15); den = cv2.GaussianBlur(w, (0, 0), 15)[..., None] + 1e-4
fill = num / den
k = np.clip(g * 0.9, 0, 0.9)[..., None]
rgb = rgb * (1 - k) + fill * k + 0.05 * g[..., None]
rgb = np.clip(rgb, 0, 1)
# levels: lift the flat fluorescent look a touch
lo, hi = 0.035, 0.97
rgb = np.clip((rgb - lo) / (hi - lo), 0, 1)
# soft S-curve
rgb = rgb + 0.10 * (rgb - 0.5) * (1 - np.abs(2 * rgb - 1))
# warm a little and add vibrance
rgb[..., 0] *= 1.025; rgb[..., 2] *= 0.975
m = rgb.mean(-1, keepdims=True); sat = rgb.max(-1, keepdims=True) - rgb.min(-1, keepdims=True)
rgb = m + (rgb - m) * (1 + 0.16 * (1 - sat))
rgb = np.clip(rgb, 0, 1)
out = Image.fromarray((rgb * 255).astype(np.uint8))
out = out.resize((c.width * 2, c.height * 2), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.4, 55, 2))
a2 = a.resize(out.size, Image.LANCZOS)
out.putalpha(a2)
(D / "poster").mkdir(exist_ok=True)
out.save(D / "poster" / "display.png", optimize=False)
print(out.size)
