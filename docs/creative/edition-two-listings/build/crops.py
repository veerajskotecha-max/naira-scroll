# Cuts product reference crops from the full-size Notion photos. Boxes are in 750x1000 preview coordinates.
import json, sys, os
from PIL import Image
SRC = sys.argv[1]; OUT = sys.argv[2]
BOX = {
 "N01_mesh_silver":  ("IMG_5628", [20, 240, 660, 700]),
 "N01_mesh_silver_d":("IMG_5628", [360, 400, 650, 660]),
 "N02_mesh_gold":    ("IMG_5630", [30, 170, 710, 680]),
 "N02_mesh_gold_d":  ("IMG_5630", [340, 450, 650, 690]),
 "N03_cable":        ("IMG_5633", [20, 170, 680, 680]),
 "N03_cable_d":      ("IMG_5633", [220, 470, 650, 680]),
 "N04_coil":         ("IMG_5634", [190, 250, 570, 670]),
 "N04_coil_d":       ("IMG_5634", [300, 340, 470, 600]),
 "N05_marquise":     ("IMG_5635", [150, 270, 460, 680]),
 "N05_marquise_d":   ("IMG_5635", [170, 290, 420, 560]),
 "N06_baguette_clear":   ("IMG_5636", [200, 40, 520, 940]),
 "N06_baguette_clear_d": ("IMG_5636", [300, 240, 480, 520]),
 "N07_drop_ring_silver":   ("IMG_5637", [300, 230, 550, 450]),
 "N08_drop_ring_gold":     ("IMG_5640", [270, 400, 490, 580]),
 "N09_star_bangle":        ("IMG_5638", [190, 420, 670, 590]),
 "N09_star_bangle_d":      ("IMG_5638", [380, 450, 610, 540]),
 "N10_tile_bangle":        ("IMG_5639", [210, 330, 720, 480]),
 "N10_tile_bangle_d":      ("IMG_5639", [380, 350, 610, 450]),
 "N11_knot_silver":        ("IMG_5641", [140, 130, 680, 440]),
 "N11_knot_silver_d":      ("IMG_5641", [370, 290, 590, 430]),
 "N12_knot_gold":          ("IMG_5642", [30, 70, 620, 560]),
 "N12_knot_gold_d":        ("IMG_5642", [320, 330, 530, 510]),
 "N13_green_pear_drops":   ("IMG_5643", [170, 200, 540, 500]),
 "N13_green_pear_drops_d": ("IMG_5643", [180, 250, 335, 495]),
 "N14_link_necklace":      ("IMG_5644", [120, 0, 610, 1000]),
 "N15_link_bracelet":      ("IMG_5644", [260, 340, 450, 770]),
 "N16_red_bracelet":       ("IMG_5645", [300, 300, 500, 950]),
 "N16_red_bracelet_d":     ("IMG_5645", [320, 380, 470, 620]),
 "N17_green_bracelet":     ("IMG_5646", [310, 250, 500, 1000]),
 "N17_green_bracelet_d":   ("IMG_5646", [330, 270, 470, 520]),
 "N18_green_ring":         ("IMG_5647", [320, 470, 470, 740]),
 "N19_red_ring":           ("IMG_5648", [280, 340, 420, 590]),
 "N20_pearl_hoops":        ("IMG_5649", [250, 400, 520, 790]),
 "N20_pearl_hoops_d":      ("IMG_5649", [265, 415, 485, 615]),
 "N21_green_c_hoops":      ("IMG_5650", [260, 400, 530, 760]),
 "N22_red_necklace":       ("IMG_5651", [270, 0, 500, 1000]),
 "N23_red_huggies":        ("IMG_5652", [150, 430, 530, 700]),
 "N23_red_huggies_d":      ("IMG_5652", [150, 480, 360, 700]),
 "N24_emerald_hoops":      ("IMG_5653", [360, 420, 600, 700]),
}
for k, (img, b) in BOX.items():
    im = Image.open(os.path.join(SRC, img + ".jpg"))
    s = im.width / 750.0
    c = im.crop(tuple(int(v * s) for v in b))
    c.thumbnail((1600, 1600))
    c.save(os.path.join(OUT, k + ".jpg"), quality=93)
    print(k, c.size)
