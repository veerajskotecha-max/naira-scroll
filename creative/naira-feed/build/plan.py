"""plan.py - builds plan.json: the Naira Petite Instagram feed, 12 weeks in six colour chapters, from the
Higgsfield library (tagged.json + colors.json + quality.json) and the live Shopify catalogue (products.json).

Grid logic: every row of three is one product family seen three ways, left to right:
  the object (still life / packshot)  |  worn (on the model)  |  the detail (macro).
Five rows make a chapter; six chapters make the season. Pinned row on top is evergreen.
Publication order runs bottom-right to top-left so the finished grid reads as designed."""
import json, re, sys, random, datetime, collections
from pathlib import Path

D = Path(sys.argv[1]); random.seed(11)
T = json.load(open(D / "tagged.json")); C = json.load(open(D / "colors.json")); Q = json.load(open(D / "quality.json"))
P = json.load(open(D / "products.json"))["products"]
for x in T:
    x.update(C.get(x["id"], {})); x["ph"] = Q.get(x["id"], {}).get("ph", 0); x["smear"] = Q.get(x["id"], {}).get("smear2", 0)
    x["pal"] = x.get("pal") or "cream"; x["prompt"] = x["prompt"] or ""

# ---------------------------------------------------------------- catalogue
CLOTHING = {p["title"] for p in P if p["vendor"] != "Naira Petite"}
PROD = {}
for p in P:
    if p["title"] in CLOTHING: continue
    v = p["variants"][0]
    PROD[p["title"]] = {"name": p["title"], "price": int(float(v["price"])), "available": any(w["available"] for w in p["variants"]),
                        "url": f"https://nairaflore.com/products/{p['handle']}", "type": (p.get("product_type") or "").lower().rstrip("s")}
CAT_WORD = {"earring": "earrings", "ring": "rings", "necklace": "necklaces", "bracelet": "bracelets", "set": "sets"}
CAT_URL = {"earring": "https://nairaflore.com/collections/earrings", "ring": "https://nairaflore.com/collections/rings",
           "necklace": "https://nairaflore.com/collections/necklaces", "bracelet": "https://nairaflore.com/collections/bracelets",
           "set": "https://nairaflore.com/collections/all"}

# ---------------------------------------------------------------- exclusions
FASHION = re.compile(r"lehenga|saree|\bsari\b|bikini|swim|poolside|co-?ord|kurta|\bgown|resort|naira flore, a luxury|indo-?western|couture|atelier|bloom edit|petal co|lookbook", re.I)
TEXT = re.compile(r"typography|wordmark reads|magazine cover|reads ['\"]|reading ['\"]|with the (words|text|headline) ['\"]|text reading|handwritten|note (that )?(reads|says)|card (that )?(reads|says)|add (a |the )?(headline|title|caption|text)|lettering that|calligraphy", re.I)
GRIDRX = re.compile(r"build one image|grid of 12|contact sheet|3-column x 4-row", re.I)
VETO = {
"6c04e7fb-a571-4d29-bd14-47db4f5ccdbf": "a pile of mixed pieces in a locker: one product per frame",
"a3e35409-ab0f-4281-92c6-73d59edcb040": "surgical tray prop: wrong register for the brand",
"60525400-60f3-4c90-a674-373f878d03ca": "shattered glass: too violent for the pale hours"
}
for x in T:
    r = []
    if x["id"] in VETO: r.append("art director veto: " + VETO[x["id"]])
    if x["model"] in ("image_background_remover", "outpaint"): r.append("processing step")
    if FASHION.search(x["prompt"]): r.append("clothing shoot")
    if x["day"] < "2026-04-01": r.append("early clothing shoot")
    if x["prod"] in CLOTHING: r.append("clothing product"); x["prod"] = None
    if TEXT.search(x["prompt"]): r.append("rendered text")
    if GRIDRX.search(x["prompt"]): r.append("composite grid")
    if x["smear"] > 3.5: r.append("smeared edges")
    if x.get("plate"): r.append("background plate, no jewellery")
    x["excl"] = r
    x["landscape"] = x["ar"] in ("16:9", "3:2", "4:3")
usable = [x for x in T if not x["excl"]]
byid = {x["id"]: x for x in T}

# ---------------------------------------------------------------- chapters
D0 = datetime.date(2026, 11, 2)
CH = [
    dict(key="red", num="I", name="The Red Room", pal=["red", "black", "charcoal", "gold"], model_pal=["apricot", "cream", "black", "charcoal"],
         kw=r"diya|\blamp|candle|marigold|pomegranate|festive|diwali|crimson|ruby|garnet|burgundy|wine|flame|cherry|lacquer|maroon",
         line="Lit for the season.", about="Diwali week. Deep reds, black lacquer, candle light and the gold that reads best against them.",
         tags=["#diwalijewellery", "#festivejewellery", "#diwaligifts"]),
    dict(key="cream", num="II", name="The Index", pal=["cream", "white"], model_pal=["cream", "white", "apricot"],
         kw=r"plaster|cube|plinth|packshot|catalogue|index|straight-on|second angle|standing up|lying flat",
         line="Every piece, in order.", about="The catalogue laid bare: cream plaster, straight light, one piece per frame. The wedding-season index.",
         tags=["#everydayjewellery", "#jewellerycatalogue", "#weddingseason"]),
    dict(key="sage", num="III", name="Sage", pal=["sage", "green", "grey"], model_pal=["sage", "grey", "cream"],
         kw=r"\bsage\b|celadon|olive|\bleaf|leaves|linen|pea pod|moss|eucalyptus|fern|mint|green|steel|chess|quiet",
         line="Quiet, on green.", about="Celadon dishes, sage linen, pea pods and brushed steel. The quiet-luxury fortnight.",
         tags=["#quietluxury", "#sagegreen", "#minimaljewellery"]),
    dict(key="blush", num="IV", name="The Gift", pal=["blush", "pink", "cream", "white"], model_pal=["cream", "blush", "apricot"],
         kw=r"\bbox\b|ribbon|\bbow\b|gift|wrap|tissue|envelope|card|pearl|satin|blush|rose|peony|present",
         line="Wrapped, with care.", about="Christmas and New Year gifting. The blush Naira box, ribbon, pearls and satin.",
         tags=["#giftsforher", "#giftideas", "#pearljewellery"]),
    dict(key="lilac", num="V", name="Lilac", pal=["lilac", "blue", "pink"], model_pal=["cream", "lilac", "apricot"],
         kw=r"lilac|lavender|butterfly|hydrangea|periwinkle|violet|pastel|rainbow|candy|iris|wisteria|mauve|\bblue\b|sky|cornflower",
         line="The pale hours.", about="New Year light: lilac paper, lavender, butterflies and pastel tennis rows.",
         tags=["#pastelaesthetic", "#lilac", "#newyearnewjewellery"]),
    dict(key="apricot", num="VI", name="Apricot", pal=["apricot", "gold", "cream"], model_pal=["apricot", "cream"],
         kw=r"apricot|peach|croissant|honey|\bsun|citrus|lemon|lime|silk|dupion|amber|butter|marmalade|orange|warm",
         line="Warm, by the window.", about="Raw apricot silk, halved fruit, croissants and brushed gold. The sunny close of the season.",
         tags=["#goldjewellery", "#apricot", "#sunlitjewellery"]),
]
MIN_LUM = {"red": 0.0, "cream": 0.5, "sage": 0.38, "blush": 0.45, "lilac": 0.42, "apricot": 0.4}
for i, c in enumerate(CH):
    c["min_lum"] = MIN_LUM[c["key"]]
    c["start"] = D0 + datetime.timedelta(days=14 * i); c["end"] = c["start"] + datetime.timedelta(days=13); c["rx"] = re.compile(c["kw"], re.I)
BRAND_TAGS = ["#nairapetite", "#nairaflore", "#demifinejewellery", "#18kgoldcoated"]
EVENTS = {"2026-11-06": "Dhanteras", "2026-11-08": "Diwali", "2026-11-10": "Bhai Dooj", "2026-12-25": "Christmas", "2026-12-31": "New Year's Eve",
          "2027-01-01": "New Year", "2027-01-14": "Makar Sankranti", "2027-01-26": "Republic Day"}

# ---------------------------------------------------------------- scoring
def pal_score(x, pals):
    return {0: 3.6, 1: 2.8, 2: 2.0, 3: 1.2}.get(pals.index(x["pal"]), 0) if x["pal"] in pals else 0

STYLE_NEG = re.compile(r"crushed|soft-?drink can|soda can|black (almond )?nails|cigarette|smok|grunge|graffiti|shattered|broken glass|locker|surgical|kidney dish|scalpel|syringe", re.I)
def ch_score(x, c, col):
    s = pal_score(x, c["model_pal"] if col == "worn" else c["pal"])
    if STYLE_NEG.search(x["prompt"]): s -= 2.5
    if col != "worn" and x.get("lum", 0.5) < c["min_lum"]: s -= 3.0
    if c["key"] == "red" and x.get("lum", 0.5) > 0.72 and x["pal"] in ("cream", "white"): s -= 1.5
    if c["rx"].search(x["prompt"]): s += 1.2
    if col != "worn" and x["pal"] not in c["pal"]: s -= 2.5 if not c["rx"].search(x["prompt"]) else 1.0
    s += {"4:5": 1.0, "3:4": 1.0, "1:1": 0.4, "9:16": -0.6}.get(x["ar"], 0.2)
    if x.get("edited"): s += 0.6
    if x["liked"]: s += 1.5
    if x["prod"]: s += 0.8
    s += min(0.8, (datetime.date.fromisoformat(x["day"]) - datetime.date(2026, 6, 1)).days / 180)
    return s

COLS = ["object", "worn", "detail"]
KINDS = {"object": {"still life", "witty", "flat lay", "texture", "packshot"}, "worn": {"on-model"}, "detail": {"macro"}}
def col_ok(x, col):
    if col == "worn": return x["kind"] == "on-model"
    if col == "detail": return x["kind"] == "macro"
    return x["kind"] in KINDS["object"]

def ham(a, b): return bin(a ^ b).count("1")
used = set(); used_ph = []; series_use = collections.Counter(); prod_use = collections.Counter()
def near_dupe(x):
    return any(ham(x["ph"], h) <= 6 for h in used_ph)
def take(x, role):
    used.add(x["id"]); used_ph.append(x["ph"]); series_use[x["series"]] += 1
    if x["prod"]: prod_use[x["prod"]] += 1
    x["role"] = role

def pick(c, col, cat, anchor=None, n=1, exclude=(), relax=False, kind_pref=None):
    cands = []
    trio = collections.Counter((y["prod"], y["kind"]) for y in usable if y["prod"] and y["id"] not in used and y["kind"] in ("on-model", "macro") and y["pal"] in c["pal"] + c["model_pal"])
    for x in usable:
        if x["id"] in used or x["id"] in exclude or x["landscape"]: continue
        if not col_ok(x, col): continue
        if cat and x["cat"] != cat and not relax: continue
        s = ch_score(x, c, col) - 0.9 * series_use[x["series"]] - 1.2 * prod_use[x["prod"]] * (x["prod"] is not None)
        if cat and x["cat"] == cat: s += 1.0
        if anchor is not None:
            if x["prod"] and x["prod"] == anchor["prod"]: s += 3.5
            if x["pal"] == anchor["pal"]: s += 0.8
            if x["series"] == anchor["series"]: s += 0.5
        if kind_pref and x["kind"] in kind_pref: s += 1.2
        if col == "object" and x["prod"]:
            s += 1.6 * min(1, trio.get((x["prod"], "on-model"), 0)) + 1.0 * min(1, trio.get((x["prod"], "macro"), 0))
        cands.append((s, x))
    cands.sort(key=lambda t: -t[0]); out = []
    for s, x in cands:
        if near_dupe(x): continue
        out.append(x)
        if len(out) >= n: break
    return out

# ---------------------------------------------------------------- the grid
FAMILIES = ["earring", "ring", "necklace", "bracelet"]
def row_cats(ci):   # rotate the family order every chapter so the index reel and each row move through the four families
    r = FAMILIES[ci % 4:] + FAMILIES[:ci % 4]
    return r + [None]
SLOT = {  # (row, col) -> type
    (0, "object"): ("carousel", 8), (0, "worn"): ("single", 1), (0, "detail"): ("single", 1),
    (1, "object"): ("reel", 36), (1, "worn"): ("single", 1), (1, "detail"): ("carousel", 5),
    (2, "object"): ("single", 1), (2, "worn"): ("reel", 8), (2, "detail"): ("single", 1),
    (3, "object"): ("carousel", 6), (3, "worn"): ("single", 1), (3, "detail"): ("reel", 10),
    (4, "object"): ("single", 1), (4, "worn"): ("carousel", 4), (4, "detail"): ("reel", 8)}
REEL_KIND = {(1, "object"): "index", (2, "worn"): "worn", (3, "detail"): "upclose", (4, "detail"): "upclose"}

tiles = []
def publish_order(k):      # k = 0..14 -> (row, col): bottom-right first so the finished grid reads top-left as designed
    return 4 - k // 3, COLS[2 - k % 3]

for ci, c in enumerate(CH):
    chapter_tiles = {}
    # fill rows top to bottom; anchor each row on the object tile so the three share a product where the library allows
    ROW_CAT = row_cats(ci)
    for row in range(5):
        cat = ROW_CAT[row]; anchor = None
        for col in COLS:
            typ, n = SLOT[(row, col)]
            kp = {"still life", "witty", "flat lay", "texture"} if (col == "object" and c["key"] != "cream") else ({"packshot"} if col == "object" else None)
            got = pick(c, col, cat, anchor, 1, kind_pref=kp) or pick(c, col, cat, anchor, 1, relax=True, kind_pref=kp) or pick(c, col, None, anchor, 1, relax=True)
            if not got: raise SystemExit(f"no image for {c['key']} row {row} {col}")
            x = got[0]; take(x, "cover"); anchor = anchor or x
            tile = {"id": f"{c['key']}-{row}-{col}", "chapter": ci, "row": row, "col": col, "type": typ, "cover": x["id"], "slides": [x["id"]],
                    "cat": x["cat"] or cat, "prod": x["prod"]}
            if typ == "carousel":
                extra = pick(c, col, tile["cat"], x, n - 1, relax=True) if col != "object" else pick(c, col, tile["cat"], x, n - 1, relax=True, kind_pref=kp)
                for e in extra: take(e, "slide")
                tile["slides"] += [e["id"] for e in extra]
            if typ == "reel":
                rk = REEL_KIND[(row, col)]
                if rk == "index":
                    pool = [y for y in usable if y["id"] not in used and y["kind"] == "packshot" and y["cat"] == tile["cat"] and y["pal"] in ("cream", "white") and not y["landscape"]]
                    if len(pool) < 12:   # a family short of fresh packshots borrows frames already cut into an earlier index reel
                        pool += [y for y in usable if y["id"] in used and y.get("role") == "reel" and y["kind"] == "packshot" and y["cat"] == tile["cat"]]
                    pool.sort(key=lambda y: (y["series"], y["t"])); frames = pool[:min(n - 1, 29)]
                else:
                    frames = pick(c, col, tile["cat"], x, n - 1, relax=True)
                for f in frames:
                    if f["id"] not in used: take(f, "reel")
                tile["frames"] = [x["id"]] + [f["id"] for f in frames]; tile["reel"] = rk
            chapter_tiles[(row, col)] = tile
    for k in range(15):
        row, col = publish_order(k); tile = chapter_tiles[(row, col)]
        day = c["start"] + datetime.timedelta(days=max(0, k - 1))
        tile["date"] = day.isoformat(); tile["k"] = k
        tile["time"] = "12:30" if tile["type"] == "reel" else ("19:30" if k != 0 else "19:30")
        if k == 0: tile["time"] = "12:30"
        tiles.append(tile)

# pinned row: evergreen, cream, the three columns at their purest
PIN = []
for col, cat, typ, n in (("object", None, "carousel", 10), ("worn", None, "single", 1), ("detail", None, "single", 1)):
    c = CH[1]; kp = {"packshot"} if col == "object" else None
    x = pick(c, col, None, None, 1, relax=True, kind_pref=kp)[0]; take(x, "cover")
    tile = {"id": f"pin-{col}", "chapter": -1, "row": -1, "col": col, "type": typ, "cover": x["id"], "slides": [x["id"]], "cat": x["cat"], "prod": x["prod"],
            "date": D0.isoformat(), "time": "19:30", "k": -1, "pinned": True}
    if typ == "carousel":
        ex = []
        for cat2 in ("earring", "ring", "necklace", "bracelet"):
            ex += pick(c, col, cat2, None, 2, kind_pref=kp)
        for e in ex: take(e, "slide")
        tile["slides"] += [e["id"] for e in ex][:n - 1]
    PIN.append(tile)

# ---------------------------------------------------------------- captions
def prodline(x_id, cat):
    x = byid[x_id]; p = PROD.get(x["prod"]) if x["prod"] else None
    if p:
        avail = f"₹{p['price']:,}" if p["available"] else "waitlist open"
        return p["name"], avail, p["url"], p
    return None, None, CAT_URL.get(cat or "set", CAT_URL["set"]), None

MAT = "[ 18k gold coated · rhodium coated ]"
OBJ_LINES = {
    "red": ["{N}, where the lamps are. Deep red, black lacquer, and the gold that reads best against them.", "{N}, set down for the night. The week the house fills with candle light.", "Dhanteras is for buying gold. {N} counts."],
    "cream": ["{N}. Cream plaster, straight light, nothing else in the frame.", "The index, one piece at a time. {N}.", "{N}, photographed the way we check every piece before it ships."],
    "sage": ["{N} on celadon. The quiet fortnight.", "{N}, on sage linen, in the kind of light that asks nothing.", "Green does something to gold. {N}."],
    "blush": ["{N}, in the blush box it arrives in.", "The gift question, answered. {N}.", "Ribbon, tissue, {N}. Ready to hand over."],
    "lilac": ["{N} on lilac paper. The pale hours of the new year.", "{N}, lavender, a slow morning.", "Pastel is a mood, not a trend. {N}."],
    "apricot": ["{N} on raw apricot silk.", "{N}, next to the fruit it was named for.", "Warm light, warm gold. {N}."]}
WORN_LINES = {
    "red": ["{N}, worn with the good silk.", "Festive dressing starts at the ear. {N}.", "{N}. On her, in lamp light."],
    "cream": ["{N}, worn plain, so you can see the scale.", "This is how big it really is. {N}, on her.", "{N}. Everyday, every day."],
    "sage": ["{N} with a green shirt and nothing else.", "{N}, worn quietly.", "On her: {N}. Minimal, by design."],
    "blush": ["{N}, worn for the party, kept for the mornings after.", "The one she'll open first. {N}.", "{N} on her. Gift-ready."],
    "lilac": ["{N}, worn on a pale morning.", "{N}. Soft colour, clear light.", "The new-year ear. {N}."],
    "apricot": ["{N}, worn in the sun.", "{N} on her, by the window.", "Gold on warm skin. {N}."]}
DET_LINES = {
    "red": ["Up close: {N}. Every claw, every stone, in candle light.", "The detail you only see this close. {N}."],
    "cream": ["Up close: {N}. Four claws, not glue.", "See it up close. {N}, at the scale the setter works at."],
    "sage": ["Up close: {N} on celadon.", "{N}, closer than the eye goes."],
    "blush": ["Up close: {N}. The finish you'll notice when it's on.", "{N}, close enough to read the setting."],
    "lilac": ["Up close: {N} on lilac.", "{N}, in the pale light, up close."],
    "apricot": ["Up close: {N} on silk.", "{N}, the setting in warm light."]}
GENERIC = {"earring": "these earrings", "ring": "this ring", "necklace": "this necklace", "bracelet": "this bracelet", "set": "this set", None: "this piece"}
PLAIN = {"earring": "Earrings", "ring": "Ring", "necklace": "Necklace", "bracelet": "Bracelet", "set": "Set", None: "Jewellery"}
REEL_HOOK = {"index": "Every {cat} we make, in 12 seconds.", "worn": "{cat}, on her. Eight pieces, one minute.", "upclose": "Closer. {cat}, at setter's distance."}
REEL_AUDIO = {"index": "Metronomic, 120 bpm, no vocals (the frames flip on the beat).", "worn": "Soft piano, slow. Cut on the phrase.", "upclose": "Room tone with a quiet string pad. No beat."}

def caption(tile):
    c = CH[tile["chapter"]] if tile["chapter"] >= 0 else CH[1]
    name, avail, url, p = prodline(tile["cover"], tile["cat"])
    N = name or GENERIC.get(tile["cat"], "this piece")
    lines = {"object": OBJ_LINES, "worn": WORN_LINES, "detail": DET_LINES}[tile["col"]][c["key"]]
    body = lines[(tile["row"] + sum(map(ord, tile["id"]))) % len(lines)].format(N=N)
    body = body[0].upper() + body[1:]
    if tile["type"] == "carousel":
        body += f" Swipe for {len(tile['slides']) - 1} more." if tile["col"] != "worn" else f" Swipe to see it worn {len(tile['slides']) - 1} more ways."
    if tile["type"] == "reel":
        body = REEL_HOOK[tile["reel"]].format(cat=CAT_WORD.get(tile["cat"], "pieces").capitalize()) + " " + body
    if tile.get("pinned"):
        body = {"object": "The index. Ten pieces from the four families, on cream plaster. Start here.",
                "worn": "Scale, honestly. Everything we make, photographed on a person before it is photographed on a plinth.",
                "detail": "See it up close. Claws, not glue. The setting is the point."}[tile["col"]]
    tail = [MAT]
    if p: tail.append(f"{name} · {avail} · nairaflore.com")
    else: tail.append(f"Shop {CAT_WORD.get(tile['cat'], 'the collection')} at nairaflore.com")
    tail.append("Hypoallergenic. Made to be worn every day.")
    tags = BRAND_TAGS + c["tags"][:2]
    cap = body + "\n\n" + "\n".join(tail)
    assert "!" not in cap, cap
    alt = f"{name or PLAIN.get(tile['cat'], 'Jewellery')} by Naira Petite, {dict(object='photographed as a still life', worn='worn on a model', detail='in macro detail')[tile['col']]}, from {c['name'] if c['name'].startswith('The') else 'the ' + c['name']} chapter."
    return cap, tags, alt, url, (p and {"name": name, "price": p["price"], "available": p["available"], "url": url})

for t in tiles + PIN:
    cap, tags, alt, url, prod = caption(t)
    t.update({"caption": cap, "tags": tags, "alt": alt, "url": url, "product": prod})
    if t["type"] == "reel":
        n = len(t["frames"]); t["reelmeta"] = {"kind": t["reel"], "frames": n, "seconds": round(n * (0.33 if t["reel"] == "index" else 1.5), 1),
                                                "hook": REEL_HOOK[t["reel"]].format(cat=CAT_WORD.get(t["cat"], "pieces").capitalize()),
                                                "audio": REEL_AUDIO[t["reel"]], "cover": t["cover"],
                                                "cut": "Stop-motion: one frame per beat, the piece stays centred, the background never moves." if t["reel"] == "index" else
                                                       ("Slow dissolves, 1.5 s per frame, end on the ear." if t["reel"] == "worn" else "Push in 10% over each frame, cut on the stone.")}

# ---------------------------------------------------------------- stories
STORY_SLOTS = [("09:00", {"texture", "still life", "witty", "flat lay", "packshot"}, "morning"), ("13:00", {"macro"}, "detail"), ("21:00", {"on-model", "packshot", "still life"}, "shop")]
STICKER = {"morning": ["poll: gold or silver today", "question box: what are you wearing this week", "emoji slider: how much shine", "quiz: guess the stone"],
           "detail": ["tap-through: three pieces, same setting", "countdown to the next drop", "link: see it up close on the site", "mention: tag a friend who wears gold"],
           "shop": ["link sticker: shop this piece", "product sticker with price", "link sticker: the index", "poll: ring or bracelet"]}
stories = []; story_used = set()
vert = [x for x in usable if x["ar"] == "9:16" and x["id"] not in used]
day = D0
for d in range(84):
    ci = min(5, d // 14); c = CH[ci]; frames = []
    for si, (tm, kinds, role) in enumerate(STORY_SLOTS):
        cands = [x for x in vert if x["id"] not in story_used and x["kind"] in kinds]
        cands.sort(key=lambda x: -(ch_score(x, c, "worn" if x["kind"] == "on-model" else "object") + 0.6 if x["pal"] in c["pal"] else ch_score(x, c, "object")))
        if not cands: cands = [x for x in vert if x["id"] not in story_used]
        if not cands: break
        x = cands[0]; story_used.add(x["id"]); x["role"] = "story"
        note = STICKER[role][(d + si) % len(STICKER[role])]
        ev = EVENTS.get(day.isoformat())
        if ev and si == 0: note = f"{ev}: a plain greeting card frame first, then this."
        frames.append({"time": tm, "id": x["id"], "role": role, "sticker": note, "cat": x["cat"], "prod": x["prod"]})
    stories.append({"date": day.isoformat(), "chapter": ci, "frames": frames, "event": EVENTS.get(day.isoformat())})
    day += datetime.timedelta(days=1)

# highlights
HL = [("The Index", "cream", "packshot"), ("Worn", "cream", "on-model"), ("Up close", "cream", "macro"), ("Red Room", "red", None),
      ("Sage", "sage", None), ("The Gift", "blush", None), ("Lilac", "lilac", None), ("Apricot", "apricot", None)]
highlights = []; hl_used = set()
for name, key, kind in HL:
    c = next(cc for cc in CH if cc["key"] == key)
    cands = [x for x in usable if x["id"] not in used and x["id"] not in story_used and x["id"] not in hl_used and (kind is None or x["kind"] == kind) and not x["landscape"]
             and (kind is not None or x["pal"] in c["pal"])]
    cands.sort(key=lambda x: -ch_score(x, c, "worn" if x["kind"] == "on-model" else "object"))
    x = cands[0]; x["role"] = "highlight"; hl_used.add(x["id"]); highlights.append({"name": name, "cover": x["id"], "chapter": c["key"]})

# ---------------------------------------------------------------- roles for everything else
feed_ph = [byid[i]["ph"] for i in used]
for x in T:
    if x.get("role"): continue
    if x["excl"]: x["role"] = "excluded"; continue
    if x["landscape"]: x["role"] = "bank"; continue
    if any(ham(x["ph"], h) <= 6 for h in feed_ph): x["role"] = "variant"; continue
    if x["kind"] == "packshot": x["role"] = "catalogue"; continue
    if x["ar"] in ("4:5", "9:16") and x["kind"] in ("still life", "witty", "texture", "flat lay", "on-model", "macro"): x["role"] = "ads"; continue
    x["role"] = "bank"
roles = collections.Counter(x["role"] for x in T)

# ---------------------------------------------------------------- export
lib_order = sorted(T, key=lambda x: -x["t"])
for i, x in enumerate(lib_order): x["ti"] = i
plan_ids = []
for t in tiles + PIN:
    plan_ids += t["slides"] + t.get("frames", [])
for s in stories: plan_ids += [f["id"] for f in s["frames"]]
plan_ids += [h["cover"] for h in highlights]
plan_ids = list(dict.fromkeys(plan_ids))
cover_ids = list(dict.fromkeys([i for t in tiles + PIN for i in t["slides"]]))
story_ids = list(dict.fromkeys([f["id"] for s in stories for f in s["frames"]]))
for i, pid in enumerate(plan_ids): byid[pid]["si"] = i
for i, pid in enumerate(cover_ids): byid[pid]["mi"] = i
for i, pid in enumerate(story_ids): byid[pid]["sti"] = i

out = {
    "built": datetime.date.today().isoformat(), "season": {"start": D0.isoformat(), "end": (D0 + datetime.timedelta(days=83)).isoformat(), "weeks": 12},
    "chapters": [{"key": c["key"], "num": c["num"], "name": c["name"], "start": c["start"].isoformat(), "end": c["end"].isoformat(), "line": c["line"],
                  "about": c["about"], "pal": c["pal"], "tags": c["tags"]} for c in CH],
    "events": EVENTS, "pinned": PIN, "tiles": tiles, "stories": stories, "highlights": highlights,
    "roles": dict(roles), "counts": {"library": len(T), "usable": len(usable), "plan_images": len(plan_ids), "covers_and_slides": len(cover_ids),
                                      "story_frames": len(story_ids), "reel_frames": sum(len(t.get("frames", [])) for t in tiles), "products": len(PROD),
                                      "named_products_used": len(set(byid[t["cover"]]["prod"] for t in tiles + PIN if byid[t["cover"]]["prod"]))},
    "library": [{"id": x["id"], "ti": x["ti"], "si": x.get("si"), "mi": x.get("mi"), "sti": x.get("sti"), "k": x["kind"], "c": x["cat"], "p": x["pal"], "a": x["ar"],
                 "d": x["day"], "n": x["prod"], "r": x["role"], "x": x["excl"], "s": x["series"][:60], "raw": x["raw"]} for x in lib_order],
    "changelog": []
}
json.dump(out, open(D / "plan.json", "w"))
print("tiles", len(tiles), "+ pinned", len(PIN), "| stories", len(stories), "days,", sum(len(s["frames"]) for s in stories), "frames | plan images", len(plan_ids))
print("roles", dict(roles))
print("named products on covers:", out["counts"]["named_products_used"])
for ci, c in enumerate(CH):
    row = [t for t in tiles if t["chapter"] == ci]
    print(c["num"], c["name"], "| pal of covers:", collections.Counter(byid[t["cover"]]["pal"] for t in row).most_common(4),
          "| kinds:", collections.Counter(byid[t["cover"]]["kind"] for t in row).most_common(5))
