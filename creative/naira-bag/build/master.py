#!/usr/bin/env python3
"""
NAIRA D-cut handle bag (6 x 9.5 x 2 in) - editable print master.

One page, 17 x 11.45 in (16.75 x 11.2 in trim + 0.125 in bleed), built as named PDF layers:

  1  Background            cream, vector
  2  Leaf pattern          the website's watercolour sprigs, each a separate 2048 px image at 34 %,
                           plus the soft cream pools that keep the pattern out from behind the lockups
  3  Florals               the tulip clusters and dots, vector
  4  Logo                  NAIRA wordmark traced to vector (sage letters, blush flower)
  5  Text                  eyebrow, tagline, rule, QR caption - live text, fonts embedded
  6  QR code               vector, opens nairaflore.com/jewellery
  7  Dieline               cut + fold lines in spot colours "Dieline" / "Fold", overprint,
                           labels - set to NOT PRINT

Each layer is rendered by Chrome to its own PDF (vector stays vector, images keep full
resolution), then stacked with PyMuPDF as optional-content groups on one page, clipped exactly to
the artboard. A second file swaps the live text for outlines so no fonts are needed at the printer.
"""
import asyncio, io, json, pathlib, re, sys
import numpy as np
import fitz
import segno
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from playwright.async_api import async_playwright

import build2 as B
from motifs import CREAM, INK, LOGO_SAGE, LOGO_BLUSH

fitz.TOOLS.set_icc(True)
ROOT = pathlib.Path(__file__).parent
M = ROOT / "master"; M.mkdir(exist_ok=True)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
BLEED = B.BLEED
W, H = B.SHEET_W + 2 * BLEED, B.SHEET_H + 2 * BLEED        # 17 x 11.45 in
WP, HP = W * 72, H * 72                                    # 1224 x 824.4 pt
PAGE_IN = (18, 12)                                          # Chrome renders on a larger page; we clip exactly
PAGE_PT = (PAGE_IN[0] * 72, PAGE_IN[1] * 72)
GLUE_EDGE = B.GLUE_X + BLEED                               # 16.125 in: nothing but cream beyond this
MAGENTA = "#E4007C"
NAME = "Naira-DCut-Bag-6x9.5x2"


# ------------------------------------------------------------------ helpers
def svg_doc(body, extra_defs="", style=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}in" height="{H}in" viewBox="0 0 {W} {H}">'
            f'{B.defs()}{extra_defs}{style}{body}</svg>')


def html(svg):
    return ("<!doctype html><html><head><meta charset='utf-8'><style>"
            f"@page{{size:{PAGE_IN[0]}in {PAGE_IN[1]}in;margin:0}}"
            "html,body{margin:0;padding:0;background:transparent}svg{display:block}</style></head>"
            f"<body>{svg}</body></html>")


NOGLUE = f'<clipPath id="noglue"><rect x="0" y="0" width="{GLUE_EDGE}" height="{H}"/></clipPath>'


def split_face(elems):
    """Sort one face's elements (from build2.face_layers) into print layers."""
    L = {"pattern": [], "florals": [], "text": [], "logo": [], "qr": []}
    for e in elems:
        if e.startswith("<ellipse") and 'rx="1.35"' in e:
            L["qr"].append(e)                            # soft cream pool under the QR block
        elif e.startswith("<ellipse"):
            L["pattern"].append(e)                       # cream pool behind the lockup
        elif e.startswith("<text"):
            L["text"].append(e)
        elif e.startswith("<image"):
            L["logo"].append(e)
        elif e.startswith("<rect") and LOGO_SAGE in e:
            L["text"].append(e)                          # the short rule under the wordmark
        elif e.startswith("<rect") and CREAM in e:
            L["qr"].append(e)                            # quiet zone behind the QR
        elif "h1v1h-1z" in e:
            L["qr"].append(e)
        else:
            L["florals"].append(e)
    return L


LOGO_VEC = json.load(open(ROOT / "assets" / "naira-logo-vector.json"))


def vector_logo(img_el):
    x, y, w = (float(re.search(rf'{k}="([\d.]+)"', img_el).group(1)) for k in ("x", "y", "width"))
    s = w / LOGO_VEC["width"]
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="{LOGO_VEC["letters"]}" fill="{LOGO_SAGE}" fill-rule="evenodd"/>'
            f'<path d="{LOGO_VEC["flower"]}" fill="{LOGO_BLUSH}" fill-rule="evenodd"/></g>')


def merged_qr(qr_el):
    """Same QR, drawn as one path of row runs instead of hundreds of touching unit squares."""
    tx, ty, sc = (float(v) for v in re.search(r'translate\(([\d.]+),([\d.]+)\) scale\(([\d.e-]+)\)', qr_el).groups())
    q = segno.make(B.QR_URL, error="m")
    d = []
    for y, row in enumerate(q.matrix_iter(scale=1, border=0)):
        row = list(row); x = 0
        while x < len(row):
            if row[x]:
                s = x
                while x < len(row) and row[x]:
                    x += 1
                d.append(f"M{s},{y}h{x - s}v1h-{x - s}z")
            else:
                x += 1
    return f'<g transform="translate({tx},{ty}) scale({sc})"><path d="{"".join(d)}" fill="{INK}"/></g>'


def sprig_instances():
    """The approved leaf repeat, reproduced instance by instance (same lattice and jitter as
    build2.ground for the full sheet), so each sprig is its own movable image."""
    ox = oy = -BLEED
    cell, sizes = 2.35, (2.0, 1.6)

    def jit(i, j, n):
        return (np.sin(i * 12.9898 + j * 78.233 + n * 37.719) * 43758.5453) % 1.0

    i0, i1 = int((ox - 3) // cell), int((ox + W + 3) // cell) + 1
    j0, j1 = int((oy - 3) // cell), int((oy + H + 3) // cell) + 1
    out = []
    for j in range(j0, j1):
        for i in range(i0, i1):
            cx = (i + 0.5 + (0.5 if j % 2 else 0)) * cell + (jit(i, j, 1) - .5) * cell * .35
            cy = (j + 0.5) * cell + (jit(i, j, 2) - .5) * cell * .35
            which = (i + j) % 2
            size = sizes[which] * (0.85 + 0.3 * jit(i, j, 3))
            rot = jit(i, j, 4) * 360
            X, Y, r = cx - ox, cy - oy, size * 0.7072
            if X + r < 0 or X - r > GLUE_EDGE or Y + r < 0 or Y - r > H:
                continue
            out.append(f'<image href="leaf-sprig-{which + 1}.png" x="{X - size/2:.4f}" y="{Y - size/2:.4f}" '
                       f'width="{size:.4f}" height="{size:.4f}" transform="rotate({-rot:.3f} {X:.4f} {Y:.4f})" '
                       f'opacity="{B.PATTERN_OP}" preserveAspectRatio="none"/>')
    return out


# ------------------------------------------------------------------ layers
def build_layers():
    front = split_face(B.face_layers(B.FRONT_X + BLEED, BLEED))
    back = split_face(B.face_layers(B.BACK_X + BLEED, BLEED, qr=True))
    both = {k: front[k] + back[k] for k in front}
    L = {}
    L["background"] = svg_doc(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{CREAM}"/>')
    L["pattern"] = svg_doc('<g clip-path="url(#noglue)">' + "".join(sprig_instances()) + "".join(both["pattern"]) + "</g>", NOGLUE)
    L["florals"] = svg_doc('<g clip-path="url(#noglue)">' + "".join(both["florals"]) + "</g>", NOGLUE)
    L["logo"] = svg_doc("".join(vector_logo(e) for e in both["logo"]))
    L["text"] = svg_doc("".join(both["text"]), style=B.style(1.0))
    L["qr"] = svg_doc("".join(e if "h1v1h-1z" not in e else merged_qr(e) for e in both["qr"]))
    L["labels"] = svg_doc(dieline_labels(), style=label_style())
    return L


def label_style():
    return (f'<style>@font-face{{font-family:"JostM";src:url(data:font/woff2;base64,{B.b64(B.FONTS/"Jost-500.woff2")}) format("woff2")}}'
            f'.lb{{font-family:"JostM",sans-serif;font-size:.1px;letter-spacing:.025px;fill:{MAGENTA}}}'
            f'.ls{{font-family:"JostM",sans-serif;font-size:.075px;letter-spacing:.012px;fill:{MAGENTA}}}</style>')


def T(v):
    return v + BLEED


def dieline_labels():
    t = []
    _fix = lambda z: z.replace("″", '"')
    for x, s in ((1, "GUSSET 2″"), (5, "FRONT 6″"), (9, "GUSSET 2″"), (13, "BACK 6″  ·  QR side")):
        t.append(f'<text x="{T(x)}" y="{T(.34)}" class="lb" text-anchor="middle">{s}</text>')
    t.append(f'<text x="{T(16.375)}" y="{T(.34)}" class="lb" text-anchor="middle">GLUE</text>')
    t.append(f'<text x="{T(16.375)}" y="{T(.5)}" class="ls" text-anchor="middle">0.75″ · no print</text>')
    for x in (5, 13):
        t.append(f'<text x="{T(x)}" y="{T(B.HANDLE_TOP) - .09}" class="ls" text-anchor="middle">D-CUT HANDLE 2.3 × 1.0″ · 1.05″ from top</text>')
    t.append(f'<text x="{T(.12)}" y="{T(8.5) - .06}" class="ls">GUSSET FOLD · 1″ above base</text>')
    t.append(f'<text x="{T(.12)}" y="{T(9.5) - .06}" class="ls">BASE FOLD · 9.5″</text>')
    t.append(f'<text x="{T(.12)}" y="{T(10.35)}" class="ls">BOTTOM FLAP 1.7″</text>')
    t.append(f'<text x="{W/2}" y="{T(11.2) - .1}" class="ls" text-anchor="middle">'
             'NAIRA D-cut bag 6 × 9.5 × 2 in  ·  flat 16.75 × 11.2 in + 0.125 in bleed  ·  magenta = cut  ·  cyan dashed = fold  ·  '
             'reference dieline from the Kraftix template, align to your die  ·  THIS LAYER DOES NOT PRINT</text>')
    return _fix("".join(t))


def dieline_pdf(path):
    """Cut and fold lines as a raw content stream in two spot colours, overprinting."""
    doc = fitz.open()
    pg = doc.new_page(width=PAGE_PT[0], height=PAGE_PT[1])
    Hpt = PAGE_PT[1]

    def P(x, y):                      # trim inches (y down) -> PDF user space points (y up)
        return f"{(x + BLEED) * 72:.3f} {Hpt - (y + BLEED) * 72:.3f}"

    cut, fold = [], []
    cut.append(f"{P(0, 0)} m {P(16.75, 0)} l {P(16.75, 11.2)} l {P(0, 11.2)} l h")
    k = 0.5523
    for x0 in (B.FRONT_X, B.BACK_X):
        cx, top, hw, hh, arc = x0 + 3, B.HANDLE_TOP, B.HANDLE_W / 2, B.HANDLE_H, B.HANDLE_ARC
        cut.append(f"{P(cx - hw, top + hh)} m {P(cx - hw, top + arc)} l "
                   f"{P(cx - hw, top + arc - k * arc)} {P(cx - k * hw, top)} {P(cx, top)} c "
                   f"{P(cx + k * hw, top)} {P(cx + hw, top + arc - k * arc)} {P(cx + hw, top + arc)} c "
                   f"{P(cx + hw, top + hh)} l h")
    for x in (1, 2, 8, 9, 10, 16):
        fold.append(f"{P(x, 0)} m {P(x, 11.2)} l")
    for y in (8.5, 9.5):
        fold.append(f"{P(0, y)} m {P(16.75, y)} l")
    for gx in (0, 8):                                   # gusset base triangles
        fold.append(f"{P(gx, 9.5)} m {P(gx + 1, 8.5)} l {P(gx + 2, 9.5)} l")
    fold.append(f"{P(16, 9.5)} m {P(16.75, 8.75)} l")
    for a, b in ((2, 3.7), (8, 6.3), (10, 11.7), (16, 14.3)):   # 45 deg base-flap folds
        fold.append(f"{P(a, 9.5)} m {P(b, 11.2)} l")

    cs_cut, cs_fold, gs = doc.get_new_xref(), doc.get_new_xref(), doc.get_new_xref()
    doc.update_object(cs_cut, "[/Separation /Dieline /DeviceCMYK <</FunctionType 2 /Domain [0 1] /C0 [0 0 0 0] /C1 [0 1 0 0] /N 1>>]")
    doc.update_object(cs_fold, "[/Separation /Fold /DeviceCMYK <</FunctionType 2 /Domain [0 1] /C0 [0 0 0 0] /C1 [1 0 0 0] /N 1>>]")
    doc.update_object(gs, "<</Type /ExtGState /OP true /op true /OPM 1>>")
    content = ("q /GSo gs 0.6 w 1 J 1 j /CSc CS 1 SCN [] 0 d\n" + "\n".join(c + " S" for c in cut) +
               "\n/CSf CS 1 SCN [3 2.5] 0 d\n" + "\n".join(f + " S" for f in fold) + "\nQ\n")
    cx = doc.get_new_xref()
    doc.update_object(cx, "<<>>")
    doc.update_stream(cx, content.encode())
    doc.xref_set_key(pg.xref, "Contents", f"{cx} 0 R")
    doc.xref_set_key(pg.xref, "Resources", f"<</ColorSpace <</CSc {cs_cut} 0 R /CSf {cs_fold} 0 R>> /ExtGState <</GSo {gs} 0 R>>>>")
    doc.save(path)


# ------------------------------------------------------------------ text -> outlines
def outline_pdf_text(src_pdf, extra=""):
    """Every glyph of a Chrome-made PDF redrawn as a filled path at its exact position, using the
    embedded font programs themselves - kerning and tracking are whatever Chrome laid out."""
    doc = fitz.open(src_pdf)
    page = doc[0]
    fonts = {}
    for f in page.get_fonts(full=True):
        xref, basefont = f[0], f[3]
        name, ext, ftype, buf = doc.extract_font(xref)
        if buf:
            fonts.setdefault(basefont.split("+")[-1], []).append(TTFont(io.BytesIO(buf)))

    def fit_error(tt, span):
        """How well this font's advances explain the laid-out glyph positions (tracking is a constant)."""
        order, hm, upm = tt.getGlyphOrder(), tt["hmtx"], tt["head"].unitsPerEm
        ch = span["chars"]
        if any(c[1] >= len(order) for c in ch):
            return 1e9
        res = [(ch[i + 1][2][0] - ch[i][2][0]) - hm[order[ch[i][1]]][0] * span["size"] / upm for i in range(len(ch) - 1)]
        if not res:
            return 0.0
        med = float(np.median(res))
        return float(sum(abs(r - med) for r in res))

    paths = []
    for span in page.get_texttrace():
        key = span["font"].split("+")[-1]
        cands = [tt for k, tts in fonts.items() if k.startswith(key) or key.startswith(k) for tt in tts]
        if not cands:
            raise RuntimeError(f"font {span['font']} not extractable; have {list(fonts)}")
        tt = min(cands, key=lambda t: fit_error(t, span))
        gs, order, upm = tt.getGlyphSet(), tt.getGlyphOrder(), tt["head"].unitsPerEm
        col = "#%02X%02X%02X" % tuple(int(round(c * 255)) for c in span["color"])
        s = span["size"] / 72.0 / upm
        for ucs, gid, origin, bbox in span["chars"]:
            if gid < 0 or gid >= len(order):
                continue
            pen = SVGPathPen(gs)
            gs[order[gid]].draw(pen)
            d = pen.getCommands()
            if not d:
                continue
            ox, oy = origin[0] / 72.0, origin[1] / 72.0
            paths.append(f'<path d="{d}" transform="translate({ox:.5f},{oy:.5f}) scale({s:.7f},{-s:.7f})" fill="{col}"/>')
    return svg_doc(extra + "".join(paths))


def text_rules():
    """Non-glyph marks that live in the Text layer (the short sage rules), for the outlined copy."""
    els = split_face(B.face_layers(B.FRONT_X + BLEED, BLEED))["text"] + split_face(B.face_layers(B.BACK_X + BLEED, BLEED, qr=True))["text"]
    return "".join(e for e in els if e.startswith("<rect"))


# ------------------------------------------------------------------ render + assemble
async def render(pages):
    """pages: {name: svg} -> master/layer-<name>.pdf"""
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        for name, svg in pages.items():
            f = M / f"layer-{name}.html"
            f.write_text(html(svg), encoding="utf-8")
            pg = await b.new_page()
            await pg.goto(f.as_uri())
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(300)
            await pg.pdf(path=str(M / f"layer-{name}.pdf"), width=f"{PAGE_IN[0]}in", height=f"{PAGE_IN[1]}in",
                         margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}, print_background=True)
            await pg.close()
            print("  rendered", name)
        await b.close()


LAYERS = [("Background · cream", "background"), ("Leaf pattern · website leaves", "pattern"),
          ("Florals · tulips and leaves", "florals"), ("Logo · vector", "logo"),
          ("QR code · nairaflore.com/jewellery", "qr"), ("Text", "text")]


def assemble(out_path, text_layer="text", text_label="Text · live, fonts embedded", spec_pdf=None, dieline_on=True):
    out = fitz.open()
    page = out.new_page(width=WP, height=HP)
    clip = fitz.Rect(0, 0, WP, HP)
    for label, key in LAYERS:
        if key == "text":
            key, label = text_layer, text_label
        oc = out.add_ocg(label, on=True)
        with fitz.open(M / f"layer-{key}.pdf") as src:
            page.show_pdf_page(page.rect, src, 0, clip=clip, oc=oc)
    dl = out.add_ocg("Dieline · cut and fold · DOES NOT PRINT" if dieline_on else "Dieline · switched off · DOES NOT PRINT", on=dieline_on)
    for key in ("dieline", text_layer.replace("text", "labels")):
        with fitz.open(M / f"layer-{key}.pdf") as src:
            page.show_pdf_page(page.rect, src, 0, clip=clip, oc=dl)
    # the dieline shows on screen but never prints or exports
    out.xref_set_key(dl, "Usage", "<</Print <</PrintState /OFF>> /View <</ViewState /ON>> /Export <</ExportState /OFF>>>>")
    cat = out.pdf_catalog()
    out.xref_set_key(cat, "OCProperties/D/AS",
                     f"[<</Event /Print /OCGs [{dl} 0 R] /Category [/Print]>> <</Event /Export /OCGs [{dl} 0 R] /Category [/Export]>>]")
    page.set_trimbox(fitz.Rect(BLEED * 72, BLEED * 72, WP - BLEED * 72, HP - BLEED * 72))
    page.set_bleedbox(page.rect)
    if spec_pdf:
        sp_page = out.new_page(width=WP, height=HP)
        with fitz.open(spec_pdf) as sp:
            sp_page.show_pdf_page(sp_page.rect, sp, 0, clip=fitz.Rect(0, 0, WP, HP))
    out.set_metadata({"title": "NAIRA D-cut handle bag 6 x 9.5 x 2 in - print master",
                      "author": "NAIRA", "subject": "Flat artwork 16.75 x 11.2 in trim + 0.125 in bleed; layered; dieline non-printing",
                      "keywords": "NAIRA, D-cut bag, print, dieline, nairaflore.com",
                      "creator": "NAIRA packaging", "producer": "PyMuPDF / Chromium"})
    out.save(out_path, garbage=4, deflate=True, clean=True)
    return out_path


if __name__ == "__main__":
    step = sys.argv[1] if len(sys.argv) > 1 else "all"
    if step in ("layers", "all"):
        import shutil
        for n in (1, 2):
            src = M / f"leaf-sprig-{n}.png"
            assert src.exists(), src
        L = build_layers()
        asyncio.run(render(L))
        dieline_pdf(M / "layer-dieline.pdf")
        print("  outlining text")
        asyncio.run(render({"text_outlined": outline_pdf_text(M / "layer-text.pdf", text_rules()),
                            "labels_outlined": outline_pdf_text(M / "layer-labels.pdf")}))
    if step in ("assemble", "all"):
        assemble(M / f"{NAME}-EDITABLE.pdf", spec_pdf=M / "spec.pdf" if (M / "spec.pdf").exists() else None)
        assemble(M / f"{NAME}-PRINT-READY.pdf", text_layer="text_outlined", text_label="Text · outlined, no fonts needed", dieline_on=False)
        for f in sorted(M.glob(f"{NAME}-*.pdf")):
            print(f"{f.name}  {f.stat().st_size/1e6:.2f} MB")
