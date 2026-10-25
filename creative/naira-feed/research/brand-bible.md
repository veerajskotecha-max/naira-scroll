# NAIRA FLORE · Brand Bible for the Instagram feed

Compiled 25 Oct 2026 for the two 12-post feed options. Read-only sweep of both repos, plus two
read-only connector checks (Shopify Admin GraphQL, Meta Ads IG endpoints). Nothing was created,
posted or changed anywhere.

**Confidence legend** used throughout:
- **[V]** verified in a primary source today (live Shopify, live Meta, or code that renders on the site)
- **[R]** stated in a repo document (date given); not re-verified today
- **[U]** unverified, contradictory, or inferred; check with the owner before it goes on an image

Kit that goes with this file: `/tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed/kit/`
(see section 20 for the file index).

---

## 1. Who, what, where

| Fact | Value | Source |
|---|---|---|
| Company / site name | **Naira Flore**, nairaflore.com | site everywhere [V] |
| Shopify store name | **Naira** (permanent domain nc5eti-gp.myshopify.com, Basic plan, INR, IST, India, email shopatnaira@gmail.com) | Shopify get-shop-info, 25 Oct [V] |
| Legal / trade name | "Naira (Managed by Vandana Sanjay Kotecha)" | `src/pages/ContactUs.tsx` [V] |
| What it is | A **Nashik couture / made-to-measure studio** that also sells **Naira Petite**, a demi-fine jewellery line | `public/llms.txt`, `FounderStoryTeaser.tsx` [V] |
| Jewellery line name | **Naira Petite** (Shopify vendor "Naira Petite"; apparel is vendor "Naira Flore") | CLAUDE.md, Shopify [V] |
| The wordmark reads | **NAIRA** (a flower stands as the I) | `src/lib/nairaFlower/*` [V] |
| Instagram | **@naira.flore** (IG id 17841475924464756), the account linked to the "naira flore meta ads" ad account | Meta `ads_get_ig_accounts`, 25 Oct [V] |
| Instagram link on the site | `instagram.com/nairaflore/` (footer + JSON-LD `sameAs`) | `Footer.tsx:235`, `siteMeta.ts:44` [V] **mismatch with @naira.flore, see 18** |
| City | Nashik, Maharashtra | site [V] |
| Addresses in code | Two different ones: "C-5, Nayantara Estate, Sambhaji Chowk, Nashik 422002" (Contact page) and "Flat 7, Veeraj Blossom, Karanyogi Nagar, Nashik 422002" (PDP + JSON-LD) | [V] **do not print an address on the feed** |
| Hours | Mon to Sat, 10 am to 7 pm IST | ContactUs, catalogue [V] |
| WhatsApp / phone | **+91 95615 57935** (fixed, per design-tokens.md) | [V] |
| Email | shopatnaira@gmail.com | [V] (the catalogue team chose not to print email because "the site lists three different addresses" [R]) |
| Languages served | en, hi, mr | `siteMeta.ts` [V] |

### The two businesses under one roof
1. **The couture / made-to-measure studio** (the origin). Outfits designed with each client over
   WhatsApp, made to measure, 4 to 8 weeks (`llms.txt`). Site page `/customize`. Recent IG couture
   posts name capsules and series: "Festive '26. The Haldi capsule, N° 01", "The Garden Series, N° 02",
   "Craft Files, N° 05" [V, IG captions June 2026]. The site is now jewellery-only apart from the
   made-to-measure section (`roadmap.md`, last entry, undated) [R].
2. **Naira Petite**, demi-fine jewellery. 117 active listings, 105 in stock today [V, Shopify 25 Oct].
   This is what the site, the ads and the feed sell.

---

## 2. Founder and story (facts as found)

- **Founder: Vandana Kotecha**, "Founder, Nashik". Photo `src/assets/about-founder.webp`
  (yellow saree), alt text "Vandana, founder of Naira Flore, in her Nashik studio" [V, `FounderStoryTeaser.tsx`].
  Copied to `kit/motifs/photo-cutouts/site-about-founder-vandana.webp`.
- The exhibition poster (Club Aquarium, Borivali, Mumbai, 3 and 4 Oct 2026) shows a woman seated at
  the Naira Petite stall in a lilac lace kurta. Cut-out: `kit/motifs/photo-cutouts/exhibition-stall-cutout.png`.
  She **appears** to be the founder [U] - confirm before captioning her by name.
- Founder's line: **"made to stay gold."** - "the founder's *made to stay gold.*" [R, upclose PLAN.md]. Printed
  on the bag and the catalogue back page.
- Founding year: **not in the codebase**. `siteMeta.ts` omits `foundingDate` on purpose: "inventing them
  would be fabricated markup" [V]. Never write "since 20XX".
- The story the site tells, verbatim (`FounderStoryTeaser.tsx`) [V]:
  > "From our Nashik studio. Born from a love of craft and colour."
  > "Naira Flore began in a small studio in Nashik, and the studio still makes outfits to measure: you share
  > the look you want on WhatsApp, choose the fabric and silhouette, and it is stitched by hand to your
  > measurements."
  > "Beside them sits Naira Petite, our demi-fine jewellery: 18K gold coated, anti-tarnish, and made to be worn every day."
- The catalogue's "About Naira" page, verbatim (`creative/naira-catalogue/build/build.py`) [R, 1 Oct]:
  > "HERE YOUR STORY IS HAND-STITCHED / *into every thread.*"
  > "Naira is an Indian couture house: soft tailoring, pressed flowers and the long quiet of an Indian afternoon.
  > Every outfit is hand-finished and made to measure in our atelier, one at a time."
  > "Naira Petite is the house's demi-fine jewellery. The same soul in a smaller object: pieces made to be worn
  > every day, light enough to forget you have them on, and finished to keep their colour."
- The upclose campaign's framing: **"NAIRA is a couture house first, so our jewellery gets styled where the
  thread is."** and the chapter "The house that sews": spool, swatch, care label, pattern key hold the jewellery.
  Judge fix: "the copy claims only what is true (NAIRA is a couture house), **never that the chain is handmade**" [R].
- Brand pillars on the homepage marquee: **Personalised · Handcrafted · Floral-Inspired** (`BrandEthos.tsx`) [V] -
  these describe the couture side.
- Brand deck: the code cites "the brand deck" (wordmark p. 5; stand-alone flower p. 7, captioned "The smallest
  piece, the brand entire") [V, comments in `wordmark.ts`/`outline.ts`]. **The deck itself is not in either repo**;
  ask the owner for it.

---

## 3. Collections, editions and series that exist

| Name | What | Source |
|---|---|---|
| **Naira Petite** | the whole jewellery line | [V] |
| **Edition One · KAVNAR** | 14 live listings (13 in the 18 Oct snapshot) tagged `Edition One`, `KAVNAR`, `pre-order` (e.g. Torsade Huggies, Lilac Papillon Ring, Prism Cluster Studs, Pearl Circlet Studs, Molten Panel Bracelet). Pre-order; the bag never one-tap-adds them | Shopify tags [V] |
| **Edition Two** | 33 live listings (31 in the 18 Oct snapshot; already in the catalogue ads by then) (Silk Mesh Cuff, Triple Coil Wrap Bangle, Baguette Tennis Bracelet/Necklace, Kiss Knot Bangle, North Star Bangle, Birthstone Heart Necklace, Roman Numeral Trio Ring, Duo Link, Marquise Drop Choker...) | CLAUDE.md, Shopify [V] |
| **"Aditya" pieces** | 12 low-priced listings (₹490-₹1,015) tagged `Aditya`, mostly 1-5 units, **without** the Waterproof / Tarnish Free / Hypoallergenic tags | Shopify [V]; meaning of the tag [U] |
| **The Golden Hour** | hidden ad-only edit at `/the-golden-hour` (10 pieces) | `.lovable/plan/the-golden-hour...md` [R] |
| **The Gilded Hour** | the pre-order launch campaign (old banners: "Pre-Order Open", solitaire render) - superseded | `marketing-assets/banners` [R] |
| **NAIRA Petite · Up Close** (`upclose-oct26`) | the live Oct-Nov paid campaign, 26 briefs C01-C26 | `creative/naira-campaign-upclose/PLAN.md` [R] |
| **Lilac Hour (VIII), Soft Matter (VI), The Red Room, Colour Theory, Slow Burn, The Pale Hours, Soft Physics, How It's Worn** | Higgsfield plate campaigns behind the ads | `naira-ads/README.md`, BRAND.md [R] |
| **Catalogue camps**: The Long Afternoon, Sage, Steel & Gold, The Red Room (Vol. One); **Apricot / Lilac / Sage editions** | print catalogues | `naira-catalogue/` [R] |
| **The Petite Index** | "every piece, on one page." A4 index of 55 listings | `naira-index/` [R] |
| **Lac bone** | IG, 9 Aug 2026: "Introducing our premier campaign : Lac bone at Naira. Made in small numbers, as always." (best-commented post: 35 likes, 8 comments) | Meta IG media [V]; what "Lac bone" refers to [U] |
| **Couture series on IG** | "The Haldi capsule, N° 01", "The Garden Series, N° 02", "Craft Files, N° 05", "Festive '26" | IG captions, June 2026 [V] |
| **The Inner Circle** | members list, "BY INVITATION ... OPENING SOON" | `InnerCircle.tsx` [V] |
| Site collections | rings, earrings, bracelets, necklaces + ~27 SEO landings (anti-tarnish, bridal, couple rings, hoops, gifts, saree, lehenga, evil eye...) | `public/llms.txt` [V] |
| Menu edits | New Arrivals, Bestsellers, Under ₹1,500, occasions Everyday / Festive / Wedding / Gifting | `data/navigation.ts` [V] |

Named product "sets" used for pairing (`src/lib/pairings.ts`): Nocturne, Duo Link, Lumière, Whisper,
Verdant/emerald, Prism, Rivière, Marquise, Torsade, Baguette, Pearl, Blush, Droplet, Baroque, Molten, Mesh [V].
Woven Gold Hoops have been "in every multi-piece website order since September" (CLAUDE.md) [R].

---

## 4. Product truths: what an image may and may not say

### 4.1 What the pieces are made of (read carefully)
- **Plating / finish** is the only material word the brand uses on images. The approved wording, from the founder
  (catalogue README) [R]: **"18k gold coated"** / **"rhodium coated"** (plus "rose gold coated" for one band, and
  two-tone for Heartbead). The site's box band says **"18K gold tone · rhodium plated"** and its comment explains:
  *"'18K gold' alone would claim gold content the pieces do not have."* (`NairaBoxShowcase.tsx`) [V].
  Shopify tags say `18k Gold Tone Plated`, `Rhodium Plated`, `Rhodium Silver Tone Plated`, `Two Tone`, `Tri Tone`,
  `Rose Gold Tone` [V].
- **Base metal is NOT uniform.** Most listings say "surgical stainless steel" in a generated summary line, one says
  "18k gold-plated 316L stainless steel" (Triple Dawn Cuff), and **Verdant Drop Earrings are "copper alloy ... with
  925 sterling silver posts"** [V, product descriptions]. CLAUDE.md: "materials are left out because some pieces are
  copper alloy." BRAND.md's blanket "18K-plated 316L stainless steel" is therefore **not safe** as a line-wide claim.
- **Stones**: cubic zirconia, called **"zircone"** or "brilliant-cut zircone" in house copy; shell pearl and (four
  listings) freshwater pearl; tiger eye on Halo Curve Ring [V]. Never "diamond".

### 4.2 Claim table

| Claim | Status | Rule |
|---|---|---|
| "[ 18k gold coated · rhodium coated ]" (the bracket line) | **SAFE** as a line-level descriptor | The house signature line; on the bag, catalogue, exhibition poster, ads |
| "18k gold coated" / "18K gold tone plated" on a piece | SAFE **only** on pieces tagged `18k Gold Tone Plated` | check the tag |
| "rhodium coated" on a piece | SAFE only on `Rhodium Plated` / `Rhodium Silver Tone Plated` pieces | 13 in-stock pieces are rhodium/silver only: Prism Rivière, Cushion Halo, Emerald Deco/Halo C-Hoops, Heartbead (two-tone), Pavé Dome, Pearl Blossom, Serpentine Whisper Silver, Trio Oval Drop, Verdant Drop, Verdant Eternity, Vintage Halo, Whisper Pavé [V] |
| "demi-fine" | SAFE | used everywhere |
| "zircone" / "cubic zirconia" / "brilliant-cut zircone" | SAFE on pieces with stones | |
| "waterproof" | **CONDITIONAL**: only pieces tagged `Waterproof`. **35 in-stock pieces lack the tag**, incl. all Edition One pre-orders, all "Aditya" pieces, Pearl Legacy Necklace, Baroque Shell Bracelet, Pearl Nugget Hoops, Verdant Drop Earrings, Garnet Cable Cuff, Emerald Deco/Halo hoops, Tile Stone Bangle, Birthstone Heart Necklace [V] | Never on a mixed-piece image. Never "swim in it" (see 18: the site FAQ says remove before swimming) |
| "tarnish-free" / "anti-tarnish" | CONDITIONAL: tagged `Tarnish Free` only (33 in-stock pieces lack it) [V] | same |
| "hypoallergenic" | CONDITIONAL: tagged `Hypoallergenic` only (32 in-stock pieces lack it) [V] | same |
| "nickel-free", "lead-free" | **UNVERIFIED** for the line (stated on one listing, Triple Dawn Cuff, which is sold out) | keep off images |
| "made to stay gold." | SAFE as the founder's sign-off, **never on a rhodium-only piece** | upclose rule [R] |
| "Every piece arrives in the Naira gift box" | SAFE (53 of 56 listings showed the box, CLAUDE.md; site band says it) | |
| "Free insured shipping" | SAFE (`SHIPPING_CHARGE = 0`, bag + PDP copy) [V] | |
| "COD available" | SAFE (PDP line); never state "no COD fee" (Fastrr adds 5% to COD orders) [V] | |
| "Delivery in 3-5 working days" | SAFE-ish (Maharashtra 3, rest of India 5, `serviceability.ts`) [V]; llms.txt says 3-7 | no dated "order by" lines (no courier cut-off confirmed [R]) |
| "Made in limited batches" / "small batches" | owner's header line (`AnnouncementBar.tsx`) [V]; "Made in small numbers, as always." (IG) | OK as house voice; never a number |
| "gold", "real gold", "solid gold", "18K gold" (alone), "gold jewellery" | **FORBIDDEN** | claims gold content. Note two PDPs still say "solid gold band" (Halo Curve Ring) and "solid gold granulation" (Granule Dome Ring): wrong, never echo [V] |
| "diamond", "American diamond" | FORBIDDEN on images (SEO pages use "American diamond" as a search term only) | |
| "surgical steel", "316L", "stainless steel" | FORBIDDEN on images (ad 104 was paused for printing "SURGICAL STEEL") [R]; not true of every piece | |
| "silver", "sterling silver", "925" | FORBIDDEN except "sterling silver posts" on Verdant Drop Earrings | |
| "handmade", "hand-set at our atelier", "crafted in Nashik", "made in Nashik" (for jewellery) | **UNVERIFIED, keep off images.** BRAND.md speaks of "a competitor sourcing the same factory", and the upclose judges banned "handmade" for the chain [R]. Some site copy (footer, SEO pages) still says it [V] | craft is argued through what the eye can see: claws, rails, weave, clasp |
| "forever", "lifetime", "permanent" | FORBIDDEN ("stayed", never "forever") [R] | |
| "pre-order open" | only on Edition One / sold-out pieces; the design-tokens.md invariant "Jewellery never shows prices; every piece shows 'Pre-order open'" is **superseded** (prices show since launch) | |
| "7-day returns" | **CONDITIONAL**: the policy allows a return within 7 days of delivery for a manufacturing defect; made-to-measure is non-returnable (`ExchangeReturnPolicy.tsx`). The jewellery page strip says "7-DAY RETURNS" [V] | keep off images |
| "Over 2,500 custom pieces handcrafted" | UNVERIFIED (`MadeForYou.tsx`) | keep off |
| "As featured in Times of India / Maharashtra Times / Lokmat / Times Now / Fashionista" | UNVERIFIED: logos sit in `PressMarquee.tsx` with no article links in the repo | keep off until the owner shows the coverage |
| "N pieces sold in the last 24/48 hours" | **FABRICATED** (`JewelTrustStrip.tsx`: N is a hash of the handle) | never |
| Customer reviews / star ratings | **The review bank is generated** (`productReviews.ts`: alphabetical names Aarti, Aditi, Akanksha..., consecutive dates Aug 28, 27, 26...) | never quote as testimonials; only real Judge.me / WhatsApp reviews with a yes (reviews-playbook.md) |
| Ring sizes | inconsistent across the site (FAQ: US 5/6/7 with 6 in stock; llms.txt US 5-8; ring chart US 5-9; Petite Pavé Band "adjusts from size 6 to 8") | piece-specific only |
| Exact mm figures | must match the listing (BRAND.md) | |

### 4.3 Piece-level truths already audited (upclose plan, 1 Oct) [R]
- **Toggle Link Chain** ships with a **spring-ring clasp and a pavé-set gate/bar**, not a turn-toggle. Say "spring ring", never "a turn, not a catch".
- **Granule Dome Ring**: an **openwork lattice** dome ("OPENWORK, like lace."), not solid granulation.
- **Chevron Whisper Ring**: **three rails** (stone V on top, plain polished V in the middle, stone curve below) - "ONE LEFT PLAIN. on purpose."
- **Verdant Circlet Studs**: two white shell pearls per stud (about 6 mm and 4 mm), green stone.
- **Baroque Shell Bracelet**: eight flat shell pearls plus a drop; not tagged waterproof.
- **Prism Rivière Bracelet**: aqua, pink, pale yellow cushion stones, each in a halo, fold-over clasp, 15-19 cm adjustable; **rhodium only** ("[ rhodium coated ]"); 67 in stock.
- **Halo Curve Ring**: a tiger eye beside a champagne crystal ("two stones that don't match").
- **Heartline Paperclip Necklace**: nine heart stations (audit count; physical count was requested).
- **Brushed Gold Huggies**: about 12 mm.
- **Ribbon Bead Bracelet**: two hearts forming a bow, adjusts 16-19 cm.

---

## 5. Price ladder (LIVE, Shopify, 25 Oct 2026) [V]

Prices move. They changed between the 1 Oct catalogue, the 18 Oct site snapshot and today
(e.g. Woven Gold Hoops ₹1,499 on 1 Oct, ₹2,349 in `jewellery.ts`, **₹1,299 live**; Halo Curve Ring ₹2,049 → **₹1,299**;
Toggle Link Chain ₹1,499 → **₹1,299**; Heartline Paperclip ₹1,899 → ₹2,449 in code → **₹1,899** live).
**Re-read Shopify the day a post is rendered; never take a price from a repo file.**
Full live list: `research/data/shopify-live-2026-10-25.json` (117 active listings).

- 117 active · **105 in stock** · 12 sold out
- In-stock price range **₹490 to ₹2,749**, median **₹1,299**
- Bands (in stock): under ₹1,000: 29 · ₹1,000-1,499: 57 · ₹1,500-1,999: 16 · ₹2,000+: 3
- Highest: Teardrop Lariat ₹2,749 (1 left), Prism Rivière Bracelet ₹2,399 (67), Baguette Tennis Necklace ₹2,300 (70)
- Floor (core line, excl. "Aditya"): Ribbon Bead Bracelet ₹799 · Star Point Band ₹799 · Birthstone Heart Necklace ₹699 · Mesh Band Ring ₹699
- 79 of 105 in-stock pieces carry an MRP (compare-at) 1.4x to 2.9x the price; the site strikes it through. **Do not show struck MRPs on feed images** (see 14).
- **CLAUDE.md's "pieces at ₹24,000-44,000" is wrong** (live data: ₹490-2,749); likely a typo. Never quote it.

**Deep stock (20+ units, not pre-order), safe to feature for weeks** [V]:
Toggle Link Chain 79 (₹1,299) · Baguette Tennis Necklace 70 (₹2,300) · Prism Rivière Bracelet 67 (₹2,399) ·
Woven Gold Hoops 63 (₹1,299) · Cushion Halo Ring 60 (₹1,199) · Verdant Eternity Band 60 (₹1,099) ·
Baguette Huggies 57 (₹1,199) · Baguette Tennis Bracelet 57 (₹1,699) · Bold Nocturne Chain 53 (₹1,799) ·
Bold Nocturne Bracelet 49 (₹1,599) · Halo Curve Ring 45 (₹1,299) · Kiss Knot Bangle 40 (₹1,199) ·
Marquise Layering Set 40 (₹1,599) · Silk Mesh Cuff 40 (₹1,499) · Brushed Gold Huggies 35 (₹999) ·
Ribbon Bead Bracelet 34 (₹799) · Rivière Eternal Bracelet 34 (₹1,449) · Baguette Eternity Band 30 (₹1,299) ·
Heartbead Bracelet 25 (₹1,299) · Baroque Shell Bracelet 23 (₹1,799) · Serpentine Whisper Chain Silver 23 (₹1,299) ·
Chain Drop Dome Ring 22 · Linked Pair Ring 22 · and 13 more at exactly 20.

**Low stock (1-5 units): do not build a post around these** (a post outlives the stock): e.g. Baguette Arc Hoops 1,
Teardrop Lariat 1, Rose Verdant Band 1, Pearl Point Studs 2, Granule Dome Ring 4, Heartline Paperclip Necklace 4,
Pearl Legacy Necklace 5, Chevron Whisper Ring 5, Verdant Circlet Studs 5, Petite Pavé Band 4, Filigree Bloom Studs 3,
Pearl Drop Studs 4.

**Sold out today**: Baroque Bloom Cuff, Baroque Pearl Lariat, Blush Station Bracelet, Clover Charm Necklace,
First Light Set, Lumière Oval Necklace, Molten Bloom Hoops, Petite Pearl Chain, Rivière Eternal Necklace,
Rivière of Light Bracelet, Solitaire Whisper Studs, Triple Dawn Cuff.

Price typography: **Velista has no ₹ glyph** (and no "·", no em dash). Set prices in Jost with the ₹ falling back to
Poppins (the catalogue's method) - `tokens.css` does this via `--nf-font-label`.

---

## 6. Offers, codes and their rules (`src/lib/promo.ts`, CLAUDE.md) [V]

| Code | Value | Rule |
|---|---|---|
| **BUY2** | 10% off, min 2 pieces | applied by the bag automatically (a code, because Fastrr ignores automatic discounts) |
| **BUY3** | 20% off, min 3 pieces | same |
| **NAIRA10** | 10%, anyone, no minimum, typed | live; the owner **asked for it to come off the header strip** (`AnnouncementBar.tsx`); auto-applying it is "a margin call for the owner" |
| **FRIENDSANDFAMILY** | 20% | outranks the 2-piece rung; not for public posts |

- **Only ONE code reaches checkout** (Fastrr). Never imply stacking ("BUY2 + NAIRA10").
- Header strip today: "SITEWIDE SALE LIVE TODAY!" (owner asked for the exclamation and no percentage), "FREE INSURED SHIPPING", "MADE IN LIMITED BATCHES".
- Bag offer line (owner's wording): "✦ Sitewide sale live today · up to 20% off".
- Paid-ad rule: **no offer, code or percentage on any image; BUY2 lives in the primary text** (upclose PLAN) [R].
  Recommendation for the feed: same rule. Codes in captions only.

## 7. Shipping, COD, returns, contact [V]
- Free insured shipping (`SHIPPING_CHARGE = 0`); "Tax included."
- Delivery: 3 working days Maharashtra, 5 rest of India (`serviceability.ts`); bag says "arrives {date}".
- COD available; **Fastrr adds 5% of the post-discount total to COD orders**, booked as shipping (`payment.ts`). 42% of orders were COD on 1 Oct [R].
- Returns: defect returns within 7 days of delivery via WhatsApp; made-to-measure non-returnable.
- Made-to-measure: 4-8 weeks; brief over WhatsApp, sketches, consultation call, delivered (`CoutureExperience.tsx`, `llms.txt`).
- Contact for the feed: **nairaflore.com · WhatsApp +91 95615 57935** (exactly as on the exhibition poster).
- Link in bio should land on `/jewellery` (or a collection), keeping UTMs; ads land on `/products/<handle>` which hops to `/jewellery/<handle>` keeping the query string.

---

## 8. Packaging (real objects you can draw or photograph)

| Object | What it looks like | Source |
|---|---|---|
| **The Naira box** | blush-pink sleeve with a lighter rim, a drawer with a front and a **pull tab**, lid printed with the wordmark (flower as the I) in dark ink; a velvet cushion holds a ring. "The Naira box, in blush." | CLAUDE.md (3D box), catalogue caption, `naira-box-poster.webp`, `naira-box-print.webp` [V] |
| Box renders in the kit | `kit/motifs/box/naira-box-poster.webp` (516x412), `naira-box-print.webp` (lid print 2048x512), ring renders `ring-cut-34.webp` (gold), `-silver` | [V] |
| **The bag** (D-cut, 6 x 9.5 x 2 in) | cream ground, watercolour leaf sprigs at 34%, **coral tulips** in the corners, wordmark sage + blush, "[ 18k gold coated · rhodium coated ]", "*made to stay gold.*", QR to nairaflore.com/jewellery | `creative/naira-bag/README.md` [R]; whether it has been printed [U] |
| Insert card (pre-order era) | "With our thanks / Thank you for your pre-order / Your piece was finished in a small batch and set aside for you. We hope it stays with you for a long while." + care: "Let perfume and sprays settle before you dress..." "After each wear, wipe gently with a soft, dry cloth." "Rest your piece in its pouch, away from moisture and direct sunlight." "With care, the Naira Flore studio" | `marketing-assets/kit/packaging-insert-1200x1800.html` [R] - pre-order wording is out of date |
| Exhibition display | bamboo trays with sage-green and cream velvet, sage velvet T-bar bracelet rollers with gold caps, bamboo necklace busts, blush Naira boxes on the table | exhibition poster photo [V] |

---

## 9. Palette

All hexes are in `kit/tokens.css` and on `kit/kit-preview.png`. Four families exist; they are not one palette.

### 9.1 Identity (the logo and packaging) - BRAND.md [R]
| Name | Hex | Use |
|---|---|---|
| Cream | `#FFF8F5` | ground |
| Sage | `#99B4AF` | **the wordmark letters** (also site `--nf-sage`) |
| Coral / Blush | `#FFBDA8` | **the wordmark flower** (site `--nf-blush`; the old logo sampled `#FDBCA9`) |
| Enamel blush | `#F5A58F` | the 3D flower's lit base (`nairaFlower/config.ts`) |

### 9.2 Site tokens (`src/index.css`, exact) [V]
ivory `#FBF3EC` (page ground) · ivory-deep `#F4EBE2` (packshot linen) · ink `#1A1614` · gold `#C99A4C`
(hairlines, sparkle) · gold-deep `#B0843A` (eyebrows, Secure Checkout gold) · gold-shadow `#9A7634` ·
gold-text `#80612A` (small gold text, AA) · sage `#99B4AF` · blush `#FFBDA8` · sage-logo `#8EA9A1`
(footer, hsl 162 14% 61%) · **sage-logo-deep `#4F7268`** (buy buttons, hsl 162 18% 38%) · cta-hover `#416258` ·
cream `#F6F3EE` (text on sage) · warm-grey `#6B625B` · linen `#E3D9CE` · announcement strip `#AEBDB6`.
Rules: never a raw hex where a token exists; **radius 0** (sharp corners are the brand); one exception
(the bag's checkout button, 10px). Do not reintroduce the old teal `#2E5B60`.

### 9.3 Ad system - BRAND.md + `naira-ads/build/studio.py` [R]
Cream `#FFF8F5` on imagery · **Marigold `#E8973A`** eyebrow + rule only · marigold-deep `#8F4E0E` (index dots) ·
Ink `#1A1614` on pale grounds · Sage reserved for the logo lockup. Grounds used: `#FBF1E6`, lilac `#EDE3F2`, `#E7DEF0`.

### 9.4 Illustration (bag + card tulips) - `motifs.py` [R]
cream `#FBF5F0` · coral `#F6AE96` · coral-deep `#EC957A` · coral-light `#FBCCBA` · coral-back `#E4886F` ·
leaf sage `#9DB5AD` · leaf deep `#7F9A91` · leaf light `#BBCDC6` · ink `#3D3530`.

### 9.5 Catalogue Volume One - `build.py` [R]
cream `#F4F0E8` · paper `#FBF5F0` · blush `#FBEDE9` · blush-mid `#F2CFC4` · ink `#1C1C1C` · ink-soft `#3D3530` ·
muted `#6B615A` · sage-deep `#5E7A70` · coral-deep `#B8604A` · **sage ground `#9CB1A5`** (Camp II) ·
**Red Room `#4B191A`** (Camp IV, "lit for the festive table").

### 9.6 Catalogue camp editions - `build_theme.py` [R]
| Edition | paper | ground | tint | deep | on-ground / mast | world |
|---|---|---|---|---|---|---|
| **Apricot** | `#FCF5EF` | `#F0C9AC` | `#F7E1D2` | `#A9532B` | head `#7A3D20`, on `#4A2B1D` | raw apricot silk, a halved apricot, an almond; gold |
| **Lilac** | `#F8F5F8` | `#C9B6CB` | `#ECE4EF` | `#5E4A78` | mast `#4E3C66`, on `#2E2338` | deckled lilac paper, lavender, lilac linen; silver |
| **Sage** | `#F6F6F1` | `#AFBFA9` | `#E3EAE1` | `#3F5A4C` | mast `#F2EFE6`, on `#1F2E25` | celadon crackle-glaze dish, sage leaves, sage linen; gold |

### 9.7 Exhibition poster - `poster.py` [R]
bottle green `#2E4238` (radial to `#4C6A5C` / `#263830`) · cream `#F6EFE6` · **date gold `#E7C27A`** · kicker `#E9D9C6` ·
italic blush `#F2CFC4`.

**Contrast note from the kit render**: the blush flower (`#FFBDA8`) almost disappears on the apricot ground
(`#F0C9AC`); on apricot, peach or blush grounds use the ink or cream wordmark (kit variants), not the brand one.

---

## 10. Type system

| Role | Face | Rules | Source |
|---|---|---|---|
| Display | **Velista 400** (Toni Studio, (c) 2025; self-hosted `public/fonts/Velista.woff2`) | **Unicase: lowercase draws the capitals, so Velista always reads as CAPS** (verified in the font: `a` and `A` share outlines). Glyphs: A-Z, 0-9, `. , ; : ! ? & ' " - ( ) @ # % /` only. **No ₹, no "·", no em dash.** Ad size 64-80px on 1080x1350; max 3 lines; balanced wrap | font file [V]; BRAND.md [R] |
| Editorial turn | **Cormorant Garamond italic** (300-500; the catalogue uses Light Italic) | the lowercase counter-line under a Velista headline: "*three colours, not seven.*" | ads, catalogue [R] |
| Support / labels | **Jost** 300 (support, tracking .08em) and 500 (eyebrows, uppercase, tracking .2-.32em) | uppercase only for the eyebrow; max two support lines + one eyebrow | BRAND.md, upclose [R] |
| Rupee | **Poppins** 400/500 for ₹ | catalogue: "Poppins (for ₹)" | [R] |
| Feed options (NOT yet brand) | Tiro Devanagari Marathi, Rozha One, Yatra One, Kalam (hand), Gotu, Playfair Display italic, DM Serif Display | downloaded to `kit/fonts/`; use only with the owner's sign-off | [this kit] |

Note BRAND.md says Velista is "sentence case, never all-caps"; the font cannot do lowercase, and every shipped piece
(ads, catalogue, exhibition, site box band) sets it in caps. Treat Velista as caps-only.
Site landmine: many site headings that "say" Velista actually render the sans fallback (design-tokens.md); irrelevant for the feed.
Velista licence terms are not in the repo [U]; it is already used on the site and in every ad.

---

## 11. Logo rules

**The mark**: NAIRA in a high-contrast serif with the I rebuilt as a plain letter and a **flower (traced from the deck,
described as a carnation in BRAND.md) laid over the I**, with a thin knock-out gap between flower and letter. Vector:
`kit/naira-wordmark.svg` (viewBox 0 0 2708 606; letters + flower placed exactly as `NairaWordmark.tsx` places them;
knock-out 10 units, fitted to the site's 4000px footer logo: 96.4% pixel IoU, residue = 1px anti-aliasing).

Colourways that exist in shipped work:
| Mode | Letters | Flower | Where |
|---|---|---|---|
| Brand | sage `#99B4AF` | blush `#FFBDA8` | header, bag, catalogue, profile picture |
| Cream on dark | cream `#F6EFE6`/`#FFF8F5` | blush | exhibition poster, site footer (cream on sage) |
| Ink | ink | ink | box lid print, some ads |
| Ink + blush, sage-deep + blush | | | catalogue modes (`build.py logo()`) |

Rules found [R]:
- **Once per frame.** "Logo shown twice" was a judged violation (upclose).
- The stand-alone flower may appear **only as a 6-15% ghost**, and **never at a similar size beside the wordmark**.
- Ad system: logo bottom-left (or bottom-centre in brand mode), 5% margin, single colour, ≤8% of canvas width.
- Sage is reserved for the logo lockup in the ad system.
- Never redraw the letters in a font; never use the old 105x24 bitmap (`naira-logo.svg`) - it is blurry at phone scale.
- "NF" monogram (`ig-highlight`/WhatsApp profile kit, ink N + gold F in a gold circle) exists in `marketing-assets/kit` [R]; it is not used in recent work.
- Profile picture today: `marketing-assets/kit/ig-profile-1000x1000.png` = brand wordmark over "FLORE" in Jost on cream [R].

---

## 12. Motifs and illustration assets that exist (all copied into `kit/motifs/`)

| Asset | File | Character |
|---|---|---|
| The flower (I-flower) | `kit/naira-flower.svg`, `naira-flower-blush.svg` | flat, five shapes: two leaves, stem with low leaf, the bloom. The brand's one drawn mark |
| Watercolour sprigs | `motifs/botanical/leaf-sprig-1.png`, `leaf-sprig-2.png` (2048px, transparent) | soft green leaves + tiny orange/pink blossoms; the bag's repeat |
| Site vine sprig | `motifs/botanical/site-vine-sprig.webp` | the website's thin flowering vine |
| Tulips (vector, from the bag) | `motifs/botanical/tulip-open.svg`, `tulip-bud.svg`, `tulip-leaf.svg`, `tulip-leaf-curl.svg`, `tulip-cluster-{tl,tr,br,bl}.svg` | flat coral tulips + sage blades with a cream vein; the closest thing the brand has to PTAT's flat-illustration motif |
| Paisley | `motifs/pattern/site-paisley-lilac-gold.webp` | lilac + gold paisley, Indian, from the site's Philosophy band |
| Hibiscus + grid | `motifs/pattern/site-hibiscus-grid.webp` | red hibiscus, dark leaves, black grid; couture side, louder |
| Lace florals | `motifs/pattern/site-lace-florals.webp` | faint beige line florals |
| Box + ring renders | `motifs/box/*` | the blush box (3/4 view), lid print, solitaire render gold/silver |
| Logo bitmaps | `motifs/logo/*` | marketing-kit PNG, footer logo (cream + blush, 1642px), site 1920 webp, bag-traced PNG + vector JSON |
| Photo cut-outs | `motifs/photo-cutouts/exhibition-stall-cutout.png` (1932x1937, transparent), `site-about-founder-vandana.webp` | real people, real stall |
| Ad devices already built (not files, ideas) | dimension line ("SHOWN LARGER."), loupe circle, Venn, prism diagram, envelope, museum label, pinked swatch, thread line, sizer rings, ghost numeral, pattern key, care label, ticker strip, specimen sheet, giant numeral, price ladder | `naira-campaign-upclose/PLAN.md`, `naira-ads/README.md` |
| Site ornaments | gold sparkle (4-point star `M6 0L7.5 4.5L12 6...`), gold hairlines and dots, falling blush/sage petals (`HeroPetals.tsx`), "№ 24 · Volume One · Spring · MMXXVI" mastheads | site [V] |

Not found in either repo: the brand deck PDF, the Higgsfield plate originals (they live in an earlier session
scratchpad), raw product photography folders, any hand-drawn illustration set. Product photos are on the Shopify CDN
(`cdn.shopify.com/s/files/1/0680/9606/5698/...`, listed per piece in `src/data/jewellerySnapshot.ts`).

---

## 13. Tone of voice

House rules (design-tokens.md, "Invariants") [V]: **quiet-luxury voice, Indian English, no exclamation marks, no em
dashes in user-visible copy.** (One owner-approved exception: "SITEWIDE SALE LIVE TODAY!".)

The grammar that won in ads (upclose PLAN) [R]: **one Velista line + one lowercase Cormorant turn**, both ending in a
full stop; then the piece named at its price with its exact material line in a quiet Jost caption; the primary text
tells that piece's own story and closes on "made to stay gold." (gold pieces) or "NAIRA Petite." (rhodium).
Evidence: "finished to be seen up close" beat "daily wear" 3.8 to 2.2 add-to-carts per ₹1,000 (p≈0.002), 10 orders to 2.

Real lines, quoted (sources in brackets):

Headline + turn pairs (ads, `naira-campaign-upclose/PLAN.md`, `naira-ads/build/ads.json`):
- "ALMOST A RAINBOW. / *three colours, not seven.*"
- "NAIRA, REARRANGED / A RAIN. / *wear it in one.*"
- "THE KING FELL. / *the hoops stayed.*"
- "*you'll know them by the weave.*"
- "*from a house that sews.*"
- "SHOWN LARGER. / *than they are.*"
- "ONE WARM NOTE. / *the rest stays cool.*"
- "NO TWO ALIKE. / *nine pearls, nine shapes.*"
- "WORN, / *not saved.*"
- "ONE LEFT PLAIN. / *on purpose.*"
- "OPENWORK, / *like lace.*"
- "ONE LINK / *dressed up.*"
- "ONE TO GIVE. / *one to keep.*"
- "NAVRATRI / NINE NIGHTS. / *nine hearts.*"
- "EMERALD GREEN, / *not emerald.*"
- "THE SAME PEARLS, / *twice.*"
- "ONE PAIR, ALL SEASON. / *she kept them on.*"
- "YOU DON'T KNOW HER SIZE. / *it adjusts from size 6 to 8.*"
- "KARWA CHAUTH / YOU AND ME. / *two stones that don't match.*"
- "DIWALI / FESTIVAL OF LIGHTS. / *it brought its own.*"
- "DIWALI LIST / *1. me.*"
- "BHAI DOOJ / NOT AN ENVELOPE THIS YEAR. / *a bow she can wear.*"
- "*a line, and a circle.*" · "*the care label is short.*" · "*woman with a pearl drop, 2026.*" · "*it's in our name.*"
- From the 21-creative set: "Every stone brought / its own sun." · "The shadows climb." · "It left / a record." ·
  "Half buried. / Still gold." · "Every price, / in the open." · "Where it starts." · "The light / misbehaves."

Catalogue (`build.py`): "fourteen ways to frame a face." · "for the hand you talk with." · "close to the collarbone." ·
"a wrist, quietly." · "THE LONG AFTERNOON / *light through a cotton blind.*" · "Cream cotton, slow hours and gold that
warms to the skin. The pieces for a whole day: put on with the first coffee, still there at the last light." ·
"STEEL & GOLD / *from the kitchen shelf.*" "The steel tumbler, the tiffin, the chessboard after lunch." ·
"THE RED ROOM / *lit for the festive table.*" "Sealing wax, a red glass, the evening the lamps come out." ·
"Our one cool note." · Editions: "*ripe silk, warm gold.*" "*lilac paper, cool silver.*" "*celadon, a leaf, gold.*" "*where the stone was.*" "*granule by granule.*"

Exhibition poster: "SEE IT UP CLOSE. / *come and say hello.*" · "NAIRA PETITE · EXHIBITION · THIS WEEKEND"
Index: "THE PETITE INDEX *every piece, on one page.*"
Site: "Luxury chic jewellery / *Crafted for the moments you keep.*" (box band) · "Brilliant-cut zircone in an 18K gold
finish." · "Demi-fine everyday pieces she will actually reach for." · "Zircone sets that read fine at wedding-light
distance." · "Tell us who it is for and your budget. We will send back three options with photographs." (Gifting) ·
"A small room for the people who wear us first" (Inner Circle) · "Soft tailoring, pressed flowers, and the long quiet of an Indian afternoon." (home hero)

Instagram, own voice (Aug 2026, jewellery) [V]: "Liquid gold with a pearl at the end of the sentence." ·
"Understated until it moves." · "Gold, caught mid-thought." · "Colour, without asking for permission." ·
"The one you reach for when nothing else is right." · "Made in small numbers, as always." ·
couture (June 2026): "Share a reference, and the sketches follow." · "[ marigold gold · the haldi capsule ]" ·
"[ chiffon · silver thread · garden series ]".

Devices that recur: **bracketed material lines** `[ 18k gold coated · rhodium coated ]`; **middle dots** as separators;
**N° numbering** of capsules and series; Roman-numeral volumes (MMXXVI, "VIII · 01"); lowercase italic turns;
full stops on headlines; the name-anagram "NAIRA → A RAIN".

Older IG voice to retire (Mar-Apr 2026) [V]: emojis, "Shop now from the link in bio!", hashtag walls, celebrity
name-drops ("Nita Ambani kind of presence", "Madhuri's twirl ... Deepika's main character energy"). These break the
current rules and imply endorsement.

---

## 14. Never-list (consolidated)

Truth and law
1. No gold-content claim: never "gold", "18K gold", "solid gold", "real gold" alone. Use "18k gold coated" / "gold tone".
2. No gold wording on rhodium-only pieces; "made to stay gold." never on them.
3. No base-metal claims on images (no "surgical steel", "316L", "stainless", "silver", "925").
4. No "diamond" / "American diamond" on images.
5. Waterproof / tarnish-free / hypoallergenic only for pieces carrying the tag; never on pearl pieces without it; never "swim".
6. No "handmade", "hand-set at our atelier", "made in Nashik" for jewellery until the owner confirms where pieces are made.
7. No "forever", "lifetime".
8. No fabricated scarcity or popularity ("N sold today", "only 2 left" unless live and true at posting, countdowns). India's dark-patterns guidelines name false urgency and false popularity (BRAND.md).
9. No fake reviews; never quote `productReviews.ts`; real reviews only with the customer's yes.
10. No press logos until coverage is confirmed. No "2,500 custom pieces".
11. No delivery dates or order-by lines.
12. No clasp/mechanism description that the listing photos do not show (Toggle = spring ring + pavé gate).
13. No Dhanteras "buy gold" frame; no Dasara gold frame. No contested festival date on an image (Karwa Chauth 28/29 Oct split).
14. No celebrity names or likenesses implying endorsement.

Commerce
15. No code, percentage or "sale" on the image; codes in captions, one code at a time, never stacked.
16. No struck-through MRPs on images (MRPs run 1.4-2.9x price; anchoring against them sits close to the dark-pattern line and fights the anti-discount position).
17. No pre-order piece in a "shop now" frame without saying pre-order; no 1-5-unit piece as a hero.

Visual
18. Radius 0 on brand surfaces (no rounded cards, pills or blobs as containers).
19. Logo once per frame; the flower elsewhere only as a 6-15% ghost.
20. No scrim boxes behind type; darken the ground instead. Contrast ≥ 4.5:1 against the actual pixels.
21. Type never over the product or the scale referent.
22. No off-palette teal `#2E5B60`; no payment-brand colours.
23. AI imagery: never orange/brassy gold, invented halos/pavé, substituted cuts, or a second piece in a one-piece frame (BRAND.md's image laws).
24. Paid-ad never-list (Up Close): **no diya, marigold, rangoli or red-gold; no two Indian cues in one frame**. This applies to the paid campaign; the feed brief deliberately moves toward an Indian-pop register, so treat it as a decision to make openly, not to break silently (see 19).
25. No jokes at tailors' or aunties' expense (dropped in judging).

---

## 15. Performance and audience facts that should shape creative

| Fact | Value | Source |
|---|---|---|
| Sessions in the Instagram in-app browser | about half | CLAUDE.md [R] |
| Orders that are a single piece | two thirds | `promo.ts` [R] |
| Orders 1 Oct | 43 orders, AOV ₹2,198, 1.33 items/order, 6 of 43 over ₹3,000, 42% COD | upclose PLAN [R] |
| Cost per ad order vs break-even | ₹3,320 vs ₹1,047 (≈₹830 from 25 Oct, festive COD returns) | upclose PLAN [R] |
| Best static | Prism Rivière with its own story: 49 add-to-carts at ₹115, ROAS 1.62; the same image with "the demi-fine edit · from ₹899" got 3 add-to-carts | [R] |
| Reels as paid placement | ₹21,368 → 7 orders, ROAS 0.55 (worse than Feed 0.76, Stories 0.84) | [R] |
| Category | offer tiles 22% of category ads, discounts 40-80%, "artisan" in 0 live Indian ads, nobody runs macro, 1 of 24 brands mentions Karwa Chauth | [R] |
| Competitors | GIVA owns silver (86%), CaratLane diamond (71%), Tyaani bridal (42%), Voylla rakhi (75%); Tyaani discounts in 0% of copy and ranks best; GIVA discounts in 80% and ranks second worst. 22,267 "jewellery 50% off" ads vs 228 "demi-fine gift for her" | BRAND.md [R] |
| Product page | 76% of PDP visits saw no second screen (21-24 Sep); `/jewellery` holds 96% of rage clicks | CLAUDE.md [R] |

## 16. Instagram today (@naira.flore, last 25 media, read 25 Oct) [V]
- **Last post: 9 Aug 2026.** No post for about 11 weeks, through Navratri and into Diwali.
- Engagement is low: 8 to 41 likes per post; comments 0-8.
- Best: couture "Haldi capsule, N° 01" (41 likes, 24 Jun); "Lac bone" campaign reel (35 likes, 8 comments, 9 Aug).
- 9 Aug: a batch of ~9 jewellery stills posted within 15 minutes (several with empty captions).
- Mar-Apr 2026: couture reels and influencer carousels (@prackritipavani), emoji- and hashtag-heavy.
- Implication: the 12 posts are effectively a **relaunch of the grid**; the first row is what a new visitor from an ad sees.

## 17. Calendar (from upclose PLAN.md, dates as the plan states them) [R]
Karwa Chauth 28 or 29 Oct (sources split, never put a date on an image) · Dhanteras 6 Nov · **Diwali Sun 8 Nov** ·
Bhai Dooj Wed 11 Nov · festive frames off after 11 Nov · wedding season follows. "From 25 Oct festive COD returns rise."
Paid frames already running this window: C20 "FESTIVAL OF LIGHTS." and C21 "DIWALI LIST / 1. me." (25 Oct-8 Nov),
C22 "NOT AN ENVELOPE THIS YEAR." (1-11 Nov). Organic posts should not duplicate those lines verbatim.

## 18. Contradictions and open questions for the owner
1. **Instagram handle**: the site links `instagram.com/nairaflore/`; the ad account's IG is **@naira.flore**. Which is live and correct? (If `nairaflore` is not the brand's, the site sends people to the wrong profile.)
2. **Where the jewellery is made**: footer/SEO say "crafted in Nashik", "hand-set at our atelier"; BRAND.md implies a sourced factory. Needed before any craft-origin line.
3. **Waterproof**: catalogue "Shower, swim, sweat" vs the site FAQ "Remove pieces before swimming". Pick one.
4. **Base metal**: BRAND.md "316L" for all vs copper alloy on at least one piece.
5. **Ring sizes**: four different statements (see 4.2).
6. **Founder on camera**: is the exhibition-stall woman Vandana, and may she be named and shown in the feed?
7. **Press marquee**: which coverage is real?
8. **Prices** drifted three times in October; which prices hold through Diwali?
9. **Codes on the feed**: may captions name NAIRA10 (the owner removed it from the header)?
10. **"Lac bone"**: what is it (a material, a collection, a shoot)?
11. **CLAUDE.md "₹24,000-44,000"**: a typo to correct.
12. **Velista licence** for social use.
13. **The paid never-list** (no diya/marigold/rangoli) vs the requested Indian-pop feed: confirm the feed may use festive Indian cues.

---

## 19. Design implications for an Instagram feed

**The brief in one tension.** The reference (@projecttteteatete) is maximalist Indian pop: hand-drawn recurring
motifs (a hand holding a lotus, marigold clusters), Devanagari display type, an event series (MILNI) that the grid
re-states in many formats, photo cut-outs collaged into illustrated frames. Naira's shipped identity is the opposite
register: quiet, editorial, cream, one product, Velista caps plus a lowercase italic turn. The answer is not to copy
PTAT's look but to **turn Naira's own assets up**: the brand already owns a drawn flower, flat coral tulips, watercolour
sprigs, a paisley, a blush box, a bottle-green exhibition, four camp palettes, numbered series and a sharp copy voice.

**What makes it Naira, whichever option**
- **The flower is the recurring motif** (PTAT's lotus-hand equivalent). It is the brand's own drawing, it already
  turns in 3D in the header, and "it's in our name". Rules: wordmark once; the flower as a ghost elsewhere, or (owner
  call) promoted to a bold, larger illustrated motif in the feed only. Tulips and sprigs are the supporting cast.
- **Series, not one-offs.** Naira already numbers things: "N° 01", "Volume One · MMXXVI", "VIII · 01", camps, editions,
  "The Petite Index". A 12-post grid can run 2-3 named series (e.g. an "Up Close" macro series, a "From a house that
  sews" couture-meets-jewellery series, a Diwali "list" series), each with a fixed frame so the grid reads as designed.
- **Type stack**: Velista caps headline (no ₹, no "·" in Velista), Cormorant italic turn, Jost eyebrow + caption,
  Jost/Poppins for prices. Optional accent: Tiro Devanagari Marathi for one Marathi/Hindi word per post (Nashik is
  Marathi-speaking; site serves en/hi/mr) - only with sign-off and only words the owner approves. Rozha/Yatra are
  PTAT-adjacent display faces and should be used sparingly if at all.
- **Palette discipline**: build each option from existing families rather than inventing. Two natural splits:
  (a) **identity + illustration** (cream `#FFF8F5`, sage `#99B4AF`, blush `#FFBDA8`, tulip corals, leaf sages, with
  marigold `#E8973A` as the single loud accent), or (b) **the camps** (Apricot, Lilac, Sage edition grounds, the Red Room
  `#4B191A`, exhibition bottle green `#2E4238` with date gold `#E7C27A`). Both keep gold-deep `#B0843A` for hairlines.
- **Product truth stays absolute** even when the art goes loud: one named piece (or a declared pair) per product post,
  correct finish word in brackets, live price, deep-stock pieces only (section 5), no offer on the image.
- **Real people and places** are Naira's edge over PTAT-style illustration: the founder, the Nashik studio, the
  exhibition stall cut-out, hands and ears on Indian skin ("the asset a competitor sourcing the same factory cannot copy").

**Grid mechanics**
- Post at **1080x1350 (4:5)**; the profile grid shows a centre crop to **3:4** (≈1012x1350 of it, ~34px off each side)
  [Instagram behaviour as of 2025; verify]. Keep type and the wordmark inside a 6% side-safe strip (the ad system's rule).
- **12 posts = 4 rows** of 3: enough for two to three series to alternate in a visible rhythm and for the top row to be a
  complete "hello again" after the 11-week gap. 26 Oct to Diwali (8 Nov) is 14 days, Bhai Dooj (11 Nov) 17: 12 posts fit
  a near-daily cadence through the season. (9 posts = 3 rows reads complete too, but leaves no room for both a festive
  arc and an evergreen arc.)
- Carousels carry the depth (the "detailed graphics" ask): specimen sheets, an index page, macro "up close" slides,
  a care label, a price ladder - the devices already proven in ads and catalogue.
- Captions carry what the image may not: the code (one), the piece story, "made to stay gold.", care notes, WhatsApp.
- Half of the audience opens links inside Instagram; the link in bio should go to `/jewellery` or one collection.

**Accessibility and craft checks to keep**
- Contrast ≥ 4.5:1 for every text block against its real background (the ads' `qa2.py` method).
- Blush flower on apricot/peach fails: use the ink or cream wordmark there.
- Sharp corners. Hairlines in gold `#C99A4C`. No scrims.

---

## 20. Kit file index (`/tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed/kit/`)

| File | What |
|---|---|
| `naira-wordmark.svg` | NAIRA vector, letters `currentColor`, flower `var(--naira-flower, currentColor)`, knock-out mask; inline it to recolour |
| `naira-wordmark-brand.svg` / `-cream-blush.svg` / `-ink-blush.svg` / `-ink.svg` / `-cream.svg` | fixed-colour variants for `<img>` use |
| `naira-wordmark-noknockout.svg` | as the site header draws it (no gap) |
| `naira-wordmark-geometry.json` | viewBox, flower box, the two path strings |
| `naira-flower.svg` (currentColor), `naira-flower-blush.svg` | the stand-alone flower, viewBox 0 0 686.8 1000 |
| `tokens.css` | `@font-face` for every font + every palette as CSS custom properties |
| `fonts/` | Velista (woff2 + ttf), Jost VF, Cormorant Garamond VF (roman + italic), Poppins (₹), Tiro Devanagari Marathi, Rozha One, Yatra One, Kalam, Gotu, Playfair Display VF, DM Serif Display; `fonts/bag/` the bag's subset files; `_google-fonts-manifest.json` |
| `motifs/` | botanical (sprigs, vine, 8 tulip SVGs), pattern (paisley, hibiscus grid, lace florals), box (renders), logo (bitmaps + bag vector JSON), photo-cutouts (exhibition stall, founder) |
| `kit-preview.html` / `kit-preview.png` | rendered sheet: wordmark in 5 colourways vs the reference bitmap, flower, every palette with hex, type specimens, motifs |
| `_build/` | `build_svgs.py`, `export_tulips.py`, `fit_viewbox.cjs`, `render.cjs` (Playwright, `NODE_PATH=/opt/node22/lib/node_modules`, launches `/opt/pw-browsers/chromium` with `--allow-file-access-from-files`), `live_catalogue.py` |
| `../research/data/shopify-live-2026-10-25.json` | the live catalogue read today: handle, title, inventory, price, MRP, tag flags |
