# Builds the Shopify handoff kit: kit/index.html (artifact page), kit/listing.json (machine-readable), kit/thumbs/*.jpg.
import json, os, shutil, html
H = os.path.dirname(os.path.abspath(__file__)); K = f"{H}/kit"
D = json.load(open(f"{H}/products.json")); EM = json.load(open(f"{H}/export_map.json"))
UM = json.load(open(f"{H}/url_map.json")) if os.path.exists(f"{H}/url_map.json") else {}
PL = json.load(open(f"{H}/pi_lines.json"))
os.makedirs(f"{K}/thumbs", exist_ok=True)
e = html.escape
def vname(v): return " / ".join(v["options"])
def roles(p):
    vimg = {v["image"]: v["options"][0] for v in p["variants"] if v["options"] and v["image"]}
    out = []
    for i, k in enumerate(p["gallery"]):
        if k not in EM: continue
        if k.endswith("_W1"): r = "worn on the model"
        elif k.endswith("_W2"): r = "worn, close detail"
        elif k.endswith("_M"): r = "macro detail: " + p["macro_alt"][0].lower() + p["macro_alt"][1:]
        else: r = "on a cream plaster block, the full piece straight on"
        base = k.rsplit("_", 1)[0] if k.endswith(("_W1", "_W2", "_M")) else None
        var = vimg.get(k) or (vimg.get(base + "_H") if base else None)
        if p["id"] in ("N25",) and k in vimg: var = vimg[k]
        alt = f"{p['title']}{', ' + var if var and len(vimg) > 1 else ''} — {r}"
        out.append(dict(key=k, file=EM[k], url=UM.get(EM[k]), alt=alt, variant=var if len(vimg) > 1 else None))
    for k, var in vimg.items():
        if k not in p["gallery"] and k in EM:
            out.append(dict(key=k, file=EM[k], url=UM.get(EM[k]), alt=f"{p['title']}, {var} — on a cream plaster block", variant=var))
    return out
data, cards, pending = [], [], []
for p in D["products"]:
    imgs = roles(p); pos = {im["key"]: n + 1 for n, im in enumerate(imgs)}
    pending += [k for k in p["gallery"] if k not in EM]
    for im in imgs: shutil.copy(f"{H}/thumbs/{im['file']}", f"{K}/thumbs/{im['file']}")
    variants = [dict(options=dict(zip(p["options"], v["options"])), sku=v["sku"], price=v["price"] or p["price"], inventory_on_arrival=v["qty"],
                     pi_line=v["pi_line"], cost_usd=v["cost_usd"], image_position=pos.get(v["image"])) for v in p["variants"]]
    data.append(dict(title=p["title"], handle=p["handle"], vendor="Naira Petite", product_type=p["type"], status="DRAFT", supplier_code=p["pi"],
                     tags=p["tags"], options=p["options"], price_inr=p["price"], tagline=p["line"], body=p["body"], size_and_fit=p["size"], stones=p["stones"],
                     variants=variants, images=[dict(position=n + 1, src=im["url"], file=im["file"], alt=im["alt"], variant=im["variant"]) for n, im in enumerate(imgs)],
                     flags=p["flags"], notes=p["notes"]))
    strip = "".join(f'<figure><img src="thumbs/{e(im["file"])}" alt="{e(im["alt"])}" loading="lazy" width="200" height="248"><figcaption>{n + 1}</figcaption></figure>' for n, im in enumerate(imgs))
    vrows = "".join(f"<tr><td>{e(vname(v)) or '—'}</td><td><code>{e(v['sku'])}</code></td><td>₹{(v['price'] or p['price']):,}</td><td>{v['pi_line'] or '—'}</td>"
                    f"<td>{v['qty'] if v['qty'] is not None else '—'}</td><td>{pos.get(v['image'], '—')}</td></tr>" for v in p["variants"])
    flags = "".join(f'<li>{e(f)}</li>' for f in p["flags"])
    urls = "".join(f'<li><span class="alt">{e(im["alt"])}</span><code>{e(im["url"] or "uploading…")}</code></li>' for im in imgs)
    src = "PI" if p["pi"] not in ("—", "") and p["id"].startswith(("P", "C")) else ("Notion + PI" if p["pi"] not in ("—", "") else "Notion")
    cards.append(f'''<article class="card" id="{e(p["handle"])}" data-src="{src}" data-type="{e(p["type"])}" data-flag="{1 if p["flags"] else 0}">
<header><div><h3>{e(p["title"])}</h3><p class="meta">{e(p["type"])} · <code>{e(p["pi"])}</code> · {src}</p></div><p class="price">₹{p["price"]:,}</p></header>
<div class="strip">{strip}</div>
<p class="line">{e(p["line"])}</p><p class="body">{e(p["body"])}</p>
<dl><dt>Size</dt><dd>{e(p["size"])}</dd><dt>Stones</dt><dd>{e(p["stones"])}</dd><dt>Tags</dt><dd>{e(", ".join(p["tags"]))}</dd>{f"<dt>Note</dt><dd>{e(p['notes'])}</dd>" if p["notes"] else ""}</dl>
<div class="tablewrap"><table><thead><tr><th>Variant</th><th>SKU</th><th>Price</th><th>PI line</th><th>Qty</th><th>Image</th></tr></thead><tbody>{vrows}</tbody></table></div>
{f'<ul class="flags">{flags}</ul>' if flags else ''}
<details><summary>Image URLs and alt text ({len(imgs)})</summary><ol class="urls">{urls}</ol></details>
</article>''')
live_rows = []
for l in D["live"]:
    im = l["image"]; th = ""
    if im and im in EM:
        shutil.copy(f"{H}/thumbs/{EM[im]}", f"{K}/thumbs/{EM[im]}"); th = f'<img src="thumbs/{e(EM[im])}" alt="{e(l["title"])} new packshot" width="80" height="99">'
    live_rows.append(f'<tr><td>{th}</td><td><b>{e(l["title"])}</b><br><code>{e(l["handle"])}</code></td><td><code>{e(l["pi"])}</code><br>lines {", ".join(map(str, l["lines"]))}</td><td>{e(l["action"])}</td></tr>')
    l2 = dict(l); l2["image_src"] = UM.get(EM.get(im)) if im else None; data.append(dict(live_update=l2))
pi_rows = "".join(f'<tr><td>{r["line"]}</td><td><code>{r["code"]}</code></td><td>{e(r["desc"])}</td><td>{r["qty"]}</td><td>${r["usd"]:.2f}</td><td>{e("; ".join(r["to"]))}</td></tr>' for r in PL)
json.dump(data, open(f"{K}/listing.json", "w"), indent=1, ensure_ascii=False)
newp = [p for p in D["products"]]; nvar = sum(len(p["variants"]) for p in newp); nimg = sum(len(roles(p)) for p in newp)
nflag = sum(len(p["flags"]) for p in newp)
types = sorted({p["type"] for p in newp})
chips = "".join(f'<button class="chip" data-f="type:{t}">{t}</button>' for t in types)
page = open(f"{H}/page_template.html").read()
page = (page.replace("%%CARDS%%", "\n".join(cards)).replace("%%LIVE%%", "".join(live_rows)).replace("%%PI%%", pi_rows).replace("%%CHIPS%%", chips)
        .replace("%%NPROD%%", str(len(newp))).replace("%%NVAR%%", str(nvar)).replace("%%NIMG%%", str(nimg)).replace("%%NLIVE%%", str(len(D["live"])))
        .replace("%%NFLAG%%", str(nflag)).replace("%%JSON%%", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
open(f"{K}/index.html", "w").write(page)
print(len(newp), "products", nvar, "variants", nimg, "images; pending gallery keys:", len(pending), pending[:40])
