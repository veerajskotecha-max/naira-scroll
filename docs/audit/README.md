# Naira Petite — Pre-Launch Audit

Measured 8 August 2026. Six brands scored on eight dimensions from raw HTML, real product
imagery, and first-party Shopify data.

Full report (published artifact): https://claude.ai/code/artifact/de1316d5-f742-40af-911d-b471bef5c7f7

## Scoreboard

| Brand | Overall |
|---|---|
| GIVA | 7.4 |
| Klissaa | 7.3 |
| Palmonas | 6.2 |
| Rubans | 5.8 |
| **Naira Petite** | **4.8** |
| Zaisha | 4.3 |

| Dimension | GIVA | Klissaa | Palmonas | Rubans | Naira | Zaisha |
|---|---|---|---|---|---|---|
| Mobile UX | 7.5 | 7.0 | 6.0 | 6.0 | 6.0 | 5.0 |
| Performance | 8.0 | 8.0 | 3.0 | 5.0 | 5.0 | 3.0 |
| PDP / CRO quality | 7.0 | 6.0 | 6.0 | 8.0 | 3.0 | 5.0 |
| Trust & social proof | 7.0 | 5.0 | 6.0 | 5.0 | 2.0 | 6.0 |
| Product photography | 8.0 | 9.0 | 8.5 | 8.0 | 6.0 | 3.0 |
| Brand story | 8.0 | 8.0 | 7.5 | 5.0 | 4.0 | 4.0 |
| Design / visual identity | 7.5 | 8.0 | 7.5 | 6.0 | 6.0 | 4.0 |
| Pricing architecture | 6.0 | 7.0 | 5.0 | 3.0 | 6.0 | 4.0 |

Naira Petite is scored on design, photography, PDP readiness and pricing — **not** on realised
conversion. The line has not been shown to traffic.

## Headline finding

24 of 25 probed SKUs already have an on-body (`_2_worn`) image uploaded to the Shopify CDN.
Only 4 of 50 active jewellery products use it as the hero. **96% own the asset, 8% use it.**
Zero cost to fix, no reshoot. This is the axis Klissaa wins photography on (9/10) and Zaisha
loses it on (3/10, zero on-body context anywhere).

## Ranked fixes

1. Delete the fake-review generator and fake urgency popups — `CustomerReviews.tsx:27-28,158-193`, `UrgencyNotification.tsx:11-18`
2. Flip every jewellery hero to the on-body shot (~50 SKUs)
3. Wire up the three dead capture forms — `ContactUs.tsx:36-41`, `Footer.tsx:154-156`
4. Fix the four dead PDP CTAs — `ProductDetails.tsx:224-241,340-362`
5. Populate `productType`/tags so category filters stop returning empty grids
6. Apply `shopifyImage()`/lazy-loading in `ProductGallery.tsx:79,112-117` (6 MB source PNGs)
7. Prune `sitemap.xml` — ~48 listed URLs resolve to 404
8. Consolidate the 7-SKU capsule and the ~52 checkout-ready SKUs into one branded line
9. Fix catalogue data defects (title/handle/SEO mismatches, 0-stock actives, 15 drafts)
10. Fix the placeholder WhatsApp number and two WCAG contrast failures (1.95:1, 1.96:1)
11. Add `quantityAvailable` to Storefront queries for real numbered scarcity
12. Claim unclaimed ground: `aggregateRating`, UPI/COD badges, size guide, founder schema
13. Tokenize the palette — `tailwind.config.ts`/`index.css` still hold stock shadcn defaults

## Files

| File | Contents |
|---|---|
| `00-scope.md` | Scope ruling — what is excluded from scoring and why |
| `01-first-party-shopify.md` | Catalogue state, pricing, data defects, dossier-vs-reality |
| `02-imagery.md` | On-body vs supplier-plinth analysis, 10 images viewed, file weights |
| `03-storefront-tech.md` | SPA/canonical/SEO findings, bundle weights |

## Method and limits

Competitor data is raw HTML fetched with a mobile Safari UA, plus product images downloaded and
viewed. Headless Chromium is blocked in this environment (curl reaches every host; the browser
gets connection-reset regardless of proxy config), so there are **no live screenshots** and
anything injected client-side is reported as "not found in fetched HTML", never as confirmed
absent. No Lighthouse or real paint timings were taken.

Ads, the couture clothing line, and pixel/tracking are excluded from all scoring per the brand's
instruction — they are pre-pivot artefacts of a different business.
