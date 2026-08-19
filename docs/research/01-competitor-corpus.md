# A — Competitor Advertising Research Corpus

Consolidated, machine-readable reference for Naira Petite's creative team. Built by reading four Claude artifacts in full and reproducing their numbers without rounding, summarising away, or inventing. Compiled 19 Aug 2026.

## 0. Source read status

| # | Document | URL | Status |
|---|---|---|---|
| 1 | Six Ways to Sell Jewellery | `.../artifact/2c47276b-9c48-4a61-8fe3-cffaf1d9f6bf` | **Read in full.** 498 creatives, 6 brands, dated pull 19 Aug 2026. |
| 2 | Palmona — Paid Social Creative Brief | `.../artifact/07c6c7a6-5d6e-4242-ab24-9a394c61c482` | **Read in full**, including the sections truncated on first fetch (Struck falsehoods table, Next/test-slate section, Open questions). Compiled 8 Aug 2026. |
| 3 | Naira Petite · Demi-Fine Competitive Dossier | `.../artifact/8a6d0ba1-d29a-4e05-8f14-d68dfad33823` | **Read in full**, including the embedded JSON data block (`players`: 22 records, `hooks`: 20 records, `priced`: 63 Naira SKUs) that the visible page renders client-side. Dated July 2026. |
| 4 | The Swarovski Benchmark | `.../artifact/895eb60f-7fb8-4623-a80f-96566f7ec4c5` | **Read in full**, including the capability-matrix table's `aria-label` fill states (strong/partial/none), which are not visible as text in the rendered page. Dated August 2026. |

No document was unreadable and nothing is missing. Two data gaps exist **inside** the source documents themselves (not fetch failures) and are flagged in place below: (a) Six Ways gives routing/destination percentages for only 3 of its 6 brands, and copy-length medians for only 2; (b) no document in this corpus states a CPM or CTR benchmark for jewellery — only ROAS, CAC, CVR and CPA figures exist in the sources, so CPM/CTR are recorded as absent rather than estimated.

**Naming flag, read before using this file:** Document 2 refers throughout to a brand called **"Palmona"** (no terminal s) — "a Palmona ad," "Palmona's price band." Documents 1 and 3 refer throughout to **"Palmonas"** (with a terminal s) — a specific, identifiable, funded Indian brand (₹39 Cr FY25 revenue, Shraddha Kapoor co-founder, Shark Tank, 1.03M followers). Document 2 never mentions Shraddha Kapoor, Shark Tank, or any revenue figure, and never resolves its own brand's price band ("Palmona's price band and range" is listed as an *open question* in Document 2's closing section). Treat these as two distinct labels unless you can confirm otherwise — this file does not silently merge them. See §9 for the full analysis.

---

## 1. Per-brand creative profiles

### 1.1 — The six live-ad accounts (Source: Six Ways to Sell Jewellery, Motion swipe file, pulled 19 Aug 2026)

This is the only document with ad-performance metrics (creative counts, image/video split, offer %, urgency %, impression rank). Impression rank is Motion's cross-library position, relative and reach-based — **not** a spend or conversion figure.

| Brand | Live creatives pulled | Active total (library) | Coverage | Image | Video | % copy carries offer | % urgency language | Median rank | Best rank | Followers |
|---|---|---|---|---|---|---|---|---|---|---|
| Palmonas | 150 | 411 | newest 150 | 106 | 44 | 58% | 23% | 701 | 19 | 1.03M |
| GIVA | 151 | 369 | newest 151 | 111 | 40 | 80% | 9% | 621 | 122 | 1.56M |
| Rubans | 97 | 97 | complete | 37 | 60 | 62% | 9% | 110 | 27 | 308K |
| CaratLane | 53 | 53 | complete | 35 | 18 | 49% | 2% | 70 | 5 | 3.9M |
| Tyaani Jewellery | 35 | 47 | newest 35 | 19 | 16 | 0% | 0% | 63 | 1 | 785K |
| Voylla | 12 | 12 | complete | 9 | 3 | 0% | 0% | 62 | 5 | 1.29M |

Caveat stated in the source itself: Palmonas, GIVA and Tyaani are "the newest slice of a larger [library]," so their creative age skews young and is **not directly comparable** to the three complete libraries (Rubans, CaratLane, Voylla).

**Positioning line, the tell, and named campaigns — verbatim per brand**

**Palmonas** — *Demi fine · 1.03M followers.*
Positioning (source prose): "The volume machine, now going physical." Strategy shift beneath the 30-day window: store openings in Panipat, Noida and Delhi; 24KT gold from ₹5,000; lab-grown diamonds; an Emily in Paris licence; a 3% armed-forces offer.
The tell: *"Their median creative ranks 701, the weakest of the six. Flooding the auction buys reach at the top and a long tail of creatives almost nobody sees."*
Named campaigns/themes: Its a Tie · 50% off · Freedom Sale · flat 40 · Lab grown diamond · Store rollout · Man of Style · men · Ode to Nature · Armed forces · 3% off · Emily in Paris collab.

**GIVA** — *Silver and lab grown · 1.56M followers.*
Positioning: "The most discount saturated account in the set," locked maroon-and-blush palette, maroon gift box as recurring hero object. Trust layer stamped onto creative: certified jewellery, anti-tarnish, hypoallergenic, making charges — a claim density no other brand in the set runs.
The tell: *"They discount hardest and rank second worst. Price Drop Alert is not a campaign, it is the house style."*
Named campaigns/themes: Buy 2 · save 15% · Price Drop Alert · Rakhi · 20% off · Anklet stack · flat off · Made to shine · Certified · anti tarnish · Anklets · Lower prices on silver.

**Rubans** — *Fashion and temple · 308K followers.*
Positioning: the only video-majority account in the set (60 video vs 37 image), mostly raw creator/UGC footage. Core product traditional (temple necklaces, jhumkas, kundan, antique gold); Buy One Get One Free is "the entire offer architecture." Social proof printed directly on the artwork: "ordered 93 times in the last 30 days," 4.4 average rating, easy returns.
The tell: *"Watch the Demifine sub line. Rubans is moving from traditional into exactly Naira's territory, and announcing it as a new launch."*
Named campaigns/themes: Demifine new launch · B1G1 · ordered 93 times · Bestselling temple · Rakhi sale · ratings badge · Creator UGC · Demifine just launched · Rakhi sale · B1G1 · Buy 1 get 1 free.

**CaratLane** — *A Tata product · 3.9M followers.*
Positioning: "Omnichannel, not e-commerce." Half the account is geo-targeted store advertising with physical addresses and phone numbers printed in the creative (Shillong, Dombivli, Ambernath, Cuddalore, a grand launch in Ranchi). Mechanic is a single Flat 30% on making charges, never stacked or varied, alongside genuine brand-film work ("Kashika," shot on the ghats of Banaras) and "Know Your Diamond" as an in-store education event.
The tell: *"They are the only brand advertising expertise. Everyone else advertises price or product."*
Named campaigns/themes: Flat 30 · store Shillong · Kashika · brand film · Solitaire Fest · Know Your Diamond · Varamahalakshmi · Ranchi store launch.

**Tyaani Jewellery** — *Karan Johar · 785K followers.*
Positioning/tagline: **"Timeless. Certified. Forever."** — zero discount badges across all 35 live creatives; the only price signal is "jewellery under ₹1.5 lacs," framed as a ceiling that grants access rather than a markdown. Editorial-fashion photography (bridal lehengas in chandelier interiors, mirror portraits, oil-painting light). Seven ads route to WhatsApp, three to Instagram.
The tell: *"The best median rank in the set at 63, and the single highest ranked creative of all 498. Proof the category can be won without a discount."*
Named campaigns/themes: Timeless. Certified. Forever. · Bridal · Gifts of Love · Now in Santacruz · Product on black · Gift of Love · bangle.

**Voylla** — *Fashion and precious · 1.29M followers.*
Positioning: "Twelve creatives, one category" — every ad is a rakhi creative, sub-segmented by recipient and motif (Kids, Kundan, Bhaiya Bhabhi, Mor Pankh, Evil Eye), plus an international-delivery axis aimed at the diaspora ("Delivering 100+ countries"). No discounts, no price in copy; "See details" rather than "Shop now" on half the set.
The tell: *"A small account beating much larger ones on median rank by refusing to compete broadly."*
Named campaigns/themes: Kids Rakhi · Kundan Rakhis · Bhaiya Bhabhi Rakhi · Mor Pankh Rakhis · Delivering 100+ countries · Evil Eye Rakhis.

### 1.2 — Additional India brands (Source: Naira Petite Dossier, `players` data, July 2026)

No ad-library performance metrics exist for these brands in any source — this is positioning/financial intelligence from brand sites, catalogues, Inc42/Entrackr/YourStory/Tracxn, Modern Retail, Glossy, WWD, Forbes and Companies House filings, not the Meta Ad Library. Where a brand also appears in §1.1 (Palmonas, GIVA, Rubans), that ad-performance data still applies; only the fields below are additive.

| Brand | Category / material | Stated price band | Lead hook (verbatim) | Revenue / scale | Growth engine |
|---|---|---|---|---|---|
| Palmonas | Demifine® 18k gold-plated steel/silver | ₹999–3,000+ | "Waterproof · tarnishproof · hypoallergenic; lifetime buyback" | ₹39 Cr FY25 (~40× YoY), profitable ₹4.3 Cr | Shraddha Kapoor co-founder · Shark Tank · DPA catalog ads |
| GIVA | 925 silver + 14k/18k gold + lab-grown | ₹599–6,000+ | "Style, Sealed in Silver; lifetime buyback, zero making charges" | ₹518 Cr FY25 (+89%); marketing spend ₹135 Cr | Anushka Sharma · 280+ stores · "₹1.15 spent per ₹1 earned" |
| Rubans | 18k/22k plated steel, waterproof | ₹500–4,000 (ASP ₹800) | "Anti-tarnish · elevate your everyday" | ₹30.5 Cr FY25; ~70% gross margin | Myntra ~75% of revenue · Shark Tank · acquired Ananta 2025 |
| **Shaya (CaratLane)** | 925 sterling silver | ₹600–11,000 | "Not Perfect But One Of A Kind (#Flawsome)" | In Titan/Tanishq | Tanishq trust + omnichannel |
| Salty | Gold-plated brass, anti-tarnish | ₹250–900 core | "Say goodbye to tarnish; Shop By Mood (Office Siren…)" | ~₹30 Cr → ₹70 Cr target | Blinkit quick-commerce 30% · micro-creators over celebrities |
| Pipa Bella (Nykaa) | Brass, gold/silver plated | ₹300–1,200 effective | "Trend, stackable, affordable" | In Nykaa Fashion | Nykaa platform merchandising |
| Melorra | 18k/14k real gold + diamonds | ₹4,000–90,000 | "Gold for every outfit; Zara-for-jewellery" | ₹364 Cr FY22 → ~₹35 Cr (fire-sale) | Cautionary tale: 33% of revenue on ads, "₹1.29 to earn ₹1" |
| Isharya | 18k gold-plated brass, hypoallergenic | ₹2,500–8,000 | "Democratize luxury; statement India-inspired" | ₹19 Cr FY25 (+37%) | Legacy demi-fine · Nykaa/AJIO/premium multi-brand outlets |
| Blingvine | CZ/AD fashion, anti-tarnish | up to ₹5,800 | "Better than real; 1-yr colour warranty" | Bootstrapped | Organic/SEO-led, light on paid |
| Outhouse | 22k gold-plated brass + Swarovski crystal | ₹10,000–35,000 | "Couture costume; runway/celebrity" | ₹16 Cr FY24 | Bootstrapped luxury · founder-influencer |
| Misho | 22k gold/rhodium-plated brass | ₹9,000–20,000 | "The shapes are the logo" | ~$8M (est.) | Organic celebrity seeding (Kendall, Rihanna) |

**Isharya and Missoma, additionally** (from the dossier's "Play" section, not the players table): "Missoma's vermeil is documented tarnishing within ~3 months; Isharya openly concedes plating tarnishes; Pipa Bella ships in ziplocks" — used in that document to argue Naira's 18K-plated 316L steel is a defensible non-tarnish/waterproof wedge against all three.

### 1.3 — Global brands (Source: Naira Petite Dossier, `players` data, July 2026)

| Brand | Category / material | Stated price band | Lead hook (verbatim) | Revenue / scale | Growth engine |
|---|---|---|---|---|---|
| Mejuri | 14k solid gold + vermeil | $80–450 (AOV $150–175) | "Fine Jewelry For Every Day · #MakeLuxuryAHabit" | ~$160–200M; 50% repeat purchase | Community + weekly drops + loyalty/app |
| Missoma | 18k gold vermeil (2.5µ) | $50–250 | "Pioneers of demi-fine; layer it yourself" | £26.5M (2024) | Influencer co-design (Lucy Williams: 30+ pieces/hr sold) |
| Astrid & Miyu | 14k/9k solid gold, welded | $65–900 | "That just welded feeling" | £34M (2023) | Experiential retail + permanent jewellery (TikTok) |
| Ana Luisa | Gold-plated, recycled | $39–150 | "Designer jewelry starting at $39; carbon neutral" | $30–40M (est.) | Influencer-DNA + YouTube storytelling |
| PDPAOLA | 925 silver + 18k plate | $85–390 (avg $150) | "Your new basics; mix & match singles" | ~€40M (2021) | 2M Instagram followers + ~45 own stores in 5 months |
| Monica Vinader | Recycled silver + 18k vermeil | $120–400+ | "Designed to empower and endure; recycled" | £108M (FY24) | Wholesale + engraving/personalisation + PR |
| Gorjana | 18k gold-plated brass + 14k fine | $45–160 core | "Jewelry you'll live in; waterproof" | ~$100M (self-funded) | Wholesale→DTC flip · ~65 own stores |
| Aurate | 14k/18k solid gold + vermeil | $150–3,200 | "Real jewelry for real life; guaranteed for life" | 400% online growth (stated, undated baseline) | Co-branded wholesale + paid social |
| Catbird | Solid 14k, 95% recycled | <$50 entry–$1,000s | "Zapping / Forever bracelets; recycled" | $10M+ (independent) | Experiential "zapping" ritual + cult PR |
| VRAI | Lab-grown diamonds + solid gold | $395–24,500 | "Carbon-neutral diamonds; true to the future" | Parent company valued $1.8B | Vertical integration + red-carpet halo effect |

### 1.4 — Hook-wall-only brands (Source: Naira Petite Dossier, `hooks` data — Meta Ad Library capture, July 2026)

These brands appear only as a single live ad-copy line each, with no positioning/price/revenue data given. India (`IN`) and Global (`GL`) as tagged in the source.

| Brand | Geo | Ad copy (verbatim) | Tag |
|---|---|---|---|
| Rare Ever | IN | "Why Thousands Trust Rare Ever 💛" | trust |
| Zitara | IN | "Real Silver. Real Shine 🤍" | authenticity |
| Priskel | IN | "Quiet Luxury, Every Day · Luxury That Loves Water" | quiet-luxury |
| Manira Luxe | IN | "Waterproof Jewellery from ₹399" | price+durability |
| Sefira | IN | "Wait… This Set Is Just ₹1,299? · COD Available" | price-shock |
| Aadhyaatmik | IN | "Made for Everyday wear (4.9/5 ⭐)" | social-proof |
| Golden Shells | IN | "Everyday Luxury, Built to Last 💛" | durability |
| Thakurani | IN | "🎁 Gift Her a Pendant She'll Treasure Forever" | gifting |
| Axesouár | IN | "Your Everyday Earrings ✨" | everyday |
| Kendra Scott | GL | "18k Gold Vermeil · 14k Yellow Gold (catalog spec)" | format |
| Sami Jewels | GL | "A Collection That Works Together · The Dainty Lariat Your Outfit Needed" | stacking |
| Ania Haie | GL | "10% Off Your First Order" | discount |
| Reclaimed With Love | GL | "Shop upcycled demi-fine jewelry for everyday wear" | sustainability |
| Tiraaya | GL | "Everyday Luxury, Made to Last" | durability |

Palmonas, GIVA, Mejuri, Ana Luisa, Astrid & Miyu and PDPAOLA also carry a hook-wall entry; those lines are folded into their §1.1/1.2/1.3 rows above rather than repeated here (Palmonas: "Dynamic catalog / Advantage+ ({{product.name}})" — format; GIVA: "Flat 15% OFF · Code NEW15" — discount).

### 1.5 — Swarovski (Source: The Swarovski Benchmark) — a different kind of profile

Swarovski is not covered as a paid-social advertiser anywhere in this corpus. Document 4 is a **supply-side sourcing document**: it scores Swarovski's own retail jewellery range against Naira's market-pull framework and then rates six Chinese manufacturers on their ability to reproduce it. None of the ad-performance fields in §1.1 (live creative count, image/video split, offer %, urgency %, impression rank, followers) exist for Swarovski in any source. What the document does give:

- **Scope:** 101 Swarovski jewellery pieces read from live US retail listings carrying the full range (Swarovski's own site blocks datacentre traffic, so it could not be read directly).
- **Overall read:** Swarovski's jewellery scores 8–9 on Naira's framework. The source attributes this explicitly to *"the setting discipline, the cut vocabulary and the fact that five families each own a clear job"* — not the crystal itself — and states this is "reproducible in brass and silver at a fraction of the cost."
- **What fails the framework:** figurines, the Disney/Marvel/Star Wars licences, zodiac pieces and the Kris Bear line score 1–3 and are explicitly excluded from the benchmark.
- Full family, price-ladder and shortlist data is in §8 below (not repeated here).

---

## 2. Vocabulary ownership matrix

Source: Six Ways to Sell Jewellery. Share of each brand's copy containing a theme; verified cell-by-cell against the raw table markup (all six brands report a value for every theme — no blanks/zeros were dropped).

| Theme | Palmonas | GIVA | Rubans | CaratLane | Tyaani | Voylla |
|---|---|---|---|---|---|---|
| rakhi | 22% | 43% | 27% | 5% | 0% | 75% |
| gifting | 25% | 30% | 24% | 15% | 25% | 16% |
| men and brothers | 26% | 20% | 1% | 1% | 0% | 41% |
| bridal | 0% | 0% | 4% | 0% | 42% | 0% |
| silver | 12% | 86% | 1% | 0% | 0% | 0% |
| gold | 26% | 11% | 5% | 7% | 11% | 0% |
| diamond | 0% | 5% | 1% | 71% | 0% | 0% |
| anti tarnish | 12% | 0% | 6% | 0% | 0% | 0% |
| hypoallergenic | 0% | 11% | 0% | 0% | 0% | 0% |
| certified | 0% | 16% | 0% | 0% | 11% | 0% |
| store and offline | 20% | 1% | 0% | 15% | 31% | 0% |

Source commentary, verbatim findings:
- "Four of the six own a word. GIVA owns silver, in eighty six percent of its copy, and is the only brand saying hypoallergenic. CaratLane owns diamond at seventy one percent. Tyaani owns bridal. Voylla owns rakhi at seventy five percent, and is the second heaviest on brothers after Palmonas."
- "Palmonas and Rubans own nothing. Their copy spreads thinly across gold, men, gifting, rakhi and stores without a majority anywhere. That is what a discount led account looks like from the language side: the offer is the message, so the vocabulary drifts."
- **The gap:** "Not one row in this table is about how a piece is made. No brand uses setting, cut, plating thickness or finishing as a theme. Anti tarnish is the closest anyone gets, and only Palmonas and Rubans touch it. The craft vocabulary is unclaimed." (This is the exact gap Document 4's Swarovski work addresses from the supply side — see §9.)

---

## 3. Offer mechanics table

Source: Six Ways to Sell Jewellery. **Counts of creatives** (not percentages) using each instrument. Verified against raw table markup cell-by-cell — GIVA and Rubans use zero of several instruments, so a dash below means the raw HTML cell was genuinely empty, not a transcription gap.

| Mechanic | Palmonas | GIVA | Rubans | CaratLane | Tyaani | Voylla |
|---|---|---|---|---|---|---|
| percent off | 55 | 118 | — | 12 | — | — |
| flat amount | 31 | 49 | — | 4 | — | — |
| buy one get one | 5 | — | 45 | — | — | — |
| promo code | 17 | 105 | — | — | — | — |
| named sale | 34 | — | 17 | — | — | — |
| price drop | — | 4 | — | — | — | — |
| free gift | — | — | — | 4 | — | — |

Verbatim findings: "GIVA runs a promo code in a hundred and five of a hundred and fifty one creatives. Codes are not a campaign for them, they are the default. Rubans reaches for buy one get one in forty five of ninety seven and almost nothing else. Palmonas is the only brand running named sales at scale, thirty four of them, which is how you keep discounting without training the customer to wait for one number." "Tyaani and Voylla are empty rows across every instrument. Nothing here is a rounding error, it is a decision."

---

## 4. Price ladder

### 4.1 — Prices named in ad copy, with citation counts (Source: Six Ways to Sell Jewellery)

| Brand | Price points named in copy |
|---|---|
| Palmonas | ₹699 · ₹999 · ₹1,899 · ₹2,999 · ₹5,000 · ₹20,000 |
| GIVA | ₹999 · ₹3,499 |
| Rubans | ₹1,000 · ₹1,500 |
| CaratLane | no price in copy |
| Tyaani | under ₹1.5 lacs (ceiling only) |
| Voylla | no price in copy |

Counts stated in prose: "Palmonas anchors at ₹699 and names it twenty five times. GIVA anchors at ₹999, named thirty one times, with a second step at ₹3,499. That gap of three hundred rupees is the whole entry battle in this category." "Above it, Palmonas ladders alone: ₹5,000 for 24KT gold and ₹20,000 for lab grown diamonds." Tyaani's "under ₹1.5 lacs" is characterised as "a ceiling, jewellery under ₹1.5 lacs, which reads as permission rather than a deal," not a discount anchor.

### 4.2 — Price bands, India (Source: Naira Petite Dossier — broader "real price band" reads, not ad-copy citations)

| Brand | Price band |
|---|---|
| Palmonas | ₹999–3,000+ |
| GIVA | ₹599–6,000+ |
| Rubans | ₹500–4,000 (ASP ₹800) |
| Shaya (CaratLane) | ₹600–11,000 |
| Salty | ₹250–900 core |
| Pipa Bella | ₹300–1,200 effective |
| Melorra | ₹4,000–90,000 |
| Isharya | ₹2,500–8,000 |
| Blingvine | up to ₹5,800 |
| Outhouse | ₹10,000–35,000 |
| Misho | ₹9,000–20,000 |

Note the Palmonas discrepancy against §4.1 — see §9.

### 4.3 — Price bands, global (Source: Naira Petite Dossier, all figures USD unless noted)

| Brand | Price band |
|---|---|
| Mejuri | $80–450 (AOV $150–175) |
| Missoma | $50–250 |
| Astrid & Miyu | $65–900 |
| Ana Luisa | $39–150 |
| PDPAOLA | $85–390 (avg $150) |
| Monica Vinader | $120–400+ |
| Gorjana | $45–160 core |
| Aurate | $150–3,200 |
| Catbird | <$50 entry–$1,000s |
| VRAI | $395–24,500 |

### 4.4 — Swarovski's own retail ladder (Source: The Swarovski Benchmark, USD)

| Rung | Price |
|---|---|
| Entry | $69 |
| Core opens | $99 |
| Core closes | $269 |
| Top of jewellery | $520 |

Carried by 5 product families (Millenia, Matrix, Constella, Idyllia, Dextera/Una) — see §8.

### 4.5 — Naira's own recommended ladder (Source: Naira Petite Dossier §06, for reference — not a competitor number)

Studs/dainty rings ₹899–1,499 · Hoops/drops/statement rings ₹1,499–2,000 · Chains & cuffs ₹1,499–2,200 · Tennis & statement necklaces ₹2,000–2,900 · Sets ₹2,200–3,299. Blended AOV target ₹1,800–2,400 at ~51% contribution margin.

---

## 5. Routing/destination data

Source: Six Ways to Sell Jewellery. **The source states destination percentages for only 3 of the 6 brands** — GIVA, Tyaani and Voylla have no equivalent "where the click goes" figure anywhere in the document. This is a genuine gap in the source, not an extraction failure; it is not filled in below.

| Brand | Destination finding (verbatim) |
|---|---|
| Rubans | **92% collection.** "The most disciplined routing in the set. Almost nothing goes to a product page, so one creative stays alive across a whole catalogue." |
| Palmonas | **75% collection.** "Plus ten percent to bespoke campaign pages and a single ad into Swiggy Instamart." |
| CaratLane | **88% elsewhere** (store/location pages, not collections). "Barely uses collections at all. Traffic goes to store and location destinations, which is what an omnichannel account looks like in the data." |
| GIVA | Not stated. |
| Tyaani | Not a destination-mix figure, but a CTA-routing note appears in the brand teardown (§1.1): 7 of 35 ads route to WhatsApp, 3 to Instagram — the remaining 25 are unaccounted for in the source. |
| Voylla | Not a destination-mix figure; the teardown notes "See details rather than Shop now on half the set" — a CTA-button observation, not a landing-destination one. |

**Copy-length medians — stated for 2 of 6 brands only:** "CaratLane writes a median of 75 characters against Palmonas at 279. When the message is in the artwork and the store address, the caption has little left to do." No median is given for GIVA, Rubans, Tyaani or Voylla.

---

## 6. Verified benchmarks (hallmarked)

Only Document 2 (Palmona brief) uses a formal three-state verification system — **Verified** (traced to a primary source, independently re-checked) / **Weak** (real but limited — vendor data, small sample, adjacent category, or inference) / **Struck** (untraceable or contradicted; a falsehood in circulation). Documents 1, 3 and 4 make direct claims without this apparatus; where useful I've noted how each would sit against the same scale, marked **[unhallmarked]**.

**No CPM or CTR benchmark exists anywhere in this corpus.** The closest performance-lift figures are CVR/CPA (below) and the ROAS/CAC figures in the next table.

### 6.1 — Meta creative specification (Source: Palmona brief)

| Property | Value | Hallmark |
|---|---|---|
| Reels/Stories canvas | 1440 × 2560 | Verified |
| Safe zone — top | 14% | Verified |
| Safe zone — bottom | 35% | Verified |
| Safe zone — each side | 6% | Verified |
| **Bottom clearance when a disclaimer/T&Cs is present** | **40%**, not 35% | Verified — "appears in Meta's own help documentation and in none of the design blogs" |
| "250px top" / any pixel safe-zone figure | — | **Struck** — stale, from the retired 1080×1920 era, arithmetically wrong on the current canvas |
| "Bottom 20%" | — | **Struck** — stale; Stories now matches Reels at 35% |
| Facebook Marketplace text | 125 primary / 40 headline / 30 description | Verified |
| Instagram Feed text | 125 primary / 40 headline | Verified |
| Instagram Stories text | 125 primary | Verified |
| Facebook Feed text | 50–150 primary / 27 headline | Verified |
| **Instagram Reels text** | **44 characters primary** — the binding constraint used for every copy line in the brief | Verified |
| Instagram Reels max ad length | 15-minute container limit (published) | Verified |
| "90-second" Reels length figure | — | Unverified — "could not be verified, so treat anything beyond 90s as unproven and check in Ads Manager" |
| Google Performance Max — horizontal | 1200 × 628 · 1.91:1 | Verified |
| Google Performance Max — square | 1200 × 1200 · 1:1 | Verified |
| Google Performance Max — vertical | 960 × 1200 · 4:5 | Verified |
| Google content rule | key content inside the centre 80% | Verified |
| Pinterest Standard Pin | 1000 × 1500 · 2:3 | Verified |
| Pinterest Video Pin | 6–15s recommended | Verified |

### 6.2 — Discount-depth and offer-framing research (Source: Palmona brief)

| Finding | Detail | Hallmark |
|---|---|---|
| Discount depth vs. purchase intent | Vassilikopoulou & Kostopoulos (2026), *British Food Journal* 128(5) 1816–1833, DOI 10.1108/BFJ-07-2025-0945. 18-condition MANOVA design, 3 promotion types × 3 depths × 2 price tiers. "For expensive products, only a 20% discount raised purchase intention; 30% and 50% reduced it." High-intensity promotions "consistently lowered perceived quality, prestige and brand image." | Verified — but scope-limited: no no-promotion control group exists, so this shows 50% underperforms 20%, **not** that 50% underperforms running no promotion. Also: wine category, unknown sample size/country/price point. |
| "Rule of 100" (% below 100 units of currency, ₹/$ amount above) | Real underlying paper (Chen, Monroe & Lou 1998, *Journal of Retailing*) shows absolute framing feels larger on higher-priced goods, but never estimated a threshold — "100" is a later simplification, and "the behavioural literature explicitly names INR as a currency the rule does not transfer to." | Weak |
| Meta Ad Library live density | `jewellery 50% off sale` → 22,267 active ads in India (mostly non-jewellery). `demi-fine jewellery gift for her` → 228 active ads, heavy on Rakhi/festival framing and WhatsApp routing. Direct observation, retrieved 8 Aug 2026. | Verified |
| Self-purchase vs. gifting | CaratLane's "Wear Your Wins" won a Gold Effie (Effie India 2025) on **self-recognition, explicitly not gifting**. McKinsey/BoF *State of Fashion 2026*: 42% of women and 35% of men report buying more jewellery for themselves than 2–3 years ago. | Verified |
| Gift-framing A/B test | Thinkerbell test found no significant difference between gift-framed and self-purchase-framed copy. | Weak — n = 10 conversions |
| CTA pronoun test | Michael Aagaard: "Start *my* free trial" beat "Start *your* free trial" by +90% CTR. | Weak — 2012 SaaS trial button, not ecommerce or jewellery; borrow the mechanism (first person), not the number |

### 6.3 — Creative-craft findings (Source: Palmona brief) — CVR/CPA, not CTR/CPM

| Finding | Detail | Hallmark |
|---|---|---|
| Open-loop visual hooks | A visual that raises a question rather than answers it (e.g. a hand mid-motion toward a clasp) measured **2.4× higher 3-second retention** than a text-overlay hook. | Weak — VidMob, n=443 |
| Boosted organic vs. manufactured in-feed | CREA Jewelry: **+44% CVR, −26.4% CPA** running Spark Ads over standard in-feed creative. | Weak — platform-published, wins-only case |
| Size reference | 42% of shoppers try to judge size from the image alone; on-body framing (wrist/neck/hand) solves this. | Weak — Baymard, PDP research not ad units |
| Creative volume | Fashion advertisers under $10K/month test ~2.9 new creatives weekly; roughly 5% of tested creatives win. | Weak — Motion, n=550k ads |
| Jewellery attention research | None exists. No eye-tracking study, no controlled on-model vs. flat-lay vs. macro test was found. | No data (explicit gap, not a finding) |

### 6.4 — ROAS, CAC and unit-economics benchmarks (Source: Naira Petite Dossier) — **all unhallmarked in the source**, flagged inline as published/agency/estimate by the document itself

| Benchmark | Value | Source's own flag |
|---|---|---|
| Median Meta ecommerce ROAS | ~1.9× | [published] |
| Indian D2C top performers, blended ROAS | ~3.2× | [agency] |
| Fashion ROAS target | 2.5–4× | [agency] |
| Jewellery on Meta | 3–6× ROAS | [agency] |
| Jewellery on Google Shopping | 6–10× ROAS | [agency] |
| GIVA's own disclosed efficiency | "spends ₹1.15 to earn ₹1" | Company-disclosed (per dossier) |
| Melorra's disclosed efficiency (cautionary) | 33% of revenue on ads; "₹1.29 to earn ₹1" | Company-disclosed (per dossier) |
| CAC, fashion, Meta India | ₹320–550 | [agency] |
| India RTO rate, COD | ~26% | [published] |
| India RTO rate, prepaid | <5% | [published] |
| Imitation jewellery GST | 3% (HSN 7117) | [published] |
| Naira catalogue market-pull average | 7.4/10 across 63 finalised styles, 30 styles scoring 8–9 | Editorial judgement, not a sales forecast (source's own caveat) |
| Naira modelled contribution margin at the recommended ladder | ~51% | Modelled |
| Naira modelled break-even ROAS | ~2.0× | Modelled |
| Creative fatigue's share of budget leakage (jewellery ads) | ~73% | [agency] — cited once, no further sourcing given |

Explicit source caveat, verbatim: "No demi-fine brand publishes ROAS, CAC or AOV — every such figure here is either a category benchmark (flagged agency/estimate) or a modelled output, not a competitor's actual return."

### 6.5 — India dark-patterns law (Source: Palmona brief)

- Governing text: **Guidelines for Prevention and Regulation of Dark Patterns, 2023**, notified 30 November 2023, File No. CCPA-1/1/2023-CCPA (Reg), Annexure 1, item 1. **Verified** count: 13 dark patterns in the notified version — not the 10 in a since-withdrawn September 2023 draft that "including in several law-firm summaries" is still being circulated as the operative text. The draft's wording **omits the two sub-limbs advertisers actually breach.**
- Full notified text of "false urgency," verbatim: *"Falsely stating or implying the sense of urgency or scarcity so as to mislead a user into making an immediate purchase or taking an immediate action, which may lead to a purchase, including — (i) showing false popularity of a product or service to manipulate user decision; (ii) stating that quantities of a particular product or service are more limited than they actually are."*
- Permitted: real stock counts, real countdowns to genuine end-times, real festival windows.
- Prohibited: invented "only 3 left," fabricated "27 people are viewing this," "offer ends soon" with no real end date.
- Also relevant: **drip pricing** (all charges visible up front; genuine gold-rate movement between browsing and checkout is exempt, hidden making charges is not) and **disguised advertisement** (influencer/UGC creative must be disclosed as paid).
- **Caveat on all of the above, verbatim:** "The notified wording above rests on three concordant secondary reproductions. The Gazette itself could not be opened during this research — the government hosts returned errors. Have Indian counsel confirm the text against the Gazette before relying on it."

Enforcement to date (reported to the Rajya Sabha, early Aug 2026):

| Platform | Penalty | Pattern cited |
|---|---|---|
| Zepto | ₹7 lakh | Drip pricing and basket sneaking |
| PhysicsWallah | ₹5 lakh | Basket sneaking, confirm shaming, forced action |
| Anuj Jindal | ₹3 lakh | Manipulative subscription renewal |
| FirstCry | ₹2 lakh | Hidden charges |
| PharmaEasy · McAfee · SpiceJet | ₹1 lakh each | Forced subscription; confirm shaming; deceptive practices |
| IndiGo · BookMyShow | No fine disclosed | Confirm shaming; basket sneaking |

Totals as stated: **seven platforms fined, ₹20 lakh in total; nine acted against.** No jewellery or fashion brand appears yet — "which means no test case has surfaced, not that the category is exempt."

---

## 7. The struck list

Every claim identified across the corpus as fabricated, untraceable, or actively contradicted. All of it comes from Document 2 (Palmona brief), the only document that runs adversarial verification; the other three documents make no equivalent falsifiable claims of this kind, so they contribute nothing to this list — not because they are cleaner, but because they don't cite the kind of secondary statistic Document 2 was checking.

| Claim in circulation | What is actually true |
|---|---|
| Pandora "Be Love" starred Millie Bobby Brown and Sydney Sweeney, drove 2.5B impressions, won a Cannes Lion | Ambassadors were Pamela Anderson, Chloe x Halle Bailey, Winona Ryder and Iman. Brown fronted "Pandora Me" in 2019, a different campaign. No such Cannes win found. |
| "Harvard Business Review: frequent discounts cut brand value by up to 33%" | No such HBR study exists. The nearest real article (Lodish & Mela, 2007) makes the qualitative point and contains no such figure. |
| "Find Her Perfect Gift" beat "Shop Gifts for Her" in 78% of tests, +23% CTR | Absent from both pages cited as its source. No brand, no dataset, no methodology anywhere. |
| "A 2020 Facebook study found Shop Now lifts conversion 2.5×" | Untraceable to any Meta publication. Every hit is a blog repeating it without a link. |
| "Discount-acquired first buyers are 50% less likely to return" | A 2014 press release from a personalisation vendor selling the opposite behaviour. Correlational, confounded by obvious selection effects. |
| BlueStone campaign drove "930% lift in watch searches" | Absent from all seven primary trade articles covering that campaign. |
| Statistics from "Meta's 2025 Creative Best Practices report" | No such report exists. |
| "250px top" / any pixel-based Reels/Stories safe-zone figure | Stale — from the retired 1080×1920 canvas era; arithmetically wrong on the current 1440×2560 canvas. |
| "Bottom 20%" Reels/Stories safe zone | Stale — Stories now matches Reels at 35% (40% with a disclaimer present). |

**Do not re-introduce any of the above from a competitor deck, a blog, or a law-firm summary** — that is verbatim how Document 2 frames this table's purpose.

---

## 8. Swarovski craft/supply-side findings (Source: The Swarovski Benchmark)

### 8.1 — What earns the 8–9 score, verbatim

*"It is not the crystal. It is the setting discipline, the cut vocabulary and the fact that five families each own a clear job. That is the thing to match, and it is reproducible in brass and silver at a fraction of the cost."*

### 8.2 — The five families and their job

| Family | Cut/setting vocabulary | Role |
|---|---|---|
| Millenia | Octagon and emerald cuts in double-prong fine-jewellery settings; tennis necklaces in purple and clear | "The most grown up thing they make" |
| Matrix | Round brilliant pavé, baguette (Vittore ring), tennis bracelets, Y necklaces, crystal pearl paired with pavé on studs | Core bench |
| Constella | Round-cut pavé halo studs and drops, sold as necklace/bracelet/stud set | "The gifting engine" |
| Idyllia | Nature motifs — pavé butterfly, mixed-cut flower, ladybird and clover, heart-lock-and-key charms, mostly multicoloured on gold tone | Nature/charm line |
| Dextera and Una | Hoops, chunky links, collar necklaces, angelic tennis | "The everyday bench that carries repeat purchase" |

What fails the framework entirely (scored 1–3, explicitly excluded): figurines, Disney/Marvel/Star Wars licences, zodiac pieces, the Kris Bear line.

### 8.3 — Capability matrix: which supplier can hold which family

"Filled [strong] is a family they already make well. Half [partial] is partial, meaning they have the technique but not the range. Empty [none] is absent from the catalogue." Extracted from the underlying `aria-label` fill states (not visible as rendered text on the page):

| Maker | Millenia (octagon, baguette) | Matrix (round pavé, tennis) | Constella (halo, solitaire) | Idyllia (nature, enamel, pearl) | Dextera (hoops, huggies) | Score |
|---|---|---|---|---|---|---|
| Arts Jewellery Co. | strong | partial | strong | partial | strong | 9 |
| Peishang Jewelry Co. | partial | strong | strong | partial | strong | 8 |
| CT Color Co. | partial | partial | partial | strong | partial | 8 |
| Panyu Longlong Jewelry Factory | none | partial | strong | partial | none | 7 |
| Yu Jing Jewelry Co. | strong | partial | strong | none | none | 7 |
| Kirin Jewelry Co. | strong | strong | strong | partial | none | 6 |

### 8.4 — The shortlist, in full (each rated on the maker's own product photography, not listing titles — "titles on these platforms are keyword stuffed and routinely describe a piece that is not in the picture")

| Score | Maker | Founded / staff / floor | Lead time | Terms | Read | Flag |
|---|---|---|---|---|---|---|
| 9/10 | Guangzhou Arts Jewellery Co., Ltd (artsjewellery.en.made-in-china.com) | 2010 · 20 staff · 815 m² · Guangzhou | 1 month | LC, T/T, D/P, PayPal | "The only house in the set that keeps a real catalogue discipline." Every piece carries a model code and stated gram weight. Vintage textured halo pendants (blue/pink/green/ruby) sit "almost line for line with Constella and Stilla." Brushed gold "reads festive in India in a way Swarovski's rhodium never will." Pieces marked "2026 New." | Twenty staff on 815 m² — confirm capacity before a first buy of any size. |
| 8/10 | Guangzhou Peishang Jewelry Co., Ltd (gzpeishang.en.made-in-china.com) | 2017 · 160 staff · 1,620 m² · Guangzhou | 15 days–1 month | T/T, PayPal | "The capacity pick." 925 silver under 14K/18K plate over moissanite and CZ. Carries the four-leaf clover motif — "the single hottest motif in the Indian demi-fine band right now" — plus the deepest hoop/huggie bench of anyone in the set. Certifications: BSCI, CE, SGS, RoHS; nickel/lead-free; OEM/ODM with free logo. | Hip-hop and iced-out lines sit in the same catalogue as the fine work — curate the buy, don't take the range whole. |
| 8/10 | CT Color Co., Limited (ctcolorjewelry.en.made-in-china.com) | Materials: 925 silver, brass. Speciality: carved shell, enamel. Stones: semi-precious, zircon | — | T/T, PayPal, Western Union | "The answer to Idyllia." Carved shell/mother-of-pearl flowers, enamel leaves, coloured zircon clusters in silver — "the craft is finer than Swarovski's own nature family." Pillow-cut baguette-halo pearl studs and pink-baguette-on-black-enamel drops are "proper deco pieces." | Company facts are thin on their profile — no staff count, no plant area disclosed. Verify before committing. |
| 7/10 | Guangzhou Panyu Longlong Jewelry Factory (longlong-jewelry.en.made-in-china.com) | 2009 · Panyu, Guangzhou | 15 workdays | T/T, PayPal, Western Union | "Panyu is the jewellery district and this is a proper 925 house inside it, trading since 2009." Two clover-stud variants, a coloured halo bench (tanzanite cushion, emerald heart, blue topaz); "the emerald and green pieces carry real festive pull in India." | Snowflake, starfish, dolphin and kitty studs sit in the same range — all four are hard exclusions on the framework. Curation is mandatory. |
| 7/10 | Yu Jing Jewelry Co., Ltd (yujingjewel.en.made-in-china.com) | 2014 · 49 staff · 949 m² · brand "Feiffer" | 15 workdays | T/T, PayPal | "The elevated specialist." Moissanite and natural gemstone set in 925; the baguette half-eternity band is "Matrix Vittore almost exactly." Most finished photography of anyone in the set. Natural garnet prong work is "genuine fine jewellery craft rather than fashion assembly." | Narrow — bridal and birthstone only, no hoops/huggies/fashion motifs. Take as a second supplier for the top of the range. |
| 6/10 | Zhuhai Kirin Jewelry Co., Ltd (kirinjewelry.en.made-in-china.com) | 2006 · 206 staff · 4,500 m² · ISO 9001:2015 certified | 15 workdays | LC, T/T, D/P | Largest house in the set, only one with a certified management system. Best stone-setting of anyone: micro pavé, baguette channel, marquise cluster work, with model code/stone count/finished weight printed on every shot. Problem is house taste — "chandelier tassels, peacock wing drops and pageant cocktail clusters read a generation behind Swarovski's current line." | The score reflects the catalogue, not the capability. Treat as a make-to-spec partner; send Naira tech packs rather than buying the range. |

### 8.5 — Five houses reviewed and rejected (recorded so the same ground is not walked twice)

| Maker | Why rejected |
|---|---|
| Joacii Jewelry | Beaded and natural-stone chains, no set stones anywhere — beautiful work, wrong construction category. |
| Ason Jewelry | Stainless steel under PVD plate; minimal stone work, kids/novelty bench underneath. |
| Shenzhen Right Grand | Implant-grade titanium body piercing; also carries SKUs described as "a brand safety problem next to a Naira storefront." |
| Goodliness Jewellery | Broad but incoherent — panda earrings and tarot charms beside men's hip-hop. |
| Starsgem, Messi Gems | Loose-stone houses — "they sell the CZ, they do not finish the jewellery." |

### 8.6 — Recommended next actions (verbatim from the source's own "Actions" section)

1. **Sample Arts and Peishang together** — "they are the two halves of one range." Arts brings the halo pendants and deco drops; Peishang brings the clover, hoops and huggies. Ask both for the same six pieces so plating thickness and stone seating can be compared on one table.
2. **Ask every house for plating spec in writing** — microns of gold, base metal, PVD vs. electroplate. "This is where demi-fine either survives an Indian summer or does not, and none of the listings state it."
3. **Put a Naira tech pack in front of Kirin** — "they have the setting bench, the ISO certificate and 206 staff. They do not have the taste. That combination is exactly what a make-to-spec partner is for."
4. **Treat CT Color as the enamel-and-shell line**, kept separate from the pavé range rather than blended into one confused edit.
5. **Confirm MOQ and unit price before any of the above** — "none of the public listings carry reliable pricing. Everything here is a design and capability read, not a commercial one."

### 8.7 — Method, and an internal number to flag

Swarovski's own site refuses datacentre traffic, so the 101-piece assortment was read from live US retail listings instead. Supplier discovery ran "22 keyword searches" across Made in China, from which "21 storefronts were harvested at 192 products each," and 6 makers went through to full visual review. **Note the internal inconsistency:** the page's own header stat reads "22 supplier catalogues skimmed," while the Method paragraph distinguishes 22 *searches* from 21 *storefronts harvested* — these are two different counts in the same document (plausibly 22 searches deduplicating to 21 unique storefronts), reproduced here exactly as stated rather than reconciled. Scores are "commercial market pull in the Indian demi-fine band, one to ten, on the Naira framework. Brand fit is carried as a flag and never deducted from the number."

---

## 9. Cross-document contradictions

### 9.1 — "Palmona" (Document 2) vs. "Palmonas" (Documents 1 and 3) — naming ambiguity, flagged not resolved

Document 2 consistently writes **"Palmona"** (no terminal s) throughout — "What to put in a Palmona ad," "Palmona's price band and range" (listed as an unresolved open question at the end of that document). It never states a revenue figure, a founder, a follower count, or a funding event for this brand.

Documents 1 and 3 consistently write **"Palmonas"** (with a terminal s) and both independently supply the same identifiable, funded company: 1.03M Instagram followers and 150 live Meta creatives (Doc 1); ₹39 Cr FY25 revenue, ~40× YoY, profitable ₹4.3 Cr, Shraddha Kapoor as co-founder, a Shark Tank appearance (Doc 3).

**This file does not merge them.** If "Palmona" in Document 2 is simply a dropped-letter version of "Palmonas," then Document 2's own "open question" about its subject's price band is answered by §4.1/§4.2 above (₹699–₹20,000 named in copy; ₹999–3,000+ as a broader band). If they are two different brands — plausible, since Document 2 never cites a single one of the identifying facts Documents 1/3 attach to Palmonas — then Document 2's specification and compliance findings (§6.1, §6.5) still apply generically to any Indian jewellery advertiser, but its Decision 01/02 recommendations should not be read as being *about* the Palmonas profiled elsewhere in this corpus. **[This distinction is flagged, not INFERRED as fact — no document states outright that these are, or are not, the same brand.]**

### 9.2 — Palmonas's entry price: ₹699 (Doc 1) vs. a stated floor of ₹999 (Doc 3)

- **Document 1** (Six Ways, live Meta Ad Library pull, 19 Aug 2026): "Palmonas anchors at ₹699 and names it twenty five times" in live ad copy.
- **Document 3** (Naira Dossier, July 2026, brand-site/catalogue-based): states Palmonas's price band as **₹999–3,000+** — a floor ₹300 above the price Document 1 shows being named twenty-five times in live ads that same month.

**Better sourced:** Document 1, for the specific claim of *what price Palmonas states in live ad copy* — it is a direct, dated, countable observation (25 citations) from the primary ad-library source, one month more recent than Document 3. Document 3's figure more plausibly describes the core catalogue/on-site range rather than promotional entry pricing, but as stated, the two documents give incompatible floors for the same brand. Do not use ₹999 as "the cheapest thing Palmonas advertises" — the evidence says ₹699.

### 9.3 — "CaratLane" is two different scopes across two documents

- **Document 1** profiles the parent CaratLane account directly (3.9M followers, "A Tata product") — diamond-heavy (71% of copy), store-launch-led, Flat-30%-on-making-charges as its sole discount mechanic, brand-film and in-store-education content (Kashika, Know Your Diamond). No mention of silver, no mention of "Flawsome."
- **Document 3**'s players table lists this competitor explicitly as **"Shaya (CaratLane)"** — a 925-sterling-silver-only line, price band ₹600–11,000, hook "Not Perfect But One Of A Kind (#Flawsome)," positioned as being "In Titan/Tanishq."

These are stated by Document 3 itself to be a named sub-brand (Shaya), not the parent account Document 1 tracked. **Do not treat the two "CaratLane" rows in this corpus as the same dataset** — Shaya's silver/Flawsome positioning does not appear anywhere in Document 1's 53-creative CaratLane teardown, and Document 1's diamond/store-launch positioning does not appear anywhere in Document 3's Shaya entry. Both are accurately reported; they are simply not describing the same storefront.

### 9.4 — Discount depth vs. live discount-mechanic performance — a tension, not a hard contradiction [this connection is this file's own synthesis, marked INFERRED]

Document 2 argues, from an 18-condition wine-purchase-intent study and Meta auction density, against leading with deep percentage discounts (§6.2). Document 1's live data shows something more specific: GIVA — the heaviest user of percent-off/promo-code mechanics (80% of copy carries an offer, code in 105/151 creatives) — has the **second-worst** median impression rank (621) of the six brands. But Rubans — which discounts almost as often (62% of copy) via **BOGO** rather than percent-off — has the **third-best** median rank (110). Neither document makes this comparison itself; Document 2 never discusses BOGO as a mechanic, and Document 1 never discusses purchase intent or brand perception. Read together, they suggest the *mechanic* (BOGO vs. percent-off-and-codes) may matter as much as the *depth* Document 2 investigated — a hypothesis this corpus surfaces but that neither source document tests directly.

### 9.5 — Where the documents agree (not a contradiction, noted for completeness)

Document 1's closing section explicitly cross-references Document 4: *"That is the gap, and it is the same gap the Swarovski benchmark work identified from the supply side: the setting discipline and cut vocabulary that separate a good piece from a cheap one are reproducible at Naira's price, and nobody is telling that story to the customer."* This is the one place in the corpus where two documents were written with direct awareness of each other, and they corroborate rather than conflict.

---

## Appendix — brand coverage map across documents

| Brand | Doc 1 (ad performance) | Doc 2 (creative/legal spec) | Doc 3 (positioning/financials) | Doc 4 (supply-side) |
|---|---|---|---|---|
| Palmonas / "Palmona" | Yes (full metrics) | Subject of the entire brief, under the spelling "Palmona" — see §9.1 | Yes | No |
| GIVA | Yes (full metrics) | No | Yes | No |
| Rubans | Yes (full metrics) | No | Yes | No |
| CaratLane / Shaya | Yes (full metrics, parent account) | No | Yes, as "Shaya (CaratLane)" — see §9.3 | No |
| Tyaani Jewellery | Yes (full metrics) | No | No | No |
| Voylla | Yes (full metrics) | No | No | No |
| Swarovski | No | No | No | Yes (entire document) |
| Salty, Pipa Bella, Melorra, Isharya, Blingvine, Outhouse, Misho | No | No | Yes | No |
| Mejuri, Missoma, Astrid & Miyu, Ana Luisa, PDPAOLA, Monica Vinader, Gorjana, Aurate, Catbird, VRAI | No | No | Yes | No |
| Rare Ever, Zitara, Priskel, Manira Luxe, Sefira, Aadhyaatmik, Golden Shells, Thakurani, Axesouár, Kendra Scott, Sami Jewels, Ania Haie, Reclaimed With Love, Tiraaya | No | No | Hook-wall only (§1.4) | No |

**Method notes carried over from each source, verbatim where useful:**
- Doc 1: "Pulled from the Motion swipe file on 19 August 2026: every active creative for six brands, deduplicated to 498 unique records." Supersedes an earlier Palmonas-only version and corrects two prior claims (Palmonas's true best rank is 19, not worse than GIVA's 122 as a 30-day window had suggested; not every brand uses "Shop now" — Tyaani routes to WhatsApp/Instagram, Voylla mostly uses "See details").
- Doc 2: "3 research passes, 2 adversarial verification passes," compiled 8 Aug 2026, India market, Meta/Google/Pinterest.
- Doc 3: Player intel from brand sites, live catalogues, Inc42/Entrackr/YourStory/Tracxn, Modern Retail, Glossy, WWD, Forbes, Companies House filings; ad hooks from the Meta Ad Library (IN/US), July 2026; ROAS/CAC/pricing benchmarks from Triple Whale and agency/vendor data (explicitly flagged directional); FX ₹86/USD, landing factor ×1.55.
- Doc 4: 101 Swarovski pieces read from live US retail listings; 22 supplier keyword searches; 21 storefronts harvested at 192 products each; 6 taken to full visual review; scores are "commercial market pull... one to ten, on the Naira framework," brand fit carried as a flag and never deducted from the score.
