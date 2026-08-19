# Naira Petite — Paid Social Creative System

Built 19 Aug 2026. Published document:
https://claude.ai/code/artifact/5d4aec9c-e4c3-431d-93ad-e7038b482219

## Position

Across **498 live creatives from six Indian jewellery brands**, not one argues how a piece is
made — no brand uses setting, cut, plating or finishing as a theme. That vocabulary is unclaimed.
Two of the six (Tyaani, Voylla) compete with **zero** discount copy and hold the best median
impression ranks in the set. Naira's ₹899 floor sits inside the Palmonas ₹699 / GIVA ₹999 entry
war, which is unwinnable at this volume.

**Lane:** Tyaani's refusal to discount + Rubans' willingness to show evidence, where the evidence
is craft rather than order counts.

## The arithmetic at ₹3,000

At ₹300 CPM / 1.29% CTR / 0.9% CVR (Luxury & Jewelry, not apparel):

| | |
|---|---|
| Impressions | 10,000 |
| Clicks | 129 |
| Orders | 1.2 |
| Revenue @ ₹1,600 AOV | ₹1,860 → **0.62 ROAS** |

Break-even at ~58% margin needs ~1.7 ROAS = 3.2 orders = 2.5% CVR, nearly 3× benchmark.
**The lever is basket size, not creative.** As a total test pot, ₹3,000 buys **3 creatives read
properly** (~3,000 impressions each) against a 1,000-impression read floor.

## Creative count

**12 launch creatives** = 6 territories × 2 executions. Not 50 SKU sets — advertisers under
$10K/month test ~2.9 creatives/week and ~5% win. Every SKU holds **5 units**, so a winning
creative sells one out in days; all ads route to **collections**, never PDPs (Rubans routes 92%
to collections for exactly this reason).

| Tier | SKUs | New assets |
|---|---|---|
| Hero | 6–8 | 12 |
| Working | ~15 | 0 — promote existing on-body frame |
| Tail | ~28 | 0 — supplier still-life |

## The six territories

| # | Territory | Frame | Status |
|---|---|---|---|
| 01 | The craft proof | `frames/01-craft-proof.jpg` | re-shot (metal was wrong) |
| 02 | The demonstration | `frames/02-waterproof-demo.jpg` | re-shot (demo too weak) |
| 03 | Actual size | `frames/03-actual-size.jpg` | first pass |
| 04 | On Indian skin | `frames/04-on-indian-skin.jpg` | first pass |
| 05 | The clasp as design | `frames/05-clasp-as-design.jpg` | re-shot (toggle drifted) |
| 06 | The box as product | `frames/06-box-as-product.jpg` | first pass |

Full prompts for each are in the published document.

## Production rules learned

1. **The reference governs structure; an explicit colour word overrides it.** Frame 03's prompt
   described the product wrongly and the reference corrected it silently. Frame 01's prompt said
   "warm gold" against a rhodium reference — the colour word won and produced the wrong metal.
   Never state metal colour without looking at the reference.
2. **Read the reference before writing the prompt.** Both first-pass failures came from briefing
   off the product *name*. "Solitaire Whisper Studs" is neither a solitaire nor gold.
3. **Name mechanisms as separate parts.** "Toggle clasp" rendered as a round push clasp; "a
   straight bar passed through an open ring, both parts clearly visible" rendered correctly.

**Connector caveat:** the model served does not always match the model requested — jobs submitted
as `nano_banana_pro` returned as `nano_banana_2`, and `nano_banana_2` returned as
`nano_banana_flash`. Verify frames by eye, not by metadata.

Cost: 2 credits per 2K generation. Nine generations produced these six.

## Gates before spend

- Conversion tracking — at a 5% win rate, measurement is what separates winner from noise
- Basket size — the arithmetic does not close on single-item orders
- Collections built and stocked (Sets currently holds one product)
- Catalogue hygiene — duplicate SKUs across active/draft, three drafts with no image

No fabricated scarcity in any frame. India's dark-patterns guidelines name false urgency and false
popularity specifically. Real scarcity at 5 units/SKU is a genuine asset — but it must be real.

## Limits

Impression rank is a relative cross-library position, not spend. The CPM is a third-party agency
estimate, not Meta-published. CTR is WordStream's US traffic-objective benchmark; CVR is a global
Luxury & Jewelry figure — no India-specific demi-fine benchmark was found and none was invented.
Unit economics assume 58% margin. **No creative here has been tested against live spend.**
