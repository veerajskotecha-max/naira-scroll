# Copy for every performance ad, one entry per passed frame -> copy.json (read by perf_ads.py) and meta.csv (the upload sheet).
# Each frame makes a 4:5 Feed ad and a 9:16 Story ad. The overlay follows the format that sold:
#   rhyme, play -> deck  ("Almost edible." / "Sweet On You.": capitals headline, italic correction, spec, CTA, price)
#   silk, worn  -> note  ("The gold note.": italic headline, two roman lines, name · price)
#   quiet       -> quiet (the Apricot camp: wordmark above, name and price below)
# A rhyme frame's Story runs with no text, as the 2.94× fruit-plate Story did; its words are in the primary text.
# Product truth: gold tone / silver tone, cubic zirconia, white shell pearl. Never "real", "diamond", "waterproof", "tarnish-free".
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))

P = {   # handle: (name, price, the noun the CTA uses)
    "toggle-link-chain": ("Toggle Link Chain", "₹1,299", "necklace"),
    "prism-riviere-bracelet": ("Prism Rivière Bracelet", "₹2,399", "bracelet"),
    "woven-gold-hoops": ("Woven Gold Hoops", "₹1,299", "hoops"),
    "heartbead-bracelet": ("Heartbead Bracelet", "₹1,299", "bracelet"),
    "brushed-gold-huggies": ("Brushed Gold Huggies", "₹999", "huggies"),
    "ribbon-bead-bracelet": ("Ribbon Bead Bracelet", "₹799", "bracelet"),
    "riviere-eternal-bracelet": ("Rivière Eternal Bracelet", "₹1,449", "bracelet"),
    "baguette-tennis-necklace": ("Baguette Tennis Necklace", "₹2,300", "necklace"),
    "baguette-tennis-bracelet": ("Baguette Tennis Bracelet", "₹1,699", "bracelet"),
    "baguette-huggies": ("Baguette Huggies", "₹1,199", "huggies"),
    "cushion-halo-ring": ("Cushion Halo Ring", "₹1,199", "ring"),
    "verdant-eternity-band": ("Verdant Eternity Band", "₹1,099", "ring"),
    "halo-curve-ring": ("Halo Curve Ring", "₹1,299", "ring"),
    "lilac-papillon-ring": ("Lilac Papillon Ring", "₹1,299", "ring"),
    "bold-nocturne-chain": ("Bold Nocturne Chain", "₹1,799", "chain"),
    "bold-nocturne-bracelet": ("Bold Nocturne Bracelet", "₹1,599", "bracelet"),
    "marquise-layering-set": ("Marquise Layering Set", "₹1,599", "set"),
    "silk-mesh-cuff": ("Silk Mesh Cuff", "₹1,499", "cuff"),
    "kiss-knot-bangle": ("Kiss Knot Bangle", "₹1,199", "bangle"),
    "molten-panel-bracelet": ("Molten Panel Bracelet", "₹1,299", "bracelet"),
    "torsade-pearl-cuff": ("Torsade Pearl Cuff", "₹1,399", "cuff"),
    "bold-dome-huggies": ("Bold Dome Huggies", "₹999", "huggies"),
    "quatrefoil-eclat-studs": ("Quatrefoil Éclat Studs", "₹1,299", "studs"),
    "verdant-cushion-studs": ("Verdant Cushion Studs", "₹1,199", "studs"),
    "baguette-halo-drops": ("Baguette Halo Drops", "₹1,499", "earrings"),
    "pearl-circlet-studs": ("Pearl Circlet Studs", "₹1,899", "studs"),
    "prism-cluster-studs-silver": ("Prism Cluster Studs", "₹1,499", "studs"),
    "aqua-heart-drops-silver": ("Aqua Heart Drops", "₹1,499", "earrings"),
}
OFFER = ("Take 2 pieces for 10% off, or 3 for 20% off, applied in your bag. "
         "Free insured shipping and cash on delivery across India.")

F = []   # (handle, format, overlay fields, meta fields)
def rhyme(k, h, c, spec, pt, variant=None, **kw): F.append((k, "rhyme", dict(layout="deck", h=h, c=c, spec=spec, **kw), dict(pt=pt, variant=variant)))
def play(k, h, c, spec, pt, variant=None, **kw): F.append((k, "play", dict(layout="deck", h=h, c=c, spec=spec, **kw), dict(pt=pt, variant=variant)))
def silk(k, h, c, pt, variant=None, **kw): F.append((k, "silk", dict(layout="note", h=h, c=c, **kw), dict(pt=pt, variant=variant)))
def worn(k, h, c, pt, variant=None, **kw): F.append((k, "worn", dict(layout="note", h=h, c=c, **kw), dict(pt=pt, variant=variant)))
def quiet(k, pt, variant=None, **kw): F.append((k, "quiet", dict(layout="quiet", **kw), dict(pt=pt, variant=variant)))

# ---- Baguette Tennis Necklace: 36 cm choker, one line of baguettes set crosswise, box clasp; Crystal, Ruby, Emerald
rhyme("baguette-tennis-necklace", "Hot stuff.", "ruby-red cubic zirconia, not chillies.", "Baguette Tennis Necklace · 36 cm · 18k gold-tone",
      "Hot stuff. 🌶️ One line of ruby-red baguette cubic zirconia, set crosswise in 18k gold-tone claws. The Baguette Tennis Necklace, ₹2,300.", "Ruby")
silk("baguette-tennis-necklace", "The green note.", "Emerald-green baguettes,<br>one line, gold-tone claws.",
     "The green note. Emerald-green baguette cubic zirconia, edge to edge on a 36 cm choker line. The Baguette Tennis Necklace, ₹2,300.", "Emerald")
worn("baguette-tennis-necklace", "Undone, done.", "One line of clear baguettes<br>for an open collar.",
     "Undone, done. One line of clear baguette cubic zirconia that sits right at the base of the neck. The Baguette Tennis Necklace, ₹2,300.", "Crystal")
quiet("baguette-tennis-necklace", "Clear baguettes, set crosswise in 18k gold-tone claws, all the way round. The Baguette Tennis Necklace, ₹2,300.", "Crystal")
play("baguette-tennis-necklace", "Matka, dressed.", "even the pot wanted one.", "Baguette Tennis Necklace · 36 cm · 18k gold-tone",
     "Matka, dressed. Clear baguette cubic zirconia on a 36 cm choker line, in 18k gold tone. The Baguette Tennis Necklace, ₹2,300.", "Crystal", reserve=True)

# ---- Baguette Tennis Bracelet: 17 cm, baguettes set crosswise, box clasp with safety tongue
rhyme("baguette-tennis-bracelet", "On the rocks.", "clear cubic zirconia, not ice.", "Baguette Tennis Bracelet · 17 cm · 18k gold-tone",
      "On the rocks. 🧊 Clear baguette cubic zirconia, lined up edge to edge in 18k gold-tone claws. The Baguette Tennis Bracelet, ₹1,699.", "Crystal")
silk("baguette-tennis-bracelet", "The red note.", "Ruby-red baguettes,<br>gold-tone claws.",
     "The red note. Ruby-red baguette cubic zirconia, set crosswise in 18k gold-tone claws. The Baguette Tennis Bracelet, ₹1,699.", "Ruby")
worn("baguette-tennis-bracelet", "Green, every day.", "Emerald-green baguettes<br>for a mulmul morning.",
     "Green, every day. Emerald-green baguette cubic zirconia on a 17 cm line, for the wrist you actually use. The Baguette Tennis Bracelet, ₹1,699.", "Emerald")
quiet("baguette-tennis-bracelet", "Emerald-green baguette cubic zirconia in 18k gold-tone claws. The Baguette Tennis Bracelet, ₹1,699.", "Emerald")
play("baguette-tennis-bracelet", "Love, all.", "the tennis bracelet, taken literally.", "Baguette Tennis Bracelet · 17 cm · 18k gold-tone",
     "Love, all. 🎾 The tennis bracelet, taken literally: clear baguette cubic zirconia, edge to edge in 18k gold-tone claws. ₹1,699.", "Crystal")

# ---- Baguette Huggies: 15 mm, hinged snap, 7 baguettes across the front; Ruby, Crystal, Emerald, Amethyst
rhyme("baguette-huggies", "Two peas.", "emerald cubic zirconia, not matar.", "Baguette Huggies · 15 mm · hinged · 18k gold-tone",
      "Two peas. 🫛 Emerald-green baguette cubic zirconia across the front of a 15 mm hinged huggie, in 18k gold tone. The Baguette Huggies, ₹1,199.", "Emerald")
silk("baguette-huggies", "The clear note.", "Seven baguettes across the front,<br>hinged to close.",
     "The clear note. Seven clear baguettes across the front of a 15 mm huggie that snaps shut. The Baguette Huggies, ₹1,199.", "Crystal")
worn("baguette-huggies", "A little red.", "Ruby baguettes,<br>small enough for every day.",
     "A little red. Ruby-red baguette cubic zirconia on a 15 mm huggie, small enough to sleep in. The Baguette Huggies, ₹1,199.", "Ruby")
quiet("baguette-huggies", "Amethyst-purple baguette cubic zirconia on a 15 mm hinged huggie. Also in Ruby, Crystal and Emerald. The Baguette Huggies, ₹1,199.", "Amethyst")
play("baguette-huggies", "Click. Locked.", "a hinged huggie that snaps shut.", "Baguette Huggies · 15 mm · hinged · 18k gold-tone",
     "Click. Locked. 🔒 A 15 mm hinged huggie with seven clear baguettes across the front, in 18k gold tone. The Baguette Huggies, ₹1,199.", "Crystal")

# ---- Cushion Halo Ring: 8 mm round centre in 4 claws, cushion halo, pavé shoulders, rhodium silver tone
rhyme("cushion-halo-ring", "Spot the odd one.", "cubic zirconia among the sabudana.", "Cushion Halo Ring · 8 mm centre · silver tone",
      "Spot the odd one. An 8 mm round cubic zirconia in a cushion halo, pavé down the shoulders, in rhodium silver tone. The Cushion Halo Ring, ₹1,199.")
silk("cushion-halo-ring", "The midnight note.", "A round centre in a cushion halo,<br>pavé down the shoulders.",
     "The midnight note. An 8 mm round cubic zirconia, a cushion halo and pavé shoulders, in rhodium silver tone. The Cushion Halo Ring, ₹1,199.", tone="cream")
worn("cushion-halo-ring", "Say yes to yourself.", "A cushion halo for the right hand.",
     "Say yes to yourself. 💍 An 8 mm round cubic zirconia in a cushion halo, for no occasion at all. The Cushion Halo Ring, ₹1,199.")
quiet("cushion-halo-ring", "An 8 mm round cubic zirconia in a cushion halo, rhodium silver tone. The Cushion Halo Ring, ₹1,199.")
play("cushion-halo-ring", "The centre.", "8 mm of cubic zirconia, measured.", "Cushion Halo Ring · cushion halo · silver tone",
     "The centre: 8 mm of round cubic zirconia, measured, then framed in a cushion halo. Rhodium silver tone. The Cushion Halo Ring, ₹1,199.")

# ---- Verdant Eternity Band: oval emerald-green cubic zirconia along a wave of pavé, open adjustable back, rhodium silver tone
rhyme("verdant-eternity-band", "Meetha paan.", "emerald-green cubic zirconia, no supari.", "Verdant Eternity Band · adjustable · silver tone",
      "Meetha paan. 🍃 Emerald-green oval cubic zirconia along a wave of pavé, in rhodium silver tone. The Verdant Eternity Band, ₹1,099.")
silk("verdant-eternity-band", "Green, all the way round.", "Emerald-green ovals in a wave of pavé,<br>open at the back to fit.",
     "Green, all the way round. Emerald-green ovals in a wave of pavé, with an open back that adjusts to fit. The Verdant Eternity Band, ₹1,099.", tone="cream")
worn("verdant-eternity-band", "One green thing.", "Emerald-green ovals,<br>adjustable to your finger.",
     "One green thing. Emerald-green oval cubic zirconia in rhodium silver tone, open at the back to fit. The Verdant Eternity Band, ₹1,099.")
quiet("verdant-eternity-band", "Emerald-green ovals along a wave of pavé, rhodium silver tone, adjustable. The Verdant Eternity Band, ₹1,099.")
play("verdant-eternity-band", "Ladyfinger, ringed.", "the eternity band on a bhindi.", "Verdant Eternity Band · adjustable · silver tone",
     "Ladyfinger, ringed. 💚 Emerald-green ovals along a wave of pavé, open at the back to fit any finger, even this one. The Verdant Eternity Band, ₹1,099.")

# ---- Bold Nocturne Chain: 46 cm, chunky oval links, one pavé link at the front, lobster clasp + 5 cm extender
rhyme("bold-nocturne-chain", "Raisin the bar.", "chunky gold-tone links, not kishmish.", "Bold Nocturne Chain · 46 cm · one pavé link",
      "Raisin the bar. Chunky 18k gold-tone links and one link set all over in pavé. The Bold Nocturne Chain, ₹1,799.")
silk("bold-nocturne-chain", "The bold note.", "Chunky gold-tone links<br>and one link in pavé.",
     "The bold note. Chunky polished links in 18k gold tone, with one link set in pavé at the front. The Bold Nocturne Chain, ₹1,799.")
worn("bold-nocturne-chain", "After dark.", "Chunky links, one in pavé,<br>right at the centre.",
     "After dark. 46 cm of chunky 18k gold-tone links, one set in pavé, with a 5 cm extender. The Bold Nocturne Chain, ₹1,799.")
quiet("bold-nocturne-chain", "Chunky 18k gold-tone links and one pavé link. The Bold Nocturne Chain, ₹1,799.")
play("bold-nocturne-chain", "Worth its weight.", "46 cm of chunky gold-tone links.", "Bold Nocturne Chain · 46 cm · one pavé link",
     "Worth its weight. 46 cm of chunky 18k gold-tone links, with one link set in pavé. The Bold Nocturne Chain, ₹1,799.")

# ---- Bold Nocturne Bracelet: 20 cm + 3 cm extender, chunky oval links, one pavé link
rhyme("bold-nocturne-bracelet", "Varq, but wearable.", "gold-tone links, not kaju katli.", "Bold Nocturne Bracelet · 20 cm · one pavé link",
      "Varq, but wearable. ✨ Chunky 18k gold-tone links and one link set in pavé. The Bold Nocturne Bracelet, ₹1,599.")
worn("bold-nocturne-bracelet", "Cuff, rolled.", "Chunky links<br>and one in pavé.",
     "Cuff, rolled. Chunky 18k gold-tone links on a 20 cm bracelet with a 3 cm extender, one link set in pavé. The Bold Nocturne Bracelet, ₹1,599.")
quiet("bold-nocturne-bracelet", "Chunky 18k gold-tone links, one in pavé. The Bold Nocturne Bracelet, ₹1,599.")
play("bold-nocturne-bracelet", "Measure twice.", "20 cm of chunky links, one in pavé.", "Bold Nocturne Bracelet · 20 cm · 18k gold-tone",
     "Measure twice. 20 cm of chunky 18k gold-tone links, plus a 3 cm extender. The Bold Nocturne Bracelet, ₹1,599.", reserve=True)

# ---- Marquise Layering Set: two fine necklaces, 40 cm marquise solitaire + 45 cm Y-lariat with marquise stations and a pear drop
worn("marquise-layering-set", "Layered, already.", "Two necklaces, one set:<br>a marquise and a Y-drop.",
     "Layered, already. A 40 cm marquise solitaire and a 45 cm Y-lariat, made to be worn together. The Marquise Layering Set, ₹1,599.")
play("marquise-layering-set", "Hangs true.", "two necklaces, layered to the line.", "Marquise Layering Set · 40 + 45 cm · 18k gold-tone",
     "Hangs true. Two fine necklaces in 18k gold tone, a marquise solitaire and a Y-lariat, layered for you. The Marquise Layering Set, ₹1,599.")

# ---- Silk Mesh Cuff: 19 mm woven mesh tube, polished oval end caps; Gold, Silver
rhyme("silk-mesh-cuff", "Ghevar, gilded.", "woven gold-tone mesh, not syrup.", "Silk Mesh Cuff · 19 mm mesh · gold or silver",
      "Ghevar, gilded. A 19 mm tube of fine woven mesh with mirror-polished end caps. In gold tone or silver tone. The Silk Mesh Cuff, ₹1,499.", "Gold")
silk("silk-mesh-cuff", "The silver note.", "Woven mesh, soft as cloth,<br>polished at the ends.",
     "The silver note. Fine woven steel mesh that moves like cloth, closed by two polished caps. The Silk Mesh Cuff, ₹1,499.", "Silver", tone="cream")
worn("silk-mesh-cuff", "Soft, but gold.", "Woven mesh that bends<br>like fabric on the wrist.",
     "Soft, but gold. Woven 18k gold-tone mesh that bends like fabric, open at the side to slip on. The Silk Mesh Cuff, ₹1,499.", "Gold")
quiet("silk-mesh-cuff", "Fine woven mesh in silver tone, polished oval end caps. Also in gold tone. The Silk Mesh Cuff, ₹1,499.", "Silver")
play("silk-mesh-cuff", "Strained, in a good way.", "the same weave as your chai strainer.", "Silk Mesh Cuff · 19 mm mesh · gold or silver",
     "Strained, in a good way. ☕ The same fine weave as your chai strainer, rolled into a cuff. In silver tone or gold tone. The Silk Mesh Cuff, ₹1,499.", "Silver")

# ---- Kiss Knot Bangle: flexible ribbed tubogas, ends crossed in one polished X; Gold, Silver
rhyme("kiss-knot-bangle", "Coiled, not fried.", "gold-tone tubogas, not murukku.", "Kiss Knot Bangle · flexible · gold or silver",
      "Coiled, not fried. A flexible ribbed bangle whose ends cross in one polished X. The Kiss Knot Bangle, ₹1,199.", "Gold")
silk("kiss-knot-bangle", "Sealed with an X.", "Ribbed silver-tone coil,<br>crossed like a kiss.",
     "Sealed with an X. 💋 A flexible ribbed bangle in silver tone, its ends crossed in one polished X. The Kiss Knot Bangle, ₹1,199.", "Silver", tone="cream")
worn("kiss-knot-bangle", "X marks the wrist.", "A flexible coil<br>that gives as you move.",
     "X marks the wrist. A flexible ribbed coil that gives as you move, crossed at the front. The Kiss Knot Bangle, ₹1,199.", "Silver")
quiet("kiss-knot-bangle", "A flexible ribbed coil in 18k gold tone, crossed in one polished X. Also in silver tone. The Kiss Knot Bangle, ₹1,199.", "Gold")
play("kiss-knot-bangle", "Zari, but solid.", "a coil you can wear.", "Kiss Knot Bangle · flexible · gold or silver",
     "Zari, but solid. A flexible ribbed coil in 18k gold tone, its ends crossed in one polished X. The Kiss Knot Bangle, ₹1,199.", "Gold")

# ---- Molten Panel Bracelet: 17 cm flat band of small oval plates in 5 staggered rows, box clasp
rhyme("molten-panel-bracelet", "Bhutta, polished.", "gold-tone plates, not kernels.", "Molten Panel Bracelet · 17 cm · 18k gold-tone",
      "Bhutta, polished. 🌽 Small oval plates laid in rows like kernels, in satin-polished 18k gold tone. The Molten Panel Bracelet, ₹1,299.")
silk("molten-panel-bracelet", "The molten note.", "Rows of small gold-tone plates<br>that drape like a strap.",
     "The molten note. Rows of small oval plates that drape like a watch strap, closed by a flat box clasp. The Molten Panel Bracelet, ₹1,299.")
worn("molten-panel-bracelet", "Poured on.", "A flat band of gold-tone plates<br>that moves with the wrist.",
     "Poured on. A flat 17 cm band of small 18k gold-tone plates that moves with the wrist. The Molten Panel Bracelet, ₹1,299.")
quiet("molten-panel-bracelet", "Rows of small oval plates in 18k gold tone, flat box clasp. The Molten Panel Bracelet, ₹1,299.")
play("molten-panel-bracelet", "It bends.", "rows of plates, not one stiff band.", "Molten Panel Bracelet · 17 cm · 18k gold-tone",
     "It bends. Rows of small 18k gold-tone plates, articulated so the band drapes. The Molten Panel Bracelet, ₹1,299.", reserve=True)

# ---- Torsade Pearl Cuff: twisted cable cuff, pavé collars, two 12 mm white shell pearls facing across the opening
rhyme("torsade-pearl-cuff", "Makhana, but forever.", "white shell pearls, not fox nuts.", "Torsade Pearl Cuff · shell pearls · 18k gold-tone",
      "Makhana, but forever. Two white shell pearls at the ends of a twisted 18k gold-tone cuff, with pavé collars. The Torsade Pearl Cuff, ₹1,399.")
silk("torsade-pearl-cuff", "The pearl note.", "Twisted gold-tone cable,<br>a white shell pearl at each end.",
     "The pearl note. A twisted cable cuff in 18k gold tone, a white shell pearl at each end in a pavé collar. The Torsade Pearl Cuff, ₹1,399.")
worn("torsade-pearl-cuff", "Two pearls, one wrist.", "Twisted cable that opens<br>to slip on.",
     "Two pearls, one wrist. A twisted 18k gold-tone cuff, open at the back to slip on, a white shell pearl at each end. The Torsade Pearl Cuff, ₹1,399.")
quiet("torsade-pearl-cuff", "Twisted 18k gold-tone cable, a white shell pearl at each end. The Torsade Pearl Cuff, ₹1,399.")
play("torsade-pearl-cuff", "Twice as nice.", "one cuff, and the mirror's opinion.", "Torsade Pearl Cuff · shell pearls · 18k gold-tone",
     "Twice as nice. One twisted gold-tone cuff, two white shell pearls, and the mirror agrees. The Torsade Pearl Cuff, ₹1,399.")

def shots():
    """copy space and the jewellery's vertical extent per plate, from the shoot manifests"""
    out = {}
    for g in ("g1", "g2", "g3", "g4"):
        p = f"{HERE}/shots_{g}.json"
        if os.path.exists(p):
            for s in json.load(open(p)):
                if s.get("pass") or s.get("file"): out[f"{s['key']}-{s['format']}"] = s
    return out

def build():
    frames, rows = [], []; S = shots()
    for k, fmt, ov, meta in F:
        name, price, noun = P[k]; plate = f"plates/{k}-{fmt}.jpg"
        if not os.path.exists(os.path.join(HERE, "..", plate)): continue
        e = dict(plate=plate, **{x: y for x, y in ov.items() if x != "reserve"})
        s = S.get(f"{k}-{fmt}", {}); lay = ov["layout"]
        if s.get("subject_y") and "cy" not in e: e["cy"] = round(min(max(sum(s["subject_y"]) / 2, .36), .64), 3)
        if s.get("copy_space") in ("tl", "tr", "bl", "br") and "at" not in e: e["at"] = s["copy_space"]
        if s.get("tone") == "dark" and "tone" not in e: e["tone"] = "cream"
        if s.get("subject_y"): e["sy"] = s["subject_y"]
        if e.get("spec", "").startswith(name + " · "): e["spec"] = e["spec"][len(name) + 3:]          # the Meta headline carries the name
        if lay == "deck": e.update(cta=f"Shop the {noun}", price=price, at=e.get("at", "tl"), w=e.get("w", 640), hs=e.get("hs", 96), cs=e.get("cs", 38))
        if lay == "note": e.update(n=f"{name} · {price}", at=e.get("at", "tl"), w=e.get("w", 600), hs=e.get("hs", 78), cs=e.get("cs", 34), ns=e.get("ns", 18))
        if lay == "quiet": e.update(name=name, price=price)
        frames.append(e)
        for tag in ("feed", "story"):
            rows.append(dict(ad=f"{k}-{fmt}-{tag}", product=name, format=fmt, placement=tag, variant=meta.get("variant") or "",
                             reserve="yes" if ov.get("reserve") else "", primary_text=f"{meta['pt']}\n\n{OFFER}",
                             headline=f"{name} · {price}", cta="SHOP_NOW", url=f"https://nairaflore.com/products/{k}"))
    json.dump({"frames": frames}, open(f"{HERE}/copy.json", "w"), ensure_ascii=False, indent=1)
    with open(f"{HERE}/meta.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(len(frames), "frames,", len(rows), "ads")

if __name__ == "__main__":
    build()
