# Exports every image a product needs (gallery + variant heroes) to exports/<handle>-NN.jpg at 1288x1600, plus 400px thumbs,
# applying export.py's per-key fixes. Writes export_map.json {key: filename} and lists keys not yet approved.
import json, os, importlib.util
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ex", f"{H}/export.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
RING_HEROES = ["P01_H", "P01_S", "P08_H", "P11_H", "P12_H", "P12_S", "P13_H", "P13_S", "P15_H", "P15_S", "P22S_H", "N19_A"]
for k in RING_HEROES: E.CROP.setdefault(k, 0.7); E.CENTRE.setdefault(k, (0.5, 0.42))
D = json.load(open(f"{H}/products.json")); A = json.load(open(f"{H}/approved.json"))
os.makedirs(f"{H}/exports", exist_ok=True); os.makedirs(f"{H}/thumbs", exist_ok=True)
emap, missing = {}, []
def keys_for(p):
    ks = list(p["gallery"])
    for v in p["variants"]:
        if v["image"] and v["image"] not in ks: ks.append(v["image"])
    return ks
items = [(p["handle"], keys_for(p)) for p in D["products"]] + [(l["handle"], [l["image"]]) for l in D["live"] if l["image"]]
for handle, ks in items:
    n = 0
    for k in ks:
        if k not in A or not os.path.exists(f"{H}/out/{k}.png"): missing.append(k); continue
        n += 1; fn = f"{handle}-{n:02d}.jpg"
        if k in emap: continue
        E.export(k, f"{H}/out/{k}.png", f"{H}/exports/{fn}")
        t = Image.open(f"{H}/exports/{fn}"); t.thumbnail((400, 497)); t.save(f"{H}/thumbs/{fn}", quality=82, optimize=True)
        emap[k] = fn
json.dump(emap, open(f"{H}/export_map.json", "w"), indent=1)
print(len(emap), "exported; missing:", len(missing), missing)
