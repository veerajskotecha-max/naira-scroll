# k04r · brief applied (camp k04 MUJHE KUCH NAHI CHAHIYE., re-shoot of cards 1-5)

Each card's take A is its planned `prompt` in `crazy100.json`, with three sets of edits:
- every redo-fix clause in that card's log, `batches/k04a/verify/k04-N.md`. This covers the take section, the redo section and the "if one more take" recommendations;
- the six points of `batches/k04r/brief_diff.md`;
- `build/learnings.md` wave 1, lessons 1-7.

Where a verify-log clause conflicts with the diff, the diff wins. Where the diff conflicts with a product card, the product card wins, and the conflict is logged below. The prompts are in `prompts.json`.

## Sources read

- `crazy100.json`: camp k04, its idea, textual graphic, brand features and changes, and ads 1-5. Each ad's picture, prompt, size line and risk were read.
- `CRAZY100.md`: §6 k04 and §9 (process, hedge list, owner rulings).
- `build/learnings.md` and `batches/bakeoff/README.md`.
- `batches/k04a/verify/k04-1.md` through `k04-5.md`, `batches/k04a/prompts.json` and `batches/k04a/jobs_redo.json` (the R prompts for cards 2-5).
- The five product cards and their reference photos (ref 1 and ref 2 of each were looked at).

`batches/k04a/loop.md` does not exist, so nothing was applied from it.

## Models and takes

- Every take A is `gpt_image_2_6`: medium, 2k, 9:16.
- Takes B are `seedream_v5_pro`: 2k, 9:16. Only two cards get one: **k04-4** and **k04-5**. These are the cards whose failure the old model would not be talked out of:
  - **k04-5** failed the lock twice, the same way each time: the 2 x 4 cap stones came back as a micro-pavé field, even with an explicit 8-stone clause. Its risk field names the overlap and the caps.
  - **k04-4** failed scale twice, at 3x and then 2.4x. The model held the earrings at one fixed render size whatever the prompt asked. Its risk field names scale with two hands in frame.
- The other three cards passed construction at least once in k04a, or the diff removes their failure mode:
  - k04-1's braid passed, so only the scale needs fixing.
  - k04-2's ref-2 pose passed construction in R, so only the placement needs fixing.
  - k04-3's ring is now worn, and wearing it anchors its scale to the finger.

## Edits applied to all seven prompts

| # | Source | Edit |
|---|---|---|
| G1 | brief task | The reference sentence is now word for word: "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece." |
| G2 | diff 6, learning 5 | "a full-bleed photograph edge to edge, with no borders, bands or panels" added after "Vertical 9:16". |
| G3 | learning 6 | Every part's metal tone is named, for example "every link, the ring, the bar and every jump ring are the same polished 18k gold tone". |
| G4 | learning 2 | Scale is given against a named body part touching the piece, with a field of view in cm and a true contact shadow. |
| G5 | brief task | Every prompt has the closing clauses "No face, no eyes, no eyebrows", "No text, no letters, no numbers, no logos, no watermark, no printing on anything" and "One product only: this one ...". |
| G6 | lint | Every prompt was linted for the banned words: diamond, real gold, solid gold, freshwater, emerald, ruby, huggie, and "gold" or "silver" not followed by "tone". The prompts are clean, and the lock's must-stay sentence was checked verbatim in each. |

## k04-1 Woven Gold Hoops: take A only

| # | Source | Edit |
|---|---|---|
| 1.1 | verify fix 1 + diff 1 | The SCALE sentence is replaced: "true size, and small in her hands". Each hoop is 25 mm, "about one and a half of her finger widths", about the top joint of her thumb, and "much narrower than her palm". The braid is a third of a finger. The hands span the frame, a field of view of about 15 cm, so each hoop is "about one sixth of the frame width; never enlarge the hoops to fill the palm". A short note names last time's 36 mm. |
| 1.2 | verify fix 2 + diff 1 | GRADE now asks for "the clean, bright lemon-yellow 18k gold tone of reference 1, with a pale butter-yellow disc ... never orange, amber, copper, brassy or a deep 22k yellow". LIGHT adds a small neutral warm-white key on the hoops. |
| 1.3 | verify fix 3 + diff 1 | The haldi is now "only the very tip of her right index finger carries the faintest pale haldi tint ... no orange or yellow fingers". |
| 1.4 | verify fix 4 + diff 1 | COMPOSITION is replaced. The pair sits 40-52% down and 40-75% across. The thumb tips are no higher than 38%. The top 38% is calm cocoa wall. The showcase is "one faint glint at the far top-right corner, no visible cabinet, glass box, vitrine, frame or counter". The left 22% is shadow. Below 60% there is only the dim heel of her hands and the pallu. |
| 1.5 | verify fix 5 | The gesture is now "both thumbs lifted a little and pressed toward the camera ... both thumbs visible". |
| 1.6 | learning 1 | "Exactly one flat disc on each hoop, never two and never none" is added after the lock. |

## k04-2 Toggle Link Chain: take A only

| # | Source | Edit |
|---|---|---|
| 2.1 | verify fix 7 (k04a) | The plan's mid-turn pose is **not** shot. The verifier found that pose is what morphs the sailor ring. Take A is built on the k04a R prompt instead: the closed clasp in the ref-2 pose, "the instant the clasp has been closed, before the hands let go". The camp's quarter turn lives in the drawn proof (BAR THROUGH · QUARTER TURN · CLOSED). |
| 2.2 | verify fixes 1-6 | These were already in R and are kept word for word: the two-chain-ends topology, the fingers resting on the lying chain, the Peter Pan collar in deep shadow, and the keep-list clauses (the ref-2 pose, the scale-by-links sentences, "never rays, never star-shaped glints", the face gate, "No water, no droplets"). |
| 2.3 | verify "one more regeneration" | The COMPOSITION opener is now "the centre of the bun sits exactly on the top edge of the picture, so only the bun's lower half and its band show". The note on the 57-60% placement is kept. |
| 2.4 | verify "one more regeneration" + diff 2 | The fingertips are now "an adult fingertip about 15 mm wide, about two thirds of the ring's width and a little wider than the bar is long". The ring is "about 22 mm across, a little wider than one fingertip". |
| 2.5 | diff 2 + learning 1 | The ring is now "the listing's own ring: one thick smooth round tube with one ribbed gate collar and one small push-pin nub, never a generic marine clasp with two ribbed collars or a nub on top". The bar is "dead straight, with one single row of tiny clear stones". |
| 2.6 | diff 2 + learning 6 | "Every link, the ring, the bar and every jump ring are the same polished 18k gold tone; no part in another metal tone." |
| 2.7 | learning 3 | The face gate now says "the camera stays behind her head, never level with an eye ... no eyelash, brow, cheek, nose or lip breaks the outline of her head". |

## k04-3 Verdant Eternity Band: take A only

| # | Source | Edit |
|---|---|---|
| 3.1 | diff 3 | **The ring is worn.** It is "WORN on her ring finger: slid all the way down and seated snugly at the base of that finger, just beyond the knuckle". The front wave faces the camera across the top of the finger, and the open back is hidden on the palm side. It is "never slipped over a fingertip, never loose, never on any other finger". |
| 3.2 | diff 3 (supersedes verify fix 1) | The k04a fix that stood the ring "alone, upright on its edge ... never on any finger" is dropped, because the diff now puts the ring on the finger. Its fallback clause goes with it. |
| 3.3 | diff 3 + bake-off note | A WAVE clause is added after the lock: "one single slim line of tiny clear stones snakes across the front in an S ... each green oval is cupped by the wave on one side only ... never a ring of clear stones around any oval, never a second line of clear stones". The bake-off found that gpt_image_2_6 drifts toward a partial halo. "Never a closed ring" is kept as its own sentence, so that the lock's must-stay sentence stays verbatim. |
| 3.4 | verify fix 5 + idea | The thread stays, because it is the card's idea. It is still "plain bright white cotton ... white and never pink". It now "lies loose and untied on the sheet just beyond her fingertips in a soft open curve with two free ends: the measuring trick nobody needed; it never forms a closed loop and never touches or circles any finger". This avoids the risk field's "thread read as a second ring", and it fits the beat ("Skip the thread trick"). |
| 3.5 | verify further fix 1 | "Both references are much closer views than this picture: copy the ring's construction, never their framing or their size." |
| 3.6 | verify fix 2 + further fix 2, adapted to the worn ring | SCALE: "her fingers are big in the frame and the ring is small and fine on them". The field of view is about 16 cm, so each fingertip is about a tenth of the width. The band is "exactly as wide as the finger it sits on, about 18 mm across outside, never wider than the finger". It is 6 mm deep, and each oval is a third of the nail. The note "twice before ... two to two and a half times too big" is kept. |
| 3.7 | verify fix 3 + further fix 3, adapted | COMPOSITION: the hand enters from the left in a band 36-56% down, with the back of the hand in shadow at the left (under the ladder). The ring is 34-42% across and 46% down. The fingertips stop about 80% across, with the thread beyond them. The top 34% is clear, and the lower 42% is empty sheet. The field and the positions were rebalanced, because a ring at the base of the finger sits about 7 cm from the fingertip. |
| 3.8 | verify fix 4 | "A tight, soft pool of warm tungsten bedside light ... about 8 cm across", with the knuckles and wrist falling into umber. The specular kicker clause is kept. |
| 3.9 | verify further fix 4 | "Its thumb on the far side" is added, so the hand reads as the right hand. |

## k04-4 Brushed Gold Huggies: takes A and B

| # | Source | Edit |
|---|---|---|
| 4.1 | verify fixes 1-8 | These were already in the k04a R prompt and are kept: true scale against both hands; her fingertips only, with the wrist out of frame; his raised-knuckle push with only the cuff showing; the paper ripple; the smooth left fall-off with no seam; the turned piece shown as ref 1's right earring; the walnut table; and the wrist-band negatives. |
| 4.2 | diff 4 | Each earring is now "about as wide as one of her fingernails". The envelope is "an ordinary salary envelope about 23 cm wide ... about twenty of these earrings standing side by side would fit across it". The field of view is stated in cm in both takes: about 16 cm in A and about 9 cm in B. |
| 4.3 | diff 4 vs product card | **Not applied as written:** "each huggie about 12 mm tall". The product card lists 14 x 9.8 mm, and its copy notes flag "12 mm" as stale. The prompts keep 14 mm. The diff's "eighteen fit across" is restated from the true width: twenty pieces at 9.8 mm, plus small gaps, fill about 23 cm. |
| 4.4 | verify "one more regeneration" | The placement is anchored to objects as well as percentages: "the pair stands just to the left of her fingertips, a little above the middle of the frame", and "the torn top edge of the envelope crosses the frame about a third of the way down". |
| 4.5 | lint | The lock keeps all its facts. "Chunky huggie hoops" is written "chunky hoops that hug the lobe", because "huggie" is on the banned list. "Never ... silver-looking" is written "never ... reading as silver tone", because bare "silver" is banned. Both rewordings match k04a. |
| 4.6 | product card | Ref 2's cardamom pod is used as a height cue and then left out: "the cardamom pod ... is about the same height as each earring; leave the pod itself out". |
| 4.B | risk field + verify "one more regeneration" | **Take B (hedge):** the verifier's extreme close-up. The field of view is about 9 cm, so the referents become big rather than the earrings small. Only her index and middle fingertips enter from the right, and only his thumb tip and index knuckle from the bottom. Her fingertip is a sixth of the width, his thumb a fifth, and each earring about two thirds of her fingertip. The tug, the ripple and the torn edge for the headline are kept. This avoids the plan's hedge (his hand alone), which the verifier said carries the same scale risk. |

## k04-5 Triple Coil Wrap Bangle: takes A and B

| # | Source | Edit |
|---|---|---|
| 5.1 | diff 5 + verify "if the owner funds another take" 1 | The trigger word "pavé" is removed from both prompts, including the lock and the LIGHT clause ("each clear stone"). In the lock, "8 clear round pavé stones in 2 columns of 4" becomes "8 separate round clear stones in 2 columns of 4". The rest of the lock, including its must-stay sentence, is verbatim. |
| 5.2 | diff 5 | A CAPS clause, "copied exactly from references 1 and 2", is added: "one solid mirror-polished 18k gold tone block ... exactly 8 separate round clear stones, 2 side by side and 4 in a row, each stone as wide as two ribs of the wire, each in its own raised round metal cup, with polished gold tone metal showing between every stone". It ends "never a field of tiny glittering stones ... (twice before ... forty or more tiny stones)". |
| 5.3 | diff 5 | The turn count from the photos is stated: "COUNT, from references 1 and 2: exactly 2 full turns; 2 wires at the back and at both sides, and 3 wires only in the short span between the 2 offset caps". |
| 5.4 | verify recommendation 2 | The forearm "enters bare from the right edge, with no sleeve and no fabric in frame". The mustard sleeve was twice the biggest warm mass. |
| 5.5 | verify recommendation 3 | The tiers are "three identical open, lidless, single-tier round steel containers, short open cylinders like deep bowls ... No lid anywhere, nothing stacked, no carrier frame or handle". |
| 5.6 | verify recommendation 4 | The wall is now "cool blue-grey white wall tiles ... never warm beige". |
| 5.7 | verify recommendation 5 | "Six to ten clear water droplets bead directly on the gold tone ribs of the bangle itself." The piece is listed as waterproof. |
| 5.8 | verify recommendation 6 | R's scale, framing and cap-shape clauses are kept: a 24 cm field, the bangle at 30% of the width, placed 36-52% down and 45-75% across, the rims 42-56% down, no window, and the dark basin in the lower 30%. The PROPORTION clause is also kept: 17 wire-widths across, and the turns half a finger. |
| 5.9 | product card | "18k gold tone or rhodium silver tone" in the lock becomes "18k gold tone", the variant shot (Gold, refs 01 and 03). The style word in brackets after "snake-coil" is dropped, as in k04a, so that no designer style is named. |
| 5.B | risk field ("the tap off, only droplets") + caps lesson | **Take B (hedge):** the tap is off and the washing is done. Her wet hand rests on the rim of the nearest of three open tiers on the draining board, with the other two in soft focus as bright rim arcs. The bangle is posed on the wrist as in ref 2, with droplets on its ribs. The camera is closer, with a 14 cm field and the bangle at half the width, so each cap is big enough for its 8 stones to read one by one. This hedges the stone count and the splash over the caps. It keeps the three tiers, the water and the never-off idea. |

## Flags for the finisher (copy, not pictures)

- **Trust line:** every ad carries "FREE INSURED SHIPPING · CASH ON DELIVERY", under the owner ruling of 20 Nov. This overrides the bible's "never free shipping" and the old footnotes. k04-3 (OBJECTION) and k04-5 (OFFER) may also use it in the hook and primary text. Never promise a delivery time, and never mention returns or exchanges.
- **k04-2:** its size line uses the product card's referent, "RING ABOUT 22 MM, A LITTLE LARGER THAN A ₹1 COIN", only if the take passes. The thumb referent cannot be shown in this pose.
- **k04-3:** the gauge is scaled from the worn ring as rendered. The ring now sits on the finger and does not stand beside it, so the size line keeps "ADJUSTS TO FIT US 5 TO 9".
- **k04-4:** the F2 name prints BRUSHED 18K GOLD TONE EARRINGS, and "huggie" stays out of all copy.
