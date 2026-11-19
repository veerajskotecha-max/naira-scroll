# b02 rescue: b02-2 and b02-5 laid out at zero credits (19 Nov 2026, about 18:52 UTC)

This is b02 loop change 2. The pictures already existed. Nothing was generated, edited, scaled or composited, and no Higgsfield
tool was called. The two Feed crops use the RULINGS §4 rule as amended at 18:45 ("Feed = any 4:5 window,
`.pic { object-position: 50% P% }`, T = 5.85 × P, Feed y = src y × 0.703125 − T"). Each Story is the native frame
(Story y = src y × 0.703125 − 7.5).

Both ads still go to both critics, scored on the final JPGs listed at the end. Nothing here is a ship verdict. Ledger and
learnings untouched.

## Crops and subject extents

Extents were measured on the source: sky-difference mask for b02-2, a green-or-unsaturated mask for b02-5. The verifier's
numbers agree to within about 5 px.

| Ad | Picture | P | T | Subject extent on the Feed | Gate |
|---|---|---|---|---|---|
| b02-2 | `pics/b02-2.png` (try 2) | **85** | 497 | huggies y 333–603, x 283–821 (49.8% wide); shadows y 831–886; full extent **333–886 (553 px)** | headline + card band 380–930 holds 550 px. The extent is **3 px too tall** for any T, so it can never sit strictly inside. The 47 px above 380 is plain sky under the beat (beat glyphs end at about 278). |
| b02-5 | `pics/b02-5_try1.png` (try 1) | **100** | 585 | ring y 79–792 (lowest prong 797), x 317–802 (45% wide); contact shadow to the right, y 690–840; full extent **79–840** | card-only band 84–930. The ring's top arc reaches 79, **5 px above 84**. T is already at its maximum (585). That 5 px is picture, not text. |

**Why b02-2 uses P 85, not loop.md's P 80**
- At P 80 (T 468) the extent is 362–915, and the shadows end only 25 px above the wordmark at 940. The card crowded the float,
  and the float is the proof.
- At P 85 the gaps are even: about 55 px from the beat to the huggies, and 54 px from the shadows to the card.
- The headline moved from top 104 to 96, and the beat from 226 to 214, to keep the top gap.

**Scale**
- **b02-2:** about 17 px/mm (338 px for 14 mm on the source × 0.703). That is under the 19 px/mm trigger, so there is no size tag.
- **b02-5:** the front ovals measure 110–120 × 85–96 px for 5 × 4 mm, which is about 23–24 px/mm. The ring's height alone would
  give about 35 px/mm, because the model drew the stones small for the band (oval ÷ inner opening 0.19, the same as the upright
  reference). Either way it is over 19, so the size tag is on both formats.

## Copy chosen, and why

### b02-2 · Brushed Gold Huggies · A13 Suspended

**On image: the brief's copy, with two fixes**
- **Headline:** "The ₹699 pair."
  - Cormorant Garamond italic 500, 96 px, ink. A13 allows Cormorant 96 when the headline holds a price.
  - The rupee and the digits cannot go in Velista, so no Velista is used on this ad.
- **Beat:** "any three pieces, 20% off."
  - **60 px.** The brief's 52 px is 0.54 × the headline, under the §4.0 floor of 0.6. At 60 px it is 0.625.
  - Set in **--oxblood**, not coral-deep: coral-deep reads 1.8:1 on this sky, oxblood 5.4:1.
  - The bundle line is allowed because BUY3 is verified, and the offer box on the same frame names the code.
- **Card line:** the brief's "soft brushed satin, not mirror polished" became **"about 14 mm · brushed satin, 18k gold tone"**
  (PLAYBOOK A1's Brushed line). `products.md` lists "mirror" as forbidden for this SKU.
- **Offer:** `Codes BUY2 · 10% off ◆ BUY3 · 20% off`, with an oxblood lozenge.
- **Story:** the brief's stack (headline Cormorant 80, beat 52 at 0.65, name and price on one baseline, offer), spaced
  270–714 so that about 108 px of plain wall stays above the pair.

**Meta**
- **Primary text:** the brief's last sentence "Never mirror polished, and waterproof." became "And yes, waterproof and tarnish-free."
  (the same "mirror" reason; the claims sit last, as proof).
  - "The ₹699 pair: Brushed Gold Huggies, about 14 mm, in soft brushed satin 18k gold tone. Any 3 pieces with BUY3: 20% off. And yes, waterproof and tarnish-free."
  - 157 characters; the offer ends at character 119.
- **Headline:** "Brushed Gold Huggies · ₹699 · 20% off 3" (39 characters).
- **Description:** "Brushed satin · 18k gold tone" (29 characters).
- **URL:** `utm_campaign=ads500_b02`, `utm_term=b02-2_a13_brushed-699-levitation`.

### b02-5 · Verdant Eternity Band · A1 Product Card (was A5)

**On image**
- No headline.
- **Size tag:** "SHOWN MAGNIFIED / ABOUT 16.5 MM INSIDE", from the listing's inner diameter of about 16.5 mm.
- **Card line:** "emerald-green cubic zirconia · adjustable US 5 to 9". `products.md` gives oval green CZ 5 × 4 mm, an open back
  adjustable US 5–9, and the allowed words "emerald-green cubic zirconia" and "adjustable". The wording matches the listing,
  so it was kept as given.

**Feed layout**
- **Tag:** kit 30 px, padding 8/16, centred at 820–912.
  - It sits 23 px under the lowest prong and 28 px over the wordmark.
  - It is set in ink-soft so that it reads as the ring's caption, below the brand in the hierarchy.
  - Beside the ring there is at most about 340 px of width, too narrow for the 438 px tag.
- **Card:** top 940 to 1252, on plain saffron.
- **Lozenge:** the stones' own green (#196B3E, sampled). Coral-deep disappears on saffron.

**Story layout**
- The whole card moves above the ring and ends at 626, before the 630 limit; the ring starts at 656.
- **Stack:** wordmark 270–326, name and price on one baseline, line, offer 458–520, then the tag at 540–626.
- **The tag** keeps the Feed's two-line form, at the brief's Story size of 26 px. A one-line tag ran 720–820 px wide and read
  as a second offer bar stacked under the first.

**Meta (the brief's, unchanged)**
- **Primary text:** "US 5 to 9, one ring: Verdant Eternity Band, ₹1,049, emerald-green cubic zirconia, open back adjusts. BUY2: 10% off 2 pieces. Silver tone, and waterproof."
  - 153 characters; the offer ends at character 124.
- **Headline:** "Verdant Eternity · ₹1,049 · 10% off 2" (37 characters).
- **Description:** "Adjustable US 5 to 9" (20 characters).
- **utm_term:** changed to `b02-5_a1_verdant-us5-9` to match the new archetype.

### Banned-word scan

Over all four pages and both copy files there are no hits for diamond, real gold, solid gold, freshwater, emerald or ruby as a
noun, free shipping, compare-at or "was" prices, or "mirror". Gold and silver appear only as "18k gold tone", "silver tone"
and inside product names.

## Contrast

Each text box was measured against the picture behind it. Figures are the median, with the 2nd percentile in brackets. No
scrim was needed anywhere.

| Page | Readings |
|---|---|
| b02-2 Feed | headline ink 8.6 (8.2) · beat oxblood 5.4 (5.2) · wordmark 12.7 · name 12.2 · price 11.5 · line 10.9 · offer 10.3 |
| b02-2 Story | wordmark 8.0 · headline 8.2 · beat oxblood 5.1 · name and price 8.5 · offer 8.6 |
| b02-5 Feed | tag ink-soft 7.3 (4.7 where the box edge meets the shadow) · wordmark 11.0 · name 11.0 · price 10.9 · line 10.8 · offer 10.7 |
| b02-5 Story (darker saffron at the top) | wordmark 5.8 · name and price 5.9 · line 6.0 · offer 6.1 · tag ink-soft 4.2 (3.9). The tag is 26 px Jost 500, which counts as large text. |

## Renders (final, from `batches/b02`, `node ../../kit/render.cjs`)

```
{"out":"b02-2_feed.jpg","size":"1080x1350","failed":[],"overflow":[],"fallback":[],"textShare":0.12,"outside":[],"minFont":26}
{"out":"b02-2_story.jpg","size":"1080x1920","failed":[],"overflow":[],"fallback":[],"textShare":0.064,"outside":[],"minFont":26}
{"out":"b02-5_feed.jpg","size":"1080x1350","failed":[],"overflow":[],"fallback":[],"textShare":0.078,"outside":[],"minFont":26}
{"out":"b02-5_story.jpg","size":"1080x1920","failed":[],"overflow":[],"fallback":[],"textShare":0.057,"outside":[],"minFont":26}
```

Final JPG times (`stat -c %y`), for the critics' `scoredFile`:

| File | Modified (UTC) |
|---|---|
| b02-2_feed.jpg | 2026-11-19 18:51:53 |
| b02-2_story.jpg | 2026-11-19 18:51:54 |
| b02-5_feed.jpg | 2026-11-19 18:51:54 |
| b02-5_story.jpg | 2026-11-19 18:51:54 |

## What I could not satisfy

1. **b02-2: the placement gate, by 3 px.** The extent is 553 px against a 550 px band, so no T fits it strictly inside
   380–930. Nothing touches type: the gaps are about 55 px above and 54 px below.
2. **b02-2: the picture's colour.** The grey-green lower halves (saturation 0.07–0.12) stay, because they are in the picture.
   The pair also spans about 49–50% of the width, against the brief's 35–45%.
3. **b02-5: the ring's top arc** sits at Feed 79, 5 px above the card-only band, with T already at its maximum. Its headroom
   (79 px) is tighter than its room below (23 px to the tag, then the card).
4. **b02-5: the space around the tag.** The tag has only 148 px between the ring and the card. It is centred with
   gaps of 23 and 28 px. That is legible, but a tag-then-card column is tighter than an art director would choose.
5. **b02-5: the Story size tag** is 26 px, the brief's Story size, not the PLAYBOOK's 30 px. At 30 px the two-line tag does not
   fit above the ring by 630 together with the card line.
6. **The kit's coral-deep accent** fails on both grounds. Oxblood is used on sky and the stone green on saffron. I did not
   change the kit.
7. **No ledger rows were written** (out of scope). Loop change 2's ledger test still needs the lead to add the new verdicts and
   the `scoredFile` values once the critics have scored.
