# k01a · brief applied (camp k01 AUNTY NE CHASHMA LAGAYA., cards 1-5)

## Loop diff: none applied

No loop diff was applied. k01a is the first batch of the Crazy 100 run, so no batch came before it and no loop note exists yet:
- `concept-50/batches/k01a/brief_diff.md` does not exist.
- `concept-50/batches/loop.md` does not exist.
- The only earlier batch in `concept-50/batches/` is `c01`, which has prompts and jobs but no loop note.

Two of the files the role names are missing too:
- `concept-50/CRAZY100.md` does not exist, so I read the camp from `concept-50/crazy100.json` (camps[k01]: idea, textual graphic, palette, sell lever, changes, ads 1-5) and from `concept-50/RULINGS.md`.
- `concept-50/build/learnings.md` does not exist, so I read the ledger at `ads-500/build/learnings.md` instead, together with `ads-500/batches/b04/review.md` (prompting learnings) and `ads-500/batches/b04/verify.md` (the shipped Toggle prompt).

## Conformance edits

Take A is each card's planned `prompt` from `crazy100.json` with only the edits listed below. These edits are not loop changes. Each one brings a prompt in line with the shooter's standing spec:
- the exact reference sentence;
- the product card's lock and its must-stay clause;
- the exact no-text negatives with "no watermark";
- "no eyes, no eyebrows";
- named calm areas for the headline and the card;
- no 4K pixel size, because the jobs render at 2k.

The words were linted against the banned list:
- diamond, real gold, solid gold, freshwater, emerald, ruby, huggie;
- bare "gold" or "silver" without "tone";
- water words outside a negative on the pieces with no waterproof claim (Baroque, Toggle).

The lint also checked that each prompt has every required part. All 6 prompts are clean.

## Take B: one card, k01-5 (Toggle Link Chain, "Aunty bhi legi")

**Why k01-5.** Its `risk` field calls the clasp "the hardest piece we generate, with eight failed toggle renders on record", and it is a Kling Reel, so a weak still costs a Reel. The past lessons point the same way (ads-500 b04 review, prompting learnings 1-4):
- At 9:16, front-on, no crop wording keeps the chin out.
- A headless crop worded around chest and skin was refused by the safety filter.
- "Posed exactly as in the clasp reference … never its framing or its size" is the only wording that held the clasp. The bar measured 0.64-0.67 of the ring, with one row of stones.
- Counts and widths against body landmarks fixed worn chain scale; fractions did not.

**Why only one take B.** The plan's `batches[k01a].hedgeTakes` lists k01-4 and k01-5, but this run's credit rule allows one take B, so k01-4 gets only take A. k01-4's risk (regularised pearls) has no failure on record yet, while the toggle has eight.

**What take B keeps.** The idea and the twist stay whole: the aunty herself wears the toggle and holds her own half-moon glasses over the sailor ring. So do:
- the rani-pink blouse and pallu;
- the plum night with marigold bokeh;
- the lens centred on the ring;
- the 33-53% piece band, the calm headline and card zones, and the two lights.

**What take B hedges.** I did not take the card's own suggested hedge (a young collarbone with the aunty's hand from the edge), because it drops the twist the ad is built on. Take B hedges the riskiest elements instead:
1. **Clasp.** It is posed exactly as in reference 2 (the clasp crop on skin): bar across the upper left of the ring with its stones to camera, ring below, gate and push-pin nub at the right, "copy its construction and pose, never its framing or its size". This is the b04 wording that held the clasp.
2. **Face.** The camera sits a little above the collarbones, looking down at about 20 degrees, and her head is turned away out of the picture. Negatives add no nose, lips, chin or jaw. This is b04 lesson 2.
3. **Safety filter.** The prompt opens with "a jewellery close-up of the necklace for its listing: a close crop of one woman's neck and collarbones only". The deep round neck becomes a modest round neckline with a zari edge. This is b04 lesson 3.
4. **Scale by counts.** The ring is about two links wide, the neck about five ring-widths (about 11 cm), about twelve links a side, and the clasp about three ring-widths below the hollow of the throat, touching the skin with a true contact shadow. This is b04 lesson 1.
5. **Lens margin.** The lens grows from 34% to about 40% of the width, and the whole ring and bar are seen through clear glass with the rim never crossing them. A rim across the clasp would spoil the 2x lens crop and the true-size read.

## Flag for the finisher

The plates render at 2k (about 1536 x 2752), not the 4K (2160 x 3840) that the camp's textual graphic plans for the native-pixel 2x lens. At 2k the 2x lens crop upsamples by about 1.4x inside the rim. Check its sharpness at Feed size before laying out the lens, or upscale the approved still first. An upscale is not an edit of the piece.

## Edit log, edit by edit
### k01-1A  (lint: clean)
1. the job renders at 2k (task spec), so the 4K pixel size is dropped from the prompt
   - was: "at 4K (2160 x 3840)"
   - now: "at high resolution"
2. reference sentence set to the required wording, card detail kept
   - was: "Reference 1 is the authority on this exact piece: copy the earring's construction exactly and ignore its block and light; reference 2 is a detail of the braid."
   - now: "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. Ignore the plaster block as well; reference 2 shows the open braid and its see-through core up close."
3. headline calm area named
   - was: "calm out-of-focus plum bokeh with soft marigold points and nothing else;"
   - now: "calm out-of-focus plum bokeh with soft marigold points and nothing else, kept clear for the headline;"
4. card calm area named
   - was: "below 55% soft ivory silk and plum shadow, darker toward the bottom."
   - now: "below 55% soft ivory silk and plum shadow, darker toward the bottom, kept calm and clear for the price card."
5. required negatives: no watermark, no eyebrows
   - was: "no text, letters, numbers or logos anywhere; no face or eyes anywhere, never reflected in the lens;"
   - now: "no text, no letters, no numbers, no logos, no watermark anywhere; no face, no eyes, no eyebrows anywhere, never reflected in the lens;"

### k01-2A  (lint: clean)
1. 2k render, 4K pixel size dropped
   - was: "at 4K (2160 x 3840)"
   - now: "at high resolution"
2. reference sentence set to the required wording, card detail kept
   - was: "Reference 1 is the authority on this exact piece: copy the ring's construction exactly and ignore its cube, background and light; reference 2 shows it worn at true scale."
   - now: "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. Ignore the plaster cube as well; reference 2 shows the same ring worn on one finger, close up, at true scale."
3. lock words restored from the product card: 'open bypass', 'about 17 mm inside'
   - was: "the ring on her index finger, stones on top: one smooth round 1.5 mm wire in 18k gold tone whose two ends pass side by side;"
   - now: "the ring on her index finger, stones on top: an open bypass ring of one smooth round 1.5 mm wire in 18k gold tone, about 17 mm inside, whose two ends pass side by side;"
4. must-stay clause set to the product card's lock wording
   - was: "The tiger eye must stay opaque, banded and golden-brown, never transparent, glassy or a twin of the crystal;"
   - now: "The tiger eye must stay opaque, banded and golden-brown and unmatched beside the clear crystal, never transparent, glassy or a twin of the crystal;"
5. headline calm area named
   - was: "calm dark bokeh with two or three soft amber points;"
   - now: "calm dark bokeh with two or three soft amber points, kept clear for the headline;"
6. card calm area named
   - was: "below 55% soft, dark steel."
   - now: "below 55% soft, dark steel, kept calm and clear for the price card."
7. required negatives: no watermark, no eyebrows
   - was: "no text, letters, numbers or logos anywhere; no faces, eyes or reflections of faces;"
   - now: "no text, no letters, no numbers, no logos, no watermark anywhere; no faces, no eyes, no eyebrows, no reflections of faces;"

### k01-3A  (lint: clean)
1. 2k render, 4K pixel size dropped
   - was: "at 4K (2160 x 3840)"
   - now: "at high resolution"
2. reference sentence set to the required wording, card detail kept
   - was: "Reference 1 is the authority on this exact piece: copy the earring's construction exactly and ignore its cube, background and light; reference 2 shows the mirrored pair from above."
   - now: "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. Ignore the plaster cube as well; reference 2 shows the mirrored pair from above."
3. 'pearl' named as shell pearl, as the product card's copy notes ask
   - was: "one plain four-point star, one small pearl, one clear stone,"
   - now: "one plain four-point star, one small white shell pearl, one clear stone,"
4. headline calm area named
   - was: "calm indigo night with soft warm points;"
   - now: "calm indigo night with soft warm points, kept clear for the headline;"
5. card calm area named
   - was: "below 55% soft green silk and shadow."
   - now: "below 55% soft green silk and shadow, kept calm and clear for the price card."
6. required negatives: no watermark, no eyebrows
   - was: "no text, letters, numbers or logos anywhere; no face or eyes, never reflected;"
   - now: "no text, no letters, no numbers, no logos, no watermark anywhere; no face, no eyes, no eyebrows, never reflected;"

### k01-4A  (lint: clean)
1. 2k render, 4K pixel size dropped
   - was: "at 4K (2160 x 3840)"
   - now: "at high resolution"
2. reference sentence set to the required wording, card detail kept
   - was: "Reference 1 is the authority on this exact piece: copy the bracelet's construction exactly and ignore its block, background and light; reference 2 shows it worn at true scale."
   - now: "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. Ignore the plaster block as well; reference 2 shows the same bracelet worn on a wrist at true scale."
3. lock size (9-20 mm) added; 'pink-silver' reworded so no bare metal word appears and the pink stays faint (b03 lesson: colour words leak)
   - was: "one strand of eight flat, irregular baroque shell pearls, white with a soft pink-silver lustre, every one a different shape and size,"
   - now: "one strand of eight flat, irregular baroque shell pearls, about 9 to 20 mm, white with a soft pearly lustre and only a faint pink sheen, every one a different shape and size,"
4. scale referent stated in mm
   - was: "field of view about 13 cm wide, so the wrist fills a little under half the frame's width;"
   - now: "the wrist is about 6 cm wide; field of view about 13 cm wide, so the wrist fills a little under half the frame's width;"
5. headline calm area named
   - was: "calm plum dark with soft diya points;"
   - now: "calm plum dark with soft diya points, kept clear for the headline;"
6. card calm area named
   - was: "below 55% soft plum velvet."
   - now: "below 55% soft plum velvet, kept calm and clear for the price card."
7. required negatives: no watermark, no eyes, no eyebrows
   - was: "no text, letters, numbers or logos anywhere; no water or droplets; no faces;"
   - now: "no text, no letters, no numbers, no logos, no watermark anywhere; no water or droplets; no faces, no eyes, no eyebrows;"

### k01-5A  (lint: clean)
1. 2k render, 4K pixel size dropped
   - was: "at 4K (2160 x 3840)"
   - now: "at high resolution"
2. reference sentence set to the required wording, card detail kept
   - was: "Reference 1 is the authority on this exact piece: copy the necklace's construction exactly and ignore its cube, background and light; reference 2 shows the clasp in detail."
   - now: "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. Ignore the plaster cube as well; reference 2 shows the clasp worn on skin: copy the clasp's construction exactly from it."
3. headline calm area named
   - was: "calm plum bokeh at both sides of the neck;"
   - now: "calm plum bokeh at both sides of the neck, kept clear for the headline;"
4. card calm area named
   - was: "below 55% soft pink silk."
   - now: "below 55% soft pink silk, kept calm and clear for the price card."
5. required negatives: no watermark, no eyes, no eyebrows
   - was: "no text, letters, numbers or logos anywhere; no water; no face;"
   - now: "no text, no letters, no numbers, no logos, no watermark anywhere; no water; no face, no eyes, no eyebrows;"

### k01-5B  (lint: clean)
- take B written from take A (see brief_applied.md)

## Generation record

- **Balance:** 342.46 before and 326.46 after. The transaction log shows 6 spends of 2 credits for this batch (17:39:15 x4 and 17:39:59 x2). The other 4 credits of the drop (17:38:02 x2) were spent by another session.
- **Rate limit:** on the first call, k01-1A and k01-4A were refused with `submission_failed` (429), so they were never submitted. I resubmitted them once after one jobs_wait round.
- **Outcome:** all 6 jobs completed, with no failed or nsfw jobs. Every job was requested as `nano_banana_pro` and served as `nano_banana_2`, at 1536 x 2752. Details are in `jobs.json`.
