# k07a brief applied (camp k07 BIJLI GAYI., cards 1-5)

## Loop diff: none

There was no loop note to apply:

- `batches/k07a/brief_diff.md` does not exist. The `k07a` folder did not exist before this run.
- The previous-batch loop path given (`batches//loop.md`) names no batch. It resolves to `batches/loop.md`, which does not exist.
- No `loop.md` exists anywhere under `concept-50/batches/`. The only `brief_diff.md` files are in `k01r` and `k02r`, and they belong to those camps' redo batches, not to k07.

What was read instead:
- **The camp:** `crazy100.json` camps[k07] (idea, insight, textual graphic, brand features, palette, sell lever, carousel text, changes and ads 1-5 with their prompts, layouts, motion and risk fields), its `CRAZY100.md` section and production table, and `RULINGS.md`.
- **The past lessons:**
  - `build/learnings.md` (wave 1) and `batches/bakeoff/README.md`;
  - `ads-500/RULINGS.md` §4, the 19 Nov framing ruling: the subject is centred and sized as a share of the frame height, with no percentage positions;
  - the verification notes for these exact pieces: `k01a/verify/k01-5.md` and `k04a/verify/k04-2.md` (Toggle), `k02a/verify/k02-5.md` (Verdant Cushion), and `k01a/verify/k01-1.md`, `k03a/verify/k03-2.md` and `k04a/verify/k04-1.md` (Woven);
  - concept-camps `build/verify/toggle_r1.json` and `toggle_r3.json` (the toggle-on-a-switch set-up);
  - the wave-2 verifies `k05a` and `k06a`: GPT Image 2.6 frames tighter than asked, places pieces low and ignores bare referent clauses.
- **The pieces:** the five product cards, with both reference photos of each looked at.

Take A is each card's planned `prompt` from crazy100.json. The only changes are the edits logged below, each an exact string replacement applied once and in order. They are of three kinds:
1. **Conformance** with this batch's prompt rules:
   - the exact reference sentence;
   - a referent touching the piece with a true contact shadow;
   - the soft light and the small hard specular kicker named;
   - calm areas named for the headline and the card;
   - the exact no-text clause with "no watermark";
   - no eyes, eyebrows or faces;
   - full-bleed;
   - the banned-word lint.
2. **Learnings:**
   - §2 (scale drifts large: counts against the referent and never-limits);
   - §3 (faces creep in);
   - §5 (letterbox padding);
   - §6 (the tone of every part).
3. **Verification lessons and card risks** for these exact pieces.

No idea was tamed. Every light, hour, prop, angle, field of view and share of the frame from the plan is kept word for word. The 19 Nov ruling's "about a fifth / a sixth of the frame height" shares stay untouched, and no percentage positions were added. The script is `scratchpad/k07a/build_prompts.py`.

## Take B: 2 cards, k07-1 and k07-4

The computed task allows a take B for **2** cards. The card risk fields and past verification decide which, and they agree with the plan's production table (hedge takes k07-1 and k07-4):

- **k07-1, Toggle Link Chain: the hardest piece in this run.**
  - Every Toggle take has failed verification so far:
    - k01-5 A and B: scale, and a two-tone fault;
    - k04-2 A, B and R: a redesigned ring, an invented third chain end, the clasp placed low;
    - concept-camps r1 and r3: the bar too long, a lumpy connector.
  - The card adds a new geometry: the ring hooked over a switch lever with the bar threaded through it. The risk field names a fused ring and lever, a lost gate and nub, a bar stretched to the ring's length, and gold going pale or greenish under moonlight.
- **k07-4, Bold Nocturne Bracelet: an anatomy risk.**
  - A cupped "bulb" hand raised overhead, seen from below, is the pose image models draw worst. The risk field names finger count, a twisted wrist and a real bulb in the hand.
  - Past lessons agree: in k04-1 the hands drove the piece's scale wrong, in k05-2 a hand turned the ring 90°, and in ads-500 a "relaxed hand" came out as a fist.
- **Not hedged:**
  - card 2, Prism: stone order and pearl count. A take A lock risk, verified on the plate.
  - card 3, Verdant Cushion: passed at k02-5 on a weaker model.
  - card 5, Woven: GPT Image 2.6 medium matched the braid, disc and latch in the quality test.
  - Their risks are hedged inside take A (edits 2.3-2.5, 3.4-3.7 and 5.3-5.6).

Each take B starts from the finished take A and keeps the same idea, light, world and copy. It swaps only the riskiest element and runs on `seedream_v5_pro`, so a second model doubles the odds of a faithful take.

- **k07-1B.**
  - **The swap:** the lever carries a paperclip link, the second one along from the bar's jump ring. The closed clasp hangs free about 2 cm below the lever, in front of the dome's lower edge, so the ring touches only its own jump ring and the bar. The toggle is still on the switch, so "TOGGLE ON." stays literal, and the two strands still run down the wall like wiring.
  - **The moonlight:** it stays as an even soft cool wash. The lattice moves to the far left edge, never on the metal, so the warm kicker is the only light on the clasp. This is the plan hedge's "warm kicker only", but it keeps the CHAANDNI cue.
  - **The bar's physics are corrected for this pose:** it lies across the ring's upper inside edge, as in reference 2, with the ring hanging from it.
  - **Field of view:** 12 cm, the plan hedge's figure.
- **k07-4B.** The plan's own hedge:
  - the same raised forearm in the same shamiana, bokeh and light;
  - the hand open and relaxed, the back of the hand to the camera, the fingers together and pointing up;
  - no "screwing a bulb" wording;
  - "BULB LAGAO." in the type carries the step.

## Lock check

All five product-card locks are in their prompts with their "must stay X, never Y" clauses. The plan prompts already carried them almost word for word, and the remaining differences are deliberate:

- **Card 1:** "Must stay ..." reads "It must stay ...".
- **Card 2:** the plan adds "blue or green" to the never-list and spells out the mirror order.
- **Card 3:** the plan adds "the green stays a cushion in a smooth bezel, never claws; the metal never gold tone" (edit 3.2 fixes the lint).
- **Card 4:** the plan adds "links stay thick flat-edged rectangles, never dainty, cable or curb".
- **Card 5:** "Must stay" reads "They must stay", and the plan adds "both hoops are identical round circles".

Reference media ids are the product cards' `mediaIds`, reference 1 first:

| Slot | Ref 1 | Ref 2 |
|---|---|---|
| k07-1A, k07-1B | `d3c384eb-487e-44e3-806d-e845a3ed32d1` = `refs/toggle-link-chain/02.jpg` | `59d6c393-8659-4dd3-bc2e-2aa573412eb7` = `ads-500/build/refs/toggle-link-chain__clasp.jpg` |
| k07-2A | `47443201-a8bb-41ed-92ce-5184a8dc6757` = `refs/prism-cluster-studs-silver/03.jpg` | `60f7ac77-dfff-4ad7-96a5-6940e81fe346` = `refs/prism-cluster-studs-silver/04.jpg` |
| k07-3A | `2e74b8da-0880-4031-8e98-480217f1108e` = `refs/verdant-cushion-studs/03.jpg` | `1febd798-3286-4d1f-8806-fc4a26863378` = `refs/verdant-cushion-studs/04.jpg` |
| k07-4A, k07-4B | `92bae303-ca38-4b9f-b595-f94c292202e2` = `refs/bold-nocturne-bracelet/01.jpg` | `a7807ef5-18a6-4435-946e-32b5949de8e3` = `refs/bold-nocturne-bracelet/02.jpg` |
| k07-5A | `74ed9a2b-4781-4ab8-b032-fd1b45e847ca` = `refs/woven-gold-hoops/01.jpg` | `b77ec5ba-42ce-4a11-99a0-b8aca88138df` = `refs/woven-gold-hoops/03.jpg` |

## Flags for the finisher (copy and layout, not the pictures)

- **Shipping line.**
  - The k01 selection note ("CASH ON DELIVERY only, never free shipping") is overridden by the owner ruling of 20 Nov (RULINGS §6). Every k07 ad carries "FREE INSURED SHIPPING · CASH ON DELIVERY".
  - The OBJECTION card (3) and the OFFER card (5) may also use it in the hook and primary text.
  - No delivery time is promised. The planned primary texts carry no shipping line, so add it.
- **Pre-order.** The sell lever says the Prism and the Verdant Cushion "say 'pre-order'", and their F2 cards print PRE-ORDER. The task's live note says every piece is in stock at the card's price. Decide the line before the card is set, and never promise dispatch either way.
- **Returns.** No line may claim returns or exchanges.
- **Prices.** Live card prices: Toggle ₹999, Prism ₹1,299, Verdant Cushion ₹1,099, Bold Nocturne ₹1,599, Woven ₹1,049. No compare-at, struck prices or price sums. The plan's offer boxes (BUY2 · 10% OFF, BUY3 · 20% OFF) match the live codes.
- **Claims.**
  - Waterproof and tarnish free are printed only on Bold Nocturne (card 4) and Woven (card 5), whose cards carry the tags.
  - The Toggle shows no waterproof claim and no water, as its card rules.
  - The Prism and the Verdant Cushion carry no claims.
- **Banned words in planned copy.** None were found in the five cards' headlines, beats, card lines or primary texts. "Yellow emerald cut" appears only in the prompt lock, as the name of a cut. The Prism beat says "clean cuts", not "emerald".
- **Card 3's leader "ITS OWN GREEN LIGHT".** Print it only if the plate shows the green patch; in k07-3A it does, under the face-up stud.

## Edits, edit by edit

Every take A carries the full-bleed edit, the exact no-text clause and the face clause. Card-specific edits sit between them, in the order applied. Each take B lists only its own edits on top of its take A.

### k07-1A · Toggle Link Chain  (lint: clean)

Starts from the plan prompt.

1. Learnings §5 (letterbox padding): one wave-1 take came back as a square padded with bands.
   - was: `vertical 9:16,`
   - now: `vertical 9:16, a full-bleed photograph edge to edge with no borders, bands or panels,`

2. Standard reference sentence (task rule). Ref 2 is the clasp crop the k04a verifier used as the gate: its gate, barrel, nub and ribs are spelled out because k04-2A redesigned the ring (two ribbed collars, nub on top, no gate step).
   - was: `Reference 1 is the authority on this exact necklace; reference 2 on its clasp.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It is the authority on the clasp: copy from it the ring's flat cut end and its slimmer gate, the barrel collar beside the gate with the chain's jump ring round it, the small push-pin nub pointing outward with two or three ribbed grooves beside it, and the straight one-row stone bar on its own jump ring; ignore the skin.`

3. Verification lessons: k04a/verify/k04-2.md (an invented third chain end; the topology clause that fixed it) and concept-camps toggle_r1/r3 (a lumpy connector at the ring); learnings §6 (tone of every part) and this card's own risk ("under moonlight the 18k gold tone can go pale or greenish").
   - was: `Do not redesign or add anything. THE WORLD:`
   - now: `Do not redesign or add anything. The chain has exactly two ends, both at the clasp: one joined to the outer end of the bar by the bar's one jump ring, the other joined to the ring by the one jump ring round its barrel collar beside the gate. Nothing else is attached to the ring: no extra link, chain end, clip or lumpy connector anywhere. Every link, the ring, its gate, the bar's setting and both jump rings are the same warm polished 18k gold tone; the cool moonlight never turns the metal pale, greenish, grey or silver tone, and the warm kicker keeps it warm yellow. THE WORLD:`

4. Scale rule (task: a referent touching the piece with a true contact shadow) and learnings §2 (scale drifts 1.35-2x; give counts against the referent and a never-limit). The ring-to-link and bar-to-ring ratios are the k04-2 re-verify gate.
   - was: `SCALE: the ring is 22 mm, half the dome's width; each link the length of a basmati grain; a dark contact shadow where the ring meets the lever.`
   - now: `SCALE: the ring is 22 mm, half the dome's width, so two rings side by side would just span the dome, never a ring bigger than half the dome; the ring is about two paperclip links long and the bar about two thirds of the ring's width; each link the length of a basmati grain; a dark contact shadow where the ring meets the lever, and soft contact shadows where the strands lie against the limewash.`

5. Calm-area rule (task): names the headline and card zones.
   - was: `calm dark wall above and below for type.`
   - now: `calm dark wall above for the headline and below for the card.`

6. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or markings.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no markings or printing on anything.`

7. No eyes, eyebrows or faces (hard rule), made explicit.
   - was: `No hands, no faces.`
   - now: `No hands, no people, no faces, no eyes, no eyebrows.`


### k07-1B · Toggle Link Chain (take B, the hedge)  (lint: clean)

Starts from take k07-1A as sent.

1. HEDGE (card risk 1: the ring fused with the lever, the gate and nub lost, the bar stretched): the lever carries a paperclip link, which a model draws easily, and the clasp hangs free just below it, so the ring touches only its own jump ring and the bar. The pun stays literal: the toggle is still on the switch.
   - was: `The closed necklace hangs by its sailor ring, hooked over the lever like a key ring on a peg, in front of the dome's lower half; the stone-set bar is threaded through the ring and rests across its lower inside edge, facing the camera. Both strands drop straight down the wall side by side,`
   - now: `The ring never touches the switch: the closed necklace hangs from the lever by one of its own paperclip links, the second link along from the bar's jump ring, hooked over the lever like a key ring on a peg. The closed clasp hangs free about 2 cm below the lever, in front of the dome's lower edge, turned to face the camera: the stone-set bar threaded through the ring and lying across its upper inside edge as in reference 2, the ring hanging from it, the gate and the push-pin nub at the ring's side, crisp and sharp. From the hooked link and from the clasp the two strands drop straight down the wall side by side,`

2. HEDGE: the new contact point gets its own size.
   - was: `SCALE: the ring is 22 mm, half the dome's width,`
   - now: `SCALE: the hooked link is 11 mm long, a quarter of the dome's width; the ring is 22 mm, half the dome's width,`

3. HEDGE: the contact shadow moves to the new contact point.
   - was: `a dark contact shadow where the ring meets the lever,`
   - now: `a dark contact shadow where the hooked link meets the lever, the clasp's own small shadow on the wall just behind it,`

4. HEDGE (card risk 2: the gold tone going pale or greenish under moonlight; the plan's hedge drops the lattice): the lattice stays as the CHAANDNI cue but never touches the metal.
   - was: `Cool moonlight through an old iron window grille lays a soft pale lattice across the left of the wall, its edge just reaching the switch.`
   - now: `Cool moonlight through an old iron window grille lays a soft pale lattice across the far left edge of the wall only, well clear of the switch and the chain; the rest of the wall gets an even, soft, cool moonlit wash.`

5. HEDGE: the warm kicker is the only light on the piece.
   - was: `The soft moonlit lattice is the fill;`
   - now: `The soft moonlit wash is the fill and never falls on the metal;`

6. HEDGE: the plan's hedge field of view (12 cm), which keeps the strands, the switch and the clasp in frame.
   - was: `Field of view about 10 cm wide;`
   - now: `Field of view about 12 cm wide;`


### k07-2A · Prism Cluster Studs  (lint: clean)

Starts from the plan prompt.

1. Learnings §5 (letterbox padding): one wave-1 take came back as a square padded with bands.
   - was: `vertical 9:16,`
   - now: `vertical 9:16, a full-bleed photograph edge to edge with no borders, bands or panels,`

2. Standard reference sentence (task rule). Ref 2 (04.jpg) shows her lips and nose, so only the piece and its scale may be taken from it (no-face hard rule).
   - was: `Reference 1 is the authority on this exact pair; reference 2 shows their true size worn.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows the pair worn at true size, each arc about the width of the earlobe; use reference 2 only for the piece and its true size, and take nothing else from it: not the person, her face, lips, nose, hair, skin or slip.`

3. Learnings §6 (two-tone mistakes): name the tone of every part. The card's risk: warm match light shifts the colours; the metal is named too.
   - was: `Rhodium silver tone, high polish, bead-tipped claws on every stone and pearl.`
   - now: `Rhodium silver tone, high polish, bead-tipped claws on every stone and pearl. Every claw, setting and post is the same bright cool rhodium silver tone; the warm match glow never tints the metal gold tone or brass.`

4. Product card morph field: models straighten the arc into a bar and grow the pearls to stone size.
   - was: `Do not redesign or add anything. THE WORLD:`
   - now: `Do not redesign or add anything. Each arc stays a gentle curve, never straightened into a bar; each pearl is a pinhead about 2 mm, never as big as a stone. THE WORLD:`

5. Scale rule (task) and learnings §2: a count against the touching referent (the tray) and a never-limit. Listing photo 02 already renders the arc 1.5x.
   - was: `dark contact shadows in the tray.`
   - now: `the box's 36 mm short side is nearly twice a stud's length, never a stud as long as the box is wide; a dark contact shadow where each stud rests on the tray floor.`

6. Two-light rule (task): names the small hard specular kicker beside the soft match glow.
   - was: `one small hard neutral-white kicker from the upper right`
   - now: `one small hard neutral-white specular kicker from the upper right`

7. Calm-area rule (task): names the headline and card zones.
   - was: `calm dark above it with only the smoke, and calm dark teak below, for type.`
   - now: `calm dark above it with only the smoke, for the headline, and calm dark teak below, for the card.`

8. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or markings.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no markings or printing on anything.`

9. No eyes, eyebrows or faces (hard rule), made explicit.
   - was: `No hands, no faces.`
   - now: `No hands, no people, no faces, no eyes, no eyebrows.`


### k07-3A · Verdant Cushion Studs  (lint: clean)

Starts from the plan prompt.

1. Learnings §5 (letterbox padding): one wave-1 take came back as a square padded with bands.
   - was: `vertical 9:16,`
   - now: `vertical 9:16, a full-bleed photograph edge to edge with no borders, bands or panels,`

2. Standard reference sentence (task rule). Ref 2 (04.jpg) shows the corner of an eye and a brow at its left edge, so only the piece and its scale may be taken from it (no-face hard rule).
   - was: `Reference 1 is the authority on this exact pair; reference 2 shows the true size worn.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows one stud worn at true size, covering most of the earlobe; use reference 2 only for the piece and its true size, and take nothing else from it: not the person, her face, eye, eyebrow, cheek, hair, skin or clothes.`

3. Lint: bare "gold" becomes "gold tone". Learnings §6 (two-tone mistakes): name the tone of every part. The card's morph field: listing photo 06 already shows a gold tone stud.
   - was: `the green stays a cushion in a smooth bezel, never claws; the metal never gold.`
   - now: `the green stays a cushion in a smooth bezel, never claws; the metal never gold tone. Every prong, ball tip, bezel rim and post is the same bright cool rhodium silver tone.`

4. Card risk: "the torch circle rendering as a soft vignette instead of a hard edge". With no take B for this card, the hedge lives in take A.
   - was: `casts one hard-edged circle of clean white light about 5 cm across on the silk;`
   - now: `casts one hard-edged circle of clean white light about 5 cm across on the silk, its rim as crisp as a coin's edge, never a soft vignette;`

5. No water imagery for a piece without a waterproof claim (hard rule): "pool" becomes "patch", and the card risk ("may come out as a blob or a stain") is named as a negative.
   - was: `a small soft pool of clean green light falls on the silk inside the face-up stud's shadow, the way a clear coloured stone throws its colour.`
   - now: `a small soft patch of clean green light falls on the silk inside the face-up stud's shadow, the way a clear coloured stone throws its colour; it is coloured light only, never a liquid, stain, blob or wet mark.`

6. Scale rule (task): a referent touching the piece. The cone, the card's named referent, moves a few mm so its tip touches the tipped stud; it still sits at the circle's rim as the plan draws it.
   - was: `At the circle's dark rim lies the tip of a mehendi cone in plain clear cellophane, 2.5 cm thick, and beyond it the faint rim of a brass thaali.`
   - now: `A mehendi cone in plain clear cellophane, 2.5 cm thick, lies with its body in the dark beyond the circle's rim and only its pointed tip crossing the rim, the tip just touching the end of the tipped stud's post; beyond it the faint rim of a brass thaali.`

7. Scale rule (task) and learnings §2: counts against the touching referent and a never-limit.
   - was: `SCALE: each stud 13 mm, half the cone's thickness, a fingertip wide; dark contact shadows on the silk.`
   - now: `SCALE: each stud 13 mm, half the cone's thickness, a fingertip wide, never as wide as the cone; the torch circle nearly four studs across; dark contact shadows on the silk under each stud and under the cone's tip where it touches the post.`

8. Calm-area rule (task): names the headline, inset and card zones.
   - was: `calm dark above and to the right for a headline and an inset; calm dark silk below.`
   - now: `calm dark above and to the right for the headline and the torch-test inset; calm dark silk below for the card.`

9. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or markings.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no markings or printing on anything.`

10. No eyes, eyebrows or faces (hard rule), made explicit. "No henna" is narrowed so it cannot be read as "no mehendi cone".
   - was: `No hands, no faces, no henna.`
   - now: `No hands, no people, no faces, no eyes, no eyebrows, no henna marks or patterns on the silk.`


### k07-4A · Bold Nocturne Bracelet  (lint: clean)

Starts from the plan prompt.

1. Learnings §5 (letterbox padding): one wave-1 take came back as a square padded with bands.
   - was: `vertical 9:16,`
   - now: `vertical 9:16, a full-bleed photograph edge to edge with no borders, bands or panels,`

2. Standard reference sentence (task rule). Ref 2 (02.jpg) shows her lips and nose, so only the piece and its scale may be taken from it (no-face hard rule).
   - was: `Reference 1 is the authority on this exact bracelet; reference 2 shows its true size worn.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows the bracelet worn loose at true size, the pave link on top of the wrist; use reference 2 only for the piece and its true size, and take nothing else from it: not the person, her face, lips, nose, hair, skin or slip.`

3. Learnings §6 (two-tone mistakes): name the tone of every part.
   - was: `Do not redesign or add anything. THE WORLD:`
   - now: `Do not redesign or add anything. Every plain link, the pave link's frame, the lobster clasp, the jump ring, the extender and its tag are the same warm 18k gold tone, never orange, copper or silver tone; the pave stones clear and colourless. THE WORLD:`

4. Scale rule (task) and learnings §2 (size against named body parts; k04a hands read the piece 1.35x large against slender fingers).
   - was: `SCALE: the pave link 11.7 mm, a third of the wrist's width; contact shadows where links rest on skin.`
   - now: `SCALE: the pave link 11.7 mm, a third of the wrist's width and about a quarter of the palm's width; her hand is an adult woman's hand at true scale, never slender or child-sized beside the bracelet; the bracelet hangs only a little looser than the wrist, never a chunky cuff; contact shadows where links rest on skin.`

5. Calm-area rule (task): names the headline, device and card zones from the layout.
   - was: `calm dark at the upper left and below for type.`
   - now: `calm dark at the upper left for the headline and switchboard, and calm dark below for the card.`

6. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or markings.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no markings or printing on anything.`

7. Learnings §3 (faces creep in) and the hard rule: a camera below and in front of a raised arm can find the head, so the frame is limited to the forearm and hand.
   - was: `No face, no rings, no bangles, no bulb or object in the hand.`
   - now: `No head, no hair, no face, no eyes, no eyebrows anywhere: the frame holds only the raised forearm and hand. No rings, no bangles, no bulb or object in the hand.`


### k07-4B · Bold Nocturne Bracelet (take B, the hedge)  (lint: clean)

Starts from take k07-4A as sent.

1. HEDGE (card risk: hand anatomy in the cupped "bulb" pose, finger count, a twisted wrist, a real bulb in the hand): the plan's own hedge, the simpler raised forearm with the hand open and relaxed; fingers together is the safest hand a model draws. The step and the bulb live in the type ("BULB LAGAO."), as the plan says.
   - was: `raises one forearm high; the hand above it is palm-up and cupped, fingers curved and slightly spread as if screwing an invisible light bulb into a socket overhead, five fingers, natural anatomy, short bare nails;`
   - now: `raises one forearm high in the step; the hand above it is open and relaxed, the back of the hand to the camera, the four fingers gently together and pointing up toward the tent roof, the thumb resting beside them, five fingers, natural anatomy, short bare nails;`


### k07-5A · Woven Gold Hoops  (lint: clean)

Starts from the plan prompt.

1. Learnings §5 (letterbox padding): one wave-1 take came back as a square padded with bands.
   - was: `vertical 9:16,`
   - now: `vertical 9:16, a full-bleed photograph edge to edge with no borders, bands or panels,`

2. Standard reference sentence (task rule); the card's own note kept.
   - was: `Reference 1 is the authority on this exact pair; reference 2 is the authority on the braid.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It is the authority on the braid and the disc; ignore its plaster block.`

3. Verification lessons (k03a/verify/k03-2.md: disc missing and core filled with a glitter mesh; k01a/verify/k01-1.md: a second disc invented; k04a/verify/k04-1.md: amber under warm light) and learnings §6 (every part's tone); the same clause k05-5A carried.
   - was: `both hoops are identical round circles.`
   - now: `both hoops are identical round circles. On each hoop exactly one flat, round, mirror-polished disc, about a third of the hoop's width, sits on the front of the braid at the top on the latch side, exactly as in reference 2; the other end is a small hinge knuckle with no disc; never omit it, never two discs. The braid is open: between the raised polished round wires you see into a see-through core of finer polished wires with dark gaps; no granular, frosted, glitter or mesh fill. Wires, discs, hinges and latch wires are all the same bright pale-yellow 18k gold tone of reference 1, never amber, orange or copper in the warm beam.`

4. Card risk: "hang one hoop from each of two holders (which would read as two pieces)".
   - was: `From the first holder hangs the pair, one hoop from each of its two opposite bayonet slots,`
   - now: `From the first holder only hangs the pair, one hoop from each of its two opposite bayonet slots, never one hoop on each of two holders,`

5. Card risk: "fuse a hoop with the bayonet holder".
   - was: `as if they were the light now.`
   - now: `as if they were the light now. Each hoop hangs free below the holder's rim, touching it only where its latch wire passes through the slot, never merged into the holder.`

6. Scale rule (task) and learnings §2 (the Woven drifts 1.4-1.5x): counts against the touching referent and a never-limit.
   - was: `and each hoop's faint shadow on the wall.`
   - now: `and each hoop's faint shadow on the wall; the two hoops side by side span about one and a half holder-widths, and the 5-6 mm braid is about a sixth of the holder's width; never enlarge them.`

7. Two-light rule (task): names the small hard specular kicker beside the soft window glow.
   - was: `slants in through the stair window as one small hard warm-white beam from the lower left,`
   - now: `slants in through the stair window as the small hard specular kicker, one small hard warm-white beam from the lower left,`

8. Calm-area rule (task): names the headline and card zones.
   - was: `calm dark wall above and below for type.`
   - now: `calm dark wall above for the headline and below for the card.`

9. Exact no-text phrase from the task rule (adds "no watermark").
   - was: `No text, letters, numbers, logos or markings.`
   - now: `No text, no letters, no numbers, no logos, no watermark, no markings or printing on anything.`

10. No eyes, eyebrows or faces (hard rule), made explicit.
   - was: `No hands, no faces, no scooter in view.`
   - now: `No hands, no people, no faces, no eyes, no eyebrows, no scooter in view.`


## Lint

Every prompt was checked by script (`build_prompts.py`, run with `python3 -I`) for:

- **Banned words:** diamond, real gold, solid gold, freshwater, ruby, huggie, and "emerald" anywhere except the lock's "yellow emerald cut" (a cut name, not a noun for the stone).
- **Bare metal words:** "gold" or "silver" not followed by "tone".
- **Water words in all seven prompts.** The camp shows no water anywhere, and three of the pieces have no waterproof claim. The words checked: water, wet, droplet, rain, dew, splash, puddle, pool, liquid, ripple, sea, river.
- **The required parts:**
  - 9:16 and full-bleed;
  - the exact reference sentence;
  - a must-stay / never clause;
  - mm, and a contact shadow;
  - a soft light and the small hard specular kicker;
  - calm areas named for the headline and the card;
  - the exact no-text clause with "no watermark";
  - no faces, eyes or eyebrows;
  - one product only.

All 7 prompts are clean. Two notes:
- Card 3's only water-family word is the negative "never a liquid, stain, blob or wet mark", which the lint allows on purpose.
- "Gold" appears only as "18k gold tone", "gold tone" or "pale-yellow 18k gold tone", and "silver" only as "rhodium silver tone" or "silver tone".

## Generation record

- **Balance:**
  - **Before:** 201.21 (read before submitting).
  - **After:** 157.71.
  - **This batch spent 10.00 credits:** 5 GPT Image 2.6 medium pictures at 1 credit and 2 Seedream 5.0 Pro pictures at 2.5. The transactions:
    - 18:56:33.46Z and 18:56:33.74Z: k07-4A and k07-5A;
    - 18:56:34.01Z and 18:56:34.24Z: k07-1B and k07-4B;
    - two of the four GPT spends at 18:59:00.7-18:59:01.5Z: k07-1A and k07-2A;
    - 18:59:47.43Z: k07-3A.
  - The rest of the drop (33.5) was spent by other sessions sharing the account.
- **Models:**
  - Take A was requested and served as `gpt_image_2_6` (quality medium, 2k, 9:16, `use_unlim` false), at 1520 x 2688.
  - Take B was requested and served as `seedream_v5_pro` (2k, 9:16, `use_unlim` false), at 1536 x 2720.
  - The verifier should read each picture's own W and H.
- **Rounds.** Every refused item was a `submission_failed` 429 (rate_limit_reached) and was never submitted, so only those items were resubmitted, unchanged:
  1. **18:56Z, one call with all 7 items.** k07-1B, 4A, 4B and 5A were accepted; k07-1A, 2A and 3A were refused.
  2. **18:57:45Z,** after jobs_wait polling on the four submitted jobs: 1A, 2A and 3A were all refused again.
  3. **18:58:35Z,** after about 50 s of polling: 1A and 2A were accepted; 3A was refused.
  4. **18:59:47Z,** after about 60 s of polling: 3A was accepted.

  All 7 jobs completed the first time. None failed or was flagged nsfw, and none had an unknown outcome, so nothing was resubmitted with words removed.
- **Files:**
  - The pictures: `pics/k07-1A.png`, `k07-1B`, `k07-2A`, `k07-3A`, `k07-4A`, `k07-4B` and `k07-5A`, downloaded with curl and unchanged. No URL was written to any file.
  - `jobs.json` holds one row per slot, with no URLs.
  - `prompts.json` holds the prompts exactly as generated.

## Shooter's first look (not the verification pass)

Seen at contact-sheet size plus full-resolution crops of each piece:

- **k07-1A, Toggle (GPT).**
  - **Delivered:** a crazed ivory porcelain dome on a blue-grey limewash wall, with the moonlit grille lattice on the left. The sailor ring hangs over the lever, and both strands run straight down the wall like surface wiring. The idea reads at once.
  - **Ring and bar:** the ring is about half the dome's width. The straight one-row bar (about 8 stones) lies across the lower front of the ring, about 0.6x the ring, with its jump ring at the left.
  - **Check the gate:** the ring shows **two** ball nubs on **two** ribbed collars, at about 2 and 3 o'clock. Reference 2 has one nub, one ribbed collar and one barrel collar with the chain's jump ring. This is the k04-2A redesign again and is likely a construction fail.
  - **Check the bar:** it reads as laid across the front of the ring rather than threaded through it.
- **k07-1B, Toggle (Seedream, the hedge).**
  - **Delivered:** a paperclip link over the lever, and the closed clasp hanging just below the dome. The ring matches reference 2 closely: one barrel collar with the jump ring at about 1 o'clock, the nub at 3 and the ribbed grooves at 4. The strands run down the wall, with hard contact shadows.
  - **Check the bar:** it is short, about 4-5 stones against about 9, so about 0.45x the ring against 0.6-0.7x.
  - **Check the grade:** the wall reads pale moonlit blue-white, much brighter than A's. Bone lit type needs a dark zone, so check the headline zone and consider the Story crop, or the Feed P.
- **k07-2A, Prism (GPT).**
  - **Delivered:** a plain kraft matchbox on dark teak, its tray half out, with the pair inside, one spent curled match across the sleeve and a wisp of smoke above. There is no label or print and no flame.
  - **Construction:** the left stud reads purple princess, pink baguette, yellow emerald cut, purple princess, pink baguette; the right stud is mirrored. The arc stays curved, and the colours are clean lilac, pink and lemon.
  - **Check:** count the pearls (about 6-7 per stud at a glance; the lock says 6).
  - **Check:** the scale against the 52 mm box.
- **k07-3A, Verdant Cushion (GPT).**
  - **Delivered:** a hard-edged torch circle on ivory silk. The left stud lies face-up and throws a clear green patch into its shadow, so the "ITS OWN GREEN LIGHT" leader can print. The right stud is tipped to show its post, and the cellophane cone's tip touches the post. A brass thaali rim sits at the top left.
  - **Construction:** a single spiky sunburst halo, a smooth bezel and rhodium silver tone.
  - **Check:** the scale. The circle is large in frame, so the studs may read bigger than 15 px/mm.
- **k07-4A, Bold Nocturne (GPT).**
  - **Delivered:** a raised forearm against shamiana pleats, marigold strings and phone-torch bokeh, with the oxblood velvet sleeve at the bottom. The cupped hand has 5 fingers and reads natural at a glance.
  - **Construction:** one pave link among thick polished links, and the extender with its tag.
  - **Check:** the palm side faces the camera, not the back of the wrist. The bracelet sits a few cm below the wrist on the forearm, with the pave link facing the lens.
  - **Check:** the plain link count and the scale.
- **k07-4B, Bold Nocturne (Seedream, the hedge).** An open hand with the fingers together, the back of the hand to the camera, and the same bokeh, marigolds and sleeve. Check the link count and the pave link.
- **k07-5A, Woven (GPT).**
  - **Delivered:** a dark bakelite-like holder close up, with two empty holders behind on twisted flex. The pair hangs from the near holder only, one hoop each side, with the latch wires hooked at the rim, the discs at the top, the braids open and nothing in the empty holders.
  - **Check the holder:** it reads more like a cup or shade than a 35 mm bayonet holder, about 1.7x a hoop's width against 1.4x. Check the hoop scale against it.

No generated text, logos, faces or extra jewellery were seen in any of the seven. The full verification is the verifier's.
