# Builds the productSet inputs for Emerald Carré's other colours (shopify/carre_colours.json), 26 Oct 2026: the green
# listing's copy, price and photos with the colour swapped, ACTIVE, 2 units each (the owner's count). The Details keep the
# green listing's PVD lines as they read live. Images come from Shopify staged uploads (a JSON map of filename -> resourceUrl).
# Usage: carre_payloads.py STAGED_MAP.json  -> shopify/payloads/<handle>.json
import json, os, re, sys, html
H = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(H, "../shopify")
COPY = json.load(open(f"{S}/carre_colours.json")); URL = json.load(open(sys.argv[1]))
SG = {"blush-carre-bracelet": "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/blush-carre-bracelet-size-guide.jpg?v=1793027192",
      "sapphire-carre-bracelet": "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/sapphire-carre-bracelet-size-guide.jpg?v=1793027191",
      "champagne-carre-bracelet": "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/champagne-carre-bracelet-size-guide.jpg?v=1793027191",
      "amethyst-carre-bracelet": "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/amethyst-carre-bracelet-size-guide.jpg?v=1793027191"}
LOCATION = "gid://shopify/Location/76267389090"; UNITS = 2; PRICE, COMPARE = "1299.00", "2500.00"  # as Emerald Carré
e = html.escape
CARE = "Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch."
PVD = ["Plating: PVD 18K gold coating, anti-tarnish",
       "PVD vs plating: Regular plating is a soft layer that wears off over time. PVD is bonded to the metal in a vacuum, so it is far "
       "harder, stands up to sweat and keeps its colour much longer."]
VIEWS = ["on a cream plaster block, the full piece", "worn on the model", "worn on the wrist, close", None]
def first_sentence(s): return re.split(r"(?<=[.!?])\s", s.strip())[0]
for p in COPY:
    t, h = p["title"], p["handle"]
    details = ["Length: Approximately 17cm", f"Stone: {p['stone']}", "Setting: Square gold four claw settings, linked edge to edge",
               "Closure: Fold over clasp"] + ([f"Stone note: {p['stone_note']}"] if p["stone_note"] else []) + ["Finish: Polished gold tone"] + PVD
    body = (f"<p>{e(p['tagline'])} {e(p['body'])}</p><p><strong>STYLING TIP:</strong> {e(p['tip'])}</p><p><strong>Details</strong></p><ul>\n"
            + "".join(f"<li>{e(x)}</li>\n" for x in details)
            + f"</ul><p><img src=\"{SG[h]}\" alt=\"Size guide — {e(t)}\" width=\"420\"></p>"
            + f"<p><strong>Care</strong></p><p>{e(CARE)}</p><p>You will receive your piece in a Naira Petite box.</p>")
    files = [{"originalSource": URL[f"{h}-0{i}.jpg"], "alt": f"{t} — {v or 'macro detail: ' + p['macro']}", "contentType": "IMAGE"}
             for i, v in enumerate(VIEWS, 1)]
    inp = {"title": t, "handle": h, "status": "ACTIVE", "vendor": "Naira Petite", "productType": "Bracelet",
           "category": "gid://shopify/TaxonomyCategory/aa-6-3",
           "tags": ["18k Gold Tone Plated", "Aditya", "Bracelet", "Cubic Zirconia", "Demi Fine", "Naira Petite", "Tennis"],
           "descriptionHtml": body, "seo": {"title": f"{t} — Bracelet | Naira Petite", "description": f"{first_sentence(p['body'])} {t} by Naira Petite."},
           "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}],
           "variants": [{"optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": p["sku"], "price": PRICE, "compareAtPrice": COMPARE,
                         "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
                         "inventoryQuantities": [{"locationId": LOCATION, "name": "available", "quantity": UNITS}]}],
           "files": files,
           "metafields": [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field", "value": "Apparel & Accessories > Jewelry > Bracelets"},
                          {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
                          {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
                          {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
                          {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": "191"}]}
    json.dump(inp, open(f"{S}/payloads/{h}.json", "w"), ensure_ascii=False, indent=1)
    print(h, p["sku"], len(files), "images")
