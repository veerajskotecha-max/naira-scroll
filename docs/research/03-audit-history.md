# Naira — Consolidated Audit History

Compiled 2026-08-19 from five prior Claude-artifact audits. This is a reference file, not a new audit: nothing below was re-verified against the live store or the supplier originals — it is a faithful merge of what the five source documents already said, with cross-references added where two documents talk about the same SKU.

## Source log — all five read in full

| # | Document | URL | Status |
|---|---|---|---|
| 1 | nairaflore.com — SEO Audit | `.../artifact/3694f4ce-ed82-4a3c-9e15-a92a4cd1643e` | Read directly (text fetch) |
| 2 | Naira Petite — Catalogue Fidelity Audit | `.../artifact/e71fdbc4-1002-45ec-adc5-a92a...` `e71fdbc4-1002-45ec-adc5-476e6a00b7e3` | Read directly (text fetch) |
| 3 | Naira Flore · Image Approval | `.../artifact/8fd8f822-958b-4bb3-a139-18e8b444e8be` | Read — page saved to disk (9.7MB, mostly base64 JPEGs), stripped of `<script>`/`<style>`/`data:` URIs, full text recovered |
| 4 | Naira Flore — Frame Review & Catalogue Conflicts | `.../artifact/87bf6e7b-4d53-4b5c-b6a7-161d0524bf57` | Read — same strip method (1.1MB saved HTML) |
| 5 | Naira Petite source verification | `.../artifact/4bbdfda4-4215-436d-84a8-0a82a175ff67` | Read — same strip method (752KB saved HTML) |

Nothing is missing. All five documents' content is reproduced below.

**A note on what "SKU" means here.** None of the five documents use one consistent identifier system. Doc 2 and Doc 5 use supplier codes (`JDB201210`, `WR23024K`, `YF5143`...). Doc 3 and Doc 4 use campaign frame codes (`R01`–`R10`, `W01`–`W10`, `D01`–`D10`, `P01`–`P10`, `S01`–`S10`, `U01`–`U05`) tied to product *names*, not supplier codes. Where I could confidently match a frame code to a supplier SKU (because both appeared against the same product name), I've merged them — this is how several of the disagreements below surfaced. Where I could not confidently match, I've left them separate rather than guess.

---

## 1. Catalogue fidelity defects — consolidated

Every defect below is reproduced from a source document; category tags (Image / Copy / Dimension / Metal tone / Data / Structural) are mine, added for filtering. **Rows marked ⚠ are contradicted by another document — see §1.7.**

### 1.1 Image defects — live and still failing (Catalogue Fidelity Audit, Doc 2)

Doc 2's own header states **63 frames still failing**; the itemised table below sums to **60** (I did the arithmetic; the other 3 aren't accounted for anywhere in the document's text). Reproduced as-is, discrepancy flagged rather than silently fixed.

| Product | SKU (where known) | Frames still live | Files | What's wrong |
|---|---|---|---|---|
| Dewdrop Bezel Necklace | — | 7 | `hf_…809b3b94`, `_1_main`, `_2_worn`, `_3_alt`, `_4_alt`, `_5_alt`, **W03** | Full bezel shown; real setting is a three-prong claw. Product **name** also carries the error. |
| Granule Dome Ring | JDR0104337 | 7 | `hf_…84717213`, `_1_main`, `_2_worn`, `_3_alt`, `_4_alt`, `_5_alt`, **R06** | Every frame invents stones on a stoneless piece (solid gold granulation) and renders the dome solid. |
| Heartline Paperclip Necklace | YF3952 | 4 | `hf_…5e670d00`, `_2_worn`, `_4_alt`, **W06** | Micro-pavé halo added around the heart stations; original is plain milgrain gold bead. |
| Verdant Rivière Bracelet | JDB201210-GN | 4 (all that remains — see §1.6) | 3× `hf_…155118`, **D07** | Centre station dropped, clasp invented, wrong stone cut. |
| Pearl Link Bracelet | — | 4 | 3× `hf_…1011`/`1014`, `_5_alt` | Invented T-bar toggle used as hero; `_5_alt` doubles two pearls, breaking the repeat pattern. |
| Rivière Eternal Necklace | YF7085-NEC | 3 ⚠ | `_1_main`, `_3_alt`, **D02** | Square/princess cut shown instead of round brilliant; buckle station wrong. **Contradicted — see §1.7.** |
| Toggle Link Chain | YF5143 | 3 ⚠ | `hf_…1a9792d2`, `_1_main_v2`, `_3_alt_v2` | "Pavé toggle bar rendered plain"; one frame makes the toggle unable to close. **Direction of this defect is contradicted — see §1.7.** |
| Pearl Blossom Earrings | E20997C ⚠ | 2 | `_1_main_v2`, `_3_alt_v2` | Pearl rendered golden; original is cream. PDP shows two pearl colours at once. **See §1.7 for a differently-worded version of this same defect.** |
| Cushion Halo Ring | WR20902K8 | 2 | `_2_worn`, **D01** | Double halo; original is a single row. |
| Vintage Halo Ring | — | 2 | `_3_alt`, `_4_alt` | Closed conventional halo; original is an interrupted crescent with a polished loop. |
| Molten Bloom Hoops | JDE0110042 | 2 | `_2_worn`, `_3_alt` | Wrong form (open C-hoop, not huggie); mismatched pair. (Silver-tone frames on this SKU were already removed — see §1.4.) |
| Pearl Reverie Bracelet | JDB2409013 | 2 (both remaining frames fail — see §1.6) | `_1_main_v2`, `_2_worn_v2` | Drops the bezel-set green heart zircon; substitutes an invented open gold ring with baroque pearls. |
| First Light Set | JDS0204301-set ⚠ | 2 | `_1_main`, `_4_alt` | Invented split "rabbit-ear" bail; real pendant threads a slider. **Contradicted — see §1.7.** |
| Bold Nocturne Chain | YF5144 | 2 | `_4_alt`, **R10** | `_4_alt` is actually the bracelet, not the necklace; campaign frame invents two toggle bars. |
| Charm Box Chain | YF5146 | 2 | `_3_alt`, **D08** | Companion bead rendered as a letter "G"; campaign frame deletes it entirely. |
| Baguette Arc Hoops | — | 1 | `WE14387B_5_alt` | Closed ring with no ear post — reads as a finger ring. |
| Silver Drop Earrings | E16676C | 1 | **D03** | Suspended from chains with no ear fitting — reads as a pendant. |
| Pavé Initial Chain Drops | — | 1 | **D10** | Shows `E11857B` Star Fall Drops — a different product entirely. |
| Halo Bloom Ring | R15464K | 1 | **W04** | Double halo against a single-row original. |
| Verdant Eternity Band | WR23024K | 1 | `WR23024K_5_alt` | Invents a haloed focal centre stone; original has none. |
| Pearl Ribbon Ring | FR03136B ⚠ | 1 | `FR03136B_2_worn` | Round pavé instead of channel-set squares; pearl moved to centre. **Contradicted — see §1.7.** |
| Golden Duet Ring | JDR0104342 ⚠ | 1 | `JDR0104342_1_main` | Drops the fluted bezel collar and the segmented ribbed shank. **Contradicted — see §1.7.** |
| Silver Dome Ring | JDR0104337-S ⚠ | 1 | `JDR0104337-S_2_worn` | Solid pavé dome; the piece has no stones. **Contradicted — see §1.7.** |
| Baroque Shell Bracelet | YF3925 | 1 | `YF3925_1_main` | Baroque pearl drop missing from the toggle ring. |
| Baguette Éclat Bracelet | JDB201083 | 1 | `JDB201083_3_alt` | Lobster clasp contradicting the box clasp shown in copy and in `_1_main`. |
| Bold Nocturne Bracelet | YF5144-BRA | 1 | `hf_…9c16c4f6` | T-bar toggle substituted for the lobster clasp; extender deleted. |
| Heartbead Bracelet | — ⚠ | 1 | `hf_…0b343d48` | Gold beads inserted into a strand the copy says is uniformly silver. **Contradicted — see §1.7.** |

### 1.2 Image defects — already fixed or partially fixed (Doc 2)

| Product | Status | Detail |
|---|---|---|
| Blush Station Bracelet | Resolved | Both failing frames removed, replaced with two real photographs. Description numbers still wrong (§1.3). |
| Halo Curve Ring | Resolved | All three failing frames removed. Copy still calls it a halo — it's a toi-et-moi bypass (§1.3). |
| Duet of Dawn Ring | Resolved | All four two-tone-shank renders removed; three surviving `hf_` frames all pass. SKU `JDR0104342-PS`. |
| Triple Dawn Cuff | Off sale | Now **DRAFT**, so the phantom triple-layer listing is no longer customer-facing. Its three frames would still show a single hammered cuff if republished. |
| Molten Bloom Hoops | Part-fixed | Three silver-tone frames removed, two real photos added (metal-colour error gone). `_2_worn`/`_3_alt` still fail (§1.1). |
| Vintage Halo Ring | Part-fixed | Four bad frames removed, two real photos added. `_3_alt`/`_4_alt` still fail (§1.1). |
| Silver Dome Ring | Part-fixed | Down to two frames; one passes. `JDR0104337-S_2_worn` still shows an invented pavé dome, and doc 2 states the description "is still wrong at root — it claims stones the piece doesn't have." |
| Brushed Gold Huggies | Part-fixed | Stud frame removed. |
| Blush Cluster Ring | Part-fixed | 12-stone frame removed (dimension error remains, §1.3 count is now 10 not 12). |
| Pearl Ribbon Ring | Part-fixed | Relocated-pearl frame removed — but `FR03136B_2_worn` remains with the same class of defect (§1.1, §1.7). |
| First Light Set | Part-fixed | `D05` wrong-product frame removed. |
| Heartbead Bracelet | Part-fixed | `R09` removed. |
| Golden Duet Ring | Part-fixed | `_2_worn` removed. |
| Baroque Shell Bracelet, Baguette Éclat Bracelet, Toggle Link Chain | Part-fixed | Real photos added to each. |

**One thing moved the wrong way (Doc 2, called out as the most urgent item on the page):**
- **Verdant Rivière Bracelet** (`JDB201210-GN`) — at audit time carried 8 frames: 4 accurate renders (`_1_main`, `_2_worn`, `_3_alt`, `_4_alt`) and 4 wrong ones. **The 4 accurate renders were deleted; the 4 wrong ones were kept.** The page now shows the all-rectangular version with the centre station missing and an invented clasp, in every remaining image.
- **Pearl Reverie Bracelet** (`JDB2409013`) — down to 2 frames, both wrong (green heart zircon dropped, invented open gold ring substituted). No correct image of this bracelet currently exists on its page.

### 1.3 Dimension and copy-vs-piece data errors (Doc 2, "Data errors" table — 21 rows, all still live)

| Product | Field | Listing says | Should say | Category |
|---|---|---|---|---|
| Blush Station Bracelet | Marquise stone | 14mm | 8 × 4mm | Dimension |
| Blush Station Bracelet | Length | 19cm | 18cm | Dimension |
| Bold Nocturne Bracelet | Length | 18cm | 20.5cm | Dimension |
| Bold Nocturne Bracelet | Pavé link | Not mentioned | Signature feature, visible in every frame | Copy (omission) |
| Heartbead Bracelet | Bead size | 6mm | 8mm | Dimension |
| Ribbon Bead Bracelet | Length | Adjustable 16–19cm | Fixed 18cm, no extender | Dimension |
| Rivière of Light / Baguette Éclat | Length | 17.5cm / 16.5cm | 18cm | Dimension |
| Dewdrop Bezel Necklace | Name + setting | "Bezel" | Three-prong claw | Copy / naming |
| Halo Curve Ring | Name | "Halo" | Toi-et-moi bypass, no halo | Copy / naming |
| Pearl Halo Studs | Name | "Halo" | No halo on the piece | Copy / naming (corroborated independently in Doc 5, §4) |
| Classic Solitaire Ring | Prongs | Four-prong | Six-prong | Copy |
| Classic Solitaire Ring | Band | Plain | Stepped pavé shoulder panels | Copy |
| Silver Dome Ring | Stones | "Pavé set across the dome" | No stones — bead mesh | Copy ⚠ (see §1.7) |
| Scatter Light Band | Stones | Baguette + round, irregular | Round only, evenly spaced | Copy |
| Textured Gold Hoops | Stone cut | Round | Marquise, four-petal flowers | Copy |
| Verdant Circlet Studs | Pearls | One, inside the circlet | Two of differing size, set into the ring | Copy |
| Pearl Link Bracelet | Pearl spec | 7mm × 5mm | Seven 5mm pearls (spec misread) | Dimension |
| Pearl Link Bracelet | Construction | Alternating link and pearl | One pearl every two links | Copy |
| Molten Bloom Hoops | Finish | "Rippled molten texture" | High-polish mirror | Copy |
| Ribbon Bow Earrings | Setting | Fine gold claws | Bezel / rail frame | Copy |
| Baguette Arc Hoops | Setting | Flush channel | Bar setting with beaded rails | Copy |

### 1.4 Metal-tone defects

| Product | SKU | What was wrong | Status |
|---|---|---|---|
| Molten Bloom Hoops | JDE0110042 | Three frames rendered the hoops in **silver**; real piece is gold-toned. | Fixed — silver frames removed, two real photos added (Doc 2). Form/pairing defects remain (§1.1). |
| Duet of Dawn Ring | JDR0104342-PS | Copy said "one bezel in cool steel tone and one in warm gold tone" and "two-tone carried down the shank" — puts steel on a bezel. Real piece: cool steel **shank**, both bezels warm gold. Images are correct; only the copy misplaced the tones. | Fixed — copy corrected (Doc 5). |
| Star Point Band | YF5214 | Tagged **Silver Tone** with no gold-plating tag, while the actual order line is the gold colourway `YF5214-Gold-leaf`. | Open (Doc 5, minor). |

### 1.5 Data / metadata defects

See §5 (Catalogue conflicts) for the full 56-item table — handle drift, legacy vendor records, tag vocabulary, missing images, the placeholder SKU, and the broken handle. Not duplicated here to avoid a second copy of the same rows.

### 1.6 Structural / SKU-identity defects (Doc 2, "Structural problems" section)

- **Two SKU codes are swapped — costs money if reordered.** Per the supplier index, `JDB201210` is defined as the **baguette** tennis bracelet and `JDB201083` as the **round** one. On the live store it is reversed: *Rivière of Light* carries `JDB201210` files showing the round design; *Baguette Éclat* carries `JDB201083` showing the baguette design. Reordering against these codes would deliver the wrong bracelets. **This claim is itself contradicted by Doc 5 — see §1.7.**
- **Two SKUs cannot be told apart.** `kav/WR20902K8_1.jpg` and `kav/R15464K_1.jpg` are **byte-identical files**, so *Cushion Halo Ring* (`WR20902K8`) and *Halo Bloom Ring* (`R15464K`) are sold from one photograph with near-identical copy. Doc 2 states this can't be resolved from the source material alone — needs someone who knows what was actually ordered.
- **Petite Pearl Chain has no ground truth.** No original in the supplier photo set, nothing in the PDFs. Its four live frames agree with each other, which the audit explicitly says "is not verification." (Note: Doc 5 separately examined a SKU `YF-DIYChain` also named "Petite Pearl Chain" and found it **is** verifiable and **is** wrong — see §1.7, this may be the same product looked at at two different times with two different reference sets.)

### 1.7 Where documents disagree — flagged explicitly

These are cases where two of the five documents make **incompatible claims about the same SKU**. Both versions are quoted; no attempt is made here to decide which is right.

1. **Rivière Eternal Necklace (`YF7085-NEC`)**
   - Doc 2 (Catalogue Fidelity Audit, "still failing" table): live frames `_1_main`, `_3_alt`, `D02` show **"square/princess cut instead of round brilliant."** Listed as an open, still-failing image defect.
   - Doc 5 (Source verification, "Copy corrected against source, live now"): *"the published necklace images show round brilliant cut stones in individual four claw settings... the copy says 'Square cut clear cubic zirconia'... Images are correct, copy is not."* Listed as **already fixed**, image-side never faulted.
   - These cannot both be true of the same live images at the same time.

2. **Pearl Ribbon Ring (`FR03136B`)**
   - Doc 5 lists it among the **34 SKUs "verified clean against the supplier photo."**
   - Doc 2 lists `FR03136B_2_worn` as a **still-failing live frame**: "round pavé instead of channel-set squares; pearl moved to centre." Doc 2 also separately notes a *different* Pearl Ribbon Ring frame (the "relocated-pearl frame") was already removed — meaning Doc 2's own account is that this SKU had a relocated-pearl problem, partially but not fully fixed. Doc 5's "clean" verdict does not match either state.

3. **Heartbead Bracelet**
   - Doc 5 lists it among the 34 "verified clean" SKUs.
   - Doc 2 lists `hf_…0b343d48` as still failing ("gold beads inserted into a strand the copy says is uniformly silver") and separately flags a bead-size dimension error (6mm listed vs 8mm actual, §1.3).

4. **Golden Duet Ring (`JDR0104342`)**
   - Doc 5 lists it among the 34 "verified clean" SKUs.
   - Doc 2 lists `JDR0104342_1_main` as still failing: "drops the fluted bezel collar and the segmented ribbed shank."

5. **Silver Dome Ring (`JDR0104337-S`)**
   - Doc 5 lists it among the 34 "verified clean" SKUs.
   - Doc 2 lists it as still failing in three separate places: the "still failing" image table (`JDR0104337-S_2_worn`, invented pavé dome), the data-errors table (copy claims pavé stones on a stoneless piece), and the "already fixed" cards ("the description is still wrong at root").

6. **First Light Set (`JDS0204301-set`)**
   - Doc 5: *"Images match the supplier photo"* — only the stone-size copy (both stones called "approximately 4mm") is wrong, and understated.
   - Doc 2: live frames `_1_main` and `_4_alt` **invent a split "rabbit-ear" bail** that the real pendant does not have (real pendant threads a slider) — an image defect, not just a copy one.

7. **Toggle Link Chain (`YF5143`)** — the two documents describe the *same class* of defect (a toggle bar shown with pavé it shouldn't have, or without pavé it should have) but **in opposite directions**:
   - Doc 5: *"Supplier photo shows the... toggle bar as plain polished gold with no stones anywhere on the piece. Every published image... adds a clear pavé cubic zirconia band on the toggle bar... Copy correctly says gold toggle bar and ring, no stone claimed."* → real = plain, images = wrongly show pavé.
   - Doc 2: *"Pavé toggle bar rendered plain; one frame makes the toggle unable to close."* → read literally, this says the pavé toggle bar is *rendered as plain* in the image, i.e. images are missing pavé they should have.
   - One of these has the direction backwards; reproduced verbatim rather than resolved, since getting the direction wrong would send a reshoot the wrong way.

8. **Pearl Blossom Earrings (`E20997C`)** — both documents flag a pearl-colour problem, but describe it differently:
   - Doc 2: pearl "rendered golden; original is cream."
   - Doc 5: supplier pearl is "warm champagne/peach tone"; listing renders "neutral white/ivory" and copy calls it "round white freshwater pearl."
   - Same defect class (pearl colour infidelity), not the same specific colours on either end — likely two passes at different times, but the "true" colour is stated three different ways across the two documents (cream / champagne / peach) and the "wrong" colour two different ways (golden / white).

9. **`JDB201083` identity** (feeds into the swap claim in §1.6):
   - Doc 5: *"Wrong product entirely. The supplier photo is a fine gold cable chain bracelet with a single tiny open circle of pave stones as its only motif."* Listed live under this SKU: a full baguette CZ tennis bracelet. Doc 5's own severity tag is "major, fix: both" — i.e. Doc 5's position is that `JDB201083` was never a tennis-bracelet code at all.
   - Doc 2: treats `JDB201083` as legitimately a tennis-bracelet SKU ("the round one" per the supplier index) that has simply had its photo files swapped with sibling `JDB201210` ("the baguette one"). This assumes a shared tennis-bracelet identity for both codes that Doc 5 does not support.
   - These readings of what `JDB201083` is *supposed to be* are not reconcilable as written.

10. **`JDB201210` identity** (the other half of the same swap claim):
    - Doc 5: **"Cannot be verified against source."** *"The supplier reference is a stacked wrist shot containing eight or nine different bracelets... No single item is identifiable as this SKU... Needs a single product photo from the supplier."*
    - Doc 2's swap claim in §1.6 asserts `JDB210210`'s identity ("the baguette one") as settled fact. Doc 5 says the same code's ground truth is currently **unknowable** from the available supplier material. The swap claim in §1.6 is therefore resting on an identification that Doc 5 says cannot actually be made.

11. **Internal inconsistency inside Doc 2 itself** (not cross-document, but worth carrying forward): the stat block claims **63** frames still failing; the itemised table beneath it sums to **60**. Also, the stat block claims **3 SKUs failing on draft**, but the document's visible text only names one draft SKU (Triple Dawn Cuff, §1.2) — the other two are not identified anywhere in the retrievable text.

---

## 2. Every image ever approved or rejected

Two documents cover this. **Doc 3 (Image Approval)** is the *proposal* stage of one 55-frame campaign shoot: every frame defaults to "Keep," with a one-line curatorial reason, and an explicit instruction — *"Say nothing and all 55 go up."* It is not itself a record of rejections; it's the ballot, not the result. **Doc 4 (Frame Review & Catalogue Conflicts)**, dated 8 Aug 2026, is the *outcome* of that same 55-frame shoot: **45 pushed live, 10 cut.** Frame codes match 1:1 between the two documents, which lets the reason for each rejection be recovered.

### 2.1 The outcome, roll by roll

| Roll | Frames | Result |
|---|---|---|
| I — The Red Room (oxblood/red glass) | R01–R10 | **All 10 pushed** |
| II — Still Water (botanical/water) | W01–W10 | **All 10 pushed** |
| III — After Dark (black ground, gifting) | D01–D10 | **All 10 pushed** |
| IV — Not a Phase (saturated colour blocks) | P01–P10 | **All 10 cut — entire roll pulled** |
| V — Softly, Slowly, Worn (Indian craft materials) | S01–S10 | **All 10 pushed** |
| Worn by You (UGC, phone-shot) | U01–U05 | **All 5 pushed** |

**The stated rejection reason (Doc 4), verbatim:** *"Frame P02 places a bracelet inside a hospital IV saline bag — reads as a medical drip, not jewellery. Whole roll pulled."* P02's own one-line description in Doc 3 confirms this: **"Suspended in a drip bag of liquid gold"** (SKU `YF6667`). Only P02 itself is described as having the actual problem; P01 and P03–P10 were cut as a bloc alongside it, not for individually-documented defects of their own. Doc 4 does not give a separate reason for each of the other 9 — reproducing that gap here rather than inventing reasons for them.

### 2.2 Full frame register (product / SKU cross-referenced from Docs 3 + 4)

| Code | SKU | Product (Doc 4 name) | Doc 3's one-line reason | Outcome |
|---|---|---|---|---|
| R01 | E20267O | Woven Gold Hoops | Wet oxblood dome. The strongest single frame of the set. | Pushed |
| R02 | WR23024K | Emerald / Verdant Eternity Band | Red glass bangles glowing behind the silver. | Pushed |
| R03 | B00681C | Prism Rivière Bracelet | Standing water, full mirror reflection. | Pushed |
| R04 | FR03136B | Pearl Ribbon Ring | Burgundy silk glove on bone white. | Pushed |
| R05 | E16355C | Solitaire Whisper Studs | Split pomegranate; a seed proves the scale. | Pushed |
| R06 | JDR0104337 | Amber / Granule Dome Ring | Macro on oxblood velvet, every granule in relief. | Pushed — but see §1.1: this same SKU's live listing carries other frames judged still-failing. |
| R07 | YF8439 | Serpentine Whisper Chain | Poured over a lacquer edge, copy space right. | Pushed |
| R08 | E19263B | Pearl Point Studs | Ear crop, crimson silk bouncing onto the jaw. | Pushed |
| R09 | YF5215 | Heartbead Bracelet | Wrist on oxblood silk. | Pushed |
| R10 | YF5144 | Bold Nocturne Chain | Graphic hero. | Pushed — sibling SKU `YF5144-BRA` (Bold Nocturne Bracelet) has its own open image defect, §1.1. |
| W01 | E21572E1 | Emerald / Verdant Drop Earrings | Hung from the curl of a calla lily stem. | Pushed |
| W02 | WE24089B | Pearl Halo Studs | Cradled in a bruised magnolia petal. | Pushed |
| W03 | YF6403 | Dewdrop Bezel Necklace | Half submerged; the waterline refracts it. | Pushed — same SKU has 7 still-failing frames listed in §1.1. |
| W04 | R15464K | Halo Bloom Ring | Hand and reflection meeting on still water. | Pushed — same SKU flagged as duplicate/byte-identical photo with Cushion Halo Ring, §1.6. |
| W05 | E16075B | Ribbon Bow Earrings | Backlit lotus petal glowing translucent. | Pushed |
| W06 | YF3952 | Heartline Paperclip Necklace | Wet slate, stations holding water beads. | Pushed — same SKU has 4 still-failing frames, §1.1. |
| W07 | WR10914B2 | Blush Halo / Blush Cluster Ring | Garden-rose petals, blush on blush. | Pushed |
| W08 | FE02847B | Emerald / Verdant Circlet Studs | Nested in the channel of a curled leaf. | Pushed |
| W09 | YF8457 | Tassel Nocturne Necklace | The pearl touching water. One ring of ripple. | Pushed |
| W10 | JDR0104333 | Trio Bloom Ring | Threaded onto a stem below an unopened bud. | Pushed |
| D01 | WR20902K8 | Cushion Halo Ring | Floating between two glowing discs. | Pushed — duplicate-photo flag, §1.6. |
| D02 | YF7085-NEC | Rivière Eternal Necklace | Draped over a champagne coupe. | Pushed — see the contradiction at §1.7 item 1. |
| D03 | E16676C | Silver Drop Earrings | Suspended in a cool spot, black all round. | Pushed — same SKU has an open no-ear-fitting defect, §1.1. |
| D04 | WR19333K8 | Classic Solitaire Ring | One hard shaft, dust in the beam. | Pushed |
| D05 | YF8396 | Teardrop Lariat (was "Pearl Ceremony Set") | Falling through the dark, beads rim-lit. | Pushed |
| D06 | E14776S | Brushed Gold Huggies (was "Golden Nugget Studs") | Mirror-black basalt, satin grain in relief. | Pushed |
| D07 | JDB201210-GN | Verdant Rivière Bracelet | Champagne glowing through green baguettes. | Pushed — this is one of the 4 frames that now make up 100% of this product's (wrong) live imagery, §1.2. |
| D08 | YF5146 | Charm Box Chain | One dead-straight vertical line. | Pushed — same SKU has 2 still-failing frames, §1.1. |
| D09 | WR12518B | Petite Pavé Band | Extreme macro in a raking beam. | Pushed |
| D10 | E11857B | (listed as "pave star chain drops") | Two stars caught having just stopped swinging. | Pushed — per §1.1, Doc 2 states this exact file is being shown on the *Pavé Initial Chain Drops* product page, where it is a different product (actually Star Fall Drop Earrings). |
| P01 | JDE0110042 | (Molten Bloom Hoops) | Green on green; a butterfly vanishing into the field. | **Cut** (whole-roll pull) |
| P02 | YF6667 | — | Suspended in a drip bag of liquid gold. | **Cut — the stated reason** (reads as medical IV drip) |
| P03 | WR22648B7 | — | Magenta colour block, hand from directly above. | **Cut** (whole-roll pull) |
| P04 | E20997C | Pearl Blossom Earrings | Held weightless inside a soap bubble. | **Cut** (whole-roll pull) — same SKU has an open pearl-colour defect, §1.1/§1.7. |
| P05 | YF5143 | Toggle Link Chain | The chain IS the horizon between sage and cream. | **Cut** (whole-roll pull) — same SKU has open, direction-disputed pavé defect, §1.1/§1.7. |
| P06 | JDS0204301-set | First Light Set | An eclipse; the stone sits dead centre and fires. | **Cut** (whole-roll pull) |
| P07 | YF6671 | — | Slipped over a travertine column. | **Cut** (whole-roll pull) |
| P08 | E14066B | — | Sage block, curb chain caught mid-swing. | **Cut** (whole-roll pull) |
| P09 | WR23569K8 | — | Tilted to an ellipse, orbiting an arc of light. | **Cut** (whole-roll pull) |
| P10 | YF8156 | — | Draped along a ribbon of silk twisting in air. | **Cut** (whole-roll pull) |
| S01 | E20267O | "sage hero" | Category authority. Colour-block hero, copy shelf across the top. | Pushed |
| S02 | YF6403 | "blush hero" | A/B pair to shot 1. The chain's V opens a copy well. | Pushed |
| S03 | E19263B | "ear" | Face cropped so the viewer sees her own ear. | Pushed |
| S04 | YF8439 | "throat" | Collarbone crop; the gold is the only saturated thing. | Pushed |
| S05 | FR03136B | "hand" | Scale proof. The bow stops at the edges of the finger. | Pushed |
| S06 | WR23024K | "cardamom" | A cardamom pod donates its size so 5mm reads. | Pushed |
| S07 | YF3925 | "khadi" | The weave dents under the pearls' weight. | Pushed — Baroque Shell Bracelet, same SKU has an open defect on a different frame (`YF3925_1_main`, §1.1). |
| S08 | JDR0104337 | "terracotta" | Clay holds a negative imprint, every granule a crater. | Pushed |
| S09 | JDB201083 | "jaali" | The one Indian cue, and it is material not motif. | Pushed — this is the SKU at the centre of the swap dispute, §1.6/§1.7. |
| S10 | WE24089B | "paper" | True overhead, half the sheet empty for a headline. | Pushed |
| U01 | YF6667 | "wrist bracelet" | Bed linen, window light, phone half out of frame. | Pushed — same SKU as the P02 IV-bag frame, different shot, kept for the UGC set. |
| U02 | E20267O | "ear hoops" | Ear and jaw crop. Unretouched skin carries it. | Pushed |
| U03 | WR20902K8 | "box ring" | The pink box open on a scratched table. No cards. | Pushed |
| U04 | YF6403 | "neck necklace" | Collarbone, warm lamp against a cold doorway. | Pushed |
| U05 | E19263B | "palm studs" | Studs loose in a palm, scale correct against a finger. | Pushed |

All 55 frames were shot at 1856 × 2304. Doc 3 notes this is materially larger than "the soft 896 × 1200 heroes still sitting on about forty live listings" — i.e. roughly 40 live product pages were, at the time of this document, still running lower-resolution hero images than what this shoot produced. Doc 3 also pre-empts a specific confusion: **"There is no green velvet set."** The emerald velvet ground was designed for the shoot and never used; any green the reader might recall is either the sage chair behind the 20 bracelet worn-frames, or an unrelated low-resolution model shot already live on the site.

### 2.3 Recurring failure modes (image rejections/defects, pooled across Docs 1–5)

The only *process* rejection recorded (§2.1) is narrow — one prop choice reading as medical equipment. The much larger body of image rejection reasoning lives in the fidelity audit (§1) and source verification (§4). Pooling all of it, the same handful of failure modes recur constantly:

1. **Invented ornamentation** — stones, halos or pavé added to a piece that doesn't have them. *Granule Dome Ring, Heartline Paperclip Necklace, Cushion Halo Ring, Halo Bloom Ring, Verdant Eternity Band, Silver Dome Ring, Toggle Link Chain (disputed direction, §1.7), Star Point Band, Verdant Drop Earrings.*
2. **Wrong stone cut/shape rendered** — round shown as square/princess or vice versa, faceted shown for opaque. *Rivière Eternal Necklace (disputed, §1.7), Prism Rivière Bracelet, Verdant Rivière Bracelet, Halo Curve Ring (tiger eye rendered as faceted crystal).*
3. **Wrong metal tone** — silver rendered for gold. *Molten Bloom Hoops (fixed), Star Point Band (tag mismatch, open).*
4. **Wrong stone/pearl colour** — *Pearl Blossom Earrings (two different colour accounts, §1.7), Verdant Drop Earrings (teal vs turquoise), Pearl Reverie Bracelet (zircon dropped entirely).*
5. **Wrong clasp / setting / construction** — *Verdant Rivière Bracelet (clasp invented), Baguette Éclat Bracelet (lobster vs box clasp), Bold Nocturne Bracelet (toggle substituted, extender deleted), Dewdrop Bezel Necklace (bezel vs claw), Pearl Ribbon Ring (disputed, §1.7), First Light Set (disputed, §1.7), Toggle Link Chain (won't close in one frame).*
6. **Wrong product under a SKU** — *Baguette Éclat Bracelet / `JDB201083` (per Doc 5), Petite Pearl Chain / `YF-DIYChain`, Clover Charm Necklace / `YF6618`, Pavé Initial Chain Drops showing `E11857B` Star Fall Drops.*
7. **Duplicate photography across two different SKUs** — *Cushion Halo Ring and Halo Bloom Ring share one byte-identical file.*
8. **Unintended real-world visual association** — a styling/prop choice reading as something other than jewellery. *Roll IV / P02, the IV-saline-bag frame — the only fully-documented rejection in this corpus.*
9. **Alt text describing a hallucinated render, not the real piece** — see §5.4.

---

## 3. SEO findings (nairaflore.com, Doc 1 — audit run 18 Aug 2026)

### 3.1 Scores

| Category | Score |
|---|---|
| Overall (weighted across measured categories only) | **39** |
| Technical SEO | **40** |
| AI search readiness | **27** |
| Schema | **45** |
| Performance / mobile | **74** |

Content quality and image optimisation were **not audited** and are excluded from the overall score rather than estimated.

### 3.2 The root-cause finding

**Every URL on the site serves byte-identical HTML.** Home page, product page, collection page, and a journal article were fetched and diffed — all identical, all 3,698 bytes, and every one declares the same canonical:
```
<title>Naira Flore | Indo-Western Wear & Demi-Fine Jewellery</title>
rel="canonical" href="https://nairaflore.com/"
og:url" content="https://nairaflore.com/"
```
All 100 sitemap URLs therefore tell non-rendering crawlers they canonicalise to the homepage — a sitewide duplicate-content declaration. `react-helmet-async` rewrites the title post-hydration, but Google favours the HTML-declared canonical when the two disagree.

**Ten crawlers, zero words.** Real user-agents for `ccbot`, `claudebot`, `chrome-browser`, `bingbot`, `googlebot`, `oai-searchbot`, `perplexitybot`, `google-extended`, `gptbot`, and `chatgpt-user` were all fetched — all returned HTTP 200, 3698 bytes, `sha256=1e29c544130c` — identical. Body text: `''`. Word count: 0. Heading tags h1–h6: 0. `<p>` tags: 0. The entire body is `<div id="root"></div>`. 31 category landing pages and 19 journal articles of "genuinely good, FAQ-rich copy" are invisible to ChatGPT, Perplexity, Claude, and Common Crawl. Googlebot/Bingbot render JS but on a deferred budget. One positive: identical bytes to every UA tested means **no cloaking**.

**Any invented URL returns HTTP 200.**
```
/jewellery/this-product-does-not-exist-xyz123  →  200, 3698 bytes
/Jewellery                                     →  200
/jewellery/definitely-not-real-xyz             →  200
/sitemap_index.xml                             →  404   ← the CDN CAN 404
```
This is the SPA catch-all rewrite serving 200 for everything under the app. Combined with the homepage-canonical finding, every typo and every crawler-invented URL becomes a soft-404 claiming to be the homepage.

**A documented self-correction inside this same audit:** the author states they had earlier told the user the audit's 404 claim was *"factually false"* because `/jewellery/:handle` exists as a route. On rechecking: the route exists but the data behind it doesn't. **The live sitemap lists 39 `/jewellery/<product>` URLs, and zero of them resolve** — the sitemap carries Shopify-style handles like `cuban-pearl-bracelet`, while `jewellery.ts` (a hardcoded array, separate from the Shopify catalogue covered in §1–§5) holds 22 pieces all named things like `the-vow`, `the-halo`, so `JewelDetail.tsx:117` bounces every one of them to `/jewellery`. The audit's original claim was right; the mid-conversation "correction" was wrong. Reproduced here because it's a real example of the corpus disagreeing with itself, not just across documents.

### 3.3 Already fixed and committed during this audit

1. **Duplicate Organization JSON-LD node** — self-introduced bug. `index.html` already carried a static Organization block; a second, richer `organizationLd` node was added to `Index.tsx` without checking the static HTML first. `react-helmet-async` can't merge with or remove a block baked into the HTML, so the next deploy would have shipped two conflicting Organization nodes. Removed, with a comment recording why it must not return.
2. **Product availability hardcoded to `InStock`** — the fetched product already carried `availableForSale`; it just never reached the markup, so sold-out SKUs told Google they were buyable. Fixed.
3. **`Product.image` was missing entirely** — required by Google for product rich results, so none of the Shopify-backed pages were eligible. Fixed (URLs were already being fetched for the OG tag).
4. **Markup published a price the page deliberately hides** — `JewelDetail.tsx` emitted `piece.price` in its Offer, while `jewellery.ts` marks that field "internal record only; not displayed during pre-order" and the page itself shows "Price shared on WhatsApp enquiry." Removed; `PreOrder` availability state (correct for the WhatsApp-only line) stays.
5. **Organization logo pointed at a `.ico`** — Google requires JPG/PNG/WEBP. Repointed at `public/logo.png`.

### 3.4 Still open

- **High — `llms.txt` describes a different business.** Well-formed, but describes Naira Flore as a *"Nashik-based atelier specializing in personalised, hand-crafted Indian couture… intricate zardosi, thread and embellishment work on premium silks"* — a bridal-couture description. 71 of the site's 100 indexed URLs are jewellery, and the site's own JSON-LD says "Indo-Western wear and gold finished demi-fine jewellery." `llms.txt` links only 9 utility pages and none of the 31 category or 19 journal pages.
- **High — three surfaces describe three different businesses:**

  | Surface | Says the business sells |
  |---|---|
  | `llms.txt` | Luxury couture — lehengas, sarees. Jewellery unmentioned. |
  | `Footer.tsx` tagline | "Indo-Western fashion, handcrafted for the modern woman." Leads with Dresses, Co-ord Sets, Fusion Sarees; jewellery unmentioned. |
  | Server-rendered JSON-LD | "Indo-Western wear and gold finished demi-fine jewellery." |
  | The actual sitemap | 71 of 100 URLs are jewellery. |

  The footer's clothing categories route to `/shop?category=X`, which appears nowhere in the sitemap — the clothing line the footer foregrounds has no crawlable page at all.
- **High — no CSP, no X-Frame-Options** on a checkout site. HSTS, `nosniff`, `referrer-policy` are correctly set. No clickjacking protection, no restriction on injected script/frame sources, despite the site's own meta description promising "secure checkout."
- **Medium — three quick wins at the edge:** `www → apex` redirects **302, not 301** (the HTTP→HTTPS hop is correctly 301, so this is inconsistent as well as weak); `/fonts/Velista.ttf` and `/og-image.jpg` ship **no `cache-control`** at all, while hashed bundles are correctly `immutable`; the **default OG image is a Lovable preview screenshot** (an `...lovable.app-<timestamp>.png` artifact on an R2 bucket) — currently the social-share card for every page that doesn't pass its own image.
- **Medium — all 19 journal articles have no author and no image.** `image` is required for Article rich results and there's no per-article asset to point at (no image field in the data model). Authorship is a sitewide `meta name="author"` of "Naira Flore" — an organisation, not a person. Explicit warning in the source: do not paper over the image gap with the default OG fallback, since that fallback is the Lovable artifact above and would be worse than omitting the property.

### 3.5 Verified already working

robots.txt (explicit allows for Googlebot, Bingbot, Twitterbot, facebookexternalhit + wildcard, correct `Sitemap:` line, no traps/Disallow) · sitemap mechanics (valid XML, correct content-type, 20 sampled URLs all 200, no redirect chains) · HTTP→HTTPS single-hop 301 · hashed asset caching (`public, max-age=31536000, immutable`) · no cloaking · Organization + WebSite JSON-LD server-rendered · no fabricated review markup (`aggregateRating` stays removed, with a code comment explaining why).

### 3.6 Recommendation and sequencing

**Prerender** (e.g. `vite-react-ssg`, or a Playwright pass over the built SPA) is the explicit recommendation — days of cost, no app rewrite, no new server runtime; the route list is already enumerable via `generate-sitemap.ts`. Full SSR (Next.js/Remix) is called out as over-building. Dynamic rendering (serving prerendered HTML only to a bot allowlist) is explicitly **not recommended** — "Google calls it a legacy workaround," and it fails this exact problem since new/unlisted AI crawler UAs would still get the empty shell.

A related detail: the hero image's `fetchpriority="high"` is inert, because the browser's preload scanner can't discover an element that doesn't exist in the initial HTML — it only appears after React mounts. Preloading the background image directly from `index.html` cut LCP by 2.7s; the `fetchpriority` hint never did anything. Prerendering would make the hint work as intended.

Stated order of work: **Now** — deploy the already-committed fixes (schema fixes, Naira Petite rename, carousel fix, image work). **This week** — reconcile the three brand descriptions (copy-only). **This sprint** — prerender the 100 routes. **Then** — edge 404 handling, CSP, the 301 fix, cache headers, a real OG image.

### 3.7 Method note

Three specialist agents (technical, schema, GEO) plus direct verification. A tooling caveat is recorded: the claude-seo plugin's own bundled fetchers don't run in this sandboxed environment (its SSRF guard hard-refuses `127.0.0.1`, which is exactly where the outbound proxy sits, with no allowlist exposed; headless Chromium is also blocked at the proxy). The agents were driven with `curl` and WebFetch instead. On an unsandboxed machine the plugin would run as designed.

---

## 4. Source verification findings (Doc 5)

**Scope, stated by the document itself:** *"Every listed SKU judged against the supplier photograph rather than against its own written description."* This means "verified" in this document specifically means **agrees with the supplier's own reference photo** — it is not a lab/material certification pass. Keep that distinction in mind reading "verified" below.

**Top-line numbers:** 68 SKUs in the catalogue · 60 shot, written and listed (8 catalogue SKUs are not yet photographed/written/listed at all — not individually named in the retrievable text) · 50 live and active · 18 draft · **24 mismatches found.** Arithmetic check: 34 clean + 8 "reshoot needed" + 2 "held on earlier instruction" + 2 "cannot be verified" + 14 "copy corrected, live now" = 60, matching the "shot/written/listed" figure. The "24 mismatches" total reconciles as 8 + 2 + 14 = 24 — i.e. the 2 "cannot be verified" SKUs are explicitly *not* counted as mismatches (undetermined, not wrong).

### 4.1 Material / plating / pearl / stone-type claims specifically

| Product | SKU | Claim type | Supplier-stated | Verified / unsupported |
|---|---|---|---|---|
| Pearl Halo Studs | WE24089B | Pearl type | Supplier states **no pearl provenance** on this stainless-steel fashion piece. | **Unsupported claim on the live listing**: copy calls it "round white freshwater pearl." Per the site's own material-honesty rule, must read **shell pearl**. Pearl *colour* (white) is verified correct — only the *type* claim ("freshwater") is unsupported. |
| Pearl Blossom Earrings | E20997C | Pearl colour | Supplier photo: warm champagne/peach tone. | **Unsupported** — copy says "round white freshwater pearl"; live images render neutral white/ivory. Both copy and image diverge from the supplier reference. |
| Halo Curve Ring | YF8453 | Stone type | Supplier stone: opaque/semi-opaque mottled brown-gold **tiger eye** with visible chatoyant banding. | Copy is **verified correct** ("natural tiger eye"). It is the *images* that are unsupported — rendered as a fully transparent, faceted amber/cognac crystal reading as citrine glass. |
| Star Point Band | YF5214 | Plating / metal tone | Order line is the gold colourway `YF5214-Gold-leaf`. | **Unsupported tag** — product tagged Silver Tone with no gold-plating tag at all. |
| Duet of Dawn Ring | JDR0104342-PS | Plating placement | Supplier photo: cool steel-tone **shank**, both bezels warm gold. | Copy was unsupported (said one bezel steel, one gold — misplacing the tone) — **now fixed**; images were always correct. |

### 4.2 Verified clean against the supplier photo — 34 SKUs (no SKU codes given for this list in the source)

Noir Huggie · Brushed Gold Huggies · Ribbon Bow Earrings · Solitaire Whisper Studs · Petal Pearl Drop Studs · Woven Gold Hoops · Verdant Circlet Studs · Textured Gold Hoops · Pearl Ribbon Ring* · Blush Station Bracelet · Molten Bloom Hoops · Clover Trio Edit · Silver Dome Ring* · Golden Duet Ring* · Chevron Whisper Ring · Halo Bloom Ring · Baguette Arc Hoops · Whisper Pavé Band · Petite Pavé Band · Cushion Halo Ring · Verdant Eternity Band · Vintage Halo Ring · Bold Nocturne Chain · Heartbead Bracelet* · Dewdrop Bezel Necklace · Pearl Link Bracelet · Baroque Bloom Cuff · Rivière Eternal Bracelet · Filigree Bloom Studs · Ribbon Bead Bracelet · Pearl Drop Studs · Teardrop Lariat · Serpentine Whisper Chain · Tassel Nocturne Necklace

*Starred entries are contradicted by the Catalogue Fidelity Audit — see §1.7.

### 4.3 Reshoot needed, pulled off the store — 8 major mismatches

| Product | SKU | Problem |
|---|---|---|
| Prism Rivière Bracelet | B00681C | Supplier uses only 3 stone colours (aqua, pink, pale yellow) in pavé-halo frames. Listing image adds a 4th lilac/lavender stone not on the real piece; copy lists "lilac" as a 4th colour and calls the setting "individual square bezels" instead of pavé halos. |
| Baguette Éclat Bracelet | JDB201083 | Wrong product. Supplier photo: fine gold cable chain bracelet with one tiny open circle of pavé stones. Listing: full baguette CZ tennis bracelet with lobster clasp; copy describes that tennis line. Nothing about the live listing matches the supplier reference. |
| Petite Pearl Chain | YF-DIYChain | Wrong product entirely. Supplier photo: chunky gold oval-link **bracelet** with large elongated oval baroque pearls. Listing: fine 42cm gold cable-chain **necklace** with small flat square white shell pearls, lobster clasp + extender. Different item type, chain gauge, pearl shape, and setting. |
| Clover Charm Necklace | YF6618 | Ordered item: 5 plain hammered gold hollow charm styles (open flower outline 22×25mm, maple leaf 19×17mm, lattice disc 22mm, spiral square 16×19mm, spiral circle 24×20mm), two of each, no stones, no chain. Listing: a small polished ~10mm quatrefoil clover pavé-set with 5 clear CZ on a 42cm cable chain. Wrong shape, size, finish, invented stones, unordered chain. |
| Halo Curve Ring | YF8453 | See §4.1 — tiger eye rendered as faceted crystal; image-only defect. |
| Pearl Blossom Earrings | E20997C | Minor — see §4.1. |
| Toggle Link Chain | YF5143 | Minor — see §1.7 item 7 for the direction dispute with Doc 2. |
| Star Point Band | YF5214 | Minor — see §4.1 for the plating-tag mismatch. Setting is also wrong: supplier shows a flush engraved recess with a cluster of 4–5 tiny pavé stones per star; listing shows a raised, embossed star with one large single solitaire. |

### 4.4 Held on your earlier instruction — 2 SKUs (previously flagged, deliberately left as-is)

- **Verdant Drop Earrings** (`E21572E1`) — major. Supplier stone sits in 4 plain claws on a plain silver basket, no halo. Every listing image adds a full pavé halo, and copy describes that halo. Supplier stone colour is also deeper green-teal vs. the lighter aqua-turquoise shown.
- **Pearl Reverie Bracelet** (`JDB2409013`) — minor. Supplier reference is a two-piece set (necklace + bracelet); every listing image reproduces both, with the worn campaign shot leading on the necklace. Only the 19cm bracelet is actually sold — the copy's last line says the 45cm necklace is not included, so the imagery sells a piece not in the box.

### 4.5 Cannot be verified against source — 2 SKUs

- **Rivière of Light Bracelet** (`JDB201210`) — supplier reference is a stacked wrist shot of 8–9 different bracelets; no single item is identifiable as this SKU. Cannot confirm or refute the live round-brilliant CZ tennis bracelet. Needs a single product photo from the supplier. (This is the SKU at the centre of the swap dispute in §1.6/§1.7.)
- **Verdant Rivière Bracelet** (`JDB201210-GN`) — same multi-product stack shot, so this SKU's item can't be isolated either. Flagged for re-sourcing: the only green bracelet visible in that stack reads as a line of small round/oval green stones with a larger rectangular emerald-cut station, whereas the listing shows a uniform line of 4×3mm rectangular step-cut stones with no station — but the reference is too low-resolution to call it a fail outright.

### 4.6 Copy corrected against source, live now — 14 SKUs (already fixed)

| Product | SKU | Fixed issue |
|---|---|---|
| Granule Dome Ring | JDR0104337 | Copy wrongly said "small clear cubic zirconia set among the granulation" — that pavé description belongs to the silver sister piece `JDR0104337-S`, not this solid-gold-granulation piece. Images were always correct. |
| Star Fall Drop Earrings | E11857B | Copy said the chain ends "in a smaller star," inverting the real proportions (drop star is ~1.4× the top stud star). |
| Silver Drop Earrings | E16676C | Copy called the bar "plain metal"; it's pavé-set with small round clear stones in both the supplier photo and the listing images. |
| Pearl Point Studs | E19263B | Copy said "four small clear zircons"; supplier and listing both show three. |
| Duet of Dawn Ring | JDR0104342-PS | See §4.1. |
| First Light Set | JDS0204301-set | See §1.7 item 6 — Doc 5 calls this copy-only and fixed; Doc 2 says the images still have an invented bail. |
| Rose Verdant Band | R18345A1 | Copy described "two pave set and two plain" bands — that description actually belongs to a different SKU, `WR12518B`. Real piece: pavé runs along all four bands. |
| Pearl Halo Studs | WE24089B | See §4.1. |
| Blush Cluster Ring | WR10914B2 | Copy said "eight round pink cubic zirconia" in the halo; supplier photo and listing image both show ten. |
| Baroque Shell Bracelet | YF3925 | Copy said a chain runs between the pearls; images correctly show gold rondelle beads. Copy also omitted a visible extra part: a baroque pearl drop hanging off the toggle ring. |
| Heartline Paperclip Necklace | YF3952 | Copy said stations were spaced through the full length; supplier photo shows all 9–10 pavé heart stations clustered at the front only (images show this correctly). |
| Bold Nocturne Bracelet | YF5144-BRA | Copy said "thick flat curb link"; supplier and listing images both show a chunky elongated oval paperclip link. |
| Charm Box Chain | YF5146 | Copy said "small rectangular clear cubic zirconia" charm; supplier and listing both show a cylindrical barrel rondelle pavé-set around its circumference. |
| Rivière Eternal Necklace | YF7085-NEC | See §1.7 item 1 — Doc 5 calls this fixed and image-correct; Doc 2 lists it as a still-failing image defect. |

---

## 5. Catalogue conflicts (Doc 4, "Catalogue conflicts" table — 56 items across 49 affected products, plus Doc 2's structural findings)

Doc 4's own framing: *"Nothing here has been changed yet — handle rewrites change live URLs and deletions are permanent."* Breakdown by type: Legacy catalogue 18 · Handle drift 16 · Alt text 9 · Tag vocabulary 8 · Missing image 2 · Broken handle 1 · Placeholder SKU 1 · Wrong tag 1. (16 critical, per the document's own stat block.)

### 5.1 Duplicate SKUs / identity conflicts

- `WR20902K8` (Cushion Halo Ring) and `R15464K` (Halo Bloom Ring) share a **byte-identical** product photo (`kav/WR20902K8_1.jpg` = `kav/R15464K_1.jpg`) — see §1.6.
- `JDB201210` / `JDB201083` code swap between Rivière of Light and Baguette Éclat — see §1.6, disputed in §1.7.

### 5.2 Handle drift — 16 products (live URL still uses the retired name)

| Product | Live URL still reads | Proposed fix |
|---|---|---|
| Toggle Link Chain | `/ivory-clasp-chain` | Redirect old handle → new |
| Baroque Pearl Lariat | `/tassel-nocturne-necklace` | Redirect old handle → new |
| Verdant Drop Earrings | `/emerald-drop-earrings` | Redirect old handle → new |
| Baguette Arc Hoops | `/clover-bloom-studs` | Redirect old handle → new |
| Filigree Bloom Studs | `/clover-fringe-earrings` | Redirect old handle → new |
| Pearl Drop Studs | `/heart-whisper-studs` | Redirect old handle → new |
| Brushed Gold Huggies | `/golden-nugget-studs` | Redirect old handle → new |
| Baroque Shell Bracelet | `/pearl-legacy-bracelet` | Redirect old handle → new |
| Verdant Rivière Bracelet | `/emerald-riviere-bracelet` | Redirect old handle → new |
| Blush Cluster Ring | `/blush-halo-ring` | Redirect old handle → new |
| Rose Verdant Band | `/rose-emerald-band` | Redirect old handle → new |
| Granule Dome Ring | `/amber-dome-ring` | Redirect old handle → new |
| Verdant Eternity Band | `/emerald-eternity-band` | Redirect old handle → new |
| Verdant Circlet Studs | `/emerald-cluster-studs` | Redirect old handle → new |
| Teardrop Lariat | `/pearl-ceremony-set` | Redirect old handle → new |
| Clover Charm Necklace | `/clover-charm` | Redirect old handle → new |

### 5.3 Broken handle and placeholder SKU (both critical)

- **Gulaal mirage** — handle is literally `/11000` (a price, not a name). Fix: set handle → `/gulaal-mirage`; also fix title case.
- **"Untitled Oct7_22:31"** — draft, ₹0.00, no images, no variants. Fix: delete.

### 5.4 Alt text — 9 products (partly overlapping with Doc 2's alt-text section, §1.7-adjacent)

| Product | Alt text problem |
|---|---|
| Pavé Initial Chain Drops | Alt reads "Noir Huggie" — a different product. |
| Marquise Layering Set | Alt reads "Teardrop Reverie Necklace." |
| Baroque Pearl Lariat | Alt reads "Tassel Nocturne Necklace." |
| Teardrop Lariat | Alt reads "…on the house set" — a copy artefact. |
| Rivière Eternal Necklace | Alt says "Riviere" — accent dropped. |
| Rivière Eternal Bracelet | Alt says "Riviere" — accent dropped. |
| Prism Rivière Bracelet | Alt says "Riviere" — accent dropped. |
| Rivière of Light Bracelet | Alt says "Riviere" — accent dropped. |
| Baguette Éclat Bracelet | Alt says "Baguette eclat" — accent and case dropped. |

Doc 2 separately documents *content*-level (not just spelling-level) alt-text failures, from an earlier pass written off the live renders rather than the supplier originals — so wherever a render hallucinated, the alt text repeated the hallucination. Confirmed wrong on at least 5 products: **Verdant Rivière** ("unbroken line of emerald-cut… with a box clasp" — actually round stones with an emerald-cut centre station); **Prism Rivière** ("baguette and round zircon set in gold" — actually square step-cuts in rhodium silver); **Rivière Eternal Bracelet** ("box clasp and safety catch" — no box clasp exists on the piece); **Rivière of Light** and **Baguette Éclat** ("graduated," "channel-set" — the lines are uniform and four-claw). Doc 2 recommends rewriting all of these from the originals once frame removals settle.

### 5.5 Legacy catalogue — 18 products (draft-vs-active / vendor conflicts)

**12 products under vendor "My Store"** — no product type, no tags, priced ₹12k–48k, proposed fix "Archive or reassign": Blush of Dawn · Ethereal Lilac · Royal Enigma · Amber Bloom Set · Amber Radiance · Golden Blossom · Midnight Bloom · Ivory Whisper Co-ord Set · Sunset Reverie · Lilac Whisper · Crimson Legacy Set · Heritage Mosaic.

**6 products under vendor "Naira"** (not "Naira Petite") — no product type, no tags, proposed fix "Reassign to Naira Petite": Noir Mela · Tangerine Bloom · Gulaal mirage (also the broken-handle item, §5.3) · Midnight Éclat · Nocturne Veil · Celeste Bloom.

### 5.6 Tag vocabulary — 8 products still on the old tag set

Using "18k Gold Plated" / "Demi-Fine" / "Anti-Tarnish" instead of the current house tag set: Pearl Legacy Necklace · Marquise Layering Set · Peach Heart Hoops · Triple Dawn Cuff · Whisper Twist Cuff · Trio Bloom Ring · Scatter Light Band · Classic Solitaire Ring.

### 5.7 Wrong tag

- **Verdant Circlet Studs** — tagged "Pearl"; it is a zircon circlet, not a pearl piece. Fix: remove the Pearl tag.

### 5.8 Missing image — 2 products (critical)

- **Pearl Legacy Necklace** — no media attached.
- **Peach Heart Hoops** — no media attached.

### 5.9 Draft-vs-active status conflicts (pulled together from Docs 2, 4, 5)

- **Triple Dawn Cuff** — moved to DRAFT since the fidelity audit ran, taking the phantom triple-layer listing off the customer-facing store; its 3 stored frames would still show the wrong single hammered cuff if it's ever republished (§1.2).
- **"Untitled Oct7_22:31"** — draft placeholder, ₹0.00, recommended for deletion (§5.3).
- **18 SKUs sitewide are in draft** per Doc 5's top-line stat (§4); only Triple Dawn Cuff is individually named as draft anywhere in the readable text of the five documents — the other 17 are uncounted by name here.
- The 12 "My Store"-vendor legacy products (§5.5) are not explicitly marked draft or active in the retrievable text, only flagged as orphaned/miscategorised — status unconfirmed, noted as a gap rather than assumed.

---

## 6. Known failure modes — pre-flight checklist

A reusable list, built from every distinct way this catalogue has been shown to fail across all five documents. Run this before publishing any new product image or listing.

**Before uploading a product image:**
- [ ] Does every stone, halo, or pavé band in the image actually exist on the physical/supplier reference? (Not "does it look plausible" — check against the supplier photo directly.) *Recurring failure: invented ornamentation, §2.3 #1.*
- [ ] Is the stone cut shown (round / square / princess / marquise / baguette) the cut the supplier photo actually shows? *§2.3 #2.*
- [ ] Is the metal tone (gold / silver / two-tone, and which part is which tone) correct against the supplier reference — not just "looks gold enough"? *§2.3 #3, and note the Duet of Dawn Ring case where the tones were right in the image but swapped in the copy.*
- [ ] Is the stone/pearl colour matched against the supplier photo, not against a stock assumption of what that gem "usually" looks like? *§2.3 #4.*
- [ ] Is the clasp, setting type, bail, or toggle mechanism shown the one the piece actually has? Check specifically whether a hero shot has invented a construction detail that doesn't exist (e.g. a bail, a box clasp) or shown a mechanism that visibly can't function (a toggle that can't close). *§2.3 #5.*
- [ ] Does the file actually belong to the SKU it's attached to — not a sibling product, not a different colourway, not the wrong item in a multi-product supplier reference shot? *§2.3 #6, and see the `JDB201210`/`JDB201083` dispute at §1.7 for what happens when this isn't checked.*
- [ ] Is this exact image file (checked by hash, not by eye) already in use under a different SKU? *§2.3 #7 — Cushion Halo Ring / Halo Bloom Ring.*
- [ ] Does any styling choice — a prop, a liquid, a container — risk reading as something other than jewellery out of context? *§2.3 #8 — the IV-saline-bag frame.*
- [ ] If the supplier reference itself is a multi-product stack shot or otherwise ambiguous, is that logged as "unverifiable" rather than silently passed? *§1.6, §4.5.*

**Before publishing product copy:**
- [ ] Every stated dimension (length, stone size, bead size) checked against the supplier spec index, not estimated from the photo. *§1.3.*
- [ ] Stone/pearl/halo counts checked by literally counting them in the supplier photo. *Blush Cluster Ring: copy said 8, supplier shows 10.*
- [ ] Material-type claims (freshwater pearl vs shell pearl, plating type) checked against what the supplier actually states — not assumed from how the piece looks. If the supplier states no provenance, the copy cannot claim one. *§4.1.*
- [ ] Product **name** itself checked for a false claim (e.g. "Halo" in the name when the piece has no halo) — naming errors are as real a defect as description errors and were found on at least 3 separate products (Dewdrop Bezel Necklace, Halo Curve Ring, Pearl Halo Studs). *§1.3.*
- [ ] Two-tone/plating placement described in the correct location (shank vs bezel, etc.), not just correct in the abstract. *Duet of Dawn Ring, §4.1.*
- [ ] Copy for one SKU isn't accidentally describing a *different, similar* SKU (Rose Verdant Band's copy matched `WR12518B`, not itself). *§4.6.*

**Before publishing or updating a Shopify listing (data hygiene):**
- [ ] Handle matches the current product title — check the actual live URL, not just the admin title field. *§5.2, 16 known cases.*
- [ ] Handle is not an artefact (a price, a timestamp, a copy-paste leftover). *§5.3.*
- [ ] Alt text is regenerated from the *supplier original*, not from whatever render is currently live — if the render was wrong, an alt-text pass done after the fact will simply encode the same wrong claim in a second place. *§5.4.*
- [ ] Alt text uses the product's actual title, including diacritics (Rivière, not Riviere). *§5.4.*
- [ ] Vendor field is the current brand name, not a legacy placeholder ("My Store," bare "Naira"). *§5.5.*
- [ ] Product has at least one tag and one product type — untagged/untyped products silently vanish from filtered collections and search. *§5.5, §5.6.*
- [ ] Tags use the current house vocabulary, not a retired set ("18k Gold Plated"/"Demi-Fine"/"Anti-Tarnish"). *§5.6.*
- [ ] Material-descriptor tags (e.g. "Pearl") match what's actually on the piece. *§5.7.*
- [ ] At least one image is actually attached before the product goes active — draft products with zero media have shipped to "live and active" before. *§5.8.*
- [ ] If a product is pulled to DRAFT for a known defect, confirm its stored images don't still carry the same defect for whenever it's republished. *Triple Dawn Cuff, §5.9.*

**Before trusting an audit's own verdict on a SKU:**
- [ ] Check whether another audit in this history already made a claim about the same SKU, and whether the two claims actually agree — nine did not, in this history (§1.7). Do not assume the most recent document is the correct one by default; in at least one case (Rivière Eternal Necklace) the *earlier* document's "already fixed" claim looks more consistent with the stated fix method than the later document's "still failing" claim, but neither was re-verified here.
- [ ] Re-derive stat-block totals from the itemised rows beneath them before quoting the stat block — Doc 2's "63 still failing" doesn't match its own table (sums to 60), and its "3 failing on draft" names only 1 SKU in the retrievable text.
- [ ] When a supplier reference photo shows multiple products in one stack shot, treat any single-SKU claim drawn from it as unverified until a dedicated photo exists — this was the direct cause of the `JDB201210`/`JDB201083` identity dispute in this history (§1.6, §1.7).

---

## Defect count

Distinct, individually-itemised defects catalogued across all sections above (not counting the recurring-failure-mode groupings in §2.3/§6, which summarise rather than add new items):

- §1.1 Image defects, still failing: 27 rows (60 frames, per the table; header claims 63)
- §1.2 Image defects, fixed/partial: 14 products + 2 "moved the wrong way"
- §1.3 Dimension/copy data errors: 21 rows
- §1.4 Metal-tone defects: 3
- §1.6 Structural/identity defects: 3
- §4.3–4.6 Source-verification mismatches: 8 (reshoot) + 2 (held) + 2 (unverifiable) + 14 (copy-corrected) = 26
- §5.2–5.8 Catalogue/data conflicts: 56 (per Doc 4's own count: 18 legacy + 16 handle drift + 9 alt text + 8 tag vocabulary + 2 missing image + 1 broken handle + 1 placeholder SKU + 1 wrong tag)
- §2.1 Image rejections (process): 10 frames cut (1 documented reason)
- §3 SEO defects: 3 critical root-cause findings + 4 open (high/medium) findings + 5 already-fixed findings = 12

**Approximate total: 172 individually-itemised defects/findings**, plus **11 explicit cross-document disagreements** (§1.7) layered on top of them.
