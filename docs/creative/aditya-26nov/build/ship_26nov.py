# One Shopify mutation (one approval) creating the seven Aditya pieces of 26 Nov 2026 as DRAFTS: copy, price at 3.5x the
# supplier price written on each photo (cost per item = that price), SKU, 10 units at Forest Colony Parijat Nagar, the
# category and feed metafields, the gallery (packshot, worn, worn close, macro: the owner's four photos, no palm) and the
# size card last, which the description also shows. autoPublish is set on the six sales channels around the creates and
# set back afterwards (as ../../stock-2nov/build/ship_new.py), so each piece is on every channel when the owner sets it Active.
# Tags and the description format follow ../../aditya-jewellery/build/shopify_payload.py (the 27 Oct Aditya listings: plain
# care line, no PVD / waterproof / tarnish claims, no compare-at price).
# Usage: python3 -I ship_26nov.py [-o NAME] [K01 K02 ...] -> ../shopify/NAME.json (variables) and ../shopify/NAME.graphql
# (NAME defaults to ship_26nov, the first seven; the second batch, K08 to K13, is ship_26nov_b2).
import html, json, os, re
H = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(H, "../shopify")
L = json.load(open(f"{S}/listing.json")); EMAP = json.load(open(f"{H}/export_map.json")); URL = json.load(open(f"{H}/url_map.json"))
LOCATION = "gid://shopify/Location/76267389090"; CDN = "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/"
PUBS = ["164676042914", "164676108450", "167637745826", "175106293922", "180607254690", "180607746210"]
CARE = "Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch."
# The store's ring-size category entries (shopify--ring-size metaobjects 5, 6, 7, 8), as on the live Lumière Oval Solitaire Ring,
# so the adjustable rings show in the storefront's size filter. There is no US 9 entry in the store.
RING_MO = {"5": "gid://shopify/Metaobject/246807953570", "6": "gid://shopify/Metaobject/246807986338", "7": "gid://shopify/Metaobject/246807920802", "8": "gid://shopify/Metaobject/643878125730"}
RING_SIZES = list(RING_MO.values())   # default; a listing may narrow it with "ring_sizes" (the marquise duet ring fits about US 6 to 8)
CAT = {"Necklace": ("aa-6-8", "Necklaces", "196"), "Earrings": ("aa-6-6", "Earrings", "194"), "Ring": ("aa-6-9", "Rings", "200")}
e = html.escape
def first_sentence(s): return re.split(r"(?<=[.!?])\s", s.strip())[0]
# Media held back from the create (shipped later with the reshoot): the marquise studs' packshot has a small drawn sparkle star on
# one stone tip (an AI tell, the owner wants a finish that does not look AI), and its size card is drawn on that packshot.
HOLD_MEDIA = {"K02"}
ONLY = None   # set by the command line: the keys to create in this run (default: every listing)
def product(p):
    t, typ = p["title"], p["type"]; cat, gleaf, fb = CAT[typ]; card = f"{p['handle']}-size-guide.jpg"
    # a card replaced after the create keeps its filename but the plain CDN URL stays cached for a year: link its ?v= version
    src = f"{CDN}{card}" + (f"?v={p['card_v']}" if p.get("card_v") else "")
    if p["key"] in HOLD_MEDIA: URL_ = {}
    else: URL_ = URL
    body = (f"<p>{e(p['tagline'])} {e(p['body'])}</p><p><strong>STYLING TIP:</strong> {e(p['tip'])}</p><p><strong>Details</strong></p><ul>\n"
            + "".join(f"<li>{e(x)}</li>\n" for x in p["details"]) + "</ul>"
            + f"<p><img src=\"{src}\" alt=\"Size guide — {e(t)}\" width=\"420\"></p>"
            + f"<p><strong>Care</strong></p><p>{e(CARE)}</p><p>You will receive your piece in a Naira Petite box.</p>")
    files = [{"originalSource": URL_[EMAP[slot]], "alt": f"{t} — {alt}", "contentType": "IMAGE"} for slot, alt in p["images"] if slot in EMAP and EMAP[slot] in URL_]
    has_card = card in URL_                                       # a piece whose card is not drawn yet ships without it
    if not has_card: body = body.replace(f"<p><img src=\"{src}\" alt=\"Size guide — {e(t)}\" width=\"420\"></p>", "")
    else: files.append({"originalSource": URL_[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    variant = {"optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": p["sku"], "price": f"{p['price']:.2f}",
               "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True, "cost": f"{p['cost']:.2f}"},
               "inventoryQuantities": [{"locationId": LOCATION, "name": "available", "quantity": p["units"]}],
               **({"file": {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}} if files and not files[0].get("filename") else {})}
    tags = sorted({typ, "Demi Fine", "Naira Petite", "Aditya", "18k Gold Tone Plated", *p["extra_tags"]})
    return {"title": t, "handle": p["handle"], "status": "DRAFT", "vendor": "Naira Petite", "productType": typ,
            "category": f"gid://shopify/TaxonomyCategory/{cat}", "tags": tags, "descriptionHtml": body,
            "seo": {"title": f"{t} — {typ} | Naira Petite", "description": p.get("seo") or f"{first_sentence(p['body'])} {t} by Naira Petite."[:320]},
            "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [variant], "files": files,
            "metafields": [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field", "value": f"Apparel & Accessories > Jewelry > {gleaf}"},
                           {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
                           {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
                           {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
                           {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": fb}]
                          + ([{"namespace": "shopify", "key": "ring-size", "type": "list.metaobject_reference", "value": json.dumps([RING_MO[x] for x in p["ring_sizes"]] if p.get("ring_sizes") else RING_SIZES)}] if typ == "Ring" else [])}
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]; NAME = "ship_26nov"
    if args[:1] == ["-o"]: NAME, args = args[1], args[2:]
    if args: L = [p for p in L if p["key"] in args]
    ids = [p["key"].lower() for p in L]
    var = {"on": {"autoPublish": True}, "off": {"autoPublish": False}}
    for p in L: var[p["key"].lower()] = product(p)
    sel = "{ publication { id autoPublish } userErrors { field message } }"
    ps = ("{ product { id handle status totalInventory mediaCount { count } variants(first: 1) { nodes { id sku price inventoryQuantity "
          "inventoryItem { unitCost { amount } } } } } userErrors { field message code } }")
    doc = ("mutation Aditya26Nov($on: PublicationUpdateInput!, $off: PublicationUpdateInput!, " + ", ".join(f"${i}: ProductSetInput!" for i in ids) + ") {\n"
           + "".join(f"  on{n}: publicationUpdate(id: \"gid://shopify/Publication/{pub}\", input: $on) {sel}\n" for n, pub in enumerate(PUBS))
           + "".join(f"  {i}: productSet(input: ${i}, synchronous: true) {ps}\n" for i in ids)
           + "".join(f"  off{n}: publicationUpdate(id: \"gid://shopify/Publication/{pub}\", input: $off) {sel}\n" for n, pub in enumerate(PUBS)) + "}\n")
    json.dump(var, open(f"{S}/{NAME}.json", "w"), ensure_ascii=False, separators=(",", ":"))
    open(f"{S}/{NAME}.graphql", "w").write(doc)
    for p in L: v = var[p["key"].lower()]; print(p["sku"], v["handle"], v["variants"][0]["price"], "cost", v["variants"][0]["inventoryItem"]["cost"], len(v["files"]), "files", v["tags"])
