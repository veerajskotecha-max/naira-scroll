import json, sys
FIX = {
 "Silk Mesh Cuff, Gold — macro detail: fine woven mesh tube with polished oval end caps, silver tone":
 "Silk Mesh Cuff, Gold — macro detail: fine woven mesh tube with polished oval end caps, gold tone",
 "Droplet Open Ring, Gold — macro detail: polished ball and teardrop ends, silver tone":
 "Droplet Open Ring, Gold — macro detail: polished ball and teardrop ends, gold tone",
 "Kiss Knot Bangle, Gold — macro detail: polished X binding the ribbed silver coil":
 "Kiss Knot Bangle, Gold — macro detail: polished X binding the ribbed gold coil",
 "Emerald Square Ear Cuff — worn, close detail":
 "Emerald Square Ear Cuff — worn on the ear with the Crystal Pear Ear Cuff above it, close detail",
 "Crystal Pear Ear Cuff — worn, close detail":
 "Crystal Pear Ear Cuff — worn on the ear above the Emerald Square Ear Cuff, close detail",
}
FIX.update({
 "Baguette Eternity Band, Emerald — macro detail: crosswise ruby baguettes around the band":
 "Baguette Eternity Band, Emerald — macro detail: crosswise emerald green baguettes around the band",
 "Baguette Tennis Bracelet, Ruby — macro detail: crosswise clear baguettes in slim gold box settings":
 "Baguette Tennis Bracelet, Ruby — macro detail: crosswise ruby red baguettes in slim gold box settings",
 "Baguette Tennis Bracelet, Emerald — macro detail: crosswise clear baguettes in slim gold box settings":
 "Baguette Tennis Bracelet, Emerald — macro detail: crosswise emerald green baguettes in slim gold box settings",
})
for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    n = 0
    for a, b in FIX.items():
        for enc in (a, json.dumps(a)[1:-1]):
            if enc in s:
                n += s.count(enc); s = s.replace(enc, b if enc == a else json.dumps(b)[1:-1])
    open(path, "w", encoding="utf-8").write(s)
    print(path, n, "replacements")
