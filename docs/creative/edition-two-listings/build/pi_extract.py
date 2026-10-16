# Extracts embedded images from the PI PDF with their page position: pi_extract.py PDF OUTDIR
import sys, fitz, json
doc = fitz.open(sys.argv[1]); out = sys.argv[2]; rows = []
for pno, page in enumerate(doc):
    for info in page.get_image_info(xrefs=True):
        x = info["xref"]
        if not x: continue
        pix = fitz.Pixmap(doc, x)
        if pix.n - pix.alpha >= 4: pix = fitz.Pixmap(fitz.csRGB, pix)
        name = f"p{pno+1}_y{int(info['bbox'][1]):04d}_x{int(info['bbox'][0]):03d}.png"
        pix.save(f"{out}/{name}")
        rows.append((pno+1, [round(v) for v in info["bbox"]], pix.width, pix.height, name))
for r in rows: print(*r)
