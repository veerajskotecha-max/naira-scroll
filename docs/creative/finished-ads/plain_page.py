# Builds the "Naira Plain Images" artifact: every plain photograph (ready for ads, reference only) and the store's listing photos,
# with the plain-image PDFs from plain_pdfs.py. Frame thumbnails and full-size JPGs are the contact sheet's own published files
# (copied server-side at publish); listing photos, the two composites and the PDFs are uploaded from <scratchpad>/plain/site.
# Usage: plain_page.py     writes <scratchpad>/plain/site/ and <scratchpad>/plain/publish.json (the files map for each publish)
import base64, glob, json, os, re, shutil
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__)); CRE = os.path.normpath(f"{HERE}/..")
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
SITE, PDFS = f"{SPB}/plain/site", f"{SPB}/plain/pdfs"
SHEET_URL = "https://claude.ai/artifact/MBR3rFTZWmy3XYHx2Xovrn"     # the contact sheet, whose t/ and f/ files are reused
LOCAL_FRAMES = {"prismC1_m1", "clusterC1_m1"}                     # not yet on the published contact sheet

def frames():
    s = open(f"{SPB}/sheet/index.html", encoding="utf-8").read()
    return json.loads(re.search(r"const DATA = (\{.*?\});\n", s, re.S).group(1).replace("<\\/", "</"))["frames"]

def main():
    for d in ["l", "lf", "t", "f", "pdfs"]: os.makedirs(f"{SITE}/{d}", exist_ok=True)
    plain = json.load(open(f"{PDFS}/plain.json")); F = {f["id"]: f for f in frames()}
    E1 = json.load(open(f"{CRE}/edition-one/build/frames.json"))["pieces"]; C4 = json.load(open(f"{CRE}/concept-camps/build/frames.json"))["pieces"]
    names = {**{k: v["name"] for k, v in C4.items()}, **{k: v["title"] for k, v in E1.items()}}
    prices = {**{k: v["price"] for k, v in C4.items()}, **{k: f"₹{v['price']:,}" for k, v in E1.items()}}
    items = []
    for g, ids in [("ready", plain["ready"]), ("ref", plain["reference"])]:
        for i in ids:
            f = F[i]; name = f["name"] + (" (composite)" if f.get("comp") else "")
            items.append(dict(g=g, id=i, title=f["piece"], name=name, price=f["price"], tall=f["aspect"] == "9:16" or f["h"] / f["w"] > 1.5,
                              meta=f"{f['code']} · {f['w']}×{f['h']} px" + (f" · ad score {f['score']}" if f.get("score") else ""),
                              line=f.get("line") or "", t=f"t/{i}.jpg", f=f"f/{i}.jpg", file=f"Naira-Plain-{i}.jpg"))
    for folder in [f"{CRE}/concept-camps/build/refs", f"{CRE}/edition-one/build/refs"]:
        for d in sorted(glob.glob(f"{folder}/*/")):
            piece = os.path.basename(d.rstrip("/"))
            for p in sorted(glob.glob(f"{d}*.jpg")):
                key = f"{piece}-{os.path.basename(p)}"; im = Image.open(p).convert("RGB"); w, h = im.size
                th = f"{SITE}/l/{key}"
                if not os.path.exists(th): im.resize((640, round(h * 640 / w)), Image.LANCZOS).save(th, "JPEG", quality=80, optimize=True, progressive=True)
                shutil.copyfile(p, f"{SITE}/lf/{key}")
                items.append(dict(g="list", id=key, title=names.get(piece, piece), name=os.path.basename(p), price=prices.get(piece, ""),
                                  tall=h / w > 1.5, meta=f"{w}×{h} px · from the store", line="", t=f"l/{key}", f=f"lf/{key}",
                                  file=f"Naira-Listing-{key}"))
    for i in LOCAL_FRAMES:
        shutil.copyfile(f"{SPB}/sheet/t/{i}.jpg", f"{SITE}/t/{i}.jpg"); shutil.copyfile(f"{SPB}/sheet/f/{i}.jpg", f"{SITE}/f/{i}.jpg")
    kind = {"1": "Ready for ads", "2": "Reference only", "3": "Listing photos"}
    pdfs = [dict(file=p["file"], title=p["title"], count=p["count"], mb=p["mb"], kind=kind[p["file"].split("-")[2]]) for p in plain["pdfs"]]
    for p in pdfs: shutil.copyfile(f"{PDFS}/{p['file']}", f"{SITE}/pdfs/{p['file']}")
    data = dict(items=items, pdfs=pdfs, mb=round(sum(p["mb"] for p in pdfs), 1),
                counts=dict(ready=len(plain["ready"]), reference=len(plain["reference"]), listing=sum(1 for x in items if x["g"] == "list")))
    tpl = open(f"{HERE}/plain_template.html", encoding="utf-8").read()
    b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
    page = (tpl.replace("__VELISTA__", b64(f"{HERE}/brand/Velista.ttf")).replace("__WM_LIGHT__", b64(f"{SPB}/plain/logo_sage_dark_480.png"))
               .replace("__WM_DARK__", b64(f"{SPB}/plain/logo_white_480.png")).replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    open(f"{SITE}/index.html", "w", encoding="utf-8").write(page)
    # files map, split so each publish stays under 255 files and 64 MB
    frame_ids = plain["ready"] + plain["reference"]
    copy = {f"{d}/{i}.jpg": ({"from": f"{SITE}/{d}/{i}.jpg"} if i in LOCAL_FRAMES else {"artifact": SHEET_URL, "path": f"{d}/{i}.jpg"})
            for i in frame_ids for d in ("t", "f")}
    lst = {f"{d}/{x['id']}": {"from": f"{SITE}/{d}/{x['id']}"} for x in items if x["g"] == "list" for d in ("l", "lf")}
    pd = {f"pdfs/{p['file']}": {"from": f"{SITE}/pdfs/{p['file']}"} for p in pdfs}
    ready_pdfs = {k: v for k, v in pd.items() if "-1-Ready" in k}; other_pdfs = {k: v for k, v in pd.items() if k not in ready_pdfs}
    json.dump([copy, {**lst, **ready_pdfs}, other_pdfs], open(f"{SPB}/plain/publish.json", "w"), indent=1)
    print("items", len(items), "page KB", round(os.path.getsize(f"{SITE}/index.html") / 1024), "publishes",
          [len(x) for x in [copy, {**lst, **ready_pdfs}, other_pdfs]])

if __name__ == "__main__":
    main()
