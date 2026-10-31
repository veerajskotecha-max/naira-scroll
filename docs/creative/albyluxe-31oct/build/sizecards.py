# Size-guide cards for the 31 Oct Albyluxe and supplier picks, in the house formats (../../size-cards/build/cards.py):
#   ring      the house ring card: open rings show US 5 to 9; closed rings show the sizes assumed until Albyluxe confirms them;
#   bracelet  the 0-24 cm ruler card;
#   necklace  the neck-outline card with the house reference lengths;
#   photo     the approved hero in a panel with measurement bars (callouts in raw frame pixels of out/<src>.png).
# Every figure is an estimate from the supplier photos (listings.json), so each card says it is approximate.
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

OPEN = {"fit": ("5", "9"), "line": "Open band · adjusts to fit US 5 to 9"}
CLOSED = {"fit": ("6", "8"), "line": "Closed band · sizes 6 to 8, to confirm"}
SPEC = {
    "A01": ("ring", CLOSED), "A05": ("ring", CLOSED), "A06": ("ring", CLOSED),
    "A02": ("ring", OPEN), "A04": ("ring", OPEN), "B09": ("ring", OPEN),
    "A11": ("bracelet", (17, None, "Length is approximate.")),
    "B01": ("bracelet", (16, (16, 22), "Adjusts with the sliding bead. Length is approximate.")),
    "B13": ("bracelet", (17, (17, 20), "Length is approximate.")),
    "A09": ("necklace", ([40], "40 cm · seven drops of 5 mm")),
    "A10": ("necklace", ([45], "45 cm · pear 9 × 13 mm")),
    "A16": ("necklace", ([45], "45 cm · pearl 8 × 10 mm")),
    "B02": ("necklace", ([42], "42 cm · emerald-cut 6 × 4 mm")),
    "B03": ("necklace", ([45], "About 90 cm · doubled, about 45 cm")),
    "B04": ("necklace", ([45], "45 cm · heart 12 mm")),
    "B07": ("necklace", ([40], "40 cm · drops of 5 mm")),
    "B10": ("necklace", ([45], "45 cm · cushion 9 mm")),
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
