# Teardrop Pear Hoops (L11), Silver (12 Nov, ../corrections.md): the pear's three claws kept a rose-gold tint in the silver close worn frame
# (L11_W2s); a Higgsfield edit asking for silver claws changed nothing there (the same edit worked on the macro, L11_Msc). Here the claws
# themselves go cool silver: inside a small circle round each claw, every warm metal pixel (hue 20-110, some colour, not dark hair) loses
# its colour, its lightness kept, so the claw's own shine stays.
# Usage: python3 -I silverfix.py KEY OUT x,y,r [x,y,r ...] -> out/OUT.png
import os, sys
import numpy as np, cv2
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); k, o = sys.argv[1], sys.argv[2]
img = np.asarray(Image.open(os.path.join(H, "out", k + ".png")).convert("RGB")).astype(np.float32) / 255
lab = cv2.cvtColor(img, cv2.COLOR_RGB2Lab); C = np.hypot(lab[..., 1], lab[..., 2]); h = (np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) + 360) % 360
zone = np.zeros(C.shape, np.float32)
for c in sys.argv[3:]:
    x, y, r = map(int, c.split(",")); cv2.circle(zone, (x, y), r, 1, -1)
w = zone * ((h > 20) & (h < 110) & (C > 4) & (lab[..., 0] > 35)).astype(np.float32)
w = cv2.GaussianBlur(w, (0, 0), 0.8)
lab[..., 1] = lab[..., 1] * (1 - w) + (-0.5) * w; lab[..., 2] = lab[..., 2] * (1 - w) + (-1.5) * w   # a faintly cool neutral, as the hoop
out = np.clip(cv2.cvtColor(lab, cv2.COLOR_Lab2RGB), 0, 1)
Image.fromarray((out * 255 + 0.5).astype(np.uint8)).save(os.path.join(H, "out", o + ".png")); print(k, "->", o, "claw px", int((w > 0.5).sum()))
