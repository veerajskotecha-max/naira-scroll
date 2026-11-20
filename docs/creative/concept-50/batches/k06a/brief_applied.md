# k06a brief applied (camp k06 UDHAAR KHATA., cards 1-5)

## Loop diff: none

None, because there is no loop note to apply:

- `batches/k06a/brief_diff.md` does not exist. The `k06a` folder did not exist before this run.
- The previous-batch loop path given (`batches//loop.md`) names no batch. It resolves to `batches/loop.md`, which does not exist, and no `loop.md` or `brief_diff.md` exists anywhere under `concept-50/batches/` (the folder holds `bakeoff`, `c01`, `k01a`, `k02a`, `k03a` and `k04a`).

What was read instead:
- the camp: `crazy100.json` camps[k06] (idea, insight, textual graphic, brand features, palette, sell lever, carousel text, changes, and ads 1-5 with their prompts, layouts, motion and risk fields), its `CRAZY100.md` section and production table, and `RULINGS.md`;
- the past verification lessons: `build/learnings.md` (wave 1), `batches/bakeoff/README.md`, the bake-off ring take on `gpt_image_2_6` (looked at), `batches/k03a/verify/k03-1.md` (the Verdant Eternity Band verification) and `batches/k04a/brief_applied.md`;
- the five product cards and their reference photos (looked at: Torsade 02 and 03, Charm Box 03 and 02, Verdant 03 and 01, Monochrome 02, Ribbon Bead pack and macro).

Take A is each card's planned `prompt` from crazy100.json. The only changes are the edits logged below: the conformance edits the batch's prompt rules require (the exact reference sentence, a referent touching the piece with a true contact shadow, two lights with the small hard specular kicker named, calm areas, the exact no-text clause, the banned-word lint) and the wave-1 learnings that apply to these five pictures (§2 scale against a touching referent, §5 full-bleed, §6 the tone of every part, the k02-1 tungsten-to-copper drift, the bake-off and k03-1 lessons on the S-wave). Each edit is an exact string replacement, applied once, in the order logged. The script is `scratchpad/k06a/build_prompts.py`.

## Take B: none

The computed task allows a take B for **0** cards in this batch (credits are limited, with 100 ads to make). The plan's production table lists hedge takes for k06-1 (the bare print in the talc) and k06-2 (the barrel under a slow shutter). They are not shot. Instead, the parts of each hedge that can live inside one prompt went into take A:

- **k06-1.** The print is spelled out as a void ("flat bare wood, darker than the dusted wood around it, never a raised rim or ridge of powder, never a ghost or shadow of a hoop"). The talc is kept a thin grey-white veil under the flash.
- **k06-2.** The barrel turns a little to show its open bore, "the chain running straight through it". The plan's own negatives against a doubled chain and streaks crossing the piece stay.

If either fails verification, the plan's hedge set-ups are the redo:
- for card 1, the twin lifted between two plum-polished fingers;
- for card 2, the barrel resting on the potli's satin with no streaks.

## Lock check

All five product-card locks are in their prompts, each with its "must stay X, never Y" clause. The plan's prompts already carried the locks almost word for word. The differences are deliberate:

- **Card 1.** "1 pair of hinged huggies, each a 20 x 18 mm round hoop" becomes "one hinged round hoop of the pair, 20 x 18 mm". One hoop is shown, as the card's variants line allows ("1 piece worn as in 03"), and "huggie" is out by lint. The plan's extra "never a smooth plain hoop" is kept.
- **Card 2.** "never a solid pavé band or a bail-hung pendant" reads "never a solid pave band or a bail". The plan's box-link and star-glint negatives are kept.
- **Card 3.** The plan's extra "never a closed full band" is kept.
- **Card 4.** "Inside plain polished 18k gold tone" reads "Inside plain polished gold tone", and the plan adds "the white stays pure white, never cream". Edit 4.2 restates "the same 18k gold tone" for every part.
- **Card 5.** "adjustable 16-19cm" is not in the prompt; the clasp is hidden under the wrist and the length is a copy fact. "a ribbon bow" reads "a fabric or metal ribbon bow".

Reference media ids are the product cards' `mediaIds`, reference 1 first:

| Slot | Ref 1 | Ref 2 |
|---|---|---|
| k06-1A | `refs/torsade-huggies/02.jpg` | `refs/torsade-huggies/03.jpg` |
| k06-2A | `refs/charm-box-chain/03.jpg` | `refs/charm-box-chain/02.jpg` |
| k06-3A | `refs/verdant-eternity-band/03.jpg` | `refs/verdant-eternity-band/01.jpg` |
| k06-4A | `refs/monochrome-enamel-hoops/02.jpg` | `refs/monochrome-enamel-hoops/01.jpg` |
| k06-5A | `ads-500/build/refs/ribbon-bead-bracelet__pack.jpg` | `ads-500/build/refs/ribbon-bead-bracelet__macro.jpg` |

## Flags for the finisher (copy and layout, not the pictures)

- **Shipping line.** The camp's brand features and sell lever say "No free-shipping footer" and "no free shipping". The owner ruling of 20 Nov (RULINGS §6) overrides both:
  - every k06 ad carries "FREE INSURED SHIPPING · CASH ON DELIVERY";
  - the OBJECTION cards (3, 4) and the OFFER card (5) may also use it in the hook and primary text;
  - no ad promises a delivery time.
- **Prices.** Ribbon Bead's `compareAtPrice` 999 is never printed or struck; the price is ₹699. Torsade's old prices (₹1,799, ₹1,299, ₹1,199) are never printed. No price sums.
- **Torsade "Pre-order."** The planned card line ends "Pre-order." The listing still carries the pre-order tag, but today's run notes say every piece is in stock at the card's price. Decide the line before the card is set; never write "ships now" for it either way.
- **Returns.** No line may claim returns or exchanges.
- **"Huggie".** The word appears only in the product name TORSADE HUGGIES (F2 card, ledger rows); body copy never uses it.
- **Card 5's hand.** The picture no longer shows fingers or nails (edit 5.4), so nothing in the layout should point at chipped plum polish on this card.
- **Card 4's water word.** The only water word in a no-claim prompt is the plan's guard "no reflections, no water" on card 4. It is a negative, kept on purpose.

## Edits to take A, edit by edit

Common to all five: the two-light edit, the full-bleed edit and the exact no-text phrase (the last three edits of each card). Card-specific edits come first.

### k06-1A · Torsade Huggies  (lint: clean)

1. Standard reference sentence (task rule). Ref 2 (03.jpg) is a worn profile with the corner of an eye at its right edge, so only the piece and its scale may be taken from it (no-face hard rule).
   - was: `Reference 1 is the authority on this exact piece; reference 2 shows it worn at true size.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows one hoop worn at true size, about a third of the ear's height; use reference 2 only for the piece and its true size, and take nothing else from it: not the person, her face, hair, skin or clothes.`

2. Lock restored word for word ("round hoop" had been dropped); "huggies" stays out (lint), and the pair is one product shown as one hoop, as the camp's truth note allows.
   - was: `Preserve the earring exactly: a hinged hoop, 20 x 18 mm,`
   - now: `Preserve the earring exactly: one hinged round hoop of the pair, 20 x 18 mm,`

3. Learnings §6 (name the tone of every part) and the k02-1 tungsten-to-copper drift.
   - was: `Mirror-polished 18k gold tone, warm-neutral yellow.`
   - now: `Mirror-polished 18k gold tone, warm-neutral yellow; the wire post in the same 18k gold tone; never orange, copper or brassy under the lamp.`

4. Scale rule (task) and learnings §2: a referent of known size touching the piece, with the count stated.
   - was: `so the hoop fills about 28% of the frame width.`
   - now: `so the hoop fills about 28% of the frame width. The referent touching it is the dropped hair tie: an ordinary black fabric hair tie, a slack loop about 45 mm across of 4 mm cord, so the hoop is a little less than half the tie's width and the rope tube is about as thick as the tie's cord; never a hoop as big as the hair tie.`

5. Scale rule (task): the hair tie moves a few mm so it touches the hoop; it is still the clue under the print.
   - was: `Just below the print lies one plain black fabric hair tie, dropped.`
   - now: `Just below the print and the hoop lies one plain black fabric hair tie, dropped, the edge of its loop just touching the hoop's lower edge, with its own true contact shadow.`

6. Card risk, with no take B this batch: the bare print drawn as a raised powder ring or a second hoop. The hedge that can live in take A is wording that makes the void unmistakable.
   - was: `with powder inside and outside the ring and crisp edges, empty.`
   - now: `with powder inside and outside the ring and crisp edges, empty. The print is a void, never a mound: flat bare wood, darker than the dusted wood around it, never a raised rim or ridge of powder, never a ghost or shadow of a hoop.`

7. Card risk: "the flash can blow the talc white and flatten the rope ridges".
   - was: `never a white pile, never a pale field.`
   - now: `never a white pile, never a pale field; under the flash the talc stays a thin grey-white veil, never blown to pure white.`

8. Two-light rule (task): names the flash as the small hard specular kicker beside the soft lamp.
   - was: `(2) hard: one small direct on-camera flash just above the lens, the main light, throwing`
   - now: `(2) hard: one small direct on-camera flash just above the lens, the main light and the small hard specular kicker, throwing`

9. Learnings §5 (letterbox padding): one wave-1 take came back as a padded square.
   - was: `candid, never glossy CGI.`
   - now: `candid, never glossy CGI. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`

10. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or labels.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no labels or printing on anything.`


### k06-2A · Charm Box Chain  (lint: clean)

1. Standard reference sentence (task rule). Ref 2 (02.jpg) shows her lips and nose, so only the piece and its scale may be taken from it (no-face hard rule).
   - was: `Reference 1 is the authority on this exact piece; reference 2 shows it worn at true size.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows the necklace worn at true size, the barrel on the upper breastbone; use reference 2 only for the piece and its true size, and take nothing else from it: not the person, her face, lips, hair, skin or camisole.`

2. Learnings §6 (name the tone of every part) and the k02-1 tungsten-to-copper drift under the sodium light.
   - was: `No star glints.`
   - now: `No star glints. Every box link, both rims and both ribs are the same 18k gold tone, warm-neutral yellow, never orange, copper or brassy; the pave stones clear and colourless.`

3. Scale rule (task) and learnings §2: referents of known size touching the piece, plus a true contact shadow (the barrel itself hangs free, so the shadow is where the chain touches the seat).
   - was: `so the barrel fills about 18% of the frame width.`
   - now: `so the barrel fills about 18% of the frame width. Referents touching the piece: the potli's knotted drawstring cord, about 3 mm thick, a little thicker than the chain, crosses the chain where it leaves the gathered neck, and the barrel is about the size of the drawstring's knot; the two strands lie over the seat's rounded front edge with a true contact shadow where they touch the vinyl. Never a barrel bigger than the knot.`

4. Card risk, with no take B this batch: the barrel hung from a bail. Showing the bore as reference 1 does proves the chain runs through it.
   - was: `its three pave bands and two ribs facing the lens,`
   - now: `its three pave bands and two ribs facing the lens, turned a little so the open bore at one end shows as in reference 1, the chain running straight through it,`

5. Calm-area rule (task): the card's layout puts the KAL pad at the left (Feed x 72, y 450, 230 x 300 px), "clear of the hanging loop", and the prompt named only the headline and strip zones.
   - was: `the bottom third is the dark footwell below the seat, calm for a strip of type.`
   - now: `the bottom third is the dark footwell below the seat, calm for a strip of type; the left quarter of the frame at mid-height, below the potli and clear of the chain, stays calm dark vinyl for a small paper card of type.`

6. Two-light rule (task): names the flash as the small hard specular kicker beside the soft lamp.
   - was: `(2) hard: one small direct on-camera flash just above the lens, the main light, throwing`
   - now: `(2) hard: one small direct on-camera flash just above the lens, the main light and the small hard specular kicker, throwing`

7. Learnings §5 (letterbox padding): one wave-1 take came back as a padded square.
   - was: `candid, never glossy CGI.`
   - now: `candid, never glossy CGI. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`

8. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or labels.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no labels or printing on anything.`


### k06-3A · Verdant Eternity Band  (lint: clean)

1. Standard reference sentence (task rule); the card's own detail note kept.
   - was: `Reference 1 is the authority on this exact piece; reference 2 shows how the ovals alternate.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows how the ovals alternate either side of the wave; ignore its plaster block too.`

2. Past verification: the bake-off ring on gpt_image_2_6 (this batch's model) drew the wave "close to a partial halo"; k03-1's verify asked for the slim two-stone wave, short back claws and cool rhodium (its take B read warm champagne under a warm key).
   - was: `never a closed full band.`
   - now: `never a closed full band. The clear pave is ONE slim line about two tiny stones wide that snakes from oval to oval: the ovals sit in a gentle zigzag, one nearer the knuckle edge of the band, the next nearer the fingertip edge, and the wave cups the half of each oval's outline that faces the middle of the band, then crosses between it and the next, so every oval has pave on one side only and bare claws on the other; never a broad sugared band, never a frame, loop or halo round any oval. Toward the back each green oval sits in 4 short claws, never a row of tall spikes. All metal, every claw and both looped tips are the same bright cool rhodium silver tone; the warm lights never tint them champagne or gold tone.`

3. Scale rule (task) and learnings §2: the size against the named finger that touches it, plus a true contact shadow (k03-1 drew this ring about 2x against its hand).
   - was: `so the ring's front fills about 28% of the frame width.`
   - now: `so the ring's front fills about 28% of the frame width. The finger it sits on is the referent touching it: the band is no wider than that finger, and her fanned fingers together fill almost the whole frame width; a true contact shadow where the band meets the skin. Never a chunky or oversized ring on a small hand.`

4. Two-light rule (task): names the flash as the small hard specular kicker beside the soft lamp.
   - was: `(2) hard: one small direct on-camera flash just above the lens, the main light, throwing`
   - now: `(2) hard: one small direct on-camera flash just above the lens, the main light and the small hard specular kicker, throwing`

5. Learnings §5 (letterbox padding): one wave-1 take came back as a padded square.
   - was: `candid, never glossy CGI.`
   - now: `candid, never glossy CGI. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`

6. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or labels.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no labels or printing on anything.`


### k06-4A · Monochrome Enamel Hoops  (lint: clean except the kept negative guard "no water")

1. Standard reference sentence (task rule); the card's own detail note kept.
   - was: `Reference 1 is the authority on this exact piece; reference 2 confirms one hoop's stripes and inside.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It confirms one hoop's stripes and its plain ribbed inside.`

2. Learnings §6 (name the tone of every part) and the k02-1 tungsten-to-copper drift.
   - was: `the white stays pure white, never cream.`
   - now: `the white stays pure white, never cream. Every rail, the inside and both posts are the same 18k gold tone, warm-neutral yellow, never orange, copper or brassy.`

3. Scale rule (task): a referent touching the piece. The hoops close the 1 cm gap so the strip of known width touches each; each still stands on its opposite colour.
   - was: `The two hoops stand upright about 1 cm either side of the brass strip:`
   - now: `The two hoops stand upright either side of the brass strip, the foot of each hoop just touching the strip's edge:`

4. Scale rule (task) and learnings §2: the count against the touching referent.
   - was: `so each hoop is about 30% of the frame width.`
   - now: `so each hoop is about 30% of the frame width. The brass strip they touch is the referent: it is 3 mm wide, so each hoop's 7 mm band is a little more than twice the strip's width and each hoop is about seven strip-widths tall.`

5. Card risk: "a black-and-white floor pulls them" into alternating bands.
   - was: `No checkerboard, no tiles, only two halves and one brass strip.`
   - now: `No checkerboard, no tiles, only two halves and one brass strip. Each hoop front shows exactly one black and one white stripe, never echoing the floor with more bands.`

6. Lint: bare "gold" in the light clause becomes "gold-tone".
   - was: `every enamel edge and gold rail stays readable`
   - now: `every enamel edge and gold-tone rail stays readable`

7. Two-light rule (task): names the flash as the small hard specular kicker beside the soft lamp.
   - was: `(2) hard: one small direct on-camera flash just above the lens, the main light, throwing`
   - now: `(2) hard: one small direct on-camera flash just above the lens, the main light and the small hard specular kicker, throwing`

8. Learnings §5 (letterbox padding): one wave-1 take came back as a padded square.
   - was: `candid, never glossy CGI.`
   - now: `candid, never glossy CGI. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`

9. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or labels.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no labels or printing on anything.`


### k06-5A · Ribbon Bead Bracelet  (lint: clean)

1. Standard reference sentence (task rule); the card's own detail note kept.
   - was: `Reference 1 is the authority on this exact piece; reference 2 is the authority on the bow.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It is the authority on the bow: two hearts points-in under the polished bar, 4 claws at the outer lobes.`

2. Learnings §6 (two-tone mistakes: name the tone of every part) and the k02-1 tungsten drift.
   - was: `never larger.`
   - now: `never larger. Every link, bead, claw, the bar and the clasp are the same 18k gold tone, warm-neutral yellow, never orange, copper or brassy; the hearts clear and colourless.`

3. Scale rule (task) and learnings §2: the size against a named body part that touches it, plus a true contact shadow (the card's risk: the bow drawn 1.3-1.5x).
   - was: `so the wrist runs edge to edge and the bow fills about 18% of the frame width.`
   - now: `so the wrist runs edge to edge and the bow fills about 18% of the frame width. The wrist it rests on is the referent touching it: the bow is a little smaller than the round knob of her wrist bone beside it, with a true soft contact shadow under the bow, the beads and the chain where they rest on the skin. Never a bow as big as the knob of the wrist.`

4. Scale truth: at a 5.5 cm field the nails are about 15 cm from the bow and cannot be in frame. Asking for them invites the model to widen the view and keep the bow large (learnings §2: the piece kept at legible size on a shrunken body). The plum polish lives on in the palette and on the cards where hands show.
   - was: `her relaxed hand at the left edge, nails short with chipped plum polish.`
   - now: `only the heel of her relaxed hand at the left edge, the rest of the hand out of frame: at this close field no fingers or nails show.`

5. Two-light rule (task): names the flash as the small hard specular kicker beside the soft lamp.
   - was: `(2) hard: one small direct on-camera flash just above the lens, the main light, throwing`
   - now: `(2) hard: one small direct on-camera flash just above the lens, the main light and the small hard specular kicker, throwing`

6. Learnings §5 (letterbox padding): one wave-1 take came back as a padded square.
   - was: `candid, never glossy CGI.`
   - now: `candid, never glossy CGI. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`

7. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or labels.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no labels or printing on anything.`


## Lint

Every prompt was checked by script (`build_prompts.py`) for:
- the banned words: diamond, real gold, solid gold, freshwater, emerald, ruby, huggie;
- bare "gold" or "silver" without "tone";
- water words in the two no-claim prompts (Torsade, Monochrome);
- the required parts: 9:16, the exact reference sentence, a must-stay / never clause, mm, a contact shadow, the soft light and the small hard specular kicker, calm areas, the exact no-text clause with "no watermark", no face, eyes or eyebrows, one product, and full-bleed.

All 5 prompts are clean, with one deliberate exception: card 4 keeps the plan's guard "no reflections, no water", a negative. "Gold" appears only as "18k gold tone", "gold tone" or "gold-tone". "Silver" appears only as "rhodium silver tone" or "silver tone".

## Generation record

- **Balance:** 264.71 before and 235.21 after.
  - This batch spent 13.75 credits: 5 pictures at 2.75 (GPT Image 2.6 transactions at 18:24:07.99Z, 18:24:08.25Z, 18:24:08.48Z, 18:24:08.81Z and 18:25:12.47Z).
  - The rest of the drop (three GPT Image 2.6 spends at 18:22:19Z, one at 18:23:25Z and a Nano Banana Pro spend at 18:25:03Z) belongs to other sessions sharing the account.
- **Model:** every job was requested and served as `gpt_image_2_6` (quality high, 2k, 9:16), at 1520 x 2688.
- **Rounds:**
  1. 18:22Z: one call with all 5 items. All 5 were refused with `submission_failed` (429), so none was submitted.
  2. 18:23Z: a resubmission of all 5. k06-2A, 3A, 4A and 5A were accepted; k06-1A was refused again (429).
  3. 18:25Z, after jobs_wait polling until the four accepted jobs were terminal (about 60 s): k06-1A alone was accepted.
- **Outcomes:** all 5 jobs completed first time. None failed or was flagged, and none had an unknown outcome, so no trigger word was removed.
- **Files:** `pics/k06-1A.png` to `pics/k06-5A.png`, downloaded unchanged. The only URLs inside them are the generator's embedded C2PA provenance certificate URLs. `jobs.json` holds no URLs.
- **Prompts:** `prompts.json` holds the prompts exactly as generated.

## Shooter's first look (not the verification pass)

Seen at contact-sheet size plus full-resolution crops of the ring, the barrel and the bow:

- **k06-1A, Torsade.**
  - One fat twisted-rope hoop lies flat in a thin talc veil on dark walnut, with the thin wire post across the top and no stones. It reads as the listing piece.
  - The print beside it is a dark, flat ring in the powder of about the hoop's outer size: a void, not a mound, and nothing in it. Check its band width: it reads thinner than the hoop's 4-5 mm tube, more an outline than a full footprint.
  - The black hair tie touches the hoop's lower edge. Against it, the hoop is about 0.55-0.6 of the tie's width (asked about 0.45), so check the scale.
  - The pink puff sits soft in the upper left, inside the headline zone.
  - The tone reads warm. Check the hue against ref 02 (the tungsten copper drift).
- **k06-2A, Charm Box.**
  - The chain escapes the knotted plum potli at the upper left, runs over the seat's worn front edge and hangs in one single loop, not doubled.
  - Sodium streaks stay in the background, top right, and never cross the piece.
  - The barrel shows 2 ribs dividing 3 pavé bands, plain rims, and the open bore at the right with the chain through it. There is no bail.
  - Count the rows: each band reads 3-4 rows deep (the lock says 2).
  - The barrel hangs at about 70% down, below centre and into the top of the strip zone (Feed y 930-1266). Check the strip and card placement.
  - The KAL-pad area at the left mid-height is calm seat.
- **k06-3A, Verdant Eternity.**
  - A mehendi hand in the display pose, back to the lens, with the ring on the middle finger. No letterforms are seen in the henna.
  - At 2x crop the clear pavé is one weaving wave that cups the upper half of one oval and the lower half of the next. That is close to ref 01's wave, with a full halo nowhere. The wave is about 2-3 stones wide, and there are 4 claws per oval.
  - The band is about as wide as the finger.
  - The fingertips reach to about 17% down, inside the top third (asked: below it), so the headline sits over the fingers. Check the scrim or Story placement.
- **k06-4A, Monochrome.**
  - The floor is black | brass strip | white, with no checkerboard.
  - Each hoop shows exactly 1 black and 1 white stripe between gold-tone rails, a ribbed gold-tone inside and a post. It is an open C, not closed, and the white reads white, not cream.
  - The left hoop stands on black and the right on white, both just off the strip. Both stand three-quarter as in ref 02.
  - The pair is large in frame as planned (6.5 cm field), centred at about 45-60% down. The upper half is calm.
- **k06-5A, Ribbon Bead.**
  - The wrist lies across red cloth, with the white tie-string knotted across the bottom third and teak at the top edge.
  - The bow shows 2 separate hearts points-in under 1 polished bar, with claws. The round beads read 3 a side, and the clasp is hidden. The bow is about 16% of the frame width.
  - Only the heel of the hand shows at the left; no fingers or nails.
  - Check that the red cloth reads as a closed bahi-khata (not just cloth) and that the cover is blank.

No generated text, logos, faces or extra jewellery were seen in any of the five. The full verification is the verifier's.
