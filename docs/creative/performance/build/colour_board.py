# Builds the Colour-Coded 50 review page (round two): the new 20 first, then the first 50 kept, then the ones I retired, each
# Feed + Story pair with its line, ingredient, rhyme, shoot notes and my review flag, a Keep / Reshoot / Drop verdict and note per ad
# (kept in the page's db, collection "verdicts", doc id = shot number), and the upload text from colour_meta.csv.
# Writes <scratchpad>/perf/colour_artifact/{index.html, f/, s/, t/} for the Artifact publish.
# Usage: colour_board.py   (run colour_meta.py first)
import base64, csv, io, json, os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); PERF = os.path.dirname(HERE)
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"; OUT = f"{SPB}/perf/colour_artifact"
BRAND = os.path.normpath(f"{PERF}/../finished-ads/brand")

def save(src, dst, w, q):
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src): return
    im = Image.open(src).convert("RGB"); h = round(im.height * w / im.width)
    im.resize((w, h), Image.LANCZOS).save(dst, quality=q, optimize=True, progressive=True)

def logo_mask():
    """the wordmark as an alpha mask, so the page paints it in its own text colour in either theme"""
    im = Image.open(f"{BRAND}/logo_ink.png").convert("RGBA"); a = im.getchannel("A")
    m = Image.new("RGBA", im.size, (0, 0, 0, 0)); m.putalpha(a); m.thumbnail((480, 480))
    b = io.BytesIO(); m.save(b, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()

def main():
    for d in ("f", "s", "t"): os.makedirs(f"{OUT}/{d}", exist_ok=True)
    import colour_meta as M
    L = json.load(open(f"{HERE}/colour50.json"))
    rows = {r["ad"]: r for r in csv.DictReader(open(f"{HERE}/colour_meta.csv"))}
    ads = []
    for e in L:
        n = e["n"]; base = os.path.basename(e["plate"])[:-4]; r = rows[f"{base}-feed"]
        feed, story = f"{PERF}/ads/colour/{base}-feed.jpg", f"{PERF}/ads/colour/{base}-story.jpg"
        save(feed, f"{OUT}/f/{n}.jpg", 1080, 84); save(story, f"{OUT}/s/{n}.jpg", 810, 84)
        save(feed, f"{OUT}/t/{n}-f.jpg", 480, 78); save(story, f"{OUT}/t/{n}-s.jpg", 270, 78)
        _, _, stock, cat = M.SHOP[n]
        kind, reason = M.REVIEW.get(n, (None, None))
        group = "new" if int(n) > 50 else "retired" if kind == "retire" else "kept"
        ads.append(dict(n=n, group=group, flag=dict(kind=kind, reason=reason) if kind else None, title=e["title"], variant=e.get("variant") or "", price=e["price"], stock=stock, cat=cat, ink=e.get("page_ink", e["ink"]),   # page_ink: a dark stand-in where the ad's own ink is cream
                        score=e["score"], line=e["line"], ingredient=e["ingredient"][0].upper() + e["ingredient"][1:],
                        short=e["ingredient"].split(",")[0], rhyme=(e["rhyme"][0].upper() + e["rhyme"][1:]).replace(" = ", " → "),
                        notes=e["notes"], tries=len(e["jobs"]), pt=r["primary_text"], hl=r["headline"], url=r["url"]))
    ads.sort(key=lambda a: (["new", "kept", "retired"].index(a["group"]), a["n"]))
    ret = ' class="ret"'
    inks = "".join(f'<a href="#a{a["n"]}"{ret if a["group"] == "retired" else ""} style="--ink:{a["ink"]}" '
                   f'aria-label="{a["n"]} {a["title"]}" title="{a["n"]} · {a["title"]}"></a>' for a in ads)
    new = [a for a in ads if a["group"] == "new"]
    html = open(f"{HERE}/colour_board.html").read()
    html = html.replace("/*DATA*/null", json.dumps(ads, ensure_ascii=False)).replace("/*LOGO*/", logo_mask()).replace("{{INKS}}", inks)
    html = html.replace("{{AVG}}", f"{sum(a['score'] for a in new) / len(new):.2f}").replace("{{FRAMES}}", str(sum(a["tries"] for a in new)))
    html = html.replace("{{N}}", str(len(ads))).replace("{{NEW}}", str(len(new)))
    html = html.replace("{{KEPT}}", str(sum(a["group"] == "kept" for a in ads))).replace("{{RET}}", str(sum(a["group"] == "retired" for a in ads)))
    open(f"{OUT}/index.html", "w").write(html)
    size = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs)
    print(len(ads), "ads,", sum(len(fs) for _, _, fs in os.walk(OUT)), "files,", round(size / 1e6, 1), "MB")

if __name__ == "__main__":
    import sys; sys.path.insert(0, HERE)
    main()
