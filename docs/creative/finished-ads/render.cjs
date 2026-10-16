// Renders each ad page to PNG at its exact pixel size. Usage: node render.cjs <dir> <id>:<width>:<height> ...
const { chromium } = require('playwright');
(async () => {
  const [, , dir, ...jobs] = process.argv;
  const browser = await chromium.launch();
  for (const job of jobs) {
    const [id, w, h] = job.split(':');
    const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
    await page.goto(`file://${dir}/${id}.html`);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(120);
    await page.screenshot({ path: `${dir}/${id}.png` });
    await page.close();
  }
  await browser.close();
})();
