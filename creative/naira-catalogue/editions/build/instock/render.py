"""catalogue-<theme>[-bleedN].html -> out/*.pdf (Chromium), then metadata, trim/bleed boxes and page previews.
Usage: python3 render.py <apricot|lilac|sage> [bleed_mm]. Also reports any price card whose text overflows its box."""
import asyncio, sys, json
import pymupdf as fitz
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
theme = sys.argv[1]
BL = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
SRC = ROOT / (f"catalogue-{theme}-bleed{BL:g}.html" if BL else f"catalogue-{theme}.html")
OUT = ROOT / "out"; OUT.mkdir(exist_ok=True)
PDF = OUT / (f"naira-petite-{theme}-edition-PRINT-{BL:g}mm-bleed.pdf" if BL else f"naira-petite-{theme}-edition.pdf")
CHROME = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"

CHECK = """() => {
  const bad = [];
  document.querySelectorAll('.ptext').forEach(e => {
    if (e.scrollHeight > e.clientHeight + 1) bad.push(['tall', e.dataset.h, e.scrollHeight - e.clientHeight]);
    e.querySelectorAll('.pprice').forEach(x => { if (x.scrollWidth > e.clientWidth + 1) bad.push(['wide', e.dataset.h, x.scrollWidth - e.clientWidth]); });
  });
  const mm = 96 / 25.4, low = [];
  document.querySelectorAll('.trim').forEach((t, i) => {
    const top = t.getBoundingClientRect().top;
    t.querySelectorAll('.ptext, .index, .key, .guide').forEach(e => {
      const b = (e.getBoundingClientRect().bottom - top) / mm;
      if (b > (e.matches('.ptext') ? 284.5 : 281)) bad.push(['low', i + 1, e.dataset.h || e.className, +b.toFixed(1)]);
      if (e.matches('.index, .key, .guide')) low.push([i + 1, e.className.replace('abs ', ''), +b.toFixed(1)]);
    });
  });
  const fonts = [...document.fonts].filter(f => f.status !== 'loaded').map(f => f.family + ' ' + f.weight + ' ' + f.status);
  return {bad, low, fonts, pages: document.querySelectorAll('.page').length};
}"""


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        pg = await b.new_page()
        await pg.goto(SRC.as_uri(), wait_until="networkidle")
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(500)
        res = await pg.evaluate(CHECK)
        print("check:", json.dumps(res))
        await pg.pdf(path=str(PDF.with_suffix(".tmp.pdf")), prefer_css_page_size=True, print_background=True)
        await b.close()

asyncio.run(main())
doc = fitz.open(PDF.with_suffix(".tmp.pdf"))
name = theme.capitalize()
doc.set_metadata({"title": f"Naira Petite · The Catalogue · The {name} Edition",
                  "author": "Naira", "subject": f"Demi-fine jewellery catalogue, the {name} camp, every piece in stock",
                  "keywords": f"Naira, Naira Petite, demi-fine jewellery, catalogue, lookbook, price list, {name}, nairaflore.com",
                  "creator": "Naira", "producer": "Naira"})
if BL:
    mm = 72 / 25.4
    for page in doc:   # top-left coordinates, as laid out in the HTML: trim exactly A4 at (BL, BL), bleed BL all round
        page.set_bleedbox(fitz.Rect(0, 0, (210 + 2 * BL) * mm, (297 + 2 * BL) * mm))
        page.set_trimbox(fitz.Rect(BL * mm, BL * mm, (BL + 210) * mm, (BL + 297) * mm))
doc.save(PDF, garbage=4, deflate=True)
PDF.with_suffix(".tmp.pdf").unlink()
doc = fitz.open(PDF)
if not BL:
    pv = ROOT / "prev" / theme
    pv.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(doc):
        page.get_pixmap(dpi=90).save(pv / f"p{i + 1:02d}.png")
print(PDF.name, len(doc), "pages", round(PDF.stat().st_size / 1e6, 1), "MB",
      f"{doc[0].rect.width / 72 * 25.4:.1f} x {doc[0].rect.height / 72 * 25.4:.1f} mm",
      f"| trim {doc[0].trimbox.width / 72 * 25.4:.2f} x {doc[0].trimbox.height / 72 * 25.4:.2f} mm" if BL else "")
