# k03b brief applied (camp k03 BEST OF THREE., cards 6-10)

Written 20 Nov 2026 by the k03b lead shooter.

## What was applied

Take A for each card is the card's planned `prompt` in `crazy100.json` with two sets of edits, in this order:

1. **The loop diff, `batches/k03b/brief_diff.md`, sections 1-6: all 94 edits applied, 0 misses.** Every edit is an exact string operation, applied once, in the order given, to a copy of camp k03:
   - 7 camp edits (C1-C7);
   - 20 on card 6, 16 on card 7, 18 on card 8, 17 on card 9 and 16 on card 10.
   - Every `old` and `after` string occurred exactly once in its field.
   - The result is identical, field by field, to the loop writer's own simulation (`scratchpad/k03a_loop/k03_after_diff.json`).
   - The diff touches the prompt, picture, beat, layout, offer, primaryText, motion and risk fields. Only the prompt is shot here. The other fields are recorded for the designer in `batches/k03b/brief_after.json`.
2. **The shooter's conformance edits (X1-X15), prompt only.** They cover the batch's prompt rules the diff left open:
   - the exact reference sentence;
   - the banned-word lint;
   - contact shadows and the calm card area;
   - the product card's scaleRef for card 10;
   - learnings 24 (no big-prop size in a macro) for cards 9 and 10.

`crazy100.json` itself is not modified, as in k01r and k03a. `batches/k03b/brief_after.json` holds camp k03 (its camp fields and cards 6-10) after both sets of edits.

Sources read:
- `crazy100.json` (camp k03 and cards 6-10);
- `CRAZY100.md` §6 k03 and §9, with the owner rulings;
- `build/learnings.md` 1-29;
- `batches/k03b/brief_diff.md` and `batches/k03a/loop.md`;
- the five product cards and their reference photos (all looked at).

## Batch rules followed

- **Model.** Take A for all five cards is `gpt_image_2_6`, medium, 2k, 9:16, use_unlim false. No product card has a `shootModel`.
- **No take B.** The batch allows take B on 0 cards, and diff §0 and learnings 16 drop the plan's hedge takes for k03-9 and k03-10.
- **No composite anywhere.** The diff removes every composite hedge and every composite motion line (C1, C2, 6.15, 6.17, 7.14, 8.16, 9.14, 10.15, 10.16).
- **No `nano_banana_pro`.**

## References (reference 1 first)

| Card | Reference 1 | Reference 2 | Reference 3 | Note |
|---|---|---|---|---|
| 6 Serpentine Whisper Chain — Silver | `7bd23f90` (01) | `25d9bbdd` (03) | `8503d83e` (scaleRef, 02_scale_crop) | as the diff table |
| 7 Charm Box Chain | `f258e0db` (03) | `5df3fb80` (02) | `acfaf09a` (scaleRef, 02_scale_crop) | as the diff table |
| 8 Brushed Gold Huggies | `7c95b6c6` (01) | `b5b784e1` (04) | none | As the diff table. The card's scaleRef `5601af98` is the same photo as reference 2 (04.jpg, the cardamom pod), so a third copy adds nothing |
| 9 Baroque Bloom Cuff | `683ba9b0` (01) | `519622c7` (02_scale_crop) | none | See below |
| 10 Triple Coil Wrap Bangle | `9ea1fd7b` (01) | `5dc75ab3` (03) | `0ea4b852` (scaleRef, 03_scale_crop) | See below |

Card 9 deviates from the generic "mediaIds" rule, on purpose:
- The diff table makes reference 2 the worn scale crop and says never to use 02.jpg (`7ea730ec`), which shows her head. Looked at: 02.jpg shows her face down from the nose.
- The crop now has a media id: `519622c7`, recorded on the product card as scaleRef after the diff was written. That is the id used, so the scale reference is in, as reference 2.

Card 10 deviates from the diff table, on purpose:
- The diff says "none on take A", but the batch rule adds the product card's scaleRef as reference 3.
- That crop (03_scale_crop) is a different, face-free image from reference 2 (03.jpg shows lips and chin).
- Learnings 11 recommends a worn scale photo for any piece that drifts large. This coil drew 1.45-1.8x wire thickness in k04-5 and k05-3.
- Its wording follows scaleRef.use, with one change: the pencil referent becomes the diff 10.5 referent (X10.2).
- The diff's redo plan (macro 02 as reference 3 if the caps miss) still stands.

## 1. Loop diff, edit by edit (brief_diff.md §1-6)

Each line gives the edit, the field, the operation and the result. The full old and new strings are in `brief_diff.md`; for prompt edits they are repeated here clause by clause.


### Camp k03

- **C1** · `idea` · replace · applied
  - why: Hard rule: never composite, move or edit a product photo.
- **C2** · `idea` · replace · applied
  - why: Kling clips start from the approved still; nothing is composited or tracked.
- **C3** · `textualGraphic` · replace · applied
  - why: Hard rule: no price sums. '45 cm' is an unlisted prop size the k03a plates never supported (verify k03-2: 25-36 cm) and the critics flagged on k03-4 V1.
- **C4** · `textualGraphic` · replace · applied
  - why: Owner ruling overrides the switched-off slot; the basket meter is this batch's new move (loop.md).
- **C5** · `brandFeatures` · replace · applied
  - why: Basket rate 0.0: every card asks for three, in the camp's chalk.
- **C6** · `sellLever` · replace · applied
  - why: Hard rule: no price sums.
- **C7** · `carouselText` · set · applied
  - why: For the k03b carousel (cards 6-10, each linking to its own product page; there is no BUY3 collection). The plan's text put BUY3 at character 178 (rule: before 125) and said 'Ten' pieces. Re-read stock on the day.

### Card 6 · Serpentine Whisper Chain — Silver

- **6.1** · `prompt` · replace · applied
  - was: `Vertical 9:16 freeze-frame macro advertising photograph, side-on, the subject centred inside the central 4:5 window.`
  - now: `Vertical 9:16 freeze-frame macro advertising photograph, side-on, a full-bleed photograph edge to edge with no borders, bands or panels: one continuous photograph fills the whole tall frame from the top edge to the bottom edge, never a square picture padded with flat colour, no frame within the frame.`
  - why: k03-3A letterbox: 'central 4:5 window' plus calm zones drew flat colour panels.
- **6.2** · `prompt` · replace · applied
  - was: `Reference 1 is the authority on this exact piece; reference 2 shows the snake chain's fine ridges and the 4 prongs.`
  - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece: use it only for the snake chain's fine ridges and the 4 prongs; its bail junction is soft, so take the bail, sitting straight on the basket with no jump ring, from reference 1; ignore its green velvet. Reference 3 shows this exact piece worn at the base of the neck at true size (40 cm, 2 mm snake chain sitting at the base of the neck, as thick as a strand of spaghetti; the 10 mm cushion stone rests in the notch between the collarbones, about a little fingernail or half a Rs 1 coin, 5 times the chain's thickness): match that scale exactly; copy only the scale, never a face, a neck or a body.`
  - why: Standard reference sentence; product card refNotes (soft bail on ref 2) and scaleRef 8503d83e as reference 3.
- **6.3** · `prompt` · after · applied
  - after: `cool bright rhodium silver tone, never the gold-tone version.`
  - inserted: ` COUNT: exactly 1 stone (one, never two), exactly 4 prongs (four), exactly 1 bail and 0 jump rings between the bail and the basket. The chain, bail, basket, prongs, extender and clasp are all the same rhodium silver tone.`
  - why: Learnings 6 and 9: counts in digits and words, one tone for every part.
- **6.4** · `prompt` · replace · applied
  - was: `SCALE: the stone is about 10mm, the size of a little fingernail and five times the chain's thickness; field of view about 7cm at the stone.`
  - now: `SCALE, set by her fingertips: field of view about 7 cm at the stone, so her two fingertips at the top edge are large in the frame, each about a fifth of the frame width; the stone is about 10 mm, the size of her little fingernail, about two thirds of the width of one fingertip pad and five times the chain's thickness; the chain is as thick as a strand of spaghetti. Never a larger stone: the stone is never as wide as her fingertip.`
  - why: k03a: numbers alone never moved scale; the crop is set by anatomy and two body referents touch the piece.
- **6.4b** · `prompt` · replace · applied
  - was: `a plain round platter about 45cm across with a rolled rim`
  - now: `a plain round platter with a rolled rim`
  - why: In a 7 cm macro the platter's size is a competing scale cue: four k03a plates framed 2-3x wider than asked (k03-1A 23 cm, k03-1R 25 cm, k03-3A 34 cm, k03-4A 23 cm against 11-12 cm).
- **6.5** · `prompt` · replace · applied
  - was: `one round bead of opaque white milk, about half the stone's height and clearly separate from it, hangs from the lowest prong of the basket, frozen the instant before it falls; a few fine milk droplets cling to the chain.`
  - now: `THREE MOMENTS IN ONE FROZEN FRAME: one drop of white milk, about half the stone's height, has just let go of the lowest prong and hangs in the air a few millimetres below the basket, joined to the prong tip only by a breaking hair-thin thread of milk, its top drawn up into a point, milky white with a translucent bluish edge, plainly liquid, never a smooth opaque pearl or bead; nothing white touches the stone; and straight below it, where the drop before it landed, a small crown of milk stands frozen up out of the milky surface at the bottom of the frame. The chain carries only a thin wet sheen, never beads or droplets.`
  - why: CRAZIER: past, present and future in one replay frame. TRUER: k03-5A's milk drip on a stone read as an added pearl, and the kit rule says a bead on the piece reads as hardware.
- **6.6** · `prompt` · replace · applied
  - was: `The upper left third is calm dark plum for a headline.`
  - now: `Above and left of the hanging chain, the same deep plum velvet falls into soft shadow, real fabric texture right up to the top edge, quiet enough for a headline; the milky band along the bottom edge stays plain apart from the one small crown, for the price card.`
  - why: Name what fills each calm zone (k03-3R fixed the letterbox this way).
- **6.7** · `prompt` · replace · applied
  - was: `LIGHT: one soft cool-neutral key from the left; one small hard specular spot from behind right fires the stone with crisp white sparkle and draws a bright line along the snake chain.`
  - now: `LIGHT: two lights only. One soft cool-neutral key from the left; one small hard specular spot from behind right fires the stone with crisp white sparkle, draws a bright line along the snake chain and makes the falling drop's edge glow. True contact where her fingertips pinch the chain, with a small true contact shadow on the skin.`
  - why: Two-light rule; a referent touching the piece with a contact shadow.
- **6.8** · `prompt` · replace · applied
  - was: `Only hands and forearms: no face, no eyes, no head. No text, letters, numbers or logos anywhere, nothing written in the mehendi. One piece of jewellery only, no star glints, no rainbow flare.`
  - now: `Only fingertips and hands: no face, no eyes, no eyebrows, no head. No text, no letters, no numbers, no logos, no watermark anywhere, nothing written in the mehendi. One product only: this one necklace is the only jewellery in the frame; no star glints, no rainbow flare.`
  - why: Exact no-face, no-text and one-product clauses.
- **6.9** · `picture` · replace · applied
  - why: Matches 6.5.
- **6.10** · `beat` · set · applied
  - why: Fix target (message 6.17): the canvas names her objection in her words; the stone's fact moves to the leader label, which already says 'CUBIC ZIRCONIA · 10 MM · STAYS'.
- **6.11a** · `layout` · replace · applied
  - why: The replay timecode leaves the device (learnings 20: one device, one label); REPLAY moves into the strip.
- **6.11** · `layout` · replace · applied
  - why: Learnings 20 (one device, at most one label); leaders end on metal, never on a stone or the liquid.
- **6.11b** · `layout` · replace · applied
  - why: Matches 6.11.
- **6.12** · `layout` · replace · applied
  - why: New move and owner ruling.
- **6.13** · `offer` · set · applied
  - why: New move.
- **6.14** · `primaryText` · set · applied
  - why: The plan's text put BUY3 at character 145 (rule: before 125). OBJECTION may carry the trust line.
- **6.15** · `motion` · replace · applied
  - why: No composite; the clip starts from the still, where the drop has already let go.
- **6.16** · `motion` · replace · applied
  - why: Matches 6.15.
- **6.17** · `risk` · replace · applied
  - why: Hard rule; k03-5A milk-bead lesson.

### Card 7 · Charm Box Chain

- **7.1** · `prompt` · replace · applied
  - was: `the camera at the level of a milk surface looking across it, the subject centred inside the central 4:5 window.`
  - now: `the camera at the level of a milk surface looking across it, a full-bleed photograph edge to edge with no borders, bands or panels: one continuous photograph fills the whole tall frame from the top edge to the bottom edge, never a square picture padded with flat colour, no frame within the frame.`
  - why: k03-3A letterbox.
- **7.2** · `prompt` · replace · applied
  - was: `Reference 1 is the authority on this exact piece; reference 2 shows its true size worn.`
  - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece worn: use it only for the charm's true size and the chain's square links; take nothing else from it: not the person, her face, clothes or background. Reference 3 shows this exact necklace worn on a woman at true size (the 50 cm box chain falls below the collarbone; the barrel charm is about 10 mm, a fingernail wide, about an eighth of the neck's width, and sits on the upper breastbone): match that scale exactly; copy only the scale, never a face.`
  - why: Standard reference sentence; scaleRef acfaf09a as reference 3.
- **7.3** · `prompt` · after · applied
  - after: `the chain keeps its small square box links, never cable, curb or rope.`
  - inserted: ` COUNT: exactly 3 pavé bands (three) and exactly 2 raised polished ribs (two); each band is 2 even rows of tiny clear stones, never 1 row of larger stones; no bail, no jump ring, no second bead. The chain, rims and ribs are all the same 18k gold tone.`
  - why: k06a k06-2 (gpt_image_2_6, passed) drew the outer bands as one row of larger stones; product morph list.
- **7.4** · `prompt` · replace · applied
  - was: `SCALE: the charm is about 10mm, about two thirds of the width of the fingertip it rests on, the size of a chickpea; field of view about 6cm; honest macro depth of field.`
  - now: `SCALE, set by the fingertip: field of view about 6 cm across, so the fingertip is large in the frame, about a quarter of the frame width; the charm is about 10 mm, as wide as her fingernail and two thirds of the fingertip's width, the size of a chickpea; the box chain is about a quarter of the charm's height; never a charm as wide as the fingertip. Honest macro depth of field.`
  - why: Two body referents touching the piece; anatomy sets the crop.
- **7.4b** · `prompt` · replace · applied
  - was: `a plain round platter about 45cm across with a rolled rim`
  - now: `a plain round platter with a rolled rim`
  - why: Same as 6.4b: no big-prop size in a 6 cm macro.
- **7.5b** · `prompt` · replace · applied
  - was: `runs back down into the milk, beaded with tiny milk droplets;`
  - now: `runs back down into the milk with a thin wet sheen and no droplets on its links;`
  - why: Kit rule: a bead on the piece reads as hardware.
- **7.5** · `prompt` · replace · applied
  - was: `the barrel charm rests on top of it with its bore running along the chain;`
  - now: `the barrel charm lies on its side across the top of it with its bore running along the chain and a small true contact shadow on the skin, the chain's weight on both sides holding it level;`
  - why: Contact shadow; the plan's risk names an unconvincing balance.
- **7.6** · `prompt` · replace · applied
  - was: `Background: deep oxblood velvet shamiana, far out of focus, with two warm fairy-light discs low near the horizon like distant ships.`
  - now: `Background: deep oxblood velvet shamiana, far out of focus, darkening toward the top like a night sky, with two warm fairy-light discs low near the horizon like distant ships; from the farther one a single long path of warm light runs across the white sea straight to the fingertip, like moonlight on water, and the fingertip stands at the exact centre of three perfectly round rings on the calm surface.`
  - why: CRAZIER: the lighthouse gets its moon path; the rings make the fingertip the bullseye the reticle locks onto.
- **7.7** · `prompt` · replace · applied
  - was: `The upper third of the frame is calm dark oxblood for a headline.`
  - now: `Above the horizon the oxblood velvet sky is plain and quiet up to the top edge, for a headline; below the horizon the white milk sea is plain and quiet down to the bottom edge, for the price card.`
  - why: Name what fills each calm zone.
- **7.8** · `prompt` · replace · applied
  - was: `LIGHT: a soft warm key from the front left; one small hard specular kicker from behind draws a thin bright rim on the fingertip and the polished ribs and puts pinpoint white sparkle in the pave.`
  - now: `LIGHT: two lights only. A soft warm key from the front left; one small hard specular kicker from behind draws a thin bright rim on the fingertip and the polished ribs and puts pinpoint white sparkle in the pavé; never a four-point star or cross glint.`
  - why: Two-light rule; product morph note (star glints).
- **7.9** · `prompt` · replace · applied
  - was: `Only hands and forearms: no face, no eyes, no head. No text, letters, numbers or logos anywhere, nothing written in the mehendi. One piece of jewellery only, no star glints, no rainbow flare.`
  - now: `Only one fingertip: no face, no eyes, no eyebrows, no head. No text, no letters, no numbers, no logos, no watermark anywhere, nothing written in the mehendi. One product only: this one necklace is the only jewellery in the frame; no star glints, no rainbow flare.`
  - why: Exact clauses.
- **7.10** · `layout` · replace · applied
  - why: 'PARAAT ABOUT 45 CM' is an unlisted prop size no plate has proved; three labels become one.
- **7.11** · `layout` · replace · applied
  - why: New move, owner ruling, magnification rule.
- **7.12** · `offer` · set · applied
  - why: New move.
- **7.13** · `primaryText` · set · applied
  - why: The plan's text put BUY3 at character 144. PAIN copy does not carry the shipping line (only OBJECTION and OFFER may); it is printed on the card.
- **7.14** · `risk` · replace · applied
  - why: Hard rule.

### Card 8 · Brushed Gold Huggies

- **8.1** · `prompt` · replace · applied
  - was: `Vertical 9:16 advertising photograph, front-on at hand height, the subject inside the central 4:5 window, lit low and warm from the side.`
  - now: `Vertical 9:16 advertising photograph, the camera a little above hand height looking slightly down onto his flat palm, a full-bleed photograph edge to edge with no borders, bands or panels: one continuous photograph fills the whole tall frame from the top edge to the bottom edge, never a square picture padded with flat colour, no frame within the frame, lit low and warm from the side.`
  - why: k03-3A letterbox; the slight downward view shows the palm as a stage for the pair.
- **8.2** · `prompt` · replace · applied
  - was: `Reference 1 is the authority on this exact piece; reference 2 shows its true size and the brushed grain (ignore the cardamom pod in it).`
  - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same pair beside a green cardamom pod at true size (each earring 14 x 9.8 mm, about the height of the pod): use it for the brushed grain and the scale, and leave the cardamom pod out of the picture.`
  - why: Standard sentence; scaleRef is the same photo, so no reference 3 (k04r k04-4).
- **8.3** · `prompt` · replace · applied
  - was: `SCALE: each earring is 14mm tall, about the height of a green cardamom pod and about a sixth of the width of the palm it stands on; field of view about 12cm.`
  - now: `SCALE, set by his hands: field of view about 12 cm, so his flat palm spans about three quarters of the frame width and each of his fingertips is about a seventh of it; each earring is 14 mm tall and 9.8 mm wide, about one twelfth of the frame width, a sixth of the palm's width, narrower than one of his fingertips and a little shorter than his thumbnail is long. Never a large hoop: earlier takes of this pair on hands came out 1.4x and 3x.`
  - why: k04r k04-4: gpt_image_2_6 draws this pair at about 1/12 of the frame whatever the text says; grow the hands to match instead of shrinking the pair.
- **8.4** · `prompt` · replace · applied
  - was: `SCENE: a young Indian man's right hand has just come up out of a wide polished brass paraat, a plain round platter about 45cm across with a rolled rim and no engraving, filled with milky water, and is held out flat, palm up, toward the camera as if renegotiating a deal, the hand a little left of centre; the pair of earrings stands upright on the dry centre of his palm, both brushed fronts facing the camera;`
  - now: `SCENE: TIME-OUT. A young Indian man, just up out of a wide polished brass paraat, a plain round platter with a rolled rim and no engraving, filled with milky water, calls a time-out with his two hands in the referee's T sign, a little left of centre: his right hand is held flat and level, palm up, as the top bar of the T, and the straight fingertips of his left hand point up and press into the middle of the back of the right hand as the T's stem; exactly two hands, both his, five fingers each with correct anatomy; the pair of earrings stands upright on the dry centre of the flat right palm, both brushed fronts facing the camera;`
  - why: CRAZIER: the sore loser's time-out is the universal T sign, so the headline is a gesture you read at 200 px; the flat top palm is still the stage.
- **8.5** · `prompt` · replace · applied
  - was: `his hand: warm medium-brown skin, short clean nails, no mehendi, an ivory raw-silk sherwani cuff and one thin red kalava thread at the wrist; no rings, no watch, no other jewellery.`
  - now: `his hands: warm medium-brown skin, short clean nails, no mehendi, ivory raw-silk sherwani cuffs, one thin red kalava thread at the right wrist; no rings, no watch, no other jewellery.`
  - why: Two hands now.
- **8.6** · `prompt` · replace · applied
  - was: `The top third and the right side of the frame are calm dark oxblood for type.`
  - now: `The right side of the frame and the space above his hands are plain dark oxblood velvet in soft vertical folds, real fabric up to the top edge, nothing in them, for a column of type.`
  - why: Name what fills each calm zone.
- **8.7** · `prompt` · replace · applied
  - was: `LIGHT: one soft warm golden key from low on the left,`
  - now: `LIGHT: two lights only. One soft warm golden key from low on the left,`
  - why: Two-light rule (the plan already has exactly two).
- **8.8** · `prompt` · replace · applied
  - was: `Only hands and forearms: no face, no eyes, no head. No text, letters, numbers or logos anywhere, nothing written in the mehendi. One piece of jewellery only, no star glints, no rainbow flare.`
  - now: `Only hands and forearms: no face, no eyes, no eyebrows, no head. No text, no letters, no numbers, no logos, no watermark anywhere, nothing written in the mehendi. One product only: this one pair of earrings is the only jewellery in the frame; no star glints, no rainbow flare.`
  - why: Exact clauses.
- **8.9** · `picture` · replace · applied
  - why: Matches 8.4.
- **8.9b** · `picture` · replace · applied
  - why: The bill is gone (8.11).
- **8.10** · `beat` · set · applied
  - why: Hard rule: no price sums (the plan's '+ about ₹190 to this bill' is a computed basket difference).
- **8.11** · `layout` · replace · applied
  - why: Hard rule: the bill was a price sum. The k03a winner's in-letter loupe replaces it, so the 14 mm pair reads at 200 px.
- **8.11a** · `layout` · replace · applied
  - why: The loupe is labelled in the strip, as RING CAM was on k03-4 (40-character strip).
- **8.12** · `layout` · replace · applied
  - why: Matches 8.11.
- **8.13** · `layout` · replace · applied
  - why: Banned word 'huggie'; new move; owner ruling.
- **8.14** · `offer` · set · applied
  - why: New move.
- **8.15** · `primaryText` · set · applied
  - why: OFFER may carry the trust line.
- **8.16** · `risk` · replace · applied
  - why: Hard rule.

### Card 9 · Baroque Bloom Cuff

- **9.1** · `prompt` · replace · applied
  - was: `the camera at the height of a brass paraat's rim, the subject centred inside the central 4:5 window.`
  - now: `the camera at the height of a brass paraat's rim, a full-bleed photograph edge to edge with no borders, bands or panels: one continuous photograph fills the whole tall frame from the top edge to the bottom edge, never a square picture padded with flat colour, no frame within the frame.`
  - why: k03-3A letterbox.
- **9.2** · `prompt` · replace · applied
  - was: `Reference 1 is the authority on this exact piece.`
  - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 shows this exact cuff worn on a wrist at true size: use it only for the cuff's size, its slim 1.5 mm wire and the sizes of the two terminals against the wrist; take nothing else from it: not the person, her clothes or background.`
  - why: Reference 2 = refs/baroque-bloom-cuff/02_scale_crop.jpg (wrist and collarbone, no face: checked). It has no media id yet: upload it once, record the id on the product card as scaleRef, and never use 02.jpg (it shows her head).
- **9.3** · `prompt` · after · applied
  - after: `never a closed bangle, never a thick wire.`
  - inserted: ` COUNT: exactly 2 terminals (two): 1 cap with exactly 1 clear stone (one) and 1 shell slab (one). The wire, cap, bezel and slab rim are all the same 18k gold tone.`
  - why: Learnings 6 and 9.
- **9.4** · `prompt` · replace · applied
  - was: `SCALE: the cuff is about 6cm across inside, its wire as thin as a matchstick; the shell slab is about the size of a thumbnail; field of view about 16cm.`
  - now: `SCALE, set by the hands: field of view about 16 cm, so the fingers are large in the frame; the cuff is about 6 cm across inside, a little narrower than her palm, its wire 1.5 mm, as thin as a matchstick and about a tenth of the width of his fingertip; the shell slab is about as tall as her thumbnail is long and the crystal cap a little smaller; never a chunky bangle, never a thick wire, never a terminal wider than a fingertip.`
  - why: Two body referents touching the piece.
- **9.5** · `prompt` · replace · applied
  - was: `From the left, a young Indian man's fingers slide it along the rim with two fingertips, the crystal cap on his side;`
  - now: `From the left, a young Indian man's fingers slide it along the rim with two fingertips, the crystal cap on his side, with a small true contact shadow where his fingertips touch the wire; behind the cuff a thin wet streak of milk on the polished brass traces the path it has slid from his side toward hers, like the mark a ball leaves on a pitch;`
  - why: CRAZIER: the fix leaves evidence: the milk trail shows he pushed it to her. Contact shadow.
- **9.6** · `prompt` · replace · applied
  - was: `The milk beyond the rim is smooth and out of focus.`
  - now: `Exactly two hands in the frame, his from the left and hers from the right, each with five fingers and correct anatomy; their fingertips never touch each other or the shell slab. The milk beyond the rim is smooth and out of focus.`
  - why: k03-3R drew a three-fingered hand in a two-hand frame.
- **9.7** · `prompt` · replace · applied
  - was: `The top third of the frame is calm and dark for a headline.`
  - now: `Above the rim the dark oxblood velvet is plain and quiet up to the top edge, for a headline; below the rim the polished brass wall of the paraat falls into soft shadow down to the bottom edge, plain enough for the price card.`
  - why: Name what fills each calm zone.
- **9.8** · `prompt` · replace · applied
  - was: `LIGHT: soft warm low tungsten raking across the rim from the left;`
  - now: `LIGHT: two lights only. Soft warm low tungsten raking across the rim from the left;`
  - why: Two-light rule.
- **9.9** · `prompt` · replace · applied
  - was: `Only hands and forearms: no face, no eyes, no head. No text, letters, numbers or logos anywhere, nothing written in the mehendi. One piece of jewellery only, no star glints, no rainbow flare.`
  - now: `Only hands and forearms: no face, no eyes, no eyebrows, no head. No text, no letters, no numbers, no logos, no watermark anywhere, nothing written in the mehendi. One product only: this one cuff is the only jewellery in the frame; no star glints, no rainbow flare.`
  - why: Exact clauses.
- **9.10** · `picture` · replace · applied
  - why: Matches 9.5.
- **9.10a** · `layout` · replace · applied
  - why: Learnings 20: one kicker line; the beat already says 'he found it first.'
- **9.10b** · `layout` · replace · applied
  - why: Two labels become one line with two leaders.
- **9.10c** · `layout` · replace · applied
  - why: Matches 9.10b.
- **9.11** · `layout` · replace · applied
  - why: New move and owner ruling.
- **9.12** · `offer` · set · applied
  - why: New move.
- **9.13** · `primaryText` · set · applied
  - why: The plan's text put BUY3 at character 130; 'crystal' becomes the listed cubic zirconia, as on the tags.
- **9.14** · `risk` · replace · applied
  - why: Hard rule.

### Card 10 · Triple Coil Wrap Bangle

- **10.1** · `prompt` · replace · applied
  - was: `Vertical 9:16 heroic advertising photograph, side-on, the subject inside the central 4:5 window.`
  - now: `Vertical 9:16 heroic advertising photograph, side-on, a full-bleed photograph edge to edge with no borders, bands or panels: one continuous photograph fills the whole tall frame from the top edge to the bottom edge, never a square picture padded with flat colour, no frame within the frame.`
  - why: k03-3A letterbox.
- **10.2** · `prompt` · replace · applied
  - was: `Reference 1 is the authority on this exact piece; reference 2 shows it worn at true scale with both caps on top of the wrist.`
  - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece worn at true scale with both caps on top of the wrist: use it only for the piece, how it sits on the wrist and its true size there; take nothing else from it: not the person, her face, lips, chin, clothes or background.`
  - why: Standard sentence; ref 03.jpg shows lips and chin (k05a flag).
- **10.3** · `prompt` · replace · applied
  - was: `1 continuous ribbed snake-coil (tubogas) wire`
  - now: `1 continuous ribbed snake-coil wire`
  - why: The word names a designer line (k05a and k04a dropped it; no real brand imitated).
- **10.4** · `prompt` · after · applied
  - after: `never a stack of separate bangles, never a smooth tube.`
  - inserted: ` COUNT, from references 1 and 2: exactly 2 full turns (two); 2 wires at the back and at both sides, and 3 wires only in the short span between the 2 offset caps at the front. PAVÉ AND CAPS, exactly as reference 1: each cap carries exactly 8 large round clear stones, 2 across and 4 down, in 4 rows of 2, each stone about 1.8 mm and almost half the cap's width, each in its own round setting with a thin line of gold tone metal between the stones; never 6 stones, never 3 rows, never a field of tiny micro-pavé. Each cap is a solid mirror-polished 18k gold tone block, twice as tall as the wire is thick and taller than it is long, with a rounded tip, as in reference 1; never a flat square plate with a raised frame. PROPORTION, as in references 1 and 2: the wire is thin and delicate, 4 mm, about as thick as a phone charging cable and about two fifths of the width of her index fingernail; the two turns together are 8 mm, narrower than her little fingernail and about half the width of her index finger; her wrist is about seven times as wide as the two turns together; the bangle is about 17 wire widths across; never a chunky, fat, heavy or tube-like coil. The wire, both caps and every stone setting are the same 18k gold tone.`
  - why: PAVÉ AND CAPS is the k05-3R wording that passed (8 stones, 2 x 4); PROPORTION is the k04-5R wording that took the coil from 1.45x to 1.15x. Four earlier takes drew 4, 6 or 40+ stones per cap.
- **10.5** · `prompt` · replace · applied
  - was: `SCALE: the two turns together are about as tall as a pencil is thick, snug just above the wrist bone; field of view about 15cm.`
  - now: `SCALE: 6 cm inside and 8 mm tall across its two turns, about half the width of her index finger, snug just above the wrist bone; field of view about 15 cm, so her raised forearm is about two fifths of the frame width.`
  - why: k04r k04-5: the pencil referent drew each wire nearer a pencil; it stays in the copy only.
- **10.6** · `prompt` · replace · applied
  - was: `Milk pours off the ribbed turns in fine glossy rivulets, dripping from the caps; below, a falling crown churns the milk.`
  - now: `Milk pours off the ribbed turns in fine glossy rivulets and drips from the lower edge of the coil, clear of both caps, whose stones stay dry and bright; but around her forearm the milk in the paraat is perfectly still, a calm white mirror with three wide perfect rings spreading out from her arm: the only still milk of the whole match, because the game is over.`
  - why: CRAZIER: after nine splashes the final is silence, an arm rising from a mirror like a monument. TRUER: milk off the stones (k03-5A).
- **10.7** · `prompt` · replace · applied
  - was: `The top quarter and the right third of the frame are calm dark oxblood for type.`
  - now: `The right side of the frame and the space above her hand are plain deep oxblood velvet in soft vertical folds, real fabric up to the top edge, with no fairy light in front of them, for a column of type.`
  - why: Name what fills each calm zone.
- **10.8** · `prompt` · replace · applied
  - was: `LIGHT: a warm amber rim light from behind left and a soft warm key from the front right; one small hard specular kicker gives every rib its own bright line and each pave stone a white catchlight.`
  - now: `LIGHT: two lights only. A soft warm key from the front right shapes the forearm; one small hard warm amber kicker from behind left is the rim light: it outlines the raised arm in amber against the oxblood, gives every rib its own bright line and each pavé stone a white catchlight.`
  - why: The plan named three lights; the amber rim is kept as the kicker (as k03-4's backlight was).
- **10.9** · `prompt` · replace · applied
  - was: `True contact where the coil meets the skin.`
  - now: `True contact where the coil meets the skin, with a thin true contact shadow along both edges of the coil.`
  - why: Contact shadow.
- **10.10** · `prompt` · replace · applied
  - was: `Only hands and forearms: no face, no eyes, no head. No text, letters, numbers or logos anywhere, nothing written in the mehendi. One piece of jewellery only, no star glints, no rainbow flare.`
  - now: `Only hands and forearms: no face, no eyes, no eyebrows, no head. No text, no letters, no numbers, no logos, no watermark anywhere, nothing written in the mehendi. One product only: this one bangle is the only jewellery in the frame; no star glints, no rainbow flare.`
  - why: Exact clauses.
- **10.11** · `picture` · replace · applied
  - why: Matches 10.6.
- **10.12** · `layout` · replace · applied
  - why: Basket rate 0.0: the closing card makes BUY3 the house's main rule.
- **10.13** · `layout` · replace · applied
  - why: Owner ruling: the trust line is on every card, even without an offer box.
- **10.14** · `primaryText` · set · applied
  - why: OFFER may carry the trust line.
- **10.15** · `motion` · replace · applied
  - why: No composite or tracking; the piece never moves.
- **10.16** · `risk` · replace · applied
  - why: k04r k04-5 redo clause 6.

## 2. Shooter conformance edits (prompt only, after the diff)


### k03-6A

- **X6.1** · replace
  - was: `Reference 2 is a detail of the same piece: use it only for`
  - now: `Reference 2 is a detail of the same piece. Use it only for`
  - why: Task rule: the exact sentence 'Reference 2 is a detail of the same piece.' (the diff joined it to the note with a colon).

### k03-7A

- **X7.1** · replace
  - was: `Reference 2 is a detail of the same piece worn: use it only for`
  - now: `Reference 2 is a detail of the same piece. It shows the necklace worn: use it only for`
  - why: Task rule: the exact reference sentence.

### k03-8A

- **X8.1** · replace
  - was: `Reference 2 is a detail of the same pair beside a green cardamom pod at true size`
  - now: `Reference 2 is a detail of the same piece. It shows the same pair beside a green cardamom pod at true size`
  - why: Task rule: the exact reference sentence.
- **X8.2** · replace
  - was: `1 pair of chunky huggie hoops,`
  - now: `1 pair of chunky wide-band hoop earrings,`
  - why: Banned-word lint: 'huggie' (the product card's lock text is not the product name).
- **X8.3** · replace
  - was: `never silver-looking, even where wet`
  - now: `never reading as silver tone, even where wet`
  - why: Banned-word lint: bare 'silver' (k03a loop: no bare metal words inside colour or negative instructions).
- **X8.4** · replace
  - was: `with a soft small shadow of each earring on the palm`
  - now: `with a small true contact shadow under each earring on the palm`
  - why: Task rule: a true contact shadow where the piece touches its referent.
- **X8.5** · after
  - after: `real fabric up to the top edge, nothing in them, for a column of type.`
  - inserted: ` Below the T, behind his forearm, the milky paraat stays plain, quiet and softly out of focus down to the bottom edge, for the price card.`
  - why: Task rule: a named calm area for the card as well as the headline (learnings 26: name what fills it).

### k03-9A

- **X9.1** · replace
  - was: `Reference 2 shows this exact cuff worn on a wrist at true size:`
  - now: `Reference 2 is a detail of the same piece. It shows this exact cuff worn on a wrist at true size:`
  - why: Task rule: the exact reference sentence (reference 2 is the worn scale crop, as diff 9.2 and the batch table say).
- **X9.2** · replace
  - was: `a plain round platter about 45cm across with a rolled rim`
  - now: `a plain round platter with a rolled rim`
  - why: Learnings 24 and diff 6.4b/7.4b: no big-prop size in a 16 cm field; the diff left it in card 9 only by omission.
- **X9.3** · replace
  - was: `the cuff's opening faces the camera so both terminals show.`
  - now: `the cuff's opening faces the camera so both terminals show, and the wire and both terminals rest on the brass with a thin true contact shadow under them.`
  - why: Task rule: a true contact shadow where the piece touches its surface (the diff gave one only at his fingertips).

### k03-10A

- **X10.1** · replace
  - was: `Reference 2 is a detail of the same piece worn at true scale with both caps on top of the wrist:`
  - now: `Reference 2 is a detail of the same piece. It shows the piece worn at true scale with both caps on top of the wrist:`
  - why: Task rule: the exact reference sentence.
- **X10.2** · after
  - after: `take nothing else from it: not the person, her face, lips, chin, clothes or background.`
  - inserted: ` Reference 3 shows this exact piece worn on the wrist at true size (6 cm inside, 4 mm wire, 8 mm tall across the 2 turns and 12 mm where the ends overlap; it sits snug just above the wrist bone, the 2-wire band about half the width of her index finger): match that scale exactly; copy only the scale, never a face; count the turns, caps and stones only from references 1 and 2, never from reference 3.`
  - why: Task rule: the product card's scaleRef (0ea4b852, 03_scale_crop.jpg) goes in as reference 3, worded as its scaleRef.use, except that its pencil referent becomes the diff 10.5 referent (k04r k04-5: 'pencil' drew each wire nearer a pencil).
- **X10.3** · replace
  - was: `a plain round platter about 45cm across with a rolled rim`
  - now: `a plain round platter with a rolled rim`
  - why: Learnings 24 and diff 6.4b/7.4b: no big-prop size in a 15 cm field.
- **X10.4** · after
  - after: `with no fairy light in front of them, for a column of type.`
  - inserted: ` The still white milk in the lower part of the frame stays plain apart from the three rings, for the price card.`
  - why: Task rule: a named calm area for the card as well as the type column.

## 3. Lint and conformance check (every final prompt)

Each final prompt was checked by script. None contains:
- diamond, real gold or solid gold;
- bare gold or silver (anything other than "gold tone", "gold-tone" or "silver tone");
- freshwater, emerald, ruby or huggie;
- tubogas, "45 cm", "pencil" or "central 4:5".

Every prompt contains:
- 9:16 and the full-bleed sentence;
- the exact sentence "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece.";
- the lock with its "must stay ..., never ..." clause;
- scale in mm against a body referent touching the piece, with a contact shadow;
- "two lights only" (one soft, one small hard specular kicker);
- named calm areas for the headline and the card;
- "no text, no letters, no numbers, no logos, no watermark" and "no face, no eyes, no eyebrows";
- "One product only".

Prompt lengths: k03-6A 4,482 characters, k03-7A 4,169, k03-8A 3,869, k03-9A 4,306, k03-10A 5,439.


## 4. Generation record

**Balance:** 95.21 credits before the shoot and 87.71 after it.

- The 7.50 difference includes other batches that share the account.
- This batch's 5 jobs are gpt_image_2_6 at medium, about 1 credit each.

**Submissions:** one `generate_image_batch` call with all five takes A.

- **Round 1:** k03-6A, k03-9A and k03-10A were accepted. k03-7A and k03-8A were refused with a 429 rate limit (`submission_failed`), so they were never submitted and cost nothing.
- **Round 2:** after about 40 s spent polling the accepted jobs, only those two were resubmitted, and both were accepted.
- **Outcome:** no failed or nsfw jobs. All 5 completed on the model requested, gpt_image_2_6, at 1520 x 2688.
- **Files:** downloaded to `pics/<slot>.png`. Job records are in `jobs.json`, and no URL is written to any file.

**Shooter's first look.** This is not the verification, which follows. Points the verifier should check first:

- **k03-6A.**
  - The three moments read: the crown, the falling drop on a thread, and the stone.
  - The piece has 1 cushion stone, 4 prongs and the bail straight on the basket with no jump ring.
  - Check whether the milk thread leaves from a prong tip or from the stone's lower edge (the gate says nothing white touches the stone).
- **k03-7A.**
  - The barrel shows 3 pavé bands between 2 ribs, the chain runs through the bore, and the box links are square.
  - The moon path and the rings are present.
  - Check the scale against the fingernail, and whether the bands hold 2 rows or about 3.
- **k03-8A.**
  - The T reads: the top palm is flat, and the stem is the fingertips of the other hand.
  - The pair matches ref 01's poses: one barrel face, one turned. The finish is brushed satin.
  - Check the scale against his fingertips.
- **k03-9A.**
  - Two hands. One clear cap faces one mother-of-pearl slab across the open gap, and the wire is slim.
  - Check the milk trail on the brass and the finger counts.
- **k03-10A.**
  - 2 turns, with the 3-wire stack between offset caps, and the arm rises from still milk with rings.
  - **But each cap carries 6 stones (2 x 3), not 8**: the k05-3 fault again.
  - A drip runs down from just below the lower cap.
  - If the verifier confirms, diff 10.16's redo applies: macro 02 (`b429323d`) as reference 3, with its wording.
