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

## Folder

- `refs/`: the owner's photos (`*_full.jpg`) and detail crops (`*_det.jpg`).
- `build/`: specs, copy, job ids, approved frames, and the build, edit, export, card and ship scripts. `build/out/` (raw frames) is not committed.
- `exports/`: the approved photos at 1288×1600.
- `cards/`: size cards.
- `shopify/`: the mutation and the ids.
