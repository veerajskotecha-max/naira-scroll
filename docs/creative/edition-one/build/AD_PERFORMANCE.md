# Do "crazy" ads beat plain ones? Naira Petite Meta ad performance

*Prepared 16 Oct 2026 for the founder. Scope: every Naira Petite jewellery ad that spent money in the main Meta ad account (903466039148509), 24 Aug – 16 Oct 2026. Three boosted posts in a second account are reported separately (Appendix B). Goal metric: purchase ROAS (Meta-attributed revenue ÷ spend), because every campaign was a Sales campaign optimising for website purchases and Motion's workspace goal metric is ROAS. Numbers are read live from the Meta Ads API unless a row says otherwise.*

## 1. The verdict

**Partly true, but "always" is wrong, and the evidence is thinner than it feels.**

- **On the goal metric, concept-led ("crazy") statics did better.** They took ₹27,161 (17% of spend) and returned **1.44× ROAS** on 16 purchases, at ₹1,698 per purchase. Plain ads (plain statics plus catalogue) took ₹86,263 and returned **0.90×** on 32 purchases, at ₹2,696 per purchase. Plain statics alone returned **0.57×**.
- **Part of plain's result was not real.** The owner confirmed on 29 Aug that all 8 purchases credited to the launch-week catalogue ad were friends-and-family or voided orders. A ninth (#1043, credited to Riya's creator reel) was a family order. With those 9 removed, plain falls to **0.52×** and concept stays at **1.44×**.
- **The gap is fragile.** As Meta reports it, the difference in purchases per rupee is not statistically significant (p = 0.13). After the correction it is (p = 0.025). One ad, **"Almost edible."** (the Prism bracelet in a bowl of gummy sweets), supplied 10 of the 16 concept purchases (67% of concept revenue). Concept ads tested against plain statics alone are not significantly different (p = 0.22).
- **Neither kind has paid for itself as a group.** Concept's 1.44× sits at about the 1.4× cash break-even the Stock Plan uses and well below its 2.1× profit break-even. Only three ads cleared 2.1× after the correction, all concept and each on a single sale (₹120–₹1,044 of spend). The whole account returned 0.95× as Meta reports it and 0.72× corrected.
- **Plain ads won on several metrics.** They drew cheaper traffic (catalogue: ₹54 CPM and ₹4.9 per landing view, against ₹716 and ₹21.5 for concept). Plain statics turned more visits into add-to-carts (20.8% against 13.0%). The founder's own remembered winner, the "3.4× hoops" ad, was a plain still life: the Apricot "quiet" Feed ad (1.49× lifetime).
- **Where both kinds ran in the same ad set, concept ads drew the higher outbound click-through rate every time** (10 of 10 ad sets, 8 of them with at least ₹300 on each side). They also had the higher ROAS in 5 of those ad sets, against 2 for plain; 3 had no purchase on either side.

**Bottom line for the founder:** the data supports *concept-led statics built around a visual pun on the product*, especially on the Prism bracelet. It does not support "crazy always works, plain never does". Concept ads that carried the idea only in the words (gift tags, Q&A cards, type-as-image) barely got delivered by Meta and sold nothing; the one exception, the Pavé dictionary card, made a single sale. A plain catalogue ad (`A · Finish / close-up`) made as many sales as the best concept ad, 10 each, though at a loss.

## 2. Sources, and what was and was not available

| Source | What it gave | Status |
|---|---|---|
| **Meta Ads API**, account 903466039148509 "naira flore meta ads" (`ads_get_ad_entities`, level = ad, `date_preset = maximum`, pulled 15–16 Oct 2026) | Spend, impressions, CTR (all), CPC (all), CPM, outbound clicks and CTR, landing-page views, add-to-carts, purchases, purchase value and ROAS for all 165 ads (130 with spend). A second pull broke spend and purchases down by placement. Ad-set level gave 3-second video plays. | Used. This is the source of every performance number unless a row says otherwise. |
| Meta Ads API, `ads_get_creatives` | Ad copy, headline, format, catalogue product set and 64-px thumbnails for 116 creatives | Used for labelling |
| Meta Ads API, other accounts | 1088886349394166: three boosted Instagram posts for Naira jewellery (₹12,405) and a Dec 2025 couture lead campaign. 1498422677060515: an unrelated medical campaign. | Reported separately (Appendix B); not in the main comparison |
| **Motion Creative Analytics** (`get_auth_context`) | — | **Unavailable.** The tool returned "Your trial or subscription has ended." No hook or thumbstop data, glossary tags or Motion spend threshold. The knowledge base records that Motion's earlier pull on 20 Aug returned no insights and a goal metric of `roas`. |
| Naira Flore Ads Board artifact (DazCYqyXArfKwAy3n7rwDV) | Daily per-ad data from the Meta API, 24 Aug – 12 Oct (reconciles to the live API to the rupee: 105 ads, ₹1,59,066.76, 62 purchases). Also the knowledge base used to correct non-genuine orders (`attribution-correction-29aug.md`, `problem-register-07sep.md`, `live-read-08sep-0702.md`). | Used for the period-matched check and the corrections |
| Naira Ads & Stock Plan (UdpRA4ZFvet6Nm9DJTcp6g) | 14 Oct audit of 105 ads in 22 creative concepts, plus embedded images of 8 key creatives and the break-even lines (1.4× cash, 2.1× profit) | Used to group ads into creatives and to see images; its totals match the API |
| Naira Ad Review (EuMHg5ftNUST6gd1WBB6Eh) and Naira Ad Library (NHb4tS12uc1CBpr1GzPX5k) | Board codes (e.g. `08-M2` = The Night Shift · The Measure) and full-size images of the IG Top 20 creatives | Used for labelling |
| Naira Ads Control Room (AxWMDdU7fe9afCoSZq7q7z) | Images of the August statics | Used for labelling |
| Naira Ad Shortlist (MQQqBJeqqQz7F2qqETDx6Z) | Notes on the two creator reels that ran (how each opens, 25%-view rates, Pankti's audience cost) | Cross-check |
| Naira — The 8+ Edit (2FxrvwcxSxUqYMtvVCuG3v, a Claude Docs doc) | A supplier sourcing scorecard. No ad-level data, but it cites one ad finding: close-up ads drew 3.8 add-to-carts per ₹1,000 against 2.2 for daily-wear ads (the "Up Close" campaign) | Cross-check for section 10 |
| The Signal Score (YDv2obmFP9ThWLeChgD1g7), Edition One Approvals (H6tBbDnLva4DVTGWYdaJ5x), Keep It On, Pigment | A 17 Sep account diagnostic (35/100); product-photo approvals; creative boards (Keep It On notes every earlier world was "one piece per frame, dry and still") | Read; no ad-level performance in them |

**Excluded spend.** 22 ads in March–May 2026 (₹55,540) advertised Naira Flore couture lehengas, not jewellery. They recorded **zero purchases** on 2.06 M impressions. The knowledge base flags their 9% CTR at ₹0.30 CPC as junk-placement delivery. They are left out of every comparison (Appendix B).

**Corrections applied in the "adjusted" rows.** Nine Meta-attributed purchases were not genuine customer orders:

- 8 on `jewellery catalogue ad 2` (25–28 Aug, ₹32,938.80): #1013 was voided, and the owner confirmed #1014–#1022 were friends and family (`attribution-correction-29aug.md`).
- 1 on `riya reel` (6 Sep, ₹2,909.20): #1043 was a family repeat order (`problem-register-07sep.md`).

Everything else is Meta's own attribution (7-day click, 1-day view). The 14 Oct audit matched 9 of "Almost edible"'s 10 purchases to real Prism orders in Shopify.

## 3. How each ad was labelled

The founder's definitions were applied to the picture first and the words second:

- **Crazy / concept**: the ad carries an idea beyond showing the piece. That means a prop or world that makes a visual pun or tells a story: a sweet bowl, a calliper, pigment powder, a fork, molten gold, a hoop rolling a track into clay. It also includes a borrowed format or witty line that drives the ad: a dictionary entry, a gift tag, a Q&A card, day versus night.
- **Plain**: the piece on a plinth, surface or colour ground; a simple model shot; any catalogue (dynamic product) ad. This includes moody art-directed surfaces and colour-matched props that carry no joke, such as the wet oxblood dome and the halved apricot.
- **Creator UGC (neither)**: Pankti's and Riya's creator reels are real people unboxing and wearing the pieces. They are neither concept-led nor product stills, so they are reported separately. Section 5.5 shows what happens if they are counted as plain.

Result: **43 concept ads, 59 plain ads, 6 creator ads** (108 in total). The basis for each label is in the creative table (section 8):

- **Image seen.** Full images were viewed for every creative with real spend: embedded in the Stock Plan and Control Room artifacts, or downloaded from the Ad Library. Catalogue ads were identified from Meta's creative record (a product set and a `{{product.name}}` headline).
- **Board code mapped.** Ad names carry board codes (`ccquiet-A1` = Colour Camps 2.0 · Apricot · quiet; `08-M2` = The Night Shift · The Measure; `13-G2` = Three Camps in Bloom · Pigment; `11-S1` = Sugarplay; `WH-` = Worlds and Hours; `NT-` = Naira Ten; `gr-` = Graphite). These were matched to the Ad Review and Ad Library.
- **Thumbnail only (marked *unsure*).** 18 September test ads (₹19–₹290 each, ₹1,976 in total, no sales) were judged from 64-px thumbnails.
- **Borderline.** Three groups could reasonably go either way and are tested in section 5.5: the Apricot still life (fruit prop, no joke), "Sweet On You" (plain image, pun only in the headline) and the copy-led concepts (Pavé, Gift tags, Answers: the idea is in the type, the photo is plain).

A spend-threshold note: Motion's spend threshold was unavailable. Rankings below use **≥ ₹1,000 per ad** (about 40% of the account's average cost per purchase) and are repeated at **≥ ₹2,500 per creative** where it matters. Only 21 of the 108 ads cleared ₹1,000.

## 4. The comparison (spend-weighted)

ROAS for a group is total revenue ÷ total spend, which is the spend-weighted average of each ad's ROAS. For CTR, CPC and CPM, the first figure is the spend-weighted mean of each ad's rate and the figure in brackets is the pooled group rate. The last column shows the simple (unweighted) mean of ad ROAS, to show how misleading it would be: dozens of tiny ads with no sales drag it down. ROAS intervals are 95% Poisson intervals on the purchase count, times the group's average order.

**4a. As Meta attributes it** (source: Meta Ads API, lifetime, 108 Naira ads)

| Group | Ads | Spend | Impressions | CTR (all), spend-wtd (pooled) | Outbound CTR, spend-wtd (pooled) | CPC (all), spend-wtd (pooled) | CPM, spend-wtd (pooled) | ₹ per landing view | Add-to-cart ÷ landing views | Purchases (95% CI) | Cost per purchase | Revenue | ROAS = spend-wtd (95% CI) | Simple mean of ad ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Crazy / concept statics** | 43 | ₹27,161 | 37,939 | 3.97% (3.64%) | 3.47% (3.23%) | ₹21.26 (₹19.67) | ₹854 (₹716) | ₹21.5 | 13.0% | 16 (9.1–26.0) | ₹1,698 | ₹39,142 | **1.44×** (0.82–2.34×) | 1.18× |
| **Plain, all** (statics + catalogue) | 59 | ₹86,263 | 11,77,158 | 2.10% (1.68%) | 1.89% (1.56%) | ₹12.16 (₹4.36) | ₹356 (₹73) | ₹6.4 | 2.5% | 32 (21.9–45.2) | ₹2,696 | ₹77,397 | **0.90×** (0.61–1.27×) | 0.20× |
| ↳ Plain statics | 43 | ₹23,471 | 23,776 | 3.30% (3.15%) | 2.88% (2.77%) | ₹33.90 (₹31.34) | ₹1,127 (₹987) | ₹37.3 | 20.8% | 8 (3.5–15.8) | ₹2,934 | ₹13,392 | **0.57×** (0.25–1.12×) | 0.10× |
| ↳ Plain catalogue | 16 | ₹62,792 | 11,53,382 | 1.65% (1.65%) | 1.52% (1.54%) | ₹4.16 (₹3.30) | ₹68 (₹54) | ₹4.9 | 1.6% | 24 (15.4–35.7) | ₹2,616 | ₹64,005 | **1.02×** (0.65–1.52×) | 0.45× |
| Creator UGC video (neither) | 6 | ₹45,740 | 79,383 | 4.50% (4.92%) | 2.40% (2.19%) | ₹17.64 (₹11.70) | ₹718 (₹576) | ₹29.8 | 7.3% | 14 (7.7–23.5) | ₹3,267 | ₹34,676 | **0.76×** (0.41–1.27×) | 0.25× |
| All Naira ads | 108 | ₹1,59,164 | 12,94,480 | 3.11% (1.94%) | 2.31% (1.65%) | ₹15.28 (₹6.35) | ₹545 (₹123) | ₹9.8 | 3.8% | 62 (47.5–79.5) | ₹2,567 | ₹1,51,216 | **0.95×** (0.73–1.22×) | 0.59× |

**4b. Corrected for the 9 non-genuine orders** (source: same, minus orders listed in section 2)

| Group | Ads | Spend | Impressions | CTR (all), spend-wtd (pooled) | Outbound CTR, spend-wtd (pooled) | CPC (all), spend-wtd (pooled) | CPM, spend-wtd (pooled) | ₹ per landing view | Add-to-cart ÷ landing views | Purchases (95% CI) | Cost per purchase | Revenue | ROAS = spend-wtd (95% CI) | Simple mean of ad ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Crazy / concept statics** | 43 | ₹27,161 | 37,939 | 3.97% (3.64%) | 3.47% (3.23%) | ₹21.26 (₹19.67) | ₹854 (₹716) | ₹21.5 | 13.0% | 16 (9.1–26.0) | ₹1,698 | ₹39,142 | **1.44×** (0.82–2.34×) | 1.18× |
| **Plain, all** (statics + catalogue) | 59 | ₹86,263 | 11,77,158 | 2.10% (1.68%) | 1.89% (1.56%) | ₹12.16 (₹4.36) | ₹356 (₹73) | ₹6.4 | 2.5% | 24 (15.4–35.7) | ₹3,594 | ₹44,458 | **0.52×** (0.33–0.77×) | 0.13× |
| ↳ Plain statics | 43 | ₹23,471 | 23,776 | 3.30% (3.15%) | 2.88% (2.77%) | ₹33.90 (₹31.34) | ₹1,127 (₹987) | ₹37.3 | 20.8% | 8 (3.5–15.8) | ₹2,934 | ₹13,392 | **0.57×** (0.25–1.12×) | 0.10× |
| ↳ Plain catalogue | 16 | ₹62,792 | 11,53,382 | 1.65% (1.65%) | 1.52% (1.54%) | ₹4.16 (₹3.30) | ₹68 (₹54) | ₹4.9 | 1.6% | 16 (9.1–26.0) | ₹3,924 | ₹31,066 | **0.49×** (0.28–0.80×) | 0.22× |
| Creator UGC video (neither) | 6 | ₹45,740 | 79,383 | 4.50% (4.92%) | 2.40% (2.19%) | ₹17.64 (₹11.70) | ₹718 (₹576) | ₹29.8 | 7.3% | 13 (6.9–22.2) | ₹3,518 | ₹31,767 | **0.69×** (0.37–1.19×) | 0.22× |
| All Naira ads | 108 | ₹1,59,164 | 12,94,480 | 3.11% (1.94%) | 2.31% (1.65%) | ₹15.28 (₹6.35) | ₹545 (₹123) | ₹9.8 | 3.8% | 53 (39.7–69.3) | ₹3,003 | ₹1,15,368 | **0.72×** (0.54–0.95×) | 0.56× |

**Is the difference real?** Exact test of purchases per rupee (two-sided p-value; below 0.05 is conventionally "significant"):

| Comparison | As attributed | Corrected |
|---|---:|---:|
| concept vs plain (all) | 0.130 | 0.025 |
| concept vs plain statics | 0.225 | 0.225 |
| concept vs catalogue | 0.227 | 0.020 |
| concept vs plain + creator UGC | 0.089 | 0.017 |
| concept minus 'Almost edible' vs plain (all) | 0.166 | 0.057 |

Read this as: concept ads beat plain overall once the fake orders are removed. Against plain statics only, the edge (1.44× against 0.57×) rests on 16 against 8 purchases, which is not enough to rule out chance.

## 5. Is it the creative, or something else?

Creative type is tangled up with timing, audience and placement. The catalogue and creator reels ran mostly from late August to mid-September, largely before the new fastrr checkout went live on 17 Sep, in broad or interest audiences and cheap placements. The concept statics ran mostly from late September, on Instagram Feed and Stories. The checks below hold those factors still where the data allows.

### 5.1 Same ad set: same audience, same budget, same days

Source: Meta Ads API, lifetime by ad, grouped by ad set. Meta chose how to split each ad set's budget between the ads.

| Campaign › ad set | Label | Ads | Spend (share of set) | CPM | Outbound CTR | Landing views | Add-to-carts (rate) | Purchases | Revenue | ROAS |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| one winner – Copy › main- one main ad set – Copy | Crazy / concept | 1 | ₹15,765 (83%) | ₹560 | 2.92% | 884 | 108 (12.2%) | 10 | ₹26,388 | 1.67× |
|  | Plain | 2 | ₹3,163 (17%) | ₹386 | 1.80% | 105 | 16 (15.2%) | 1 | ₹1,499 | 0.47× |
|  | Creator UGC (neither) | 2 | ₹139 (1%) | ₹313 | 0.68% | 1 | 0 (0.0%) | 0 | ₹0 | 0.00× |
| Naira — Statics + Riya Collab Reel · ₹1,000/day › Naira · FEED only · Women 20-55 · Metro 25km | Crazy / concept | 1 | ₹1,740 (22%) | ₹913 | 4.67% | 84 | 2 (2.4%) | 0 | ₹0 | 0.00× |
|  | Plain | 6 | ₹6,048 (78%) | ₹1,183 | 2.50% | 120 | 10 (8.3%) | 1 | ₹2,849 | 0.47× |
| Naira · IG Top 20 · Stories + Feed › IG Feed posts · Top 20 · High stock | Crazy / concept | 12 | ₹2,233 (31%) | ₹887 | 2.58% | 63 | 19 (30.2%) | 2 | ₹5,497 | 2.46× |
|  | Plain | 8 | ₹4,894 (69%) | ₹682 | 2.08% | 140 | 28 (20.0%) | 4 | ₹5,996 | 1.23× |
| Naira · IG Top 20 · Stories + Feed › IG Stories · Top 20 · High stock | Crazy / concept | 12 | ₹1,622 (23%) | ₹1,453 | 3.23% | 31 | 8 (25.8%) | 1 | ₹2,399 | 1.48× |
|  | Plain | 8 | ₹5,490 (77%) | ₹992 | 3.00% | 160 | 52 (32.5%) | 1 | ₹1,099 | 0.20× |
| Naira — Static Winners · ₹800/day (15 Sep) › Winners · RETARGET warm + hot · Feed + Stories · A+A OFF · purchasers excluded | Crazy / concept | 3 | ₹2,397 (60%) | ₹1,541 | 4.63% | 70 | 5 (7.1%) | 1 | ₹1,769 | 0.74× |
|  | Plain | 1 | ₹1,618 (40%) | ₹1,660 | 2.77% | 27 | 11 (40.7%) | 0 | ₹0 | 0.00× |
| Naira — Sept Test · COLD / WARM / HOT · 3 sets › 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | Crazy / concept | 6 | ₹1,296 (60%) | ₹1,187 | 4.30% | 45 | 5 (11.1%) | 0 | ₹0 | 0.00× |
|  | Plain | 8 | ₹851 (40%) | ₹926 | 3.59% | 31 | 0 (0.0%) | 0 | ₹0 | 0.00× |
| Naira — Statics + Riya Collab Reel · ₹1,000/day › Naira · STORIES only · Women 20-55 · Metro 25km | Crazy / concept | 1 | ₹495 (24%) | ₹1,465 | 5.92% | 19 | 1 (5.3%) | 0 | ₹0 | 0.00× |
|  | Plain | 5 | ₹1,578 (76%) | ₹1,856 | 4.94% | 45 | 4 (8.9%) | 1 | ₹1,949 | 1.24× |
| Naira — Sept Test · COLD / WARM / HOT · 3 sets › 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | Crazy / concept | 5 | ₹1,374 (81%) | ₹1,327 | 5.89% | 58 | 14 (24.1%) | 2 | ₹3,089 | 2.25× |
|  | Plain | 3 | ₹318 (19%) | ₹1,276 | 5.22% | 13 | 2 (15.4%) | 0 | ₹0 | 0.00× |
| one winner › main- one main ad set | Crazy / concept | 1 | ₹213 (54%) | ₹1,096 | 6.19% | 12 | 2 (16.7%) | 0 | ₹0 | 0.00× |
|  | Plain | 2 | ₹146 (37%) | ₹1,096 | 5.26% | 8 | 8 (100.0%) | 0 | ₹0 | 0.00× |
|  | Creator UGC (neither) | 2 | ₹37 (9%) | ₹516 | 4.23% | 1 | 0 (0.0%) | 0 | ₹0 | 0.00× |
| Naira · Statics · ₹1,000/day · Oct 2026 › Statics · Hoops · one-winner audience · IG Feed only | Crazy / concept | 1 | ₹26 (28%) | ₹1,241 | 4.76% | 0 | 0 (—) | 0 | ₹0 | 0.00× |
|  | Plain | 1 | ₹68 (72%) | ₹904 | 2.67% | 0 | 0 (—) | 0 | ₹0 | 0.00× |

- **Outbound CTR: concept higher in 10 of 10 ad sets.** This is the most consistent signal in the data. The concept ads stop the scroll and earn the click.
- **ROAS: concept higher in 5, plain higher in 2, 3 ties at zero.** The biggest win is "Almost edible" in the `one winner – Copy` ad set: Meta gave it 83% of the budget and it made 10 sales at 1.67×, against 1 sale at 0.47× for the plain ads beside it.
- **Plain won the two August static ad sets** (Feed-only and Stories-only, Women 20–55, metros), where "Almost edible" first ran: ₹2,235 and no sale. Meta also gave the majority of budget to the plain ads in 4 of the 8 ad sets with real spend.
- **Add-to-cart rate: plain higher in 5 of 8** ad sets with spend on both sides. Plain ads got carts but fewer purchases.

### 5.2 Same placement

Source: Meta Ads API, lifetime, ad × placement breakdown, corrected for the 9 non-genuine orders. Placements with at least ₹1,000 shown.

| Placement | Crazy / concept | Plain statics | Plain catalogue | Creator UGC |
|---|---|---|---|---|
| Instagram Feed | 1.79× on ₹14,746 · 10 sales · outCTR 2.85% | 0.53× on ₹11,232 · 4 sales · outCTR 2.39% | 0.49× on ₹23,324 · 7 sales · outCTR 2.03% | 0.94× on ₹22,766 · 8 sales · outCTR 4.52% |
| Instagram Stories | 1.36× on ₹9,313 · 6 sales · outCTR 4.31% | 0.36× on ₹8,434 · 2 sales · outCTR 3.64% | 0.74× on ₹11,973 · 4 sales · outCTR 3.39% | 0.57× on ₹6,764 · 1 sale · outCTR 5.21% |
| Facebook Feed | 0.00× on ₹2,654 · 0 sales · outCTR 2.95% | 1.20× on ₹3,609 · 2 sales · outCTR 2.47% | 0.47× on ₹7,087 · 1 sale · outCTR 2.37% | 0.38× on ₹5,852 · 1 sale · outCTR 3.86% |
| Instagram Reels | 0.00× on ₹154 · 0 sales · outCTR 1.17% | — | 0.49× on ₹15,140 · 4 sales · outCTR 1.36% | 0.45× on ₹9,391 · 3 sales · outCTR 1.37% |

On Instagram Feed (45% of all spend) and Instagram Stories, concept statics beat every other kind. On Facebook Feed, plain statics made the only static sales (2 on ₹3,609) and concept made none on ₹2,654. Reels was poor for everything that ran there.

### 5.3 Same product (Woven Gold Hoops)

Source: Meta Ads API, lifetime, corrected. Only the hoops had real spend on both kinds of creative. Plain Prism ads spent ₹360 in total, so the bracelet cannot be compared this way.

| Hoops ads | Spend | Outbound CTR | Add-to-cart ÷ landing views | Purchases | Revenue | ROAS |
|---|---:|---:|---:|---:|---:|---:|
| Crazy / concept (Rolling for miles, The Width, 07:15/23:30) | ₹4,723 | 4.14% | 17.7% | 3 | ₹5,037 | 1.07× |
| Plain (Apricot, Woven not cast, Gold that stays) | ₹16,250 | 2.79% | 26.2% | 7 | ₹10,543 | 0.65× |

### 5.4 Same period

Source: Ads Board daily per-ad data (Meta API, reconciles to the live API), corrected. Concept ads did better in both halves. In the first half every kind lost money, and concept was level with creator video.

| Period | Crazy / concept | Plain statics | Plain catalogue | Creator UGC |
|---|---|---|---|---|
| 24 Aug–20 Sep | 0.67× on ₹7,302 · 3 sales | 0.46× on ₹10,391 · 2 sales | 0.51× on ₹56,695 · 15 sales | 0.70× on ₹45,320 · 13 sales |
| 21 Sep–12 Oct | 1.73× on ₹19,832 · 13 sales | 0.66× on ₹13,009 · 6 sales | 0.35× on ₹6,097 · 1 sale | 0.00× on ₹420 · 0 sales |

### 5.5 Does the answer depend on how the borderline ads are labelled?

Source: Meta Ads API, lifetime. p = exact test of purchases per rupee.

| Scenario | Concept: spend · sales · ROAS | Plain: spend · sales · ROAS (as attributed) | p | Plain ROAS, corrected | p, corrected |
|---|---|---|---:|---:|---:|
| Base (UGC excluded) | ₹27,161 · 16 · 1.44× | ₹86,263 · 32 · 0.90× | 0.130 | 0.52× | 0.025 |
| UGC counted as plain | ₹27,161 · 16 · 1.44× | ₹1,32,003 · 46 · 0.85× | 0.089 | 0.58× | 0.017 |
| Apricot counted as concept | ₹36,938 · 21 · 1.25× | ₹76,486 · 27 · 0.92× | 0.122 | 0.49× | 0.010 |
| Copy-led concepts (Pavé, Gift, Answer) counted as plain | ₹25,934 · 15 · 1.42× | ₹87,490 · 33 · 0.91× | 0.170 | 0.54× | 0.037 |
| Drop every 'unsure' and 'borderline' ad | ₹25,127 · 15 · 1.46× | ₹70,378 · 26 · 0.96× | 0.155 | 0.49× | 0.017 |
| Concept without 'Almost edible' | ₹8,948 · 6 · 1.43× | ₹86,263 · 32 · 0.90× | 0.166 | 0.52× | 0.057 |
| Statics only (no catalogue, no UGC) | ₹27,161 · 16 · 1.44× | ₹23,471 · 8 · 0.57× | 0.225 | 0.57× | 0.225 |

The direction never flips: concept ROAS is higher in every scenario. Without the friends-and-family correction, no scenario is significant at 5%. With it, five of the seven scenarios are significant (p ≤ 0.04); the exceptions are dropping "Almost edible" (p = 0.057) and comparing statics only (p = 0.225).

### 5.6 How much rests on one ad

"Almost edible." spent ₹18,213 across four ads and made 10 of the 16 concept sales and 67% of concept revenue. The other 39 concept ads together spent ₹8,948 and made 6 sales. That is still about 1.4× ROAS, but no other ad made more than one sale. The same "Almost edible" image made **no sale on ₹2,235** in its first run (29 Aug – 14 Sep, Feed-only and Stories-only ad sets). It took off only in the `one winner – Copy` campaign from 23 Sep. Audience and timing mattered as much as the picture.

## 6. Where plain ads won

- **Cheapest traffic and reach.** Catalogue ads bought impressions at ₹54 CPM and landing views at ₹4.9, against ₹716 and ₹21.5 for concept statics. Much of that gap is placement and audience rather than the picture: 24% of catalogue spend went to Instagram Reels at about ₹16 CPM, which supplied most of its impressions, and the catalogue ran mainly in broad audiences. On Instagram Feed alone the gap is smaller (catalogue ₹486 CPM against ₹624 for concept).
- **Most sales in absolute terms.** Plain ads produced 32 attributed sales (24 genuine) against 16 for concept, because they had 3× the budget. The plain catalogue ad `A · Finish / close-up (set 1)` in the broad Metro · A ad set tied the best concept ad for the most sales by a single ad: 10 on ₹22,267 (0.95×), against 10 on ₹15,765 (1.67×) for "Almost edible".
- **More add-to-carts per visit.** Plain statics 20.8% against 13.0% for concept. Within hoops it was 26.2% against 17.7%, and on Instagram Stories 26.8% against 12.5%. Those carts converted less often: the Apricot Story got 47 carts and 1 sale.
- **The founder's own "3.4× hoops" ad was plain.** The Apricot "quiet" Feed ad (hoops on a halved apricot, no joke) made 4 sales on ₹4,033 (1.49×). All four came on 5–7 Oct (Stock Plan).
- **Facebook Feed:** plain statics 1.20× (2 sales) against concept 0 sales on ₹2,654.
- **Meta's own delivery** gave plain ads the majority of the budget in 4 of the 8 shared ad sets with real spend. Its prediction did not favour the crazy ads by default.
- **The best single ROAS by raw attribution** was a plain catalogue ad (3.68×). As section 2 explains, those sales were not real.

## 7. Top 5 ads by ROAS (the goal metric)

**7a. Ad level, spend ≥ ₹1,000** (source: Meta Ads API, lifetime). Six rows are shown because the #1 ad drops out once its non-genuine orders are removed.

| Rank | Ad | What it is | Label | Spend | Purchases | ROAS as attributed | ROAS corrected |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `jewellery catalogue ad 2` | Catalogue · Aug launch | Plain | ₹8,948 | 8 | 3.68× | 0.00× |
| 2 | `Story · 01-E1 · PAVÉ` | 'PAVÉ' (dictionary entry over a macro) | Crazy / concept | ₹1,044 | 1 | 2.30× | 2.30× |
| 3 | `104 bracelet ad – Copy` | 'Almost edible.' (Prism in a bowl of gummy sweets) | Crazy / concept | ₹15,765 | 10 | 1.67× | 1.67× |
| 4 | `Feed · ccquiet-A1 · Apricot quiet · Woven Gold Hoops` | Colour Camps · Apricot (hoops on a halved apricot, peach linen) | Plain | ₹4,033 | 4 | 1.49× | 1.49× |
| 5 | `S1 · Woven Gold Hoops · STORY` | 'Woven, not cast.' (hoops on a wet oxblood dome) | Plain | ₹1,333 | 1 | 1.46× | 1.46× |
| 6 | `Feed · 08-M2 · THE WIDTH.` | 'THE WIDTH.' (hoop in a brass calliper + ruler) | Crazy / concept | ₹1,359 | 1 | 1.10× | 1.10× |

As Meta reports it, the top 5 ads are 3 plain and 2 concept. Once the launch-week catalogue ad's non-genuine orders are removed, the top 5 is: Pavé story (concept, 1 sale), "Almost edible" (concept, 10 sales), Apricot quiet Feed (plain, 4 sales), "Woven, not cast" story (plain, 1 sale) and The Width Feed (concept, 1 sale). That is **3 concept and 2 plain**. Four of the five rest on a single sale or a few days.

**7b. Creative level (all placements of the same image pooled), spend ≥ ₹1,000, corrected** (source: same)

| Rank | Creative | Label | Ads | Spend | Purchases | ROAS corrected (95% CI) |
|---:|---|---|---:|---:|---:|---:|
| 1 | 'PAVÉ' (dictionary entry over a macro) | Crazy / concept | 2 | ₹1,089 | 1 | 2.20× (0.06–12.27×) |
| 2 | 'Almost edible.' (Prism in a bowl of gummy sweets) | Crazy / concept | 4 | ₹18,213 | 10 | 1.45× (0.69–2.66×) |
| 3 | 'Poured, not made.' (molten gold drip on cobalt) | Crazy / concept | 3 | ₹1,098 | 1 | 1.20× (0.03–6.70×) |
| 4 | 'It has been rolling for miles.' (hoop rolling a braid track into clay) | Crazy / concept | 4 | ₹3,162 | 2 | 1.12× (0.14–4.04×) |
| 5 | 'THE WIDTH.' (hoop in a brass calliper + ruler) | Crazy / concept | 3 | ₹1,469 | 1 | 1.02× (0.03–5.68×) |
| 6 | Catalogue · Clean Metro A 'Finish' | Plain | 4 | ₹27,538 | 13 | 0.95× (0.50–1.62×) |
| 7 | Pankti collab reel | Creator UGC (neither) | 3 | ₹28,259 | 8 | 0.79× (0.34–1.56×) |
| 8 | Colour Camps · Apricot (hoops on a halved apricot, peach linen) | Plain | 8 | ₹9,777 | 5 | 0.73× (0.24–1.69×) |

At creative level the top five are all concept-led: Pavé, Almost edible, Poured not made, Rolling for miles and The Width. Only "Almost edible" has enough sales to mean much, and its interval is wide. At ≥ ₹2,500 per creative the order is "Almost edible" (concept, 1.45×), "Rolling for miles" (concept, 1.12×), the Finish catalogue (plain, 0.95×), Pankti's reel (UGC, 0.79×) and the Apricot camp (plain, 0.73×).

## 8. Every creative (ads that share an image pooled)

Source: Meta Ads API, lifetime (`date_preset = maximum`). Hook rate = 3-second video plays ÷ impressions (ad-set level; each creator reel ran alone in its ad set). Meta reports no hook or thumbstop metric for still images, and Motion, which would have, was unavailable. "ROAS corrected" removes the 9 non-genuine orders.

| # | Creative (what the picture shows) | Label | Confidence | Ads | Spend | Impressions | CTR (all) | Outbound CTR | CPC (all) | CPM | Hook rate | Add-to-carts | Purchases | Cost per purchase | ROAS | ROAS corrected |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Pankti collab reel | Creator UGC (neither) · creator video | sure | 3 | ₹28,259 | 29,983 | 3.83% | 2.73% | ₹24.63 | ₹942 | 20.4% | 70 | 8 | ₹3,532 | 0.79× | 0.79× |
| 2 | Catalogue · Clean Metro A 'Finish' | Plain · catalogue | sure | 4 | ₹27,538 | 4,42,926 | 1.54% | 1.44% | ₹4.03 | ₹62 | n/a (catalogue) | 113 | 13 | ₹2,118 | 0.95× | 0.95× |
| 3 | Catalogue · Clean Metro B 'Daily wear' | Plain · catalogue | sure | 4 | ₹18,860 | 2,23,085 | 1.80% | 1.63% | ₹4.70 | ₹85 | n/a (catalogue) | 40 | 2 | ₹9,430 | 0.15× | 0.15× |
| 4 | 'Almost edible.' (Prism in a bowl of gummy sweets) | Crazy / concept · visual pun / unexpected world | sure | 4 | ₹18,213 | 30,602 | 3.41% | 3.08% | ₹17.44 | ₹595 | n/a (static) | 113 | 10 | ₹1,821 | 1.45× | 1.45× |
| 5 | Riya collab reel | Creator UGC (neither) · creator video | sure | 3 | ₹17,481 | 49,400 | 5.59% | 1.86% | ₹6.33 | ₹354 | 13.7% | 42 | 6 | ₹2,914 | 0.71× | 0.54× |
| 6 | Catalogue · Aug launch | Plain · catalogue | sure | 3 | ₹10,505 | 4,00,445 | 1.80% | 1.71% | ₹1.46 | ₹26 | n/a (catalogue) | 31 | 8 | ₹1,313 | 3.14× | 0.00× |
| 7 | Colour Camps · Apricot (hoops on a halved apricot, peach linen) | Plain · styled still life (colour-matched prop) | borderline | 8 | ₹9,777 | 12,045 | 2.76% | 2.52% | ₹29.38 | ₹812 | n/a (static) | 78 | 5 | ₹1,955 | 0.73× | 0.73× |
| 8 | 'Woven, not cast.' (hoops on a wet oxblood dome) | Plain · product on plinth / dramatic surface | sure | 5 | ₹6,436 | 4,998 | 3.90% | 3.44% | ₹32.99 | ₹1,288 | n/a (static) | 41 | 2 | ₹3,218 | 0.54× | 0.54× |
| 9 | Catalogue tests CT1–CT3 | Plain · catalogue | sure | 3 | ₹5,184 | 81,467 | 1.12% | 0.97% | ₹5.68 | ₹64 | n/a (catalogue) | 25 | 1 | ₹5,184 | 0.42× | 0.42× |
| 10 | 'Sweet On You.' (charm bracelet on a coral gradient) | Plain · plain ground + pun headline | borderline | 2 | ₹4,939 | 4,539 | 3.04% | 2.58% | ₹35.79 | ₹1,088 | n/a (static) | 8 | 1 | ₹4,939 | 0.58× | 0.58× |
| 11 | 'It has been rolling for miles.' (hoop rolling a braid track into clay) | Crazy / concept · visual pun / object-play | sure | 4 | ₹3,162 | 2,282 | 6.00% | 4.82% | ₹23.08 | ₹1,385 | n/a (static) | 9 | 2 | ₹1,581 | 1.12× | 1.12× |
| 12 | 'THE WIDTH.' (hoop in a brass calliper + ruler) | Crazy / concept · object-play / borrowed format | sure | 3 | ₹1,469 | 1,368 | 3.73% | 3.07% | ₹28.83 | ₹1,074 | n/a (static) | 14 | 1 | ₹1,469 | 1.02× | 1.02× |
| 13 | Sept Edit · product on lilac / neutral ground | Plain · product on plain ground | unsure | 11 | ₹1,169 | 1,168 | 4.62% | 3.94% | ₹21.65 | ₹1,001 | n/a (static) | 2 | 0 | — | 0.00× | 0.00× |
| 14 | 'Poured, not made.' (molten gold drip on cobalt) | Crazy / concept · visual pun | likely | 3 | ₹1,098 | 835 | 6.83% | 6.11% | ₹19.26 | ₹1,315 | n/a (static) | 12 | 1 | ₹1,098 | 1.20× | 1.20× |
| 15 | 'PAVÉ' (dictionary entry over a macro) | Crazy / concept · borrowed format (copy-led) | borderline | 2 | ₹1,089 | 708 | 3.11% | 2.82% | ₹49.54 | ₹1,539 | n/a (static) | 7 | 1 | ₹1,089 | 2.20× | 2.20× |
| 16 | Catalogue · 'ad 101' | Plain · catalogue | likely | 2 | ₹706 | 5,459 | 1.19% | 1.03% | ₹10.82 | ₹129 | n/a (catalogue) | 0 | 0 | — | 0.00× | 0.00× |
| 17 | Worlds · type-as-image ('Light.', 'Link.') | Crazy / concept · type play | sure | 4 | ₹519 | 853 | 2.70% | 2.34% | ₹22.55 | ₹609 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 18 | Sept Edit · pearl lariat dipped in milk | Crazy / concept · object-play | unsure | 2 | ₹401 | 244 | 4.10% | 4.10% | ₹40.07 | ₹1,643 | n/a (static) | 2 | 0 | — | 0.00× | 0.00× |
| 19 | 'PASTEL.' (bracelet in heaps of pigment powder) | Crazy / concept · object-play / colour world | sure | 2 | ₹385 | 311 | 4.50% | 3.86% | ₹27.52 | ₹1,239 | n/a (static) | 3 | 1 | ₹385 | 10.38× | 10.38× |
| 20 | Colour Camps · Lilac (bracelet on lilac paper) | Plain · styled still life | sure | 4 | ₹360 | 473 | 1.69% | 1.69% | ₹45.04 | ₹762 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 21 | Naira Ten · 'What I wear to…' (simple model / product shot) | Plain · simple model shot | sure | 4 | ₹282 | 245 | 3.26% | 2.04% | ₹35.26 | ₹1,150 | n/a (static) | 2 | 0 | — | 0.00× | 0.00× |
| 22 | 'One pool of light.' (ring under a spotlight on black) | Plain · product on plain ground | sure | 2 | ₹259 | 164 | 3.05% | 3.05% | ₹51.73 | ₹1,579 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 23 | Sept Edit · 'It splits the light' (rainbow beam) | Crazy / concept · visual pun | unsure | 2 | ₹223 | 214 | 3.74% | 3.27% | ₹27.86 | ₹1,043 | n/a (static) | 1 | 0 | — | 0.00× | 0.00× |
| 24 | 'PICK 'N' MIX.' (bracelet in a candy bowl) | Crazy / concept · visual pun | sure | 2 | ₹159 | 169 | 2.37% | 1.78% | ₹39.78 | ₹942 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 25 | Sept Edit · ring on a red wax seal | Crazy / concept · object-play | unsure | 2 | ₹145 | 92 | 1.09% | 1.09% | ₹144.68 | ₹1,571 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 26 | 'One warm note.' (bracelet on a fabric roll) | Plain · product on prop/plinth | sure | 2 | ₹141 | 54 | 1.85% | 0.00% | ₹140.91 | ₹2,613 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 27 | Hours · '07:15 / 23:30' (same hoops, day vs night) | Crazy / concept · story | sure | 2 | ₹92 | 70 | 2.85% | 2.86% | ₹45.82 | ₹1,308 | n/a (static) | 3 | 0 | — | 0.00× | 0.00× |
| 28 | Gift tags ('to: the sister who borrows everything') | Crazy / concept · story (copy-led) | borderline | 4 | ₹87 | 92 | 4.35% | 1.09% | ₹21.61 | ₹940 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 29 | Objection answers ('will it tarnish? NO.') | Crazy / concept · witty Q&A (copy-led) | borderline | 4 | ₹51 | 40 | 5.00% | 2.50% | ₹25.53 | ₹1,276 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 30 | 'Links, and a little light.' (necklace on wet stone) | Plain · product on surface | sure | 2 | ₹44 | 26 | 11.54% | 3.85% | ₹14.66 | ₹1,692 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 31 | Sept Edit · 'It keeps going' (bracelet runs into a chain) | Crazy / concept · object-play | unsure | 1 | ₹39 | 15 | 6.67% | 6.67% | ₹38.87 | ₹2,593 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 32 | Naira Ten · 'Gold that stays.' (ear close-up) | Plain · simple model shot | sure | 2 | ₹36 | 29 | 3.45% | 3.45% | ₹36.32 | ₹1,254 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 33 | Graphite · 'The clasp is the design' (chain on a fork) | Crazy / concept · object-play | sure | 2 | ₹30 | 44 | 2.27% | 2.27% | ₹29.87 | ₹679 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |
| 34 | 'The quiet solitaire.' (chain over a box) | Plain · product on plinth | sure | 1 | ₹28 | 35 | 8.57% | 2.86% | ₹9.29 | ₹796 | n/a (static) | 0 | 0 | — | 0.00× | 0.00× |

How each creative was labelled:

- **Pankti collab reel**: Creator unboxing reel (Meta video creative; Ad Shortlist artifact).
- **Catalogue · Clean Metro A 'Finish'**: Meta creative is a product-set catalogue ad ({{product.name}} headline).
- **Catalogue · Clean Metro B 'Daily wear'**: Meta creative is a product-set catalogue ad.
- **'Almost edible.' (Prism in a bowl of gummy sweets)**: Image seen (Stock Plan + Control Room artifacts); image hash shared by 104/A7 per 14 Oct audit.
- **Riya collab reel**: Creator haul reel (Meta video creative; Ad Shortlist artifact).
- **Catalogue · Aug launch**: Meta creative is a product-set catalogue ad.
- **Colour Camps · Apricot (hoops on a halved apricot, peach linen)**: Image seen (Stock Plan + Ad Library) — Colour Camps; no joke or headline idea.
- **'Woven, not cast.' (hoops on a wet oxblood dome)**: Image seen (Stock Plan + Control Room); image hash shared by A1/S1/105 per 14 Oct audit. The 105 ads carry Garba copy.
- **Catalogue tests CT1–CT3**: Meta creative is a product-set catalogue ad.
- **'Sweet On You.' (charm bracelet on a coral gradient)**: Image seen (Stock Plan + Control Room); pun lives only in the headline.
- **'It has been rolling for miles.' (hoop rolling a braid track into clay)**: Image seen (Stock Plan artifact) + thumbnail.
- **'THE WIDTH.' (hoop in a brass calliper + ruler)**: Image seen (Stock Plan) — The Night Shift · The Measure.
- **Sept Edit · product on lilac / neutral ground**: 64px thumbnail only.
- **'Poured, not made.' (molten gold drip on cobalt)**: Thumbnail + headline (Cover Proofs / Stock Plan).
- **'PAVÉ' (dictionary entry over a macro)**: Image seen (Stock Plan) — The Night Shift · The Dictionary; image itself is a plain macro.
- **Catalogue · 'ad 101'**: Meta creative has a product set and {{product.name}} title (the 14 Oct audit had no record of it).
- **Worlds · type-as-image ('Light.', 'Link.')**: Image seen (Ad Library preview) — Worlds and Hours.
- **Sept Edit · pearl lariat dipped in milk**: 64px thumbnail only.
- **'PASTEL.' (bracelet in heaps of pigment powder)**: Image seen (Ad Library) — Three Camps in Bloom · Pigment.
- **Colour Camps · Lilac (bracelet on lilac paper)**: Image seen (Ad Library) — Colour Camps.
- **Naira Ten · 'What I wear to…' (simple model / product shot)**: Image seen (Ad Library preview) — Naira Ten.
- **'One pool of light.' (ring under a spotlight on black)**: Image seen (Control Room).
- **Sept Edit · 'It splits the light' (rainbow beam)**: 64px thumbnail only.
- **'PICK 'N' MIX.' (bracelet in a candy bowl)**: Image seen (Ad Library) — Sugarplay.
- **Sept Edit · ring on a red wax seal**: 64px thumbnail only.
- **'One warm note.' (bracelet on a fabric roll)**: Image seen (Control Room).
- **Hours · '07:15 / 23:30' (same hoops, day vs night)**: Image seen (Ad Library preview) — Worlds and Hours.
- **Gift tags ('to: the sister who borrows everything')**: Image seen (Ad Library) — The Night Shift · The Gift; product in a box, idea is in the tag copy.
- **Objection answers ('will it tarnish? NO.')**: Image seen (Ad Library) — The Night Shift · The Answer; plain model shot, idea is in the type.
- **'Links, and a little light.' (necklace on wet stone)**: Image seen (Control Room).
- **Sept Edit · 'It keeps going' (bracelet runs into a chain)**: 64px thumbnail only.
- **Naira Ten · 'Gold that stays.' (ear close-up)**: Image seen (Ad Library preview) — Naira Ten.
- **Graphite · 'The clasp is the design' (chain on a fork)**: Image seen (Ad Library) — Naira Graphite.
- **'The quiet solitaire.' (chain over a box)**: Image seen (Control Room).

## 9. Every ad with spend ≥ ₹500

Source: Meta Ads API, lifetime. CPC (all) and CTR (all) count every click, including clicks to the profile and to "see more". Outbound CTR counts only clicks to the website. All 108 ads are listed in Appendix A.

| Ad name (Meta) | Campaign › ad set | Label | Creative | Spend | Impressions | CTR (all) | Outbound CTR | CPC (all) | CPM | Hook rate | Purchases | Cost per purchase | ROAS | ROAS corrected |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `pankti collab reel` | Naira — Pankti Collab Reel · ₹400/day (cut 15 Sep) › Pankti collab · INT Luxury + First-class travel × Shoppers · A+A ON · 7 metros | Creator UGC (neither) | Pankti collab reel | ₹28,182 | 29,855 | 3.83% | 2.73% | ₹24.66 | ₹944 | 20.4% | 8 | ₹3,523 | 0.79× | 0.79× |
| `A · Finish / close-up (set 1)` | Naira — Clean Metro Prospecting (28 Aug) › Metro · A · BROAD no interests · A+A ON · 7 metros · geo-expand OFF | Plain | Catalogue · Clean Metro A 'Finish' | ₹22,267 | 3,15,675 | 1.58% | 1.46% | ₹4.47 | ₹71 | n/a | 10 | ₹2,227 | 0.95× | 0.95× |
| `riya reel` | Naira — Statics + Riya Collab Reel · ₹1,000/day › Riya collab reel · INT Online shopping × Shoppers · A+A ON · 7 metros | Creator UGC (neither) | Riya collab reel | ₹17,382 | 49,013 | 5.59% | 1.87% | ₹6.34 | ₹355 | 13.7% | 6 | ₹2,897 | 0.71× | 0.54× |
| `B · Daily wear — cleaned copy (set 2)` | Naira — Clean Metro Prospecting (28 Aug) › Metro · A · BROAD no interests · A+A ON · 7 metros · geo-expand OFF | Plain | Catalogue · Clean Metro B 'Daily wear' | ₹16,704 | 1,66,137 | 1.94% | 1.73% | ₹5.17 | ₹101 | n/a | 2 | ₹8,352 | 0.17× | 0.17× |
| `104 bracelet ad – Copy` | one winner – Copy › main- one main ad set – Copy | Crazy / concept | 'Almost edible.' | ₹15,765 | 28,163 | 3.21% | 2.92% | ₹17.46 | ₹560 | n/a | 10 | ₹1,576 | 1.67× | 1.67× |
| `jewellery catalogue ad 2` | Jewllery launch sales camp 1 › jewellery 2  broad ctalgoue 2 set – Copy | Plain | Catalogue · Aug launch | ₹8,948 | 3,37,486 | 1.74% | 1.65% | ₹1.52 | ₹27 | n/a | 8 | ₹1,118 | 3.68× | 0.00× |
| `A6 · Sweet On You · bracelets` | Naira — Statics + Riya Collab Reel · ₹1,000/day › Naira · FEED only · Women 20-55 · Metro 25km | Plain | 'Sweet On You.' | ₹4,917 | 4,525 | 3.05% | 2.59% | ₹35.63 | ₹1,087 | n/a | 1 | ₹4,917 | 0.58× | 0.58× |
| `Story · ccquiet-A1 · Apricot quiet · Woven Gold Hoops` | Naira · IG Top 20 · Stories + Feed › IG Stories · Top 20 · High stock | Plain | Colour Camps · Apricot | ₹4,533 | 4,982 | 3.27% | 3.09% | ₹27.81 | ₹910 | n/a | 1 | ₹4,533 | 0.24× | 0.24× |
| `CT3 · Necklaces + Bracelets (13 in stock)` | catalogue testing › Catalogue test · | Plain | Catalogue tests CT1–CT3 | ₹4,066 | 55,276 | 1.19% | 1.04% | ₹6.18 | ₹74 | n/a | 1 | ₹4,066 | 0.53× | 0.53× |
| `Feed · ccquiet-A1 · Apricot quiet · Woven Gold Hoops` | Naira · IG Top 20 · Stories + Feed › IG Feed posts · Top 20 · High stock | Plain | Colour Camps · Apricot | ₹4,033 | 6,306 | 2.36% | 2.03% | ₹27.07 | ₹640 | n/a | 4 | ₹1,008 | 1.49× | 1.49× |
| `A · Finish / close-up (set 1)` | Naira — Clean Metro Prospecting (28 Aug) › Metro · B · INT category: Jewellery + Silver + Necklace · A+A ON · geo-expand ON | Plain | Catalogue · Clean Metro A 'Finish' | ₹3,705 | 86,260 | 1.41% | 1.37% | ₹3.04 | ₹43 | n/a | 2 | ₹1,852 | 0.87× | 0.87× |
| `105 golden woops – Copy` | one winner – Copy › main- one main ad set – Copy | Plain | 'Woven, not cast.' | ₹2,467 | 2,770 | 3.65% | 3.32% | ₹24.43 | ₹891 | n/a | 1 | ₹2,467 | 0.61× | 0.61× |
| `W2 · STORY · S2 Woven Gold Hoops v2` | Naira — Static Winners · ₹800/day (15 Sep) › Winners · RETARGET warm + hot · Feed + Stories · A+A OFF · purchasers excluded | Crazy / concept | 'It has been rolling for miles.' | ₹2,090 | 1,332 | 6.08% | 4.73% | ₹25.81 | ₹1,569 | n/a | 1 | ₹2,090 | 0.85× | 0.85× |
| `B · Daily wear — cleaned copy (set 2)` | Naira — Clean Metro Prospecting (28 Aug) › Metro · C · INT brands: Swarovski + Pandora + Cartier × Shoppers · A+A ON · geo-expand ON | Plain | Catalogue · Clean Metro B 'Daily wear' | ₹1,940 | 43,315 | 1.35% | 1.30% | ₹3.32 | ₹45 | n/a | 0 | — | 0.00× | 0.00× |
| `A7 · The Demi-Fine Edit — bracelets` | Naira — Statics + Riya Collab Reel · ₹1,000/day › Naira · FEED only · Women 20-55 · Metro 25km | Crazy / concept | 'Almost edible.' | ₹1,740 | 1,907 | 5.61% | 4.67% | ₹16.27 | ₹913 | n/a | 0 | — | 0.00× | 0.00× |
| `W3 · STORY · S1 Woven Gold Hoops` | Naira — Static Winners · ₹800/day (15 Sep) › Winners · RETARGET warm + hot · Feed + Stories · A+A OFF · purchasers excluded | Plain | 'Woven, not cast.' | ₹1,618 | 975 | 3.28% | 2.77% | ₹50.57 | ₹1,660 | n/a | 0 | — | 0.00× | 0.00× |
| `A · Finish / close-up (set 1)` | Naira — Clean Metro Prospecting (28 Aug) › Metro · D · INT Indian designers + Online shopping · A+A ON · geo-expand ON | Plain | Catalogue · Clean Metro A 'Finish' | ₹1,552 | 38,874 | 1.56% | 1.47% | ₹2.55 | ₹40 | n/a | 1 | ₹1,552 | 1.03× | 1.03× |
| `Feed · 08-M2 · THE WIDTH.` | Naira · IG Top 20 · Stories + Feed › IG Feed posts · Top 20 · High stock | Crazy / concept | 'THE WIDTH.' | ₹1,359 | 1,296 | 3.47% | 2.85% | ₹30.20 | ₹1,048 | n/a | 1 | ₹1,359 | 1.10× | 1.10× |
| `catalalogue 1` | Jewllery launch sales camp 1 › ad set 1 broad – Copy 2 | Plain | Catalogue · Aug launch | ₹1,341 | 60,539 | 2.12% | 2.02% | ₹1.05 | ₹22 | n/a | 0 | — | 0.00× | 0.00× |
| `S1 · Woven Gold Hoops · STORY` | Naira — Statics + Riya Collab Reel · ₹1,000/day › Naira · STORIES only · Women 20-55 · Metro 25km | Plain | 'Woven, not cast.' | ₹1,333 | 689 | 5.81% | 5.37% | ₹33.32 | ₹1,935 | n/a | 1 | ₹1,333 | 1.46× | 1.46× |
| `Story · 01-E1 · PAVÉ` | Naira · IG Top 20 · Stories + Feed › IG Stories · Top 20 · High stock | Crazy / concept | 'PAVÉ' | ₹1,044 | 649 | 3.08% | 2.77% | ₹52.19 | ₹1,608 | n/a | 1 | ₹1,044 | 2.30× | 2.30× |
| `CT1 · Earrings (14 in stock)` | catalogue testing › Catalogue test · | Plain | Catalogue tests CT1–CT3 | ₹978 | 24,552 | 0.95% | 0.81% | ₹4.20 | ₹40 | n/a | 0 | — | 0.00× | 0.00× |
| `A1 · Woven Gold Hoops` | Naira — Statics + Riya Collab Reel · ₹1,000/day › Naira · FEED only · Women 20-55 · Metro 25km | Plain | 'Woven, not cast.' | ₹882 | 456 | 3.51% | 1.97% | ₹55.12 | ₹1,934 | n/a | 0 | — | 0.00× | 0.00× |
| `Story · ccv1-A1 · Apricot · Woven Gold Hoops` | Naira · IG Top 20 · Stories + Feed › IG Stories · Top 20 · High stock | Plain | Colour Camps · Apricot | ₹868 | 459 | 2.83% | 2.61% | ₹66.79 | ₹1,892 | n/a | 0 | — | 0.00× | 0.00× |
| `STORY · C3 Molten Bloom Hoops` | Naira — Sept Test · COLD / WARM / HOT · 3 sets › 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | Crazy / concept | 'Poured, not made.' | ₹696 | 538 | 7.25% | 6.69% | ₹17.84 | ₹1,294 | n/a | 1 | ₹696 | 1.90× | 1.90× |
| `ad 101 – Copy` | one winner – Copy › main- one main ad set – Copy | Plain | Catalogue · 'ad 101' | ₹696 | 5,434 | 1.20% | 1.03% | ₹10.70 | ₹128 | n/a | 0 | — | 0.00× | 0.00× |
| `FEED · S2 Woven Gold Hoops v2` | Naira — Sept Test · COLD / WARM / HOT · 3 sets › 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | Crazy / concept | 'It has been rolling for miles.' | ₹587 | 623 | 5.62% | 4.65% | ₹16.76 | ₹942 | n/a | 0 | — | 0.00× | 0.00× |

## 10. What the winners have in common

Source: Meta Ads API, lifetime, corrected; tags from the images viewed. Small numbers throughout: treat these as leads to test, not laws.

| Pattern | Evidence |
|---|---|
| **The joke is in the picture, on the product** | Visual puns where the piece is the punchline (sweets bowl "Almost edible", hoop rolling a braid track "Rolling for miles", molten drip "Poured, not made", Pick 'n' Mix) returned **1.37×** on ₹22,855 (13 sales). Puns only in the words on a plain image ("Sweet On You" on a coral gradient; Garba copy on the oxblood hoops) returned **0.58×** on ₹7,542 (2 sales). |
| **Copy-only concepts got starved** | Gift-tag, Q&A and type-as-image ads (12 ads) got just ₹657 of delivery from Meta in the IG Top 20 ad sets and made no sale. The dictionary-style Pavé card was the exception: 1 sale on ₹1,089 across its two ads. The idea has to read in the thumbnail, not in the paragraph. |
| **Props and worlds that worked** | Food (gummy sweets), measuring tools (brass calliper, ruler), craft materials (clay track, pigment powder), molten metal. Props that did not show a win: halved apricot (0.73× across versions), wet oxblood dome (0.54×), fabric roll, spotlight on black. |
| **Product: lead with the Prism Rivière** | Concept ads on the Prism bracelet (₹2,399) made 12 of the 16 concept sales at **1.63×**. Hoops (₹1,499–1,799) top out lower: concept 1.07×, plain 0.65×. At ₹1,500–3,000 per sale a ₹1,499 piece cannot reach break-even, whatever the creative. |
| **Palette: light, pastel, cream** | Light-ground concept statics 1.35× on ₹23,942. Light plain 0.63×. Dark or saturated plain (oxblood, black, maroon) 0.49×. In the second ad account, the three boosted posts, all dark and oxblood-toned, returned 0.33× combined (Appendix B). |
| **Still life beat on-body, so far** | Still-life concept 1.45×; still-life plain 0.58×; creator on-body video 0.69×. On-body statics (Gold that stays, Q&A, What I wear) got under ₹400 together: **untested, not failed**. |
| **Image beat video on sales; video drew the most clicks** | Statics 1.04× on ₹50,632; creator video 0.69× on ₹45,740; catalogue 0.49×. Creator reels had the highest CTR (all) (4.92% pooled) and 20.4% / 13.7% hook rates, but only 7% / 4% watched a quarter, and they bought expensive impressions (Pankti ₹944 CPM in a luxury-interest audience). Riya's reel spent 3–4 seconds on her face before any jewellery appeared; it had the lower hook rate and quarter-view rate (Ad Shortlist). |
| **Within plain: craft close-up beat daily-wear framing** | Two catalogue ads in the same broad ad set (Clean Metro, Metro · A): "finished to be seen up close" made 10 sales at 0.95× on ₹22,267; "made for daily wear" made 2 sales at 0.17× on ₹16,704. Across all ad sets: 4.1 against 2.1 add-to-carts per ₹1,000 (The 8+ Edit reports 3.8 against 2.2 from an earlier window). The two also used different product sets, so copy and product mix are tangled. |
| **Indian references: almost no data** | The only Indian-reference ad that ran was the Garba line ("Garba moves in circles. So do these.") on the plain oxblood hoops image: ₹2,603, 1 sale, 0.58×. The Diwali, Hinglish and "Kisne diya? Maine." pieces on the boards have not run yet. |
| **Placement: Feed over Stories over Reels** | Concept statics: IG Feed 1.79×, IG Stories 1.36×. Plain statics: IG Feed 0.53×, IG Stories 0.36×. Reels: catalogue 0.49×, creator 0.45×. Same Apricot image: Feed 1.49×, Story 0.24×. |
| **Copy hooks** | The winner pairs a two-word visual headline with a plain-spoken correction ("Almost edible. *cubic zirconia, not candy.*"). Concrete numbers drew carts: The Width ("25 millimetres across") got 13 add-to-carts on 37 landing views. Claims alone ("Woven, not cast.", "Gold that stays.") did not lift results. |

## 11. Rules for the next camps

1. **Make the product the punchline of a visual pun** (sweets, tools, materials, physics), legible in the thumbnail. Visual puns returned 1.37× on 13 sales; puns carried only in the words returned 0.58×. Don't put the idea only in the type, a gift tag or a Q&A card: Meta barely served those (12 ads, ₹657, no sale).
2. **Lead with the Prism Rivière and other ₹2,000+ pieces or bundles.** Prism concept ads made 12 of the 16 concept sales at 1.63×. A single ₹1,499 pair of hoops can't pay for ₹1,500–3,000 per sale, so put hoops into a bundle or gift-set offer.
3. **Use light, pastel or cream grounds.** Retire the oxblood and black "moody plinth" look for prospecting: it was the worst-performing static family (0.49×) and ran 0.33× again in the second account.
4. **Build for 4:5 Feed first and treat Stories as secondary.** Skip Reels for statics and catalogue.
5. **Keep a plain control in every test, and make it a craft close-up.** Plain shots win add-to-carts and Facebook Feed sales, and the founder's own best hoops days came from one. Among plain ads, the close-up catalogue set beat the daily-wear set 0.95× to 0.17× in the same ad set. Run each new crazy concept against a plain close-up of the same product, in the same ad set, with Meta's creative test or equal budgets. That way the next verdict is not confounded.
6. **Judge on cost per purchase, with add-to-cart as the early read.** Don't judge on CTR. Concept ads won outbound CTR 10 of 10 times, yet creator reels had the highest CTR and lost money, and plain ads had the most carts and fewer sales.
7. **If you use creator video, open on the piece, not the face, and run it broad.** Riya's reel showed 3–4 seconds of face before any jewellery: 13.7% hook rate, 4% watched a quarter. Pankti's unboxing had 20.4% and 7%, and the best clicks and carts of the reels (Ad Shortlist). It made 8 sales but still lost money (0.79×) because its narrow luxury-interest audience cost ₹944 per 1,000 impressions.
8. **Test the untested before ruling it out:** on-body statics, Indian and festive (Diwali) concepts, and a visual-pun concept for hoops in a light palette. Each needs about ₹2,500–3,000 of spend to show even one or two sales.

## 12. Caveats

- **Thin data.** 53 genuine attributed purchases on ₹1,59,164, and 16 for the whole concept group. Ten of the 16 came from one image. As the Stock Plan puts it, even 20 sales at a measured 3× would still leave a range of 1.8–4.6×, so no single creative here has a firm number.
- **Confounding.** Creative type was not randomised. It moved together with campaign, audience, placement and date: catalogue and creator reels ran in August and early September, concept statics from late September. Sections 5.1–5.4 control for each of these one at a time, but not all at once.
- **Attribution.** These are Meta-attributed purchases (7-day click, 1-day view), not Shopify-verified, except for the 9 removals. Early weeks had a pixel split and a deduplication fault (`platform-data.md`, `attribution-correction-29aug.md`), which mostly touched the August catalogue ads.
- **Labels.** The 18 September test ads were labelled from 64-px thumbnails (marked *unsure*). Three borderline groups are tested in 5.5. None of these changes the direction of the result.
- **No hook or thumbstop data for statics.** Motion's trial has ended and Meta reports no such metric for images. Outbound CTR stands in as the attention measure.
- **Spend after 12 Oct** is ₹97 across three statics created on 15–16 Oct. Delivery stopped on the evening of 12 Oct over an unpaid balance and had only just restarted, so the window effectively ends on 12 Oct.

## Appendix A. All 108 Naira ads with spend

Source: Meta Ads API, account 903466039148509, lifetime, pulled 15–16 Oct 2026.

| Ad name | Ad set | Created | Label | Creative | Spend | Impr. | Outbound CTR | Purchases | ROAS | ROAS corrected |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| `pankti collab reel` | Pankti collab · INT Luxury + First-class travel × Shoppers · A+A ON · 7 metros | 2026-08-30 | Creator UGC | Pankti collab reel | ₹28,182 | 29,855 | 2.73% | 8 | 0.79× | 0.79× |
| `A · Finish / close-up (set 1)` | Metro · A · BROAD no interests · A+A ON · 7 metros · geo-expand OFF | 2026-08-29 | Plain | Catalogue · Clean Metro A 'Finish' | ₹22,267 | 3,15,675 | 1.46% | 10 | 0.95× | 0.95× |
| `riya reel` | Riya collab reel · INT Online shopping × Shoppers · A+A ON · 7 metros | 2026-09-02 | Creator UGC | Riya collab reel | ₹17,382 | 49,013 | 1.87% | 6 | 0.71× | 0.54× |
| `B · Daily wear — cleaned copy (set 2)` | Metro · A · BROAD no interests · A+A ON · 7 metros · geo-expand OFF | 2026-08-29 | Plain | Catalogue · Clean Metro B 'Daily wear' | ₹16,704 | 1,66,137 | 1.73% | 2 | 0.17× | 0.17× |
| `104 bracelet ad – Copy` | main- one main ad set – Copy | 2026-09-23 | Crazy / concept | 'Almost edible.' | ₹15,765 | 28,163 | 2.92% | 10 | 1.67× | 1.67× |
| `jewellery catalogue ad 2` | jewellery 2  broad ctalgoue 2 set – Copy | 2026-08-24 | Plain | Catalogue · Aug launch | ₹8,948 | 3,37,486 | 1.65% | 8 | 3.68× | 0.00× |
| `A6 · Sweet On You · bracelets` | Naira · FEED only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'Sweet On You.' | ₹4,917 | 4,525 | 2.59% | 1 | 0.58× | 0.58× |
| `Story · ccquiet-A1 · Apricot quiet · Woven Gold Hoops` | IG Stories · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Apricot | ₹4,533 | 4,982 | 3.09% | 1 | 0.24× | 0.24× |
| `CT3 · Necklaces + Bracelets (13 in stock)` | Catalogue test · | 2026-09-25 | Plain | Catalogue tests CT1–CT3 | ₹4,066 | 55,276 | 1.04% | 1 | 0.53× | 0.53× |
| `Feed · ccquiet-A1 · Apricot quiet · Woven Gold Hoops` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Apricot | ₹4,033 | 6,306 | 2.03% | 4 | 1.49× | 1.49× |
| `A · Finish / close-up (set 1)` | Metro · B · INT category: Jewellery + Silver + Necklace · A+A ON · geo-expand ON | 2026-09-16 | Plain | Catalogue · Clean Metro A 'Finish' | ₹3,705 | 86,260 | 1.37% | 2 | 0.87× | 0.87× |
| `105 golden woops – Copy` | main- one main ad set – Copy | 2026-09-23 | Plain | 'Woven, not cast.' | ₹2,467 | 2,770 | 3.32% | 1 | 0.61× | 0.61× |
| `W2 · STORY · S2 Woven Gold Hoops v2` | Winners · RETARGET warm + hot · Feed + Stories · A+A OFF · purchasers excluded | 2026-09-15 | Crazy / concept | 'It has been rolling for miles.' | ₹2,090 | 1,332 | 4.73% | 1 | 0.85× | 0.85× |
| `B · Daily wear — cleaned copy (set 2)` | Metro · C · INT brands: Swarovski + Pandora + Cartier × Shoppers · A+A ON · geo-expand ON | 2026-09-16 | Plain | Catalogue · Clean Metro B 'Daily wear' | ₹1,940 | 43,315 | 1.30% | 0 | 0.00× | 0.00× |
| `A7 · The Demi-Fine Edit — bracelets` | Naira · FEED only · Women 20-55 · Metro 25km | 2026-08-29 | Crazy / concept | 'Almost edible.' | ₹1,740 | 1,907 | 4.67% | 0 | 0.00× | 0.00× |
| `W3 · STORY · S1 Woven Gold Hoops` | Winners · RETARGET warm + hot · Feed + Stories · A+A OFF · purchasers excluded | 2026-09-15 | Plain | 'Woven, not cast.' | ₹1,618 | 975 | 2.77% | 0 | 0.00× | 0.00× |
| `A · Finish / close-up (set 1)` | Metro · D · INT Indian designers + Online shopping · A+A ON · geo-expand ON | 2026-09-16 | Plain | Catalogue · Clean Metro A 'Finish' | ₹1,552 | 38,874 | 1.47% | 1 | 1.03× | 1.03× |
| `Feed · 08-M2 · THE WIDTH.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | 'THE WIDTH.' | ₹1,359 | 1,296 | 2.85% | 1 | 1.10× | 1.10× |
| `catalalogue 1` | ad set 1 broad – Copy 2 | 2026-08-24 | Plain | Catalogue · Aug launch | ₹1,341 | 60,539 | 2.02% | 0 | 0.00× | 0.00× |
| `S1 · Woven Gold Hoops · STORY` | Naira · STORIES only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'Woven, not cast.' | ₹1,333 | 689 | 5.37% | 1 | 1.46× | 1.46× |
| `Story · 01-E1 · PAVÉ` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | 'PAVÉ' | ₹1,044 | 649 | 2.77% | 1 | 2.30× | 2.30× |
| `CT1 · Earrings (14 in stock)` | Catalogue test · | 2026-09-25 | Plain | Catalogue tests CT1–CT3 | ₹978 | 24,552 | 0.81% | 0 | 0.00× | 0.00× |
| `A1 · Woven Gold Hoops` | Naira · FEED only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'Woven, not cast.' | ₹882 | 456 | 1.97% | 0 | 0.00× | 0.00× |
| `Story · ccv1-A1 · Apricot · Woven Gold Hoops` | IG Stories · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Apricot | ₹868 | 459 | 2.61% | 0 | 0.00× | 0.00× |
| `STORY · C3 Molten Bloom Hoops` | 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | 'Poured, not made.' | ₹696 | 538 | 6.69% | 1 | 1.90× | 1.90× |
| `ad 101 – Copy` | main- one main ad set – Copy | 2026-09-23 | Plain | Catalogue · 'ad 101' | ₹696 | 5,434 | 1.03% | 0 | 0.00× | 0.00× |
| `FEED · S2 Woven Gold Hoops v2` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | 'It has been rolling for miles.' | ₹587 | 623 | 4.65% | 0 | 0.00× | 0.00× |
| `S7 · The Demi-Fine Edit — bracelets · STORY` | Naira · STORIES only · Women 20-55 · Metro 25km | 2026-08-29 | Crazy / concept | 'Almost edible.' | ₹495 | 338 | 5.92% | 0 | 0.00× | 0.00× |
| `FEED · C3 Molten Bloom Hoops` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | 'Poured, not made.' | ₹399 | 293 | 5.12% | 0 | 0.00× | 0.00× |
| `Feed · ccquiet-L1 · Lilac quiet · Prism Rivière` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Lilac | ₹310 | 392 | 2.04% | 0 | 0.00× | 0.00× |
| `W4 · FEED · S2 Woven Gold Hoops v2` | Winners · RETARGET warm + hot · Feed + Stories · A+A OFF · purchasers excluded | 2026-09-15 | Crazy / concept | 'It has been rolling for miles.' | ₹304 | 219 | 4.11% | 0 | 0.00× | 0.00× |
| `Feed · WH-C2 · Light.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | Worlds · type-as-image | ₹299 | 539 | 2.23% | 0 | 0.00× | 0.00× |
| `FEED · L6 Verdant Drop Earrings` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹290 | 326 | 4.29% | 0 | 0.00× | 0.00× |
| `STORY · S6 Pearl Point Studs v2` | 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹272 | 221 | 4.07% | 0 | 0.00× | 0.00× |
| `Story · 13-G2 · PASTEL.` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | 'PASTEL.' | ₹265 | 192 | 4.69% | 0 | 0.00× | 0.00× |
| `STORY · P3 Baroque Pearl Lariat` | 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | Sept Edit · pearl lariat dipped in milk | ₹254 | 174 | 5.75% | 0 | 0.00× | 0.00× |
| `catalalogue 1` | ad set 1 broad – Copy 3 | 2026-08-27 | Plain | Catalogue · Aug launch | ₹216 | 2,420 | 1.65% | 0 | 0.00× | 0.00× |
| `104 bracelet ad` | main- one main ad set | 2026-09-21 | Crazy / concept | 'Almost edible.' | ₹213 | 194 | 6.19% | 0 | 0.00× | 0.00× |
| `Feed · WH-C5 · Link.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | Worlds · type-as-image | ₹201 | 286 | 2.80% | 0 | 0.00× | 0.00× |
| `Feed · ccv1-A1 · Apricot · Woven Gold Hoops` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Apricot | ₹190 | 162 | 3.70% | 0 | 0.00× | 0.00× |
| `S2 · Cushion Halo Ring · STORY` | Naira · STORIES only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'One pool of light.' | ₹187 | 120 | 4.17% | 0 | 0.00× | 0.00× |
| `STORY · S2 Woven Gold Hoops v2` | 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | 'It has been rolling for miles.' | ₹181 | 108 | 8.33% | 1 | 9.79× | 9.79× |
| `B · Daily wear — cleaned copy (set 2)` | Metro · D · INT Indian designers + Online shopping · A+A ON · geo-expand ON | 2026-09-16 | Plain | Catalogue · Clean Metro B 'Daily wear' | ₹157 | 11,550 | 1.50% | 0 | 0.00× | 0.00× |
| `Feed · NT-B4 · What I wear to the airport.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Plain | Naira Ten · 'What I wear to…' | ₹152 | 113 | 2.65% | 0 | 0.00× | 0.00× |
| `FEED · P3 Baroque Pearl Lariat` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | Sept Edit · pearl lariat dipped in milk | ₹147 | 70 | — | 0 | 0.00× | 0.00× |
| `CT2 · Rings (12 in stock)` | Catalogue test · | 2026-09-25 | Plain | Catalogue tests CT1–CT3 | ₹140 | 1,639 | 1.04% | 0 | 0.00× | 0.00× |
| `STORY · C1 Prism Riviere Bracelet` | 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | Sept Edit · 'It splits the light' | ₹137 | 141 | 3.55% | 0 | 0.00× | 0.00× |
| `105 golden woops` | main- one main ad set | 2026-09-21 | Plain | 'Woven, not cast.' | ₹136 | 108 | 6.48% | 0 | 0.00× | 0.00× |
| `FEED · S1 Heartline Paperclip Necklace v2` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹136 | 164 | 4.88% | 0 | 0.00× | 0.00× |
| `Feed · 13-G2 · PASTEL.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | 'PASTEL.' | ₹120 | 119 | 2.52% | 1 | 33.30× | 33.30× |
| `A5 · Heartbead Bracelet` | Naira · FEED only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'One warm note.' | ₹118 | 31 | — | 0 | 0.00× | 0.00× |
| `FEED · L8 Pearl Blossom Earrings` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹107 | 141 | 2.13% | 0 | 0.00× | 0.00× |
| `STORY · R1 Pearl Ribbon Ring` | 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | Sept Edit · ring on a red wax seal | ₹106 | 74 | 1.35% | 0 | 0.00× | 0.00× |
| `Feed · NT-B5 · What I wear to brunch.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Plain | Naira Ten · 'What I wear to…' | ₹103 | 103 | 1.94% | 0 | 0.00× | 0.00× |
| `FEED · L5 Verdant Circlet Studs` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹99 | 99 | 2.02% | 0 | 0.00× | 0.00× |
| `ad 102 reel riya – Copy` | main- one main ad set – Copy | 2026-09-23 | Creator UGC | Riya collab reel | ₹98 | 383 | 0.78% | 0 | 0.00× | 0.00× |
| `Story · 11-S1 · PICK 'N' MIX.` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | 'PICK 'N' MIX.' | ₹98 | 107 | 2.80% | 0 | 0.00× | 0.00× |
| `FEED · S3 Baroque Shell Bracelet v2` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹96 | 115 | 5.22% | 0 | 0.00× | 0.00× |
| `FEED · C1 Prism Riviere Bracelet` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | Sept Edit · 'It splits the light' | ₹86 | 73 | 2.74% | 0 | 0.00× | 0.00× |
| `Story · 08-M2 · THE WIDTH.` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | 'THE WIDTH.' | ₹85 | 51 | 7.84% | 0 | 0.00× | 0.00× |
| `FEED · S6 Pearl Point Studs v2` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹78 | 31 | — | 0 | 0.00× | 0.00× |
| `Feed · WH-D4 · 07:15 / 23:30` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | Hours · '07:15 / 23:30' | ₹73 | 60 | 3.33% | 0 | 0.00× | 0.00× |
| `A2 · Cushion Halo Ring` | Naira · FEED only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'One pool of light.' | ₹71 | 44 | — | 0 | 0.00× | 0.00× |
| `Static · Hoops · Apricot quiet · original post · Feed only` | Statics · Hoops · one-winner audience · IG Feed only | 2026-10-16 | Plain | Colour Camps · Apricot | ₹68 | 75 | 2.67% | 0 | 0.00× | 0.00× |
| `Feed · 11-S1 · PICK 'N' MIX.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | 'PICK 'N' MIX.' | ₹62 | 62 | — | 0 | 0.00× | 0.00× |
| `B · Daily wear — cleaned copy (set 2)` | Metro · B · INT category: Jewellery + Silver + Necklace · A+A ON · geo-expand ON | 2026-09-16 | Plain | Catalogue · Clean Metro B 'Daily wear' | ₹58 | 2,083 | 1.58% | 0 | 0.00× | 0.00× |
| `Feed · 01-E1 · PAVÉ` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | 'PAVÉ' | ₹46 | 59 | 3.39% | 0 | 0.00× | 0.00× |
| `Feed · ccframed-A1 · Apricot framed · Woven Gold Hoops` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Apricot | ₹45 | 27 | 3.70% | 0 | 0.00× | 0.00× |
| `Feed · 09-G1 · Gift · sister who borrows` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | Gift tags | ₹44 | 43 | — | 0 | 0.00× | 0.00× |
| `102 pankti reel – Copy` | main- one main ad set – Copy | 2026-09-23 | Creator UGC | Pankti collab reel | ₹41 | 61 | — | 0 | 0.00× | 0.00× |
| `FEED · R1 Pearl Ribbon Ring` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | Sept Edit · ring on a red wax seal | ₹39 | 18 | — | 0 | 0.00× | 0.00× |
| `FEED · L3 Bold Nocturne Bracelet` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Crazy / concept | Sept Edit · 'It keeps going' | ₹39 | 15 | 6.67% | 0 | 0.00× | 0.00× |
| `Story · ccframed-A1 · Apricot framed · Woven Gold Hoops` | IG Stories · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Apricot | ₹37 | 27 | — | 0 | 0.00× | 0.00× |
| `102 pankti reel` | main- one main ad set | 2026-09-21 | Creator UGC | Pankti collab reel | ₹36 | 67 | 4.48% | 0 | 0.00× | 0.00× |
| `Feed · ccv1-L1 · Lilac · Prism Rivière` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Lilac | ₹33 | 49 | — | 0 | 0.00× | 0.00× |
| `A4 · Heartline Paperclip Necklace` | Naira · FEED only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'Links, and a little light.' | ₹32 | 22 | 4.55% | 0 | 0.00× | 0.00× |
| `Story · 09-G3 · Gift · friend who wears colour` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | Gift tags | ₹30 | 32 | 3.12% | 0 | 0.00× | 0.00× |
| `Feed · NT-A5 · Gold that stays.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Plain | Naira Ten · 'Gold that stays.' | ₹29 | 22 | 4.55% | 0 | 0.00× | 0.00× |
| `A3 · Serpentine Whisper Chain` | Naira · FEED only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'The quiet solitaire.' | ₹28 | 35 | 2.86% | 0 | 0.00× | 0.00× |
| `FEED · L4 Halo Curve Ring` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹27 | 9 | — | 0 | 0.00× | 0.00× |
| `STORY · S3 Baroque Shell Bracelet v2` | 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹27 | 18 | 11.11% | 0 | 0.00× | 0.00× |
| `Story · NT-B5 · What I wear to brunch.` | IG Stories · Top 20 · High stock | 2026-09-30 | Plain | Naira Ten · 'What I wear to…' | ₹26 | 27 | — | 0 | 0.00× | 0.00× |
| `Static · Hoops · The Width v2 (no tarnish claim) · Feed only` | Statics · Hoops · one-winner audience · IG Feed only | 2026-10-16 | Crazy / concept | 'THE WIDTH.' | ₹26 | 21 | 4.76% | 0 | 0.00× | 0.00× |
| `Story · 10-A2 · will it tarnish? NO.` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | Objection answers | ₹23 | 15 | 6.67% | 0 | 0.00× | 0.00× |
| `S5 · Heartbead Bracelet · STORY` | Naira · STORIES only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'One warm note.' | ₹23 | 23 | — | 0 | 0.00× | 0.00× |
| `S6 · Sweet On You · STORY` | Naira · STORIES only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'Sweet On You.' | ₹22 | 14 | — | 0 | 0.00× | 0.00× |
| `STORY · S1 Heartline Paperclip Necklace v2` | 6 · RETARGET STORY 9x16 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹19 | 10 | 20.00% | 0 | 0.00× | 0.00× |
| `FEED · L7 Clover Trio Edit` | 5 · RETARGET FEED 4x5 · VC30d + Cart14d · excl purchasers | 2026-09-12 | Plain | Sept Edit · product on lilac / neutral ground | ₹19 | 34 | — | 0 | 0.00× | 0.00× |
| `Story · WH-D4 · 07:15 / 23:30` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | Hours · '07:15 / 23:30' | ₹19 | 10 | — | 0 | 0.00× | 0.00× |
| `Story · 10-A5 · will it fit my wrist? 15 TO 19.` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | Objection answers | ₹18 | 9 | — | 0 | 0.00× | 0.00× |
| `Story · gr-02 · The clasp is the design` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | Graphite · 'The clasp is the design' | ₹16 | 16 | — | 0 | 0.00× | 0.00× |
| `Story · ccv1-L1 · Lilac · Prism Rivière` | IG Stories · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Lilac | ₹15 | 22 | — | 0 | 0.00× | 0.00× |
| `Feed · gr-02 · The clasp is the design` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | Graphite · 'The clasp is the design' | ₹14 | 28 | 3.57% | 0 | 0.00× | 0.00× |
| `A · Finish / close-up (set 1)` | Metro · C · INT brands: Swarovski + Pandora + Cartier × Shoppers · A+A ON · geo-expand ON | 2026-09-16 | Plain | Catalogue · Clean Metro A 'Finish' | ₹14 | 2,117 | 1.32% | 0 | 0.00× | 0.00× |
| `S4 · Heartline Paperclip Necklace · STORY` | Naira · STORIES only · Women 20-55 · Metro 25km | 2026-08-29 | Plain | 'Links, and a little light.' | ₹12 | 4 | — | 0 | 0.00× | 0.00× |
| `Story · WH-C2 · Light.` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | Worlds · type-as-image | ₹12 | 18 | — | 0 | 0.00× | 0.00× |
| `ad 101` | main- one main ad set | 2026-09-21 | Plain | Catalogue · 'ad 101' | ₹10 | 25 | — | 0 | 0.00× | 0.00× |
| `Feed · 10-A5 · will it fit my wrist? 15 TO 19.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | Objection answers | ₹9 | 13 | — | 0 | 0.00× | 0.00× |
| `Story · NT-A5 · Gold that stays.` | IG Stories · Top 20 · High stock | 2026-09-30 | Plain | Naira Ten · 'Gold that stays.' | ₹7 | 7 | — | 0 | 0.00× | 0.00× |
| `Story · WH-C5 · Link.` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | Worlds · type-as-image | ₹7 | 10 | — | 0 | 0.00× | 0.00× |
| `Story · 09-G1 · Gift · sister who borrows` | IG Stories · Top 20 · High stock | 2026-09-30 | Crazy / concept | Gift tags | ₹6 | 7 | — | 0 | 0.00× | 0.00× |
| `Feed · 09-G3 · Gift · friend who wears colour` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | Gift tags | ₹6 | 10 | — | 0 | 0.00× | 0.00× |
| `Static · Hoops · Apricot quiet · original post` | Statics · Prism · one-winner audience · IG Feed + Stories | 2026-10-15 | Plain | Colour Camps · Apricot | ₹4 | 7 | — | 0 | 0.00× | 0.00× |
| `W1 · STORY · C3 Molten Bloom Hoops` | Winners · RETARGET warm + hot · Feed + Stories · A+A OFF · purchasers excluded | 2026-09-15 | Crazy / concept | 'Poured, not made.' | ₹3 | 4 | — | 0 | 0.00× | 0.00× |
| `Story · ccquiet-L1 · Lilac quiet · Prism Rivière` | IG Stories · Top 20 · High stock | 2026-09-30 | Plain | Colour Camps · Lilac | ₹2 | 10 | — | 0 | 0.00× | 0.00× |
| `Story · NT-B4 · What I wear to the airport.` | IG Stories · Top 20 · High stock | 2026-09-30 | Plain | Naira Ten · 'What I wear to…' | ₹1 | 2 | — | 0 | 0.00× | 0.00× |
| `Feed · 10-A2 · will it tarnish? NO.` | IG Feed posts · Top 20 · High stock | 2026-09-30 | Crazy / concept | Objection answers | ₹1 | 3 | — | 0 | 0.00× | 0.00× |
| `ad 102 reel riya` | main- one main ad set | 2026-09-21 | Creator UGC | Riya collab reel | ₹1 | 4 | — | 0 | 0.00× | 0.00× |

## Appendix B. Spend left out of the comparison

| Account / campaigns | What it advertised | Spend | Impressions | Result | Why excluded |
|---|---|---:|---:|---|---|
| 903466039148509: `New Sales campaign` (11 Mar), `Cbo / 24 Mar`, `Cb / 20 May`. 22 ads: `New Sales ad`, `Video 2–4`, `Reel 4/15/33/34`, `Carosel` | Naira Flore couture lehengas (copy: "handcrafted designer lehengas") | ₹55,540 | 20,63,470 | 0 purchases; CTR (all) ~9% at ₹0.30 CPC | Not jewellery; delivery flagged as junk placements in `platform-data.md` |
| 1088886349394166: three boosted Instagram posts (16–17 Sep): "The one you reach for…" (halo ring on a hand), "Gold, caught mid-thought" (Molten Bloom hoops on a wet oxblood dome), "Lac bone asks you to slow down" (brand mood video) | Naira jewellery; all three **plain** | ₹12,405 | 49,464 | 2 purchases, ₹4,049 → **0.33×** | Separate account and boost settings. If added to the plain group it lowers plain ROAS further (corrected plain: ₹98,668, 26 sales, ₹48,507 → 0.49×) |
| 1088886349394166: `Naira \| Lead Camp \| Dec 2025` | Custom couture (lead form) | ₹14,111 | 1,60,462 | 189 leads | Couture, lead objective |
| 1498422677060515 | An unrelated medical (adenoids) WhatsApp campaign | ₹43,196 | 18,12,643 | — | Not Naira |

## Appendix C. Method notes

- **Pull:** `ads_get_ad_entities` (level = ad, date_preset = maximum) with fields amount_spent, impressions, reach, ctr, cpc, cpm, outbound_clicks, outbound_clicks_ctr, landing_page_view, omni_add_to_cart, omni_initiated_checkout, omni_purchase, omni_purchase_values, purchase_roas, results, cost_per_result, video_play_actions, video_p25_watched_actions, video_thruplay_watched_actions and creative_id. A second pull broke the same ads down by `publisher_platform` × `platform_position`. A third, at ad-set level, gave `3_second_video_plays`. Field names were checked with `ads_get_field_context`. Nothing in any account was created, edited, paused or activated.
- **Totals reconcile:** 108 Naira ads, ₹1,59,164.15, 62 purchases, ₹1,51,215.53. The Stock Plan's 14 Oct audit (105 ads, ₹1,59,067) is the same set minus three ads created on 15–16 Oct with ₹97 of spend.
- **Spend-weighted averages:** a group's ROAS is Σrevenue ÷ Σspend. Spend-weighted CTR, CPC and CPM are Σ(spend × ad rate) ÷ Σspend. Pooled rates are Σclicks ÷ Σimpressions and so on.
- **Intervals and tests:** exact (Garwood) 95% Poisson intervals on purchase counts, scaled by the group's average order value. Group comparisons use the exact conditional binomial test for two Poisson rates (purchases per rupee).
- **Scripts and intermediate files** are in the session scratchpad, not in this repository.
