# One Shopify mutation (one approval), 13 Nov 2026: the Toggle Link Chain (YF5143, live) after the ad-reel size check.
# The owner chose "Fix all of it": the clasp ring is about 22mm across (the ad reel, against the chain's 4mm links; README.md),
# not the 15mm the listing gave for the whole clasp, and the copy loses its waterproof and tarnish wording, which the house rules
# never use. The SEO title and description named the piece "Ivory Clasp Chain"; both now name the Toggle Link Chain.
# Only descriptionHtml and seo are sent (productUpdate). Status, price, stock, photos and tags are left as they are; the tags
# still read Hypoallergenic, Tarnish Free and Waterproof, held over for the owner (they may drive badges and filters).
# OLD is the live text read on 13 Nov (updatedAt 2026-11-13T03:41:56Z, unchanged at 11:4x UTC); each phrase in FIX is found
# exactly once. Usage: python3 -I toggle_13nov.py -> toggle_13nov.json (variables) and toggle_13nov.graphql (the mutation)
import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
PRODUCT = "gid://shopify/Product/9294915567778"
OLD = ("<p>A chain that closes with a turn rather than a catch. This necklace runs 50cm in a 4mm width, finished with a gold toggle bar "
       "and ring clasp of about 15mm that sits at the front or the side as you prefer. The PVD coating is a non tarnish finish, so the "
       "gold tone holds through daily wear. Wear it over a knit in winter, or alone on a warm evening.</p><p><strong>STYLING TIP:</strong> "
       "Wear it with the toggle turned to the front so the clasp becomes part of it.</p><p><strong>Details</strong></p><ul>\n"
       "<li>Length: 50cm</li>\n<li>Width: 4mm</li>\n<li>Weight: 12g</li>\n<li>Closure: Gold toggle bar and ring clasp, approximately 15mm</li>\n"
       "<li>Finish: Non tarnish</li>\n<li>Plating: PVD 18K gold coating, anti-tarnish</li>\n<li>Material: Surgical stainless steel</li>\n"
       "<li>PVD vs plating: Regular plating is a soft layer that wears off over time. PVD is bonded to the metal in a vacuum, so it is far "
       "harder, stands up to sweat and keeps its colour much longer.</li>\n</ul><p><img src=\"https://cdn.shopify.com/s/files/1/0680/9606/"
       "5698/files/toggle-link-chain-size-guide.jpg\" alt=\"Size guide — Toggle Link Chain\" width=\"420\"></p><p><strong>Care</strong></p>"
       "<p>Waterproof and tarnish free, so daily wear and water are fine. Keep it away from perfume and harsh chemicals, wipe with a soft dry "
       "cloth and store it flat in its pouch.</p><p>You will receive your piece in a Naira Petite box.</p>")
FIX = [("finished with a gold toggle bar and ring clasp of about 15mm that sits at the front or the side as you prefer.",
        "finished with a gold toggle clasp that sits at the front or the side as you prefer: a ring of about 22mm across and a bar of about 15mm."),
       ("The PVD coating is a non tarnish finish, so the gold tone holds through daily wear.",
        "The PVD coating is bonded to the steel, so the gold tone holds through daily wear."),
       ("<li>Closure: Gold toggle bar and ring clasp, approximately 15mm</li>",
        "<li>Closure: Gold toggle clasp, the ring approximately 22mm across and the bar approximately 15mm</li>"),
       ("<li>Finish: Non tarnish</li>", "<li>Finish: Polished gold tone</li>"),
       ("<li>Plating: PVD 18K gold coating, anti-tarnish</li>", "<li>Plating: PVD 18k gold tone coating</li>"),
       ("<p>Waterproof and tarnish free, so daily wear and water are fine. Keep it away from perfume and harsh chemicals, wipe with a soft "
        "dry cloth and store it flat in its pouch.</p>",
        "<p>Keep it dry and away from perfume and harsh chemicals. Wipe with a soft dry cloth and store it flat in its pouch.</p>")]
NEVER = re.compile(r"\b(real|diamonds?|waterproof|tarnish\w*|anti-tarnish|freshwater|hypoallergenic)\b", re.I)


def build():
    body = OLD
    for old, new in FIX:
        assert body.count(old) == 1, old
        body = body.replace(old, new)
    second = re.sub(r"<[^>]+>", "", body).split(". ")[1].rstrip(".")
    seo = {"title": "Toggle Link Chain — Necklace | Naira Petite", "description": f"{second}. Toggle Link Chain by Naira Petite."}
    words = json.dumps([body, seo], ensure_ascii=False)
    assert not NEVER.search(words), NEVER.search(words).group(0)
    assert "22mm" in seo["description"] and len(seo["description"]) <= 320
    return {"id": {"id": PRODUCT}, "p": {"descriptionHtml": body, "seo": seo}}


DOC = ("mutation ToggleClasp13Nov($id: ProductUpdateIdentifiers!, $p: ProductUpdateInput!) {\n"
       "  toggle: productUpdate(identifier: $id, product: $p) { product { id handle status updatedAt descriptionHtml seo { title description } "
       "tags mediaCount { count } variants(first: 1) { nodes { sku price compareAtPrice inventoryQuantity } } } userErrors { field message } }\n}\n")

if __name__ == "__main__":
    var = build()
    json.dump(var, open(os.path.join(H, "toggle_13nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(H, "toggle_13nov.graphql"), "w").write(DOC)
    print(var["p"]["seo"]); print(len(var["p"]["descriptionHtml"]), "chars")
