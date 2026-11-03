# One Shopify mutation (one approval), 3 Nov 2026, for the owner's two notes with photos of the stock in hand:
#   "Also list this, check images we made in higgsfield if we can use that or this. and do all corrections proper!" (the charm huggies)
#   "This red necklace also. And the chain of other necklace on listing is wrong, the second image"
#  - C2 Clover Garland Necklace (red): created as a DRAFT with 5 units, CLGN-RD, Rs 2,199 against 3,499 (beside the Laurel Marquise),
#    the Clover Garland Bracelet's clover at necklace length; tag "Clover" as on the bracelet. No cost per item was given.
#  - A14 Solitaire Charm Huggies: created as a DRAFT with 5 units, SCH, Rs 1,199 against 2,199. The 31 Oct images (an 8 mm cuff with the
#    stone on a jump ring) and the live Solitaire Drop Huggies (ADT27, a different piece) were not usable; new photos from the photo in hand.
#  - A16 V-Bar Teardrop Necklace (ACTIVE, the owner's price Rs 1,399): the five photos are replaced by the wheat-chain redraws and the copy
#    and SEO say wheat chain. The size card is kept by its media id. Nothing else is sent: no status, price, compare-at, cost, stock or tags.
#  - A13 Slim Pave Huggies (DRAFT), owner: "Check diamond setting and change it": the five photos are replaced by edits with the stones in
#    raised claws and a second row of tiny stones down the outer side, as on the pair in hand, and the copy says so; the size card is
#    redrawn from the new packshot as slim-pave-huggies-size-guide-v2.jpg and the description links to it. Same rules as A16.
# autoPublish is turned on for the six sales channels around the two creates and off again (ship_a13.py), so the new pieces show on every
# channel the moment the owner sets them Active. No status other than DRAFT is ever sent.
# Usage: ship_3nov.py -> ../shopify/ship_3nov.json (variables) and ../shopify/ship_3nov.graphql (the mutation)
import importlib.util, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s2", os.path.join(H, "ship_2nov.py")); S2 = importlib.util.module_from_spec(s); s.loader.exec_module(S2)
S31 = S2.S31; L = S2.L; F = json.load(open(os.path.join(H, "frames.json"))); URL = json.load(open(os.path.join(H, "url_map.json")))
D = json.load(open(os.path.join(H, "drafts_new.json")))
ALTS = {"Earrings": dict(S31.ALTS["Earrings"], P="the pair resting in an open palm, to show their size"),
        "Necklace": dict(S31.ALTS["Necklace"], P="resting in an open palm, to show its size")}
CODE = {"C2": "", "A14": S2.OLD["A14"]["code"]}; EXTRA = {"C2": ["Clover"]}
NEWCARD = {"A13": "slim-pave-huggies-size-guide-v2.jpg"}    # the card's photo is the new packshot, with the new setting
OPT = [{"name": "Title", "values": [{"name": "Default Title"}]}]; OV = [{"optionName": "Title", "name": "Default Title"}]

ALT_OVERRIDE = {("C2", "M"): "macro detail of the clovers and the small rings between them"}   # no pendant on this necklace

def gallery(i):
    x = L[i]; t, h = x["title"], S31.handle(x["title"])
    return [{"originalSource": URL[f"{h}-{n:02d}.jpg"], "contentType": "IMAGE",
             "alt": f"{t} — {ALT_OVERRIDE.get((i, S31.shot(key)), ALTS[x['type']][S31.shot(key)])}"}
            for n, key in enumerate(F[i][""], 1)]

def seo(x, ptype):
    second = x["intro"].split(". ")[1].rstrip(".")
    return {"title": f"{x['title']} — {ptype} | Naira Petite", "description": f"{second}. {x['title']} by Naira Petite."}

def create(i):
    x = dict(L[i]); x["code"] = CODE[i]; t, h = x["title"], S31.handle(x["title"]); ptype, cat, gcat, fb = S31.TYPES[x["type"]]
    card = f"{h}-size-guide.jpg"
    files = gallery(i) + [{"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"}]
    v = {"optionValues": OV, "sku": x["sku"], "price": S31.money(x["price"]), "compareAtPrice": S31.money(x["compare"]),
         "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
         "inventoryQuantities": [{"locationId": S31.LOCATION, "name": "available", "quantity": x["units"]}],
         "file": {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}}
    return {"title": t, "handle": h, "status": "DRAFT", "vendor": "Naira Petite", "productType": ptype,
            "category": f"gid://shopify/TaxonomyCategory/{cat}", "tags": sorted(set(S31.tags(x, ptype)) | set(EXTRA.get(i, []))),
            "descriptionHtml": S2.body(x, card), "seo": seo(x, ptype), "productOptions": OPT, "variants": [v], "files": files,
            "metafields": S2.METAFIELDS(gcat, fb)}

def update(i):
    """Replace the gallery (photos by URL, the size card kept by its media id) and the copy and SEO of a listing; the variant keeps its id
    and takes the new first photo as its image. No status, price, compare-at, cost, stock or tags are sent."""
    x = dict(L[i]); t, h = x["title"], S31.handle(x["title"]); ptype = S31.TYPES[x["type"]][0]
    if i in NEWCARD:                          # a redrawn card goes in under a new name, as the old one holds the plain name in Shopify Files
        card = NEWCARD[i]; files = gallery(i) + [{"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"}]
    else:
        card = f"{h}-size-guide.jpg"; files = gallery(i) + [{"id": D[i]["media"]["card"]}]
    v = {"id": D[i]["variant"], "optionValues": OV, "file": {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}}
    return {"title": t, "handle": h, "descriptionHtml": S2.body(x, card), "seo": seo(x, ptype),
            "productOptions": OPT, "variants": [v], "files": files}

if __name__ == "__main__":
    var = {"on": {"autoPublish": True}, "off": {"autoPublish": False}, "c2": create("C2"), "a14": create("A14"),
           "a16": update("A16"), "a16id": {"id": D["A16"]["product"]}, "a13": update("A13"), "a13id": {"id": D["A13"]["product"]}}
    sel = "{ publication { id autoPublish } userErrors { field message } }"
    ps = ("{ product { id handle status totalInventory tags mediaCount { count } variants(first: 1) { nodes { id sku price compareAtPrice "
          "inventoryQuantity } } } userErrors { field message code } }")
    doc = ("mutation CloverCharmVBar($on: PublicationUpdateInput!, $off: PublicationUpdateInput!, $c2: ProductSetInput!, $a14: ProductSetInput!, "
           "$a16: ProductSetInput!, $a16id: ProductSetIdentifiers!, $a13: ProductSetInput!, $a13id: ProductSetIdentifiers!) {\n"
           + "".join(f"  on{k}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $on) {sel}\n" for k, p in enumerate(S31.PUBS))
           + f"  c2: productSet(input: $c2, synchronous: true) {ps}\n"
           + f"  a14: productSet(input: $a14, synchronous: true) {ps}\n"
           + f"  a16: productSet(identifier: $a16id, input: $a16, synchronous: true) {ps}\n"
           + f"  a13: productSet(identifier: $a13id, input: $a13, synchronous: true) {ps}\n"
           + "".join(f"  off{k}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $off) {sel}\n" for k, p in enumerate(S31.PUBS))
           + "}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_3nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_3nov.graphql"), "w").write(doc)
    for k in ("c2", "a14", "a16", "a13"):
        p = var[k]; print(k, p["handle"], len(p["files"]), "files", p.get("tags"), p["seo"]["description"][:80])
