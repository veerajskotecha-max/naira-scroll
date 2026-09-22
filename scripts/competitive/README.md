# Competitive pricing, Naira Flore vs Palmonas

Tooling for pulling both catalogues live and pricing the basket each
brand's offer is built to create. Run from the repo root; no install,
no keys, Node 22's built-in `fetch` is all any of it needs.

```sh
node scripts/competitive/scrape-catalogue.mjs www.palmonas.com      /tmp/pal.json
node scripts/competitive/scrape-catalogue.mjs nc5eti-gp.myshopify.com /tmp/ours.json
node scripts/competitive/compare.mjs /tmp/pal.json /tmp/ours.json
node scripts/competitive/verify-offers.mjs BUY2 NAIRA10
```

`compare.mjs --json` emits the same figures as machine-readable output;
`data/palmonas-2026-09-21.json` is that output from the 21 Sep 2026 run,
and `data/type-audit-skus.json` is the 85-SKU Type Audit range parsed out
of the PDF. Both are small enough to keep in the repo, the raw Palmonas
dump (39 MB) is not, so re-scrape rather than committing it.

## What the 21 Sep 2026 run found

**Scale.** Palmonas list 9,005 products / 20,742 variants; 6,007 of them
are demi-fine pieces in our five categories. We list 55 jewellery SKUs
(plus 18 couture pieces, which are not in this market and are excluded
from every figure below).

**We list cheaper and sell dearer.** Our median jewellery list is ₹1,499
against ₹2,229 for the products Palmonas puts B1G1 on, 33% below them.
But per piece, on a two-piece basket:

| basket | ours (BUY2) | their B1G1 | their 2/₹1,899 | their 4/₹2,999 |
| ------ | ----------- | ---------- | -------------- | -------------- |
| 1      | ₹1,499      | ₹2,229     | ₹1,111         | ₹1,111         |
| 2      | ₹1,349      | ₹1,115     | ₹950           | ₹1,111         |
| 3      | ₹1,349      | ₹1,486     | ₹1,003         | ₹1,111         |
| 4      | ₹1,349      | ₹1,115     | ₹950           | ₹750           |

We are +21% on their B1G1 and +42% on their fixed two-piece bundle. The
gap is the offer, not the price.

**`BUY2` is live at 10%, not 20%.** `verify-offers.mjs` builds real carts
and reads the total back: the code gates correctly at two units and holds
flat at 10% for three and four. No 20%-on-two code exists on the store ,
25 candidates were tested against a live cart and none applied. The rate
lives in Shopify admin, so nothing in this repo can be read to confirm it;
run the script.

**Their offer is a ladder, ours is one rung.** Read off their live product
tags: `Buy1Get1` (842 products, median list ₹2,229, the premium half),
`B2FOR1899` (1,101) and `B4FOR2999` (1,547) on their ₹1,111 entry pool,
with 545 products carrying both so the basket is pushed from two to four.
Their announcement bar runs "Buy 1 Get 1 Free | Use Code B1G1" sitewide;
ours (`src/components/AnnouncementBar.tsx`) sells 10% off a first order
and never mentions `BUY2`.

**Stock.** 16 of 55 jewellery SKUs are out of stock, 29%, concentrated in
the categories that carry a basket (7 necklaces, 7 bracelets, against 1
ring and 1 earring). A two-piece offer needs two pieces in stock.

**The Type Audit range.** 81 of its 85 SKUs are net-new, only 4 names
touch anything live, so it is a fresh range rather than a re-price. Its
median is ₹1,899 against ₹1,499 live, a +27% step that lands just under
Palmonas' ₹2,099 median ring. At today's 10% that range prices at ₹1,709
a piece on two, or +53% on Palmonas' B1G1; matching them from ₹1,899 needs
41% off on two.

## Two things that make a naive comparison lie

Both are handled in `compare.mjs`, and both are worth knowing before
anyone re-runs this by hand:

1. **Palmonas sell fine gold and lab-grown alongside demi-fine.** Left in,
   their median ring reads ₹34,415 and we look untouchably cheap. Only the
   stainless-steel / 18k-plated tier is our peer set.
2. **List price is not what anyone pays.** Their mechanics live in product
   tags and ours in a discount code, so any comparison that stops at the
   price on the card gets the answer backwards.

## The deep dig, 22 Sep 2026

A second pass went further: every Naira piece was rated by looking at
its photograph (55 live, the 7-piece pre-order capsule, the 85-row Type
Audit), 55 Palmonas counterparts were design-matched and rated the same
way, and Palmonas was read through their own tags, collections and
bestseller curation. Outputs in `data/`:

- `naira-range-ratings.json` and `Naira_Flore_Range_Rating_vs_Palmonas.xlsx`,
  the 147-row rating workbook on the house market-pull framework (Summary,
  Ratings, Buy Shortlist). The LibreOffice headless recalc could not run in
  the build sandbox; the 171 formulas were audited statically (COUNTIF,
  COUNTIFS, AVERAGEIF, IF, ROUND, SUM only, no IFS) and the tier counts
  re-derived in Python match. Open once in Excel to recalc.
- `palmonas-counterparts-2026-09-22.json`, the 55 design-matched pairs with
  both ratings and the two- and four-piece per-piece prices.
- `deep-dig-2026-09-22.json`, the Palmonas structure: sell-through by
  category and band, launch cadence, motif shares, claims, IP-adjacent
  counts, gold floor, bundle pools, and the capsule positioning.

**Three views of the basket, all true.** Pool view: two pieces at our
median list against two from their B1G1 pool is +21% per piece. Design
view: across 55 like-for-like pairs the two-piece median gap is +4% (we
cost more on 28, less on 24). Four-piece view: 33 of 55 counterparts carry
4-for-Rs 2,999, Rs 750 a piece, and we cost more on 41 of 55, median +32%.
The offer gap is widest on the basket their ladder is built to sell.

**Their price architecture skips Rs 1,500 to 2,000.** 485 SKUs there, 19%
sold out, against 42% across demi-fine; the bundles stop at Rs 1,199 and
B1G1 starts at Rs 2,029. Eighteen of our 55 live SKUs and 33 of 85 audit
SKUs sit in that band. The Rs 4,000-plus band is thin (255 SKUs) but clears
at 54%, which matters for the capsule.

**Their bestsellers are the Rs 999 pool with every rung stacked**, fronted
by Shraddha Kapoor, with a licensed Emily in Paris line and a Tanya Ghavri
stylist collab. Demi-fine launches ran 600 to 800 a month through mid 2026
and then fell to 35 to 83 a month from June; the fine-gold line (920 SKUs,
floor Rs 5,276) is where new work is going.

**Ratings.** Live range 7.24 (3 Hero, 41 Strong, 11 Viable; photo 7.4),
their counterparts 6.84 (ours higher on 19, lower on 6), capsule 6.29
(photo 9.0, all renders), Type Audit 6.20 (51 distinct designs in 85 rows,
9 purple or pastel, 8 raw supplier images, 5 IP-adjacent references, 4
near-twins of live SKUs). Our three heroes are the Clover Charm Necklace
(out of stock), Pearl Ribbon Ring and Ribbon Bow Earrings.

**The capsule** sits in the pocket between their demi-fine p95 (Rs 3,779)
and their gold floor (Rs 5,276). Bloom Studs and Sage Vine Band open at
parity with their nearest pieces; the solitaire, halo studs, petal drops
and chandbali have no counterpart at their price. Palmonas carry no
pressed-flower or resin piece, and one chandbali, sold out.
