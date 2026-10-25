// Usage: node reel.cjs <page.html> <seconds> <out.mp4> [fps=30]
// The page animates with CSS @keyframes / Web Animations (any delays, any durations). Each frame, every
// animation in the document is paused and seeked to t, then the 1080x1920 viewport is captured and piped
// to ffmpeg (H.264 High, yuv420p, +faststart, ~6 Mbps): the format Instagram Reels takes cleanly.
// Optional: the page may define window.atTime = (ms) => {...} for anything CSS cannot express.
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
(async () => {
  const [page_, secs, out, fpsArg] = process.argv.slice(2);
  const fps = +(fpsArg || 30), total = Math.round(+secs * fps);
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(page_), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-',
    '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-b:v', '6M', '-maxrate', '8M', '-bufsize', '12M',
    '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < total; i++) {
    const t = (i / fps) * 1000;
    await page.evaluate((t) => {
      for (const a of document.getAnimations()) { a.pause(); a.currentTime = t; }
      if (window.atTime) window.atTime(t);
    }, t);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log(JSON.stringify({ out, frames: total, fps }));
})();
