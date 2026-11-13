# One Shopify mutation (one approval), 13 Nov 2026, for the owner's "make changes and ship ... once in depth verification done":
# the size corrections measured in the owner's stock video (IMG_7514.MOV), see ../../size-check-13nov/. All five pieces are live
# (ACTIVE) and stay live: no status, price, compare-at price, stock, title, tags or metafields are sent.
#  - SPP Soleil Petal Pendant (N02): about 18mm across with a stone of about 5.5mm (was 25mm and 7mm). Its two worn photos, drawn on
#    2 Nov with the pendant about 31mm on the neck, come off the listing: two new tries on 13 Nov still drew it at about 32 to 34mm
#    (jobs.json), and a photo on a body is never resized by hand, so the listing keeps its two product photos until a worn photo
#    at the true size is made. New card soleil-petal-pendant-size-guide-v2.jpg.
#  - HTN V-Bar Teardrop Necklace (A16): bars about 17mm (was 15mm), pear about 10 x 14mm (was 10 x 13mm). New card -v2.
#  - POHS Pave Open Heart Studs (A15): about 23mm across and 22mm tall (was 20 x 19mm). New card -v3 (-v2 is the 3 Nov card).
#  - CLGN-RD Clover Garland Necklace (C2): clovers about 8.5mm (was 10mm), stones about 3mm (was 3.5mm). New card -v2.
#  - CLG Clover Garland Bracelet: the same clovers, so the same two lines change. Its card shows the length only and stays.
# The four productSets pass the photos that stay by media id (nothing uploaded twice), the new card by URL under its new filename
# (the description's size-guide image links to that name; Shopify renames a duplicate filename, so each card gets a new one), and
# the one variant by id with its image plus the Title option that goes with it, as ship_a16_w2.py. The bracelet has three colour
# variants, so its copy goes through productUpdate, which leaves its variants and photos alone.
# The text sent is the live text with only the phrases in FIX replaced, each found exactly once. On 13 Nov the live text was
# checked to equal ship_2nov.body() of listings.json (with ' stored as a plain apostrophe) and, for the bracelet, the 30 Oct record.
# Usage: python3 -I fix_13nov.py          -> ../shopify/fix_13nov.json (variables) and ../shopify/fix_13nov.graphql (the mutation)
#        python3 -I fix_13nov.py --record -> the same corrections into listings.json, once the ship is verified
import importlib.util, json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../shopify")
s = importlib.util.spec_from_file_location("s2", os.path.join(H, "ship_2nov.py")); S2 = importlib.util.module_from_spec(s); s.loader.exec_module(S2)
LPATH = os.path.join(H, "listings.json"); LIST = json.load(open(LPATH)); L = {x["id"]: x for x in LIST}
URL = json.load(open(os.path.join(H, "url_map.json")))
CLOVER = json.load(open(os.path.join(H, "../../clover-garland/shopify/ship_30oct.json")))["clover"]
NEVER = re.compile(r"\b(real|diamonds?|waterproof|tarnish\w*|anti-tarnish|freshwater|hypoallergenic)\b", re.I)
MI = "gid://shopify/MediaImage/"

# sku: listing id, product, variant, variant image, card now linked, new card, photos kept (in order), media dropped
P = {"SPP": ("N02", "10377183002786", "50798485045410", "46712237621410", "soleil-petal-pendant-size-guide.jpg",
             "soleil-petal-pendant-size-guide-v2.jpg", ["46712237719714", "46712237621410"],
             ["46712287559842", "46712287592610", "46712003231906"]),
     "HTN": ("A16", "10377179857058", "50798476820642", "46723504865442", "v-bar-teardrop-necklace-size-guide.jpg",
             "v-bar-teardrop-necklace-size-guide-v2.jpg",
             ["46723504865442", "46723504898210", "46723504930978", "46723504963746", "46723504996514"], ["46717163241634"]),
     "POHS": ("A15", "10375501742242", "50785485324450", "46717162848418", "pave-open-heart-studs-size-guide-v2.jpg",
              "pave-open-heart-studs-size-guide-v3.jpg", ["46717162848418", "46723869245602", "46723869278370", "46717162946722"],
              ["46717163012258"]),
     "CLGN-RD": ("C2", "10377922838690", "50804419887266", "46723504472226", "clover-garland-necklace-size-guide.jpg",
                 "clover-garland-necklace-size-guide-v2.jpg", ["46723504570530", "46723504472226"], ["46723504636066"])}
CLG = "gid://shopify/Product/10374743261346"
FIX = {"SPP": [("cubic zirconia of about 7mm", "cubic zirconia of about 5.5mm"),
               ("about 25mm across in all", "about 18mm across in all"),
               ("Pendant: Approximately 25mm across", "Pendant: Approximately 18mm across"),
               ("cubic zirconia, approximately 7mm, in a claw setting", "cubic zirconia, approximately 5.5mm, in a claw setting")],
       "HTN": [("cubic zirconia of about 10 x 13mm hangs", "cubic zirconia of about 10 x 14mm hangs"),
               ("Two polished bars, approximately 15mm each", "Two polished bars, approximately 17mm each"),
               ("cubic zirconia, approximately 10 x 13mm, hanging", "cubic zirconia, approximately 10 x 14mm, hanging")],
       "POHS": [("open heart of about 20mm", "open heart of about 23mm"),
                ("Approximately 20mm across and 19mm tall", "Approximately 23mm across and 22mm tall")],
       "CLGN-RD": [("Clovers: Approximately 10mm across", "Clovers: Approximately 8.5mm across"),
                   ("petals per clover, approximately 3.5mm", "petals per clover, approximately 3mm")],
       "CLG": [("Clovers: Fifteen, approximately 10mm across", "Clovers: Fifteen, approximately 8.5mm across"),
               ("petals per clover, approximately 3.5mm", "petals per clover, approximately 3mm")]}
STALE = {"SPP": ["7mm", "25mm"], "HTN": ["10 x 13mm", "15mm"], "POHS": ["20mm", "19mm"], "CLGN-RD": ["10mm", "3.5mm"],
         "CLG": ["10mm", "3.5mm"]}


def fix(text, pairs, strict=True):
    for old, new in pairs:
        n = text.count(old)
        assert n == 1 or (not strict and n == 0), (old, n)
        text = text.replace(old, new)
    return text


def stale(k, text):
    hits = [v for v in STALE[k] if re.search(r"(?<![\d.])" + re.escape(v), text)]
    assert not hits, (k, hits)


def unfix(x, pairs):            # listings.json after --record holds the new phrases: rebuild the 13 Nov live text from it
    x = json.loads(json.dumps(x))
    for old, new in pairs:
        x["intro"] = x["intro"].replace(new, old); x["details"] = [d.replace(new, old) for d in x["details"]]
    return x


def live(x, card):              # Shopify keeps ' as a plain apostrophe (html.escape writes &#x27;)
    return S2.body(x, card).replace("&#x27;", "'")


def build():
    var, args, calls = {}, [], []
    for k, (i, pid, vid, vimg, oc, nc, keep, drop) in P.items():
        x = unfix(L[i], FIX[k]); t = x["title"]; ptype = S2.S31.TYPES[x["type"]][0]
        body = fix(live(x, oc), FIX[k] + [(S2.S31.CDN + oc + '"', S2.S31.CDN + nc + '"')])
        stale(k, body)
        second = x["intro"].split(". ")[1].rstrip("."); seo = f"{second}. {t} by Naira Petite."
        nseo = fix(seo, FIX[k], strict=False); stale(k, nseo)
        files = [{"id": MI + m} for m in keep] + [{"originalSource": URL[nc], "filename": nc, "alt": f"Size guide — {t}",
                                                   "contentType": "IMAGE"}]
        inp = {"descriptionHtml": body, "files": files, "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}],
               "variants": [{"id": f"gid://shopify/ProductVariant/{vid}", "optionValues": [{"optionName": "Title", "name": "Default Title"}],
                             "file": {"id": MI + vimg}}]}
        if nseo != seo:
            inp["seo"] = {"title": f"{t} — {ptype} | Naira Petite", "description": nseo}
            assert len(nseo) <= 320, k
        assert vimg in keep and not set(keep) & set(drop) and "status" not in inp, k
        a = k.split("-")[0].lower(); var[a] = inp; var[a + "id"] = {"id": f"gid://shopify/Product/{pid}"}
        args += [f"${a}: ProductSetInput!", f"${a}id: ProductSetIdentifiers!"]
        calls.append(f"  {a}: productSet(identifier: ${a}id, input: ${a}, synchronous: true) {{ product {{ id handle status descriptionHtml "
                     "seo { title description } mediaCount { count } media(first: 10) { nodes { id alt status } } variants(first: 1) "
                     "{ nodes { id sku price compareAtPrice inventoryQuantity media(first: 1) { nodes { id } } } } } "
                     "userErrors { field message code } }\n")
    clg = fix(CLOVER["descriptionHtml"], FIX["CLG"]); stale("CLG", clg)
    var["clg"] = {"descriptionHtml": clg}; var["clgid"] = {"id": CLG}
    args += ["$clg: ProductUpdateInput!", "$clgid: ProductUpdateIdentifiers!"]
    calls.append("  clg: productUpdate(identifier: $clgid, product: $clg) { product { id handle status descriptionHtml mediaCount { count } "
                 "variants(first: 3) { nodes { sku price compareAtPrice inventoryQuantity } } } userErrors { field message } }\n")
    words = json.dumps(var, ensure_ascii=False)
    assert not NEVER.search(words), NEVER.search(words).group(0)
    return var, "mutation SizeFix13Nov(" + ", ".join(args) + ") {\n" + "".join(calls) + "}\n"


if __name__ == "__main__":
    if sys.argv[1:] == ["--record"]:
        for k, (i, *_ ) in P.items():
            x = L[i]
            for old, new in FIX[k]:
                if new in x["intro"] or any(new in d for d in x["details"]): continue
                n = x["intro"].count(old) + sum(d.count(old) for d in x["details"]); assert n == 1, (k, old, n)
                x["intro"] = x["intro"].replace(old, new); x["details"] = [d.replace(old, new) for d in x["details"]]
        json.dump(LIST, open(LPATH, "w"), ensure_ascii=False, indent=1)
        print("listings.json:", ", ".join(f"{P[k][0]} {k}" for k in P))
    else:
        var, doc = build()
        os.makedirs(OUT, exist_ok=True)
        json.dump(var, open(os.path.join(OUT, "fix_13nov.json"), "w"), ensure_ascii=False, separators=(",", ":"))
        open(os.path.join(OUT, "fix_13nov.graphql"), "w").write(doc)
        for a, v in var.items():
            if not a.endswith("id"):
                print(a, len(v.get("files", [])), "files", "seo" if "seo" in v else "", len(v["descriptionHtml"]), "chars")
