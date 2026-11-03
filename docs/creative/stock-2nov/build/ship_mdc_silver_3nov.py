# One Shopify mutation (one approval), 3 Nov 2026, for the owner's note on the live Marquise Drop Choker (Edition Two, YF7059, gold):
#   "Add same 10 in silver"
#  - A Metal option, Gold and Silver, as on the Kiss Knot Bangle and the Droplet Open Cuff. The gold variant keeps its id, SKU YF7059,
#    price, compare-at, cost and stock (none of them are sent) and takes the gold cube photo as its image.
#  - A Silver variant: SKU YF7059-S at the gold's price and compare-at (Rs 1,199 against 2,388), 10 units, inventory policy DENY;
#    no cost per item was given for the silver.
#  - The gallery keeps every live media by id (five gold photos, the gift box, the size card) and adds the five silver photos after the
#    gold ones: Higgsfield edits of the live gold photos with only the metal changed (edits.py MDC_*s).
#  - The description's "Plating: PVD 18K gold coating" line now names both metals; nothing else in it changes. Tag Rhodium Silver Tone
#    Plated is added (tagsAdd, so the other tags are not resent). No status, title, SEO or price of the gold is changed.
# Usage: ship_mdc_silver_3nov.py -> ../shopify/ship_mdc_silver_3nov.json (variables) and ../shopify/ship_mdc_silver_3nov.graphql
import json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify"); URL = json.load(open(os.path.join(H, "url_map.json")))
PRODUCT = "gid://shopify/Product/10344382726306"; GOLD = "gid://shopify/ProductVariant/50651979415714"
LOCATION = "gid://shopify/Location/76267389090"
GOLD_MEDIA = ["gid://shopify/MediaImage/46458302136482", "gid://shopify/MediaImage/46532695720098", "gid://shopify/MediaImage/46532695752866",
              "gid://shopify/MediaImage/46532695785634", "gid://shopify/MediaImage/46626492580002"]
BOX, CARD = "gid://shopify/MediaImage/37245466149026", "gid://shopify/MediaImage/46509171867810"
T = "Marquise Drop Choker"
SILVER_ALTS = ["macro detail: marquise stone and the start of the drop", "worn at the base of the neck, the drop falling over the breastbone",
               "macro detail: the sideways marquise in its claws on the ribbed collar", "worn, close on the collarbones",
               "the ribbed collar, the marquise and the drop laid on ivory"]
OLD_LINE = "<li>Plating: PVD 18K gold coating, anti-tarnish</li>"
NEW_LINE = "<li>Metal: Gold, with a PVD 18K gold coating, or silver tone</li>"

def body(live):
    assert live.count(OLD_LINE) == 1, "the plating line changed on Shopify; read the live description again"
    return live.replace(OLD_LINE, NEW_LINE)

def product(live_html):
    silver = [{"originalSource": URL[f"marquise-drop-choker-silver-0{n}.jpg"], "contentType": "IMAGE", "alt": f"{T} in silver — {a}"}
              for n, a in enumerate(SILVER_ALTS, 1)]
    files = [{"id": m} for m in GOLD_MEDIA] + silver + [{"id": BOX}, {"id": CARD}]
    variants = [{"id": GOLD, "optionValues": [{"optionName": "Metal", "name": "Gold"}], "file": {"id": GOLD_MEDIA[0]}},
                {"optionValues": [{"optionName": "Metal", "name": "Silver"}], "sku": "YF7059-S", "price": "1199.00", "compareAtPrice": "2388.00",
                 "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
                 "inventoryQuantities": [{"locationId": LOCATION, "name": "available", "quantity": 10}],
                 "file": {"originalSource": silver[0]["originalSource"], "contentType": "IMAGE"}}]
    return {"title": T, "handle": "marquise-drop-choker", "descriptionHtml": body(live_html),
            "productOptions": [{"name": "Metal", "values": [{"name": "Gold"}, {"name": "Silver"}]}], "variants": variants, "files": files}

if __name__ == "__main__":
    live = json.load(open(os.path.join(H, "mdc_live.json")))["descriptionHtml"]      # read from Shopify just before the ship
    var = {"id": {"id": PRODUCT}, "p": product(live), "pid": PRODUCT, "tags": ["Rhodium Silver Tone Plated"]}
    doc = ("mutation MarquiseDropSilver($id: ProductSetIdentifiers!, $p: ProductSetInput!, $pid: ID!, $tags: [String!]!) {\n"
           "  p: productSet(identifier: $id, input: $p, synchronous: true) { product { id handle status totalInventory options { name optionValues { name } } "
           "mediaCount { count } variants(first: 3) { nodes { id sku title price compareAtPrice inventoryQuantity } } } userErrors { field message code } }\n"
           "  t: tagsAdd(id: $pid, tags: $tags) { node { id } userErrors { field message } }\n}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_mdc_silver_3nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_mdc_silver_3nov.graphql"), "w").write(doc)
    p = var["p"]; print(len(p["files"]), "files;", [v.get("sku", v.get("id")) for v in p["variants"]]); print(NEW_LINE in p["descriptionHtml"])
