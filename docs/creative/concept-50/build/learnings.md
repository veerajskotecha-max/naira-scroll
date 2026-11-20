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
