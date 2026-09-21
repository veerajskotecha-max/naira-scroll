/* ───────────────────────────────────────────────────────────────
   Compare our live catalogue against a competitor's, and price the
   basket each brand's offer is built to create.

     node scripts/competitive/scrape-catalogue.mjs www.palmonas.com /tmp/pal.json
     node scripts/competitive/scrape-catalogue.mjs nc5eti-gp.myshopify.com /tmp/ours.json
     node scripts/competitive/compare.mjs /tmp/pal.json /tmp/ours.json

   Two things make a naive comparison lie, and both are handled here:

   1. Palmonas sells a fine-gold and lab-grown line alongside the
      demi-fine one. Left in, their median ring reads ₹34,415 and we
      look untouchably cheap. Only the steel / 18k-plated tier is our
      peer set, so that is all this compares.
   2. List price is not what anyone pays. Their bundle mechanics live
      in product tags (Buy1Get1, B2FOR1899, B4FOR2999); ours lives in
      a discount code. The per-piece table below applies both.
   ─────────────────────────────────────────────────────────────── */

import { readFileSync } from "node:fs";

/* Palmonas' own tag vocabulary, read off their live products. */
const DEMIFINE_TAGS = ["Metal_Stainless Steel", "Plating_18k Gold Plated"];
const BUNDLE_TAGS = { bogo: "Buy1Get1", two: "B2FOR1899", four: "B4FOR2999" };
const BUNDLE_PRICE = { two: 1899, four: 2999 };

/** Our own 2-piece code, at the rate checkout actually applies. */
const OUR_MULTIBUY = { minQty: 2, rate: 0.1 };

const CATEGORY = {
  Earrings: "EARRINGS", Necklaces: "NECKLACE", Necklace: "NECKLACE",
  Rings: "RING", Ring: "RING", Bracelets: "BRACELET", Bracelet: "BRACELET",
  "Jewellery Sets": "SET", "Jewellery Set": "SET",
};

const tagsOf = (p) => new Set((p.tags ?? []).map((t) => t.trim()));
const priceOf = (p) => Number(p.variants?.[0]?.price ?? 0);
const isDemifine = (p) => {
  const t = tagsOf(p);
  return [...t].some((x) => x.startsWith("Demifine_")) ||
    DEMIFINE_TAGS.some((x) => t.has(x));
};

const quantile = (sorted, f) =>
  sorted.length ? sorted[Math.min(sorted.length - 1, Math.floor(sorted.length * f))] : 0;

function band(products, category, filter = () => true) {
  const v = products
    .filter((p) => CATEGORY[(p.product_type ?? "").trim()] === category)
    .filter(filter)
    .map(priceOf)
    .filter((n) => n > 0)
    .sort((a, b) => a - b);
  return { n: v.length, p25: quantile(v, 0.25), median: quantile(v, 0.5), p75: quantile(v, 0.75) };
}

/** Median list price of the pool a given bundle tag is applied to. */
function poolMedian(products, tag) {
  const v = products
    .filter((p) => tagsOf(p).has(tag))
    .map(priceOf)
    .filter((n) => n > 0)
    .sort((a, b) => a - b);
  return quantile(v, 0.5);
}

/** What one piece costs when you buy `n`, under each live mechanic. */
function perPiece(n, ourList, pools) {
  const ourRate = n >= OUR_MULTIBUY.minQty ? 1 - OUR_MULTIBUY.rate : 1;
  return {
    basket: n,
    ours: Math.round((ourList * n * ourRate) / n),
    // BOGO: you pay for half, rounded up.
    bogo: Math.round((pools.bogo * Math.ceil(n / 2)) / n),
    // Fixed bundles: whole bundles at the fixed price, remainder at list.
    two: Math.round((BUNDLE_PRICE.two * Math.floor(n / 2) + pools.two * (n % 2)) / n),
    four: n === 4 ? Math.round(BUNDLE_PRICE.four / 4) : pools.four,
  };
}

const args = process.argv.slice(2);
const asJson = args.includes("--json");
const [theirsFile, oursFile] = args.filter((a) => !a.startsWith("--"));
if (!theirsFile || !oursFile) {
  console.error("usage: compare.mjs <competitor.json> <ours.json> [--json]");
  process.exit(1);
}

const theirs = JSON.parse(readFileSync(theirsFile, "utf8"));
const ours = JSON.parse(readFileSync(oursFile, "utf8"));

/* Our couture pieces carry no product_type and run to five figures;
   they are not in this market and would swamp every median. */
const ourJewellery = ours.filter((p) => (p.product_type ?? "").trim());
const oos = ourJewellery.filter((p) => !p.variants?.[0]?.available);

const pools = Object.fromEntries(
  Object.entries(BUNDLE_TAGS).map(([k, tag]) => [k, poolMedian(theirs, tag)])
);
const ourList = quantile(ourJewellery.map(priceOf).filter(Boolean).sort((a, b) => a - b), 0.5);
const CATEGORIES = ["RING", "EARRINGS", "BRACELET", "NECKLACE", "SET"];

if (asJson) {
  console.log(JSON.stringify({
    counts: {
      theirTotal: theirs.length,
      theirDemifine: theirs.filter(isDemifine).length,
      theirPeers: theirs.filter((p) => isDemifine(p) && CATEGORY[(p.product_type ?? "").trim()]).length,
      ourJewellery: ourJewellery.length,
      ourCouture: ours.length - ourJewellery.length,
      ourOOS: oos.length,
    },
    ourMedianList: ourList,
    pools,
    bands: Object.fromEntries(CATEGORIES.map((c) => [c, {
      ours: band(ourJewellery, c),
      theirs: band(theirs, c, isDemifine),
    }])),
    perPiece: [1, 2, 3, 4].map((n) => perPiece(n, ourList, pools)),
  }, null, 1));
  process.exit(0);
}

console.log(`THEIRS  ${theirs.length} products, ${theirs.filter(isDemifine).length} demi-fine`);
console.log(`OURS    ${ourJewellery.length} jewellery (${oos.length} out of stock), ` +
            `${ours.length - ourJewellery.length} couture\n`);

console.log("PRICE BANDS — demi-fine only, p25 / median / p75");
console.log("category    side          n     p25   median     p75");
console.log("─".repeat(54));
for (const cat of CATEGORIES) {
  for (const [label, set, filter] of [
    ["ours", ourJewellery, () => true],
    ["competitor", theirs, isDemifine],
  ]) {
    const b = band(set, cat, filter);
    if (!b.n) continue;
    console.log(
      `${cat.padEnd(11)} ${label.padEnd(12)} ${String(b.n).padStart(4)} ` +
      `${String(b.p25).padStart(7)} ${String(b.median).padStart(8)} ${String(b.p75).padStart(7)}`
    );
  }
}

console.log(`\nPER-PIECE PRICE AFTER OFFERS — our median list ₹${ourList}`);
console.log("basket     ours     BOGO   2/1899   4/2999");
console.log("─".repeat(44));
for (const n of [1, 2, 3, 4]) {
  const r = perPiece(n, ourList, pools);
  const flag = r.ours > Math.min(r.bogo, r.two, r.four) ? "  <- we cost more" : "";
  console.log(
    `${String(n).padEnd(6)} ${String(r.ours).padStart(8)} ${String(r.bogo).padStart(8)} ` +
    `${String(r.two).padStart(8)} ${String(r.four).padStart(8)}${flag}`
  );
}
