"""catalogue.html -> out/*.pdf (Chrome), then metadata, trim/bleed boxes and page previews (PyMuPDF)."""
import asyncio, sys
import pymupdf as fitz
from pathlib import Path
from playwright.async_api import async_playwright
C = Path(__file__).resolve().parent
bleed = "--bleed" in sys.argv
SRC = C / ("catalogue-bleed.html" if bleed else "catalogue.html")
PDF = C / "out" / ("naira-petite-catalogue-PRINT-3mm-bleed.pdf" if bleed else "naira-petite-catalogue.pdf")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = await b.new_page()
        await pg.goto(SRC.as_uri(), wait_until="networkidle")
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(500)
        await pg.pdf(path=str(PDF.with_suffix(".tmp.pdf")), prefer_css_page_size=True, print_background=True)
        await b.close()

asyncio.run(main())
doc = fitz.open(PDF.with_suffix(".tmp.pdf"))
doc.set_metadata({"title": "Naira Petite · The Catalogue · Volume One",
                  "author": "Naira", "subject": "Demi-fine jewellery catalogue, festive 2026",
                  "keywords": "Naira, Naira Petite, demi-fine jewellery, catalogue, price list, nairaflore.com",
                  "creator": "Naira", "producer": "Naira"})
if bleed:
    mm = 72 / 25.4
    for page in doc:
        r = page.rect
        page.set_bleedbox(r)
        page.set_trimbox(fitz.Rect(3 * mm, 3 * mm, r.width - 3 * mm, r.height - 3 * mm))
doc.save(PDF, garbage=4, deflate=True)
PDF.with_suffix(".tmp.pdf").unlink()
doc = fitz.open(PDF)
if not bleed:
    (C / "prev").mkdir(exist_ok=True)
    for i, page in enumerate(doc):
        page.get_pixmap(dpi=90).save(C / "prev" / f"p{i+1:02d}.png")
print(PDF.name, len(doc), "pages", round(PDF.stat().st_size / 1e6, 1), "MB",
      f"{doc[0].rect.width / 72 * 25.4:.1f} x {doc[0].rect.height / 72 * 25.4:.1f} mm")
