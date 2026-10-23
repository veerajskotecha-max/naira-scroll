# The approved-ads handoff (23 Oct 2026): one page and one manifest that Claude Code reads to make the colour-coded Meta ads.
#   approved  23 ads kept on the round-two review page: ready
#   review    43 ads redone in round three with sensible props (REDO43.md): the founder marks Keep or Drop on the handoff page
#   unmarked  4 ads never marked (24, 41, 45, 61): held back until marked
# The page's db (collection "verdicts", doc id = ad number, {verdict: keep | drop, note, at}) is the live truth; it is seeded with
# the 23 keeps after the first publish. Writes <scratchpad>/perf/handoff/ (index.html, manifest.json, ads.csv, approved.csv,
# ads/ full-size files, t/ thumbnails) for the Artifact publish, and copies the manifest and the two sheets to ../handoff/.
# Usage: handoff.py [artifact-url]   (run colour_meta.py first; pass the URL once it exists so the page and manifest carry it)
import base64, csv, io, json, os, shutil, sys
from collections import defaultdict
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); PERF = os.path.dirname(HERE); sys.path.insert(0, HERE)
import colour_meta as M
from colour_board import save, logo_mask
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"; OUT = f"{SPB}/perf/handoff"
REPO = "veerajskotecha-max/naira-scroll"; BRANCH = "claude/higgfield-12-angles-4j09gn"; REL = "docs/creative/performance"
URL = sys.argv[1] if len(sys.argv) > 1 else ""

HOW = [
    "Read the founder's verdicts in this artifact's database: collection \"verdicts\", one document per ad, its id the ad number "
    "(\"02\"), its field \"verdict\" either \"keep\" or \"drop\". Make an ad only when its verdict is \"keep\". If the verdicts "
    "cannot be read, use only ads whose status here is \"approved\".",
    "Each ad is two images of one photograph. The Feed file (1080x1350, 4:5) already carries the NAIRA wordmark, the line and the "
    "name and price; use it for Facebook and Instagram Feed and Explore. The Story file (1080x1920, 9:16) is the photograph alone; "
    "use it for Stories and Reels. Never crop, retouch or add text to either file.",
    "Give both images the ad's primary_text, headline, cta and url exactly as written here. The url opens the ad's own colour "
    "and carries its UTM tags.",
    "Campaign: \"" + M.CAMPAIGN + "\", one ad set per ad_set value (Bracelets, Earrings, Necklaces & rings), the rows of ads.csv.",
    "Create every campaign, ad set and ad paused, for the founder to review and switch on. Do not change any live campaign or ad.",
    "Stock is as read from Shopify on 23 Oct 2026. Check stock again before spending on any ad with 10 units or fewer.",
]
WORDS = {"say": ["gold tone", "silver tone", "18k gold tone", "rhodium silver tone", "cubic zirconia",
                 "white pearl or white shell pearl, as the listing says"],
         "never_say": ["real", "diamond", "waterproof", "tarnish-free", "freshwater"],
         "offer": M.OFFER}

def ink(e): return e.get("page_ink", e["ink"])   # a dark stand-in for the page where the ad's own ink is cream

def main():
    for d in ("ads", "t"): os.makedirs(f"{OUT}/{d}", exist_ok=True)
    L = json.load(open(f"{HERE}/colour50.json"))
    dropped = {e["n"]: e for e in json.load(open(f"{HERE}/colour_dropped.json"))}
    twins = defaultdict(list)                                     # one product and colour -> its ads
    for e in L: twins[M.SHOP[e["n"]][:2]].append(e["n"])
    ads, page = [], []
    for e in L:
        n = e["n"]; a = M.ad(e); base = a["base"]
        feed, story = f"{PERF}/ads/colour/{base}-feed.jpg", f"{PERF}/ads/colour/{base}-story.jpg"
        for src in (feed, story): shutil.copy2(src, f"{OUT}/ads/{os.path.basename(src)}")
        save(feed, f"{OUT}/t/{n}-f.jpg", 480, 78); save(story, f"{OUT}/t/{n}-s.jpg", 270, 78)
        same = [x for x in twins[M.SHOP[n][:2]] if x != n]
        prop = e["ingredient"][0].upper() + e["ingredient"][1:]; why = (e["rhyme"][0].upper() + e["rhyme"][1:]).replace(" = ", " → ")
        rec = dict(n=n, status=a["status"], product=e["title"], variant=e.get("variant"), price=e["price"], handle=a["handle"],
                   variant_id=a["variant_id"], stock_23oct=a["stock"], ad_set=a["adset"], line=a["line"], prop=prop, why=why,
                   primary_text=a["primary_text"], headline=a["headline"], cta="SHOP_NOW", url=a["url"], ink=e["ink"],
                   files=dict(feed=f"ads/{base}-feed.jpg", story=f"ads/{base}-story.jpg"),
                   repo_files=dict(feed=f"{REL}/ads/colour/{base}-feed.jpg", story=f"{REL}/ads/colour/{base}-story.jpg",
                                   plate=f"{REL}/{e['plate']}"),
                   same_product_as=same, replaces=(dropped[n]["ingredient"] if n in dropped else None), notes=e["notes"])
        ads.append(rec)
        page.append(dict(n=n, status=a["status"], title=e["title"], variant=e.get("variant") or "", price=e["price"], stock=a["stock"],
                         cat=a["adset"], ink=ink(e), line=a["line"], prop=prop, why=why, notes=e["notes"], tries=len(e["jobs"]),
                         replaces=rec["replaces"], same=same, pt=a["primary_text"], hl=a["headline"], url=a["url"],
                         f=rec["files"]["feed"], s=rec["files"]["story"]))
    order = ["approved", "review", "unmarked"]
    ads.sort(key=lambda r: (order.index(r["status"]), r["n"])); page.sort(key=lambda r: (order.index(r["status"]), r["n"]))
    count = {k: sum(r["status"] == k for r in ads) for k in order}
    manifest = dict(
        name="Naira approved ads · colour-coded set", as_of="2026-10-23", artifact=URL or None, shop="https://www.nairaflore.com",
        how_to_use=HOW, verdicts=dict(collection="verdicts", doc_id="the ad number, for example \"02\"", field="verdict",
                                      keep="make this ad", drop="do not make this ad"),
        formats=dict(feed=dict(size="1080x1350", ratio="4:5", placements="Facebook and Instagram Feed, Explore",
                               text="wordmark, line and name and price are in the image"),
                     story=dict(size="1080x1920", ratio="9:16", placements="Stories and Reels",
                                text="none; the words are in the primary text")),
        words=WORDS, campaign=M.CAMPAIGN, cta="SHOP_NOW", counts=dict(count, total=len(ads)),
        statuses=dict(approved="kept by the founder in round two: ready",
                      review="redone in round three with a sensible prop: make it only once its verdict is keep",
                      unmarked="never marked: make it only once its verdict is keep"),
        repo=dict(repo=REPO, branch=BRANCH, folder=REL), ads=ads)
    json.dump(manifest, open(f"{OUT}/manifest.json", "w"), ensure_ascii=False, indent=1)
    rows = list(M.rows(L)); key = {r["n"]: r["status"] for r in ads}
    cols = M.COLS + ["status", "image"]
    for name, keep in (("ads.csv", lambda s: True), ("approved.csv", lambda s: s == "approved")):
        with open(f"{OUT}/{name}", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
            for r in rows:
                n = r["ad"][:2]
                if keep(key[n]): w.writerow(dict(r, status=key[n], image=f"ads/{r['ad']}.jpg"))
    os.makedirs(f"{PERF}/handoff", exist_ok=True)
    for name in ("manifest.json", "ads.csv", "approved.csv"): shutil.copy2(f"{OUT}/{name}", f"{PERF}/handoff/{name}")
    html = open(f"{HERE}/handoff.html").read()
    html = html.replace("/*DATA*/null", json.dumps(page, ensure_ascii=False)).replace("/*LOGO*/", logo_mask())
    html = html.replace("/*URL*/\"\"", json.dumps(URL)).replace("/*HOW*/null", json.dumps(HOW, ensure_ascii=False))
    for k, v in dict(APPROVED=count["approved"], REVIEW=count["review"], UNMARKED=count["unmarked"], TOTAL=len(ads),
                     FILES=2 * len(ads), CAMPAIGN=M.CAMPAIGN).items():
        html = html.replace("{{" + k + "}}", str(v))
    open(f"{OUT}/index.html", "w").write(html)
    files = sorted(os.path.relpath(os.path.join(dp, f), OUT) for dp, _, fs in os.walk(OUT) for f in fs if f != "index.html")
    json.dump(files, open(f"{SPB}/perf/handoff_files.json", "w"))
    size = sum(os.path.getsize(f"{OUT}/{f}") for f in files)
    print(count, len(files), "files,", round(size / 1e6, 1), "MB")

if __name__ == "__main__":
    main()
