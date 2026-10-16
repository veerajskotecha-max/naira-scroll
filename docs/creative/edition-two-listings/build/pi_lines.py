# The 59 lines of the Yiss Fera PI (Sept 2026) and the product/variant each one became; checks every line is covered.
import json, os
H = os.path.dirname(os.path.abspath(__file__))
L = [(1,"YF3608","Tubogas ring, gold, sizes 6–8",9,3.18),(2,"YF3608","Tubogas ring, silver, sizes 6–8",9,3.18),(3,"YF5244","Tassel necklace, gold",20,3.05),
(4,"YF5244","Big zircon necklace, gold",20,2.22),(5,"YF7085","Tennis bracelet, white",30,3.65),(6,"YF3482","Mesh cuff, gold",20,3.95),(7,"YF3482","Mesh cuff, silver",20,3.95),
(8,"YF7116","Thin tennis bracelet, gold",20,3.25),(9,"YF7126","Flower studs, silver",10,2.65),(10,"YF7126","Flower studs, gold",10,2.65),(11,"YF4152","Knot bangle, gold",20,3.20),
(12,"YF4152","Knot bangle, silver",20,3.20),(13,"YF3791","Drop ring, gold",10,3.73),(14,"YF3791","Drop cuff bracelet, gold",10,5.21),(15,"YF3791","Drop ring, silver",10,3.48),
(16,"YF3791","Drop cuff bracelet, silver",10,4.68),(17,"YF2931","Roman numeral ring, sizes 6–8",9,5.15),(18,"YF7034","Green pear drop earrings",20,2.91),
(19,"YF7016","Linked ring, gold, sizes 6–8",9,3.28),(20,"YF7016","Linked ring, silver, sizes 6–8",9,3.28),(21,"YF3165","Baguette necklace, gold-white",30,5.95),
(22,"YF3165","Baguette bracelet, gold-white",30,4.15),(23,"YF3165","Baguette necklace, gold-red",20,5.95),(24,"YF3165","Baguette bracelet, gold-red",20,4.15),
(25,"YF3165","Baguette necklace, gold-green",20,5.95),(26,"YF3165","Baguette bracelet, gold-green",20,4.15),(27,"YF2604","Baguette eternity ring, white, sizes 6–8",9,5.65),
(28,"YF8086","Chain drop ring, gold, sizes 6–8",9,2.54),(29,"YF8086","Chain drop ring, silver, sizes 6–8",9,2.54),(30,"YF2645","Watch link ring, gold, sizes 6–8",9,2.27),
(31,"YF2645","Watch link ring, silver, sizes 6–8",9,2.27),(32,"YF3652","Ear cuff, white waterdrop",20,2.72),(33,"YF3652","Ear cuff, green square",20,2.72),
(34,"YF3508","Marquise cuff, gold",20,4.52),(35,"YF7059","Omega drop necklace",20,3.15),(36,"YF3558","Mesh ring, gold, sizes 6–8",9,1.68),(37,"YF3558","Mesh ring, silver, sizes 6–8",9,1.68),
(38,"YF8079","Two-tone link necklace",20,3.65),(39,"YF8079","Two-tone link bracelet",20,2.45),(40,"YF3937","Three-layer coil, gold",10,4.15),(41,"YF3937","Three-layer coil, silver",10,3.51),
(42,"YF8156","Bow bracelet",20,2.23),(43,"YF3925","Baroque pearl bracelet, gold",10,10.00),(44,"YF5144","Pavé link necklace, gold",30,7.35),(45,"YF5144","Pavé link bracelet, gold",30,4.95),
(46,"YF5144","Pavé link earrings, gold",30,4.35),(47,"YF8453","Tiger eye stone ring",20,3.11),(48,"YF5214","Star band ring, gold, sizes 6–8",9,2.38),(49,"YF5214","Star band ring, silver, sizes 6–8",9,2.29),
(50,"YF5204","Star bangle, gold",10,2.30),(51,"YF5204","Star bangle, silver",10,2.18),(52,"YF8221","Pear open cuff",20,4.62),(53,"YF3923","Baguette huggies, gold-white",15,3.19),
(54,"YF3923","Baguette huggies, gold-red",15,3.19),(55,"YF3923","Baguette huggies, gold-green",15,3.19),(56,"YF3923","Baguette huggies, gold-purple",15,3.19),
(57,"YF3143","Baguette band, gold-purple, sizes 6–8",9,2.98),(58,"YF3143","Baguette band, gold-red, sizes 6–8",9,2.98),(59,"YF3143","Baguette band, gold-green, sizes 6–8",9,2.98)]
D = json.load(open(f"{H}/products.json")); cover = {}
for p in D["products"]:
    for v in p["variants"]:
        if v["pi_line"]: cover.setdefault(v["pi_line"], set()).add(p["title"] + (" — " + v["options"][0] if v["options"] else ""))
for l in D["live"]:
    for n in l["lines"]: cover.setdefault(n, set()).add(l["title"] + " (live)")
rows = [dict(line=n, code=c, desc=d, qty=q, usd=u, to=sorted(cover.get(n, []))) for n, c, d, q, u in L]
json.dump(rows, open(f"{H}/pi_lines.json", "w"), indent=1, ensure_ascii=False)
print("uncovered:", [r["line"] for r in rows if not r["to"]], "| pcs", sum(r["qty"] for r in rows), "| USD", round(sum(r["qty"] * r["usd"] for r in rows), 2))
