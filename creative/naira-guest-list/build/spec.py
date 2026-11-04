"""The Guest List: Naira's wedding-season collection campaign. One invitation suite, ten cards, three layers.

Every card is one function from the shaadi itinerary (or one practical reason to buy), links to the collection it
belongs to, and carries the dress-code colour of that function. The heroes are the pieces with the deepest stock on
4 November 2026 (30 to 80 units each; every tile in a grid or carousel has at least 10), so the campaign sells what the
warehouse can ship. Photographs: nine new Higgsfield generations locked to the product photos, the rest from the
brand's existing library, and the shop's own plinth photographs for the tiles. Prices are the live nairaflore.com
prices on 4 November 2026."""

UTM = "utm_source=meta&utm_medium=paid&utm_campaign=guest-list-nov26&utm_content={id}"
LINKS = {
    "all": "https://nairaflore.com/collections/shop-all",
    "bracelets": "https://nairaflore.com/collections/bracelets",
    "earrings": "https://nairaflore.com/collections/earrings",
    "necklaces": "https://nairaflore.com/collections/necklaces",
    "rings": "https://nairaflore.com/collections/rings",
}
OFFER = "Buy 2, 10% off · Buy 3, 20% off"
OFFER_LONG = "Take 2 pieces for 10% off or 3 for 20% off with codes BUY2 and BUY3 at checkout. Free insured shipping and cash on delivery across India."
MIN_HERO, MIN_GRID = 30, 10          # units in stock a hero piece / a tile must have

# dress-code colours (band, type on the band, flower on the wordmark)
COL = {
    "green": ("#1E6B47", "#F7F1E6", "#FFBDA8"),
    "yellow": ("#E9B414", "#1F1A14", "#C86F58"),
    "magenta": ("#B41E63", "#F7F1E6", "#FFBDA8"),
    "red": ("#A41E22", "#F7F1E6", "#FFBDA8"),
    "navy": ("#16213B", "#F7F1E6", "#FFBDA8"),
    "cream": ("#FBF7F1", "#1F1A14", "#C86F58"),
    "blush": ("#F2CFC4", "#1F1A14", "#C86F58"),
    "sage": ("#CFDFD9", "#1F1A14", "#C86F58"),
}

# photos: image id (img/raw/<id>.png) with a focus point (x, y in 0..1) for the crop
ADS = [
    dict(id="I1", layer="Inform", kind="carousel", link="all", colour="cream",
         eyebrow="THE GUEST LIST · NOVEMBER 2026", hook="Every function. One guest list.",
         sub="121 pieces in stock, from ₹599.",
         cover=["verdant-circlet-studs", "toggle-link-chain", "baguette-tennis-necklace", "prism-riviere-bracelet", "verdant-eternity-band",
                "cushion-halo-ring", "baguette-tennis-bracelet", "woven-gold-hoops", "halo-curve-ring"],
         cover_extra=["marquise-layering-set", "kiss-knot-bangle", "ribbon-bead-bracelet"],
         cards=[("EARRINGS", "earrings", ["verdant-circlet-studs", "woven-gold-hoops", "brushed-gold-huggies", "pearl-nugget-hoops"]),
                ("RINGS", "rings", ["cushion-halo-ring", "verdant-eternity-band", "halo-curve-ring", "baguette-eternity-band"]),
                ("NECKLACES", "necklaces", ["toggle-link-chain", "baguette-tennis-necklace", "marquise-layering-set", "marquise-drop-choker"]),
                ("BRACELETS", "bracelets", ["prism-riviere-bracelet", "baguette-tennis-bracelet", "kiss-knot-bangle", "ribbon-bead-bracelet"])],
         headline="121 pieces · from ₹599",
         primary="Mehendi, haldi, sangeet, the engagement and the reception: one guest list, 121 pieces in stock, from ₹599.\n"
                 "18k gold coating over surgical steel, PVD anti-tarnish, waterproof.\n" + OFFER_LONG,
         why="Catalogue carousels at current prices are the account's best format (ROAS 2.6 to 2.7, cost per purchase under ₹500). "
             "This one opens the suite, and every card links to its own collection, so the client's four collection links all run from one ad."),
    dict(id="I2", layer="Inform", kind="photo", link="all", colour="sage", piece="brushed-gold-huggies",
         feed=("g10", 0.45, 0.47), story=("d5554e67", 0.50, 0.42),
         eyebrow="THE PETITE PROMISE", title="WATERPROOF", hook="Shower in it. Sleep in it. Still gold.",
         sub="PVD gold on surgical steel, so the colour stays.",
         headline="Brushed Gold Huggies · ₹799",
         primary="Shower in it, sleep in it, wear it to all five functions. 18k gold coating bonded to surgical steel in a vacuum (PVD), so it does not wear off like plating. The Brushed Gold Huggies, ₹799. Most of the collection is waterproof; it says so on every page.\n" + OFFER_LONG,
         why="Nobody in the category argues craft. PVD and waterproof are Naira's unclaimed lane, and the ₹799 pair was the judge's best entry-price hook (8.20). New photograph: the huggie under the shower, generated from the product photo."),
    dict(id="D1", layer="Desire", kind="photo", link="earrings", colour="green", piece="verdant-circlet-studs",
         feed=("g01", 0.47, 0.50), story=("g03", 0.60, 0.45),
         eyebrow="THE GUEST LIST · DRESS CODE: GREEN", title="MEHENDI", hook="Greener than the mehendi.",
         sub="A 10mm green stone, a circlet of light and one pearl.",
         headline="Verdant Circlet Studs · ₹1,099",
         primary="Mehendi. Dress code: green. A 10mm cushion-cut green stone over an open circlet of clear stones, gold stars and a 6mm pearl, 17mm tall, so one bold ear is enough. The Verdant Circlet Studs, ₹1,099. Earrings from ₹599.\n" + OFFER_LONG,
         why="The mehendi line scored highest of all twenty judged ads (8.20). It now carries the deepest-stocked piece in the warehouse (80 pairs), photographed on a hand in fresh green mehendi."),
    dict(id="D2", layer="Desire", kind="photo", link="earrings", colour="yellow", piece="woven-gold-hoops",
         feed=("g04", 0.47, 0.50), story=("g11", 0.50, 0.45),
         eyebrow="THE GUEST LIST · DRESS CODE: YELLOW", title="HALDI", hook="Only the haldi washes off.",
         sub="18k gold PVD, anti-tarnish, waterproof.",
         headline="Woven Gold Hoops · ₹1,199",
         primary="Haldi. Dress code: yellow. Only the haldi washes off: 18k gold coating, PVD anti-tarnish, waterproof. Our bestselling Woven Gold Hoops, 25mm of braided gold rope, ₹1,199. Earrings from ₹599.\n" + OFFER_LONG,
         why="Haldi yellow was the strongest thumb-stop of the judged round (8.07), and the Woven Gold Hoops are the account's most-bought single piece (56 pairs in stock). The new photograph puts the haldi on the cheek and keeps the hoop clean, which is the PVD promise as a joke."),
    dict(id="D3", layer="Desire", kind="photo", link="bracelets", colour="magenta", piece="prism-riviere-bracelet",
         feed=("eb2b553c", 0.50, 0.55), story=("g13", 0.50, 0.45),
         eyebrow="THE GUEST LIST · EVERY COLOUR", title="SANGEET", hook="Dress code: all of them.",
         sub="Aqua, pink and yellow stones in pavé halos, 18cm.",
         headline="Prism Rivière Bracelet · ₹2,399",
         primary="Sangeet. Dress code: all of them. An 18cm line of 5mm cushion-cut stones in aqua, pink and pale yellow, each in its own pavé halo, rhodium coated, with a fold-over clasp that keeps the line flat while you dance. The Prism Rivière Bracelet, ₹2,399. Bracelets from ₹599.\n" + OFFER_LONG,
         why="Sangeet scored 8.18 with the judge. The bracelet is the deepest-stocked bracelet (63 units) and the most colourful piece in the range: the feed card uses the brand's prism-and-rainbow still life, the story a new magenta flat lay, and it carries the bracelets link the client asked for."),
    dict(id="D4", layer="Desire", kind="photo", link="rings", colour="red", piece="cushion-halo-ring",
         feed=("g09", 0.68, 0.48), story=("eac58fb8", 0.46, 0.42),
         eyebrow="THE GUEST LIST · DRESS CODE: RED", title="ENGAGEMENT", hook="Fits every finger at the table.",
         sub="Open at the back, so it adjusts from US 5 to 9.",
         headline="Cushion Halo Ring · ₹1,099",
         primary="Engagement. Dress code: red. An 8mm clear stone in four claws inside a 12mm cushion pavé halo, rhodium coated, open at the back so it adjusts to fit US 5 to 9. The Cushion Halo Ring, ₹1,099. Rings from ₹599.\n" + OFFER_LONG,
         why="The judge called this hand the most convincing of the twenty (8.05). Fit is the biggest doubt when buying a ring online; the adjustable band answers it, and 58 are in stock."),
    dict(id="D5", layer="Desire", kind="photo", link="necklaces", colour="navy", piece="baguette-tennis-necklace",
         feed=("g07", 0.45, 0.60), story=("g08", 0.50, 0.45),
         eyebrow="THE GUEST LIST · DRESS CODE: BLACK TIE", title="RECEPTION", hook="One line of light for the last dance.",
         sub="36cm of crosswise baguettes, choker length.",
         headline="Baguette Tennis Necklace · ₹2,099",
         primary="Reception. Dress code: black tie. A straight line of clear baguettes set crosswise, each held by gold claws, 6mm wide and 36cm long, so it sits close at the base of the neck, with a box clasp. The Baguette Tennis Necklace, ₹2,099, in crystal, ruby or emerald. Necklaces from ₹699.\n" + OFFER_LONG,
         why="Diya-lit night shots of the tennis bracelet were the top Story creative in the account (4% link CTR, ROAS 2.3). Same line of light, now the necklace (69 in stock) on a piano and at the neck, for the necklaces link."),
    dict(id="C1", layer="Convert", kind="trio", link="all", colour="blush",
         trio=["verdant-circlet-studs", "toggle-link-chain", "baguette-tennis-bracelet"],
         eyebrow="THREE FUNCTIONS · ONE ORDER", hook="Any three pieces, 20% off.",
         sub="Code BUY3 at checkout.",
         headline="Any 3 pieces · 20% off",
         primary="Three functions, three pieces, one order. Pick any three and take 20% off with code BUY3 at checkout. Shown: Verdant Circlet Studs ₹1,099, Toggle Link Chain ₹1,199 and Baguette Tennis Bracelet ₹1,499, together ₹3,797, or ₹3,038 with the code. Free insured shipping and cash on delivery across India.",
         why="'Any three pieces, 20% off' was the judge's strongest offer card (8.03). The three shown are the deepest-stocked piece in each of three collections, and the two totals make the maths visible."),
    dict(id="C2", layer="Convert", kind="photo", link="necklaces", colour="blush", piece="toggle-link-chain",
         feed=("0e5342cd", 0.40, 0.58), story=("4654eedc", 0.50, 0.40),
         eyebrow="RSVP · 3 TO 5 DAYS", title="DELIVERY", hook="Arrives before the wedding does.",
         sub="Gift-boxed, insured shipping, pay on delivery.",
         headline="Toggle Link Chain · ₹1,199",
         primary="Arrives before the wedding does. Every order ships insured and free across India in 3 to 5 working days, arrives in the Naira box, and you can pay when it arrives. Shown: the Toggle Link Chain, a 50cm paperclip chain with a 15mm toggle worn at the front, ₹1,199. Necklaces from ₹699.\n" + OFFER_LONG,
         why="The judge marked down the gift-box card for not showing the box (7.88). This one shows the real pink Naira box with the deepest-stocked necklace (79 units), and puts the three trust levers (delivery, box, cash on delivery) in one card for warm audiences."),
    dict(id="C3", layer="Convert", kind="grid", link="all", colour="cream",
         grid=["ribbon-bead-bracelet", "brushed-gold-huggies", "emerald-square-ear-cuff", "petal-flower-studs", "duo-link-bracelet",
               "north-star-bangle", "twin-heart-studs", "mesh-band-ring", "birthstone-heart-necklace"],
         eyebrow="THE PLUS-ONE BUDGET", hook="Forty-two pieces under ₹1,000.",
         sub="Rings and earrings from ₹599, necklaces from ₹699.",
         headline="42 pieces under ₹1,000",
         primary="The plus-one budget: 42 pieces under ₹1,000, in stock now. Rings from ₹599, earrings from ₹599, bracelets from ₹599, necklaces from ₹699. 18k gold coating, PVD anti-tarnish.\n" + OFFER_LONG,
         why="Price-floor grids at current prices are the proven converter in this account, and 'The ₹799 pair' was the judge's clearest entry-price hook. The nine tiles are the nine deepest-stocked pieces under ₹1,000."),
]

# the hook drafts: four per card, the chosen one first (40 in all)
DRAFTS = {
    "I1": ["Every function. One guest list.", "You're invited. So is your jewellery.", "Five functions. Zero repeat looks.", "The whole guest list, from ₹599."],
    "I2": ["Shower in it. Sleep in it. Still gold.", "Gold that outlasts the wedding.", "Made to stay gold.", "PVD, not plating. Ask us the difference."],
    "D1": ["Greener than the mehendi.", "Mehendi. Dress code: green.", "Goes on before the mehendi, stays on after.", "The green that doesn't fade by the pheras."],
    "D2": ["Only the haldi washes off.", "Haldi. Dress code: yellow.", "Haldi-proof. Actually.", "Yellow is the dress code."],
    "D3": ["Dress code: all of them.", "Every colour of the sangeet, on one wrist.", "Catches every light on the floor.", "Sangeet. Dress code: colour."],
    "D4": ["Fits every finger at the table.", "Engagement. Dress code: red.", "Say yes. It adjusts.", "No ring size required."],
    "D5": ["One line of light for the last dance.", "Reception. Dress code: black tie.", "Black tie, one bright line.", "The last dance deserves the tennis necklace."],
    "C1": ["Any three pieces, 20% off.", "Three functions. Three pieces. 20% off.", "One for each function. 20% off the lot.", "Mehendi, sangeet, reception: sorted, 20% off."],
    "C2": ["Arrives before the wedding does.", "RSVP: 3 to 5 days.", "Ships insured. Arrives boxed. Pay on delivery.", "Boxed, insured, at your door before the baraat."],
    "C3": ["Forty-two pieces under ₹1,000.", "The plus-one budget.", "Under ₹1,000. Over-dressed.", "Rings from ₹599. Earrings from ₹599."],
}

PLAN = dict(
    name="Naira · The Guest List · Shop All + collections · ₹1,000/day · Nov 2026",
    objective="Sales (OUTCOME_SALES), conversion event Purchase, website",
    launch="Launch at 10:10 IST on the day the client approves; Dhanteras is 6 November and Diwali 8 November, then the wedding season opens from mid-November.",
    budget="₹1,000 per day, campaign budget (CBO), 14 days before the first review of the full set",
    adsets=[
        dict(name="Cold · all India · women 22 to 45 · Advantage+ audience", budget="₹700/day (CBO minimum ₹600)", ads=["I1", "I2", "D1", "D2", "D3", "D4", "D5", "C3"],
             placements="Instagram Feed, Stories and Reels; Facebook Feed and Stories. Advantage+ placements on, with the 9:16 files for Stories and Reels."),
        dict(name="Warm · website visitors 30 days + Instagram engagers 60 days + add to cart 14 days, purchasers excluded", budget="₹300/day", ads=["C1", "C2", "D1", "D3"],
             placements="Same placements. Frequency cap 2 per 7 days."),
    ],
    kpis=["Link CTR at or above 2.5% (the account's statics run 2.3 to 3.4%)", "Cost per link click at or below ₹20", "Cost per purchase at or below ₹600 (the catalogue campaigns run ₹450 to ₹520)", "Purchase ROAS at or above 2.0 (the best catalogue campaigns run 2.6 to 2.7)"],
    rules=["Do not judge any ad before 1,500 impressions or 48 hours.", "At 1,500 impressions: link CTR under 1.2% means switch the ad off.",
           "At ₹1,500 spent with no purchase: switch the ad off and move its budget to the layer's best card.",
           "Any ad under ₹600 per purchase over three days: raise the campaign budget by 20% (never more than 20% in one day, so learning holds).",
           "Day 7: keep the top five by cost per purchase, replace the bottom three with the reserve hooks in the drafts list.",
           "Day 14: read the carousel against the single cards; if the carousel is winning on ROAS, add a second carousel built from the week's top sellers.",
           "Stock: every hero has 30 to 80 units; if any hero drops under 15 units, swap it for the next piece in its carousel card and keep the hook."],
)
