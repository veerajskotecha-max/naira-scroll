# Size-guide cards (1600x1600, the live <handle>-size-guide.jpg format) drawn with the house drawer
# ../../aditya-jewellery/build/sizeguide.py: a photo card (the approved packshot in a panel with measurement bars;
# callouts in raw frame pixels, photocards.json) for the pendant and the studs, and the ring card for the adjustable ring.
# Sizes are measured against the 80 mm velvet card in the supplier photos (the ring against the finger it is worn on).
# Usage: python3 -I sizecards.py [K ...] -> ../cards/<handle>-size-guide.jpg
import importlib.util, json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../cards"); os.makedirs(OUT, exist_ok=True)
s = importlib.util.spec_from_file_location("sg", os.path.join(H, "../../aditya-jewellery/build/sizeguide.py"))
SG = importlib.util.module_from_spec(s); s.loader.exec_module(SG)
L = {p["key"]: p for p in json.load(open(f"{H}/../shopify/listing.json"))}
PC = json.load(open(f"{H}/photocards.json")) if os.path.exists(f"{H}/photocards.json") else {}
C = json.load(open(f"{H}/chosen.json")) if os.path.exists(f"{H}/chosen.json") else {}
APPROX = "Measurements are approximate, give or take 1 mm."
def draw(k):
    p = L[k]; g = p["sizeguide"]
    if g["kind"] == "ring":
        im = SG.ring(p["title"], g)
    else:
        spec = dict(PC[k]); spec["path"] = f"{H}/out/{C.get(k + '_H', k + '_H')}.png"; spec["line"] = g["line"]; spec.setdefault("note", APPROX)
        im = SG.photo(p["title"], spec)
    dst = f"{OUT}/{p['handle']}-size-guide.jpg"; im.convert("RGB").save(dst, quality=92); return dst
if __name__ == "__main__":
    for k in sys.argv[1:] or [k for k in L if L[k]["sizeguide"]["kind"] == "ring" or k in PC]:
        print(k, os.path.basename(draw(k)))
