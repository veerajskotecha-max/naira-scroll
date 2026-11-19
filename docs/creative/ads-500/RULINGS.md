# Rulings in force for production (19 Nov 2026)

These override `PLAYBOOK.md` wherever the two disagree. The playbook was written before the owner's answers below and before the
live reads of 19 Nov 15:25 UTC.

## 1. Owner decisions

1. **Claims ("Remove any ban").** Waterproof, tarnish-free and hypoallergenic may be said, and water imagery may be shown, for every
   product whose live listing carries the tags Waterproof, Tarnish Free and Hypoallergenic. That is 16 of the 18 in-stock products:
   all except **Pearl Double Halo Studs** and **Monochrome Enamel Hoops**, which get no such claim and no water imagery.
   - Still never: "diamond", "real gold", "solid gold", "gold" or "silver" alone as the metal, "freshwater", "emerald" or "ruby" as a
     noun. Say cubic zirconia, gold tone, silver tone, emerald-green cubic zirconia, shell pearl only where the listing says so.
   - This supersedes PLAYBOOK §4.0 "No water…", §8.1, the water lines of the §5.5 lint and the compliance gate in §7.
   - Evidence to respect: the claim-led W1 "Waterproof, for the wedding" lost (₹3,236, 0 sales) while the texture-led W1 sold 5.
     So a claim works best as a **proof beat** (second beat, chip, callout) or shown by the picture, not as the whole headline.
2. **New pictures only.** Every ad gets its own new Higgsfield picture, generated directly. No existing plate, finished ad, listing
   photo or ads-20 frame is re-used as an ad picture. PLAYBOOK §5.0 (Batch 0) and the re-use plan in §5.4 do not apply.
   One picture per ad; a failed picture is regenerated once at most, with the fix written into the prompt.
3. **Stop when the credits run out.** Higgsfield balance at 15:25 UTC on 19 Nov: **88.46 credits** (it was 200, then 144.46; another
   user or session on the account is also spending). At 2 credits a picture that is about 44 pictures, so about 8 batches of 5.
   Read the balance before every batch; stop when it is under 10.
   **Update 19 Nov, about 16:00 UTC:** the owner added credits; the balance read 202.46 (about 100 pictures). The owner's instruction:
   make the best ads in quantity, one batch after another, each better than the last, with a loop check after every batch that
   finds changes or improvements for the next one, or says none.

## 2. Reads of 19 Nov 15:25 UTC (re-read before every batch)

**Offers (Shopify, all active codes, none automatic):**

| Code | Value | Minimum |
|---|---|---|
| NAIRA10 | 10% off the order | none, any order, reusable |
| BUY2 | 10% off | 2 or more items |
| BUY3 | 20% off | 3 or more items |
| BUY4 | 30% off | 4 or more items |

The offer box may print the verified value, for example "BUY 2 · 10% OFF • BUY 3 · 20% OFF" with "CODES BUY2 · BUY3", or
"CODE NAIRA10 · 10% OFF". No free-shipping discount exists, so never print free shipping. Never print compare-at ("was") prices.

**Stock and price (every variant shown must have 20+):**

| Product | Stock | Price | Claims |
|---|---|---|---|
| Toggle Link Chain | 77 | ₹999 | yes |
| Woven Gold Hoops | 89 | ₹1,049 | yes |
| Brushed Gold Huggies | 58 | ₹699 | yes |
| Verdant Eternity Band | 58 | ₹1,049 | yes (Adjustable tag) |
| Cushion Halo Ring | 45 | ₹999 | yes (Adjustable tag, so "adjustable" may be printed) |
| Prism Rivière Bracelet | 41 | ₹2,399 | yes |
| Verdant Circlet Studs | 32 | ₹899 | yes |
| Halo Curve Ring | 29 | ₹899 | yes (Adjustable tag) |
| Pearl Double Halo Studs | 25 | ₹1,199 | **no** |
| Monochrome Enamel Hoops | 24 | ₹999 | **no** |
| Serpentine Whisper Chain — Silver | 23 | ₹899 | yes |
| Ribbon Bead Bracelet | 21 | ₹699 | yes |
| Serpentine Whisper Chain (gold) | 20 | ₹1,299 | yes |
| Bold Nocturne Drops | 20 | ₹1,299 | yes |

Out (a shown variant is under 20): Triple Coil Wrap Bangle (gold 20 / silver 19; also its turn count is unconfirmed), Baguette
Huggies (crystal 10, emerald 6, amethyst 12, ruby 0), Droplet Open Ring (9 / 11), Marquise Drop Choker (15 / 9).

## 3. Rulings I made where the playbook asked the owner (change any of them by saying so)

- **Faces:** no eyes, no full face. A lips-to-chest crop is allowed (our own best static, F2, is cropped that way). Mirror shots
  only with the phone covering the face.
- **Edit passes:** none. Every picture is generated directly at true size; a picture that is wrong is regenerated, never edited.
- **Toggle Link Chain:** the clasp must match `build/refs/toggle-link-chain__clasp.jpg` (a round ring of about 22 mm and a bar of
  about 15 mm). A Toggle picture that fails this is out.
- **Pearl wording:** the Pearl Double Halo listing does not state the pearl's source, so ads say "pearl" only as part of the
  product name, with "silver tone · cubic zirconia".

## 4. Production format

- Generate at **9:16, 2K** with the subject inside the central 4:5 window (y 14.8%–85.2% of the frame), so one picture makes both
  the Feed ad (1080×1350, the central crop) and the Story/Reels ad (1080×1920, text only between y 270 and 1250).
- Every ad ships as `bNN/<id>_feed.jpg`, `bNN/<id>_story.jpg`, their HTML, and `copy.json` (primary text, headline, description,
  CTA, landing URL with UTMs). Nothing is uploaded to Meta.
- Type: Velista caps, Cormorant Garamond italic, Jost (kit v2). `kit/render.cjs` reports font fallback, text share, text outside
  the safe area and the smallest font. Any fallback or text outside the safe area is a fail.
