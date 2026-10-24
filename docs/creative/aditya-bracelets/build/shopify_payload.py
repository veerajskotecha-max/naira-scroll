# Builds the Shopify productSet input for each Aditya bracelet (DRAFT, vendor Naira Petite) from shopify/listing.json in the
# store's house description format (intro, STYLING TIP, Details list, size guide, Care, box line). Prices are left unset for the
# owner; every variant is tracked with 5 units at the main location. Images come from their public URLs (url_map.json).
# Usage: shopify_payload.py  -> shopify/payloads/<handle>.json
import json, os, re, html
H = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(H, "../shopify")
L = json.load(open(f"{S}/listing.json")); EMAP = json.load(open(f"{H}/export_map.json")); URL = json.load(open(f"{H}/url_map.json"))
SG = json.load(open(f"{S}/sizeguide_urls.json"))
LOCATION = "gid://shopify/Location/76267389090"; UNITS = 5
e = html.escape
# Base metal unknown for these pieces (only the clear round card says stainless steel), so the plain care line and no
# waterproof / tarnish-free / hypoallergenic claims, as the house does for unknown-material products.
CARE = "Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch."
GCAT = ("Apparel & Accessories > Jewelry > Bracelets", "191")
def first_sentence(s): return re.split(r"(?<=[.!?])\s", s.strip())[0]
os.makedirs(f"{S}/payloads", exist_ok=True)
for p in L:
    t = p["title"]
    body = (f"<p>{e(p['tagline'])} {e(p['body'])}</p><p><strong>STYLING TIP:</strong> {e(p['tip'])}</p><p><strong>Details</strong></p><ul>\n"
            + "".join(f"<li>{e(x)}</li>\n" for x in p["details"])
            + f"</ul><p><img src=\"{SG[p['handle']]}\" alt=\"Size guide — {e(t)}\" width=\"420\"></p>"
            + f"<p><strong>Care</strong></p><p>{e(CARE)}</p><p>You will receive your piece in a Naira Petite box.</p>")
    tags = ["Bracelet", "Cubic Zirconia", "Demi Fine", "Naira Petite", "Aditya",
            "18k Gold Tone Plated" if p["metal"] == "gold" else "Rhodium Silver Tone Plated"] + (["Tennis"] if p["tennis"] else [])
    files, by_key = [], {}
    values = [v.get("value") for v in p["variants"] if v.get("value")]
    for k, alt in p["images"]:
        head, _, rest = alt.partition(", ")
        f = {"originalSource": URL[EMAP[k]], "alt": f"{t}, {head} — {rest}" if head in values else f"{t} — {alt}", "contentType": "IMAGE"}
        files.append(f); by_key[k] = f
    opt = p.get("option")
    variants = []
    for v in p["variants"]:
        var = {"optionValues": [{"optionName": opt or "Title", "name": v.get("value", "Default Title")}], "sku": v["sku"], "inventoryPolicy": "DENY",
               "inventoryItem": {"tracked": True}, "inventoryQuantities": [{"locationId": LOCATION, "name": "available", "quantity": UNITS}]}
        if opt: var["file"] = dict(by_key[f"{v['src']}_H"])
        variants.append(var)
    vals = [v.get("value", "Default Title") for v in p["variants"]]
    inp = {"title": t, "handle": p["handle"], "status": "DRAFT", "vendor": "Naira Petite", "productType": "Bracelet", "tags": sorted(set(tags)),
           "descriptionHtml": body, "seo": {"title": f"{t} — Bracelet | Naira Petite", "description": f"{first_sentence(p['body'])} {t} by Naira Petite."[:320]},
           "productOptions": [{"name": opt or "Title", "values": [{"name": x} for x in vals]}], "variants": variants, "files": files,
           "metafields": [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field", "value": GCAT[0]},
                          {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
                          {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
                          {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
                          {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": GCAT[1]}]}
    json.dump(inp, open(f"{S}/payloads/{p['handle']}.json", "w"), ensure_ascii=False, indent=1)
    print(p["handle"], len(variants), "variants,", len(files), "images")
