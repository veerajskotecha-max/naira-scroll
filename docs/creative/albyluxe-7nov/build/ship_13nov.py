# One Shopify mutation (one approval), 13 Nov 2026, for the owner's "Ship approved ones, hold ones keep data stored we will
# use later": the four pieces marked Approve on the approval page (https://claude.ai/artifact/TTS2ManafPXJ3ujNQaNSLR,
# collection approve, read 13 Nov 01:10 UTC): L01, L02, L03 and L06, at the prices and units the owner set there.
#  - Each is created with its one variant (stock at the shop's one location), its photos in frames.json order, its first
#    photo as the variant image, and the size card last as <handle>-size-guide.jpg, the name the description's size-guide
#    image links to (no file of that name was in the store's Files on 13 Nov, so none is renamed).
#  - No status is sent (the house rule for productSet). A new product is ACTIVE by default, as the approval page promised
#    ("Approved pieces go live on all six sales channels in one batch"). autoPublish is turned on for the six sales channels
#    just before the productSets and back off right after them, as ../../albyluxe-31oct/build/ship_31oct.py.
#  - Type, category, SEO and the Google / Facebook category metafields as ship_31oct.py (the live ring listings). Tags are
#    the store's: no claim of waterproof, tarnish-free or hypoallergenic. L06 has no cubic zirconia, so it is tagged Pearl.
# The 12 pieces on Hold (L04, L05, L08 to L13, L15 to L18) and the two with no choice saved (L07, L14) are not sent. Their
# photos, copy, size cards and page choices stay here to ship later.
# Usage: python3 -I ship_13nov.py -> ../shopify/ship_13nov.json (variables) and ../shopify/ship_13nov.graphql (the mutation)
import importlib.util, json, os, re
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s31", os.path.join(H, "../../albyluxe-31oct/build/ship_31oct.py"))
S31 = importlib.util.module_from_spec(s); s.loader.exec_module(S31)
L = {x["id"]: x for x in json.load(open(os.path.join(H, "listings.json")))}
F = json.load(open(os.path.join(H, "frames.json"))); URL = json.load(open(os.path.join(H, "url_map.json")))

SHIP = ["L01", "L02", "L03", "L06"]
# what the owner changed on the page (approve/<id>): L01 and L02 at Rs 1,249; L01 and L03 at 12 units. Compare-at as listed.
OWNER = {"L01": {"price": 1249, "units": 12}, "L02": {"price": 1249}, "L03": {"units": 12}, "L06": {}}
TAGS = {"L01": ["Cubic Zirconia"], "L02": ["Cubic Zirconia"], "L03": ["Cubic Zirconia"], "L06": ["Pearl"]}
BASE = ["18k Gold Tone Plated", "Adjustable", "Albyluxe", "Demi Fine", "Naira Petite", "Ring"]
MACRO = {"L01": "macro detail of the oval stone and the molten strands", "L02": "macro detail of the marquise stone and the molten bar",
         "L03": "macro detail of the two clusters", "L06": "macro detail of the baroque shell pearl and the gold tone nugget"}
NEVER = re.compile(r"\b(real|diamonds?|waterproof|tarnish\w*|anti-tarnish|freshwater|hypoallergenic)\b", re.I)


def alt(i, key):
    shot = re.match(r"L\d+_(W\d|H|M)", key).group(1)
    return MACRO[i] if shot == "M" else S31.ALTS["Ring"][shot]


def product(i):
    x = dict(L[i]); x.update(OWNER[i]); t, h = x["title"], S31.handle(x["title"])
    ptype, cat, gcat, fb = S31.TYPES[x["type"]]
    files = [{"originalSource": URL[f"{h}-{n:02d}.jpg"], "alt": f"{t} — {alt(i, key)}", "contentType": "IMAGE"}
             for n, key in enumerate(F[i][""], 1)]
    card = f"{h}-size-guide.jpg"
    files.append({"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    variant = {"optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": x["sku"], "price": S31.money(x["price"]),
               "compareAtPrice": S31.money(x["compare"]), "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
               "inventoryQuantities": [{"locationId": S31.LOCATION, "name": "available", "quantity": x["units"]}],
               "file": {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}}
    second = x["intro"].split(". ")[1].rstrip(".")
    p = {"title": t, "handle": h, "vendor": "Naira Petite", "productType": ptype, "category": f"gid://shopify/TaxonomyCategory/{cat}",
         "tags": sorted(BASE + TAGS[i]), "descriptionHtml": S31.body(x, h),
         "seo": {"title": f"{t} — {ptype} | Naira Petite", "description": f"{second}. {t} by Naira Petite."},
         "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [variant], "files": files,
         "metafields": [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field",
                         "value": f"Apparel & Accessories > Jewelry > {gcat}"},
                        {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
                        {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
                        {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
                        {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": fb}]}
    words = json.dumps([p["title"], p["descriptionHtml"], p["seo"], p["tags"], [f["alt"] for f in files]], ensure_ascii=False)
    assert not NEVER.search(words), (i, NEVER.search(words).group(0))
    assert "status" not in p and len(p["seo"]["description"]) <= 320, i
    return p


if __name__ == "__main__":
    var = {"on": {"autoPublish": True}, "off": {"autoPublish": False}}
    for i in SHIP: var[i.lower()] = product(i)
    sel = "{ publication { id autoPublish } userErrors { field message } }"
    ps = ("{ product { id handle status totalInventory variants(first: 3) { nodes { id sku price compareAtPrice inventoryQuantity } } "
          "media(first: 10) { nodes { id status } } } userErrors { field message code } }")
    doc = ("mutation Ship13Nov($on: PublicationUpdateInput!, $off: PublicationUpdateInput!, "
           + ", ".join(f"${i.lower()}: ProductSetInput!" for i in SHIP) + ") {\n"
           + "".join(f"  on{n}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $on) {sel}\n" for n, p in enumerate(S31.PUBS))
           + "".join(f"  {i.lower()}: productSet(input: ${i.lower()}, synchronous: true) {ps}\n" for i in SHIP)
           + "".join(f"  off{n}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $off) {sel}\n" for n, p in enumerate(S31.PUBS))
           + "}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_13nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_13nov.graphql"), "w").write(doc)
    for i in SHIP:
        p = var[i.lower()]; v = p["variants"][0]
        print(i, p["handle"], v["sku"], v["price"], v["compareAtPrice"], v["inventoryQuantities"][0]["quantity"], "units",
              len(p["files"]), "files", p["tags"], len(p["seo"]["description"]), "seo chars")
