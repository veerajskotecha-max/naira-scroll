# One Shopify mutation (one approval) creating A13 Slim Pave Huggies as a DRAFT with 5 units. It was held back on the
# 31 Oct final page; the owner sent a photo of the pair in hand on 2 Nov ("Add this sku too"). The photos are new, made from
# that photo (packshot, worn x2, macro, in the palm) at the size measured there (about 18 mm, not the 31 Oct 13 mm), then
# the size card. Copy, tags, category, SEO and the feed metafields follow ship_2nov.py (A16's create). autoPublish is turned
# on for the six sales channels around the create and off again, as ship_new.py did, so the piece shows on every channel the
# moment the owner sets it Active. No status other than DRAFT is ever sent.
# Usage: ship_a13.py -> ../shopify/ship_a13.json (variables) and ../shopify/ship_a13.graphql (the mutation)
import importlib.util, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s2", os.path.join(H, "ship_2nov.py")); S2 = importlib.util.module_from_spec(s); s.loader.exec_module(S2)
S31 = S2.S31; L = S2.L; F = S2.F; URL = json.load(open(os.path.join(H, "url_map.json")))
ALTS = dict(S31.ALTS["Earrings"], P="the pair resting in an open palm, to show their size")

def product(i):
    x = dict(L[i]); x["code"] = S2.OLD[i]["code"]; t, h = x["title"], S31.handle(x["title"]); ptype, cat, gcat, fb = S31.TYPES[x["type"]]
    card = f"{h}-size-guide.jpg"
    files = [{"originalSource": URL[f"{h}-{n:02d}.jpg"], "alt": f"{t} — {ALTS[S31.shot(key)]}", "contentType": "IMAGE"}
             for n, key in enumerate(F[i][""], 1)]
    files.append({"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    v = {"optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": x["sku"], "price": S31.money(x["price"]),
         "compareAtPrice": S31.money(x["compare"]), "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
         "inventoryQuantities": [{"locationId": S31.LOCATION, "name": "available", "quantity": x["units"]}],
         "file": {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}}
    second = x["intro"].split(". ")[1].rstrip(".")
    return {"title": t, "handle": h, "status": "DRAFT", "vendor": "Naira Petite", "productType": ptype,
            "category": f"gid://shopify/TaxonomyCategory/{cat}", "tags": S31.tags(x, ptype), "descriptionHtml": S2.body(x, card),
            "seo": {"title": f"{t} — {ptype} | Naira Petite", "description": f"{second}. {t} by Naira Petite."},
            "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [v], "files": files,
            "metafields": S2.METAFIELDS(gcat, fb)}

if __name__ == "__main__":
    var = {"on": {"autoPublish": True}, "off": {"autoPublish": False}, "a13": product("A13")}
    sel = "{ publication { id autoPublish } userErrors { field message } }"
    ps = ("{ product { id handle status totalInventory mediaCount { count } variants(first: 1) { nodes { id sku price compareAtPrice "
          "inventoryQuantity } } } userErrors { field message code } }")
    doc = ("mutation SlimPaveHuggies($on: PublicationUpdateInput!, $off: PublicationUpdateInput!, $a13: ProductSetInput!) {\n"
           + "".join(f"  on{k}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $on) {sel}\n" for k, p in enumerate(S31.PUBS))
           + f"  a13: productSet(input: $a13, synchronous: true) {ps}\n"
           + "".join(f"  off{k}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $off) {sel}\n" for k, p in enumerate(S31.PUBS))
           + "}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_a13.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_a13.graphql"), "w").write(doc)
    p = var["a13"]; print(p["handle"], p["variants"][0]["sku"], p["variants"][0]["price"], len(p["files"]), "files", p["tags"])
