# One Shopify mutation (one approval) for the three pieces fixed on 2 Nov 2026 against the owner's photos of the stock in hand, all DRAFT:
#  - A08 Bow and Heart Gift Set and A12 Heart Solitaire Huggies are updated in place (productSet with identifier {id}): new photos,
#    new size card, corrected copy. Their variant keeps its id, SKU, price and stock (no inventoryQuantities sent). The file list is
#    replaced, so the 1 Nov photos drop off the product. The new size card is <handle>-size-guide-v2.jpg, because the 1 Nov card
#    already holds the plain name in Shopify Files, and the description's size-guide image links to the -v2 name.
#  - A16 Herringbone Teardrop Necklace (held on 31 Oct) is created as a DRAFT with 5 units.
# Tags, category, SEO and the feed metafields follow ../../albyluxe-31oct/build/ship_31oct.py.
# Usage: ship_2nov.py -> ../shopify/ship_2nov.json (variables) and ../shopify/ship_2nov.graphql (the mutation)
import importlib.util, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s31", os.path.join(H, "../../albyluxe-31oct/build/ship_31oct.py"))
S31 = importlib.util.module_from_spec(s); s.loader.exec_module(S31)
L = {x["id"]: x for x in json.load(open(os.path.join(H, "listings.json")))}
OLD = {x["id"]: x for x in S31.L}
F = json.load(open(os.path.join(H, "frames.json"))); URL = json.load(open(os.path.join(H, "url_map.json")))
EXISTING = {"A08": ("gid://shopify/Product/10375501578402", "gid://shopify/ProductVariant/50785485160610"),
            "A12": ("gid://shopify/Product/10375501709474", "gid://shopify/ProductVariant/50785485291682")}
e = S31.e

def body(x, card):
    return (f"<p>{e(x['intro'])}</p><p><strong>STYLING TIP:</strong> {e(x['tip'])}</p><p><strong>Details</strong></p><ul>\n"
            + "".join(f"<li>{e(d)}</li>\n" for d in x["details"])
            + f"</ul><p><img src=\"{S31.CDN}{card}\" alt=\"Size guide — {e(x['title'])}\" width=\"420\"></p>"
            + f"<p><strong>Care</strong></p><p>{e(S31.CARE)}</p><p>You will receive your piece in a Naira Petite box.</p>")

def product(i):
    x = dict(L[i]); x["code"] = OLD[i]["code"]; t, h = x["title"], S31.handle(x["title"]); ptype, cat, gcat, fb = S31.TYPES[x["type"]]
    card = f"{h}-size-guide-v2.jpg" if i in EXISTING else f"{h}-size-guide.jpg"
    files = []
    for n, key in enumerate(F[i][""], 1):
        files.append({"originalSource": URL[f"{h}-{n:02d}.jpg"], "alt": f"{t} — {S31.ALTS[x['type']][S31.shot(key)]}", "contentType": "IMAGE"})
    files.append({"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    v = {"optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": x["sku"], "price": S31.money(x["price"]),
         "compareAtPrice": S31.money(x["compare"]), "inventoryPolicy": "DENY", "file": {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}}
    if i in EXISTING: v["id"] = EXISTING[i][1]
    else: v.update({"inventoryItem": {"tracked": True}, "inventoryQuantities": [{"locationId": S31.LOCATION, "name": "available", "quantity": x["units"]}]})
    second = x["intro"].split(". ")[1].rstrip(".")
    return {"title": t, "handle": h, "status": "DRAFT", "vendor": "Naira Petite", "productType": ptype,
            "category": f"gid://shopify/TaxonomyCategory/{cat}", "tags": S31.tags(x, ptype), "descriptionHtml": body(x, card),
            "seo": {"title": f"{t} — {ptype} | Naira Petite", "description": f"{second}. {t} by Naira Petite."},
            "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [v], "files": files,
            **({} if i in EXISTING else {"metafields": METAFIELDS(gcat, fb)})}

def METAFIELDS(gcat, fb):                     # left out of the updates: productSet replaces the whole list, and the drafts also hold global SEO tags
    return [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field",
                            "value": f"Apparel & Accessories > Jewelry > {gcat}"},
                           {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
                           {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
                           {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
                           {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": fb}]

if __name__ == "__main__":
    ids = ["A08", "A12", "A16"]; var = {i.lower(): product(i) for i in ids}
    for i in EXISTING: var[f"{i.lower()}id"] = {"id": EXISTING[i][0]}
    ps = ("{ product { id handle status totalInventory mediaCount { count } variants(first: 3) { nodes { id sku price compareAtPrice inventoryQuantity } } } "
          "userErrors { field message code } }")
    doc = ("mutation Fix2Nov($a08: ProductSetInput!, $a12: ProductSetInput!, $a16: ProductSetInput!, $a08id: ProductSetIdentifiers!, $a12id: ProductSetIdentifiers!) {\n"
           f"  a08: productSet(identifier: $a08id, input: $a08, synchronous: true) {ps}\n"
           f"  a12: productSet(identifier: $a12id, input: $a12, synchronous: true) {ps}\n"
           f"  a16: productSet(input: $a16, synchronous: true) {ps}\n}}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_2nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_2nov.graphql"), "w").write(doc)
    for i in ids: p = var[i.lower()]; print(i, p["handle"], p["status"], len(p["files"]), "files", p["tags"])
