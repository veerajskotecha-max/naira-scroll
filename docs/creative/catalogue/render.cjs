// Renders HTML pages to JPEG at their exact size, in one browser. Usage: node render.cjs <dir> <id>:<width>:<height> ...
// Writes <dir>/<id>.jpg (quality 92). Pages load their images and fonts from file:// paths.
const { chromium } = require('playwright');
(async () => {
  const [, , dir, ...jobs] = process.argv;
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ deviceScaleFactor: 1 });
  for (const job of jobs) {
    const [id, w, h] = job.split(':');
    const page = await ctx.newPage();
    await page.setViewportSize({ width: +w, height: +h });
    await page.goto(`file://${dir}/${id}.html`);
    await page.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(i => i.decode().catch(() => {}))); });
    await page.waitForTimeout(60);
    await page.screenshot({ path: `${dir}/${id}.jpg`, type: 'jpeg', quality: 92 });
    await page.close();
  }
  await browser.close();
})();
