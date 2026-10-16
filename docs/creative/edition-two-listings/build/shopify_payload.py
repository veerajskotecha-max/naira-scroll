# Builds the Shopify productSet input for every Edition Two product (DRAFT, vendor Naira Petite) from kit/listing.json, in the
# store's house description format (intro, STYLING TIP, Details list, Care, box line), with variants (SKU, price, cost, tracked
# inventory), images from their public URLs with alt text, variant images, SEO and Google Shopping metafields.
# Usage: shopify_payload.py LISTING_JSON OUTDIR  -> OUTDIR/<handle>.json (one ProductSetInput each) and OUTDIR/batches.json
import json, os, sys, html, re
listing, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
P = [x for x in json.load(open(listing)) if "title" in x]
e = html.escape
YF_STEEL = "Surgical stainless steel"
UNKNOWN_MATERIAL = {"Garnet Cable Cuff", "Tile Stone Bangle", "Pearl Nugget Hoops", "Emerald Halo C-Hoops", "Emerald Deco Hoops", "Birthstone Heart Necklace"}
GOLD = "18k gold tone plated"; SILVER = "Rhodium plated silver tone"; BOTH = "18k gold tone plated or rhodium plated silver tone (choose above)"
D = {  # title: (styling tip, [details])
 "Silk Mesh Cuff": ("Wear it on the wrist opposite your watch, or pair it with the Mesh Band Ring in the same metal.",
   ["Style: Open cuff", "Mesh: Rounded tube of fine woven mesh, approximately 15mm wide", "Ends: Two mirror polished oval caps facing each other",
    "Inner width: Approximately 6cm, with an opening of about 2.5cm", f"Plating: {BOTH}"]),
 "Garnet Cable Cuff": ("Stack it with a plain gold bangle so the gold ends have company.",
   ["Style: Slim open cuff", "Cable: Twisted silver tone cable, approximately 5mm thick", "Ends: Gold tone barrels, approximately 9mm, each with two rows of clear pavé",
    "Stones: One round garnet red stone at each tip", "Inner width: Approximately 6cm", "Finish: Silver tone cable with 18k gold tone ends"]),
 "Triple Coil Wrap Bangle": ("Wear it alone. It already looks like a stack of three.",
   ["Construction: One continuous ribbed snake coil wire, approximately 4mm, wound in three turns", "Height: Approximately 14mm across the three turns",
    "Ends: Two small rectangular caps set with clear pavé, on the top and bottom turns", "Fit: Flexible wrap that eases over the hand", f"Plating: {BOTH}"]),
 "Marquise Wheat Cuff": ("Let it be the only bracelet, with a bare neckline and hair pulled back.",
   ["Style: Open cuff", "Stones: Two slanted rows of clear marquise cut cubic zirconia, approximately 7mm each", "Width: Approximately 14mm across the stone rows",
    "Setting: Fine claw settings, laid like the grains of a wheat ear", f"Plating: {GOLD}"]),
 "Baguette Tennis Bracelet": ("Wear two colours together, ruby with crystal, for a stack that reads festive without trying.",
   ["Length: Approximately 17cm", "Stone: Rectangular baguette cut cubic zirconia set crosswise, the line approximately 4 to 5mm wide",
    "Colours: Crystal, Ruby or Emerald", "Setting: Each stone held at its corners by fine gold claws", "Closure: Box clasp with fold over safety", f"Plating: {GOLD}"]),
 "Droplet Open Ring": ("Wear it with the Droplet Open Cuff in the same metal.",
   ["Style: Adjustable open ring", "Ends: A round ball, approximately 7mm, and a long teardrop, approximately 9mm", "Fit: Open at the back, so it adjusts to fit",
    f"Plating: {BOTH}"]),
 "North Star Bangle": ("Stack the silver and the gold together on one wrist.",
   ["Style: Slim rigid oval bangle", "Band: Approximately 6mm wide, mirror polished",
    "Pattern: Engraved eight point north stars, each with a tiny stone at its centre, alternating with round clear cubic zirconia in flush bezels",
    "Plating: Rhodium plated silver tone or 18k gold tone plated (choose above)"]),
 "Tile Stone Bangle": ("Stack it with a fine chain bracelet so the square line has something soft beside it.",
   ["Style: Slim rigid bangle", "Pattern: Square tiles, approximately 4mm, alternating plain polished gold with a round clear stone in a square bezel",
    "Finish: Polished gold tone"]),
 "Kiss Knot Bangle": ("Wear gold and silver together with both knots on top of the wrist.",
   ["Construction: Flexible ribbed snake coil, approximately 5mm thick", "Front: The two ends cross under one smooth polished X, approximately 12mm",
    "Fit: Flexible, slips over the hand", f"Plating: {BOTH}"]),
 "Mint Pear Drop Earrings": ("Wear them with hair tucked back and a white or ivory neckline so the mint reads.",
   ["Length: Approximately 22mm", "Stones: Three small clear pear cut cubic zirconia leading to one pale mint green pear, approximately 9mm",
    "Setting: Fine gold claws", "Closure: Post with butterfly back", f"Plating: {GOLD}"]),
 "Duo Link Necklace": ("Wear it with the Duo Link Bracelet, or with your gold and silver rings together.",
   ["Length: Approximately 45cm plus a short extender", "Chain: Long oval links in gold tone and silver tone, approximately 20mm, joined by small stacked gold rings",
    "Closure: Lobster clasp with extender", "Plating: 18k gold tone plated and rhodium plated silver tone"]),
 "Duo Link Bracelet": ("Pair it with the Duo Link Necklace, or with a gold watch.",
   ["Length: Approximately 18cm plus a short extender", "Chain: Long oval links in gold tone and silver tone, approximately 20mm, joined by small stacked gold rings",
    "Closure: Lobster clasp with extender", "Plating: 18k gold tone plated and rhodium plated silver tone"]),
 "Baguette Eternity Band": ("Stack two colours on one finger, or wear one beside a plain gold band.",
   ["Width: Approximately 5mm", "Stones: Rectangular baguette cut cubic zirconia set crosswise all the way round", "Colours: Ruby, Emerald or Amethyst",
    "Setting: Small gold claws at each stone's corners", "Sizes: US 6, 7 and 8", f"Plating: {GOLD}"]),
 "Pearl Nugget Hoops": ("Wear them with a crisp white shirt or a silk blouse.",
   ["Size: Approximately 22mm across", "Pearl: One round white pearl, approximately 10mm, inside each hoop", "Detail: Lower curve set with short faceted gold beads",
    "Closure: Hinged lever back", "Finish: Gold tone"]),
 "Emerald Halo C-Hoops": ("Wear them with ivory or deep green.",
   ["Size: Approximately 22mm tall", "Stones: Small round emerald green cubic zirconia, each ringed in clear pavé", "Shape: Open C shaped half hoop",
    "Closure: Post back", "Finish: Bright silver tone"]),
 "Baguette Tennis Necklace": ("Wear it close at the base of the neck with an open neckline, and add the matching bracelet.",
   ["Length: Approximately 40cm", "Stone: Rectangular baguette cut cubic zirconia set crosswise, the line approximately 5mm wide", "Colours: Ruby, Crystal or Emerald",
    "Setting: Each stone held at its corners by fine gold claws", "Closure: Box clasp", f"Plating: {GOLD}"]),
 "Baguette Huggies": ("Mismatch them, one ruby and one emerald, or wear a pair beside the matching band.",
   ["Size: Approximately 18mm across", "Stones: One row of baguette cut cubic zirconia standing crosswise along the lower front", "Colours: Ruby, Crystal, Emerald or Amethyst",
    "Upper half: Plain polished gold", "Closure: Hinged snap", f"Plating: {GOLD}"]),
 "Emerald Deco Hoops": ("Let them be the statement, with hair up and no necklace.",
   ["Size: Approximately 22mm across", "Stones: Square emerald green cubic zirconia alternating with pairs of clear baguettes", "Setting: Bright claws",
    "Closure: Post back", "Finish: Bright silver tone"]),
 "Birthstone Heart Necklace": ("Give it in the month's colour, or layer two hearts for two birthdays.",
   ["Pendant: One heart cut cubic zirconia, approximately 7mm, in four slim gold claws", "Chain: Fine gold cable, fixed at the heart's shoulders so it sits straight",
    "Length: Approximately 40cm plus extender",
    "Colours: January garnet, February amethyst, March aquamarine, April crystal, May emerald, June light amethyst, July ruby, August peridot, September sapphire, October rose, November topaz, December blue zircon",
    "Finish: Gold tone"]),
 "Tubogas Dome Ring": ("Wear it alone on the index finger, or beside a slim plain band.",
   ["Width: Approximately 10mm", "Construction: Flexible tubogas with a puffed dome and fine parallel ridges", "Sizes: US 6, 7 and 8", f"Plating: {BOTH}"]),
 "Fine Tennis Bracelet": ("Wear it beside a watch every day.",
   ["Length: Approximately 17cm", "Stones: Round brilliant clear cubic zirconia, approximately 2.5mm each", "Setting: Each stone in its own gold claw cup, edge to edge",
    "Closure: Box clasp", f"Plating: {GOLD}"]),
 "Petal Flower Studs": ("Wear them every day, or as a second piercing beside a small hoop.",
   ["Size: Approximately 13mm tall", "Stones: Three round clear cubic zirconia, approximately 4mm, and one pear cut stone below", "Centre: Polished metal disc",
    "Closure: Post with butterfly back", f"Plating: {BOTH}"]),
 "Droplet Open Cuff": ("Pair it with the Droplet Open Ring in the same metal.",
   ["Style: Slim open cuff", "Wire: Approximately 3mm, polished", "Ends: A round ball, approximately 9mm, and a smooth teardrop", "Inner width: Approximately 6cm", f"Plating: {BOTH}"]),
 "Roman Numeral Trio Ring": ("Wear it as your one statement ring with gold and silver pieces alike.",
   ["Construction: Three bands fixed as one", "Top: Rose gold tone band engraved with Roman numerals and set with small round stones",
    "Middle: Silver tone band with two rows of pavé", "Bottom: Gold tone band with Roman numerals cut through the metal", "Height: Approximately 16mm",
    "Sizes: US 6, 7 and 8", "Plating: Rose gold tone, rhodium silver tone and 18k gold tone"]),
 "Linked Trio Ring": ("Wear all three on one finger, or spread them across two.",
   ["Construction: Three rings joined by small jump rings", "Rings: A polished band with flush set round stones, approximately 5mm; a slim pavé band, approximately 2.5mm; a box chain ring",
    "Sizes: US 6, 7 and 8", f"Plating: {BOTH}"]),
 "Crystal Baguette Eternity Ring": ("Stack it with the Baguette Eternity Band in a colour.",
   ["Width: Approximately 5mm", "Stones: Clear baguette cut cubic zirconia set crosswise all the way round", "Setting: Tall gold claws between the stones",
    "Sizes: US 6, 7 and 8", f"Plating: {GOLD}"]),
 "Chain Drop Dome Ring": ("Wear it on the middle finger so the drop swings when you move.",
   ["Band: Polished dome, approximately 6mm wide", "Detail: Two slim pavé collars with a short chain swag between them", "Drop: One pear cut clear cubic zirconia, approximately 7mm",
    "Sizes: US 6, 7 and 8", f"Plating: {BOTH}"]),
 "Watch Link Ring": ("Wear it on the hand with your watch.",
   ["Width: Approximately 11mm", "Construction: Three rows of polished links with a softly scalloped edge", "Inside: Smooth and polished", "Sizes: US 6, 7 and 8",
    f"Plating: {BOTH}"]),
 "Marquise Drop Choker": ("Wear it with an open neckline so the drop falls clear.",
   ["Collar: Smooth round omega, approximately 2mm", "Stone: One marquise cut clear cubic zirconia, approximately 10mm, set sideways at the front",
    "Drop: A fine chain of approximately 6cm with one small pear stone halfway and another at the end", f"Plating: {GOLD}"]),
 "Mesh Band Ring": ("Pair it with the Silk Mesh Cuff in the same metal.",
   ["Width: Approximately 10mm", "Construction: Fine woven metal mesh with neat rolled edges", "Sizes: US 6, 7 and 8", f"Plating: {BOTH}"]),
 "Bold Nocturne Drops": ("Wear them with the Bold Nocturne Chain or Bracelet.",
   ["Length: Approximately 30mm", "Construction: A polished oval link on a post, with a larger pavé set oval link hanging below",
    "Stone: Clear cubic zirconia pavé", "Closure: Post back", "Plating: 18k PVD gold tone plated"]),
 "Pear Point Open Cuff": ("Wear it with the opening on top of the wrist so both pears show.",
   ["Style: Slim open cuff", "Band: Polished, approximately 4mm, tapering to the ends", "Stones: One pear cut clear cubic zirconia, approximately 7mm, at each end",
    "Inner width: Approximately 6cm", f"Plating: {GOLD}"]),
 "Emerald Square Ear Cuff": ("Wear it with the Crystal Pear Ear Cuff on the same ear.",
   ["Style: Ear cuff, no piercing needed", "Size: Approximately 12mm across", "Stone: One square princess cut emerald green cubic zirconia, approximately 5mm, in four claws",
    "Fit: Slides onto the middle ridge of the ear", f"Plating: {GOLD}"]),
 "Crystal Pear Ear Cuff": ("Wear it with the Emerald Square Ear Cuff on the same ear.",
   ["Style: Ear cuff, no piercing needed", "Size: Approximately 12mm across", "Stone: One pear cut clear cubic zirconia, approximately 7mm, in gold claws",
    "Fit: Slides onto the middle ridge of the ear", f"Plating: {GOLD}"]),
}
CARE_STEEL = ("Waterproof and tarnish free, so daily wear and water are fine. Keep it away from perfume and harsh chemicals, wipe with a soft dry cloth "
              "and store it flat in its pouch.")
CARE_PLAIN = "Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch."
GCAT = {"Bracelet": ("Apparel & Accessories > Jewelry > Bracelets", "191"), "Necklace": ("Apparel & Accessories > Jewelry > Necklaces", "196"),
        "Ring": ("Apparel & Accessories > Jewelry > Rings", "200"), "Earrings": ("Apparel & Accessories > Jewelry > Earrings", "194")}
def first_sentence(s): return re.split(r"(?<=[.!?])\s", s.strip())[0]
inputs = []
for p in P:
    t = p["title"]; tip, det = D[t]; steel = t not in UNKNOWN_MATERIAL
    if steel: det = det + [f"Material: {YF_STEEL}"]
    body = (f"<p>{e(p['tagline'])} {e(p['body'])}</p><p><strong>STYLING TIP:</strong> {e(tip)}</p><p><strong>Details</strong></p><ul>\n"
            + "".join(f"<li>{e(x)}</li>\n" for x in det) + "</ul><p><strong>Care</strong></p><p>" + e(CARE_STEEL if steel else CARE_PLAIN)
            + "</p><p>You will receive your piece in a Naira Petite box.</p>")
    tags = [x for x in p["tags"] if steel or x not in ("Waterproof", "Tarnish Free", "Hypoallergenic")] + ["Edition Two"]
    seo_desc = f"{first_sentence(p['body'])} {t} by Naira Petite."
    files, seen = [], {}
    for im in p["images"]:
        files.append({"originalSource": im["src"], "alt": im["alt"], "contentType": "IMAGE"}); seen[im["position"]] = files[-1]
    opts = p["options"] or ["Title"]
    vals = {o: [] for o in opts}
    variants = []
    for v in p["variants"]:
        ov = v["options"] if p["options"] else {"Title": "Default Title"}
        for o in opts:
            if ov[o] not in vals[o]: vals[o].append(ov[o])
        cost = round(v["cost_usd"] * 83 * 1.2) if v["cost_usd"] else None
        inv = {"tracked": True, **({"cost": str(cost)} if cost else {})}
        var = {"optionValues": [{"optionName": o, "name": ov[o]} for o in opts], "price": str(v["price"]), "sku": v["sku"], "inventoryPolicy": "DENY",
               "inventoryItem": inv}
        if p["options"] and v.get("image_position") and len(p["variants"]) > 1:
            f = seen[v["image_position"]]; var["file"] = {"originalSource": f["originalSource"], "alt": f["alt"], "contentType": "IMAGE"}
        variants.append(var)
    gc, fb = GCAT[p["product_type"]]
    inp = {"title": t, "handle": p["handle"], "status": "DRAFT", "vendor": "Naira Petite", "productType": p["product_type"], "tags": sorted(set(tags)),
           "descriptionHtml": body, "seo": {"title": f"{t} — {p['product_type']} | Naira Petite", "description": seo_desc[:320]},
           "productOptions": [{"name": o, "values": [{"name": x} for x in vals[o]]} for o in opts], "variants": variants, "files": files,
           "metafields": [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field", "value": gc},
                          {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
                          {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
                          {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
                          {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": fb}]}
    json.dump(inp, open(f"{out}/{p['handle']}.json", "w"), ensure_ascii=False, indent=1); inputs.append(inp)
B = [[i["handle"] for i in inputs[k:k + 4]] for k in range(0, len(inputs), 4)]
json.dump(B, open(f"{out}/batches.json", "w"), indent=1)
print(len(inputs), "products,", sum(len(i["variants"]) for i in inputs), "variants,", sum(len(i["files"]) for i in inputs), "images,", len(B), "batches")
