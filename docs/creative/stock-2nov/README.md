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

## Waiting for credits

Higgsfield ran out after 19 generations, about 38 credits. Still to shoot, 4 photos each:
- N01 to N08: 32 photos.
- N09: 3 photos. Its macro is the approved frame `N09_M`, the first set macro, which shows exactly that necklace.

That is about 35 generations, roughly 70 credits plus reshoots. Specs (`build/skus.json`), copy and prices (`build/listings.json`), references (`build/ref_ids.json`) and the size cards (`cards/`) are ready. After a top-up:
1. `build.py` for H first, then W1, W2 and M from the approved packshot.
2. Verify against the owner's photos, export, upload with `build/put.py`.
3. One productSet per piece as DRAFT with 5 units, as `ship_2nov.py` does for A16.

## Folder

- `refs/`: the owner's photos (`*_full.jpg`) and detail crops (`*_det.jpg`).
- `build/`: specs, copy, job ids, approved frames, and the build, edit, export, card and ship scripts. `build/out/` (raw frames) is not committed.
- `exports/`: the approved photos at 1288×1600.
- `cards/`: size cards.
- `shopify/`: the mutation and the ids.
