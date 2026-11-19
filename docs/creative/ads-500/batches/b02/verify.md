# b02 picture verification (19 Nov 2026, about 17:55 UTC)

I checked each b02 picture in `pics/` against `brief.md` (the acceptance lists), `build/study/products.md` and the reference
photos `build/refs/<handle>__*.jpg`. Zoomed and gridded crops are in `tmp/`. `tmp/verify_sheet.jpg` shows every try side by side.

## Result

| Id | Product | Verdict | Deciding reason |
|---|---|---|---|
| b02-1 | Woven Gold Hoops | **pass-with-notes** (try 2) | Try 1 drew each hoop about 1.7× true size (hoop ÷ neck 0.41). Try 2 is close to true size: hoop ÷ ear is 0.56, the same as the verified worn plate's 0.54, and hoop ÷ neck is 0.25 (width) to 0.30 (height). The braid, disc and latch match the reference. Notes are for layout only. |
| b02-2 | Brushed Gold Huggies | **dropped** (one try) | The generator's 429 left this slot empty, so I generated it once, with the brief's prompt unchanged, in my single batch call. The pair spans 69% of the frame width (the brief asks 35–45%). The float shadows sit at 62.2–68.0% of the height, under the Feed card. The floor gap is 0.27× the huggie height (at least 0.5× is required). The barrels are wider than the real piece. **This slot still has its one regeneration**; the corrected prompt is below. |
| b02-3 | Verdant Circlet Studs | **dropped** (both tries fail) | Try 1: perfect construction and selective colour, but the stud is about 1.5× true size (stud ÷ ear 0.42 against a true 0.28). **The outer corner of the eye and the lashes show at the right edge.** Try 2 is worse: the circlet is inflated (green ÷ stud 0.39 against 0.5–0.7), the big pearl became a bezel-set teardrop, there are 6 clear stones, the stud is 1.5–1.75× true size, and the eye corner is still at the edge. |
| b02-4 | Prism Rivière Bracelet | **pass-with-notes** (try 1, not regenerated) | Colours, halos and links are correct. Scale is within 1.2×: pitch ÷ stone is 1.61, the reference's is 1.62. The hand is relaxed and palm down, not a fist. Notes: it is a right hand, the thumb's edge reaches 63.2%, the gel rims read as flat coloured strokes, and pitch ÷ wrist is 0.178 (just over the brief's 0.17; see below). |
| b02-5 | Verdant Eternity Band | **dropped** (both tries fail) | Try 1: construction faithful to the upright reference, but the ring fills **34.5–71.3%** of the height, so no Feed card fits. Try 2: the S-wave turned into **a straight row of ovals beside one pavé line** (the documented morph), and the ring still reaches 65.7%. |

**Kept: 2 of 5 (b02-1, b02-4), both worn.** The brief's success test needs at least 3 shipped with 2 worn, so b02 can reach it only
if b02-2's remaining regeneration passes.

**Credits.** The balance read 40.46 before the one `generate_image_batch` call (4 jobs) and 32.46 after it, so each picture
cost **2 credits**. Every job was served as `nano_banana_2`, although `nano_banana_pro` was requested. `jobs.json` is updated: try-1
files are kept as `<id>_try1.png`, and each entry records `submitted_at`, `credits`, `served_model` and `verdict`.

**Coordinates.** The source is 1536 × 2752. `.pic` uses object-fit cover, so it scales to 1080 × 1935.
- Feed y = src_y × 0.703125 − 292.5
- Story y = src_y × 0.703125 − 7.5
- x = src_x × 0.703125
- Frame % = src_y ÷ 2752.

---

## b02-1 · Woven Gold Hoops · A2 worn nape (the new move) · pass-with-notes

Kept: try 2, job `12795a65-ab0a-49c6-9143-06f98bb1117c`. Try 1 was `545045e9-d29d-44a6-a373-8b54991aa63f`.

**Try 1 failed on scale.**
- Each hoop measured about 225–266 px wide and 320 px tall (src). The ear is 440 px and the neck 775–790 px.
- Hoop ÷ neck = 0.41 (the brief allows 0.20–0.30; true is about 0.24). Hoop ÷ ear = 0.73.
- By the ear, head breadth and neck, each hoop reads about 42–46 mm against a true 25 mm, so about **1.7×**.
- The droplets also ran down the nape into the card band (Feed y 903–1142).

**Try 2 measurements**
- **Placement.** Left hoop src x 132–332, y 1258–1535; right hoop x 1222–1418, y 1263–1547. That is **45.7–56.2%** of the frame (allowed 36–61%). Pass.
- **Face.** The head is seen from directly behind. No eye, nose, lips or face. Pass.
- **The pair.**
  - Both hoops are visible, whole and sharp, and read as round rings.
  - Ellipse ratio is 200 ÷ 240 = **0.83** (at least 0.75 required).
  - Each hoop hangs just below its lobe, mirror-imaged, with the post in the lobe, the latch over the top and the disc on the outer side, as in the pack.
- **Construction (zoom `tmp/b02-1r_hoops.png`).**
  - A many-strand polished braid with deep ridge-and-shadow interlace, not a tube or a twist.
  - A thin latch wire with a small hinge, a small flat polished disc, zero stones.
  - Warm-neutral gold, not orange.
  - One tiny bead under each hoop. Pass.
- **Ratio inside the piece (logged).** Hoop diameter ÷ braid thickness = **4.3** (240 ÷ about 55 px).
  - The brief's 4.5–5.5 comes from the nominal 25/5 mm.
  - The reference detail photo itself measures **4.1**, so the render matches the real piece. Accepted.
- **Body ratio (logged).**
  - Hoop ÷ neck width = **0.25 by width, 0.30 by height** (neck 790 px at its narrowest). That is inside 0.20–0.30.
  - Hoop ÷ ear height = **0.56**. The verified worn plate `performance/plates/woven-gold-hoops-worn.jpg` (measured 22–26 mm on the reel) gives **0.54**.
  - By the ear-to-ear head width (1372 px, about 16.5 cm) the hoop is about 24 mm wide.
  - Conclusion: about 1.0–1.15× true. Pass.
- **Size.**
  - The near hoop is **13.0%** of the frame width (at least 12% required).
  - It is about 141 px wide on the 1080 Feed, about 5.6 px/mm, so **no size tag** (as the brief says).
- **Water.**
  - Droplets of 2–3 mm only on the sides of the neck beside the hoops (Feed y 692–854, x 281–302 and 771–823).
  - One bead per hoop. None in the card band. They read as water. Pass.
- **Skin and styling.**
  - Warm medium-brown skin with pores and fine downy hair.
  - Wet, sleek hair to a high knot.
  - An oxblood raw-silk blouse with a gold zari edge. Pass.
- **Negatives.** No other jewellery, no second piercings, no star glints, no flare, no text. Pass.

**Notes (minor)**
1. **Light.** It came out soft and frontal. The L5 backlit rim and bloom did not render. The picture is clean, but the "backlit glow" borrow is lost.
2. **Ears.** They show in full (the hair is behind them). The ear tops reach Feed y 291 at x 59–183 and x 907–1024, in the lower headline band.
3. **Zari edge.** It dips to 91.9% at the centre, so in the Feed it shows only at the bottom corners (x < 200 and x > 880, from y about 1180). In the Story it is fully visible (y 1525 and below).

**Calm zones and layout notes**
- **Feed (1080 × 1350).**
  - Subject: hoops x 93–233 and 859–997, y 592–795. Ears x 59–183 and 907–1024, y 291–592. Droplets y 692–854.
  - **Headline band y 84–370.** Dark wet hair spans x 112–980 on every row (mean luminance 18 across x 240–840, 95th percentile 50). From x 72 to 112 it is bright apricot (240,178,117), and the ear tops intrude at y 291–370.
  - **Use the brief's fallback: centre both lines** ("BRAIDED HOOPS. / ZERO STONES." Velista 92 and the beat at 48) inside x 140–940. Bone and gold-light then sit on near-black hair.
  - **Card band y 940–1258.** Calm, dry nape skin with no droplets, warm medium-brown (about rgb 196,127,86). Mean luminance 147 (5th–95th percentile 114–165): this is a **mid-light ground**.
  - The brief's scrim (oxblood-brown, 0 at 860 to .55 at 1350) is too weak for bone type: alpha is only about .25 at the name line, about 2.9:1 contrast.
  - **Either** raise it (0 at 860 → .75 by 1000, held to 1350, in the blouse's own oxblood rgb(99,30,33)), **or** set the card in ink with `logo_ink`, which gives about 5:1 on this skin. The brief holds b01-4's card fixed, so the scrim route keeps the test clean.
  - **Type must NOT go:**
    - over x 80–250 or x 840–1010 at y 580–810 (the hoops);
    - over the ear tops (x 59–183 and 907–1024, y 291–592);
    - left of x 112 in the headline band (apricot).
- **Story (1080 × 1920).**
  - Hoops at y 877–1080. Ears from y 576.
  - **Text band y 270–650** is dark hair across x 112–980 (mean luminance 19 at the centre). The wordmark, headline, name and price, and offer fit centred there. The ears sit only at the far edges (x < 183, x > 907) from y 576.
  - Below 1100 is calm nape, then the oxblood blouse from about 1525. Nothing is placed below 650.

---

## b02-2 · Brushed Gold Huggies · A13 levitation · dropped (one try; one regeneration left)

Job `a336378a-f6fd-46cb-bab3-ae16006ee3b9`. This is its first generation: the generator's submission got a 429 and was not resubmitted. I sent it in
my single batch call, with the brief's prompt unchanged, because the brief says to resubmit a 429 item.

**Measurements**
- **Placement: FAIL.**
  - Huggies at src y 976–1556 (35.5–56.5%).
  - **Shadows at y 1712–1872 (62.2–68.0%)**, which is Feed y 911–1024. The Feed card at 940 would cover the float proof. No other card position fits the fixed F2 card.
  - The Story alone would work (shadows at Story 1196–1309, text at 270–650), but the ad needs both.
- **Width: FAIL.** The pair spans x 256–1316, **69%** of the width (35–45% asked). Each huggie is about 29 px/mm on the Feed, so it is strongly magnified.
- **Float: FAIL by the number, though it reads clearly.**
  - The floor gap between each huggie and its shadow is 156 px, **0.27×** the huggie height (at least 0.5× required).
  - The shadows are the right shape and directly below. No supports.
- **Finish: pass.**
  - Soft brushed satin with fine parallel lines and one broad sheen.
  - The two are identical. Zero stones. Warm gold. The lower halves pick up a pale greenish-blue reflection from the floor, but it does not read as silver.
- **Shape: drift.**
  - The left (front-face) huggie is 490 × 580 px, a face aspect of **0.84** against 0.71 in the pack (9.8 ÷ 14).
  - The right one shows a barrel about 0.6 of its height deep (true 6 ÷ 14 = 0.43).
  - Both read chunkier and squatter than the real piece.

**Corrected prompt for its remaining regeneration** (refs unchanged: slot 1 `7c95b6c6-b5a1-4886-82e7-69c1c6a3940f` pack, the authority; slot 2 `4c630657-80e8-47f5-ad65-1f0938c70900` macro, finish only).
It asks for a smaller pair than wanted because the model grew it about 1.7×, it raises the group, and it locks the face aspect:

> Reference 1 is the authority on this exact piece; ignore its background and light. From reference 2 take only the brushed-satin finish. Product still life in a vertical 9:16 frame, 100 mm macro, camera low at about 12 degrees above the floor: a pair of Brushed Gold Huggies hover side by side, about one huggie-width apart, high above a flat matte sky-blue floor that curves up into a sky-blue wall with no horizon line, each tilted about 15 degrees off vertical, the left one turned so its broad brushed front face shows, the right one turned three-quarters so its round opening shows. FIDELITY: each huggie is the piece in the reference: a chunky huggie about 14 mm tall by 9.8 mm wide, its broad brushed face clearly taller than it is wide (width about seven tenths of its height, never as wide as it is tall, never a squat barrel), a band about 6 mm deep, soft brushed-satin 18k PVD gold tone with very fine parallel brush lines, hidden hinge, zero stones; the two are identical; the finish stays matte and light-scattering with one broad soft sheen, never mirror-polished, ridged, hammered or stone-set, never a large thin hoop. SIZE IN FRAME, the most important instruction: the pair is small in a big empty sky-blue frame; the two huggies together span only about 30% of the frame width, each huggie about one eighth of the frame width wide and about one ninth of the frame height tall. PLACEMENT: the huggies float between about 36% and 46% of the frame height; directly below each, separated by a clear gap of empty blue floor at least as tall as the huggie itself, lies its own crisp soft-edged shadow of the same shape, the two shadows between about 52% and 57% of the frame height; nothing at all is below 58% of the frame height, the whole lower 42% of the frame is empty sky-blue floor for the card, and the frame above 35% is empty sky-blue wall for type. LIGHT, L1: one hard warm spotlight from directly above and slightly in front casts the two shadows straight down and gives each band one broad satin sheen; one soft white bounce card low in front lifts the underside of each band; the gold tone stays warm-neutral against the blue, never orange, brassy or reading as silver tone, and the floor colour must not tint the metal. NEGATIVES: no hands, no people, no strings, wires, stands, pins or supports of any kind, no props, no flowers, no text, no logos, no other jewellery, soft round highlights only with no star-shaped glints, no starburst, no lens flare, no water, no droplets.

At about 30% width, expect a render at about 22 px/mm, so the size tag ("Shown magnified / about 14 mm tall") is required.

---

## b02-3 · Verdant Circlet Studs · A2 selective colour · dropped

Try 2 job: `814ee4e7-390c-4a84-8f50-42f4cee88aa3`. Try 1: `4003757f-8f25-495f-b4d4-5213f674794c`, kept as `pics/b02-3_try1.png`.

**Try 1**
- **Construction: pass, exact to the pack's left stud.**
  - One cushion green CZ at the top, overlapping the circlet. The circlet is open.
  - **5** claw-set clear stones, **2** four-point gold stars, **2** pearls (the round one on the right side, the small one at the lower left).
  - Warm gold tone.
  - Logged ratio: green width ÷ stud height = 135 ÷ 248 = **0.54** (allowed 0.5–0.7).
- **Selective colour: pass.** A saturation scan found **zero** coloured pixels outside the stud's box (src x 644–836, y 1100–1336).
- **Placement: pass.** The stud sits at 39.8–48.8%.
- **Scale: FAIL.**
  - The stud is 248 px tall and the fully exposed ear about 590 px (helix top 590 to lobe about 1180). Stud ÷ ear = **0.42** (allowed 0.22–0.33; true 0.28).
  - The green stone is about 13.8 mm against a true 10 mm.
  - So about **1.4–1.5× true**.
- **Face: FAIL.**
  - The outer corner of the eye and the lashes show at the right edge: src x about 1450–1536, y 520–750, which is Feed x 1020–1080, y 73–235 (`tmp/b02-3_topright.png`).
  - The frame came out about 15.7 cm wide, not the 11 cm asked.
- **Calm zone: fail.** The hair did not cover the ear, so the ear sits in the headline band (Feed x 330–580, y 120–370 is bright ear).

**Try 2** (the prompt added a tight-crop clause, a hair curtain over the ear, an earlobe referent, and a 25° turn away)
- **Construction: FAIL.**
  - The circlet is inflated against the stone: green ÷ stud = 107 ÷ 278 = **0.39**.
  - The large pearl became a **bezel-set teardrop** (the real pearl is round).
  - **6** clear stones instead of about 5. The green stone is in 4 claws rather than its gold frame.
- **Scale: FAIL.** Stud ÷ visible ear is about **0.49** (about 1.5–1.75×).
- **Face: FAIL.** The eye corner, lashes and brow tail are at the right edge again (src x 1450–1536, y 620–800).
- The hair curtain was ignored again: the whole ear shows.
- Selective colour held: the stud is still the only colour.

**For a later batch (not run).** The ear-side view always brings in the eye, because the model frames about 15 cm whatever the "11 cm" says. Brief the Circlet:
- either from behind the ear, as b02-1's back three-quarter view, where the face is physically hidden;
- or as a product-only macro.

Lock the stud's outline against the ear ("the ear is three and a half studs tall"). Keep "the circlet is about 1.3× the green stone's width, never twice" and "the large pearl is a round bead, never a teardrop".

---

## b02-4 · Prism Rivière Bracelet · A1 card (F2 grammar) · pass-with-notes

Job `9da063c2-5bac-4bac-9a4a-9c5db8417b1b` (try 1; not regenerated). The PNG is RGBA with a fully opaque alpha channel.

**Measurements**
- **Placement: pass.**
  - Bracelet src x 700–900, y 1118–1625: **40.6–59.0%**.
  - Forearm y 1110–1615.
  - Hand top 1066 (38.7%). The thumb's lower edge is at **1740 (63.2%)**, just past the brief's "hand inside 35–62%". It is at x 0–510 (Feed x 0–359), and on the Feed it ends at y 931, 9 px above the card top. Minor; see the layout notes.
- **Colours: pass.** From the top across the wrist: pink · yellow · aqua · pink · yellow · pink · aqua · pink · yellow. Three pastels only, no two neighbours the same, no fourth colour. The gel rims do not touch the stones.
- **Construction: pass.** Every square cushion stone has its own fine clear pavé halo. The stones are linked edge to edge in bright silver tone, with no gold. The clasp is hidden.
- **Ratio inside the piece (logged).** Pitch ÷ stone width = 75.5 ÷ 47 = **1.61** (allowed 1.4–1.7). The reference detail photo measures **1.62** (195 ÷ 120 px).
- **Body ratio (logged).** Pitch ÷ wrist breadth = 75.5 ÷ 413–427 = **0.178**, over the brief's 0.12–0.17 by about 5%.
  - The brief's "true 0.14" assumed a 7.5 mm pitch. The reference shows pitch = 1.62 × 5 mm = **8.1 mm**, so the true ratio on a 50–56 mm wrist is 0.145–0.162 and this render is **about 1.1–1.2× true**, at the edge but inside the 1.2× drop line.
  - **9 stones** show across the wrist (7 full, 2 foreshortened). The brief allows 8–11. That count matches a true pitch on an average wrist.
  - The stone measures 47 px against a 413 px wrist, about 5.2–5.9 mm against a true 5 mm.
- **Size.**
  - The bracelet line runs **33%** of the frame width in length (500 px across the wrist).
  - Its horizontal footprint is 13% (x 700–900).
  - About 6.6 px/mm on the Feed, so no size tag.
- **Hand: pass with a note.**
  - Relaxed, palm down, the fingers bending off the left edge, not a fist. Anatomy is plausible.
  - It is a **right** hand (the thumb lies along the lower edge), though the prompt said left. Nothing in the ad depends on which hand.
  - The mehendi is only on the back of the hand and ends before the wrist bone, so the bracelet sits on bare skin.
- **Skin.** Deep brown with pores and fine creases. The forearm's skin texture has a faint regular cross-hatch at full size, invisible at Feed size.
- **Light.** The L3 gel rims came out as a uniform aqua stroke along the top contour and a pink stroke along the bottom, about 6–8 px on the Feed (`tmp/b02-4_rims.png`). They read as a thin coloured edge; a critic may read them as a cut-out outline. Not a composite.
- **Negatives.** No other jewellery, nail art, text, starbursts or flare. The pavé sparkle is small round points. Pass.

**Calm zones and layout notes**
- **Feed (1080 × 1350).**
  - Bracelet x 492–633, y 494–850. The forearm and hand cross the **full width** at y 457–931 (thumb to 931 at x 0–359).
  - **Top band y 0–440:** plain ink-navy velvet (about rgb 0,13,39; mean luminance 13, 95th percentile 17). Calm. A1 puts nothing here.
  - **Card band y 940–1258:** plain velvet (mean luminance 7, 95th percentile 11), near-black navy. Bone and gold-light type pass contrast easily.
  - The hand passes below 880, so use the brief's `.scrim` in the velvet's ink (rgb 0,5,27): 0 at 880 to about .6 at 980. That softens the thumb edge at the far left. Keep the card top at 940; no card element may go left of x 360 above y 960.
  - **Type must NOT go** anywhere in y 440–945. The arm spans the frame edge to edge.
- **Story (1080 × 1920).**
  - Bracelet y 779–1135. Arm y 742–1216.
  - **Text band y 270–650:** plain velvet (mean luminance 13). Calm for the logo, name 344–375, price 389–445, line 459–490 and offer 506–568.
  - Below 1230 is plain velvet (mean luminance 8).
  - Nothing may sit between y 720 and 1230.

---

## b02-5 · Verdant Eternity Band · A5 numeral · dropped

Try 2 job: `85a92bc6-8041-420c-b016-f1f0f2ed23c4`. Try 1: `a51af63b-9874-4e3d-a9ac-7b8bfa292e56`, kept as `pics/b02-5_try1.png`.

**Try 1**
- **Construction: pass. It is nearly the pose of `__upright.jpg`.**
  - About 7 emerald-green ovals on the front arc, each in 4 claws.
  - Set alternately either side of one scalloped pavé S-wave.
  - The open back has two looped tips with a gap. Cool silver tone. A true contact shadow.
  - Logged oval ÷ inner opening = **0.19** (the brief's 0.25–0.35 came from 5 ÷ 16.5 mm; the upright reference itself measures 0.19).
- **Placement: FAIL.**
  - The ring is at src x 450–1142, y 950–1963: **34.5–71.3%** of the height (37% of the frame height tall, 45% of the width wide).
  - On the Feed it covers y 376–1088, so the card (940–1236) would sit on the ring, and no lower card position fits.
  - The ring is turned about 50°, which makes it 0.68 as wide as it is tall. The brief's width lock (44%) therefore pushed its height far past the 481 px band.
- About 35 px/mm on the Feed.

**Try 2** (the prompt locked the height to a quarter of the frame and turned the ring 35°)
- **Construction: FAIL.** All the ovals now sit in **one straight row** down the left side, with **a single gently waving pavé line beside them** (`tmp/b02-5r_grid.png`). They no longer alternate either side of the wave. This is the documented morph ("the S-wave flattens into a straight row").
- **Placement: still FAIL.** The ring is at 34.5–65.7% (31% of the frame height) and x 477–1034 (36% of the width).

**For a later batch (not run).** Keep the reference pose, which held the construction perfectly in try 1, and get the size by framing, not by turning the ring. For example: "shot from further back so the ring stands small in the frame: it is only one quarter of the frame height tall and about 30% of the frame width wide, centred at 49%". Accept about 30% width with the A5 deviation noted, or lay the ring flat for a wide, low silhouette.

---

## Prompts used for the one regeneration call

All four used `nano_banana_pro`, 2k, 9:16, with refs as `image_references`, slot 1 first. The brief's refs were unchanged.

- **b02-1.** The brief's prompt with these changes:
  - The camera is directly behind, level, about 20 cm across, with both ears visible.
  - A "SCALE, the most important instruction" clause: each hoop is about 40% of the ear's height, four hoops fit across the neck, one eighth of the frame width, and never as tall as half the ear or a third of the neck.
  - The hoops hang squarely facing the camera, as wide as tall.
  - Droplets only beside the hoops, none lower on the nape.
  - A high, nearly level neckline at 78%.
  - Ear tops at 35%, lobes at 50%, hoops at 50–58%.
  - **Result: fixed.**
- **b02-2.** The brief's prompt unchanged (its first try).
- **b02-3.** The brief's prompt with these changes:
  - The head turned 25° past profile, an 11 cm frame whose right edge cuts the cheek 3 cm in front of the ear, and eye, lash and brow negatives.
  - A hair curtain over the top and middle of the ear.
  - A SCALE clause: the stud as tall as the earlobe, the green stone half the lobe, one eighth of the frame width.
  - **Result: worse** (see above).
- **b02-5.** The brief's prompt with these changes:
  - A 35° turn, "almost as wide as it is tall".
  - A SIZE IN FRAME clause: height one quarter of the frame (37–61%), 37% width, nothing below 62%.
  - **Result: the construction morphed** and the placement still fails.

---

## Skeptic

Skeptic and rescuer pass, 19 Nov 2026, about 18:10 UTC. It covers one rescue (b02-2) and the two verifier passes (b02-1, b02-4).
Measurements are on the 1536 × 2752 source with PIL. Zooms are in `tmp/sk_*`. `tmp/skeptic_sheet.jpg` shows b02-1 and both
tries of b02-2 and b02-4. `tmp/sk_feedbands_sheet.jpg` overlays the Feed bands on the new tries: headline 84–370 in red, card
140–940 × 940–1258 in green.

### Result

| Id | Verifier | Skeptic | Deciding measurement |
|---|---|---|---|
| b02-1 | pass-with-notes | **kept unchanged (not refuted)** | Hoop ring 223–233 px (unforeshortened height). Hoop ÷ ear = 0.49; the ear is 463 px (helix 829 to lobe 1292). At a 6 cm ear that gives 29.5 mm, **1.18×**. The neck (776 px) gives 1.12–1.23×, the head (1,250 px) 1.06–1.13×. All under 1.25×. Braid, latch post, disc and finish match the pack and detail refs. |
| b02-4 | pass-with-notes | **refuted on scale → regenerated once → dropped** | **Try 1:** pitch ÷ wrist = 73.75 ÷ 412–431 = **0.175–0.179** (the brief allows 0.12–0.17). At a 5.5–6.5 cm wrist that is **1.19–1.42×, central about 1.3×**. **Try 2:** the scale is fixed (0.15, about 1.0–1.2×), but the arm runs diagonally from **17.4% to 74.1%** of the height, and the fingers sit under the Feed card. |
| b02-2 | dropped (one try) | **rescued once → dropped** | **Try 2:** the float, the finish and the face aspect are much better, but the **shadows are at 68.9–71.6%** of the height (under the Feed card), the pair spans **49%** of the width, and the lower halves go grey-green. It fits only a Feed crop shifted down (object-position 50% 80%), which RULINGS §4 does not allow today. |

**Refuted: b02-4.** **Kept: b02-1 only** (worn).

**Credits:** one `generate_image_batch` call of 2 jobs. The balance was 32.46 before and **28.46** after, so 2 credits a picture. Both jobs were served as `nano_banana_2`.

**Files:**
- `pics/b02-2.png` and `pics/b02-4.png` are now the skeptic's tries (try 2).
- The previous files are kept as `pics/b02-2_try1.png` and `pics/b02-4_try1.png`.
- `jobs.json` is updated with the new job ids, `submitted_at`, credits, served model and verdicts.

---

### b02-1 · Woven Gold Hoops · not refuted

**(a) Scale**

Zooms: `tmp/sk_b02-1_hoopL_grid.png`, `hoopR_grid`, `earL_grid`, `lobeL`, `eartopL`.

- **Hoop rings.**
  - Left: x 133–332 (199 wide), y 1287–1510 (223 tall).
  - Right: x 1227–1419 (192 wide), y 1292–1525 (233 tall).
  - The hoops are turned about a vertical axis, so the height is the true diameter: **228 px mean**.
  - The verifier's 240 included part of the disc and post. The latch posts reach y 1255 and 1267, the water beads 1537 and 1545.
- **Ear.** Helix top y 829, lobe bottom about y 1292: **463 px**. Hoop ÷ ear = **0.49**.
  - At a 6.0 cm ear: 29.5 mm, **1.18×**.
  - At a 5.5 cm ear: 27.1 mm, 1.08×.
- **Neck.** Narrowest width is 776 px at y 1700. Hoop ÷ neck = 0.29. At a 9.5–10.5 cm neck that is 27.9–30.8 mm, **1.12–1.23×**.
- **Head.** Widest wet-hair width is 1,250 px (y 550–700). At 14.5–15.5 cm it gives 26.5–28.3 mm, **1.06–1.13×**.
- **Inside the piece.** Hoop ÷ braid is about 4.1–4.3. The detail ref is 4.1.
- **Verdict on scale: about 1.1–1.2× true**, under the 1.25× refute line. The verifier's "1.0–1.15×" is a little generous; log it as 1.1–1.2×.

**(b) Fidelity against `woven-gold-hoops__pack.jpg` and `__detail.jpg`**
- A many-strand polished braid with deep open interlace, not a tube or a twist.
- One flat polished round disc at the upper outer side of each hoop. The post and latch sit at the top inner side.
- A mirrored pair. Zero stones. Warm 18k gold tone.
- The tiny bottom beads read as water droplets, not as a jump ring.
- Same product. **Not refuted.** The verifier's object is kept unchanged.

---

### b02-4 · Prism Rivière Bracelet · refuted on scale → try 2 → dropped

**Try 1** (job `9da063c2…`, now `pics/b02-4_try1.png`). Zooms: `tmp/sk_b02-4_brace_grid.png`, `braceTop_grid`, `braceBot_grid`.

- **Pitch.** Halo starts at y 1200 (aqua), 1270 (pink), 1345 (yellow), 1420 (pink) and 1495 (aqua): **73.75 px**. Halo 72 px wide (x 747–819). Centre stone 47.5 px.
- **Wrist.** Velvet-to-velvet edges per column:
  - 431 px at x 720 and 428 px at x 740 (at the bracelet);
  - **412 px** at x 850–900 (the narrowest, just behind it);
  - 548–573 px for the back of the hand at x 100–200.
  - The hand ÷ wrist ratio of 1.36 is anatomically normal, so the body is self-consistent.
- **Pitch ÷ wrist = 0.175–0.179.** The brief's acceptance is **0.12–0.17** (true about 0.14), so this fails the brief's own body ratio.
- **In mm, against the true 8.1 mm pitch (pitch ÷ stone 1.62 × 5 mm; it also fits 18 cm with about 21 stones and the clasp):**

| Referent | Pitch | Scale |
|---|---|---|
| Wrist 5.5 cm | 9.7 mm | 1.19× |
| Wrist 6.0 cm | 10.5 mm | **1.30×** |
| Wrist 6.5 cm | 11.4 mm | 1.41× |
| Hand breadth 7.5–8.0 cm (560 px) | 9.9–10.5 mm | **1.22–1.30×** |
| Centre stone at a 5.5–6.0 cm wrist | 6.2–6.8 mm against 5 mm | **1.24–1.36×** |
| Count: 9 stones show across the top half of the loop, where an 18 cm loop holds about 11 at true pitch | | about 1.2× |

- **Verdict: about 1.2–1.4×, central about 1.3×. Refuted** (over 1.25×, and outside the brief's 0.17).
- The verifier reached 1.1–1.2× only by assuming a 50–56 mm wrist. That is narrower than the 5.5–6.5 cm referent and than this hand's own proportions allow.
- Fidelity was not in question. The verifier's count holds: P Y A P Y P A P Y, three pastels, a halo on every stone, silver tone.

**Corrected prompt (sent once).** This is the brief's prompt with these changes:
- A "SCALE, the most important instruction" clause with the wrist as the ruler. Each haloed square is one eighth of the wrist's width, "never one sixth and never one fifth". Twelve stones run edge to edge across the top of the wrist, "never fewer than eleven". (Asked lower than true, because the model drew 0.175 when asked for 1/7 ≈ 0.143.)
- A 20 cm frame with the wrist a quarter of the frame width.
- The thumb tucked alongside, never below the forearm's lower edge (try 1's thumb reached 63.2%).
- Hand and thumb at 39–59%, with everything above 38% and below 60% stated as plain velvet, the largest areas of the frame.
- The L3 rims as "a soft faint glow that fades into the skin, never a solid coloured outline" (try 1's rims read as a cut-out stroke).

Refs unchanged: slot 1 `f9e23a88…` pack, slot 2 `8f1ff732…` detail.

> Reference 1 is the authority on this exact piece; ignore its background and light. From reference 2 take only the pave halo around each cushion stone and the three pastel colours. Overhead photograph in a vertical 9:16 frame, the camera pointing straight down at 90 degrees, about 20 cm across, so the wrist is about one quarter of the frame width: a woman's bare left forearm lies flat and horizontal across the middle of the frame on deep ink-blue velvet, entering from the right edge where the elbow side is cut by the frame, and running left to her hand, which rests relaxed and palm down with the fingers gently curved and their tips touching the velvet, never a clenched fist, the fingers running out of the left edge; the thumb lies close alongside the hand and never reaches below the lower edge of the forearm; the hand is no wider than about one and a third times the wrist. FIDELITY: on her wrist the Prism Riviere Bracelet from the reference: one continuous single line of small square cushion-cut pastel cubic zirconia about 5 mm each in aqua blue, soft pink and pale yellow mixed along the line with no two neighbours the same colour, each stone framed by its own fine halo of tiny clear pave, linked edge to edge in bright PVD rhodium silver tone, the fold-over clasp hidden under the wrist. It must stay three pastel colours, never a fourth colour such as lilac, green or white, never bare stones without halos, never gold. SCALE, the most important instruction: a slim, delicate bracelet on a normal adult wrist about 5.5 cm wide. Each haloed square is only about one eighth of the wrist's width, never one sixth and never one fifth; twelve haloed stones line up across the top of the wrist from its upper edge to its lower edge, never fewer than eleven; the line of stones is a narrow strip only about one eighth as wide as the wrist, lying flat on the skin with a fine contact shadow along both edges. SCENE: deep brown skin with visible pores and fine wrist creases; a fine traditional mehendi pattern on the back of the hand only, ending before the wrist bone, so the bracelet sits on bare skin; the velvet is plain. PLACEMENT: the forearm crosses the frame between about 41% and 57% of the frame height, and the hand and thumb stay between about 39% and 59%, inside the central 4:5 window, with the bracelet at the horizontal centre. The largest areas of the frame are empty plain ink velvet: everything above 38% of the frame height and everything below 60% is plain velvet with nothing on it. LIGHT, L3 two-colour gel rim on a dark ground: one large soft white light from directly above keeps the stones' true aqua, pink and yellow and shows the skin texture; one low rim light from the far side, split-gelled aqua and soft pink, leaves only a soft, faint coloured glow that fades into the skin along the top contour of the forearm and hand, never a solid coloured outline or stroke, never on the stones; the pave sparkles as small round points. NEGATIVES: no face, no other jewellery (no rings, no bangles, no watch), no nail art, no text, no logos, no star-shaped glints, no starburst, no lens flare, no water, no droplets.

**Try 2** (job `79345141-8730-4e7d-8c62-a96f71a59ea4`, now `pics/b02-4.png`). Zoom: `tmp/sk_b02-4r_brace_grid.png`.

- **Scale: fixed.**
  - Stone centres run along a line about 61° from horizontal, square to the arm: aqua (862,1037) → aqua (957,1197) and pink (895,1087) → pink (985,1252). Pitch **62–63 px**.
  - The wrist along the bracelet line is about 410–420 px (the arm is at about 29°; vertical extent 457–481 × cos 28°).
  - Pitch ÷ wrist = **0.149–0.152**: 8.2–9.9 mm at a 5.5–6.5 cm wrist, **about 1.0–1.2×, central 1.1×**.
- **Fidelity: pass.**
  - Y A P Y A P Y A P across the wrist: 9 visible (7 full and 2 at the edges), three pastels, no neighbours the same.
  - A pavé halo on every stone, bright silver tone, clasp hidden.
- **Rims: fixed.** They are now a faint fade, not a stroke.
- **Placement: FAIL.**
  - The forearm came in **diagonally**, from the top-right edge at 17.4% (x 1535, y 479) down to the fingertips at **74.1%** (x 0, y 2039).
  - The hand and fingers are at 64.5–73.5% across x 0–500. That is Feed x 0–352 and Feed y 940–1141, under the left third of the fixed card.
  - The bracelet itself is at 35.8–50.9% (x 795–1050). The forearm's top edge reaches the Story text band (y 270–650) right of Story x 830 to 1040, depending on the line.
  - **Dropped**, with the slot's one regeneration spent.
- **Note for the lead.** Try 1 is layout-ready and true in every count. It fails only on scale, about 1.3× (1.19× at a 5.5 cm wrist). It is in `pics/b02-4_try1.png` if the owner accepts that.

---

### b02-2 · Brushed Gold Huggies · rescue → dropped

**What failed before.** The verifier's measurements of try 1:
- the pair at 69% of the width;
- the shadows at 62.2–68.0%;
- a gap of 0.27× the huggie height;
- a face aspect of 0.84 against 0.71.

The model drew the pair about 1.7× the 40% asked.

**Corrected prompt (sent once).** The changes against the brief:
- **Shot from far back with a 50 mm lens** in a "large empty studio". The brief's "100 mm macro feel", "3 cm above the floor" and "chunky" were removed, because they invite a frame-filling piece.
- **SIZE as the most important instruction:**
  - each huggie one twelfth of the frame height and one tenth of the width;
  - the pair about 28% of the width;
  - "the empty blue to the left and to the right of the pair are each wider than the pair itself".
  - This was asked lower than wanted to allow for the model's growth.
- Huggies at 37–45%, shadows at 51–55%, a gap of three quarters of the huggie's height. "Everything above 36% … and everything below 57% is plain" is stated as the largest areas of the frame.
- The face lock: "a tall rounded rectangle, width seven tenths of its height, never a squat barrel". The band less than half the height.
- "The same warm-neutral gold from top to bottom; the blue floor must not reflect into or tint the metal."
- **Slot 2 (the macro) was left out.** Its frame-filling close-up shows the face wider than tall, which pulls both size and shape. Slot 1 `7c95b6c6…`, the pack, was the only ref; it shows the brushed finish clearly.

> Reference 1 is the authority on this exact piece; ignore its background, plinth and light. Product still life in a vertical 9:16 frame, shot from far back with a 50 mm lens, the camera low at about 12 degrees above the floor, in a large empty seamless sky-blue studio: a flat matte sky-blue floor curves up into a sky-blue wall with no horizon line. Two small Brushed Gold Huggies hover in mid-air side by side, about half a huggie-width apart, each tilted about 15 degrees off vertical; the left one turned so its broad brushed front face shows, the right one turned three-quarters so its round opening shows. FIDELITY: each huggie is the piece in reference 1: a wide-band huggie about 14 mm tall and 9.8 mm wide; its brushed front face is a tall rounded rectangle, clearly taller than it is wide (its width seven tenths of its height), never as wide as it is tall, never a squat barrel; the band is about 6 mm deep, less than half the huggie's height, never a deep barrel or a thick cylinder, and the round opening shows a thin metal wall; soft brushed-satin 18k gold tone with very fine parallel brush lines and one broad soft sheen; hidden hinge; zero stones; the two are identical. The finish must stay matte and light-scattering, never mirror-polished, ridged, hammered or stone-set, never a large thin hoop. SIZE, the most important instruction: the pair is small in a big empty frame. Each huggie is only about one twelfth of the frame height tall and about one tenth of the frame width wide; the two together, including the gap between them, span only about 28% of the frame width, and the empty blue to the left of the pair and the empty blue to the right of it are each wider than the pair itself. PLACEMENT: the two huggies float on the vertical centre line between about 37% and 45% of the frame height. Directly below each huggie, separated from it by a clear band of empty blue floor about three quarters of the huggie's height, lies its own crisp soft-edged shadow of the same shape; the two shadows lie between about 51% and 55% of the frame height. The largest areas of the frame are empty: everything above 36% of the frame height is plain, evenly lit sky-blue wall, and everything below 57% is plain empty sky-blue floor with nothing on it. LIGHT, L1: one hard warm spotlight from directly above and slightly in front casts the two shadows straight down and gives each band one broad satin sheen; one soft white bounce card low in front lifts the underside of each band. Each huggie stays the same warm-neutral gold tone from its top to its bottom: the blue floor must not reflect into or tint the metal, never orange or brassy, never reading as silver tone. NEGATIVES: no hands, no people, no strings, wires, stands, pins, plinths or supports of any kind, no props, no flowers, no text, no logos, no other jewellery, soft round highlights only with no star-shaped glints, no starburst, no lens flare, no water, no droplets.

**Try 2** (job `6e938236-e5d6-483f-8682-d3071eab6499`, now `pics/b02-2.png`). Zooms: `tmp/sk_b02-2r_pair.png`, `sk_b02-2r_shadows.png`.

- **Placement: FAIL.**
  - Huggies at y 1182–1551, **42.9–56.4%**.
  - **Shadows at y 1895–1970, 68.9–71.6%.** That is Feed y 1040–1093, under the fixed card (940–1258).
  - The model centred the pair at about 50% and doubled the gap. Placement is no better than try 1's (62–68%).
- **Width: FAIL (minor).** x 406–1163 is **49.3%** of the width (28% asked, 35–45% accepted). The model grew it about 1.75× again.
- **Float: pass.** The gap is 344–374 px, about **1.0×** the huggie height (at least 0.5× required). Each shadow is directly below and the same shape. No supports.
- **Finish: pass.**
  - Soft brushed satin with fine parallel lines and one broad sheen, not mirror. Both identical. Zero stones.
  - The right huggie shows its click post at the top of the opening and a seam at the bottom. That is normal for a huggie seen from its opening; the pack hides it. Minor.
- **Shape: improved.**
  - The left huggie's bounding box is 268 × 338, an aspect of **0.79** with a slight tilt (0.84 before, 0.71 true).
  - Band depth is about 0.5 of the height.
  - The left huggie is nearly upright (the brief asks 10–20°).
- **Colour: note.** The upper halves are warm gold: rgb(223,199,166), hue 35°, saturation 0.47. The lower halves go **grey-green**: rgb(166,167,143) on the left and rgb(162,174,162) on the right, saturation 0.07–0.12. This is the floor bounce the prompt forbade; at Feed size it reads pale champagne rather than silver.
- **Scale.** 338 px for 14 mm is 24.1 px/mm on the source, **17.0 px/mm on the Feed**: under 19, so no size tag.
- **Calm zones.**
  - Central crop: the Feed headline band (src 535–942) is plain sky wall (luminance standard deviation 3.7). The Story text band 270–650 (src 395–935) is plain wall: mean luminance 173, 5th–95th percentile 167–179.
  - Story placement: huggies at 824–1083, shadows at 1325–1378, so the **Story works**.
- **Verdict: dropped** under the brief's acceptance (35–62%) with the central Feed crop. The slot's one regeneration is spent.
- **Possible rescue: a lead decision, not taken here.**
  - With the Feed crop shifted down (`.pic { object-position: 50% 80% }`, crop src 663–2583), the Feed works:
    - huggies at Feed 365–624;
    - shadows at 866–919;
    - the card at 940–1258 on plain floor;
    - the headline (104–215) and beat (226–290) on plain wall.
  - See `tmp/sk_b02-2_feedshift80.jpg`. That needs RULINGS §4 ("the central crop") relaxed for this ad. The width (49%) and the grey-green lower halves would ship as notes.

---

### Learnings for the next batch (skeptic)

1. **Placement percentages still do not move the subject.** Both new tries centred their subject (huggies about 50%, bracelet about 43%) whatever the 37–45% or 41–57% asked.
   - The huggie pair grew 1.75× over the asked width again.
   - The diagonal arm appeared once "horizontal" was no longer the first geometric phrase of the shot.
   - Brief the template around a centred subject: put the float shadows above or beside the piece, or accept a Feed crop offset, rather than asking for 36–61% by numbers.
2. **A wrist ratio inside the scale clause works.** "One eighth of the wrist's width, never one sixth or one fifth" plus "twelve stones edge to edge" moved pitch ÷ wrist from 0.178 to 0.150.
3. **Verifier calibration.** For worn scale, use the referent ranges in the brief (wrist 5.5–6.5 cm, ear about 6 cm), not the most favourable body size. Report the central estimate. b02-4 passed at an assumed 50–56 mm wrist and fails at 6 cm.
4. **Brushed on a blue floor.** The lower halves pick up a grey-green bounce in both tries, even with a never-clause. A warmer floor (or a gold bounce card named as the only light below) may be needed for the satin to stay gold.
