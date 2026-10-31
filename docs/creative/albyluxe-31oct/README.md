# Albyluxe and supplier picks (31 Oct 2026)

## The ask

The owner sent screenshots of the pieces they bought, then the 28 to 31 Oct buy book. They asked for:

- 4 to 5 verified listing photos per piece, made from the buy book's photos;
- names, copy, prices, stock and changes;
- a page to check it all on.

Nothing ships until they have verified everything.

## Where things stand

- **The review page.** <https://claude.ai/artifact/K7RkNg1b5Zbqi58Cxyb5k3>. It is private to the owner.
  - Each piece has Approve, Change and Hold, with price, units and a note.
  - Choices are saved in the page's database, in the collection `decisions/<id>`.
- **Nothing has gone to Shopify.** No Meta ad was changed.

## The 28 listings

| Id | Listing | Variants (SKU) | Price / compare-at | Stock | In the buy book |
|---|---|---|---|---|---|
| A01 | Quintet Stack Ring | 6 (QSR-6), 7 (QSR-7), 8 (QSR-8) | ₹1,499 / ₹2,999 | 5 each | **not in the book** |
| A02 | Heart Duet Open Ring | Crystal (HDR-CZ), Pearl (HDR-PL) | ₹999 / ₹1,899 | 5 each | yes |
| A04 | Duet Emerald-Cut Ring | Green (DER-GR), Pink (DER-PK), Clear (DER-CL) | ₹999 / ₹1,899 | 5 each | yes |
| A05 | Oval Duet Ring | Emerald Green (ODR-EM), Sapphire Blue (ODR-SA), Citrine Yellow (ODR-CI), Olive Green (ODR-OL) | ₹999 / ₹1,899 | 5 each | yes |
| A06 | Marquise Charm Band | Gold (MCB-G), Two-Tone (MCB-TT) | ₹999 / ₹1,899 | 5 each | yes |
| A07 | Cascade Pear Drop Earrings | One style (CPDE) | ₹999 / ₹1,899 | 5 each | yes |
| A08 | Bow and Heart Gift Set | One style (BHGS) | ₹1,499 / ₹2,800 | 5 each | yes |
| A09 | Trillion Fringe Necklace | One style (TFN) | ₹1,199 / ₹2,199 | 5 each | yes |
| A10 | Verdant Pear Pendant Necklace | One style (VPPN) | ₹1,199 / ₹2,199 | 5 each | yes |
| A11 | Heartline Tennis Bracelet | One style (HTB) | ₹1,299 / ₹2,499 | 5 each | yes |
| A12 | Heart Solitaire Huggies | One style (HSH) | ₹1,199 / ₹2,199 | 5 each | yes |
| A13 | Slim Pave Huggies | One style (SPH) | ₹999 / ₹1,899 | 5 each | yes |
| A14 | Solitaire Bar Huggies | One style (SBH) | ₹1,199 / ₹2,199 | 5 each | yes |
| A15 | Pave Open Heart Studs | One style (POHS) | ₹999 / ₹1,899 | 5 each | yes |
| A16 | Herringbone Pearl Drop Necklace | One style (HPDN) | ₹1,299 / ₹2,499 | 5 each | **not in the book** |
| B01 | Rouge Heart Bar Bracelet | One style (RHBB) | ₹1,199 / ₹2,199 | 5 each | yes |
| B02 | Emerald Station Snake Chain | One style (ESSC) | ₹1,299 / ₹2,499 | 5 each | yes |
| B03 | Confetti Long Station Necklace | One style (CLSN) | ₹1,799 / ₹3,299 | 5 each | **not in the book** |
| B04 | Rouge Heart Pendant | One style (RHP) | ₹1,199 / ₹2,199 | 5 each | yes |
| B05 | Pastel Trio Cluster Studs | One style (PTCS) | ₹899 / ₹1,599 | 5 each | **not in the book** |
| B06 | Pastel Line Drop Earrings | One style (PLDE) | ₹1,099 / ₹1,999 | 5 each | **not in the book** |
| B07 | Pastel Drop Necklace | One style (PDN) | ₹1,299 / ₹2,499 | 5 each | yes |
| B08 | Ocean Cushion Drop Earrings | One style (OCDE) | ₹1,199 / ₹2,199 | 5 each | **not in the book** |
| B09 | Ocean Cushion Duet Ring | One style (OCDR) | ₹1,099 / ₹1,999 | 5 each | **not in the book** |
| B10 | Ocean Cushion Pendant | One style (OCP) | ₹1,199 / ₹2,199 | 5 each | **not in the book** |
| B11 | Aqua Channel Huggies | One style (ACH) | ₹1,199 / ₹2,199 | 5 each | yes |
| B12 | Verdant Pear Drop Huggies | One style (VPDH) | ₹1,199 / ₹2,199 | 5 each | yes |
| B13 | Pastel Drop Bracelet | One style (PDB) | ₹1,299 / ₹2,499 | 5 each | yes |

- **Totals.** 28 listings, 37 variants and 185 units.
- **Prices.** The 20 pieces in the buy book carry its list prices; the other eight follow the house lines. No cost per item was given, so no margin is set.
- **Clash check.** On 31 Oct, a read-only Admin query found that none of these SKUs or titles is already in the store.

## Photos

The recipe is the house one (`build/build.py`), on Higgsfield Nano Banana Pro at 2K, 4:5:

- a packshot on the cream plaster cube;
- two worn frames on the saffron-camisole model;
- a macro.

The gift set also has an earrings-only packshot.

**References.** Each piece's buy-book photo (`refs/*_hd.jpg`) is IMAGE 1. Where the book has no photo, the owner's screenshot crop is used instead (`refs/*_full.jpg`). The approved packshot (`build/approved.json`) is IMAGE 2 for the worn frames and the macro.

**Credits.** There were 125 generations, about 250 credits; 132 credits are left. Every job id is in `build/jobs.json`, with replaced ones kept as `*_old`.

### Checks and fixes

Every frame was checked against the buy-book photo: build, stone count, colours, metal, and size against the cube or the body. The page lists the checks for each piece (`build/checks.json`).

**Reshot (8 frames):**

| Frame | What was wrong |
|---|---|
| A07 hero | Top stone sideways |
| A15 hero | Pearls; the buy book shows pave |
| B11 hero | A round hoop; it is a tall oval |
| B13 hero | Nine stones; it has seven |
| A02 first worn frame | Fold creases |
| A07 macro | Part of the second earring in frame |
| A08 macro | Repeated the packshot |
| A13 second worn frame | Two huggies on one ear |

The B13 reshoot used `refs/B13_hd.jpg`, the bracelet alone cut from the buy-book photo, with an explicit seven-stone lock.

**Fixed by hand:**

- **A06 Two-Tone worn frame.** It came with a border. It is cropped to the clean picture inside, as `A06t_W1c`.
- **B06 top stud.** The shoot drew it pink. `build/topstud.py` recolours it lilac inside a small box in the three frames that show it, to the lilac of the B05 studs.

**Colour variants** come from `build/recolour.py`, which changes only the stone:

- Duet Emerald-Cut: Pink and Clear.
- Oval Duet: Sapphire, Citrine and Olive.

Macro frames use their own mask: the whole stone outline including near-black facets, plus a hue-only shift for the coloured glow on the plaster. The first macro recolours left black facets and a hard-edged smear.

**Prompt rules added after the failures:**

- exactly one earring per ear in worn frames;
- one earring only in an earring macro;
- a clean modern photograph, with no creases or aged paper.

## Size cards

`cards/` holds 28 cards, drawn by `build/sizecards.py` with the house generators (`../size-cards/build/cards.py`).

- **Rings.** Open rings fit US 5 to 9. The three closed bands are shown at 6 to 8, to confirm.
- **Bracelets.** The ruler card.
- **Necklaces.** The neck card.
- **Earrings and the set.** Photo cards with measuring bars (`build/photocards.json`).
  - A07 and B08 lie diagonally in their packshots, so their cards use the close worn frame, where the earring hangs straight.

Every size is an estimate from photos until the stock is measured.

## Open questions (also on the page)

- **A14 Solitaire Bar Huggies.** A new listing, or +4 units on the live Solitaire Drop Huggies (₹649)?
- **B11 Aqua Channel Huggies.** Their own listing, or a fifth colour, Aqua, on the live Baguette Huggies?
- **Closed-band ring sizes.** A01, A05 and A06 assume 6 to 8.
- **316L PVD labels.** A08, A13 and A16 carry them. The copy quotes the label and makes no waterproof or tarnish claim.
- **Ask Albyluxe:**
  - Do they make the Clear duet ring (A04)?
  - Do the rouge hearts (B01, B04) come in gold?
  - Confirm A15's metal, B02's side stones and B12's shade.
- **Not in the buy book.** Eight pieces: confirm they were bought, or hold them.

## Folder

- `refs/`: screenshot crops and buy-book crops.
- `build/`: specs, prompts, job ids, copy and the scripts that make everything below. `build/out/`, the raw frames, is not committed.
- `exports/`: 137 listing photos at 1288×1600 (`<handle>-NN.jpg`, variant by variant), from `build/export.py` and `build/frames.json`.
- `cards/`: the size cards (`<handle>-size-guide.jpg`).
- `review/`: the review page and its images, from `build/review.py`.

## On "ship"

Ship only what is approved, in one mutation, as `../clover-garland/build/ship_30oct.py` did:

1. Put the exports and cards on Higgsfield's store for public URLs (`build/put.py`).
2. Turn autoPublish on for the six sales channels.
3. Run one productSet per approved listing: ACTIVE, with variants, stock, photos, each variant's hero, the size card last, metafields and SEO.
4. Turn autoPublish off again.
