# Copy for every performance ad, one entry per passed frame -> copy.json (read by perf_ads.py) and meta.csv (the upload sheet).
# Each frame makes a 4:5 Feed ad and a 9:16 Story ad. The overlay follows the format that sold:
#   rhyme, play -> deck  ("Almost edible." / "Sweet On You.": capitals headline, italic correction, spec, CTA, price)
#   silk, worn  -> note  ("The gold note.": italic headline, two roman lines, name · price)
#   quiet       -> quiet (the Apricot camp: wordmark above, name and price below)
# A rhyme frame's Story runs with no text, as the 2.94× fruit-plate Story did; its words are in the primary text.
# Product truth: gold tone / silver tone, cubic zirconia, white shell pearl. Never "real", "diamond", "waterproof", "tarnish-free".
import csv, json, os, re
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
OFFER = ("Take 2 pieces for 10% off or 3 for 20% off, with codes BUY2 and BUY3 at checkout. "
         "Free insured shipping and cash on delivery across India.")
STOCK = {"toggle-link-chain": 80, "baguette-tennis-necklace": 70, "prism-riviere-bracelet": 67, "baguette-tennis-bracelet": 64,
         "woven-gold-hoops": 63, "cushion-halo-ring": 60, "verdant-eternity-band": 60, "baguette-huggies": 58, "bold-nocturne-chain": 54,
         "bold-nocturne-bracelet": 50, "halo-curve-ring": 45, "marquise-layering-set": 40, "silk-mesh-cuff": 40, "kiss-knot-bangle": 40,
         "brushed-gold-huggies": 35, "ribbon-bead-bracelet": 35, "riviere-eternal-bracelet": 34, "bold-dome-huggies": 30,
         "quatrefoil-eclat-studs": 30, "verdant-cushion-studs": 30, "baguette-halo-drops": 30, "pearl-circlet-studs": 30,
         "torsade-pearl-cuff": 30, "molten-panel-bracelet": 30, "prism-cluster-studs-silver": 30, "aqua-heart-drops-silver": 30,
         "lilac-papillon-ring": 30, "heartbead-bracelet": 25}     # live Shopify stock, 22 Oct 2026
VARIANT = {("silk-mesh-cuff", "Gold"): 50651894546594, ("silk-mesh-cuff", "Silver"): 50651894579362,
           ("baguette-tennis-bracelet", "Crystal"): 50651931738274, ("baguette-tennis-bracelet", "Ruby"): 50651931771042,
           ("baguette-tennis-bracelet", "Emerald"): 50651931803810, ("kiss-knot-bangle", "Gold"): 50651938881698,
           ("kiss-knot-bangle", "Silver"): 50651938914466, ("baguette-tennis-necklace", "Ruby"): 50651962409122,
           ("baguette-tennis-necklace", "Crystal"): 50651962441890, ("baguette-tennis-necklace", "Emerald"): 50651962474658,
           ("baguette-huggies", "Ruby"): 50651968929954, ("baguette-huggies", "Crystal"): 50651968962722,
           ("baguette-huggies", "Emerald"): 50651968995490, ("baguette-huggies", "Amethyst"): 50651969028258}
EARRINGS = {"woven-gold-hoops", "brushed-gold-huggies", "baguette-huggies", "bold-dome-huggies", "quatrefoil-eclat-studs",
            "verdant-cushion-studs", "baguette-halo-drops", "pearl-circlet-studs", "prism-cluster-studs-silver", "aqua-heart-drops-silver"}
NECK_RINGS = {"toggle-link-chain", "baguette-tennis-necklace", "bold-nocturne-chain", "marquise-layering-set", "cushion-halo-ring",
              "verdant-eternity-band", "halo-curve-ring", "lilac-papillon-ring"}
# Campaigns: one per overlay family (the thing under test); ad sets by category; five ads live per ad set, the rest wait in waves.
CAMPAIGN = {"rhyme": "PERF · Rhyme (fruit-plate / Almost edible) · Oct 2026", "play": "PERF · Play (object wit) · Oct 2026",
            "silk": "PERF · Silk & Worn (gold note) · Oct 2026", "worn": "PERF · Silk & Worn (gold note) · Oct 2026",
            "quiet": "PERF · Quiet · retarget warm · Oct 2026"}
HOLD = {"pearl-circlet-studs"}   # listing copy says gold tone, every photo shows silver tone: held until the listing is confirmed
FORMAT_W = {"rhyme": 1.0, "play": .85, "silk": .8, "worn": .8, "quiet": .7}

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
rhyme("bold-nocturne-chain", "Golden, by the handful.", "chunky gold-tone links, not kishmish.", "Bold Nocturne Chain · 46 cm · one pavé link",
      "Golden, by the handful. Chunky 18k gold-tone links and one link set all over in pavé. The Bold Nocturne Chain, ₹1,799.")
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
worn("silk-mesh-cuff", "Soft, but solid.", "Woven mesh that bends<br>like fabric on the wrist.",
     "Soft, but solid. Woven 18k gold-tone mesh that bends like fabric, open at the side to slip on. The Silk Mesh Cuff, ₹1,499.", "Gold")
quiet("silk-mesh-cuff", "Fine woven mesh in silver tone, polished oval end caps. Also in gold tone. The Silk Mesh Cuff, ₹1,499.", "Silver")
play("silk-mesh-cuff", "Strained, in a good way.", "the same weave as your chai strainer.", "Silk Mesh Cuff · 19 mm mesh · gold or silver",
     "Strained, in a good way. ☕ The same fine weave as your chai strainer, rolled into a cuff. In silver tone or gold tone. The Silk Mesh Cuff, ₹1,499.", "Silver")

# ---- Kiss Knot Bangle: flexible ribbed tubogas, ends crossed in one polished X; Gold, Silver
rhyme("kiss-knot-bangle", "Murukku, minus the oil.", "a ribbed gold-tone coil, crossed in an X.", "Kiss Knot Bangle · flexible · gold or silver",
      "Murukku, minus the oil. A flexible ribbed bangle whose ends cross in one polished X. The Kiss Knot Bangle, ₹1,199.", "Gold")
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
quiet("molten-panel-bracelet", "Rows of small oval plates in 18k gold tone, flat box clasp. The Molten Panel Bracelet, ₹1,299.", reserve=True)
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

# ---- Bold Nocturne Bracelet silk (filled on the third attempt)
silk("bold-nocturne-bracelet", "The champagne note.", "Chunky gold-tone links,<br>one of them in pavé.",
     "The champagne note. Chunky 18k gold-tone links on a 20 cm bracelet, one link set all over in pavé. The Bold Nocturne Bracelet, ₹1,599.")

# ---- Toggle Link Chain: 50 cm, 4 mm paperclip links, spring-gate ring and a short pavé bar, worn at the front or the side
rhyme("toggle-link-chain", "Raisin the bar.", "a pavé bar, not a kishmish.", "50 cm · paperclip links · toggle clasp",
      "Raisin the bar. A 50 cm paperclip chain in 18k gold tone that closes with a pavé bar through a ring. The Toggle Link Chain, ₹1,299.")
silk("toggle-link-chain", "The apricot note.", "Paperclip links that close<br>with a turn, not a catch.",
     "The apricot note. Open paperclip links in 18k gold tone, closed with a turn: a pavé bar through a ring. The Toggle Link Chain, ₹1,299.")
worn("toggle-link-chain", "Front or side.", "Wear the toggle where you like;<br>it closes with a turn.",
     "Front or side. A 50 cm paperclip chain whose toggle clasp is the pendant. The Toggle Link Chain, ₹1,299.", reserve=True)
quiet("toggle-link-chain", "Paperclip links and a toggle clasp in 18k gold tone. The Toggle Link Chain, ₹1,299.")
play("toggle-link-chain", "Closes like a kundi.", "a bar through a ring, one turn.", "50 cm · paperclip links · toggle clasp",
     "Closes like a kundi. 🔑 A pavé bar through a ring, the way the old door latch works. 50 cm of 18k gold-tone paperclip chain. The Toggle Link Chain, ₹1,299.")

# ---- Prism Rivière Bracelet: aqua, pink and yellow cushion cubic zirconia, each in a pavé halo, rhodium silver tone, 15-19 cm
rhyme("prism-riviere-bracelet", "After-dinner sparkle.", "pastel cubic zirconia, not mukhwas.", "aqua · pink · yellow · silver tone",
      "After-dinner sparkle. 🍬 Aqua, pink and yellow cubic zirconia, each in its own pavé halo, in rhodium silver tone. The Prism Rivière Bracelet, ₹2,399.")
silk("prism-riviere-bracelet", "The pastel note.", "Aqua, pink and yellow,<br>each in its own halo.",
     "The pastel note. Aqua, pink and yellow cushion cubic zirconia, each framed in pavé, in one straight line. The Prism Rivière Bracelet, ₹2,399.", tone="cream")
worn("prism-riviere-bracelet", "Every colour, one line.", "Aqua, pink and yellow cushions,<br>18 cm, flat on the wrist.",
     "Every colour, one line. Aqua, pink and yellow cubic zirconia in pavé halos, an 18 cm line with a fold-over clasp. The Prism Rivière Bracelet, ₹2,399.")
quiet("prism-riviere-bracelet", "Aqua, pink and yellow cubic zirconia in pavé halos, rhodium silver tone. The Prism Rivière Bracelet, ₹2,399.")
play("prism-riviere-bracelet", "Prism, meet prism.", "the light splits; so does the bracelet.", "aqua · pink · yellow · silver tone",
     "Prism, meet prism. 🌈 Aqua, pink and yellow cubic zirconia in one line, each in a pavé halo. The Prism Rivière Bracelet, ₹2,399.", reserve=True)

# ---- Woven Gold Hoops: 25 mm braided rope hoops, no stones
rhyme("woven-gold-hoops", "Twisted, not fried.", "braided gold-tone hoops, not murukku.", "25 mm · braided · 18k gold-tone",
      "Twisted, not fried. 25 mm hoops of braided rope in 18k gold tone. No stones, all texture. The Woven Gold Hoops, ₹1,299.")
silk("woven-gold-hoops", "The braided note.", "25 mm of braided gold-tone rope,<br>no stones, all texture.",
     "The braided note. 25 mm hoops of braided gold-tone rope that catch the light on every twist. The Woven Gold Hoops, ₹1,299.")
worn("woven-gold-hoops", "Bun day.", "Braided gold-tone hoops,<br>25 mm, close at the lobe.",
     "Bun day. Braided 18k gold-tone hoops, 25 mm, that sit close at the lobe. The Woven Gold Hoops, ₹1,299.")
quiet("woven-gold-hoops", "Braided rope hoops, 25 mm, in 18k gold tone. The Woven Gold Hoops, ₹1,299.")
play("woven-gold-hoops", "Plait, perfected.", "a 25 mm hoop, braided like a plait.", "25 mm · braided · 18k gold-tone",
     "Plait, perfected. Braided like a plait, then closed into a 25 mm hoop. 18k gold tone. The Woven Gold Hoops, ₹1,299.")

# ---- Heartbead Bracelet: 6 mm mirror-polished steel beads, a gold-tone toggle and one puffed gold-tone heart
rhyme("heartbead-bracelet", "Paan, with heart.", "6 mm steel beads, one gold-tone heart.", "6 mm steel beads · gold-tone toggle and heart",
      "Paan, with heart. 💚 6 mm mirror-polished steel beads, a gold-tone toggle and one puffed gold-tone heart. The Heartbead Bracelet, ₹1,299.")
silk("heartbead-bracelet", "Still the gold note.", "Mirror-polished beads,<br>a gold-tone toggle and heart.",
     "Still the gold note. Mirror-polished 6 mm steel beads with a gold-tone toggle and a puffed heart. The Heartbead Bracelet, ₹1,299.", tone="cream")
F.append(("heartbead-bracelet", "worn", dict(layout="deck", h="Sweet on you.", c="the charm bracelet, worn.", spec="6 mm steel beads · gold-tone toggle and heart", at="tc", w=900),
          dict(pt="Sweet on you. ❤️ The charm bracelet: 6 mm mirror-polished steel beads, a gold-tone toggle and one puffed heart. The Heartbead Bracelet, ₹1,299.")))
quiet("heartbead-bracelet", "Mirror-polished steel beads, a gold-tone toggle and heart. The Heartbead Bracelet, ₹1,299.")
play("heartbead-bracelet", "Listen closely.", "surgical steel, both of them.", "6 mm steel beads · gold-tone toggle and heart",
     "Listen closely. 🩺 Mirror-polished surgical steel beads, a gold-tone toggle and one puffed heart. The Heartbead Bracelet, ₹1,299.")

# ---- Brushed Gold Huggies: small satin-brushed gold-tone huggies
rhyme("brushed-gold-huggies", "Kaju, but gold.", "brushed gold-tone huggies, not cashews.", "satin-brushed · 18k gold-tone · huggie hoops",
      "Kaju, but gold. Small huggie hoops with a satin-brushed finish in 18k gold tone. The Brushed Gold Huggies, ₹999.")
silk("brushed-gold-huggies", "The satin note.", "Brushed, not mirrored,<br>so they never shout.",
     "The satin note. Brushed, not mirror-polished, so the gold glows instead of flashing. The Brushed Gold Huggies, ₹999.")
worn("brushed-gold-huggies", "Every day, every ear.", "Brushed gold-tone huggies<br>that sit snug at the lobe.",
     "Every day, every ear. Satin-brushed 18k gold-tone huggies that sit snug at the lobe. The Brushed Gold Huggies, ₹999.")
quiet("brushed-gold-huggies", "Satin-brushed 18k gold-tone huggies. The Brushed Gold Huggies, ₹999.")
play("brushed-gold-huggies", "Brushed, literally.", "a satin finish, not a mirror.", "satin-brushed · 18k gold-tone · huggie hoops",
     "Brushed, literally. A satin-brushed finish on small 18k gold-tone huggies. The Brushed Gold Huggies, ₹999.")

# ---- Ribbon Bead Bracelet: a fine gold-tone chain with a small crystal bow
rhyme("ribbon-bead-bracelet", "A bow, edible.", "a crystal bow, not mithai.", "fine chain · crystal bow · 18k gold-tone",
      "A bow, edible? Not this one. A small crystal bow on a fine 18k gold-tone chain. The Ribbon Bead Bracelet, ₹799.")
silk("ribbon-bead-bracelet", "The bow note.", "A small crystal bow<br>on a fine gold-tone chain.",
     "The bow note. A small crystal bow on a fine 18k gold-tone chain. The Ribbon Bead Bracelet, ₹799.")
worn("ribbon-bead-bracelet", "Tied on.", "A small crystal bow<br>on a fine gold-tone chain.",
     "Tied on. A small crystal bow on a fine 18k gold-tone chain, for ₹799. The Ribbon Bead Bracelet.")
quiet("ribbon-bead-bracelet", "A small crystal bow on a fine 18k gold-tone chain. The Ribbon Bead Bracelet, ₹799.")
play("ribbon-bead-bracelet", "Gift, wrapped.", "the bracelet is the ribbon.", "fine chain · crystal bow · 18k gold-tone",
     "Gift, wrapped. 🎁 The bracelet is the ribbon: a small crystal bow on a fine gold-tone chain, ₹799. The Ribbon Bead Bracelet.")

# ---- Rivière Eternal Bracelet: one fine line of clear cubic zirconia, a polished buckle clasp at the front
rhyme("riviere-eternal-bracelet", "Sabudana, set.", "clear cubic zirconia, not tapioca.", "one line of clear stones · polished buckle",
      "Sabudana, set. One fine line of clear cubic zirconia with a polished buckle clasp. The Rivière Eternal Bracelet, ₹1,449.")
silk("riviere-eternal-bracelet", "The fine note.", "One fine line of clear stones,<br>a polished buckle at the front.",
     "The fine note. One fine line of clear cubic zirconia and a polished buckle at the front. The Rivière Eternal Bracelet, ₹1,449.")
worn("riviere-eternal-bracelet", "One line, all day.", "Clear stones, edge to edge,<br>a buckle on top.",
     "One line, all day. Clear cubic zirconia edge to edge, with a polished buckle clasp. The Rivière Eternal Bracelet, ₹1,449.")
quiet("riviere-eternal-bracelet", "One fine line of clear cubic zirconia. The Rivière Eternal Bracelet, ₹1,449.", reserve=True)
play("riviere-eternal-bracelet", "Game, set, match.", "a tennis bracelet that wraps a ball.", "one line of clear stones · polished buckle",
     "Game, set, match. 🎾 One fine line of clear cubic zirconia, flexible enough to wrap a ball. The Rivière Eternal Bracelet, ₹1,449.")

# ---- Halo Curve Ring: open gold-tone bypass ring ending in a tiger's eye and a champagne crystal
rhyme("halo-curve-ring", "Gur, in gold.", "tiger's eye, not jaggery.", "tiger's eye · champagne crystal · open band",
      "Gur, in gold. A tiger's eye and a champagne crystal, side by side on an open 18k gold-tone band. The Halo Curve Ring, ₹1,299.")
silk("halo-curve-ring", "Two stones, one curve.", "Tiger's eye and champagne crystal<br>on an open gold-tone band.",
     "Two stones, one curve. Tiger's eye and champagne crystal on an open 18k gold-tone band. The Halo Curve Ring, ₹1,299.")
worn("halo-curve-ring", "Point taken.", "Tiger's eye and champagne crystal,<br>side by side.",
     "Point taken. A tiger's eye and a champagne crystal, side by side on an open gold-tone band. The Halo Curve Ring, ₹1,299.")
quiet("halo-curve-ring", "Tiger's eye and champagne crystal on an open 18k gold-tone band. The Halo Curve Ring, ₹1,299.")
play("halo-curve-ring", "Light, and shade.", "one stone lets the sun through; one doesn't.", "tiger's eye · champagne crystal · open band",
     "Light, and shade. ☀️ The crystal lets the sun through; the tiger's eye keeps it. The Halo Curve Ring, ₹1,299.")

# ---- Lilac Papillon Ring: a gold-tone butterfly, its wings in lilac micro-pavé, over an openwork outline in clear stones
rhyme("lilac-papillon-ring", "Butterfly, pea.", "lilac pavé wings, not petals.", "lilac pavé · 18k gold-tone · butterfly",
      "Butterfly, pea. 🦋 A gold-tone butterfly whose wings are set edge to edge in lilac pavé. The Lilac Papillon Ring, ₹1,299.")
silk("lilac-papillon-ring", "The lilac note.", "A gold-tone butterfly,<br>its wings set in lilac pavé.",
     "The lilac note. A gold-tone butterfly with lilac pavé wings, over an outline traced in clear stones. The Lilac Papillon Ring, ₹1,299.")
worn("lilac-papillon-ring", "Landed.", "A gold-tone butterfly<br>in lilac pavé.",
     "Landed. 🦋 A gold-tone butterfly ring, its wings set in lilac pavé. The Lilac Papillon Ring, ₹1,299.")
quiet("lilac-papillon-ring", "A gold-tone butterfly with lilac pavé wings. The Lilac Papillon Ring, ₹1,299.")
play("lilac-papillon-ring", "Butterfly, twice.", "one ring, and its reflection.", "lilac pavé · 18k gold-tone · butterfly",
     "Butterfly, twice. One gold-tone butterfly ring in lilac pavé, and its reflection. The Lilac Papillon Ring, ₹1,299.")

# ---- Bold Dome Huggies: 16 mm chunky polished dome huggies, hinged snap
rhyme("bold-dome-huggies", "Chunky, not crunchy.", "polished gold-tone huggies, not fryums.", "16 mm · hinged · 18k gold-tone",
      "Chunky, not crunchy. 16 mm dome huggies in mirror-polished 18k gold tone, with a hinged snap. The Bold Dome Huggies, ₹999.")
silk("bold-dome-huggies", "The dome note.", "16 mm of polished gold tone,<br>full at the front, slim at the hinge.",
     "The dome note. 16 mm huggies, full at the front and slim at the hinge, in polished 18k gold tone. The Bold Dome Huggies, ₹999.")
worn("bold-dome-huggies", "Small, but loud.", "Chunky 16 mm huggies<br>in polished gold tone.",
     "Small, but loud. Chunky 16 mm dome huggies in mirror-polished 18k gold tone. The Bold Dome Huggies, ₹999.")
quiet("bold-dome-huggies", "Chunky 16 mm dome huggies in polished 18k gold tone. The Bold Dome Huggies, ₹999.")
play("bold-dome-huggies", "Snap.", "a hinged huggie, closed round a pencil.", "16 mm · hinged · 18k gold-tone",
     "Snap. ✏️ A 16 mm hinged dome huggie in polished 18k gold tone. The Bold Dome Huggies, ₹999.")

# ---- Quatrefoil Éclat Studs: 15 mm four-point star, pavé outline, four pear stones and a round centre, gold tone
rhyme("quatrefoil-eclat-studs", "Mithai-shaped.", "four-point stars, not varq.", "15 mm · four-point star · 18k gold-tone",
      "Mithai-shaped. A 15 mm four-point star in clear cubic zirconia: a pavé outline, four pear stones and a round centre. The Quatrefoil Éclat Studs, ₹1,299.")
silk("quatrefoil-eclat-studs", "The star note.", "A four-point star in pavé,<br>four pear stones inside.",
     "The star note. A four-point star outlined in pavé, with four pear stones and a round centre inside. The Quatrefoil Éclat Studs, ₹1,299.")
worn("quatrefoil-eclat-studs", "One star, each ear.", "A 15 mm four-point star<br>in clear cubic zirconia.",
     "One star, each ear. A 15 mm four-point star in clear cubic zirconia and 18k gold tone. The Quatrefoil Éclat Studs, ₹1,299.")
quiet("quatrefoil-eclat-studs", "A 15 mm four-point star in clear cubic zirconia and 18k gold tone. The Quatrefoil Éclat Studs, ₹1,299.")
play("quatrefoil-eclat-studs", "Look closer.", "four pear stones inside a pavé star.", "15 mm · four-point star · 18k gold-tone",
     "Look closer. 🔍 Four pear stones and a round centre inside a pavé star. The Quatrefoil Éclat Studs, ₹1,299.", reserve=True)

# ---- Verdant Cushion Studs: 8 mm emerald-green cushion in a sunburst halo of clear stones, 13 mm, rhodium silver tone
rhyme("verdant-cushion-studs", "Pista, polished.", "emerald-green cubic zirconia, not pistachios.", "13 mm · emerald-green · silver tone",
      "Pista, polished. An emerald-green cushion cubic zirconia in a sunburst halo of clear stones, rhodium silver tone. The Verdant Cushion Studs, ₹1,199.")
silk("verdant-cushion-studs", "Green, on navy.", "An emerald-green cushion<br>in a sunburst halo.",
     "Green, on navy. An emerald-green cushion cubic zirconia framed in a sunburst of clear stones. The Verdant Cushion Studs, ₹1,199.", tone="cream")
worn("verdant-cushion-studs", "One green dot.", "An emerald-green cushion<br>in a halo of clear stones.",
     "One green dot. A 13 mm stud: an emerald-green cushion in a halo of clear cubic zirconia. The Verdant Cushion Studs, ₹1,199.")
quiet("verdant-cushion-studs", "An emerald-green cushion in a sunburst halo, rhodium silver tone. The Verdant Cushion Studs, ₹1,199.", reserve=True)
play("verdant-cushion-studs", "The exact green.", "matched, spool by spool.", "13 mm · emerald-green · silver tone",
     "The exact green. 🧵 Emerald-green cubic zirconia in a sunburst halo of clear stones. The Verdant Cushion Studs, ₹1,199.")

# ---- Baguette Halo Drops: 14 mm disc of baguettes around a small pearl, a white pearl drop below, gold tone
rhyme("baguette-halo-drops", "Makhana, matched.", "a pearl drop under a sunburst of baguettes.", "14 mm disc · pearl drop · 18k gold-tone",
      "Makhana, matched. A 14 mm sunburst of clear baguettes around a small pearl, with a white pearl drop below. The Baguette Halo Drops, ₹1,499.", reserve=True)
silk("baguette-halo-drops", "The sunburst note.", "A ring of clear baguettes,<br>a white pearl drop below.",
     "The sunburst note. A ring of clear baguettes around a small pearl, with a white pearl drop below. The Baguette Halo Drops, ₹1,499.")
worn("baguette-halo-drops", "Sunburst, then a pearl.", "A disc of baguettes<br>and a white pearl drop.",
     "Sunburst, then a pearl. A 14 mm disc of clear baguettes with a white pearl drop. The Baguette Halo Drops, ₹1,499.")
quiet("baguette-halo-drops", "A sunburst of clear baguettes and a white pearl drop, 18k gold tone. The Baguette Halo Drops, ₹1,499.")
play("baguette-halo-drops", "Button up.", "a sunburst stud, pearl and all.", "14 mm disc · pearl drop · 18k gold-tone",
     "Button up. A sunburst of clear baguettes with a white pearl drop, for the collar and the ear. The Baguette Halo Drops, ₹1,499.", reserve=True)

# ---- Pearl Circlet Studs: a cushion-square pearl in a pavé halo, about 13 mm (listing copy and photos disagree on the metal)
rhyme("pearl-circlet-studs", "Paneer? Pearl.", "a cushion pearl in a pavé halo.", "13 mm · cushion pearl · pavé halo",
      "Paneer? Pearl. A soft cushion-square pearl framed in a halo of pavé. The Pearl Circlet Studs, ₹1,899.")
silk("pearl-circlet-studs", "Square, but soft.", "A cushion pearl<br>in a halo of pavé.",
     "Square, but soft. A cushion-square pearl in a halo of tiny clear stones. The Pearl Circlet Studs, ₹1,899.", tone="cream")
worn("pearl-circlet-studs", "Hair up, pearl on.", "A cushion pearl<br>framed in pavé.",
     "Hair up, pearl on. A cushion-square pearl framed in pavé, about 13 mm. The Pearl Circlet Studs, ₹1,899.")
quiet("pearl-circlet-studs", "A cushion-square pearl in a pavé halo. The Pearl Circlet Studs, ₹1,899.")
play("pearl-circlet-studs", "One lump or two?", "a cushion pearl, sugar-cube sized.", "13 mm · cushion pearl · pavé halo",
     "One lump or two? ☕ A cushion-square pearl in a pavé halo, about the size of a sugar cube. The Pearl Circlet Studs, ₹1,899.")

# ---- Prism Cluster Studs: an arc of five coloured cubic zirconia (purple, pink, yellow) with tiny pearls, rhodium silver tone
rhyme("prism-cluster-studs-silver", "Pastel, with sugar.", "purple, pink and yellow cubic zirconia.", "purple · pink · yellow · silver tone",
      "Pastel, with sugar. An arc of purple, pink and yellow cubic zirconia with tiny pearls, rhodium silver tone. The Prism Cluster Studs, ₹1,499.")
silk("prism-cluster-studs-silver", "The colour note.", "Purple, pink and yellow,<br>in one small arc.",
     "The colour note. Purple, pink and yellow cubic zirconia in one small arc, with tiny pearls. The Prism Cluster Studs, ₹1,499.", tone="cream")
worn("prism-cluster-studs-silver", "Five colours, one lobe.", "Purple, pink and yellow<br>in one small arc.",
     "Five colours, one lobe. An arc of purple, pink and yellow cubic zirconia with tiny pearls. The Prism Cluster Studs, ₹1,499.")
quiet("prism-cluster-studs-silver", "An arc of purple, pink and yellow cubic zirconia, rhodium silver tone. The Prism Cluster Studs, ₹1,499.")
play("prism-cluster-studs-silver", "Watercolour, set in stone.", "purple, pink and yellow cubic zirconia.", "purple · pink · yellow · silver tone",
     "Watercolour, set in stone. 🎨 Purple, pink and yellow cubic zirconia in one small arc. The Prism Cluster Studs, ₹1,499.")

# ---- Aqua Heart Drops: a C of six round brilliants with baguettes inside, an icy aqua heart below, rhodium silver tone
rhyme("aqua-heart-drops-silver", "Kanche, but kept.", "aqua hearts, not marbles.", "aqua heart · clear brilliants · silver tone",
      "Kanche, but kept. A curve of clear brilliants with an icy aqua heart below, rhodium silver tone. The Aqua Heart Drops, ₹1,499.")
silk("aqua-heart-drops-silver", "The aqua note.", "A curve of clear brilliants,<br>an aqua heart below.",
     "The aqua note. A curve of clear brilliants with an icy aqua heart hanging below. The Aqua Heart Drops, ₹1,499.", tone="cream")
worn("aqua-heart-drops-silver", "A little blue.", "A curve of clear brilliants,<br>an aqua heart below.",
     "A little blue. A curve of clear brilliants with an icy aqua heart below. The Aqua Heart Drops, ₹1,499.")
quiet("aqua-heart-drops-silver", "Clear brilliants and an icy aqua heart, rhodium silver tone. The Aqua Heart Drops, ₹1,499.")
play("aqua-heart-drops-silver", "The exact blue.", "an aqua heart, matched to the pigment.", "aqua heart · clear brilliants · silver tone",
     "The exact blue. An icy aqua heart below a curve of clear brilliants. The Aqua Heart Drops, ₹1,499.")

def shots():
    """copy space and the jewellery's vertical extent per plate, from the shoot manifests"""
    out = {}
    for g in ("g1", "g2", "g3", "g4"):
        p = f"{HERE}/shots_{g}.json"
        if os.path.exists(p):
            for s in json.load(open(p)):
                if s.get("pass") or s.get("file"): out[f"{s['key']}-{s['format']}"] = s
    return out

def url(k, fmt, variant):
    q = f"variant={VARIANT[(k, variant)]}&" if (k, variant) in VARIANT else ""
    return f"https://www.nairaflore.com/products/{k}?{q}utm_source=meta&utm_medium=paid&utm_campaign=perf_oct26_{fmt}&utm_content={k}-{fmt}"

def plan(rows):
    """campaign, ad set and launch wave for every ad pair; reserves (scored under 8) wait for the last wave"""
    pairs = {}
    for r in rows: pairs.setdefault(r["ad"].rsplit("-", 1)[0], r)
    out = []
    for stem, r in pairs.items():
        k, fmt = stem.rsplit("-", 1)
        cat = "Earrings" if k in EARRINGS else "Necklaces & rings" if k in NECK_RINGS else "Bracelets"
        aset = "Warm · site visitors 30d + add-to-cart 14d + IG engagers 90d · excl. purchasers 180d" if fmt == "quiet" else cat
        pri = STOCK[k] / 80 * .6 + FORMAT_W[fmt] * .4 - (1 if r["reserve"] else 0)
        out.append(dict(stem=stem, key=k, format=fmt, campaign=CAMPAIGN[fmt], adset=aset, priority=round(pri, 3), reserve=bool(r["reserve"])))
    for (c, a) in {(o["campaign"], o["adset"]) for o in out}:
        grp = sorted([o for o in out if o["campaign"] == c and o["adset"] == a], key=lambda o: -o["priority"])
        size = 8 if "Quiet" in c else 5
        for i, o in enumerate(grp): o["wave"] = i // size + 1
    return sorted(out, key=lambda o: (o["campaign"], o["adset"], o["wave"], -o["priority"]))

def review_fixes():
    out = {}
    for n in ("a", "b"):
        p = f"{HERE}/review_{n}.json"
        if os.path.exists(p):
            for r in json.load(open(p)):
                if r.get("fix"): out[r["ad"]] = {k: v for k, v in r["fix"].items() if k != "band"}
    return out

def glue_h(h):
    """keep a short word with the next one, so no headline line is a lone "IT", "BUT" or "note." """
    h = re.sub(r"\b(\w{1,3}) (?=\S)", lambda m: m.group(1) + "\u00a0", h)
    return re.sub(r" (\S+)$", "\u00a0\\1", h)                       # and the last word with the one before it

def build():
    frames, rows = [], []; S = shots(); global FX; FX = review_fixes()
    for k, fmt, ov, meta in F:
        name, price, noun = P[k]; plate = f"plates/{k}-{fmt}.jpg"
        if not os.path.exists(os.path.join(HERE, "..", plate)): continue
        e = dict(plate=plate, **{x: y for x, y in ov.items() if x != "reserve"})
        if e.get("h"): e["h"] = glue_h(e["h"])
        stem = f"{k}-{fmt}"; fx = {t: FX.get(f"{stem}-{t}", {}) for t in ("feed", "story")}
        if fx["feed"].get("drop"): continue
        for t in ("feed", "story"):
            f = dict(fx[t])
            if f.pop("drop", None): f = {"layout": "plain"}
            if ov["layout"] == "quiet": f = {x: y for x, y in f.items() if x not in ("y", "fixed")}   # the calm-band finder places the name
            if f: e[t] = f
        s = S.get(f"{k}-{fmt}", {}); lay = ov["layout"]
        if s.get("subject_y") and "cy" not in e: e["cy"] = round(min(max(sum(s["subject_y"]) / 2, .36), .64), 3)
        if s.get("copy_space") in ("tl", "tr", "bl", "br") and "at" not in e: e["at"] = s["copy_space"]
        if s.get("tone") == "dark" and "tone" not in e: e["tone"] = "cream"
        if s.get("subject_y"): e["sy"] = s["subject_y"]
        if e.get("spec", "").startswith(name + " · "): e["spec"] = e["spec"][len(name) + 3:]          # the Meta headline carries the name
        if lay == "deck": e.update(cta=f"Shop the {noun}", price=price, at=e.get("at", "tl"), w=e.get("w", 640), hs=e.get("hs", 96), cs=e.get("cs", 38))
        if lay == "note": e.update(n=f"{name}\u00a0·\u00a0{price}", at=e.get("at", "tl"), w=e.get("w", 600), hs=e.get("hs", 78), cs=e.get("cs", 34), ns=e.get("ns", 18))
        if lay == "quiet": e.update(name=name, price=price)
        frames.append(e)
        for tag in ("feed", "story"):
            rows.append(dict(ad=f"{k}-{fmt}-{tag}", product=name, format=fmt, placement=tag, variant=meta.get("variant") or "",
                             reserve="yes" if ov.get("reserve") or k in HOLD else "", primary_text=f"{meta['pt']}\n\n{OFFER}",
                             headline=f"{name} · {price}", cta="SHOP_NOW", url=url(k, fmt, meta.get("variant"))))
    json.dump({"frames": frames}, open(f"{HERE}/copy.json", "w"), ensure_ascii=False, indent=1)
    P_ = plan(rows); W = {o["stem"]: o for o in P_}
    for r in rows:
        o = W[r["ad"].rsplit("-", 1)[0]]; r.update(campaign=o["campaign"], adset=o["adset"], wave=o["wave"])
    json.dump(P_, open(f"{HERE}/plan.json", "w"), ensure_ascii=False, indent=1)
    with open(f"{HERE}/meta.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(len(frames), "frames,", len(rows), "ads")

if __name__ == "__main__":
    build()
