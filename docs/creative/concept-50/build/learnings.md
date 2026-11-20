# Crazy 100: learnings carried from batch to batch

Every shooter, designer and loop writer reads this file. Loop writers append a dated section per batch (at most 6 lessons).

## Wave 1 (k01a, k02a, k03a, k04a), read at verification, 20 Nov 2026

1. **Model.** `nano_banana_pro` requests were served by `nano_banana_2`, which lost locks the listing photos show: the Woven
   hoop's single flat disc (dropped or doubled), its open many-wire plait (a flat three-strand ribbon), the Toggle's sailor ring
   (a generic marine clasp), the Halo Curve stars. The bake-off (`batches/bakeoff/README.md`) moved take A to `gpt_image_2_6`
   (high, 2k) and take B or the redo to `seedream_v5_pro` (2k). Picture sizes now vary (1520x2688, 1536x2720): read W and H and
   use the general crop rule.
2. **Scale drifts large, 1.35-2x.** It happened on worn hoops (0.59 of the ear's height against about 0.43 true), a necklace at
   the nape, a ring in a gripping hand and huggies beside a VHS cassette. Every prompt now gives the size against a named body
   part ("the hoop's outer width is a little less than half the ear's height"; "the ring about as wide as the finger"; "the
   sailor ring about 22 mm, a little wider than a fingertip") and a field of view in cm. Never set a 25 mm piece against a big
   prop without saying how many pieces fit across that prop.
3. **Faces creep in.** A three-quarter head turn shows lashes and a brow past the cheek; glasses held near the head carry an
   eyelid in the lens. Write "head turned fully away; no eyelash, brow, cheek, nose or lip breaks the outline of the head", and
   keep the camera behind the ear, never level with the eye.
4. **Props that must sit over the piece** (the aunty's lens over a ring or clasp) land 2-18 mm off. Do not ask the model to
   place a lens over a small piece. Shoot the hand holding the glasses near the piece, and build the magnified view in the HTML
   as a loupe: a circular 2x crop of the same picture, drawn inside a lens frame, with the size line stating the magnification.
   This is the owner's allowed in-place technique and it can never mis-register.
5. **Letterbox padding.** One take came back as a square photograph padded with flat colour bands to 9:16. Write "full-bleed
   9:16 photograph edge to edge; no borders, bands or panels".
6. **Two-tone mistakes.** On a gold-tone piece a jump ring or the last link came out silver tone. Name the metal tone of every
   part: "every link, ring and jump ring in the same 18k gold tone".
7. **Rate limits.** With four batches and a test running, Higgsfield refused submissions with 429s; one redo gave up and was
   never shot. Retry 429s patiently (30-60 s apart, up to 10 times). A refused submission costs nothing.

## Director's notes from wave 2 verification (20 Nov 2026, evening)

8. **Toggle Link Chain clasp (9 ads).** Both models keep redesigning the sailor ring into a marine clasp with two nubs on two
   ribbed collars and grow the bar to 0.87x the ring. Write it as: "ONE thick round sailor ring with ONE ribbed spring-gate
   collar and ONE small push-pin nub at about 2 o'clock; never two collars or two nubs; ONE short straight bar, about 0.6 of the
   ring's outer diameter, set with one row of about 9 tiny clear stones, hanging from one jump ring". Prefer a frame where the
   clasp is seen flat-on, as in reference 2.
9. **Counts drift by one.** A stud grew a seventh pearl; check every count in the lock and write the count in digits and in
   words ("six pearls, 6, never seven").
10. **Scale under the new models** is better but still drifts on necklaces at the neck (1.3-1.8x) and small bows on wrists
    (1.4x): give two body referents, not one, and the field of view in cm.
11. **Toggle scale reference.** Every Toggle Link Chain take now carries a third reference, the listing's studio worn photo
    (`products/toggle-link-chain.json` "scaleRef", media id 94bfe9cf-8809-4bc6-959d-4b31d8f80139): "Reference 3 shows this
    exact necklace worn on a woman at true size: match its scale against the neck and collarbone exactly". The same move (a
    worn listing photo as reference 3) is worth using for any piece that keeps drifting large, when the listing has one.
12. **Woven scale reference.** Woven Gold Hoops also carry a third reference: the listing's worn photo 05 cropped to the ear and
    hoop (no face), `refs/woven-gold-hoops/05_ear_crop.jpg`, media id ea0201cf-5eb2-4d42-a9b3-7b6bd230a42c (card "scaleRef").
13. **Ribbon Bead Bracelet scale reference:** listing worn photo 02 cropped to the wrist (no face),
    `refs/ribbon-bead-bracelet/02_wrist_crop.jpg`, media id 6bdbd714-033f-46f3-ac6d-c9b417fefbb8 (card "scaleRef").
14. **Brushed Gold Huggies scale reference:** listing photo 04 (the pair beside a cardamom pod, 14 x 9.8 mm each),
    media id 5601af98-29ec-4a35-bb32-a1cf1c4f1e0c (card "scaleRef"). A listing photo with a known-size prop (cardamom, coin,
    size guide) is the best third reference: it carries scale without a face.
15. **Toggle takes use high quality.** At gpt_image_2_6 medium the Toggle clasp failed in k07-1, k08-1, k10-2 (and k04-2 at
    any quality, scale): two collars, two nubs, a long bar, 1.5x scale. The bake-off take at quality **high** matched the clasp
    reference exactly. Every Toggle Link Chain take A is therefore `gpt_image_2_6` quality **high** 2k (2.75 credits) with all
    three references (packshot, clasp close-up, worn scale photo), the clasp seen flat-on and large enough to read, and the
    exact clasp sentence from lesson 8. The redo stays seedream_v5_pro with the same three references.
16. **Credits (20 Nov, 20:05 UTC: 110 left).** From the b-batches on: no hedge takes (the scale references replace them),
    redos on `gpt_image_2_6` medium (1 credit) unless the product card's "shootModel" says otherwise. Spend credits on
    the 50 b-batch ads and the held rescues first; Kling clips only with what is left at the end.

## First rating (k03a, k03-4 Tubogas Dome Ring, 20 Nov 20:10 UTC): expert 6.91, customer 6.71, basket 0, gate failed

17. **The piece must be the hero even at true size.** Every rater's worst issue: the ring was about 8% of the frame width
    (about 16 px at 200 px), so the best pain line sold a piece nobody could see. When the piece is under about 15% of the
    Feed width, every variation carries a large magnified inset of the SAME picture (a pixel-exact 2-3x crop of the piece, at
    least 30% of the Feed width, in a clean circle, lens or die-cut frame tied to the camp's device), labelled "shown
    magnified · about N mm", while the true-size piece stays in the scene as the scale proof. The inset is the thumb-stopper;
    the headline names what the inset proves.
18. **Check the inset against the references before using it.** At x1.5 the inset exposed ridges at about twice the real pitch,
    and the truth critic held the ad at 7.2. Crop the inset, set it beside the same crop of reference 1, and use a
    magnification at which the construction reads true; if the picture's detail is wrong at any magnification, the ad cannot
    rely on a close-up, so say so in the notes.
19. **Hook to picture.** "NOT OUT." with the "RING NOT OUT / MILK OUT" tags was the strongest hook, but it lost because the
    picture could not carry it at 200 px. Keep the type system to one device plus the footer; the kicker line, a two-line
    headline, one subline, one device, the card.

## Second rating (k01a, k01-4 Baroque Shell Bracelet: expert 6.73, customer 6.38, gate failed)

20. **At most 6 text elements per Feed.** About 14 elements (two kicker lines, headline, eye-chart numbers, stamp, quote,
    FIG. callout with its own quote, lens callout, an outline strip with two labels, a five-line card) capped "message" at 6
    with every critic. The six: (1) one kicker line, (2) the two-line headline, (3) one subline, (4) ONE device with at most
    one label, (5) the card (name, price, offer box), (6) the footer trust line. Everything else goes, however clever.
21. **The payoff line sits under the headline,** never at the bottom: "EK BHI MATCH NAHI KARTA." reads as a complaint until
    "Isiliye toh liya." answers it, so the answer must be read second, not last.
22. **The prop must prove the headline.** "BHAARI HAI. ACHHA HAI." (weight) over a sight-test picture lost on fit; a weight
    hook needs a weighing picture (the piece pooled in an open palm or on a balance). Pick the hook the picture proves.
23. **Show the whole piece.** A bracelet whose 8 mismatched pearls are the selling point must show all 8; a lens or frame may
    magnify one or two, never hide the rest.

## k03a loop (20 Nov 2026, 20:30 UTC): 0 of 5 shipped; 1 of 10 pictures passed; expert 6.91, crazy 6.5, customer 6.71, basket 0.0

24. **Set scale by the crop, not by numbers.** The model draws the piece at a fixed legible size (about 1/12 of the frame)
    and builds the hand around it. In k03a, field-of-view cm, percent-of-frame and thumb-ratio clauses did not move it:
    four hand plates came out 2-3x (k03-1A, k03-1R, k03-5A, k03-5R), and four were framed 23-34 cm against the 11-12 cm
    asked (k03-1A, k03-1R, k03-3A, k03-4A). k04r saw the same habit on gpt_image_2_6. Choose a crop whose anatomy makes that size true:
    - for a 10-18 mm piece, the fingertips fill the frame width;
    - for 14 mm earrings, the palm spans three quarters of a 12 cm frame.
    Never write "hand large in the frame" or "piece large and clearly legible": both were obeyed by growing the piece
    (k03-5R about 3x; k03-3R split the ring). Keep a big prop's size, such as "paraat about 45 cm", out of macro prompts.
25. **Copy reference 1's own pose and camera angle for any complex setting.** Poses the reference does not show broke
    construction:
    - a pinch or a dangle produced the named column morph (k03-5A);
    - putting one end on each finger split a two-ended ring (k03-3R);
    - a straight-down view turned the Woven hoop's disc edge-on, twice.
    The reference's own pose held the hardest locks (k03-5R's 3 + 1 sweep, k03-1B's S-wave). Set the pose first, then
    set the scale with the crop.
26. **Name what fills every calm zone; never describe it as "quarters" or "the central 4:5 window".** On k03-3A, "the top
    quarter is calm oxblood, the bottom quarter calm" was drawn as flat colour panels: a 1:1 photograph letterboxed to
    9:16. "Velvet folds to the top edge, milk to the bottom edge" fixed it on the redo (k03-3R). Strip "the subject
    centred inside the central 4:5 window" from every bible prompt before shooting.
27. **Liquid never sits on the piece.** A milk drip hanging from a stone read as an added pearl (k03-5A), and a bead on
    metal reads as hardware. Show liquid running off the metal clear of every stone, or detached in the air on a breaking
    thread, and gate it at verification.
28. **Lint the bible and brief the raters before a batch.** The k03 bible, though truth-checked, carried:
    - a price sum (card 8's bill);
    - composite hedges and composite Kling lines;
    - an unlisted prop size printed as fact ("PARAAT ABOUT 45 CM");
    - BUY3 after character 125 in four texts;
    - the trust line switched off.
    Every critic then failed compliance on the owner-required "FREE INSURED SHIPPING". Before each batch, lint every device
    and line for sums, composites, prop numbers and the BUY3 position, and paste the owner rulings (RULINGS §6) into every
    critic's prompt.
29. **A basket of three needs three ads in front of the panel.** With one ad rated, the basket rate is 0 by construction
    (k03a: 5 of 6 baskets held the one ring, and Meera planned BUY3 gifts but had nothing else to add). Record the rate as
    "not measurable (n ads)" when fewer than three are rated, and spend the next credit on a third passing plate. From
    k03b, every offer box asks for the basket: "THIS + ANY TWO · BUY3 · 20% OFF" after three chalk circles.

## k01a loop (20 Nov 2026): 0 of 5 shipped; 1 of 9 pictures passed; expert 6.73, crazy 6.83, customer 6.38, basket 0.0

30. **Never ask the model to put a lens, loupe or glass in front of a small piece; draw it.** Asked to hold a reading lens
    over the piece, the model missed every time it tried:
    - 18 mm above the toggle (k01-4A);
    - about 550 Feed px above the ring, with a second ring painted inside the glass, which is two products (k01-2A);
    - over an eye instead of the stud (k01-3A);
    - glare that turned a gold-tone link silver (k01-5B).

    Shoot the prop held beside the piece, with a CLEAN SPACE clause and "no magnifier and no magnified view anywhere in
    the picture". Then draw the rim in SVG over the piece and fill it with exactly 2x of the same picture about its
    centre. k01r passed three cards this way.
31. **Size a drawn magnifier from the part it magnifies.** Two rules:
    - The inner glass must be at least 2.3 times the part's longest side at true size, or the 2x part cannot fit (k01-3R:
      a half-moon could not hold a 2x stud, and the rim would have cut both stars).
    - Never let the piece cross the rim half in and half out. Where the drop crossed the rim of k01-4's 2x lens, perf1
      read the T-bar as 2.5-3x the ring, and truth stayed at 7.17, although the verifier measured it true.

    Magnify one whole part with glass all round it, and keep the rest of the piece visible at true size outside.
32. **Describe a prop by its geometry, not its name.** "Half-moon reading glasses" came back round, rounded or cat-eye on
    7 of 9 nano plates. "Two flat-topped D-shaped lenses with the straight edge on top, thin dark tortoiseshell rims, a thin
    bridge" held on every k01r gpt plate. The same goes for any shape the model has a default for (frames, clasps, cuts).
33. **On neck crops, keep the ears and the chin outside the frame in words.** A neck crop "from just below the chin"
    still showed the chin's underside (k01-5A). The redo brought the chin back and added a gold drop earring at the top
    edge, which is a second product (k01r k01-5R). Write "the top edge cuts straight across the middle of her neck, well
    below the jaw, and her ears are outside the frame: no chin, jaw… or earring anywhere in frame". Use a listing's
    face-free scale crop as the worn reference, never a worn photo that shows lips or a chin.
34. **Count or trace only what the plate shows.** V1's line-up traced "all eight" pearls from a wrist plate that shows
    five. A count device (numerals, a line-up, swatches, a register) prints only what verify counted on that plate. If it
    shows more, it must name its source ("traced from listing photo 01"), or the line falls back to a version without the
    count.
35. **Give the buyer the last word, loud.** The k01-4 variation with the talk-back ("EK BHI MATCH NAHI KARTA." /
    "Isiliye toh liya.") had the higher would-buy (5.67 against 5.33) and buy-yes share (0.67 against 0.5), and customers
    quoted it as the reply they always wanted to give. It lost only because it was set as the smallest row under 14
    elements. Customers quote lines in their family's voice ("Bhaari hai, achha hai" in all six runs), and minimal buyers
    reject spec-sheet yardsticks ("weight isn't why I'd buy pearls"). Pair aunty's doubt with the buyer's one-line Hinglish
    answer, set larger than the line above it and directly under the headline, and keep facts in the labels.
