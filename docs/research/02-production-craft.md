# Ad-Production Methodology — Consolidated Reference

Consolidated from four Claude artifacts for the creative team. All four sources were read in full (two required extracting text from JavaScript-rendered artifact bodies — see note below). No document was skipped.

**Source read status**

| # | Document | Status | Note |
|---|---|---|---|
| 1 | Bambi Swim — Ad Production Research | Read in full | Static HTML, returned complete on first fetch |
| 2 | Ad Desk — Naira Flore & Bambi Swim | Read in full | 573 KB; body content is rendered client-side from a 510 KB JS bundle (a 345-entry Q&A knowledge base + a `BRIEFING` object + account-data constants). Parsed all 345 KB entries programmatically; every entry quoted below is verbatim from that parse. |
| 3 | The Indian Demi-Fine Review Photo — Field Spec | Read in full | Static HTML, all 5 parts + prompt scaffolds + footer captured |
| 4 | Naira Petite · Feed 01 — Lac & Bone | Read in full | Narrative sections returned directly; the 9 shot prompts were rendered from an embedded `application/json` script block, parsed programmatically — all 9 reproduced verbatim below |

Where a figure carries a letter grade (V / A / B / C / L), that grade is the Ad Desk tool's own evidence-weight system — reproduced in full in §0 below, since it is the most rigorous confidence taxonomy across all four sources and the task explicitly asks for evidence weight to travel with each claim.

---

## 0. Evidence-grading key (from Ad Desk)

The Ad Desk tool grades every claim in its knowledge base on a five-point scale. This key is carried through the tables below wherever a claim originates from that document.

| Grade | Label | Meaning |
|---|---|---|
| **V** | Verified | Pulled directly from a live Meta Ads connector response, 30 Jul 2026 |
| **A** | Meta / large dataset | Meta first-party data, or a study with a disclosed sample |
| **L** | Ad Library | Observed live in the Meta Ad Library on 30 Jul 2026 (competitor-ad observation, not a lab result) |
| **B** | Practitioner | A named source with a stated method, but not first-party or large-sample |
| **C** | Unverified | Agency assertion with no disclosed method — "treat as a hypothesis" |

The tool's own standing caveat, reproduced verbatim because it governs how every number below should be used:

> "EVIDENCE CAVEATS — read before acting on any number... The research is graded. [C] items are agency assertions with no disclosed method and must not drive budget decisions. The 2026 search index is heavily polluted with AI-written marketing pages that invent precise-sounding benchmarks and cite each other... India CPM and ROAS benchmark ranges differ by up to 10x across sources. Use them as sanity checks, never as targets. Build your own baseline from your own account... If you disagree with a conclusion here, say so and show the arithmetic. Do not simply agree with the framing."

The Bambi Swim document uses its own, looser three-tier vocabulary for the same idea: **Measured** (a real dataset), **Observed** (seen directly in competitor material), and **Rejected** (untraceable to a primary source — explicitly not used). Both grading systems are preserved as-is per source below rather than merged, since they come from different tools with different rigor.

---

## 1. Script / Creative Structure Frameworks

### 1.1 The core beat structure (Bambi Swim doc)

> "Six independently-authored frameworks describe the same script skeleton with only cosmetic differences: **hook (0–3s) → problem → product → proof → CTA in the final 3–5 seconds**. Beat counts vary; the 3-second hook window and closing CTA don't. That externally validates the 5-beat structure already written."

Evidence weight: cross-source recurrence across six independent authors (Bambi doc's own standard for confidence, not a numeric dataset — closest to Ad Desk's "B/practitioner" tier, elevated by consensus).

The sharpest single insight found in that pass, source-attributed:

> "the problem is rarely the garment itself — it is the moment the garment fails" — CKStudio

Applied rule: **write the moment (slipping strap, colour fade, a fit mismatch discovered at the worst moment), not the feature.**

### 1.2 Structural and technical rules (Ad Desk KB, graded)

| Rule | Detail | Grade | Source |
|---|---|---|---|
| One ad set, many creatives | Meta's internal test: **one ad set with 25 diverse creatives produced 17% more conversions at 16% lower cost** than five ad sets of five creatives each. Splitting creatives across ad sets splits the optimisation signal. | A | Meta internal test |
| Test-reading ladder | Read metrics as a ladder: **hook rate first** (stabilises at 2,000–3,000 impressions) → **hold rate** → **click-through** → **cost per purchase**. "If Meta will not spend on a creative, that is the verdict." | A | Ad Desk |
| Native format, not re-crop | Reels ads built **native 9:16 with audio, key elements inside the safe zone, cost 34.5% less per result** than image ads on Reels. Vertical sound-on video: **4.8% lower CPA, 5.1% higher CTR, 2.9% higher conversion**. Music + voiceover together scores **15 points higher** on positive response than silent. | A | Meta first-party |
| Safe zone | Keep text/logos/key elements out of **top 14%, bottom 35%, each side 6%**. On 1080×1920 that's y=269–1248 — a usable band of ~51% of frame height, 88% of width. | A | Meta Business Help Centre |
| Six moves for editorial→Reels (Naira-specific) | 1. Shoot 9:16 natively or reframe by hand — never auto-crop. 2. Move the money shot to frame one (editorial builds; Reels front-loads). 3. Cut on motion every 1.5–2.5s. 4. One text hook, 3–6 words, held 1.5s, own serif not Meta default. 5. Design for sound-off with burned-in captions, but still design the audio. 6. Put one deliberately imperfect phone-shot cut in every batch (a hanger, a dupatta adjustment) — "costs no extra shoot time and is your hook-rate insurance." | B | Ad Desk |
| Trending audio is legally blocked | Meta's music licences don't cover commercial use in paid ads; boosting a Reel on trending audio is blocked and tracks get auto-muted. Fix: shoot once, publish organic on the trend, cut a paid version with Meta Sound Collection/Soundtrack+; **voiceover is the loophole** — licence-free and the higher-scoring option anyway. | A | Ad Desk |
| Video length by brand | No Meta-published number, but sources cluster: **under 15s for prospecting** has highest completion/lowest CPM; **15–30s** is the Reels working range (room for hook, demo, CTA). Practical split: **Bambi 12–20s** (impulse, montage grammar); **Naira Flore 18–30s** (needs room for craft detail and a justification beat). On-screen text: **one idea, ≤6 words** — copy under 50 characters had the strongest 30-day survival rate in the largest corpus available. | B | Ad Desk |
| Production cadence | At <$10K/month spend: **~2.8 new creatives/week, 3.8% hit rate** (≈1 winner per 25 ads). Mix **60–70% static / 30–40% video** — a static takes 30 min vs 4–8 hrs for video, "how a small account reaches volume at all." Ignore "15–20 new ads/week" advice — calibrated for $30K+/month accounts. | A | Ad Desk |
| Format choice | Two disclosed samples agree statics dominate: **55.6% of all ads are static (64.8% among DTC brands)** — 67,852 ads across 106 DTC/consumer brands (Curtis Howland). Hit rate by format (578,750 creatives, Motion 2026): **text-only 11.60%, product image+text 8.75%, UGC-style 7.56%** — all above the 5–8% average; the expensive lookbook video is not the format the data favours. | A | Curtis Howland / Motion |

### 1.3 CTA placement (measured — Wistia, via Bambi doc)

| Placement | Engagement rate |
|---|---|
| Mid-roll CTA | **16.95%** |
| End CTA | **10.98%** |
| Pre-roll CTA | **3.15%** |

Grade: Measured (Wistia dataset). This is the strongest single piece of evidence on *where* inside a script the call-to-action should sit — mid-roll beats end beats pre-roll by a wide margin.

### 1.4 Script/angle output as applied to the two live brands

Both documents show the framework being *applied*, not just described — useful as worked examples of the beat structure in practice.

**Naira Flore — 10 creative angles run through the Ad Library white-space findings (Ad Desk, grade L for the competitive gaps, angle-writing itself ungraded):**
1. The measurement film — *"Your size isn't a letter. It's eleven measurements."*
2. Four functions, one suitcase — *"Four functions. She packed three pieces."*
3. The date counter — *"There are four wedding dates in November. Yours is one of them."*
4. An evergreen carousel, season-agnostic copy, built to run 90 days untouched.
5. Named hands — *"This neckline takes him nine hours."*
6. The whole look, garment and jewellery together.
7. *"The best compliment is the one that doesn't mention the label."*
8. Three ways to wear it.
9. *"We stitch to you, so there is nothing to send back."*
10. An always-on catalog with a descriptive clause per card instead of a price.

**Bambi Swim — 10 angles constrained to the no-returns policy (Ad Desk):**
1. Same suit, three bodies — *"Same suit. Size S, M and L. Look."*
2. Sarong-forward — *"Poolside version. Family-lunch version. Same price."*
3. Booking-season capture — *"You booked in July. You'll pack in December."*
4. Trousseau/honeymoon — *"Getting married this winter?"*
5. Fit proof in fabric only, no body in frame.
6. Exchange promise (once policy changes) — *"Wrong size? Send it back."*
7. Pool not beach, Apr–Jun — *"You don't need a holiday. You have a building."*
8. Evidenced scarcity — a real waitlist counter, not an assertion.
9. Delivered-before-you-fly.
10. The wet test — *"Fully lined. Doesn't go see-through."*

Note attached in-source: angles 5, 6, 8, 9 need **no body imagery at all**, so carry zero ad-policy risk — a deliberate design constraint, not an accident.

---

## 2. Every Measured Finding

Combined from both documents. Number / source / confidence in every row, exactly as stated.

### 2.1 Hook types and CAC/CPA

| Finding | Source | Confidence |
|---|---|---|
| Direct-contradiction hooks (*"Stop buying…"*) cut CAC **25–40%** on cold traffic | 52-DTC-account study | Measured (Bambi doc) / Grade B (Ad Desk) |
| Objection-first hooks (*"I almost didn't buy this"*) cut CAC **15–25%**; explicitly best archetype for **considered purchases** | Same 52-account study | Measured / Grade B |
| Comment-style overlay and problem-acknowledgment hooks each cut CAC **10–20%** | Same study | Measured / Grade B |
| Benefit-led aspiration is the **baseline, not the winner** — plateaued accounts are usually leading with aspiration to cold audiences | Same study | Measured / Grade B |
| Andie Swim ad programme cut CPA **48%** | QuickFrame case study | Measured, swimwear-specific |
| Andie Swim's top hook leans on **"free shipping and returns"** — precisely what Bambi (no returns) cannot say | Same case study | Measured — but noted as a lever unavailable to Bambi |

### 2.2 Hook rate, hold rate, CTR benchmarks

| Metric | Benchmark | Source / confidence |
|---|---|---|
| Hook rate | Kill **below 20–25%**; good **30%+**; elite **40%+**. Stabilises at **2,000–3,000 impressions**, callable in a day. Runs structurally lower on Reels/Stories than in-feed — never compare across placements. Fatigues fast: proven hooks drop **~37% after 7 days**. | Ad Desk, Grade A/B |
| Hold rate | Formula = **15-second plays ÷ 3-second plays** (NOT ÷ impressions). Bands: **<30% weak, 40–50% average, >60% strong**. Warning: the widely repeated "25% is good" figure almost certainly uses a different denominator — can differ by 20 points on the same ad depending which is used. | Ad Desk (Motion's published bands) |
| Impressions needed for a reliable read | Motion: run ≥3 days and reach **2,000 impressions, 50–100 clicks, or 3–5 purchases** before judging. Meta's own A/B doc: confidence is not meaningful below **100 observed events**; treats 65% confidence as a win. At 30% hook rate, 2,000 impressions gives ±2pp (fine); at 1.5% CTR the same 2,000 impressions gives ±0.5pp, so 1.0% and 2.0% are indistinguishable — need **~10,000 impressions** before CTR reliably separates two ads. | Ad Desk, Grade B |
| Do hook rates differ by placement (Reels/Stories/Feed)? | **No trustworthy figure exists.** Confident-looking tables claiming Reels 24–36% / Feed 18–28% / Stories 22–32% circulate alongside the *exact opposite* claim — both stated with no disclosed sample. Segment your own account instead. | Ad Desk, Grade C — explicitly rejected as unusable |
| India-specific creative benchmarks | **None exist with a disclosed sample.** What Meta does publish is *audience* research, not creative-performance research: Ipsos/Meta Sept 2025, 3,500+ respondents/33 centres — 95% watch Reels daily, 80% discover brands on Meta, Reels ads show 2× top-of-mind recall and 4× message association vs long-form video. Useful for format choice, useless as a hook-rate target. | Ad Desk, Grade A (for the Ipsos data) / explicit "do not use" for the fabricated 340-account benchmarking-tool site |

### 2.3 Demo vs. narrate

| Finding | Number | Source |
|---|---|---|
| Zivame | Demo format: **54%** (of what — share of top-performing creative type, per Bambi doc's own framing) | Bambi doc |
| Cupshe | Split-screen format: **24%** | Bambi doc |
| Shapellx | Demo **26%**, Before-and-After **21%**, across **833 live ads** | Motion public ad library, "Observed" |
| Cross-check | "Shapellx's Demo-26% independently reinforces Zivame's Demo-54% and Cupshe's Split-Screen-24%. **Four unrelated datasets now say the same thing: demonstrate and compare, don't narrate.**" | Bambi doc synthesis |
| UGC vs. studio — circulating claims | "UGC at 1.8% CTR vs 1.1% studio", "2–4× higher CTR", "30–60% lower CAC", "48% click lift inside Advantage+" | **All unverified** — traced to vendors publishing their own case studies recycling each other's numbers, no primary source (Ad Desk, Grade C) |
| UGC vs. studio — what actually survives scrutiny | Motion's 2026 dataset (578,750 creatives / 6,015 accounts): **UGC hit rate 7.56%** — good, but *below* text-only statics (11.60%) and product-image-with-text (8.75%). Separately: face-to-camera creator hooks get **2.3× the 15-second view rate** of product-only ads; hybrid accounts beat pure strategies either way. | Ad Desk, Grade A for the Motion figures |
| Founder-led as the "underrated middle" | For Naira Flore: *"a founder explaining why a print exists is authentic and on-brand in a way a paid creator's delivery never will be."* Suggested content-source split: **Naira ~50% editorial / 30% founder-led / 20% real customer; Bambi ~70% creator-led.** | Ad Desk, B |

### 2.4 Fit, sizing, returns mechanics

| Finding | Number | Source |
|---|---|---|
| Sizing drives apparel returns | **~52%** of apparel returns | Fit Analytics / ARMEDANGELS |
| Fit-quiz lift | **+29.9% CVR, +47% AOV** | Fit Analytics / ARMEDANGELS — flagged explicitly as **vendor case study**, not independent |
| Realistic return-reduction from fit tooling | **2–10% off returns** — "well below the 30–40% vendors advertise." Conversion lift is the more reliable win than return reduction. | Ad Desk / Bambi doc, B |
| No human model / insufficient sizing info | **21%** of apparel sites have no human model; **82%** lack sufficient sizing information | Independently-tested finding cited in Ad Desk |
| COD return-to-origin (RTO) vs prepaid | RTO runs **25–40%** on COD vs **under 5%** on prepaid | Ad Desk, B |
| India's blended online-apparel return rate | **25–40%** | Ad Desk (used in "what can I pay to acquire a customer" arithmetic) |
| Swimwear return rate — the *correct* sourced number | **21.6%** (Loop Returns) — the frequently-quoted **"40% swimwear return rate" attributed to Statista is not a real Statista figure** | Ad Desk CAVEATS — explicit correction, see §9 |

### 2.5 Kill rules and fatigue signals

| Rule | Detail | Source |
|---|---|---|
| Bambi doc's original kill rule | **2× CPA** | Superseded — see §3 |
| Bambi doc's corrected kill rule | **2× CPA + a floor**: never kill before **~1,000 impressions / 48–72 hours**, "otherwise noise gets killed as signal" | Corrected in the KPI pass — see §3 |
| Ad Desk's gated kill sequence (both brands) | Run gates in order, stop at first failure: **hook rate <20% at 5,000 impressions → kill, no exceptions. Outbound CTR <0.6% at 8,000 impressions → kill. Add-to-cart rate <3% at 300 landing-page views → the problem is the offer/page, not the ad. Zero purchases at 3× target CPA → kill.** Confident read needs **5–10× target CPA spent**. | Ad Desk, B |
| Applied kill-spend thresholds | **Naira Flore:** ₹8,000 to early-kill, ₹13,000–27,000 for confidence. **Bambi:** ₹2,150 to early-kill, ₹3,600–7,100 for confidence. | Ad Desk, derived from each brand's target CPA |
| Rule of asymmetry | "Kill on the upper-funnel gates, scale only on the purchase gates — **a 40% hook rate with a 2% add-to-cart rate is a beautiful ad for the wrong product.**" | Ad Desk |
| Fatigue signals (act when they compound, not on one alone) | 7-day **frequency >3.5** (degradation starts 2.5, cliff at 4.0); **CTR down >25%** from week-one peak; **CPM up 10–35%**. Earliest detectable signal: declining CTR at flat impressions, **3–5 days before** frequency crosses. If CPM rises but CTR flat → auction pressure (check the calendar), not creative fatigue. | Ad Desk, B |
| Effective creative lifespan | Compressed to **2–4 weeks** | Ad Desk |
| Ad-fatigue "circulating framework" (explicitly flagged unverified) | Frequency 2.5+ causes decline on cold; first-time-impression ratio <50% on prospecting = saturation; CPM drift >18% over 2 weeks = de-prioritisation; CTR down 10–15% WoW = warning, 40% = pause | Ad Desk, Grade C — "no sample, no date range, no method for any threshold... use as starting defaults to calibrate against your own account, not as facts" |
| Ad lifespan on Meta (large dataset) | Median **4.0 days**, mean **52.4 days**, **29.8%** of ads survive 30+ days. By format, 30-day survival: **carousel 39.9%, video 26.2%, single image 23.3%**. | AdSpyder — 400M ads / 55M Meta ads since 2012, Ad Desk Grade A-adjacent (large disclosed sample, vendor-run) |
| Ad-set overlap / duplication is not a real test | Meta's auction only enters one of your own overlapping ad sets — "its docs say the ad with the highest total value... the others are simply not considered." A duplicated ad set never gets even impressions. | Ad Desk, A |
| Winners are rare — budget for it | Motion 2026: **578,750 creatives / 6,015 accounts / $1.29B spend.** A "winner" = spends ≥10× the account's median single-ad spend. Hit rate **3.8%** under $10K/mo rising to **8.2%** above $1M/mo. Overall **5–8%** of ads win; **~6%** of ads absorb the majority of spend; **roughly half** of all ads never get meaningful spend. At 3 ads/week, expect **one winner roughly every two months.** | Ad Desk, A |

### 2.6 Naira Flore's own verified account numbers (grade V — pulled live, 30 Jul 2026)

| Metric | Value |
|---|---|
| Total spend | **₹55,539.60** (28 Feb–30 Jul 2026) |
| Impressions | 2,063,470 |
| Clicks | 178,962 (CTR 8.67%) |
| CPM | ₹26.92 |
| Outbound clicks | ~94,830 (outbound CTR 4.60%) |
| Landing-page views | 33,527 (35.4% of outbound clicks arrived) |
| Add-to-carts | 31 (₹1,791.60 cost per ATC) |
| Purchases | **0** — `purchase_roas: null`, no Purchase event ever recorded |
| ATC rate off LPVs | **0.092%**, vs. a healthy 3–8% — "30–80× low" |
| Platform split | Facebook ₹47,863 (86.2%) · Instagram ₹5,842 (10.5%) · Audience Network ₹1,811 · Threads ₹22 · Messenger ₹0.03 |
| Instagram vs Facebook efficiency | Facebook bought **0.19 ATC per ₹1,000**; Instagram bought **1.03** — **5.5× better** — on 10.5% of the budget |
| Facebook Reels waste | ₹17,621 (32% of total budget) → 62,924 clicks → only **1,124 landing-page views** (1.79% arrival rate) |
| Pixel status | Created 10 Mar 2026 while delivery began 28 Feb — 10 days unmeasured. **Zero configured event rules**, no EMQ record, **4 events total in the last 28 days** |

This is the account-level baseline underneath every Naira Flore benchmark and kill-gate number quoted above.

---

## 3. KPI Targets — the corrected table

Straight from the Bambi Swim document, reproduced in full with its stated reasoning for each correction:

| Metric | Was | Now | Why it was corrected |
|---|---|---|---|
| **Thumbstop** | ≥30% | **≥22–25%** | "I'd derived 30% from a *female-only segment* of a jewellery proxy account. Published cold median is 18–28%." |
| **Hold to 15s** | ≥15% | **≥20%** | "Sources flag below 18% as a body-content problem — my bar sat under it." |
| **Link CTR** | ≥1.2% | **1.2–1.5%** | "WordStream apparel 1.29%, US-only. No India apparel benchmark exists." |
| **Kill rule** | 2× CPA | **2× CPA + floor** | "Never before ~1,000 impressions / 48–72h. Otherwise noise gets killed as signal." |

Context that explains *why* the original targets existed at all: the connected Motion analytics account behind this research is a **jewellery brand** (i.e., Naira Flore's own account data, per the Ad Desk document) with **zero purchases in 90 days** — so every KPI target in the Bambi document is explicitly labelled a **craft default**, not a measured swimwear benchmark. The one directly usable signal pulled from that account: **female audiences thumbstopped 34.8% vs. male 20.3%** — which is the actual origin of the since-corrected 30% figure (a female-only segment, generalised too broadly in the first pass).

**Complementary framework (Ad Desk, applied to both brands, not presented as a "correction" but structurally consistent):** hook rate kill <20–25% / good 30%+ / elite 40%+; hold rate <30% weak / 40–50% average / >60% strong (denominator = 15s-plays ÷ 3s-plays, not ÷ impressions — see §2.2 warning); kill-spend gates of 5,000 / 8,000 impressions and 3× / 5–10× target CPA (see §2.5). These numbers are not identical to the Bambi table's thumbstop/hold/CTR bands because they come from a different tool measuring a different quantity (hook rate ≠ thumbstop as separately defined; hold rate's denominator differs from "hold to 15s" as a share of impressions) — treat the two frameworks as parallel and cross-checking, not as the same metric restated.

---

## 4. Asset Audit Methodology (reusable process)

Reverse-engineered from how the Bambi Swim catalogue/asset audit was actually built. Written as a repeatable sequence.

1. **Pull the live catalogue from the store's own data endpoint — never from assumption or a stale export.** The Bambi audit read stock directly from the storefront's catalog endpoint so the advertisability split reflected real-time inventory, not a snapshot.
2. **Split every SKU into stock tiers before any creative work begins.** Four tiers used: **Full stock, Partial, 1 size left, Sold out.** In the Bambi case: 9 SKUs full stock (37.5%), 5 partial (21%), 7 with one size left (29%), 3 sold out (12.5%) — out of 24 total. "You cannot brief an ad against a product with one size left, so this split comes before any creative work."
3. **Identify hero sets/products from the full-stock tier only** — specifically complete, sellable propositions (e.g., a matched top+bottom pair stocked **across the entire size run**, not just "in stock somewhere"). Two hero sets qualified in the Bambi case (Merlot, Malibu Triangle — both XS–XL); a single hero product was separately flagged (Dotty Baby Blue) because its own copy resolved a category-specific anxiety (coverage) inside one SKU.
4. **Audit for a pricing/bundling gap** between assembling a "set" piece-by-piece vs. a pre-built bundle SKU. In the Bambi case, buying Merlot as two separate pieces cost ~₹1,000 more than a comparable pre-built Set SKU — flagged as "the easiest offer in the deck to build."
5. **Copy-bug detection: compare every product's live copy word-for-word against that product's own primary photo.** This is the reusable mechanism — download the image, look at it, and check three things against the copy: (a) **colour** — does the stated colour match the pixels; (b) **garment type/silhouette** — does the description match what the photo shows (a bikini bottom vs. a skirt); (c) **coverage claim** — does a word like "moderate coverage" match what the cut actually shows. Every bug reported was confirmed this way, not inferred from category norms. In the Bambi case this caught: a "rich wine hue" top that is actually pink floral; "chocolate brown and white" described on a navy-and-white product; a bottom described as a floor-length skirt that is in fact a bikini bottom.
6. **Flag coverage/claim mismatches as a legal and reputational exposure, not a copy nitpick, whenever the brand has a no-returns or restricted-returns policy.** Explicit reasoning: "a customer who expected moderate and received cheeky has no remedy... Coverage claims must be audited against the actual garments."
7. **Inventory existing footage/photo assets by category, and score each category against what the planned scripts actually require.** Categories used: video, wet/in-water, movement, body diversity, size comparison, lifestyle stills, UGC/mirror-selfie. In the Bambi case: 86 catalog images downloaded, 57 inspected individually by eye (covering 34 of 35 images across the 9 advertisable SKUs) — video, wet, movement and size-comparison assets were all at **zero**; lifestyle stills sat at 45%, UGC mirror-selfie at 9%.
8. **Explicitly flag which planned scripts are blocked by the missing-asset audit, rather than quietly working around the gap.** "The top-priority script cannot be made from existing assets... The concept stands — it just makes the [missing footage type] a prerequisite, not an optional extra." The stated fix was to schedule one production day covering every missing setup at once (in the Bambi case: wet-opacity demo, movement, fabric macro, body diversity, and vertical creator b-roll in a single shoot day) rather than treating each gap separately — and to run only what the *existing* assets already support (static/carousel) until that day happens.
9. **Separately flag catalogue-infrastructure defects** uncovered incidentally during the audit — e.g. a long-running competitor's dynamic-catalog ad whose title template literally never rendered (`{{product.name}}` still showing live after four months, per the Ad Desk competitor teardown). These are a different failure class from a copy bug (infrastructure, not content) and belong on a separate checklist line.

---

## 5. Demand / Media Calendar and the Cost-vs-Demand Decoupling Argument

### 5.1 Bambi Swim's calendar (India swimwear)

| Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|
| High | High | Med | Med | High | High | Soft | Soft *(now)* | Soft | High | Peak | Peak |

Built by triangulating destination peak seasons, state school calendars, and wedding timing; the heat rating itself is **INFERRED** from those cited facts (source's own caveat).

- **Nov–Feb**: sharp, high-value peak. ~**65%** of Indian weddings fall in this window, alongside honeymoon travel and the Goa/Kerala/Andaman/Maldives seasons.
- **May–Jun**: second peak, driven by state school holidays and Bali travel.
- **Jul–Sep**: monsoon trough (the point the research was written from).

**The decoupling argument, verbatim reasoning:**

> "Nov–Dec is peak demand *and* India's most expensive ad auction. Diwali drives documented CPC spikes of **30–50%**; wedding season — now rivalling Diwali as the year's biggest ad-spend climax, with **~46–48 lakh weddings concentrated 1 Nov–14 Dec** — extends that into **six continuous weeks of inflated CPMs**. And swimwear has no thematic fit with either occasion, so we'd pay festive prices without being able to use festive creative.
>
> Demand and cost decouple in **January**. The wedding cluster ends ~14 Dec and competition collapses, while Maldives runs Dec–Feb, Goa and Kerala run through Feb, and February is a top honeymoon month. **Mid-December through February is the efficiency sweet spot** — that's where acquisition spend belongs, not November."

Explicit self-caveat attached to this argument (important — it is a synthesis, not a measured result):

> "That's my synthesis of two sourced datasets — the demand calendar and the festive cost data — not a measured result. The honest test is CPA, not CPM: a high CPM is worth paying if conversion rises faster than cost. Watch blended CPA weekly through November and be willing to overrule it."

**A structural insight that should change where the calendar is shot at all:**

> "Private and gated-community pools — **150,000 across India's top 50 cities** — are cited as a bigger structural growth driver than beach access." — Euromonitor, via FashionNetwork, 2025

Applied conclusion: shoot pools, terraces and staycations at least as much as beaches — more relatable to the buyer, and dramatically cheaper to produce.

### 5.2 Naira Flore's calendar (India occasionwear/jewellery) — Ad Desk

This is the calendar that applies directly to Naira Flore, and it counter-cycles almost exactly against swim:

> "They counter-cycle almost perfectly, which is the most valuable structural fact about running both. **Naira Flore peaks Oct–Dec** (pre-Diwali 12 Oct–6 Nov, Diwali 8 Nov, then wedding season to mid-Dec) with a **second wave from February 2027 onward** — 2027 carries about **96 auspicious wedding days** against roughly **59 in 2026**, and the density sits in **May (18 dates) and June (16)**, landing after the cheapest CPM months of the year. Bambi peaks in the opposite window. So a single blended budget shifted between the two brands by month is worth more than any bidding optimisation either could achieve alone."

**Auspicious wedding dates, 2026** (Drik Panchang, New Delhi — ~59 total): Feb 12 · Mar 8 · Apr 8 · May 8 · Jun 8 · Jul 4 · **Aug/Sep/Oct: zero** (blocked by Chaturmas) · Nov 4 · Dec 7. Because Chaturmas blocks August through October entirely, the next wedding date from the point of writing (30 Jul 2026) was November 2026. Also: **Adhik Maas ran 17 May–15 Jun 2026 with no permitted weddings at all** — flagged as a drag on wedding demand by **Kalyan Jewellers in its own Q1 FY27 exchange filing.**

**Auspicious wedding dates, 2027** (~96 total, roughly double 2026): Jan 9 · Feb 13 · Mar 7 · Apr 9 · **May 18** · **Jun 16** · Jul 6 · **Aug–Oct: zero** · Nov 11 · Dec 7. May 2027 and June 2027 alone carry 34 of the year's 96 dates. Practical consequence: "buying for a May 2027 wedding starts landing from around February 2027, so your winter 2026 cash has to survive long enough to fund that inventory."

**Cheapest month:** February — "the largest India dataset available puts the annual CPM and CPC low in February... February 2027 carries nine muhurat dates — the most of any month in the year — in the cheapest month observed, which makes it Naira Flore's single best ROAS opportunity." The stated strategic implication is about *sequencing*, not just budget: "half of everything you produce will never earn meaningful spend, so you want that attrition happening in a cheap month, not in October when inventory is expensive."

**What to do in the trough (August–September, the point both documents were written from):**

> "Build, at the cheapest CPMs of the year. For Naira Flore this is the window to fix the pixel, relink Instagram, and produce and test the festive creative library... Occasion creative lead times run weeks, not days. For Bambi, prospect now against the honeymoon-booking wave, build the Instagram engagers audience, and fix the returns policy before the Oct–Feb concentration."

**The honest urgency mechanic this calendar licenses (Naira-specific, and stated as currently unused by the whole competitive set):**

> "The wedding date and your stitching lead time... 'Order by [date] and it reaches you before the sangeet' is true, verifiable and useful, where 'Limited Stock Available' is false for a made-to-order house and forfeits the credibility of the real deadline. The 2026 calendar makes it sharper: only 4 auspicious wedding dates in November and 7 in December, so demand piles onto very few days and the lead-time squeeze is severe. **Bridal fabric lead times stretch from ~25 days off-season to 55–65 days at peak.**"

### 5.3 Cross-document note on the Diwali/wedding CPM claim (see also §9)

The Bambi document states Diwali "drives documented **CPC** spikes of 30–50%" and wedding season brings "six continuous weeks of **inflated CPMs**" (no number attached to the CPM figure). The Ad Desk document separately and explicitly **flags and downgrades** the more extreme, commonly-circulated version of this same genre of claim — *"Diwali CPMs triple"* — to Grade C ("unsupported — the only large India dataset shows CPM **falling** Oct→Nov 2025"), and gives its own corrected planning range: **"+25–60% in your own auction, not +200%."** The two documents are not strictly measuring the same thing (CPC vs. CPM), and the Ad Desk's corrected +25–60% range roughly brackets the Bambi document's 30–50% CPC figure rather than contradicting it — but the explicit rejection of the "triples" framing in the Ad Desk document is the more rigorous, dataset-backed position and should govern planning. **INFERRED cross-reference; the two documents were not written to reconcile with each other.**

---

## 6. The Field Spec — what an Indian demi-fine review/product photo must contain

Full reproduction of "The Indian Demi-Fine Review Photo — Field Spec." Method: 2,500 live Palmonas reviews (via the Loox widget endpoint `https://loox.io/widget/Vk-K-0aYJ3/reviews?page=N&rating=R`), 612 photo-attachment ratio records, 28 review images downloaded and inspected directly, plus 333 Giva reviews / 295 AI-written photo descriptions used for composition statistics (Giva skews toward silver/kids/*nazariya* pieces, so its ankle and baby counts run high — **treat the framing split as directional, and the Palmonas-observed detail as literal**, per the source's own caveat).

### 6.1 Headline stats

| Stat | Value |
|---|---|
| Of 5★ reviews carrying a photo | **21.2%** |
| Review photos that are portrait orientation | **79.2%** |
| Review photos showing the box/packaging | **39.3%** |
| Review texts ≤40 characters | **57.4%** |
| Review texts using any emoji | **8.7%** |

### 6.2 Framing (composition, n=295 described photos)

| Configuration | Share |
|---|---|
| Worn on the body (no packaging in frame) | **45.4%** |
| In the open box, set down (flat-lay on a surface) | **29.2%** |
| Holding the open box up (in-hand unboxing) | **9.2%** |
| Product alone on a surface (out of the box) | **7.8%** |
| Held in the hand (no box) | **7.5%** |
| Worn, with the box also in frame | **1.0%** |

Within worn shots, ranked by body part: **ear (70), neck (33), ankle (27), wrist (25), finger (14)**, plus a *nazariya*/kids'-anklet band (12 instances). The crop is characteristically *wrong*: a chin sliced off, an ear shot with half the face out of frame, a neckline shot with an unflattering amount of collarbone/t-shirt — "the framing serves 'here is the thing on me', not composition."

### 6.3 Aspect ratio and orientation (n=612, measured from `data-img-ratio`)

| Ratio | Share |
|---|---|
| 3:4 portrait (1.33 — default phone camera) | **47.5%** |
| 9:16 portrait (1.78 — full-screen mode) | **15.0%** |
| 4:3 landscape (0.75) | **6.4%** |
| Ultra-tall (2.15–2.23 — cropped/screenshot) | **5.1%** |
| Square-ish (0.99–1.00) | **2.8%** |
| 16:9 landscape (0.56) | **1.0%** |

Rolled up: **Portrait 79.2% · landscape 15.2% · square 5.6%.** ~10.3% of photos are taller than 2:1 — hand-cropped or phone-screen captures, and the odd ratio is itself an authenticity signal. Video reviews are overwhelmingly 9:16 (18 of 31 measured). **Rule: generate portrait by default — a 1:1 or 3:2 landscape "product shot" ratio is the fastest way to make an image read as brand-made.**

### 6.4 Lighting — four situations account for nearly the whole observed set, none of them soft studio light

1. **Overhead domestic tube/CFL, mixed white balance** — most common. Cool ceiling light on top of warm lamp/window light: top of frame reads blue-grey, bottom reads amber. Never neutral.
2. **Warm tungsten, underexposed** — heavy orange cast, visible luminance noise in shadows, metal reads brown-gold not yellow-gold. Common in evening unboxing shots.
3. **Hard window daylight** — sharp directional shadow across the surface, blown highlights on the plating. The shadow is often the most prominent shape in the frame.
4. **Flat outdoor overcast** — for outdoor selfies; low contrast, hazy, sky blown to white.

Direct flash is rarer than expected — shows as a hot specular blowout on the plating with a hard black shadow rim behind the piece.

### 6.5 Background and setting — domestic, busy, unchosen

Inventory from the 28 directly-inspected images: **bedsheets/printed fabric** (checked grey/white cotton, beige-pink florals, purple batik, a teal embroidered kurta — often the busiest element in frame, jewellery small against it); **car interiors** (hand on a steering wheel, instrument cluster lit behind; a passenger-seat selfie); **plain painted walls** (a purple wall with peeling paint; a teal wall with a plastic monobloc chair); **public seating** (a blue moulded bench, a stranger's leg, concrete floor); **desks/tables** (a hand on a Marathi-language newspaper; a dark wooden tabletop); **outdoors** (a fort/monument selfie with a parent; trees/overcast sky behind an ear crop); **the lap** (the wearer's own navy-with-yellow-polka-dot pyjamas as the lower third of an unboxing shot).

> "There is almost never a clean sweep, a neutral seamless, or a styled prop surface. When the background *is* plain, it is plain because it is a bare wall or a bathroom counter — not because it was staged. Clutter at the frame edges... is the norm, not the exception."

### 6.6 Image quality

- **Focus misses constantly** — phone macro at 10–15cm hunts and fails (chain sharp, pendant soft; branded card sharper than the piece).
- **Aggressive computational processing** — budget Android HDR: over-sharpened edges with halos, crushed shadows, oversaturated gold; skin smoothed while fabric stays crunchy — "an internally inconsistent look no studio image has."
- **Small files** — originals served at **14–28 KB, ≤500px**, heavily recompressed, JPEG blocking in flat areas.
- **Motion blur/handshake** in low light, especially one-handed shots (other hand wearing the product).
- **Front-camera beautification** on selfies — smoothed skin, brightened eyes, plasticky texture — while the jewellery itself stays small and soft.

### 6.7 The unboxing pattern

Packaging appears in **39.3%** of photos — "far more than a brand would stage" — but almost never as a designed flat-lay.

| Configuration | Share | What it looks like |
|---|---|---|
| Piece inside the open box, set down | **29.2%** | Shot from directly above or a steep tilt; lid behind or beside the base, rarely aligned; surface is a bedsheet, table or sofa arm |
| Open box held up toward camera | **9.2%** | One hand grips the box edge — **thumb and fingertips clearly in frame**; slightly tilted, often soft (one-handed); lap/floor/room visible behind |
| Worn, with box also in shot | **1.0%** | Rare; usually an arm extended, open box resting nearby |

**Recurring furniture of an unboxing shot:** the branded insert card (matte near-black, brand name in light grey caps, two die-cut earring holes + a slot); a black velvet cushion for bracelets; the lid, logo-side up; a grey microfibre polishing cloth pushed to the frame edge; a black fabric pouch, flat and crumpled; a printed card/leaflet (one observed example carried Devanagari text); multiple boxes when several pieces were ordered. Box colours: **red (23), pink/blush (12), white/cream (10), black (6)**.

**Conspicuously absent:** no ribbons in any observed shot; no certificates displayed as the subject; no thank-you notes held to camera; no arranged, symmetrically-fanned "unboxing flat-lay." The box is shot roughly as opened — contents still seated, lid dropped wherever it landed.

### 6.8 Review text register

A third of reviews are one or two words. **Praise is terse; complaint is verbose.**

| Length | Share |
|---|---|
| 1–15 characters | **32.0%** |
| 16–40 characters | **25.4%** |
| 41–100 characters | **25.4%** |
| 101–250 characters | **13.1%** |
| 251+ characters | **4.1%** |

Median 5★ review: **20 characters**. Median 1★ review: **64 characters**, mean 102.

**Measured register markers:** Emoji **8.7%** (❤️ 😍 😊 🥰 👌🙏 🤌, usually appended, occasionally used as spacing); ALL CAPS **0.1%** — "effectively nonexistent" (2 of 2,495 — do not write caps-heavy reviews); Roman-script Hindi/Hinglish **0.9%**, and **14 of those 15 instances sit in 1–3 star reviews** — customers switch to Hindi when angry, not pleased; ellipsis as comma substitute is pervasive ("Looks pretty.... But little bit heavy"); missing space *after* punctuation, present *before* it ("I really liked it ,daily used its very nice"); doubled words/dropped letters ("but the the shining faded", "it broke just in rwo weeks", "sinple, sleek, elegant").

**Rating distribution on the live wall:** 65,272 reviews, 4.6 average — **5★ 80.7% · 4★ 12.9% · 3★ 1.3% · 2★ 0.9% · 1★ 4.2%.** Photo attachment is *highest* on 1-star reviews (28.8%) and lowest on 5-star (21.2%) — "people photograph problems."

**Verbatim sample (5★, reproduced character-for-character):**
- Priya S., Moon Charm Necklace: *"It was amazing the quality & packaging although the delivery was bit slow but I would say it was worth waiting & I loved it❤️"*
- Sunita B., Ekansha Diamond Mangalsutra: *"I really liked it ,daily used its very nice,I wear it every day👌🙏"*
- Sonal W., Crystal Crown Petite Pendant Necklace: *"Nice"*

**Verbatim sample (mild complaint, 3–4★):**
- Swechha S., Square Charm Accent Necklace: *"Its really good but the the shining faded"*
- Manjari J., Studded Pearl Drop Set: *"Design was quite nice but it broke just in rwo weeks"*

**Verbatim sample (1–2★):**
- Kirtika S., Classic Gold Chain Bracelet: *"The color faded after a single hand wash, and now it has turned black. Waste of money"*
- Tasmiya S. (Hinglish), Round Solitaire Necklace: *"Bilkul kala ho rha hai poorana piece bhej diya kya mujhe change karna hai aisa expect nhi kiya tha aap logo se"*
- Srilatha, Square Charm Accent Necklace: *"colour is defferent I ordered white / But I received pink stoned locket"*

Pairing rule stated in-source: for every ten generated reviews — **three** of 1–15 characters, **two or three** of 16–40, **two or three** of 41–100, **one** short paragraph, **at most one** long one. Attach a photo to roughly **one in five**. Emoji in fewer than **one in ten**. No ALL CAPS. A critical review should run longer than positive ones and carry a specific number (days, weeks, a price).

### 6.9 Authenticity tells, ranked (top 5 worth more than everything below combined)

1. **A burned-in phone-camera watermark** — e.g. `REDMI NOTE 8 PRO / AI QUAD CAMERA`, bottom-left, two lines. "No studio image ever has this. It is the single most decisive tell available." Observed directly in 2 of 28 images.
2. **Mirrored text from the front camera** — selfie cameras save un-flipped, so lettering reads backwards. Observed: a mangalsutra selfie with a red printed t-shirt slogan reversed.
3. **A thumb or fingertips gripping the object** — slightly out of focus, nail texture, cuticles, a chipped polish edge. Present in 9.2% of all photos (the held-box configuration).
4. **Split white balance across the frame** — cool ceiling light top, warm lamp/window light below; gold reads greenish in one corner, orange in another. "Uniformly neutral colour is the fastest studio giveaway."
5. **The subject is not the sharpest thing in frame** — the branded insert card is crisper than the pendant; the chain is sharp and the charm is smeared.
6. Unretouched skin at close range — pores, forearm hair, knuckle creases, a cracked heel wearing an anklet.
7. A background busier than the product — batik, florals, an embroidered kurta swamping a 6mm pendant.
8. Non-standard aspect ratio from hand-cropping (e.g. 2.22:1, 500×310) — avoid clean 1:1/4:5/3:2, they read as designed.
9. Domestic clutter at frame edges — a second box, a half-out-of-shot polishing cloth, a stranger's leg.
10. A hard directional shadow — single-source light throwing one dense shape, often bigger than the jewellery itself.
11. Awkward, unflattering crop — a sliced chin, half a face, too much collarbone.
12. Social filter overlays left on — one observed car selfie carries a pink floating-hearts filter.
13. JPEG degradation — blocking in flat wall areas, mosquito noise, shadow banding; files 14–28 KB at ≤500px.
14. The piece tangled/dumped, not arranged — a chain shot in a loose knot where it landed, especially in complaint photos.
15. Motion blur from one-handed shooting — the other hand is wearing the product.

**Anti-tells (any of these flips the read back to "studio" — avoid):** a seamless/gradient backdrop; even, shadowless three-point lighting; the piece perfectly centred and level; a clean 1:1 crop; retouched skin; a styled prop arrangement (ribbon, dried flowers, marble); consistent neutral white balance; edge-to-edge sharpness; artistic-looking bokeh that reads like a fast prime lens rather than phone computational blur.

### 6.10 Prompt scaffolds (application — see also §8 for AI-generation technique)

Four templates matching the four highest-frequency configurations, weighted to the measured distribution:

**A · Worn detail shot — target ~45% of output:**
> "Amateur smartphone photo, 3:4 portrait, shot on a budget Android phone. Close crop of a woman's [wrist / ear / collarbone] wearing a delicate 18k gold-plated [piece]. Indian skin tone, unretouched — visible pores, fine hair, knuckle creases. Shot one-handed indoors under mixed lighting: cool ceiling tube light above, warm lamp light below, inconsistent white balance across the frame. Background is a crumpled printed bedsheet, out of focus and busier than the jewellery. Slight motion blur, over-sharpened HDR edges, mild JPEG compression artifacts. Awkward crop — part of the chin cut off at the top edge. Not a studio photo. No professional lighting."

**B · Held-box unboxing — target ~10%, highest-converting configuration:**
> "Amateur smartphone photo, 3:4 portrait. A woman's hand holds an open cream-white jewellery box up toward the camera — thumb and two fingertips clearly in frame at the left edge, slightly out of focus, natural nails. Inside, a delicate gold [piece] is still seated on a matte near-black branded insert card with two die-cut holes punched in it. Below and behind the box: the woman's lap in navy polka-dot pyjamas, and a cluttered domestic floor. Overhead tube light, cool at the top of the frame and warm at the bottom. The insert card is sharper than the jewellery. Handheld tilt of a few degrees. Low-resolution phone snapshot, not a product photo."

**C · Flat-lay in the open box — target ~29%:**
> "Amateur overhead smartphone photo, 4:3, shot at a slight tilt rather than square-on. An open blush-pink jewellery box sits on a floral bedsheet, lid dropped beside it not aligned. A gold [piece] rests on a black velvet cushion inside. A grey microfibre polishing cloth is pushed to the right edge, half out of frame; a second unopened box sits behind. Warm tungsten room light casting one hard directional shadow across the bedsheet. Slightly underexposed, visible shadow noise, heavy JPEG compression. Casual snapshot."

**D · Front-camera selfie — target ~10%, use sparingly:**
> "Amateur front-camera selfie, 9:16 vertical, taken in a car passenger seat. A young Indian woman looks at the camera wearing a fine gold [piece] at her neck. Front-camera beautification — smoothed skin, slightly plastic texture — while the jewellery stays small and soft in frame. Any text on her t-shirt appears mirrored / reversed. Daylight through the windscreen, blown-out window behind, dashboard visible. Casual, unstyled, phone-quality."

---

## 7. The Lac & Bone Feed Document — art direction, palette, prop vocabulary, shot recipes

Full reproduction of "Naira Petite · Feed 01 — Lac & Bone." All 9 product shots were generated on **Nano Banana Pro at 2K, 1:1**, and the document frames itself as "ready for graphics" (i.e., delivered creative, not a plan).

### 7.1 Why the reference feeds (chessboard jewellery grid, red-organic grid, Zoro Burger red grid) score 10/10 — the five mechanics extracted and reapplied

| Mechanic | Rule |
|---|---|
| 01 — One world, no exceptions | Every tile lives in a single universe (all game pieces, or all red objects) — "not 'a nice photo each.' The world is the brand. Nine unrelated pretty shots read as a stock feed." |
| 02 — A value checkerboard | The reference chess feed alternates black/white tiles — "that's *why* it reads so well at thumbnail size... gives the grid rhythm before anyone sees a product." |
| 03 — Jewellery meets a wrong object | Rings on chess pieces, earrings on chillies, a chain across a mouth. "The wit is the stop. A ring on velvet is a catalogue; a ring inside a rose is a post." |
| 04 — Macro, and body fragments only | Fingertips, one ear, lips — never a full face ("a face makes it a model shot and the product shrinks"). Extreme macro makes a low-price piece "read as an object worth looking at." |
| 05 — Quiet tiles between loud ones | 2–3 tiles carry deliberate negative space. "Without them the grid is noise." |

### 7.2 Palette

| Swatch | Hex | Role |
|---|---|---|
| Oxblood Lac | `#6E1A20` | Deep/loud tiles |
| Near-Black | `#3A0F13` | Deep-tile shadow floor |
| Bone Plaster | `#F2EDE4` | Quiet/bone tiles |
| Warm Gold | `#C2A05A` | Accent |

**Why Lac & Bone (the world's own stated justification, in full):**
- "It's ours, not borrowed. Lac and glass bangles are Indian jewellery craft. It gets the saturated boldness of the red reference feed without copying chess or chillies."
- "It's warm-only. Monsoon scored lowest of the five hero worlds because cool light fights the brand rule. Every light here is warm."
- "Oxblood and bone give the checkerboard. The alternation is structural, not decorative — it is the single biggest reason those reference grids read well small."
- "It carries the craft moat. Wet lacquer, drying plaster, hand-drawn glass, a dented petal. **Provenance texture is ~0% of Indian demi-fine paid social** — this is the open lane."
- "No repeats." — explicitly checked against nine other hero worlds already shot for the brand: **Monsoon, Jaali, Atelier, Herbarium, Silk, Marble+Palm, Honey Lift, on-ear, Pomegranate.**

**Grid structure:** 5 deep (oxblood) tiles, 4 bone tiles, arranged as a checkerboard for thumbnail-scale rhythm. **Posting note: Instagram fills newest-first, so post 9→1 to preserve the intended 1–9 top-left-to-bottom-right reading order.**

### 7.3 The nine shot recipes

Every prompt below is reproduced verbatim — these are the actual, tested, paste-ready Nano Banana Pro prompts, not summaries.

| # | Name | Category | Price | World / tone | Score | SKU |
|---|---|---|---|---|---|---|
| 1 | Molten Bloom Hoops | Earrings | ₹2,949 | Lac Sphere / deep | 9 | JDE0110042 |
| 2 | Serpentine Whisper Chain | Necklaces | ₹2,449 | Plaster Ledge / bone | 8 | YF5144 |
| 3 | Cushion Halo Ring | Rings | ₹1,499 | Fingerprint / deep | 8 | WR20902K8 |
| 4 | Pearl Reverie Bracelet | Bracelets | ₹999 | Raw Silk / bone | 9 | JDB2409013 |
| 5 | Prism Rivière Bracelet | Bracelets | ₹1,049 | Submerged / deep | 9 | JDB201210 |
| 6 | Woven Gold Hoops | Earrings | ₹2,349 | On Ear / bone | 9 | E20267O |
| 7 | Clover Trio Edit | Sets | ₹1,799 | Glass Bangles / deep | 9 | JDS0204301-set |
| 8 | First Light Necklace | Necklaces | ₹1,849 | Cracked Plaster / bone | 8 | YF8439 |
| 9 | Golden Duet Ring | Rings | ₹1,399 | Rose Interior / deep | 8 | JDR0104342 |

**Shot 1 — Molten Bloom Hoops (Lac Sphere).** *Why:* "Opening tile, top-left — the first thing anyone sees. Our single most scroll-stopping product against the most saturated surface in the world. Sets the oxblood immediately." *Check:* hoops still irregular and molten (not a smooth even circle); size unchanged; gold warm not orange; droplet flattened under the metal.
> "A single pair of irregular molten gold hoop earrings resting against a wet, high-gloss oxblood-red lacquered sphere. The hoops are an uneven, hand-poured ribbon of metal, every curve different — the wave must stay irregular and molten, never resolving into a smooth even circle. Preserve the earrings at the identical height, width, proportions and colour shown in the reference; do not enlarge, shrink, restyle or recolour them. Each hoop is 19-21 mm across, about the width of a thumbnail. Honest macro optics: depth of field only a few millimetres, so the near hoop's front edge is sharp and the far curve of the sphere falls soft. Two light sources: a large soft source from the upper left, plus one small hard specular kicker that draws a narrow bright line along the molten ridge of the gold. Warm-neutral gold, never brassy or orange. The lacquer is deeply saturated oxblood with water beading across it — droplets of varying size, two or three merged; where the metal rests it presses a soft contact shadow and flattens the droplet beneath it. Grain of matter: dust motes on the lacquer, micro-scratches in the gloss, faint orange-peel texture in the thick lacquer. Background deep oxblood falling to near-black at the corners — absolutely never sand, tan, beige or golden. Square 1:1 composition, product filling about 45% of the frame, sitting slightly left of centre."

**Shot 2 — Serpentine Whisper Chain (Plaster Ledge).** *Why:* "The first breath. Comes straight after the loudest tile, so it is deliberately the emptiest frame in the grid — one heavy chain, a lot of nothing." *Check:* each link still a distinct flat curb link; link width unchanged; plaster reads chalk-white, never beige.
> "A single heavy curb-link gold chain necklace pouring over the edge of a bone-white lime plaster ledge, part of the chain pooled on the surface and part hanging free into space... Each link is roughly 9 mm wide, about the width of a little fingernail; the chain is 45 cm long... The plaster is chalk bone-white and slightly uneven, with a visible trowel sweep and open pores; the chain's weight presses a faint dark contact shadow into the ledge, and one link has picked up a smear of plaster dust... Background cool bone-white and almost shadowless — absolutely never sand, tan, beige or golden."

**Shot 3 — Cushion Halo Ring (Fingerprint).** *Why:* "Top-right corner, and the grid's first body fragment. Fingerprint ridges at macro are the strongest scale cue we have — this is the tile that proves the ring is ring-sized, not costume." *Check:* halo still unbroken; centre stone ~7mm relative to the nail; skin shows real ridges; band dimples the finger.
> "One cushion-cut halo ring worn on a single fingertip, cropped very tight so only the last knuckle and the nail are visible against a deep oxblood ground... The centre stone is about 7 mm across, roughly the width of the fingernail behind it... Skin rendered honestly at macro: visible fingerprint ridges, the fine dry texture of the cuticle, one small natural imperfection. The band presses very slightly into the finger, dimpling the skin beneath it... No face, no second finger in focus."

**Shot 4 — Pearl Reverie Bracelet (Raw Silk).** *Why:* "Softest tile in the grid and the only textile. Sits directly under the loud opener to cool it down. The pearls give the feed its one non-metal material." *Check:* pearls still lumpy and irregular; two pearls, not three; silk pulled into a trough under the weight.
> "A single gold figaro-link chain bracelet laid across a fold of raw undyed bone silk, with two irregular baroque pearls set into the line of the chain... The larger pearl is about 17 mm long, roughly the width of a thumbnail; the bracelet is 19 cm... The silk is undyed bone with visible slubs and an open weave; the bracelet's weight pulls the silk down into a shallow trough beneath it and one loose fibre has caught in the clasp."

**Shot 5 — Prism Rivière Bracelet (Submerged).** *Why:* "Dead centre — the tile the whole grid is built around, and the one to shoot first. Water is the strongest possible proof of the waterproof claim, and the bent meniscus is the best scale cue in the system." *Check:* stones still a single unbroken row; meniscus visibly bent at the waterline; submerged half refracted and darker.
> "A single tennis bracelet lying half-submerged in a very shallow pool of deep oxblood-tinted water, the near half above the surface and the far half beneath it... Each stone is 3 mm across, roughly the width of a grain of rice; the bracelet is 17.5 cm long... The water is only three or four millimetres deep and deeply tinted oxblood; the bracelet visibly bends the meniscus where it breaks the surface, with water climbing very slightly up the metal, and the submerged stones read darker and optically displaced. Grain of matter: a few fine dust particles floating on the surface, one small air bubble clinging to the clasp..."

**Shot 6 — Woven Gold Hoops (On Ear).** *Why:* "The grid's only worn shot at scale, placed centre-right so a human element sits beside the hero." *Check:* braid still legibly over-under; hoop ~2/3 the ear's height; lobe pulled slightly by the weight; no face visible.
> "A single chunky braided gold hoop earring worn on one ear, shot in tight profile against a bone-white ground, with no face visible — only the ear, the very edge of the jawline and a fall of dark hair... The hoop is about 30 mm across, roughly two-thirds the height of the ear it hangs from... Skin rendered honestly: fine peach fuzz along the lobe, visible pores, and the slight translucency of the earlobe where light passes through it. The weight of the hoop pulls the lobe down very slightly... No face, no eye, no mouth."

**Shot 7 — Clover Trio Edit (Glass Bangles).** *Why:* "Bottom-left corner. The most Indian frame in the grid and the only one with transmitted light — red caustics from the glass give the feed a texture nothing else has. Also our gifting hero." *Check:* pendant still a single bezel-set stone; studs match the pendant; red caustic thrown onto the surface below.
> "A fine gold chain necklace with a single bezel-set solitaire pendant, shown with its matching pair of studs, arranged over a loose stack of deep red Indian glass bangles on a dark ground... The pendant stone is 6 mm across, about the width of a shirt button; the chain is 42 cm... The bangles are translucent deep red hand-drawn glass with tiny internal bubbles and slight variation in thickness; light passes through them and throws a soft red caustic onto the surface below."

**Shot 8 — First Light Necklace (Cracked Plaster).** *Why:* "The second breath and the quietest tile in the bottom row. A mirror-flat chain against dry cracked plaster is the cleanest craft statement in the set — poured metal against something drying." *Check:* chain still seamless and flat (no visible round links); one continuous liquid highlight down its length; chain dips into the crack.
> "A single flat snake-chain necklace coiled loosely on a slab of cracked bone-white lime plaster... The chain is about 3 mm wide, roughly the width of a matchstick... The plaster is chalk bone-white with a genuine drying crack running through it and fine dust settled into the fissure; the chain crosses the crack and dips very slightly into it, and where it rests it has disturbed a little of the dust."

**Shot 9 — Golden Duet Ring (Rose Interior).** *Why:* "Closing tile, bottom-right. The only organic living material in the grid, and the strongest substrate deformation we can get — a dented petal proves weight better than any shadow. Ends the feed on softness." *Check:* two separate bezels of equal size; petal visibly dented under the weight; droplet trapped at the metal-petal contact.
> "A single gold ring set with two clear bezel-set zirconia sitting side by side, resting deep inside the folded inner petals of a dark crimson rose... Each stone is about 13 mm across, roughly the width of a fingernail... The rose is deep crimson, its inner petals velvety and slightly damp, with one petal edge just beginning to darken and curl. The ring's weight presses the petal beneath it into a visible dent, and a single droplet of water sits trapped where the metal meets the petal."

### 7.4 Shooting protocol

**Setup:** Model **Nano Banana Pro**, aspect **1:1**. **1K** for the test pass, **2K** for finals. Slot 1 = the product cut-out; **slots 2 and 3 stay empty** (see §8 — this is the single-reference-image rule). Clear the red billing banner first, "or generation silently blocks."

**Per-shot loop:** hover thumbnail → ✕ to clear the old reference → find the file input → upload the product → find the prompt box → Ctrl+A → Delete → type → find "Generate submit button" → click the ref, never a pixel → wait 35–40s → verify before moving on.

**Verify against reference (checklist):** size and proportion unchanged; colour still warm-neutral, not brassy; countable facts intact (stone count, pearl count); the morph-risk feature survived (e.g. "the braid is still a braid"). Redo if off. Then log the shot and append the prompt to `tested-prompts.md`.

**Sequence:** shoot **5 first** — "it's the centre and sets the water/colour reference." Then **1, 3, 7, 9** (the deep corners). Then the four bone tiles last, matching their plaster to tile 2. Review all nine as a grid before any 2K finals.

**Explicit warning on a second reference image (verbatim, important — this is a live disagreement resolved in the document itself):**

> "You suggested product in slot 1 and the environment as image 2. If that means *describing* the environment in the prompt, that's exactly what these nine do. If it means uploading a second reference image — the project's own Law 1 says don't: **multi-reference destroyed scale before, and the rings came out costume-sized.** It's an expensive failure to repeat across nine shots. Suggestion: shoot all nine single-reference, and if you want the test, run tile 4 (Raw Silk) a second time with a silk swatch in slot 2 and compare. One controlled test, not nine."

---

## 8. AI Image Generation — prompt strategy, fidelity locks, scale technique, tooling, failure modes

Cross-cutting section, drawn from all four documents (Lac & Bone is the primary source for technique; Field Spec supplies a second, distinct application; Ad Desk supplies the platform-side risk layer).

### 8.1 Tooling

**Nano Banana Pro** is the generation model used for all product photography (Lac & Bone). Settings: **1K for the test pass, 2K for finals**, aspect **1:1** for the feed grid. The interface used has a billing banner that must be cleared first or "generation silently blocks" — a stated operational gotcha, not a creative one.

### 8.2 Fidelity-lock language (the standard clause, repeated in every one of the 9 shot prompts)

Every prompt in the Lac & Bone set carries a structurally identical fidelity-lock sentence:

> "Preserve the [item] at the identical [dimension], proportions and colour shown in the reference; do not enlarge, shrink, restyle or recolour [it/them]."

Paired with a **morph-lock** clause naming the specific feature most at risk of drifting during generation — e.g. "the wave must stay irregular and molten, never resolving into a smooth even circle" (hoops); "the halo must stay a continuous unbroken ring of separate small stones, never merging into a solid bezel" (pave ring); "the braid must stay a legible braid and never smooth into a plain solid band" (woven hoop); "the pendant must stay a single small bezel-set stone and never become a cluster or a halo." **This is the reusable pattern: identify the one geometric feature a generative model is most likely to simplify or average away, and lock it by name, every time.**

### 8.3 Scale-lock technique

Every prompt anchors true-to-life size using a familiar real-world object as a ruler, stated as a plain comparison rather than only a millimetre figure:
- "Each hoop is 19-21 mm across, **about the width of a thumbnail**."
- "Each link is roughly 9 mm wide, **about the width of a little fingernail**."
- "The centre stone is about 7 mm across, **roughly the width of the fingernail behind it**."
- "Each stone is 3 mm across, **roughly the width of a grain of rice**."
- "The pendant stone is 6 mm across, **about the width of a shirt button**."
- "The chain is about 3 mm wide, **roughly the width of a matchstick**."

Numeric millimetre specs alone were evidently judged insufficient — the prompts always pair the number with a familiar object precisely to give the model (and the human reviewer checking the output) an intuitive scale anchor.

### 8.4 Two-light-source rule

Every one of the 9 shots specifies exactly two light sources, worded near-identically each time: **one large soft source** (direction varies by shot) **plus one small hard specular kicker** that picks out one specific detail (a molten ridge, a crown facet, a braid strand, a bezel rim). This is a deliberate, repeatable lighting formula, not a one-off description.

### 8.5 "Grain of matter" — the texture-realism rule

Every prompt includes a dedicated micro-texture clause, always introduced with the phrase **"Grain of matter:"**, listing 2–3 specific imperfections appropriate to the surface in that shot — dust motes and micro-scratches on lacquer; plaster pores and a hairline chip; silk fibres and lint; dust particles and an air bubble in water; a petal's velvet nap and subtle veining. This is presented as a named, repeatable step in the prompt template, not incidental description.

### 8.6 Background discipline

Every single prompt in the set ends its background clause with the identical negative constraint: **"absolutely never sand, tan, beige or golden."** This is a hard brand rule enforced at the prompt level in every shot, not just a style preference stated once.

### 8.7 The single-reference-image law (and its failure mode)

Documented rule, stated as "the project's own Law 1": **only one reference image (the product cut-out) goes into generation; the other reference slots stay empty.** The failure mode is documented explicitly and by name: **"multi-reference destroyed scale before, and the rings came out costume-sized."** When a second reference image was proposed (to carry an environment/material reference, e.g. a silk swatch), the correct response documented was to *describe* the environment in the text prompt instead of uploading a second image — and if the multi-reference approach must be tested at all, to run **one controlled A/B test on a single tile**, not risk it across a whole batch. This is the single most important documented AI-generation failure mode across all four sources.

### 8.8 Per-shot production loop (operational, reusable)

1. Hover the reference thumbnail → click ✕ to clear the previous reference.
2. Locate the file input → upload the new product cut-out.
3. Locate the prompt box → Ctrl+A → Delete → type the new prompt.
4. Locate the "Generate" submit button by its accessible reference, **never by pixel position** (explicit instruction — UI elements move).
5. Wait 35–40 seconds.
6. Verify against the reference checklist (below) before moving to the next shot.

### 8.9 Verify-against-reference checklist

Size and proportion unchanged · colour still warm-neutral, not brassy · countable facts intact (stone count, pearl count, etc.) · the specific morph-risk feature named in the prompt survived. **Redo if any check fails.** Log the shot and append the working prompt to a running `tested-prompts.md` file — i.e., a growing prompt library, not one-off prompts thrown away after use.

### 8.10 Shoot sequencing logic

Shoot the **centre/reference tile first** (it sets the colour and material reference for everything after it), then the **loud/corner tiles**, then the **quiet tiles last** (matching their material to the established quiet-tile reference). Review the full set as a grid before committing to final resolution.

### 8.11 A second, distinct generation use case: synthetic review photography (Field Spec)

The Field Spec's four prompt scaffolds (§6.10) are a *different* application of AI image generation from Lac & Bone's hero product shots — they exist to generate photos that pass as **organic customer review photos**, not polished product photography. The technique inverts almost every rule in §8.2–8.6: instead of fidelity-locking a clean subject against a controlled background, the goal is to deliberately reproduce amateur-camera failure modes — mixed white balance, focus misses, JPEG compression, awkward crops, motion blur, front-camera beautification artifacts, and even a mirrored-text failure mode unique to selfie cameras. The two techniques (hero-shot fidelity-lock vs. review-photo authenticity-fake) are complementary halves of the same overall AI-image toolkit for this brand: one produces the ad creative, the other produces the social proof around it. **INFERRED framing — the two documents don't explicitly cross-reference each other, but the complementary relationship follows directly from what each technique targets.**

### 8.12 Platform-side AI risk (Meta/Advantage+ — Ad Desk)

This layer concerns *distribution*-side AI risk (what Meta's ad platform will do to an already-generated image), distinct from *generation*-side risk above:

| Feature | Risk to a hand-made/AI-fidelity-locked image | Grade |
|---|---|---|
| Image Expansion / generative outpainting | "Extends bodies impossibly," mismatches lighting | A |
| Image Animation | Fake zoom/pan/parallax motion on stills | A (live, default-on) |
| Image Enhancement | Shifts graded colour, pushes saturation — "fatal for a muted palette" | A |
| Background Generation | AI backdrops on catalog ads (Meta claims 2–3% conversion lift) | A (first-party claim, unaudited) |
| Muse Image | Meta Superintelligence Labs' first image model; will "restyle existing ad images and pull still frames out of video" via Advantage+ creative — announced 7 Jul 2026, rolling out "in the coming weeks" | A (Meta newsroom) — but notably pulled its Instagram @-mention feature after backlash on 10 Jul, three days after launch: "the company ships fast and walks back later" |
| AI disclosure labels | Since June 2026, using Background Generation / Image Generation / Add Animation auto-stamps an "AI info" label — "the advertiser gets no say." Explicit risk for this brand: "a customer primed to wonder whether the flowers are real is a customer half-lost." | B/first-party per trade reporting |
| Virtual Try-On | Announced for fashion; **no GA date, relevance to jewellery unproven**; "an AI-generated depiction of your product... raises the same fidelity question as every other generative surface" | B — watch item, not a lever |
| Brand Memory | Ingests up to 18 months of ad history to match tone/look when generating variants — "Meta's answer to the exact complaint this desk has." Limited testing from 23 Jun 2026, no firm broader-rollout date. | B — "zero independent evidence it preserves identity for a niche aesthetic like pressed-flower jewellery. Let bigger brands debug it first." |

**Standing operational response:** a maintained "kill-list" of Advantage+ creative enhancements to disable at every campaign launch (since Feb 2026 these arrive pre-ticked by default). Full current list per the Ad Desk's own consolidated verdict: kill Music, 3D Animation, Visual Touch-Ups, Text Improvements, Expand Image, Image Animation, Relevant Comments, Site Links, Add Overlays, Enhance CTA, Dynamic Description, Generate Background, and the catalog-level auto-enhancement switch; watch (do not touch yet) Muse variants, Brand Memory, virtual try-on.

---

## 9. All Stated Limits and Corrections

Every place a document explicitly overturned, downgraded, or flagged its own earlier conclusion — or flagged something as unreachable/unverifiable rather than silently omitting it.

| # | What was corrected / limited | From → To (or the flag itself) | Why | Source |
|---|---|---|---|---|
| 1 | No-returns competitive benchmark | Was: "every serious competitor offers exchanges" (implying Bambi uniquely exposed) → **Now:** benchmarked against the wrong cohort (global swim / India activewear-intimates). Against the correct cohort (India swim specialists), restricted returns is the **category norm** — Bambi, Flirtatious, Nadi Nadi, Amante and Shyaway all offer none; only The Curvves offers real 7-day no-questions returns. | Original comparison used the wrong peer set | Bambi doc |
| 2 | Thumbstop target | ≥30% → **≥22–25%** | Original 30% was derived from a *female-only segment* of a proxy account; published cold median is 18–28% | Bambi doc §3 |
| 3 | Hold-to-15s target | ≥15% → **≥20%** | Sources flag below 18% as a body-content problem; original bar sat under that line | Bambi doc §3 |
| 4 | Link CTR target | ≥1.2% → **1.2–1.5%** | Original was US-only WordStream apparel data; no India apparel benchmark exists | Bambi doc §3 |
| 5 | Kill rule | 2× CPA → **2× CPA + a spend/impression floor (~1,000 impr / 48–72h)** | Without a floor, noise gets killed as if it were signal | Bambi doc §3 |
| 6 | "Diwali CPMs triple" | Explicitly downgraded to Grade C, **"unsupported"** → corrected range **"+25–60% in your own auction, not +200%"** | "The only large India dataset shows CPM **falling** Oct→Nov 2025" | Ad Desk CAVEATS |
| 7 | "Swimwear has a 40% return rate" | Attributed claim → **flagged as not a real Statista figure at all**; the only sourced number is **Loop Returns' 21.6%** | No such Statista publication exists | Ad Desk CAVEATS |
| 8 | Afterpay "+40% AOV" claim | +40% → **the peer-reviewed causal estimate is closer to +10%** | Original figure overstated | Ad Desk CAVEATS |
| 9 | "67% of American women wear plus sizes" | Flagged: **no primary source found** | — | Ad Desk CAVEATS |
| 10 | Dove "$2.5B-to-$4B" revenue claim | Flagged: **circularly cited, unverifiable** | Every citation traces back to another secondary source, never a filing | Ad Desk CAVEATS |
| 11 | India CPM/ROAS benchmarks generally | Flagged: ranges **differ by up to 10× across sources** | "Use them as sanity checks, never as targets. Build your own baseline from your own account." | Ad Desk CAVEATS |
| 12 | A research stream in the Ad Desk build | **Produced a fabricated report and was discarded entirely** | Not detailed further, stated plainly | Ad Desk CAVEATS |
| 13 | A second research stream | **Terminated by a spend limit** before completion | — | Ad Desk CAVEATS |
| 14 | Competitor ad transcripts/hooks/CTA copy (Bambi research) | **None retrievable, none invented** | Motion's competitor ad-library endpoint returns a non-retriable 401 (confirmed 4×); Meta's public Ad Library returns 403. Every quote used instead comes from a brand's own site, Motion brand-level data, or an attributed published source. | Bambi doc, "Honest limits" |
| 15 | Browser automation for competitor research | **Unavailable** | Playwright/Chromium installed and launches, but every navigation dies with `ERR_CONNECTION_RESET` — including against a host `curl` fetches fine, sandbox disabled. Proxy logs show Chromium telemetry but never a CONNECT for page loads — rules out a Meta-specific egress block. "Not fixable from inside the session." | Bambi doc |
| 16 | KPI benchmarks' true origin | The connected Motion account behind all KPI targets is a **jewellery brand** (Naira Flore itself) with **zero purchases in 90 days** — so every target is a **craft default**, not a measured swimwear benchmark. One usable real signal: **female audiences thumbstopped 34.8% vs. male 20.3%.** | Stated plainly rather than presented as swim-specific data | Bambi doc |
| 17 | Instagram follower counts | **Not verifiable for Bambi or any competitor** — every direct fetch returned HTTP 429. **No follower figures appear anywhere in the research.** | Rate-limited | Bambi doc |
| 18 | Google Trends / search seasonality | **No Google Trends data accessible**; seasonality is instead **inferred** from travel-booking lead times | — | Bambi doc |
| 19 | Candidate competitor brands | **Disproved, not assumed**: "Blue Terra Swim" and "Salt Attack" **do not exist**; "Cover Story" and "Tailor and Circus" **don't sell swimwear** | Checked directly rather than left ambiguous | Bambi doc |
| 20 | ASCI advertising-disclosure guidelines | **Could not be retrieved** — the primary PDF returned unparseable binary, both URLs 404'd. Disclosure rules used elsewhere are **secondary-sourced and must be verified before operational reliance**. What *is* confirmed: CCPA penalties reach ₹50 lakh for repeat offences, and claims must be "capable of substantiation" — which is why the wet-opacity script (Bambi) specifically must be shot as a genuine demonstration and dropped on any SKU that fails it. | Bambi doc |
| 21 | Giva photo-composition statistics | **Directional, not literal** — Giva's catalogue skews toward silver/kids/*nazariya* pieces, inflating ankle and baby-jewellery counts; the framing split (§6.2) should be read as directional, while the 28 directly-inspected Palmonas images (lighting, background, quality) are literal | Field Spec, §00 Provenance |
| 22 | Multi-reference AI image generation | **Explicit warning, treated as an already-proven failure, not a hypothesis**: "multi-reference destroyed scale before, and the rings came out costume-sized... an expensive failure to repeat across nine shots" | Lac & Bone doc, §7.4/§8.7 |
| 23 | UGC-superiority statistics ("4× better," "1.8% vs 1.1% CTR," "30–60% lower CAC," "48% Advantage+ lift") | **All unverified** — traced to vendors publishing their own case studies and recycling each other's numbers with no primary source; the vendors quoting them sell UGC production | Ad Desk, Grade C |
| 24 | Body-positive marketing → purchase intent | Common assumption ("body-positive marketing sells") **does not hold**: a 2026 meta-analysis (421 effect sizes / 48 studies) found **negligible effect on purchase intent — the only reliable lift is engagement** — and it may worsen body-image outcomes. What *does* have consistent support: **authenticity disclosure** (retouch-free/no-AI pledges), which lifts perceived honesty and buying intent. Every documented backfire shares one root cause: messaging the product/sizing/returns layer doesn't honour. | Ad Desk, Grade A (meta-analysis) |
| 25 | Hold-rate "25% is good" benchmark | **Likely uses a different denominator** than the standard 15s÷3s formula — can differ by up to 20 points on the same ad depending which is used. "Pick one definition and never change it." | Ad Desk |
| 26 | Ad-fatigue signal thresholds (frequency 2.5+, first-time-impression <50%, CPM drift >18%, CTR down 10–15%) | Explicitly downgraded: **"no sample, no date range, no method... use as starting defaults to calibrate against your own account, not as facts"** | Ad Desk, Grade C |
| 27 | Benchmark websites to actively distrust | 19 named sites listed (adlibrary.com, adsights.ai, admanage.ai, benly.ai, zeely.ai, rule1.ai, sovran.ai, adstellar.ai, superscale.ai, adsuploader.com, tryvizup.com, get-ryze.ai, sepia-lab.com, adliftr.com, digitalapplied.com, orangemonke.com, influee.co, coinis.com, heylect.com, wittelsbach.ai) — "every page is dated 2026, every page covers the identical metric list, and they contradict each other on the same effect." | Ad Desk |

---

*Compiled from: Bambi Swim — Ad Production Research (11 Aug 2026); Ad Desk — Naira Flore & Bambi Swim (generated 30 Jul 2026, build v15); The Indian Demi-Fine Review Photo — Field Spec (compiled 8 Aug 2026); Naira Petite · Feed 01 — Lac & Bone. Every number, quote and grade above is reproduced from source; cross-document connections not explicitly stated in the originals are marked INFERRED.*
