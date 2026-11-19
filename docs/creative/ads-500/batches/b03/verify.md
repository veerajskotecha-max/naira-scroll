# b03 picture verification (19 Nov 2026, about 19:30 UTC)

I checked each b03 picture in `pics/` against `brief.md` (the acceptance lists), `RULINGS.md` §4 (the sliding-window gate),
`build/study/products.md` and the reference photos in `build/refs/<handle>__*.jpg`. Zoomed crops are in `tmp/`.
`tmp/gate200.jpg` is the 200 px gate sheet. It shows every try, Feed window on top and Story below.

## Result

| Id | Product | Verdict | Deciding reason |
|---|---|---|---|
| b03-1 | Brushed Gold Huggies | **pass-with-notes** (try 1) | The construction, brushed finish, pose and ratio (1.41) match the pack. The extent is 502 Feed px (506 allowed), so it fits at **P 56**. The pair is **74.5%** of the width (58–70% asked), and each huggie is 31.4% and 39.4% (25–30% asked). That is 1.06× the band. The size tag declares the magnification. The floor shows a soft, diffuse reflection glow under the card. |
| b03-2 | Cushion Halo Ring | **pass-with-notes** (try 1) | It is an almost exact copy of the macro ref: 4 claws, a single-row cushion halo, shoulder pavé, cool silver tone. The ratios pass (0.74 and 1.74). The extent is 483 Feed px, so it fits at **P 62**. The shoulder span is **76%** of the width (52–66% asked), which is 1.15× the band, with the halo at 43.8%. The size tag is required (39 px/mm). In the Story, the ring top is at 719, so the brief's fallback applies (drop the line). |
| b03-3 | Halo Curve Ring | **pass-with-notes** (try 2) | **Try 1 failed on extent.** The ring stood tall (width ÷ height 1.0 against the ref's 1.24) at 506 Feed px. With its long side shadow it was 561 px (420 allowed, and 550 at the RULINGS gate). **Try 2** copies the cube pose, and every logged ratio passes. Ring plus shadow is 430 Feed px. That is 10 px over the band, but the layout fits at **P 63**. It renders at 16.8 px/mm (about life size), so **drop the "Shown magnified" tag**. The notes: a soft wall/floor seam, and a mid-tone sage under the card that needs a scrim. |
| b03-4 | Monochrome Enamel Hoops | **dropped** (both tries fail) | Construction and float are right on both tries: one black and one white stripe, three rails, an open C, gap 0.41–0.43× the hoop. But hoops plus shadows run **693 Feed px (try 1) and 712 (try 2)** against 550 allowed. No P fits the headline, beat, float and card together, and at P 50 the card covers the shadows. A size ask at about a third of the first ask did not shrink anything (try 2 is larger). A zero-credit **card-only rescue at P 100** fits the RULINGS A1 gate (84–930). That is the lead's call (below). |
| b03-5 | Pearl Double Halo Studs | **pass-with-notes** (try 1) | Two pavé bands, an open gap with 4 bridges, a softened-square outer band, bright silver tone, an identical pair. The ratios pass (0.59 and 0.76). The pair is 56.4% of the width, at 16.4 px/mm (no tag). The extent is 419 Feed px, so it fits at **P 56**. 75% of the frame is near-black. The notes: the pearl reads faintly blush (a* 7 against the ref's 2–4), the pool edge is soft, not crisp, and the pavé reads as fine glitter. |

**Kept: 4 of 5** (b03-1, b03-2, b03-3 try 2, b03-5), all product-only. **Dropped: b03-4**, the crazy slot. It can still be rescued at zero credits as a card-only Feed.

**Credits.** The balance read 18.46 before my one `generate_image_batch` call (2 jobs: b03-3 and b03-4) and **14.46** after it, so
each picture cost 2 credits. Both jobs were served as `nano_banana_2`, although `nano_banana_pro` (2k, 9:16, refs as `image_references`) was
requested. `jobs.json` is updated: try-1 files are kept as `pics/b03-3_try1.png` and `pics/b03-4_try1.png`, and each entry records
`try1`, `regenerated`, `served_model`, `credits` and `verdict`.

**Coordinates.** The source is 1536 × 2752, displayed at 1080 × 1935.
- Feed y = src_y × 0.703125 − T, with T = 5.85 × P.
- Story y = src_y × 0.703125 − 7.5.
- x = src_x × 0.703125.

**Size growth this batch (prompt ask vs. render).**

| Slot | Height asked (share of frame) | Height rendered | Growth | Width asked | Width rendered | Growth |
|---|---|---|---|---|---|---|
| b03-1 | 1/6 (16.7%) | 24.9% | 1.5× | under half (about 45%) | 74.5% | 1.65× |
| b03-2 | 1/7 (14.3%, halo) | 24.6% | 1.7× | under half (about 45%) | 76% | 1.7× |
| b03-3 try 1 | 1/7 | 26.2% | 1.8× | over a third (about 36%) | 48% | 1.3× |
| b03-3 try 2 | 1/10 | 21.2% | 2.1× | a third | 46.9% | 1.4× |
| b03-4 try 1 | 1/9 (11.1%) | 20.5% | 1.85× | a third | 60.7% | 1.8× |
| b03-4 try 2 | 1/12 (8.3%) | 22.1% | 2.65× | a quarter | 63.5% | 2.5× |
| b03-5 | 1/8 (12.5%) | about 16.7% (face) | 1.3× | under half | 56.4% | 1.25× |

---

## b03-1 · Brushed Gold Huggies · A4 Monument Macro (the new move) · pass-with-notes

Job `b856168b-fe23-42eb-9881-e1082d6c94d1` (try 1, kept). Zooms: `tmp/b03-1_pair.jpg`, `b03-1_leftface.jpg`, `b03-1_opening.jpg`,
`b03-1_floor.jpg`; reference zoom `tmp/ref_brushed_pack_zoom.jpg`.

**Measurements (src px)**
- **Extent (first): pass.**
  - Pair x 227–1372, y 1074–1760. The contact shadows end at y 1788 (L 17–21 band at 1728–1784).
  - The extent is 1074–1788 = 714 src = **502 Feed px** (506 allowed).
  - Some P puts it inside Feed 424–930 only for **P 55.9–56.6**. **Use P 56, T 327.6.** The pair then sits at Feed y 428–930.
- **Pose: pass.** Both huggies are upright and whole. The left one is face-on; the right one is turned three-quarters with its opening and the inside of the band showing. Both are sharp.
- **Finish: pass.**
  - Soft brushed satin with very fine parallel lines (vertical on the left face, as in the pack's left huggie) and one broad soft sheen.
  - Never mirror, ridged, hammered or stone-set. Zero stones. An identical pair.
  - Note: the three-quarter view shows the inner clicker seam and hinge pin at the top and bottom of the opening, which the pack never shows. It is plausible hardware for a hinged huggie, and the outside stays seamless.
- **Ratio inside the piece (logged).** Left huggie height ÷ face width = 681 ÷ 482 = **1.41** (1.25–1.5 allowed; pack 1.37). Pass.
- **Width share (logged, the new-move metric).**
  - Left huggie x 227–709 = **31.4%** of the width (Feed x 160–499).
  - Right huggie x 767–1372 = **39.4%** (Feed x 539–965). It is wider because the three-quarter barrel shows its depth.
  - **Pair 74.5%** (Feed x 160–965). The brief asked 25–30% each and 58–70% for the pair.
  - The pair is centred on Feed x 562 (22 px right of centre).
  - The outer edges (160 and 965) are outside the asked x 170–910. The left face starts at 160 and the opening spans Feed x about 752–935, so both cross the x 216–864 column.
  - **Accepted as a note:** the overshoot is 1.06× the band max, the extent fits, and every Feed and Story text block fits (below). Regenerating risked the finish and pose for a marginal gain.
- **Scale (logged).** 681 src px for 14 mm = 48.6 src px/mm = **34.2 Feed px/mm** (29–32 expected), about 2.1× on a phone. The size tag "Shown magnified · about 14 mm tall" is required.
- **Colour (logged).**
  - Gold face Lab 51–80 / a 4–8 / b 16–21 (hue 68–76°, warm-neutral, not orange, grey or greenish).
  - Plum wall Lab 18 / 18 / −3 (hue 351°), darker and cooler than the gold. **ΔE76 42–66.** The pair is the only gold.
- **Floor: note.**
  - No mirror image of the huggies, no water, no props.
  - The satin glaze does throw a **soft, diffuse reflection glow**: two blurred vertical streaks under the huggies, src y 1800–2200, Feed y about 944–1220 at x about 200–480 and 600–900. It reaches L 108–112 at Feed 980–1050, against a floor mean of L 76.
  - It is not part of the subject's extent, but it sits under the card.
- **Light rendered:** an L1-like warm key from the left with one broad sheen, short contact shadows to the right, and a soft front fill. It is softer than a true rake, but the brush lines read.
- **Negatives: pass.** No star glints, flare, text or extra jewellery.
- **200 px gate: pass.** The gold pair lands first, and the opening reads as an earring.

**Calm zones and layout notes (P 56, T 327.6)**
- **Feed (1080 × 1350).**
  - Subject box: x 160–965, y 428–930.
  - **Headline and beat (y 96–369, left 72) and size tag (x 629–1008, y 304–400): calm plum wall**, rgb (66,33,48), L 41 (p5–p95 37–45). Bone is about 11:1.
  - The size tag clears the pair by **28 px** (24 needed).
  - **Card 940–1252: plum floor**, rgb (107,68,73), L 76 (p95 98), with the reflection streaks. Bone is about 6:1, or about 5:1 on the streaks.
  - **Use the brief's plum scrim** sampled from the floor (0 at 860 → .55 at 1350, rgb about 92,56,66). It mutes the streaks. Keep it below 930 so it never touches the contact shadows.
  - **Type must NOT go** over x 160–965, y 428–930, or the opening (x 750–940, y 450–900).
- **Story (1080 × 1920).**
  - Pair at Story y 748–1250. Text must end by 724.
  - The brief's stack ends at 738, which is 14 px too low, so **set the headline at 72** (lines 346–486): name and price 506–562, offer 580–642, size tag 660–722, with a 26 px gap.
  - Moving the tag below the pair does not fit (it would end at 1336).
  - The wall behind the text (Story 0–740) is calm plum, L 42. Below the pair is floor with the soft glow (L 69), and no text goes there.

---

## b03-2 · Cushion Halo Ring · A1 Product Card (NAIRA10 cell) · pass-with-notes

Job `852c5553-7888-4baa-9a23-768ce82f8777` (try 1, kept). Zooms: `tmp/b03-2_halo.jpg`, `b03-2_lshoulder.jpg`,
`b03-2_rshoulder.jpg`; reference zoom `tmp/ref_cushion_macro_lshoulder.jpg`.

**Measurements (src px)**
- **Extent (first): pass.**
  - Ring x 177–1346, y 1033–1709 (the halo's bottom). The contact shadow ends at y 1720.
  - The extent is 687 src = **483 Feed px** (600 allowed; the RULINGS A1 gate allows 846).
  - **P 62, T 362.7** puts the ring at Feed y 364–847. Any P from 48 to 68 also fits.
- **Construction: pass. It is nearly a pixel-faithful copy of the macro ref.**
  - One round brilliant centre stone in **exactly 4** ball claws.
  - **One single-row cushion (rounded-square) halo**, never round, never two rows.
  - Pavé down each shoulder, which reads as a top row plus the shank's side row, exactly as in the macro ref.
  - Cool bright silver tone, never gold. The band's back is hidden behind the head.
- **Pose: pass.** The head is face-on, the shoulders run left and right, and the far (right) shoulder tip softens slightly.
- **Ratios inside the piece (logged).**
  - Centre stone ÷ halo width = 494 ÷ 671 = **0.74** (0.66–0.80; ref 0.76). Pass.
  - Shoulder span ÷ halo = 1169 ÷ 671 = **1.74** (1.5–1.9; ref 1.69). Pass.
- **Width share.**
  - Shoulder span x 177–1346 = **76.1%** (52–66% asked, target 60%). The halo x 434–1105 = **43.8%** (at least 30%). Pass.
  - Halo and claws are inside x 216–864 (Feed x 305–777). Pass.
  - The shoulder tips reach Feed x 124 and 946.
  - **Accepted as a note:** the overshoot is 1.15× the band max, it lies only in the soft shoulder tips, the halo is centred, and the extent and layout fit. A regeneration risked the documented halo morph on the best-evidence hero.
- **Scale (logged).** The halo is 671 src px for 12 mm = 55.9 src px/mm = **39.3 Feed px/mm** (28–34 expected), about 2.5× on a phone. The size tag "Shown magnified / halo about 12 mm" is required.
- **Light rendered:** L7. A soft warm wrap from the upper left with small round speculars and faint fire. No rays and no star glints; the star in the stone is its arrows-pattern facets, not a glint. Pass.
- **Ground.**
  - Cocoa backdrop rgb (131,94,75), L 100, and a cocoa block, tone on tone.
  - The block's lit top is a lighter tan strip, Feed y 852–914 (L about 155), just above the card. It is plain and less saturated than the ring's sparkle.
  - The block face below 920 is plain plaster, rgb (110,74,57), L 81.
- **Colour (logged).** Halo Lab 71 / 4 / 5 against backdrop Lab 43 / 13 / 17: **ΔE76 32**. The ring is the brightest, least saturated shape.
- **200 px gate: pass.** The ring is the first and brightest shape and reads as a halo ring.

**Calm zones and layout notes (P 62, T 362.7)**
- **Feed.**
  - Subject box: ring x 124–946, y 364–847. Halo x 305–777, y 364–839.
  - **Size tag** (382 × 96, right 72): its bottom must be at 340 (24 above the ring top at 364), so place it at **y 244–340, x 626–1008**. It sits on calm cocoa backdrop, L 100, where bone is about 4.6:1. That is fine at 30 px, but keep the 2-line tag at weight 500.
  - **Card at 940** on the plain block face, L 81, where bone is about 6:1. No scrim is needed. The lit tan strip (852–914) sits just above the wordmark, so do not move the card above 930.
  - **Type must NOT go** over x 124–946, y 364–914 (ring plus lit block top).
- **Story.**
  - Ring at Story y 719–1202 (halo x 305–777). The text must end by **695**.
  - The brief's stack ends at 710 and its rule needs the ring at 734 or lower, and the ring sits at 719. **Apply the fallback: drop the line**, so the logo is at 270–326, name 350–388, price 404–460, offer 478–540, and the size tag (two lines) 560–656. That leaves a 63 px gap.
  - The backdrop behind the text is calm cocoa, L 99.

---

## b03-3 · Halo Curve Ring · A8 Callout Anatomy · pass-with-notes (try 2)

Try 2: job `e9f5364c-4c82-4ba4-aca7-974ddd680165`, now `pics/b03-3.png`. Try 1: `8d7a6fa1-461e-4e8e-803f-4ff875a0879f`, kept as
`pics/b03-3_try1.png`. Zooms: `tmp/b03-3_ring.jpg` (try 1), `tmp/b03-3r_ring.jpg`, `tmp/b03-3r_tigereye.jpg` (try 2), and the ref
zoom `tmp/ref_halocurve_cube_zoom.jpg`.

**Try 1: FAIL on extent.**
- Construction was right: an open bypass of smooth round wire, an opaque banded faceted tiger eye, a faceted transparent champagne crystal, two unmatched stones, slim bezels.
- But the ring stood tall: x 431–1169 (48%), y 1027–1747, so width ÷ height = **1.0** against the cube ref's 1.24. Its height was 26.2% of the frame (1/7 asked).
- A long soft shadow ran right to the frame edge (to y 1825, x 1535).
- The ring alone was 506 Feed px; **ring plus shadow 561** (420 allowed for the callout layout; 550 at the RULINGS gate). The C3 callout and the size tag at Feed 828 would have overlapped the loop and the shadow.
- Light: a soft key from the left, not the asked L2 flash.

**Corrected prompt (try 2; ref slot 1 only, `ac8bad23-c21e-447f-801c-3ec328d118f6`, the cube):**

> Reference 1 is the authority on this exact ring; ignore its background and light. Vertical 9:16 jewellery macro photograph, 100 mm macro lens, camera about 35 degrees above the surface in a three-quarter high view: the Halo Curve Ring from the reference stands on its open band on a flat matte deep sage-green surface that sweeps up into a matching sage wall with no horizon line, centred in the frame. POSE, copy the reference exactly: the tiger eye sits on top, a little left of centre, its face tilted up toward the camera; the champagne crystal sits to its right and a little lower; the open loop of the band reaches out to the LEFT, well past the tiger eye's left edge, and curves down to the surface, so the whole ring reads clearly wider than it is tall, about 1.3 times as wide as it is tall; never stood up tall with the tiger eye stacked high above a small loop. FIDELITY: an open bypass ring of one smooth round 1.5 mm polished 18k PVD gold-tone wire, about 17 mm across inside, whose two ends pass each other and sit side by side, each holding one stone in a slim irregular gold-tone bezel: an opaque banded golden-brown tiger eye about 11.8 mm, a softly faceted cushion with a silky moving band of sheen, and a faceted transparent pale champagne crystal cushion a little smaller. Exactly two stones and they must stay unmatched, one opaque banded brown and one clear pale champagne, never two matching cushions, never a transparent or glassy tiger eye, never a halo of small stones, never a thick or flat band; the band stays open between the two ends. SCALE: the tiger eye is about eight times as wide as the wire is thick and about a third of the ring's full width. SIZE IN FRAME, the most important instruction: the ring is small in a big empty sage frame; its height is only about one tenth of the frame's height and its width about a third of the frame's width; everything above it is calm empty sage wall and everything below it is calm empty sage floor, and the ring stays well inside the central 4:5 window of the 9:16 frame; honest macro depth of field, both stones sharp. LIGHT AND SHADOW, L2: one direct flash from the camera's own position, hard and frontal, gives the gold-tone wire a crisp bright edge and wakes the tiger eye's silky band; the ring's shadow is short, hard-edged and tucked directly behind and under the ring, reaching no further than a quarter of the ring's height beyond it; never a long shadow stretching sideways across the floor toward the frame edge; plus one large soft overhead fill so the shaded part of the band and the crystal's facets keep their detail. The gold tone stays warm-neutral, never orange or brassy. NEGATIVES: no text, no logos, no star-shaped glints, no starburst, no lens flare, no other jewellery, no props, no plinth or cube, no hands, no water.

**Try 2 measurements (src px)**
- **Extent (first): pass-with-note.**
  - Ring x 398–1119, y 1070–1654. The shadow ends at y 1681 (its soft tail runs to x 1366, under and right of the crystal).
  - The extent is 611 src = **430 Feed px**, 10 px over the 420 band and inside the RULINGS 550 gate.
  - **Use P 63, T 368.55.** The ring top is at Feed 384 (24 px under the callout row), the loop bottom at 794, and the shadow tail at 813.
  - The tail lies at Feed x 703–960, under the right-hand C3/tag slot. Nothing goes there once the size tag is dropped (below).
- **Construction: pass.**
  - One smooth round polished gold-tone wire in an open bypass: the loop reaches left past the tiger eye and the band stays open between the ends, as in the cube ref.
  - Exactly two unmatched stones in slim, slightly irregular bezels:
    - an **opaque banded golden-brown tiger eye** (softly faceted, with silky chatoyant bands, not glassy);
    - a **faceted transparent pale champagne crystal**, a little smaller.
  - No halo, no extra stones, no thick band.
- **Ratios inside the piece (logged).**
  - Tiger eye (with bezel) ÷ wire = 282 ÷ about 40 = **7.0** (7–10 allowed). Pass, at the low edge.
  - Tiger eye ÷ ring width = 282 ÷ 721 = **0.39** (0.30–0.42; ref 0.37). Pass.
  - Ring width ÷ height = 721 ÷ 584 = **1.23** (1.15–1.45; ref 1.24). Pass.
- **Width share: pass.** **46.9%** (46–56%), centred on Feed x 533. Both stones are inside x 216–864: the tiger eye at Feed 433–631, the crystal at 605–786.
- **Scale (logged).** The tiger eye is 282 src px for 11.8 mm = 23.9 src px/mm = **16.8 Feed px/mm**. The brief expected 24–26. This is about life size on a phone, so **do NOT print "Shown magnified"** (there is no tag under 19 px/mm). The callouts carry the mm. The ring reads as 30.5 mm wide, matching the cube ref's 2.6 tiger-eye widths.
- **Colour (logged).**
  - Wire Lab 63 / 6 / 28 (hue 78°, warm-neutral). Tiger eye Lab 50 / 13 / 34 (golden-brown, not black).
  - Sage Lab 45 / −7 / 6 (hue 141°), cooler than the gold. **ΔE76 29–35.**
- **Light rendered:** a soft frontal/top key, L7-like, with a short soft shadow down and right. **The hard L2 flash did not render, on either try.**
- **Scene: note.** "No horizon line" was ignored. There is a **soft wall/floor seam at src y 870–915**: the wall is darker (L 86–90) and the floor lighter (L 113–130).
- **Negatives: pass.** No glints, no props, no hands, no text.
- **200 px gate: pass.** A two-stone ring and nothing else lands first. It is smaller in the frame than the other four.

**Calm zones and layout notes (P 63, T 368.55)**
- **Feed.**
  - Subject box: ring x 280–787, y 384–794. The shadow tail runs to y 813 at x 703–960.
  - **Seam at Feed y 243–275.** It runs under the bottom of headline line 2 (178–260), a soft tonal step only.
  - **Headline 96–260** sits on the wall, rgb (77,94,79), L 90. Bone is about 5.5:1.
  - **Callouts C1/C2 284–360** sit on the floor, L 114, about 4:1, which is acceptable at 26 px weight 500 caps.
  - **Leader end points (on metal, never on a stone):**
    - C1: the tiger eye's left bezel rim at about **(433, 475)**;
    - C2: the crystal's top bezel rim at about **(703, 593)** or its right rim at **(786, 707)**;
    - C3: the band wire at the loop's left extreme, about **(280, 744)**.
  - **C3 at left 72, top 828** clears the loop bottom (794) by 34 px.
  - **Drop the size tag** (16.8 px/mm), so the right slot at 828 stays empty over the shadow tail.
  - **Card 940–1200** sits on mid sage, rgb (113,132,113), L 127. **Bone is only about 3.2:1 there, too low for the 26 px lines.** Add a scrim sampled from the picture's own wall sage, rgb (77,94,79): 0 at Feed 860 → .6 at 960, held to 1350. That brings it to about 4.8:1 and keeps the bone series. The alternative, an ink card with `logo_ink` (about 4.2:1), would break the batch's bone series.
  - **Type must NOT go** over x 280–787, y 384–813, or across any stone.
- **Story.**
  - Ring at Story y 745–1156; the shadow ends at 1174. The seam is at Story 604–636.
  - With the size tag dropped, the stack ends with the offer at 588–650, 95 px above the ring.
  - The logo, headline and name/price sit on the wall (L 92). The offer box crosses the seam at 604–636 (L 100–117), so give the offer box its own fill (the same sage scrim, at .6 behind the box) for contrast.
  - With the size tag kept, the brief would need the ring at 754 or lower, and it sits at 745. Dropping the tag (as above) makes the limit 650 + 24 = 674, which the ring clears.

---

## b03-4 · Monochrome Enamel Hoops · A13 Suspended (float), the crazy slot · dropped

Try 2: job `90a690db-8c87-43a1-84a5-b96d65579c93`, now `pics/b03-4.png`. Try 1: `394dd5a7-2134-4249-8675-3519d5c9ab97`, kept as
`pics/b03-4_try1.png`. Zooms: `tmp/b03-4_lefthoop.jpg`, `b03-4_shadows.jpg` (try 1), `b03-4r_lefthoop.jpg` (try 2), and the ref
zoom `tmp/ref_mono_pack_left.jpg`.

**Both tries pass truth.**
- Per hoop: **exactly one black and one white enamel stripe between three polished gold-tone rails**, an **open C**, the post at the top, a plain ridged polished gold-tone inside (as in the detail ref), zero stones.
- The pair is identical, in the three-quarter pose with the stripes to the camera, as in the pack.
- Black ÷ white stripe width is about 0.8–0.9 (0.8–1.25 allowed).
- Hoop height ÷ width = **1.34** (try 1, 565 ÷ 421). The brief's 1.65 is not what the pack ref measures at this pose: I measure **1.37** on it (253 ÷ 185). So the render matches the real piece, and the brief's ratio was wrong (learnings b02: "measure ratios from the reference photos").
- Gold rail Lab 66–71 / 10–14 / 27–37 (hue 63–75°, warm, not orange). Terracotta Lab 43 / 39 / 34 (hue 41°), darker and redder. **ΔE76 35–40.**
- **Float: pass on both.**
  - Each shadow lies directly below its hoop, separated by a clear gap of floor: **0.41×** the hoop height on try 1, **0.43×** on try 2 (0.4 needed).
  - No wire, stand or support.
  - The shadows are soft rounded parallelograms, not C shapes. Under a light directly overhead that is the physically right footprint of an upright hoop, so I accept it.
- **Light rendered:** L6 overhead with a front-left kicker on the rails, as asked.
- **200 px gate:** two floating earrings land first, and the float reads.

**Both tries fail on extent (the deciding gate).**

| Try | Hoops (src) | Shadows (src) | Extent | Pair width | Scale |
|---|---|---|---|---|---|
| 1 | x 304–725 and 814–1237, y 1022–1611 | y 1843–2008 | 986 src = **693 Feed px** | **60.7%** | **19.9 px/mm** |
| 2 | x 279–738 and 795–1255, y 1023–1656 | y 1920–2035 | 1012 src = **712 Feed px** | **63.5%** | **21.4 px/mm** |

- Allowed: an extent of 550 (Feed 380–930), a pair width of 40–52%, and 14–17 px/mm.
- The Feed has only 940 − 347 = 593 px between the beat and the card. So no P fits the headline, beat, float and card.
  - At the brief's P 53, the shadows land at Feed 990–1100, under the card (b02-2's failure again).
  - Raising the hoops into the beat and headline puts type over the piece.
- **The Story works** as briefed: hoops at Story 712, at or below 682, with the shadows at 1289–1424.

**Corrected prompt used for try 2** (refs: slot 1 pack `970635a3-fe88-4ac1-bdf9-a62c7554a87e`, slot 2 detail
`2ee2cf91-322a-4c28-819c-94b7b7c9989d`). It is the brief's prompt with the size clause replaced, the gap clause raised, and the hoops brought closer:

> Reference 1 is the authority on this exact pair of earrings; ignore its background and light. From reference 2 take only the stripe order and widths, the three fine gold rails and the open C. Vertical 9:16 product photograph, 100 mm lens, low hero camera about 12 degrees above the floor: the pair of Monochrome Enamel Hoops from the reference hover side by side in mid-air above a flat matte terracotta floor that sweeps up into a terracotta wall with no horizon line, both upright and turned three-quarters to the camera exactly as in the reference, the black-and-white striped front face toward the camera, the open side of the C toward the right and the short post at the top, about half a hoop-width apart, centred in the frame. FIDELITY: (unchanged from the brief). SIZE IN FRAME, the most important instruction: the pair is small in a big empty terracotta frame; each hoop's height is only about one twelfth of the frame's height and the pair together spans only about a quarter of the frame's width; the whole group, from the post tips down to the bottom of the shadows, is compact, only about one sixth of the frame's height; never large, never filling the frame. FLOAT: directly below each hoop on the floor lies its own soft-edged shadow, separated from the hoop by a clear gap of empty floor a little more than half a hoop tall, so the pair visibly floats; honest depth of field, both hoops sharp. SCENE, LIGHT, NEGATIVES: (unchanged from the brief).

The model ignored the size clause completely: it asked for about a third of try 1's share and rendered 1.04× try 1's size. **Verdict: dropped.**
The remaining flaw is not minor for the briefed layout.

**Zero-credit rescue for the lead (not taken; a creative call).** Under RULINGS §4, a **card-only** Feed (A1 grammar) has the gate 84–930.
- **Try 1** at **P 100** (T 585) puts hoops plus shadows at Feed **134–827**: hoops 134–548, shadows 711–827. The card at 940 then sits on plain floor.
- The headline and beat would move to the Story only, which fits as briefed.
- Try 1 is the better rescue frame: smaller (693 against 712 px), with darker, crisper shadows.
- At 19.9 px/mm it needs the size tag "Shown magnified · about 20 mm tall". There is no room above the post tips (Feed 134), so set it on one 26 px line (about 650 × 62, centred) at **Feed 851–913**: 24 px under the shadows and 27 px over the card.
- This changes the archetype's copy structure, so it goes to the lead and the critics as a new layout, not as b03-4 as briefed.

---

## b03-5 · Pearl Double Halo Studs · A6 Single Spotlight · pass-with-notes

Job `db922542-6d17-4a32-ba14-7f6966e4a6d6` (try 1, kept). Zooms: `tmp/b03-5_leftstud.jpg`, `b03-5_rightstud.jpg` (2×),
`b03-5_pave_1to1.jpg`; reference crop `tmp/ref_pearl_detail_crop.jpg`.

**Measurements (src px)**
- **Extent (first): pass.**
  - Studs x 339–746 and 804–1206, y 1094–1554. Their forward shadows on the riser top end at y 1690.
  - The extent is 596 src = **419 Feed px** (580 allowed).
  - **P 56, T 327.6** puts the studs at Feed 442–765 and the shadows at 861. Any P from 44 to 71 fits.
- **Construction, per stud: pass.**
  - One round pearl at the centre.
  - An **inner round band of fine pavé**.
  - A **narrow open gap crossed by 4 small bridges** (top, right, bottom, left, as in the detail ref).
  - An **outer softened-square band of pavé**.
  - Bright silver tone, never gold. An identical pair, faces to the camera.
  - At 1:1 the pavé reads as fine glittering micro-pavé, less crisply individual than the ref's round stones. At Feed scale it reads as pavé.
- **Ratios inside the piece (logged).**
  - Pearl ÷ outer band = 485 ÷ 820 (2× zoom) = **0.59** (0.45–0.60; detail ref 0.57). Pass, at the upper edge.
  - Inner band's outer edge ÷ outer band = **0.76** (0.70–0.82). Pass.
- **Width share: pass.** Pair x 339–1206 = **56.4%** (52–66%), centred. Both pearls are inside x 216–864 (centres at Feed x 380 and 707).
- **Scale (logged).** 407 src px for 17.5 mm = 23.3 src px/mm = **16.4 Feed px/mm** (15–18), about life size. **No size tag.**
- **Light rendered: pass with note.**
  - L1 pool: a spotlight from high behind lands as a pool on the riser top and the floor around it. The studs' shadows fall forward toward the camera, with the light passing through each open gap as bright arcs (physically right).
  - The pool's edge is **soft-graded, not crisp**.
  - No beam, haze, rays or star glints.
  - The frame is **75% under L 30 and 79% under L 45** (70–90% asked).
  - The silver stays bright and the pearls keep a round lustre.
- **Pearl colour: note.** The pearl reads **faintly blush**: Lab 71 / **7.2** / 1.5, against the pack ref's 89 / 1.9 / 3.0 and the detail ref's 82 / 4.0 / 9.5.
  - The prompt asked for "a soft pink-white lustre", and the model took the pink. At 200 px it still reads as a white pearl with a pink overtone, not a pink pearl.
  - It is not fixable in layout (no edits), and the copy says "pearl" only in the product name, so it is acceptable.
  - Fix the prompt wording next time (see learnings).
- **Riser: pass.** Charcoal; its lit top (L about 140) is darker than the pavé and the pearls. Not saturated.
- **200 px gate: pass.** Two pearls in silver bands land first. The riser disc and the pool ellipse are the second shape.

**Calm zones and layout notes (P 56, T 327.6)**
- **Feed.**
  - Subject box: studs x 238–848, y 442–765, with shadows to 861. The riser's front face is at Feed about 868–1080; the pool on the floor fades by about 1250.
  - **Headline stagger 110–264 and beat 276–325: near-black**, rgb (13,15,21), L 15. Gold-light and bone are both strong.
  - The pool's glow begins at about Feed 305 at the centre (L 20 → 57 by 376), under the end of the beat. That is fine.
  - The 117 px gap from the beat to the studs is calm.
  - **Card 940–1252:** dark riser face and floor, L 16 (p95 44 at the faint floor glow near 1219). No scrim is needed.
  - **Type must NOT go** over x 238–848, y 442–861.
- **Story.**
  - Studs at Story 762–1085, with shadows to 1181.
  - The brief's stack ends with the offer at 645–707, a 55 px gap (the studs are at or below 731). Pass.
  - The text band 270–707 is dark (L 21). The offer box at 645–707 touches the top rim of the pool glow (p95 L 83), which is still fine for bone.

---

## Light: asked against rendered

| Id | Asked | Rendered |
|---|---|---|
| b03-1 | L1 raking | L1-like warm key from the left, a broad sheen, short shadows to the right; the satin floor adds a diffuse reflection glow |
| b03-2 | L7 | L7, as asked |
| b03-3 | L2 flash | Soft key on both tries (L7-like). Try 1 threw a long side shadow; try 2 a short soft one. **The flash did not render.** |
| b03-4 | L6 | L6, as asked (overhead footprint shadows, kicker on the rails) |
| b03-5 | L1 pool | Pool rendered, with a soft-graded edge rather than a crisp one |

## Prompting learnings from b03 (for the learnings agent)

1. **The size words do not shrink a product-only subject.**
   - With the 0.7× rule, product-only subjects still came out at **1.3–1.85×** the share asked (table above).
   - Asking for about a third of try 1's share (b03-4 try 2: "one twelfth of the height, a quarter of the width, the group one sixth of the height") rendered **2.5–2.65×** the ask, *larger* than try 1.
   - nano_banana_2 has a preferred hero size for a lone product: about 47–76% of the frame width and 21–26% of the height. Size phrases below it are ignored.
2. **Pose and aspect move the extent; size words do not.**
   - b03-3 shrank from 26% to 21% of the height, with the width unchanged at 47%. The prompt copied the reference's own pose ("the loop reaches out to the LEFT past the tiger eye … about 1.3 times as wide as tall; never stood up tall") and raised the camera to 35°.
   - Control the vertical extent by the subject's width ÷ height and the camera angle.
3. **Shadow geometry can be described and it renders.** "Short, tucked directly behind and under, no further than a quarter of the ring's height; never a long shadow sideways" removed try 1's frame-wide shadow.
4. **A floating pair cannot fit the 550 px headline-plus-card gate at the model's hero size.**
   - Hoop (about 21% of the frame height) + gap (at least 0.4× the hoop) + footprint shadow (about 0.3×) comes to about 700 Feed px on both tries.
   - Brief floats as card-only (gate 846), or with a layout budget of about 720 px, or float one piece, not a pair.
   - Overhead L6 gives physically right parallelogram footprints, not C-shaped shadows. Do not require "the same C shape".
5. **Locks and the reference pose held on all 7 pictures.**
   - Cushion halo: 4 claws, one row, cushion shape. Brushed: satin, no mirror. Monochrome: 1 black + 1 white + 3 rails, open C. Pearl: two bands with a bridged gap. Halo Curve: two unmatched stones, open bypass.
   - "Exactly as in the macro/pack reference" reproduced the refs almost exactly. **No morph in b03.**
6. **Light words.** "L2 direct on-camera flash" rendered as a soft key twice: the model does not do hard frontal flash. L6 overhead, L7 window and L1 pool rendered; the pool has a soft edge, not crisp.
7. **Scene words that failed.**
   - "No horizon line" was ignored once the camera went to 35°: a wall/floor seam appeared.
   - "A satin-sheen glaze floor … no mirror reflection" gave a diffuse reflection glow. Ask for a **matte** floor where the card sits.
8. **Colour words leak.** "A soft pink-white lustre" gave a blush pearl (a* 7 against the ref's 2–4). Write "a white pearl with a faint warm cream lustre, never pink".
9. **Brief ratios.** Monochrome H ÷ W is 1.37 on the pack ref at the three-quarter pose, not 1.65. Measure every acceptance ratio from the ref photo itself, at the same pose.
10. **Sage "deep" rendered mid-tone** (L 113–130 on the floor). Bone type on it needs a scrim sampled from the wall. Ask for "dark sage, as dark as forest moss" if the card sits on the floor.

---

## Skeptic

Skeptic and rescuer pass, 19 Nov 2026, about 20:00 UTC. I re-measured each kept picture on two grounds only: **scale** and
**fidelity**. Scale is the piece against a referent and against the sizes in `build/study/products.md`. Fidelity is the
countable features against `build/refs/`. My zoom crops are in `tmp/sk_*.jpg`. All coordinates are source px (1536 × 2752).
Feed px/mm = src px/mm × 0.703. On a phone 64–71 mm wide, life size is about 15–17 Feed px/mm.

**Rescue.** The rescue list was empty: no picture was dropped without a regeneration. b03-4 was dropped after its one
regeneration, so it stays dropped. It still has the zero-credit card-only option, which is the lead's call.

**Result: nothing refuted.** I made no regeneration. The balance read **14.46** credits before and after.
The four kept pictures stand as the verifier logged them, with the notes added below.

| Id | Scale | Fidelity | Skeptic verdict |
|---|---|---|---|
| b03-1 | Product-only, no referent, 34.0 Feed px/mm (about 2.1×). The layout carries the size tag. | Holds. | not refuted |
| b03-2 | Product-only, no referent, 39.3 Feed px/mm (about 2.4×). The layout carries the size tag. | Holds. It nearly copies the macro ref. | not refuted |
| b03-3 | Product-only, no referent, 16.4–16.8 Feed px/mm at the listing's 11.8 mm, so about life size. | Holds. It nearly copies the cube ref. | not refuted (one size flag) |
| b03-5 | Product-only, no referent, 15.7–16.4 Feed px/mm, about life size. | Holds. The pearl overtone and the bridge count are notes. | not refuted (notes) |

### b03-1 · Brushed Gold Huggies

**Scale: not refuted.**
- I masked the gold (Lab b* > 14, L > 35) above the contact shadow.
  - Left huggie: x 227–708, y 1076–1751, so **482 × 676**. Height ÷ width = **1.40** (listing 14 ÷ 9.8 = 1.43; pack ref 1.42).
  - Right huggie: x 767–1371.
- 676 px = 14 mm. That gives 48.3 src px/mm = **34.0 Feed px/mm**, about 2.0–2.2× on a phone. The verifier logged 34.2.
- The listing's 14 mm is confirmed by the 13 Nov size check, which measured 13.1–14.5 mm in the ear
  (`size-check-13nov/page/img/brushed-gold-huggies.jpg`).
- There is no referent in the frame. This is a monument macro, so it is acceptable only because the layout prints
  "Shown magnified · about 14 mm tall" in both the Feed and the Story. **The tag is mandatory. Without it, this picture fails.**

**Fidelity: not refuted.** Crops: `tmp/sk_b03-1_right.jpg`, `sk_b03-1_left.jpg`.
- Zero stones.
- Brushed satin with fine parallel lines on both pieces: vertical on the left face, diagonal on the right. Never mirror.
- Chunky barrels, warm-neutral gold tone, the same piece twice.
- Notes:
  - The right huggie shows its hinge pin at the top of the opening and the clicker seam at the bottom. This is plausible hinge
    hardware, and the outside stays seamless.
  - The right barrel's three-quarter width (605 px) is narrower than a 14 × 9.8 mm barrel would project at the rotation its
    opening suggests (about 730–830 px). That is the model's perspective, not a countable feature.

### b03-2 · Cushion Halo Ring

**Scale: not refuted.**
- The halo is 671 px at 12 mm, so **39.3 Feed px/mm**, about 2.3–2.5×.
- The 13 Nov size check measured the real halo at 12.1–15.0 mm and the stone ÷ halo at 0.70
  (`size-check-13nov/page/img/cushion-halo-ring.jpg`).
- There is no referent in the frame. The layout prints "Shown magnified / halo about 12 mm" in the Feed and the Story.
  **The tag is mandatory.**

**Fidelity: not refuted.** Crops: `tmp/sk_b03-2_halo.jpg` against `tmp/sk_ref_cushion_halo.jpg`; also `sk_b03-2_lshoulder.jpg`.
- Exactly 4 ball claws.
- One single-row cushion halo, with about 9 stones along the top edge, corner to corner, the same count as the macro ref.
- Cool silver tone.
- Centre stone ÷ halo = 0.74 (real piece 0.70, macro ref 0.76).
- The shoulders show a top row plus a side row, exactly as the macro ref does. The brief made that ref the authority for pose,
  halo and shoulder pavé. The upright supplier ref shows only a single top row at its angle. The halo is not doubled and not
  rounded, so there is no D01 drift.

### b03-3 · Halo Curve Ring (try 2)

**Scale: not refuted, with one flag.**
- Ring mask (b* > 18 or L > 70): **723 × 588**.
- Tiger eye: the brown-stone mask gives 275 px wide, or 277 px with its bezel; the bezel is 320 px tall, so height ÷ width
  is 1.16 (cube ref 1.15).
- At the listing's 11.8 mm, that is 23.3–23.9 src px/mm = **16.4–16.8 Feed px/mm**, about 1.0× on a phone.
  There is no referent in the frame, so the verifier's call to drop the size tag stands.
- **Flag for `products.md`.** The worn ref `halo-curve-ring__close.jpg` has a finger in it. Grid crop: `tmp/sk_ref_halocurve_close_grid.jpg`.
  - The finger is about 265 px across at the ring. The tiger eye face is 134 px and the crystal 132 px.
  - At a 17–20 mm finger, the tiger eye's face is about **8.6–10.2 mm**.
  - So the listing's 11.8 mm is probably the stone's diagonal or length (1.3 × the face is about 11–13 mm), not its face width.
  - If the face is really about 9.5 mm, this picture is about 1.2× life size. That is under the 1.25× line, and with no
    referent in the frame it is not refuted.
  - Keep the callout as the listing's own words ("about 11.8 mm"). Before any worn Halo Curve frame, measure the size from
    the close ref.

**Fidelity: not refuted.** Crops: `tmp/sk_b03-3_ring.jpg` against `tmp/sk_ref_halocurve_cube.jpg`.
- It copies the cube ref part for part:
  - the open loop of round wire to the left;
  - the short wire between the stones;
  - exactly 2 unmatched stones in slim bezels.
- The tiger eye is opaque, faceted and banded. It is lighter than in the refs (Lab L 48 against 23–26; hue 71° against
  63–64°), because it is front-lit rather than back-lit. It is still golden-brown and not glassy.
- The crystal is transparent, faceted and pale champagne (Lab 66 / 0.7 / 14.7, hue 87°). It is paler than the warm-lit refs
  (C 21–27) but not pink and not clear-white.

### b03-5 · Pearl Double Halo Studs

**Scale: not refuted.**
- An L profile across the studs at y 1300 puts the left stud at x 345–748 and the right at 805–1195, so **390–403 px**.
- At 17.5 mm, that is 22.3–23.0 src px/mm = **15.7–16.2 Feed px/mm**, about life size. The verifier logged 16.4.
- There is no referent in the frame. No size tag is needed.

**Fidelity: not refuted (notes).** Crops: `tmp/sk_b03-5_leftgap.jpg` and `sk_b03-5_topgap_3x.jpg` against
`tmp/sk_ref_pearl_detail_gap.jpg` and `sk_ref_pearl_pack_studs.jpg`; also `sk_b03-5_feedscale.jpg`.
- Per stud: 1 round pearl, an inner round pavé band, an open gap, and an outer softened-square pavé band, in silver tone.
  The pair is identical.
- **Pearl colour: a note, not a refutation.**
  - Render pearl cores: Lab 74.6 / 6.2 / 1.5 and 74.3 / 5.8 / 0.5 (hue 5–14°, C 6–7).
  - Refs: pack 82.9 / 3.1 / 2.6 and 90.5 / 3.1 / 6.0; detail 83.9 / 3.9 / 9.4 (hue 40–67°).
  - The scene itself is magenta-cool: the render's silver reads a* +2.4 to +3.0, b* −2.4 to −3.4, and the background reads
    a* 0.4, b* −2.5. So I compared each pearl with its own silver:
    - render pearl − its silver: a* +3.2 to +4.1, b* +3.8 to +4.8;
    - detail ref pearl − its silver: a* +1.5 to +2.9, b* +7.2 to +8.8.
  - The real tint gap is about 4 ΔE: a little pinker and less cream. That is a rosé overtone on a white pearl, not a pink
    pearl, and not a different product.
  - At Feed scale it does read blush. The copy must never name the pearl's colour, which is already the verifier's rule.
- **Bridges.** The render has **8 bridges** per stud (4 sides plus 4 corners, evenly spaced; see `sk_b03-5_topgap_3x.jpg`).
  The pack and detail refs show about **5, irregularly spaced**, so the verifier's "4" undercounts the render.
  - At Feed scale each bridge is 2–4 px wide.
  - What reads is "two bands with an open gap", and that holds. This is a minor deviation, not a refutation.
- **Pavé.** At 3× the pavé is a granular stipple with a few larger sparkles, not distinct set stones. At Feed scale
  (`sk_b03-5_feedscale.jpg`) it reads as rows of small round stones, as pavé should. A note only.

### Prompting learnings (skeptic)

1. **Pearl colour.** Use the verifier's fix ("a white pearl with a faint warm cream lustre, never pink"). For dark,
   spotlit scenes, also ask for a **neutral white key on the piece**. The magenta-cool scene light adds about 3 a* to every
   white, on top of the prompt's "pink".
2. **Pavé bridges and stones.** Say "about five tiny bridges, unevenly spaced", and "each band one or two rows of distinct
   round stones about 1 mm, never a frosted or glitter texture".
3. **Halo Curve size truth.** The listing's 11.8 mm is likely the stone's diagonal or length. The finger in the close ref
   gives a face of about 9–10 mm. Before the next Halo Curve brief, settle the face size against the close ref, then set
   that brief's tag threshold from it. b03-3 keeps the verifier's no-tag layout: at either size it is at most 1.25×, and
   there is no referent in the frame.
