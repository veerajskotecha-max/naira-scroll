# For each embedded PI image, prints the text that sits in the same row band: pi_rows.py PDF
import sys, pymupdf
doc = pymupdf.open(sys.argv[1])
for pno, page in enumerate(doc):
    words = page.get_text("words")
    for info in sorted(page.get_image_info(xrefs=True), key=lambda i: i["bbox"][1]):
        x0, y0, x1, y1 = info["bbox"]
        t = " ".join(w[4] for w in sorted(words, key=lambda w: (w[1], w[0])) if w[1] >= y0 - 8 and w[3] <= y1 + 8)
        print(f"p{pno+1} y{int(y0)}: {t[:230]}")
