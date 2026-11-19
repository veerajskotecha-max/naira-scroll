// Renders ad pages to JPG at their exact size once fonts and images have loaded, and checks them.
// Usage: node render.cjs <page.html> <out.jpg> [<page.html> <out.jpg> ...]
// Size comes from the page: 1080x1350 by default, 1080x1920 when <body class="story">.
// Prints one JSON line per page:
//   failed   - requests that failed (missing image or font)
//   overflow - [data-fit] elements whose content overflows them
//   fallback - text drawn with a font that is not one of the kit's web fonts (system fallback), with the text
//   textShare - share of the canvas covered by text boxes (glyph line boxes, 8 px grid), 0-1
//   outside  - text boxes outside the safe area (Feed x 72-1008, y 84-1266; Story y 270-1250)
//   minFont  - smallest computed font size of any visible text, px
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const a = process.argv.slice(2), jobs = [];
  for (let i = 0; i + 1 < a.length; i += 2) jobs.push({ html: path.resolve(a[i]), out: path.resolve(a[i + 1]) });
  const browser = await chromium.launch();
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
    const errs = []; page.on('requestfailed', r => errs.push(r.url() + ' ' + (r.failure() || {}).errorText));
    page.on('response', r => { if (r.status() >= 400) errs.push(r.status() + ' ' + r.url()); });
    await page.goto('file://' + j.html);
    const story = await page.evaluate(() => document.body.classList.contains('story'));
    if (story) await page.setViewportSize({ width: 1080, height: 1920 });
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))));
    await page.waitForTimeout(150);
    const H = story ? 1920 : 1350;
    const info = await page.evaluate(({ H, story }) => {
      const over = [...document.querySelectorAll('[data-fit]')].filter(e => e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1).map(e => e.dataset.fit);
      const G = 8, cols = Math.ceil(1080 / G), rows = Math.ceil(H / G), grid = new Uint8Array(cols * rows);
      const outside = []; let minFont = 999;
      const safe = story ? { x0: 0, x1: 1080, y0: 270, y1: 1250 } : { x0: 72, x1: 1008, y0: 84, y1: 1266 };
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      for (let n; (n = walker.nextNode());) {
        if (!n.textContent.trim()) continue;
        const el = n.parentElement, cs = getComputedStyle(el);
        if (cs.visibility === 'hidden' || cs.display === 'none' || +cs.opacity === 0) continue;
        minFont = Math.min(minFont, parseFloat(cs.fontSize));
        const r = document.createRange(); r.selectNodeContents(n);
        for (const b of r.getClientRects()) {
          if (b.width < 1 || b.height < 1) continue;
          if (b.left < safe.x0 - 1 || b.right > safe.x1 + 1 || b.top < safe.y0 - 1 || b.bottom > safe.y1 + 1)
            outside.push(n.textContent.trim().slice(0, 30));
          for (let y = Math.max(0, Math.floor(b.top / G)); y < Math.min(rows, Math.ceil(b.bottom / G)); y++)
            for (let x = Math.max(0, Math.floor(b.left / G)); x < Math.min(cols, Math.ceil(b.right / G)); x++) grid[y * cols + x] = 1;
        }
      }
      let on = 0; for (const v of grid) on += v;
      return { over, textShare: +(on / grid.length).toFixed(3), outside: [...new Set(outside)], minFont: minFont === 999 ? null : minFont };
    }, { H, story });
    // Fallback check: ask the renderer which fonts drew each text-bearing element.
    const cdp = await page.context().newCDPSession(page);
    await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
    const { root } = await cdp.send('DOM.getDocument', { depth: -1 });
    const fallback = [], seen = new Set();
    const walk = async n => {
      if (n.nodeType === 1 && (n.children || []).some(c => c.nodeType === 3 && c.nodeValue.trim())) {
        try {
          const { fonts } = await cdp.send('CSS.getPlatformFontsForNode', { nodeId: n.nodeId });
          for (const f of fonts) if (!f.isCustomFont) {
            const t = (n.children.find(c => c.nodeType === 3) || {}).nodeValue.trim().slice(0, 30), k = f.familyName + t;
            if (!seen.has(k)) { seen.add(k); fallback.push({ family: f.familyName, glyphs: f.glyphCount, text: t }); }
          }
        } catch (e) {}
      }
      for (const c of n.children || []) await walk(c);
    };
    await walk(root);
    await page.screenshot({ path: j.out, type: 'jpeg', quality: 92 });
    const failed = errs.filter(e => !e.startsWith('file://' + j.html + ' '));
    console.log(JSON.stringify({ out: path.relative(process.cwd(), j.out), size: story ? '1080x1920' : '1080x1350', failed,
      overflow: info.over, fallback, textShare: info.textShare, outside: info.outside, minFont: info.minFont }));
    await page.close();
  }
  await browser.close();
})();
