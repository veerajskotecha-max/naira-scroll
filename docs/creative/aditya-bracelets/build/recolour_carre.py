# Emerald Carré (ADT03) in the supplier's other colours, 26 Oct 2026.
# The owner sent Aditya's photo of the same square-stone tennis line in pink, blue, champagne, green and purple, and asked
# for each colour as its own listing with the green listing's photos. Only the stones are recoloured: every pixel whose
# CIELab hue is the stones' green moves to the target colour, keeping its shading (lightness and chroma relative to the
# stones' median), so facets, glints and shadows stay where they are. Gold, skin, the saffron camisole and the plaster sit
# at other hues and are untouched. Usage: python3 -I recolour_carre.py [OUTDIR]
import os, sys
import numpy as np, cv2
from PIL import Image

H = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.join(H, "../exports")
SRC = [os.path.join(EXP, f"emerald-carre-bracelet-0{i}.jpg") for i in range(1, 5)]

HANDLES = {"pink": "blush-carre-bracelet", "blue": "sapphire-carre-bracelet", "champagne": "champagne-carre-bracelet",
           "purple": "amethyst-carre-bracelet"}

# Target stone body in the listing's light: (L, C, hue in degrees, lightness contrast). Read from Aditya's photo, where
# each colour sits beside the green under the same light: blue is darker than the green, purple a little lighter and
# duller, pink and champagne pale.
TARGETS = {
    "pink": (76, 20, 342, 0.55),
    "blue": (21, 47, 277, 0.95),
    "champagne": (66, 32, 67, 0.60),
    "purple": (38, 38, 299, 0.90),
}


GOLD_HUE = 82  # the settings' polished gold tone, in CIELab degrees


def _ramp(x, a, b):
    return np.clip((x - a) / (b - a), 0, 1)


def recolour(path, target):
    rgb = np.asarray(Image.open(path).convert("RGB")).astype(np.float32) / 255
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2Lab)
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.hypot(A, B); h = (np.degrees(np.arctan2(B, A)) + 360) % 360
    # Between the gold (hue about 80) and the stones (130 to 200) lie yellow-greens, where a stone is seen through or
    # against the gold, as on the back of the loop. Each is split by hue into a gold share, set to the gold's hue, and
    # a stone share, recoloured, so no olive is left. Pixels with little colour (glints, the cream ground) stay put.
    # Nothing but stone is green here, so in the green hues even faint, pale tints (the far side's glints) are taken.
    f = _ramp(h, 86, 130); fade = 1 - _ramp(h, 200, 215)
    cw = np.maximum(_ramp(C, 6, 16), _ramp(C, 2, 7) * _ramp(h, 118, 130) * fade)
    t = cw * f * fade                                  # stone share
    g = cw * (1 - f) * ((h > 86) & (h < 130))          # gold share
    t, g = (cv2.GaussianBlur(x.astype(np.float32), (0, 0), 0.8) for x in (t, g))
    gold = np.stack([L, C * np.cos(np.radians(GOLD_HUE)), C * np.sin(np.radians(GOLD_HUE))], -1)
    core = (h > 125) & (h < 200) & (C > 18)
    Lm, Cm = np.median(L[core]), np.median(C[core])
    hm = np.degrees(np.arctan2(np.sin(np.radians(h[core])).mean(), np.cos(np.radians(h[core])).mean())) % 360
    Lt, Ct, ht, k = target
    L2 = np.clip(Lt + (L - Lm) * k, 4, 97)
    C2 = np.clip(Ct * (C / Cm) ** 0.8, 0, 90)
    dh = ((h - hm + 180) % 360) - 180
    h2 = np.radians(ht + dh * 0.3)
    out = np.stack([L2, C2 * np.cos(h2), C2 * np.sin(h2)], -1)
    lab2 = lab * (1 - t - g)[..., None] + out * t[..., None] + gold * g[..., None]
    rgb2 = np.clip(cv2.cvtColor(lab2.astype(np.float32), cv2.COLOR_Lab2RGB), 0, 1)
    return Image.fromarray((rgb2 * 255 + 0.5).astype(np.uint8))


if __name__ == "__main__":
    # No OUTDIR: write the listing exports, ../exports/<handle>-NN.jpg, in the green listing's order.
    out = sys.argv[1] if len(sys.argv) > 1 else EXP; os.makedirs(out, exist_ok=True)
    for name, handle in HANDLES.items():
        for i, p in enumerate(SRC, 1):
            stem = f"{handle}-0{i}" if out == EXP else f"{name}-0{i}"
            recolour(p, TARGETS[name]).save(os.path.join(out, stem + ".jpg"), quality=93, subsampling=0)
        print(name, handle)
