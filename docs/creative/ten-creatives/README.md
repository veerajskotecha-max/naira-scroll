# Ten Creatives — two sets, two formats

Designed static ads for Naira Petite, built the way the Encore "PIERCE NOTHING" / "WHAT I WEAR TO THE RAVE"
references are built — a typographic system with product tiles, prices set as design, and one idea per ad —
translated into Naira's own identity rather than copied.

Artifact: https://claude.ai/artifact/HCCqaCCy17dVC3hyFENAzu

| | Feed 1080×1350 | Story 1080×1920 |
|---|---|---|
| Contact sheets | `00-contact-feed.jpg` | `00-contact-story.jpg` |
| Files | `feed/` | `story/` |

## What the references actually do (the mechanism, not the surface)

1. **One idea, stated as a rule** — 2–4 words, imperative or confessional ("Pierce nothing", "What I wear to the rave").
2. **A parenthetical aside** in italic serif gives the brand a *person*: dry, lowercase, knowing.
3. **Uniform tiles** — same light, same ground, so a grid reads as a system, not a collage.
4. **Price is a design element**, set as large as the name. It says the brand isn't embarrassed by the number.
5. **A format the reader already owns** — catalogue grid, packing checklist — so the ad is a useful object first.
6. **The CTA names the collection**, never "shop now". Every ad routes to a collection, which is also Naira's own rule.
7. Restraint: one accent, one weight, lots of ground.

## Naira's version of that system

Everything below is pulled from the brand's own assets, not invented:

| Element | Source | Decision |
|---|---|---|
| Display type | `public/fonts/Velista.ttf` — the site's brand serif | Headline in Velista caps, second line in the accent |
| Aside | Cormorant Garamond italic — already loaded by `index.html` | The parenthetical |
| Labels / prices | Jost — the site's sans | Product names and prices, tracked caps |
| Spec lines | JetBrains Mono | `01 // WRIST · RHODIUM · 5MM CUSHION CZ` — the craft vocabulary no competitor uses |
| Corners | `tailwind.config.ts` sets **every radius to 0** | Sharp CTA rectangles, sharp tiles — the one place this deliberately differs from Encore's pills |
| Ground, Set A | The house product photography is a warm ivory plinth | Ivory `#F1EBE1` — tiles melt into the ground exactly as Encore's melt into black |
| Accent | The brand's own campaign shoot (Prism Rivière, Woven Gold Hoops on wet oxblood) | Oxblood `#6E1E2A` |
| Ground, Set B | Same oxblood, deepened | Wine `#2A0D14`, ivory type, blush `#F2C4BD` accent; the ivory plinth photos become cards |
| Wordmark | `public/logo.png`, cropped to its alpha bbox | Ink tint on ivory, ivory tint on wine |

Tiles are square crops of the *existing* website plinth photographs — no cutouts, no generation — chosen per
SKU from all 3–6 listing images (`build/tiles.py`). The only cutouts are the three hoops in A2, which have to be
transparent to sit on a ruler.

## The two sets

**SET A — THE SPEC SHEET** (ivory). The craft lane: across 498 competitor creatives, no brand talks about how a
piece is made. These do, plainly.

| # | Kind | Headline | Pieces (live stock) | Routes to |
|---|---|---|---|---|
| A1 | grid 2×2 | STEEL. / NOT SILVER. | Prism Rivière (77) · Heartbead (29) · Vintage Halo (5) · Pearl Blossom (5) | *Steel* — needs a smart collection, tag `Rhodium Plated` |
| A2 | actual size | ACTUAL SIZE. / HOLD IT UP. | Brushed Gold Huggies 12mm (16) · Baguette Arc 20mm (4) · Woven Gold Hoops 25mm (77) | Earrings |
| A3 | spec sheet | THE SPEC. / ALL OF IT. | Toggle Link Chain (80) | Necklaces |
| A4 | plain | SWEAT / IN IT. | Toggle Link Chain (80) — Keep It On plate 07 | Necklaces |
| A5 | plain | GOLD / THAT STAYS. | Woven Gold Hoops (77) — territory frame 04 | Earrings |

**SET B — WHAT I WEAR** (wine). The stack: the research says the lever is basket size, not creative. Every ad is a
look with a total.

| # | Kind | Headline | Pieces (live stock) | Total | Routes to |
|---|---|---|---|---|---|
| B1 | checklist | WHAT I WEAR / TO THE SANGEET. | Heartline Paperclip (5) · Baguette Arc (4) · Baroque Shell (13) · Chevron Whisper (5) | ₹6,896 | Shop All |
| B2 | checklist | WHAT I WEAR / TO WORK. | Brushed Gold Huggies (16) · Toggle Link (80) · Heartbead (29) · Star Point Band (3) | ₹4,696 | Shop All |
| B3 | receipt | WHAT I WEAR / ON ONE HAND. | Petite Pavé (4) · Chevron Whisper (5) · Vintage Halo (5) | ₹3,197 | Rings |
| B4 | plain card | WHAT I WEAR / TO THE AIRPORT. | Toggle Link Chain (80) — website model shot | — | Necklaces |
| B5 | plain card | WHAT I WEAR / TO BRUNCH. | Prism Rivière (77) — website oxblood shot | — | Bracelets |

## The stock gate (this is why these SKUs and not others)

Live query, 26 Sep 2026: 73 active products, 55 jewellery, **38 in stock**. Seventeen active jewellery SKUs sit at
zero — including Baguette Éclat, Blush Station, Molten Bloom and the gold Serpentine, all of which appeared in
earlier campaigns. Rules applied:

- Hero of a plain ad: ≥ 13 units. Only six SKUs qualify — Toggle Link Chain 80, Prism Rivière 77, Woven Gold
  Hoops 77, Heartbead 29, Brushed Gold Huggies 16, Baroque Shell 13. They carry 12 of the 23 placements.
- Named in a grid or list: ≥ 3 units, and the CTA routes to a collection so a sell-out doesn't break the ad.
- Nothing at 1–2 units anywhere (that removes Rose Verdant, Solitaire Whisper, Verdant Eternity, Charm Box,
  Bold Nocturne Bracelet, Baroque Pearl Lariat).
- Water claims only on SKUs whose Care block says waterproof. Baroque Shell is not — it appears only in B1,
  which makes no water claim. **Do not overlay a waterproof line on B1.**

## Verification

`build/gen.py` refuses to render if any SKU is inactive, unavailable or under 3 units. Names and prices are read
from Shopify at build time — nothing is typed. A second pass checks that every figure in the mono lines
(4mm, 50cm, 15mm, 12g, 25mm, 8×6mm, US 7 …) exists in that SKU's listing Details. All 23 placements passed both.

**1:1 in A2.** Scale is 1080 px ÷ 68 mm = 15.9 px/mm — a 68 mm display is most 6.5–6.7 in phones. A 6.1 in
iPhone is 65 mm wide, so it shows the hoops ≈5 % small; the ad says so in the footnote. Outer diameters were
measured on the isolated front hoop of each cutout (largest connected component), then scaled to the listing's mm.

## What this does not claim

- These are designed for overlays *not* to be needed — but copy space is not reserved as it was in Keep It On.
- The "Steel" CTA on A1 needs a smart collection that doesn't exist yet (tag `Rhodium Plated`); until then route
  to Shop All.
- The A4 plate shows more chin than the neck-down standard. Usable in a paid feed; a tighter reshoot is optional.
- Nothing here has been tested against live spend.

## Rebuild

```
python3 build/tiles.py      # square tiles from the website plinth photos
python3 build/gen.py "" feed,story
```
