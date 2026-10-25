// Usage: node render.cjs <file.html> [more.html ...]
// Renders each HTML file to a PNG beside it. Size comes from <meta name="canvas" content="1080x1350">
// (default 1080x1350). Renders at 2x then the PNG is written at 2x; export.py downsamples.
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const files = process.argv.slice(2);
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  for (const f of files) {
    const abs = path.resolve(f);
    const html = fs.readFileSync(abs, 'utf8');
    const m = html.match(/<meta name="canvas" content="(\d+)x(\d+)"/);
    const w = m ? +m[1] : 1080, h = m ? +m[2] : 1440;
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await page.goto('file://' + abs, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    const out = abs.replace(/\.html$/, '@2x.png');
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: w, height: h } });
    const missing = await page.evaluate(() => [...document.images].filter(i => !i.complete || !i.naturalWidth).map(i => i.src));
    const fontsBad = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'error').map(f => f.family + ':' + f.status));
    console.log(JSON.stringify({ file: f, out, w, h, missingImages: missing, fontsNotLoaded: fontsBad }));
    await page.close();
  }
  await browser.close();
})();
