# One Shopify mutation (one approval) adding the approved photos to the nine new necklace drafts of 2 Nov 2026 (created by
# ship_new.py with only their size cards). productSet by id: the file list is the photos in frames.json order, then the media the
# draft already holds, passed by id (the size card, and N09's macro), so nothing is uploaded twice and the description's size-guide
# link keeps its filename. Variant id, SKU, price and stock stay as they are (no inventoryQuantities); metafields are not sent.
# Each variant's image becomes the packshot. No status is sent, so each piece keeps the status it has (A08 and A12 were set
# ACTIVE by the owner after the 2 Nov fixes).
# A08, A12 and A16 (the three pieces fixed on 2 Nov) are in drafts_new.json too, with the media they already hold, so the same
# mutation adds their in-palm size photo (and A16's worn photo, which had dropped off the draft).
# Alt text for the in-palm shot (P) is added here, as the 31 Oct table has none.
# N02's description and SEO text are re-sent, as its petal count was corrected on 2 Nov.
# Usage: ship_photos.py [id ...] -> ../shopify/ship_photos.json and ../shopify/ship_photos.graphql
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
import importlib.util
s = importlib.util.spec_from_file_location("s2", os.path.join(H, "ship_2nov.py")); S2 = importlib.util.module_from_spec(s); s.loader.exec_module(S2)
S31 = S2.S31; L = S2.L; URL = json.load(open(os.path.join(H, "url_map.json")))
F = json.load(open(os.path.join(H, "frames.json"))); D = json.load(open(os.path.join(H, "drafts_new.json")))
PALM = {"Necklace": "resting in an open palm, to show its size", "Earrings": "the pair resting in an open palm, to show their size",
        "Set": "the necklace and the earrings resting in an open palm, to show their size"}
for k, v in PALM.items(): S31.ALTS[k]["P"] = v
RECOPY = {"N02"}   # Soleil Petal: five petals fanned below the stone (the stock photo), not six all round

def product(i):
    x = L[i]; t, h = x["title"], S31.handle(x["title"]); d = D[i]; files = []
    for n, key in enumerate(F[i][""], 1):
        sh = S31.shot(key)
        if sh in d["media"]: files.append({"id": d["media"][sh]})               # already on the draft
        else: files.append({"originalSource": URL[f"{h}-{n:02d}.jpg"], "alt": f"{t} — {S31.ALTS[x['type']][sh]}", "contentType": "IMAGE"})
    files.append({"id": d["media"]["card"]})
    v = {"id": d["variant"], "optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": x["sku"], "price": S31.money(x["price"]),
         "compareAtPrice": S31.money(x["compare"]), "inventoryPolicy": "DENY",
         "file": files[0] if "id" in files[0] else {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}}
    p = {}
    if i in RECOPY:                                                            # copy corrected after the draft was made
        ptype = S31.TYPES[x["type"]][0]; second = x["intro"].split(". ")[1].rstrip(".")
        p = {"descriptionHtml": S2.body(x, f"{h}-size-guide.jpg"),
             "seo": {"title": f"{t} — {ptype} | Naira Petite", "description": f"{second}. {t} by Naira Petite."}}
    return {**p, "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [v], "files": files}

if __name__ == "__main__":
    ids = sys.argv[1:] or sorted(D); var = {}
    for i in ids: var[i.lower()] = product(i); var[i.lower() + "id"] = {"id": D[i]["product"]}
    ps = "{ product { id handle status totalInventory mediaCount { count } } userErrors { field message code } }"
    doc = ("mutation Photos2Nov(" + ", ".join(f"${i.lower()}: ProductSetInput!, ${i.lower()}id: ProductSetIdentifiers!" for i in ids) + ") {\n"
           + "".join(f"  {i.lower()}: productSet(identifier: ${i.lower()}id, input: ${i.lower()}, synchronous: true) {ps}\n" for i in ids) + "}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_photos.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_photos.graphql"), "w").write(doc)
    for i in ids: print(i, len(var[i.lower()]["files"]), "files")
