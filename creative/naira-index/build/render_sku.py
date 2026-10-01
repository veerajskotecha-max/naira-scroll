import asyncio, sys
import pymupdf as fitz
from pathlib import Path
from playwright.async_api import async_playwright
K = Path(__file__).resolve().parent
bleed = "--bleed" in sys.argv
SRC = K / ("index-bleed.html" if bleed else "index.html")
PDF = K / "out" / ("naira-petite-index-A4-PRINT-3mm-bleed.pdf" if bleed else "naira-petite-index-A4.pdf")
PDF.parent.mkdir(exist_ok=True)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = await b.new_page()
        await pg.goto(SRC.as_uri(), wait_until="networkidle")
        await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
        await pg.pdf(path=str(PDF.with_suffix('.tmp.pdf')), prefer_css_page_size=True, print_background=True)
        await b.close()
asyncio.run(main())
doc = fitz.open(PDF.with_suffix('.tmp.pdf'))
doc.set_metadata({"title": "Naira Petite · The Petite Index", "author": "Naira", "subject": "Every Naira Petite listing on one A4 page, 1 October 2026", "creator": "Naira", "producer": "Naira"})
if bleed:
    mm = 72 / 25.4; r = doc[0].rect
    doc[0].set_bleedbox(r); doc[0].set_trimbox(fitz.Rect(3 * mm, 3 * mm, r.width - 3 * mm, r.height - 3 * mm))
doc.save(PDF, garbage=4, deflate=True); PDF.with_suffix('.tmp.pdf').unlink()
doc = fitz.open(PDF)
if not bleed:
    doc[0].get_pixmap(dpi=int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 150).save(K / "out" / "preview.png")
bad = [sp['font'] for b in doc[0].get_text("dict")["blocks"] for l in b.get("lines", []) for sp in l["spans"] if 'Liberation' in sp['font'] or 'DejaVu' in sp['font']]
print(PDF.name, round(PDF.stat().st_size / 1e6, 2), "MB", f"{doc[0].rect.width / 72 * 25.4:.1f}x{doc[0].rect.height / 72 * 25.4:.1f} mm", "fallback fonts:", bad)
