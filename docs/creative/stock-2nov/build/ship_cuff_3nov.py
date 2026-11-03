# One Shopify mutation (one approval), 3 Nov 2026, for the owner's note with a photo of the stock in hand: "List this cuff also 10 pieces".
#  - B1 Orb Cable Cuff: created as a DRAFT with 10 units, OCC, Rs 1,299 against 2,299 (beside the Garnet Cable Cuff at 1,399 and the
#    Kiss Knot Bangle at 1,199), a plain gold tone cable cuff with no stones, so the Cubic Zirconia tag the house tags() adds is left
#    off and Cuff is added. No supplier card was in the photo, so no material is claimed; no cost per item was given.
#  - Five photos (packshot, worn, worn close, macro, in the palm) and the size card; the gallery's gold was toned to the stock's paler
#    yellow (comp.py tone), and the card is drawn on the toned packshot.
# autoPublish is turned on for the six sales channels around the create and off again, as in ship_3nov.py, so the cuff shows on every
# channel the moment the owner sets it Active. No status other than DRAFT is sent.
# Usage: ship_cuff_3nov.py -> ../shopify/ship_cuff_3nov.json (variables) and ../shopify/ship_cuff_3nov.graphql (the mutation)
import importlib.util, json, os
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s3", os.path.join(H, "ship_3nov.py")); S3 = importlib.util.module_from_spec(s); s.loader.exec_module(S3)
S2 = S3.S2; S31 = S3.S31
S3.ALTS["Bracelet"] = dict(S31.ALTS["Bracelet"], P="resting in an open palm, to show its size")
S3.ALT_OVERRIDE[("B1", "M")] = "macro detail of one end: the twisted cable, the wrapped collar and the ball"
S3.CODE["B1"] = ""

def create(i):
    p = S3.create(i)
    p["tags"] = sorted((set(p["tags"]) - {"Cubic Zirconia"}) | {"Cuff"})     # no stones on this piece
    return p

if __name__ == "__main__":
    var = {"on": {"autoPublish": True}, "off": {"autoPublish": False}, "b1": create("B1")}
    sel = "{ publication { id autoPublish } userErrors { field message } }"
    ps = ("{ product { id handle status totalInventory tags mediaCount { count } variants(first: 1) { nodes { id sku price compareAtPrice "
          "inventoryQuantity } } } userErrors { field message code } }")
    doc = ("mutation OrbCableCuff($on: PublicationUpdateInput!, $off: PublicationUpdateInput!, $b1: ProductSetInput!) {\n"
           + "".join(f"  on{k}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $on) {sel}\n" for k, p in enumerate(S31.PUBS))
           + f"  b1: productSet(input: $b1, synchronous: true) {ps}\n"
           + "".join(f"  off{k}: publicationUpdate(id: \"gid://shopify/Publication/{p}\", input: $off) {sel}\n" for k, p in enumerate(S31.PUBS))
           + "}\n")
    os.makedirs(OUT, exist_ok=True)
    json.dump(var, open(os.path.join(OUT, "ship_cuff_3nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "ship_cuff_3nov.graphql"), "w").write(doc)
    p = var["b1"]; print(p["handle"], len(p["files"]), "files", p["tags"], p["seo"], p["variants"][0]["sku"], p["variants"][0]["price"],
                         p["variants"][0]["compareAtPrice"], p["variants"][0]["inventoryQuantities"])
