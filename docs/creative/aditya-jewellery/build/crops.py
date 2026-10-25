# Cuts the single-piece reference crops (refs/<key>_full.jpg, refs/<key>_det.jpg) from Aditya's call screenshots, 2x
# LANCZOS. Boxes are in the 923-px-wide display grid the screenshots were read on (x1.2774 to the 1179-px originals);
# a mask paints out a neighbouring piece on a shared card so each reference shows one product only.
import json, os, sys
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../refs"); K = 1179 / 923
SRC = sys.argv[1]  # folder holding the original <id>-image.png uploads
C = {  # key: (upload id, full box, det box or None, masks)
 "J01": ("6f95a343", (240, 800, 680, 1180), (400, 970, 515, 1155), []),
 "J02": ("2bb852ef", (315, 860, 635, 1100), (338, 885, 437, 1078), []),
 "J03": ("4d67cd3b", (40, 1050, 745, 1230), (312, 1076, 438, 1204), []),
 "J04": ("e116ebee", (175, 1080, 735, 1290), (418, 1182, 518, 1282), []),
 "J05": ("6689aa13", (240, 820, 680, 1180), (388, 1072, 527, 1172), []),
 "J06": ("c5eef062", (295, 965, 630, 1100), (478, 982, 612, 1072), []),
 "J07": ("faedccfc", (240, 800, 715, 1198), (412, 1046, 534, 1199), []),
 "J08": ("41921703", (135, 910, 775, 1070), (406, 936, 524, 1049), []),
 "J09": ("47ce8b5b", (165, 1000, 785, 1190), None, []),
 "J10": ("1ed2e870", (90, 970, 815, 1110), (330, 975, 580, 1105), []),
 "J11": ("16509319", (330, 978, 645, 1190), (395, 975, 610, 1135), []),
 "J12": ("65b654ce", (300, 860, 600, 1120), (380, 905, 530, 1070), []),
 "J13": ("86bcd9c7", (320, 870, 600, 1110), (385, 905, 540, 1075), []),
 "J14": ("da231cf6", (300, 845, 465, 1035), None, [(440, 940, 620, 1130)]),
 "J15": ("da231cf6", (425, 945, 605, 1128), None, [(300, 845, 452, 1015)]),
 "J16": ("90ad6ac6", (245, 700, 695, 1095), (452, 898, 528, 1098), [(318, 940, 372, 1300), (582, 950, 640, 1300)]),
 "J17": ("90ad6ac6", (300, 925, 665, 1295), (572, 948, 652, 1292), [(452, 890, 530, 1100)]),
 "J18": ("3c55237d", (85, 570, 845, 1220), (300, 900, 640, 1200), []),
}
def cut(im, box, masks):
    im = im.copy(); d = ImageDraw.Draw(im)
    for m in masks: d.rectangle(tuple(round(v * K) for v in m), fill=(8, 8, 10))
    c = im.crop(tuple(round(v * K) for v in box))
    return c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
os.makedirs(OUT, exist_ok=True)
for k, (f, full, det, masks) in C.items():
    im = Image.open(os.path.join(SRC, f"{f}-image.png")).convert("RGB")
    cut(im, full, masks).save(f"{OUT}/{k}_full.jpg", quality=93)
    if det: cut(im, det, masks).save(f"{OUT}/{k}_det.jpg", quality=93)
    print(k, "full" + (" det" if det else ""))
