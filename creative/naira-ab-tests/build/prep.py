"""Prepares every crop the 14 ads use, all cut from the two original photos:
   2ebe51f1 (Prism Rivière in sugared jelly sweets, the Sweet On You photo) and
   141d0fbd (Woven Gold Hoops on the oxblood dome, the red Woven photo)."""
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np, cv2

IMG = Path(__file__).resolve().parent.parent / 'img'
SUG = Image.open(IMG / 'src_sugar.png').convert('RGB')   # 2048 x 2048
RED = Image.open(IMG / 'src_red.png').convert('RGB')     # 1856 x 2304


def save(im, name, q=95):
    im.save(IMG / name, quality=q, subsampling=0) if name.endswith('.jpg') else im.save(IMG / name)


# Prism: feed 4:5 base (full height of the square), comparison window, sugar texture for the type fill
save(SUG.crop((410, 0, 2048, 2048)).resize((1080, 1350), Image.LANCZOS), 'p_base.jpg')
save(SUG.crop((410, 300, 2048, 1498)).resize((1080, 790), Image.LANCZOS), 'p_win.jpg')
tex = SUG.crop((1380, 760, 2048, 1520)).resize((760, 864), Image.LANCZOS)
tex = ImageEnhance.Contrast(ImageEnhance.Color(tex).enhance(1.25)).enhance(1.12)
save(tex, 'p_tex.jpg')

# Woven: full-bleed 9:16 and the 'push' placement (photo from y 600, hoops larger and lower)
save(RED.crop((308, 0, 1604, 2304)).resize((1080, 1920), Image.LANCZOS), 'w_full.jpg')
push = RED.crop((313, 513, 1600, 2086)).resize((1080, 1320), Image.LANCZOS)
save(push, 'w_push.jpg')

# hoop cut-out on the push image (GrabCut seeded with the gold mask) for the type-behind-hoops edit
a = np.asarray(push).copy()
r, g, b = [a[..., i].astype(int) for i in range(3)]
gold = (r > 150) & (g > 95) & (b < 0.75 * g) & (r - b > 70)
mask = np.full(a.shape[:2], cv2.GC_BGD, np.uint8)
ys, xs = np.nonzero(gold)
x0, x1, y0, y1 = max(xs.min() - 30, 0), min(xs.max() + 30, a.shape[1] - 1), max(ys.min() - 30, 0), min(ys.max() + 30, a.shape[0] - 1)
mask[y0:y1, x0:x1] = cv2.GC_PR_BGD
warm = (r > 95) & (g > 55) & (r - b > 45) & (g > 0.45 * r)
mask[(warm) & (mask == cv2.GC_PR_BGD)] = cv2.GC_PR_FGD
mask[gold] = cv2.GC_FGD
bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
cv2.grabCut(cv2.cvtColor(a, cv2.COLOR_RGB2BGR), mask, None, bgd, fgd, 6, cv2.GC_INIT_WITH_MASK)
fg = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
n, lab, stats, _ = cv2.connectedComponentsWithStats(fg)
keep = np.zeros_like(fg)
for i in range(1, n):
    if stats[i, cv2.CC_STAT_AREA] > 4000: keep[lab == i] = 255
alpha = Image.fromarray(keep).filter(ImageFilter.GaussianBlur(1.2))
cut = push.copy(); cut.putalpha(alpha); save(cut, 'w_push_hoops.png')
print('hoop bbox', x0, x1, y0, y1, 'fg px', int((keep > 0).sum()))
prev = Image.new('RGB', push.size, (40, 160, 60)); prev.paste(cut, (0, 0), cut); prev.resize((540, 660)).save(IMG / 'chk_hoops.jpg', quality=85)

# W3 detail lens: source pixels under a 95px frame-circle at (790, 1130) in push coordinates, shown 1.81x
s = 1080 / 1287
cx, cy = 790 / s + 313, (1130 - 600) / s + 513
rs = 95 / s
lens = RED.crop((round(cx - rs), round(cy - rs), round(cx + rs), round(cy + rs))).resize((344, 344), Image.LANCZOS)
lens = lens.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
save(lens, 'w_lens.jpg')
print('lens src centre', round(cx), round(cy), 'r', round(rs))
