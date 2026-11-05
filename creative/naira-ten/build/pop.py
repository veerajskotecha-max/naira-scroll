"""Warhol-style screenprint of one portrait: flat colour fills under a black key, the gold hoops left as photograph."""
import numpy as np, cv2
from PIL import Image
from kit import T

IMG = T / 'img'
SRC = np.array(Image.open(IMG / 'lib' / 'a4e5d25c.png').convert('RGB'))
ALPHA = np.array(Image.open(IMG / 'pop_cut.png').convert('RGBA'))[:, :, 3]
H, W = SRC.shape[:2]


def hoop_mask():
    m = np.zeros((H, W), np.uint8)
    for (x0, y0, x1, y1) in [(462, 1140, 620, 1365), (1240, 1068, 1405, 1318)]:
        gc = np.full((H, W), cv2.GC_BGD, np.uint8)
        gc[y0:y1, x0:x1] = cv2.GC_PR_BGD
        # the braided band: an annulus inside the box is probably hoop
        cx, cy, ax, ay = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2
        yy, xx = np.mgrid[0:H, 0:W]
        r = ((xx - cx) / ax) ** 2 + ((yy - cy) / ay) ** 2
        gc[(r < 0.92) & (r > 0.36)] = cv2.GC_PR_FGD
        gc[(r < 0.80) & (r > 0.52)] = cv2.GC_FGD
        bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
        sub = (slice(y0 - 40, y1 + 40), slice(x0 - 40, x1 + 40))
        g = gc[sub].copy()
        cv2.grabCut(SRC[sub][:, :, ::-1].copy(), g, None, bgd, fgd, 6, cv2.GC_INIT_WITH_MASK)
        mm = ((g == cv2.GC_FGD) | (g == cv2.GC_PR_FGD)).astype(np.uint8)
        m[sub] |= mm
    # the braid is busy, skin is smooth: keep only textured pixels, then close the braid's gaps
    g = cv2.cvtColor(SRC, cv2.COLOR_RGB2GRAY).astype(np.float32)
    mu = cv2.blur(g, (11, 11)); sd = np.sqrt(np.maximum(cv2.blur(g * g, (11, 11)) - mu * mu, 0))
    tex = (sd > 16).astype(np.uint8)
    tex = cv2.morphologyEx(tex, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    m = m & tex
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.zeros_like(m)
    for i in range(1, n):
        if st[i, 4] > 1500: keep[lab == i] = 1
    return cv2.GaussianBlur(keep.astype(np.float32), (5, 5), 0)


if __name__ == '__main__':
    hm = hoop_mask()
    np.save(IMG / 'pop_hoops.npy', hm)
    vis = SRC.copy().astype(np.float32)
    vis = vis * (0.25 + 0.75 * hm[..., None])
    Image.fromarray(vis.astype(np.uint8)[1000:1450, 380:1500]).save(IMG / 'rev_hoopmask.jpg', quality=90)
    print('hoop pixels', int(hm.sum()))


PAL = {   # the nine functions, in order: background, skin, hair, clothes, lips
    'ROKA': ('#9ED9EF', '#BFE6C9', '#C1272D', '#F2B705', '#1D3C8F'),
    'SAGAI': ('#F4C6D7', '#FFC4A3', '#2F6B3A', '#FBF5EA', '#C2185B'),
    'MEHENDI': ('#2F6B3A', '#F9D976', '#C2185B', '#FBF5EA', '#C1272D'),
    'HALDI': ('#F2B705', '#FF9EBB', '#1D3C8F', '#FFFFFF', '#C1272D'),
    'SANGEET': ('#C2185B', '#9ED9EF', '#F2B705', '#FBF5EA', '#1D3C8F'),
    'COCKTAIL': ('#1F1A14', '#C9B6F2', '#2F6B3A', '#F2B705', '#C2185B'),
    'PHERAS': ('#C1272D', '#FFD3A6', '#E8742A', '#F2B705', '#8E1219'),
    'VIDAAI': ('#2F6B3A', '#FFF1B8', '#9ED9EF', '#C2185B', '#C1272D'),
    'RECEPTION': ('#1D3C8F', '#F4C6D7', '#9ED9EF', '#F2B705', '#C2185B'),
}


def rgb(h):
    h = h.lstrip('#'); return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], np.float32)


def regions():
    hsv = cv2.cvtColor(SRC, cv2.COLOR_RGB2HSV).astype(np.int32)
    Hh, Ss, Vv = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    person = ALPHA > 127
    yy = np.mgrid[0:H, 0:W][0]
    clothes = person & (Ss < 70) & (Vv > 160) & (yy > 1480)
    dark = (person & (Vv < 132)).astype(np.uint8)
    dark = cv2.morphologyEx(dark, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(dark, 8)
    hair = np.zeros((H, W), bool)
    for i in range(1, n):
        if st[i, 4] > 40000: hair |= lab == i
    hair = cv2.morphologyEx(hair.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8)).astype(bool) & person & ~clothes
    lips = np.zeros((H, W), bool)
    box = (slice(1170, 1290), slice(660, 1010))
    lb = ((Hh[box] <= 9) | (Hh[box] >= 172)) & (Ss[box] > 85) & (Vv[box] < 215)
    lb = cv2.morphologyEx(lb.astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    lips[box] = lb.astype(bool)
    def smooth(m, sig=2.5):
        return cv2.GaussianBlur(m.astype(np.float32), (0, 0), sig) > 0.5
    hair, clothes = smooth(hair, 4), smooth(clothes, 3)
    lips = cv2.dilate(smooth(lips, 3.5).astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)
    skin = person & ~hair & ~clothes & ~lips
    return person, skin, hair, clothes, lips


def key_layer(hair):
    g = cv2.cvtColor(SRC, cv2.COLOR_RGB2GRAY)
    b = cv2.GaussianBlur(g, (0, 0), 2.2)
    det = cv2.adaptiveThreshold(b, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 51, 10) > 0
    deep = b < 70
    strands = cv2.adaptiveThreshold(b, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 9) > 0
    k = ((det | deep) & ~hair) | ((strands | (b < 34)) & hair)
    k = k.astype(np.float32)
    k = cv2.GaussianBlur(k, (0, 0), 1.6)
    return (k > 0.5).astype(np.float32)


HM = hoop_mask()
REG = regions()
KEY = key_layer(REG[2])


def screenprint(name, crop, size, misreg=(9, 6)):
    bg, sk, ha, cl, li = [rgb(c) for c in PAL[name]]
    person, skin, hair, clothes, lips = REG
    out = np.empty((H, W, 3), np.float32); out[:] = bg
    fill = np.zeros((H, W, 3), np.float32); fm = np.zeros((H, W), bool)
    for m, c in ((skin, sk), (hair, ha), (clothes, cl), (lips, li)):
        fill[m] = c; fm |= m
    dx, dy = misreg                                      # screenprint misregistration: colour layer slips off the key
    fill = np.roll(fill, (dy, dx), (0, 1)); fm = np.roll(fm, (dy, dx), (0, 1))
    out[fm] = fill[fm]
    ink = rgb('#141012')
    k = KEY * person
    out = out * (1 - k[..., None]) + ink * k[..., None]
    gold = SRC.astype(np.float32)
    gold = np.clip((gold - 128) * 1.12 + 128 + 6, 0, 255)  # a touch more contrast so the gold reads as the only real thing
    hm = HM[..., None]
    out = out * (1 - hm) + gold * hm
    x0, y0, x1, y1 = crop
    img = Image.fromarray(out[y0:y1, x0:x1].clip(0, 255).astype(np.uint8)).resize(size, Image.LANCZOS)
    # paper grain
    noise = np.random.default_rng(len(name)).normal(0, 7, (size[1], size[0], 1)).astype(np.float32)
    a = np.array(img).astype(np.float32) + noise
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))
