# Builds the "Naira Catalogue Ads" artifact page: the three covers (1:1, 4:5, 9:16) and three cards for every in-stock
# product, by category, with single and ZIP downloads, product links and a links CSV.
# Inputs: <scratchpad>/cat/out/cards (cards.py), out/covers (covers.py), src/products_pick.json.
# Usage: page.py -> <scratchpad>/cat/site/ (index.html, v/ covers, c/ cards, s/ thumbnail strips) and site_files.json
import base64, csv, io, json, os, shutil
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/cat"
SITE = f"{SP}/site"
CATS = [("earrings", "Earrings", "Earrings"), ("rings", "Rings", "Ring"), ("bracelets", "Bracelets", "Bracelet"), ("necklaces", "Necklaces", "Necklace")]
COVERS = [("wall", "The Wall", "Every piece, on her, in one dense wall: a coral badge with the count and price range, and marker circles on the favourites."),
          ("poster", "Now Showing", "A Bollywood film poster. CHAMAK in gold-tone 3D type over the Verdant Drop shot, the cast of pieces with prices, and a billing block."),
          ("times", "The Naira Times", "A tabloid front page. SHE WORE IT ALL., the Marquise Drop Choker as the lead photo, three side stories with prices and an EXTRA! stamp.")]
FMT = [("1x1", "1:1 · 1080×1080"), ("4x5", "4:5 · 1080×1350"), ("9x16", "9:16 · 1080×1920")]
LAB = {True: ("worn", "worn-closeup", "magnifier"), False: ("product", "product-closeup", "closeup")}
TONE = {"Gold": "gold tone", "Silver": "silver tone", "Ruby": "ruby red", "Emerald": "emerald green", "Crystal": "crystal clear", "Amethyst": "amethyst"}

def jpg(src, dst, q, size=None):
    im = Image.open(src).convert("RGB")
    if size: im = im.resize(size, Image.LANCZOS)
    im.save(dst, quality=q, optimize=True, progressive=True)

def main():
    for d in ("v", "c", "s"): os.makedirs(f"{SITE}/{d}", exist_ok=True)
    meta = json.load(open(f"{SP}/out/cards/cards.json")); pick = {r["handle"]: r for r in json.load(open(f"{SP}/src/products_pick.json"))}
    covers = []
    for key, name, desc in COVERS:
        files = []
        for f, label in FMT:
            fn = f"naira-cover-{key}-{f}.jpg"; jpg(f"{SP}/out/covers/{fn}", f"{SITE}/v/{fn}", 90)
            files.append(dict(label=label, path=f"v/{fn}", name=f"Naira-Cover-{name.replace(' ', '-')}-{f}.jpg"))
        covers.append(dict(name=name, desc=desc, files=files))
    prods, rows = [], []
    order = {t: i for i, (_, _, t) in enumerate(CATS)}
    for m in sorted(meta, key=lambda m: (order[m["type"]], not m["worn"], m["title"])):
        h = m["handle"]; p = pick[h]; labs = LAB[m["worn"]]; files, names = {}, {}
        strip = Image.new("RGB", (1200, 400), "white")
        for i, k in enumerate("ABC"):
            src = f"{SP}/out/cards/{h}-{k}.jpg"; jpg(src, f"{SITE}/c/{h}-{k}.jpg", 86)
            strip.paste(Image.open(src).convert("RGB").resize((400, 400), Image.LANCZOS), (400 * i, 0))
            files[k] = f"c/{h}-{k}.jpg"; names[k] = f"Naira-{h}-{i + 1}-{labs[i]}.jpg"
            rows.append([names[k], p["title"], labs[i], p["price"], p["url"] if k != "C" or not m.get("alt") else (p.get("alt_url") or p["url"])])
        strip.save(f"{SITE}/s/{h}.jpg", quality=80, optimize=True, progressive=True)
        c = p.get("worn_colour"); pr = f"₹{p['price']:,}" + (f" · {TONE.get(c, c)}" if c else "")
        cat = next(k for k, _, t in CATS if t == m["type"])
        prods.append(dict(h=h, t=p["title"], cat=cat, worn=m["worn"], pr=pr, url=p["url"], strip=f"s/{h}.jpg", files=files, names=names))
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(["file", "product", "card", "price_inr", "link"]); w.writerows(rows)
    open(f"{SITE}/naira-catalogue-links.csv", "w", encoding="utf-8").write(buf.getvalue())
    nomodel = [p["t"] for p in prods if not p["worn"]]
    nm = (f"{len(nomodel)} pieces have no on-model photo in the store yet ({', '.join(nomodel)}). Their cards use the product shots until they are shot on a model."
          if nomodel else "")
    cats = [dict(key=k, name=n) for k, n, _ in CATS]
    chips = "\n    ".join(f'<a class="chip" href="#{k}">{n} · {sum(1 for p in prods if p["cat"] == k)}</a>' for k, n, _ in CATS)
    data = dict(covers=covers, products=prods, cats=cats, csv=buf.getvalue())
    b64 = base64.b64encode(open(f"{HERE}/../finished-ads/brand/Velista.ttf", "rb").read()).decode()
    page = (open(f"{HERE}/page_template.html", encoding="utf-8").read().replace("__VELISTA__", b64).replace("__COUNT__", str(len(prods)))
            .replace("__CHIPS__", chips).replace("__NOMODEL__", nm)
            .replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    open(f"{SITE}/index.html", "w", encoding="utf-8").write(page)
    allf = [f"v/{c['files'][i]['path'][2:]}" for c in covers for i in range(3)] + [p["strip"] for p in prods] + ["naira-catalogue-links.csv"]
    cards = [p["files"][k] for p in prods for k in "ABC"]
    json.dump(dict(first=allf + cards[:150], second=cards[150:]), open(f"{SP}/site_files.json", "w"))
    size = lambda fs: round(sum(os.path.getsize(f"{SITE}/{f}") for f in fs) / 1e6, 1)
    print(len(prods), "products;", len(allf + cards), "files;", size(allf + cards[:150]), "MB first,", size(cards[150:]), "MB second")

if __name__ == "__main__":
    main()
