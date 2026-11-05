# How to build one Shop All concept (for builder agents)

You get one concept spec (Feed + Story). Build both images in HTML/CSS over pool photos, render them, look at them, fix them.

## Files
- Work in `<S>/shopall/build/<NO>/` (create it): `feed.html`, `story.html`, `jobs.json`.
- Render to `<S>/shopall/out/<NO>_feed.jpg` (1080x1350) and `<S>/shopall/out/<NO>_story.jpg` (1080x1920).
- Render command: `cd <S>/shopall/kit && node render.cjs <S>/shopall/build/<NO>/jobs.json`
  jobs.json: `[{"html":"<abs feed.html>","out":"<abs out jpg>","w":1080,"h":1350},{"html":"<abs story.html>","out":"…","w":1080,"h":1920}]`
- Every HTML starts with `<link rel="stylesheet" href="file://<S>/shopall/kit/kit.css">` and `<body class="feed">` / `<body class="story">`.
- Photos: `file://<S>/shopall/pool/...` absolute URLs. Use CSS `background-image` with `background-size/position`, or `<img>` with `object-fit:cover; object-position`. Crop in to make the jewellery large: a piece the viewer cannot see is a wasted tile. Check pool.json "size" and the photo itself before choosing a crop.
- If you need a cut-out or a pixel measurement, use Python with PIL (`python3 -I`), writing any derived image into your build folder. Never recolour, repaint or warp the jewellery.

## Craft bar (what the judges will check)
1. **Stops the thumb in half a second**: one dominant thing (a face of type, a huge jewel, a surprising format). Not a busy collage of equals.
2. **The jewellery reads**: in every tile or photo, the piece is large, sharp and correctly coloured. Grid tiles at least 300 px; crop each listing photo to the piece, not the face.
3. **Type is legible on a phone**: nothing below 26 px; headline 60-140 px; enough contrast (use a solid or 90% paper panel, never text over busy detail).
4. **Story safe zone**: all text and the logo between y=270 and y=1500. The photo can run full bleed.
5. **One NAIRA logo** (logo_ink on light, logo_white on dark), 220-320 px wide, clear of other things.
6. **Honest and exact**: only the words in the spec (you may fix typos and tighten; record changes); prices exactly as in pool.json; obey every ban in BRIEF.md. No fake app logos, no fake comments, no fake ratings.
7. **Finished**: aligned edges, consistent margins (60-72 px), no text touching the jewellery, no overlaps, no cut-off letters, nothing accidental. Lo-fi formats are deliberately rough but still composed.
8. **Brand**: cream paper / ink / gold / sage world, Velista + Cormorant + Jost by default; handwriting (Kalam/Caveat/Marker) only where the format calls for it.

## Loop
Render → open both JPGs with Read → list every defect against the bar above → fix → render again. Do at least two looks. Stop when you would put ₹100 of your own money on it, or after four rounds; report anything still wrong.
