# Builds one Shopify mutation (one approval) for the two pieces the owner sent on 30 Oct 2026:
#  - Clover Garland Bracelet: one listing, Colour Sky Blue / Pink / White, 5 units each, Rs 1,299 against Rs 2,500 (the Carré and
#    Clarté lines' price). Four photos per colour, each colour's hero as its variant image, then the size card.
#  - Rivière Classique Necklace: one listing, Metal Silver / Gold, 10 units each, Rs 1,499 against Rs 2,800 (the Lumière Oval
#    Necklace's price). Four photos per metal, then the size card.
# Both are created ACTIVE. ProductSetInput cannot publish, so the mutation turns autoPublish on for the six sales channels just
# before the two productSets and back off right after them (as ../../aditya-bracelets/build/ship_27oct.py).
# The size cards go in as the galleries' last photo under <handle>-size-guide.jpg, the name each description's image links to.
# Copy rules: gold tone / silver tone and cubic zirconia; no waterproof, tarnish-free or hypoallergenic claims (base metal and
# plating are not confirmed, except the clover card's "Stainless Steel" sleeve).
# Usage: ship_30oct.py  (reads url_map.json: export filename -> public URL)
#        -> ../shopify/ship_30oct.json (variables) and ../shopify/ship_30oct.graphql (the mutation)
import html, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
URL = json.load(open(os.path.join(H, "url_map.json")))
LOCATION = "gid://shopify/Location/76267389090"
CDN = "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/"
PUBS = ["164676042914", "164676108450", "167637745826", "175106293922", "180607254690", "180607746210"]
CARE = "Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch."
e = html.escape


def meta(kind, fb):
    return [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field",
             "value": f"Apparel & Accessories > Jewelry > {kind}"},
            {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
            {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
            {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
            {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": fb}]


def body(title, handle, intro, tip, details):
    return (f"<p>{e(intro)}</p><p><strong>STYLING TIP:</strong> {e(tip)}</p><p><strong>Details</strong></p><ul>\n"
            + "".join(f"<li>{e(x)}</li>\n" for x in details)
            + f"</ul><p><img src=\"{CDN}{handle}-size-guide.jpg\" alt=\"Size guide — {e(title)}\" width=\"420\"></p>"
            + f"<p><strong>Care</strong></p><p>{e(CARE)}</p><p>You will receive your piece in a Naira Petite box.</p>")


def product(p):
    t, h, opt = p["title"], p["handle"], p["option"]
    files, variants = [], []
    for i, (value, sku) in enumerate(p["values"]):
        shots = [f"{h}-{4 * i + n:02d}.jpg" for n in range(1, 5)]
        for fn, alt in zip(shots, p["alts"]):
            files.append({"originalSource": URL[fn], "alt": f"{t}, {value} — {alt}", "contentType": "IMAGE"})
        variants.append({"optionValues": [{"optionName": opt, "name": value}], "sku": sku, "price": p["price"],
                         "compareAtPrice": p["compare"], "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
                         "inventoryQuantities": [{"locationId": LOCATION, "name": "available", "quantity": p["units"]}],
                         "file": {"originalSource": URL[shots[0]], "contentType": "IMAGE"}})
    card = f"{h}-size-guide.jpg"
    files.append({"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    return {"title": t, "handle": h, "status": "ACTIVE", "vendor": "Naira Petite", "productType": p["type"],
            "category": p["category"], "tags": p["tags"], "descriptionHtml": body(t, h, p["intro"], p["tip"], p["details"]),
            "seo": {"title": f"{t} | Naira Petite", "description": f"{p['intro'].split('. ')[1]}. {t} by Naira Petite."},
            "productOptions": [{"name": opt, "values": [{"name": v} for v, _ in p["values"]]}],
            "variants": variants, "files": files, "metafields": meta(p["kind"], p["fb"])}


CLOVER = {
    "title": "Clover Garland Bracelet", "handle": "clover-garland-bracelet", "type": "Bracelet", "kind": "Bracelets", "fb": "191",
    "category": "gid://shopify/TaxonomyCategory/aa-6-3", "option": "Colour", "units": 5, "price": "1299.00", "compare": "2500.00",
    "values": [("Sky Blue", "CLG-SB"), ("Pink", "CLG-PK"), ("White", "CLG-WH")],
    "tags": ["18k Gold Tone Plated", "Bracelet", "Clover", "Cubic Zirconia", "Demi Fine", "Naira Petite"],
    "intro": ("A garland of tiny clovers. Fifteen small four petal clovers, each four round stones in gold tone cups with a fine "
              "beaded rim around one small clear stone at the centre, are linked petal to petal by fine gold rings, so the line "
              "moves softly with the wrist. In sky blue, rose pink or clear white."),
    "tip": "Wear one alone, or the sky blue and the pink together on one wrist.",
    "details": ["Clovers: Fifteen, approximately 10mm across, linked petal to petal by small gold tone rings",
                "Stones: Four round cubic zirconia petals per clover, approximately 3.5mm, around a small clear centre stone",
                "Colours: Sky Blue, Pink or White",
                "Setting: Gold tone cups with a fine beaded rim",
                "Length: Approximately 17cm, adjustable to about 21cm with the extender",
                "Closure: Lobster clasp with an extender chain",
                "Metal: Stainless steel, polished gold tone"],
    "alts": ["on a cream plaster block, the full piece", "worn on the model's wrist", "worn close, the hand resting on the shoulder",
             "macro detail: the clovers and the gold rings between them"]}

NECKLACE = {
    "title": "Rivière Classique Necklace", "handle": "riviere-classique-necklace", "type": "Necklace", "kind": "Necklaces", "fb": "196",
    "category": "gid://shopify/TaxonomyCategory/aa-6-8", "option": "Metal", "units": 10, "price": "1499.00", "compare": "2800.00",
    "values": [("Silver", "RCN-S"), ("Gold", "RCN-G")],
    "tags": ["18k Gold Tone Plated", "Cubic Zirconia", "Demi Fine", "Naira Petite", "Necklace", "Rhodium Silver Tone Plated", "Tennis"],
    "intro": ("One unbroken line of light. Round brilliant cut clear cubic zirconia of about 3mm, each in its own four claw cup, are "
              "linked edge to edge all the way round, with no chain between them and nothing hanging at the front. At about 40cm "
              "it sits at the base of the neck, in silver tone or gold tone."),
    "tip": "Wear it alone with an open neckline, or under a longer pendant chain.",
    "details": ["Stones: Round brilliant cut clear cubic zirconia, approximately 3mm, each in its own four claw cup",
                "Line: One continuous row, approximately 3mm wide",
                "Length: Approximately 40cm",
                "Closure: Box clasp",
                "Metal: Silver tone or gold tone"],
    "alts": ["draped over a cream plaster block", "worn at the base of the neck", "worn, turned a quarter to the side",
             "macro detail: the round stones in their four claw cups"]}

if __name__ == "__main__":
    var = {"on": {"autoPublish": True}, "off": {"autoPublish": False}, "clover": product(CLOVER), "necklace": product(NECKLACE)}
    sel = "{ publication { id autoPublish } userErrors { field message } }"
    ps = ("{ product { id handle status totalInventory variants(first: 5) { nodes { id title sku price inventoryQuantity } } "
          "media(first: 16) { nodes { alt status } } } userErrors { field message code } }")
    doc = ("mutation Ship30Oct($on: PublicationUpdateInput!, $off: PublicationUpdateInput!, $clover: ProductSetInput!, "
           "$necklace: ProductSetInput!) {\n"
           + "".join(f"  on{i}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $on) {sel}\n" for i, p in enumerate(PUBS))
           + f"  clover: productSet(input: $clover, synchronous: true) {ps}\n"
           + f"  necklace: productSet(input: $necklace, synchronous: true) {ps}\n"
           + "".join(f"  off{i}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $off) {sel}\n" for i, p in enumerate(PUBS))
           + "}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_30oct.json"), "w"), ensure_ascii=False, indent=1)
    open(os.path.join(OUT, "ship_30oct.graphql"), "w").write(doc)
    print(len(var["clover"]["files"]), "clover files,", len(var["necklace"]["files"]), "necklace files")
