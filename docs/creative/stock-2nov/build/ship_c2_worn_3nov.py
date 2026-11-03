# One Shopify mutation (one approval), 3 Nov 2026, for the owner's note: "Clover size check bracelet keep same sizing for neck".
#  - C2 Clover Garland Necklace (DRAFT): its copy and size card already give the bracelet's 10 mm clover and 3.5 mm stones, and the palm
#    photo was composited at 10 mm, but the two worn photos drew the clovers at about 15 mm (about 0.32 of the lip width, against about
#    0.22 on the Clover Garland Bracelet's worn photos, about 12 across the front). Both are replaced by the comp.py garland rebuilds
#    (C2_W1g, C2_W2qg). The packshot, macro, palm and size card are kept by media id; the variant keeps its id and the packshot as image.
#    Nothing else is sent: no status, title change, copy, price, stock or tags.
# Usage: ship_c2_worn_3nov.py -> ../shopify/ship_c2_worn_3nov.json (variables) and ../shopify/ship_c2_worn_3nov.graphql (the mutation)
import json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
URL = json.load(open(os.path.join(H, "url_map.json"))); D = json.load(open(os.path.join(H, "drafts_new.json")))["C2"]
T = "Clover Garland Necklace"; M = D["media"]
files = [{"id": M["H"]},
         {"originalSource": URL["clover-garland-necklace-02.jpg"], "contentType": "IMAGE", "alt": f"{T} — worn at the base of the neck"},
         {"originalSource": URL["clover-garland-necklace-03.jpg"], "contentType": "IMAGE", "alt": f"{T} — worn, turned a quarter to the side"},
         {"id": M["M"]}, {"id": M["P"]}, {"id": M["card"]}]
OV = [{"optionName": "Title", "name": "Default Title"}]
var = {"id": {"id": D["product"]},
       "p": {"title": T, "handle": "clover-garland-necklace", "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}],
             "variants": [{"id": D["variant"], "optionValues": OV, "file": {"id": M["H"]}}], "files": files}}
doc = ("mutation CloverNeckSize($id: ProductSetIdentifiers!, $p: ProductSetInput!) {\n"
       "  p: productSet(identifier: $id, input: $p, synchronous: true) { product { id handle status totalInventory mediaCount { count } "
       "media(first: 10) { nodes { id alt } } variants(first: 1) { nodes { id sku price inventoryQuantity } } } userErrors { field message code } }\n}\n")
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_c2_worn_3nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_c2_worn_3nov.graphql"), "w").write(doc)
    print(json.dumps(var, ensure_ascii=False))
