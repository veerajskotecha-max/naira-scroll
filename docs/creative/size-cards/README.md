# Size cards for the last 21 listings (28 Oct 2026)

The owner asked for size cards on the rest of the live listings that had none ("rest do all"), and for the white Clarté
not to be listed. Clarté Baguette Bracelet — Silver stays a Draft, as the owner set it at 09:12 UTC; nothing was
deleted. The storefront audit that morning ([`../aditya-jewellery/README.md`](../aditya-jewellery/README.md), "28 Oct:
size cards in every gallery") found 22 live jewellery listings without a card. 21 now have one; Triple Dawn Cuff was
skipped (below).

## The cards

`build/cards.py` draws them from `cards.json` into `out/<handle>-size-guide.jpg` (1600×1600). It uses the existing
generators, so the cards match the live ones:

- **Photo card** (12): the listing photo (`src/`) in a panel with measurement bars, from
  `../aditya-jewellery/build/sizeguide.py` `photo()`. That function now also takes a photo `path`, a bar label `below`
  its bar, and its own footnote.
- **Bracelet card** (5): the length on a 0–24 cm ruler and the wrists it fits (length less 1.5 to 2.5 cm), from
  `../aditya-bracelets/build/sizeguide.py` `card()`, which now takes its own footnote.
- **Necklace card** (4): `necklace()` in `build/cards.py`, after the live Serpentine Whisper Chain card. It draws a neck
  and shoulders outline with the house reference lengths (36 cm choker, 40 base of the neck, 45 collarbone, 50
  mid-chest, 60 matinee), plus the piece's own length in gold.

| Listing | Card | Figures | Source |
|---|---|---|---|
| Baguette Halo Drops | photo | drop 27 mm, disc 14 mm | Edition One shoot's size (14 mm disc); drop from the hero's proportion |
| Petite Square Huggies | photo | 15 mm across | Edition One shoot's size |
| Pearl Circlet Studs | photo | 13 mm, pearl 9 mm | performance-ads shoot's size |
| Petite Bow Studs | photo | 14 mm wide | Edition One shoot's size |
| Prism Cluster Studs (silver) | photo | arc 20 mm, centre stone 6 mm | Edition One shoot's size |
| Verdant Cushion Studs | photo | 13 mm, stone 8 mm | performance-ads shoot's size |
| Lilac Papillon Ring | photo | butterfly 18 mm, 24 mm with its outline | Edition One shoot's size; the outline from the macro |
| Molten Panel Bangle | photo | 10 mm wide | the listing's Width line |
| Watch Link Bangle | photo | 10 mm wide | the listing's Width line (it uses the Molten Panel Bangle's photos) |
| Marquise Coil Cuff | photo | 14 mm across the two turns, marquise 7 mm | the listing's Width and Stones lines |
| Tile Stone Bangle | photo | 4 mm wide, 4 mm tiles | the listing's Pattern line |
| Baroque Pearl Lariat | photo | ring 20 mm, drop pearl 15 mm, slides to adjust | the listing's Details. No chain length is stated, so the card shows none |
| Heartbead Bracelet | bracelet | 18 cm | **estimate**: about 24 beads of 6 mm, plus the toggle |
| Lumière Oval Bracelet | bracelet | 17 cm | **estimate**: the house tennis-bracelet length |
| Clover Chain Bracelet | bracelet | 17 cm | **estimate**: shown on the same display as the 17 cm Watch Link Strap |
| Clover Station Bracelet | bracelet | 17 cm | **estimate**: as the Clover Chain |
| Open Heart Layered Bracelet | bracelet | 17 cm | **estimate**: as the Clover Chain |
| Heartline Paperclip Necklace | necklace | 42 cm, hearts 5 mm | **estimate**: its model photo sits it just below the base of the neck |
| Pearl Legacy Necklace | necklace | 42 cm, pearls 9–11 mm | **estimate**: worn at the collarbone |
| Lumière Oval Necklace | necklace | 40 cm | **estimate**: worn at the base of the throat |
| Pearl Heart Layered Necklace | necklace | 40 and 45 cm, heart pearls 7 mm | **estimate**: where the two strands sit |

`cards.json` gives each figure's source in full. None was tape-measured. The bars on a photo card share one scale, so
its numbers agree with each other. The cards with the nine estimated lengths say the length is approximate. A tape
measure on the stock should confirm them: correct `cards.json`, run `build/cards.py` and ship the card again.

## Skipped: Triple Dawn Cuff

Its copy describes three graduated bands, but all three photos show a single wide hammered cuff. This was flagged in
`docs/research/03-audit-history.md` when it was moved to Draft; it is Active again. A card drawn on those photos would
size the wrong piece. It needs new photos, or copy for the cuff in the photos, before it can have a card.

## Shipped

The owner approved one mutation: `payloads/ship_28oct_cards.graphql`, with variables in
`payloads/ship_28oct_cards.json`. `build/ship.py LIVE.json` builds it from a storefront read taken just before.

- `fileCreate` stored each card as `<handle>-size-guide.jpg`, the name its description links to.
  - `molten-panel-bracelet-size-guide.jpg` was already taken by that listing's unused 21 Oct card (17 cm, from before the
    piece was found to be a rigid bangle), so it was replaced in place (`REPLACE`).
  - That file's alt text in Shopify Files still reads "Molten Panel Bracelet". Nothing shows it.
- `productUpdate`, once per listing:
  - put the card in the description before Care, with every other line as it was live;
  - added a copy of the card to the end of the gallery. The copy is a second file in Shopify Files, named after its
    upload.
- Public URLs for Shopify came from Higgsfield's media store (`url_map.json`). No Higgsfield credits were used, and no
  Meta ads were touched.

## Verified (28 Oct)

- **Files.** All 21 are READY, 1600×1600, at their named URLs. Each CDN copy matches `out/`, with a mean difference of
  0.24 to 1.04 out of 255 (JPEG noise), with or without `?v=`. That includes the replaced Molten Panel file.
- **Listings.** All 21 are Active. Each gallery ends with the card, READY, within the 20 photos the storefront reads.
  The storefront's description shows the card once, before Care.
- **Audit.** A fresh storefront read found 154 live products, 136 of them jewellery. 135 have the card in both the
  description and the gallery. Triple Dawn Cuff is the only jewellery listing without one. The other 18 products have
  no product type (clothing and the like).

## Seen on the way, not changed

- **Pearl Circlet Studs and Petite Bow Studs** are silver tone in every photo, but their copy says gold tone metal and
  PVD 18K gold coating. Their cards show the silver photos.
  - Pearl Circlet's pearl and halo are cushion shaped, though the copy says round, and the macro's alt text says yellow
    gold.
  - Petite Bow's knot is a heart shaped stone.
  - The copy is the owner's to approve, so it was left.
- **The Watch Link Bangle** listing uses the Molten Panel Bangle's photos (ADT18 duplicates that listing), so the two
  cards are the same apart from their titles.

Scripts run with `python3 -I`: `build/cards.py` (draws `out/`) and `build/ship.py LIVE.json` (the payload).
