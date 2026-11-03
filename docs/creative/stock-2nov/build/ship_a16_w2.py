# Second Shopify mutation (one approval) for A16 V-Bar Teardrop Necklace, 3 Nov 2026, after ship_a15a16.py. The review sheet showed
# the gallery's two worn photos as near twins (the front view had been made from the quarter view and both faced the camera), so a true
# quarter-turn view (A16_W2q, made from A16_W2s2 to keep the necklace's size) replaces photo 3. productSet replaces the files list in
# full, so the four unchanged photos and the size card are passed by their media ids (nothing uploaded twice) and only photo 3 comes in
# by URL. The variant keeps its image by id; nothing else is sent (no title, copy, status, price, cost or stock).
# Usage: ship_a16_w2.py -> ../shopify/ship_a16_w2.json (variables) and ../shopify/ship_a16_w2.graphql (the mutation)
import json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
URL = json.load(open(os.path.join(H, "url_map.json"))); D = json.load(open(os.path.join(H, "drafts_new.json")))["A16"]
M = D["media"]
files = [{"id": M["H"]}, {"id": M["W1"]},
         {"originalSource": URL["v-bar-teardrop-necklace-03.jpg"], "alt": "V-Bar Teardrop Necklace — worn, turned a quarter to the side",
          "contentType": "IMAGE"},
         {"id": M["M"]}, {"id": M["P"]}, {"id": M["card"]}]
var = {"a16": {"files": files, "variants": [{"id": D["variant"], "optionValues": [{"optionName": "Title", "name": "Default Title"}],
                                             "file": {"id": M["H"]}}],
               "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}]},
       "a16id": {"id": D["product"]}}
doc = ("mutation VBarQuarterTurn($a16: ProductSetInput!, $a16id: ProductSetIdentifiers!) {\n"
       "  a16: productSet(identifier: $a16id, input: $a16, synchronous: true) { product { id handle title status totalInventory mediaCount "
       "{ count } variants(first: 1) { nodes { id sku price compareAtPrice inventoryQuantity inventoryItem { unitCost { amount } } } } } "
       "userErrors { field message code } }\n}\n")
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_a16_w2.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_a16_w2.graphql"), "w").write(doc)
    print(json.dumps(var, ensure_ascii=False))
