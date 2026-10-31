# Shrinks a hanging pendant inside an approved packshot without touching anything else (31 Oct, B04: the owner asked for the
# heart at half its review size; two edit requests only reached 63%). Inputs: the frame (SRC) and a clean plate of the same frame
# with the pendant removed by an edit request (PLATE; it matches SRC to about 1 level outside the pendant).
#   - The pendant (bail + heart: very dark or clearly coloured pixels, C > 24 or L < 45, so its grey shadow is left out) is
#     warped about the point where the chain enters the bail: unscaled there, so the chain still meets the bail, easing to an
#     exact SCALE from R1 px out, which covers the whole heart.
#   - The chain arms into the bail top come from SRC; the plaster comes from PLATE, and the stretch of chain the plate drew past
#     the bail top is covered with bare plate plaster from DX px to the right, Poisson-blended (seamless clone).
#   - The smaller pendant gets a soft contact shadow thrown down and right, the way the key light from camera-left throws it.
# Usage: python3 -I shrink.py SRC PLATE DST ANCHOR_X ANCHOR_Y SCALE
import sys, numpy as np, cv2
from PIL import Image
src, plate, dst, ax, ay, s = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
BAIL = (893, 1214, 982, 1345)        # x0, y0, x1, y1: the bail and its loop
HEART = (785, 1325, 1090, 1600)      # the heart and its rose-gold rim
TOP = (830, 1120, 1045, 1240)        # the chain arms running into the bail top, kept from SRC
FILL = (845, 1226, 1035, 1345)       # where the plate drew chain past the bail top
R0, R1, DX = 14.0, 95.0, 175
I = np.asarray(Image.open(src).convert("RGB")).astype(np.float32); H, W = I.shape[:2]
Pl = np.asarray(Image.open(plate).convert("RGB")).astype(np.float32)
lab = cv2.cvtColor(I / 255, cv2.COLOR_RGB2Lab); L = lab[..., 0]; C = np.hypot(lab[..., 1], lab[..., 2])
box = np.zeros((H, W), np.uint8)
for x0, y0, x1, y1 in (BAIL, HEART): box[y0:y1, x0:x1] = 1
obj = (((C > 24) | (L < 45)) & (box > 0)).astype(np.uint8)
obj = cv2.morphologyEx(obj, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
cnts, _ = cv2.findContours(obj, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = [c for c in cnts if cv2.contourArea(c) > 400]
f = np.zeros_like(obj); cv2.drawContours(f, cnts, -1, 1, -1); obj = f & box
# warp: output point at distance r from the anchor samples the input at r / k(r); k eases from 1 (r < R0) to SCALE (r > R1)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); dx, dy = xx - ax, yy - ay; r = np.hypot(dx, dy)
t = np.clip((r - R0) / (R1 - R0), 0, 1); t = t * t * (3 - 2 * t); k = 1 + (s - 1) * t
mx, my = (ax + dx / k).astype(np.float32), (ay + dy / k).astype(np.float32)
remap = lambda a, v, fl=cv2.INTER_LINEAR: cv2.remap(a, mx, my, fl, borderValue=v)
a2 = remap(cv2.GaussianBlur(obj.astype(np.float32), (0, 0), 0.7), 0.0)
# plate, with the chain it drew past the bail top covered by bare plaster from DX px to the right, Poisson-blended in
x0, y0, x1, y1 = FILL; mask = np.zeros((H, W), np.uint8); mask[y0:y1, x0:x1] = 255
shifted = np.ascontiguousarray(np.roll(Pl, -DX, axis=1).clip(0, 255).astype(np.uint8))
out = cv2.seamlessClone(shifted, Pl.clip(0, 255).astype(np.uint8), mask, ((x0 + x1) // 2, (y0 + y1) // 2), cv2.NORMAL_CLONE).astype(np.float32)
# the chain arms into the bail top from SRC (not the old bail itself), feathered into the plate
tm = np.zeros((H, W), np.float32); x0, y0, x1, y1 = TOP; tm[y0:y1, x0:x1] = 1
tm = cv2.GaussianBlur(tm, (0, 0), 3) * (1 - cv2.dilate(obj, np.ones((5, 5), np.uint8)))
out = out * (1 - tm[..., None]) + I * tm[..., None]
# soft contact shadow, then the pendant
SH = np.float32([[1, 0, 9], [0, 1, 13]])
shadow = cv2.GaussianBlur(cv2.warpAffine(a2, SH, (W, H)), (0, 0), 9) * 0.2
out = out * (1 - shadow[..., None])
out = out * (1 - a2[..., None]) + remap(I, (0, 0, 0), cv2.INTER_CUBIC) * a2[..., None]
Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(dst)
hm = remap(((C > 38) & (box > 0)).astype(np.float32), 0.0) > 0.5; ys, xs = np.nonzero(hm)
print("red heart now x", xs.min(), "y", ys.min(), "w", xs.max() - xs.min(), "h", ys.max() - ys.min())

def white_balance(path, da, db=0.0):
    """Global white-balance shift in CIELab (the chain of edits had warmed B04's frame by about 4 a* units against the review frame)."""
    im = np.asarray(Image.open(path).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(im, cv2.COLOR_RGB2Lab); lab[..., 1] += da; lab[..., 2] += db
    Image.fromarray((np.clip(cv2.cvtColor(lab, cv2.COLOR_Lab2RGB), 0, 1) * 255 + 0.5).astype(np.uint8)).save(path)
