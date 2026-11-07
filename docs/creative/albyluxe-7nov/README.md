# Albyluxe pieces (7 Nov 2026)

## The ask

The owner sent 16 photos of Albyluxe pieces, then 4 more, and asked for:

- the baguette ring in green, white and red;
- "both blue rings", and the two pieces still pending in the second set of photos, skipping the three two-stone rings;
- listing photos made "the way you always do": verified against the photos, with exact sizing (worn photos at true size, an in-palm size photo, a size card);
- names, copy, prices, SKUs and stock, on a page to approve before anything goes to Shopify. Nothing ships until the owner approves it there and says ship.

## Where things stand

- **The approval page.** <https://claude.ai/artifact/TTS2ManafPXJ3ujNQaNSLR>. It is private to the owner.
  - It shows all 18 pieces with every listing photo, the size card, the photo each piece was made from, the copy, the price and compare-at price, the variants and SKUs, what was checked and what is still to confirm.
  - Each piece has Approve, Change and Hold, editable price, compare-at and units, and a note. "Approve N for Shopify" records the sign-off.
  - Choices are saved in the page's database: `approve/<id>` and `approve/signoff`.
- **Audit, 7 Nov ([corrections.md](corrections.md)).** Every piece was checked again against your and the supplier's photos: 22 must-fix items across 14 pieces, the largest being the plain silver band on L10, the cuff shape of L13, the turned construction of L02 and the oversized worn photos on several pieces. Nothing is fixed yet; hold sign-off on those pieces until they are redone. The redos need about 83 Higgsfield credits (balance 6.96).
- **Nothing has been created or changed on Shopify or Meta.**
- The ship (one mutation, as `../albyluxe-31oct/build/ship_31oct.py`) runs only after the sign-off and the word "ship".

## The pieces

| Id | Name | SKU | Price / compare-at | Variants | Photos |
|---|---|---|---|---|---|
| L01 | Molten Wave Oval Ring | MWOR | ₹1,099 / ₹1,999 | adjusts US 5 to 9 | 5 |
| L02 | Marquise Molten Bar Ring | MMBR | ₹1,099 / ₹1,999 | adjusts US 5 to 9 | 3 |
| L03 | Twin Cluster Open Ring | TCOR | ₹1,199 / ₹2,199 | adjusts US 5 to 9 | 5 |
| L04 | Lilac Flutter Studs | LFS | ₹999 / ₹1,899 | one | 5 |
| L05 | Blush Octagon Studs | BOS | ₹999 / ₹1,899 | one | 5 |
| L06 | Baroque Pearl Duet Ring | BPDR | ₹999 / ₹1,899 | adjusts US 5 to 9 | 5 |
| L07 | Two-Tone Heart Snake Chain | TTHS | ₹1,299 / ₹2,499 | one | 5 |
| L08 | Baguette Heart Necklace | JDN0305301 | ₹1,199 / ₹2,199 | one | 5 |
| L09 | Duet Emerald-Cut Cuff | DEC-PK, DEC-CL, DEC-AQ | ₹1,199 / ₹2,199 | Pink, Clear, Aqua | 15 |
| L10 | Interlocked Baguette Trio Ring | IBTR-GR, IBTR-WH, IBTR-RD | ₹1,499 / ₹2,999 | Green, White, Red × US 6, 7, 8 | 15 |
| L11 | Teardrop Pear Hoops | TPH-G, TPH-S | ₹1,199 / ₹2,199 | Gold, Silver | 10 |
| L12 | Baguette Heart Studs | BHS | ₹999 / ₹1,899 | one | 5 |
| L13 | Lattice Lace Ring | LLR | ₹999 / ₹1,899 | adjusts US 5 to 9 | 5 |
| L14 | Zigzag Gem Eternity Ring | ZGER-RD, ZGER-GR, ZGER-WH | ₹1,199 / ₹2,199 | Red, Green, White × US 6, 7, 8 | 15 |
| L15 | Emerald-Cut Bezel Studs | ECBS | ₹999 / ₹1,899 | one | 5 |
| L16 | Charm Chain Duo Ring | CCDR | ₹1,199 / ₹2,199 | adjusts US 5 to 9 | 4 |
| L17 | Aqua Emerald-Cut Band | AECB | ₹1,199 / ₹2,199 | US 6, 7, 8 | 5 |
| L18 | Aqua Oval Cocktail Ring | AOCR | ₹1,099 / ₹1,999 | US 6, 7, 8 | 5 |

41 variants, 5 units each as proposed (205 units). The three two-stone rings (a pear and an emerald-cut side by side, pink and clear) are
left out, as the owner said: they are the Duet Emerald-Cut Ring already on Shopify as a draft (DER-GR, DER-PK, DER-CL). No SKU or title
clashes with the live store (checked on Shopify).

## How the photos were made and checked

1. **References** (`refs/`): the owner's 20 photos (`src01`–`src20`) and a crop of each piece (`L01_full` … `L18_det`), uploaded to Higgsfield (`build/ref_ids.json`).
2. **Packshots** (`build/build.py`, `build/skus.json`): Nano Banana Pro at 2K, 4:5, the piece on the house cream cube, with a construction lock, a negative list and a scale line per piece. Each packshot was checked against its reference before anything else was made from it.
3. **Worn photos and macros**, made from the approved packshot alone (`wref: hero`), so the supplier's hands, trays and props could not leak in. L16 kept its supplier photo as a second reference for how the two rings sit. Each was checked for the design and for size against the body: an earlobe is about 18 mm and a finger about 17 mm wide.
4. **In-palm size photos** (`build/palm.py`, `build/palm.json`): Higgsfield's background remover cuts out the packshot, and the cut-out is laid on the house empty-palm plate (6.25 px per mm) at its true size, from one measured feature per piece. L08's remover kept the cube, so its necklace was cut out locally (`build/l08cut.py`).
5. **Colours the supplier does not show** (`build/recolour.py`): only the stones change, by CIELab hue window. L10 and L14 green to Red and White; L09 pink to Clear and Aqua (the aqua read off the supplier's cuff). L11 Silver is four Higgsfield edits of the gold photos, with only the metal changed (`build/edits.py`).
6. **Size cards** (`build/sizecards.py`, `build/photocards.json`, `cards/`): the house ring card (open rings US 5 to 9; closed rings 6 to 8, to confirm), the necklace card, and photo cards with measurement bars for the earrings and the cuff.
7. **Exports** (`build/export.py`, `exports/`): every photo at 1288 × 1600 after the house 1.5% inset, in gallery order (`build/frames.json`).

### What failed and what was done

| Piece | Problem | Fix |
|---|---|---|
| L04 | In the owner's photo the upper-right stone is smaller than the upper-left, and the lilac is paler. | Two Higgsfield edits did not change the stone (one turned only one stud pink); a local redraw left marks. The photos keep four near-equal stones (flagged), and every L04 photo gets the same paler lilac (`build/l04fix.py`). |
| L01 | The first worn photo looked like an old creased print. | Redone. |
| L02 | Worn photos laid the marquise and bar along the finger, then (redone) at about 1.5 to 1.8 × size; two shrink edits barely moved it. | No worn photo is used; the palm photo shows its true size (flagged, one more try offered). |
| L03 | The second worn photo had four pears and no round stone. | Redone. |
| L07 | The macro came back as a copy of the packshot. | Redone as three hearts close up. |
| L10 | The two worn photos were the same pose. | The second redone. |
| L16 | One worn photo had the wrong charms on neighbouring fingers; the other had six charms. | The first left out; the extra pear removed from the second by cloning the skin beside it (`build/l16fix.py`), after an edit failed. |
| L17 | The macro set the stones across the band. | Redone with them end to end along the band. |

### Higgsfield

The first 12 packshots came before this count. From there, 171 credits (177.96 to 6.96): 6 packshots and 2 L04 edits (16), 54 worn photos and macros (108), 10 redos and fixes (20), 4 silver edits (8) at 2 credits each, and 19 background cut-outs at 1 each (19). Several submissions were refused with `429 rate_limit_reached` (the plan runs 4 jobs at once) and resubmitted unchanged.

## Still to confirm with Albyluxe (on the page in amber)

- L01, L13, L16: whether the bands are open (adjustable).
- L07: the chain length (about 42 cm).
- L10, L14, L17, L18: closed band sizes (6, 7, 8 assumed).
- L12: the code JDE0105301 (4.0 g, stainless steel) is on the card above the emerald-cut stud in the owner's screenshot; it is probably this pair.
- L15: whether the frame's edge is beaded, as drawn from a small photo.
- L17: full or half eternity. L18: the stone size (about 13 × 18 mm, a second reading gave 10 × 15).

## Files

- `approve/`: the page (`index.html`, built by `build/approve.py` from `template.html` and `base.css`) and its web photos (`img/`).
- `build/`: specs (`skus.json`), listings (`listings.json`), checks (`checks.json`), frames (`frames.json`), job ids (`jobs.json`) and result URLs (`results.json`), and the scripts above. `build/out/` (the 2K frames and cut-outs) is not committed.
- `cards/`, `exports/`, `refs/`.

## Rebuilding

```
cd build
python3 -I sizecards.py            # cards/
python3 -I export.py               # exports/
python3 -I approve.py              # approve/index.html and approve/img/
```

The frames themselves are regenerated from `req_*.json` (prompts) and `jobs.json` (job ids); the local steps are `l04fix.py`, `recolour.py`, `palm.py`, `l08cut.py` and `l16fix.py`.
