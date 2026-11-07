# Size-guide cards for the 7 Nov Albyluxe pieces, in the house formats (../../size-cards/build/cards.py), as ../../albyluxe-31oct/build/sizecards.py:
#   ring      the house ring card: open rings show US 5 to 9; closed rings show the sizes assumed until Albyluxe confirms them;
#   necklace  the neck-outline card with the house reference lengths;
#   photo     an approved frame in a panel with measurement bars (photocards.json: callouts in raw frame pixels of out/<src>.png),
#             for the earrings and the cuff.
# Every figure is an estimate from the supplier photos and sheets (listings.json), so each card says it is approximate.
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
    "L01": ("ring", OPEN), "L02": ("ring", OPEN), "L03": ("ring", OPEN), "L06": ("ring", OPEN), "L13": ("ring", OPEN), "L16": ("ring", OPEN),
    "L10": ("ring", CLOSED), "L14": ("ring", CLOSED), "L17": ("ring", CLOSED), "L18": ("ring", CLOSED),
    "L07": ("necklace", ([42], "About 42 cm · eleven hearts of 7 mm")),
    "L08": ("necklace", ([44, 49], "44 cm + 5 cm extender · heart 12 mm")),
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
