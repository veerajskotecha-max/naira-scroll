# -*- coding: utf-8 -*-
"""Export Colour Camps 2.0 (both directions) to the artifact folder and the repo, and write manifest_v2.json."""
import sys, os, json, shutil
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
sys.path.insert(0, f"{SP}/sets3")
from PIL import Image
from minimal import ROWS, COPY, ORDER, F
import heroes_framed, cards_framed

ART = f"{SP}/art_v2"; REPO = "/home/user/naira-scroll/docs/creative/colour-camps-2"
CAMPN = {"peach": "APRICOT", "sage": "SAGE", "lilac": "LILAC"}
DIRS = {"framed": ("v2-framed-heroes", "v2-framed-cards"), "quiet": ("v2-quiet-heroes", "v2-quiet-cards")}


def save(src, dst, thumb=None, q=90):
    im = Image.open(src).convert("RGB")
    os.makedirs(os.path.dirname(dst), exist_ok=True); im.save(dst, quality=q, optimize=True, progressive=True, subsampling=0)
    if thumb:
        t = im.copy(); t.thumbnail((10000, thumb[1]), Image.LANCZOS)
        os.makedirs(os.path.dirname(thumb[0]), exist_ok=True); t.save(thumb[0], quality=80, optimize=True, progressive=True)


def main():
    for d in (ART, REPO):
        if os.path.isdir(d): shutil.rmtree(d)
        os.makedirs(d)
    man = {"directions": {}, "compare": []}
    cards_by = {}
    for c in cards_framed.CREATIVES: cards_by.setdefault(c["sku"], []).append(c)
    for dname, (hs, cs) in DIRS.items():
        camps = []
        for camp in ("peach", "sage", "lilac"):
            prods = []
            for c in [c for c in heroes_framed.CREATIVES if c["camp"] == camp]:
                sku = c["sku"]; r = ROWS[sku]; base = f"{CAMPN[camp]}-{c['id']}-{c['file']}"
                p = {"sku": sku, "id": c["id"], "title": r["title"], "price": int(round(r["price"])), "stock": r["inv"],
                     "url": f"https://nairaflore.com/products/{r['handle']}", "line": COPY[sku]["sub"].strip("()").rstrip(".").capitalize() + ".",
                     "story": {}, "feed": {}, "cards": []}
                for fmt, dim in (("feed", "1080x1350"), ("story", "1080x1920")):
                    fn = f"{dname}/{base}-{fmt}-{dim}.jpg"
                    save(f"{SP}/sets/{hs}/out/{c['id']}_{fmt}.png", f"{ART}/{fn}", thumb=(f"{ART}/th/{fn}", 720))
                    os.makedirs(os.path.dirname(f"{REPO}/{fn}"), exist_ok=True); shutil.copy(f"{ART}/{fn}", f"{REPO}/{fn}")
                    p[fmt] = {"file": fn, "thumb": f"th/{fn}"}
                p["cards"].append(p["feed"])
                for k, cc in enumerate(cards_by.get(sku, []), 2):
                    fn = f"{dname}/{base}-carousel-{k}-1080x1350.jpg"
                    save(f"{SP}/sets/{cs}/out/{cc['id']}_feed.png", f"{ART}/{fn}", thumb=(f"{ART}/th/{fn}", 540))
                    shutil.copy(f"{ART}/{fn}", f"{REPO}/{fn}")
                    p["cards"].append({"file": fn, "thumb": f"th/{fn}"})
                prods.append(p)
            camps.append({"key": camp, "name": CAMPN[camp], "products": prods})
        man["directions"][dname] = camps
    # v1 -> 2.0 comparison (feed), one product per camp
    for cid, sku in (("A1", "E20267O"), ("S2", "YF5215"), ("L1", "B00681C")):
        row = {"sku": sku, "title": ROWS[sku]["title"]}
        for k, path in (("v1", f"{SP}/sets/cc-heroes/out/{cid}_feed.png"), ("framed", f"{SP}/sets/v2-framed-heroes/out/{cid}_feed.png"),
                        ("quiet", f"{SP}/sets/v2-quiet-heroes/out/{cid}_feed.png")):
            fn = f"compare/{cid}-{k}.jpg"; im = Image.open(path).convert("RGB"); im.thumbnail((10000, 900), Image.LANCZOS)
            os.makedirs(f"{ART}/compare", exist_ok=True); im.save(f"{ART}/{fn}", quality=84, optimize=True, progressive=True)
            row[k] = fn
        man["compare"].append(row)
    json.dump(man, open(f"{ART}/manifest.json", "w"), indent=1, ensure_ascii=False)
    n = sum(1 for _ in os.walk(ART) for _ in _[2])
    print("files", n, "size MB", round(sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(ART) for f in fs) / 1e6, 1))


if __name__ == "__main__":
    main()
