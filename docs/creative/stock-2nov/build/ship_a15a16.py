# One Shopify mutation (one approval) for two drafts the owner flagged on 3 Nov with photos of the stock in hand:
# "These 2 products too the heart is gold and also for this chain the pattern of chain on our listing is wrong!"
#  - A15 Pave Open Heart Studs (listed 31 Oct from the buy-book photo as silver tone, about 11 mm): the pair in hand is gold tone,
#    each heart about 20 mm with a broad band of two rows of tiny stones. New gallery (packshot, worn x2, macro, in the palm), a
#    new size card under a -v2 name (the 31 Oct card holds the plain name in Shopify Files), gold copy and SEO, and the tag
#    "Rhodium Silver Tone Plated" swapped for the store's "18k Gold Tone Plated". Tags are sent in full because productSet
#    replaces the list; the feed metafields are left alone.
#  - A16 Herringbone Teardrop Necklace: the chain in hand is a dense curb chain of faceted links, not a herringbone, so the piece
#    is renamed V-Bar Teardrop Necklace (handle v-bar-teardrop-necklace; still a draft, never published) with a new gallery,
#    a new size card (pear about 10 x 13 mm), new copy and SEO. The supplier's line on the owner's photo, 390x5 1,950, is
#    recorded as the cost per item (Rs 390); the SKU stays HTN.
# Both variants are passed by id with their image (and A16's cost) only: no status, no price, no compare-at and no stock are
# sent, so both stay DRAFT at their prices with 5 units each.
# Usage: ship_a15a16.py -> ../shopify/ship_a15a16.json (variables) and ../shopify/ship_a15a16.graphql (the mutation)
import importlib.util, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s2", os.path.join(H, "ship_2nov.py")); S2 = importlib.util.module_from_spec(s); s.loader.exec_module(S2)
S31 = S2.S31; L = S2.L; F = json.load(open(os.path.join(H, "frames.json"))); URL = json.load(open(os.path.join(H, "url_map.json")))
D = json.load(open(os.path.join(H, "drafts_new.json")))
ALTS = {"Earrings": dict(S31.ALTS["Earrings"], P="the pair resting in an open palm, to show their size"),
        "Necklace": dict(S31.ALTS["Necklace"], P="resting in an open palm, to show its size")}
CARD = {"A15": "pave-open-heart-studs-size-guide-v2.jpg", "A16": "v-bar-teardrop-necklace-size-guide.jpg"}
TAGS = {"A15": ["18k Gold Tone Plated", "Albyluxe", "Cubic Zirconia", "Demi Fine", "Earrings", "Heart", "Naira Petite"]}

def product(i):
    x = dict(L[i]); t, h = x["title"], S31.handle(x["title"]); ptype = S31.TYPES[x["type"]][0]; card = CARD[i]
    files = [{"originalSource": URL[f"{h}-{n:02d}.jpg"], "alt": f"{t} — {ALTS[x['type']][S31.shot(key)]}", "contentType": "IMAGE"}
             for n, key in enumerate(F[i][""], 1)]
    files.append({"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    v = {"id": D[i]["variant"], "optionValues": [{"optionName": "Title", "name": "Default Title"}],
         "file": {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}}
    if x.get("cost"): v["inventoryItem"] = {"cost": S31.money(x["cost"])}
    second = x["intro"].split(". ")[1].rstrip(".")
    p = {"title": t, "handle": h, "descriptionHtml": S2.body(x, card),
         "seo": {"title": f"{t} — {ptype} | Naira Petite", "description": f"{second}. {t} by Naira Petite."},
         "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [v], "files": files}
    if i in TAGS: p["tags"] = TAGS[i]
    return p

if __name__ == "__main__":
    var = {"a15": product("A15"), "a15id": {"id": D["A15"]["product"]}, "a16": product("A16"), "a16id": {"id": D["A16"]["product"]}}
    ps = ("{ product { id handle title status totalInventory tags mediaCount { count } variants(first: 1) { nodes { id sku price "
          "compareAtPrice inventoryQuantity inventoryItem { unitCost { amount } } } } } userErrors { field message code } }")
    doc = ("mutation HeartAndVBar($a15: ProductSetInput!, $a15id: ProductSetIdentifiers!, $a16: ProductSetInput!, $a16id: ProductSetIdentifiers!) {\n"
           f"  a15: productSet(identifier: $a15id, input: $a15, synchronous: true) {ps}\n"
           f"  a16: productSet(identifier: $a16id, input: $a16, synchronous: true) {ps}\n}}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_a15a16.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_a15a16.graphql"), "w").write(doc)
    for k in ("a15", "a16"):
        p = var[k]; print(k, p["handle"], len(p["files"]), "files;", p["seo"]["description"][:90])
