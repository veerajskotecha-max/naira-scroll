// Renders ad pages to JPG at their exact size once fonts and images have loaded.
// Usage: node render.cjs <page.html> <out.jpg> [width height] ...   (pairs repeat: html out [w h] html out [w h])
// Pages link ../../kit/kit.css (fonts, brand tokens) and set their own layout; default size 1080x1350 (Meta feed 4:5).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const a = process.argv.slice(2), jobs = [];
  for (let i = 0; i < a.length;) {
    const html = a[i++], out = a[i++]; let w = 1080, h = 1350;
    if (a[i] && /^\d+$/.test(a[i])) { w = +a[i++]; h = +a[i++]; }
    jobs.push({ html: path.resolve(html), out: path.resolve(out), w, h });
  }
  const browser = await chromium.launch();
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 1 });
    const errs = []; page.on('requestfailed', r => errs.push(r.url()));
    await page.goto('file://' + j.html);
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))));
    await page.waitForTimeout(120);
    const over = await page.evaluate(() => [...document.querySelectorAll('[data-fit]')].filter(e => e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1).map(e => e.dataset.fit));
    await page.screenshot({ path: j.out, type: 'jpeg', quality: 92 });
    console.log(JSON.stringify({ out: j.out, failed: errs, overflow: over }));
    await page.close();
  }
  await browser.close();
})();
