"""retouch_corner.py <plate> <cutout> <out> <target_hue> <target_chroma> — recolour the warm cream table showing past the
torn paper at the TOP of a lilac plate into the lilac of the paper. Only pixels in warm regions connected to the top edge,
never inside the product cut-out (dilated). Lightness and texture are kept; hue/chroma move with feathered weights."""
import sys, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
from lab import rgb2lab, lab2rgb
src, cutp, dst, TH, TC = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5])
im = np.asarray(Image.open(src).convert('RGB')).astype(float) / 255
L = rgb2lab(im); C = np.hypot(L[..., 1], L[..., 2]); h = (np.degrees(np.arctan2(L[..., 2], L[..., 1])) + 360) % 360
def ss(x, a, b): t = np.clip((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)
warm = ss(h, 15, 35) * (1 - ss(h, 115, 140)) * ss(C, 2.0, 4.0)
# region: connected to the top edge and above the product
lab_, n = ndimage.label(warm > 0.3)
top_ids = set(np.unique(lab_[0, :])) - {0}
region = np.isin(lab_, list(top_ids))
region = ndimage.binary_dilation(region, iterations=6)
prot = np.asarray(Image.open(cutp).convert('RGBA').split()[3].resize(im.shape[1::-1]).filter(ImageFilter.MaxFilter(21))).astype(float) / 255
w = np.asarray(Image.fromarray((region * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(8))).astype(float) / 255
w = w * np.clip(warm * 1.2 + 0.25, 0, 1) * (1 - prot)
dh = ((TH - h + 180) % 360) - 180
nh = h + dh * w; nC = C + (TC - C) * w
nL = L[..., 0] - (L[..., 0] - 84) * 0.35 * w          # pull the very bright cream down a little toward the paper
lab2 = np.stack([nL, nC * np.cos(np.radians(nh)), nC * np.sin(np.radians(nh))], -1)
out = np.clip(lab2rgb(lab2), 0, 1)
Image.fromarray((out * 255 + 0.5).astype(np.uint8)).save(dst)
print(dst, 'retouched px %.2f%%' % (100 * (w > 0.5).mean()), 'max weight inside product %.3f' % (w * (prot > 0.5)).max())
