"""Open the back of a ring in an approved take, keeping every other pixel.

An image model draws the gap (an adjustable ring's open back) into a copy of the take;
this script aligns that copy to the take, keeps only the patch around the gap, and
feathers it into the original. The stones, claws, light and grain stay the approved take's.

    python3 -I openback.py            # writes out/<key>o.png for every key in GAP
"""
import cv2, numpy as np, os, sys

H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
# key: (original take, model copy with the gap, box around the gap x0, y0, x1, y1)
GAP = {
    "J12_H": ("J12_H.png", "J12_Ho1.png", (900, 1200, 1200, 1500)),
    "J14_H": ("J14_Hn.png", "J14_Ho1.png", (900, 950, 1090, 1120)),
    "J14_M": ("J14_Mn.png", "J14_Mo1.png", (600, 760, 920, 1010)),
}

def align(orig, edit, box):
    """Affine-align `edit` onto `orig` (ECC on the ring region around the gap)."""
    g1 = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
    g2 = cv2.cvtColor(edit, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
    x0, y0, x1, y1 = box; pad = 400
    mask = np.zeros(g1.shape, np.uint8); mask[max(0, y0 - pad):y1 + pad, max(0, x0 - pad):x1 + pad] = 255
    # the gap itself differs by design: keep it out of the fit
    mask[y0:y1, x0:x1] = 0
    warp = np.eye(2, 3, dtype=np.float32)
    crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 300, 1e-7)
    cc, warp = cv2.findTransformECC(g1, g2, warp, cv2.MOTION_AFFINE, crit, mask, 5)
    out = cv2.warpAffine(edit, warp, (orig.shape[1], orig.shape[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REFLECT)
    return out, warp, cc

def patch(orig, aligned, box, thresh=10, grow=21, feather=31):
    """Mask of the gap: where the aligned copy differs inside the box, grown and feathered."""
    x0, y0, x1, y1 = box
    d = np.abs(orig.astype(np.int16) - aligned.astype(np.int16)).max(2)
    m = np.zeros(d.shape, np.uint8)
    m[y0:y1, x0:x1] = (d[y0:y1, x0:x1] > thresh).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (grow, grow)))
    box_m = np.zeros(d.shape, np.uint8); box_m[y0:y1, x0:x1] = 255
    m = cv2.min(m, cv2.erode(box_m, np.ones((feather, feather), np.uint8)))
    return cv2.GaussianBlur(m.astype(np.float32) / 255, (0, 0), feather / 3)[..., None]

if __name__ == "__main__":
    keys = sys.argv[1:] or list(GAP)
    for k in keys:
        a, b, box = GAP[k]
        orig = cv2.imread(os.path.join(H, a)); edit = cv2.imread(os.path.join(H, b))
        aligned, warp, cc = align(orig, edit, box)
        m = patch(orig, aligned, box)
        out = (orig * (1 - m) + aligned * m).round().clip(0, 255).astype(np.uint8)
        cv2.imwrite(os.path.join(H, f"{k}o.png"), out)
        outside = np.abs(out.astype(int) - orig.astype(int))[m[..., 0] < 0.01].max()
        print(k, "ecc", round(float(cc), 4), "shift", warp[:, 2].round(2).tolist(), "patch px", int((m > 0.5).sum()), "max change outside patch", int(outside))
