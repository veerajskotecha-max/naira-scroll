// Renders each {html, out, w, h} job in jobs.json to a JPEG at its exact pixel size. Usage: node shot.cjs jobs.json
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch();
  for (const j of jobs) {
    const p = await b.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 1 });
    await p.goto('file://' + j.html, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(150);
    await p.screenshot({ path: j.out, type: 'jpeg', quality: 93 });
    await p.close();
    console.log('ok', j.out.split('/').pop());
  }
  await b.close();
})();
