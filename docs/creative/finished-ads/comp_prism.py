# Composites the real Prism Rivière Bracelet (the listing photo refs/prism/listing-3.jpg, the bracelet closed in a loop on a
# plinth) into the Z Image candy-bowl scene, lying on the ground around one of the loose sweets. Scale is true within tolerance:
# the loop is 676 px across its outer edge, about 61 mm against sweets of about 2.5 cm (an 18 cm bracelet closed is about 65 mm).
# The scene's sun sits low behind the sweets on the left, so each link's shadow falls toward the camera and to the right, and the
# pink sweet's own shadow falls across the links in front of it. The two sweets the loop passes behind are redrawn over it from
# the original plate, each through a matte traced to its own sugar crystals. Verdicts: concept-camps/build/verify/composite_r*.json
# Usage: comp_prism.py [key=value ...]   Output: <scratchpad>/<out>.png (the full 1536×2048 scene, or with frame=[x0,y0,x1,y1,w]
# that crop of it rendered w px wide)
import json, os, sys
import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
SRC = f"{HERE}/../concept-camps/build/refs/prism/listing-3.jpg"
MASK, SCENE = f"{HERE}/masks/prism-listing-3.png", f"{SPB}/e1/plates/clusterC1_scene.png"   # mask: GrabCut, hand-seeded
# the loop's contact ellipse in the listing photo: centre, semi-axes (front links' foot at y 1070, back links' foot at y 590), and the
# cut-out's real outer width (source x 268-1410)
SRC_C, SRC_A, SRC_B, SRC_W = (861, 830), 591, 240, 1143

P = dict(cx=480, cy=1626,      # centre of the loop's contact ellipse in the scene
         w=676,                # outer width: 61 mm at 11.1 px/mm (the pink sweet is 278 px across, a 2.5 cm sweet)
         sy=1.12,              # the scene's camera is a little steeper than the listing's: open the ellipse slightly
         band=99,              # screen height of the links (8 mm), for telling front links from back ones
         sun=(0.43, 0.66),     # shadow offset per px of height above the ground, from the sweets' own shadows (57° below level)
         sh=(0.70, 0.54, 0.50),  # ground multiplier in full shadow (sampled in the sweets' cast shadows)
         blur=(1.2, 3.5), ao=0.35,
         lit=(237.8, 219.2, 208.3),  # the open ground's colour beside the loop, for reading the sweets' shadows
         shade=0.8,            # how much of the ground's shadow the links take where the pink sweet's shadow crosses them
         tint=(1.0, 0.97, 0.945), lift=(36, 28, 26), gain=1.0, glow=0.12, grain=2.4, env=0.35,
         # sweets drawn back over the loop (they are nearer the camera): circle fits to their sugar, refined ray by ray to the
         # crystals' own edge (matte=0 draws plain discs instead)
         balls=[(595.7, 1514.4, 138.9), (861.9, 1658.4, 145.1)], matte=1, unmix=1,
         out="c4/plates/prismC1_m1",  # relative to the scratchpad
         # the plate reviews' tested fixes (composite_r1, r2): feet measured on the cut-out and blended into the fitted ellipse at the
         # loop's ends (cblend), no second shadow on shaded ground, shadows cast from the camera-facing face (78 px, the 8 mm band)
         # rather than the link tops, the piece softened to the scene's focus, the metal warmed toward the sweets
         contact="mask", cblend=1, sunlit_cap=1, soft=0.5, wall=78, wallshade=1.0, rim=0,
         # the front links face away from the back sun: faces darker, a sun rim on their tops, but none on links in a sweet's shadow
         front=1, fshade=0.86, frim=0.35, rimsun=1)
for kv in sys.argv[1:]:
    k, v = kv.split("=", 1); P[k] = json.loads(v) if v[:1] in "[{0123456789-." else v

def sweet_matte(sc, bx, by, br, n=2048, span=7):
    """Alpha of one sweet: along each of n rays from its centre, the outermost strong colour step within span px of the fitted
    circle; rays with no clear step take the edge of the strong rays either side."""
    scs = cv2.GaussianBlur(sc, (0, 0), .7); th = np.linspace(0, 2 * np.pi, n, endpoint=False)
    rr = np.arange(br - span - 2, br + span + 2.01, .25)
    xs = (bx + rr[None] * np.cos(th)[:, None]).astype(np.float32); ys = (by + rr[None] * np.sin(th)[:, None]).astype(np.float32)
    C = np.stack([cv2.remap(np.ascontiguousarray(scs[..., c]), xs, ys, cv2.INTER_LINEAR) for c in range(3)], -1) * 255
    d = np.zeros(C.shape[:2], np.float32); d[:, 4:-4] = np.linalg.norm(C[:, 8:] - C[:, :-8], axis=-1)   # the step across 2 px
    d[:, (rr < br - span) | (rr > br + span)] = 0
    st = d.max(1); cand = d >= np.maximum(0.6 * st[:, None], 12); rb = np.full(n, br, np.float64)
    for i in np.nonzero(cand.any(1))[0]:       # the peak of the outermost strong step (its middle, not its outer tail)
        j = np.nonzero(cand[i])[0][-1]; k = j
        while k > 0 and cand[i, k - 1]: k -= 1
        rb[i] = rr[k + np.argmax(d[i, k:j + 1])]
    weak = ~cand.any(1) | (st < 9); i = np.nonzero(~weak)[0]
    rb[weak] = np.interp(np.nonzero(weak)[0], np.r_[i - n, i, i + n], np.r_[rb[i], rb[i], rb[i]])
    rb = np.median(np.stack([np.roll(rb, s_) for s_ in range(-6, 7)]), 0)
    H, W = sc.shape[:2]; X, Y = np.meshgrid(np.arange(W), np.arange(H)); dx, dy = X - bx, Y - by
    t = (np.arctan2(dy, dx) % (2 * np.pi)) / (2 * np.pi) * n; i0 = np.floor(t).astype(int) % n; f = t - np.floor(t)
    return np.clip(rb[i0] * (1 - f) + rb[(i0 + 1) % n] * f - np.hypot(dx, dy) + .5, 0, 1).astype(np.float32)

def main():
    sc_im = Image.open(SCENE).convert("RGB"); full = np.asarray(sc_im).astype(np.float32) / 255
    # each sweet's matte is cut at the scene's own resolution, then framed with it
    mattes = [sweet_matte(full, bx, by, br) if P["matte"] else None for bx, by, br in P["balls"]]
    if P.get("frame"):                     # [x0, y0, x1, y1, out_w]: render one framing at its own resolution, not upscaled after
        x0, y0, x1, y1, ow = P["frame"]; f = ow / (x1 - x0); oh = round((y1 - y0) * f)
        sc_im = sc_im.crop((x0, y0, x1, y1)).resize((ow, oh), Image.LANCZOS)
        mattes = [None if m_ is None else cv2.resize(m_[y0:y1, x0:x1], (ow, oh), interpolation=cv2.INTER_AREA) for m_ in mattes]
        P.update(cx=(P["cx"] - x0) * f, cy=(P["cy"] - y0) * f, w=P["w"] * f, band=P["band"] * f, wall=P["wall"] * f, soft=P["soft"] * f,
                 blur=[b * f for b in P["blur"]], balls=[((bx - x0) * f, (by - y0) * f, br * f) for bx, by, br in P["balls"]])
    scene = np.asarray(sc_im).astype(np.float32) / 255; H, W = scene.shape[:2]
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
    if P["soft"]: S = cv2.GaussianBlur(S, (0, 0), P["soft"])
    S = (S * np.array(P["tint"]) * (1 - np.array(P["lift"]) / 255) + np.array(P["lift"]) / 255) * P["gain"]
    # polished metal mirrors what is around it: the plinth's cream gives way to the sweets' colours nearby
    if P.get("env", 0):
        env = cv2.GaussianBlur(scene, (0, 0), 45); env = env / np.maximum(env.mean(-1, keepdims=True), 1e-3)
        mx_, mn_ = S.max(-1), S.min(-1); metal = np.clip(1 - ((mx_ - mn_) / np.maximum(mx_, 1e-3)) / .12, 0, 1) * A
        S = S * (1 + P["env"] * metal[..., None] * (env - 1))
    # height of every link pixel above its foot on the contact ellipse (front branch or back branch, whichever band it is in)
    X = np.arange(W, dtype=np.float32)[None, :]; Y = np.arange(H, dtype=np.float32)[:, None]
    q = np.sqrt(np.clip(1 - ((X - cx) / a) ** 2, 0, 1)); yf = cy + b * q; yb = cy - b * q
    if P["contact"] == "mask":       # contact curves measured on the cut-out itself, not an ellipse
        mm = (cv2.imread(MASK, cv2.IMREAD_GRAYSCALE) > 127).astype(np.uint8)
        n_, lab_ = cv2.connectedComponents(1 - mm)
        brd = set(np.unique(np.r_[lab_[0], lab_[-1], lab_[:, 0], lab_[:, -1]]))
        hs = [i for i in range(1, n_) if i not in brd]; hole = lab_ == hs[int(np.argmax([(lab_ == i).sum() for i in hs]))]
        xs_, fr_, bk_ = [], [], []
        for xsrc in range(mm.shape[1]):
            hc = np.nonzero(hole[:, xsrc])[0]
            if len(hc) < 3: continue
            xs_.append(xsrc); bk_.append(hc.min()); fr_.append(np.nonzero(mm[:, xsrc])[0].max())
        xs_, fr_, bk_ = map(np.array, (xs_, fr_, bk_)); ker = np.ones(15) / 15
        fr_s = np.convolve(np.pad(fr_, 7, mode="edge"), ker, "valid"); bk_s = np.convolve(np.pad(bk_, 7, mode="edge"), ker, "valid")
        px = P["cx"] + k * (xs_ - SRC_C[0]); pf = P["cy"] + ky * (fr_s - SRC_C[1]); pb = P["cy"] + ky * (bk_s - SRC_C[1])
        ex, ey, ea, eb = 803, 845, 547, 250          # ellipse fitted to the same contact points, for the loop's two ends
        ecx, ecy, eaa, ebb = P["cx"] + k * (ex - SRC_C[0]), P["cy"] + ky * (ey - SRC_C[1]), ea * k, eb * ky
        qq = np.sqrt(np.clip(1 - ((X - ecx) / eaa) ** 2, 0, 1)); yf = (ecy + ebb * qq).copy(); yb = (ecy - ebb * qq).copy()
        xx = X[0]; ins = (xx >= px.min()) & (xx <= px.max())
        yf[0, ins] = np.interp(xx[ins], px, pf); yb[0, ins] = np.interp(xx[ins], px, pb)
        if P["cblend"]:   # no step where the measured curves hand over to the ellipse: each end's offset fades to 0 at its tip
            ef, eb_ = ecy + ebb * qq[0], ecy - ebb * qq[0]
            i0, i1 = int(np.nonzero(ins)[0].min()), int(np.nonzero(ins)[0].max()); xl, xr = ecx - eaa, ecx + eaa
            for i, x_lo, x_hi in ((i0, xl, i0), (i1, i1, xr)):
                dfi, dbi = yf[0, i] - ef[i], yb[0, i] - eb_[i]
                sel = (xx >= x_lo) & (xx <= x_hi) & ~ins
                wgt = np.clip((xx[sel] - xl) / max(i0 - xl, 1), 0, 1) if i == i0 else np.clip((xr - xx[sel]) / max(xr - i1, 1), 0, 1)
                yf[0, sel] = ef[sel] + dfi * wgt; yb[0, sel] = eb_[sel] + dbi * wgt
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
    # relight for the back sun: the camera-facing outer walls fall into shade and the tops' back-left edges catch a rim. Globally
    # (wallshade, rim) or on the front links only (front=1: weight wf toward the front band, fading out past 0.75 a from the centre,
    # where the loop turns side-on and the front/back assignment flips)
    wall_ = P["wall"] or band / 2
    wsh = np.clip((wall_ - hpx) / 12 + 0.5, 0, 1)                    # 1 on the wall, 0 on the top, 12 px blend
    M1 = np.float32([[1, 0, 2], [0, 1, 2]]); rim = A * (1 - cv2.warpAffine(A, M1, (W, H)))
    rim = cv2.GaussianBlur(rim, (0, 0), .7) * np.clip((hpx - wall_ * 0.8) / 4 + .5, 0, 1)
    wfr = np.ones((H, W), np.float32)
    if P["front"]:
        wfr = wf * np.clip((0.75 - np.abs(X - cx) / a) / 0.12 + 0.5, 0, 1)
        S = S * (1 - (1 - P["fshade"]) * (wsh * wfr)[..., None])
        rsun = np.ones((H, W), np.float32)
        if P["rimsun"]:               # the sun's share at each link's foot: links in a sweet's shadow get no sun rim
            shm_ = float(np.mean(P["sh"])); rsun = np.clip((Gf.mean(-1) - shm_) / (1 - shm_), 0, 1)
        S = S + (1 - S) * np.clip(rim * wfr * rsun * P["frim"], 0, 1)[..., None] * np.array([1, .96, .9])
    if P["wallshade"] != 1.0:
        S = S * (1 - (1 - P["wallshade"]) * wsh[..., None])
    if P["rim"]:
        S = S + (1 - S) * np.clip(rim * P["rim"], 0, 1)[..., None] * np.array([1, .96, .9])
    # each link pixel's shadow: from its foot, toward the camera and to the right, in proportion to its height
    ys, xs = np.nonzero(A > .02); al = A[ys, xs]; hh = hpx[ys, xs]
    if P["wall"]:                     # above the wall the link is its flat top: same height, footprint further back
        top = hh > P["wall"]; fy = np.where(top, ys + P["wall"], foot[ys, xs]); hh = np.minimum(hh, P["wall"])
        tx = xs + P["sun"][0] * hh; ty = fy + P["sun"][1] * hh
    else:
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
    if P["sunlit_cap"]:               # ground already out of the sun cannot be shadowed again
        shm = float(np.mean(P["sh"])); sunlit = np.clip((G.mean(-1) - shm) / (1 - shm), 0, 1)
        dark = dark * sunlit; gl = gl * sunlit
    g = np.random.default_rng(5).normal(0, P["grain"] / 255, (H, W, 1)).astype(np.float32)
    def paint(base):                  # shadows, coloured light and the piece itself, laid on a ground
        o = base * (1 - dark[..., None] * (1 - np.array(P["sh"])))
        o = o + (base * np.clip(.35 + .65 * hue, 0, 1.4) - o) * P["glow"] * gl[..., None]
        return np.clip(o * (1 - A[..., None]) + S * A[..., None] + g * A[..., None], 0, 1)
    # the sweets nearer the camera go back over the loop, from the untouched plate
    al = np.zeros((H, W), np.float32)
    for (bx, by, br), m_ in zip(P["balls"], mattes):
        if m_ is None:
            m_ = np.zeros((H, W), np.float32); cv2.circle(m_, (round(bx), round(by)), round(br) + 1, 1.0, -1, lineType=cv2.LINE_AA)
            m_ = soft(m_, 1.2)
        al = np.maximum(al, m_)
    if P["unmix"]:   # a sweet's rim pixels hold some of the old ground behind it: unmix it (I = aF + (1-a)B) and lay them on the new one
        wg = (al < .02).astype(np.float32)
        Bg = np.clip(soft(scene * wg[..., None], 2.5) / np.maximum(soft(wg, 2.5), 1e-4)[..., None], 0, 1)
        out_bg = paint(np.where(al[..., None] > 0, Bg, scene))
        out = np.where(al[..., None] > 0, np.clip(scene + (1 - al[..., None]) * (out_bg - Bg), 0, 1), out_bg)
    else:
        out = paint(scene); out = out * (1 - al[..., None]) + scene * al[..., None]
    Image.fromarray((out * 255 + .5).astype(np.uint8)).save(f"{SPB}/{P['out']}.png")
    ys2, xs2 = np.nonzero(A > .5); print("loop box", (xs2.min(), ys2.min(), xs2.max(), ys2.max()), "->", P["out"])

if __name__ == "__main__":
    main()
