# One Shopify mutation (one approval), 3 Nov 2026 (afternoon), for the owner's note with the photos of the two earrings in hand:
#   "Create the two earrings, the heart and the solitaire drop one. It already has check if it is correct in detail and do the listings
#    with six images and sizes. These listings need to check colours, diamond placement and everything the heart one. The colour was
#    different so we had rejected. Please make the new colour one and check sizing properly as well always."
#  - A14 Solitaire Charm Huggies (DRAFT): against the pair in hand the 3 Nov gallery drew a thin-wire hoop, a small tube and a stone about
#    0.4 of the hoop. The five photos are replaced by the redraws (thick band, a tube about a third of the hoop, a stone about half of it,
#    the worn frames at a 13 mm hoop), the copy and SEO say so, and the size card is redrawn from the new packshot as
#    solitaire-charm-huggies-size-guide-v2.jpg (the old card holds the plain name in Shopify Files); the description links to it.
#  - A15 Pave Open Heart Studs (ACTIVE): the gold tone, the two rows of tiny stones and the shape match the owner's photo; the two worn
#    frames are replaced by the same frames with the heart pasted back at about 20 mm (it read about 22 mm against the ear). The packshot,
#    the macro, the palm and the size card are kept by their media ids, and the copy is resent unchanged (checked against the live text).
# Nothing else is sent: no status, price, compare-at, cost, stock, tags or channels.
# Usage: ship_earrings_3nov.py -> ../shopify/ship_earrings_3nov.json (variables) and ../shopify/ship_earrings_3nov.graphql
import importlib.util, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s3", os.path.join(H, "ship_3nov.py")); S3 = importlib.util.module_from_spec(s); s.loader.exec_module(S3)
S31, S2, L, D, URL, OV, OPT = S3.S31, S3.S2, S3.L, S3.D, S3.URL, S3.OV, S3.OPT
S3.NEWCARD.clear(); S3.NEWCARD["A14"] = "solitaire-charm-huggies-size-guide-v2.jpg"
SHOTS = ["H", "W1", "W2", "M", "P"]

def partial(i, new):
    """Gallery order kept; the shots in `new` come in by URL with the house alt text, every other photo and the card by media id."""
    x = L[i]; t, h = x["title"], S31.handle(x["title"]); ptype = S31.TYPES[x["type"]][0]; alts = S3.ALTS[x["type"]]
    files = [{"originalSource": URL[f"{h}-{n:02d}.jpg"], "contentType": "IMAGE", "alt": f"{t} — {alts[k]}"} if k in new
             else {"id": D[i]["media"][k]} for n, k in enumerate(SHOTS, 1)] + [{"id": D[i]["media"]["card"]}]
    v = {"id": D[i]["variant"], "optionValues": OV, "file": {"id": D[i]["media"]["H"]}}
    return {"title": t, "handle": h, "descriptionHtml": S2.body(x, f"{h}-size-guide-v2.jpg" if i == "A15" else f"{h}-size-guide.jpg"),
            "seo": S3.seo(x, ptype), "productOptions": OPT, "variants": [v], "files": files}

if __name__ == "__main__":
    var = {"a14": S3.update("A14"), "a14id": {"id": D["A14"]["product"]}, "a15": partial("A15", {"W1", "W2"}), "a15id": {"id": D["A15"]["product"]}}
    ps = ("{ product { id handle status totalInventory tags mediaCount { count } variants(first: 1) { nodes { id sku price compareAtPrice "
          "inventoryQuantity } } } userErrors { field message code } }")
    doc = ("mutation CharmHeartFix($a14: ProductSetInput!, $a14id: ProductSetIdentifiers!, $a15: ProductSetInput!, $a15id: ProductSetIdentifiers!) {\n"
           f"  a14: productSet(identifier: $a14id, input: $a14, synchronous: true) {ps}\n"
           f"  a15: productSet(identifier: $a15id, input: $a15, synchronous: true) {ps}\n"
           "}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_earrings_3nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_earrings_3nov.graphql"), "w").write(doc)
    for k in ("a14", "a15"):
        p = var[k]; print(k, p["handle"], len(p["files"]), "files", p["seo"]["description"][:90])
