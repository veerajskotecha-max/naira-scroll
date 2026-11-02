# One Shopify mutation (one approval) creating the nine new necklaces of 2 Nov 2026 as DRAFTS before their photos exist (Higgsfield
# credits ran out): each with its copy, price, SKU, 5 units, feed metafields and its size card; N09 also carries its one approved
# frame (N09_M, the heart-and-three-stones macro). autoPublish is turned on for the six sales channels around the creates (as
# ../../albyluxe-31oct/build/ship_31oct.py does) and A16, created on 2 Nov without it, is published to the six, so every piece shows
# on every channel the moment the owner sets it Active.
# When the photos arrive: productSet each by id with the full file list, and pass the size card as {"id": <its MediaImage id>}
# rather than re-uploading it, or Shopify renames the duplicate filename and the description's size-guide link breaks.
# Usage: ship_new.py -> ../shopify/ship_new.json (variables) and ../shopify/ship_new.graphql (the mutation)
import importlib.util, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s2", os.path.join(H, "ship_2nov.py")); S2 = importlib.util.module_from_spec(s); s.loader.exec_module(S2)
S31 = S2.S31; L = S2.L; URL = S2.URL
IDS = ["N01", "N02", "N03", "N04", "N05", "N06", "N07", "N08", "N09"]
PHOTOS = {"N09": [("petite-heart-trio-necklace-04.jpg", "M")]}            # approved frames that exist already
A16 = "gid://shopify/Product/10377179857058"

def product(i):
    x = dict(L[i]); x["code"] = ""; t, h = x["title"], S31.handle(x["title"]); ptype, cat, gcat, fb = S31.TYPES[x["type"]]
    card = f"{h}-size-guide.jpg"
    files = [{"originalSource": URL[fn], "alt": f"{t} — {S31.ALTS[x['type']][sh]}", "contentType": "IMAGE"} for fn, sh in PHOTOS.get(i, [])]
    files.append({"originalSource": URL[card], "filename": card, "alt": f"Size guide — {t}", "contentType": "IMAGE"})
    v = {"optionValues": [{"optionName": "Title", "name": "Default Title"}], "sku": x["sku"], "price": S31.money(x["price"]),
         "compareAtPrice": S31.money(x["compare"]), "inventoryPolicy": "DENY", "inventoryItem": {"tracked": True},
         "inventoryQuantities": [{"locationId": S31.LOCATION, "name": "available", "quantity": x["units"]}]}
    if i in PHOTOS: v["file"] = {"originalSource": files[0]["originalSource"], "contentType": "IMAGE"}
    second = x["intro"].split(". ")[1].rstrip(".")
    return {"title": t, "handle": h, "status": "DRAFT", "vendor": "Naira Petite", "productType": ptype,
            "category": f"gid://shopify/TaxonomyCategory/{cat}", "tags": sorted(set(S31.tags(x, ptype)) | ({"Pearl"} if "Pearl" in t else set())), "descriptionHtml": S2.body(x, card),
            "seo": {"title": f"{t} — {ptype} | Naira Petite", "description": f"{second}. {t} by Naira Petite."},
            "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [v], "files": files,
            "metafields": S2.METAFIELDS(gcat, fb)}

if __name__ == "__main__":
    var = {"on": {"autoPublish": True}, "off": {"autoPublish": False}, "pubs": [{"publicationId": f"gid://shopify/Publication/{p}"} for p in S31.PUBS]}
    for i in IDS: var[i.lower()] = product(i)
    sel = "{ publication { id autoPublish } userErrors { field message } }"
    ps = "{ product { id handle status totalInventory mediaCount { count } variants(first: 1) { nodes { id sku price compareAtPrice inventoryQuantity } } } userErrors { field message code } }"
    doc = ("mutation New2Nov($on: PublicationUpdateInput!, $off: PublicationUpdateInput!, $pubs: [PublicationInput!]!, "
           + ", ".join(f"${i.lower()}: ProductSetInput!" for i in IDS) + ") {\n"
           + "".join(f"  on{k}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $on) {sel}\n" for k, p in enumerate(S31.PUBS))
           + "".join(f"  {i.lower()}: productSet(input: ${i.lower()}, synchronous: true) {ps}\n" for i in IDS)
           + "".join(f"  off{k}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $off) {sel}\n" for k, p in enumerate(S31.PUBS))
           + f"  a16pub: publishablePublish(id: \"{A16}\", input: $pubs) {{ userErrors {{ field message }} }}\n}}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_new.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_new.graphql"), "w").write(doc)
    for i in IDS: p = var[i.lower()]; print(i, p["handle"], p["variants"][0]["sku"], p["variants"][0]["price"], len(p["files"]), "files", p["tags"])
