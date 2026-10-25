"""library.json + products.json -> tagged.json: format, kind, product match, palette words, shoot day, series key."""
import json, re, sys, collections, datetime
from pathlib import Path
D = Path(sys.argv[1])
L = json.load(open(D / "library.json")); P = json.load(open(D / "products.json"))["products"]
titles = sorted(((p["title"], p) for p in P), key=lambda t: -len(t[0]))
def norm(s): return re.sub(r"[^a-z0-9 ]", " ", s.lower())
tnorm = [(norm(t), t, p) for t, p in titles]
EDITED = r"\b(edit image|edit this|keep everything|change one thing|retouch|remove the artificial|remove the (star|sparkle))"
KIND = [("texture", r"(filling the entire frame|fills the frame edge to edge|seamless background texture)"),
        ("on-model", r"\b(on-?model|worn (photograph|frame|on|e-?commerce)|the model|a woman|the woman|her (ear|neck|wrist|hand|finger|collarbone|lobe|skin)|portrait|forearm|décolletage|decolletage|hand raised|hand resting|wearing it|beauty portrait|the same woman)\b"),
        ("macro", r"\b(macro|extreme close|close-?up of (the|one) )"),
        ("packshot", r"\b(packshot|e-?commerce|catalog(ue)? shot|plinth)\b"),
        ("witty", r"\b(witty|pun|visual joke|playful)\b"),
        ("flat lay", r"\b(flat ?lay|top-?down|overhead|from directly above)\b"),
        ("still life", r"\b(still life|still-life)\b")]
PAL = ["apricot", "lilac", "lavender", "sage", "celadon", "cream", "ivory", "blush", "peach", "coral", "red", "crimson", "emerald", "green",
       "pearl", "gold", "silver", "rhodium", "black", "white", "terracotta", "honey", "butter", "rose", "pink", "blue", "navy", "cobalt", "mint",
       "chocolate", "espresso", "caramel", "linen", "silk", "velvet", "marble", "plaster", "stone", "water", "fruit", "flower", "petal"]
CAT = [("earring", r"\b(earring|stud|hoop|huggie|ear ?cuff|drop|dangl)"), ("ring", r"\bring\b"), ("necklace", r"\b(necklace|pendant|chain|choker|lariat|collar)\b"),
       ("bracelet", r"\b(bracelet|cuff|bangle|tennis)\b"), ("set", r"\b(set|matching)\b")]
def shot_text(p):
    """The paragraph that describes the frame itself (after 'SHOT' when present), not the reference notes."""
    m = re.search(r"\bSHOT\b[:\s—–-]*", p)
    if m:
        rest = p[m.end():]; e = re.search(r"\n\s*\n|THE PRODUCT|STRICT PRODUCT|NEGATIVES|THE SETTING", rest)
        return rest[:e.start()] if e and e.start() > 40 else rest[:600]
    for q in re.split(r"\n\s*\n", p):
        if q.strip() and not re.match(r"\s*(IMAGE \d|REFERENCE|Reference|ref image|Ref )", q): return q[:700]
    return p[:500]
NEGATED = re.compile(r"\b(no|without|not|never|ignore|ignoring|remove|minus|instead of)\s+(a\s+|an\s+|any\s+|the\s+|her\s+|its\s+)?(hands?|model|models|skin|people|person|faces?|fingers?|body|woman|human|wrist|ear|neck|wearer|mannequin)\b|\bnot worn\b|\bunworn\b|\bno one\b", re.I)
STRONG = re.compile(r"\b(ear|ears|earlobe|lobe|collarbone|throat|neckline|wrist|forearm|knuckle|finger|fingers|hand|hands|on-?body|on-?model|worn on|worn at|the model|her neck|her hand|décolletage|decolletage|portrait|woman|she|her|skin|jawline|jaw|cheek|lips|hair|shoulder|nape|bust|wearing|wears|wearer)\b", re.I)
PLATE = re.compile(r"poster background|background (plate|only|for)|reserved for|will be placed|remove the (necklace|earrings?|rings?|bracelet|jewell?ery|piece)|no jewellery|empty (plinth|cube|scene|set)|without (the|any) (jewellery|piece|product)|greeting card|family portrait", re.I)
JEWEL = re.compile(r"earring|\bring\b|rings\b|necklace|bracelet|\bchain|pendant|\bstud|\bhoop|\bcuff|bangle|charm|lariat|choker|anklet|brooch|jewel|huggie|solitaire|tennis|\bband\b|the piece|one piece", re.I)
out = []
for x in L:
    p = x["prompt"] or ""; pl = norm(p); head = shot_text(p); clean = NEGATED.sub(" ", head)
    prod = None
    for tn, t, pp in tnorm:
        if tn and tn in pl: prod = t; break
    if not p: kind = "unknown"
    elif re.search(KIND[0][1], p, re.I): kind = "texture"
    elif STRONG.search(clean): kind = "on-model"
    elif re.search(r"\bmacro\b|extreme close|close-?up of|razor-sharp on the stones", clean, re.I): kind = "macro"
    elif re.search(r"packshot|e-?commerce|plinth|cube|catalog(ue)? (shot|photograph)|straight-on", clean, re.I): kind = "packshot"
    else: kind = next((k for k, rx in KIND[1:] if k in ("witty", "flat lay") and re.search(rx, p, re.I)), "still life")
    plate = bool(PLATE.search(p)) or (bool(p) and not JEWEL.search(p))
    edited = bool(re.search(EDITED, p, re.I))
    cat = next((c for c, rx in CAT if re.search(rx, p, re.I)), None)
    pal = [w for w in PAL if re.search(r"\b" + w + r"\b", pl)]
    day = datetime.datetime.utcfromtimestamp(x["t"]).strftime("%Y-%m-%d")
    series = re.sub(r"\s+", " ", p[:70]).strip()
    out.append({**x, "prod": prod, "kind": kind, "cat": cat, "pal": pal[:6], "day": day, "series": series, "edited": edited, "plate": plate})
json.dump(out, open(D / "tagged.json", "w"))
c = collections.Counter
print(len(out), "images |", "fmt", dict(c(x["ar"] for x in out)))
print("kind", dict(c(x["kind"] for x in out)))
print("cat", dict(c(x["cat"] for x in out)))
print("product matched", sum(1 for x in out if x["prod"]), "| distinct products", len(set(x["prod"] for x in out if x["prod"])))
print("top products", c(x["prod"] for x in out if x["prod"]).most_common(25))
print("days", len(set(x["day"] for x in out)), "| busiest", c(x["day"] for x in out).most_common(12))
print("palette", c(w for x in out for w in x["pal"]).most_common(25))
