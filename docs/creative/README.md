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
| 01 | The craft proof | `frames/01-craft-proof.jpg` | re-shot ×2 — metal, then size |
| 02 | The demonstration | `frames/02-waterproof-demo.jpg` | re-shot ×2 — demo, then buckle station |
| 03 | Actual size | `frames/03-actual-size.jpg` | re-shot — inverted scale proof |
| 04 | On Indian skin | `frames/04-on-indian-skin.jpg` | re-shot — hoop oversized |
| 05 | The clasp as design | `frames/05-clasp-as-design.jpg` | re-shot ×2 — toggle, then gauge |
| 06 | The box as product | `frames/06-box-as-product.jpg` | re-shot — pearl type + missing drop |

Full prompts for each are in the published document.

## The generation system: two references, not one

Set by the brand 19 Aug: prompting uses **two** reference images — the product in Higgsfield slot 1,
an empty **setting plate** in slot 2. That contradicted the standing single-reference law, so it was
tested rather than assumed. Full method and the seven plates: `two-slot-system.md` and `plates/`.

Five control frames, same prompt and same product reference, ratios measured in pixels:

| Frame | Product : referent | rendered / true | accuracy |
|---|---|---|---|
| Stud, one slot | 12 : 9mm described | 0.84 / 1.33 | 63% — **inverted** |
| Stud, two slot on S5 | 12 : 9mm shown | 1.18 / 1.33 | 89% |
| Hoop, one slot | 25 : 9mm described | 2.37 / 2.78 | 85% |
| Hoop, two slot on S5 | 25 : 9mm shown | 1.87 / 2.78 | 67% — compressed |
| Hoop, two slot on S7 | 25 : 11mm shown | 1.98 / 2.27 | 87% — recovered |

The plate **compresses the size range toward its own referent** — it pulled the 12mm stud up and the
25mm hoop down, both toward pod-size. So the rule is not "always use a plate" but **size-match the
plate's referent to the piece**, within roughly 2.5×. Inside that band it holds at 87–89%; one-slot
is erratic at 63–85% and inverted the small piece outright.

The compression is not a two-slot artefact: plate S7, generated from text alone with no reference,
still rendered a 45mm matchstick against an 11mm button at 2.8× instead of 4.1×. Size compression is
general diffusion behaviour; the plate only transmits it.

**Three measured pairs, not a law.** The prompt gains a seventh block — reference roles, assigning
what each slot supplies and what to ignore in each — because otherwise the model blends the frames
and renders the supplier plinth inside the new scene.

## Merged research

`../research/` now holds three consolidated references totalling ~31,000 words: the competitor
corpus (498 creatives), production craft and KPI/kill gates, and the 172-defect audit history.

## Dimension audit (added 19 Aug)

Every frame was re-checked against the **manufacturer figures in each product listing**. Five of six
were wrong on the first build and all six were re-shot.

| SKU | Listed | First build | Corrected |
|---|---|---|---|
| Solitaire Whisper Studs | 12mm head, 7mm centre, rhodium | 9mm/5mm, gold | 12mm/7mm, rhodium |
| Rivière Eternal Necklace | 3mm stones + 12mm flat buckle station | station absent | station present, 4 stones wide |
| Pearl Halo Studs | 12mm tall, CZ above pearl, no halo | 9mm, "halo", pod claimed larger | 12mm, pod correctly shorter |
| Woven Gold Hoops | 25mm across | 30mm | 25mm, compact at lobe |
| Toggle Link Chain | 4mm width, 15mm toggle | 8mm links, 20mm toggle | fine 4mm chain |
| Baroque Shell Bracelet | shell pearls, pearl drop from ring | "freshwater", no drop | shell, drop present |

The inverted scale proof matters most: a cardamom pod is 8–10mm and the stud is 12mm, so the earring
is the larger object — the first frame argued the opposite, in an ad whose whole job is honest sizing.
Nothing in the image looked wrong; only the listing caught it.

## Campaign structure at ₹3,000/day

| Phase | Campaign | Ad set | Daily | Audience |
|---|---|---|---|---|
| Weeks 1–2 | Sales — prospecting | A · Broad | ₹1,500 | Advantage+, women 22–44, metro India |
| Weeks 1–2 | Sales — prospecting | B · Lookalike | ₹1,500 | 1–3% LAL of IG engagers + site visitors |
| Week 3+ | Sales — prospecting | A / B | ₹1,200 / ₹900 | as above |
| Week 3+ | Sales — retargeting | C · Warm | ₹900 | 30-day visitors, ATC, engagers |

Three creatives per ad set. At ₹300 CPM, ₹1,500 buys ~1,670 impressions per ad per day — clears the
1,000-impression read floor inside a day, reaches a usable 3,300 in two. Six creatives read every
2–3 days; twelve clear in about a week. Kill at 2× target CPA, never before 1,000 impressions or 72h.

All routing is to **collections**, never product pages — 5 units per SKU makes PDP routing a dead end.

## Prior-generation audit

400 unique generations audited (26 Jul – 19 Aug): 61% stated a mm figure, but only **6% used a scale
referent**, and **41% rendered at 1K** — too thin for 4:5 feed at full width. Four different model IDs
appear across the history for jobs that requested two.

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

Cost: 2 credits per 2K generation. Fifteen generations produced these six, including the dimension
re-shoot; a further fourteen produced the seven setting plates and the five control frames. Twelve launch creatives with a re-shoot round budgeted is roughly 60 credits.

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
