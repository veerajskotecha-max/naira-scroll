# Naira motion cookbook (tested 25 Oct 2026)

All paths relative to the feed root `FEED=/tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed`.

## Render
- Reel: `node tools/reel.cjs page.html <seconds> out.mp4 [fps=30]` — 1080×1920, H.264 High, yuv420p, +faststart.
  Every CSS animation / Web Animation in the page is paused and seeked to t each frame, so timing is exact and
  infinite loops (flicker, sway) work. Optional `window.atTime = ms => {}` for anything CSS cannot express.
- Still (cover, carousel slide): `node tools/render.cjs page.html` → `page@2x.png` (2×), then
  `python3 tools/export.py page@2x.png` → `.jpg` (1080×1440), `-45.jpg` (4:5 crop) and `-thumb.png` (391×521).
  Size from `<meta name="canvas" content="1080x1920">` (default 1080×1440).
- Video carousel slide (1080×1440 loop): build the page at 1080×1440 and run reel.cjs with a modified viewport,
  or render 1080×1920 and crop with ffmpeg: `ffmpeg -i in.mp4 -vf crop=1080:1440:0:240 -c:v libx264 -pix_fmt yuv420p -movflags +faststart out.mp4`.
- Check motion by pulling frames: `ffmpeg -ss 2.4 -i out.mp4 -frames:v 1 f.jpg` and VIEW them (strip several
  timestamps side by side). Never ship a reel you have not looked at frame by frame at its key beats.
- Renderers launch Chromium with --allow-file-access-from-files, so CSS masks/SVG images from local files work.

## Files
- `kit/tokens.css` fonts + palette; `kit/post-base.css` canvas helpers; `kit/motion/motion.css` the keyframes.
- `kit/motion/demo.html` (shopfront: line-drawn awning, shutter roll, tube light, piece drop, glint, type-up,
  diya flicker) and `kit/motion/demo-box.html` (CSS 3D box: sleeve with print, drawer slides out, pop-up
  layers stand). Both render cleanly; copy from them.

## Tested techniques (motion.css)
| effect | how | notes |
|---|---|---|
| fade / rise / drop / scale in | `.m` + `animation-name` | drop-in uses `--ease-drop` (one small overshoot) |
| type line reveal | `<span class=line><span class=m style="display:inline-block;animation-name:type-up">` | stagger 0.12–0.2 s per line |
| rolling shutter | `.shutter` + `shutter-up 2.2s var(--ease-inout)` | put it last inside an `overflow:hidden` opening |
| line drawing | SVG path `class="draw" pathLength="1"` + `animation:draw 1.6s` | stagger strokes; stroke-linecap round |
| gold glint on metal only | `<div class=glint style="--src:url(cutout.png)">` sized exactly like the img + `glint 1.4s` | masked by the cut-out alpha |
| iris / peephole | `iris-open` with `--ix --iy --ir` | the bioscope / moon / chalni reveal |
| wipes | `wipe-down`, `wipe-right` (clip-path inset) | |
| diya | `.flame` + `flicker 1.1s infinite`, `.glow` + `glow-breathe 2.4s infinite` | |
| tube light catching | `light-on 1.2s linear` | once only |
| sway | `sway 3s ease-in-out infinite`, transform-origin top | toran, tassel, kandil tail |
| petals / paper | `fall` with `--dx --rot`, 6–12 items | |
| push-in / drift | `push-in` ≤ 6%, `drift-x` | parallax: different speeds per layer |
| stamp landing | `stamp` | a seal pressed onto paper |
| doors / flaps | `door-open-left/right`, `flap-open` with parent `perspective:1600px` | |
| drawer / pop-up | see demo-box.html: `preserve-3d`, drawer `translateY`, pop-up `rotateX` from flat | 3D needs frame checks: faces can vanish if backface-visibility or rotation order is wrong |

## House rules of motion (owner-tuned)
- Calm. Entrances 0.8–1.4 s; holds ≥ 1.2 s on anything with words; end card holds ≥ 2.5 s.
- One hero movement per beat. No shake, no spin-for-fun, no whip pans, no strobe. A single overshoot max.
- Seamless loops where the post is a loop (last frame = first frame).
- On-screen words stay inside x 72–1008 and y 290–1630 (Reels UI covers the bottom ~300 px and the right edge
  icons from ~x 960 between y 1100–1700). The grid tile of a reel is y 240–1680.
- The jewellery is always a real photo cut-out; give it a soft contact shadow (`.cut` in post-base.css) and,
  at most once per reel, a glint.
- No lyrics on screen. Words are few, set in Velista caps / Cormorant italic / Jost.

## Indian scripts (kit/scripts.css, tested in Chromium 25 Oct)
Link `kit/scripts.css` after tokens.css. Families: 'Tiro Devanagari Marathi' (Marathi, in tokens.css),
'Tiro Devanagari Hindi', 'Noto Serif Gujarati', 'Tiro Bangla', 'Tiro Kannada', 'Tiro Telugu', 'Tiro Gurmukhi',
'Tiro Tamil', 'Noto Serif Malayalam', 'Noto Nastaliq Urdu'. Verified spellings (render/_test/scripts.jpg):
मंगळवार/मंगळ (mr) · मंगलवार/मंगल (hi) · મંગળવાર/મંગળ (gu) · মঙ্গলবার/মঙ্গল (bn) · ಮಂಗಳವಾರ/ಮಂಗಳ (kn) ·
మంగళవారం/మంగళ (te) · ਮੰਗਲਵਾਰ/ਮੰਗਲ (pa) · செவ்வாய்/மங்கலம் (ta; Tamil's Tuesday is not 'mangal') ·
ചൊവ്വ/മംഗളം (ml) · منگل (ur). Any other non-Latin string: render it, view it, and keep it only if certain.
