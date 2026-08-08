# LIVE SITE TECHNICAL AUDIT — nairaflore.com — measured 2026-08-08

## WHAT IS ACTUALLY SERVED

`nairaflore.com` is **not** a Shopify storefront. It is a client-rendered Vite/React SPA on Cloudflare
that talks to Shopify's **Storefront API** headlessly.

Evidence:
- `<body>` contains only `<div id="root"></div>` — empty shell, 3,698 bytes.
- Vite build chunks: `index-udiQdeLN.js`, `vendor-`, `query-`, `ui-`, `gsap-` (matches the `naira-scroll` repo stack).
- `server: cloudflare`; no `x-shopify-*` headers.
- Bundle references `nc5eti-gp.myshopify.com` and `X-Shopify-Storefront` → headless Storefront API integration.
- `www.nairaflore.com` 301s to apex `nairaflore.com`.

### Every route returns byte-identical HTML
| URL | HTTP | Bytes | Add-to-cart in HTML |
|---|---|---|---|
| `/` | 200 | 3,698 | no |
| `/collections/all` | 200 | 3,698 | no |
| `/products/star-point-band` | 200 | 3,698 | no |

Not password-protected. TTFB 0.98–1.68 s.

## CRITICAL DEFECT 1 — canonical hardcoded to homepage on every URL

```html
<link rel="canonical" href="https://nairaflore.com/" />
<meta property="og:url" content="https://nairaflore.com/" />
<title>Naira Flore | Indo-Western Wear & Demi-Fine Jewellery</title>
```
This is served on `/products/star-point-band` and on every other route. Consequences:
- Google is told all 87 product URLs *are* the homepage → the entire catalogue collapses to one indexable page.
- Every WhatsApp / Instagram / Facebook share of any product shows the same generic title, description and OG image.
- Matches the measured reality: **3 organic search sessions in 90 days.**

## CRITICAL DEFECT 2 — no Meta Pixel

Grepped the full served bundles (`index` + `vendor`):

| Signal | Occurrences |
|---|---|
| `fbq` | **0** |
| `fbevents` | **0** |
| `connect.facebook.net` | **0** |
| GA4 measurement ID (`G-XXXXXXXX`) | **none found** |
| Klaviyo / Judge.me / Okendo / Loox | 0 |
| Hotjar / Clarity | 0 |
| `wa.me` | 6 → `wa.me/919561557935` |
| Razorpay | 1 |
| Shopify Storefront API | present |

There is a live, ACTIVE Meta ad account with a payment method attached (`903466039148509`, INR) and
**no pixel on the site**. No purchase signal, no optimisation event, no retargeting pool, no catalogue matching.
Any Meta spend against this site cannot be optimised toward purchase and cannot be measured.
Analytics appears to be a first-party proxy only: `<script defer src="/~flock.js" data-proxy-url="/~api/analytics">`.

## PERFORMANCE — not the bottleneck

| Asset | Raw KB | Served (br/gzip) KB |
|---|---|---|
| index js | 451 | **125** |
| vendor js | 159 | 52 |
| query js | 37 | 11 |
| ui js | 23 | 5 |
| gsap js | 69 | 27 |
| index css | 126 | 22 |
| **Total** | **865** | **~242** |

~242 KB transferred for the app shell is respectable. Fonts are preloaded, Google Fonts is async
(`media="print"` + `onload`), hero LCP image is bundled with `fetchpriority="high"`. Whoever built this
did care about performance. **The problem is not speed — it is that the page is invisible to crawlers,
untracked by Meta, and that product routes render nothing server-side.**

## CHECKOUT SIGNAL
`supportedDigitalWallets: []` on the Shopify shop — no accelerated/wallet checkout (Shop Pay / Google Pay /
Apple Pay) is configured. *Caveat: UPI offered inside a Razorpay-hosted checkout would not necessarily surface
in this field, so treat this as a strong signal, not proof that UPI is absent — verify in Shopify admin.*

Abandoned checkouts, all time: **1**, created 2026-08-07, ₹899.10 for Star Point Band
(₹999 list less a 10% discount — so a discount code is live). Almost certainly an internal test.

## HOW THIS EXPLAINS THE 0%
The 5,460-session burst landed in the week of 2026-05-11. The jewellery catalogue was created
2026-08-06/07 — **three months later.** The traffic and the product line never coexisted. 89% of those
sessions landed on `/collections/all`, and the products that got PDP views were all legacy ₹9,500–₹55,000
couture clothing.

So the honest reading is not "the jewellery store converts at 0%" — it is **"the jewellery store has never
been shown to traffic, and the one real burst of attention the brand has ever bought was spent on a
catalogue it was abandoning."**
