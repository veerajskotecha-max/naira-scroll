# Competitive pricing — Naira Flore vs Palmonas

Tooling for pulling both catalogues live and pricing the basket each
brand's offer is built to create. Run from the repo root; no install,
no keys — Node 22's built-in `fetch` is all any of it needs.

```sh
node scripts/competitive/scrape-catalogue.mjs www.palmonas.com      /tmp/pal.json
node scripts/competitive/scrape-catalogue.mjs nc5eti-gp.myshopify.com /tmp/ours.json
node scripts/competitive/compare.mjs /tmp/pal.json /tmp/ours.json
node scripts/competitive/verify-offers.mjs BUY2 NAIRA10
```

`compare.mjs --json` emits the same figures as machine-readable output;
`data/palmonas-2026-09-21.json` is that output from the 21 Sep 2026 run,
and `data/type-audit-skus.json` is the 85-SKU Type Audit range parsed out
of the PDF. Both are small enough to keep in the repo — the raw Palmonas
dump (39 MB) is not, so re-scrape rather than committing it.

## What the 21 Sep 2026 run found

**Scale.** Palmonas list 9,005 products / 20,742 variants; 6,007 of them
are demi-fine pieces in our five categories. We list 55 jewellery SKUs
(plus 18 couture pieces, which are not in this market and are excluded
from every figure below).

**We list cheaper and sell dearer.** Our median jewellery list is ₹1,499
against ₹2,229 for the products Palmonas puts B1G1 on — 33% below them.
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
flat at 10% for three and four. No 20%-on-two code exists on the store —
25 candidates were tested against a live cart and none applied. The rate
lives in Shopify admin, so nothing in this repo can be read to confirm it;
run the script.

**Their offer is a ladder, ours is one rung.** Read off their live product
tags: `Buy1Get1` (842 products, median list ₹2,229 — the premium half),
`B2FOR1899` (1,101) and `B4FOR2999` (1,547) on their ₹1,111 entry pool,
with 545 products carrying both so the basket is pushed from two to four.
Their announcement bar runs "Buy 1 Get 1 Free | Use Code B1G1" sitewide;
ours (`src/components/AnnouncementBar.tsx`) sells 10% off a first order
and never mentions `BUY2`.

**Stock.** 16 of 55 jewellery SKUs are out of stock — 29%, concentrated in
the categories that carry a basket (7 necklaces, 7 bracelets, against 1
ring and 1 earring). A two-piece offer needs two pieces in stock.

**The Type Audit range.** 81 of its 85 SKUs are net-new — only 4 names
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
