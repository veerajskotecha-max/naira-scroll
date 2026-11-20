# k08a brief applied (camp k08 EK MATRA KI KAMI., cards 1-5)

## Loop diff: none

None, because there is no loop note to apply:

- `batches/k08a/brief_diff.md` does not exist. The `k08a` folder did not exist before this run.
- The previous-batch loop path given (`batches//loop.md`) names no batch. It resolves to `batches/loop.md`, which does not exist.
- No `loop.md` exists anywhere under `concept-50/batches/`. The only `brief_diff.md` files are the k01r and k02r rescue notes. They change k01 and k02 cards, not these five briefs.

What was read instead:
- **The camp:** `crazy100.json` camps[k08] (idea, insight, textual graphic, brand features, palette, sell lever, carousel text, changes and truth fixes) and ads 1-5 (picture, prompt, layout, size line, motion, risk, variant). Also batches[k08a] (hedge takes k08-1 and k08-2), the k08 section and production table in `CRAZY100.md`, and `RULINGS.md`.
- **Past verification lessons:**
  - `build/learnings.md` (wave 1) and `batches/bakeoff/README.md`, including the quality-tier test: gpt_image_2_6 medium held the toggle and the S-wave.
  - `batches/k01a/verify/k01-5.md`, the only faithful toggle on record, and its redoFix.
  - `batches/k04a/verify/k04-2.md` (toggle: an invented third chain end; ring and link ratios).
  - `batches/k01a/verify/k01-3.md` (Verdant Circlet: both stars redesigned).
  - `batches/k06a/verify/k06-3.md` (Verdant Eternity on gpt_image_2_6: wave a little broad).
  - `batches/k01r/brief_diff.md`.
  - The ads-500 `build/learnings.md` Prism and composite-scale lessons.
- **The five product cards and all ten reference photos, each looked at:** Toggle `02.jpg` and the clasp crop; Circlet `01`, `03`; Prism `03`, `04`; Verdant Eternity `03`, `01`; Bold Nocturne `01`, `02`.

**How take A was built.** Take A is each card's planned `prompt` from crazy100.json. The only changes are the edits logged below. They come from three sources:
- **The batch's prompt rules:** the exact reference sentence, the lock word for word, a referent touching the piece with a true contact shadow, two named lights, calm areas, the exact no-text clause, no face, eyes or eyebrows, one product, and the banned-word lint.
- **The wave-1 learnings that apply** to these pictures (§2 scale, §5 full-bleed, §6 the tone of every part).
- **Each card's risk field** and the past verifications named above.

Each edit is an exact string replacement that must occur exactly once, applied in the order logged. The script is `scratchpad/k08a/build_prompts.py`. Its edit record is `scratchpad/k08a/edit_log.json`. Every prompt passed the lint, which checks:
- **Banned words:** diamond, real or solid gold, freshwater, emerald (except "emerald cut"), ruby, huggie, and gold or silver not followed by "tone".
- **Water words** on the Toggle and Prism (no waterproof claim).
- **Presence** of every required clause.

## Take B: two cards, k08-1 and k08-2

The batch allows take B for 2 cards. The plan's `hedgeTakes` and production table name k08-1 and k08-2, and the risk fields and the record agree.

- **k08-1, the Toggle clasp on a dead-straight strand.**
  - The toggle clasp has the longest failure record in this run: eight failed renders before k01-5A (the first faithful one), then k04-2A (ring redesigned) and k04-2B (an invented third chain end).
  - This card adds two more hard asks: a strand pulled dead straight across the frame, and a foil border that can grow letter-like marks.
  - Take B is the plan's hedge: the toggle at the exact centre of the strand (models pull pieces to the centre, RULINGS §4) and the border cut to one plain rule.
  - It also adds a "crisp, full size" clasp clause, because the bake-off found seedream draws this clasp "smaller and softer".
- **k08-2, a clean card beside a henna cone.**
  - The cone invites henna patterns and letter-like squiggles, a hard-rule rejection (no generated text or pseudo-script).
  - The Circlet's lopsided circlet and stars have failed before (k01-3: both stars redesigned; ads-500: the circlet swelled, the pearl became a teardrop and a sixth stone appeared).
  - Take B is the plan's hedge: no cone at all, the studs on one diagonal, and the HTML henna word alone carrying the ink.
- **Why the other three get no B.**
  - **k08-3 (Prism)** is shot in reference 1's own straight-on pose, with the internal ratios locked.
  - **k08-4 (Verdant Eternity)** keeps reference 1's own pose. gpt_image_2_6 passed this ring in k06-3.
  - **k08-5 (Bold Nocturne)** is a flat lay of a simple chain.
- Take B runs on `seedream_v5_pro` (2k), the model the bake-off found best on the S-wave and closest on the toggle's ring and bar, so each hedged card has two models.

## Lock check

All five product-card locks are in their prompts word for word, each with its "must stay X, never Y" clause.
- **Card 1:** one punctuation fix restores the card's full stop (edit 1.2).
- **Card 4:** the plan's extra "the back stays open, never a closed full circle" is kept after the lock.
- **Cards 2, 3 and 5:** the locks were already verbatim.

Reference media ids are the product cards' `mediaIds`, reference 1 first. Take B uses the same two.

| Slot | Ref 1 (media id) | Ref 2 (media id) |
|---|---|---|
| k08-1A, k08-1B | `concept-50/refs/toggle-link-chain/02.jpg` (d3c384eb…) | `ads-500/build/refs/toggle-link-chain__clasp.jpg` (59d6c393…) |
| k08-2A, k08-2B | `concept-50/refs/verdant-circlet-studs/01.jpg` (ef075ae6…) | `concept-50/refs/verdant-circlet-studs/03.jpg` (d7f77110…) |
| k08-3A | `concept-50/refs/prism-cluster-studs-silver/03.jpg` (47443201…) | `concept-50/refs/prism-cluster-studs-silver/04.jpg` (60f7ac77…) |
| k08-4A | `concept-50/refs/verdant-eternity-band/03.jpg` (2c3d1209…) | `concept-50/refs/verdant-eternity-band/01.jpg` (702645c3…) |
| k08-5A | `concept-50/refs/bold-nocturne-bracelet/01.jpg` (92bae303…) | `concept-50/refs/bold-nocturne-bracelet/02.jpg` (a7807ef5…) |

Two of the second references show a face: Prism `04.jpg` (nose, lips) and Bold Nocturne `02.jpg` (nose, lips). Their prompts say to take only the piece and its true size from them.

## Picture changes the layout must follow (the type is set to the plate)

1. **k08-1:**
   - **Fingertips:** they moved from the card's bottom edge to the strand's right end, just above the line, as the touching referent. The Naira seal planned at the card's top right (x≈930, y≈600) may need to move left or down past the fingers.
   - **Toggle position:** in A it came out near the centre, not right of centre, so पक्का centres on it.
   - **The wrap:** both takes render a whole card with the chain laid across it, not wrapped round it. The idea still reads.
   - **B's fingers:** they pinch the chain's end instead of pressing it flat.
2. **k08-2 marigold:** it now rests on the card's top edge, touching stud 1's green stone from above, as the touching referent. In A the cone stays where the plan put it.
3. **k08-3:** the tabs are given as about 10 mm wide (half an arc). The hairlines from the lilac, rose and turmeric tabs still drop to the matching stones.
4. **k08-4 thread:** the thread loop now lies on the card just behind the ring, touching the band, not on the velvet at the upper right. The 'धागा · THE THREAD TRICK · RETIRED' leader points there. In A it sits near the open back, so check that it does not hide a looped tip.
5. **k08-5:**
   - **Card width:** the card is now a little narrower than the frame (about 9 cm), so thin satin strips show at both sides.
   - **Pave link position:** in A it came out a little right of centre, so तीनों centres on it.
   - **Size fact:** the plan prompt's "pave link about an eighth of the frame width" described its 11.7 mm width. Its length along the line is about 20 mm (a fifth of the frame), and both are now in the prompt.

## Flags for the finisher (copy and layout, not the pictures)

- **Shipping line (owner ruling, 20 Nov 2026).** The camp's brand features and changes leave "FREE INSURED SHIPPING · CASH ON DELIVERY" off as an open question. The ruling overrides that:
  - every k08 ad carries the line, in the F2 foot after RSVP · NAIRAFLORE.COM;
  - the OBJECTION card (4) and the OFFER card (5) may also use it in the hook and primary text;
  - no ad promises a delivery time.
- **No BUY3 collection.** The sell lever and carousel text send retargeting to "a BUY3 collection". There is none, so every card links to its own product page.
- **Codes.** BUY2 10% (2+), BUY3 20% (3+), BUY4 30% (4+) and NAIRA10 are live. Cards 1-5 use BUY3. No struck or compare-at prices and no price sums.
- **Pre-order (card 3, Prism).** The plan's beat, primary text and card line say "Pre-order", and the listing carries the tag. Today's run notes say every piece is in stock at the card's price. Decide the line before setting the card; never promise arrival before a function, or any delivery time.
- **Returns.** No line may claim returns or exchanges.
- **Claims.**
  - Prism has none: no waterproof or tarnish free.
  - The Toggle has no waterproof claim and no water imagery.
  - Cards 2, 4 and 5 may say waterproof (tagged).
  - Say "green cubic zirconia", never "emerald".
  - Card 3 copy may say "yellow emerald cut" only as a cut name; the plan's copy says "lemon" instead, which is safer.
- **Picture metadata.** The downloaded PNGs carry the models' C2PA provenance (certificate and OCSP addresses, IPTC "trainedAlgorithmicMedia"). They hold no result or signed URL. The files are as delivered.

## Edits, edit by edit

The B edits apply on top of that card's finished take A, so each B prompt equals its A prompt plus the B edits.

### k08-1A · Toggle Link Chain · take A, gpt_image_2_6 medium 2k  (lint: clean; 14 edits; 4554 characters)

1. Task rule: the exact reference sentence. The clause after it is k01a/verify/k01-5.md redoFix 2 (reference 2 is a close crop on skin: take its construction and pose, never its framing or size).
   - was: `Reference 1 is the authority on this exact piece; reference 2 is the same clasp up close.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It is the clasp up close on skin, a much closer view than this picture: copy the clasp's construction and pose from it, never its framing, its skin or its size.`

2. Lock pasted word for word from products/toggle-link-chain.json (the plan had a semicolon where the card has a full stop).
   - was: `in polished 18k gold tone; 1 thick round`
   - now: `in polished 18k gold tone. 1 thick round`

3. Card risk (the clasp) and past verification: k01a/verify/k01-5.md (the one faithful toggle on record: gate sleeve 11, barrel and jump ring 1, nub 3, ribs 4, bar across the upper left) and k04a/verify/k04-2.md (an invented third chain end failed take B). Learnings §6: a silver jump ring on a gold tone toggle (k01-5B).
   - was: `never a plain donut ring, a lobster clasp, or a curved or multi-row pave bar.`
   - now: `never a plain donut ring, a lobster clasp, or a curved or multi-row pave bar. The clasp is built exactly as in reference 2: the left strand ends in one jump ring at the outer end of the stone bar; the bar lies across the upper left of the sailor ring with its single row of tiny stones facing the camera; the ring's flat-cut gate sleeve sits at about 11 o'clock; the barrel collar at about 1 o'clock carries the one jump ring that joins the right strand; the small push-pin nub points outward at 3 o'clock with two or three ribbed grooves just below it at 4 o'clock. Exactly two chain ends meet the clasp, never a third strand or a loose jump ring. Every link, the ring, the bar and every jump ring are the same polished 18k gold tone, never a silver-tone, white-metal or rose part.`

4. Card risk: letter-like marks creeping into the foil border. Plain straight lines and no corner ornaments leave the model nothing to letter.
   - was: `a thin double-rule border in muted saffron and oxblood foil.`
   - now: `a thin double-rule border of plain straight lines in muted saffron and oxblood foil, with no corner ornaments.`

5. Card risk: the strand may not lie dead straight. "Pulled taut" gives the model a physical reason for the straight line; the reference-2 pose keeps the clasp in the one pose that has rendered faithfully.
   - was: `the closed toggle lies face up on that line right of centre, the stone bar threaded through the ring.`
   - now: `the closed toggle lies face up on that line right of centre, the stone bar threaded through the ring, posed as in reference 2 and turned so both strands leave it level. The strand is pulled taut so it cannot sag, curve or kink.`

6. Task rule: scale in mm against a referent touching the piece. Learnings §2 (scale drifts 1.35-2x; give counts against a named body part) and k04a/verify/k04-2.md gates (ring 1.8-2.3x a link; fingertip at least 0.55x the ring). The coin and the rice stay similes only, never props (a coin would carry numerals).
   - was: `SCALE: the frame is about 9 cm wide; each link is the length of a grain of basmati rice and the sailor ring is a little larger than a one-rupee coin, about a quarter of the frame width.`
   - now: `SCALE: the frame is about 9 cm wide; each link is the length of a grain of basmati rice and the sailor ring is a little larger than a one-rupee coin, about a quarter of the frame width. About six paperclip links lie across the frame besides the clasp; the sailor ring is about as wide as two links laid end to end and the bar about one and a half links long. The referent touching the chain is her forefinger's tip (below): its pad is about 15 mm wide, so the ring is about one and a half fingertips across, never two. No coin and no rice in the picture.`

7. Task rule: calm areas for the headline as well as the card (the layout sets RISHTA PAKKA. at y 290-530 on the silk).
   - was: `Below the chain the card is smooth, bare and empty for a long way, for type set later.`
   - now: `The oxblood silk across the top and the strip of card just under it stay calm and empty for a headline; below the chain the card is smooth, bare and empty for a long way, for type set later.`

8. Task rule: the referent must touch the piece. The plan's fingertips rested on the card's bottom edge, away from the chain (and below the Feed window); they now press the strand at its right end, above the line, so the word that hangs under the chain stays clear. Same hand, same skin, same bare nails.
   - was: `At the bottom edge the tips of two fingers of a woman's right hand, light wheatish skin, short bare natural nails, rest on the card.`
   - now: `The tips of two fingers of a woman's right hand, light wheatish skin, short bare natural nails, enter from the right edge of the frame just above the line and rest on the strand near its right end, the forefinger's pad pressing one link flat to the card as if she has just drawn the ribbon straight; the fingers stay in the right fifth of the frame, clear of the clasp.`

9. Task rule: a true contact shadow, now also where the referent touches the piece.
   - was: `CONTACT: every link casts its own small sharp shadow on the paper; the ring casts a crescent shadow.`
   - now: `CONTACT: every link casts its own small, sharp, true contact shadow on the paper where it lies; the ring and the bar cast crisp crescent shadows; the fingertips cast a soft true contact shadow where they press the strand.`

10. Task rule: two named lights, one soft and one small hard specular kicker (wording made explicit; the lights are the plan's).
   - was: `LIGHT: one large soft warm window light from the left rakes the paper so its fibres show; one small hard specular kicker`
   - now: `LIGHT, two sources: (1) soft: one large soft warm window light from the left rakes the paper so its fibres show; (2) one small hard specular kicker`

11. Learnings §5: one wave-1 take came back as a square padded to 9:16.
   - was: `Natural film grain, real paper tooth.`
   - now: `Natural film grain, real paper tooth. Full-bleed 9:16 photograph edge to edge; no letterbox bands, frames or panels.`

12. Task rule: the exact no-text phrase.
   - was: `No text, letters, numbers, monograms, names, symbols, deity motifs or pseudo-script on the card or anywhere in the frame; no logos, no watermarks.`
   - now: `No text, no letters, no numbers, no logos, no watermark: no monograms, names, symbols, deity motifs or pseudo-script on the card or anywhere in the frame.`

13. Hard rule: no eyes, eyebrows or faces.
   - was: `No face, no eyes.`
   - now: `No face, no eyes, no eyebrows.`

14. Hard rule: one product per picture, stated as a count.
   - was: `No rings, bangles or any other jewellery on the fingers: this necklace is the only piece in the frame.`
   - now: `No rings, bangles or any other jewellery on the fingers. Exactly one product: this necklace is the only piece in the frame.`

### k08-1B · Toggle Link Chain · take B, seedream_v5_pro 2k: the hedge  (lint: clean; 3 edits on top of take A; 4677 characters)

1. The plan's hedge (card risk field): the toggle at the exact centre of the strand. Models pull pieces to the centre (RULINGS §4), so this asks for what the model wants to do and spends its effort on the clasp.
   - was: `the closed toggle lies face up on that line right of centre,`
   - now: `the closed toggle lies face up on that line at the exact centre of the frame's width,`

2. The plan's hedge: the border reduced to one plain rule, the least letter-like decoration possible.
   - was: `a thin double-rule border of plain straight lines in muted saffron and oxblood foil, with no corner ornaments.`
   - now: `one thin plain straight rule in muted saffron foil, with no corner ornaments.`

3. Bake-off (batches/bakeoff/README.md): seedream_v5_pro drew the toggle's ring and bar right but the clasp "smaller and softer". Take B runs on seedream_v5_pro.
   - was: `Exactly two chain ends meet the clasp,`
   - now: `The clasp is crisp and full size: the ring's tube thick and round, the gate, nub and ribs sharp, the stone bar straight and sharp. Exactly two chain ends meet the clasp,`

### k08-2A · Verdant Circlet Studs · take A, gpt_image_2_6 medium 2k  (lint: clean; 13 edits; 4280 characters)

1. Task rule: the exact reference sentence; the card's own detail note kept.
   - was: `Reference 1 is the authority on this exact piece; reference 2 shows the mirrored pair from above.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows the mirrored pair from above, both circlets face up; ignore its plaster block too.`

2. Past verification: k01a/verify/k01-3.md failed on both stars redesigned (a filigree outline, a dark lump). ads-500 learnings: a scale clause on the whole outline of a composite piece inflated the Circlet's parts (the circlet swelled, the round pearl became a teardrop, a sixth stone appeared): lock the internal ratios first, then size the outline. Card risk: the stone becoming a step cut. Ratios are the product card's sizeMm and reference 1.
   - was: `Metal: 18k gold tone, high polish. SCALE:`
   - now: `Metal: 18k gold tone, high polish. Inside each stud, before any size: the green stone is a tilted cushion cut with softly rounded corners and many small facets, never a rectangular step cut; the large shell pearl is about 4-4.5 mm, a little under half the green stone's width; the small pearl is about half the large one; the clear stones are about 2.5 mm; the two four-point stars are small solid polished stars with four sharp points, about the size of a clear stone, never outline filigree, never a lump; the circlet's open centre is about two-thirds of the green stone's width, and the paper shows through it. SCALE:`

3. Banned-word lint: "gold" alone. The border is the card's foil, not the piece, but the prompt says gold tone everywhere.
   - was: `a fine pale-gold foil border of small leaf-shaped dots`
   - now: `a fine pale gold-tone foil border of small plain leaf-shaped dots`

4. Task rule: a referent touching the piece. The plan's marigold sat at the corner, touching nothing; it moves a few cm to touch stud 1 from above (above the word, so no matra is covered). Slightly dried keeps its orange below the green stones, which must stay the most saturated colour. The cone stays where the plan put it, a little clear of stud 2, so no paste is invited onto the piece.
   - was: `with one marigold head at the top-left corner.`
   - now: `with one small, slightly dried marigold head, about 30 mm across, resting on the card's top edge just above the first stud, its petal tips touching the top of that stud's green stone setting.`

5. Task rule: scale in mm against the touching referent; learnings §2 (never enlarge).
   - was: `SCALE: the frame is about 8 cm wide, so each stud is about a sixth of the frame width, the size of a fingertip pad.`
   - now: `SCALE: the frame is about 8 cm wide, so each stud, 16.8 mm tall and about 14 mm wide, is about a sixth of the frame width, the size of a fingertip pad, never larger. The referent touching the pair is the marigold head (below): it is about twice as wide as a stud.`

6. Card risk: the two studs coming out identical instead of mirrored. Names which stud is which, from reference 1 and 2.
   - was: `the first in the upper left of the card, the second lower down and right of centre, about two stud-heights below the first.`
   - now: `the first in the upper left of the card, the second lower down and right of centre, about two stud-heights below the first. The first is the left earring of reference 1, its large pearl at 3 o'clock on its right; the second is its mirror twin, its large pearl at 9 o'clock on its left.`

7. Task rule: a true contact shadow, including where the referent touches.
   - was: `CONTACT: crisp 2 mm contact shadows under each circlet and post; the cone casts a soft long shadow.`
   - now: `CONTACT: crisp 2 mm true contact shadows under each circlet and post where they touch the paper, and a soft one under the marigold's petals; the cone casts a soft long shadow.`

8. Task rule: two named lights. Lint: "the gold" alone became "the 18k gold tone metal". Learnings §6: the tone of every part.
   - was: `LIGHT: one large soft late-afternoon window light from the left; one small hard specular kicker from behind right gives each green stone one hot facet flash, each shell pearl a soft round highlight and the gold a bright edge.`
   - now: `LIGHT, two sources: (1) soft: one large soft late-afternoon window light from the left; (2) one small hard specular kicker from behind right gives each green stone one hot facet flash, each shell pearl a soft round highlight and the 18k gold tone metal a bright edge. Every collet, prong, star and the circlet itself are the same 18k gold tone, never silver tone or brassy.`

9. Task rule: calm areas for the headline (layout: MEHENDI? HAAN. on the silk) and the card.
   - was: `Around and below the studs the card is smooth and empty, for type set later.`
   - now: `The sage silk across the top stays calm for a one-line headline; around and below the studs the card is smooth and empty, for type set later.`

10. Learnings §5: letterbox padding.
   - was: `Natural film grain, real paper tooth and silk weave.`
   - now: `Natural film grain, real paper tooth and silk weave. Full-bleed 9:16 photograph edge to edge; no letterbox bands, frames or panels.`

11. Task rule: the exact no-text phrase.
   - was: `No text, letters, numbers, monograms, names, symbols, henna designs, deity motifs or pseudo-script on the card, the cone or anywhere in the frame; no logos, no watermarks.`
   - now: `No text, no letters, no numbers, no logos, no watermark: no monograms, names, symbols, henna designs, deity motifs or pseudo-script on the card, the cone or anywhere in the frame.`

12. Hard rule: no eyes, eyebrows or faces.
   - was: `No hands, no face, no eyes.`
   - now: `No hands, no face, no eyes, no eyebrows.`

13. Hard rule: one product per picture (a pair of earrings is one product).
   - was: `No other jewellery: this pair is the only piece in the frame.`
   - now: `No other jewellery. Exactly one product: this pair is the only piece in the frame.`

### k08-2B · Verdant Circlet Studs · take B, seedream_v5_pro 2k: the hedge  (lint: clean; 4 edits on top of take A; 4104 characters)

1. The plan's hedge (card risk field): no cone at all, so nothing invites henna marks or a printed wrapper; the HTML henna word alone carries the mehendi ink.
   - was: `One plain unprinted cellophane-wrapped henna cone lies diagonally across the lower right of the card, its fine open tip resting on the card a little below and to the right of the second stud, with one tiny glossy bead of dark henna paste at the tip. The card carries no other henna: no pattern, no drawing, no lines and no marks of any kind.`
   - now: `There is no henna cone and no henna in the picture at all: no paste, no bead, no pattern, no drawing, no lines and no marks of any kind on the card.`

2. The plan's hedge: the studs on the same diagonal.
   - was: `the first in the upper left of the card, the second lower down and right of centre, about two stud-heights below the first.`
   - now: `the two on one clean diagonal from the upper left of the card down to the right of centre, the second about two stud-heights below and about three stud-widths to the right of the first.`

3. No cone, so no cone shadow.
   - was: `; the cone casts a soft long shadow.`
   - now: `.`

4. No cone.
   - was: `on the card, the cone or anywhere in the frame.`
   - now: `on the card or anywhere in the frame.`

### k08-3A · Prism Cluster Studs · take A, gpt_image_2_6 medium 2k  (lint: clean; 10 edits; 3911 characters)

1. Task rule: the exact reference sentence. Reference 2 (04.jpg) shows her nose and lips, so only the piece and its scale may be taken from it (no-face hard rule). ads-500 learnings: leaving the reference pose breaks complex settings, so the prompt names reference 1's straight-on view as the pose.
   - was: `Reference 1 is the authority on this exact piece, the pair; reference 2 shows their true size worn.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows the pair worn at true size, each arc about as long as the earlobe is wide; use reference 2 only for the piece and its true size, and take nothing else from it: not the person, her face, nose, lips, hair, skin or clothes. Reference 1 shows the pair straight on, the very view wanted here.`

2. Card risk and product morph: the order and pearl count even out (listing photo 01 drifted to 8 pearls; pearls grow to stone size). ads-500 learnings: lock the internal ratios first, then size the outline. Learnings §6: the tone of every part.
   - was: `The left stud runs purple, pink, yellow, purple, pink; the right stud mirrors it.`
   - now: `The left stud runs purple, pink, yellow, purple, pink; the right stud mirrors it. Inside each arc, before any size: the yellow centre stone is the largest, about 6 mm tall, standing upright; the purple princess stones are a little smaller and the pink baguettes slim; the 6 pearls are pinheads about 1.5-2 mm, a third of the yellow stone's height, never stone-sized and never more than 6; every stone and pearl is held in round bead-tipped claws. All the metal is the same bright cool rhodium silver tone; the warm light never tints it champagne or gold tone.`

3. Task rule: scale in mm with a referent touching the piece. The studs touch only the card they pierce, so the card and its tabs carry the mm (product morph: worn photo 02 renders the arc about 1.5x).
   - was: `SCALE: the frame is about 8 cm wide; each arc is about a quarter of the frame width, the width of a one-rupee coin.`
   - now: `SCALE: the frame is about 8 cm wide; each arc is 20 mm long, about a quarter of the frame width, the width of a one-rupee coin, never larger (no coin in the picture). The referent touching the pair is the card they are pinned through, thick handmade paper about 1.5 mm thick; each of its five paper tabs is about 10 mm wide, half an arc's length, so one arc is never wider than two tabs.`

4. Task rule: a true contact shadow.
   - was: `CONTACT: each stud casts a small soft shadow on the card.`
   - now: `CONTACT: each arc lies flat against the paper and casts a thin, true contact shadow along its lower edge; the paper dimples very slightly round each post.`

5. Task rule: two named lights (the plan's lights).
   - was: `LIGHT: one large soft frontal window light from the upper left; one small hard specular kicker`
   - now: `LIGHT, two sources: (1) soft: one large soft frontal window light from the upper left; (2) one small hard specular kicker`

6. Task rule: calm areas for the headline (layout: two lines over the drape, y 280-510) and the card.
   - was: `The card below them is smooth and empty, for type set later.`
   - now: `The card below them is smooth and empty, for type set later, and the soft plum drape across the top stays calm for a two-line headline.`

7. Learnings §5: letterbox padding.
   - was: `Natural film grain, real paper fibre.`
   - now: `Natural film grain, real paper fibre. Full-bleed 9:16 photograph edge to edge; no letterbox bands, frames or panels.`

8. Task rule: the exact no-text phrase.
   - was: `No text, letters, numbers, monograms, names, symbols, deity motifs or pseudo-script on the card, the tabs or anywhere in the frame; no logos, no watermarks.`
   - now: `No text, no letters, no numbers, no logos, no watermark: no monograms, names, symbols, deity motifs or pseudo-script on the card, the tabs or anywhere in the frame.`

9. Hard rule: no eyes, eyebrows or faces.
   - was: `No hands, no face, no eyes.`
   - now: `No hands, no face, no eyes, no eyebrows.`

10. Hard rule: one product per picture (a pair of earrings is one product).
   - was: `No other jewellery: this pair is the only piece in the frame.`
   - now: `No other jewellery. Exactly one product: this pair is the only piece in the frame.`

### k08-4A · Verdant Eternity Band · take A, gpt_image_2_6 medium 2k  (lint: clean; 12 edits; 4124 characters)

1. Task rule: the exact reference sentence. ads-500 learnings: a new 35-degree pose flattened the S-wave into a row, so the pose is reference 1's own (the plan's "standing as it stands there", now spelled out).
   - was: `Reference 1 is the authority on this exact piece, standing as it stands there; reference 2 shows how the ovals alternate either side of the wave.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. Reference 1 also gives the pose: keep the ring standing exactly as it stands there, upright on its edge, the S-wave front turned three-quarters to the camera and the open back with both looped tips at the right. Reference 2 shows how the ovals alternate either side of the wave; ignore its plaster block too.`

2. Card risk (the S-wave straightens or closes into halos). Bake-off: gpt_image_2_6 drew the wave "close to a partial halo"; k06a/verify/k06-3.md passed with a note (wave a little broad, one oval wrapped three-quarters); k03a k03-1 take B read warm champagne under a warm key. This batch's key is warm and the ground is coral, so the tone is named.
   - was: `the back stays open, never a closed full circle.`
   - now: `the back stays open, never a closed full circle. The clear pave is ONE slim line about two tiny stones wide that snakes from oval to oval: the ovals sit in a gentle zigzag, one nearer the top edge of the band, the next nearer the bottom edge, and the wave cups the half of each oval's outline that faces the middle of the band, then crosses to the next, so every oval has pave on one side only and bare claws on the other; never a broad sugared band, never a frame, loop or halo round any oval. Toward the back each green oval sits in 4 short claws. All metal, every claw and both looped tips are the same bright cool rhodium silver tone; the warm key and the coral velvet never tint them champagne, rose or gold tone.`

3. Banned-word lint: "silver" alone. Straight lines leave nothing letter-like.
   - was: `a fine silver-foil border of plain lines`
   - now: `a fine silver-tone foil border of plain straight lines`

4. Task rule: scale in mm against a touching referent; learnings §2. The thread loop is the size of her finger, so it is the size of the ring's inside (16.5 mm at rest, US 5 to 9 = 15.7-18.9 mm).
   - was: `SCALE: the frame is about 6 cm wide at the ring, so the ring is about a third of the frame width, the size of a large coat button.`
   - now: `SCALE: the frame is about 6 cm wide at the ring, so the ring is about a third of the frame width, the size of a large coat button, never larger; each green oval is 5 x 4 mm, about a quarter of the ring's height. The referent touching it is the retired measuring thread (below): a loop about 17 mm across, the same size as the ring's inside.`

5. Task rule: the referent must touch the piece. The plan's thread lay apart on the velvet; it now touches the back of the band, so the proof is in one glance: the loop that measured her finger is the ring's own size. Card risk (the thread reading as a second band) is guarded by "limp, matte, never a rigid ring, never metal".
   - was: `On the velvet beyond the card, upper right, lies a short loop of plain white cotton sewing thread, knotted once, its two snipped ends frayed.`
   - now: `On the card just behind the ring lies the retired measuring thread: a limp loop of plain white cotton sewing thread about 17 mm across, knotted once, its two snipped ends frayed, lying flat with its near edge touching the back of the band; it is soft matte thread, never a rigid ring, never metal and never shiny, and it never covers the looped tips.`

6. Task rule: a true contact shadow.
   - was: `CONTACT: a dark believable contact shadow where the band meets the card.`
   - now: `CONTACT: a dark, true contact shadow where the band meets the card, and a faint one under the thread.`

7. Task rule: two named lights (the plan's lights).
   - was: `LIGHT: one large soft warm key from the left; one small hard specular kicker`
   - now: `LIGHT, two sources: (1) soft: one large soft warm key from the left; (2) one small hard specular kicker`

8. Task rule: calm areas for the headline (layout: two lines on the blurred velvet, y 280-520) and the card.
   - was: `the velvet tray falls softly out of focus at the top.`
   - now: `the velvet tray falls softly out of focus at the top and stays calm for a two-line headline.`

9. Learnings §5: letterbox padding.
   - was: `Honest macro depth of field. Natural film grain.`
   - now: `Honest macro depth of field. Natural film grain. Full-bleed 9:16 photograph edge to edge; no letterbox bands, frames or panels.`

10. Task rule: the exact no-text phrase.
   - was: `No text, letters, numbers, monograms, names, symbols, deity motifs or pseudo-script on the card or anywhere in the frame; no logos, no watermarks.`
   - now: `No text, no letters, no numbers, no logos, no watermark: no monograms, names, symbols, deity motifs or pseudo-script on the card or anywhere in the frame.`

11. Hard rule: no eyes, eyebrows or faces.
   - was: `No hands, no face, no eyes.`
   - now: `No hands, no face, no eyes, no eyebrows.`

12. Hard rule: one product per picture, stated as a count.
   - was: `No other jewellery, and the thread is loose plain thread, never a bracelet or a band: this ring is the only piece in the frame.`
   - now: `No other jewellery, and the thread is loose plain thread, never a bracelet or a band. Exactly one product: this ring is the only piece in the frame.`

### k08-5A · Bold Nocturne Bracelet · take A, gpt_image_2_6 medium 2k  (lint: clean; 13 edits; 3765 characters)

1. Task rule: the exact reference sentence. Reference 2 (02.jpg) shows her nose and lips, so only the piece and its scale may be taken from it (no-face hard rule).
   - was: `Reference 1 is the authority on this exact piece; reference 2 shows its true size worn.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows the bracelet worn at true size, the pave link about a third of the wrist's width; use reference 2 only for the piece and its true size, and take nothing else from it: not the person, her face, nose, lips, hair, skin or clothes.`

2. Card risk and product morph: the chunky flat-edged links thin into a dainty paperclip or round into cable or curb. Learnings §6: the tone of every part (the supplier labels the pave link brass).
   - was: `Must stay exactly 1 pave link among plain polished links, never more stone-set links or an all-plain chain.`
   - now: `Must stay exactly 1 pave link among plain polished links, never more stone-set links or an all-plain chain. Every plain link is a thick, flat-edged, elongated rounded rectangle about twice as long as it is wide, never a dainty paperclip, cable or curb link; the pave link's metal, every plain link, the jump ring and the clasp are all the same 18k gold tone, never silver tone or white metal.`

3. Fact fix and task rule. Laid along the line, the pave link's length (about 19-20 mm, product card) runs across the frame, so "an eighth of the frame width" (its 11.7 mm width) would shrink it or confuse the model; both dimensions are now given. The card becomes the touching referent, sized in cm.
   - was: `SCALE: the frame is about 10 cm wide; each plain link is about the length of a fingernail and the pave link about an eighth of the frame width.`
   - now: `SCALE: the frame is about 10 cm wide; each plain link is about the length of a fingernail; the pave link is about 20 mm long along the line and 11.7 mm wide, so it spans about a fifth of the frame's width and stands about an eighth of the frame's width tall, never larger. The referent touching the bracelet is the card it lies on: about 9 cm wide, about four and a half pave links.`

4. Task rule: a referent of known size touching the piece. Both deckled edges in frame make the 9 cm card readable as a ruler under the chain.
   - was: `The bracelet is laid open and dead straight, level across the full width of the frame a little above the middle, every link flat and touching the next, the pave link at the exact centre; the lobster clasp and the extender run off the frame edges.`
   - now: `The card is a little narrower than the frame, so a thin strip of satin shows past each of its deckled side edges. The bracelet is laid open and dead straight, level across the full width of the frame a little above the middle, every link flat and touching the next, the pave link at the exact centre, with about three plain links on each side of it lying on the card; it runs over both deckled edges onto the satin, and the lobster clasp and the extender run off the frame edges.`

5. Banned-word lint: "gold" alone.
   - was: `a fine gold-foil border of plain rays`
   - now: `a fine gold-tone foil border of plain straight rays`

6. Card risk: the sparks forming letter-like streaks.
   - was: `a stage cold-spark fountain falls as a soft out-of-focus curtain of fine warm golden streaks and small round bokeh, dim against the black.`
   - now: `a stage cold-spark fountain falls as a soft out-of-focus curtain of fine warm golden streaks and small round bokeh, dim against the black. The streaks fall straight down, soft and blurred, and never form shapes, letters or numbers.`

7. Task rule: calm areas for the headline (layout: two lines over the spark curtain, y 280-520) and the card.
   - was: `The card below the bracelet is smooth and empty, for type set later.`
   - now: `The dark satin and the dim spark curtain above the card stay calm for a two-line headline; the card below the bracelet is smooth and empty, for type set later.`

8. Task rule: a true contact shadow.
   - was: `CONTACT: every link casts a short sharp shadow toward the lower left.`
   - now: `CONTACT: every link casts a short, sharp, true contact shadow toward the lower left where it lies on the card.`

9. Task rule: two named lights (the plan's lights).
   - was: `LIGHT: the soft key is a large warm honey glow from the upper right, the colour of the sparks; one small hard specular kicker from the left`
   - now: `LIGHT, two sources: (1) soft: the key is a large warm honey glow from the upper right, the colour of the sparks; (2) one small hard specular kicker from the left`

10. Learnings §5: letterbox padding.
   - was: `Natural film grain, deep warm shadows.`
   - now: `Natural film grain, deep warm shadows. Full-bleed 9:16 photograph edge to edge; no letterbox bands, frames or panels.`

11. Task rule: the exact no-text phrase.
   - was: `No text, letters, numbers, monograms, names, symbols, deity motifs or pseudo-script on the card or anywhere in the frame; no logos, no watermarks.`
   - now: `No text, no letters, no numbers, no logos, no watermark: no monograms, names, symbols, deity motifs or pseudo-script on the card or anywhere in the frame.`

12. Hard rule: no eyes, eyebrows or faces.
   - was: `No people, no hands, no face, no eyes.`
   - now: `No people, no hands, no face, no eyes, no eyebrows.`

13. Hard rule: one product per picture, stated as a count.
   - was: `No other jewellery: this bracelet is the only piece in the frame.`
   - now: `No other jewellery. Exactly one product: this bracelet is the only piece in the frame.`

## Submission and results

- **Round 1** (19:00Z), one `generate_image_batch` call with all seven items: k08-2A and k08-4A were submitted; k08-1A, k08-1B, k08-2B, k08-3A and k08-5A were refused with a 429 rate limit (shared account). Refused items were never submitted, so they cost nothing.
- **Round 2** (19:01:51Z), after about 35 s of polling `jobs_wait` on the submitted jobs: the five refused items were resubmitted with identical params. k08-1A, k08-1B, k08-3A and k08-5A were submitted; k08-2B was refused again.
- **Round 3** (19:03:02Z), after more polling: k08-2B was submitted.
- **Outcome:** all seven jobs completed. None failed or was flagged nsfw, so nothing was resubmitted for a failure. No item had an unknown outcome.
- **Files and record:** pictures are in `pics/<slot>.png`, downloaded with curl; no URL was written to any file. `jobs.json` records each job: id, size, model, credits, medias and prompt.
- **Credits:** 10 for this batch (5 × 1 for gpt_image_2_6 medium, 2 × 2.5 for seedream_v5_pro), matched to the account's spend log by timestamp. The balance read 173.21 before and 149.71 after. The rest of the drop is other batches running on the same account.
