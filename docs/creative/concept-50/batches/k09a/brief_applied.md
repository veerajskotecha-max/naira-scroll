# k09a brief applied (camp k09 AAJ KA BHAAV., cards 1-5)

## Loop diff: none

None, because there is no loop note to apply:

- `batches/k09a/brief_diff.md` does not exist. The `k09a` folder did not exist before this run.
- The previous-batch loop path given (`batches//loop.md`) names no batch. It resolves to `batches/loop.md`, which does not exist.
- No `loop.md` exists anywhere under `concept-50/batches/`. The only `brief_diff.md` files are `k01r/brief_diff.md` and `k02r/brief_diff.md`, which are rescue notes for k01 and k02 cards and name none of these five briefs.
- `k08b`, the batch before this one in the plan, has no folder yet.

What was read instead:
- the camp: `crazy100.json` camps[k09] (idea, insight, textual graphic, brand features, palette, sell lever, carousel text, changes with its truth check, and ads 1-5 with their pictures, prompts, layouts, motion and risk fields), the batch row (`hedgeTakes`: k09-2, k09-3), its `CRAZY100.md` section and production table, and `RULINGS.md`;
- `build/learnings.md` (wave 1, 7 lessons) and `batches/bakeoff/README.md` (models and quality tiers);
- the past verification notes for these exact pieces:
  - Brushed: `k02a/verify/k02-4.md` (1.9x beside a cassette) and `k04a/verify/k04-4.md` (3x beside hands; the turned piece curled into a cuff);
  - Toggle: `k01a/verify/k01-5.md` and `k04a/verify/k04-2.md` (the ring redesigned off the reference-2 pose; a third chain end);
  - Verdant Eternity: `k03a/verify/k03-1.md`, `k04a/verify/k04-3.md` and `k06a/verify/k06-3.md` (scale 2x; broad sugared wave; champagne claws; the wave wrapping three-quarters of one oval);
  - Verdant Cushion: `k02a/verify/k02-5.md` (passed; stud landed at 50% down, not 38%);
  - Woven: `k01a/verify/k01-1.md`, `k03a/verify/k03-2.md` and `k04a/verify/k04-1.md` (disc missing, core filled with mesh, amber tone, 1.4-1.5x);
  - `k04a/brief_applied.md`, `k05a/brief_applied.md` and `k06a/brief_applied.md` for the shared conventions;
- the five product cards and both reference photos of each (looked at).

Take A is each card's planned `prompt` from crazy100.json. The only changes are the edits logged below. Each is an exact string replacement, applied once, in the order logged. There are three kinds:
1. **conformance** with this batch's prompt rules: the exact reference sentence, a referent touching the piece in mm with a true contact shadow, the small hard specular kicker named, calm areas pinned to the layout's own numbers, the exact no-text clause with "no watermark", no eyes or eyebrows, and the banned-word lint;
2. **learnings.md** lessons: 2 (scale drifts large: count against a touching referent, field of view in cm), 3 (faces), 5 (full-bleed, no letterbox bands) and 6 (name the tone of every part);
3. **verification lessons** already written for these exact pieces (listed above).

No idea was tamed. Every stage, camera, prop and light of the plan is kept: the night counter, the black velvet pad and tube-light streak (1), the top-down V with the ring as the 0 (2), the safe seen from inside with one blade of shop light (3), the ear from behind with the shop's bokeh (4), and the tipped antique balance with the empty pan (5).

The script is `scratchpad/k09a/build_prompts.py`. It reads the plan prompts, applies the edits, lints, and writes `prompts.json`.

## Take B: two cards, k09-2 and k09-3

The batch allows a take B for 2 cards. The plan's batch row names the same two as hedge takes: k09-2 (the toggle ring as the 0 of 20%) and k09-3 (the S-wave under a single blade of light). The risk fields and the past verification lessons agree, and they rank these two above the other three:
- **k09-2 (Toggle).** Its risk field is "the sailor ring smoothed into a plain donut, or the bar threaded through the ring". Every past take of this clasp failed when the pose left reference 2: k01-5 A and B, and k04-2 A (a generic marine clasp). k04-2 B invented a third chain end. The whole device, the ring as the 0 of '20%', depends on that one ring.
- **k09-3 (Verdant Eternity).** Its risk field is "the S-wave straightened into a row, or closed into a halo", plus the blade blowing out the pavé and a dial or key on the door. The bake-off's `gpt_image_2_6` ring drew the wave "close to a partial halo", and seedream's was closest to the listing. The plan's own pose (square to the lens in a pad slit) is not the pose of reference 1.

The other three have lower picture risk on the new models:
- **Card 1 (Brushed)** passed construction in both past takes; its fault was scale against a large prop, and here the only prop is a 4 cm pad.
- **Card 4 (Verdant Cushion)** passed in k02-5 on the older model.
- **Card 5 (Woven)** passed the bake-off at gpt medium (open plait, one disc). Its past fails were on nano_banana_2.

Both B takes run on `seedream_v5_pro` (2k). Each keeps the idea whole and hedges only the riskiest element.

### k09-2B · Toggle Link Chain (seedream_v5_pro)

What it hedges:
- **The ring morph.** The risk field says "the sailor ring smoothed into a plain donut, or the bar threaded through the ring", and k04-2 found that "leaving the reference-2 pose is what morphs this clasp". So the clasp is laid exactly as reference 2 arranges it, with the ring's parts at reference 2's clock positions: the flat gate end and thin gate at 11-12, the barrel collar with the right strand's jump ring at 1, the nub at 3 and the ribs at 4 o'clock. It is then opened by one move only: the bar slides straight back along its own line and stops about 6 mm short of the ring, with velvet between them.
- **A soft clasp.** The bake-off found seedream draws this clasp "smaller and softer". The prompt fixes the tube at about a fifth of the ring's width and the opening at about two thirds, and the kicker lights the gate step and the nub.

What it keeps: the idea whole. The same top-down V on cocoa velvet, the ring at 52% down and three tenths of the width, and empty velvet either side for the '2' and the '%'. The ring is still the 0 of '20%'. B also carries take A's conformance and lesson edits (2.1-2.7): the exact reference sentence, the tone of every part, two chain ends, the count scale, true contact shadows and the no-text clause.

### k09-3B · Verdant Eternity Band (seedream_v5_pro)

What it hedges:
- **The wave morph.** The risk field names it: the S-wave straightened into a row or closed into a halo, the b02-5 and b01-3 failures and the bake-off's gpt ring. B copies reference 1's own three-quarter stance on top of a small black velvet cube, the same set-up as the listing photo. The wave, the back claws and both looped tips are copied rather than re-imagined square to the lens in a pad slit that hides the lower band. The bake-off found seedream's S-wave closest to the listing.
- **The light and the door.** The second risk is the blade blowing out the pavé, or a dial or key appearing on the door. The blade is a little wider than the ring and at moderate strength. The door is reduced to its thick plain edge and three bolt heads, deeply out of focus at the far left.

What it keeps: the idea whole. The same camera inside the night safe looking out, the door open a hand's width, and one blade of shop light finding the ring alone. The graphite walls and black velvet stay, as do the calm top quarter and right third for the H1 and the tag strings. Both looped tips are now clear for FIG. 3 THE BACK.

## Lock check

Every product card's lock is in its prompt word for word, with its "must stay X, never Y" clause, in all seven prompts. There are two deliberate lint differences, both on card 1 and both the same wording as k04a's shipped Brushed lock:
- "chunky huggie hoops" becomes "chunky hoops that hug the lobe" ("huggie" is banned in copy, and here it is not the product name);
- "never mirror-polished or silver-looking" becomes "never mirror-polished or reading as silver tone".

Each card's lock checked by script as a substring of its prompt: card 1 differs only by those two edits; cards 2, 3, 4 and 5 and both B takes contain the lock exactly.

Reference media ids are the product cards' `mediaIds`, reference 1 first:

| Slot | Ref 1 | Ref 2 |
|---|---|---|
| k09-1A | `refs/brushed-gold-huggies/01.jpg` (`7c95b6c6…`) | `refs/brushed-gold-huggies/04.jpg` (`b5b784e1…`) |
| k09-2A, k09-2B | `refs/toggle-link-chain/02.jpg` (`d3c384eb…`) | `ads-500/build/refs/toggle-link-chain__clasp.jpg` (`59d6c393…`) |
| k09-3A, k09-3B | `refs/verdant-eternity-band/03.jpg` (`2c3d1209…`) | `refs/verdant-eternity-band/01.jpg` (`702645c3…`) |
| k09-4A | `refs/verdant-cushion-studs/03.jpg` (`2e74b8da…`) | `refs/verdant-cushion-studs/04.jpg` (`1febd798…`) |
| k09-5A | `refs/woven-gold-hoops/01.jpg` (`74ed9a2b…`) | `refs/woven-gold-hoops/03.jpg` (`b77ec5ba…`) |

## Flags for the finisher (copy and layout, not the pictures)

- **Shipping line.** The camp's brand features and truth note 1 swap the footer to "CASH ON DELIVERY · PAY AT THE DOOR" and hold "FREE INSURED SHIPPING" off. The owner ruling of 20 Nov (RULINGS §6; CRAZY100 §9) overrides that:
  - every k09 ad carries "FREE INSURED SHIPPING · CASH ON DELIVERY";
  - the OFFER cards (2, 5) may also use it in the hook and primary text;
  - no ad promises a delivery time.
- **The BUY3 collection.** The camp's sell lever says cards 5 and 10 link to a BUY3 collection. There is none, so every card links to its own product page.
- **Prices.** Brushed's `compareAtPrice` 999 is never printed or struck; the price is ₹699. Per-card prices are ₹699, ₹999, ₹1,049, ₹1,099 and ₹1,049. The sell lever's basket maths (₹2,747 to ₹2,198, and so on) is planning only and is never printed as a price sum.
- **Returns.** No line may claim returns or exchanges.
- **Codes.** BUY2 10%, BUY3 20% and BUY4 30% are live (owner ruling §2), so card 2's "BUY 4 · 30% OFF" line and its Reels '3' flip can run.
- **"Huggie".** It appears only in the product name BRUSHED GOLD HUGGIES on the counter strip (card 1); body copy never uses it.
- **Card 4 is pre-order and carries no claims.** No water, tarnish or hypoallergenic words. The card line's "pre-order" stays only if the listing still carries the tag at upload. The run notes say every piece is in stock at the card's price, so never write "ships now" either way.
- **Card 2 carries no waterproof claim.** Its prompt's "no water" is a negative guard, kept on purpose.
- **"Kal bhi yahi"** is a price promise. Owner ruling §3 says it is printed only while all ten k09 prices hold for the flight.
- **"Shown magnified"** goes only where the rendered size meets the camp's 19 Feed px per listed mm (cards 1 and 3 by plan). Measure each chosen take before printing it.

## Edits to take A, edit by edit

Common to all five: the exact reference sentence, the exact no-text clause with "no watermark", the no-eyes and no-eyebrows rule, and the full-bleed sentence (learnings §5). Card-specific edits sit between them, in prompt order.

### k09-1A · Brushed Gold Huggies  (lint: clean)

1. Standard reference sentence (task rule). The plan's own notes are kept: take the finish from both, and drop the cardamom pod that reference 2 shows.
   - was: `Reference 1 is the authority on this exact piece: copy its construction, finish and colour exactly and ignore its cube, background and light; reference 2 shows the same brushed satin finish (ignore its cardamom pod; there is no pod here).`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. Copy the finish and colour of both and ignore the plaster: reference 2 shows the same brushed satin grain and the pair's true size beside a green cardamom pod (ignore the pod; there is no pod here).`

2. Lint: 'huggie' is banned and is not the product name here; same wording as k04a's shipped lock.
   - was: `1 pair of chunky huggie hoops,`
   - now: `1 pair of chunky hoops that hug the lobe,`

3. Lint: bare 'silver' in the lock's must-stay clause; same wording as k04a's shipped lock.
   - was: `never mirror-polished or silver-looking.`
   - now: `never mirror-polished or reading as silver tone.`

4. Past verification for this exact piece (k04-4: the turned piece curled into a round, cuff-like C that read as a ring; the fix written there).
   - was: `the right one stands a little behind and to the right, turned a quarter to show the 6 mm depth of the band.`
   - now: `the right one stands a little behind and to the right, turned three-quarters as the right earring in reference 1 is, showing the 6 mm depth of the band, its short C only as a shallow concave dip in its top edge and a glimpse of the smooth inner face; never curled into a round ring with both ends standing up.`

5. Scale rule (task) and learnings section 2, with this piece's own history (k02-4 drew it 1.9x beside a cassette, k04-4 3x beside hands): the pad it touches becomes a counted referent, the contact shadow is named as true.
   - was: `with crisp short contact shadows;`
   - now: `with crisp short true contact shadows where each band meets the velvet; the pad they touch is the referent: about four hoop-widths across, so the pair with its gap covers only a little over half the pad's width; they are small 14 mm earrings, never the size of napkin rings, cuffs or finger rings;`

6. Calm areas (task rule): the layout puts the pair at Feed y 380-910, which is 24-52% down the 9:16 frame, under the board and above the H1; 'a little above the middle' is pinned to those numbers.
   - was: `COMPOSITION: the pair centred left-right, a little above the middle of the frame;`
   - now: `COMPOSITION: the pair centred left-right, its centre about 40% of the way down the frame, the tops of the hoops no higher than 30% down and the front edge of the velvet pad no lower than 52% down;`

7. Card risk ('turned orange by the amber haze ... keep the haze off the hoops'), written into the light.
   - was: `keeps the satin pale and warm, never orange;`
   - now: `keeps the satin pale and warm, never orange; the amber haze stays at the very top edge and never reaches or tints the hoops;`

8. Exact no-text phrase (task rule: adds 'no watermark') and the no-eyebrows rule.
   - was: `NEGATIVES: no text, no letters, no numbers, no logos, no signs, no price tags, no hallmarks, no faces, no eyes, no hands,`
   - now: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark, no signs, no price tags, no hallmarks, no faces, no eyes, no eyebrows, no hands,`

9. Learnings section 5 (letterbox padding).
   - was: `no star glints, no lens flare.`
   - now: `no star glints, no lens flare. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`


### k09-2A · Toggle Link Chain  (lint: clean)

1. Standard reference sentence (task rule). The plan's note that reference 2 is the clasp standard is kept; reference 2 is a crop of a worn photo, so only the clasp is taken from it.
   - was: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its cube, background and light; reference 2 is a close-up of the same clasp and the standard for the ring and the bar.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It is a close-up of the same clasp on skin and the standard for the ring and the bar: copy its sailor ring (the spring gate, the small push-pin nub, the ribbed collar) and its straight one-row stone bar exactly, and take nothing else from it, not the skin. Ignore the plaster cube in reference 1.`

2. Learnings section 6 (a silver-tone jump ring appeared on this piece in wave 1): the tone of every part is named.
   - was: `Must stay a sailor ring with a straight bar 0.6-0.7x the ring, never a plain donut ring, a lobster clasp, or a curved or multi-row pave bar.`
   - now: `Must stay a sailor ring with a straight bar 0.6-0.7x the ring, never a plain donut ring, a lobster clasp, or a curved or multi-row pave bar. Every link, the ring, the gate, the nub, the bar's setting and both jump rings are the same polished 18k gold tone; never a silver-tone, white-metal or two-tone part.`

3. Past verification for this exact piece (k04-2: take B invented a third chain end at the ring): the chain's two ends are spelled out.
   - was: `never threaded through the ring.`
   - now: `never threaded through the ring. The chain has exactly two ends, and both are at the clasp: the right strand ends in the one jump ring around the ring's barrel collar beside the gate, and the left strand ends in the jump ring at the outer end of the bar. Exactly one strand comes down to the clasp from each top corner; nothing else is attached to or touches the ring.`

4. Scale rule (task) and learnings section 2: field of view in cm and a count against the links that touch the ring (the frame width follows from the ring at three tenths).
   - was: `SCALE: the ring is 22 mm across, a little larger than a 1-rupee coin; each link about 11 mm long;`
   - now: `SCALE: the field of view is about 7.5 cm wide; the ring is 22 mm across, a little larger than a 1-rupee coin, and about as wide as two of the paperclip links it touches laid end to end; each link about 11 mm long, so about seven links run along each strand from its top corner down to the clasp;`

5. Contact shadow named as true (task rule).
   - was: `crisp short contact shadows under every link and the ring;`
   - now: `crisp short true contact shadows under every link, the bar and the ring where they rest on the velvet;`

6. Exact no-text phrase (task rule: adds 'no watermark') and the no-eyes, no-eyebrows rule.
   - was: `NEGATIVES: no text, no letters, no numbers, no logos, no price tags, no hallmarks, no bust, no hands, no faces,`
   - now: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark, no price tags, no hallmarks, no bust, no hands, no faces, no eyes, no eyebrows,`

7. Learnings section 5 (letterbox padding).
   - was: `no star glints, no lens flare.`
   - now: `no star glints, no lens flare. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`


### k09-3A · Verdant Eternity Band  (lint: clean)

1. Standard reference sentence (task rule). The plan's 'copy its upright pose' and its note on reference 2 are kept.
   - was: `Reference 1 is the authority on this exact piece: copy its construction and its upright pose exactly and ignore its cube, background and light; reference 2 shows how the green ovals alternate either side of the wave.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. Copy reference 1's upright stance too, and ignore the plaster cubes in both; reference 2 shows how the green ovals alternate either side of the wave.`

2. Past verification of this exact piece: the bake-off ring on gpt_image_2_6 drew the wave 'close to a partial halo', k06-3 broad and wrapping three-quarters round one oval, k03-1 'broad and sugared' with a comb of tall back claws. The plan's card risk names the same morph.
   - was: `never a full pave halo around each oval.`
   - now: `never a full pave halo around each oval. The clear pave is ONE slim line about two tiny stones wide that snakes from oval to oval: it cups one side of an oval, crosses between it and the next oval and cups that one on the opposite side, so every oval has pave on one side only and bare claws on the other; never a broad sugared band, never a frame, loop or halo round any oval. Toward the back each green oval sits in 4 short claws, never a row of tall spikes. All metal, every claw and both looped tips are the same bright cool rhodium silver tone.`

3. Scale rule (task) and learnings section 2 (k03-1 drew this ring 2x and 4.5x): the pad it touches becomes a counted referent.
   - was: `SCALE: the band is about 20 mm across the outside;`
   - now: `SCALE: the band is about 20 mm across the outside, a small finger ring; the velvet ring pad it stands in is the referent it touches, about 3 cm wide, so the band is about two thirds of the pad's width and each green oval about a quarter of the band's outside width;`

4. Calm areas (task rule): the layout puts the ring at Feed y 400-910, which is 25-52% down the 9:16 frame; the true contact shadow is named.
   - was: `centred a little above the middle of the frame; crisp short contact shadow on the pad;`
   - now: `centred left-right with its centre about 38% of the way down the frame and the pad's front edge no lower than 52% down; crisp short true contact shadow where the band meets the pad;`

5. Two-light rule (task): the blade is named as the small hard specular kicker; card risk ('the blade of light blowing out the pave') written in.
   - was: `rakes across the front of the ring only, acting as the specular kicker:`
   - now: `rakes across the front of the ring only, acting as the small hard specular kicker, never blowing the pave out into a white glare:`

6. Lint: bare 'gold' becomes 'gold tone'; k03-1's champagne drift on the claws is named.
   - was: `the metal stays cool white, never gold, with no colour cast.`
   - now: `the metal stays cool white rhodium silver tone, never gold tone or champagne, with no colour cast.`

7. Exact no-text phrase (task rule: adds 'no watermark') and the no-eyebrows rule.
   - was: `NEGATIVES: no text, no letters, no numbers, no logos, no dial,`
   - now: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark, no dial,`

8. No-eyebrows rule (task).
   - was: `no faces, no eyes,`
   - now: `no faces, no eyes, no eyebrows,`

9. Learnings section 5 (letterbox padding).
   - was: `no star glints, no lens flare.`
   - now: `no star glints, no lens flare. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`


### k09-4A · Verdant Cushion Studs  (lint: clean)

1. Standard reference sentence (task rule). Reference 2 (04.jpg) shows her cheek, jaw and the edge of her lips, so only the stud and its size on the lobe may be taken from it (no-face hard rule).
   - was: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its cube and light; reference 2 shows it worn at true size on the lobe.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows the stud worn at true size on the lobe; use reference 2 only for how the stud sits on the lobe and its size there, and take nothing else from it: not the person, her face, cheek, jaw, lips, hair or the yellow strap.`

2. Learnings section 3 (faces creep in from a three-quarter turn), in its own words, and the card risk ('a cheek, eyelash or brow creeping into the right edge').
   - was: `not even at the edge.`
   - now: `not even at the edge. The head is turned fully away; no eyelash, brow, cheek, nose or lip breaks the outline of the head anywhere in the frame; the camera is behind the ear and a little above it, never level with the eye.`

3. Scale rule (task) and learnings section 2: the size against the named body part it touches, and a true contact shadow.
   - was: `SCALE: the stud is 13 mm across and covers most of the earlobe, about a fingertip wide;`
   - now: `SCALE: the stud is 13 mm across and covers most of the earlobe, about a fingertip wide, never spreading past the lobe; the whole ear is about four and a half studs tall, so the stud's width is about a fifth of the ear's height; a soft true contact shadow where the halo meets the lobe;`

4. Calm areas (task rule): the layout puts the stud at Feed x 640, y 680 (about 59% across and 40% down the 9:16 frame) and the hero board at Feed y 925-1095 (53-62% down). 'A little below the middle' would put the stud under the board (k02-5's stud landed at 50%).
   - was: `the lobe and stud sit a little right of centre, a little below the middle of the frame.`
   - now: `the stud sits a little right of centre, about 60% across and about 40% of the way down the frame, never lower than 48% down, with the upper part of the ear rising above it toward the top edge.`

5. Calm areas (task rule): the layout sets the H1 left-aligned on the hair at Feed y 160-340, so the calm hair is named on the left, clear of the ear.
   - was: `COMPOSITION: the top quarter is the calm, softly lit black of the swept-back hair;`
   - now: `COMPOSITION: the top quarter of the left half of the frame is the calm, softly lit black of the swept-back hair, with no ear or skin in it;`

6. Lint: bare 'gold' becomes 'gold tone' (the product card names photo 06's gold-tone drift).
   - was: `the metal stays cool white, never gold.`
   - now: `the metal stays cool white rhodium silver tone, never gold tone.`

7. Exact no-text phrase (task rule: adds 'no numbers' and 'no watermark') and no eyelashes.
   - was: `NEGATIVES: no face, no eyes, no eyebrows, no mirror,`
   - now: `NEGATIVES: no face, no eyes, no eyebrows, no eyelashes, no mirror,`

8. Exact no-text phrase (task rule).
   - was: `no text, no letters, no logos,`
   - now: `no text, no letters, no numbers, no logos, no watermark,`

9. Learnings section 5 (letterbox padding).
   - was: `no plastic skin.`
   - now: `no plastic skin. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`


### k09-5A · Woven Gold Hoops  (lint: clean)

1. Standard reference sentence (task rule). The plan's note on reference 2 is kept, with the see-through core named.
   - was: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its cube, background and light; reference 2 shows the braid, the disc and the latch from another angle.`
   - now: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece. It shows the braid, its see-through core, the disc and the latch from another angle; ignore the plaster block in both.`

2. Past verification of this exact piece (learnings section 1: the disc dropped or doubled; k03-2: the core filled with glittery mesh and the metal amber-orange; the bake-off's low tier drew two discs) and learnings section 6.
   - was: `Must stay a many-wire open braid, never a smooth tube, simple twist or oval.`
   - now: `Must stay a many-wire open braid, never a smooth tube, simple twist or oval. Each hoop has exactly one flat round disc, at the top on the latch side, never two and never none; the see-through core shows dark gaps between the wires, never a filled glittery mesh. Every wire, both discs, both hinges and both latch wires are the same clean bright lemon-yellow 18k gold tone, never orange, amber or copper.`

3. Scale rule (task) and learnings section 2 (k04-1 and k03-2 drew this hoop 1.4-1.5x): field of view in cm and a count against the pan it touches.
   - was: `SCALE: each hoop is 25 mm across, half the pan's width, a little smaller than a 10-rupee coin;`
   - now: `SCALE: the field of view is about 12 cm across; each hoop is 25 mm across, exactly half the pan's width, so two hoops laid side by side would just fill the pan, a little smaller than a 10-rupee coin; the braid is about a fifth of the hoop's width; a hoop never fills the pan;`

4. Calm areas (task rule): the layout puts the near pan and hoops at Feed y 430-910 (27-52% down the 9:16 frame) and the empty pan, which carries the ghost slots, at Feed x 760-900, y 300-420 (about 76% across, 23% down).
   - was: `a little left of centre and a little above the middle of the frame;`
   - now: `a little left of centre, its centre about 40% of the way down the frame and its lowest point no lower than 52% down; the far empty pan hangs at the upper right, its centre about 23% down and about 76% across, soft but still readable as an empty round pan;`

5. Contact shadow named as true (task rule).
   - was: `crisp contact shadows in the pan.`
   - now: `crisp true contact shadows where each hoop touches the pan.`

6. Exact no-text phrase (task rule: adds 'no watermark') and the no-eyes, no-eyebrows rule.
   - was: `NEGATIVES: no text, no letters, no numbers, no logos, no hallmarks, no price tags, no weights, no hands, no faces,`
   - now: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark, no hallmarks, no price tags, no weights, no hands, no faces, no eyes, no eyebrows,`

7. Learnings section 5 (letterbox padding).
   - was: `no star glints, no lens flare.`
   - now: `no star glints, no lens flare. Full-bleed 9:16 photograph edge to edge; no borders, bands or panels.`


## Lint

`build_prompts.py` checked every prompt (5 take A, 2 take B) for:
- the banned words: diamond, real gold, solid gold, freshwater, emerald, ruby, huggie;
- bare "gold" or "silver" without "tone";
- water words in the two prompts without a waterproof claim (Toggle, Verdant Cushion);
- the required parts:
  - 9:16;
  - the exact reference sentence;
  - a must-stay / never clause;
  - mm;
  - "true contact shadow";
  - a soft light and the "small hard specular kicker";
  - calm areas;
  - the exact no-text clause "no text, no letters, no numbers, no logos, no watermark";
  - no faces, no eyes, no eyebrows;
  - one product;
  - full-bleed.

All 7 prompts are clean. The only water word in a no-claim prompt is Toggle's "no water", a negative guard from the plan. "Gold" appears only as "18k gold tone", "gold tone" or "gold-tone". "Silver" appears only as "rhodium silver tone" or "silver tone"/"silver-tone". The first run flagged "never a silver, white-metal or two-tone part" on card 2; it now reads "never a silver-tone, white-metal or two-tone part" in both card 2 prompts (part of edit 2.2 above and of take B).

## Generation record

- **Balance:** 201.21 before (18:55Z), 164.21 when the last job finished (19:01Z) and 157.71 at the final read (19:02Z).
  - This batch spent **10 credits**: five GPT Image 2.6 jobs at quality medium, at 1 credit each, and two Seedream 5.0 Pro jobs at 2.5 each.
  - The rest of the drop (43.5 credits by the final read) belongs to other sessions sharing the account. The transaction ledger carries no job ids. It shows GPT Image 2.6 spends of 1 credit and Seedream 5.0 Pro spends of 2.5 interleaved with other sessions' spends in the same seconds.
- **Models:** every job was served as requested.
  - Take A: `gpt_image_2_6` (medium, 2k, 9:16), at 1520 x 2688.
  - Take B: `seedream_v5_pro` (2k, 9:16), at 1536 x 2720.
- **Rounds** (only refused items were resubmitted; no outcome was ever unknown):
  1. 18:55Z: one call with all 7 items. All 7 were refused with `submission_failed` (429), so none was submitted.
  2. 18:56Z, about 35 s later: k09-1A, k09-3B and k09-5A were accepted. k09-2A, 2B, 3A and 4A were refused again (429).
  3. 18:58Z, after jobs_wait polling on the three accepted jobs (about 45 s): k09-2A and k09-4A were accepted. k09-2B and 3A were refused (429).
  4. 18:59Z, after polling (about 40 s): k09-2B and k09-3A were accepted.
- **Outcomes:** all 7 jobs completed first time. None failed or was flagged nsfw, so no trigger word was removed.
- **Files:** `pics/k09-1A.png`, `2A`, `2B`, `3A`, `3B`, `4A` and `5A`, downloaded unchanged with curl. `jobs.json` and `prompts.json` hold no URLs.

## Shooter's first look (not the verification pass)

I looked at each take at 900 px tall, and at full-resolution crops of the toggle clasp (A and B) and the stud's right edge.

- **k09-1A, Brushed.**
  - The pair stands on a black velvet pad on dark glass, with tube-light streaks, warm bokeh and amber at the top edge. It reads as Naira's counter at night.
  - Left: the barrel face. Right: turned, showing the concave dip in its top edge, not curled into a ring.
  - Brushed satin with fine straight lines, pale warm 18k gold tone, no mirror. The haze stays off the hoops.
  - Check the scale: the pair spans about 55% of the width (asked about half).
  - The pad's front edge sits near 58% down (asked no lower than 52%), so the H1 band (Feed y 930-1025) sits over the pad's reflection in the glass. Check the layout.
- **k09-2A, Toggle (gpt).**
  - The clasp construction is right at full size:
    - the flat gate end with its thin gate across the top;
    - the ribbed barrel collar with the right strand's jump ring at about 1 o'clock;
    - the ball nub at 3;
    - the ribs at 4;
    - all in one 18k gold tone.
  - There are two chain ends.
  - **But the bar lies across the ring's upper-left tube**, in reference 2's closed pose, not beside it. That is the risk the card names, so the '0' would read as 'Ø'.
  - The bar shows only 5 larger stones (the lock says about 9 tiny ones).
- **k09-2B, Toggle (seedream).** It has the same ring construction, matching reference 2 closely, with about 8 stones on a slimmer bar. **Its bar also crosses the ring's upper-left tube**, with its tip in the opening: the closed reference-2 pose, despite "slid straight back out". Both models pulled the bar back into reference 2's closed position.
  - If the verifier rules the Ø unusable, the redo note should give the bar a fixed, measured place well clear of the ring (for example, lying along the left strand a full ring-width away). Shooting the ring alone is not an option, because the bar is part of the one product.
- **k09-3A, Verdant Eternity (gpt).**
  - The band stands upright in a black velvet ring pad inside a graphite safe. The open door at the left has three plain round bolts and a cool slit of light, with no dial and no key.
  - The pose came out as reference 1's three-quarter stance, not square to the lens. The S-wave cups each oval on one side and alternates, with no halo, and both looped tips show at the right.
  - **The ring is large in frame**, about 60-65% of the width (asked four tenths), spanning about 22-57% down. Check "SHOWN MAGNIFIED" and the H1 and tag zones.
- **k09-3B, Verdant Eternity (seedream).**
  - The band stands free on a black velvet cube in reference 1's three-quarter stance, and both looped tips are clear.
  - The S-wave cups one side of each oval. The door edge has three bolts, and there is a soft cool light from the door gap.
  - The ring sits at about 40-68% down (asked a centre at 38%), so it sits low. Check the Feed and Story zones.
- **k09-4A, Verdant Cushion.**
  - The left ear from behind, with sleek black hair, a bare neck, an ivory collar at the foot and the shop's bokeh at the left.
  - One stud on the lobe: a cushion green stone in a smooth bezel, with a single spiky sunburst ring of clear stones in rhodium silver tone.
  - No eye, brow, lash, nose or lips anywhere. The right edge shows only the skin in front of the ear down to the jaw. Check it at full size against the face rule.
  - The stud sits at about 70% across and 46% down (asked about 60% and 40%).
- **k09-5A, Woven.**
  - A dark oxidised antique balance on oxblood velvet, with the beam clearly tipped: the near left pan is low and the far right pan high and empty.
  - Plain brass, with no stamps or weights.
  - In the near pan, one hoop stands showing its disc and latch and one lies flat with its disc. Each has one disc, and the braid is open with dark gaps. The 18k gold tone reads warm yellow.
  - The near pan sits about 43-60% down (asked no lower than 52%), and the empty pan is at about 25% down, 85% across. Check the Feed card and beat zones.
  - The hoops are about 0.4 of the pan's width (asked 0.5), so check the scale against the pan.

I saw no generated text, logos, faces or extra jewellery in any of the seven. The full verification is the verifier's.
