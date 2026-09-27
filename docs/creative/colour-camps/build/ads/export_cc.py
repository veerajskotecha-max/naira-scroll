# -*- coding: utf-8 -*-
"""Export the colour-camps delivery: hero ads (feed + story), carousels, standee previews and print PDFs,
to the repo (docs/creative/colour-camps) and to the artifact folder, plus manifest.json for the delivery page."""
import sys, os, json, shutil, glob
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
sys.path.insert(0, f"{SP}/sets2")
from PIL import Image
import heroes_all, car_all
from core import ROWS
from campcopy import COPY, ORDER

ART = f"{SP}/art_cc"; REPO = "/home/user/naira-scroll/docs/creative/colour-camps"
HOUT = f"{SP}/sets/cc-heroes/out"; COUT = f"{SP}/sets/cc-carousels/out"; SOUT = f"{SP}/standee/out"
CAMPN = {"peach": "APRICOT", "sage": "SAGE", "lilac": "LILAC"}
STANDEES = [("A-apricot", "APRICOT — The Fruit Stall"), ("B-sage", "SAGE — The Colour Card"), ("C-lilac", "LILAC — The Stamp Sheet")]
SIZES = [("2x5ft", "61 × 152.4 cm", "2 × 5 ft"), ("2.5x6ft", "76.2 × 182.6 cm", "2.5 × 6 ft"),
         ("3x6ft", "91.4 × 182.6 cm", "3 × 6 ft"), ("4x6ft", "122 × 182.6 cm", "4 × 6 ft")]


def fresh(d):
    if os.path.isdir(d): shutil.rmtree(d)
    os.makedirs(d, exist_ok=True)


def jpg(src, dst, q=92, thumb=None):
    im = Image.open(src).convert("RGB")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im.save(dst, quality=q, optimize=True, progressive=True, subsampling=0)
    if thumb:
        t = im.copy(); t.thumbnail((thumb[1], thumb[1]) if False else (thumb[1] * 10, thumb[1]), Image.LANCZOS)
        os.makedirs(os.path.dirname(thumb[0]), exist_ok=True); t.save(thumb[0], quality=82, optimize=True, progressive=True)
    return os.path.getsize(dst)


def main(with_pdf=True):
    for d in (f"{REPO}/ads", f"{REPO}/carousels", f"{REPO}/standees", f"{ART}/ads", f"{ART}/th", f"{ART}/standees"):
        fresh(d)
    if with_pdf: fresh(f"{ART}/print")
    man = {"camps": [], "standees": []}
    cars = {}
    for c in car_all.CREATIVES: cars.setdefault(c["sku"], []).append(c)
    for camp in ("peach", "sage", "lilac"):
        cm = {"key": camp, "name": CAMPN[camp], "products": []}
        for c in [c for c in heroes_all.CREATIVES if c["camp"] == camp]:
            sku = c["sku"]; r = ROWS[sku]; base = f"{CAMPN[camp]}-{c['id']}-{c['file']}"
            p = {"sku": sku, "id": c["id"], "title": r["title"], "price": int(round(r["price"])), "stock": r["inv"],
                 "url": f"https://nairaflore.com/products/{r['handle']}", "spec": COPY[sku]["spec"], "sub": COPY[sku]["sub"], "cta": COPY[sku]["cta"],
                 "ads": {}, "carousel": []}
            for fmt, dim in (("feed", "1080x1350"), ("story", "1080x1920")):
                fn = f"{base}-{fmt}-{dim}.jpg"
                jpg(f"{HOUT}/{c['id']}_{fmt}.png", f"{REPO}/ads/{CAMPN[camp]}/{fn}")
                shutil.copy(f"{REPO}/ads/{CAMPN[camp]}/{fn}", f"{ART}/ads/{fn}")
                jpg(f"{HOUT}/{c['id']}_{fmt}.png", f"{ART}/ads/{fn}", thumb=(f"{ART}/th/{fn}", 720))
                p["ads"][fmt] = {"file": f"ads/{fn}", "thumb": f"th/{fn}"}
            # carousel: card 1 is the feed hero, then the verified detail cards
            p["carousel"].append(p["ads"]["feed"])
            for k, cc in enumerate(cars.get(sku, []), 2):
                fn = f"{base}-carousel-{k}-1080x1350.jpg"
                jpg(f"{COUT}/{cc['id']}_feed.png", f"{REPO}/carousels/{CAMPN[camp]}/{fn}")
                jpg(f"{COUT}/{cc['id']}_feed.png", f"{ART}/ads/{fn}", thumb=(f"{ART}/th/{fn}", 540))
                p["carousel"].append({"file": f"ads/{fn}", "thumb": f"th/{fn}"})
            cm["products"].append(p)
        man["camps"].append(cm)
    for key, name in STANDEES:
        st = {"key": key, "name": name, "sizes": []}
        for tag, cmsz, ft in SIZES:
            png = f"{SOUT}/{key}-{tag}.png"
            if not os.path.exists(png): continue
            im = Image.open(png).convert("RGB")
            prev = im.copy(); prev.thumbnail((4000, 2400), Image.LANCZOS)
            os.makedirs(f"{REPO}/standees/preview", exist_ok=True)
            prev.save(f"{REPO}/standees/preview/{key}-{tag}.jpg", quality=86, optimize=True, progressive=True)
            prev.save(f"{ART}/standees/{key}-{tag}.jpg", quality=86, optimize=True, progressive=True)
            th = im.copy(); th.thumbnail((4000, 900), Image.LANCZOS); th.save(f"{ART}/th/{key}-{tag}.jpg", quality=82, optimize=True)
            e = {"tag": tag, "cm": cmsz, "ft": ft, "preview": f"standees/{key}-{tag}.jpg", "thumb": f"th/{key}-{tag}.jpg", "px": list(im.size)}
            pdf = f"{SOUT}/{key}-{tag}.pdf"
            if with_pdf and os.path.exists(pdf):
                shutil.copy(pdf, f"{ART}/print/{key}-{tag}.pdf")
                e["pdf"] = f"print/{key}-{tag}.pdf"; e["pdf_mb"] = round(os.path.getsize(pdf) / 1e6, 1)
            st["sizes"].append(e)
        man["standees"].append(st)
    json.dump(man, open(f"{ART}/manifest.json", "w"), indent=1, ensure_ascii=False)
    n_ads = sum(len(p["ads"]) for c in man["camps"] for p in c["products"])
    n_car = sum(len(p["carousel"]) - 1 for c in man["camps"] for p in c["products"])
    print("hero files", n_ads, "carousel cards", n_car, "standees", sum(len(s["sizes"]) for s in man["standees"]))


if __name__ == "__main__":
    main(with_pdf="--nopdf" not in sys.argv)
