/* ───────────────────────────────────────────────────────────────
   Verify what our discount codes ACTUALLY take off, by building
   real carts against the Storefront API and reading the total back.

     node scripts/competitive/verify-offers.mjs
     node scripts/competitive/verify-offers.mjs BUY2 NAIRA10

   Carts are throwaway objects — nothing is ordered, nothing is
   charged. This is the only honest way to check a rate: the
   discount lives in Shopify admin, not in this repo, so reading
   the code tells you nothing about what a shopper is charged.
   ─────────────────────────────────────────────────────────────── */

/* Mirrors src/lib/shopify.ts — a .mjs script can't import the .ts source
   without a build step. The Storefront token is public by design; it is
   already in the shipped client bundle. Keep these in step if they move. */
const DOMAIN = "nc5eti-gp.myshopify.com";
const VERSION = "2025-07";
const TOKEN = "0f6fd83502924ac437a5d19180bb08c3";
const ENDPOINT = `https://${DOMAIN}/api/${VERSION}/graphql.json`;

async function gql(query, variables = {}) {
  const res = await fetch(ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Shopify-Storefront-Access-Token": TOKEN,
    },
    body: JSON.stringify({ query, variables }),
  });
  const body = await res.json();
  if (body.errors) throw new Error(JSON.stringify(body.errors));
  return body.data;
}

const PROBE = `
  query Probe {
    products(first: 1, query: "available_for_sale:true") {
      edges { node { title variants(first: 1) { edges { node { id price { amount } } } } } }
    }
  }`;

const PRICE_CART = `
  mutation PriceCart($lines: [CartLineInput!]!, $codes: [String!]) {
    cartCreate(input: { lines: $lines, discountCodes: $codes }) {
      cart {
        cost { subtotalAmount { amount } totalAmount { amount } }
        discountCodes { code applicable }
      }
      userErrors { message }
    }
  }`;

/** Price a basket of `quantity` units of one variant under `code`. */
export async function priceBasket(variantId, quantity, code) {
  const data = await gql(PRICE_CART, {
    lines: [{ merchandiseId: variantId, quantity }],
    codes: code ? [code] : [],
  });
  const { cart, userErrors } = data.cartCreate;
  if (userErrors?.length) throw new Error(userErrors[0].message);
  return {
    total: Number(cart.cost.totalAmount.amount),
    applicable: cart.discountCodes[0]?.applicable ?? null,
  };
}

const codes = process.argv.slice(2);
const list = codes.length ? codes : ["BUY2", "NAIRA10"];

const probe = await gql(PROBE);
const node = probe.products.edges[0].node;
const variant = node.variants.edges[0].node;
const unit = Number(variant.price.amount);

console.log(`probe SKU: ${node.title} @ ₹${unit.toLocaleString("en-IN")}\n`);
console.log("code       qty   list      paid    off   gated");
console.log("─".repeat(50));

for (const code of list) {
  for (const qty of [1, 2, 3, 4]) {
    const { total, applicable } = await priceBasket(variant.id, qty, code);
    const list_ = unit * qty;
    const off = ((1 - total / list_) * 100).toFixed(0);
    console.log(
      `${code.padEnd(10)} ${String(qty).padStart(2)}  ` +
        `${list_.toFixed(0).padStart(7)} ${total.toFixed(0).padStart(9)} ` +
        `${(off + "%").padStart(6)}   ${applicable ? "yes" : "no"}`
    );
  }
  console.log("─".repeat(50));
}
