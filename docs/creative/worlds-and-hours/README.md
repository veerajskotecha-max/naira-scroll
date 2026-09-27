# Worlds and Hours — ten creatives, volume two

Built on the studio's own Higgsfield archive rather than new generation: 2,767 image generations
(24 Jun – 26 Sep 2026) were pulled, classified against the live catalogue, and 19 frames chosen for
in-stock pieces. Three candidates were rejected on inspection. Every piece is in stock; every
name and price is read from Shopify at build time.

Artifact: https://claude.ai/artifact/H3gMwTjyN6WNb6UYAw3RKw

| | Feed 1080×1350 | Story 1080×1920 |
|---|---|---|
| Contact sheets | `00-contact-feed.jpg` | `00-contact-story.jpg` |
| Files | `feed/` | `story/` |

## The two sets

**SET C — WORLDS** (one word, one colour world, the piece in front)

| # | Word | Piece (stock) | Device | Source gen |
|---|---|---|---|---|
| C1 | HEART. | Heartbead Bracelet (29) | masthead behind the subject | `1fb1bc7b` 11 Sep |
| C2 | LIGHT. | Prism Rivière Bracelet (77) | type as a window — letters filled with the photograph | `25132ba1` 11 Sep |
| C3 | LOUD. | Woven Gold Hoops (77) | masthead behind, oxblood on grey | `c97553ca` 9 Aug |
| C4 | QUIET. | Brushed Gold Huggies (16) | the hidden letter | `85841af6` 6 Aug |
| C5 | LINK. | Toggle Link Chain (80) | word set along the groove the chain cut | `3badd58e` 11 Sep |

**SET D — HOURS** (same piece, different hour; numerals straddle the seam)

| # | Hours | Piece (stock) | Top / bottom source |
|---|---|---|---|
| D1 | 10:00 desk / 22:00 bar | Heartbead Bracelet (29) | website wrist shot `4d465995` / red tumbler `b5f1901f` |
| D2 | 07:30 after the run / 20:00 dinner | Toggle Link Chain (80) | Keep It On plate 07 `382b55d4` / collarbone `19d5af6f` |
| D3 | 11:00 brunch / 23:00 ice | Prism Rivière (77) | wrist `21d81f3b` / purple ice `213dc07f` |
| D4 | 07:15 mirror / 23:30 last drink | Woven Gold Hoops (77) | fogged mirror `4e50565d` / oxblood lacquer `141d0fbd` |
| D5 | 06:40 · 10:15 · 17:00 | six pieces, ₹7,794 | monochrome day series `7d3d3b79` `ee11fd45` `566b81ec` |

## What the archive study found

- 1,451 of 2,767 generations name a catalogue piece; only **386 carried a reference image**. A prompt
  naming a piece is no guarantee the render is that piece, so every frame was checked by eye.
- Four of the most-photographed pieces are now out of stock and unusable: Rivière Eternal (164 gens),
  Molten Bloom (63), Baroque Bloom Cuff (61), Pearl Reverie (19).
- The in-stock pieces with the deepest archive — Toggle Link 147, Woven Hoops 139, Prism 63,
  Heartbead 25 — carry nine of the ten creatives.

## Rejected on inspection

| Gen | Why |
|---|---|
| `0563ad45` #583 | Heartbead rendered as grey pearls; the listing says mirror-polished steel, "not pearl". |
| `d29e0053` #1028 | The "Star Point Band" came out as a pavé clover bangle Naira does not sell. |
| `a661d880` #2120 | Tumblers slice the Prism so the clasp and stone count cannot be read. |

## Gates

`build/gen2.py` refuses to render if a piece is inactive, unavailable, under 13 units for a hero
frame or under 3 for a listed piece. All ten pieces carry the waterproof Care line, so the shower,
run, rain and ice frames claim nothing the listings do not. `build/ledger.json` holds every frame's
generation id, prompt head, pieces, stock and check note.

## Limits

- C2's type-as-window uses a fixed-attachment background clip; it renders in Chromium and the
  exported JPEGs are what ship.
- D2 top and D4 top re-use approved plates from earlier volumes.
- Nothing here has been tested against live spend.
