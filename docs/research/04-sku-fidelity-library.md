# Naira Petite — Per-SKU Fidelity Reference

Compiled 2026-08-19 from a live Shopify Admin GraphQL pull (`mcp__Shopify__graphql_query`), paginated to exhaustion, filtered to `status: ACTIVE`. Manufacturer dimensions were parsed out of each product's `descriptionHtml` programmatically (`extract_details.py`, a regex/HTML parser run over every listing's "Details" bullet block, not hand-transcribed) before any fidelity-lock paragraph was written. This file is the SKU-level Block 3 ("FIDELITY LOCK") library referenced by the two-slot prompt architecture already documented in this workspace (`E-two-slot-system.md`).

## What was pulled, and what it does not include

Two GraphQL pages returned **63 ACTIVE products** in total (50 + 13, `hasNextPage: false` on the second page — pagination is exhausted, not truncated). Of those 63, **45 carry `vendor: "Naira Petite"`** and sit in the **₹899–₹2,849** band; the other **18 carry `vendor: "My Store"` or `vendor: "Naira"`** and sit in the **₹9,500–₹55,000** band — the legacy couture clothing line, excluded per the task brief. The vendor field, not requested in the original field list, was added to the query specifically to make this split mechanical rather than judgement-based.

This comes in slightly under the brief's "roughly 51" jewellery SKUs and "roughly 72" active products. The gap is explained, not hand-waved: a supplementary query against 20 product titles that recur in this workspace's prior audit documents (`source_verification.txt`, `D-naira-audits.md`) — titles like *Classic Solitaire Ring*, *Granule Dome Ring*, *Halo Bloom Ring*, *Bold Nocturne Bracelet* — found **all twenty currently `DRAFT`**, not `ACTIVE`. The brief's rough counts most plausibly predate those items being unpublished. Every figure in this document reflects the store as it stood on 2026-08-19; none of it is backfilled from the older audit files, which are cited only where explicitly labelled as such.

Every one of the 45 active SKUs returned at least one image and at least some Details content, so the "no usable image" half of the Gaps section (§4) is empty — but four SKUs carry **no mm/cm figure anywhere in the listing**, confirmed by full-text search, not just the Details block. Those are listed in §4 rather than estimated.

## Contents
1. Summary table — all 45 SKUs
2. Fidelity-lock paragraphs, grouped earrings → necklaces → bracelets → rings → sets
3. Contradictions
4. Gaps

---

## 1. Summary table

| Handle | Title | SKU | Price (INR) | Category | Metal / plating | Key mm/cm figures | Inventory |
|---|---|---|---:|---|---|---|---:|
| `baguette-arc-hoops` | Baguette Arc Hoops | `WE14387B` | 2849.00 | Earrings | 18k gold tone | 20mm | 5 |
| `brushed-gold-huggies` | Brushed Gold Huggies | `E14776S` | 1449.00 | Earrings | 18k gold tone | 12mm, 6mm | 5 |
| `clover-trio-edit` | Clover Trio Edit | `JDE0201327` | 2749.00 | Earrings | 18k gold tone | 10.2mm, 8.5mm, 6.2mm, 3.7mm; 4.4g | 5 |
| `filigree-bloom-studs` | Filigree Bloom Studs | `YF8147` | 1949.00 | Earrings | 18k gold tone | 30mm, 29mm, 8mm; 4g | 5 |
| `molten-bloom-hoops` | Molten Bloom Hoops | `JDE0110042` | 1300.00 | Earrings | 18k gold tone | 21mm, 19mm, 4.7mm; 5.3g | 5 |
| `pearl-blossom-earrings` | Pearl Blossom Earrings | `E20997C` | 2299.00 | Earrings | Rhodium-plated silver tone | 18mm, 9mm | 5 |
| `pearl-drop-studs` | Pearl Drop Studs | `YF8333` | 1899.00 | Earrings | 18k gold tone | 30mm, 18mm | 5 |
| `pearl-halo-studs` | Pearl Halo Studs | `WE24089B` | 1399.00 | Earrings | 18k gold tone | 12mm, 5mm, 7mm | 5 |
| `pearl-point-studs` | Pearl Point Studs | `E19263B` | 2199.00 | Earrings | 18k gold tone | 16mm, 9mm | 5 |
| `ribbon-bow-earrings` | Ribbon Bow Earrings | `E16075B` | 2299.00 | Earrings | 18k gold tone | 15mm | 5 |
| `silver-drop-earrings` | Silver Drop Earrings | `E16676C` | 2449.00 | Earrings | Rhodium-plated silver tone | 40mm | 5 |
| `solitaire-whisper-studs` | Solitaire Whisper Studs | `E16355C` | 1899.00 | Earrings | Rhodium-plated silver tone | 12mm, 7mm | 5 |
| `textured-gold-hoops` | Textured Gold Hoops | `FE03586B` | 2200.00 | Earrings | 18k gold tone | 22mm, 6mm | 5 |
| `verdant-circlet-studs` | Verdant Circlet Studs | `FE02847B` | 1899.00 | Earrings | 18k gold tone | 20mm, 10mm, 6mm | 5 |
| `verdant-drop-earrings` | Verdant Drop Earrings | `E21572E1` | 1459.00 | Earrings | not stated as Plating (see notes) | 25mm, 9mm | 5 |
| `woven-gold-hoops` | Woven Gold Hoops | `E20267O` | 1799.00 | Earrings | 18k gold tone | 25mm | 5 |
| `baroque-pearl-lariat` | Baroque Pearl Lariat | `YF8457` | 2299.00 | Necklace | 18k gold tone | 1.5mm, 20mm, 6mm, 15mm | 5 |
| `charm-box-chain` | Charm Box Chain | `YF5146` | 2149.00 | Necklace | 18k gold tone | 50cm; 2.5mm, 10mm; 12.3g | 5 |
| `heartline-paperclip-necklace` | Heartline Paperclip Necklace | `YF3952` | 2449.00 | Necklace | 18k gold tone | not stated in listing | 5 |
| `marquise-layering-set` | Marquise Layering Set | `YF5244` | 1799.00 | Necklace | 18k gold tone | 40cm; 5mm, 1.2mm | 5 |
| `riviere-eternal-necklace` | Rivière Eternal Necklace | `YF7085-NEC` | 1799.00 | Necklace | 18k gold tone | 40cm; 12mm | 5 |
| `serpentine-whisper-chain` | Serpentine Whisper Chain | `YF8439` | 1849.00 | Necklace | Gold tone (PVD) | 40cm, 5cm; 2mm, 10mm; 10g | 5 |
| `toggle-link-chain` | Toggle Link Chain | `YF5143` | 1999.00 | Necklace | Gold tone (PVD) | 50cm; 4mm, 15mm; 12g | 5 |
| `baguette-eclat-bracelet` | Baguette Éclat Bracelet | `JDB201210` | 1549.00 | Bracelet | 18k gold tone | 16.5cm; 6mm; 7.5g | 5 |
| `baroque-bloom-cuff` | Baroque Bloom Cuff | `YF6671` | 1849.00 | Bracelet | Gold tone (PVD) | 6cm, 5.5cm, 1.8cm, 0.7cm, 0.25cm, 1.7cm; 1.5mm | 5 |
| `baroque-shell-bracelet` | Baroque Shell Bracelet | `YF3925` | 2049.00 | Bracelet | 18k gold tone | not stated in listing | 5 |
| `blush-station-bracelet` | Blush Station Bracelet | `JDB0103317-PK` | 1699.00 | Bracelet | 18k gold tone | 19cm, 5cm; 14mm, 3mm; 12.1g | 5 |
| `heartbead-bracelet` | Heartbead Bracelet | `YF5215` | 1399.00 | Bracelet | 18k gold tone | 6mm, 15mm | 5 |
| `pearl-reverie-bracelet` | Pearl Reverie Bracelet | `JDB2409013` | 999.00 | Bracelet | 18k gold tone | 19cm, 3cm; 8.4mm, 17mm; 11.3g | 4 |
| `prism-riviere-bracelet` | Prism Rivière Bracelet | `B00681C` | 1699.00 | Bracelet | Rhodium-plated silver tone | 18cm; 5mm | 5 |
| `ribbon-bead-bracelet` | Ribbon Bead Bracelet | `YF8156` | 899.00 | Bracelet | 18k gold tone | 16cm, 19cm; 1.2mm, 2mm, 5mm, 10mm, 5.5mm; 2g | 4 |
| `riviere-eternal-bracelet` | Rivière Eternal Bracelet | `YF7085` | 1449.00 | Bracelet | 18k gold tone | 18cm; 3mm, 12mm | 4 |
| `blush-cluster-ring` | Blush Cluster Ring | `WR10914B2` | 1999.00 | Ring | 18k gold tone | 5mm, 2.5mm | 5 |
| `chevron-whisper-ring` | Chevron Whisper Ring | `JDR0303312-7` | 1449.00 | Ring | 18k gold tone | 17.3mm, 9.5mm; 2g | 5 |
| `cushion-halo-ring` | Cushion Halo Ring | `WR20902K8` | 1199.00 | Ring | Rhodium-plated silver tone | 8mm, 12mm | 5 |
| `halo-curve-ring` | Halo Curve Ring | `YF8453` | 2049.00 | Ring | Gold tone (PVD) | 17mm, 1.5mm, 11.8mm; 4g | 5 |
| `pearl-ribbon-ring` | Pearl Ribbon Ring | `FR03136B` | 1099.00 | Ring | 18k gold tone | 10mm | 5 |
| `petite-pave-band` | Petite Pavé Band | `WR12518B` | 999.00 | Ring | 18k gold tone | not stated in listing | 5 |
| `rose-verdant-band` | Rose Verdant Band | `R18345A1` | 1999.00 | Ring | Rose gold tone | 4mm | 5 |
| `silver-dome-ring` | Silver Dome Ring | `JDR0104337-S` | 1499.00 | Ring | Rhodium-plated silver tone | 16.8mm, 15.7mm; 4.5g | 5 |
| `star-point-band` | Star Point Band | `YF5214` | 999.00 | Ring | Gold tone OR rhodium/silver tone (order-confirmed; single variant live) | not stated in listing | 5 |
| `verdant-eternity-band` | Verdant Eternity Band | `WR23024K` | 1899.00 | Ring | Rhodium-plated silver tone | 5mm by 4mm | 5 |
| `vintage-halo-ring` | Vintage Halo Ring | `WR23569K8` | 1299.00 | Ring | Rhodium-plated silver tone | 8mm by 6mm | 5 |
| `whisper-pave-band` | Whisper Pavé Band | `WR10170K7` | 899.00 | Ring | Rhodium-plated silver tone | 8mm, 12mm | 5 |
| `first-light-set` | First Light Set | `JDS0204301-set` | 1600.00 | Jewellery Set | 18k gold tone | 42cm, 5cm; 1mm, 5.8mm, 7.3mm | 5 |

---

## 2. Fidelity-lock paragraphs

Each paragraph follows the fixed shape: metal exactly as this listing's own Plating field states it (never inferred from the product name), every countable feature as a digit, and one named structural feature — the single detail a diffusion model is most likely to smooth away or substitute — locked explicitly against drift. Grouped earrings, necklaces, bracelets, rings, then the one jewellery set.

## Earrings (16 SKUs)

### Baguette Arc Hoops — `WE14387B`
Preserve the open hoop earring from reference 1 exactly: identical 18k gold tone plating, identical baguette cut clear cubic zirconia set flush in a channel the whole way round with no claws visible, same 20mm diameter, same open C-shaped gap at the front, same proportions, same lustre, same warm gold tone. Do not redesign, restyle, resize or add anything to the piece; the flush channel setting must stay a smooth unbroken band of rectangular stones, never grow prongs or round out into pavé. Only the background, surface and lighting change.

### Brushed Gold Huggies — `E14776S`
Preserve the huggie hoop from reference 1 exactly: identical 18k gold tone plating, identical 12mm diameter, identical 6mm deep flat band, zero stones, same soft brushed satin surface, same proportions, same huggie fitting, same warm gold tone. Do not redesign, restyle, resize or add anything to the piece; the brushed satin finish must stay matte and light-scattering, never turn into a smooth mirror-polished surface. Only the background, surface and lighting change.

### Clover Trio Edit — `JDE0201327`
Preserve all 3 pairs from reference 1 exactly as 3 separate items: identical 18k gold tone plating, identical clear cubic zirconia, huggie hoops at 10.2mm, detachable 4-petal clover charms at 8.5mm drop, clover studs at 6.2mm, round solitaire studs at 3.7mm, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize, merge or add anything to the pieces; the 3 pairs must stay 3 distinct, separable items, never collapse into one hoop-and-charm hybrid or a single pair. Only the background, surface and lighting change.

### Filigree Bloom Studs — `YF8147`
Preserve the stud earring from reference 1 exactly: identical 18k gold tone plating, identical 5-petal flower outline at 30mm across and 29mm tall, identical round white freshwater pearl of 8mm at the centre, same open radiating wirework, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the open filigree wire petals must stay pierced, negative-space openwork, never fill in into solid flat gold petals. Only the background, surface and lighting change.

### Molten Bloom Hoops — `JDE0110042`
Preserve the huggie hoop from reference 1 exactly: identical 18k gold tone plating, identical 21mm by 19mm size, identical 4.7mm band thickness, zero stones, same hinged snap closure, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the thick irregular band must stay rippled and molten, swelling and narrowing unevenly around the circle, never smooth out into a uniform round tube. Only the background, surface and lighting change.

### Pearl Blossom Earrings — `E20997C`
Preserve the stud earring from reference 1 exactly: identical rhodium plated silver tone, identical pave set bow of small clear zircons at the top, identical round shell pearl of 9mm in a warm champagne tone below, identical 18mm total height, same open circle of pave cradling the pearl, same proportions, same cool silver tone. Do not redesign, restyle, resize or add anything to the piece; the top motif must stay a two-loop bow silhouette, never round out into a plain pave cluster or disc. Only the background, surface and lighting change.

### Pearl Drop Studs — `YF8333`
Preserve the stud earring from reference 1 exactly: identical 18k gold tone plating, identical round white shell pearl at the lobe, identical polished gold sphere of 18mm suspended directly beneath it, identical 30mm total drop, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the lower element must stay one smooth solid polished sphere, never gain facets, texture, or shrink smaller than the pearl above it. Only the background, surface and lighting change.

### Pearl Halo Studs — `WE24089B`
Preserve the stud earring from reference 1 exactly: identical 18k gold tone plating, identical round clear cubic zirconia of 5mm in 4 plain claws, identical round white shell pearl of 7mm stacked directly beneath it, identical 12mm total height, same 2-tier stacked structure, same proportions, same gold tone. Do not redesign, restyle, resize or add anything to the piece; despite the product name, the stone must stay a single 4-claw-set solitaire with no halo, never gain a ring of pave stones around the stone or the pearl. Only the background, surface and lighting change.

### Pearl Point Studs — `E19263B`
Preserve the stud earring from reference 1 exactly: identical 18k gold tone plating, identical twisted gold rope circle frame at 16mm across, identical round white shell pearl of 9mm at the centre, identical 3 small clear zircons set into the rope, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the frame must stay a visibly twisted, braided rope texture, never smooth out into a plain round bezel, and the zircon count must stay 3, never 4. Only the background, surface and lighting change.

### Ribbon Bow Earrings — `E16075B`
Preserve the stud earring from reference 1 exactly: identical 18k gold tone plating, identical pear cut and tapered clear cubic zirconia set in fine gold claws, identical soft bow silhouette reading as one continuous curve, identical 15mm width, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the stones must stay pear cut and tapered in graduated sizes, never round out into uniform round brilliant stones. Only the background, surface and lighting change.

### Silver Drop Earrings — `E16676C`
Preserve the drop earring from reference 1 exactly: identical rhodium plated silver tone, identical 3 linked ovals ending in a flat open oval, identical baguette cut clear zircons on the lower oval, identical bar pave set with small round clear stones crossing the open oval, identical 40mm total drop, same proportions, same cool silver tone. Do not redesign, restyle, resize or add anything to the piece; the chain must stay exactly 3 linked ovals, never collapse into a single link or a plain drop. Only the background, surface and lighting change.

### Solitaire Whisper Studs — `E16355C`
Preserve the stud earring from reference 1 exactly: identical rhodium plated silver tone (not gold), identical round brilliant clear cubic zirconia of 7mm at the centre, identical cushion shaped pave halo surrounding it, identical 12mm square face, same proportions, same lustre, same cool silver tone. Do not redesign, restyle, resize or add anything to the piece; despite the product name, the halo must stay a full cushion shaped ring of pave stones, never strip away into a bare solitaire with no halo. Only the background, surface and lighting change.

### Textured Gold Hoops — `FE03586B`
Preserve the open half hoop from reference 1 exactly: identical 18k gold tone plating, identical alternating fluted gold discs of about 6mm each and clusters of small round clear cubic zirconia, identical 22mm diameter, same straight post fitting, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the surface must stay an alternating rhythm of disc-then-stone-cluster segments, never blur into one continuous pave band or one continuous fluted band. Only the background, surface and lighting change.

### Verdant Circlet Studs — `FE02847B`
Preserve the stud earring from reference 1 exactly: identical 18k gold tone plating, identical cushion cut emerald green cubic zirconia of 10mm over an open circlet of small clear cubic zirconia and gold points, identical white shell pearl of 6mm inside the circle, identical 20mm total height, same 3-tier structure, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the pearl nested inside the circlet must stay visible, never dropped or hidden behind the green stone. Only the background, surface and lighting change.

### Verdant Drop Earrings — `E21572E1`
Preserve the drop earring from reference 1 exactly: identical silver tone finish over a copper alloy body, identical cushion cut zircon of 9mm in vivid mint turquoise green, identical 4 plain claws on a plain open basket, identical curved bar of tiny clear zircons at the lobe, identical 25mm total drop. Do not redesign, restyle, resize or add anything to the piece; the green stone must stay bare in 4 plain claws, never gain a halo or surround of extra stones. Only the background, surface and lighting change.

### Woven Gold Hoops — `E20267O`
Preserve the hoop earring from reference 1 exactly: identical 18k gold tone plating, identical thick braided rope of gold strands, identical 25mm diameter, zero stones, same raised ridge-and-shadow woven texture, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the surface must stay a distinct braided rope of multiple gold strands, never smooth out into a single plain curved tube. Only the background, surface and lighting change.

## Necklaces (7 SKUs)

### Baroque Pearl Lariat — `YF8457`
Preserve the lariat necklace from reference 1 exactly: identical 18k gold tone plating, identical fine 1.5mm snake chain, identical open oval ring of 20mm, identical small round white shell pearl of 6mm held in the ring, identical large baroque white shell pearl of 15mm at the sliding end, same proportions, same lustre. Do not redesign, restyle, resize or add anything to the piece; the large terminal pearl must stay baroque, irregular and organically lumpy, never round out into a smooth spherical pearl. Only the background, surface and lighting change.

### Charm Box Chain — `YF5146`
Preserve the necklace from reference 1 exactly: identical 18k gold tone plating, identical fine 2.5mm gold box chain built from square links, identical 50cm length, identical cylindrical barrel rondelle charm of about 10mm pave set with many tiny clear cubic zirconia around its circumference, same proportions, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the chain links must stay square box-chain geometry, never round out into a curb or cable chain, and the charm must stay cylindrical, never flatten into a disc. Only the background, surface and lighting change.

### Heartline Paperclip Necklace — `YF3952`
Preserve the necklace from reference 1 exactly: identical 18k gold tone plating, identical fine gold paperclip links, identical small heart shaped clear cubic zirconia stations grouped only through the front centre section, identical plain chain along both sides, same proportions, same lustre. No length or stone size is stated in the listing; do not invent one. Do not redesign, restyle or add anything to the piece; the links must stay elongated rectangles, never a plain cable chain, and the hearts must stay clustered at the front, never spread along the whole length. Only the background, surface and lighting change.

### Marquise Layering Set — `YF5244`
Preserve both necklaces from reference 1 exactly as 2 separate pieces: identical 18k gold tone plating, the shorter a fine 1.2mm cable chain of 40cm with a single marquise cut zircon of 10mm by 5mm, the longer a Y-lariat scattered with marquise zircon stations of 5mm, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize, merge or add anything to the pieces; the longer chain must stay a Y-shaped split junction, never straighten into a single strand, and both necklaces must stay 2 distinct items. Only the background, surface and lighting change.

### Rivière Eternal Necklace — `YF7085-NEC`
Preserve the necklace from reference 1 exactly: identical 18k gold tone plating, identical round brilliant cut clear cubic zirconia of 3mm each, identical 40cm length, identical flat rectangular buckle station of 12mm at the front, same individual 4-claw settings linked directly stone to stone with no connecting chain wire, same proportions, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the stones must stay directly linked claw to claw, never gain a visible connecting chain or blur into a solid pave band. Only the background, surface and lighting change.

### Serpentine Whisper Chain — `YF8439`
Preserve the necklace from reference 1 exactly: identical 18k PVD gold tone plating, identical 2mm snake chain measuring 40cm plus a 5cm extender, identical single cushion cut clear cubic zirconia of 10mm in a fine gold basket setting at the front, same proportions, same lustre, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the chain must stay a finely ridged snake-link texture, never smooth out into a plain round cable or box chain. Only the background, surface and lighting change.

### Toggle Link Chain — `YF5143`
Preserve the necklace from reference 1 exactly: identical 18k PVD gold tone plating, identical 4mm chain width, identical 50cm length, identical gold toggle bar and ring clasp of about 15mm at the front, same proportions, same lustre, same gold tone, zero stones anywhere on the chain or clasp. Do not redesign, restyle, resize or add anything to the piece; the closure must stay a toggle bar that passes through a plain ring, never turn into a lobster clasp or a round push clasp. Only the background, surface and lighting change.

## Bracelets (9 SKUs)

### Baguette Éclat Bracelet — `JDB201210`
Preserve the bracelet from reference 1 exactly: identical 18k gold tone plating, identical rectangular step cut baguette clear cubic zirconia set upright in a continuous row, identical 16.5cm length, identical fine gold four-claw settings linked directly to one another, identical 6mm wide set line, same gold box clasp, same proportions. Do not redesign, restyle, resize or add anything to the piece; the stones must stay rectangular step cut baguettes standing upright, never round out into round brilliant cut stones. Only the background, surface and lighting change.

### Baroque Bloom Cuff — `YF6671`
Preserve the open cuff from reference 1 exactly: identical 18k PVD gold tone plating, identical 6cm by 5.5cm size on 1.5mm wire, one terminal an irregular white mother of pearl slab of 1.8cm by 0.7cm in a 0.25cm bezel, the other terminal a 1.7cm gold cap set with a clear emerald cut cubic zirconia, same proportions. Do not redesign, restyle, resize or add anything to the piece; the two terminals must stay different from each other, never mirrored into two matching ends. Only the background, surface and lighting change.

### Baroque Shell Bracelet — `YF3925`
Preserve the bracelet from reference 1 exactly: identical 18k gold tone plating, identical large irregular baroque shell pearls linked by small round gold beads between them, identical gold toggle bar and ring clasp, identical single baroque pearl drop hanging from the toggle ring, same proportions, same lustre. No length is stated in the listing; do not invent one. Do not redesign, restyle or add anything to the piece; the pearls must stay baroque and irregular, never round out, and the small drop pearl at the clasp must not be dropped. Only the background, surface and lighting change.

### Blush Station Bracelet — `JDB0103317-PK`
Preserve the bracelet from reference 1 exactly: identical 18k gold tone plating, identical marquise cut pale rose cubic zirconia stations of 14mm alternating with small round pink cubic zirconia of 3mm, identical 19cm length plus a 5cm extender, same individual fine gold bezel setting on every stone, same proportions, same lustre. Do not redesign, restyle, resize or add anything to the piece; each stone must stay fully rimmed in a smooth gold bezel, never gain visible claws or prongs. Only the background, surface and lighting change.

### Heartbead Bracelet — `YF5215`
Preserve the bracelet from reference 1 exactly: identical polished silver tone steel bead spheres of 6mm strung in short runs on fine silver links, identical gold tone toggle bar and ring clasp, identical single puffed gold tone heart of 15mm hanging from the ring, same proportions, same lustre. Do not redesign, restyle, resize or add anything to the piece; the strand must stay silver tone and the clasp and heart must stay gold tone, never unify into one single metal colour throughout. Only the background, surface and lighting change.

### Pearl Reverie Bracelet — `JDB2409013`
Preserve the bracelet from reference 1 exactly: identical 18k gold tone plating, identical broad elongated oval paperclip links, identical 2 irregular baroque freshwater pearls of 8.4mm each threaded into the run, identical 1 organic open gold link of 17mm between them, identical 19cm length plus a 3cm extender, same lobster clasp. Only the bracelet is sold; do not render the matching necklace anywhere in frame. Do not redesign, restyle, resize or add anything to the piece; the open link must stay uneven and hand-formed, never regularize into a perfect oval. Only the background, surface and lighting change.

### Prism Rivière Bracelet — `B00681C`
Preserve the bracelet from reference 1 exactly: identical rhodium plated silver tone, identical cushion cut pastel cubic zirconia of 5mm each framed by its own fine pave halo, identical 18cm length, identical fold over clasp, same continuous linked row, same proportions. Do not redesign, restyle, resize or add anything to the piece; the colour rotation must stay exactly 3 repeating colours — aqua blue, soft pink, pale yellow — never gain a fourth colour such as lilac. Only the background, surface and lighting change.

### Ribbon Bead Bracelet — `YF8156`
Preserve the bracelet from reference 1 exactly: identical 18k gold tone plating, identical fine 1.2mm cable chain dotted with 2mm gold satellite beads, identical 2 heart cut clear zircons of 5mm set side by side in fine gold claws forming a 10mm by 5.5mm bow motif, identical adjustable 16cm to 19cm length, same proportions. Do not redesign, restyle, resize or add anything to the piece; the centre must stay 2 distinct heart cut stones side by side, never merge into one stone. Only the background, surface and lighting change.

### Rivière Eternal Bracelet — `YF7085`
Preserve the bracelet from reference 1 exactly: identical 18k gold tone plating, identical round brilliant clear cubic zirconia of 3mm each, identical 18cm length, identical polished rectangular buckle station of 12mm at the front, same individual four-prong settings linked directly stone to stone, same proportions, same lustre. Do not redesign, restyle, resize or add anything to the piece; the stones must stay directly linked prong to prong, never gain a visible connecting chain between them. Only the background, surface and lighting change.

## Rings (12 SKUs)

### Blush Cluster Ring — `WR10914B2`
Preserve the ring from reference 1 exactly: identical 18k gold tone plating, identical round pink cubic zirconia of 5mm at the centre, identical 10 round pink cubic zirconia of 2.5mm surrounding it, identical 1 further small pink stone on the shoulder, same slim round shank, same proportions, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the surround must stay exactly 10 stones, never fewer such as 8, and the shoulder stone must stay exactly 1. Only the background, surface and lighting change.

### Chevron Whisper Ring — `JDR0303312-7`
Preserve the ring from reference 1 exactly: identical 18k gold tone plating, identical double-V chevron band with 2 fine pave lines of small round clear cubic zirconia meeting at a point, identical 17.3mm inner diameter, identical 9.5mm band height at the chevron, same proportions, same gold tone. Do not redesign, restyle, resize or add anything to the piece; the band must stay a sharp double-V point where the 2 pave lines meet, never soften into a rounded wave or a single continuous band. Only the background, surface and lighting change.

### Cushion Halo Ring — `WR20902K8`
Preserve the ring from reference 1 exactly: identical rhodium plated silver tone, identical round brilliant clear cubic zirconia of 8mm in 4 claws, identical cushion shaped pave halo of about 12mm as a single row around it, identical pave down both shoulders, same plain polished shank behind, same proportions. Do not redesign, restyle, resize or add anything to the piece; the halo outline must stay cushion shaped, never round out into a circle, and it must stay 1 single row, never double into 2 concentric rows. Only the background, surface and lighting change.

### Halo Curve Ring — `YF8453`
Preserve the ring from reference 1 exactly: identical 18k PVD gold tone plating, identical natural tiger eye of about 11.8mm beside a faceted pale champagne crystal, identical 17mm inner diameter on 1.5mm metal, same 2 separate irregular bezels each individually shaped to its own stone, same proportions. Do not redesign, restyle, resize or add anything to the piece; the tiger eye must stay opaque with banded chatoyant sheen, never turn transparent like the crystal, and the 2 bezels must stay unmatched and irregular, never regularize into 2 identical smooth cushion bezels. Only the background, surface and lighting change.

### Pearl Ribbon Ring — `FR03136B`
Preserve the ring from reference 1 exactly: identical 18k gold tone plating, identical bow formed from 2 flat gold loops channel set with rectangular baguette clear cubic zirconia, identical polished gold knot, identical round white freshwater pearl of 10mm resting to one side, same slim plain gold shank, same proportions. Do not redesign, restyle, resize or add anything to the piece; the pearl must stay offset to one side of the bow, never re-centre itself beneath the knot. Only the background, surface and lighting change.

### Petite Pavé Band — `WR12518B`
Preserve the ring from reference 1 exactly: identical 18k gold tone plating, identical 4 fine parallel bands with exactly 2 pave set with clear zircons and 2 left plain polished gold, crossing over each other at the front, identical 1 slightly larger clear zircon in 4 claws at the crossing point. No mm dimension is stated; do not invent one. Do not redesign, restyle or add anything; the split must stay exactly 2 pave and 2 plain, never shift to all 4 pave. Only the background, surface and lighting change.

### Rose Verdant Band — `R18345A1`
Preserve the ring from reference 1 exactly: identical rose gold tone plating, identical 4 fine parallel bands all 4 pave set with clear stones across the front and plain around the back, identical 4 round emerald green cubic zirconia of 4mm at staggered points, same open adjustable back, same proportions, same rose gold tone. Do not redesign, restyle, resize or add anything to the piece; all 4 bands must stay pave set at the front, never reduce to only 2 of the 4 bands pave. Only the background, surface and lighting change.

### Silver Dome Ring — `JDR0104337-S`
Preserve the ring from reference 1 exactly: identical rhodium plated silver tone (not sterling silver), identical broad rounded dome of 16.8mm long by 15.7mm wide, identical small clear zircons pave set across the entire dome surface, same heavy tapered open-back shank, same proportions, same cool silver tone. Do not redesign, restyle, resize or add anything to the piece; the pave coverage must stay total across the whole dome, never thin out to a partial or sparse scatter of stones. Only the background, surface and lighting change.

### Star Point Band — `YF5214`
Preserve the ring from reference 1 exactly: identical 18k gold tone plating (the gold-tagged version actually listed), identical wide flat band with repeating 4-pointed star motifs engraved in low relief, identical 1 small clear cubic zirconia centred on each star. No mm dimension is stated in the listing; do not invent one. Do not redesign, restyle, resize or add anything to the piece; each star must stay a flush low-relief engraving with exactly 1 small stone, never rise into a raised embossed star with 1 large solitaire at its centre. Only the background, surface and lighting change.

### Verdant Eternity Band — `WR23024K`
Preserve the ring from reference 1 exactly: identical rhodium plated silver tone, identical oval emerald green cubic zirconia of 5mm by 4mm claw set continuously all the way around the band, identical scalloped pave settings of small clear stones alternating between the green stones, same open adjustable back, same proportions. Do not redesign, restyle, resize or add anything to the piece; the settings between the green stones must stay scalloped and decorative, never flatten into plain straight metal links. Only the background, surface and lighting change.

### Vintage Halo Ring — `WR23569K8`
Preserve the ring from reference 1 exactly: identical rhodium plated silver tone, identical oval clear zircon of 8mm by 6mm inside a pave halo, identical shank that twists into a knot just beneath the setting, identical pave running along the twist, same proportions, same cool silver tone. Do not redesign, restyle, resize or add anything to the piece; the shank must stay visibly twisted into a knot beneath the stone, never straighten into a plain round band. Only the background, surface and lighting change.

### Whisper Pavé Band — `WR10170K7`
Preserve the ring from reference 1 exactly: identical rhodium plated silver tone, identical round brilliant clear zircon of 8mm in 4 claws at the heart of a cushion shaped pave halo of about 12mm square, identical pave down both shoulders, identical fine open gallery beneath the setting, same proportions. Do not redesign, restyle, resize or add anything to the piece; the gallery beneath the stone must stay open and pierced so light passes through, never fill in solid. Only the background, surface and lighting change.

## Jewellery Sets (1 SKU)

### First Light Set — `JDS0204301-set`
Preserve both pieces from reference 1 exactly as a 2-piece set: identical 18k gold tone plating, a pendant necklace on a fine 1mm chain of 42cm plus a 5cm extender with a round clear cubic zirconia of 5.8mm in a gold 4-prong setting, and matching studs of 7.3mm each, same proportions, same gold tone. Do not redesign, restyle or add anything; both pieces must stay present, and the studs must stay larger than the pendant stone, never shrink smaller than it. Only the background, surface and lighting change.

---

## 3. Contradictions

Method: every one of the 45 active SKUs was checked programmatically (title vs. tags vs. Details-block dimensions) and then read by hand, cross-checking metal family, stone counts, and any structural term in the title (solitaire, halo, dome, circlet, chevron…) against what the Details block actually describes. Nothing below is resolved silently — each row states what every field says and which one this pass treats as authoritative, with the reasoning.

A fifth row is included for **Classic Solitaire Ring**, the example the task brief itself named. It is **not** one of the 45 active SKUs — a live query confirms it is currently `DRAFT` — so it sits outside the fidelity-lock library above, but it is documented in full because it was pre-flagged and because it is the clearest four-way contradiction found anywhere in this catalogue.

| # | SKU / Title | Field | What it says | Authoritative? |
|---|---|---|---|---|
| 1 | `WR19333K8` — **Classic Solitaire Ring** (status: **DRAFT**, not in the active 45) | Title | "Classic Solitaire Ring" — a solitaire has one stone, no shoulder ornament | — |
| | | Description, opening line | *"The classic, in silver."* and "a round brilliant solitaire in a four-prong **silver-tone** setting on a **plain** band" | Contradicted by the next field |
| | | Description, "The making" bullets | *"18k **gold**-plated 316L stainless steel"* | Agrees with tags and images |
| | | Tags | `18k Gold Tone Plated` | Agrees with "the making" + images |
| | | Image alt text (×2) | *"a five-millimetre round zircon in **gold** claws above **stepped pavé shoulders**"*; *"the shoulders stepping down in **zigzag pavé** panels"* | Agrees with gold; contradicts "plain band" |
| | | **Verdict** | **Gold** is authoritative for metal — two independent signals (tags, both image alt-texts) agree, against one stray "in silver" sentence that reads like copy carried over from a different draft. **Pavé shoulders** are authoritative over "plain band" — both image alt-texts independently describe stepped/zigzag pavé shoulders, and a title-vs-body-vs-image split this clean only resolves toward the images. The title "Classic Solitaire Ring" is itself the least reliable field here: a piece with pavé shoulder panels is not a solitaire in the technical sense. | |
| 2 | `E16355C` — **Solitaire Whisper Studs** (active) | Title | "Solitaire" — implies one bare stone, no halo | Contradicted |
| | | Details → Halo | "Cushion shaped pave halo of small clear cubic zirconia" | Authoritative |
| | | Details → Plating | "Rhodium plated silver tone" | Authoritative (confirms not gold) |
| | | **Verdict** | The Details block is authoritative: this is a cushion-halo stud in rhodium, not a solitaire, and not gold. The title is a marketing name, not a technical spec, and should not be trusted for structure or metal. This is the exact pattern named in the task brief. | |
| 3 | `WE24089B` — **Pearl Halo Studs** (active) | Title | "Halo" — implies a ring of small stones surrounding a centre stone | Contradicted |
| | | Details → Stone | "Round clear cubic zirconia, approximately 5mm, four claw set" — no halo language anywhere in the Details block | Authoritative |
| | | Details → Pearl | "Round white shell pearl, approximately 7mm" stacked beneath the stone | Authoritative |
| | | **Verdict** | The Details block is authoritative: this is a plain 4-claw stone stacked over a pearl, with no halo. This matches a prior supplier-photo verification pass in this workspace (`source_verification.txt`), which flagged the same title as imprecise for the same reason — the issue is still live in the current copy, it was never fixed. | |
| 4 | `YF5214` — **Star Point Band** (active) | Details → Plating | "18k gold tone plated **or** rhodium plated silver tone, confirmed at order" — copy describes a colourway choice | Partially contradicted |
| | | Tags | `18k Gold Tone Plated` only — no `Silver Tone` tag | — |
| | | Variants | A single variant, one SKU (`YF5214`), one price — no colour option exists to select | Authoritative |
| | | **Verdict** | The live variant structure is authoritative: only the gold version is actually sold under this listing, so the "or rhodium plated silver tone" clause in the copy describes an option that does not exist at checkout. The fidelity-lock paragraph above is written to the gold version because that is what a buyer actually receives. This SKU also carries zero mm figures anywhere in the listing (see Gaps). | |
| 5 | `FE02847B` — **Verdant Circlet Studs** (active, minor) | Details → Pearl | "White shell pearl, approximately 6mm, inside the circlet" — a pearl is explicitly present | — |
| | | Tags | No `Pearl` tag, despite every other pearl-bearing SKU in the catalogue carrying one | Contradicted |
| | | **Verdict** | The Details block is authoritative — the pearl is real and stated with a size. This is a tagging omission, not a factual error, but it means storefront filtering ("shop by pearl") would silently exclude this SKU. Flagged for the merchandising team, not for the fidelity-lock prompt itself. | |

### A note on scope: SKU/title reassignment since the prior audit

This workspace already holds an earlier supplier-photo verification pass (`source_verification.txt`, `D-naira-audits.md`) that flagged **Baguette Éclat Bracelet** as a "wrong product" — supplier photo a fine cable-chain bracelet, listing selling a baguette tennis bracelet — under SKU `JDB201083`. In the current live pull, `JDB201083` now belongs to a **different, draft** product titled **Rivière of Light Bracelet**, and the SKU actually live under **Baguette Éclat Bracelet** today is `JDB201210`, whose current copy is internally consistent (baguette stones, four-claw settings, box clasp — no mismatch found). SKU-to-title assignment has shifted since that audit ran. The old finding should not be read as still applying to the bracelet currently sold as "Baguette Éclat Bracelet" — it applied to a code that now sits under a different, unpublished listing. This is stated explicitly rather than silently carried forward or silently dropped.

Twenty product titles that recur heavily in this workspace's prior audit documents (`Classic Solitaire Ring`, `Granule Dome Ring`, `Halo Bloom Ring`, `Duet of Dawn Ring`, `Golden Duet Ring`, `Trio Bloom Ring`, `Scatter Light Band`, `Teardrop Lariat`, `Bold Nocturne Chain`, `Bold Nocturne Bracelet`, `Dewdrop Bezel Necklace`, `Clover Charm Necklace`, `Petite Pearl Chain`, `Pearl Legacy Necklace`, `Peach Heart Hoops`, `Star Fall Drop Earrings`, `Rivière of Light Bracelet`, `Verdant Rivière Bracelet`, `Triple Dawn Cuff`, `Whisper Twist Cuff`) were checked directly against the live store for this report. **All twenty are currently `DRAFT`**, confirming they sit outside the ACTIVE catalogue this task scopes to. They are not included in the fidelity-lock library above and their older, pre-this-pull defect findings are not re-asserted here as current — only re-verification against a live listing would confirm whether those specific defects still hold.

---

## 4. Gaps

### No dimension figures at all in the listing

Confirmed by full-text search across `descriptionHtml` (intro paragraph, styling tip, Details block and Care block) — not just the Details bullets — so these are genuine absences, not parser misses:

| SKU | Title | What the listing does state instead |
|---|---|---|
| `YF3952` | Heartline Paperclip Necklace | Link style (paperclip), stone shape (heart), placement (front centre only), plating, material — no length, no stone size |
| `YF3925` | Baroque Shell Bracelet | Pearl shape (baroque, irregular), closure (toggle bar and ring), plating, material — no bracelet length, no pearl size |
| `YF5214` | Star Point Band | Motif (repeating 4-point star, low relief), stone placement (one per star), plating (dual, see Contradictions #4) — no band width, no stone size |
| `WR12518B` | Petite Pavé Band | Band count (4, split 2 pavé / 2 plain), size range (US 6–8) — no mm figure for width, stone size or band thickness |

For all four, the fidelity-lock paragraph above states the structural facts that are present and explicitly does not invent a millimetre figure. Where a paragraph needed a size word at all, it used the listing's own qualitative language ("fine," "small," "wide flat band") rather than a fabricated number.

### No usable image

None by the literal test: all 45 active SKUs returned at least one `images` edge with a populated `url`, so no SKU was excluded from the fidelity-lock library for lack of an image.

A related, narrower gap: **14 of the 45** SKUs carry at least one image with an **empty `altText`** (`""`) alongside their other, captioned images — `Toggle Link Chain`, `Molten Bloom Hoops`, `Pearl Point Studs`, `Pearl Reverie Bracelet`, `Baroque Bloom Cuff`, `Baroque Shell Bracelet`, `Baguette Éclat Bracelet`, `Blush Station Bracelet`, `Prism Rivière Bracelet`, `Heartbead Bracelet`, `Ribbon Bead Bracelet`, `Star Point Band`, `Halo Curve Ring`, `Vintage Halo Ring`. One SKU, **`Blush Station Bracelet` (`JDB0103317-PK`), has empty `altText` on *both* of its two images** — the URLs load, but nothing in the API response names what either frame shows; every fact used for its fidelity-lock paragraph above therefore comes from the text fields (Details block, intro paragraph), not from any image description.

### Structural/field-naming outlier

`E21572E1` (Verdant Drop Earrings) does not use this catalogue's standard `Plating:` / `Material:` label pair at all — its Details block instead carries `Ear post: 925 sterling silver` and `Body: Copper alloy with zircon inlay, finished in silver tone`. This is not a contradiction (nothing disagrees; the tags — `Silver Tone`, `Sterling Silver Posts`, `Zircon` — match this exactly), but it is the one listing in the active 45 that does not fit the field-extraction pattern used everywhere else, so it is called out rather than silently normalised. The fidelity-lock paragraph above sources its metal description from `Body` and `Ear post`, not from a `Plating` field, because none exists on this listing.

### Price-band and count calibration

The brief described the jewellery band as ₹899–₹2,749. The live pull's actual ceiling is **₹2,849** (`Baguette Arc Hoops`, `WE14387B`) — ₹100 above the brief's figure. This is stated as observed rather than silently rounded down to fit; it does not affect which SKUs were included, since the same 18 couture SKUs at ₹9,500+ remain the only exclusions and there is no product priced in the ₹2,750–₹9,499 gap between the two tiers.
