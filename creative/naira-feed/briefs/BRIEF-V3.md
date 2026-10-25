# VARIATION 3 · the motion feed (brief addendum, 25 Oct 2026)

The owner, after seeing the plan for options A and B: "Make variation 3 next and it should be better than both.
Think with what you know and be creative, go all out. Maybe make motion graphic posts. Make this variation 3 a
separate artifact and deeply done, take all the tokens you need. Think 10/10."

Everything in BRIEF.md still binds (read it first, and the research it lists). This file adds the V3 bar.

## The bar
- Better than BOTH options A and B. A and B are being chosen from four proposals in this folder
  (proposal-couture-scrapbook.json "The Fitting Book", proposal-indian-pop.json "MANGAL",
  proposal-retro-print.json "The Naira Reissue / FLOWER BRAND", proposal-free-best.json "Naira Matching Centre").
  Read all four. If briefs/judge-*.json and briefs/selection.json exist when you start (or appear while you
  work), read them: they say what the judges loved, what they flagged, and which two became A and B. V3 must
  not be a re-skin of either; it may absorb their best insights.
- MOTION-FIRST. Every one of the 12 posts moves. Instagram treats every feed video as a Reel; a carousel may
  hold video slides. So each post is either a Reel (1080×1920, 6–20 s) with a designed cover, or a carousel
  whose slides include short motion loops (1080×1440 video slides) and stills.
- 10/10 means: a stranger names the idea in three seconds; every tile is a piece of design worth saving;
  the motion is crafted and calm (the owner tuned the 3D box to a 35 s turn and the flower to 10 s, and
  sent back fast or jittery motion; no lyrics on screen), with one witty, true, Indian idea per post; and the
  grid of 12 covers is itself a composition, readable at 391×521 per tile.

## Motion production reality (what we can actually render)
- Each motion piece is an HTML page animated with CSS @keyframes / Web Animations / SVG
  (stroke-dashoffset line drawing, masks and clip-paths, 3D CSS transforms for doors, drawers, shutters, flaps,
  parallax layers, kinetic type, cut-out pieces moving with soft shadows, light and glint sweeps, petals,
  paper folds). tools/reel.cjs seeks every animation to each frame and pipes 30 fps to ffmpeg (H.264, +faststart).
  Hand-drawn feel comes from SVG line art and from AI-illustrated plates split into LAYERS.
- AI illustration budget for V3: up to ~25 generations (gpt_image_2_5 quality medium 2k ≈ 1 credit; use
  background "transparent" for layer elements; nano_banana_pro 2k ≈ 2 credits for painted plates). Design
  the plates as layers you can animate (background / midground / foreground objects separately). Never generate
  jewellery, faces or text.
- Jewellery is always the real photographed piece: BiRefNet cut-outs in cutouts/ (README.md lists 75+ with
  variants), and real photos/plates in assets/ (research/assets-*.md).
- Reel covers: design each cover as a still frame (1080×1920) whose centre 1080×1440 (y 240–1680) is the grid
  tile. Every reel ends on an end card: piece name, live price (Jost), nairaflore.com, the series lockup.
- Sound: Instagram's in-app library (no lyrics, sober instrumental/ambient) — give a direction per reel and,
  where useful, a list of 2–4 sound effects (timed) we could add.
