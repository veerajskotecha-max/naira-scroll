# k01r · brief applied (camp k01 AUNTY NE CHASHMA LAGAYA., rescue of cards 1, 2, 3, 5)

Take A for each card is the card's planned `prompt` in `crazy100.json`, with two sets of edits:
- every redo-fix clause from that card's log in `batches/k01a/verify/k01-N.md`;
- the five points of `batches/k01r/brief_diff.md`.

Where a redo-fix clause conflicts with the diff, the diff wins. The prompts are in `prompts.json`.

Sources read:
- `crazy100.json` (camp k01: idea, textual graphic, changes, and ads 1, 2, 3 and 5);
- `CRAZY100.md` §6 k01 and §9, including the owner rulings;
- `build/learnings.md` (wave 1, lessons 1-7);
- `batches/bakeoff/README.md`;
- `batches/k01a/verify/k01-1.md`, `k01-2.md`, `k01-3.md` and `k01-5.md`;
- the k01a prompts, `jobs_redo.json` and the two unshot redo prompts in the scratchpad (`k01-2R/prompt.txt`, `k01-5R/prompt.txt`);
- the four product cards.

`batches/k01a/loop.md` does not exist, so there was nothing to apply from it.

## Edits applied to all four prompts

| # | Source | Edit |
|---|---|---|
| G1 | diff 1 | **The lens is no longer in the picture.** Every "lens hovers 8 cm in front of the piece, centred on it" clause is removed, along with the redo fixes that pushed the lens in front: k01-1 fix 6, k01-2 fix 4, k01-3 fix 5 and k01-5 fix 4. In their place, the aunty's hand holds her folded tortoiseshell half-moon glasses by one folded temple arm, beside the piece and never in front of it. The glass shows only background, "never the [piece]". |
| G2 | diff 1 | New **CLEAN SPACE** clause: a calm, evenly lit area centred on the piece, with no fingers, glasses, temple arms, loose hairs or bright bokeh crossing it and nothing in front of the piece. The designer draws the SVG half-moon lens there and fills it with the 2x crop. Its size is set to the lens footprint: 5 cm for the hoop (11 cm field), 5 cm for the ring (11 cm), 4 cm for the stud (11 cm) and 6.5 cm for the toggle (15 cm). |
| G3 | diff 1 + learning 4 | New negative: "no magnifier and no magnified view anywhere". The model must not draw its own loupe, and must not repeat k01-2A's phantom ring inside the glass. |
| G4 | diff 2 + learning 3 | The face clause is now k01-1R's wording, which held: "head turned fully away ... no eyelash, eyelid, brow, cheek, nose or lip breaks the outline of her head", and the camera is behind the ear. k01-5 gets the diff's necklace framing (G-5 below). |
| G5 | diff 3 + learning 2 | Scale is now given against a named body part, with the field of view in cm. Each card's values are in the per-card sections. |
| G6 | diff 4 + learning 6 | A METAL line names every part in one 18k gold tone and bans two-tone. |
| G7 | diff 5 + learning 5 | "a full-bleed photograph edge to edge with no borders, bands or panels" |
| G8 | shooter spec | The reference sentence is now exact: "Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece." The card's own note on reference 2 follows it. |
| G9 | shooter spec | The negatives now read "no text, no letters, no numbers, no logos, no watermark"; "no eyes, no eyebrows" is added. |
| G10 | shooter spec | The light is now stated as "two lights only": one soft fill and one small hard specular kicker. |
| G11 | k01a practice | "at 4K (2160 x 3840)" became "at high resolution", because the jobs render at 2k. |
| G12 | learnings 4, k01-3 recommendation 3 | Placement is now written as landmarks ("a little right of the frame's centre", "just above the middle of the frame", "60% of the way across") as well as percentages, because percentages alone were ignored. The headline band (14-32%) and the card band (below 55%) are named as calm. |

## Two errors in brief_diff.md, applied to the right piece

1. **Diff 4 says "Halo Curve = the two four-point stars exactly as reference 1, a mirror-polished band".**
   - The Halo Curve Ring has no stars. Its lock is a wire, two bezels, a tiger eye and a crystal.
   - The two four-point stars and the "smooth, mirror-polished band" are the Verdant Circlet Studs' lock and k01-3R's held fix clause 4.
   - So the stars clause went into **k01-3**.
   - Only the "mirror-polished band" half went into **k01-2**, which is true of the ring: "the wire and both bezels are one mirror-polished band".
   - Putting stars on the ring would have redesigned the piece and broken hard rule 1.
2. **Diff 3 says "Verdant Circlet stud about 10 mm, the size of the fingernail of a little finger".**
   - 10 mm is the green cushion stone. The stud is 16.8 mm tall, with a circlet about 14 mm wide (see the lock and `sizeMm`).
   - Prompting the whole stud at 10 mm would make it about 0.6x true, an unintended mis-scale.
   - The prompt applies the referent to the stone: "the green cushion stone is about 10 mm, about the size of the fingernail of a little finger".
   - It keeps the stud true: "16.8 mm tall, a little less than a third of the ear's height". This is k01-3 fix 2, which held at about 1.15x.

## k01-1A · Woven Gold Hoops

The base is the plan prompt plus all of k01-1R's fix clauses (k01-1R is the job recorded in `jobs_redo.json`).

| Clause | Source | Applied as |
|---|---|---|
| Braid | k01-1 fix 1, diff 4 | the full THE BRAID clause, with "NOT a flat three-strand ribbon ... NOT a twisted rope" and "twice before it came out as a flat three-strand ribbon" |
| Disc | k01-1 fix 2, diff 4 | "exactly ONE flat, round, mirror-polished disc, about one third of the hoop's width, on the latch end only ... Never two discs" |
| Latch | k01-1 fix 3 | "one thin curved latch wire ... passes through the earlobe piercing ... one closed ring" |
| Scale | k01-1 fix 4, diff 3 | "the hoop's outer width is a little less than half the ear's height ... two hoops stacked would not reach the top of the ear ... a 25 mm coin". Both past drifts (0.59 and 0.62) are named. |
| Face | k01-1 fix 5, diff 2 | the held wording, with "eyelid" added. Also: "beyond the outline of her head ... only out-of-focus plum night, never a cheek". |
| Glasses | k01-1 fix 6 replaced by diff 1 | Folded half-moons held by one folded temple arm, beside the hoop to the left, over the dark background. The near lens's nearest edge is 2 cm outside the clean area, and the bridge and the far lens may leave the left edge. The "complete pair in front of the hoop" request is dropped, since it gave a malformed one-lens prop. |
| Placement | k01-1 fix 7, verify recommendation | The hoop moves off-centre: its centre is about 60% across, the disc at about 37% and its bottom no lower than 50%. This leaves room on the left for the glasses outside the lens footprint. The wrist and pallu stay at the left edge, and the zone below 55% is calm. |
| Finish | k01-1 fix 8, diff 4 | "mirror polish ... never satin, brushed, matte" in METAL |
| Clean space | diff 1 | about 5 cm round the hoop |
| Ear | plan "right earlobe" changed to "left earlobe" | Seen from behind on the left outline of the head, this is the ear k01-1R's wording actually framed, and it stays clear of the face. |

## k01-2A · Halo Curve Ring

The base is the plan prompt plus the seven clauses of the unshot k01-2R. That redo was never submitted because of a 429 and a blocked retry.

| Clause | Source | Applied as |
|---|---|---|
| Reference | k01-2 fix 1 | the exact sentence, then "Reference 2 shows the ring worn on one finger, close up, at true scale: copy how the two stones sit on the finger, never its framing" |
| Stones | k01-2 fix 2 | the diagonal offset as in reference 2; soft irregular facet lines, never a checkerboard; deep golden-brown, not light honey; the crystal never pink or blue |
| Finger | k01-2 fix 3 | the index finger, the topmost finger curled round the glass |
| Lens over the ring | k01-2 fix 4 replaced by diff 1 | The aunty's hand comes from the right edge at ring height and holds the folded half-moons beside the ring, never over it. The fix's "the ring appears exactly once ... no second, smaller or larger copy ... inside or outside the glasses" is kept, because it guards the phantom ring of k01-2A. |
| Half-moons | k01-2 fix 5 | "flat-topped D-shaped lenses ... about 2.5 cm tall ... never round, oval or full-height lenses" |
| Grid | k01-2 fix 6 | 0-32% is only night with amber points; the ring at 43% of the height. Its horizontal position moves from 50% to 42% of the width, to leave room for the glasses on the right. The aunty and the pallu stay at the right edge only; the kettle is small at the far left at 30-45%; the glass rim is at 34%; below 60% is dark and calm. |
| Scale | k01-2 fix 7, diff 3 | an 11 cm field; the two stones span about 20% of the frame's width and about the width of the finger |
| Metal | diff 4 (the half that fits this ring) | "one mirror-polished band of warm-neutral 18k gold tone, never orange, copper, brassy or two-tone" |
| Hand | new | The wearer's wrist leaves at the lower left, so her hand and the aunty's hand do not crowd the same edge. |
| Lint | new | "no halo" became "no border of small stones round either stone", to keep the word that pulls a halo out of the prompt. |

## k01-3A · Verdant Circlet Studs

The base is the plan prompt plus k01-3R's clauses (k01-3R is the job recorded in `jobs_redo.json`) and the verify note's recommendation 3.

| Clause | Source | Applied as |
|---|---|---|
| Framing and face | k01-3 fix 1 replaced by diff 2 and recommendation 3 | The cheek-cut wording did not hold: the eye corner and brow tail appeared. It is replaced by k01-1R's held wording: the camera behind her, a little to her left; the left ear on the left outline of the head; "never a cheek". |
| Scale | k01-3 fix 2, diff 3 (corrected, see above) | the green stone 10 mm, a little-finger nail; the stud 16.8 mm, a little less than a third of the ear's height; the green stone over the lower half of the lobe |
| Orientation | k01-3 fix 3 | the big pearl toward the back of the head (frame right), the stars toward the face (frame left) |
| Stars and metal | k01-3 fix 4, diff 4 (moved from "Halo Curve") | solid, bevelled, mirror-polished four-point stars exactly as reference 1; a smooth, mirror-polished band; never filigree or crinkled metal; the collet, circlet, stars and settings all in the same 18k gold tone |
| Glasses and lens | k01-3 fix 5 replaced by diff 1 | The glasses come from the left edge, not the top edge, so the hand stays out of the headline band, which is what failed on k01-3R. They are folded half-moons beside the stud over the indigo night. Recommendation 4 offered to relax the half-moon shape; I kept it, because the diff names half-moons and the glasses no longer have to hold a 2x view. |
| Placement | k01-3 fix 6, recommendation 3 | The green stone's top at 37% and the circlet's bottom at 46%, with landmarks: "a little right of the frame's centre", "just above the middle". The hand is not in the top band. |
| Negatives | k01-3R change | "no star-shaped light glints ... (the two metal four-point stars on the circlet are part of the piece and must stay)" |
| Clean space | diff 1 | about 4 cm round the stud |

## k01-5A · Toggle Link Chain

The base is the plan prompt plus the eight clauses of the unshot k01-5R. That redo was never submitted because of a 429 and a blocked retry.

| Clause | Source | Applied as |
|---|---|---|
| Scale | k01-5 fix 1, diff 3 | The count wording: neck five ring-widths, about twelve links a side, four fingers wider than three rings, the ring narrower than the collarbone hollow. The "15% of the frame's width" fraction is deleted. Added from diff 3: "a little wider than a fingertip"; "the 50 cm chain lies along the collarbones and dips to the clasp ... about three ring-widths below the hollow of the throat". |
| Clasp pose | k01-5 fix 2 | "posed exactly as in reference 2 ... copy its construction and pose, never its framing or its size" |
| Glass and colour | k01-5 fix 3, diff 4 | METAL names every link, the ring, the gate, the bar, the jump ring and the last link in one 18k gold tone, "never silver tone, white metal, rose tone"; the glass has no glare or white sheen. The "chain passes behind the rim" part is dropped, because nothing is behind the glass now. |
| Glasses | k01-5 fix 4 replaced by diff 1 | Her own left hand comes from the right edge and holds her folded half-moons beside the clasp, never in front of it; her fingers stay in the right fifth, at 40-62% of the height. |
| Face | k01-5 fix 5 replaced by diff 2 | "framed from the base of the neck down to the neckline of her blouse; the top edge ... crosses the lower neck about two finger-widths above the hollow of the throat, so the chin, the jaw and everything above lie outside the frame". Two finger-widths is the height that puts the clasp at about 42% once it sits three ring-widths below the hollow. |
| Placement | k01-5 fix 6 | The ring's centre at 42% of the height and 45% of the width; nothing of the necklace below 50%; below 55% only silk. The blouse edge is about one finger-width below the ring, at about 52%. |
| Top band | k01-5 fix 7 | the lower neck and collarbones in soft warm shadow at 14-32%, the upper links crisp |
| Negatives | k01-5 fix 8 | "no silver-tone, white-metal or two-tone parts"; "no glare on the glass"; "no metallic zari or trim". The wording was linted, so "gold zari" became "metallic zari". |
| Clean space | diff 1 | about 6.5 cm round the clasp |
| Lint | k01a lesson (a headless crop worded around chest and skin was refused) | The prompt says "the blouse neckline" and "the upper breastbone", not "chest". |

## Take B: none

The role allots take B to 0 cards. All four cards are single take A jobs on `gpt_image_2_6` (high, 2k, 9:16). The order of risk, kept here for a later redo on `seedream_v5_pro`:
1. k01-1: the braid has morphed on every nano_banana take, though it was good on gpt_image_2_6 in the bake-off.
2. k01-5: scale on an older neck.
3. k01-3: the face and the stars.
4. k01-2: staging only; the ring was already faithful.

## Lint

All four prompts were checked:
- **Banned words:** diamond, real gold, solid gold, freshwater, emerald, ruby, huggie; "gold" or "silver" not followed by "tone". None found.
- **Required parts:** 9:16, the exact reference sentence, the lock's must-stay clause, the no-text negatives with watermark, no eyes, one product only, contact shadow, specular kicker, field of view in cm, full-bleed, headline and price-card zones. All present.
- **URLs:** none.

Water appears only as "no water" in k01-5's negatives (Toggle has no waterproof claim). k01-2's chai is tea in a glass on a piece that does carry a waterproof claim.

Media ids come from each product card's `mediaIds`, reference 1 first:

| Card | Reference 1 | Reference 2 |
|---|---|---|
| Woven | `refs/woven-gold-hoops/01.jpg` | `03.jpg` |
| Halo Curve | `refs/halo-curve-ring/02.jpg` | `01.jpg` |
| Verdant Circlet | `refs/verdant-circlet-studs/01.jpg` | `03.jpg` |
| Toggle | `refs/toggle-link-chain/02.jpg` | `ads-500/build/refs/toggle-link-chain__clasp.jpg` |
