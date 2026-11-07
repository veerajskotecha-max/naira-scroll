# Charm Chain Duo Ring (L16): the worn frame W1 has the two rings right (a finger between them, as the supplier's photo) but SIX charms;
# the edit that was asked to remove one (L16_W1e in edits.py) changed nothing. So the extra charm, the lower of the two pears hanging one under
# the other, is removed here: its outline and jump ring (traced on a 2x grid of the frame, kept clear of the chain beside it) are filled with the
# skin just to its left (same light, same texture) by seamless (Poisson) cloning, so its tone meets the skin around it.
# That leaves the supplier's five in order: emerald-cut, pear, emerald-cut, pear, emerald-cut.  Usage: python3 -I l16fix.py -> out/L16_W1f.png
import os
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
POLY = [(850, 1338), (866, 1336), (871, 1350), (872, 1370), (872, 1400), (870, 1425), (862, 1440), (845, 1446), (826, 1441), (814, 1422),
        (812, 1400), (817, 1380), (830, 1364), (843, 1350)]
DX = -70                                      # the skin source: the same rows, 70 px to the left
img = np.asarray(Image.open(os.path.join(H, "out", "L16_W1.png")).convert("RGB"))
m = np.zeros(img.shape[:2], np.uint8); cv2.fillPoly(m, [np.array(POLY, np.int32)], 255)
m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))     # the gold rim and the soft shadow go too
n_px = int((m > 0).sum())
src = np.roll(img, -DX, axis=1)                                              # src[y, x] = img[y, x + DX]
ys, xs = np.nonzero(m); centre = (int((xs.min() + xs.max()) / 2), int((ys.min() + ys.max()) / 2))
out = cv2.seamlessClone(np.ascontiguousarray(src[..., ::-1]), np.ascontiguousarray(img[..., ::-1]), m, centre, cv2.NORMAL_CLONE)[..., ::-1]
Image.fromarray(out).save(os.path.join(H, "out", "L16_W1f.png")); print("px", n_px, "centre", centre)
