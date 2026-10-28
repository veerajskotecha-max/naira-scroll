# Builds the variables for one Shopify mutation, 28 Oct 2026 (the owner asked for everything in a single approval):
#  - Clarté Baguette Bracelet — Silver (ADT01-SV): the slimmer baguette line from Aditya's photo becomes a second Width,
#    "Slim 5mm" (ADT01-SV-SL, 5 units at ₹1299 against ₹2500 like the Classic), with its four photos (A11: hero, worn, worn
#    close, macro). The Title placeholder becomes the Width option, the existing variant becomes "Classic 6mm" with its two
#    units and takes its own hero, the four Classic photos get "Classic 6mm" alts, and the live description gains the two
#    widths (every other line, including the PVD rhodium lines and the size guide card, kept as it reads live). The owner set
#    the listing to Draft at 09:12 UTC on 28 Oct, so it stays Draft.
#  - Size cards: each bracelet and earring card that is embedded in a live description is added to that listing's gallery,
#    and the Clarté card to the Silver gallery. The gold Clarté and Rivière Classique are Draft, so their galleries are left.
#    The Watch Link Strap Bracelet gets its new card (fileCreate under the name the description links to, plus a gallery copy).
# Usage: ship_28oct.py LIVE_SILVER_DESCRIPTION.html  -> ../shopify/payloads/ship_28oct.json
import json, os, sys, html
H = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(H, "../shopify")
L = {p["handle"]: p for p in json.load(open(f"{S}/listing.json"))}
EMAP = json.load(open(f"{H}/export_map.json")); URL = json.load(open(f"{H}/url_map.json"))
CARDS = json.load(open(os.path.join(H, "../../aditya-jewellery/shopify/payloads/sizecards_28oct.json")))
LOCATION = "gid://shopify/Location/76267389090"; UNITS = 5
PRODUCT = "gid://shopify/Product/10365930569890"; CLASSIC = "gid://shopify/ProductVariant/50749309911202"
CLASSIC_MEDIA = {"A1s_H": "gid://shopify/MediaImage/46625723809954", "A1s_W1": "gid://shopify/MediaImage/46625723842722",
                 "A1s_W2": "gid://shopify/MediaImage/46625723875490", "A1s_M": "gid://shopify/MediaImage/46625723908258"}
DRAFTS = {"gid://shopify/Product/10353404903586", "gid://shopify/Product/10353405001890"}   # gold Clarté, Rivière Classique
e = html.escape

sv = L["clarte-baguette-bracelet-silver"]; name = sv["title"].replace(" — ", ", ")
slim = next(v for v in sv["variants"] if v["src"] == "A11")
alts = {k: f"{name}, {head} — {rest}" for k, alt in sv["images"] for head, _, rest in [alt.partition(", ")]}
media = [{"originalSource": URL[EMAP[k]], "alt": alts[k], "mediaContentType": "IMAGE"} for k, _ in sv["images"] if k.startswith("A11_")]
variant = {"optionValues": [{"optionName": sv["option"], "name": slim["value"]}], "price": "1299.00", "compareAtPrice": "2500.00",
           "inventoryPolicy": "DENY", "inventoryItem": {"sku": slim["sku"], "tracked": True},
           "inventoryQuantities": [{"availableQuantity": UNITS, "locationId": LOCATION}], "mediaSrc": [URL[EMAP["A11_H"]]]}
classic = next(v for v in sv["variants"] if v["src"] == "A1s")

desc = open(sys.argv[1]).read()
widths = "It comes in " + sv["body"].split(" It comes in ")[1].split(" Wear it alone")[0]   # the two sentences on the widths
for a, b in [("The line is about 6mm wide and closes with a slim silver tone fold over clasp, so it lies flat and catches the light "
              "from every side.", e(widths)),
             ("Stack it with a fine round tennis bracelet so the two cuts play off each other.", e(sv["tip"])),
             ("<li>Stone: Baguette cut clear cubic zirconia, approximately 6mm by 3mm, set crosswise</li>",
              "<li>" + e(next(x for x in sv["details"] if x.startswith("Stone"))) + "</li>"),
             ("<li>Width: Approximately 6mm</li>", "<li>" + e(next(x for x in sv["details"] if x.startswith("Width"))) + "</li>")]:
    assert desc.count(a) == 1, a; desc = desc.replace(a, b)

files = [{"id": CLASSIC_MEDIA[k], "alt": alts[k]} for k in CLASSIC_MEDIA]
for f in CARDS["files"]:
    refs = [p for p in f["referencesToAdd"] if p not in DRAFTS]
    if refs: files.append({"id": f["id"], "referencesToAdd": refs})

out = {"product": PRODUCT, "options": [{"name": sv["option"], "position": 1, "values": [{"name": classic["value"]}]}],
       "variants": [variant], "media": media, "classic": [{"id": CLASSIC, "mediaId": CLASSIC_MEDIA["A1s_H"]}],
       "svProduct": {"id": PRODUCT, "descriptionHtml": desc}, "files": files,
       "newFiles": CARDS["newFiles"], "wl": CARDS["wl"], "wlMedia": CARDS["wlMedia"]}
json.dump(out, open(f"{S}/payloads/ship_28oct.json", "w"), ensure_ascii=False, indent=1)
print(slim["sku"], len(media), "photos;", len(files), "file updates (", len(files) - 4, "size cards)")
