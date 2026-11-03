# One Shopify mutation (one approval) for N05 Petite Pear Solitaire Necklace, 3 Nov 2026, after the owner's "Reduce sizing check
# supplier pic". The pear in the owner's photo is about 6 x 8 mm (75 x 90 px against ~200 px fingers and ~22 px cable links); the
# 2 Nov photos drew it about 10 x 14 mm worn and about 20 mm in the palm, and the copy said 7 x 10 mm. productSet by id:
#  - the five new photos (packshot edit, two worn, macro, palm composite) replace the old five;
#  - the new size card petite-pear-solitaire-necklace-size-guide-v2.jpg ("pear 6 x 8 mm") replaces the old card, and the description,
#    its size-guide link and the SEO text say 6 x 8 mm;
#  - the variant is passed by id with its file only: no price, no compare-at, no stock and no status are sent, so the owner's
#    Active status and the Rs 1,099 price they set stay as they are.
# Usage: ship_n05.py -> ../shopify/ship_n05.json (variables) and ../shopify/ship_n05.graphql (the mutation)
import importlib.util, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s2", os.path.join(H, "ship_2nov.py")); S2 = importlib.util.module_from_spec(s); s.loader.exec_module(S2)
S31 = S2.S31; L = S2.L; F = json.load(open(os.path.join(H, "frames.json"))); URL = json.load(open(os.path.join(H, "url_map.json")))
D = json.load(open(os.path.join(H, "drafts_new.json")))
ALTS = dict(S31.ALTS["Necklace"], P="resting in an open palm, to show its size")

def product(i="N05"):
    x = dict(L[i]); t, h = x["title"], S31.handle(x["title"]); card = f"{h}-size-guide-v2.jpg"
    files = [{"originalSource": URL[f"{h}-{n:02d}.jpg"], "alt": f"{t} — {ALTS[S31.shot(key)]}", "contentType": "IMAGE"}
             for n, key in enumerate(F[i][""], 1)]
    files.append({"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    v = {"id": D[i]["variant"], "optionValues": [{"optionName": "Title", "name": "Default Title"}],
         "file": {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}}
    second = x["intro"].split(". ")[1].rstrip(".")
    return {"descriptionHtml": S2.body(x, card), "seo": {"title": f"{t} — Necklace | Naira Petite", "description": f"{second}. {t} by Naira Petite."},
            "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [v], "files": files}

if __name__ == "__main__":
    var = {"n05": product(), "n05id": {"id": D["N05"]["product"]}}
    ps = ("{ product { id handle status totalInventory mediaCount { count } variants(first: 1) { nodes { id sku price compareAtPrice "
          "inventoryQuantity } } } userErrors { field message code } }")
    doc = ("mutation PetitePearSize($n05: ProductSetInput!, $n05id: ProductSetIdentifiers!) {\n"
           f"  n05: productSet(identifier: $n05id, input: $n05, synchronous: true) {ps}\n}}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_n05.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_n05.graphql"), "w").write(doc)
    p = var["n05"]; print(len(p["files"]), "files;", p["seo"]["description"])
