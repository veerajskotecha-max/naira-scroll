# Albyluxe pieces (7 Nov 2026)

## The ask

The owner sent 16 photos of Albyluxe pieces, then 4 more, and asked for:

- the baguette ring in green, white and red;
- "both blue rings", and the two pieces still pending in the second set of photos, skipping the three two-stone rings;
- listing photos made "the way you always do": verified against the photos, with exact sizing (worn photos at true size, an in-palm size photo, a size card);
- names, copy, prices, SKUs and stock, on a page to approve before anything goes to Shopify. Nothing ships until the owner approves it there and says ship.

On 12 Nov the owner asked for the audit's corrections to be made ("Do changes"), then to stop three rings and keep them aside.

## Where things stand

- **The approval page.** <https://claude.ai/artifact/TTS2ManafPXJ3ujNQaNSLR> (version 3, 12 Nov). It is private to the owner.
  - It shows the 15 pieces up for sign-off with every listing photo, the size card, the photo each piece was made from, the copy, the price and compare-at price, the variants and SKUs, what was checked and redone, and what is still to confirm.
  - Each piece has Approve, Change and Hold, editable price, compare-at and units, and a note. "Approve N for Shopify" records the sign-off.
  - Choices are saved in the page's database: `approve/<id>` and `approve/signoff`. On 12 Nov the only saved choice was L01, marked Change with the owner's note (done: its third photo is removed). No sign-off yet.
- **Corrections, 12 Nov.** The 7 Nov audit ([corrections.md](corrections.md)) is worked through: the status of every piece is at the top of that file, and each card's checks on the page say what was redone. Defaults taken while Albyluxe's answers are open: L10 has four bands (title kept), L13 keeps the open back as drawn, L15 keeps the beaded edge, L17 is a full eternity, L18 is unchanged; each is flagged in amber.
- **Set aside, 12 Nov, at the owner's word:** L02 Marquise Molten Bar Ring, L03 Twin Cluster Open Ring and L06 Baroque Pearl Duet Ring, the three rings whose photos on the hand kept failing. They sit read-only at the foot of the page, outside the counts and the sign-off (`"aside"` in `build/listings.json`). Their photos and notes are kept as they are, and no more credits go to them until the owner says.
- **Nothing has been created or changed on Shopify or Meta.**
- The ship (one mutation, as `../albyluxe-31oct/build/ship_31oct.py`) runs only after the sign-off and the word "ship".

## The pieces

| Id | Name | SKU | Price / compare-at | Variants | Photos |
|---|---|---|---|---|---|
| L01 | Molten Wave Oval Ring | MWOR | ₹1,099 / ₹1,999 | adjusts US 5 to 9 | 4 |
| L02 | Marquise Molten Bar Ring (set aside) | MMBR | ₹1,099 / ₹1,999 | adjusts US 5 to 9 | 3 |
| L03 | Twin Cluster Open Ring (set aside) | TCOR | ₹1,199 / ₹2,199 | adjusts US 5 to 9 | 4 |
| L04 | Lilac Flutter Studs | LFS | ₹999 / ₹1,899 | one | 5 |
| L05 | Blush Octagon Studs | BOS | ₹999 / ₹1,899 | one | 5 |
| L06 | Baroque Pearl Duet Ring (set aside) | BPDR | ₹999 / ₹1,899 | adjusts US 5 to 9 | 4 |
| L07 | Two-Tone Heart Snake Chain | TTHS | ₹1,299 / ₹2,499 | one | 5 |
| L08 | Baguette Heart Necklace | JDN0305301 | ₹1,199 / ₹2,199 | one | 3 |
| L09 | Duet Emerald-Cut Cuff | DEC-PK, DEC-CL, DEC-AQ | ₹1,199 / ₹2,199 | Pink, Clear, Aqua | 15 |
| L10 | Interlocked Baguette Trio Ring | IBTR-GR, IBTR-WH, IBTR-RD | ₹1,499 / ₹2,999 | Green, White, Red × US 6, 7, 8 | 15 |
| L11 | Teardrop Pear Hoops | TPH-G, TPH-S | ₹1,199 / ₹2,199 | Gold, Silver | 10 |
| L12 | Baguette Heart Studs | BHS | ₹999 / ₹1,899 | one | 5 |
| L13 | Lattice Lace Ring | LLR | ₹999 / ₹1,899 | adjusts US 5 to 9 | 5 |
| L14 | Zigzag Gem Eternity Ring | ZGER-RD, ZGER-GR, ZGER-WH | ₹1,199 / ₹2,199 | Red, Green, White × US 6, 7, 8 | 15 |
| L15 | Emerald-Cut Bezel Studs | ECBS | ₹999 / ₹1,899 | one | 5 |
| L16 | Charm Chain Duo Ring | CCDR | ₹1,199 / ₹2,199 | adjusts US 5 to 9 | 4 |
| L17 | Aqua Emerald-Cut Band | AECB | ₹1,199 / ₹2,199 | US 6, 7, 8 | 4 |
| L18 | Aqua Oval Cocktail Ring | AOCR | ₹1,099 / ₹1,999 | US 6, 7, 8 | 5 |

Up for sign-off: 15 pieces, 38 variants, 5 units each as proposed (190 units), 105 listing photos. The three set-aside rings would add 3 variants
(15 units). The three two-stone rings (a pear and an emerald-cut side by side, pink and clear) are left out, as the owner said: they are the
Duet Emerald-Cut Ring already on Shopify as a draft (DER-GR, DER-PK, DER-CL). No SKU or title clashes with the live store (checked on Shopify).

## How the photos were made and checked

1. **References** (`refs/`): the owner's 20 photos (`src01`–`src20`) and a crop of each piece (`L01_full` … `L18_det`), uploaded to Higgsfield (`build/ref_ids.json`).
2. **Packshots** (`build/build.py`, `build/skus.json`): Nano Banana Pro at 2K, 4:5, the piece on the house cream cube, with a construction lock, a negative list and a scale line per piece. Each packshot was checked against its reference before anything else was made from it.
3. **Worn photos and macros**, made from the approved packshot alone (`wref: hero`), so the supplier's hands, trays and props could not leak in. L16 kept its supplier photo as a second reference for how the two rings sit. Each was checked for the design and for size against the body: an earlobe is about 18 mm and a finger about 17 mm wide, measured across the finger gaps in the frame.
4. **In-palm size photos** (`build/palm.py`, `build/palm.json`): Higgsfield's background remover cuts out the packshot, and the cut-out is laid on the house empty-palm plate (6.25 px per mm) at its true size, from one measured feature per piece. The edge is trimmed by a pixel so no cube shows round it, and a necklace's chain runs out of the palm at the hand's edge (the `CLIP` argument). L08's cut-out is the remover run on a crop of the packshot (`L08_rbcrop`); the 7 Nov local cut-out (`build/l08cut.py`, no longer used) had turned its cable chain into beads.
5. **Colours** (`build/recolour.py`, `build/tone.py`): only the stones change. `recolour.py` makes the colours the supplier does not show, by CIELab hue window, inside each stone's outline (L10 and L14 green to Red and White; L09 pink to Clear and Aqua). `tone.py` (formerly `l04fix.py`) moves a stone's colour toward the owner's or supplier's photo, by a fixed shift or to a target hue and chroma, optionally inside an ellipse so skin is untouched: L04 lilac (cooler), L05 blush, L10 and L14 green, L18's macro (mint). L11 Silver is Higgsfield edits of the gold photos with only the metal changed (`build/edits.py`), and `build/silverfix.py` takes the warm cast off claws an edit left gold.
6. **Local corrections** (12 Nov): `build/shrink.py` takes a piece the generator drew too large down to its true size in place (it lifts the piece, fills the skin under it with nearby skin, and pastes the piece back smaller about an anchor): L09 and L13 worn photos. `build/l10fix.py` turns L10's white channel stones green in one worn photo; `build/l15fix.py` removes the small clusters at L15's stone corners; `build/l16fix.py` removes L16's sixth charm cleanly; `build/l18fix.py` takes dark specks out of L18's macro stone.
7. **Size cards** (`build/sizecards.py`, `build/photocards.json`, `cards/`): the house ring card (open rings US 5 to 9; closed rings shade only US 6, 7 and 8, to confirm, through a `sizes` key added to `../aditya-jewellery/build/sizeguide.py`), the necklace card, and photo cards with measurement bars for the earrings and the cuff.
8. **Exports** (`build/export.py`, `exports/`): every photo at 1288 × 1600 after the house 1.5% inset, in gallery order (`build/frames.json`). Each run clears a piece's old numbered files first.

### What failed and what was done (7 Nov)

| Piece | Problem | Fix |
|---|---|---|
| L04 | In the owner's photo the upper-right stone looked smaller than the upper-left, and the lilac is paler. | The audit found the two upper stones equal; the lilac is now set cooler (12 Nov). |
| L01 | The first worn photo looked like an old creased print. | Redone. |
| L03 | The second worn photo had four pears and no round stone. | Redone. |
| L07 | The macro came back as a copy of the packshot. | Redone as three hearts close up (replaced 12 Nov). |
| L10 | The two worn photos were the same pose. | The second redone (replaced 12 Nov). |
| L16 | One worn photo had the wrong charms on neighbouring fingers; the other had six charms. | The first left out; the extra pear removed from the second (`build/l16fix.py`), after an edit failed. |
| L17 | The macro set the stones across the band. | Redone with them end to end along the band. |

### The corrections round (12 Nov)

| Piece | Done |
|---|---|
| L01 | Third photo (second worn) removed, as the owner noted on the page; copy: a 5 × 7 mm oval held by the strand and slim claws. |
| L02 | Packshot, macro and palm rebuilt with the marquise and bar following the band; four more worn tries all too large or turned, none used. Set aside. |
| L03 | Five worn retries; the best is kept. Set aside. |
| L04 | Lilac moved cooler on every photo; copy stone sizes; the owner is asked to measure one stud. |
| L05 | Every photo redone as a near-regular octagon (the first round drew a clipped square), the blush matched to the owner's photo. |
| L06 | Five worn retries, still too large or over two fingers; the best is kept. Set aside. |
| L07 | Both worn photos redone: the second's hearts were twice their size; the first still reads about 1.3 times (flagged). Macro tried three times, the last showing five hearts running out of frame on a flat chain; palm rebuilt so the chain runs off the palm. |
| L08 | Four worn tries drew the heart 1.5 to 2 times its size: no worn photo is used. New cut-out; copy 14 mm across. |
| L09 | Packshot edited to a nearly square emerald-cut; macro and both worn photos redone, the worn stones shrunk in place; recolours redone inside the stone only. |
| L10 | Redone with four bands and baguettes in the silver band (packshot, both worn photos, macro); green matched to the supplier; recolours redone. The second worn photo is on the middle finger, about 15% large (flagged). |
| L11 | First worn photo redone at its true size; gold claws on the silver photos fixed (edits, and a local fix where an edit changed nothing); copy and card sizes. |
| L12 | Small stones redrawn square (packshot edit, both worn photos, macro); worn photos read 15 to 16 mm against 14 (noted). |
| L13 | Redone as the lozenge front (packshot, both worn photos, macro); worn photos shrunk in place. |
| L14 | Copy ("high and low" removed); green matched; recolours redone, no green left at the edges, the white macro's flecks gone. |
| L15 | Corner clusters removed from both worn photos; palm rebuilt at true size (was 11% small); card bar fixed. |
| L16 | Traces of the removed charm cleaned up; copy: chain about 6 cm. |
| L17 | First worn photo redone with the stones end to end; the second (back of the hand) failed twice and is left out; copy 6 mm band. |
| L18 | Macro stone matched to mint (was sky blue); palm rebuilt at true size (was 8% large). |

What did not work: a Higgsfield edit to shrink a heart in place (L08), to fix a chain (L07) or silver claws (L11) changed nothing; a radial warp to shrink a pendant with its chain (L08) and a local shrink across finger gaps (L06) smeared, and were dropped; removing a four-point star glint on L14's macro claw looked worse than leaving it. Two worn photos came back as old folded prints; the prompt's ending named creases and old paper to forbid them, and now describes a clean modern photograph instead (`build/build.py` `END`).

### Higgsfield

7 Nov: the first 12 packshots came before this count. From there, 171 credits (177.96 to 6.96): 6 packshots and 2 L04 edits (16), 54 worn photos and macros (108), 10 redos and fixes (20), 4 silver edits (8) at 2 credits each, and 19 background cut-outs at 1 each (19). Several submissions were refused with `429 rate_limit_reached` (the plan runs 4 jobs at once) and resubmitted unchanged.

12 Nov, the corrections round: 139 credits by the job log (`build/jobs.json`): 66 photos and edits at 2 credits and 7 cut-outs at 1. The account was topped up before the round; its balance afterwards was 1,189.96, shared with another session. The prompts are in `build/requests_12nov/` (`req_*.json` as `build.py` wrote them; `b*.json` as submitted, in groups of three, with any hand edits; `req_561.json` is the five-heart L07 macro).

## Still to confirm with Albyluxe (on the page in amber)

- L01, L13, L16: whether the bands are open (adjustable). L02 and L06 (set aside) too.
- L04: one stud's width across the pears (the copy says about 15 mm).
- L05: step cut or sparkly all over, and whether it has claws.
- L07: the chain length (about 42 cm).
- L10: how many bands (four drawn, with a plain gold link band), and the closed sizes (6, 7, 8 assumed); a rename is offered.
- L12: the stud's width (14 mm kept) and the JDE0105301 code, probably this pair.
- L14, L17, L18: closed band sizes (6, 7, 8 assumed).
- L15: plain or beaded edge (beaded drawn), step or radiant cut.
- L17: full or half eternity (full drawn). L18: the stone size (about 13 × 18 mm) and whether the oval sits along or across the finger.

## Files

- `approve/`: the page (`index.html`, built by `build/approve.py` from `template.html` and `base.css`) and its web photos (`img/`, rebuilt from scratch on each run).
- `build/`: specs (`skus.json`), listings (`listings.json`, with `aside` on the three set-aside rings), checks (`checks.json`), frames (`frames.json`), job ids (`jobs.json`) and result URLs (`results.json`), batch indexes (`idx_*.json`), prompts (`req_*.json` for 7 Nov, `requests_12nov/`), and the scripts above. `build/out/` (the 2K frames and cut-outs) is not committed.
- `cards/`, `exports/`, `refs/`, and [corrections.md](corrections.md) (the 7 Nov audit, with the 12 Nov status at the top).

## Rebuilding

```
cd build
python3 -I sizecards.py            # cards/
python3 -I export.py               # exports/
python3 -I approve.py              # approve/index.html and approve/img/
```

The frames themselves are regenerated from the prompts and `jobs.json` (job ids; `results.json` has each result's URL). The local steps are `tone.py`, `recolour.py`, `shrink.py`, `l10fix.py`, `l15fix.py`, `l16fix.py`, `l18fix.py`, `silverfix.py` and `palm.py`; each script's header gives its usage and the exact settings used.
