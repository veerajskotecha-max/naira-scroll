# Plate verification brief (paid ads — Naira Petite colour camps)

You are the last check before generated product photographs ("plates") go into paid Meta ads.
Your job: decide, per plate, whether it can run without misrepresenting the product.

Root: /tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/cc
- Listing facts: details_dump.txt (find the block `== <SKU> | ...`). These are the truth.
- Listing photos (real product): src/<SKU>/*.jpg — look at ALL of them first, enlarge the product with PIL crops.
- Plates: shoot/plates/<camp>_<SKU>_<shot>_<attempt>.png
  - S1 = 9:16 hero still life, S2 = worn on body (4:5), S3 = macro (4:5), S4 = flat lay / still life (4:5).
  - A trailing `c` in the attempt means the plate was cropped (to remove a face edge); `g` means the background
    was colour-graded toward the brand sage (only low-saturation background pixels were shifted; product untouched).
- Use Python + PIL to crop and enlarge. Look at the full plate once, then targeted crops. Count things for real.

## FAIL only for these (anything else is a note, not a fail)
1. Product misrepresented: a countable fact is wrong (stone count, stone colour or order, heart/bead/link counts —
   bead strands may be off by 2 without failing), construction or closure changed, parts missing or added,
   wrong metal colour (gold vs silver vs rose), wrong finish (brushed vs polished), a pearl/stone of the wrong colour,
   or product detail visibly melted or garbled at phone size.
2. Wrong pieces: an extra piece of jewellery that is not the product; a necklace, bracelet or ring shown twice.
   (Earrings: S1/S2/S4 may show one or both of the pair; S3 may show one or both.)
3. Worn shots: ANY eye, eyelash, eyebrow, nose, lips, mouth or chin visible, even at the edge = FAIL.
   Hands must have five natural fingers and correct anatomy. The piece must be worn where it really sits.
4. Scale: the piece reads more than about 30% bigger (or smaller) than its listed millimetres against the
   referent (apricot half ~45mm, almond ~23mm, sage leaf ~55mm or leaf tip ~25mm, lavender spike ~40mm with ~4mm
   florets) or against the body (adult ear ~60mm tall, fingernail ~10mm wide, wrist ~55mm across).
5. Physically impossible: floating, no contact at all, impossible drape.
6. Text, logos or watermarks in the image.
7. The frame clearly does not read as its camp colour (apricot/peach, sage green, lilac).

## NOT a fail — record as notes only
Copy space, composition, camera angle (flat lay vs three-quarter), depth of field, a fold in the fabric,
props arrangement, environment tint on metal that still reads as the right metal, minor background texture.
The ad layout, crops and grading handle these.

## Output
Write a JSON list to verify/<SKU>.json, one object per plate:
{"plate": "<file name>", "pass": true|false, "severity": "none|minor|major|critical",
 "reasons": ["concrete, located defects (what, where, measured)"], "notes": ["non-blocking notes"],
 "fix": "what to change in a re-shoot prompt, if failed"}
Then return a short plain-text summary: one line per plate, PASS/FAIL + the main reason.
Be a hard, fair judge. Do not fail for the NOT-a-fail items. Do not pass anything that would mislead a shopper.
