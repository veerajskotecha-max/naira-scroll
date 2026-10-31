# Builds one Shopify mutation (one approval) for the Albyluxe and supplier picks the owner told us to ship on 31 Oct 2026
# ("Ship ones approved"): every listing in listings.json with status "ship", less the four the owner held back on the final
# approval page (https://claude.ai/artifact/FsneG4AyJgJqAEB5Rn9hRP, collection final: A13, A14, A16 and B11 -> "hold").
#  - Each listing is created ACTIVE with its variants (5 units each at the shop's one location), its photos variant by variant
#    in frames.json order, each variant's hero as its variant image, and the size card last as <handle>-size-guide.jpg, the
#    name each description's size-guide image links to.
#  - ProductSetInput cannot publish, so the mutation turns autoPublish on for the six sales channels just before the
#    productSets and back off right after them (as ../../clover-garland/build/ship_30oct.py).
#  - Category, tags, SEO and the Google / Facebook category metafields follow the live listings of each type (read on 31 Oct).
#    The tags never claim waterproof, tarnish-free or hypoallergenic; metal tags are the store's tone tags.
# Usage: ship_31oct.py  (reads url_map.json: filename -> public URL)
#        -> ../shopify/ship_31oct.json (variables) and ../shopify/ship_31oct.graphql (the mutation)
import html, json, os, re, unicodedata
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
L = json.load(open(os.path.join(H, "listings.json"))); F = json.load(open(os.path.join(H, "frames.json")))
URL = json.load(open(os.path.join(H, "url_map.json")))
HELD_ON_FINAL = {"A13", "A14", "A16", "B11"}
LOCATION = "gid://shopify/Location/76267389090"
CDN = "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/"
PUBS = ["164676042914", "164676108450", "167637745826", "175106293922", "180607254690", "180607746210"]
CARE = "Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch."
# listing type -> (Shopify product type, taxonomy category, Google category leaf, Facebook category id)
TYPES = {"Ring": ("Ring", "aa-6-9", "Rings", "200"), "Earrings": ("Earrings", "aa-6-6", "Earrings", "194"),
         "Necklace": ("Necklace", "aa-6-8", "Necklaces", "196"), "Bracelet": ("Bracelet", "aa-6-3", "Bracelets", "191"),
         "Set": ("Jewellery Set", "aa-6-7", "Jewelry Sets", "6463")}
OPEN_RINGS = {"A02", "A04"}
ALTS = {"Ring": {"H": "on a cream plaster block, the full ring", "W1": "worn on the ring finger, the hand at the collarbone",
                 "W2": "worn, the back of the hand to the camera", "M": "macro detail of the stones and the setting"},
        "Earrings": {"H": "the pair on a cream plaster block", "W1": "worn, in three-quarter profile", "W2": "worn close at the ear",
                     "M": "macro detail of one earring"},
        "Necklace": {"H": "on a cream plaster block, the full piece", "W1": "worn at the base of the neck",
                     "W2": "worn, turned a quarter to the side", "M": "macro detail of the pendant and the chain"},
        "Bracelet": {"H": "on a cream plaster block, the full piece", "W1": "worn on the wrist",
                     "W2": "worn close, the hand resting on the shoulder", "M": "macro detail"},
        "Set": {"H": "the necklace and the earrings on a cream plaster block", "E": "the earrings on a cream plaster block",
                "W1": "worn: the necklace and one earring", "W2": "worn close at the ear", "M": "macro detail of one earring"}}
e = html.escape


def handle(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower(); return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def money(v): return None if v is None else f"{v:.2f}"


def shot(key):
    return re.match(r"[A-Z]\d+[a-z]*_([A-Z]+\d?)", key).group(1)


def tags(x, ptype):
    metal = " ".join(d for d in x["details"] if d.lower().startswith(("metal", "material", "finish", "setting"))).lower()
    t = {"Cubic Zirconia", "Demi Fine", "Naira Petite", "Jewellery Set" if x["type"] == "Set" else x["type"]}
    if "rose gold" in metal: t.add("Rose Gold Tone")
    elif "gold" in metal: t.add("18k Gold Tone Plated")
    if "silver" in metal: t.add("Rhodium Silver Tone Plated")
    if x["id"] in OPEN_RINGS: t.add("Adjustable")
    if x["id"].startswith("A") or re.search(r"\bAL\b|AL-|Albyluxe", x["code"]): t.add("Albyluxe")   # the A pieces are Albyluxe's
    if "Heart" in x["title"]: t.add("Heart")
    if "Tennis" in x["title"]: t.add("Tennis")
    if any(v == "Pearl" for v, _ in (x["option"][1] if x["option"] else [])): t.add("Pearl")
    return sorted(t)


def body(x, h):
    return (f"<p>{e(x['intro'])}</p><p><strong>STYLING TIP:</strong> {e(x['tip'])}</p><p><strong>Details</strong></p><ul>\n"
            + "".join(f"<li>{e(d)}</li>\n" for d in x["details"])
            + f"</ul><p><img src=\"{CDN}{h}-size-guide.jpg\" alt=\"Size guide — {e(x['title'])}\" width=\"420\"></p>"
            + f"<p><strong>Care</strong></p><p>{e(CARE)}</p><p>You will receive your piece in a Naira Petite box.</p>")


def product(x):
    t, h = x["title"], handle(x["title"]); ptype, cat, gcat, fb = TYPES[x["type"]]
    files, heroes, n = [], {}, 0
    for vname, keys in F[x["id"]].items():
        for i, key in enumerate(keys):
            n += 1; fn = f"{h}-{n:02d}.jpg"; alt = ALTS[x["type"]][shot(key)]
            files.append({"originalSource": URL[fn], "alt": f"{t}, {vname} — {alt}" if vname else f"{t} — {alt}", "contentType": "IMAGE"})
            if i == 0: heroes[vname] = URL[fn]
    card = f"{h}-size-guide.jpg"
    files.append({"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    opt = x["option"]
    if opt:
        name, values = opt[0], opt[1]; options = [{"name": name, "values": [{"name": v} for v, _ in values]}]
        pairs = [([{"optionName": name, "name": v}], s, heroes.get(v, heroes.get(""))) for v, s in values]
    else:
        options = [{"name": "Title", "values": [{"name": "Default Title"}]}]
        pairs = [([{"optionName": "Title", "name": "Default Title"}], x["sku"], heroes[""])]
    variants = []
    for ov, sku, hero in pairs:
        v = {"optionValues": ov, "sku": sku, "price": money(x["price"]), "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
             "inventoryQuantities": [{"locationId": LOCATION, "name": "available", "quantity": x["units"]}],
             "file": {"originalSource": hero, "contentType": "IMAGE"}}
        if x["compare"] is not None: v["compareAtPrice"] = money(x["compare"])
        variants.append(v)
    second = x["intro"].split(". ")[1].rstrip(".")
    return {"title": t, "handle": h, "status": "ACTIVE", "vendor": "Naira Petite", "productType": ptype,
            "category": f"gid://shopify/TaxonomyCategory/{cat}", "tags": tags(x, ptype), "descriptionHtml": body(x, h),
            "seo": {"title": f"{t} — {ptype} | Naira Petite", "description": f"{second}. {t} by Naira Petite."},
            "productOptions": options, "variants": variants, "files": files,
            "metafields": [{"namespace": "mm-google-shopping", "key": "google_product_category", "type": "single_line_text_field",
                            "value": f"Apparel & Accessories > Jewelry > {gcat}"},
                           {"namespace": "mm-google-shopping", "key": "gender", "type": "single_line_text_field", "value": "Female"},
                           {"namespace": "mm-google-shopping", "key": "age_group", "type": "single_line_text_field", "value": "Adult"},
                           {"namespace": "mm-google-shopping", "key": "condition", "type": "single_line_text_field", "value": "New"},
                           {"namespace": "mc-facebook", "key": "google_product_category", "type": "single_line_text_field", "value": fb}]}


if __name__ == "__main__":
    ship = [x for x in L if x["status"] == "ship" and x["id"] not in HELD_ON_FINAL]
    var = {"on": {"autoPublish": True}, "off": {"autoPublish": False}}
    for x in ship: var[x["id"].lower()] = product(x)
    sel = "{ publication { id autoPublish } userErrors { field message } }"
    ps = ("{ product { id handle status totalInventory variants(first: 5) { nodes { sku price compareAtPrice inventoryQuantity } } "
          "media(first: 1) { nodes { status } } } userErrors { field message code } }")
    doc = ("mutation Ship31Oct($on: PublicationUpdateInput!, $off: PublicationUpdateInput!, "
           + ", ".join(f"${x['id'].lower()}: ProductSetInput!" for x in ship) + ") {\n"
           + "".join(f"  on{i}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $on) {sel}\n" for i, p in enumerate(PUBS))
           + "".join(f"  {x['id'].lower()}: productSet(input: ${x['id'].lower()}, synchronous: true) {ps}\n" for x in ship)
           + "".join(f"  off{i}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $off) {sel}\n" for i, p in enumerate(PUBS))
           + "}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_31oct.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_31oct.graphql"), "w").write(doc)
    for x in ship:
        p = var[x["id"].lower()]
        print(x["id"], p["handle"], p["productType"], len(p["variants"]), "variants", len(p["files"]), "files", p["tags"])
