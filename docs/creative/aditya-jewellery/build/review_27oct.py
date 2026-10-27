# Review sheet for the three 27 Oct pieces (shopify/proposed_27oct.json): per piece the supplier photo, then the four listing
# photos in order (hero, worn, worn close, macro), with the proposed name, SKU, price and the measured sizes -> oct27_review.jpg
import json, os
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(H, "..")
P = json.load(open(f"{D}/shopify/proposed_27oct.json")); E = json.load(open(f"{H}/export_map.json"))
FD = os.path.join(H, "../../aditya-bracelets/build/fonts")
F1, F2, F3 = (ImageFont.truetype(f"{FD}/Jost-500.ttf", 30), ImageFont.truetype(f"{FD}/Jost-500.ttf", 22),
              ImageFont.truetype(f"{FD}/Jost-500.ttf", 19))
TW, TH, GAP, M, HEAD, CAP = 400, 497, 12, 28, 92, 34
BG, INK, SOFT = (244, 235, 226), (28, 23, 18), (110, 98, 86)
SIZES = {"J19": "About 20 mm long  ·  huggie 10.5 mm tall, 2.5 mm face  ·  round stone 4 mm, four claws",
         "J20": "About 17 mm long  ·  three marquise petals 8.5 mm across  ·  pear drop 6 × 4.5 mm  ·  post",
         "J21": "About 9 mm wide, 2.5 mm thick, 17 cm long  ·  five rows of links  ·  flexible, bends round the wrist"}
CAPS = ["Supplier photo", "Hero", "Worn", "Worn, close", "Macro"]
RUPEE = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"   # Jost has no rupee sign
def text(xy, s, font, fill):  # draws s, setting each rupee sign in Inter at the same size
    x, y = xy; alt = ImageFont.truetype(RUPEE, font.size)
    for part in s.replace("₹", "\0₹\0").split("\0"):
        f = alt if part == "₹" else font; d.text((x, y), part, font=f, fill=fill); x += d.textlength(part, font=f)
W = 2 * M + 5 * TW + 4 * GAP; Hh = M + len(P) * (HEAD + TH + CAP + M)
sheet = Image.new("RGB", (W, Hh), BG); d = ImageDraw.Draw(sheet)
for r, p in enumerate(P):
    y = M + r * (HEAD + TH + CAP + M)
    text((M, y), f"{p['title']}   ₹{p['price']}", F1, INK)
    text((M, y + 42), f"{p['sku']}  ·  supplier {p['supplier']}  ·  {SIZES[p['key']]}", F3, SOFT)
    sup = Image.open(f"{D}/refs/{p['key']}_full.jpg").convert("RGB"); sup.thumbnail((TW, TH))
    tile = Image.new("RGB", (TW, TH), (30, 27, 24)); tile.paste(sup, ((TW - sup.width) // 2, (TH - sup.height) // 2))
    tiles = [tile] + [Image.open(f"{D}/exports/{E[k]}").convert("RGB").resize((TW, TH), Image.LANCZOS) for k, _ in p["images"]]
    for i, t in enumerate(tiles):
        x = M + i * (TW + GAP); sheet.paste(t, (x, y + HEAD))
        d.text((x + 2, y + HEAD + TH + 6), CAPS[i], font=F2, fill=SOFT)
sheet.save(f"{D}/oct27_review.jpg", quality=88); print(sheet.size)
