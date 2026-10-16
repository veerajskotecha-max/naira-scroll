# Cuts single-product reference crops from PI thumbnails (fractional boxes), upscaled to 1024 long side.
import sys, os
from PIL import Image
S = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pi")
B = {
 "P01_gold": ("p1_y0330_x127", (0.10, 0.40, 0.95, 0.98)),
 "P01_silver": ("p1_y0330_x127", (0.08, 0.04, 0.88, 0.62)),
 "P02_lariat": ("p1_y0406_x126", (0.30, 0.30, 0.78, 1.00)),
 "P02P03_full": ("p1_y0406_x126", (0.18, 0.00, 0.85, 1.00)),
 "P03_marquise": ("p1_y0406_x126", (0.28, 0.00, 0.80, 0.48)),
 "P04_tennis_bold": ("p1_y0487_x128", (0, 0, 1, 1)),
 "P05_tennis_fine": ("p1_y0642_x130", (0, 0, 1, 1)),
 "P06_silver": ("p1_y0711_x130", (0.00, 0.10, 0.50, 0.95)),
 "P06_gold": ("p1_y0711_x130", (0.47, 0.25, 1.00, 0.98)),
 "P07_gold": ("p2_y0238_x126", (0.00, 0.08, 0.48, 0.75)),
 "P07_silver": ("p2_y0238_x126", (0.33, 0.04, 0.88, 0.75)),
 "P08_roman": ("p2_y0337_x131", (0.14, 0.00, 0.96, 1.00)),
 "P09_gold": ("p2_y0466_x129", (0.08, 0.30, 0.62, 1.00)),
 "P09_silver": ("p2_y0466_x129", (0.40, 0.00, 1.00, 0.55)),
 "P11_crystal_band": ("p3_y0086_x132", (0, 0, 1, 1)),
 "P12_gold": ("p3_y0162_x126", (0.03, 0.15, 0.52, 1.00)),
 "P12_silver": ("p3_y0162_x126", (0.45, 0.00, 0.98, 0.78)),
 "P13_gold": ("p3_y0248_x128", (0.03, 0.25, 0.56, 0.98)),
 "P13_silver": ("p3_y0248_x128", (0.44, 0.08, 1.00, 0.82)),
 "P14_omega": ("p3_y0526_x128", (0, 0, 1, 1)),
 "P15_silver": ("p3_y0602_x127", (0.03, 0.25, 0.56, 0.98)),
 "P15_gold": ("p3_y0602_x127", (0.40, 0.08, 0.98, 0.80)),
 "P16_bow": ("p4_y0150_x126", (0, 0, 1, 1)),
 "P17_pearl": ("p4_y0209_x127", (0, 0, 1, 1)),
 "P18_necklace": ("p4_y0301_x128", (0.10, 0.00, 0.95, 0.62)),
 "P19_bracelet": ("p4_y0301_x128", (0.40, 0.42, 1.00, 0.86)),
 "P20_earrings": ("p4_y0301_x128", (0.04, 0.58, 0.45, 1.00)),
 "P21_tiger": ("p4_y0395_x125", (0, 0, 1, 1)),
 "P22_gold": ("p4_y0462_x127", (0, 0, 1, 1)),
 "P22_silver": ("p4_y0526_x128", (0, 0, 1, 1)),
 "P23_pearcuff": ("p4_y0657_x127", (0, 0, 1, 1)),
 "V1_coil_silver": ("p4_y0081_x125", (0.40, 0.08, 1.00, 0.72)),
 "V2_star_gold": ("p4_y0593_x126", (0.00, 0.10, 0.66, 0.92)),
 "V3_white_necklace": ("p2_y0542_x128", (0.12, 0.00, 0.88, 0.32)),
 "V3_green_necklace": ("p2_y0689_x127", (0.12, 0.00, 0.88, 0.36)),
 "V4_purple_huggie": ("p5_y0085_x127", (0.20, 0.00, 0.78, 0.36)),
 "V4_green_huggie": ("p5_y0085_x127", (0.00, 0.24, 0.62, 0.70)),
 "V4_white_huggie": ("p5_y0085_x127", (0.15, 0.58, 0.72, 1.00)),
 "V4_red_huggie": ("p5_y0085_x127", (0.66, 0.36, 1.00, 0.80)),
 "V5_purple_ring": ("p5_y0178_x127", (0, 0, 1, 1)),
}
for k, (f, (a, b, c, d)) in B.items():
    im = Image.open(f"{S}/img/{f}.png").convert("RGB"); W, H = im.size
    im = im.crop((int(a * W), int(b * H), int(c * W), int(d * H)))
    s = 1024 / max(im.size); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    im.save(f"{S}/refs/{k}.jpg", quality=93)
print(len(B))
