# Builds one Shopify mutation (the owner asked for a single approval) that puts each card in ../cards.json on its listing:
#   fileCreate stores the card as <handle>-size-guide.jpg, the name the description links to. molten-panel-bracelet's name
#   was already taken by its unused 21 Oct card (17 cm, from before the piece was found to be a rigid bangle), which is
#   replaced in place; every other name was free;
#   productUpdate, once per listing, embeds the card before the Care paragraph, the house position, and adds a copy of it
#   to the end of the gallery. Every other line of each description reads as it does live.
# Usage: ship.py LIVE.json  (the storefront read of the listings: handle -> {id, descriptionHtml})
#        -> ../payloads/ship_28oct_cards.json (variables) and ../payloads/ship_28oct_cards.graphql (the mutation)
import html, json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(H)
CDN = "https://cdn.shopify.com/s/files/1/0680/9606/5698/files/"; CARE = "<p><strong>Care</strong></p>"
cards = json.load(open(os.path.join(C, "cards.json")))["cards"]; URL = json.load(open(os.path.join(C, "url_map.json")))
live = json.load(open(sys.argv[1])); REPLACE = {"molten-panel-bracelet"}
files, var, fields, heads = [], {}, [], []
for i, c in enumerate(cards):
    h, alt = c["handle"], f"Size guide — {c['title']}"
    p = live[h]; assert p["id"] == c["id"], h
    desc = p["descriptionHtml"]; assert desc.count(CARE) == 1 and "size-guide" not in desc, h
    img = f'<p><img src="{CDN}{h}-size-guide.jpg" alt="{html.escape(alt)}" width="420"></p>'
    f = {"originalSource": URL[h], "filename": f"{h}-size-guide.jpg", "alt": alt, "contentType": "IMAGE"}
    if h in REPLACE: f["duplicateResolutionMode"] = "REPLACE"
    files.append(f)
    var[f"p{i}"] = {"id": c["id"], "descriptionHtml": desc.replace(CARE, img + CARE)}
    var[f"m{i}"] = [{"originalSource": URL[h], "alt": alt, "mediaContentType": "IMAGE"}]
    heads.append(f"$p{i}: ProductUpdateInput!, $m{i}: [CreateMediaInput!]")
    fields.append(f"  u{i}: productUpdate(product: $p{i}, media: $m{i}) {{ product {{ handle }} userErrors {{ field message }} }}")
var["files"] = files
doc = ("mutation SizeCards28Oct($files: [FileCreateInput!]!, " + ", ".join(heads) + ") {\n"
       "  c: fileCreate(files: $files) { files { id fileStatus alt } userErrors { field message code } }\n" + "\n".join(fields) + "\n}\n")
os.makedirs(os.path.join(C, "payloads"), exist_ok=True)
json.dump(var, open(os.path.join(C, "payloads/ship_28oct_cards.json"), "w"), ensure_ascii=False, indent=1)
open(os.path.join(C, "payloads/ship_28oct_cards.graphql"), "w").write(doc)
print(len(cards), "listings;", len(files), "files;", len(doc), "chars of mutation")
