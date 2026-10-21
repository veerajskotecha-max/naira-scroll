# Prepares the stall photo for the pop-up stories:
#   1 paints out the red cable hanging on the right (traced path + cable-coloured pixels, OpenCV inpaint)
#   2 cuts her out with rembg's birefnet-portrait model, then adds back the jewellery table and the pink box below a traced
#     line, keys out wall still showing round the box, and drops the side-table sliver at the left edge
# Writes <scratchpad>/pop/work/stall_clean.jpg and fg.png (RGBA, photo x 440–2000, y 430–1536).
# Needs a venv with rembg[cpu] (rembg downloads the model into U2NET_HOME). Usage: <venv>/bin/python cutout.py <photo.jpg>
import os, sys
import cv2, numpy as np
from PIL import Image
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/pop"
os.environ.setdefault("U2NET_HOME", f"{SP}/models")

def keyed_wall(img, y0, y1, x0, x1, lo, spread, edges):
    """Bright, colourless pixels in a region that connect to its open edges (so tags inside the box are kept)."""
    reg = img[y0:y1, x0:x1].astype(int); mn, mx = reg.min(2), reg.max(2)
    n, lab = cv2.connectedComponents(((mn > lo) & (mx - mn < spread)).astype(np.uint8), connectivity=4)
    border = {"top": lab[0, :], "left": lab[:, 0], "right": lab[:, -1]}
    keep = set(np.unique(np.concatenate([border[e] for e in edges]))) - {0}
    return cv2.dilate(np.isin(lab, list(keep)).astype(np.uint8), np.ones((3, 3), np.uint8))

def main(photo):
    im = cv2.imread(photo); H, W = im.shape[:2]
    b, g, r = [im[:, :, i].astype(int) for i in range(3)]
    band = np.zeros((H, W), np.uint8)
    cable = [(1488, 0), (1500, 150), (1507, 300), (1543, 493), (1568, 670), (1584, 815), (1600, 960), (1610, 1012)]
    cv2.polylines(band, [np.array(cable, np.int32)], False, 255, 46)
    lum = (r + g + b) / 3; wl = cv2.medianBlur(im, 31).astype(int).sum(2) / 3
    m = cv2.dilate(((band > 0) & (((r - g > 14) & (r - b > 6)) | (lum < wl - 28))).astype(np.uint8) * 255, np.ones((5, 5), np.uint8), iterations=2)
    im = cv2.inpaint(im, m, 12, cv2.INPAINT_TELEA)
    b, g, r = [im[:, :, i].astype(int) for i in range(3)]
    lum = (r + g + b) / 3; wl = cv2.medianBlur(im, 41).astype(int).sum(2) / 3
    m = np.zeros((H, W), np.uint8); m[950:1028, 1612:1656] = ((lum < wl - 18) | ((r - g > 14) & (r - b > 8)))[950:1028, 1612:1656] * 255
    m = cv2.dilate(m, np.ones((5, 5), np.uint8), iterations=2); m[1026:, :] = 0
    im = cv2.inpaint(im, m, 10, cv2.INPAINT_TELEA)
    cv2.imwrite(f"{SP}/work/stall_clean.jpg", im, [cv2.IMWRITE_JPEG_QUALITY, 95])

    from rembg import remove, new_session
    person = np.array(remove(Image.open(f"{SP}/work/stall_clean.jpg").convert("RGB"), session=new_session("birefnet-portrait"), only_mask=True)).astype(np.float32) / 255
    k = 1.024
    left = [(round(x * k), round(y * k)) for x, y in [(0, 940), (430, 940), (470, 1062), (540, 1082), (860, 1068), (1180, 1052), (1500, 1048), (1630, 1052)]]
    poly = left + [(1660, 1040), (1662, 870), (1960, 870), (1962, 1072), (W, 1072), (W, H), (0, H)]
    table = np.zeros((H, W), np.uint8); cv2.fillPoly(table, [np.array(poly, np.int32)], 255)
    table[860:1140, 1650:W][keyed_wall(im, 860, 1140, 1650, W, 188, 26, ("top", "left", "right")) > 0] = 0
    table[960:1125, 1938:2000][keyed_wall(im, 960, 1125, 1938, 2000, 140, 30, ("top", "right")) > 0] = 0
    alpha = np.maximum(person, cv2.GaussianBlur(table, (0, 0), 1.4).astype(np.float32) / 255)
    a = (alpha * 255).astype(np.uint8); a[:1088, 440:500] = 0
    x0, x1, y0 = 440, 2000, 430
    rgba = np.dstack([cv2.cvtColor(im, cv2.COLOR_BGR2RGB), a])[y0:, x0:x1]
    Image.fromarray(rgba).save(f"{SP}/work/fg.png"); print("fg.png", rgba.shape)

if __name__ == "__main__":
    main(sys.argv[1])
