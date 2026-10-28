# Builds the variables for one Shopify mutation, 27 Oct 2026 (the owner asked for everything in a single approval):
#  - Aquarelle Rivière Bracelet (ADT06): White and Pink colours, 2 units each at ₹1299 against ₹1800 like Royal Blue and
#    Lavender, with their four photos each, and the live description moved from two colours to four (every other line,
#    including the owner's PVD lines, kept as it reads live).
#  - Clarté Baguette Bracelet — Silver (ADT01-SV): a new ACTIVE listing, 2 units at ₹1299 against ₹2500 like the Carré
#    lines, the gold Clarté's copy in silver tone with the PVD rhodium lines the owner uses on the silver Bougainvillea, and
#    the gold Clarté's size guide card (same title and length).
# ProductSetInput cannot publish, so the mutation turns autoPublish on for the six sales channels just before productSet and
# back off right after it, which publishes the new listing everywhere in the same request.
# Usage: ship_27oct.py LIVE_AQUARELLE_DESCRIPTION.html  -> ../shopify/payloads/ship_27oct.json
import json, os, sys, html
H = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(H, "../shopify")
L = {p["handle"]: p for p in json.load(open(f"{S}/listing.json"))}
EMAP = json.load(open(f"{H}/export_map.json")); URL = json.load(open(f"{H}/url_map.json"))
LOCATION = "gid://shopify/Location/76267389090"; UNITS = 2
e = html.escape
CARE = "Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch."
PVD = ["Plating: PVD rhodium coating, anti-tarnish",
       "PVD vs plating: Regular plating is a soft layer that wears off over time. PVD is bonded to the metal in a vacuum, so it is far "
       "harder, stands up to sweat and keeps its colour much longer."]
SG = "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/clarte-baguette-bracelet-size-guide.jpg"
GMETA = [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field", "value": "Apparel & Accessories > Jewelry > Bracelets"},
         {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
         {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
         {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
         {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": "191"}]

# Aquarelle: the new colours' variants and photos, and the live description with only the colour lines changed. The owner
# took Lavender's worn-on-the-model photo (A7_W1) off the live listing at 08:11 UTC on 27 Oct, so the White and Pink takes
# of that frame stay in the exports but are not listed: each new colour gets Lavender's live three, hero, worn close and macro.
SKIP = {"A7w_W1", "A7p_W1"}
aq = L["aquarelle-riviere-bracelet"]; t = aq["title"]
new = [v for v in aq["variants"] if v["sku"] in ("ADT06-WH", "ADT06-PK")]
media, variants = [], []
for v in new:
    for k, alt in aq["images"]:
        if k.startswith(v["src"] + "_") and k not in SKIP:
            head, _, rest = alt.partition(", ")
            media.append({"originalSource": URL[EMAP[k]], "alt": f"{t}, {head} — {rest}", "mediaContentType": "IMAGE"})
    variants.append({"optionValues": [{"optionName": "Colour", "name": v["value"]}], "price": "1299.00", "compareAtPrice": "1800.00",
                     "inventoryPolicy": "DENY", "inventoryItem": {"sku": v["sku"], "tracked": True},
                     "inventoryQuantities": [{"availableQuantity": UNITS, "locationId": LOCATION}],
                     "mediaSrc": [URL[EMAP[v["src"] + "_H"]]]})
desc = open(sys.argv[1]).read()
for a, b in [("One fine line, in two colours.", aq["tagline"]),
             ("In bright Royal Blue or soft Lavender.", "In bright Royal Blue, soft Lavender, rose Pink or clear White."),
             ("Wear Royal Blue and Lavender together on one wrist.", e(aq["tip"])),
             ("<li>Colours: Royal Blue or Lavender</li>", "<li>" + e(next(x for x in aq["details"] if x.startswith("Colours"))) + "</li>")]:
    assert desc.count(a) == 1, a; desc = desc.replace(a, b)

# Clarté Silver: the house description format, as shopify_payload.py.
sv = L["clarte-baguette-bracelet-silver"]; ts = sv["title"]
body = (f"<p>{e(sv['tagline'])} {e(sv['body'])}</p><p><strong>STYLING TIP:</strong> {e(sv['tip'])}</p><p><strong>Details</strong></p><ul>\n"
        + "".join(f"<li>{e(x)}</li>\n" for x in sv["details"] + PVD)
        + f"</ul><p><img src=\"{SG}\" alt=\"Size guide — {e(ts)}\" width=\"420\"></p>"
        + f"<p><strong>Care</strong></p><p>{e(CARE)}</p><p>You will receive your piece in a Naira Petite box.</p>")
name = ts.replace(" — ", ", ")
sv_input = {"title": ts, "handle": sv["handle"], "status": "ACTIVE", "vendor": "Naira Petite", "productType": "Bracelet",
            "category": "gid://shopify/TaxonomyCategory/aa-6-3",
            "tags": ["Aditya", "Bracelet", "Cubic Zirconia", "Demi Fine", "Naira Petite", "Rhodium Silver Tone Plated", "Tennis"],
            "descriptionHtml": body,
            "seo": {"title": f"{ts} | Naira Petite", "description": f"{sv['body'].split('. ')[0]}. {ts} by Naira Petite."},
            "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}],
            "variants": [{"optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": sv["variants"][0]["sku"],
                          "price": "1299.00", "compareAtPrice": "2500.00", "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
                          "inventoryQuantities": [{"locationId": LOCATION, "name": "available", "quantity": UNITS}]}],
            "files": [{"originalSource": URL[EMAP[k]], "alt": f"{name} — {alt}", "contentType": "IMAGE"} for k, alt in sv["images"]],
            "metafields": GMETA}

out = {"aqId": "gid://shopify/Product/10353413292194", "aqVariants": variants, "aqMedia": media,
       "aqProduct": {"id": "gid://shopify/Product/10353413292194", "descriptionHtml": desc},
       "sv": sv_input, "on": {"autoPublish": True}, "off": {"autoPublish": False}}
json.dump(out, open(f"{S}/payloads/ship_27oct.json", "w"), ensure_ascii=False, indent=1)
print(len(variants), "Aquarelle variants,", len(media), "photos;", ts, len(sv_input["files"]), "photos")
