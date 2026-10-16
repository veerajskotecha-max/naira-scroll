# Composites the real Prism Rivière Bracelet (the listing photo refs/prism/listing-3.jpg, the bracelet closed in a loop on a
# plinth) into the Z Image candy-bowl scene, lying on the ground around one of the loose sweets. Scale is true: the loop is
# about 65 mm across its outer edge (an 18 cm bracelet closed), against sweets of about 2.5 cm. The scene's sun sits low behind
# the sweets on the left, so each link's shadow falls toward the camera and to the right, and the pink sweet's own shadow falls
# across the links in front of it. The two sweets the loop passes behind are redrawn over it from the original plate.
# Usage: comp_prism.py [key=value ...]   Output: <scratchpad>/<out>.png (the full 1536×2048 scene)
import json, os, sys
import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
SRC = f"{HERE}/../concept-camps/build/refs/prism/listing-3.jpg"
MASK, SCENE = f"{HERE}/masks/prism-listing-3.png", f"{SPB}/e1/plates/clusterC1_scene.png"   # mask: GrabCut, hand-seeded
# the loop's contact ellipse in the listing photo: centre, semi-axes (front links' foot at y 1070, back links' foot at y 590)
SRC_C, SRC_A, SRC_B, SRC_W = (861, 830), 591, 240, 1186

P = dict(cx=480, cy=1626,      # centre of the loop's contact ellipse in the scene
         w=702,                # outer width: 65 mm at 10.8 px/mm (the pink sweet is 270 px across)
         sy=1.12,              # the scene's camera is a little steeper than the listing's: open the ellipse slightly
         band=99,              # screen height of the links (8 mm), for telling front links from back ones
         sun=(0.64, 0.68),     # shadow offset per px of height above the ground, from the sweets' own shadows
         sh=(0.70, 0.54, 0.50),  # ground multiplier in full shadow (sampled in the sweets' cast shadows)
         blur=(1.2, 3.5), ao=0.35,
         lit=(237.8, 219.2, 208.3),  # the open ground's colour beside the loop, for reading the sweets' shadows
         shade=0.8,            # how much of the ground's shadow the links take where the pink sweet's shadow crosses them
         tint=(1.0, 0.97, 0.945), lift=(36, 28, 26), gain=1.0, glow=0.45, grain=1.6,
         balls=[(599, 1517, 135), (861, 1658, 141)],   # sweets drawn back over the loop (they are nearer the camera)
         out="c4/plates/prismC1_m1")   # relative to the scratchpad
for kv in sys.argv[1:]:
    k, v = kv.split("=", 1); P[k] = json.loads(v) if v[:1] in "[{0123456789-." else v

def main():
    scene = np.asarray(Image.open(SCENE).convert("RGB")).astype(np.float32) / 255; H, W = scene.shape[:2]
    src = np.asarray(Image.open(SRC).convert("RGB")).astype(np.float32) / 255
    m = cv2.imread(MASK, cv2.IMREAD_GRAYSCALE)
    m = cv2.GaussianBlur(cv2.erode(m, np.ones((3, 3), np.uint8), iterations=1), (0, 0), 1.0).astype(np.float32) / 255
    k = P["w"] / SRC_W; ky = k * P["sy"]
    # source → scene: scale about the contact-ellipse centre, then move it to (cx, cy)
    M = np.float32([[k, 0, P["cx"] - k * SRC_C[0]], [0, ky, P["cy"] - ky * SRC_C[1]]])
    pre = np.dstack([src * m[..., None], m])
    big = cv2.warpAffine(pre, M, (W, H), flags=cv2.INTER_AREA if k < 1 else cv2.INTER_LINEAR)
    A = np.clip(big[..., 3], 0, 1); S = np.where(A[..., None] > 1e-3, big[..., :3] / np.maximum(A, 1e-3)[..., None], 0)
    a, b = SRC_A * k, SRC_B * ky; cx, cy = P["cx"], P["cy"]
    S = (S * np.array(P["tint"]) * (1 - np.array(P["lift"]) / 255) + np.array(P["lift"]) / 255) * P["gain"]
    # height of every link pixel above its foot on the contact ellipse (front branch or back branch, whichever band it is in)
    X = np.arange(W, dtype=np.float32)[None, :]; Y = np.arange(H, dtype=np.float32)[:, None]
    q = np.sqrt(np.clip(1 - ((X - cx) / a) ** 2, 0, 1)); yf = cy + b * q; yb = cy - b * q
    band = P["band"]
    front = np.abs(Y - (yf - band / 2)) <= np.abs(Y - (yb - band / 2))
    foot = np.where(front, yf, yb) * np.ones_like(Y); hpx = np.clip(foot - Y, 0, None)
    # the sweets' shadows on the ground, read where each link stands: links inside a shadow are darkened like the ground
    lit = np.array(P["lit"]) / 255
    G = np.clip(cv2.GaussianBlur(scene, (0, 0), 4) / lit, 0, 1)
    fx = np.clip(np.round(X * np.ones_like(Y)).astype(int), 0, W - 1)
    def at(yy_): return G[np.clip(np.round(yy_ * np.ones_like(Y)).astype(int), 0, H - 1), fx]
    # blend the two feet softly where the bands meet at the loop's ends, so the shading has no seam
    wf = 1 / (1 + np.exp(-(np.abs(Y - (yb - band / 2)) - np.abs(Y - (yf - band / 2))) / 8))
    Gf = at(yf) * wf[..., None] + at(yb) * (1 - wf[..., None])
    S = S * (1 - P["shade"] * (1 - Gf))
    # each link pixel's shadow: from its foot, toward the camera and to the right, in proportion to its height
    ys, xs = np.nonzero(A > .02); al = A[ys, xs]; hh = hpx[ys, xs]
    tx = xs + P["sun"][0] * hh; ty = foot[ys, xs] + P["sun"][1] * hh
    lo, hi = np.zeros((H, W), np.float32), np.zeros((H, W), np.float32); hmax = max(float(hh.max()), 1)
    for buf, wgt in ((lo, 1 - hh / hmax), (hi, hh / hmax)):
        ix, iy = np.clip(np.round(tx).astype(int), 0, W - 1), np.clip(np.round(ty).astype(int), 0, H - 1)
        np.add.at(buf, (iy, ix), al * wgt)
    def soft(img, s): return cv2.GaussianBlur(img, (0, 0), s)
    close = np.ones((5, 5), np.uint8)
    sh = np.clip(soft(cv2.morphologyEx(np.clip(lo, 0, 1), cv2.MORPH_CLOSE, close), P["blur"][0]) +
                 soft(cv2.morphologyEx(np.clip(hi, 0, 1), cv2.MORPH_CLOSE, close), P["blur"][1]), 0, 1)
    # a thin contact line where the links meet the ground
    contact = np.zeros((H, W), np.float32)
    for yy_ in (yf, yb):
        for xi in range(int(cx - a), int(cx + a) + 1):
            yi = int(round(float(yy_[0, xi]))) if 0 <= xi < W else -1
            if 0 <= yi < H: contact[yi, xi] = 1
    contact = soft(contact, 2.5) * 2.2
    dark = np.clip(sh + P["ao"] * np.clip(contact, 0, 1) * (1 - sh), 0, 1)
    # the stones let coloured light into their own shadow
    mx, mn = S.max(-1), S.min(-1); sat = np.clip(((mx - mn) / np.maximum(mx, 1e-3) - .15) / .2, 0, 1) * A
    gl = np.zeros((H, W), np.float32); col = np.zeros((H, W, 3), np.float32)
    sv = sat[ys, xs]; ix, iy = np.clip(np.round(tx).astype(int), 0, W - 1), np.clip(np.round(ty).astype(int), 0, H - 1)
    np.add.at(gl, (iy, ix), sv); [np.add.at(col[..., c], (iy, ix), sv * S[ys, xs, c]) for c in range(3)]
    gl = soft(gl, 2.5); col = soft(col, 2.5) / np.maximum(gl, 1e-3)[..., None]; gl = np.clip(gl * 1.4, 0, 1) * dark
    hue = col / np.maximum(col.mean(-1, keepdims=True), 1e-3)
    out = scene * (1 - dark[..., None] * (1 - np.array(P["sh"])))
    out = out + (scene * np.clip(.35 + .65 * hue, 0, 1.4) - out) * P["glow"] * gl[..., None]
    out = out * (1 - A[..., None]) + S * A[..., None]
    g = np.random.default_rng(5).normal(0, P["grain"] / 255, (H, W, 1)).astype(np.float32)
    out = np.clip(out + g * A[..., None], 0, 1)
    # the sweets nearer the camera go back over the loop, from the untouched plate
    for (bx, by, br) in P["balls"]:
        disc = np.zeros((H, W), np.float32); cv2.circle(disc, (bx, by), br, 1.0, -1, lineType=cv2.LINE_AA)
        disc = soft(disc, 1.2)[..., None]; out = out * (1 - disc) + scene * disc
    Image.fromarray((out * 255 + .5).astype(np.uint8)).save(f"{SPB}/{P['out']}.png")
    ys2, xs2 = np.nonzero(A > .5); print("loop box", (xs2.min(), ys2.min(), xs2.max(), ys2.max()), "->", P["out"])

if __name__ == "__main__":
    main()
