# Builds products.json: the Shopify handoff structure. One product per design; metal / stone colour / ring size are variants.
# Each variant carries its PI line, supplier code, qty, SKU, price and its own hero image; the gallery lists image keys in order.
import json, os
H = os.path.dirname(os.path.abspath(__file__)); M = json.load(open(f"{H}/meta.json"))
SIZES = ["6", "7", "8"]
GOLD = ["18k Gold Tone Plated"]; SILV = ["Rhodium Silver Tone Plated"]
BASE = ["Demi Fine", "Hypoallergenic", "Naira Petite", "Tarnish Free", "Waterproof"]
P = []
def prod(pid, title, handle, ptype, price, meta, options, variants, gallery, tags, flags=(), status="NEW", pi="", notes=""):
    m = M[meta]
    P.append(dict(id=pid, title=title, handle=handle, type=ptype, price=price, pi=pi, status=status, options=options, variants=variants,
                  gallery=gallery, line=m["line"], body=m["body"], size=m["size"], macro_alt=m["macro"], stones=m["stones"],
                  tags=sorted(set(tags + BASE + [ptype])), flags=list(flags), notes=notes))
def v(opts, sku, line, qty, img, price=None, cost=None):
    return dict(options=opts, sku=sku, pi_line=line, qty=qty, image=img, price=price, cost_usd=cost)
def sized(metal, code, line, qty_total, img, cost, price=None):
    return [v([metal, s], f"{code}-{s}", line, 3, img, price, cost) for s in SIZES]
RING_FLAG = "PI ships US sizes 6, 7 and 8 only, 3 pcs each: no size 9 variant until it is ordered."
# ---- Notion SKUs (also on the PI) ----
prod("N01", "Silk Mesh Cuff", "silk-mesh-cuff", "Bracelet", 1899, "N01", ["Metal"],
     [v(["Gold"], "YF3482-G", 6, 20, "N02_H", cost=3.95), v(["Silver"], "YF3482-S", 7, 20, "N01_H", cost=3.95)],
     ["N02_H", "N02_W1", "N02_M", "N01_H", "N01_W1", "N01_M"], ["Cuff"] + GOLD + SILV, pi="YF3482")
prod("N03", "Garnet Cable Cuff", "garnet-cable-cuff", "Bracelet", 1999, "N03", [], [v([], "N03-GARNET", None, None, "N03_H")],
     ["N03_H", "N03_W1", "N03_M"], ["Cuff", "Two Tone", "Cubic Zirconia"], ["Not on the Yiss Fera PI: confirm supplier code and stock."], pi="—")
prod("N04", "Triple Coil Wrap Bangle", "triple-coil-wrap-bangle", "Bracelet", 1899, "N04", ["Metal"],
     [v(["Gold"], "YF3937-G", 40, 10, "N04_H", cost=4.15), v(["Silver"], "YF3937-S", 41, 10, "N04_S", 1799, 3.51)],
     ["N04_H", "N04_W1", "N04_M", "N04_S"], ["Bangle", "Cubic Zirconia"] + GOLD + SILV, pi="YF3937")
prod("N05", "Marquise Wheat Cuff", "marquise-wheat-cuff", "Bracelet", 2199, "N05", [], [v([], "YF3508", 34, 20, "N05_H", cost=4.52)],
     ["N05_H", "N05_W1", "N05_M"], ["Cuff", "Cubic Zirconia"] + GOLD, pi="YF3508")
prod("BTB", "Baguette Tennis Bracelet", "baguette-tennis-bracelet", "Bracelet", 1699, "N06", ["Stone"],
     [v(["Crystal"], "YF3165-BR-CR", 22, 30, "N06_H", cost=4.15), v(["Ruby"], "YF3165-BR-RU", 24, 20, "N16_H", cost=4.15),
      v(["Emerald"], "YF3165-BR-EM", 26, 20, "N17_H", cost=4.15)],
     ["N06_H", "N06_W1", "N06_M", "N16_H", "N16_W1", "N16_M", "N17_H", "N17_W1", "N17_M"], ["Tennis", "Cubic Zirconia"] + GOLD,
     ["Crystal is near-identical to the live Baguette Éclat Bracelet (₹1,800, JDB201210). Either list Crystal here or add this stock to Baguette Éclat; do not run both at different prices."],
     pi="YF3165")
prod("DRP", "Droplet Open Ring", "droplet-open-ring", "Ring", 1199, "N07", ["Metal"],
     [v(["Gold"], "YF3791-R-G", 13, 10, "N08_H", cost=3.73), v(["Silver"], "YF3791-R-S", 15, 10, "N07_H", cost=3.48)],
     ["N08_H", "N08_W1", "N08_M", "N07_H", "N07_W1", "N07_M"], ["Adjustable"] + GOLD + SILV, pi="YF3791 ring")
prod("NSB", "North Star Bangle", "north-star-bangle", "Bracelet", 1599, "N09", ["Metal"],
     [v(["Silver"], "YF5204-S", 51, 10, "N09_H", cost=2.18), v(["Gold"], "YF5204-G", 50, 10, "N09_G", cost=2.30)],
     ["N09_H", "N09_W1", "N09_M", "N09_G"], ["Bangle", "Cubic Zirconia"] + GOLD + SILV, pi="YF5204")
prod("N10", "Tile Stone Bangle", "tile-stone-bangle", "Bracelet", 1599, "N10", [], [v([], "N10-TILE", None, None, "N10_H")],
     ["N10_H", "N10_W1", "N10_M"], ["Bangle", "Cubic Zirconia"] + GOLD, ["Not on the Yiss Fera PI: confirm supplier code and stock."], pi="—")
prod("KKB", "Kiss Knot Bangle", "kiss-knot-bangle", "Bracelet", 1499, "N11", ["Metal"],
     [v(["Gold"], "YF4152-G", 11, 20, "N12_H", cost=3.20), v(["Silver"], "YF4152-S", 12, 20, "N11_H", cost=3.20)],
     ["N12_H", "N12_W1", "N12_M", "N11_H", "N11_W1", "N11_M"], ["Bangle"] + GOLD + SILV, pi="YF4152")
prod("N13", "Mint Pear Drop Earrings", "mint-pear-drop-earrings", "Earrings", 1499, "N13", [], [v([], "YF7034", 18, 20, "N13_H", cost=2.91)],
     ["N13_H", "N13_W1", "N13_M"], ["Cubic Zirconia"] + GOLD, pi="YF7034")
prod("N14", "Duo Link Necklace", "duo-link-necklace", "Necklace", 1799, "N14", [], [v([], "YF8079-NEC", 38, 20, "N14_H", cost=3.65)],
     ["N14_H", "N14_W1", "N14_M"], ["Two Tone"], pi="YF8079")
prod("N15", "Duo Link Bracelet", "duo-link-bracelet", "Bracelet", 1299, "N15", [], [v([], "YF8079-BRA", 39, 20, "N15_H", cost=2.45)],
     ["N15_H", "N15_W1", "N15_M"], ["Two Tone"], pi="YF8079")
prod("BEB", "Baguette Eternity Band", "baguette-eternity-band", "Ring", 1499, "N19", ["Stone", "Size"],
     sized("Ruby", "YF3143-RU", 58, 9, "N19_H", 2.98) + sized("Emerald", "YF3143-EM", 59, 9, "N18_H", 2.98) + sized("Amethyst", "YF3143-AM", 57, 9, "N19_A", 2.98),
     ["N19_H", "N19_W1", "N19_M", "N18_H", "N18_W1", "N18_M", "N19_A"], ["Eternity", "Cubic Zirconia"] + GOLD, [RING_FLAG], pi="YF3143")
prod("N20", "Pearl Nugget Hoops", "pearl-nugget-hoops", "Earrings", 1499, "N20", [], [v([], "N20-PEARL", None, None, "N20_H")],
     ["N20_H", "N20_W1", "N20_M"], ["Pearl", "Hoops"] + GOLD, ["Not on the Yiss Fera PI: confirm supplier code, pearl type and stock."], pi="—")
prod("N21", "Emerald Halo C-Hoops", "emerald-halo-c-hoops", "Earrings", 1699, "N21", [], [v([], "N21-HALO", None, None, "N21_H")],
     ["N21_H", "N21_W1", "N21_M"], ["Hoops", "Cubic Zirconia"] + SILV, ["Not on the Yiss Fera PI: confirm supplier code and stock."], pi="—")
prod("BTN", "Baguette Tennis Necklace", "baguette-tennis-necklace", "Necklace", 2299, "N22", ["Stone"],
     [v(["Ruby"], "YF3165-NE-RU", 23, 20, "N22_H", cost=5.95), v(["Crystal"], "YF3165-NE-CR", 21, 30, "N22_C", cost=5.95),
      v(["Emerald"], "YF3165-NE-EM", 25, 20, "N22_E", cost=5.95)],
     ["N22_H", "N22_W1", "N22_M", "N22_C", "N22_E"], ["Tennis", "Cubic Zirconia"] + GOLD, pi="YF3165")
prod("BHG", "Baguette Huggies", "baguette-huggies", "Earrings", 1399, "N23", ["Stone"],
     [v(["Ruby"], "YF3923-RU", 54, 15, "N23_H", cost=3.19), v(["Crystal"], "YF3923-CR", 53, 15, "N23_C", cost=3.19),
      v(["Emerald"], "YF3923-EM", 55, 15, "N23_E", cost=3.19), v(["Amethyst"], "YF3923-AM", 56, 15, "N23_A", cost=3.19)],
     ["N23_H", "N23_W1", "N23_M", "N23_C", "N23_E", "N23_A"], ["Huggies", "Cubic Zirconia"] + GOLD, pi="YF3923")
prod("N24", "Emerald Deco Hoops", "emerald-deco-hoops", "Earrings", 1899, "N24", [], [v([], "N24-DECO", None, None, "N24_H")],
     ["N24_H", "N24_W1", "N24_M"], ["Hoops", "Cubic Zirconia"] + SILV, ["Not on the Yiss Fera PI: confirm supplier code and stock."], pi="—")
MONTHS = [("January", "Garnet", "jan"), ("February", "Amethyst", "feb"), ("March", "Aquamarine", "mar"), ("April", "Crystal", "apr"), ("May", "Emerald", "may"),
          ("June", "Light Amethyst", "jun"), ("July", "Ruby", "jul"), ("August", "Peridot", "aug"), ("September", "Sapphire", "sep"), ("October", "Rose", "oct"),
          ("November", "Topaz", "nov"), ("December", "Blue Zircon", "dec")]
prod("N25", "Birthstone Heart Necklace", "birthstone-heart-necklace", "Necklace", 999, "N25", ["Month"],
     [v([f"{mo} · {st}"], f"N25-{ab.upper()}", None, None, ("N25_H" if ab == "may" else f"N25_{ab}")) for mo, st, ab in MONTHS],
     ["N25_H"] + [f"N25_{ab}" for _, _, ab in MONTHS if ab != "may"], ["Birthstone", "Cubic Zirconia", "Gift"] + GOLD,
     ["Not on the Yiss Fera PI: confirm supplier code and stock per colour.", "The May variant uses the approved green hero."], pi="—")
# ---- New designs from the PI ----
prod("P01", "Tubogas Dome Ring", "tubogas-dome-ring", "Ring", 1399, "P01", ["Metal", "Size"],
     sized("Gold", "YF3608-G", 1, 9, "P01_H", 3.18) + sized("Silver", "YF3608-S", 2, 9, "P01_S", 3.18),
     ["P01_H", "P01_W1", "P01_M", "P01_S"], ["Tubogas"] + GOLD + SILV, [RING_FLAG], pi="YF3608")
prod("P05", "Fine Tennis Bracelet", "fine-tennis-bracelet", "Bracelet", 1299, "P05", [], [v([], "YF7116", 8, 20, "P05_H", cost=3.25)],
     ["P05_H", "P05_W1", "P05_M"], ["Tennis", "Cubic Zirconia"] + GOLD, ["Sits close to the live Rivière Eternal Bracelet (YF7085, 3mm stones, draft): keep both only if the stone sizes really differ (2.5mm vs 3–4mm)."], pi="YF7116")
prod("P06", "Petal Flower Studs", "petal-flower-studs", "Earrings", 1199, "P06", ["Metal"],
     [v(["Gold"], "YF7126-G", 10, 10, "P06_H", cost=2.65), v(["Silver"], "YF7126-S", 9, 10, "P06_S", cost=2.65)],
     ["P06_H", "P06_W1", "P06_M", "P06_S"], ["Studs", "Cubic Zirconia"] + GOLD + SILV, pi="YF7126")
prod("P07", "Droplet Open Cuff", "droplet-open-cuff", "Bracelet", 1799, "P07", ["Metal"],
     [v(["Gold"], "YF3791-B-G", 14, 10, "P07_H", cost=5.21), v(["Silver"], "YF3791-B-S", 16, 10, "P07_S", cost=4.68)],
     ["P07_H", "P07_W1", "P07_M", "P07_S"], ["Cuff"] + GOLD + SILV, notes="Pairs with the Droplet Open Ring.", pi="YF3791 bracelet")
prod("P08", "Roman Numeral Trio Ring", "roman-numeral-trio-ring", "Ring", 1699, "P08", ["Size"],
     [v([s], f"YF2931-{s}", 17, 3, "P08_H", cost=5.15) for s in SIZES],
     ["P08_H", "P08_W1", "P08_M"], ["Tri Tone", "Cubic Zirconia"], [RING_FLAG, "Tri-tone (rose, silver, gold): confirm the three bands are fixed together, as the supplier photo's side bar suggests."], pi="YF2931")
prod("P09", "Linked Trio Ring", "linked-trio-ring", "Ring", 1399, "P09", ["Metal", "Size"],
     sized("Gold", "YF7016-G", 19, 9, "P09_H", 3.28) + sized("Silver", "YF7016-S", 20, 9, "P09_S", 3.28),
     ["P09_H", "P09_W1", "P09_M", "P09_S"], ["Cubic Zirconia"] + GOLD + SILV,
     [RING_FLAG, "Construction read from a small supplier thumbnail: check the generated three-ring layout against the physical piece before publishing."], pi="YF7016")
prod("P11", "Crystal Baguette Eternity Ring", "crystal-baguette-eternity-ring", "Ring", 1699, "P11", ["Size"],
     [v([s], f"YF2604-{s}", 27, 3, "P11_H", cost=5.65) for s in SIZES], ["P11_H", "P11_W1", "P11_M"], ["Eternity", "Cubic Zirconia"] + GOLD, [RING_FLAG], pi="YF2604")
prod("P12", "Chain Drop Dome Ring", "chain-drop-dome-ring", "Ring", 1199, "P12", ["Metal", "Size"],
     sized("Gold", "YF8086-G", 28, 9, "P12_H", 2.54) + sized("Silver", "YF8086-S", 29, 9, "P12_S", 2.54),
     ["P12_H", "P12_W1", "P12_M", "P12_S"], ["Cubic Zirconia"] + GOLD + SILV, [RING_FLAG], pi="YF8086")
prod("P13", "Watch Link Ring", "watch-link-ring", "Ring", 1199, "P13", ["Metal", "Size"],
     sized("Gold", "YF2645-G", 30, 9, "P13_H", 2.27) + sized("Silver", "YF2645-S", 31, 9, "P13_S", 2.27),
     ["P13_H", "P13_W1", "P13_M", "P13_S"], GOLD + SILV, [RING_FLAG], pi="YF2645")
prod("P14", "Marquise Drop Choker", "marquise-drop-choker", "Necklace", 1599, "P14", [], [v([], "YF7059", 35, 20, "P14_H", cost=3.15)],
     ["P14_H", "P14_W1", "P14_M"], ["Choker", "Cubic Zirconia"] + GOLD, pi="YF7059")
prod("P15", "Mesh Band Ring", "mesh-band-ring", "Ring", 999, "P15", ["Metal", "Size"],
     sized("Gold", "YF3558-G", 36, 9, "P15_H", 1.68) + sized("Silver", "YF3558-S", 37, 9, "P15_S", 1.68),
     ["P15_H", "P15_W1", "P15_M", "P15_S"], GOLD + SILV, [RING_FLAG], notes="Pairs with the Silk Mesh Cuff.", pi="YF3558")
prod("P20", "Bold Nocturne Drops", "bold-nocturne-drops", "Earrings", 1499, "P20", [], [v([], "YF5144-EAR", 46, 30, "P20_H", cost=4.35)],
     ["P20_H", "P20_W1", "P20_M"], ["Cubic Zirconia"] + GOLD, notes="Completes the live Bold Nocturne Chain and Bracelet set.", pi="YF5144 earrings")
prod("P23", "Pear Point Open Cuff", "pear-point-open-cuff", "Bracelet", 1799, "P23", [], [v([], "YF8221", 52, 20, "P23_H", cost=4.62)],
     ["P23_H", "P23_W1", "P23_M"], ["Cuff", "Cubic Zirconia"] + GOLD, pi="YF8221")
M["C1"] = dict(line="One green square, no piercing needed.", body="An ear cuff of slim polished gold wire that slides onto the middle ridge of the ear, carrying one square princess cut emerald green stone in four claws. Wear it alone or with the Crystal Pear Ear Cuff above it.",
               size="Cuff about 12mm across; stone about 5mm (confirm on sample)", macro="Square emerald-green stone in four gold claws", stones="Emerald-green princess-cut cubic zirconia")
M["C2"] = dict(line="One clear pear, no piercing needed.", body="An ear cuff of slim polished gold wire that slides onto the middle ridge of the ear, carrying one clear pear cut stone in gold claws. Wear it alone or with the Emerald Square Ear Cuff.",
               size="Cuff about 12mm across; pear about 7mm (confirm on sample)", macro="Clear pear stone in gold claws", stones="Clear pear-cut cubic zirconia")
prod("C1", "Emerald Square Ear Cuff", "emerald-square-ear-cuff", "Earrings", 1199, "C1", [], [v([], "YF3652-GRN", 33, 20, "C1_H", cost=2.72)],
     ["C1_H", "C1_W1", "C1_M"], ["Ear Cuff", "Cubic Zirconia"] + GOLD, ["The approved packshot shows two cuffs: confirm whether YF3652 is sold as a single cuff or a pair and set the title to match."], pi="YF3652")
prod("C2", "Crystal Pear Ear Cuff", "crystal-pear-ear-cuff", "Earrings", 1199, "C2", [], [v([], "YF3652-WHT", 32, 20, "C2_H", cost=2.72)],
     ["C2_H", "C2_W1", "C2_M"], ["Ear Cuff", "Cubic Zirconia"] + GOLD, ["The approved packshot shows two cuffs: confirm whether YF3652 is sold as a single cuff or a pair and set the title to match."], pi="YF3652")
# ---- Changes to live products ----
LIVE = [
 dict(title="Star Point Band", handle="star-point-band", pi="YF5214", lines=[48, 49], action="Restock Gold (9 pcs: sizes 6, 7, 8 × 3) and ADD a Silver variant (9 pcs: sizes 6, 7, 8 × 3) at ₹799 with the new silver packshot; add Size as an option.", image="P22S_H"),
 dict(title="Rivière Eternal Bracelet", handle="riviere-eternal-bracelet", pi="YF7085", lines=[5], action="Currently DRAFT with 4 in stock: 30 more arriving. Re-activate. Optional fresh cube packshot in the new format.", image="P04_H"),
 dict(title="Marquise Layering Set", handle="marquise-layering-set", pi="YF5244", lines=[3, 4], action="Reorder: 20 tassel + 20 big-zircon necklaces = 20 sets. Restock only.", image=None),
 dict(title="Bold Nocturne Chain", handle="bold-nocturne-chain", pi="YF5144", lines=[44], action="Reorder: 30 pcs. Restock. PI cost US$7.35 against ₹1,799 retail: review margin.", image=None),
 dict(title="Bold Nocturne Bracelet", handle="bold-nocturne-bracelet", pi="YF5144-BRA", lines=[45], action="Reorder: 30 pcs. Restock. Link to the new Bold Nocturne Drops.", image=None),
 dict(title="Baroque Shell Bracelet", handle="baroque-shell-bracelet", pi="YF3925", lines=[43], action="Reorder: 10 pcs (supplier owes 10 more from the last order). PI cost US$10.00 against ₹1,799 retail: review price.", image=None),
 dict(title="Halo Curve Ring", handle="halo-curve-ring", pi="YF8453", lines=[47], action="Reorder: 20 pcs. Restock.", image=None),
 dict(title="Ribbon Bead Bracelet", handle="ribbon-bead-bracelet", pi="YF8156", lines=[42], action="Reorder: 20 pcs. Restock.", image=None),
]
OVR = {
 "N01": dict(line="Soft to the eye, firm on the wrist.", body="An open cuff built from a rounded tube of fine woven mesh, about 15mm wide, that ends in two mirror-polished oval caps facing each other across the opening. The mesh catches light like brushed silk, so it reads quietly on its own and holds its own beside a watch. In warm gold or bright silver tone."),
 "N04": dict(body=M["N04"]["body"] + " In warm gold or bright silver tone."),
 "BTB": dict(line="A straight line of light, in three colours.", body="A tennis bracelet of rectangular baguettes set crosswise, side by side, each held at its corners by gold claws and closed with a gold box clasp. About 4 to 5mm wide: fine enough for every day, bright enough for evening. In clear Crystal, deep Ruby or Emerald.",
             size="Line about 4–5mm wide; box clasp; length about 17cm (confirm on sample)", stones="Baguette-cut cubic zirconia: Crystal, Ruby or Emerald"),
 "DRP": dict(line="A ball and a drop, almost touching.", body="An open ring of smooth polished wire that swells at one end into a round ball and at the other into a long teardrop, the two sitting side by side on top of the finger. Open at the back, so it adjusts to fit. In warm gold or bright silver tone; pairs with the Droplet Open Cuff."),
 "NSB": dict(line="Stars and stones, in turn.", body="A slim flat bangle, about 6mm wide and mirror polished, its outer face alternating an engraved eight-point north star with a tiny stone at its heart and a round clear stone set flush in a bezel. In bright silver or warm gold tone."),
 "KKB": dict(line="Two ends, one kiss.", body="A flexible snake-coil bangle, finely ribbed and about 5mm thick, whose two ends cross on top of the wrist under one smooth polished X. In warm gold or bright silver tone."),
 "BEB": dict(line="Colour all the way round.", body="An eternity band set all the way round with rectangular baguettes laid crosswise, edge to edge, each held by small gold claws. About 5mm wide. In Ruby, Emerald or Amethyst.",
             size="Band about 5mm wide; US sizes 6, 7 and 8 (3 pcs each per colour on this PI)", stones="Baguette-cut cubic zirconia: Ruby, Emerald or Amethyst"),
 "BTN": dict(line="One line of colour at the base of the neck.", body="A tennis necklace of rectangular baguettes set crosswise, side by side, each held at its corners by gold claws, closed with a box clasp. About 5mm wide, it sits close at the base of the neck. In deep Ruby, clear Crystal or Emerald.",
             stones="Baguette-cut cubic zirconia: Ruby, Crystal or Emerald"),
 "BHG": dict(line="A small hoop of colour.", body="Gold huggie hoops with one row of baguettes standing crosswise along the lower front, the upper half plain polished gold. Hinged snap closure. In Ruby, Crystal, Emerald or Amethyst.",
             stones="Baguette-cut cubic zirconia: Ruby, Crystal, Emerald or Amethyst"),
}
W2 = {q["key"] for q in json.load(open(f"{H}/queue2.json"))}
for p in P:
    p.update(OVR.get(p["id"], {}))
    g = p["gallery"]
    for k in list(g):
        if k.endswith("_W1") and k[:-1] + "2" in W2: g.insert(g.index(k) + 1, k[:-1] + "2")
    if p["id"] in ("C1", "C2"): g.insert(2, "C12_W2")
json.dump(dict(products=P, live=LIVE), open(f"{H}/products.json", "w"), indent=1, ensure_ascii=False)
json.dump(M, open(f"{H}/meta.json", "w"), indent=1, ensure_ascii=False)
nv = sum(max(1, len(p["variants"])) for p in P)
print(len(P), "products,", nv, "variants;", len(LIVE), "live updates")
