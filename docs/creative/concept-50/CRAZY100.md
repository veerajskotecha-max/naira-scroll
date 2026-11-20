# Crazy 100: production plan (10 crazy camps × 10 ads, slow-stock list)

Naira Petite (nairaflore.com) · plan written 20 Nov 2026 · production started 20 Nov (batches k01a and k02a first) · machine-readable twin: `crazy100.json` · supersedes `PLAN.md` · owner rulings: `RULINGS.md`

One hundred ads: ten camps, ten ads each, produced in 20 batches of 5, every one built for a slow-stock piece. Each camp is its own world with its own graphic device; every ad carries a motivation angle and a funnel layer, so the best of them drop straight into a layered ₹5,000-a-day campaign. The ten bibles in `crazy100.json` (`camps`) are the production authority: prompts, layouts, copy, motion and risks are there in full and are used exactly as written. Nothing is uploaded to Meta without the owner's go-ahead.

## 1. The owner's brief

> "Be creative, go all out to make these ads and make something conceptual in batches of 5. Naira branding features, textual award-winning graphics. Winning hooks. ... all conceptual, crazy and different! Some maybe animated like the dhol tasha on bracelet we did? Think 10 crazy ad concepts that should work!"
>
> "Think what will make this work and crazy"
>
> "we need ROAS 5"
>
> "We don't want all red-teamed! I said crazy camps, all different, all innovative and 10/10"
>
> "Keep going till you make the finest ads"
>
> "Focus only on these products for the 100 ads"

Scope: the slow-stock list: pieces with no sale in 28 days or more than 16 weeks of stock; this is cash tied up that the ads must move.

## 2. The products: the slow-stock list (37 pieces)

Prices and stock as read for the product cards (`products/<handle>.json`, listing photos in `refs/<handle>/`). 13 pieces are tagged pre-order: they carry no claims, no water and no dispatch promise. Pieces under 20 units run because the owner put the whole slow list in the run (RULINGS §2); stock is re-read at render and an ad pauses if its variant sells out.

| # | Piece | Handle | Price | Stock | Pre-order | Claims the ads may make | Ads |
|---|---|---|---|---|---|---|---|
| 1 | Woven Gold Hoops | `woven-gold-hoops` | ₹1,049 | 88 | no | Waterproof, tarnish free, hypoallergenic | 9 |
| 2 | Toggle Link Chain | `toggle-link-chain` | ₹999 | 77 | no | Tarnish free, hypoallergenic; no waterproof claim, no water | 9 |
| 3 | Verdant Eternity Band | `verdant-eternity-band` | ₹1,049 | 58 | no | Waterproof, tarnish free, hypoallergenic; adjusts US 5 to 9 | 7 |
| 4 | Brushed Gold Huggies | `brushed-gold-huggies` | ₹699 | 58 | no | Waterproof, tarnish free, hypoallergenic | 6 |
| 5 | Triple Coil Wrap Bangle | `triple-coil-wrap-bangle` | ₹1,149 | 39 | no | Waterproof, tarnish free, hypoallergenic | 4 |
| 6 | Halo Curve Ring | `halo-curve-ring` | ₹899 | 27 | no | Waterproof, tarnish free, hypoallergenic; adjusts US 5 to 9 | 3 |
| 7 | Bold Nocturne Bracelet | `bold-nocturne-bracelet` | ₹1,599 | 19 | no | Waterproof, tarnish free, hypoallergenic | 2 |
| 8 | Prism Cluster Studs | `prism-cluster-studs-silver` | ₹1,299 | 26 | yes | None | 3 |
| 9 | Verdant Cushion Studs | `verdant-cushion-studs` | ₹1,099 | 30 | yes | None | 3 |
| 10 | Verdant Circlet Studs | `verdant-circlet-studs` | ₹899 | 32 | no | Waterproof, tarnish free, hypoallergenic | 3 |
| 11 | Charm Box Chain | `charm-box-chain` | ₹1,199 | 18 | no | Waterproof, tarnish free, hypoallergenic (never 'never tarnishes') | 2 |
| 12 | Aqua Heart Drops | `aqua-heart-drops-silver` | ₹1,299 | 24 | yes | None | 2 |
| 13 | Baroque Shell Bracelet | `baroque-shell-bracelet` | ₹1,899 | 18 | no | Tarnish free, hypoallergenic; not waterproof, no water | 2 |
| 14 | Rivière Hoops — Silver | `riviere-huggies-silver` | ₹1,499 | 19 | yes | None | 2 |
| 15 | Serpentine Whisper Chain — Silver | `serpentine-whisper-chain-silver` | ₹899 | 23 | no | Waterproof, tarnish free, hypoallergenic; water allowed | 2 |
| 16 | Molten Panel Bangle | `molten-panel-bracelet` | ₹999 | 29 | yes | None | 3 |
| 17 | Baguette Halo Drops | `baguette-halo-drops` | ₹1,199 | 24 | yes | None ('PVD 18K gold coating' as a material fact only) | 2 |
| 18 | Serpentine Whisper Chain (gold tone) | `serpentine-whisper-chain` | ₹1,299 | 20 | no | Waterproof, tarnish free, hypoallergenic; never 'lasts forever' | 2 |
| 19 | Torsade Pearl Cuff | `torsade-pearl-cuff` | ₹1,099 | 23 | yes | None | 2 |
| 20 | Quatrefoil Éclat Studs | `quatrefoil-eclat-studs` | ₹1,099 | 23 | yes | None | 2 |
| 21 | Lilac Papillon Ring | `lilac-papillon-ring` | ₹1,199 | 20 | yes | None | 2 |
| 22 | Marquise Drop Choker | `marquise-drop-choker` | ₹999 | 24 | no | Waterproof, tarnish free, hypoallergenic (gold variant shown) | 2 |
| 23 | Torsade Huggies | `torsade-huggies` | ₹999 | 25 | yes | None | 3 |
| 24 | Monochrome Enamel Hoops | `monochrome-enamel-hoops` | ₹999 | 24 | no | None (no water) | 2 |
| 25 | Droplet Open Cuff | `droplet-open-cuff` | ₹1,199 | 14 | no | Waterproof, tarnish free, hypoallergenic | 1 |
| 26 | Bold Dome Huggies | `bold-dome-huggies` | ₹999 | 23 | yes | None | 2 |
| 27 | Droplet Open Ring | `droplet-open-ring` | ₹899 | 20 | no | Waterproof, tarnish free, hypoallergenic | 2 |
| 28 | Heartbead Bracelet | `heartbead-bracelet` | ₹999 | 11 | no | Waterproof, tarnish free, hypoallergenic | 1 |
| 29 | Ribbon Bead Bracelet | `ribbon-bead-bracelet` | ₹699 | 21 | no | Waterproof, tarnish free, hypoallergenic | 2 |
| 30 | Duo Link Necklace | `duo-link-necklace` | ₹1,099 | 17 | no | Waterproof, tarnish free; 'hypoallergenic surgical stainless steel' | 2 |
| 31 | Petite Square Huggies | `petite-square-huggies` | ₹899 | 20 | yes | None | 2 |
| 32 | Bougainvillea Vine Bracelet | `bougainvillea-vine-bracelet` | ₹799 | 11 | no | None; keep dry, no water ('PVD rhodium coating, anti-tarnish' as a material fact only) | 1 |
| 33 | Tubogas Dome Ring | `tubogas-dome-ring` | ₹999 | 16 | no | Waterproof, tarnish free, hypoallergenic | 2 |
| 34 | Petite Bow Studs | `petite-bow-studs` | ₹999 | 16 | yes | None | 2 |
| 35 | Mint Pear Drop Earrings | `mint-pear-drop-earrings` | ₹1,049 | 17 | no | Waterproof, tarnish free, hypoallergenic | 2 |
| 36 | Marquise Coil Cuff | `marquise-wheat-cuff` | ₹1,549 | 10 | no | Waterproof, tarnish free; 'hypoallergenic surgical stainless steel' | 1 |
| 37 | Baroque Bloom Cuff | `baroque-bloom-cuff` | ₹1,399 | 10 | no | Waterproof, tarnish free, hypoallergenic | 1 |

Reference 1 for every picture is the listing photo named first in the card's `refs`; reference 2 is the second. Media ids are in `crazy100.json` (`products`).

## 3. What changed from the tamed PLAN.md

PLAN.md (10 camps × 5 ads) was red-teamed into product macros on plain grounds with a clever headline. The owner rejected it as too safe ("We don't want all red-teamed! I said crazy camps, all different, all innovative and 10/10") and moved the run to the slow-stock list. What is different now:

- **No red team.** Nobody votes boldness down. The only checks are hard-rule truth checks (RULINGS §1): the real piece built from its listing photo as reference 1 with the construction exactly right; one product per generated picture; no eyes, eyebrows or faces (hands, napes, ears from behind, wrists and collarbones only); no text, letters or logos generated inside a picture (every word is HTML); banned words never used (diamond, real or solid gold, gold or silver alone as the metal, emerald or ruby as nouns, huggie in copy); claims only where the product's tags allow; no water near a piece without a waterproof claim; live prices and real offer codes; no free shipping, compare-at or struck prices; no imitation of a real brand, person, publication or app.
- **Scale play and surreal worlds are allowed when the type owns the joke.** A piece may sit in a painted city, cast an impossible shadow or fill a 2× lens, as long as the real size is printed (and 'SHOWN MAGNIFIED' wherever a plate runs at 19 or more Feed px per listed mm). Milk paraats, power cuts, VHS effects, Devanagari matras, miniature paintings and shadow figures are all in.
- **Slow-stock list only.** 37 pieces with no sale in 28 days or more than 16 weeks of stock; the allocation gives the deepest stock the most ads (Woven 9, Toggle 9, Verdant Eternity 7, Brushed 6).
- **100 ads, not 50: ten ads per camp, 20 batches of 5.** Each camp has to stretch across ten different pieces without repeating its picture.
- **Every ad has an angle and a layer** (PAIN, OUTCOME, OBJECTION or OFFER; EDUCATION, TRUST or SELL), so the winners slot into the layered campaign (RULINGS §4).
- **Past camps are references, not templates** (RULINGS §3): the teams mined the 200-ad winners board, the PLAYBOOK, our own past camps and the owner's favourites for thinking, never for artwork.
- **Much more motion.** 37 of the 100 are planned as Reels (30 through Kling 3.0, 7 in HTML only), against one or two clips per camp before; the piece never moves.
- **Kept from PLAN.md:** the F2 card on every ad, cards 5 and 10 of every camp as OFFER cards on BUY3 (BUY4 where a camp earns it), every primary text carrying the BUY3 line, one big real named and priced piece per card, and the batch loop.

## 4. The jury and how the ten were picked

Eight creative teams (one per lens: metaphor, surreal, type, ritual, culture, everyday, story, art) each wrote five fully planned camps: 40 concepts. Seven judges scored every concept 1-10 on seven measures: two award jurors (a Cannes Lions Print & Outdoor and Film Craft juror; a D&AD typography and art-direction juror), the performance creative strategist who has to make the account sell, and four customer personas (Meera, the family gift buyer with three weddings this December; Ananya, minimal taste, office Secret Santa, allergic to discount posters; Sunita, mother of the groom, wary that online jewellery looks cheap; Rohan, a student buying for his maa, didi and girlfriend). The measures: **crazy** (never seen, talked about), **stop** (stops the thumb at 200 px), **sell** (makes her buy, ideally three), **brand** (feels like Naira), **make** (can be made truthfully with the real piece as the hero), **stretch** (carries ten ads without repeating), **ten** (a 10/10 campaign overall). Boredom was the worst sin; confusing or product-invisible the second.

| Rank | Concept | Overall | Crazy | Stop | Sell | Brand | Make | Stretch | Ten | Used in |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **story-3 AUNTY NE CHASHMA LAGAYA.** | 7.92 | 7.71 | 7.86 | 7.71 | 8.43 | 6.71 | 8.29 | 8.57 | k01 lead |
| 2 | **story-1 MUJHE KUCH NAHI CHAHIYE.** | 7.84 | 6.29 | 7.71 | 8.71 | 9.29 | 7.43 | 7.57 | 8.29 | k04 lead |
| 3 | **metaphor-3 SHAADI KA VIDEO. (the 90s wedding-video effects, made solid)** | 7.81 | 8.43 | 8.29 | 6.71 | 7.43 | 7.71 | 7.71 | 8.29 | k02 lead |
| 4 | **metaphor-1 PARCHHAI. (the shadow says what the gift means)** | 7.71 | 7.57 | 8.00 | 7.29 | 8.43 | 6.29 | 8.57 | 7.86 | k05 lead |
| 5 | **ritual-5 BEST OF THREE (the ring game)** | 7.67 | 7.14 | 8.14 | 8.43 | 8.14 | 5.71 | 6.43 | 7.57 | k03 lead |
| 6 | **story-2 UDHAAR KHATA.** | 7.65 | 7.14 | 7.14 | 8.14 | 8.14 | 7.00 | 8.14 | 8.00 | k06 lead |
| 7 | ritual-1 NAZAR UTAARO (seven turns of light) | 7.40 | 7.57 | 8.57 | 6.43 | 8.00 | 7.57 | 6.14 | 7.29 |  |
| 8 | story-4 FULL HOUSE. | 7.37 | 6.14 | 6.71 | 9.00 | 7.14 | 7.71 | 8.57 | 7.14 | k01 graft |
| 9 | **surreal-3 BIJLI GAYI.** | 7.29 | 7.86 | 8.14 | 6.43 | 7.71 | 6.00 | 6.29 | 7.29 | k07 lead |
| 10 | story-5 PLASTIC MAT UTAARNA. | 7.22 | 6.86 | 7.43 | 7.14 | 7.43 | 7.57 | 7.86 | 7.14 | k04 graft |
| 11 | surreal-1 COW FOR SCALE. | 7.03 | 7.57 | 9.00 | 5.29 | 7.00 | 4.86 | 8.00 | 6.86 | k03 graft |
| 12 | type-2 DO MATLAB (two meanings) | 7.00 | 5.86 | 6.71 | 7.57 | 8.29 | 7.71 | 7.71 | 6.86 | k07 graft, k08 graft |
| 13 | **type-1 EK MATRA KI KAMI (one mark short)** | 6.95 | 7.71 | 6.14 | 6.14 | 8.71 | 7.00 | 6.43 | 7.00 | k08 lead |
| 14 | everyday-1 RISHTA AAYA HAI. | 6.89 | 6.00 | 7.29 | 6.86 | 7.57 | 7.71 | 8.14 | 6.57 | k06 graft |
| 15 | **culture-5 AAJ KA BHAAV** | 6.88 | 5.86 | 7.14 | 7.57 | 6.43 | 8.14 | 7.43 | 6.71 | k09 lead |
| 16 | metaphor-4 ROLL A THREE. (every piece is a move) | 6.82 | 5.57 | 7.14 | 8.00 | 6.43 | 8.00 | 7.57 | 6.14 |  |
| 17 | art-4 THE WALL DANCES | 6.81 | 6.00 | 7.43 | 6.14 | 8.00 | 7.29 | 8.14 | 6.86 | k10 graft |
| 18 | **art-5 PAINTED BIGGEST** | 6.81 | 6.86 | 6.86 | 5.86 | 8.57 | 5.86 | 7.86 | 6.86 | k10 lead |
| 19 | metaphor-2 MEHENDI, FINISHED. (she drew the vine; we set the leaves) | 6.69 | 5.86 | 6.43 | 7.14 | 8.43 | 5.71 | 7.43 | 6.43 |  |
| 20 | art-1 SAFETY SPARKS | 6.63 | 5.00 | 7.29 | 7.00 | 7.57 | 8.00 | 7.57 | 6.29 |  |
| 21 | surreal-5 SANGEET INSIDE. | 6.56 | 5.86 | 6.86 | 6.71 | 8.00 | 6.00 | 6.14 | 6.43 |  |
| 22 | art-3 FOUR SHOWS DAILY | 6.52 | 5.14 | 8.00 | 7.29 | 6.00 | 6.00 | 7.43 | 5.86 | k02 graft |
| 23 | ritual-2 UTHAO! UTHAO! (the varmala lift) | 6.40 | 6.86 | 6.86 | 6.29 | 7.43 | 3.71 | 5.86 | 5.71 |  |
| 24 | everyday-2 SAFETY MATCHES. | 6.40 | 4.86 | 7.00 | 7.29 | 7.14 | 8.00 | 6.29 | 5.71 |  |
| 25 | type-4 AAJ KA BHAAV (today's rate) | 6.31 | 5.57 | 7.57 | 6.86 | 6.00 | 6.43 | 5.14 | 5.71 |  |
| 26 | culture-1 SUITABLE MATCH | 6.25 | 4.14 | 7.14 | 6.86 | 7.43 | 7.29 | 8.14 | 5.57 | k01 graft |
| 27 | surreal-4 HALKA PHULKA (LOOKS HEAVY. ISN'T.) | 6.19 | 5.57 | 7.86 | 6.00 | 6.57 | 5.71 | 5.57 | 5.57 | k09 graft |
| 28 | ritual-3 BARAAT KI ROSHNI (the baraat's light, at actual size) | 6.19 | 7.71 | 8.00 | 4.71 | 5.71 | 3.71 | 5.71 | 5.29 |  |
| 29 | culture-4 WINDOW SEAT | 6.15 | 5.00 | 6.57 | 6.00 | 7.71 | 6.43 | 7.43 | 6.00 |  |
| 30 | everyday-3 NOT LOCKER MATERIAL. | 6.03 | 5.43 | 5.43 | 6.71 | 6.00 | 7.86 | 7.57 | 5.43 |  |
| 31 | art-2 POINT. LINE. CIRCLE. | 6.02 | 4.86 | 7.57 | 5.86 | 5.29 | 8.29 | 7.57 | 5.29 |  |
| 32 | culture-2 HAT-TRICK | 5.94 | 4.00 | 7.29 | 7.14 | 5.00 | 8.14 | 6.86 | 5.00 |  |
| 33 | culture-3 HOOP OK PLEASE | 5.84 | 3.86 | 7.86 | 6.43 | 5.14 | 7.43 | 7.43 | 4.86 |  |
| 34 | ritual-4 MUDRA (the hand speaks) | 5.70 | 4.71 | 6.71 | 5.00 | 8.29 | 6.14 | 6.29 | 5.00 |  |
| 35 | metaphor-5 SAMMOHAN. (look into the piece) | 5.58 | 4.57 | 7.43 | 5.71 | 4.57 | 6.86 | 6.14 | 4.71 |  |
| 36 | surreal-2 THE STARS SAID DECEMBER. | 5.41 | 4.57 | 7.00 | 4.71 | 6.86 | 5.00 | 6.57 | 4.57 |  |
| 37 | everyday-5 DEKHO MAGAR PYAAR SE. | 5.34 | 3.14 | 7.86 | 5.43 | 5.14 | 7.43 | 7.14 | 4.29 |  |
| 38 | type-3 SET IN 18K GOLD TONE (the Naira typeface) | 5.07 | 6.00 | 5.29 | 3.14 | 5.29 | 8.29 | 7.57 | 4.14 |  |
| 39 | everyday-4 LESS THAN ONE CUTTING. | 4.63 | 2.71 | 6.00 | 5.57 | 4.14 | 7.14 | 6.43 | 3.29 |  |
| 40 | type-5 LAMBI PARCHHAI (a long shadow) | 4.59 | 3.57 | 5.71 | 4.14 | 6.86 | 4.71 | 5.57 | 3.57 | k05 graft |

**How the ten were picked.** The selection took the six highest-scoring concepts as they stood (ranks 1-6: AUNTY NE CHASHMA LAGAYA, MUJHE KUCH NAHI CHAHIYE, SHAADI KA VIDEO, PARCHHAI, BEST OF THREE, UDHAAR KHATA), then the strongest camp from each lens not yet in the set: BIJLI GAYI for surreal, EK MATRA KI KAMI for type (chosen over DO MATLAB, which edged it by 0.05 overall, for its far higher crazy score; DO MATLAB's two-meaning device is grafted into two camps instead), AAJ KA BHAAV for culture and PAINTED BIGGEST for art (tied with THE WALL DANCES, which became its graft). Concepts that overlapped a lead were folded in as grafts rather than dropped: story-4 FULL HOUSE and culture-1 SUITABLE MATCH into k01, art-3 into k02, surreal-1 COW FOR SCALE into k03, story-5 into k04, type-5 LAMBI PARCHHAI into k05, everyday-1 RISHTA AAYA HAI into k06, type-2 DO MATLAB into k07 and k08, surreal-4 HALKA PHULKA into k09, art-4 into k10. ritual-1 NAZAR UTAARO (rank 7) was the one high scorer left out: ritual already leads with BEST OF THREE and story already holds three camps. Seven of the eight lenses lead a camp (story ×3, metaphor ×2, ritual, surreal, type, culture, art); everyday lives on as a graft. No two camps share a world or a device.

Each pick was then built into a full bible, pushed once more for craziness, and truth-checked against the hard rules only; the `changes` field of each camp in `crazy100.json` records what was pushed and every truth fix.

## 5. The ten camps at a glance

| Batches | Camp | Lead concept (jury) | World | Device | Reels | Angles P/Ou/Ob/Of | Layers E/T/S |
|---|---|---|---|---|---|---|---|
| 1-2 (k01a, k01b) | **k01 AUNTY NE CHASHMA LAGAYA.** | story-3, rank 1, 7.92 | one wedding through an aunty's reading glasses | honest 2× lens + FIG report | 1, 5, 7, 10 | 2/3/3/2 | 3/5/2 |
| 3-4 (k02a, k02b) | **k02 SHAADI KA VIDEO.** | metaphor-3, rank 3, 7.81 | the 1996 shaadi cassette, paused and recording | VHS display; titles that perform their effect | 1, 3, 5, 6, 10 | 3/3/2/2 | 3/3/4 |
| 5-6 (k03a, k03b) | **k03 BEST OF THREE.** | ritual-5, rank 5, 7.67 | the ring-in-the-milk game, broadcast live | commentator's call + chalk score strip | 1, 3, 5, 6, 10 | 2/3/2/3 | 2/4/4 |
| 7-8 (k04a, k04b) | **k04 MUJHE KUCH NAHI CHAHIYE.** | story-1, rank 2, 7.84 | one home at night under one bulb | her sentence + the ladder of years | 1, 3, 5, 6 | 2/3/2/3 | 4/2/4 |
| 9-10 (k05a, k05b) | **k05 PARCHHAI.** | metaphor-1, rank 4, 7.71 | sunlit lime-washed walls on 21 December | object line + its own type-shadow | 1, 2, 5, 9 | 3/3/2/2 | 3/3/4 |
| 11-12 (k06a, k06b) | **k06 UDHAAR KHATA.** | story-2, rank 6, 7.65 | flash photographs of small family crimes | the excuse + Didi's ledger + the stamp | 1, 5 | 3/2/3/2 | 3/2/5 |
| 13-14 (k07a, k07b) | **k07 BIJLI GAYI.** | surreal-3, rank 9, 7.29 | one power cut, ten lights | lit type + inverter log + switchboard | 1, 4, 10 | 2/3/3/2 | 3/3/4 |
| 15-16 (k08a, k08b) | **k08 EK MATRA KI KAMI.** | type-1, rank 13, 6.95 | blank shaadi cards, one per function | the jewel as the missing matra | 1, 2, 5, 7, 10 | 3/3/2/2 | 4/3/3 |
| 17-18 (k09a, k09b) | **k09 AAJ KA BHAAV.** | culture-5, rank 15, 6.88 | Naira's own counter at night | a rate board that never moves | 1 | 3/2/2/3 | 1/3/6 |
| 19-20 (k10a, k10b) | **k10 PAINTED BIGGEST.** | art-5, rank 18, 6.81 | royal album folios, hand-painted miniatures | hieratic scale + jadval ruler | 2, 3, 6, 8 | 2/3/3/2 | 4/2/4 |
| | **All 100** | | | | 37 | 25/28/24/23 | 30/30/40 |

## 6. The camps

### k01 · AUNTY NE CHASHMA LAGAYA.

Batches 1 and 2 (`k01a`: cards 1-5, `k01b`: cards 6-10).

- **Jury:** story-3 AUNTY NE CHASHMA LAGAYA. (rank 1, overall 7.92: crazy 7.71 · stop 7.86 · sell 7.71 · brand 8.43 · make 6.71 · stretch 8.29 · ten 8.57).
- **Grafts:** story-4 FULL HOUSE. (rank 8, overall 7.37: crazy 6.14 · stop 6.71 · sell 9.00 · brand 7.14 · make 7.71 · stretch 8.57 · ten 7.14); culture-1 SUITABLE MATCH (rank 26, overall 6.25: crazy 4.14 · stop 7.14 · sell 6.86 · brand 7.43 · make 7.29 · stretch 8.14 · ten 5.57).
- **Idea in one line:** One wedding seen through an aunty's reading glasses: inside her half-moon lens the piece is shown honestly at 2×, outside it stays true size, and ten inspections run in clock order from the sangeet to the kitty party.
- **Why it is 10/10:** It names the fear every wedding guest carries (will it look cheap up close?) and answers it in the same frame, with real magnification owned by a character everyone recognises from her hand and pallu alone. It is the jury's top camp, and the turn on card 5, where the inspector becomes the buyer, makes it a series people forward rather than ten separate ads.
- **Why it sells, and buys three:** Trust first: the 2× lens with the listed size printed beside it is the proof. Then basket size: five functions and an aunty who remembers repeats make three pieces a need, not a discount. Card 5 is her BUY3 order slip (hers, the bahu's, the samdhan's, with the padosan struck out 'agli baar'); card 10 pays it off as BUY4: four aunties, four ring sizes, one ring that adjusts from US 5 to 9.
- **What it borrows in thinking from the research:** Board #60 (dashed zoom circles on a detail) and #29 (leader-line notes on a still life) become the lens and the FIG report; PLAYBOOK archetype A8, Callout Anatomy; the owner's graphic bar, the FIG layout on the live lotus Story; and our own 'Where is this from?' hook, which becomes 'Then she asked for the link'. Grafts: story-4 FULL HOUSE (the kitty party and BUY4) and culture-1 SUITABLE MATCH ('love cum arranged', so GOLD TONE weds SILVER TONE).
- **What is new:** Magnification as a character, not a badge: an honest 2× crop of the same photograph clipped to a real lens rim. An eye-chart headline that gets harder to read as it goes, THE SQUINT on Reels (the type stays blurred until her glasses lock on), a log that turns the carousel into one wedding night, and a seal that flips from AUNTY APPROVED to KITTY APPROVED.
- **Textual graphic device:** THE INSPECTION REPORT: an inspection log ('SANGEET · 10:40 PM · INSPECTION 1 OF 10'), an eye-chart Velista headline with acuity marks, the 2× lens composite, up to three FIG callouts (the fact in the Jost label, her Hinglish verdict in the Cormorant quote, never a claim in a quote), a scale tag ('IN HER LENS ABOUT 2× · ACTUAL 25 MM'), the round seal and a 6/6 line of allowed claims.
- **Motion:** Four Reels (1, 5, 7, 10). Cards 1 and 5 are Kling clips played in reverse so the glasses land on the verified still; card 7 plays forward with a live 2× lens on the swinging pearl; card 10 is post-only type motion (five hands are too risky to move). A voice actor opens every Reel: 'Beta, zara idhar aana.'

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Woven Gold Hoops | PAIN · TRUST | AUNTY NE CHASHMA LAGAYA. | Sangeet at 10:40 PM: an ear seen from behind, the aunty's tortoiseshell half-moon held over the hoop, the open braid at 2× inside the lens. | yes (Kling 3.0) |
| 2 | Halo Curve Ring | OBJECTION · EDUCATION | YEH BROWN WALA KAUNSA HAI? | 1 a.m. at the chai counter: a hand round a cutting-chai glass, her lens over the tiger eye and the pale champagne crystal. |  |
| 3 | Verdant Circlet Studs | OUTCOME · TRUST | AUNTY KO TAARE DIKH GAYE. | Rooftop mehendi under an indigo sky: her lens finds the two little stars hidden on the circlet. |  |
| 4 | Baroque Shell Bracelet | OBJECTION · TRUST | EK BHI MATCH NAHI KARTA. | Diya-lit baithak: a wrist on plum velvet, her lens over the toggle and the drop pearl; the eight pearls traced as a line-up. |  |
| 5 | Toggle Link Chain | OFFER · SELL | AUNTY BHI LEGI. | The twist: the aunty herself, a neck crop in rani-pink silk, holds her own lens over the sailor ring; her order slip beside it. | yes (Kling 3.0) |
| 6 | Duo Link Necklace | OBJECTION · EDUCATION | GOLD TONE WEDS SILVER TONE. | Pheras at 2:10 a.m.: both lenses across one collar chain, one over a gold-tone link, one over a silver-tone link. |  |
| 7 | Baguette Halo Drops | OUTCOME · TRUST | SHE COUNTED TWENTY. TWICE. | Reception at midnight: an ear from behind with a mogra gajra, her lens over the twenty-baguette disc, the pearl swinging below. | yes (Kling 3.0) |
| 8 | Prism Cluster Studs | OUTCOME · EDUCATION | ITNE RANG, EK KAAN PE? | Cocoa cocktail lounge: her lens over the five-cut arc on an ear; a tailor's matching card with swatches taken from the stones. |  |
| 9 | Marquise Drop Choker | PAIN · TRUST | PICHLI SHAADI MEIN BHI YAHI THA? | Haldi morning, the one daylight frame: the sideways marquise and two pear drops under her lens; her repeat register. |  |
| 10 | Verdant Eternity Band | OFFER · SELL | AUNTY KI KITTY BHI LEGI. | Overhead kitty party on plum velvet: four aunties' fingertips and four pairs of glasses round one ring hand. | yes (HTML only) |

Angle mix: PAIN 2 · OUTCOME 3 · OBJECTION 3 · OFFER 2. Layers: EDUCATION 3 · TRUST 5 · SELL 2.

### k02 · SHAADI KA VIDEO.

Batches 3 and 4 (`k02a`: cards 1-5, `k02b`: cards 6-10).

- **Jury:** metaphor-3 SHAADI KA VIDEO. (the 90s wedding-video effects, made solid) (rank 3, overall 7.81: crazy 8.43 · stop 8.29 · sell 6.71 · brand 7.43 · make 7.71 · stretch 7.71 · ten 8.29).
- **Grafts:** art-3 FOUR SHOWS DAILY (rank 22, overall 6.52: crazy 5.14 · stop 8.00 · sell 7.29 · brand 6.00 · make 6.00 · stretch 7.43 · ten 5.86).
- **Idea in one line:** The 1996 shaadi cassette, paused: the slow pieces turn out to be the video's own effects made solid (the star filter, the heart frame, the butterfly wipe, the lens flare, the crash zoom), and the REC cards give those effects to her own tape this season.
- **Why it is 10/10:** The joke is the product description: a four-point star stud is the star filter, a heart drop is the heart frame, a butterfly ring is the butterfly wipe. Every family has laughed at that cassette, so the forward carries the piece. It has the highest crazy score of all forty concepts.
- **Why it sells, and buys three:** Two tenses split the funnel: REC cards (her tape, 2026) carry the outcome; playback cards carry the pains the tape recorded (the same jhumkas in all five tapes, casserole number seven, the plating that went dark). The offers speak the tape's language: COLLECT ANY THREE (BUY3); THREE BOWS, NO CASSEROLES (each bow under ₹800 with BUY3); ONE PIECE PER TAPE, four VHS spines as a ready BUY4 basket, three of the four in stock.
- **What it borrows in thinking from the research:** Board #78 (a heart-shaped swatch frames the headline) becomes the heart frame; #19 and #47 (visual puns that make the product the joke); PLAYBOOK A3, Literal Rhyme. It is written to avoid repeating concept-50's c08 THE ONLY COLOUR (card 6 is a 90s ripple-dissolve flashback, not a grey wedding) and c01's struck gift list (card 7 is the 1996 gift register). Graft: art-3 FOUR SHOWS DAILY (four functions become four tapes).
- **What is new:** Every title performs its own effect (the full stop of FILTER is a star, the wipe cuts through BUTTERFLY, SOFT is blurred while FOCUS is sharp, FORWARD tears), all of 1996 lives in HTML masked off the metal and stones, and a woman of the buyer's own age is finally the one on the tape.
- **Textual graphic device:** A VHS on-screen display (REC, PLAY, PAUSE, REW, FF, STOP, EJECT) that names both the angle and the tense, a 90s title card in Velista, one tracking band on playback only, viewfinder brackets on REC, the Naira wordmark as the videographer's studio bug and the F2 card as a lower-third name super.
- **Motion:** Five animated: cards 1 and 3 through Kling (the world moves, the piece stays rigid); cards 5, 6 and 10 are HTML only (iris and credit roll, colour drain, crash zoom and spines), so the hardest pieces never pass through a video model.

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Quatrefoil Éclat Studs | OUTCOME · EDUCATION | THE STAR FILTER. | REC: an ear from behind under a shamiana; the HTML star filter twinkles on the bokeh, the real star stud hangs at its own angle. | yes (Kling 3.0) |
| 2 | Aqua Heart Drops | OUTCOME · TRUST | THE HEART FRAME. | REC: the ear and drop of a woman in her late forties inside a feathered 1996 heart frame whose edge is written in listing facts. |  |
| 3 | Lilac Papillon Ring | OUTCOME · SELL | THE BUTTERFLY WIPE. | REC: a hand on a plum lehenga; a giant butterfly wipe lands its body exactly on the ring. | yes (Kling 3.0) |
| 4 | Brushed Gold Huggies | PAIN · TRUST | THE SOFT FOCUS. | REW: the pair standing on a black VHS cassette under a hard 1996 video light, soft-focus mist on everything but the pair. |  |
| 5 | Verdant Cushion Studs | OFFER · SELL | THE END. | STOP: the iris closes to black round one green stud on an ear; THE END and the cast credits roll the offer. | yes (HTML only) |
| 6 | Monochrome Enamel Hoops | OBJECTION · EDUCATION | THE FLASHBACK. | PAUSE: a mehendi-day ear drained to a 90s black-and-white flashback, only the hoop left in colour. | yes (HTML only) |
| 7 | Petite Bow Studs | PAIN · SELL | THE PAGE PEEL. | REW: bow studs pinned to a plum gift-box lid; the page peel lifts to show the 1996 casserole register. |  |
| 8 | Rivière Hoops — Silver | PAIN · EDUCATION | THE FAST FORWARD. | FF: a 35 mm hoop frozen mid sangeet turn, mirror-ball streaks behind; the tape index skips the same jhumkas. |  |
| 9 | Baguette Halo Drops | OBJECTION · TRUST | THE LENS FLARE. | SLOW: the drop on cocoa velvet; a picture-in-picture of the listing photo, and the fake flare on the title only. |  |
| 10 | Toggle Link Chain | OFFER · SELL | THE CRASH ZOOM. | EJECT: collarbones with the sailor ring turned to the front; crash-zoom streaks and four VHS spines as a BUY4 basket. | yes (HTML only) |

Angle mix: PAIN 3 · OUTCOME 3 · OBJECTION 2 · OFFER 2. Layers: EDUCATION 3 · TRUST 3 · SELL 4.

### k03 · BEST OF THREE.

Batches 5 and 6 (`k03a`: cards 1-5, `k03b`: cards 6-10).

- **Jury:** ritual-5 BEST OF THREE (the ring game) (rank 5, overall 7.67: crazy 7.14 · stop 8.14 · sell 8.43 · brand 8.14 · make 5.71 · stretch 6.43 · ten 7.57).
- **Grafts:** surreal-1 COW FOR SCALE. (rank 11, overall 7.03: crazy 7.57 · stop 9.00 · sell 5.29 · brand 7.00 · make 4.86 · stretch 8.00 · ten 6.86).
- **Idea in one line:** Angoothi dhoondhna, the ring-in-the-milk game after the pheras, broadcast like a world final: hands burst out of a brass paraat of milk holding the piece, the commentator's call is the headline, and best of three is BUY3.
- **Why it is 10/10:** It is the one Indian wedding ritual whose climax is finding a piece of jewellery, and its own rule (best of three, and the winner runs the house) is the offer. A hand bursting out of milk proves waterproof without a claims panel, and ten broadcast moments (burst, wire cam, photo finish, trophy lift, replay, time-out, match fixed) keep ten splashes from looking alike.
- **Why it sells, and buys three:** BUY3 is the game's rule, so cards 5 and 10 close on it; on card 8 the sore loser asks 'best of four?' and a chalk bill shows the fourth piece adding about ₹190 under BUY4. Only waterproof-tagged pieces go into the milk, and the anchors are the deepest slow stock (Woven 88, Verdant Eternity 58, Brushed 58).
- **What it borrows in thinking from the research:** Board #15 and #17 (a piece mid-splash or bursting through a splash to show waterproof) and #7 (the shower moment as proof); #59 (three steps on podiums) becomes three rounds; PLAYBOOK A13, Suspended (the frozen fall). Graft: surreal-1 COW FOR SCALE, the honest two-row scale bar (PARAAT · ABOUT 45 CM over RING · 17 MM INSIDE).
- **What is new:** Every call is literally true of the piece (TOO CLOSE TO CALL for two ends that almost touch, NOTHING TO LOSE for a ring with no stones, MATCH FIXED for a cuff with one end for each of them); a chalk score strip runs one match and a rematch across the carousel; one proof device per card grows out of the plate (size gun, ripple text, photo finish, replay, search reticle, the bill, house rules).
- **Textual graphic device:** THE MATCH-DAY KIT, hand-made and never a real channel's: a live dot and a chalk-tally score strip, the Velista call with its winning words in saffron, one proof device per card carrying a listing fact, and the F2 card on cocoa.
- **Motion:** Five Kling clips (1, 3, 5, 6, 10): the burst, the reach, the petal shower, the falling milk drop, the raised arm. The verified piece is composited as a rigid cut-out and tracked, never re-rendered.

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Verdant Eternity Band | OBJECTION · TRUST | ROUND ONE: HERS. | A mehendi hand bursts out of a paraat of milk holding the ring inside a frozen milk crown; the size gun reads US 5 to 9. | yes (Kling 3.0) |
| 2 | Woven Gold Hoops | OUTCOME · EDUCATION | VISIBLE FROM THE CHHAT. | Wire cam, straight down: the pair on a palm rising out of the milk, concentric ripples carrying the specs. |  |
| 3 | Droplet Open Ring | OUTCOME · EDUCATION | TOO CLOSE TO CALL. | Photo finish: two hands reach out of the milk, fingertips a centimetre apart, the ring's two ends almost touching. | yes (Kling 3.0) |
| 4 | Tubogas Dome Ring | PAIN · TRUST | NOTHING TO LOSE. | Low hero angle: a victory fist punches up through a backlit milk crown, the ridged band on the ring finger. |  |
| 5 | Mint Pear Drop Earrings | OFFER · SELL | BEST OF THREE. | Trophy lift under a petal shower: the pair pinched up out of the milk; three rounds and a prize drawn on the piece. | yes (Kling 3.0) |
| 6 | Serpentine Whisper Chain — Silver | OBJECTION · TRUST | ONE DROP IS MILK. | Freeze-frame replay on plum: the chain lifted out, one bead of milk about to fall off the stone's prong. | yes (Kling 3.0) |
| 7 | Charm Box Chain | PAIN · TRUST | DAY FIVE. STILL BRIGHT. | A milk-line horizon like a white sea: one fingertip rises like a lighthouse with the barrel charm on top. |  |
| 8 | Brushed Gold Huggies | OFFER · SELL | BEST OF FOUR? | Time-out: the groom's palm held out under diya light with the pair standing on it; the BUY3-to-BUY4 bill. |  |
| 9 | Baroque Bloom Cuff | OUTCOME · SELL | MATCH FIXED. | On the paraat's wet rim, his fingers slide the cuff toward her reaching fingertips: match fixed. |  |
| 10 | Triple Coil Wrap Bangle | OFFER · SELL | HOUSE RULES. | Her forearm rises out of the milk, milk pouring off the two-turn coil; her house rules beside it. | yes (Kling 3.0) |

Angle mix: PAIN 2 · OUTCOME 3 · OBJECTION 2 · OFFER 3. Layers: EDUCATION 2 · TRUST 4 · SELL 4.

### k04 · MUJHE KUCH NAHI CHAHIYE.

Batches 7 and 8 (`k04a`: cards 1-5, `k04b`: cards 6-10).

- **Jury:** story-1 MUJHE KUCH NAHI CHAHIYE. (rank 2, overall 7.84: crazy 6.29 · stop 7.71 · sell 8.71 · brand 9.29 · make 7.43 · stretch 7.57 · ten 8.29).
- **Grafts:** story-5 PLASTIC MAT UTAARNA. (rank 10, overall 7.22: crazy 6.86 · stop 7.43 · sell 7.14 · brand 7.43 · make 7.57 · stretch 7.86 · ten 7.14).
- **Idea in one line:** Every Indian mother's yearly line, 'Mujhe kuch nahi chahiye', set huge over the one bright thing she would never buy herself, above a 32-year ladder of her refusals that breaks in 2026: order anyway.
- **Why it is 10/10:** It is the truest sentence in Indian family life, and one terracotta stroke through NAHI turns it into what she always meant. It reaches both buyers at once (the daughter or first-salary son, and the woman who has started saying it herself), and the jury put it second overall with the second-highest sell score of all forty.
- **Why it sells, and buys three:** Emotional permission plus gift maths, with offers that climb like the ladder: BUY2 for two sisters who each push the gift to the other, BUY3 for three tiffin tiers (Mummy, Mausi, tum), BUY4 for Nani, Mummy, Mausi and you. Every piece is too practical to be saved for later: waterproof, tarnish free, adjustable, made for a Tuesday.
- **What it borrows in thinking from the research:** The PLAYBOOK's F2 grammar (one saturated piece in a dark frame) and board #3 (one product under one light on black) set the look; board #25 (items tagged by where they go) becomes the tiffin tiers labelled MUMMY, MAUSI, TUM; the RED ROOM rule (each card's graphic comes out of the picture and carries real facts) makes every card re-tune its ladder. Graft: story-5 PLASTIC MAT UTAARNA (she saves every good thing for later; 'made for Tuesdays').
- **What is new:** A ladder of years that is texture first and text second, one struck word as the camp's turn, refusals acted out by hands (thumbs lifting to hand the hoops back, an envelope pushed back across the table, two sisters pushing one bracelet at each other), and a drawn proof grown from each ladder (a quarter-turn diagram, a US 5 to 9 gauge, a dial with no hands).
- **Textual graphic device:** THE SENTENCE in Velista with a giant gold-light open quote and a Jost signature ('MUMMY, EVERY YEAR SINCE 1994'); THE LADDER down the left edge, fading like a till roll; THE BREAK in terracotta (2026, the piece's name, 'Order anyway.'); one drawn proof per card.
- **Motion:** Four Kling clips (1, 3, 5, 6): her fingers close over the hoops as the stroke lands through NAHI; a fan shadow sweeps the thread-trick bed; the tap runs over the tiffin; she clicks off the house's last switch and only the bangle keeps the light.

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Woven Gold Hoops | PAIN · EDUCATION | MUJHE KUCH NAHI CHAHIYE. | A mother's cupped hands under one bulb, thumbs lifting to hand the hoops back; NAHI struck through in terracotta. | yes (Kling 3.0) |
| 2 | Toggle Link Chain | OUTCOME · EDUCATION | HILNA MAT, MUMMY. | 11 pm, from behind: a daughter's hands close the sailor-ring clasp at her mother's grey-streaked nape. |  |
| 3 | Verdant Eternity Band | OBJECTION · EDUCATION | NOBODY KNOWS HER RING SIZE. | Her sleeping hand on an oxblood sheet, a measuring thread round the ring finger, the ring standing beside it. | yes (Kling 3.0) |
| 4 | Brushed Gold Huggies | OUTCOME · SELL | PEHLI SALARY, MAA. | A first-salary envelope pushed across the table by his hand and pushed back by her fingertips, the pair on the flap. |  |
| 5 | Triple Coil Wrap Bangle | OFFER · SELL | AB TUM BHI KEHTI HO. | 7 am at a steel sink: three tiffin tiers, the coil on her wrist under the running tap. | yes (Kling 3.0) |
| 6 | Molten Panel Bangle | PAIN · EDUCATION | TIME KAHAN HAI? | 11:20 pm: her finger presses the house's last switch; the bangle catches the last light. | yes (Kling 3.0) |
| 7 | Heartbead Bracelet | OUTCOME · TRUST | MERE PAAS SAB HAI. | Black granite counter: the bracelet in front of a leaning tower of twelve steel katoris. |  |
| 8 | Baroque Shell Bracelet | OBJECTION · TRUST | BAAD MEIN PEHNUNGI. | Her hand pushes the empty almirah locker shut, the shell pearls finally out on her wrist. |  |
| 9 | Ribbon Bead Bracelet | OFFER · SELL | MAUSI BHI YAHI KEHTI HAI. | Two sisters' fingertips push one bracelet toward each other across a faded razai. |  |
| 10 | Torsade Pearl Cuff | OFFER · SELL | BILKUL MAA PE GAYI HAI. | A mother's hand cradles her daughter's forearm; two pearls face each other across the cuff's gap. |  |

Angle mix: PAIN 2 · OUTCOME 3 · OBJECTION 2 · OFFER 3. Layers: EDUCATION 4 · TRUST 2 · SELL 4.

### k05 · PARCHHAI.

Batches 9 and 10 (`k05a`: cards 1-5, `k05b`: cards 6-10).

- **Jury:** metaphor-1 PARCHHAI. (the shadow says what the gift means) (rank 4, overall 7.71: crazy 7.57 · stop 8.00 · sell 7.29 · brand 8.43 · make 6.29 · stretch 8.57 · ten 7.86).
- **Grafts:** type-5 LAMBI PARCHHAI (a long shadow) (rank 40, overall 4.59: crazy 3.57 · stop 5.71 · sell 4.14 · brand 6.86 · make 4.71 · stretch 5.57 · ten 3.57).
- **Idea in one line:** On 21 December, the day of the longest shadows, each real piece casts not its shape but its meaning (two people holding hands, a cobra with one jewel, a circle of sangeet dancers, a house key), and the headline casts its own shadow under the same sun.
- **Why it is 10/10:** It is the best type idea in the set: the object line counts honestly (TWO STONES.) and its skewed shadow says what the gift means (tum aur main.). A shadow is the only prop with no colour, so it can fill the wall and never compete with the jewel. The jury gave it the joint-highest stretch score: anything with an outline casts something.
- **Why it sells, and buys three:** December is the month she buys for everyone, so each piece arrives with one named person and one sentence: nine different people across ten cards. Cards 3, 4 and 5 thread one sentence through three shadows ('a whole stack, for didi; the nagamani, for you; and the whole sangeet, for the cousin'), which turns three pieces into one order; card 10 sells three of the same adjustable ring to nani, maa and you.
- **What it borrows in thinking from the research:** Board #1 (a sun arc from 10 AM to 5 PM) becomes the sundial hour on every card, and #82 (a product drawn as a padlock) becomes the toggle's key shadow, both cited in the bible; the lesson of our winners that the piece must be the loudest colour in a calm frame; PLAYBOOK A3, Literal Rhyme. Graft: type-5 LAMBI PARCHHAI (one sentence through three shadows).
- **What is new:** Real solar angles over Delhi on 21 December, so the shadows lengthen as she swipes; light passing through the type wherever it passes through the plate (the lit 'aur', the jewel dot over 'nagamani'); a size line that escalates from 'SHADOW NOT INCLUDED' to 'THE OTHER 1,740 KM NOT INCLUDED' and flips once on the moon card ('MOON INCLUDED · STARS NEXT DECEMBER'). Shadow art in the line of Shigeo Fukuda, never used in Indian jewellery.
- **Textual graphic device:** THE DOUBLE LINE: a Velista object line in the light, its type-shadow in Cormorant italic skewed to the plate's measured lean, a sundial dot and hour on the frame edge, a size line at the root of the piece, and sun-ray callouts for proof.
- **Motion:** Four Kling clips (1, 2, 5, 9) with the piece pixel-locked: the shadow stretches from the true outline into its meaning while the type's own shadow re-letters into the meaning line; the dancers turn to a dhol-tasha beat on card 5; the moon rises on card 9.

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Halo Curve Ring | OUTCOME · EDUCATION | TWO STONES. | The ring on a ledge against a sky-blue wall; its long shadow becomes two people holding hands. | yes (Kling 3.0) |
| 2 | Lilac Papillon Ring | OUTCOME · EDUCATION | ONE BUTTERFLY. | A hand against a pista wall; the ring's shadow comes loose and flies off as a butterfly. | yes (Kling 3.0) |
| 3 | Triple Coil Wrap Bangle | OBJECTION · TRUST | TWO TURNS. | A forearm against saffron; one two-turn coil on the arm, a stack of twelve bangles on its shadow. |  |
| 4 | Serpentine Whisper Chain (gold tone) | OUTCOME · TRUST | ONE STONE. | The pendant over a terracotta parapet; its shadow rears up as a cobra with one jewel of light. |  |
| 5 | Woven Gold Hoops | OFFER · SELL | TWO HOOPS. | The pair on one brass nail on coral; their round shadow is a circle of sangeet dancers. | yes (Kling 3.0) |
| 6 | Toggle Link Chain | PAIN · SELL | ONE TURN. | The chain in a V on sky blue; the toggle's shadow becomes one big old house key. |  |
| 7 | Duo Link Necklace | OBJECTION · TRUST | SIXTEEN KNOTS. | Top-down loop on terracotta; the shadow is a dupatta and a shawl tied in the wedding knot. |  |
| 8 | Droplet Open Cuff | PAIN · EDUCATION | TWO ENDINGS. | The cuff standing on a ledge; its shadow is two hands reaching, never quite touching. |  |
| 9 | Bold Dome Huggies | PAIN · SELL | ONE MOON. | Dusk on a plum wall: the dome hoop throws a crescent moon of reflected light up the shade. | yes (Kling 3.0) |
| 10 | Verdant Eternity Band | OFFER · SELL | ONE RING. | A grandmother's hand in the last light; its shadow grows into a tree lit by the ring's green. |  |

Angle mix: PAIN 3 · OUTCOME 3 · OBJECTION 2 · OFFER 2. Layers: EDUCATION 3 · TRUST 3 · SELL 4.

### k06 · UDHAAR KHATA.

Batches 11 and 12 (`k06a`: cards 1-5, `k06b`: cards 6-10).

- **Jury:** story-2 UDHAAR KHATA. (rank 6, overall 7.65: crazy 7.14 · stop 7.14 · sell 8.14 · brand 8.14 · make 7.00 · stretch 8.14 · ten 8.00).
- **Grafts:** everyday-1 RISHTA AAYA HAI. (rank 14, overall 6.89: crazy 6.00 · stop 7.29 · sell 6.86 · brand 7.57 · make 7.71 · stretch 8.14 · ten 6.57).
- **Idea in one line:** In an Indian family, jewellery is on permanent loan: every card is a flash photograph of a small family crime, the borrower's excuse is the headline, and Didi's red ledger fills with question marks until three pieces close the account.
- **Why it is 10/10:** Every sister has both said and heard these excuses ('sirf ek function ke liye', 'kal wapas kar dungi'). Flash-caught evidence reads as a crime at 200 px, a ledger filling with ?, ?? and ??? is a type joke people screenshot, and 'buy three, get yours back' is the most natural three-piece logic on the table.
- **Why it sells, and buys three:** BUY3 is the only known way to get your own earrings back: one for you, one for her, one for whoever she lends it to. Cards 5 and 10 close the books (the question marks become ticks), and the two ₹699 pieces (Ribbon Bead, Brushed Gold) make a three-piece order easy. Each slow piece gets a reason to be wanted: it is the thing someone in the family would not give back.
- **What it borrows in thinking from the research:** Board #49 (handwritten labels with dotted arrows name each piece) becomes the ledger entries; #76 (one witty prop makes the product unmissable) becomes one document per card; the RED ROOM rule that every graphic comes out of the picture and carries real facts. Graft: everyday-1 RISHTA AAYA HAI (the joint-family close, JOINT FAMILY. SEPARATE EARRINGS.).
- **What is new:** Ten kinds of evidence instead of one gesture: a clean ring left in spilled talc, a getaway auto, a missing-person notice whose INAAM (reward) line is the offer, a floor that is the earring's own face with a headline that changes colour mid-word, a library issue card with a waiting list, an identification sketch, a family ring-size ruler, a TO: me / FROM: me gift tag.
- **Textual graphic device:** THE EXCUSE (Velista inside a giant terracotta open quote), THE KHATA strip (a torn bone ledger page, an oxblood cloth spine, a WAPAS column of question marks), THE STAMP (a distressed terracotta roundel whose word changes on every card) and one document per card.
- **Motion:** Two Kling clips (1, 5): on card 1 the date imprint rolls from the 2nd to the 20th while the ledger writes itself and the stamp thuds; on card 5 the question marks turn into ticks and KHATA BAND lands on a dholak hit.

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Torsade Huggies | PAIN · SELL | SIRF EK FUNCTION KE LIYE. | Flash evidence: one hoop in spilled talc beside the clean ring its twin left, and a dropped hair tie. | yes (Kling 3.0) |
| 2 | Charm Box Chain | PAIN · SELL | KAL WAPAS KAR DUNGI. | A getaway auto at night: the chain escaping a shut potli, the barrel frozen by flash while the city streaks. |  |
| 3 | Verdant Eternity Band | OBJECTION · TRUST | BAS PHOTOS KE LIYE. | Sangeet flash: a mehendi hand in the display pose, the green ring on the middle finger. |  |
| 4 | Monochrome Enamel Hoops | OBJECTION · EDUCATION | SAB KE SAATH CHALTE HAIN. | An Art Deco floor split black \| brass \| white, one hoop standing on each side of the line. |  |
| 5 | Ribbon Bead Bracelet | OFFER · SELL | KHATA BAND. | Chhoti's wrist lying across the closed red bahi-khata, the two-heart bow on top. | yes (Kling 3.0) |
| 6 | Woven Gold Hoops | OUTCOME · TRUST | MERE OUTFIT SE MATCH KARTE HAIN. | From behind at the front door, a hand on the latch, one braided hoop leaving the house. |  |
| 7 | Toggle Link Chain | OUTCOME · EDUCATION | SIRF MANDAP TAK. | A throat crop frozen in a shower of mandap rose petals, the sailor ring turned to the front. |  |
| 8 | Droplet Open Ring | OBJECTION · EDUCATION | ADJUSTABLE HAI NA. | The ring halfway down a walnut sizing mandrel in an emptied oxblood ring tray. |  |
| 9 | Petite Bow Studs | PAIN · SELL | BIRTHDAY MERA THA. | Chipped-plum fingertips lift one bow stud out of a plain birthday box on the bed. |  |
| 10 | Brushed Gold Huggies | OFFER · SELL | JOINT FAMILY. SEPARATE EARRINGS. | Three open palms reaching in: one holds the pair, two wait empty. |  |

Angle mix: PAIN 3 · OUTCOME 2 · OBJECTION 3 · OFFER 2. Layers: EDUCATION 3 · TRUST 2 · SELL 5.

### k07 · BIJLI GAYI.

Batches 13 and 14 (`k07a`: cards 1-5, `k07b`: cards 6-10).

- **Jury:** surreal-3 BIJLI GAYI. (rank 9, overall 7.29: crazy 7.86 · stop 8.14 · sell 6.43 · brand 7.71 · make 6.00 · stretch 6.29 · ten 7.29).
- **Grafts:** type-2 DO MATLAB (two meanings) (rank 12, overall 7.00: crazy 5.86 · stop 6.71 · sell 7.57 · brand 8.29 · make 7.71 · stretch 7.71 · ten 6.86).
- **Idea in one line:** One power cut in a wedding-season house, 8:41 to 9:31 PM, lit by ten different lights every Indian has used in the dark, each one a different test of the finish, until the lights come back and BIJLI AAYI means she walked in.
- **Why it is 10/10:** Darkness is the one honest test of how jewellery handles light, and every Indian can name the power cut's lights (the moon through the grille, the maachis, the torch, two hundred phone torches, the lalten, the last diya). The piece is always the brightest thing in the frame, the grammar our winners share, and the dark-to-light arc ends the carousel on the double meaning.
- **Why it sells, and buys three:** Each card sells one piece as the thing that still shines under one light: polish throws pinpoints, pavé a scatter, satin a glow, a clear stone its own colour. Every home keeps backups for the power cut, so keep three pieces: card 5 hangs the pair in one of three bulb holders with two still empty (1 · LAG GAYA, 2 · BUY2, 3 · BUY3); card 10 flips every switch on, the last one BUY3.
- **What it borrows in thinking from the research:** Card 1 makes the founder's favourite 'Toggle on.' (concept-camps THE TURN, the chain on a vintage light switch) right for 8:41, with moonlight only; board #3 and #4 (one product under a spotlight or a light burst on black) and PLAYBOOK A6, Single Spotlight. Graft: type-2 DO MATLAB (BIJLI AAYI: the power is back, and the stunner walked in).
- **What is new:** LIT TYPE: the headline is lit by the piece through a radial mask, with four deliberate exceptions (a torch circle cutting through card 3's words, a dead-and-live two-tone headline, a dimmed one, a fully lit one). A saffron seven-segment inverter log names each light, and an Indian switchboard with masking-tape labels is the spec device.
- **Textual graphic device:** A lit Velista headline, the second beat in the piece's own sampled colour, the seven-segment log, the switchboard in the F2 card's line, light dots shaped like each cut (never on the piece) and one room device per card.
- **Motion:** Three Kling clips (1, 4, 10): the fan winds down and a cloud crosses the moon; the generator dies mid-sangeet and the dholi plays on unplugged; the inverter beeps and the screen literally lights up.

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Toggle Link Chain | OUTCOME · EDUCATION | BIJLI GAYI. / TOGGLE ON. | 8:41, moonlight through a grille: the chain hung on an old porcelain switch, both strands running down the wall like wiring. | yes (Kling 3.0) |
| 2 | Prism Cluster Studs | OUTCOME · EDUCATION | MAACHIS KAHAN HAI? | 8:42, the found matchbox: its tray pushed out with the pair inside instead of matches. |  |
| 3 | Verdant Cushion Studs | OBJECTION · TRUST | TORCH MAAR KE DEKHO. | 8:47, a hard torch circle on ivory silk: the green stud throws its own pool of green light. |  |
| 4 | Bold Nocturne Bracelet | PAIN · SELL | GENERATOR GAYA. / BULB LAGAO. | 8:55, the generator dies mid-sangeet: a raised arm in the 'bulb' step, phone torches behind. | yes (Kling 3.0) |
| 5 | Woven Gold Hoops | OFFER · SELL | EK LAG GAYA. DO BAAKI. | 9:03, a stairwell of three empty bulb holders; the pair hangs where the first bulb was. |  |
| 6 | Rivière Hoops — Silver | PAIN · SELL | RING LIGHT GAYI. | 9:10, a dead ring light behind; a hand holds the hoop up inside its circle. |  |
| 7 | Marquise Coil Cuff | OBJECTION · TRUST | PARCHHAI JHOOTH NAHI BOLTI. | 9:14, lalten light: a hand makes the swan on the wall, the coil cuff at its neck. |  |
| 8 | Aqua Heart Drops | OUTCOME · EDUCATION | PANDRAH SAAL BAAD, / CANDLELIGHT DINNER. | 9:20, the first candlelight dinner in fifteen years: an ear from behind with the aqua heart. |  |
| 9 | Brushed Gold Huggies | OBJECTION · TRUST | DHEEMI ROSHNI. | 9:26, the candles burnt to stubs; a hoop stands on each stub where the flame was. |  |
| 10 | Petite Square Huggies | OFFER · SELL | BIJLI AAYI. | 9:31, the lights come back: an ear from behind stepping into the bright room. | yes (Kling 3.0) |

Angle mix: PAIN 2 · OUTCOME 3 · OBJECTION 3 · OFFER 2. Layers: EDUCATION 3 · TRUST 3 · SELL 4.

### k08 · EK MATRA KI KAMI.

Batches 15 and 16 (`k08a`: cards 1-5, `k08b`: cards 6-10).

- **Jury:** type-1 EK MATRA KI KAMI (one mark short) (rank 13, overall 6.95: crazy 7.71 · stop 6.14 · sell 6.14 · brand 8.71 · make 7.00 · stretch 6.43 · ten 7.00).
- **Grafts:** type-2 DO MATLAB (two meanings) (rank 12, overall 7.00: crazy 5.86 · stop 6.71 · sell 7.57 · brand 8.29 · make 7.71 · stretch 7.71 · ten 6.86).
- **Idea in one line:** Every December shaadi card on the fridge carries a Devanagari word one mark short, and the real piece lies exactly where that mark goes: a chain is the top bar of पक्का, a ring the dot of अंगूठी, a bangle the dot of कंगन.
- **Why it is 10/10:** It is the only idea where the jewel literally becomes a letter, so type and picture are one object, an award-level move no Indian brand has made. Every Hindi teacher's line (one wrong matra turns meaning into nonsense) is the insight, and the two-script gloss plus the teacher's red pen let non-Hindi readers in.
- **Why it sells, and buys three:** Functions come in threes (mehendi, sangeet, shaadi), so the offer is TEEN FUNCTION, TEEN MATRA · BUY3. Card 5 sets the offer as a haggle she has already won (TEENON CHAHIYE? / TEENON LO.), card 6 climbs to BUY4 (a new haar for every function), and card 10 turns the wedding card's own line, सपरिवार पधारें, into the ladder: bring the bangle's family.
- **What it borrows in thinking from the research:** PLAYBOOK A14 (In-Word Swap) and concept-50's c06 KAHAN SE LIYA? (the piece as punctuation), pushed from Roman punctuation into Devanagari matras; board #82 (a product drawn as the symbol); Absolut's long series on one rule. Graft: type-2 DO MATLAB, the two-script dictionary gloss.
- **What is new:** Each function writes in its own ink (gold foil, henna piped from the cone in frame, a frosted etch under water, turmeric finger-painted by the hand in frame); the teacher's terracotta caret on the minimal-pair cards (हा/हाँ, अगूठी/अंगूठी, हर/हार); proofs inside the picture (a ring gauge round the open back, a real ripple as the matra ring).
- **Textual graphic device:** Six layers: the word in the function's ink, the ghost stroke (the missing mark as a blind deboss), the dashed matra ring with the mark's real name and size, the red-pen caret, the Velista Hinglish headline and the two-script gloss; the Naira wordmark is the invitation's foil seal.
- **Motion:** Five animated: Kling on 1, 5, 7 and 10 (the loose letters snap up under the chain; cold sparks fall; a drop rings out; sunlight climbs the bangle) and HTML only on 2 (the henna pipes itself to the cone's tip, so no video model touches the studs).

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Toggle Link Chain | OUTCOME · EDUCATION | RISHTA PAKKA. | Top-down roka card: the chain laid dead straight as the top bar of पक्का. | yes (Kling 3.0) |
| 2 | Verdant Circlet Studs | OUTCOME · EDUCATION | MEHENDI? HAAN. | Mehendi card: the two studs are the moons of मेहँदी? हाँ, piped in henna from the cone lying in frame. | yes (HTML only) |
| 3 | Prism Cluster Studs | PAIN · EDUCATION | PAANCH FUNCTION, PAANCH DRESS CODE. | An upright plum sangeet card with the pair pinned through it and five dress-code tabs along its edge. |  |
| 4 | Verdant Eternity Band | OBJECTION · TRUST | RING SIZE? PATA NAHIN. | The ring standing in a coral velvet tray as the dot of a giant अ; a ring gauge and a retired measuring thread. |  |
| 5 | Bold Nocturne Bracelet | OFFER · SELL | TEENON CHAHIYE? TEENON LO. | The bracelet laid straight across a cocoa reception card as the bar of तीनों, cold sparks far behind. | yes (Kling 3.0) |
| 6 | Marquise Drop Choker | PAIN · SELL | HAR FUNCTION, WAHI HAAR? | The choker on a stepped stack of function cards; its drop is the ा that turns हर into हार. |  |
| 7 | Serpentine Whisper Chain — Silver | OBJECTION · TRUST | PAANI LAGE TOH? LAGNE DO. | A wet acrylic cocktail invitation: the stone is the dot of बूँद, a real drop beaded on it. | yes (Kling 3.0) |
| 8 | Torsade Huggies | OUTCOME · EDUCATION | KISI KI NAZAR NA LAGE. | The pair standing on an oxblood winter card as the two curls of किसी; a kaala teeka in the corner. |  |
| 9 | Woven Gold Hoops | PAIN · TRUST | HALDI KI PHOTO, KHAALI KAAN? | A haldi banana leaf: a turmeric fingertip has just written पीली; the hoops are its two curls. |  |
| 10 | Molten Panel Bangle | OFFER · SELL | TEEN FUNCTION, TEEN MATRA. | The bangle standing like a monument as the dot of कंगन on the programme page. | yes (Kling 3.0) |

Angle mix: PAIN 3 · OUTCOME 3 · OBJECTION 2 · OFFER 2. Layers: EDUCATION 4 · TRUST 3 · SELL 3.

### k09 · AAJ KA BHAAV.

Batches 17 and 18 (`k09a`: cards 1-5, `k09b`: cards 6-10).

- **Jury:** culture-5 AAJ KA BHAAV (rank 15, overall 6.88: crazy 5.86 · stop 7.14 · sell 7.57 · brand 6.43 · make 8.14 · stretch 7.43 · ten 6.71).
- **Grafts:** surreal-4 HALKA PHULKA (LOOKS HEAVY. ISN'T.) (rank 27, overall 6.19: crazy 5.57 · stop 7.86 · sell 6.00 · brand 6.57 · make 5.71 · stretch 5.57 · ten 5.57).
- **Idea in one line:** Naira's own jewellery counter at night, opened like every Indian shop (the shutter goes up, the tube light ticks on, the rate board lights), where the dot-matrix rate never moves: AAJ ₹699, KAL ₹699, and THOK BHAAV, the wholesale rate, is BUY3.
- **Why it is 10/10:** In a wedding season of record metal rates, the rate is the loudest number in every Indian family, and a board whose number never moves turns 'by the piece, not by the gram' into relief. BHAAV also means attitude, which gives each piece a personality line (BHAAV NAHI KHAATI: the ring that doesn't act pricey).
- **Why it sells, and buys three:** Certainty plus quantity. THOK BHAAV is a bargain she already wins at the mandi; PALDA BARABAR KARO turns BUY3 into an instruction (one pan sinks, two ghost slots wait); the sailor ring is the 0 of '20%'; the torn estimate slip has blank lines 'didi ke liye' and 'apne liye'. Three-piece baskets at live prices come to ₹1,998-2,478 after BUY3.
- **What it borrows in thinking from the research:** Board #8 and #30 (us-versus-them tables) become a board that never moves beside rates that climb; #58 (an equation headline sells the bundle) becomes THOK BHAAV; #49 (handwritten price labels) becomes the estimate slip; concept-50's c02 LAST PRICE? (the haggle answered by the piece); and the PLAYBOOK lesson that spec infographics win clicks rather than purchases, so each instrument carries at most three facts. Graft: surreal-4 HALKA PHULKA (listed grams on a real scale).
- **What is new:** One honest jeweller's instrument per card, grown out of its own picture (scale readout, sizing cone, balance, safe, estimate pad, the flower-seller's pan), the shutter-up opening as motion, and a board that breaks only once: on card 4 its LOOK row overflows the frame because it cannot price the look.
- **Textual graphic device:** THE BHAAV BOARD: an SVG dot-matrix rate board in a brushed-aluminium frame with AAJ and KAL rows at the same price and a gold-light THOK BHAAV offer row; the Naira wordmark as the shop's fascia; one instrument per card; and the F2 card compressed into a counter strip.
- **Motion:** One Kling clip (card 1): the shutter rattles up, the tube light ticks on, the price fields roll like a live rate update and clunk back onto exactly ₹699. Cards 2, 5, 6, 7 and 10 have cheap HTML-only Reels cuts.

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Brushed Gold Huggies | PAIN · SELL | AAJ KA BHAAV. | The shutter rattles up: the pair on a velvet pad under Naira's rate board, AAJ ₹699, KAL ₹699. | yes (Kling 3.0) |
| 2 | Toggle Link Chain | OFFER · SELL | THOK BHAAV. | Top-down V of chain on cocoa velvet; the real sailor ring is the 0 of '20%'. |  |
| 3 | Verdant Eternity Band | OUTCOME · TRUST | BHAAV NAHI KHAATI. | From inside the night safe, looking out: one blade of shop light finds the ring. |  |
| 4 | Verdant Cushion Studs | OUTCOME · EDUCATION | SHAHI LOOK. SAADA BHAAV. | An ear from behind at the counter; the board's LOOK row overflows its frame. |  |
| 5 | Woven Gold Hoops | OFFER · SELL | PALDA BARABAR KARO. | An antique balance: the hoops sink one pan, two ghost slots wait in the other. |  |
| 6 | Serpentine Whisper Chain (gold tone) | OBJECTION · TRUST | TAULO. | The chain coiled wet in a pocket-scale pan; the readout shows the listed 10 g. |  |
| 7 | Tubogas Dome Ring | OBJECTION · TRUST | NAAP SE. | The ring on an upright steel sizing cone; US 6, 7 and 8 ticked with inside diameters. |  |
| 8 | Bougainvillea Vine Bracelet | PAIN · SELL | PHOOL MEHENGE HO GAYE. | The vine loop on a brass pan heaped with marigold petals under a phool-mandi board. |  |
| 9 | Mint Pear Drop Earrings | PAIN · SELL | PAANCH FUNCTION. DO KAAN. | The pair resting on a tuft of cotton wool in an oxblood jeweller's packet. |  |
| 10 | Torsade Huggies | OFFER · SELL | TEEN TOHFE. EK BILL. | The pair standing on a blank carbon-copy bill pad; the torn estimate slip beside it. |  |

Angle mix: PAIN 3 · OUTCOME 2 · OBJECTION 2 · OFFER 3. Layers: EDUCATION 1 · TRUST 3 · SELL 6.

### k10 · PAINTED BIGGEST.

Batches 19 and 20 (`k10a`: cards 1-5, `k10b`: cards 6-10).

- **Jury:** art-5 PAINTED BIGGEST (rank 18, overall 6.81: crazy 6.86 · stop 6.86 · sell 5.86 · brand 8.57 · make 5.86 · stretch 7.86 · ten 6.86).
- **Grafts:** art-4 THE WALL DANCES (rank 17, overall 6.81: crazy 6.00 · stop 7.43 · sell 6.14 · brand 8.00 · make 7.29 · stretch 8.14 · ten 6.86).
- **Idea in one line:** Every ad is a folio from a royal album: the real piece with its real shadow lies on a commissioned miniature where palaces and elephants are fingernail-sized, so by the old painters' rule (hieratic scale) the jewel is the biggest and most important thing in the picture.
- **Why it is 10/10:** Hieratic scale makes the real piece the biggest thing in the picture without enlarging it by a millimetre, and the painted world turns toward it (cranes fly to it, elephants queue at it, windows are lit facing it). A credited living painter makes it culture rather than pastiche, and the riderless baraat whose drums beat by themselves is the heir to the dhol-tasha bracelet the owner loved.
- **Why it sells, and buys three:** Self-worth turned into baskets. Card 5's architecture trilogy (DOME, GATE, WALL at the ear, neck and wrist; three ₹999 pieces) makes BUY3 a building, not a discount; card 10's treasury register has three measured entries already written in and an empty fourth line for BUY4. The folio mark (I of X) tells her there are ten to choose from.
- **What it borrows in thinking from the research:** The owner's dhol-tasha bracelet (the motion) and concept-50's c10 NOT A GIANT HOOP (a true-size piece in a 1:50 model room), turned around: the world is painted small instead of the piece made big. Board #3 ('own the room' under one light) for the most-important-thing idea; Volkswagen's Think Small turned inside out. Graft: art-4 THE WALL DANCES (a commissioned, credited artist and a painted world that moves).
- **What is new:** Ten schools on ten pages, everything in each painting facing the jewel, a jadval border that is a true-millimetre ruler, a folio series I to X, a tracing-paper geometry proof (card 3), footnote daggers as the punchline (card 4), and a gold marker circling the one lit window of hundreds: 'THAT'S YOU.'
- **Textual graphic device:** THE FOLIO: a marbled album border with the jadval ruler, the lobed inscription cartouche for the Velista headline, the hieratic caption ('Old painters drew the most important thing biggest.' plus the real size), hieratic labels (big for the real piece, small for painted things), the F2 cartouche, the collector's seal and the painter's credit.
- **Motion:** Four Reels: Kling on 2 (the baraat walks up the chain, the drums beat, the last firework draws the clasp) and 8 (two shooting stars land exactly on the studs); HTML only on 3 (the tracing paper folds over the axis) and 6 (the marker circles the lit window).

| Card | Piece | Angle · layer | Headline | Picture in one line | Animated |
|---|---|---|---|---|---|
| 1 | Halo Curve Ring | OUTCOME · EDUCATION | SUN AND MOON. | The ring on a Mewar miniature whose sky splits into noon and midnight; the stones are the sun and the moon. |  |
| 2 | Toggle Link Chain | OUTCOME · SELL | THE BARAAT CAME FOR THE CLASP. | The chain as the road a painted riderless baraat walks up to a palace gate. | yes (Kling 3.0) |
| 3 | Verdant Circlet Studs | OBJECTION · TRUST | MADE AS REFLECTIONS. | The studs as a moon and its reflection over a painted Kishangarh lake; a tracing-paper proof. | yes (HTML only) |
| 4 | Molten Panel Bangle | OBJECTION · EDUCATION | PARADISE, WALLED. | The bangle as the wall round a painted Mughal garden, nine elephants queueing outside. |  |
| 5 | Bold Dome Huggies | OFFER · SELL | DOME, GATE, WALL. | The pair standing among a painted golden city's domes; the palace elevation spread. |  |
| 6 | Woven Gold Hoops | PAIN · SELL | NOBODY SAW YOUR EARRINGS. | The pair on a painted facade of hundreds of windows, one lit inside the hoop. | yes (HTML only) |
| 7 | Triple Coil Wrap Bangle | PAIN · EDUCATION | STILL MATCHING TWELVE BANGLES? | A real forearm lying across a painted bangle bazaar like a giant. |  |
| 8 | Quatrefoil Éclat Studs | OUTCOME · EDUCATION | TAARE TOD LAYE. | The studs on painted dunes under a sky of tiny four-point stars. | yes (Kling 3.0) |
| 9 | Petite Square Huggies | OBJECTION · TRUST | ALL FOUR, HOME. | The hoop on the home square of a painted chaupar courtyard. |  |
| 10 | Torsade Pearl Cuff | OFFER · SELL | ALMOST TOUCHING. | The cuff in a painted Bundi garden, its pearls facing like the two pavilions. |  |

Angle mix: PAIN 2 · OUTCOME 3 · OBJECTION 3 · OFFER 2. Layers: EDUCATION 4 · TRUST 2 · SELL 4.

## 7. The layered campaign the ads feed (₹5,000 a day)

The hundred ads are the pool; the campaign takes the best of them after rating (RULINGS §4, framework in `refs/_style/campaign-framework-motivations.png`). The final budget split between prospecting and retargeting, and between the ad sets, is decided after the blind rating, not now.

| Part | Ad sets | Ads | What goes in |
|---|---|---|---|
| Prospecting: one CBO | PAIN · OUTCOME · OBJECTION · OFFER | 4 per ad set (16) | the four top-rated ads of each motivation angle, mixing camps so no ad set is one camp; EDUCATION-layer ads and the strongest Reels lead here |
| Retargeting | TRUST · SELL | rotated from the same camps | TRUST: proof-led cards (lens, replay, scale, register, tracing proof) for people who engaged; SELL: offer-led cards (BUY3 order slips, house rules, four tapes, the palace) for people who visited or added to cart |

**The pool by angle and layer (all 100):**

| Angle | EDUCATION | TRUST | SELL | Total |
|---|---|---|---|---|
| PAIN | 6 | 6 | 13 | 25 |
| OUTCOME | 17 | 7 | 4 | 28 |
| OBJECTION | 7 | 17 | 0 | 24 |
| OFFER | 0 | 0 | 23 | 23 |
| Total | 30 | 30 | 40 | 100 |

**Suggested first wave** (from the selection; every ad still carries this angle in its final bible). It is a starting line-up only: rating replaces any ad that loses.

| Ad set | Ads |
|---|---|
| PAIN | k01-1 Woven Gold Hoops ('AUNTY NE CHASHMA LAGAYA.') · k06-1 Torsade Huggies ('SIRF EK FUNCTION KE LIYE.') · k02-8 Rivière Hoops — Silver ('THE FAST FORWARD.') · k04-1 Woven Gold Hoops ('MUJHE KUCH NAHI CHAHIYE.') |
| OUTCOME | k02-1 Quatrefoil Éclat Studs ('THE STAR FILTER.') · k05-1 Halo Curve Ring ('TWO STONES.') · k07-1 Toggle Link Chain ('BIJLI GAYI. / TOGGLE ON.') · k08-2 Verdant Circlet Studs ('MEHENDI? HAAN.') |
| OBJECTION | k03-1 Verdant Eternity Band ('ROUND ONE: HERS.') · k01-2 Halo Curve Ring ('YEH BROWN WALA KAUNSA HAI?') · k09-6 Serpentine Whisper Chain (gold tone) ('TAULO.') · k05-7 Duo Link Necklace ('SIXTEEN KNOTS.') |
| OFFER | k01-5 Toggle Link Chain ('AUNTY BHI LEGI.') · k06-5 Ribbon Bead Bracelet ('KHATA BAND.') · k03-5 Mint Pear Drop Earrings ('BEST OF THREE.') · k04-5 Triple Coil Wrap Bangle ('AB TUM BHI KEHTI HO.') |

**Retargeting pools:** TRUST (30): k01-1, k01-3, k01-4, k01-7, k01-9, k02-2, k02-4, k02-9, k03-1, k03-4, k03-6, k03-7, k04-7, k04-8, k05-3, k05-4, k05-7, k06-3, k06-6, k07-3, k07-7, k07-9, k08-4, k08-7, k08-9, k09-3, k09-6, k09-7, k10-3, k10-9. SELL (40): k01-5, k01-10, k02-3, k02-5, k02-7, k02-10, k03-5, k03-8, k03-9, k03-10, k04-4, k04-5, k04-9, k04-10, k05-5, k05-6, k05-9, k05-10, k06-1, k06-2, k06-5, k06-9, k06-10, k07-4, k07-5, k07-6, k07-10, k08-5, k08-6, k08-10, k09-1, k09-2, k09-5, k09-8, k09-9, k09-10, k10-2, k10-5, k10-6, k10-10.

**Carousels.** Every camp also has carousel text in its bible: the statics of a camp can run as one carousel in card order (k01 runs as one ten-card wedding night in clock order; k05 splits into two locked-order carousels; k08 adds a retargeting trio of the pieces that finish their own names: हार, अंगूठी, कंगन). Card order stays locked wherever a camp tells a story across cards.

## 8. Allocation: every ad, by piece

| Piece | Price | Stock | Pre-order | Ads | Ad ids |
|---|---|---|---|---|---|
| Woven Gold Hoops | ₹1,049 | 88 | no | 9 | k01-1, k03-2, k04-1, k05-5, k06-6, k07-5, k08-9, k09-5, k10-6 |
| Toggle Link Chain | ₹999 | 77 | no | 9 | k01-5, k02-10, k04-2, k05-6, k06-7, k07-1, k08-1, k09-2, k10-2 |
| Verdant Eternity Band | ₹1,049 | 58 | no | 7 | k01-10, k03-1, k04-3, k05-10, k06-3, k08-4, k09-3 |
| Brushed Gold Huggies | ₹699 | 58 | no | 6 | k02-4, k03-8, k04-4, k06-10, k07-9, k09-1 |
| Triple Coil Wrap Bangle | ₹1,149 | 39 | no | 4 | k03-10, k04-5, k05-3, k10-7 |
| Halo Curve Ring | ₹899 | 27 | no | 3 | k01-2, k05-1, k10-1 |
| Bold Nocturne Bracelet | ₹1,599 | 19 | no | 2 | k07-4, k08-5 |
| Prism Cluster Studs | ₹1,299 | 26 | yes | 3 | k01-8, k07-2, k08-3 |
| Verdant Cushion Studs | ₹1,099 | 30 | yes | 3 | k02-5, k07-3, k09-4 |
| Verdant Circlet Studs | ₹899 | 32 | no | 3 | k01-3, k08-2, k10-3 |
| Charm Box Chain | ₹1,199 | 18 | no | 2 | k03-7, k06-2 |
| Aqua Heart Drops | ₹1,299 | 24 | yes | 2 | k02-2, k07-8 |
| Baroque Shell Bracelet | ₹1,899 | 18 | no | 2 | k01-4, k04-8 |
| Rivière Hoops — Silver | ₹1,499 | 19 | yes | 2 | k02-8, k07-6 |
| Serpentine Whisper Chain — Silver | ₹899 | 23 | no | 2 | k03-6, k08-7 |
| Molten Panel Bangle | ₹999 | 29 | yes | 3 | k04-6, k08-10, k10-4 |
| Baguette Halo Drops | ₹1,199 | 24 | yes | 2 | k01-7, k02-9 |
| Serpentine Whisper Chain (gold tone) | ₹1,299 | 20 | no | 2 | k05-4, k09-6 |
| Torsade Pearl Cuff | ₹1,099 | 23 | yes | 2 | k04-10, k10-10 |
| Quatrefoil Éclat Studs | ₹1,099 | 23 | yes | 2 | k02-1, k10-8 |
| Lilac Papillon Ring | ₹1,199 | 20 | yes | 2 | k02-3, k05-2 |
| Marquise Drop Choker | ₹999 | 24 | no | 2 | k01-9, k08-6 |
| Torsade Huggies | ₹999 | 25 | yes | 3 | k06-1, k08-8, k09-10 |
| Monochrome Enamel Hoops | ₹999 | 24 | no | 2 | k02-6, k06-4 |
| Droplet Open Cuff | ₹1,199 | 14 | no | 1 | k05-8 |
| Bold Dome Huggies | ₹999 | 23 | yes | 2 | k05-9, k10-5 |
| Droplet Open Ring | ₹899 | 20 | no | 2 | k03-3, k06-8 |
| Heartbead Bracelet | ₹999 | 11 | no | 1 | k04-7 |
| Ribbon Bead Bracelet | ₹699 | 21 | no | 2 | k04-9, k06-5 |
| Duo Link Necklace | ₹1,099 | 17 | no | 2 | k01-6, k05-7 |
| Petite Square Huggies | ₹899 | 20 | yes | 2 | k07-10, k10-9 |
| Bougainvillea Vine Bracelet | ₹799 | 11 | no | 1 | k09-8 |
| Tubogas Dome Ring | ₹999 | 16 | no | 2 | k03-4, k09-7 |
| Petite Bow Studs | ₹999 | 16 | yes | 2 | k02-7, k06-9 |
| Mint Pear Drop Earrings | ₹1,049 | 17 | no | 2 | k03-5, k09-9 |
| Marquise Coil Cuff | ₹1,549 | 10 | no | 1 | k07-7 |
| Baroque Bloom Cuff | ₹1,399 | 10 | no | 1 | k03-9 |
| **Total: 37 pieces** | | | | **100** | |

Every piece hits its target exactly, no piece appears twice in one camp, and the silver and gold-tone Serpentine never share a camp (silver in k03 and k08, gold tone in k05 and k09).

## 9. Production process

1. **Twenty batches of five, in order** (table below): `k01a` is k01 cards 1-5, `k01b` k01 cards 6-10, then `k02a` and so on to `k10b`.
2. **One take per picture, plus a hedge take on the riskiest cards** (about two per batch, listed below; each bible's `risk` field says what the hedge changes). k10 card 5's spread reuses the approved plates of k10 cards 2 and 4 for its two side windows, so only its own plate is shot.
3. **The listing photo is reference 1** for every plate, exactly as each prompt says; reference 2 is the card's second ref. The construction lock in each prompt is pasted word for word.
4. **Verify the piece against the listing** before anything is designed: construction (count the stones, pearls, turns, links and knots the lock names), the variant and its tone, the scale against the referent in the prompt, the placement gate, and nothing generated as text, faces or extra jewellery. Count-gated devices (twenty baguettes, four pearls, the mirrored tracing, the size gauge) are printed only if the plate passes.
5. **One redo if it fails**, with the fix written into the prompt; if the redo fails too, use the hedge take, and if that fails, the bible's named fallback (a composite of the verified listing cut-out, or the hedge set-up).
6. **Three designed variations per ad** on the approved plate, all in Feed 4:5 and Story 9:16 from one 9:16 plate: A is the bible's layout as written; B pushes the device or the headline (an alternative beat or headline variant from the bible); C leads with the offer or the proof. Type, palette tokens, the F2 card and safe areas follow each bible and the kit.
7. **Blind rating** of every variation, labels hidden, at 200 px and full size, by award jurors, the performance buyer and the customer panel, scored on **crazy, stop, truth and sell**. Truth is a gate: a variation that breaks a hard rule scores zero whatever else it does.
8. **Pick the best** variation of each ad (and drop an ad that cannot reach the bar rather than ship it).
9. **Animate the planned cards** once their still is approved: 30 through Kling 3.0 from the approved still (the piece held rigid, matted back where the bible says), 7 in HTML or post only. The planned list is in `crazy100.json` (`animated`, and per batch `motionKling` / `motionHtmlOnly`).
10. **Loop note after every batch.** Before the next five run, a short note records what won, what failed and why, and changes the next batch's briefs so the next five are crazier and better (a failed morph becomes a new negative; a winning device is pushed further). The bibles are the start line, not a ceiling.
11. **All remaining credits go into better ads at the end:** re-shoots of near-winners, more variations and more motion for the top-rated cards, and new Reels cuts for the ads the rating puts into the campaign.

| # | Batch | Camp | Cards and pieces | Reels (Kling / HTML only) | Hedge takes |
|---|---|---|---|---|---|
| 1 | `k01a` | k01 AUNTY NE CHASHMA LAGAYA. | 1 Woven Gold Hoops; 2 Halo Curve Ring; 3 Verdant Circlet Studs; 4 Baroque Shell Bracelet; 5 Toggle Link Chain | k01-1, k01-5 / - | k01-4 (eight mismatched pearls and one drop, traced into the line-up); k01-5 (the toggle clasp on an older neck) |
| 2 | `k01b` | k01 AUNTY NE CHASHMA LAGAYA. | 6 Duo Link Necklace; 7 Baguette Halo Drops; 8 Prism Cluster Studs; 9 Marquise Drop Choker; 10 Verdant Eternity Band | k01-7 / k01-10 | k01-7 (exactly twenty baguettes, counted on screen); k01-10 (four aunties' fingertips round one ring hand) |
| 3 | `k02a` | k02 SHAADI KA VIDEO. | 1 Quatrefoil Éclat Studs; 2 Aqua Heart Drops; 3 Lilac Papillon Ring; 4 Brushed Gold Huggies; 5 Verdant Cushion Studs | k02-1, k02-3 / k02-5 | k02-1 (the star outline and the round bokeh); k02-3 (the butterfly's two separate layers) |
| 4 | `k02b` | k02 SHAADI KA VIDEO. | 6 Monochrome Enamel Hoops; 7 Petite Bow Studs; 8 Rivière Hoops — Silver; 9 Baguette Halo Drops; 10 Toggle Link Chain | - / k02-6, k02-10 | k02-8 (a hoop frozen mid-turn); k02-10 (the toggle clasp; the bible asks for three takes) |
| 5 | `k03a` | k03 BEST OF THREE. | 1 Verdant Eternity Band; 2 Woven Gold Hoops; 3 Droplet Open Ring; 4 Tubogas Dome Ring; 5 Mint Pear Drop Earrings | k03-1, k03-3, k03-5 / - | k03-1 (the S-wave inside a milk burst); k03-3 (two hands that must not touch) |
| 6 | `k03b` | k03 BEST OF THREE. | 6 Serpentine Whisper Chain — Silver; 7 Charm Box Chain; 8 Brushed Gold Huggies; 9 Baroque Bloom Cuff; 10 Triple Coil Wrap Bangle | k03-6, k03-10 / - | k03-9 (two hands and two mismatched ends); k03-10 (two turns, never three, on a raised arm) |
| 7 | `k04a` | k04 MUJHE KUCH NAHI CHAHIYE. | 1 Woven Gold Hoops; 2 Toggle Link Chain; 3 Verdant Eternity Band; 4 Brushed Gold Huggies; 5 Triple Coil Wrap Bangle | k04-1, k04-3, k04-5 / - | k04-2 (the toggle clasp between two pairs of hands); k04-4 (two hands pushing one envelope) |
| 8 | `k04b` | k04 MUJHE KUCH NAHI CHAHIYE. | 6 Molten Panel Bangle; 7 Heartbead Bracelet; 8 Baroque Shell Bracelet; 9 Ribbon Bead Bracelet; 10 Torsade Pearl Cuff | k04-6 / - | k04-9 (fingertips from both edges round a 10 mm bow); k04-10 (two hands and the two-row collars) |
| 9 | `k05a` | k05 PARCHHAI. | 1 Halo Curve Ring; 2 Lilac Papillon Ring; 3 Triple Coil Wrap Bangle; 4 Serpentine Whisper Chain (gold tone); 5 Woven Gold Hoops | k05-1, k05-2, k05-5 / - | k05-1 (the tiger eye and the two-figure shadow); k05-3 (two turns on the arm, twelve bangles on the shadow) |
| 10 | `k05b` | k05 PARCHHAI. | 6 Toggle Link Chain; 7 Duo Link Necklace; 8 Droplet Open Cuff; 9 Bold Dome Huggies; 10 Verdant Eternity Band | k05-9 / - | k05-6 (the toggle clasp and its key shadow); k05-7 (sixteen knot connectors; a knot that must not read as a tie) |
| 11 | `k06a` | k06 UDHAAR KHATA. | 1 Torsade Huggies; 2 Charm Box Chain; 3 Verdant Eternity Band; 4 Monochrome Enamel Hoops; 5 Ribbon Bead Bracelet | k06-1, k06-5 / - | k06-1 (the bare print left in the talc); k06-2 (the barrel under a slow shutter) |
| 12 | `k06b` | k06 UDHAAR KHATA. | 6 Woven Gold Hoops; 7 Toggle Link Chain; 8 Droplet Open Ring; 9 Petite Bow Studs; 10 Brushed Gold Huggies | - / - | k06-7 (the toggle clasp inside a petal shower); k06-10 (three hands in one frame) |
| 13 | `k07a` | k07 BIJLI GAYI. | 1 Toggle Link Chain; 2 Prism Cluster Studs; 3 Verdant Cushion Studs; 4 Bold Nocturne Bracelet; 5 Woven Gold Hoops | k07-1, k07-4 / - | k07-1 (the toggle ring hooked on a switch lever); k07-4 (the cupped 'bulb' hand pose) |
| 14 | `k07b` | k07 BIJLI GAYI. | 6 Rivière Hoops — Silver; 7 Marquise Coil Cuff; 8 Aqua Heart Drops; 9 Brushed Gold Huggies; 10 Petite Square Huggies | k07-10 / - | k07-7 (the swan hand and the two-turn coil); k07-10 (four side-wall pearls on an ear from behind) |
| 15 | `k08a` | k08 EK MATRA KI KAMI. | 1 Toggle Link Chain; 2 Verdant Circlet Studs; 3 Prism Cluster Studs; 4 Verdant Eternity Band; 5 Bold Nocturne Bracelet | k08-1, k08-5 / k08-2 | k08-1 (the toggle clasp on a dead-straight strand); k08-2 (a clean card with no henna marks) |
| 16 | `k08b` | k08 EK MATRA KI KAMI. | 6 Marquise Drop Choker; 7 Serpentine Whisper Chain — Silver; 8 Torsade Huggies; 9 Woven Gold Hoops; 10 Molten Panel Bangle | k08-7, k08-10 / - | k08-7 (the snake chain seen through a water film); k08-9 (the turmeric hand and a clean card) |
| 17 | `k09a` | k09 AAJ KA BHAAV. | 1 Brushed Gold Huggies; 2 Toggle Link Chain; 3 Verdant Eternity Band; 4 Verdant Cushion Studs; 5 Woven Gold Hoops | k09-1 / - | k09-2 (the toggle ring as the 0 of 20%); k09-3 (the S-wave under a single blade of light) |
| 18 | `k09b` | k09 AAJ KA BHAAV. | 6 Serpentine Whisper Chain (gold tone); 7 Tubogas Dome Ring; 8 Bougainvillea Vine Bracelet; 9 Mint Pear Drop Earrings; 10 Torsade Huggies | - / - | k09-7 (ridges running up the cone, not round it); k09-9 (the mint pear beside the lowest clear pear) |
| 19 | `k10a` | k10 PAINTED BIGGEST. | 1 Halo Curve Ring; 2 Toggle Link Chain; 3 Verdant Circlet Studs; 4 Molten Panel Bangle; 5 Bold Dome Huggies | k10-2 / k10-3 | k10-2 (the toggle clasp on the painted gate); k10-3 (a true mirrored pair for the tracing proof) |
| 20 | `k10b` | k10 PAINTED BIGGEST. | 6 Woven Gold Hoops; 7 Triple Coil Wrap Bangle; 8 Quatrefoil Éclat Studs; 9 Petite Square Huggies; 10 Torsade Pearl Cuff | k10-8 / k10-6 | k10-7 (two turns on a forearm over the bazaar); k10-9 (exactly four pearls on the side walls) |

### Owner rulings applied before batch 1 (20 Nov 2026)

1. **The shipping line: settled by the owner.** The owner confirmed that free insured shipping and cash on delivery are true on every order and asked for both on every ad (RULINGS §6: "No its true free shipping and all COD, pls mention!"). Every one of the 100 ads therefore carries the trust line "FREE INSURED SHIPPING · CASH ON DELIVERY"; OBJECTION and OFFER ads may use it in the hook and primary text. Any "no free shipping" or switched-off footer slot in a camp bible is overridden by this ruling at production. No ad promises a delivery time.
2. **BUY4 at 30% off: a live code.** BUY2 10% (2+ items), BUY3 20% (3+), BUY4 30% (4+) and NAIRA10 were read live on Shopify on 20 Nov, so the BUY4 lines stay. Re-read the codes on the day of upload.
3. **Price promises.** k09's "Kal bhi yahi" and "one rate all season" are printed only as long as all ten k09 prices are held for the flight; k09-10's "MAKING CHARGE NAHI · WASTAGE NAHI" is true and stays.
4. **Stock floors to re-read at upload:** Marquise Drop Choker gold (15 units, gold only), Triple Coil gold (20), Serpentine gold tone (20, named swap in k05-4), Petite Square (20), Duo Link (17), Baroque Shell (18), Droplet Open Cuff gold (8, rhodium 6), Tubogas gold (US 6, 7, 8 only), Heartbead (11), Bougainvillea violet (10), Marquise Coil Cuff (10), Baroque Bloom (10). No ad prints a scarcity count.
5. **People and rights.** In this run the k10 miniature pages are generated pictures, so no ad names, credits or implies a human painter or a hand-painted commission; a real commission is an option for the owner later. Motion in this run is silent (no voice or music); any sound bed added later is licensed or made for us.
6. **Molten Panel rows.** k04-6, k08-10 and the card lock say five brick-set rows; k10-4 prints no row count because the supplier photos disagree. The verifier counts rows on the reference photos for every Molten Panel picture.

## 10. Files

- `crazy100.json`: the brief, product cards, ranked jury, selection, the ten final bibles exactly as written (every prompt, layout, line of copy, motion plan, risk and truth fix), the 20 batches with hedge takes and motion engines, the allocation by piece and the animated list.
- `CRAZY100.md`: this plan.
- `PLAN.md`: the earlier, tamed plan, kept for the record and marked superseded.
- `RULINGS.md`: the owner's rulings for this run.

