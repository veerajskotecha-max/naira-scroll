# Builds the Shopify productSet input for each Aditya piece (DRAFT, vendor Naira Petite) from shopify/listing.json in the
# store's house description format (intro, STYLING TIP, Details list, size guide where there is one, Care, box line).
# Price is 3.5x the supplier's price on the call photos (the owner's rule for phase 2, 25 Oct); cost per item is that
# supplier price. Pieces whose photo showed no price stay unpriced.
# Every variant is tracked with 5 units at the main location. Images come from their public URLs (url_map.json).
# Usage: shopify_payload.py [HANDLE ...]  -> shopify/payloads/<handle>.json (every piece, or just the handles given)
import json, os, re, html, sys
H = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(H, "../shopify")
L = json.load(open(f"{S}/listing.json")); EMAP = json.load(open(f"{H}/export_map.json")); URL = json.load(open(f"{H}/url_map.json"))
SG = json.load(open(f"{S}/sizeguide_urls.json"))
LOCATION = "gid://shopify/Location/76267389090"; UNITS = 5
e = html.escape
# Base metal unknown for these pieces (only the ear cuff's card says stainless steel), so the plain care line and no
# waterproof / tarnish-free / hypoallergenic claims, as in aditya-bracelets. Pearls get the house pearl care line.
CARE = {"plain": "Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch.",
        "pearl": "Pearls are softer than metal and do not like chemicals. Put it on after perfume, moisturiser and hairspray, keep it out of the shower, the pool and the sea, and wipe it with a soft dry cloth after wearing. Store it flat in its pouch, away from anything that could scratch the surface."}
# type -> (Shopify taxonomy category, Google category, Facebook category id), as on the live pieces of each type
CAT = {"Necklace": ("gid://shopify/TaxonomyCategory/aa-6-8", "Apparel & Accessories > Jewelry > Necklaces", "196"),
       "Earrings": ("gid://shopify/TaxonomyCategory/aa-6-6", "Apparel & Accessories > Jewelry > Earrings", "194"),
       "Ring": ("gid://shopify/TaxonomyCategory/aa-6-9", "Apparel & Accessories > Jewelry > Rings", "200"),
       "Bracelet": ("gid://shopify/TaxonomyCategory/aa-6-3", "Apparel & Accessories > Jewelry > Bracelets", "191")}
def first_sentence(s): return re.split(r"(?<=[.!?])\s", s.strip())[0]
os.makedirs(f"{S}/payloads", exist_ok=True); only = set(sys.argv[1:])
for p in L:
    if only and p["handle"] not in only: continue
    t, typ = p["title"], p["type"]; cat, gcat, fcat = CAT[typ]
    guide = (f"<p><img src=\"{SG[p['handle']]}\" alt=\"Size guide — {e(t)}\" width=\"420\"></p>" if p["handle"] in SG else "")
    body = (f"<p>{e(p['tagline'])} {e(p['body'])}</p><p><strong>STYLING TIP:</strong> {e(p['tip'])}</p><p><strong>Details</strong></p><ul>\n"
            + "".join(f"<li>{e(x)}</li>\n" for x in p["details"]) + "</ul>" + guide
            + f"<p><strong>Care</strong></p><p>{e(CARE[p['care']])}</p><p>You will receive your piece in a Naira Petite box.</p>")
    tags = [typ, "Demi Fine", "Naira Petite", "Aditya", "18k Gold Tone Plated"] + p["extra_tags"]
    files = [{"originalSource": URL[EMAP[k]], "alt": f"{t} — {alt}", "contentType": "IMAGE"} for k, alt in p["images"]]
    item = {"tracked": True, **({"cost": str(p["cost"])} if p["cost"] else {})}
    variant = {"optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": p["sku"], "inventoryPolicy": "DENY",
               **({"price": str(p["price"])} if p.get("price") else {}),
               "inventoryItem": item, "inventoryQuantities": [{"locationId": LOCATION, "name": "available", "quantity": UNITS}]}
    inp = {"title": t, "handle": p["handle"], "status": "DRAFT", "vendor": "Naira Petite", "productType": typ, "category": cat,
           "tags": sorted(set(tags)), "descriptionHtml": body,
           "seo": {"title": f"{t} — {typ} | Naira Petite", "description": f"{first_sentence(p['body'])} {t} by Naira Petite."[:320]},
           "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [variant], "files": files,
           "metafields": [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field", "value": gcat},
                          {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
                          {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
                          {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
                          {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": fcat}]}
    json.dump(inp, open(f"{S}/payloads/{p['handle']}.json", "w"), ensure_ascii=False, indent=1)
    print(p["sku"], p["handle"], typ, len(files), "images,", "cost", p["cost"], "price", p.get("price"), "| guide" if guide else "")
