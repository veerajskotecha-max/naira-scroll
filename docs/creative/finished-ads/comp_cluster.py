# Composites the real Prism Cluster stud (the listing macro, refs/cluster/listing-5.jpg) into the Z Image candy-bowl scene that the
# last credits paid for, so the "Almost edible." frame shows the product's own photograph rather than a generated likeness.
# The stud is scaled to its true size against the sweets (the arc is about 20 mm; the sweets were asked for at about 2 cm), and
# given the scene's light: the sun sits low behind the bowl on the left, so the stud casts a short, warm shadow toward the camera
# and to the right, like the loose sweets do. Usage: comp_cluster.py [key=value ...]  Output: <scratchpad>/<out>.png
import json, os, sys
import cv2
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
SRC = f"{HERE}/../edition-one/build/refs/cluster/listing-5.jpg"
MASK, SCENE = f"{HERE}/masks/cluster-listing-5.png", f"{SPB}/e1/plates/clusterC1_scene.png"   # mask: GrabCut, hand-seeded

P = dict(cx=465, cy=1705,      # where the stud's centre sits in the scene (1536×2048): nestled at the pink sweet's lower left
         w=236,                # stud width in px: 0.88 of the neighbouring sweet's diameter (20 mm arc against ~2.2 cm sweets)
         rot=1.5,              # degrees, counter-clockwise
         face=111,             # screen height of the 10 mm face (it rests on its lowest claw and the post tip, about 63° up)
         shx=50, shy=20,       # where the shadow of the top edge lands, relative to the contact point (from the sweets' shadows:
                               # the sun is about 43° up, behind and left; the camera about 36° up)
         sh=(0.70, 0.54, 0.50),  # ground multiplier in full shadow (sampled in the sweets' cast shadows)
         blur=(0.8, 5.0),      # penumbra σ at the contact and at the far edge
         ao=0.6,               # contact darkening right under the lowest claws
         tint=(1.0, 0.965, 0.935), lift=(34, 26, 24), gain=0.96,   # warm the metal toward the blush scene, lift its black reflections
         glow=0.6,             # light the stones let through into their own shadow
         grain=1.8, out="e1/plates/clusterC1_m1")   # relative to the scratchpad
for kv in sys.argv[1:]:
    k, v = kv.split("=", 1); P[k] = json.loads(v) if v[:1] in "[{0123456789-." else v
    if isinstance(P[k], list): P[k] = tuple(P[k])

def resize_f(a, size):
    return np.stack([np.asarray(Image.fromarray(a[..., c]).resize(size, Image.LANCZOS)) for c in range(a.shape[2])], -1)

def place():
    src = np.asarray(Image.open(SRC).convert("RGB")).astype(np.float32) / 255
    m = Image.open(MASK).convert("L").filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    al = np.asarray(m).astype(np.float32)[..., None] / 255
    ys, xs = np.where(al[..., 0] > .5); x0, x1, y0, y1 = xs.min() - 24, xs.max() + 24, ys.min() - 24, ys.max() + 24
    pre = np.concatenate([src * al, al], -1)[y0:y1, x0:x1]                     # premultiplied RGBA
    if P["rot"]:
        pre = np.stack([np.asarray(Image.fromarray(pre[..., c]).rotate(P["rot"], Image.BICUBIC, expand=True)) for c in range(4)], -1)
    ys, xs = np.where(pre[..., 3] > .5); bw = xs.max() - xs.min() + 1
    k = P["w"] / bw; size = (round(pre.shape[1] * k), round(pre.shape[0] * k))
    pre = np.clip(resize_f(pre, size), 0, None); pre[..., 3] = np.clip(pre[..., 3], 0, 1)
    a = pre[..., 3:]; rgb = np.where(a > 1e-3, pre[..., :3] / np.maximum(a, 1e-3), 0)
    return np.clip(rgb, 0, 1), a[..., 0]

def main():
    scene = np.asarray(Image.open(SCENE).convert("RGB")).astype(np.float32) / 255; H, W = scene.shape[:2]
    rgb, a = place(); h, w = a.shape
    ox, oy = round(P["cx"] - w / 2), round(P["cy"] - h / 2)
    A = np.zeros((H, W), np.float32); A[oy:oy + h, ox:ox + w] = a
    S = np.zeros((H, W, 3), np.float32); S[oy:oy + h, ox:ox + w] = rgb
    # grade: warm the white metal toward the blush light, lift its black studio reflections, a touch darker (the face is backlit)
    S = (S * np.array(P["tint"]) * (1 - np.array(P["lift"]) / 255) + np.array(P["lift"]) / 255) * P["gain"]
    # the sun is low behind the stud on the left: its face sits in fill light, a little darker toward the ground, and the
    # upper-left rims of the claws, pearls and stones catch the sun
    yy = (np.arange(H, dtype=np.float32)[:, None] - oy) / h
    S = S * (1 + P.get("grad", .06) * (0.5 - np.clip(yy, 0, 1)))[..., None]
    M1 = np.float32([[1, 0, P.get("rimdx", -1)], [0, 1, P.get("rimdy", -2)]])
    rim = A * (1 - cv2.warpAffine(A, M1, (W, H)))                            # inside the stud, with open air toward the sun
    rim = cv2.GaussianBlur(rim, (0, 0), .7)
    S = S + (1 - S) * np.clip(rim * P.get("rim", .45), 0, 1)[..., None] * np.array([1, .96, .9])
    # the stones (saturated pixels) pass coloured light into the shadow
    mx, mn = S.max(-1), S.min(-1); sat = np.clip(((mx - mn) / np.maximum(mx, 1e-3) - .18) / .25, 0, 1) * A
    rows = np.where(A.max(1) > .5)[0]; yc = rows.max()                      # the contact: the stud's lowest point
    sx, sy, f = P["shx"], P["shy"], P["face"]
    # shadow of a point t of the way up the face lands at (x + sx·t, yc + sy·t): an affine flip-and-shear of the silhouette
    aff = (1, -sx / sy, sx / sy * yc, 0, -f / sy, yc * (1 + f / sy))
    M = np.float32([aff[:3], aff[3:]])
    def proj(img): return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR | cv2.WARP_INVERSE_MAP)
    core = cv2.erode(sat, np.ones((3, 3), np.uint8), iterations=2)            # stone centres: their rims refract light away
    sh0, gl0 = proj(A), proj(core)
    col0 = np.stack([proj(S[..., c] * core) for c in range(3)], -1)
    t = np.clip((np.arange(H)[:, None] - yc) / sy, 0, 1).astype(np.float32) * np.ones((1, W), np.float32)
    b0, b1 = P["blur"]
    def soft(img, s): return cv2.GaussianBlur(img, (0, 0), s)
    lv = [(b0, soft(sh0, b0)), ((b0 + b1) / 2, soft(sh0, (b0 + b1) / 2)), (b1, soft(sh0, b1))]
    sh = np.where(t < .5, lv[0][1] * (1 - 2 * t) + lv[1][1] * 2 * t, lv[1][1] * (2 - 2 * t) + lv[2][1] * (2 * t - 1))
    gs = (b0 + b1) / 2; gl = soft(gl0, gs); col = soft(col0, gs) / np.maximum(gl, 1e-3)[..., None]
    gl = np.clip(gl * 1.6, 0, 1) * sh
    # contact darkening: a short skirt under the lower edge, strongest where the edge is nearest the ground (the crescent's
    # tips are in the air, so they get little)
    cols = np.where(A.max(0) > .5)[0]; low = np.full(W, -1e9, np.float32)
    for x in cols: low[x] = np.where(A[:, x] > .5)[0].max()
    near = np.clip(1 - (yc - low) / P.get("near", 45), 0, 1)
    d = np.arange(H, dtype=np.float32)[:, None] - low[None, :]
    ao = soft(np.where(d > -1, np.exp(-np.maximum(d, 0) / P.get("aolen", 10)), 0).astype(np.float32) * near[None, :], 2.5)
    dark = np.clip(sh + P["ao"] * ao * (1 - sh), 0, 1)[..., None]
    mult = 1 - dark * (1 - np.array(P["sh"]))
    lit = scene * mult
    hue = col / np.maximum(col.mean(-1, keepdims=True), 1e-3)                # each stone's colour, at unit brightness
    lit = lit + (scene * np.clip(.35 + .65 * hue, 0, 1.4) - lit) * P["glow"] * gl[..., None]   # coloured light through the stones
    out = lit * (1 - A[..., None]) + S * A[..., None]
    g = np.random.default_rng(3).normal(0, P["grain"] / 255, (H, W, 1)).astype(np.float32)
    out = np.clip(out + g * A[..., None], 0, 1)
    Image.fromarray((out * 255 + .5).astype(np.uint8)).save(f"{SPB}/{P['out']}.png")
    print("stud box", (ox, oy, ox + w, oy + h), "contact y", yc, "->", f"{SPB}/{P['out']}.png")

if __name__ == "__main__":
    main()
