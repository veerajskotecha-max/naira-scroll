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
