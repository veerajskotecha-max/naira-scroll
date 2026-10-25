# Naira Flore — remote imagery inventory (Shopify CDN + Higgsfield)

Generated 25 Oct 2026. Read-only on every connector: nothing was generated, uploaded, edited or deleted on Shopify or Higgsfield. Feed root: `/tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed/` — `S:` = `assets/shopify/`, `H:` = `assets/higgsfield/`. Machine-readable twin: `research/assets-remote.json` (every image with path, WxH, subject, shot, palette, mood, quality, baked text, cutout, best use).

## What is here

- **Shopify galleries:** 118 handles, 525 files (515 unique CDN URLs, packaging shots are shared) at width 1200, in `S:<handle>/NN.ext`. 102 handles come from `src/data/jewellery.ts` (21) and `jewellerySnapshot.ts` (81); 16 more live pieces exist only in Shopify (see Gaps) and were pulled from the roster's CDN URLs. Every image was viewed on 33 contact sheets (`research/contact-remote/shopify_*.jpg`, 4x4, 300px) and rated.
- **Higgsfield:** one private workspace (basic plan, 66 credits), one empty project ('New folder'), so the archive is the generation history. Paged 2,428 image generations (29 Aug to 25 Oct 2026; all nano_banana_2 2K except 43 background-remover cutouts). By prompt: 1490 editorial/ad plates, 762 listing packshots and worn listing frames, 108 retouch edits, 24 empty sets (product removed), 43 transparent cutouts. All 1,558 editorial, cutout, empty-set and outpaint frames were viewed on 39 triage sheets (`work/hf/triage/t_NN.jpg`, labelled by triage number). **95 were downloaded** at full resolution (1856x2304 for 4:5, 1536x2752 for 9:16, PNG) to `H:` with `H:metadata.json` (job id, date, prompt snippet, aspect, resolution, raw and webp URLs, product, stock, rating). They were rated again on 6 detailed sheets (`research/contact-remote/higgsfield_0N.jpg`).
- **No liked/favourite flags** exist in the history. Prompts never carry campaign names, so campaigns were attributed by date plus a visual match to the Proof Sheet and Contact Sheet descriptions.

## Higgsfield campaign map (where each named world lives)

| World | Date (UTC) | Triage nos. | Read | Status |
|---|---|---|---|---|
| Listing era (cardamom/elaichi props, cube packshots) | 29 Aug – 7 Sep | 1–100 | mostly the photos already in Shopify galleries | reference |
| The Bench (craft tools) | 7 Sep | 101–111 | brass calipers, wax carving | owner reversed the "made on the bench" claim: mood only |
| Pigment (flat colour fields) | 7 Sep | 112–120 | jade, cobalt, chrome yellow, lilac grounds | strong pop, downloaded 113, 117 |
| Sugarplay | 7 Sep | 124–129 | bubblegum, hopscotch, candy stickers | downloaded 124, 125, 126 |
| Keep It On (wet, worn) | 7 Sep + 27 Sep | 130–144, 385–400 | shower, pool, wet hair, sleep | downloaded 132; waterproof claim only for eligible steel pieces |
| I Colour Theory | 11 Sep | 146–151, 164–170 | cobalt, rainbow on yellow, green ink, coral ribbon, magenta/orange | all six downloaded (146 is stock 0) |
| II Slow Burn / The Red Room | 11 Sep + 27 Sep | 152–157, 168–177, 426–427 | cherries, red glass, chilli, onion, wax, oxblood | downloaded 152–154, 156; dark-red grounds |
| III The Pale Hours | 11 Sep | 158–192 | lavender, porcelain, milk, plaster | candidates only (quiet) |
| IV Soft Physics | 11–12 Sep | 185, 257–269 | ring shadow is a flower, hoop braids sage clay | downloaded 261; 185 is the DRAFT Trio Bloom Ring |
| V How It's Worn | 11 Sep + 27 Sep | 193–208, 401–415 | on-model, blush cami; toggle on five skin tones | downloaded 412, 415 |
| VI Soft Matter | 11 Sep | 209–228 | chain carves wax, flowers print pink dots, crepe fan | downloaded 209, 216 |
| VII Clear | 12 Sep | 229–241 | ice, fluted glass, tumblers, droplet lens | downloaded 230 |
| VIII Lilac Hour | 12 Sep | 241–256 | one impossible light per frame | downloaded 242, 243, 245, 247, 249 (Forty suns, stock 0) |
| Lit from within / granulation | 12 Sep | 270–285 | amber glow, pouring granules | downloaded 275 |
| Packaging set (pink NAIRA box) | 15 Sep | 286–329 | box in 40 contexts | downloaded 293 |
| Festive graphics (Paryushan/Diwali) | 15 Sep | 330–340 | marigold toran and diya cutouts, devotional backgrounds | downloaded 330, 331, 334; 337/340 are a real family photo cutout, do not use |
| Background-remover cutouts | 17–27 Sep | 368–384, 557–588 | transparent PNGs, many with props | downloaded 373, 376, 377, 562, 564, 569 |
| Catalogue camps: Apricot / Sage / Lilac | 27 Sep | 432–588 | apricot silk + fruit, celadon crackle + cardamom, lilac wool + lavender | downloaded 432, 448, 456, 479, 503, 519 |
| Graphite (cool grey, steel objects) | 28 Sep | 589–658 | chess king, tiffin, fork, scissors | off the pastel palette; candidates only |
| Sage studio (sewing notions) | 28–30 Sep | 659–695 | spool, thimble, needle, cardamom on deep sage | candidates only |
| Contact Sheet: Hand-Woven / Heartbeat / The Turn / Colour in a Straight Line | 15 Oct | 696–771 | embroidery hoop, ECG, kulhad, haveli door, rangoli stripes, mukhwas | downloaded 697–699, 705, 709, 711, 713, 724, 728, 733 |
| Edition One (witty peach world) | 15–16 Oct | 772–793 | pea pod, jaali, mints, ice tray, strawberry, coupe | downloaded 776–790 |
| Edition Two (Indian-rhyme still lifes) | 16 Oct | 797–825 | mogra, elaichi, anaar, mishri, gathbandhan, Ganga-Jamuni, ghadi, zari, chai channi, jamun | downloaded 797–817 (held plates excluded: mint nimbu, droplet rain, watch, diya, jalebi, north star, kandil) |
| Square listing packshots w/ cardamom | 21 Oct | 826–938 | listing set | reference |
| Object puns (pastel) | 22 Oct | 939–1154 | fruit, mithai, flowers, objects | downloaded 969, 980, 1001, 1074, 1099 |
| Bold cinematic Indian pop | 22 Oct | 1155–1234 | parrot, nimbu-mirchi, cricket, train berth, cherries, sneakers; several dark grounds | downloaded 1157, 1164, 1176, 1191, 1192, 1212, 1214 |
| Pantry / object series (cream) | 23 Oct | 1237–1480 | one piece + one Indian ingredient each | downloaded 1287, 1307, 1373, 1389, 1401, 1443, 1462 |
| Evening accessories + empty sets | 23 Oct | 1481–1541 | clutches, heels, gloves; mostly dark | candidates only |
| Diwali / Bhai Dooj 2026 | 25 Oct | 1543–1558 | rangoli, pomegranate, potlis, toran; some night scenes | downloaded 1544, 1546, 1550, 1554, 1558 |

Not located by name: **Lac & Bone** (no prompt or frame matches; the "Lac & Bone rule" about sand/beige grounds is the only trace) and **Up Close** (its on-model close crops are most likely among the 762 listing-class frames of 17 Sep, 16 Oct and 24–25 Oct, which I did not view one by one; those are the same worn crops now in the Shopify galleries).

## Per-product best images

Packshot = cleanest frame to cut out (`y` = clean separable ground; most house packshots sit on a cream plaster cube, which only cuts out with a matte). On-model prefers the ivory-shirt/editorial frames over the repeated saffron-cami listing crop. Editorial = strongest campaign plate on file (top-40 rank where it has one). Stock is the 25 Oct roster count.

| Handle | Stock | Best packshot (cutout source) | Best on-model | Best editorial plate |
|---|---|---|---|---|
| toggle-link-chain | 79 | `S:toggle-link-chain/01.jpg` (1200x1490, q7) | `S:toggle-link-chain/02.jpg` (896x896, q8) | `H:0713_contact-sheet-the-turn_toggle-link-chain_8004b8b7.png` (1856x2304, q9) #10 · Contact Sheet: The Turn |
| baguette-tennis-necklace *(roster only)* | 70 | `S:baguette-tennis-necklace/01.jpg` (1200x1491, q9) | `S:baguette-tennis-necklace/08.jpg` (1200x1200, q9) | `H:1462_object-series-23-oct_baguette-tennis-necklace_9a5400e0.png` (1536x2752, q9) #17 · Object series (23 Oct) |
| prism-riviere-bracelet | 67 | `S:prism-riviere-bracelet/05.jpg` (1200x1200, q9) | `S:prism-riviere-bracelet/06.jpg` (896x1200, q8) | `H:0699_contact-sheet-colour-in-a-st_prism-riviere-bracelet_5f648330.png` (1856x2304, q9) #1 · Contact Sheet: Colour in a Straight Line |
| woven-gold-hoops | 63 | `S:woven-gold-hoops/01.jpg` (896x896, q9) | `S:woven-gold-hoops/04.jpg` (640x794, q8) | `H:0711_contact-sheet-hand-woven_woven-gold-hoops_96f0685b.png` (1856x2304, q9) #9 · Contact Sheet: Hand-Woven |
| cushion-halo-ring | 60 | `S:cushion-halo-ring/02.jpg` (1200x1607, q8) | — | `H:0147_colour-theory_cushion-halo-ring_8c39c73a.png` (1856x2304, q9) #3 · Colour Theory |
| verdant-eternity-band | 60 | `S:verdant-eternity-band/02.jpg` (896x1200, q8) | `S:verdant-eternity-band/01.jpg` (896x896, q8) | `H:1212_bold-cinematic-22-oct_verdant-eternity-band_c1d9d687.png` (1536x2752, q9) #7 · Bold cinematic (22 Oct) |
| baguette-huggies | 57 | `S:baguette-huggies/02.jpg` (1200x1491, q8) | `S:baguette-huggies/01.jpg` (1200x1491, q8) | `H:1176_bold-cinematic-22-oct_baguette-huggies_a2670bdc.png` (1536x2752, q9) #5 · Bold cinematic (22 Oct) |
| baguette-tennis-bracelet | 57 | `S:baguette-tennis-bracelet/04.jpg` (1200x1491, q9) | `S:baguette-tennis-bracelet/05.jpg` (1200x1491, q8) | `H:0808_edition-two_baguette-tennis-bracelet_5781a8b3.png` (1856x2304, q9) #15 · Edition Two |
| bold-nocturne-chain | 53 | `S:bold-nocturne-chain/01.png` (1200x1200, q9) **y** | `S:bold-nocturne-chain/04.png` (1200x1490, q9) | `S:bold-nocturne-chain/04.png` (1200x1490, q9) #39 |
| bold-nocturne-bracelet | 49 | `S:bold-nocturne-bracelet/01.png` (1200x1200, q9) **y** | `S:bold-nocturne-bracelet/03.png` (896x1200, q8) | `H:0243_lilac-hour_bold-nocturne-bracelet_56fce370.png` (1856x2304, q9) #30 · Lilac Hour |
| halo-curve-ring | 45 | `S:halo-curve-ring/03.jpg` (743x918, q8) | `S:halo-curve-ring/01.jpg` (1150x1348, q8) | `H:0124_sugarplay_halo-curve-ring_6250668c.png` (1856x2304, q9) #4 · Sugarplay |
| kiss-knot-bangle | 40 | `S:kiss-knot-bangle/02.jpg` (1200x1491, q8) | `S:kiss-knot-bangle/01.jpg` (1200x1491, q8) | `H:0809_edition-two_kiss-knot-bangle_eb00c7c3.png` (1856x2304, q9) #16 · Edition Two |
| marquise-layering-set | 40 | `S:marquise-layering-set/01.jpg` (1200x1490, q8) | `S:marquise-layering-set/02.jpg` (1200x1490, q9) | `H:0242_lilac-hour_marquise-layering-set_6969203d.png` (1856x2304, q9) #32 · Lilac Hour |
| silk-mesh-cuff | 40 | `S:silk-mesh-cuff/02.jpg` (1200x1491, q8) | `S:silk-mesh-cuff/05.jpg` (1200x1491, q8) | `S:silk-mesh-cuff/03.jpg` (1200x1491, q9) |
| brushed-gold-huggies | 35 | `S:brushed-gold-huggies/02.jpg` (896x896, q9) | `S:brushed-gold-huggies/01.jpg` (896x1200, q8) | — |
| ribbon-bead-bracelet | 34 | `S:ribbon-bead-bracelet/04.png` (1200x1490, q8) **y** | `S:ribbon-bead-bracelet/03.jpg` (896x1200, q7) | `S:ribbon-bead-bracelet/01.jpg` (640x857, q8) |
| riviere-eternal-bracelet | 34 | — | `S:riviere-eternal-bracelet/01.png` (896x1200, q8) | `S:riviere-eternal-bracelet/02.png` (1200x1490, q9) |
| aqua-heart-drops-silver | 30 | `S:aqua-heart-drops-silver/02.jpg` (1200x1491, q8) | `S:aqua-heart-drops-silver/03.jpg` (1200x1491, q8) | `S:aqua-heart-drops-silver/04.jpg` (1200x1491, q9) |
| baguette-eternity-band | 30 | `S:baguette-eternity-band/02.jpg` (1200x1491, q8) | `S:baguette-eternity-band/04.jpg` (1200x1491, q8) | `S:baguette-eternity-band/01.jpg` (1200x1491, q9) |
| baguette-halo-drops | 30 | `S:baguette-halo-drops/02.jpg` (1200x1491, q9) **y** | `S:baguette-halo-drops/01.jpg` (1200x1491, q8) | `S:baguette-halo-drops/04.jpg` (1200x1491, q9) |
| bold-dome-huggies | 30 | `S:bold-dome-huggies/02.jpg` (1200x1491, q9) | `S:bold-dome-huggies/01.jpg` (1200x1491, q8) | `H:0778_edition-one_bold-dome-huggies_9a6139db.png` (1856x2304, q9) #25 · Edition One |
| lilac-papillon-ring | 30 | `S:lilac-papillon-ring/02.jpg` (1200x1491, q9) | `S:lilac-papillon-ring/03.jpg` (1200x1491, q8) | `H:1214_bold-cinematic-22-oct_lilac-papillon-ring_1dd90fd9.png` (1536x2752, q9) #22 · Bold cinematic (22 Oct) |
| molten-panel-bracelet | 30 | `S:molten-panel-bracelet/02.jpg` (1200x1491, q8) | `S:molten-panel-bracelet/01.jpg` (1200x1491, q8) | `S:molten-panel-bracelet/04.jpg` (1200x1491, q9) #40 |
| pearl-circlet-studs | 30 | `S:pearl-circlet-studs/02.jpg` (1200x1491, q9) | `S:pearl-circlet-studs/03.jpg` (1200x1491, q8) | `S:pearl-circlet-studs/05.jpg` (1200x1491, q9) |
| prism-cluster-studs-silver | 30 | `S:prism-cluster-studs-silver/02.jpg` (1200x1491, q8) | `S:prism-cluster-studs-silver/01.jpg` (1200x1491, q8) | `H:0788_edition-one_prism-cluster-studs-silver_75c3f0d7.png` (1856x2304, q9) #24 · Edition One |
| quatrefoil-eclat-studs | 30 | `S:quatrefoil-eclat-studs/02.jpg` (1200x1491, q8) | `S:quatrefoil-eclat-studs/03.jpg` (1200x1491, q8) | `H:0777_edition-one_quatrefoil-eclat-studs_0d52cc33.png` (1856x2304, q9) · Edition One |
| torsade-pearl-cuff | 30 | `S:torsade-pearl-cuff/02.jpg` (1200x1491, q9) | `S:torsade-pearl-cuff/01.jpg` (1200x1491, q8) | `S:torsade-pearl-cuff/05.jpg` (1200x1491, q9) |
| verdant-cushion-studs | 30 | `S:verdant-cushion-studs/02.jpg` (1200x1491, q8) | `S:verdant-cushion-studs/03.jpg` (1200x1491, q8) | `H:1192_bold-cinematic-22-oct_verdant-cushion-studs_75adce81.png` (1536x2752, q9) #6 · Bold cinematic (22 Oct) |
| torsade-huggies | 29 | `S:torsade-huggies/02.jpg` (1200x1491, q9) | `S:torsade-huggies/03.jpg` (1200x1491, q8) | `S:torsade-huggies/05.jpg` (1200x1491, q8) |
| heartbead-bracelet | 25 | `S:heartbead-bracelet/05.jpg` (1200x1490, q8) | `S:heartbead-bracelet/04.jpg` (1200x1490, q8) | `H:0724_contact-sheet-heartbeat_heartbead-bracelet_f60b5c34.png` (1856x2304, q9) #11 · Contact Sheet: Heartbeat |
| baroque-shell-bracelet | 23 | `S:baroque-shell-bracelet/02.png` (1200x1200, q8) | `S:baroque-shell-bracelet/04.png` (896x1200, q8) | `S:baroque-shell-bracelet/03.png` (1200x1200, q8) |
| serpentine-whisper-chain-silver | 23 | `S:serpentine-whisper-chain-silver/04.webp` (640x797, q8) **y** | `S:serpentine-whisper-chain-silver/01.png` (1200x1200, q8) | `S:serpentine-whisper-chain-silver/03.png` (1200x1200, q9) |
| chain-drop-dome-ring | 22 | `S:chain-drop-dome-ring/02.jpg` (1200x1491, q8) | `S:chain-drop-dome-ring/01.jpg` (1200x1491, q8) | — |
| linked-trio-ring | 22 | `S:linked-trio-ring/02.jpg` (1200x1491, q7) | — | `S:linked-trio-ring/01.jpg` (1200x1491, q8) |
| petite-square-huggies | 22 | `S:petite-square-huggies/01.jpg` (1200x1491, q8) | `S:petite-square-huggies/03.jpg` (1200x1491, q8) | `H:0790_edition-one_petite-square-huggies_b7061a3e.png` (1856x2304, q9) #26 · Edition One |
| riviere-huggies-silver *(roster only)* | 21 | `S:riviere-huggies-silver/01.jpg` (1200x1200, q9) **y** | `S:riviere-huggies-silver/02.jpg` (1200x1200, q9) | `S:riviere-huggies-silver/04.jpg` (1200x1200, q9) |
| charm-box-chain | 20 | `S:charm-box-chain/01.jpg` (1200x1200, q8) | `S:charm-box-chain/02.jpg` (896x1200, q7) | `H:0150_colour-theory_charm-box-chain_93ec0cbd.png` (1856x2304, q8) · Colour Theory |
| droplet-open-cuff | 20 | `S:droplet-open-cuff/02.jpg` (1200x1491, q8) | `S:droplet-open-cuff/01.jpg` (1200x1491, q8) | `S:droplet-open-cuff/03.jpg` (1200x1491, q9) |
| droplet-open-ring | 20 | `S:droplet-open-ring/03.jpg` (1200x1491, q9) | `S:droplet-open-ring/01.jpg` (1200x1491, q8) | — |
| duo-link-bracelet | 20 | `S:duo-link-bracelet/02.jpg` (1200x1491, q8) | `S:duo-link-bracelet/01.jpg` (1200x1491, q8) | `S:duo-link-bracelet/04.jpg` (1200x1491, q9) |
| emerald-square-ear-cuff | 20 | `S:emerald-square-ear-cuff/02.jpg` (1200x1491, q8) | `S:emerald-square-ear-cuff/03.jpg` (1200x1491, q8) | `H:1443_object-series-23-oct_emerald-square-ear-cuff_80aec933.png` (1536x2752, q9) #18 · Object series (23 Oct) |
| fine-tennis-bracelet | 20 | `S:fine-tennis-bracelet/02.jpg` (1200x1491, q8) | `S:fine-tennis-bracelet/01.jpg` (1200x1491, q8) | `S:fine-tennis-bracelet/04.jpg` (1200x1491, q8) |
| marquise-drop-choker | 20 | `S:marquise-drop-choker/02.jpg` (1200x1491, q8) | `S:marquise-drop-choker/01.jpg` (1200x1491, q8) | `S:marquise-drop-choker/04.jpg` (1200x1491, q9) |
| marquise-wheat-cuff *(roster only)* | 20 | `S:marquise-wheat-cuff/01.jpg` (1200x1200, q9) **y** | `S:marquise-wheat-cuff/02.jpg` (1200x1200, q8) | `S:marquise-wheat-cuff/04.jpg` (1200x1200, q9) |
| mint-pear-drop-earrings | 20 | `S:mint-pear-drop-earrings/02.jpg` (1200x1491, q8) | `S:mint-pear-drop-earrings/03.jpg` (1200x1491, q8) | `S:mint-pear-drop-earrings/04.jpg` (1200x1491, q9) |
| north-star-bangle | 20 | `S:north-star-bangle/02.jpg` (1200x1491, q8) | `S:north-star-bangle/01.jpg` (1200x1491, q8) | `S:north-star-bangle/03.jpg` (1200x1491, q8) |
| petal-flower-studs | 20 | `S:petal-flower-studs/02.jpg` (1200x1491, q8) | `S:petal-flower-studs/01.jpg` (1200x1491, q8) | `S:petal-flower-studs/03.jpg` (1200x1491, q9) |
| serpentine-whisper-chain | 20 | `S:serpentine-whisper-chain/02.jpg` (1200x1490, q8) | — | `H:0152_slow-burn_serpentine-whisper-chain_4b9e8c71.png` (1856x2304, q8) · Slow Burn |
| triple-coil-wrap-bangle | 20 | `S:triple-coil-wrap-bangle/02.jpg` (1200x1491, q8) | — | `S:triple-coil-wrap-bangle/01.jpg` (1200x1491, q9) |
| bold-nocturne-drops | 19 | `S:bold-nocturne-drops/02.jpg` (1200x1491, q8) | `S:bold-nocturne-drops/01.jpg` (1200x1491, q8) | `S:bold-nocturne-drops/03.jpg` (1200x1491, q9) |
| garnet-cable-cuff | 19 | `S:garnet-cable-cuff/02.jpg` (1200x1491, q8) | `S:garnet-cable-cuff/01.jpg` (1200x1491, q8) | `S:garnet-cable-cuff/04.jpg` (1200x1491, q9) |
| pear-point-open-cuff | 19 | `S:pear-point-open-cuff/02.jpg` (1200x1491, q8) | `S:pear-point-open-cuff/01.jpg` (1200x1491, q8) | `S:pear-point-open-cuff/04.jpg` (1200x1491, q9) |
| duo-link-necklace | 18 | — | `S:duo-link-necklace/02.jpg` (1200x1491, q8) | `S:duo-link-necklace/01.jpg` (1200x1491, q9) |
| petite-bow-studs | 17 | `S:petite-bow-studs/02.jpg` (1200x1491, q8) | `S:petite-bow-studs/03.jpg` (1200x1491, q8) | `H:0786_edition-one_petite-bow-studs_05acecab.png` (1856x2304, q9) #27 · Edition One |
| mesh-band-ring | 16 | `S:mesh-band-ring/02.jpg` (1200x1491, q8) | `S:mesh-band-ring/01.jpg` (1200x1491, q7) | `S:mesh-band-ring/03.jpg` (1200x1491, q9) |
| baguette-eclat-bracelet | 15 | `S:baguette-eclat-bracelet/02.jpg` (1200x1490, q8) | `S:baguette-eclat-bracelet/03.jpg` (896x1200, q8) | `S:baguette-eclat-bracelet/01.jpg` (640x640, q8) |
| star-point-band | 15 | `S:star-point-band/02.jpg` (896x1200, q8) | `S:star-point-band/01.jpg` (896x1200, q7) | `H:0154_slow-burn_star-point-band_2facc558.png` (1856x2304, q8) · Slow Burn |
| watch-link-ring | 14 | `S:watch-link-ring/02.jpg` (1200x1491, q8) | `S:watch-link-ring/01.jpg` (1200x1491, q7) | `S:watch-link-ring/03.jpg` (1200x1491, q8) |
| birthstone-heart-necklace | 12 | `S:birthstone-heart-necklace/01.jpg` (1200x1491, q8) | — | — |
| crystal-baguette-eternity-ring | 10 | `S:crystal-baguette-eternity-ring/02.jpg` (1200x1491, q8) | `S:crystal-baguette-eternity-ring/01.jpg` (1200x1491, q7) | `S:crystal-baguette-eternity-ring/04.jpg` (1200x1491, q9) |
| crystal-pear-ear-cuff | 10 | `S:crystal-pear-ear-cuff/02.jpg` (1200x1491, q8) | `S:crystal-pear-ear-cuff/03.jpg` (1200x1491, q8) | `S:crystal-pear-ear-cuff/04.jpg` (1200x1491, q9) |
| emerald-deco-hoops | 10 | `S:emerald-deco-hoops/02.jpg` (1200x1491, q8) | `S:emerald-deco-hoops/01.jpg` (1200x1491, q8) | `S:emerald-deco-hoops/03.jpg` (1200x1491, q9) |
| lumiere-oval-bracelet | 10 | `S:lumiere-oval-bracelet/02.png` (1200x1200, q9) | `S:lumiere-oval-bracelet/01.png` (1200x1200, q8) | `S:lumiere-oval-bracelet/03.png` (1200x1200, q8) |
| emerald-halo-c-hoops | 9 | `S:emerald-halo-c-hoops/02.jpg` (1200x1491, q8) | `S:emerald-halo-c-hoops/01.jpg` (1200x1491, q8) | `S:emerald-halo-c-hoops/03.jpg` (1200x1491, q9) |
| golden-duet-ring | 9 | — | — | `S:golden-duet-ring/02.jpg` (1200x1200, q8) |
| bow-pear-drop-necklace *(roster only)* | 5 | `S:bow-pear-drop-necklace/01.jpg` (1200x1491, q8) | `S:bow-pear-drop-necklace/02.jpg` (1200x1491, q7) | `S:bow-pear-drop-necklace/03.jpg` (1200x1491, q9) |
| chevron-whisper-ring | 5 | `S:chevron-whisper-ring/01.jpg` (1200x1200, q8) | `S:chevron-whisper-ring/03.jpg` (896x1200, q7) | — |
| dewdrop-bezel-necklace | 5 | `S:dewdrop-bezel-necklace/03.png` (1200x1490, q8) | `S:dewdrop-bezel-necklace/02.png` (896x1200, q7) | `S:dewdrop-bezel-necklace/04.jpg` (1200x1490, q7) |
| pearl-blossom-earrings | 5 | `S:pearl-blossom-earrings/02.jpg` (1200x1200, q9) | `S:pearl-blossom-earrings/03.png` (896x1200, q8) | `H:0519_catalogue-camp-lilac_pearl-blossom-earrings_240a53f1.png` (1856x2304, q9) · Catalogue camp: Lilac |
| pearl-legacy-necklace | 5 | — | `S:pearl-legacy-necklace/02.png` (1200x1200, q8) | `S:pearl-legacy-necklace/01.png` (1200x1200, q8) |
| pearl-nugget-hoops | 5 | `S:pearl-nugget-hoops/02.jpg` (1200x1491, q8) | `S:pearl-nugget-hoops/01.jpg` (1200x1491, q8) | `S:pearl-nugget-hoops/03.jpg` (1200x1491, q9) |
| pearl-ribbon-ring | 5 | `S:pearl-ribbon-ring/01.jpg` (1200x1200, q9) | `S:pearl-ribbon-ring/02.jpg` (896x1200, q8) | `H:0156_slow-burn_pearl-ribbon-ring_568dbfe1.png` (1856x2304, q9) #38 · Slow Burn |
| petite-blossom-bracelet *(roster only)* | 5 | `S:petite-blossom-bracelet/01.jpg` (1200x1491, q8) | `S:petite-blossom-bracelet/02.jpg` (1200x1491, q7) | `S:petite-blossom-bracelet/03.jpg` (1200x1491, q8) |
| tile-stone-bangle *(roster only)* | 5 | `S:tile-stone-bangle/01.jpg` (1200x1491, q8) | `S:tile-stone-bangle/02.jpg` (1200x1491, q8) | `S:tile-stone-bangle/03.jpg` (1200x1491, q9) |
| verdant-circlet-studs | 5 | `S:verdant-circlet-studs/02.jpg` (1200x1200, q9) | `S:verdant-circlet-studs/01.jpg` (896x1200, q8) | `H:0448_catalogue-camp-sage_verdant-circlet-studs_1320b2d5.png` (1856x2304, q9) · Catalogue camp: Sage |
| vintage-halo-ring | 5 | `S:vintage-halo-ring/01.jpg` (1200x1490, q8) | `S:vintage-halo-ring/03.jpg` (640x794, q8) | — |
| clover-chain-bracelet *(roster only)* | 4 | `S:clover-chain-bracelet/01.jpg` (1200x1491, q7) | `S:clover-chain-bracelet/02.jpg` (1200x1491, q7) | `S:clover-chain-bracelet/03.jpg` (1200x1491, q9) |
| clover-drop-earrings *(roster only)* | 4 | `S:clover-drop-earrings/01.jpg` (1200x1491, q8) | `S:clover-drop-earrings/02.jpg` (1200x1491, q7) | `S:clover-drop-earrings/03.jpg` (1200x1491, q9) |
| granule-dome-ring | 4 | `S:granule-dome-ring/01.jpg` (1200x1200, q9) | `S:granule-dome-ring/02.jpg` (640x794, q8) | `H:0275_lit-from-within_granule-dome-ring_dcb341d4.png` (1856x2304, q9) · Lit from within |
| heartline-paperclip-necklace | 4 | `S:heartline-paperclip-necklace/01.jpg` (1200x1200, q8) | `S:heartline-paperclip-necklace/03.jpg` (896x1200, q8) | — |
| molten-wave-ear-cuff *(roster only)* | 4 | `S:molten-wave-ear-cuff/01.jpg` (1200x1491, q8) | `S:molten-wave-ear-cuff/02.jpg` (1200x1491, q8) | `S:molten-wave-ear-cuff/03.jpg` (1200x1491, q9) |
| pave-zigzag-ring *(roster only)* | 4 | `S:pave-zigzag-ring/01.jpg` (1200x1491, q8) | `S:pave-zigzag-ring/02.jpg` (1200x1491, q7) | `S:pave-zigzag-ring/03.jpg` (1200x1491, q9) |
| pearl-drop-studs | 4 | — | — | `H:0126_sugarplay_pearl-drop-studs_da3b0b8c.png` (1856x2304, q8) · Sugarplay |
| petite-pave-band | 4 | `S:petite-pave-band/02.jpg` (1200x1200, q9) | — | `H:0125_sugarplay_petite-pave-band_1953d3c3.png` (1856x2304, q8) · Sugarplay |
| ribbon-bow-earrings | 4 | `S:ribbon-bow-earrings/01.jpg` (1200x1490, q8) | — | `H:0149_colour-theory_ribbon-bow-earrings_7ed2a8bb.png` (1856x2304, q9) · Colour Theory |
| silver-dome-ring | 4 | `S:silver-dome-ring/01.jpg` (1200x1200, q9) | `S:silver-dome-ring/03.webp` (640x794, q8) | — |
| silver-drop-earrings | 4 | `S:silver-drop-earrings/01.jpg` (1200x1490, q8) | `S:silver-drop-earrings/04.jpg` (1200x1607, q8) | `S:silver-drop-earrings/02.jpg` (1200x1200, q9) |
| asscher-solitaire-ring *(roster only)* | 3 | `S:asscher-solitaire-ring/01.jpg` (1200x1491, q8) | `S:asscher-solitaire-ring/02.jpg` (1200x1491, q8) | `S:asscher-solitaire-ring/03.jpg` (1200x1491, q9) |
| blush-cluster-ring | 3 | `S:blush-cluster-ring/02.jpg` (1179x1443, q8) | `S:blush-cluster-ring/01.jpg` (1200x1200, q8) | — |
| clover-drop-pendant-necklace *(roster only)* | 3 | `S:clover-drop-pendant-necklace/01.jpg` (1200x1491, q8) | `S:clover-drop-pendant-necklace/02.jpg` (1200x1491, q7) | `S:clover-drop-pendant-necklace/03.jpg` (1200x1491, q9) |
| clover-trio-edit | 3 | `S:clover-trio-edit/01.jpg` (1200x1200, q8) | `S:clover-trio-edit/04.jpg` (896x1200, q8) | `H:0245_lilac-hour_clover-trio-edit_226fde22.png` (1856x2304, q9) · Lilac Hour |
| filigree-bloom-studs | 3 | `S:filigree-bloom-studs/02.jpg` (1200x1200, q9) | `S:filigree-bloom-studs/01.jpg` (896x1200, q8) | `H:0216_soft-matter_filigree-bloom-studs_ed788411.png` (1856x2304, q9) · Soft Matter |
| lumiere-oval-solitaire-ring *(roster only)* | 3 | `S:lumiere-oval-solitaire-ring/01.jpg` (1200x1491, q7) | `S:lumiere-oval-solitaire-ring/02.jpg` (1200x1491, q8) | `S:lumiere-oval-solitaire-ring/03.jpg` (1200x1491, q9) |
| pearl-heart-layered-necklace *(roster only)* | 3 | `S:pearl-heart-layered-necklace/01.jpg` (1200x1491, q8) | `S:pearl-heart-layered-necklace/02.jpg` (1200x1491, q8) | `S:pearl-heart-layered-necklace/03.jpg` (1200x1491, q8) |
| pearl-reverie-bracelet | 3 | — | `S:pearl-reverie-bracelet/01.jpg` (1200x1490, q8) | `S:pearl-reverie-bracelet/03.jpg` (640x794, q9) |
| roman-numeral-trio-ring | 3 | `S:roman-numeral-trio-ring/02.jpg` (1200x1491, q8) | `S:roman-numeral-trio-ring/01.jpg` (1200x1491, q8) | `S:roman-numeral-trio-ring/04.jpg` (1200x1491, q9) |
| textured-gold-hoops | 3 | `S:textured-gold-hoops/01.jpg` (1200x1200, q8) | `S:textured-gold-hoops/02.jpg` (896x1200, q7) | — |
| verdant-drop-earrings | 3 | `S:verdant-drop-earrings/02.jpg` (1200x1200, q8) | `S:verdant-drop-earrings/01.jpg` (1200x1490, q9) | `S:verdant-drop-earrings/04.png` (896x1200, q9) |
| whisper-pave-band | 3 | `S:whisper-pave-band/02.jpg` (1200x1200, q9) | `S:whisper-pave-band/01.jpg` (896x1200, q7) | — |
| pearl-point-studs | 2 | `S:pearl-point-studs/02.jpg` (640x640, q8) | `S:pearl-point-studs/04.jpg` (640x794, q9) | `S:pearl-point-studs/01.jpg` (1200x1490, q9) |
| baguette-arc-hoops | 1 | `S:baguette-arc-hoops/02.jpg` (1200x1200, q9) | `S:baguette-arc-hoops/01.jpg` (896x1200, q8) | `S:baguette-arc-hoops/05.jpg` (1200x1490, q8) |
| rose-verdant-band | 1 | `S:rose-verdant-band/03.jpg` (896x1200, q9) | `S:rose-verdant-band/02.png` (1200x1490, q8) | — |
| teardrop-lariat | 1 | `S:teardrop-lariat/02.png` (896x1200, q7) | `S:teardrop-lariat/01.png` (896x1200, q8) | `S:teardrop-lariat/04.png` (1200x1490, q8) |
| twin-heart-necklace *(roster only)* | 1 | `S:twin-heart-necklace/01.jpg` (1200x1491, q7) | `S:twin-heart-necklace/02.jpg` (1200x1491, q7) | `S:twin-heart-necklace/03.jpg` (1200x1491, q9) |
| twin-heart-studs *(roster only)* | 1 | `S:twin-heart-studs/01.jpg` (1200x1491, q7) | `S:twin-heart-studs/02.jpg` (1200x1491, q7) | `S:twin-heart-studs/03.jpg` (1200x1491, q9) |
| baroque-bloom-cuff | 0 | `S:baroque-bloom-cuff/05.jpg` (1200x1490, q9) | `S:baroque-bloom-cuff/04.jpg` (896x1200, q8) | `S:baroque-bloom-cuff/01.jpg` (640x640, q8) |
| baroque-pearl-lariat | 0 | `S:baroque-pearl-lariat/04.jpg` (1161x1388, q9) **y** | `S:baroque-pearl-lariat/03.jpg` (1179x1391, q8) | `S:baroque-pearl-lariat/02.jpg` (1200x1490, q9) |
| blush-station-bracelet | 0 | `S:blush-station-bracelet/02.jpg` (640x640, q8) | — | `S:blush-station-bracelet/01.jpg` (640x794, q9) |
| clover-charm-necklace | 0 | `S:clover-charm-necklace/02.jpg` (896x896, q8) | `S:clover-charm-necklace/01.jpg` (896x1200, q8) | — |
| first-light-set | 0 | `S:first-light-set/01.jpg` (1200x1200, q8) | `S:first-light-set/05.jpg` (896x1200, q8) | `S:first-light-set/07.jpg` (1200x1490, q8) |
| lumiere-oval-necklace | 0 | — | `S:lumiere-oval-necklace/02.png` (1200x1200, q8) | `S:lumiere-oval-necklace/03.png` (1200x1200, q8) |
| molten-bloom-hoops | 0 | `S:molten-bloom-hoops/01.jpg` (1200x1200, q9) | `S:molten-bloom-hoops/06.jpg` (640x794, q9) | `H:0146_colour-theory_molten-bloom-hoops_176960ea.png` (1856x2304, q9) · Colour Theory |
| petite-pearl-chain | 0 | `S:petite-pearl-chain/03.jpg` (896x1200, q7) | `S:petite-pearl-chain/02.jpg` (896x1200, q8) | `S:petite-pearl-chain/04.jpg` (896x1200, q8) |
| riviere-eternal-necklace | 0 | `S:riviere-eternal-necklace/01.jpg` (1200x1200, q8) | `S:riviere-eternal-necklace/02.jpg` (1200x1607, q8) | `H:0249_lilac-hour_riviere-eternal-necklace_cffedacf.png` (1856x2304, q10) · Lilac Hour |
| riviere-of-light-bracelet | 0 | `S:riviere-of-light-bracelet/01.jpg` (1200x1200, q8) | `S:riviere-of-light-bracelet/02.jpg` (896x1200, q8) | — |
| solitaire-whisper-studs | 0 | `S:solitaire-whisper-studs/02.jpg` (896x1200, q8) | `S:solitaire-whisper-studs/01.jpg` (1200x1607, q7) | `S:solitaire-whisper-studs/04.jpg` (1200x1490, q9) |
| triple-dawn-cuff | 0 | `S:triple-dawn-cuff/02.jpg` (1200x1490, q7) | — | `S:triple-dawn-cuff/01.jpg` (1200x1490, q9) |
| tubogas-dome-ring | DRAFT | `S:tubogas-dome-ring/02.jpg` (1200x1491, q8) | `S:tubogas-dome-ring/01.jpg` (1200x1491, q8) | `S:tubogas-dome-ring/03.jpg` (1200x1491, q9) |

## Top 40 editorial plates for the feed

Hand-curated from the 95 downloaded Higgsfield plates and the 515 unique rated Shopify images: in-stock first, one idea per frame, spread across colour worlds (pop brights, pastel, sage/lilac calm, festive red) so either feed option can draw from it. Excluded despite quality: Lilac Hour L1 Forty suns (Riviere Eternal Necklace, stock 0) and Colour Theory C3 molten hoops (Molten Bloom Hoops, stock 0) — brand mood only.

| # | Plate | Product (stock) | Size | Palette | Why it earns a feed slot |
|---|---|---|---|---|---|
| 1 | `H:0699_contact-sheet-colour-in-a-st_prism-riviere-bracelet_5f648330.png` | prism-riviere-bracelet (67) | 1856x2304 | aqua/pink/yellow rangoli powder stripes | Diwali / colour hero: bracelet ruled across aqua-pink-yellow rangoli stripes ('Rangoli, in a line.') |
| 2 | `H:1546_diwali-2026_prism-riviere-bracelet_616187a1.png` | prism-riviere-bracelet (67) | 1536x2752 | ivory, pastel rangoli circle with dots | Diwali morning: the bracelet becomes part of a pastel rangoli circle — cover for a festive carousel |
| 3 | `H:0147_colour-theory_cushion-halo-ring_8c39c73a.png` | cushion-halo-ring (60) | 1856x2304 | chrome yellow, rainbow shadow, rhodium | Colour Theory C5: halo ring throws a rainbow on chrome yellow — loudest clean pop plate |
| 4 | `H:0124_sugarplay_halo-curve-ring_6250668c.png` | halo-curve-ring (45) | 1856x2304 | coral, bubblegum pink, gold, tiger-eye | Bubblegum + statement rings on coral — thumb-stopper with a human mouth, eyes cropped |
| 5 | `H:1176_bold-cinematic-22-oct_baguette-huggies_a2670bdc.png` | baguette-huggies (57) | 1536x2752 | candy pink, cherries on a twig, ruby | Ruby huggies hung like cherries on candy pink — pure pop single |
| 6 | `H:1192_bold-cinematic-22-oct_verdant-cushion-studs_75adce81.png` | verdant-cushion-studs (30) | 1536x2752 | tomato-red ground, pea pod | Emerald studs in a pea pod on tomato red — maximal colour, Indian-kitchen pun |
| 7 | `H:1212_bold-cinematic-22-oct_verdant-eternity-band_c1d9d687.png` | verdant-eternity-band (60) | 1536x2752 | leaf green, Indian ring-neck parrot | Tota (ring-neck parrot) with the emerald band — Indian folk-pop motif, photographic |
| 8 | `H:1001_object-puns-22-oct_verdant-cushion-studs_8f3c1e46.png` | verdant-cushion-studs (30) | 1536x2752 | sage linen, kiwi half — studs as eyes | Kiwi with emerald 'eyes' — meme-able face, humour slot |
| 9 | `H:0711_contact-sheet-hand-woven_woven-gold-hoops_96f0685b.png` | woven-gold-hoops (63) | 1856x2304 | back of head, plait, pink paranda, ivory kurta | Plait with pink paranda + woven hoop ('Woven, twice.') — cultural, intimate |
| 10 | `H:0713_contact-sheet-the-turn_toggle-link-chain_8004b8b7.png` | toggle-link-chain (79) | 1856x2304 | blush linen, terracotta kulhad chai, cardamom | Toggle chain round a kulhad of chai with cardamom — Indian everyday ritual |
| 11 | `H:0724_contact-sheet-heartbeat_heartbead-bracelet_f60b5c34.png` | heartbead-bracelet (25) | 1856x2304 | blush plate, kaju katli star with silver varq | Heartbead on kaju katli with silver varq — mithai / Diwali gifting |
| 12 | `H:0698_contact-sheet-heartbeat_heartbead-bracelet_cd86485b.png` | heartbead-bracelet (25) | 1856x2304 | pink graph paper, red ECG line, steel beads | Heartbead drawn as an ECG on pink graph paper — graphic pun that carries type |
| 13 | `H:0697_contact-sheet-hand-woven_woven-gold-hoops_8f64be6d.png` | woven-gold-hoops (63) | 1856x2304 | blush linen, embroidery hoop, floral stitch | 'Hoop in a hoop' — woven hoops in an embroidery hoop with stitched florals (illustration-adjacent) |
| 14 | `H:0728_contact-sheet-colour-in-a-st_prism-riviere-bracelet_2a263cea.png` | prism-riviere-bracelet (67) | 1856x2304 | blush, bowl of pastel mukhwas | Prism bracelet in a bowl of pastel mukhwas — after-dinner pun |
| 15 | `H:0808_edition-two_baguette-tennis-bracelet_5781a8b3.png` | baguette-tennis-bracelet (57) | 1856x2304 | ivory plaster, ruby baguettes, pomegranate | Ruby baguette tennis + pomegranate (anaar) — festive red on a light ground |
| 16 | `H:0809_edition-two_kiss-knot-bangle_eb00c7c3.png` | kiss-knot-bangle (40) | 1856x2304 | crimson silk dupatta with gold zari, knot | Kiss Knot bangle on a red zari dupatta knot (gathbandhan) — wedding season |
| 17 | `H:1462_object-series-23-oct_baguette-tennis-necklace_9a5400e0.png` | baguette-tennis-necklace (70) | 1536x2752 | emerald Kanjivaram silk with gold zari | Emerald baguette necklace on green Kanjivaram silk with gold zari — heritage richness |
| 18 | `H:1443_object-series-23-oct_emerald-square-ear-cuff_80aec933.png` | emerald-square-ear-cuff (20) | 1536x2752 | ivory, peacock feather | Emerald ear cuff with a peacock feather (mor pankh) — Indian motif, elegant negative space |
| 19 | `H:1389_object-series-23-oct_baguette-huggies_daa15e7c.png` | baguette-huggies (57) | 1536x2752 | cream, green glass bangles | Emerald huggies nested in green glass chudiyan — cultural colour match |
| 20 | `H:1157_bold-cinematic-22-oct_baguette-tennis-bracelet_257a6269.png` | baguette-tennis-bracelet (57) | 1536x2752 | cobalt cloth, French baguette, bread knife | 'Baguette' bracelet on a baguette loaf, cobalt — bold pun |
| 21 | `H:1164_bold-cinematic-22-oct_verdant-eternity-band_683b3644.png` | verdant-eternity-band (60) | 1536x2752 | chrome-yellow wall, teal door, lemon + green chillies | Nimbu-mirchi on a teal door + chrome-yellow wall — street-pop; verify piece fidelity at full size |
| 22 | `H:1214_bold-cinematic-22-oct_lilac-papillon-ring_1dd90fd9.png` | lilac-papillon-ring (30) | 1536x2752 | periwinkle dusk, pink candyfloss (buddhi ke baal) | Butterfly ring on pink candyfloss (buddhi ke baal) at dusk — dreamy pop |
| 23 | `H:0783_edition-one_lilac-papillon-ring_f6db544d.png` | lilac-papillon-ring (30) | 1856x2304 | peach, pink coupe glass, butterfly | Butterfly ring perched on a pink coupe — glam/peach |
| 24 | `H:0788_edition-one_prism-cluster-studs-silver_75c3f0d7.png` | prism-cluster-studs-silver (30) | 1856x2304 | peach, lilac/yellow pastel nails | 'Almost edible.' — lilac/yellow nails matching the cluster studs |
| 25 | `H:0778_edition-one_bold-dome-huggies_9a6139db.png` | bold-dome-huggies (30) | 1856x2304 | blush, pastel ring mints | 'One of these is not a mint.' — dome huggie among pastel mints |
| 26 | `H:0790_edition-one_petite-square-huggies_b7061a3e.png` | petite-square-huggies (22) | 1856x2304 | blush ice-cube tray, ice | 'Cool, squared.' — square huggie in an ice-cube tray |
| 27 | `H:0786_edition-one_petite-bow-studs_05acecab.png` | petite-bow-studs (17) | 1856x2304 | peach, strawberry, hard light | Bow studs on a strawberry — peach pop |
| 28 | `H:0113_pigment_prism-riviere-bracelet_7bea52f2.png` | prism-riviere-bracelet (67) | 1856x2304 | jade green, aqua/pink/yellow pigment cones, rhodium | Prism bracelet across aqua/pink/yellow pigment cones on jade — Holi/gulal bridge |
| 29 | `H:0148_colour-theory_verdant-eternity-band_0d463920.png` | verdant-eternity-band (60) | 1856x2304 | white, glass shelf, emerald ink bloom | Colour Theory C2: emerald ink blooming from the band through glass — surreal clean |
| 30 | `H:0243_lilac-hour_bold-nocturne-bracelet_56fce370.png` | bold-nocturne-bracelet (49) | 1856x2304 | lilac wall, bone shelf, plum band, grey shadow | Lilac Hour L3: the shadow runs on past the chain — graphic, carries type |
| 31 | `H:0247_lilac-hour_halo-curve-ring_8bb891df.png` | halo-curve-ring (45) | 1856x2304 | white, lilac + honey shadows | Lilac Hour L4: two stones swap their coloured shadows |
| 32 | `H:0242_lilac-hour_marquise-layering-set_6969203d.png` | marquise-layering-set (40) | 1856x2304 | bone / lilac split | Lilac Hour L2: the chain holds two rooms apart (bone/lilac) |
| 33 | `H:0261_soft-physics-sage-clay_woven-gold-hoops_efdef672.png` | woven-gold-hoops (63) | 1856x2304 | sage clay, braided imprint | Soft Physics: woven hoop leaves its braid in sage clay |
| 34 | `H:0209_soft-matter_toggle-link-chain_3badd58e.png` | toggle-link-chain (79) | 1856x2304 | blush wax, gold chain cut channel | Soft Matter: chain carves a channel in blush wax — calm pastel breather |
| 35 | `H:0412_how-it-s-worn-ii-skin-tones_toggle-link-chain_07d02e33.png` | toggle-link-chain (79) | 1856x2304 | deep brown skin, ivory strap, gold | Toggle chain on an older woman's deep-brown neck — skin-tone / every-body slide |
| 36 | `H:1554_diwali-2026_baguette-huggies_b70009d6.png` | baguette-huggies (57) | 1536x2752 | ivory, four jewel-colour potli pouches | Four huggie colours with four raw-silk potlis — gifting carousel cover |
| 37 | `H:1373_object-series-23-oct_prism-riviere-bracelet_8d368181.png` | prism-riviere-bracelet (67) | 1536x2752 | powder blue, paper boats | Prism bracelet with paper boats (kaagaz ki kashti) on powder blue — nostalgia |
| 38 | `H:0156_slow-burn_pearl-ribbon-ring_568dbfe1.png` | pearl-ribbon-ring (5) | 1856x2304 | oxblood, red wax seal, gold, pearl | Slow Burn 'Sealed': Pearl Ribbon Ring on a red wax seal (stock 5) |
| 39 | `S:bold-nocturne-chain/04.png` | bold-nocturne-chain (53) | 1200x1490 | white shirt, skin, gold | Editorial on-model: chain at an open white shirt collar, hand at collar (Shopify gallery) |
| 40 | `S:molten-panel-bracelet/04.jpg` | molten-panel-bracelet (30) | 1200x1491 | gold oval plates, full frame | Full-frame gold scale texture — background/pattern plate (Shopify gallery) |

## Cutouts and festive elements ready for compositing

- `H:0330_festive-cutouts_festive-graphic_9008663e.png` (2752x1536, RGBA): transparent CUTOUT diyas+marigold for Diwali collage (16:9 approx 1600x900)
- `H:0331_festive-cutouts_festive-graphic_392fb3e5.png` (2752x1536, RGBA): transparent CUTOUT toran — top-border element for Diwali posts
- `H:0373_cutouts_woven-gold-hoops_28a78fcb.png` (896x1200, RGBA): CUTOUT pair (hoop + flat) for collage
- `H:0376_cutouts_prism-riviere-bracelet_9ad303c6.png` (1856x2304, RGBA): CUTOUT straight bracelet line — collage stripe/ruler
- `H:0377_cutouts_heartbead-bracelet_f066b053.png` (1856x2304, RGBA): CUTOUT heartbead over red tumbler — collage object
- `H:0562_camp-cutouts_toggle-link-chain_98b9ea6c.png` (1536x2752, RGBA): CUTOUT chain + leaf (prop already composed)
- `H:0564_camp-cutouts_prism-riviere-bracelet_65313b73.png` (1536x2752, RGBA): CUTOUT bracelet + lavender sprig
- `H:0569_camp-cutouts_ribbon-bow-earrings_b7c9ea85.png` (1536x2752, RGBA): CUTOUT bows + almond
- Shopify frames on a flat ground (cut cleanly with a simple matte): `S:bold-nocturne-chain/01`, `S:bold-nocturne-bracelet/01`, `S:baroque-pearl-lariat/04`, `S:heartbead-bracelet/03`, `S:ribbon-bead-bracelet/04`, `S:serpentine-whisper-chain-silver/04`, `S:bold-dome-huggies/03`, `S:baguette-halo-drops/02`, `S:riviere-huggies-silver/01`, `S:riviere-huggies-silver/03`, `S:marquise-wheat-cuff/01`, `S:marquise-wheat-cuff/03`
- 35 more transparent background-remover cutouts (apricot, sage-leaf, lavender, almond props; jewellery box; crushed can; seashell; a real family photo that must not be used) are listed with URLs under `higgsfield.all_cutouts` (`downloaded: false`).

## Gaps and cautions

- **16 live pieces are missing from the site data files** (`jewellery.ts` / `jewellerySnapshot.ts`): Baguette Tennis Necklace (stock 70, the best-stocked necklace), Rivière Hoops — Silver (KAVNAR pre-order), Marquise Coil Cuff, Tile Stone Bangle and the 12 pieces added 24–25 Oct (Bow Pear Drop Necklace, Petite Blossom Bracelet, Clover Drop Earrings, Clover Chain Bracelet, Molten Wave Ear Cuff, Pavé Zigzag Ring, Clover Drop Pendant Necklace, Asscher Solitaire Ring, Lumière Oval Solitaire Ring, Pearl Heart Layered Necklace, Twin Heart Necklace, Twin Heart Studs). Their galleries were fetched from the roster URLs and rated. The 12 newest pieces have listing photos only, no campaign plate, and stock of 1–5.
- **Tubogas Dome Ring is in the snapshot but DRAFT in Shopify** (roster with drafts): do not feature it.
- **Best plates on zero-stock pieces:** Forty suns (Rivière Eternal Necklace), Colour Theory C3 and the Red Room/green-organza frames (Molten Bloom Hoops), Baroque Bloom Cuff, Blush Station Bracelet, Lumière Oval Necklace, First Light Set, Baroque Pearl Lariat, Petite Pearl Chain, Rivière of Light Bracelet, Solitaire Whisper Studs, Triple Dawn Cuff, Clover Charm Necklace. Use as brand mood only, never with a price or shop tag.
- **Low stock (≤5) under strong plates:** Ribbon Bow Earrings (4), Pearl Ribbon Ring (5), Clover Trio Edit (3), Filigree Bloom Studs (3), Verdant Circlet Studs (5), Pearl Blossom Earrings (5), Granule Dome Ring (4), Roman Numeral Trio Ring (3), Pearl Drop Studs (4), Petite Pavé Band (4). Re-check stock before posting.
- **Products without a strong editorial plate on file** (best is a listing macro or nothing): heartline-paperclip-necklace, dewdrop-bezel-necklace, textured-gold-hoops, riviere-of-light-bracelet, baroque-bloom-cuff, baguette-eclat-bracelet, chevron-whisper-ring, first-light-set, pearl-legacy-necklace, petite-pearl-chain, baguette-arc-hoops, brushed-gold-huggies, baroque-shell-bracelet, ribbon-bead-bracelet, golden-duet-ring, blush-cluster-ring, rose-verdant-band, vintage-halo-ring, silver-dome-ring, whisper-pave-band, teardrop-lariat, clover-charm-necklace, lumiere-oval-necklace, lumiere-oval-bracelet, torsade-huggies, droplet-open-ring, north-star-bangle, birthstone-heart-necklace, fine-tennis-bracelet, linked-trio-ring, chain-drop-dome-ring, watch-link-ring, petite-blossom-bracelet, pearl-heart-layered-necklace. Several have undownloaded Higgsfield candidates in the JSON (for example Brushed Gold Huggies 449/553/555/1075, Fine Tennis Bracelet 1465 clay court, Ribbon Bead Bracelet 1102, Baroque Shell Bracelet 1315, North Star Bangle 1347, Droplet Open Ring 1351).
- **Nothing illustrated exists remotely.** Every remote asset is photographic. The only graphic elements are kitsch festive backgrounds (334, 333, 336) and two marigold/diya cutouts (330, 331). The maximalist illustrated layer of the reference feed has to be drawn (SVG/CSS), with these photos and cutouts set inside it.
- **Cutout supply is thin.** Only 12 Shopify product frames sit on a clean flat ground; the house packshots (223 of 515) are on a cream plaster cube and need a matte. Eight transparent Higgsfield cutouts were downloaded; 35 more are listed. No local matting model was found in the earlier local sweep.
- **On-model sameness.** 118 of the 153 Shopify worn frames are the same saffron-cami crop on one model; in a grid they read as one photo repeated. The ivory-shirt editorial frames (Bold Nocturne Chain 04, Marquise Layering Set 02, Verdant Drop 01, Baroque Pearl Lariat 03) and the Higgsfield skin-tone series (411–415) are the variety.
- **Dark grounds.** Many 22–23 Oct "bold cinematic" and evening plates sit on black, navy or oxblood (disco ball, piano, boxing glove, gulab jamun, clutches). The owner bans black grounds; they were not selected. Eight Shopify gallery images carry a baked NAIRA wordmark (charm-box-chain/06, silver-drop-earrings/03, petite-pave-band/01 and riviere-eternal-necklace/03 on black; woven-gold-hoops/02 and prism-riviere-bracelet/01 on oxblood; dewdrop-bezel-necklace/04 and ribbon-bow-earrings/07 on light grounds); avoid them as plates.
- **Fidelity checks still owed at full size:** 1164 (nimbu-mirchi, the band is small in frame), 777 (jaali, the stud is small), 705 (haveli door, the chain is small). The owner has caught product errors before.
- **Coverage limits:** the 762 listing-class and 108 retouch-class generations were classified by prompt but not viewed one by one, and nothing before 29 Aug was paged. Higgsfield has no project or folder organisation to lean on. Shopify CDN returned transient 502s; every URL was fetched after retries.
