# Pieces in stock, 2 Nov 2026

## The ask

The owner sent 12 photos of pieces in hand and asked:
- which of them match the recent listings, and what is wrong with those listings;
- to list each piece at 5 units as a Shopify draft, with photos sized against the hand.

They named the Bow and Heart set (the earrings' stones and the heart pendant are different) and "2 or 3 pendants" whose design is a bit different. Later they added: "The bow one is a set … Bow set is complete set." So the set's necklace carries the same bow-and-heart motif as its earrings, as in the buy book. They chose 4 photos per piece.

## What the photos match

| Photo | Piece | Finding |
|---|---|---|
| 5 | A08 Bow and Heart Gift Set (earrings) | Each bow is two heart cut stones in pave rims, not a pave ribbon bow. Fixed. |
| 6 | N09 Petite Heart Trio Necklace (new) | A gold puffed heart beside three small stones: its own necklace, not the set's. |
| 4 | A12 Heart Solitaire Huggies | The stock has a plain hoop of about 15 mm and a bezel heart of about 6.5 mm. The 1 Nov photos showed a pave hoop and a claw heart. Fixed. |
| 9 | A16 Herringbone Teardrop Necklace | Two polished bars form a V at the front, with the pear hanging from its point. Fixed. |
| 1, 2, 3, 7, 8, 10, 11, 12 | N01 to N08 (new) | Laurel Marquise Necklace, Soleil Petal Pendant, Pearl Crescent Pendant, Molten Solitaire Pendant, Petite Pear Solitaire Necklace, Petite Fleur Y Necklace, Asscher Solitaire Pendant, Cushion Bezel Pendant. |

Sizes are measured against fingers, cards and chain links in the owner's photos (`refs/`, detail crops `*_det.jpg`). Chain lengths could not be measured from the photos, so the copy says "to confirm".

## Done (2 Nov)

One mutation (`build/ship_2nov.py` builds `shopify/ship_2nov.graphql` and `shopify/ship_2nov.json`). All three are DRAFT with 5 units, and every photo is READY.
- **A08 Bow and Heart Gift Set:** updated in place.
  - Packshot of the complete matching set, worn shot (pendant and earring), earring macro, size card.
  - The copy describes the set as it is.
- **A12 Heart Solitaire Huggies:** updated in place.
  - Packshot, worn shot and macro of the plain hoop with its bezel heart, plus the size card.
- **A16 Herringbone Teardrop Necklace:** created.
  - Packshot, two worn shots, macro, size card.

Other details:
- The new size cards for A08 and A12 are `-size-guide-v2.jpg`, because the 1 Nov cards hold the plain names in Shopify Files. Each description's size-guide link points at the new card.
- The updates left the products' metafields alone (feed categories and SEO tags).
- `shopify/pushed_2nov.json` has the ids.

## The nine new necklaces as drafts (2 Nov)

The owner said "Start doing all new too! Do for all skus" while the Higgsfield balance stood at 0.16 credits. So `build/ship_new.py` created all nine (N01 to N09) in one mutation:
- each as a DRAFT with copy, price, SKU, 5 units, feed metafields and its size card;
- N09 also carries its approved macro;
- autoPublish was on around the creates, and the Herringbone Teardrop Necklace was published too.

The ids are in `shopify/pushed_2nov.json`.

## Photos for all twelve (2 Nov, after the credit top-up)

Every piece now has its full gallery plus an in-palm size photo (shot P, the piece resting in an open palm), then its size card. `review/galleries_2nov.jpg` shows all twelve galleries in order.

| Piece | Gallery |
|---|---|
| N01 to N09, A16 | packshot, worn at the base of the neck, worn turned a quarter, macro, in the palm, size card |
| A12, A08 | packshot, worn, macro, in the palm, size card |

Generations: 32 in one batch, then 13 fixes and follow-ups, then 5 for the seven-petal Soleil, 50 in all, about 88 credits by the balance. Every frame was checked against the owner's photos. Changes from that check:
- **Soleil Petal Pendant (N02).** I first read the stock photo as five petals and shipped a five-petal set (`N02_Hv`). The owner then picked the seven-petal packshot `N02_Hf` (seven open loops fanned below the stone, nothing above it): "Other images are wrong for this product. Only this one seems okay". That is now the packshot. W1, W2, M and P were rebuilt with `N02_Hf` as the only reference (`wref: hero` in `skus.json`), and the spec and copy say seven petals. The first W2 came back with solid petals and was reshot. The five-petal frames are kept as `*_5p` in `jobs.json`. The Shopify draft got the new five photos and the seven-petal description and SEO text in a single-product productSet; the size card was kept by id.
- **Soleil Petal size (owner: "size check and make smaller").** From the owner's photo the pendant spans about 1.8 finger widths, about 27 to 30mm, with a stone of about 7 to 8mm. The rebuilt worn and palm shots drew it about 1.7 to 2 times that. Two worn shots were shrunk by edit (`N02_W1s`, `N02_W2s`) to about 31mm, measured against her lips and neck. The palm shot would not shrink by edit or reshoot, so it was rebuilt: a background-removed cut-out of the approved packshot's pendant (`comp/n02_pendant_cut.png`) pasted at 1.8 finger widths onto an empty-palm plate (`N02_Pclean`), then one blending edit that drew the chain and shadow and kept the size (`N02_Pc`). The packshot and macro were kept. The copy still says about 25mm; a ruler check of the real piece would settle 25 against 28.
- **Pearl Crescent Pendant (N03), owner: "pearl isn't crossed, the chain is normal".** In the stock photo the chain happens to lie looped round the pearl's left side in the pouch; the first photos read that loop as part of the pendant, a gold rim round the pearl. The packshot was edited to hang the pendant from its bail with the chain going straight up (`N03_He`), and W1, W2 and M were rebuilt from it only (`wref: hero`). The palm shot drew the pearl about 1.1 finger widths against the stock photo's 0.76, so it was rebuilt like Soleil's: a cut-out of the packshot pendant at true size on the empty-palm plate, then a blending edit (`N03_Pc`).
- **Asscher Solitaire Pendant (N07), owner: "reduce sizing".** The stock photo has no hand; against the pouch width the stone with its claws is about 9 to 11mm and the chain about 0.12 of its width. The old photos drew the stone about 13mm worn and 19mm in the palm, with a curb chain about three times too thick and an oversized bail. The packshot was edited to a fine curb chain and a slim bail (`N07_He`); W1, W2 and M were rebuilt from it with the stone tied to a fifth of her lip width (now about 10 to 11mm); the palm shot was rebuilt from a cut-out at 0.6 finger widths (`N07_Pc`). Both drafts got all five new photos in one productSet; the size cards were kept by id.
- **Petite Fleur Y Necklace (N06).** The packshot edit (single chain each side, five-stone flower with a gold centre) was approved, then W1, W2, M and P were shot.
- **In-palm shots.** The first Pear and Cushion palm shots had the hand raised upright, like a stop sign. `build.py` now asks for the palm turned up and nearly level, and both were reshot.
- **Herringbone Teardrop Necklace (A16).** Its worn-at-the-neck photo had dropped off the draft. It was put back from its export.

`build/ship_photos.py` did the Shopify side in one productSet mutation for all twelve:
- photos already on a product, and every size card, were passed by media id, so nothing was uploaded twice and the size-guide links keep their filenames;
- no status was sent;
- variants kept their ids, SKUs and stock.

Checked afterwards:
- all 58 media READY, in gallery order, each packshot set as the variant image;
- 5 units each, prices unchanged;
- the size-guide links answer 200;
- the Storefront API shows the new palm photos on the two active pieces.

Status at the update:
- **ACTIVE:** the Bow and Heart Gift Set (A08) and the Heart Solitaire Huggies (A12). The owner had set them Active; they show all six channels.
- **DRAFT:** the other ten, at 5 units each. Every DRAFT product in the store reads 0 channels, older ones included, so check channels when they are set Active.

By 3 Nov the owner had set ten of the twelve Active, each on all six channels. The Herringbone Teardrop Necklace (A16) and the Petite Fleur Y Necklace (N06) are still DRAFT.

## Slim Pave Huggies (A13), added 3 Nov

The owner sent one more photo, a pair of gold pave huggies on a STAINLESS STEEL card ("Add this sku too").

**The match.** It is A13 Slim Pave Huggies from the Albyluxe order. That piece was held back on the 31 Oct final page, so it had never been listed. The same card as A12 places it in the same order.

**What the 31 Oct listing had wrong:**
- **Size.** The pair is about 18 mm tall, not 13 mm. Against the card, the huggie is 1.22 times the A12 hoop (15 mm). The thumb and a USB cable in the photo give 19 to 22 mm.
- **Setting.** About ten round stones sit in fine claws down the front edge, not in a channel.
- None of the 31 Oct photos were used.

**Shape.** The owner's 31 Oct review note on this piece was "Square, it is an earring".
- In the stock photo each huggie hangs through the card at an angle, so the photo cannot settle its true depth.
- The generator would not draw a square outline:
  - first packshot `A13_H_clip`: about 3:1;
  - edit `A13_Hs`: 2:1;
  - fresh packshot `A13_Hq`: 2.5:1;
  - drawing-guided edit `A13_Hd`: 2.4:1.
- A fresh packshot guided by a flat outline drawing (`refs/A13_shape.jpg`) came out about 1.9:1 (`A13_Hg`). That matches the outline the huggies show in the owner's photo, and it was approved.
- The copy says about 18 × 10 mm, a rectangle with softly rounded corners. If the pair in hand is a true square, the photos and copy need redoing.

**Photos.** Gallery: packshot `A13_Hg`, worn `A13_W1qh`, worn close `A13_W2qs`, upright macro `A13_Mq`, in the palm `A13_P`, size card.
- W1, W2 and M were made from `A13_Hg` only (`wref: hero`).
- The first worn shots drew the huggie at about 26 mm and 21 mm against the ear (taken as about 58 mm). Shrink edits brought them to about 19 mm.
- The palm shot reads about 19 to 21 mm against the fingers and palm.
- The paperclip-shaped frames are kept in `jobs.json` under `_clip`.
- Higgsfield: 18 generations, about 39 credits; the balance went from 337.16 to 297.71.

**Shopify.** `build/ship_a13.py` built one mutation (`shopify/ship_a13.graphql`, `shopify/ship_a13.json`). It turned autoPublish on for the six channels, created the product, then turned it off again.
- **Product:** DRAFT, SKU `SPH`, ₹999 with ₹1,899 compare-at, 5 units, inventory policy DENY.
- **Copy:** "Material: Stainless steel, as on the supplier's card".
- **Listing data:** feed metafields, SEO, the Earrings category and tags, as for the A16 create.
- **Checked afterwards:**
  - all six media READY and in gallery order, with the packshot as the variant image;
  - the size-guide link answers 200;
  - each Shopify copy matches its export, with a mean difference of 0.2 to 0.44 out of 255.
- Ids are in `shopify/pushed_2nov.json` and `build/drafts_new.json`.

## Petite Pear Solitaire Necklace (N05) made smaller, 3 Nov

The owner sent a screenshot of the listing: "Reduce sizing check supplier pic".

**True size.** In the owner's photo the pear is about 75 × 90 px, against fingers of about 200 px and cable links of about 22 px. That makes it about 6 × 8 mm, about three chain links wide.

**What the 2 Nov listing had wrong:**
- the worn shots drew the pear about 10 × 14 mm, and the palm shot about 20 mm;
- the bail was a big ball;
- the copy said 7 × 10 mm.

**New photos**, all now about 6 to 7 mm × 8 to 8.5 mm:
- **Packshot `N05_He`:** an edit of the approved packshot. The pear and its claws come down to about two thirds, about three links wide, and the bail is a tiny bead about a quarter of the stone's width.
- **Worn `N05_W1e`, `N05_W2e` and macro `N05_Mf`:** rebuilt from `N05_He` only (`wref: hero`). Worn, the pear is tied to about a sixth of her lip width.
- **Palm `N05_Pf`:** a local composite. The AI blending edit (`N05_Pc`) enlarged the pasted pendant about 1.3 times, and a shrink edit (`N05_Pcs`) barely helped. So the oversized pendant in `N05_Pcs` was covered with palm texture cloned from just below it, tone-matched and feathered. A cut-out of the `N05_He` pendant (`comp/n05_pendant_cut.png`) was then pasted at true size, turned to follow the chain, with a soft shadow. No AI step came after.
- The 2 Nov frames are kept in `jobs.json` under `_big`.
- Higgsfield: 7 generations and 2 background removals, 16 credits; the balance went from 297.71 to 281.71.

**Copy and card.** The intro, the details and the SEO text say 6 x 8mm. The new size card `petite-pear-solitaire-necklace-size-guide-v2.jpg` reads "45 cm · pear 6 × 8 mm", and the description's size-guide link points at it.

**Shopify.** `build/ship_n05.py` built one productSet (`shopify/ship_n05.graphql`, `shopify/ship_n05.json`).
- The five photos and the card replace the old six files.
- The variant was passed by id with its image only. No status, price or stock was sent, so the piece stays ACTIVE at the owner's new price of ₹1,099 (compare-at ₹1,899) with 5 units.
- **Checked afterwards:**
  - all six media READY and in gallery order, with the packshot as the variant image;
  - the size-guide link answers 200;
  - each Shopify copy matches its export, with a mean difference of 0.3 to 2.3 out of 255. The 2.3 is the worn shot's silk and hair re-compressed; the file uploaded was the export byte for byte.
- The new media ids are in `build/drafts_new.json`.

## Pave Open Heart Studs (A15) and V-Bar Teardrop Necklace (A16), 3 Nov

The owner sent two photos: "These 2 products too the heart is gold and also for this chain the pattern of chain on our listing is wrong!"
- **Photo 1:** the open-heart studs on a "stainless steel" card. It was cropped from a fuller photo of the same pair, saved as `refs/A15_full.jpg`, which is the one measured.
- **Photo 2:** the 2 Nov photo of the V necklace, forwarded with the supplier's line "390x5 1,950".

### Pave Open Heart Studs (A15)

**What the 31 Oct listing had wrong.** It was made from the buy-book photo:
- silver tone, with one row of bigger stones;
- about 11 mm.

**What the stock pair is:**
- gold tone, a broad band with two rows of tiny stones between polished rims;
- each heart about 20 × 19 mm. Against the card the heart is about 250 px of a 600 px card. In the buy-book photo it is about 1.4 times the thickness of the thumb holding the box.

**Photos.** Gallery: packshot `A15_He`, worn `A15_W1`, worn close `A15_W2`, macro `A15_M`, in the palm `A15_Pf`, size card.
- The first packshot `A15_H` leaned both hearts outward, and the worn shots copied the tilt (the 31 Oct note on this piece was "On model heart shapes are wrong"). An edit stood them upright (`A15_He`), and the worn shots and macro were rebuilt from it.
- A worn shot that showed an eye, and one with a ghost second face, were reshot.
- **Palm:** generated palm shots drew the hearts about twice their size. So the palm shot is a local composite: a background-removed cut-out of the `A15_He` hearts (the posts through the open centres erased) pasted at 125 px each, about 20 mm against 100 px fingers, onto the empty-palm plate `N02_Pclean`, with a soft shadow.
- The size card is `pave-open-heart-studs-size-guide-v2.jpg` ("Each heart about 20 × 19 mm · band about 2.5 mm"). The 31 Oct card holds the plain name in Shopify Files.

### V-Bar Teardrop Necklace (A16, was Herringbone Teardrop Necklace)

**The chain.** In hand it is a dense curb chain of flat, faceted, interlocking links, not a smooth herringbone. The 2 Nov lock had said herringbone, "never a rope, curb or cable".

**Sizes.** Against the bars (about 170 px, taken as 15 mm, as on 2 Nov) and the fingertips:
- the chain is about 3.5 mm;
- the pear is about 10 × 13 mm (the 2 Nov copy said 3 mm and 8 × 11 mm).

The thumb in the photo would make the piece bigger, so these stay estimates until the piece is measured.

**Photos.** Gallery: packshot `A16_He2`, worn `A16_W1f2`, worn quarter turn `A16_W2q`, macro `A16_M`, in the palm `A16_Ps2`, size card.
- **Packshot.** Two edits of the 2 Nov packshot:
  - the first swapped the chain for a curb and set a larger pear straight at the V point;
  - the second packed the links tight like the real chain.
- **Worn.**
  - The generated worn shots drew the necklace about 1.8 times too big (the pear about 0.37 of the lip width against 0.2). Shrink edits brought the quarter view to a pear of about 11 mm; its bars were shortened by a further edit (`A16_W2s2`).
  - The front view `A16_W1f` was made from `A16_W2s2` so the size carried over, then its bars were shortened (`A16_W1f2`).
  - Because both of those faced the camera, a true quarter-turn view (`A16_W2q`), also made from `A16_W2s2`, replaced photo 3.
  - The bars still read about 19 to 21 mm in these frames against the 15 mm in the copy.
- **Palm.** Halved, then its bars shortened (`A16_Ps2`).
- The 2 Nov herringbone frames are kept in `jobs.json` under `_herringbone`; their exports and card were removed from `exports/` and `cards/`.
- The size card is `v-bar-teardrop-necklace-size-guide.jpg` ("45 cm · teardrop 10 × 13 mm").

### Higgsfield

27 generations and one background removal, 55 credits. The balance went from 281.71 to 226.71.

### Shopify

Two productSet mutations: `build/ship_a15a16.py`, then `build/ship_a16_w2.py` for the photo 3 swap. No status, price, compare-at or stock was sent, so both stay DRAFT at their prices with 5 units each.
- **A15:**
  - the five photos and the -v2 card;
  - gold copy and SEO ("Material: Stainless steel, as on the supplier's card");
  - the tag "Rhodium Silver Tone Plated" swapped for "18k Gold Tone Plated", with the tags sent in full.
- **A16:**
  - renamed V-Bar Teardrop Necklace, handle `v-bar-teardrop-necklace` (a draft that was never published); the SKU stays HTN;
  - curb-chain copy and SEO, the five photos and the new card;
  - the cost per item set to ₹390 from the supplier's line.
  - The second mutation passed the four unchanged photos and the card by media id and brought in only the new photo 3.
- **Checked afterwards:**
  - six media READY and in gallery order on each, with the packshot as the variant image;
  - both size-guide links answer 200;
  - each Shopify copy matches its export, with a mean difference of 0.27 to 1.59 out of 255.
- Ids are in `build/drafts_new.json` and `shopify/pushed_2nov.json`.
- `review/hearts_vbar_3nov.jpg` sets the owner's photos beside the new galleries.

## Clover Garland Necklace, Solitaire Charm Huggies, V-Bar chain and Slim Pave setting, 3 Nov

The owner sent three more notes:
- "Also list this, check inages we made in higgsfield if we can use thst or this .and do all corrections proper!", with a photo of a pair of gold huggies with a round stone charm in a clear bag (`refs/A14_full.jpg`).
- "This red necklace also. And the chain of other necklace on listing is weong, the second image", with two photos:
  - five sleeves of a red clover necklace beside the Laurel Marquise Necklace (`refs/C2_full.jpg` is the front sleeve);
  - the V-Bar photo with the supplier's line "390x5 1,950".
- "Check diamond setting and change it", on a screenshot of the Slim Pave Huggies review sheet.

### Clover Garland Necklace (C2), new

**The match.** The same clover as the Clover Garland Bracelet (sky blue, pink and white), in red and at necklace length, on a STAINLESS STEEL card. It is not among the Albyluxe pieces (`albyluxe-31oct/` has no clover), so it carries no Albyluxe tag.

**Sizes.** In the owner's photo a clover is about 78 px and a stone about 27 px, the same ratio as the bracelet, whose clover was measured at about 10 mm. That gives about 7.8 px per mm.
- Each half of the folded necklace runs about 1,800 px, about 23 cm, so the necklace is about 42 to 46 cm with the clasp, about 34 clovers.
- The copy says "Approximately 42cm (to confirm)": measure it with a tape.

**Photos.** Gallery: packshot `C2_H_b`, worn `C2_W1_a`, worn quarter turn `C2_W2q_a`, macro `C2_Me_a`, in the palm `C2_Pu`, size card.
- The first quarter turn (`C2_W2_a`) came back facing the camera, so `C2_W2q_a` was made as a new photograph from `C2_W1_a`, which keeps its size.
- The macro `C2_M_a` drew oval stones; the edit `C2_Me_a` made them round.
- **Palm.** The generated palm shot `C2_P_a` drew the clovers about 1.6 times too big, and a shrink edit (`C2_Ps_a`) did not help. So the palm shot is a composite:
  - a run of clovers cut from the packshot (`comp/c2_run_cut.png`) was laid across the empty-palm plate `N02_Pclean` at 10 mm a clover (`comp.py run_palm`) and uploaded as `C2_Pcomp_ref`;
  - a blending edit followed. Variant `C2_Pb_a` changed the design and was rejected. In `C2_Pb_b` the loop hanging off the hand showed gold backs, and a front-fix edit (`C2_Pf_a`) did not cure it;
  - `comp.py unloop` keeps `C2_Pf_a` only inside the hand mask (`comp/n02_hand_mask.png`) and the plate everywhere else, so the hanging loop is gone. A first version that used a threshold left ghost outlines.
- The size card is `clover-garland-necklace-size-guide.jpg` ("42 cm · clover 10 mm").

### Solitaire Charm Huggies (A14), new

**The match.** A14, held back on 31 Oct as Solitaire Bar Huggies (buy-book photo, AL-449). The pair in hand is a slim plain round huggie with a charm threaded on it: a small square gold tone tube, and below it a round clear stone in four claws.

**The older images were not used:**
- the 31 Oct A14 frames were drawn from the buy-book photo: an 8 mm cuff with the stone on a jump ring;
- the live Solitaire Drop Huggies (ADT27) is a different piece.

**Sizes.** In the owner's photo the closed hoop is about 150 px and the stone about half of it.
- The hoop is taken as about 13 mm, the size AL-449 was booked at. That makes the stone about 6 mm and the earring about 22 mm long.
- Nothing in the bag gives a second scale, so these are estimates.
- There is no supplier card in the photo, so no material is claimed.

**Photos.** Gallery: packshot `A14_H_a`, worn `A14_W1c`, worn close `A14_W2c`, macro `A14_M_a`, in the palm `A14_Pcomp`, size card.
- **Worn.** The generated worn shots (`A14_W1_a`, `A14_W2_a`) drew the earring too big, and the shrink edits (`A14_W1s_a`, `A14_W2s_a`) dropped the square tube. So both worn shots are composites (`comp.py worn`):
  - an edit took the earring off the lobe (`A14_W1bare_a`, `A14_W2bare_a`);
  - the earring was cut from the worn shot using the difference between the two frames, kept to gold and stone colours, with its holes filled (`comp/A14_W1c_mask.png`, `comp/A14_W2c_mask.png`);
  - it was then scaled about the piercing to its true size and laid on the bare lobe;
  - the first W2 mask lost the back half of the hoop. A lower threshold for shadowed gold and a split at the lobe brought it back.
- **Palm.** `A14_P_a` stood the pair upright and drew it about 1.3 times too big. The palm shot is a cut-out of the packshot pair (`comp/a14_pair_cut.png`) on the empty-palm plate `N02_Pclean` at 6.25 px per mm, with a soft contact shadow (`comp.py palm`).
- The size card is `solitaire-charm-huggies-size-guide.jpg` ("Hoop about 13 mm · stone about 6 mm · about 22 mm long").

### V-Bar Teardrop Necklace (A16), chain redrawn again

**The note.** "The other necklace … the second image" is the V-Bar in the owner's second photo. It could also have meant the Laurel Marquise beside the red necklace in the first photo. Its listing was checked against that photo: the three-stone marquise links match, so it was left as it is.

**The chain.** The curb chain drawn earlier on 3 Nov (`CHAIN6`) came out as an open chain of round wire links, like a Cuban chain (`A16_Hc_a`, `A16_Hc_b`, `A16_W1c_a`, `A16_W1c_b`).
- At 6x (`refs/A16_chain6x.jpg`) the stock chain is a dense wheat (spiga) chain. Its tiny rice-grain links each have a bright flat cut face and lean in a chevron, with no holes.
- The word "curb" kept pulling the generator to open links. The new wording (`CHAIN7`) names a wheat chain and rules out open links, curb and Cuban chains.

**Photos.** All five were redrawn with `CHAIN7`, using the 6x crop as IMAGE 2, from the approved frames: packshot `A16_Hw_a` (from `A16_He2`), worn `A16_W1w_a` (from `A16_W1f2`), worn quarter turn `A16_W2w_a` (from `A16_W2q`), macro `A16_Mw_a` (from `A16_M`), in the palm `A16_Pw_a` (from `A16_Ps2`).
- The size card is unchanged and was kept by its media id.
- The curb frames stay in `jobs.json`.

**Copy.** The intro, the details and the SEO text now say "a dense gold tone wheat chain about 3.5mm wide, its small bright cut links set in a tight chevron". The spec in `build/skus.json` now names a wheat chain too.

**Status.** The owner set the piece Active at 06:39 on 3 Nov, on all six channels, at ₹1,399 (compare-at ₹2,499). The mutation sent no status, price or stock, so these stay as the owner set them. `build/listings.json` now records ₹1,399.

### Slim Pave Huggies (A13), stone setting redrawn

**The note.** "Check diamond setting and change it", on the review sheet.

**What changed.**
- The earlier gallery drew one small row of stones sunk in a framed channel between polished rails.
- In a close crop of the owner's photo (`refs/A13_set.jpg`), the stones stand in raised claws, almost touching, and a second row of tiny stones runs along the outer edge of the band.

**Photos.** All five were edited (`SET13` in `build/edits.py`, with the crop as IMAGE 2) from the approved gallery: packshot `A13_Hs_a`, worn `A13_W1s_a`, worn close `A13_W2s_a`, macro `A13_Ms_a`, in the palm `A13_Ps_a`. The shape, size and hinge are unchanged.
- **Known gap.** The edits put the second row on the inner edge, towards the opening, not the outer edge. The copy describes the pair in hand. The photos can be flipped with five more edits, about 10 credits.
- The size card was redrawn from the new packshot as `slim-pave-huggies-size-guide-v2.jpg`, because the old card held the plain name in Shopify Files.

**Copy.** The intro and details now read "a row of round clear cubic zirconia in raised claws and a row of tiny stones down the outer side". The spec in `build/skus.json` describes the setting too.

### Higgsfield

37 generations and 2 background removals, 76 credits. The balance went from 226.71 to 150.71.
- **Clover, Solitaire Charm and the V-Bar chain:** 32 generations (12, 10 and 10) and 2 background removals, 66 credits against the 55 to 60 estimated.
- **Slim Pave setting:** 5 edits, 10 credits.

### Shopify

One mutation, `CloverCharmVBar` (`build/ship_3nov.py`, `shopify/ship_3nov.graphql`, `shopify/ship_3nov.json`). It turned autoPublish on for the six channels, made the two creates and the two updates, then turned autoPublish off.
- **Clover Garland Necklace:**
  - DRAFT, SKU `CLGN-RD`, ₹2,199 with ₹3,499 compare-at, 5 units, inventory policy DENY;
  - Necklaces category, feed metafields, SEO and tags;
  - "Material: Stainless steel, as on the supplier's card".
- **Solitaire Charm Huggies:**
  - DRAFT, SKU `SCH`, ₹1,199 with ₹2,199 compare-at, 5 units, inventory policy DENY;
  - Earrings category, feed metafields, SEO and tags;
  - no material line.
- **V-Bar Teardrop Necklace:** the five new photos, the card kept by media id, and the wheat copy and SEO.
- **Slim Pave Huggies:** the five new photos, the -v2 card, and the setting copy and SEO. It stays DRAFT at ₹999.
- **Checked afterwards:**
  - all 24 media READY and in gallery order, with the packshot as the variant image on each;
  - the four size-guide links answer 200;
  - each Shopify copy matches its export, with a mean difference of 0.74 to 2.29 out of 255 for the photos and 0.27 to 0.73 for the cards;
  - on the V-Bar and the Slim Pave, in the pixels where the new photos differ from the old, the live photos sit 3 to 7 from the new ones and 67 to 99 from the old;
  - autoPublish is off again on all six. Both new drafts are attached to all six channels and will show once they are set Active.
- Ids are in `build/drafts_new.json` and `shopify/pushed_2nov.json`.
- `review/clover_charm_vbar_slim_3nov.jpg` sets the owner's photos beside the four galleries.

## Pave Open Heart Studs (A15) and Solitaire Charm Huggies (A14) checked again, 3 Nov afternoon

**The note.** "Create the two earrings, the heart and the solitaire drop one. It already has check if it is correct in detail and do the listings with six images and sizes. These listings need to check colours, diamond placement and everything the heart one. The colour was different so we had rejected. Please make the new colour one and check sizing properly as well always." It came with the owner's photos of both pairs and two necklace screenshots. The screenshots had no instruction, so nothing was done with them.

Each listing has six images: five photos and the size card.

### Pave Open Heart Studs (A15)

- **Checked against `refs/A15_full.jpg` and `refs/A15_det.jpg`.** These matched the owner's photo and were kept:
  - the gold tone (the colour fixed this morning);
  - the two rows of tiny stones round the broad outline;
  - the shape and the posts.
- **Sizing.** Against the ear, both worn hearts read about 22 mm, not 20.
  - The earring was edited out of each worn photo to make a bare-lobe plate (`BARE15`: `A15_W1bare_a`, `A15_W2bare_a`).
  - Each heart was pasted back at 0.92 about the piercing, so it is about 20 mm (`comp.py stud`).
- **Kept.** The packshot, the macro, the palm and the size card. In the palm the heart reads about 20 mm against the fingers.
- **Copy.** Unchanged: about 20 mm, gold tone, two rows of tiny stones.

### Solitaire Charm Huggies (A14)

- **Checked against `refs/A14_full.jpg` and `refs/A14_det.jpg`.** This morning's gallery was wrong in three ways:
  - it drew a thin-wire hoop;
  - the tube was small;
  - the stone was about 0.4 of the hoop.

  The pair in hand has:
  - a thick, flat-faced band, with an opening about three quarters of the hoop;
  - a chunky square tube, about a third of the hoop;
  - one small ring;
  - a round stone in four claws, about half the hoop.
- **Packshot and macro.** Two rounds of edits, with the detail crop as IMAGE 2 (`A14_det_ref`):
  - `PROP14` changed the band and tube proportions (`A14_Hp`, `A14_Mp`).
  - `STONE14` made the stone 1.25 times bigger and kept exactly one jump ring (`A14_Hs2`, `A14_Ms2`).

  The approved frames are `A14_Hs2_b` and `A14_Ms2_b`. On the packshot:
  - the hoop is 490 px;
  - the stone with its claws is 256 to 264 px, about 6.5 to 7 mm on a 13 mm hoop;
  - the whole earring is 883 to 897 px, about 23.5 mm.
- **Worn.** `WORN14` put the new earring on the bare-lobe plates from this morning, but drew it about 1.5 times too big. `comp.py hug` pasted each earring back at a 13 mm hoop, about a quarter of the ear's height:
  - W1 at 0.67;
  - W2 at 0.84.

  Hair specks under 200 px were dropped from the masks.
- **Palm.** The new packshot's earring was cut out (`A14_Hs2_b_cut`, saved as `build/comp/a14_pair_cut2.png`) and laid in the palm at 13 mm (6.25 px per mm).
- **Size card.** It was redrawn from the new packshot as `cards/solitaire-charm-huggies-size-guide-v2.jpg`. The callouts are 13 mm hoop, 6.5 mm stone and 24 mm long. The old card is kept because Shopify Files holds its name.
- **Copy and spec.** The intro and details now say:
  - a thick band with a hinged snap;
  - a square tube of about 4 mm;
  - a clear cubic zirconia of about 6.5 mm in four claws on one small ring;
  - about 24 mm long;
  - sold as one pair, polished gold tone.

  The lock and negatives in `build/skus.json` describe the same proportions.
- **Not the live Solitaire Drop Huggies (ADT27).** That is a different piece: a 10.5 mm huggie with a 4 mm stone and no tube.

### Composites (`build/comp.py`)

- **`stud`.** For an open stud, the mask is built from the shape:
  - close, then open to cut hair strands;
  - keep the largest part and fill it solid;
  - subtract the smoothed big hole.

  The heart's open centre then shows the bare lobe.
- **`hug`.** This is `worn` with small specks dropped from the mask.
- **`palm`.** It now takes the cut-out, the output name, the hoop size in px, the angle and the centre.

Commands run:

```
comp.py stud A15_W1 A15_W1bare_a A15_W1r 720 370 950 600 828 448 0.92
comp.py stud A15_W2 A15_W2bare_a A15_W2r 1040 440 1330 710 1177 510 0.92
comp.py hug  A14_W1n_a A14_W1bare_a A14_W1k 1090 470 1290 830 1182 495 0.67
comp.py hug  A14_W2n_a A14_W2bare_a A14_W2k 1110 470 1270 840 1190 497 0.84
comp.py palm a14_pair_cut2.png A14_Pk 490 -25 960 1255
```

### Higgsfield

12 generations and 1 background removal, 25 credits. The balance went from 150.71 to 125.71.
- **Solitaire Charm:** 10 generations (4 proportion edits, 4 stone edits and 2 worn) and the cut-out, 21 credits.
- **Open heart:** 2 bare-lobe plates, 4 credits.

### Shopify

One mutation, `CharmHeartFix` (`build/ship_earrings_3nov.py`, `shopify/ship_earrings_3nov.graphql`, `shopify/ship_earrings_3nov.json`), with two updates.
- **Solitaire Charm Huggies:**
  - the five new photos and the -v2 card, with the new packshot as the variant image;
  - the new copy and SEO.

  It stays DRAFT at ₹1,199 with ₹2,199 compare-at and 5 units. It is attached to all six channels and will show once it is set Active.
- **Pave Open Heart Studs:**
  - the two new worn photos;
  - the packshot, macro, palm and card kept by media id;
  - the description unchanged.

  It stays ACTIVE on all six channels at ₹999 with ₹1,899 compare-at and 5 units.
- **Checked afterwards:**
  - both galleries have six media READY, in order;
  - both size-guide links answer 200;
  - each Shopify copy matches its export, with a mean difference of 0.67 to 1.52 out of 255.
- Ids are in `build/drafts_new.json` and `shopify/pushed_2nov.json`.
- `review/charm_heart_3nov.jpg` sets the owner's photo of each pair beside its five photos and size card.

## Folder

- `refs/`: the owner's photos (`*_full.jpg`) and detail crops (`*_det.jpg`).
- `build/`: specs, copy, job ids, approved frames, and the build, edit, composite (`comp.py`), export, card and ship scripts. `build/comp/` holds the cut-outs and masks for the composites. `build/out/` (raw frames) is not committed.
- `review/`: sheets that set the owner's photos beside the new galleries.
- `exports/`: the approved photos at 1288×1600.
- `cards/`: size cards.
- `shopify/`: the mutation and the ids.
