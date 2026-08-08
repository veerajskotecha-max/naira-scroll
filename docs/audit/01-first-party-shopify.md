# FIRST-PARTY DATA — Naira (nairaflore.com) — pulled 2026-08-08

Source: live Shopify Admin API (store `nc5eti-gp.myshopify.com`, plan Basic, INR, IST, India)
and Meta Ads API (account 903466039148509 "naira flore meta ads", business `nairaflore.meta`).
Everything below is measured, not estimated.

## THE FUNNEL (last 90 days)

| Metric | Value |
|---|---|
| Sessions | 5,482 |
| Sessions with cart additions | **2** |
| Sessions that reached checkout | 14 |
| Sessions that completed checkout | **0** |
| Conversion rate | **0.0%** |
| Orders (90d) | **0** |
| Revenue (90d) | **₹0** |
| Cart-add rate | **0.036%** (norm 5–10%) |

Lifetime (365d): **3 orders, ₹90,000** → AOV ₹30,000. Those are couture clothing orders, not jewellery.

## TRAFFIC SHAPE

| Dimension | Data |
|---|---|
| Device | mobile 5,452 / desktop 28 / other 2 → **99.5% mobile** |
| Referrer | social 5,368 / direct 106 / unknown 5 / search 3 → **97.9% social**, organic search ≈ 0 |
| Timing | week of 2026-05-11: **5,460 sessions**. Every other week in the 90d window: 0–10. |
| Current run-rate | ~10 sessions/week |

**Landing pages (90d):**
| Path | Sessions | Completed checkout |
|---|---|---|
| /collections/all | **4,881 (89%)** | 0 |
| / | 249 | 0 |
| /products/midnight-eclat | 41 | 0 |
| /products/tangerine-bloom | 34 | 0 |
| /products/heritage-mosaic | 32 | 0 |
| /products/lilac-whisper | 31 | 0 |
| /products/11000 | 30 | 0 |
| /products/blush-of-dawn | 24 | 0 |

Every product page that received traffic is a **legacy couture CLOTHING** SKU. Zero jewellery PDP traffic.

## CATALOGUE STATE

| Metric | Count |
|---|---|
| Total products | 87 |
| Active | 72 |
| Draft | 15 |
| Archived | 0 |
| Active but out of stock | 4 |
| Collections | 8 |

**Collections:** Home page (18), DUSK (18), Shop All (68), Necklaces (13), Earrings (20), Bracelets (15), Rings (19), **Sets (1)**.

### Two catalogues are merged into one storefront
- **Jewellery** — vendor `Naira Petite`, created 2026-08-06/07 (2 days old), price band **₹899–₹2,749**.
- **Couture clothing** — 18 SKUs still ACTIVE, vendor `My Store` (Shopify default placeholder, 12 SKUs) or `Naira` (6 SKUs), created Sep–Oct 2025, price band **₹9,500–₹55,000**, mostly inventory = 1.

Legacy clothing still live: Blush of Dawn ₹44,000 · Ethereal Lilac ₹33,000 · Royal Enigma ₹24,000 · Amber Bloom Set ₹48,000 · Amber Radiance ₹49,000 · Golden Blossom ₹41,000 (0 stock) · Midnight Bloom ₹18,000 · Ivory Whisper Co-ord ₹12,000 · Sunset Reverie ₹16,000 · Lilac Whisper ₹19,500 · Crimson Legacy Set ₹47,000 · Heritage Mosaic ₹32,000 · Noir Mela ₹9,500 · Tangerine Bloom ₹42,000 · Gulaal mirage ₹11,000 · Midnight Éclat ₹48,000 · Nocturne Veil ₹55,000 · Celeste Bloom ₹29,000 (0 stock).

→ `/collections/all` (89% of all landings) shows a ₹899 bracelet beside a ₹55,000 lehenga. **61x price spread on the first screen.**

### Active + out of stock (live, unbuyable)
Golden Blossom ₹41,000 · Celeste Bloom ₹29,000 · Star Fall Drop Earrings ₹1,799 · Petal Pearl Drop Studs ₹2,499

## DATA-INTEGRITY DEFECTS

**Title ≠ handle ≠ SEO title** (renamed products, handles/SEO never updated). Wrong name gets indexed; URL contradicts the page:
| Displayed title | URL handle | SEO title |
|---|---|---|
| Baguette Arc Hoops | `clover-bloom-studs` | Clover Bloom Studs |
| Baroque Shell Bracelet | `pearl-legacy-bracelet` | Pearl Legacy Bracelet |
| Blush Cluster Ring | `blush-halo-ring` | Blush Halo Ring |
| Teardrop Lariat | `pearl-ceremony-set` | — |
| Verdant Circlet Studs | `emerald-cluster-studs` | — |
| Granule Dome Ring | `amber-dome-ring` | — |

Others:
- Junk handle in the wild: `/products/11000` (30 sessions).
- Legacy SKUs have **null SEO title/description** and carry `shopify/fabric` metafields (fabric — on a jewellery store).
- Two metafield regimes: jewellery has `global/title_tag` + `mm-google-shopping/*` + `mc-facebook/google_product_category`; legacy has `reelfy/productVideos` and no feed fields → inconsistent product feed = catalogue-ad disapprovals.
- Vendor `My Store` (Shopify default) on 12 live products.
- Image depth uneven: some PDPs 5 images, "Blush of Dawn" has **1**.
- Ships to 29 countries (US, GB, AE, SG…) on Basic plan with 0 orders.

## BRAND ARCHITECTURE CONFUSION
Four names for one thing: Shopify store name **"Naira"** · domain **nairaflore.com** · product vendor **"Naira Petite"** · dossier collection **"The Gilded Hour"**.

## DOSSIER vs REALITY

| Dossier claim | Reality |
|---|---|
| Collection "The Gilded Hour", 66 SKUs | Live line is **"Naira Petite"**; 87 products, 72 active. No SKU named "The Vow"/"The Halo"/"The Whirl" exists. |
| Price range ₹1,299–₹8,999 | Actual jewellery **₹899–₹2,749** |
| Target AOV ₹3,200 | **Impossible single-item** — top jewellery SKU is ₹2,749. Needs 2+ units/order. |
| Baseline ROAS 3.5x by M3–6 | Store has done **0 jewellery orders**; no conversion baseline exists |
| SKU names (Vow, Halo, Whirl, Vine, Dew Ring, Toi et Moi, Chevron Stack…) | None present in catalogue |

The dossier describes an aspirational brand that does not match the live store.

## META ADS ACCOUNT

Account `903466039148509` "naira flore meta ads" (business `nairaflore.meta`) — ACTIVE, payment method
attached, INR, min daily budget ₹97.09. Vertical returned by Meta: **Ecommerce / Apparel and Accessories**.
A second account `1498422677060515` is also ACTIVE with a payment method.

**25+ ad creatives exist, every one created 2026-05-27, every one still status ACTIVE.** Creative names:

| Creative name pattern | Count in first page | What it sells |
|---|---|---|
| `{{product.name}}` | 14 | Dynamic catalogue / Advantage+ product ads |
| `Luxury Designer Couture` | 8 | **The old couture clothing line** |
| `Naira` | 3 | Brand |
| `Make Every Occasion Grand` | 1 | **Occasion wear / clothing** |

Two problems, both live right now:
1. **The active creative still sells couture** ("Luxury Designer Couture", "Make Every Occasion Grand") while
   the business has pivoted to ₹899–₹2,749 demi-fine jewellery. The messaging is one business model behind.
2. The `{{product.name}}` dynamic ads pull from a product catalogue that still contains the ₹9,500–₹55,000
   clothing SKUs, so DPA can serve a ₹55,000 lehenga to a jewellery audience.

Timing note: creatives are dated 2026-05-27, but the 5,460-session burst was the week of **2026-05-11** —
it predates them. Sessions after 27 May run 0–10/week, so these ACTIVE creatives are either not delivering
(no budget above them) or delivering negligibly.

### GAP — spend and ROAS unread
`ads_get_ad_entities` fails server-side at every level: Meta returns `Object with ID '5'/'6'/'7' does not
exist`, an incrementing internal object-id bug in the MCP layer, not a parameter error.
**Spend, impressions, CTR, CPM and ROAS are UNVERIFIED.** Read them in Ads Manager directly.
