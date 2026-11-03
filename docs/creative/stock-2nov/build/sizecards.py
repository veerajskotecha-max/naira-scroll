# Size-guide cards for the pieces in stock on 2 Nov 2026, in the house formats (../../size-cards/build/cards.py), as
# ../../albyluxe-31oct/build/sizecards.py: necklaces get the neck-outline card with the house reference lengths; the huggies and the
# set get a photo card (an approved frame in a panel with measurement bars, callouts in raw pixels of out/<src>.png, photocards.json).
# Sizes are measured against the hand and the cards in the owner's photos, so each card says it is approximate.
# Usage: python3 -I sizecards.py [id ...] -> ../cards/<handle>-size-guide.jpg
import importlib.util, json, os, re, sys, unicodedata
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../cards"); os.makedirs(OUT, exist_ok=True)
s = importlib.util.spec_from_file_location("cards", os.path.join(H, "../../size-cards/build/cards.py"))
C = importlib.util.module_from_spec(s); s.loader.exec_module(C)
L = {x["id"]: x for x in json.load(open(os.path.join(H, "listings.json")))}
APPROX = "Measurements are approximate, give or take 1 mm."

def handle(title):
    t = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

SPEC = {
    "N01": ("necklace", ([42], "42 cm · marquise 5 × 10 mm")),
    "N02": ("necklace", ([42], "42 cm · pendant 25 mm across")),
    "N03": ("necklace", ([45], "Adjustable · pearl 10 mm")),
    "N04": ("necklace", ([45], "45 cm · pendant 12 mm")),
    "N05": ("necklace", ([45], "45 cm · pear 6 × 8 mm")),
    "N06": ("necklace", ([42], "42 cm · flower 6 mm · drop 5 cm")),
    "N07": ("necklace", ([42], "42 cm · Asscher 9 mm")),
    "N08": ("necklace", ([42], "42 cm · bezel 8 mm")),
    "N09": ("necklace", ([42], "42 cm · heart 7 mm")),
    "A16": ("necklace", ([45], "45 cm · teardrop 10 × 13 mm")),
}
PHOTO = {k: v for k, v in json.load(open(os.path.join(H, "photocards.json"))).items() if not k.startswith("_")} if os.path.exists(os.path.join(H, "photocards.json")) else {}

def draw(i):
    x = L[i]; t = x["title"]
    if i in PHOTO:
        p = dict(PHOTO[i]); p["path"] = os.path.join(H, "out", p.pop("src") + ".png"); p.setdefault("note", APPROX)
        im = C.SGJ.photo(t, p)
    else:
        kind, a = SPEC[i]
        if kind == "ring": im = C.SGJ.ring(t, a)
        elif kind == "bracelet": im = C.SGB.card(t, a[0], a[1], a[2])
        else: im = C.necklace(t, a[0], a[1], "Chain length is approximate.")
    dst = os.path.join(OUT, f"{handle(t)}-size-guide.jpg"); im.convert("RGB").save(dst, quality=92); return dst

if __name__ == "__main__":
    for i in sys.argv[1:] or sorted(set(SPEC) | set(PHOTO)):
        print(i, os.path.basename(draw(i)))
