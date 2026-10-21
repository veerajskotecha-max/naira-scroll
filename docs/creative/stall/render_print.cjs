// Renders each poster page to an exact-size PDF (24 × 36 in, from 96 px/in layout), a 150 ppi JPG and a 600 px preview.
// Usage: node render_print.cjs <workdir> <outdir> <name> ...   (reads <workdir>/<name>.html)
const { chromium } = require('playwright');
(async () => {
  const [, , dir, out, ...names] = process.argv;
  const browser = await chromium.launch();
  for (const n of names) {
    for (const [scale, file] of [[1, null], [150 / 96, `${out}/${n}.jpg`], [600 / 2304, `${out}/previews/${n}.jpg`]]) {
      const ctx = await browser.newContext({ viewport: { width: 2304, height: 3456 }, deviceScaleFactor: scale });
      const page = await ctx.newPage();
      await page.goto(`file://${dir}/${n}.html`);
      await page.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(i => i.decode().catch(() => {}))); });
      await page.waitForTimeout(150);
      if (!file) await page.pdf({ path: `${out}/${n}.pdf`, width: '24in', height: '36in', printBackground: true, pageRanges: '1' });
      else await page.screenshot({ path: file, type: 'jpeg', quality: file.includes('previews') ? 85 : 92 });
      await ctx.close();
    }
  }
  await browser.close();
})();
