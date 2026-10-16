# Builds the contact sheet artifact: every photograph the 15 Oct Higgsfield top-up made, across the four concept camps and Edition
# One, each with its reviewer verdict, plus the keepers, the credit ledger, the ad data and the PDFs.
# Output: <scratchpad>/sheet (index.html, t/ thumbnails, f/ full-size JPGs, pdfs/). Card lines come from sheet_lines.json when it
# has the frame, otherwise from the verdict itself. Usage: build_sheet.py
import base64, collections, glob, json, os, re, shutil, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
E1 = os.path.normpath(os.path.join(HERE, "..", "..", "edition-one", "build"))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
OUT = f"{SPB}/sheet"
BAR = 8.5
PLATES = {"c4": f"{SPB}/c4/plates", "e1": f"{SPB}/e1/plates"}
E1_ORDER = ["aqua", "quatrefoil", "cluster", "halo", "verdant", "riviere", "papillon", "torsade", "dome", "square", "bow"]   # ₹ high to low

def verdicts(folder):
    V = {}
    for p in sorted(glob.glob(f"{folder}/verify/*.json"), key=os.path.getmtime):
        for v in json.load(open(p)):
            s = v["plate"].rsplit(".", 1)[0]
            V[s if "_" in s else s + "_a1"] = v
    return V
V = {**verdicts(HERE), **verdicts(E1)}
LINES = json.load(open(f"{HERE}/sheet_lines.json")) if os.path.exists(f"{HERE}/sheet_lines.json") else {}

LABELS = [("Face in frame", r"\bface\b|jaw|chin|\blips\b|eyebrow"), ("Stone order", r"same-colour|stone order"),
          ("Stone count", r"only \d+ stones"), ("Pearl count", r"pearl count"), ("Wrong stones", r"wrong stones"),
          ("Fix not made", r"(fix|change) was not made"), ("Scale", r"\bscale\b"), ("Off-palette", r"off-brand|beige|backdrop"),
          ("Clasp", r"clasp|t-bar|\bbar\b"), ("Construction", r".")]
def fallback(v):
    txt = next(iter((v.get("notes") if v.get("pass") else v.get("reasons")) or []), "") or next(iter(v.get("reasons") or []), "")
    t = re.sub(r"\s*\([^)]*\)", "", txt)
    t = re.split(r"(?<=\.)\s", t.strip())[0]
    if len(t) > 110: t = t[:107].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return ("Note" if v.get("pass") else next(l for l, rx in LABELS if re.search(rx, txt, re.I))), t

D4 = json.load(open(f"{HERE}/frames.json")); F4 = {f["id"]: f for f in D4["frames"]}
DE = json.load(open(f"{E1}/frames.json")); FE = {f["id"]: f for f in DE["frames"]}
FE.update({f["id"]: f for f in json.load(open(f"{E1}/frames_bold.json"))["frames"]})
FE["clusterC1"] = dict(id="clusterC1", camp="cluster", name="Almost edible", copy="Almost edible.", aspect="4:5")
# Composites (attempt mN): a real listing photo set by hand into the candy scene the last credits paid for (finished-ads/comp_*.py)
F4["prismC1"] = dict(id="prismC1", camp="prism", name="Almost edible", copy="Almost edible.", aspect="4:5")
SK = {s["key"]: s for s in json.load(open(f"{E1}/skus.json"))}

# Shoot order: the job ledgers in submission order, each crop straight after the frame it was cut from.
seq = []
for tag, folder in [("c4", HERE), ("e1", E1)]:
    have = {f[:-4] for f in os.listdir(PLATES[tag]) if f.endswith(".png")}; done = set()
    for j in json.load(open(f"{folder}/jobs.json")):
        s = f"{j['frame']}_{j['attempt']}".replace("_lite1k", "_lite")
        for t in [s, s + "c"]:
            if t in have and t not in done: seq.append((tag, t)); done.add(t)
    seq += [(tag, s) for s in sorted(have - done)]

def kind(att):
    if att == "lite": return "1K test"
    if att == "scene": return "Scene test, no product"
    if re.fullmatch(r"m\d", att): return "Composite, real listing photo"
    t, n, c = re.fullmatch(r"([ae])(\d)(c?)", att).groups()
    return ("Take " if t == "a" else "Edit ") + n + (", cropped" if c else "")
def order(att):
    if att == "lite": return (9, 0)
    if att == "scene": return (9, 1)
    if re.fullmatch(r"m\d", att): return (9, 2)
    t, n, c = re.fullmatch(r"([ae])(\d)(c?)", att).groups()
    return (int(n), 1 if c else 0) if t == "a" else (1, 1 + int(n))
def slug(s): return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")

frames = []
for n, (tag, stem) in enumerate(seq, 1):
    fid, att = stem.split("_", 1); comp = bool(re.fullmatch(r"m\d", att))
    F = (F4 if tag == "c4" else FE)[fid]; camp = F["camp"]
    sec = camp if tag == "c4" else ("e1b" if re.search(r"[BC]1$", fid) else "e1h")
    v = V.get(stem)
    st = "scene" if att == "scene" else "wait" if not v else "keep" if v.get("pass") and (v.get("score") or 0) >= BAR else "pass" if v.get("pass") else "fail"
    if att == "scene": label, line = "", "The candy bowl without the stud, on Z Image for the last 0.15 credits: a palette, light and copy-space test for the 2K shoot."
    elif not v: label, line = "", "With the reviewer now."
    elif stem in LINES: label, line = LINES[stem]["label"], LINES[stem]["line"]
    else: label, line = fallback(v)
    if tag == "c4": P = D4["pieces"][camp]; piece, price, sku = P["name"], P["price"], P["sku"]
    else: P = DE["pieces"][camp]; piece, price, sku = P["title"], f"₹{P['price']:,}", P["sku"]
    w, h = Image.open(f"{PLATES[tag]}/{stem}.png").size
    frames.append(dict(n=n, id=stem, tag=tag, sec=sec, camp=camp, code=(f"{fid} · " if tag == "c4" else "") + kind(att), kind=kind(att),
        name=F["name"], copy=F["copy"], aspect=F["aspect"], w=w, h=h, st=st, score=(v or {}).get("score"), label=label, line=line,
        reasons=(v or {}).get("reasons") or [], notes=(v or {}).get("notes") or [], fix=(v or {}).get("fix") or "",
        cr=0 if att.endswith("c") or comp else 1 if att == "lite" else 0.15 if att == "scene" else 2, piece=piece, price=price, sku=sku,
        candy=fid == "clusterC1", comp=comp, mk="comp" if comp else "scene" if att == "scene" else "candy" if att == "lite" else (camp if tag == "c4" else ("e1b" if re.search(r"[BC]1$", fid) else "e1h")), sort=(E1_ORDER.index(camp) if tag == "e1" else 0, fid, order(att)),
        t=f"t/{stem}.jpg", f=f"f/{stem}.jpg", file=f"Naira-{stem}-{slug(F['name'])}.jpg"))

# Images: a 640px thumbnail for the sheet and the full-size JPG for the lightbox and saves.
for d in ["t", "f", "pdfs"]: os.makedirs(f"{OUT}/{d}", exist_ok=True)
for f in frames:
    src = f"{PLATES[f['tag']]}/{f['id']}.png"; th, fu = f"{OUT}/{f['t']}", f"{OUT}/{f['f']}"
    if not os.path.exists(fu) or os.path.getmtime(fu) < os.path.getmtime(src):
        im = Image.open(src).convert("RGB")
        im.save(fu, "JPEG", quality=88, optimize=True, progressive=True)
        im.resize((640, round(im.height * 640 / im.width)), Image.LANCZOS).save(th, "JPEG", quality=76, optimize=True, progressive=True)
    f["tw"], f["th"] = 640, round(f["h"] * 640 / f["w"])

# Keepers: the best 8.5+ take of each frame idea, as the PDFs carry them.
best = {}
for f in frames:
    if f["st"] != "keep": continue
    key = f["id"].split("_")[0]
    if key not in best or f["score"] > best[key]["score"]: best[key] = f
SEC_ORDER = ["toggle", "woven", "heart", "prism", "e1h", "e1b"]
keepers = sorted(best.values(), key=lambda f: (SEC_ORDER.index(f["sec"]), f["sort"]))
for f in frames:
    if f["st"] == "keep" and best[f["id"].split("_")[0]] is not f: f["st"], f["line"] = "pass", "Passed; a better take of this idea is the keeper."
frames.sort(key=lambda f: (SEC_ORDER.index(f["sec"]), f["sort"]))
for f in frames: del f["sort"]

def sync(src, dst):
    # Copy only when the bytes differ, so a republish uploads just what changed.
    if not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(src) or open(dst, "rb").read() != open(src, "rb").read():
        shutil.copy(src, dst)

def thumb(im, dst, w=640):
    # Write a thumbnail only when it would differ from the one on disk.
    import io
    b = io.BytesIO(); im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(b, "JPEG", quality=80, optimize=True, progressive=True)
    if not os.path.exists(dst) or open(dst, "rb").read() != b.getvalue(): open(dst, "wb").write(b.getvalue())

# Finished ads: each keeper with its copy set (finished-ads/build_ads.py), scored by the newest review_r*.json.
FA = os.path.normpath(os.path.join(HERE, "..", "..", "finished-ads"))
# A score shows only if a reviewer saw this exact version of the ad (each round's .sig.json snapshot; see finished-ads/reviews.py).
sys.path.insert(0, FA); from reviews import current
ADS_CFG, CTL_CFG = json.load(open(f"{FA}/ads.json"))["ads"], json.load(open(f"{FA}/controls.json"))["ads"]
REV, CREV = current("review", ADS_CFG), current("controls_review", CTL_CFG)
byid = {f["id"]: f for f in frames}; finished = []
def sub_of(a): return a.get("n") or " · ".join(x.replace("<br>", " · ") for x in [a.get("spec"), a.get("price")] if x)   # the brand layout's spec and price
os.makedirs(f"{OUT}/ads", exist_ok=True); os.makedirs(f"{OUT}/at", exist_ok=True)
for a in ADS_CFG:
    src = f"{SPB}/ads/out/{a['id']}.jpg"
    if not os.path.exists(src) or a.get("plate", a["id"]) not in byid: continue
    fr, r = byid[a.get("plate", a["id"])], REV.get(a["id"], {}); im = Image.open(src); w, h = im.size
    sync(src, f"{OUT}/ads/{a['id']}.jpg"); thumb(im, f"{OUT}/at/{a['id']}.jpg")
    finished.append(dict(n=fr["n"], id="ad_" + a["id"], tag=fr["tag"], sec=fr["sec"], code=f"{a.get('plate', a['id'])} · finished ad" + (" · Story" if a.get("ext") else ""), kind="Finished ad",
        name=a["h"], copy=a["c"].replace("<br>", " "), aspect=a["fmt"], w=w, h=h, st="ad", score=r.get("score"), label=r.get("verdict", ""),
        line=(r.get("strengths") or [sub_of(a)])[0], reasons=r.get("issues", []), notes=r.get("strengths", []), fix=" ".join(r.get("fixes", [])),
        cr=0, piece=fr["piece"], price=fr["price"], sku=fr["sku"], t=f"at/{a['id']}.jpg", f=f"ads/{a['id']}.jpg",
        file=f"Naira-Ad-{a['id']}-{slug(a['h'])}.jpg", tw=640, th=round(h * 640 / w), sub=sub_of(a)))
controls = []
PIECE_OF = {"toggle": "toggle", "woven": "woven", "heart": "heart", "prism": "prism", "dome": "dome", "verdant": "verdant",
            "quatrefoil": "quatrefoil", "square": "square"}
for a in CTL_CFG:
    src = f"{SPB}/ads/out/{a['id']}.jpg"
    if not os.path.exists(src): continue
    k = a["id"].split("_", 1)[1].split("-")[0]; im = Image.open(src); w, h = im.size
    if k in D4["pieces"]: P = D4["pieces"][k]; piece, price, sku = P["name"], P["price"], P["sku"]
    else: P = DE["pieces"][k]; piece, price, sku = P["title"], f"₹{P['price']:,}", P["sku"]
    sync(src, f"{OUT}/ads/{a['id']}.jpg"); thumb(im, f"{OUT}/at/{a['id']}.jpg")
    controls.append(dict(n=0, id=a["id"], tag="ctl", sec="", code=f"{piece} · plain control" + (" · Story" if a.get("ext") else ""), kind="Plain control", name=a["h"], copy=a["c"],
        aspect=a["fmt"], w=w, h=h, st="ctl", score=CREV.get(a["id"], {}).get("score"), label="",
        line=(CREV.get(a["id"], {}).get("strengths") or ["The listing’s own close-up, to run beside the crazy ad as the control."])[0],
        reasons=CREV.get(a["id"], {}).get("issues", []), notes=CREV.get(a["id"], {}).get("strengths", []), fix=" ".join(CREV.get(a["id"], {}).get("fixes", [])), cr=0, piece=piece, price=price, sku=sku, t=f"at/{a['id']}.jpg", f=f"ads/{a['id']}.jpg",
        file=f"Naira-Control-{slug(piece)}{'-Story' if a.get('ext') else ''}.jpg", tw=640, th=round(h * 640 / w), sub=sub_of(a)))
SEC_RANK = {k: i for i, k in enumerate(["toggle", "woven", "heart", "prism", "e1h", "e1b"])}
finished.sort(key=lambda f: (f["label"] == "drop", -(f["score"] or 0), SEC_RANK[f["sec"]], f["n"]))   # dropped ads last

TITLES = {"toggle": "The Turn", "woven": "Hand-Woven", "heart": "Heartbeat", "prism": "Colour, in a Straight Line"}
sections = []
for k in ["toggle", "woven", "heart", "prism"]:
    P, C = D4["pieces"][k], D4["camps"][k]
    sections.append(dict(key=k, kicker=f"Concept camp · {P['name']}", title=TITLES[k], line=C["line"], idea=C["idea"],
                         facts=f"{P['price']} · SKU {P['sku']} · {P['stock']} in stock"))
sections[1]["extra"] = "W08's first render failed on Higgsfield and its two credits were refunded, so its frames start at take 2."
sections[3]["extra"] = ("The last card is a composite, not a render: the real bracelet from its listing photo, closed round a sweet in the candy "
                        "scene the last credits paid for. True scale (an 18 cm bracelet closed, beside sweets about 2.5 cm), the scene's own "
                        "sun, and the pink sweet's shadow falling across the links in front of it.")
sections += [
    dict(key="e1h", kicker="Edition One · eleven pre-order pieces", title="First heroes", line="One quiet visual pun per piece.",
         idea=("The first pass at the pre-orders: a doorbell, a box of mints, a specimen box, barfi, rangoli, a jaali screen, a shisha "
               "mirror, croissants and a pea pod, each holding one piece. Most missed on scale: the generator draws jewellery about 1.5 "
               "times too big beside a prop."), facts="₹1,399 to ₹2,449 · pre-order"),
    dict(key="e1b", kicker="Edition One · after “these aren’t good enough yet”", title="Bold, version two",
         line="One bold everyday object wears each piece, under hard sun.",
         idea=("The style changed after your note. A teacup, a pink cricket ball, a strawberry, a coupe, a lemonade glass, a "
               "shuttlecock, an ice tray, painted nails and rock sugar each wear one piece, close up, in low hard sun, with the product "
               "big in frame. The last whole credit went on the candy pun your ads proved, and the last 0.15 on a scene test of the same candy bowl, without the stud. "
               "The real stud from its listing macro was then set into that scene by hand, at true size: the last card."), facts="₹1,399 to ₹2,449 · pre-order")]
for s in sections:
    fs = [f for f in frames if f["sec"] == s["key"]]
    s.update(n=len(fs), keep=sum(f["st"] == "keep" for f in fs), credits=round(sum(f["cr"] for f in fs), 2))

# Credits: one square per credit, grouped by set, then the ledger from the Higgsfield transaction log (times in IST).
METER = [("toggle", "The Turn · Toggle Link Chain"), ("woven", "Hand-Woven · Woven Gold Hoops"), ("heart", "Heartbeat · Heartbead Bracelet"),
         ("prism", "Colour, in a Straight Line · Prism Rivière"), ("e1h", "Edition One · first heroes"), ("e1b", "Edition One · bold v2"),
         ("candy", "Candy test · 1K"), ("scene", "Scene test · Z Image")]
def credits_of(k): return round(sum(f["cr"] for f in frames if f["mk"] == k), 2)
def images_of(k): return sum(1 for f in frames if f["cr"] and f["mk"] == k)
meter = [dict(key=k, label=l, credits=credits_of(k), images=images_of(k)) for k, l in METER]
c4 = [f for f in frames if f["tag"] == "c4"]
cnt = lambda fs: (len(fs), sum(f["cr"] for f in fs))
first = cnt([f for f in c4 if f["kind"] == "Take 1"]); redo = cnt([f for f in c4 if f["kind"] not in ("Take 1",) and f["cr"]])
retakes = sum(1 for f in c4 if f["kind"] in ("Take 2", "Take 3")); edits = sum(1 for f in c4 if f["kind"].startswith("Edit"))
heroes = cnt([f for f in frames if f["mk"] == "e1h" and f["cr"]]); bold = cnt([f for f in frames if f["mk"] == "e1b" and f["cr"]])
candy = cnt([f for f in frames if f["mk"] == "candy"]); scene = cnt([f for f in frames if f["mk"] == "scene"])
comps = sum(1 for f in frames if f["comp"]); crops = sum(1 for f in frames if not f["cr"] and not f["comp"])
spent = round(sum(f["cr"] for f in frames), 2)
ledger = [["15 Oct, 23:32", "Credit package added", "", "+200"],
          ["15 Oct, 23:51", f"Four concept camps, first pass: 40 frames. One render failed and its 2 credits were refunded", first[0], first[1]],
          ["16 Oct, 00:05 to 01:12", f"Retakes ({retakes}) and edits ({edits}) over nine rounds, each fixing what the reviewer found", redo[0], redo[1]],
          ["16 Oct, 05:19", "Edition One heroes, one for each pre-order piece", heroes[0], heroes[1]],
          ["16 Oct, 05:42", "Edition One bold v2, after “these aren’t good enough yet”", bold[0], bold[1]],
          ["16 Oct, 05:48", "Candy test on Nano Banana 2 Lite at 1K, the last whole credit", candy[0], candy[1]],
          ["16 Oct, 12:32", "Scene test on Z Image, the candy bowl without the stud: the only model under the last 0.22 credits", scene[0], round(scene[1], 2)],
          ["", "Crops cut here from passing frames, at no cost", crops, 0],
          ["16 Oct, afternoon", "Composites: the real listing photos of the Prism bracelet and the Cluster stud, set into the paid candy scene at true scale, at no cost", comps, 0]]
total = dict(images=len(frames), generated=len(frames) - crops - comps, crops=crops, comps=comps, spent=spent, left=round(201.22 - spent, 2), carried=1.22, cheapest=0.15)

C = collections.Counter(f["st"] for f in frames)
stats = dict(keep=len(keepers), keepframes=C["keep"], passed=C["pass"], fail=C["fail"], wait=C["wait"],
             failScale=sum(1 for f in frames if f["st"] == "fail" and f["label"] == "Scale"))

PDF_TITLES = [("Ready-To-Run", "Ready-to-run ads, one per page"), ("Toggle", f"{TITLES['toggle']} · Toggle Link Chain"),
              ("Woven", f"{TITLES['woven']} · Woven Gold Hoops"), ("Heartbead", f"{TITLES['heart']} · Heartbead Bracelet"),
              ("Prism", f"{TITLES['prism']} · Prism Rivière Bracelet"), ("Board", "The four concept camps on one board"),
              ("Edition-One", "Edition One · every keeper")]
pdfs = []
for src in [f"{SPB}/c4/pdf_out", f"{SPB}/e1/pdf_out", f"{SPB}/ads/pdf_out"]:
    if not os.path.isdir(src): continue
    for fn in os.listdir(src):
        sync(f"{src}/{fn}", f"{OUT}/pdfs/{fn}")
        b = open(f"{src}/{fn}", "rb").read()
        i, title = next((i, t) for i, (k, t) in enumerate(PDF_TITLES) if k in fn)
        pdfs.append(dict(file=fn, title=title, order=i, pages=len(re.findall(rb"/Type\s*/Page[^s]", b)), mb=round(len(b) / 1e6, 1)))
pdfs.sort(key=lambda p: p.pop("order"))

ad = dict(lede=("Naira’s own Meta account, every jewellery ad to 12 Oct 2026: 108 ads and ₹1.59 lakh, spend-weighted and corrected "
                "for nine friends-and-family orders."),
          nums=[["1.44×", "ROAS on concept statics, against 0.57× on plain statics"],
                ["10 of 10", "ad sets where concept won outbound click-through, side by side"],
                ["10 of 16", "concept sales came from one image, “Almost edible.”"],
                ["1.79×", "concept statics in the 4:5 Instagram Feed; Stories 1.36×"]],
          caveat=("So crazy has beaten plain, but not always. One candy image carries most of the lead, and the gap is only "
                  "statistically safe once the friends-and-family orders are removed. These camps follow what won: a visual pun with the "
                  "piece as the punchline, food and measuring tools, light pastel grounds, the 4:5 Feed first, pieces over ₹2,000, and a "
                  "plain craft close-up beside each one as the control."))
nxt = dict(lede=(f"{round(201.22 - spent, 2)} credits are left, under the 0.15 the cheapest Higgsfield model costs. The next top-up is "
                 "planned in edition-one/PLAN_V3.md."),
           items=[["About 85 credits", "About 30 Edition One frames, ₹2,000+ pieces first: Aqua, Quatrefoil, Cluster, Halo and Verdant. "
                                       "Each prompt asks for about 0.6 times the true size, so the piece lands at true size."],
                  ["30 to 40 credits", "The four camps’ gaps, mostly the Toggle clasp and the Prism stone count."],
                  ["2 credits a scene", "Shoot each new set once more without the piece. The real piece can then be set in by hand at true "
                                        "scale, as the empty candy bowl now carries the Prism bracelet and the Cluster stud."]],
           questions=["Prism Cluster Studs: the listing macro shows 8 tiny pearls; the description and the other photos show 6. Which is right?",
                      "Petite Bow Studs and Verdant Cushion Studs: the listing text says gold, but every photo shows white metal.",
                      "Petite Square Huggies: the description doesn’t mention the seed pearls that appear in every photo."])

# Run sheet: each ad set pairs the finished ads with their plain control (AD_PERFORMANCE rule 5: same ad set, judge on cost per
# purchase), Prism first because it is the proven product and the only one with 10/10 ads; Feed first, Stories second.
FIN = {f["id"][3:]: f for f in finished}; CTL = {c["id"]: c for c in controls}
def pick(ids, pool): return [dict(id=i, name=pool[i]["name"] if i in pool else i, score=pool[i]["score"] if i in pool else None,
                                  aspect=pool[i]["aspect"] if i in pool else "") for i in ids if i in pool]
RUN = [("Prism Rivière Bracelet", "₹2,399 · in stock · the proven product (12 of 16 concept sales)",
        ["P01_a1", "prismC1_m1", "P10_a1c", "P09_a1"], ["P02_a2c", "P01_a1-story"], ["ctl_prism", "ctl_prism-story"],
        "Lead here. prismC1_m1 is a fresh picture for the account's best ad (the same pun, the real bracelet), so run it in the "
        "Feed beside P01. P10_a1c (‘Watercolour, set in stone.’) is P01's head-to-head challenger, not a third concept: the winner "
        "keeps the slot, and the loser becomes the refresh after Diwali. A/B the two rangoli Stories (both 10) rather than running "
        "them against each other; hold P10_a1c-story until P10_a1c wins its Feed test."),
       ("Prism Cluster Studs", "₹2,099 · pre-order", ["clusterC1_m1"], [], ["ctl_cluster"],
        "The ‘Almost edible.’ pun on a ₹2,000+ piece, with the real stud. Settle the pearl count on the listing first: the macro "
        "shows 8, the text says 6."),
       ("Verdant Cushion Studs", "₹1,399 · pre-order", ["verdant1_a1"], ["verdant1_a1-story"], ["ctl_verdant", "ctl_verdant-story"],
        "Fix the listing's metal line (text says yellow gold, photos show white metal) before spending."),
       ("Woven Gold Hoops", "₹1,499 · in stock", ["W01_a1", "W07_a2"], ["W02_a1", "W05_a2"], ["ctl_woven", "ctl_woven-story"],
        "Strongest as part of a ₹2,000+ set; alone, a ₹1,499 pair struggles to pay back."),
       ("Bold Dome Huggies", "₹1,649 · pre-order", ["dome1_a1"], ["dome1_a1-story"], ["ctl_dome", "ctl_dome-story"],
        "The closest copy of the ‘Almost edible.’ mechanic. Watch cost per purchase."),
       ("Petite Square Huggies", "₹1,599 · pre-order", ["squareB1_a1"], ["squareB1_a1-story"], ["ctl_square", "ctl_square-story"],
        "Name the seed pearls on the listing before spending."),
       ("Heartbead Bracelet", "₹1,299 · in stock", ["H01_e1", "H09_a1"], ["H01_e1-story"], ["ctl_heart", "ctl_heart-story"],
        "Lowest ticket in the set; best inside a gift set."),
       ("Diwali test", "Toggle Link Chain and Woven Gold Hoops · ₹1,499", ["T10_a1", "W10_a2"], [], ["ctl_toggle", "ctl_woven"],
        "End both on the last order date that still delivers before Diwali (8 Nov).")]
run = [dict(set=n, facts=fa, feed=pick(fe, FIN), story=pick(st, FIN), ctl=pick(ct, CTL), note=no) for n, fa, fe, st, ct, no in RUN]

data = dict(frames=frames, keepers=[f["id"] for f in keepers], sections=sections, meter=meter, ledger=ledger, total=total,
            stats=stats, pdfs=pdfs, ad=ad, next=nxt, finished=finished, controls=controls, run=run)
velista = base64.b64encode(open(f"{SPB}/c4/fonts/Velista.ttf", "rb").read()).decode()
page = open(f"{HERE}/sheet_template.html").read()
page = page.replace("__VELISTA__", velista).replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
open(f"{OUT}/index.html", "w").write(page)
tot = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs)
print(f"{OUT}/index.html {round(len(page) / 1024)} KB; site {round(tot / 1e6, 1)} MB")
print(f"{len(frames)} frames ({total['generated']} generated, {crops} crops), {spent} credits; keepers {len(keepers)}, "
      f"passed {C['pass']}, missed {C['fail']}, awaiting {C['wait']}; lines from file {sum(f['id'] in LINES for f in frames)}")
print("ledger", [(r[2], r[3]) for r in ledger[1:]], "meter", [(m["key"], m["credits"]) for m in meter])
