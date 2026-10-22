# Builds the Naira Performance Ads page: the campaign plan, every ad (Feed + Story) with its upload copy, the clean image library
# and the verification board. Writes <scratchpad>/perf/artifact/{index.html, t/, f/, p/, pt/, meta.csv} for the Artifact publish.
# Usage: board.py
import base64, csv, io, json, os, shutil
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); PERF = os.path.dirname(HERE)
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"; OUT = f"{SPB}/perf/artifact"
import ad_copy as C   # names, prices, stock and the campaign plan

def save(src, dst, w, q):
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src): return
    im = Image.open(src).convert("RGB"); h = round(im.height * w / im.width)
    im.resize((w, h), Image.LANCZOS).save(dst, quality=q, optimize=True, progressive=True)

def thumb(src, w, q=70):
    """a small JPEG as a data URI, so the page carries its own thumbnails (a version holds at most 511 files)"""
    im = Image.open(src).convert("RGB"); b = io.BytesIO()
    im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(b, "JPEG", quality=q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def main():
    for d in ("t", "pt"): shutil.rmtree(f"{OUT}/{d}", ignore_errors=True)
    for d in ("f", "p", "w"): os.makedirs(f"{OUT}/{d}", exist_ok=True)
    for n in ("almost_edible", "E2_ruby_anaar_916", "H08_gold_note", "apricot_quiet", "sweet_on_you_feed", "rangoli_P02"):
        save(f"{SPB}/perf/winners/{n}.jpg", f"{OUT}/w/{n}.jpg", 480, 80)
    frames = {f.get("id") or f["plate"].split("/")[-1][:-4]: f for f in json.load(open(f"{HERE}/copy.json"))["frames"]}
    rows = list(csv.DictReader(open(f"{HERE}/meta.csv")))
    plan = {o["stem"]: o for o in json.load(open(f"{HERE}/plan.json"))}
    review = {}
    for n in ("a", "b"):
        p = f"{HERE}/review_{n}.json"
        if os.path.exists(p):
            for r in json.load(open(p)): review[r["ad"]] = r
    shots, crazy = {}, []
    for g in ("g1", "g2", "g3", "g4"):
        for s in json.load(open(f"{HERE}/shots_{g}.json")): shots[f"{s['key']}-{s['format']}"] = s
        p = f"{HERE}/shots_crazy_{g}.json"
        if os.path.exists(p): crazy += json.load(open(p))
    ads = []
    for stem, o in plan.items():
        r = next(x for x in rows if x["ad"] == f"{stem}-feed"); fr = frames[stem]
        for t in ("feed", "story"):
            save(f"{PERF}/ads/{stem}-{t}.jpg", f"{OUT}/f/{stem}-{t}.jpg", 1080, 88)

        sc = [review[f"{stem}-{t}"]["score"] for t in ("feed", "story") if f"{stem}-{t}" in review]
        ads.append(dict(stem=stem, key=o["key"], fmt=o["format"], camp=o["campaign"], adset=o["adset"], wave=o["wave"], reserve=o["reserve"],
                        h=fr.get("h") or fr.get("name"), pt=r["primary_text"], hl=r["headline"], url=r["url"], variant=r["variant"],
                        score=min(sc) if sc else None, tf=thumb(f"{PERF}/ads/{stem}-feed.jpg", 300), ts=thumb(f"{PERF}/ads/{stem}-story.jpg", 200)))
    plates = []
    for k, s in shots.items():
        f = f"{PERF}/plates/{k}.jpg"
        if not os.path.exists(f): plates.append(dict(id=k, key=s["key"], fmt=s["format"], score=s.get("score"), empty=True, notes=s.get("notes", ""))); continue
        save(f, f"{OUT}/p/{k}.jpg", 1080, 86)
        plates.append(dict(id=k, key=s["key"], fmt=s["format"], score=s.get("score"), prop=s.get("prop", ""), notes=s.get("notes", ""),
                           flagged=bool(s.get("flagged")) or (s.get("score") or 10) < 8, attempts=s.get("attempts"), t=thumb(f, 240)))
    for s in crazy:
        f = f"{PERF}/plates/crazy/{s['id']}.jpg"
        if not os.path.exists(f): plates.append(dict(id=s["id"], key=s["key"], fmt="crazy", cid=s["id"], score=s.get("score"), empty=True, notes=s.get("notes", ""))); continue
        save(f, f"{OUT}/p/{s['id']}.jpg", 1080, 86)
        plates.append(dict(id=s["id"], key=s["key"], fmt="crazy", cid=s["id"], score=s.get("score"), prop=s.get("concept", s.get("prop", "")),
                           notes=s.get("notes", ""), flagged=(s.get("score") or 10) < 8, t=thumb(f, 240)))
    products = [dict(key=k, name=v[0], price=v[1], stock=C.STOCK[k], cat="Earrings" if k in C.EARRINGS else "Necklaces & rings" if k in C.NECK_RINGS else "Bracelets")
                for k, v in C.P.items()]
    shutil.copy(f"{HERE}/meta.csv", f"{OUT}/meta.csv")
    data = dict(products=products, ads=ads, plates=plates)
    html = open(f"{HERE}/board_template.html").read().replace("/*DATA*/null", json.dumps(data, ensure_ascii=False))
    open(f"{OUT}/index.html", "w").write(html)
    print(len(ads), "ad pairs,", sum(1 for p in plates if not p.get("empty")), "plates,", sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs) // 1_000_000, "MB")

if __name__ == "__main__":
    main()
