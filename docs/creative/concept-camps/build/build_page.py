# Builds the board page for the artifact: four camps, every verified frame, a lightbox, and saves for the PDFs and full-size JPGs.
# Usage: build_page.py <final.json> <outdir> [final_e1.json]   (outdir receives index.html; web/, full/, pdfs/ are copied separately)
# With final_e1.json the page also carries the Edition One camps and the ad-data band.
import base64, html, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/c4"
sel = json.load(open(sys.argv[1])); out = sys.argv[2]
D = json.load(open(f"{HERE}/frames.json")); idx = {f["id"]: f for f in D["frames"]}
velista = base64.b64encode(open(f"{SP}/fonts/Velista.ttf", "rb").read()).decode()
ORDER = ["toggle", "woven", "heart", "prism"]
pdfs = json.load(open(f"{out}/pdfs.json"))          # {camp: filename, "board": filename}
stats = json.load(open(f"{out}/stats.json"))        # numbers for the checking note

camps = []
for n, camp in enumerate(ORDER, 1):
    if camp not in sel: continue
    P, C = D["pieces"][camp], D["camps"][camp]
    frames = []
    for it in sel[camp]:
        f = idx[it["id"]]
        frames.append(dict(id=f["id"], name=f["name"], aspect=f["aspect"], copy=f["copy"], score=it.get("score"),
                           note=it.get("note", ""), w=it["w"], h=it["h"], web=f"web/{f['id']}.jpg", full=f"full/{f['id']}.jpg",
                           fullname=f"Naira-{f['id']}-{f['name'].replace(' ', '-').replace(',', '')}.jpg"))
    camps.append(dict(key=camp, n=n, group="Concept camp", title=C["title"], line=C["line"], idea=C["idea"], name=P["name"], price=P["price"],
                      sku=P["sku"], stock=P["stock"], pdf=pdfs[camp], frames=frames))
if len(sys.argv) > 3:
    E1 = os.path.join(HERE, "..", "..", "edition-one", "build")
    sel1 = json.load(open(sys.argv[3])); DE = json.load(open(f"{E1}/frames.json"))
    SK = {s["key"]: s for s in json.load(open(f"{E1}/skus.json"))}
    for m, k in enumerate(["aqua", "quatrefoil", "cluster", "halo", "verdant", "riviere", "papillon", "torsade", "dome", "square", "bow"], 1):
        if not sel1.get(k): continue
        P, C = DE["pieces"][k], DE["camps"][k]
        frames = [dict(id=it["id"], name=it["name"], aspect=it["aspect"], copy=it["copy"], score=it.get("score"), note=it.get("note", ""),
                       w=it["w"], h=it["h"], web=f"web/{it['id']}.jpg", full=f"full/{it['id']}.jpg",
                       fullname=f"Naira-E1-{it['id']}-{it['name'].replace(' ', '-').replace(',', '')}.jpg") for it in sel1[k]]
        camps.append(dict(key=k, n=m, group="Edition One", title=C["name"], line=P["title"], idea=C["idea"], name=P["title"],
                          price=f"₹{P['price']:,}", sku=P["sku"], stock=SK[k]["stock"], pdf=pdfs["e1"], frames=frames))
data = json.dumps(dict(camps=camps, board=pdfs["board"]), ensure_ascii=False)

page = """<title>Naira Crazy Camps</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Jost:wght@400;500&display=swap">
<style>
@font-face{font-family:"Velista";src:url(data:font/ttf;base64,__VELISTA__) format("truetype");font-display:swap}
/* Layout: a lookbook board. Masthead, then one band per camp (story left, frames right on wide screens, stacked on phones). */
:root{
  --paper:#F4F0E8; --sheet:#FBF8F3; --ink:#1C1C1C; --muted:#6E625A; --rule:#E2D9CC; --blush:#FBEDE9; --chip:#EFE3D6; --gold:#9C7A3C;
  --a-toggle:#D8A9A1; --a-woven:#E2BE98; --a-heart:#EDB9B2; --a-prism:#9FD3D9; --a-e1:#C9A3C8;
  --display:"Velista","Cormorant Garamond",Georgia,serif; --text:"Cormorant Garamond",Georgia,serif; --label:"Jost","Helvetica Neue",Arial,sans-serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --paper:#1D1917; --sheet:#25201D; --ink:#F1EAE0; --muted:#B9AA9B; --rule:#3A322D; --blush:#2E2522; --chip:#352C27; --gold:#D6B678;
  --a-toggle:#B98A83; --a-woven:#C19C77; --a-heart:#C9938C; --a-prism:#76AFB5; --a-e1:#A882A7; color-scheme:dark}}
:root[data-theme="dark"]{
  --paper:#1D1917; --sheet:#25201D; --ink:#F1EAE0; --muted:#B9AA9B; --rule:#3A322D; --blush:#2E2522; --chip:#352C27; --gold:#D6B678;
  --a-toggle:#B98A83; --a-woven:#C19C77; --a-heart:#C9938C; --a-prism:#76AFB5; --a-e1:#A882A7; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--text);font-size:19px;line-height:1.5;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.wrap{max-width:1240px;margin:0 auto;padding-block:40px 64px;display:flex;flex-direction:column;gap:56px}
.lab{font-family:var(--label);font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
header{display:grid;gap:14px;border-bottom:1px solid var(--rule);padding-bottom:32px}
h1{font-family:var(--display);font-weight:400;font-size:clamp(46px,8vw,96px);line-height:1;margin:0;text-wrap:balance}
.lede{font-style:italic;font-size:clamp(21px,2.6vw,28px);max-width:40ch;margin:0}
.bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
button{font-family:var(--label);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink);background:transparent;
  border:1px solid var(--ink);padding:11px 16px;cursor:pointer;border-radius:0}
button:hover{background:var(--ink);color:var(--paper)} button:focus-visible{outline:2px solid var(--gold);outline-offset:3px}
button[disabled]{opacity:.45;cursor:default} button.quiet{border-color:var(--rule)}
.note{font-family:var(--label);font-size:13px;letter-spacing:.04em;color:var(--muted);min-height:1em}
.toc{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.data{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;border-top:1px solid var(--rule);padding-top:28px}
.data div{display:grid;gap:6px;align-content:start}
.data b{font-family:var(--display);font-weight:400;font-size:clamp(34px,4.4vw,48px);line-height:1}
.data span{font-size:17px;line-height:1.35}
.datahead{display:grid;gap:8px;max-width:72ch}
.datahead h2{font-family:var(--display);font-weight:400;font-size:clamp(30px,4vw,44px);margin:0}
.toc a{display:grid;gap:4px;text-decoration:none;color:var(--ink);padding:14px 14px 16px;background:var(--sheet);border-top:3px solid var(--acc)}
.toc a span:first-child{font-family:var(--display);font-size:24px;line-height:1.1}
section.camp{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:40px;border-top:1px solid var(--rule);padding-top:36px}
.story{display:grid;gap:14px;align-content:start;position:sticky;top:calc(env(safe-area-inset-top,0px) + 16px)}
.story h2{font-family:var(--display);font-weight:400;font-size:clamp(34px,4.6vw,52px);line-height:1.02;margin:0;text-wrap:balance}
.story .line{font-style:italic;font-size:24px;line-height:1.25;margin:0}
.story p{margin:0;max-width:60ch}
.swatch{width:44px;height:6px;background:var(--acc)}
.facts{font-family:var(--label);font-size:13px;letter-spacing:.06em;color:var(--muted);display:grid;gap:2px}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;align-items:start}
figure{margin:0;display:grid;gap:8px}
figure button.img{padding:0;border:0;background:var(--sheet);display:block;width:100%;cursor:zoom-in}
figure img{display:block;width:100%;height:auto;max-width:100%}
figcaption{display:grid;gap:2px}
.code{font-family:var(--label);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.chip{font-family:var(--label);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;background:var(--chip);color:var(--ink);padding:2px 7px}
.hl{font-style:italic;font-size:19px;line-height:1.25}
footer{border-top:1px solid var(--rule);padding-top:28px;display:grid;gap:12px;max-width:72ch}
footer h3{font-family:var(--display);font-weight:400;font-size:30px;margin:0}
footer p{margin:0}
dialog{border:0;padding:0;background:var(--paper);color:var(--ink);max-width:min(96vw,1100px);width:100%;max-height:96vh}
dialog::backdrop{background:rgba(20,16,14,.82)}
.lb{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,300px);gap:0}
.lb .pic{background:var(--sheet);display:flex;align-items:center;justify-content:center;max-height:96vh}
.lb img{max-height:92vh;width:auto;max-width:100%}
.lb .side{padding:24px;display:grid;gap:12px;align-content:start}
.lb .side h4{font-family:var(--display);font-weight:400;font-size:30px;margin:0;line-height:1.1}
@media (max-width:900px){.data{grid-template-columns:repeat(2,minmax(0,1fr))} section.camp{grid-template-columns:minmax(0,1fr)} .story{position:static} .grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .toc{grid-template-columns:repeat(2,minmax(0,1fr))} .lb{grid-template-columns:minmax(0,1fr)} .lb img{max-height:70vh}}
@media (max-width:460px){.grid{gap:12px} body{font-size:18px}}
@media (prefers-reduced-motion:no-preference){figure button.img img{transition:opacity .2s} figure button.img:hover img{opacity:.92}}
</style>
<div class="wrap">
  <header>
    <span class="lab">Naira Petite · Crazy camps · October 2026</span>
    <h1>Crazy Camps</h1>
    <p class="lede">__LEDE__</p>
    <div class="bar"><button id="saveBoard" type="button" disabled>Save the board PDF</button><span class="note" id="boardNote"></span></div>
    <nav class="toc" id="toc" aria-label="Camps"></nav>
  </header>
  <section id="dataBand" hidden><div class="datahead"><span class="lab">What your ad account says</span><h2>Crazy wins, mostly</h2><p id="dataLede"></p></div><div class="data" id="dataGrid"></div></section>
  <main id="camps" style="display:flex;flex-direction:column;gap:56px"></main>
  <footer>
    <h3>How these were made and checked</h3>
    <p>Every photograph was generated on Higgsfield (Nano Banana Pro, 2K) from the product's own listing photos, one piece per frame, using the Naira image skill's six-part prompt: the shot, a lock on what must not change, real-world scale against a known object, the scene, two lights, and what must never appear.</p>
    <p id="checkNote"></p>
    <p>The PDFs hold each camp's cover, board and plan, then one photograph per page at its full 2K size, ready to upload to Claude Design. The photographs carry no text, logo or price; set those in Claude Design.</p>
  </footer>
</div>
<dialog id="lb" aria-label="Photograph"><div class="lb"><div class="pic"><img id="lbImg" alt=""></div><div class="side">
  <span class="lab" id="lbCode"></span><h4 id="lbName"></h4><span class="hl" id="lbCopy"></span><span class="note" id="lbMeta"></span>
  <div class="bar"><button id="lbSave" type="button" disabled>Save full-size JPG</button><button id="lbClose" class="quiet" type="button">Close</button></div>
  <span class="note" id="lbNote"></span></div></div></dialog>
<script>
const DATA = __DATA__;
const STATS = __STATS__;
const $ = s => document.querySelector(s);
const el = (t, a = {}, ...kids) => { const e = document.createElement(t); for (const [k, v] of Object.entries(a)) { if (k === "class") e.className = v; else if (k === "text") e.textContent = v; else e.setAttribute(k, v); } for (const k of kids) if (k) e.append(k); return e; };
const FMT = {"4:5": "Feed 4:5", "9:16": "Story 9:16"};
let downloads = null;

function render() {
  const toc = $("#toc"), main = $("#camps");
  for (const c of DATA.camps) {
    const a = el("a", {href: "#" + c.key, style: "--acc:var(--a-" + c.key + ", var(--a-e1))"}, el("span", {text: c.title}), el("span", {class: "lab", text: c.name}));
    toc.append(a);
    const story = el("div", {class: "story"},
      el("span", {class: "swatch", style: "--acc:var(--a-" + c.key + ", var(--a-e1))"}),
      el("span", {class: "lab", text: c.group + " · " + c.name}),
      el("h2", {text: c.title}), el("p", {class: "line", text: c.line}), el("p", {text: c.idea}),
      el("div", {class: "facts"}, el("span", {text: c.price + " · SKU " + c.sku}), el("span", {text: c.stock + (c.group === "Edition One" ? " available to pre-order" : " in stock on Shopify, 15 Oct 2026")}), el("span", {text: c.frames.length + " verified frames"})),
      el("div", {class: "bar"}, el("button", {type: "button", class: "savePdf", "data-file": "pdfs/" + c.pdf, disabled: ""}, document.createTextNode(c.group === "Edition One" ? "Save Edition One PDF" : "Save camp PDF"))),
      el("span", {class: "note"}));
    const grid = el("div", {class: "grid"});
    for (const f of c.frames) {
      const img = el("img", {src: f.web, alt: c.name + ", " + f.name, loading: "lazy", width: f.w, height: f.h});
      const btn = el("button", {type: "button", class: "img", "aria-label": "Open " + f.id + " " + f.name}, img);
      btn.addEventListener("click", () => openLb(c, f));
      grid.append(el("figure", {}, btn, el("figcaption", {},
        el("span", {class: "code"}, document.createTextNode(f.id + " · " + FMT[f.aspect]), f.score != null ? el("span", {class: "chip", text: "Checked · " + f.score.toFixed(1)}) : el("span", {class: "chip", text: "Checked"})),
        el("span", {text: f.name}), el("span", {class: "hl", text: f.copy}))));
    }
    main.append(el("section", {class: "camp", id: c.key}, story, grid));
  }
  $("#checkNote").textContent = STATS.note;
  if (STATS.data) { $("#dataLede").textContent = STATS.dataLede; for (const [b, t] of STATS.data) $("#dataGrid").append(el("div", {}, el("b", {text: b}), el("span", {text: t}))); $("#dataBand").hidden = false; }
}

let current = null;
function openLb(c, f) {
  current = {c, f};
  $("#lbImg").src = f.web; $("#lbImg").alt = c.name + ", " + f.name;
  $("#lbCode").textContent = f.id + " · " + FMT[f.aspect] + " · " + f.w + "×" + f.h;
  $("#lbName").textContent = f.name; $("#lbCopy").textContent = f.copy;
  $("#lbMeta").textContent = c.name + " · " + c.price + (f.note ? " · " + f.note : "");
  $("#lbNote").textContent = "";
  const full = new Image(); full.onload = () => { if (current && current.f === f) $("#lbImg").src = f.full; }; full.src = f.full;
  $("#lb").showModal();
}
$("#lbClose").addEventListener("click", () => $("#lb").close());
$("#lb").addEventListener("click", e => { if (e.target === $("#lb")) $("#lb").close(); });

async function save(path, name, note) {
  if (!downloads) return;
  note.textContent = "Preparing…";
  try {
    const r = await fetch(path); if (!r.ok) throw {code: "missing"};
    const blob = await r.blob();
    await downloads.save({filename: name, data: blob});
    note.textContent = "Saved " + name;
  } catch (e) {
    const code = e && e.code;
    note.textContent = code === "declined" ? "Not saved." : code === "rate_limited" ? "Another save is open. Try again in a moment." :
      code === "missing" ? "That file did not load. Reload the page and try again." : "Saving is not available in this view.";
  }
}

render();
(window.claude && window.claude.use ? window.claude.use("downloads") : Promise.resolve(null)).then(d => {
  downloads = d; if (!d) return;
  const sb = $("#saveBoard"); sb.disabled = false; sb.addEventListener("click", () => save("pdfs/" + DATA.board, DATA.board, $("#boardNote")));
  document.querySelectorAll(".savePdf").forEach(b => { b.disabled = false; const note = b.parentElement.nextElementSibling;
    b.addEventListener("click", () => save(b.dataset.file, b.dataset.file.split("/").pop(), note)); });
  const ls = $("#lbSave"); ls.disabled = false; ls.addEventListener("click", () => current && save(current.f.full, current.f.fullname, $("#lbNote")));
}).catch(() => {});
</script>
"""
lede = ("Every photograph here passed a check against its Shopify listing: four in-stock concept camps and the Edition One pre-orders." if len(sys.argv) > 3 else "Four in-stock pieces, four ideas, forty photographs, each one checked against its Shopify listing.")
page = page.replace("__LEDE__", lede).replace("__VELISTA__", velista).replace("__DATA__", data).replace("__STATS__", json.dumps(stats, ensure_ascii=False))
open(f"{out}/index.html", "w").write(page)
print(f"{out}/index.html", round(len(page) / 1024), "KB")
