/* ───────────────────────────────────────────────────────────────
   Scrape a full Shopify catalogue from its public products feed.

     node scripts/competitive/scrape-catalogue.mjs www.palmonas.com out.json
     node scripts/competitive/scrape-catalogue.mjs nc5eti-gp.myshopify.com ours.json

   Every Shopify store exposes /products.json, paginated at 250.
   No key needed — this is the same feed the storefront reads.
   ─────────────────────────────────────────────────────────────── */

const UA =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/120 Safari/537.36";

const PAGE_SIZE = 250;
const MAX_PAGES = 200;
const THROTTLE_MS = 400;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export async function scrapeCatalogue(domain, { onPage } = {}) {
  const products = [];

  for (let page = 1; page <= MAX_PAGES; page++) {
    const url = `https://${domain}/products.json?limit=${PAGE_SIZE}&page=${page}`;
    const res = await fetch(url, { headers: { "User-Agent": UA } });
    if (!res.ok) throw new Error(`${domain} page ${page} -> HTTP ${res.status}`);

    const batch = (await res.json()).products ?? [];
    if (batch.length === 0) break;

    products.push(...batch);
    onPage?.(page, batch.length, products.length);

    if (batch.length < PAGE_SIZE) break;
    await sleep(THROTTLE_MS);
  }

  // The feed can repeat a product across pages when the catalogue shifts
  // mid-scrape, so key by id rather than trusting the page boundaries.
  return [...new Map(products.map((p) => [p.id, p])).values()];
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [domain, outfile] = process.argv.slice(2);
  if (!domain) {
    console.error("usage: scrape-catalogue.mjs <domain> [outfile]");
    process.exit(1);
  }

  const products = await scrapeCatalogue(domain, (page, got, total) =>
    process.stderr.write(`  page ${page}: +${got} (${total})\n`)
  );

  const variants = products.reduce((n, p) => n + p.variants.length, 0);
  console.error(`${domain}: ${products.length} products, ${variants} variants`);

  if (outfile) {
    const { writeFileSync } = await import("node:fs");
    writeFileSync(outfile, JSON.stringify(products));
    console.error(`wrote ${outfile}`);
  }
}
