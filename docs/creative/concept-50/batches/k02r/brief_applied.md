# k02r brief applied (camp k02 SHAADI KA VIDEO., rescue of cards 1 and 4)

Inputs read: `crazy100.json` (camp k02 and ads 1 and 4), `CRAZY100.md` (k02 section, production process and the owner rulings),
`build/learnings.md` (wave 1), `batches/k02r/brief_diff.md` (the director's rescue note), and `batches/k02a/verify/k02-1.md` and
`k02-4.md` (the take sections and the redo sections). `batches/k02a/loop.md` does not exist, so there was no loop note to apply.

Two cards, two slots: `k02-1A` and `k02-4A`. No take B, because the step allots 0 hedge cards. The verifier's redo will run on
`seedream_v5_pro`. Both prompts were linted. They contain no "diamond", "real gold", "solid gold", "freshwater", "emerald", "ruby",
"huggie", "quatrefoil" or "clover". Every "gold" is "18k gold tone" and every "silver" is "silver tone". Each prompt has the
standard reference sentence word for word, 9:16, full bleed, the lock with its must-stay clause, a scale built in mm with a
referent that touches the piece and a contact shadow, two lights (one soft, one small and hard), calm areas, the no-text phrase,
the no-face clause and one product.

## Card-level choices that apply to both

- **Base text.** Each take A starts from the last prompt the model was sent: the k02a redo prompt in
  `batches/k02a/jobs_redo.json`. That prompt is the card's planned prompt with the k02a fixes already written in. Each edit below
  is applied on top of it.
- **References: two, from the product card (kept against verifier fix k02-1 (1)).** The k02-1 verifier asked for ref 02 to be
  dropped. Ref 02 is the frontal worn photo with lips and nose in it. This step's rule is that the media are the product card's
  two `mediaIds`, so both were sent: `6eb60a80…` (01) first, then `821ee837…` (02). Ref 02 is held in check by the prompt, which
  says to use it "only for how big the star is against the lobe" and to "take nothing else from it: not the person, not her
  face, lips, nose or jaw, not the front view…". It is also the only true-scale worn view, and scale is the fault still open
  after the redo. The no-face fault was fixed by the camera geometry, which is kept. For k02-4 both card ids (01, 04) were sent,
  as in k02a.
- **Lock wording (two product-card words changed).**
  - The Quatrefoil lock's "four-leaf clover" is written as "four-leaf shape". The card's own `morph` note says to leave
    "clover" out of image prompts.
  - The Huggies lock's "chunky huggie hoops" is written as "chunky hoops", because "huggie" is a banned word.
  - Everything else in both locks is pasted as is, including the must-stay clause.

## k02-1A: Quatrefoil Éclat Studs, THE STAR FILTER. (REC)

Director's note (`brief_diff.md`):

1. **No face (diff 1).** The camera is behind the ear and the head is turned fully away. Added word for word: "no eyelash, eyelid,
   brow, cheek, nose or lip breaks the outline of the head anywhere in the frame". Also added: "the right edge of the frame cuts
   across the jaw about 3 cm in front of the ear, so the outline of the cheek and face never enters the frame". The mirrored
   geometry that passed the face gate is kept: the right ear, with the camera about 35 degrees right of straight behind.
2. **Clean wedding photograph (diff 1).** The closing clause now reads: "The picture stays a clean, modern, pin-sharp wedding
   photograph: the VHS effects are added later as overlays…". The round-bokeh, no-starburst and no-glint clauses stay word for
   word.
3. **Full bleed and tone (diff 3).** Added "a full-bleed photograph edge to edge with no borders, bands or panels", and "Every
   prong, frame, bezel, plate and the outline are the same 18k gold tone".

Verifier's next fix (`k02a/verify/k02-1.md`, end of the Redo section), clause by clause:

1. **Height.** Added word for word: "the top of the ear is 22 percent of the way down the frame and the earlobe ends at 48
   percent", and the bun is "high on the back of the crown… in the top half of the frame… below the earlobe there is only the
   bare nape, neck and blouse". Kept: the stud's centre "44 percent of the way down".
2. **Scale.**
   - Added word for word: "no taller than the earlobe itself", "its top tip just below the bottom of the ear bowl (the
     concha)", "its lower tip stops at the lobe's lower edge, which stays visible as a curve of skin below it", and "about a
     quarter of the ear's height".
   - **One number corrected.** The fix said "an eleventh of the frame width". With the ear running 22 to 48 percent of the
     height, that does not fit a 58 mm ear: the ear would need a frame about 12.5 cm wide, and the 15 mm star is one eighth to
     one ninth of that.
   - The eleventh was an over-ask to offset nano_banana_2, which drew the star 1.35x too big. In the bake-off gpt_image_2_6
     drew true scale, so the prompt now gives the true, consistent numbers: an ear of about 58 mm, a frame "about 13 cm wide at
     the ear", and the star "about one ninth of the frame width".
   - Contact shadow: "a true soft contact shadow… all around the star's edge".
3. **Pavé.** Added "ONE row of about 11 round stones along each concave side, each stone as wide as the 18k gold tone border is
   thick, with tiny 18k gold tone prongs between them: never a band of micro pave 2 stones wide". The fix wrote "gold border" and
   "gold prongs", which the lint changed to "18k gold tone".
4. **Pears.** Added "large clean facets, like the pears in reference 1, … not a crushed-ice speckle".
5. **Colour.** Added "one large soft key from the left, cool daylight at about 5000 K, lights the ear and the stud", "The only
   tungsten is in the background bokeh", and "must match the pale warm yellow 18k gold tone of reference 1, never copper, rose or
   orange". The fix's "(as in a yellow-gold packshot)" was dropped because it contains a bare "gold".
6. **Kept word for word:** the redo's construction clauses (single-stone pears, 8 windows, the round bezel on the 4-pointed
   plate), "No face, no eyes, no eyebrows", "Only this one earring; no other jewellery", and the must-stay clause, which is
   repeated last.
7. **WORLD.** The bokeh is now placed "beyond the back of the head in the upper left and down the left edge". That is where the
   layout puts the HTML filter stars, so the device has discs to land on.

**Note for the designer:** the plan's `cardLine` and `primaryText` say "pre-order". Today's live rule is that every piece is in
stock at the card's price (₹1,099), so the copy needs that word changed. The trust line "FREE INSURED SHIPPING · CASH ON DELIVERY"
goes on the card under the owner ruling.

## k02-4A: Brushed Gold Huggies, THE SOFT FOCUS. (REW)

Director's note (`brief_diff.md`):

1. **True scale (diff 2), with its numbers corrected.**
   - The note says "each huggie is about as tall as the cassette is thick, so about seven huggies would fit across the
     cassette's label". Both numbers contradict the product card: 14 mm is 0.56 of the 25 mm thickness, and 187 / 9.8 is about
     19. "As tall as the cassette is thick" is the exact 1.5-1.9x fault that both k02a takes showed.
   - The prompt keeps the note's method and uses the true numbers. It says how many pieces fit across the prop: "About nineteen
     of these earrings standing side by side would fit along the cassette's length, and about nine side by side would span the
     width of the frame".
   - It states the earring's height against the edge: "each earring reaches only a little above halfway up it".
   - It gives the field of view in cm, as the note asks: "The frame is about 9 cm wide and 16 cm tall at the pair, so each
     earring's height is about 9 percent of the frame's height" (the verifier's frame-fraction form).
2. **Full bleed and tone (diff 3).** Added "a full-bleed photograph edge to edge with no borders, bands or panels" and "both
   pieces the same 18k gold tone all over".

Verifier's next attempt (`k02a/verify/k02-4.md`, "Recommendation to the orchestrator"), clause by clause:

1. **Placement (scale).** The pair now stands "on the silk directly in front of the label edge… each piece touching the label
   edge behind it". The fix's reason: the 25 mm edge stands right beside the pieces, so the model cannot hide the comparison in a
   foreshortened top face. The cassette is still the referent and it touches the piece. The camp's idea of a tape on silk, lit
   like 1996, is unchanged. The low 15 degree camera is kept. Both cassette ends are outside the frame.
2. **Hard 1996 light.**
   - The on-camera hard light now throws "a crisp, hard-edged dark shadow of each earring onto the cream label behind it".
   - In k02a the shadow fell on black plastic and could not be seen, so the "hard light, still soft sheen" proof was only half
     shown. Now it lands on cream.
   - Two lights: a large soft warm fill from the upper left, and the small hard light beside the lens.
3. **Copper band.** Added "The silk in front of the pair, toward the camera, falls into deep, almost black shadow, so nothing warm
   or red faces the pair: the brushed metal reflects only the dark room, the black plastic and the cream label… no pink, red or
   copper reflection band and no clipped white patch".
4. **Rim.** The top face is now "a narrow, foreshortened band… its far half and back rim melt into deep blur". The plain-plastic
   clause (no embossed letters, numbers, dots, arrows or symbols) is kept word for word.
5. **Composition.**
   - The tops of the earrings are at 40 percent and their bottoms at 49 percent, "never lower than 50 percent". That keeps the
     Story band at y 1010 clear.
   - The label edge runs from 33 to 49 percent. The top 33 percent is the blurred top of the cassette and dark silk, for the
     title. From 52 percent down is shadowed silk, for the lower third.
   - The pair stands slightly right of centre (its middle about 56 percent across). That leaves a long stretch of blank label on
     its left for the handwritten "Shaadi · Haldi to Reception · Dec 96".
6. **Kept word for word:** the reference sentences with "leave out the cardamom pod", the piece description, "Do not redesign,
   restyle or resize it", the palette (cream added), "clean, modern and pin-sharp… effects are added later", the no-text,
   blank-label and plain-plastic clauses, "No people, no face, no eyes, no eyebrows, no hands, no other jewellery, no water", and
   the satin must-stay clause, which is repeated last.

**Note for the designer:** the label strip is now behind the pair, not below it. Write the handwritten contents on the free
stretch of label to the left of the pair, matched to its perspective and never touching a piece or its shadow. The spec sticker
stays an HTML sticker. Under the owner ruling, the trust line "FREE INSURED SHIPPING · CASH ON DELIVERY" goes on the card.
