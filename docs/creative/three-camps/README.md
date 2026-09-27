# Three Camps in Bloom — Pigment, The Long Afternoon, The Bench

Three earlier camps re-dressed one after another with the brand's own florals, taken from the site: the six vector rose
petals of the homepage (HeroPetals), the painted bloom, the watercolour sprig, the line vine, the flat brand flower, the
floral wallpaper and the gold embroidery photograph. Every plate was verified against its listing and its photographs
before anything was drawn on it. Feed 1080×1350 and story 1080×1920 for every card; names and prices read from Shopify
at build time; every figure printed exists in that SKU's listing; every card carries nairaflore.com.

Artifact: https://claude.ai/artifact/YMzPKFTDB9E5RWSDH1BKEn

| Camp | Device | Lead card | Hero-stock cards |
|---|---|---|---|
| A · Pigment | the colour field is the card; the photo through a petal-shaped window; petals tinted from the pigment | LILAC. (the purple one) | PASTEL., CORNFLOWER. |
| B · The Long Afternoon | herbarium specimen sheets: mounted plate, sprig and vine pressed across the corners, ruled label, referent named botanically | Specimen 01, the braided hoop | 01 hoops, 05 chain |
| C · The Bench | a painted bloom left on the bench, petals with the bench's shadow, the embroidery as the cloth edge, the tool as headline | THE CALLIPER. | THE CALLIPER. |

## What the award research changed
Cannes Lions 2025 print winners (Penny Price Packs, Faber-Castell, Dove, Stella Artois, Oreo, Colgate) reward one idea
per frame, type that is the message, craft that borrows another medium, residue and texture over polish, and restraint
with negative space; the Cartier system runs on a few repeated parts. Applied here: one graphic idea per camp, the
colour name as the whole headline in Pigment, the herbarium borrowing the botanist's craft, powder residue and fallen
petals as texture, a repeated label and stamp system, and the same top bar and foot across all fifteen cards.

## Stock notes
Pigment: four plates passed over (Verdant Eternity 2 units, Blush Station 0, Molten Bloom 0, Rose Verdant 1).
Long Afternoon: five plates passed over (solitaire studs 1, gold serpentine, baguette bracelet, pearl reverie, molten
hoop all inactive); the Toggle Link Chain was generated on khadi to complete the set.
Bench: four plates passed over (wax, buff, bench pin, wrist — inactive SKUs); the loupe frame is cropped so a one-unit
stud is out of the picture.

Each set folder holds `feed/`, `story/`, two contact sheets and `build/` (the set module, notes, and for Pigment the
floral toolkit `flora.py` with `petals.json` and the asset folder). The shared build system lives in
`../night-shift/core.py`; `artifact.py` here builds this page.
