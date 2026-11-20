# k10a brief applied (camp k10 PAINTED BIGGEST., cards 1-5)

## Loop diff: none

None, because there was no loop note to apply:

- `batches/k10a/brief_diff.md` does not exist. The `k10a` folder did not exist before this run.
- The loop path given for the previous batch (`batches//loop.md`) names no batch. It resolves to `batches/loop.md`, which does not exist.
- The only `brief_diff.md` files under `concept-50/batches/` are `k01r` and `k02r`, the wave-1 rescue notes for other cards. No `loop.md` exists anywhere.

What was read instead:

- **The camp.** `crazy100.json` camps[k10]: idea, insight, textual graphic, brand features, palette, sell lever, carousel text, changes, and ads 1-5 with their picture, prompt, layout, copy, motion and risk fields. Also its `CRAZY100.md` section, the production table (§9) and the owner rulings applied before batch 1, and `RULINGS.md`.
- **Past lessons.** `build/learnings.md` (wave 1) and `batches/bakeoff/README.md` (models and quality tier), plus the verification logs for these pieces:
  - `k01a/verify/k01-2.md` and `k05a/verify/k05-1.md` (Halo Curve Ring);
  - `k01a/verify/k01-3.md` (Verdant Circlet Studs: the four-point stars redesigned, then fixed by the redo's clause 4);
  - `k01a/verify/k01-5.md` and `k04a/verify/k04-2.md` (Toggle Link Chain: two-tone parts, an invented third chain end, scale);
  - `k06a/brief_applied.md` (the format).
- **The five product cards and their reference photos**, all looked at: Halo 02 and 01, Toggle 02 and the ads-500 clasp crop, Verdant 01 and 03, Molten Panel 01 and 02, Bold Dome 02 and 05.

Take A is each card's planned `prompt` from crazy100.json with only the edits logged below. They cover three things:

1. **Conformance edits the batch rules require:**
   - the exact reference sentence;
   - no third reference (there is no commissioned page);
   - scale in mm with a referent touching the piece, and a true contact shadow;
   - two lights, named as one soft light and one small hard specular kicker;
   - full-bleed;
   - the exact no-text clause and "no eyes, no eyebrows";
   - the banned-word lint.
2. **The wave-1 and verification lessons** that apply to these five pictures.
3. **The parts of a plan hedge that fit inside one prompt.**

Each edit is an exact string replacement, applied once, in the order logged. The script asserts that each old string occurs exactly once and that every product-card lock is still in the prompt word for word. The script is `/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/k10a/build_prompts.py`, and it also writes the machine log `edits_log.json`.

### Edits that apply to every card

- **The "a hand-painted Indian miniature" wording** (x.2) becomes "an Indian miniature painting", plus "an original composition in that school's manner, never a copy of any known or museum painting" (x.4).
  - Why: owner ruling 5 (generated art is never implied as a human commission) and the camp rule "no copy of any museum miniature".
- **The reference sentence** (x.1). The plan's "...reference 2 shows it ... A third reference, if attached, is the commissioned painting: keep it exactly as the ground, never repaint it." is replaced by the exact batch sentence: "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece."
  - A per-card guard follows it, saying what to take from reference 2 and what not to.
  - Two medias are attached; there is no reference 3.
- **Full bleed** (x.2, learnings §5): "Full-bleed 9:16 picture edge to edge: the painted paper fills the whole frame, with no painted border, margin, ruled frame, mount, table edge, bands or panels anywhere."
  - This matters on this camp: miniatures carry their own ruled borders, and the album frame is drawn in HTML.
- **Negatives** (last edit on each card). "No text, letters, numerals, script, signatures, logos or inscription panels anywhere. No painted people or deities, no faces, no eyes; animals only as tiny silhouettes." becomes:
  > No text, no letters, no numbers, no logos, no watermark: no script, signatures, seals, stamps or inscription panels anywhere in the painting. No painted people or deities, no faces, no eyes, no eyebrows; animals only as tiny flat profile silhouettes.
  - "One product only: no other jewellery, no props." is kept.
- **Light.** "LIGHT:" becomes "LIGHT, two lights only: one ...". On cards 3, 4 and 5, "one small hard kicker" becomes "one small hard specular kicker".

### Card 1 · Halo Curve Ring · SUN AND MOON.

| Edit | Change | Why |
|---|---|---|
| 1.1 | Reference sentence. Ref 2 is the worn close-up, so the guard reads: "use reference 2 only for the stones, the band and the true size, and take nothing else from it: no hand, finger, skin or dark background". | batch rule |
| 1.2 | Hand-painted wording and full bleed. | ruling 5, learnings §5 |
| 1.3 | Added after the lock: "the tiger eye's top shows a few soft irregular facet lines, never a regular checkerboard grid; the crystal stays pale champagne, faintly warm, never pink, blue or colourless white; the band and both bezels are the same warm 18k gold tone, never orange or brassy". | k01-2 verification (checkerboard facets, pink-tinted crystal); learnings §6 |
| 1.4 | Original composition, not a museum copy. | camp rule |
| 1.5 | "SCALE AND CONTACT: the ring is wider than the palace; the tiger eye is about a fingernail." becomes: the frame shows about 60 mm; the ring spans about 21 mm (35% of the width); the tiger eye is 11.8 mm. **The lower curve of the band touches the tip of the palace's tallest painted dome**, so the ring and the 20 mm palace compare edge to edge, "never twice as wide". | referent touching the piece; learnings §2 |
| 1.6 | "...one short soft real shadow..." gains "a thin dark contact line wherever the metal touches the paper". | true contact shadow |
| 1.7 | Two lights named. | batch rule |
| 1.8 | Negatives, plus "No painted sun, moon, crescent or sun disc anywhere: the two stones are the sun and the moon." | the plan's hedge clause ("no sun, no moon" repeated in the negatives), folded into A |

### Card 2 · Toggle Link Chain · THE BARAAT CAME FOR THE CLASP.

| Edit | Change | Why |
|---|---|---|
| 2.1 | Reference sentence. Ref 2 (the ads-500 clasp crop) is "the authority on the sailor ring's spring gate, push-pin nub, ribbed collar and the straight one-row stone bar; take nothing else from it: no skin, neck or body". | batch rule |
| 2.2 | Hand-painted wording and full bleed. | ruling 5, learnings §5 |
| 2.3 | Added after the lock: "Every link, the sailor ring, the bar and both jump rings are the same polished 18k gold tone, never silver tone, white metal or rose." Also: "Exactly two chain ends in the picture: the long strand that forms the road ends at the ring's barrel collar on one jump ring; a second short strand ends at the bar's one jump ring and runs off the right edge just above the gate; no third strand, no loose jump ring, no extra chain end." | k04-2 verification (invented third chain end); k01-5B two-tone fault; learnings §6 |
| 2.4 | Added: "SCALE: the frame shows about 100 mm of the painting across; the ring is 22 mm, a little bigger than a one-rupee coin, each link 4 x 11 mm; the ring rests on and overlaps the 18 mm painted gate, so the door-knocker is bigger than the door, by the old painters' rule, never bigger than about a quarter of the frame." | referent touching; learnings §2 (the toggle drew 1.4-1.8x large before) |
| 2.5 | Original composition. | camp rule |
| 2.6 | "Beside the chain walks..." becomes "On the far (upper) side of the road only, with a clear 5 mm gap of plain dune between it and the chain, walks...". | **the plan's hedge for this card, folded into take A** (take B goes to cards 3 and 4; see below) |
| 2.7 | "each animal smaller than two links and a clear finger's width from the chain. No riders, no water." becomes "each animal shorter than two links, flat brushwork on the paper, never touching, crossing or overlapping any link. No riders, mahouts, drummers or people of any kind on or beside the animals, no water." | the plan's second risk (animals merging into links); a painted rider would also bring a face |
| 2.8 | The contact line now names the bar as well as the links and the ring. | true contact shadow |
| 2.9 | Two lights named. | batch rule |
| 2.10 | Negatives. | batch rule |

### Card 3 · Verdant Circlet Studs · MADE AS REFLECTIONS.

| Edit | Change | Why |
|---|---|---|
| 3.1 | Reference sentence. Ref 2 is listing 03, "both studs of the pair from above ... the authority on how the two mirror each other; ignore its cube, background and light". | batch rule |
| 3.2 | Hand-painted wording and full bleed. | ruling 5, learnings §5 |
| 3.3 | Added after the lock: solid, bevelled, mirror-polished four-point stars with long sharp points, in one piece with the circlet; "never wire outlines, open petals, leaves, butterflies, flowers or filigree"; a smooth mirror-polished band with clean claws, "no granulated, crinkled or textured metal"; "Posts, collets, claws and stars are all the same 18k gold tone." | k01-3 verification: take A failed on exactly these, and the redo's clause 4 fixed them |
| 3.4 | Added: "The bottom of the upper stud's circlet and the top of the lower stud's circlet both just touch the painted horizon line, one from above and one from below, exactly one above the other." | the tracing proof's 3 px gate needs both studs equidistant from the fold line |
| 3.5 | "far left a tiny white pavilion about 12 mm wide..." becomes "on the far shore just left of the upper stud, a tiny white pavilion about 12 mm wide whose roof edge touches that stud's circlet...". Its lamps still face the studs. | referent touching the piece (12 mm painted pavilion against the 16.8 mm stud) |
| 3.6 | Original composition. | camp rule |
| 3.7 | "CONTACT: each stud casts..." becomes "SCALE AND CONTACT: the frame shows about 70 mm ...; each stud is 16.8 mm tall, a little taller than the 12 mm pavilion is wide, and its green stone is 10 mm", plus the contact line. | learnings §2; true contact shadow |
| 3.8 | Two lights; specular kicker. | batch rule |
| 3.9 | Negatives. | batch rule |

Water: the painted lake stays. This is the only piece in the batch tagged waterproof, and the prompt keeps "paint, not real water".

### Card 4 · Molten Panel Bangle · PARADISE, WALLED.

| Edit | Change | Why |
|---|---|---|
| 4.1 | Reference sentence. Ref 2 is the worn photo, with a face cropped at the lips, so it is guarded hard: "use reference 2 only for the band's width and its plates, and take nothing else from it: no person, face, lips, hand, skin or clothes". | batch rule; no faces |
| 4.2 | Hand-painted wording and full bleed. | ruling 5, learnings §5 |
| 4.3 | Added after the lock: "Lying flat, the band is a low wall about 10 mm tall round a circle about 60 mm across: six band widths fit across the circle, as in reference 1, never a tall drum. Every plate is the same mirror-polished 18k gold tone." | the card's morph (drawn 1.5-2x too wide in 5 of 8 takes, once as a cuff), answered with the hero's own proportion (outer height about 6 band widths); learnings §6 |
| 4.4 | Original composition. | camp rule |
| 4.5 | Added the field: "the frame shows about 90 mm of the painting across; the band is 10 mm, about a fingernail wide". | learnings §2 |
| 4.6 | Contact line all round where the band meets the paper. The lead elephant still touches the band; it is the referent touching the piece. | true contact shadow |
| 4.7 | Two lights; specular kicker. | batch rule |
| 4.8 | Negatives. | batch rule |

The plan prints no row count in copy (ruling 6). The prompt keeps the product card's 5-row lock, and the verifier counts rows against references 01 and 02.

### Card 5 · Bold Dome Huggies · DOME, GATE, WALL.

| Edit | Change | Why |
|---|---|---|
| 5.1 | Reference sentence. Ref 2 is the cardamom-pod scale photo: "use reference 2 only for the true size, the knobs, the seams and the taper, and take nothing else from it: no cardamom pod, no plaster". | batch rule; the product card says to drop the pod |
| 5.2 | Hand-painted wording and full bleed. | ruling 5, learnings §5 |
| 5.3 | Added after the lock: "On each hoop the slim hinge wire is visible across the top gap, so the C stays open at the top and never closes into a solid ring; the hinge wire and its knob are the same 18k gold tone; no ribs, twists, hammering or stones." | the card's second morph; learnings §6 |
| 5.4 | Original composition. | camp rule |
| 5.5 | "saffron-to-pale-gold sky" becomes "saffron-to-pale-honey sky". | banned-word lint ("gold" alone) |
| 5.6 | "each hoop is about three times as tall as the tallest painted dome" now opens with "the frame shows about 65 mm ...; each hoop is 16 mm, a little smaller than a one-rupee coin; **the front hoop's foot touches a painted 5 mm dome beside it**", and ends "never a 25-30 mm statement hoop". | referent touching; the card's morph (blown up to 25-30 mm) |
| 5.7 | Two lights; specular kicker. | batch rule |
| 5.8 | Negatives. | batch rule |

## Take B: two cards, k10-3 and k10-4 (seedream_v5_pro, 2k)

**Why these two.** The plan's table lists hedges for k10-2 and k10-3. The task asks for the two cards whose idea is hardest for the image model, judged by each card's risk field and by past verification lessons.

- **k10-3 stays.** Its main risk is geometric: a mirrored twin turned 180 degrees so that it reads as the reflection across the horizon. A model can easily return two identical studs or put the pearl on the wrong side, and the tracing proof dies on a 3 px gate. On top of that, this stud's two stars were redesigned on its last shoot (k01-3A).
- **k10-4 replaces k10-2.**
  - The Molten Panel's documented failure rate is the worst in the batch. Higgsfield drew it 1.5-2x too wide in 5 of 8 takes and once as a cuff, and drift back to the old strap or mesh is listed. This card also asks for the band at a new angle (lying flat at 45 degrees, not standing on its rim as in ref 1), with an elephant touching it and a charbagh that pulls water channels in.
  - The Toggle's main risk, the clasp, is the one the bake-off settled on this exact model: `gpt_image_2_6` held the sailor gate, nub and straight stone bar at both high and medium quality.
  - k10-2's own hedge (the procession on the far side of the road with a clear gap) fits in one prompt, so it went into take A (edit 2.6).
  - If k10-2A fails, the plan's one redo per card still applies.

**k10-3B · the hedge** (the plan's own hedge, kept equally bold):

- Both studs lie face up and upright side by side above the horizon, mirror images across a vertical centre line, exactly as in reference 2 (listing 03). The big pearls face each other in the middle and the stars sit on the outer sides.
- This hedges the riskiest element: the model copies a layout it can see rather than computing a 180-degree mirrored turn.
- Two new elements keep it as bold as A:
  - A perfectly symmetrical tiny white pavilion (12 mm) stands on the axis between them, with its central spire as the fold line. Each stud's circlet touches one side of its roof, which is the touching referent. Its lamps glow on both sides, each facing its stud ("everything faces the jewel").
  - "No moon is painted: the two green stones are the twin moons."
- The horizon is at 47%, with the calm painted lake below for type. In HTML, the tracing slip folds sideways along the spire.
- Every other clause matches take A: lock, stars, metal, scale, light and negatives.

**k10-4B · the hedge** (the riskiest elements are the band's width and pattern, and the elephant merging into the band):

- The camera rises from about 45 to about 60 degrees, "like looking down on a walled garden from a tall hill". The garden reads more as the old map-like plan, and a too-tall wall shows less, while the near side still shows its brick courses.
- I did not take the plan's straight 90-degree top-down. From directly above, a flat-lying bangle shows its rim and inner face, not the plates on its outer face. A model would be likely to redesign it as a flat plated washer, which is a worse construction risk.
- The lead elephant "stops about 2 mm short of the band, still waiting, with a clear strip of plain buff paper between its forehead and the metal". This is the plan's hedge, so the layout's ‡ note becomes "STILL WAITING", and the band's real shadow now falls outward toward the queue.
- The band takes about 60% of the frame width (A: 62%). The six-band-widths proportion, the lock and every other clause match A.
- The second model also hedges construction: in the bake-off, seedream gave the best fine construction (the open plait).

## Lock check

All five product-card locks are in their prompts word for word, each with its "must stay X, never Y" clause, and so are both B prompts. The script checks this, and every insertion comes after the lock sentence. Nothing in any lock was shortened.

Banned-word lint, run on all seven prompts, is clean:
- no "diamond", "real gold", "solid gold", "freshwater", "emerald" or "ruby";
- no "huggie";
- every "gold" or "silver" is followed by "tone".

"golden-brown" (the tiger eye) and "golden-city" (the painting school) are not metal words. Each prompt also contains the required strings: 9:16, the reference sentence, the no-text clause, no eyes and eyebrows, one product only, the specular kicker, contact, and mm.

Reference media ids are the product cards' `mediaIds`, reference 1 first:

| Slot | Ref 1 | Ref 2 |
|---|---|---|
| k10-1A | `refs/halo-curve-ring/02.jpg` (ac8bad23…) | `refs/halo-curve-ring/01.jpg` (d99052b5…) |
| k10-2A | `refs/toggle-link-chain/02.jpg` (d3c384eb…) | `ads-500/build/refs/toggle-link-chain__clasp.jpg` (59d6c393…) |
| k10-3A, k10-3B | `refs/verdant-circlet-studs/01.jpg` (ef075ae6…) | `refs/verdant-circlet-studs/03.jpg` (d7f77110…) |
| k10-4A, k10-4B | `refs/molten-panel-bracelet/01.jpg` (72962237…) | `refs/molten-panel-bracelet/02.jpg` (ebab2107…) |
| k10-5A | `refs/bold-dome-huggies/02.jpg` (c524c1be…) | `refs/bold-dome-huggies/05.jpg` (da442fe7…) |

## Flags for the finisher (copy and layout, not the pictures)

- **No painter, no commission (owner ruling 5 and the hard rule on generated art).** Several parts of the camp bible assume a living painter and cannot ship as written:
  - "THE GRAFT" (a commissioned living Rajasthani painter);
  - the PAINTER'S CREDIT line (8): "Painted for Naira by [painter], [town] · gouache on wasli · the jewellery is real";
  - "A credited living painter" in the insight;
  - "Naira commissions artists" in brand features;
  - the carousel text's "we laid real jewellery on hand-painted miniatures".

  Drop the credit line. Rewrite the carousel line as, for example, "we laid real jewellery on painted miniatures" or "miniature-style paintings". Neither copy nor captions may say hand-painted or commissioned.
- **Shipping line.** The camp's brand features keep "INSURED SHIPPING · CASH ON DELIVERY" with FREE switched off until checkout is fixed, and changes §20 says the same. The owner ruling of 20 Nov overrides both: every k10 ad carries "FREE INSURED SHIPPING · CASH ON DELIVERY". Cards 3 and 4 (OBJECTION) and card 5 (OFFER) may also use it in the hook and primary text. No delivery times.
- **No price sums or compare-at.** The sell lever's basket arithmetic must not be printed: "₹999 + ₹999 + ₹999 = ₹2,997, about ₹2,398 after BUY3". Bold Dome's compare-at of ₹1,429 must never appear. Card 5 prints the code (BUY3, 20% off any three), not a total.
- **No BUY3 collection.** Every card, including card 5's "BUILD THE PALACE", links to its own product page.
- **Scale caption.** Every card already carries the hieratic caption with the real size. That is the type that owns the giant-on-a-small-world joke. Keep it on every crop, and recompute px per mm on each plate as the camp says.
- **k10-4B.** If B is chosen, card 4's ‡ footnote becomes "the elephants are still waiting outside" (the plan's hedge label "STILL WAITING"), since the lead elephant does not touch the band.
- **Card 1 claims.** Its card line says "waterproof". This is allowed: the Halo Curve carries the Waterproof tag. Its picture is dry anyway.
- **"Huggie" stays out of all printed copy.** The F2 name is BOLD DOME. The product title appears only on the landing page.
