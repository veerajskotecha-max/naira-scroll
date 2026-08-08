# IMAGERY AUDIT — Naira Petite — 10 real CDN images downloaded and viewed, 2026-08-08

## THE HEADLINE: the best asset is already paid for and sitting unused

Probed 25 live SKUs for a `_2_worn` (on-body) file on the Shopify CDN:

| Result | Count |
|---|---|
| **Have an on-body image uploaded** | **24 / 25 (96%)** |
| Missing | 1 (YF8453) |

Now counted how many jewellery PDPs actually *lead* with that on-body image (featured/hero) across 50 active `Naira Petite` products:

| Hero image type | Count | Share |
|---|---|---|
| `_2_worn` (on-body) | 4 | **8%** |
| `_1_main` (still-life on plinth) | 46 | **92%** |

The four leading with on-body: Toggle Link Chain, Pearl Blossom Earrings, Prism Rivière Bracelet, Star Point Band.

→ **96% of the catalogue owns an on-body hero. 8% uses it.** Zero shoot cost, zero new assets, one bulk
reorder of media. This is the single cheapest conversion lever in the audit.

## THREE VISUAL LANGUAGES IN ONE CATALOGUE

### 1. Supplier plinth still-life — 92% of heroes
Viewed `E19269B_1_main.jpg` (Petal Pearl Drop Studs), `WR12518B`, `WR10914B2`, `YF8396`, `JDS0204301`.
Cream/beige seamless backdrop, white plaster cube plinth, soft warm key from upper left, shallow depth of field.
Honestly *competent* — better than typical factory catalogue work. Gold reads warm and rich, not brassy;
the CZ holds sparkle without blowing out.
**But**: filenames are raw supplier SKU codes (`E19269B`, `WR12518B`, `JDR0104337-PS`). This is the manufacturer's
own catalogue photography — the same frames almost certainly appear on competitor storefronts sourcing the same
Yiwu/Guangzhou catalogue. It cannot carry a premium, differentiated brand, because it isn't exclusive.
At mobile grid size the product occupies ~35% of frame with heavy negative space — small items read as tiny.

### 2. Higgsfield AI-generated stills — on DRAFT products
Viewed `hf_20260806_170242_*.png` (Classic Solitaire Ring) and `hf_20260806_182909_*.png` (Trio Bloom Ring).
**These are good.** Art direction matches the supplier plinth set almost exactly — same beige seamless,
same white plaster cube, same warm directional light, same shallow DOF. Someone deliberately matched the house look.
The gold on the Trio Bloom reads convincingly; prong geometry and pear/marquise facets hold up at full size.
Two problems:
- **File weight: 4.96 MB and 5.89 MB PNGs.** Photographic content stored as PNG. 8–10× a comparable WebP.
- Both sit on **DRAFT** products, so the best-controlled imagery in the catalogue is invisible to customers.
- Data defect: "Classic Solitaire Ring" — image shows silver-tone, description says "The classic, in silver…
  silver-tone setting", but the product tags say **"18k Gold Plated"**. Tag contradicts both image and copy.

### 3. On-body campaign shoot — the actual brand asset (only 8% of heroes)
Viewed `YF5214_2_worn.jpg` (Star Point Band) and `B00681C_2_worn.jpg` (Prism Rivière Bracelet).
One cohesive shoot: same Indian model, warm brown skin, marigold/saffron satin slip, soft white background,
natural window light, cropped mid-face (chin to collarbone) so the jewellery is the subject.
**This is the strongest thing the brand owns.** It does three jobs the plinth stills cannot:
- Shows scale on a real hand/wrist — the #1 unanswered question in demi-fine.
- Shows the metal against **Indian skin**, which is the actual customer. Gold-on-brown-skin is a different
  colour relationship than gold-on-white-plinth, and it flatters.
- Reads instantly at mobile thumbnail size — skin + fabric + metal gives contrast a beige-on-beige still cannot.
The saffron slip against warm brown skin and gold is a genuinely good colour decision and is repeatable as a
house signature.

## FILE-WEIGHT PROBLEM (store is 99.5% mobile)

| Asset class | Format | Typical weight |
|---|---|---|
| On-body worn (newer) | JPG | 143–200 KB ✅ |
| On-body worn (older) | **PNG** | **1.43–1.60 MB** ❌ |
| Supplier hero | PNG | ~1.1 MB ❌ |
| Supplier hero | JPG | 75–249 KB ✅ |
| Higgsfield AI | **PNG** | **4.96–5.89 MB** ❌❌ |

Format is inconsistent within the same asset class — some worn shots are 150 KB JPG, others 1.5 MB PNG for
the same kind of picture. Every photographic PNG should be WebP/JPG. Shopify's CDN can serve resized variants,
but oversized PNG sources still inflate transfer on themes that request near-original widths, and they slow
every admin/feed/ad-catalogue operation that pulls the original.

## VERDICT
Photography is not the brand's weakness — it has one genuinely strong, on-brand, customer-accurate asset class.
The weakness is **merchandising of the assets it already owns**: the differentiated on-body shoot is hidden
behind commodity supplier stills that any competitor can also use.
