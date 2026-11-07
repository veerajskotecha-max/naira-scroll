# Lilac Flutter Studs (L04): the paler lilac. In the owner's photo the stones are a paler, pinker lilac than in the packshot, so every lilac
# pixel of the approved frames moves the same way toward the photo's colour: hue +DH degrees, chroma x SK, lighter by DL (each stone's own
# shading kept), so the two studs stay identical and every frame matches. The owner's photo also shows the upper-right stone of each
# butterfly a little smaller than the upper-left one. Two Nano Banana edits (L04_He, L04_Hg in edits.py) left the four stones the same
# size (the first also turned one stud pinker), and redrawing the wing locally left visible marks on the plaster, so the photos keep four
# near-equal stones and the approval page says so.
# Usage: python3 -I l04fix.py KEY [KEY ...]   (out/KEY.png -> out/KEY_t.png)
import os, sys
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); O = lambda k: os.path.join(H, "out", k + ".png")
DH, SK, DL = 14.0, 0.72, 6.0
def lab_of(rgb):
    lab = cv2.cvtColor(rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab); A, B = lab[..., 1], lab[..., 2]
    return lab, np.hypot(A, B), (np.degrees(np.arctan2(B, A)) + 360) % 360

def tone(src, dst):
    rgb = np.asarray(Image.open(O(src)).convert("RGB")); lab, C, h = lab_of(rgb)
    w = np.clip((C - 5) / 6, 0, 1) * np.clip(1 - np.abs(((h - 300 + 180) % 360) - 180 - 0) / 55, 0, 1) ** 0.5
    w = cv2.GaussianBlur(w.astype(np.float32), (0, 0), 1.0)
    A, B = lab[..., 1], lab[..., 2]; h2 = np.radians(h + DH * w); C2 = C * (1 - (1 - SK) * w)
    lab2 = lab.copy(); lab2[..., 0] = np.clip(lab[..., 0] + DL * w, 0, 100)
    lab2[..., 1] = C2 * np.cos(h2); lab2[..., 2] = C2 * np.sin(h2)
    rgb2 = np.clip(cv2.cvtColor(lab2.astype(np.float32), cv2.COLOR_Lab2RGB), 0, 1)
    Image.fromarray((rgb2 * 255 + 0.5).astype(np.uint8)).save(O(dst)); print(src, "->", dst, "lilac px", int((w > 0.5).sum()))

if __name__ == "__main__":
    for k in sys.argv[1:]: tone(k, k + "_t")
