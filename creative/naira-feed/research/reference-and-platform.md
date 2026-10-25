# Reference teardown, platform facts, calendar, exemplars

Research sweep for the Naira Flore / Naira Petite Instagram feed (two curated 12-post options).
Compiled 25 Oct 2026. Read-only: no connector was written to; no Instagram login was used.

Evidence labels used throughout:

- **[measured]** taken from the user's screenshot with pixel measurement (PIL), reproducible.
- **[observed]** read by eye from the screenshot tiles (crops in `research/tiles/`).
- **[sourced]** from a web source, cited inline with date.
- **[inferred]** reasoning from the above; treat as a hypothesis.
- **[unverified]** could not be confirmed this session.

Tile crops (2x upscales) are saved at
`/tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed/research/tiles/` as `r{row}c{col}.png`
(plus `r1c3_x3.png`, the multi-script poster at 3x, and `r1c1_sign.png`, the event standee).

---

## A. Reference teardown: @projecttteteatete (PTAT)

### A0. Who PTAT is

- **Project Tête-à-Tête (PTAT)** describes itself as "Mumbai's leading luxury multi-designer store and experiential
  platform, bringing together emerging and established Indian designers under one roof" [sourced: projectteteatete.com,
  fetched 25 Oct 2026]. Store at 502 Jai Mahal, Linking Road, Khar West, Mumbai 400052 [sourced: projectteteatete.com;
  LBB listing lbb.in/places/Project-TeteATete-khar-0b03b2]. Categories: clothing, jewellery, accessories, beauty, art,
  preloved; brands grouped as Ethnic / Street Style / Party / Active / Vacation; site lists Workshops and Popups under
  "Experiences" and runs a WhatsApp community for "new arrivals, private previews & exclusive events" [sourced].
  Founders not named anywhere found [unverified].
- A March 2025 report places a Duchess Kumari collection launch at the PTAT store with a high-tea co-hosted by
  influencer Reshma Ajbani [sourced via web search summary; article not opened, treat as secondary].
- **MILNI**: no press coverage found (searches for MILNI + Soho House + PTAT returned nothing) [unverified]. Everything
  known comes from the screenshot itself: "PTAT BRINGS YOU MILNI · SOHO HOUSE MUMBAI · 24 & 25TH OCT · SEE YOU",
  "24-25TH OCT 12-8PM · SOHO HOUSE, JUHU MUMBAI", co-branded **PTAT × SOHO FRIENDS** (Soho House's community
  programme mark, a 3x3 grid glyph) [observed]. The physical standee lists a "FEATURING" roster of designers
  (unreadable at this resolution) [observed]. Year is not printed; 24–25 Oct 2026 is a Saturday–Sunday, i.e. this
  weekend, so the grid is most likely live right now [inferred].
- **What "Milni" means**: in Punjabi/North-Indian (notably Sikh) weddings the *milni* is the ritual meeting of the two
  families before the ceremony, relatives embracing and exchanging garlands. Naming a designer pop-up MILNI frames the
  event as "the families meeting": designers, community, shoppers [inferred from common knowledge; no PTAT statement
  found]. The wedding framing is deliberate seasonal timing: the pop-up lands two weeks before Diwali and a month before
  the wedding season opens (see section C).
- Soho House Mumbai: 11-storey converted building on Juhu Beach, opened 2018, interiors from locally sourced furniture,
  Indian antiques and Rajasthani block prints; art by Subodh Gupta, Bharti Kher, Thukral & Tagra [sourced: Wallpaper*,
  Dezeen 10 Dec 2018]. The venue itself (vines, lanterns, block prints, rooftop pool with blue mosaic) appears in the
  reels [observed], so the location is part of the art direction.

### A1. The grid geometry (what the screenshot proves about Instagram today)

- Screenshot 1179 x 2556 px (iPhone, 3x). Tiles measure **391 x 521 px** with **3 px gutters** (x: 0–390, 394–784,
  788–1178; y rows end at 878/1402/1926) → **0.7505 = 3:4** [measured]. This confirms the 3:4 profile grid on the
  user's own device.
- Each tile renders at ~130 pt wide. A 1080-px-wide design is shown at **36.2%** of its size in the grid [measured:
  391/1080]. Rule of thumb that follows: anything below ~65 px cap height on a 1080 canvas becomes unreadable in the
  grid (~24 physical px, ~8 pt) [inferred]. Check against PTAT: the "MILNI" wordmark in r2c1 is ~62 px tall in the tile
  ≈ 170 px on the 1080 canvas (reads instantly); the date line ≈ 97 px canvas (reads); "SOHO HOUSE, JUHU MUMBAI" ≈ 33 px
  canvas (does not read in grid, reads on tap) [measured, approx ±10%].
- **UI chrome on tiles**: the format icon (reel play-button / carousel stacked-squares) sits in the top-right at
  roughly x 84–96%, y 4–13% of the tile [measured from r2c1/r2c3/r3c2]. The profile also overlays "Just seen" across a
  tile you recently opened (r1c1) [observed]. Keep the top-right ~16% x 14% of every cover free of essential content.
- Profile tabs visible: Grid, Reels, Reposts (circular arrows), Tagged [observed]. Row 1 is partly scrolled off, so its
  corner icons are not visible; row 5 is a 100 px sliver.

### A2. Tile-by-tile

Format is read from the corner icon (play-button = Reel; stacked squares = carousel; none = single image).
Position = row/column from top-left of the visible grid.

| Pos | Format | Subject | Technique | Typography | Colour (dominant, sampled) | Recurring motif |
|---|---|---|---|---|---|---|
| **r1c1** | not visible (icon scrolled off; "Just seen" overlay) | Guest in an olive pre-draped sari-gown, sequinned bodice, sunglasses, phone to ear, posing beside the MILNI standee in a hotel corridor | Event documentation photo / video still; the physical standee repeats the digital key art | MILNI 3D slab lockup bottom; "PTAT" logo below | dark browns #3F3830 / #321316 / #120B08 (dim interior) | MILNI lockup (wordmark + mehndi hand holding lotus + marigold cluster) |
| **r1c2** | not visible | "MILNI FIRST LOOK": model in a metallic red-gold crushed/tie-dye oversized shirt over a black lace corset, gold collar necklace; night bokeh of brass oil lamps (deepastambha) | Studio/editorial photo, festive night bokeh | MILNI lockup + "FIRST LOOK" in the same chiselled 3D caps, magenta | near-black #130E0E, oxblood #682527, copper #7F4C3E | MILNI lockup; brass lamp light |
| **r1c3** | not visible | Key-art poster: the word MILNI hand-lettered in ~7 scripts: Latin (cut off), Urdu/Nastaliq ملنی, Devanagari मिलनी, Bengali মিলনী, Gurmukhi ਮਿਲਣੀ, Malayalam മിലനി, Devanagari again, Tamil மில்னி | Indian hand-painted signboard / truck-art / Bollywood poster idiom: 3D extruded letters, white keyline, sunburst rays, rose-vine borders, yellow torana scrolls, hot-pink frame, a dhol/drum at the base | Multi-script display lettering, each script in a different colour; footer in hand-drawn caps on an arc: "PTAT BRINGS YOU MILNI / SOHO HOUSE MUMBAI / 24 & 25TH OCT / SEE YOU" | acid yellow #E7EE59, hot pink #DB3375, crimson #9B2636, violet #3A3149 | Multi-script MILNI = the event's hero idea ("meeting" said in every language of the families who meet) |
| **r2c1** | **Reel** | Animated key-art card: "PTAT × SOHO FRIENDS / MILNI / 24-25TH OCT 12-8PM / SOHO HOUSE, JUHU MUMBAI" | Flat hot-pink field; illustrated banana/plantain leaves bleeding in from top-left and bottom-right corners; lockup centre | Logo row (PTAT + SOHO FRIENDS) small caps; MILNI in 3D chiselled slab caps; date in thin geometric sans caps | hot pink **#E83A8D** (65% of tile), oxblood #812C44 | Lockup; plantain leaves |
| **r2c2** | **Carousel** | "MILNI F.O.M.O · BOLLYWOOD EDITION": posterised painted portrait of a 1970s–80s screen-siren (reads as the actress Rekha; identity unverified) in bindi, jhumkas and a choker | Mixed media: posterised photo-painting in a scalloped green "mirror" cut-out frame with a hand-drawn brown scalloped border, on a magenta block-print ground of gold buti (marigold sprigs); marigold clusters tucked at two corners | MILNI F.O.M.O in 3D caps; "BOLLYWOOD EDITION" set on an arc following the frame; tiny PTAT on the portrait | magenta #A02248, maroon #561F20, antique gold #B69155 | Lockup; block-print pattern; scalloped frame; nostalgia portrait |
| **r2c3** | **Reel** | Crowd shot inside the pop-up: Soho House terrace with hanging vines, rope macramé, paper lanterns, clothing racks, shoppers | Documentary/UGC-feel video; branding laid over it | Folio-style corner text: "SOHO HOUSE JUHU" top-left, "24-25 OCT 12-8PM" top-right in thin sans; MILNI lockup bottom; PTAT + SOHO FRIENDS logos | warm browns #7D5C4E / #403A35, foliage | Lockup; folio corners; proof of footfall |
| **r3c1** | **Carousel** | Featured-designer look: model in black cross-halter crop top + black floral-sequin skirt, seated on the rooftop pool's blue mosaic edge, overcast sky | Fashion photo, natural light; a small designer logo watermark mid-frame | Folio corners "AT SOHO HOUSE, JUHU" / "OCT 24-25 12-8 PM" in thin sans caps; MILNI lockup bottom | cool grey #B4BDBC sky, umber #71574C | Lockup; folio corners; designer showcase wrapped in event branding |
| **r3c2** | **Carousel** | "PTAT's Accessory Guide · vol 1": a stainless-steel tray (the Indian kitchen *thali*/serving tray) holding gold hoops with rainbow stones, enamel beetle studs, a brass horse brooch, gold safety-pin drops, gold scroll earrings | Product flat-lay photographed on a steel tray, dropped onto a baby-pink tartan ground; scrapbook stickers: glitter rainbows, smiley flower, felt smiley badge, torn felt heart, pink gingham fabric patch | "PTAT's" in navy serif caps; "Accessory" and "Guide" in navy copperplate script split above and below the tray; "vol 1" between dotted rules | baby pink **#E9C0C6**, steel grey #786C72, white | Series device ("vol 1"); sticker scrapbook; Indian domestic object as a display surface |
| **r3c3** | **Reel** | Model (white scalloped crop top, pleated mint mini skirt, printed tote, headband) waving from inside an open wardrobe | Real video composited into a **pen-and-ink line illustration** of a carved Rococo armoire with doors swung open, and a sketched room around it (pinned drawings of a flower and a heart, side table, vase of branches, fringed lamp, mirror) | none on cover | ivory line-paper #F8F6EF, tan #D4B692 | Illustration framing a photo cut-out ("step into my wardrobe") |
| **r4c1** | **Single image** (no icon) | "NEW Collection DROP": four full-length model cut-outs labelled [01]–[04] with a legend: "[01] Weekend Wanderer [02] Brunch Ready [03] Festive Fit [04] Soft Girl Era" | Catalogue-index layout: cut-outs on aqua/white candy stripes | "NEW" + "DROP" in teal geometric caps around "Collection" in teal script; subtitle in sans "Fresh silhouettes, bold textures, made for right now."; bracketed numerals | aqua/white stripe #EFFDFD / #DDF7F4, teal type | Numbered cut-outs; script + caps lockup; patterned ground |
| **r4c2** | **Carousel** | "YOUR Wardrobe NEEDS MORE whimsy": five full-length cut-outs standing on a lined notebook page | Scrapbook collage: ruled-paper card clipped by a rose-gold heart-shaped bulldog clip, laid over a photo of a cosmos-flower meadow and sky; stickers: blue flower, smiley daisy, pink bow, hand-doodled sun and daisies | Burgundy copperplate script ("Wardrobe", "whimsy") + burgundy sans caps ("YOUR", "NEEDS MORE") | white paper #F7F6F4, slate #B1B1B5, meadow pinks | Scrapbook note; cut-outs; script + caps |
| **r4c3** | **Reel** | "ASMR": model in a silver paillette-sequin halter mini dress holding a gold ball clutch, in a pastel room with framed pop-art paintings and a glass stair rail | Trend-format video; texture/sound hook | "ASMR" in small white sans with sparkle glyphs | warm beige #BA9D6C / #CAB185 | Texture as content (sequins, sound) |
| r5c1 | Reel | Model in a peach interior with striped curtain | photo/video | n/a | peach | partial |
| r5c2 | Reel | Model in a pink room with pink glass-front cabinets and framed art | photo/video | n/a | blush pink | partial |
| r5c3 | unknown | Paper-clipped white card with a cut-out red/purple striped strapless top and skirt, on blue chevron/gingham | Scrapbook cut-out collage | n/a | blue/white | Scrapbook + paper-clip (repeat of r4c2 device) |

Format count, rows 2–4 (the nine tiles whose icons are visible): **4 Reels, 4 carousels, 1 single image** [observed].
Reels sit in column 3 for all three of rows 2–4 (plus r2c1) [observed]; whether deliberate is unknown [inferred].

### A3. The recurring motifs (the "brand furniture")

1. **The MILNI lockup**, used on 7 of 9 event tiles [observed]: a chiselled, bevelled slab-serif wordmark (magenta face,
   darker bevel, white keyline, like a carved sign) + a hand-drawn **mehndi-patterned hand with long nails holding a pink
   lotus** (a dance-mudra gesture) on the right + a **cluster of orange marigolds** on the left. The hand and the
   marigolds bracket the word like parentheses. It is laid at the bottom third of every event photo, so the series
   reads as one campaign even when the photos differ completely.
2. **Folio corners**: venue top-left, date/time top-right, in a thin geometric sans, like a magazine running head
   (r2c3, r3c1). Pure logistics, never competing with the hero.
3. **Indian vernacular graphic idioms**, used as *quotation*, not costume: signboard/truck-art multi-script lettering
   (r1c3), block-print buti wallpaper (r2c2), Bollywood poster portrait (r2c2), the steel tray (r3c2), plantain leaves
   (r2c1). Each tile quotes one idiom; none stacks them all.
4. **Photo cut-outs on a graphic ground**: figures with clean silhouettes dropped onto stripes (r4c1), ruled paper
   (r4c2), a drawn wardrobe (r3c3), a steel tray (r3c2). Real product, illustrated world.
5. **Scrapbook stickers** (rainbows, smileys, felt heart, gingham patch, bow, binder clip, paper clip): the product
   side's "whimsy" vocabulary (r3c2, r4c2, r5c3).
6. **Script + caps type pairing**: an expressive script word carrying the emotion ("Accessory", "Collection",
   "Wardrobe", "whimsy") locked against small geometric caps carrying the information ("PTAT's", "NEW … DROP",
   "YOUR … NEEDS MORE").
7. **Series naming**: "vol 1", "FIRST LOOK", "F.O.M.O · BOLLYWOOD EDITION", "New Collection Drop" with numbered looks.
   Every post title promises a sequel.

### A4. Grid-level system: why it reads as curated

- **Two blocks, two palettes, one hand.** Rows 1–2 (+ r3c1) are an **event takeover**: hot pink / marigold / crimson,
  maximal, every tile carrying the MILNI lockup. Rows 3–4 are **product/editorial**: baby pink, aqua, ivory, lilac,
  navy/burgundy type. What ties them is the hand: illustration over photo, cut-outs, script+caps type, stickers
  [observed]. A visitor scrolling sees "something is happening right now" (top) and "this is what the store is like"
  (below).
- **Event content in waves, not one poster.** MILNI is told as ~8 posts with distinct jobs: key art (r1c3), animated
  invite (r2c1), first look (r1c2), designer feature (r3c1), FOMO/nostalgia hook (r2c2), live crowd (r2c3), guest
  arrival (r1c1). Same lockup, different job each time [observed]. That is how one event fills two rows without
  repeating itself.
- **Checkerboard of weight.** Within each row, at least one tile is a dense graphic and one is a breathing photo/video
  (row 2: graphic, graphic, crowd video; row 3: photo, graphic, illustrated photo; row 4: graphic, graphic, video)
  [observed]. No row is three photos or three posters.
- **Colour fields are big.** Grounds are edge-to-edge single colours or patterns (hot pink, magenta print, baby-pink
  tartan, aqua stripe, ruled white), so each tile reads as one colour at thumbnail size and the grid becomes a colour
  rhythm [observed, confirmed by quantised colours above].
- **Type is legible at tile size only where it matters.** The wordmark/title is huge; logistics are tiny and in the
  corners [measured].
- **Interleave rule (inferred).** Product content never stops during the event: r3c1 is a product post *wearing* event
  branding, and r3c2 (Accessory Guide) sits directly beside it. The feed sells while it promotes.
- **Format mix**: ~45% Reels / 45% carousels / 10% single among the countable tiles: video for proof and texture, carousels
  for guides and lookbooks, one static for an index page [observed].

### A5. What transfers to Naira, and what collides (read with design-rules.md)

| PTAT device | Transfer? | Naira version (suggestion, not a decision) |
|---|---|---|
| One lockup repeated across an event series | **Yes, strongly** | A Naira festive/wedding lockup: the NAIRA wordmark with its flower-as-I, bracketed by Naira's own motifs (pressed blush petals, sage line-drawn botanicals, a spool or tailor's tape from the couture house) rather than marigolds and a mehndi hand |
| Multi-script title | **Yes, with care** | A single word said in several Indian scripts is a strong "Indian-pop" idea. Must be typeset by someone who reads each script (or verified glyph by glyph); a broken conjunct in a public post is worse than none. One word only, in Naira's palette |
| Vernacular idioms (truck-art, block print, Bollywood poster, steel thali) | **Partly** | The Naira brand bible caps festive cues at **one Indian cue per frame** and prefers **material** cues (khadi, brass, terracotta, raw silk, jaali) over **iconographic** ones (diyas, rangoli, marigolds). Quote one idiom per tile, choose material idioms: a brass tray instead of steel; a jaali shadow; a block-print ground in blush/sage |
| Photo cut-outs on graphic grounds | **Yes** | Jewellery cut-outs are small; follow the image skill's "isolation, not filling the frame" rule. Better: cut-out on-body crops (ear, hand, collarbone) on a Naira pattern ground |
| Line-drawn frame around a real photo (wardrobe) | **Yes, very on-brand** | Naira is a couture atelier from Nashik: a pen-drawn atelier (cutting table, dress form, mirror, thread spools) or a drawn jewellery box/drawer (the 3D Naira box exists on the site) with a real photo inside |
| Scrapbook stickers (smileys, rainbows, felt hearts) | **Mostly no** | Too young for a demi-fine line whose voice is "quiet, warm, hand-touched" (live examples price single pieces around ₹1,300–₹2,200: CLAUDE.md quotes ₹4,298 for two pieces and the Triple Coil bangle at ₹1,899/₹1,799; note CLAUDE.md's opening line says "₹24,000–44,000", which contradicts its own examples; check live prices before any price appears). Naira's equivalents: pressed flowers, a swatch card, a care label, a stitched tag, a wax seal, washi in sage |
| Script + caps type pairing | **Yes, already Naira** | Naira's rule is high-contrast serif caps (Velista) + an italic serif (Cormorant italic) counterpoint, Jost for labels. Same mechanism, Naira's faces |
| Series naming ("vol 1", "first look") | **Yes, already Naira** | Naira already numbers things: "VIII Lilac Hour", "VI Soft Matter", "Edition One/Two", "VOLUME ONE · … · № 24". Use numbered series in the feed |
| Hot-pink / acid-yellow maximal palette | **No** | Brand bible: never black-and-gold, never discount-loud. Naira's maximal end is blush + sage + ivory + gold at full saturation of *material* (raw silk, brass, terracotta) |
| Folio corners for logistics | **Yes** | Small Jost caps, top-left / top-right, kept out of the IG icon zone (top-right 16% x 14%) |
| Event in waves (key art → invite → first look → live → recap) | **Yes** | Naira's festive calendar (Karwa Chauth → Dhanteras → Diwali → Bhai Dooj → Tulsi Vivah / wedding season) can be told as one series the same way |

Brand-tension flag for the parent: the reference is maximalist pop; Naira's own documents describe the brand as
"quiet, warm, pale, botanical, hand-touched, unhurried" and **not** "loud, festive-maximalist" (brand bible,
imagegenerationnaira skill, 13 Jul 2026). The Up Close plan (creative/naira-campaign-upclose/PLAN.md, 1 Oct 2026)
rests on "quiet, detailed and owned is the loudest position available". Two honest options: (1) borrow PTAT's
*system* (series, lockup, illustrated frames, cut-outs, colour-field rhythm) inside Naira's palette; (2) push one
option further toward PTAT's energy (saturated blush/sage/gold, hand-lettering, collage) while keeping Naira's
never-list. Copying PTAT's palette or iconography would read as a different brand.

---

## B. Platform facts (Instagram, as of Oct 2026)

| Fact | Status | Source (date) |
|---|---|---|
| Profile grid thumbnails are **3:4** (portrait), changed from 1:1 in **January 2025** | Confirmed; also measured on the user's phone (391 x 521 px = 0.7505) | Kapwing (30 Dec 2025); Planoly (updated 31 Oct 2025); Hopper HQ (18 Sep 2026); MacRumors (9 Jun 2026) refers to the January 2025 switch. Buffer (26 Feb 2025) says 4:5; contradicted by all others and by the screenshot |
| Grid crops every post to 3:4 by centre-crop; the original is shown in full when tapped | Confirmed | Kapwing (30 Dec 2025); Planoly |
| **3:4 photo uploads (1080 x 1440)** supported natively for feed photos **and carousels** since **29 May 2025** | Confirmed (announcement); pixel size from secondary sources | Adam Mosseri on Threads, 29 May 2025: "Instagram now supports 3:4 aspect ratio photos – the format that almost every phone camera defaults to", reported by PetaPixel and 9to5Mac (29 May 2025), Business Today (2 Jun 2025) |
| Conflict: Kapwing (31 Dec 2025) says images taller than 4:5 are cropped, and lists only 4:5, 1:1, 1.91:1 | Conflicting; Kapwing's own example shows a 9:16 cropped to 3:4, which supports 3:4 | kapwing.com/resources/how-to-post-multiple-images-with-different-sizes-to-instagram |
| **Meta's content-publishing API** (used by schedulers) still states feed/carousel images "Must be within a 4:5 to 1.91:1 range", max width 1440, JPEG, up to 20 carousel items | Confirmed (fetched today) | developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media (25 Oct 2026) |
| 4:5 (1080 x 1350) posts lose ~34 px each side in the grid (1350 x 0.75 = 1012.5 wide) | Arithmetic; Planoly states 1013 x 1350 visible | Planoly |
| 1:1 (1080 x 1080) posts lose 135 px each side in the grid (shown 810 x 1080) | Arithmetic [inferred] | n/a |
| Reel covers 1080 x 1920 (9:16) are cropped to 3:4 (1080 x 1440) in the grid: **240 px lost top and bottom** | Confirmed | Hopper HQ, "Instagram Reel Size in 2026" (18 Sep 2026) |
| Reel UI safe zones on 1080 x 1920: top 14% (~270 px), bottom 35% (~670 px), right action rail ~21% wide over the bottom 40%, sides ~6%; centred safe area ~950 x 980 | Vendor guidance | Hopper HQ (18 Sep 2026) |
| Reels feed view shows 4:5 (1080 x 1350) of a 9:16 reel; keep in-video text inside the central 1080 x 1350 | Vendor guidance | Planoly (31 Oct 2025) |
| Reel cover **cannot be changed after posting** (fix = delete and re-upload) | **Conflicting / unverified**: Hopper HQ says so; I could not confirm an official statement. Test in-app before relying on it | Hopper HQ (18 Sep 2026) |
| "Adjust preview" (⋯ → Edit → Adjust preview) repositions a post's grid thumbnail after posting | Confirmed by three vendors | Kapwing; Buffer; Planoly |
| Carousels hold **up to 20** photos/videos (raised from 10) | Confirmed | Instagram announcement ~9 Aug 2024 via TechRadar, Social Media Today, Business Today (9 Aug 2024); Meta API docs (20 items) |
| Carousel aspect: **the first slide sets the ratio** for all slides unless the "Mixed" resize option is chosen; Portrait forces 4:5, Square forces 1:1 | Vendor-sourced; whether Mixed preserves 3:4 is unverified | Kapwing (30–31 Dec 2025) |
| **Grid reordering**: long-press a post → "Reorder grid" → drag. Rolling out to all users from **8 Jun 2026**; changes save immediately, visible to all; pinned posts stay on top | Confirmed | Social Media Today (8 Jun 2026); MacRumors (9 Jun 2026) |
| **Pin up to 3** posts/Reels at the top of the grid; a Reel must be shared to the grid to be pinnable | Confirmed (third-party guides; no Help Centre page retrieved) | Social Media Examiner; PhoneArena; MacRumors (9 Jun 2026) |
| Posting cadence: Buffer's study of 2.1M feed posts from 102K accounts finds **3–5 posts/week** the sweet spot; follower growth +0.12% at 1–2/week vs +0.26% at 3–5 vs +0.44% at 6–9; reach per post +~12% at 3–5 vs 1–2 | Correlational, vendor data | Buffer, "How Often Should You Post on Instagram in 2026?" (13 Aug 2025) |
| Other cadence guidance: 2–5 feed posts/week (HeyOrca survey), 3–5 feed + 2–4 Reels/week + near-daily Stories (Hopper HQ), 3–5 + 2–3 Stories/day (Kontentino) | Vendor guidance | via web search, 2026 pages |
| Meta's old "20% text" rule for ads | **Retired by Meta in 2020** [from prior knowledge, unverified this session]; skills that still cite it (banner-design, design) should be read as "less text tends to perform better", not a hard limit | n/a |

### B1. Recommended export spec for the feed (derived)

- **Master canvas: 1080 x 1440 (3:4)** for single images and every carousel slide; it fills the grid tile exactly and
  shows uncropped in the feed when posted **natively from the Instagram app** [sourced: Mosseri 29 May 2025].
- **If posting through a scheduler/API** (Meta Business Suite, Buffer, Later…): the API range is 4:5–1.91:1, so a
  3:4 file may be rejected or cropped to 4:5 (1080 x 1350) [sourced: Meta API docs]. Design so nothing essential sits in
  the top and bottom **45 px** of the 1440 canvas (1440 − 1350 = 90), and test one draft first. Alternatively export a
  4:5 twin (1080 x 1350) with the same composition.
- **Reels: 1080 x 1920**, custom cover uploaded at 1080 x 1920 with title, faces and product inside the **central
  1080 x 1440** (grid) and ideally inside **1080 x 1350** (Reels feed) [sourced: Hopper HQ, Planoly].
- Keep the **top-right ~16% x 14%** of every cover clear (format icon / "Just seen") [measured].
- Margins: ≥ 60–72 px from left/right edges for type (≈ 6% side strip, matching Naira's own ads "6% side-safe strip",
  creative/naira-ads/README.md).
- Grid legibility: a word meant to be read in the grid needs **≥ ~90–110 px font size** (≈ 65–75 px cap height) on the
  1080 canvas; logistics can be 34–44 px because they are read on tap [measured/inferred, see A1].
- JPEG quality ~92, 4:4:4 chroma (no subsampling) as Naira's ad pipeline already does (creative/naira-ads/README.md);
  sRGB.
- Carousel: keep every slide the same 3:4; slide 1 must work alone because it is also the grid tile (the repurposing
  table in the social-content-engine skill makes the same point).

### B2. Curated-grid practice (2026)

- **Plan in rows of three.** The grid is three columns; a 12-post plan = 4 rows, a 9-post plan = 3 rows. Each row
  should balance one dense graphic, one breathing photo/video and one middle-weight tile (PTAT pattern, A4).
- **Posting order no longer has to be reversed**: since the 8 Jun 2026 rollout the grid can be reordered after
  posting [sourced]. Still post the intended top-left last if possible so the newest-first chronology also makes sense
  in followers' home feeds (people see posts in time order there, not in grid order) [inferred].
- **Pins shift the plan.** Pinned posts occupy the first slots. Pinning 1 or 2 posts pushes every planned row one or
  two columns along; plan with **0 or 3 pins** (a full row), or design the pins into the plan [inferred from
  "Pinned posts continue to appear at the top regardless of any reordering", MacRumors 9 Jun 2026].
- **Puzzle grids (one image split across tiles)**
  - Pros: high visual impact on the profile; strong "takeover" moment; with reordering they no longer break when a
    single new post lands (the set can be dragged back into place) [inferred].
  - Cons: each tile must still work alone in followers' home feeds (most views happen there, not on the profile);
    every new post shifts alignment unless posted in multiples of 3 or reordered; the 3 px gutters and the 3:4 crop
    cut through anything spanning tiles; split tiles tend to under-perform as individual posts [inferred; vendor
    material found was promotional only (PostNitro, Griddy app listing) and gave no reliable data].
  - Better compromise: a **row lockup**, three self-contained posts that share one ground colour or pattern or a
    continuous line so the row reads as one, while each tile is complete on its own (PTAT does this with its event
    block without splitting any image).
- **Covers are part of the grid.** Every Reel needs a designed cover, because the grid shows the cover, not the video
  (Hopper HQ). PTAT's reels show either the lockup (r2c1, r2c3) or a strong composite (r3c3).
- **Cadence for a small D2C brand**: 3–4 feed posts a week, sustainable for a founder-led team [sourced: Buffer 3–5;
  social-content-engine skill calendar.md: "Owner plus an office manager: 3–4 posts a week"]. A 12-post grid is
  therefore ~3–4 weeks of feed; a 9-post grid ~2–3 weeks.
- **Theme mix** (social-content-engine skill, calendar.md): ~40% useful, ~30% proof, ~20% offer, ~10% people. For Naira,
  "proof" = macro/finish, craft and real customers; "offer" never on the image (Up Close never-list).

---

## C. Calendar: 25 Oct 2026 → 1 Jan 2027

Dates are for New Delhi unless noted. Hindu festival dates follow tithi and local sunrise and can shift a day by city or
tradition; **Drik Panchang is the primary source** where it could be fetched today.

| Date (2026) | Day | Occasion | Confidence / source |
|---|---|---|---|
| 24–25 Oct | Sat–Sun | PTAT's MILNI pop-up, Soho House Juhu (the reference) | from screenshot; year inferred |
| **29 Oct** | Thu | **Karwa Chauth** (moonrise 8:17 PM, New Delhi) | Drik Panchang (fetched 25 Oct 2026). Naira's Up Close plan notes "sources split 28/29 Oct" and keeps the date off images and copy: do the same |
| **6 Nov** | Fri | **Dhanteras** | Drik Panchang (Diwali puja calendar, fetched 25 Oct 2026) |
| 7 Nov | Sat | Chhoti Diwali per several secondary sources | Drik lists Narak Chaturdashi on **8 Nov**; secondary sources say 7 Nov. Conflicting; avoid naming it |
| **8 Nov** | Sun | **Diwali / Lakshmi Puja** (also Narak Chaturdashi per Drik) | Drik Panchang; agreed by kissht.com, Aza Fashions blog and others. (bankbazaar pages give Oct dates and are wrong) |
| **10 Nov** | Tue | **Govardhan Puja** (Pratipada 12:31 PM 9 Nov – 2:00 PM 10 Nov) | Drik Panchang. Some secondary sources say 9 Nov |
| **11 Nov** | Wed | **Bhai Dooj** | Drik Panchang; matches Up Close plan ("Bhai Dooj, Wed 11 Nov"). Some secondary sources say 10 Nov |
| 14 Nov | Sat | Children's Day (India, fixed: Nehru's birth anniversary) | fixed date |
| **15 Nov** | Sun | **Chhath Puja** (Drik lists 15 Nov; Shashthi tithi 11:23 PM 14 Nov – 2:00 AM 16 Nov). Sandhya Arghya evening of 15 Nov; Usha Arghya at sunrise 16 Nov [inferred] | Drik Panchang |
| 20 Nov | Fri | Dev Uthani / Prabodhini Ekadashi (end of Chaturmas) | Hindutone citing Drik; SmartPuja says 19 Nov. Conflicting |
| **21 Nov** | Sat | **Tulsi Vivah** (Dwadashi 6:31 AM 21 Nov – 4:56 AM 22 Nov) = **wedding season opens**; also the first vivah muhurat | Drik Panchang (fetched 25 Oct 2026) |
| **24 Nov** | Tue | **Kartik Purnima / Dev Deepawali** (Varanasi) / **Guru Nanak Jayanti** | Hindutone (citing Drik), SmartPuja, HappyFares; one travel blog says 25 Nov. Not fetched from Drik directly |
| 21, 24, 25, 26 Nov | Sat, Tue, Wed, Thu | **Vivah muhurat dates, November** (1–20 Nov "prohibited, Chaturmas") | Drik Panchang shubh marriage dates (fetched 25 Oct 2026); matches VedicFeed, SmartPuja, Bluestone |
| 2, 3, 4, 5, 6, 11, 12 Dec | Wed–Sun, Fri–Sat | **Vivah muhurat dates, December** (7 days) | Drik Panchang. The Wedding Focus lists 1–4, 11–13 Dec instead: minor conflict |
| mid-Dec → mid-Jan | | No muhurats after 12 Dec in Drik's list; the Kharmas pause (Sun in Sagittarius) usually runs to Makar Sankranti (~14/15 Jan) | [inferred from Drik list; Kharmas dates unverified] |
| 25 Dec | Fri | Christmas | fixed |
| 31 Dec / 1 Jan 2027 | Thu / Fri | New Year's Eve / New Year: party-season dressing, sequins, "first piece of the year" gifting | fixed |

Planning reads [inferred]:
- **Gifting peak** is now → 8 Nov (Karwa Chauth gifts from husbands, Dhanteras, Diwali, then Bhai Dooj gifts to sisters
  on 11 Nov). Courier cut-offs are not confirmed, so no "order by" dates on images (Up Close rule).
- **Dhanteras is a gold/metal-buying day**: Naira's pieces are plated/coated, so no "buy gold" framing (Up Close
  never-list; CLAUDE.md: copy must say "18K gold tone & rhodium plated", never "18K gold" alone).
- **Wedding season** (21 Nov → 12 Dec) is guest-dressing season: sangeet, mehendi, cocktail, reception; demi-fine fits the
  *guest*, not the bride's heirloom set.
- **A 12-post feed at 3/week** starting Tue 27 Oct runs to ~Sun 22 Nov and covers Karwa Chauth → Dhanteras → Diwali →
  Bhai Dooj → Children's Day → Tulsi Vivah. A 9-post feed at 3/week ends ~15 Nov (misses the wedding-season opening).

---

## D. Exemplar feeds

Method note: the instagramprofilefinder skill requires live browsing in the user's logged-in Chrome and forbids
answering from memory. No browser was available in this session, so **no feed below was viewed live**. Each entry
separates sourced background from the analyst's read of the brand's known visual device; treat the device column as
**[unverified-live]** until someone scrolls the actual grid. Ad-side facts come from the Meta Ad Library harvest in the
imagegenerationnaira skill (`references/ad-formats.md`, 401 ads, 24 advertisers, 13 Jul 2026).

| Brand | Sourced background | The device that makes the feed work (unverified-live) | What Naira could borrow without copying |
|---|---|---|---|
| **Missoma** (UK demi-fine) | Instagram described by founder Marisa Hordern as the main channel; Lucy Williams collabs (three sell-out collections), Instagram Shops with "Lucy Williams Collection" (Instagram Business success story; Marie Claire; Fashion Network). Ad harvest: owns terracotta, deep olive, ink-blue, chalk colour blocks (ad-formats.md) | **Owned colour fields** + layered "stack" close-ups on skin; muse-led collections as a recurring series | Own blush/sage/ivory as full-bleed fields (Missoma proves colour = recall). A muse series: one real Naira customer or the couture-house founder styling one piece per post |
| **Mejuri** (CA) | UGC on branded hashtags (#thefinecrew, #moregold) with "User Submissions" terms (Fera blog); ad harvest: 15-card "Shop Solid Gold" catalogue carousels, "Jewelry You Can Win In" permission hooks | Everyday skin crops, imperfect real-life light, UGC woven with brand shots; the message is "wear it daily" | A rights-cleared customer series ("worn, not saved" is already an Up Close line). Honest skin texture, no glam retouching |
| **Laura Lombardi** (Brooklyn, est. 2010) | Art-school/sculpture background; handcrafted from repurposed and recycled metal (Kindred Black; Passerby; retailer copy) | Sculptural still lifes: chunky gold placed among found objects, fruit, stone, film grain | Naira's "made, not expensive" still-life direction (clay thumbprint, khadi dent, cardamom pod) as a feed series |
| **Sophie Buhai** (LA) | Sterling silver, modernist/sculptural; designed jewellery for Lemaire 2015–17; "Jewelry Objects" book with Galerie Anne-Sophie Duval (Wikipedia; CFDA Jul 2026) | Museum-object framing: one piece, plinth, art-historical restraint, objects as artworks | One-piece "specimen" posts on a plinth or in a drawn vitrine; numbered like an exhibition catalogue (Naira already has "Edition" numbering) |
| **Jacquemus** (FR) | Apr 2023 Instagram video of giant Le Bambino bags driving through Paris, a 3D render by Ian Padgham ("I think I like Paris now"); popularised "faux out-of-home"; preceded by a Galeries Lafayette pop-up with oversized props (Retail Boss, T2 Online, Atlantic Sun). View-count claims unverified | **Scale play and surreal props**: the product made monumental in a real place; a feed of sun-drenched pastoral moments | Naira already owns a 3D box on its site (NairaBox3D). A "giant Naira box in a Nashik street / on a ghat" FOOH Reel is the Naira-scale version, but only as one hero moment. Never fake a real event or location claim |
| **Bhaane** (IN) | Creative director Nimish Shah; "doesn't do logos", "live simple"; AW22 Mahabharata collection with hyper-pixelated motifs, shot by Rid Burman (Elle India; Homegrown) | Graphic, witty campaigns that re-read Indian myth and nostalgia in a contemporary street register | Re-read one Indian story per series with wit (the Up Close "THE KING FELL." chess line is this instinct) rather than iconography |
| **Nicobar** (IN, Eicher Goodearth) | Founded Mar 2016 by Simran Lal and Raul Rai; "island" aesthetic of the Indian Ocean; stamped tiger/tent illustrations on travel bags; store designed with Instagram in mind; Nicobar Journal (nicobar.com press pages; Khaleej Times) | An illustrated world + travel-journal storytelling: the brand as a place you visit | A Naira "atelier journal" voice: the Nashik studio as the place; illustrated maps/sketches of the couture house |
| **Outhouse** (IN, Kaabia & Sasha Grewal) | Launched Oct 2011 (some say 2012), Noida; "distinct monograms and edgy designs"; "cosmopolitan tribalism"; Alia Bhatt wore custom OH Jewellery at the Met Gala; 5th store in Goa 2025 (YourStory; Fashion Network; Elle India) | Dramatic, high-contrast editorial portraits; jewellery as performance and power; a recognisable monogram | Not the drama (off-brand), but the **recurring mark**: Naira's flower-as-I is a monogram waiting to be used as a consistent seal/stamp |
| **Misho** (IN, Suhani Parekh) | Goldsmiths fine art/sculpture background; "wearable sculpture"; architectural, geometric forms; Araku coffee collab (2022); 'Volume One' RTW capsule Mar 2026 (Harper's Bazaar India Nov 2025; Fashion Network) | Gallery-like restraint: sculptural forms on stark grounds, art-world references | Brand bible calls Misho the "nearest reference point (Indian craft, Western restraint). Study it; don't copy it." Borrow the *volume numbering* and gallery pacing, not the minimal palette |
| **Bluorng** (IN streetwear, 2020) | Founded by Siddhant Sabharwal and Mokam Singh; GQ India Streetwear Label of the Year 2023; stores "monotone, simple and brutalist, so the products do the talking" (Confetti audit; Indian Retailer) | Product-forward, high-production 3D and campaign imagery; the CLAUDE.md notes the site's bag spins at Bluorng's pace | The product-as-object hero: Naira's 3D box turning as a Reel cover series ("tap to open" becomes "swipe to open") |
| **Tyaani** (IN fine jewellery, Karan Johar) | Polki/uncut diamond house; "Forces of Tyaani" ambassador series from Sep 2025: Jim Sarbh, Kusha Kapila, Zeenat Aman, Kalki Koechlin, Shefali Shah and others (Impact; exchange4media; Media Infoline) | Personality-led portrait series with one framing device across many faces | The *series grammar* (one frame, many people) for real Naira customers or the women of the atelier, without celebrity spend |
| **Lovebirds** (IN, Gursi Singh & Amrita Khanna) | Delhi label rooted in Indian craft; Singh a former graphic and space designer; 10th-anniversary "warm, moody montage" on Instagram (Harper's Bazaar India Dec 2024); LFW SS27 on Indian cultural memory (T2 Online) | Graphic-designer eye: considered type and montage, whimsy with restraint | Montage/collage carousels in a strict palette: proof that whimsy can be adult |
| **The Summer House** (IN, Bengaluru, Feb 2015) | Shivangini Padhiyar & Rekha Datla; 17 craft clusters; organic cotton, handwoven linen, khadi (Platform; YourStory; Good On You) | Craft-cluster storytelling, maker-first, earthy natural light | "Show the hands" (ad-formats.md gap #1): maker and material posts, khadi and thread as surfaces |
| **Pipa Bella** (IN fashion jewellery, Nykaa, 2013) | Acquired by Nykaa Fashion Apr 2021; 1,500+ styles; Rhea Kapoor collab 2023 priced ₹3,995–₹9,995; ~327k followers per an aggregator (unverified) | Contrast case: high-volume product tiles and trend edits | What to avoid: catalogue-grid sameness |
| **Palmonas** (IN demi-fine, Pune) | Stainless steel / sterling with 18K gold vermeil, "100% safe to wear in water", lifetime buyback; Shraddha Kapoor co-founder after an Instagram comment (Entrepreneur India; Outlook Business). Ad harvest: 18 live variants of a "9KT" explainer tile; heavy DPA and price tiles (ad-formats.md) | Contrast case: celebrity + claim-led tiles + offer tiles | What to avoid: material claims in type, price flashes. Naira's answer is proof by macro, not claim by type |

Cross-cutting lessons [inferred, consistent with ad-formats.md PART D "The Gap"]:
1. The feeds people remember **own one colour story** and **repeat one framing device**.
2. Series beat singles: muse collections (Missoma), ambassador frames (Tyaani), volume numbers (Misho, PTAT "vol 1").
3. In Indian demi-fine, nobody shows the making, nobody runs macro texture, nobody decouples festive from red-and-gold
   (ad-formats.md, 401 ads, 13 Jul 2026): the feed is where Naira can show all three.

---

## Sources (all accessed 25 Oct 2026)

- Project Tête-à-Tête: https://projectteteatete.com · https://lbb.in/places/Project-TeteATete-khar-0b03b2
- Soho House Mumbai: https://www.wallpaper.com/travel/india/mumbai/hotels/soho-house · https://www.dezeen.com/2018/12/10/soho-house-mumbai-india-interior-design-textiles/amp/
- 3:4 grid and uploads: https://www.kapwing.com/resources/instagrams-new-grid-layout-size-and-dimensions-2025/ · https://www.kapwing.com/resources/how-to-post-multiple-images-with-different-sizes-to-instagram/ · https://planoly.com/blog/guide-to-instagrams-new-vertical-grid · https://buffer.com/resources/instagram-grid/ · https://petapixel.com/2025/05/29/instagram-finally-adds-support-for-34-aspect-ratio-photos · https://9to5mac.com/2025/05/29/instagram-changes-standard-photo-aspect-ratio/ · https://www.businesstoday.in/technology/news/story/no-need-to-crop-your-photos-as-instagram-now-supports-34-aspect-ratio-for-photos-478651-2025-06-02
- Meta API image spec: https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media
- Reels sizes: https://www.hopperhq.com/blog/instagram-reel-size/
- Carousels 20: https://www.techradar.com/computing/instagram/instagram-will-now-let-you-post-up-to-20-photos-or-videos-in-a-gallery-your-friends-should-be-thrilled · https://www.socialmediatoday.com/news/instagram-expands-carousels-to-20-frames/723792/
- Grid reorder: https://www.socialmediatoday.com/news/instagram-releases-profile-grid-rearranging/822304/ · https://www.macrumors.com/2026/06/09/instagram-now-lets-users-reorder-posts/
- Pins: https://www.socialmediaexaminer.com/instagram-marketing-how-to-pin-posts-and-reels-to-a-profile/ · https://www.phonearena.com/news/instagram-now-lets-you-pin-posts-and-reels-to-your-profile_id140634
- Cadence: https://buffer.com/resources/how-often-to-post-on-instagram/ · https://www.heyorca.com/blog/social-media-posting-frequency-by-platform-2026 · https://www.hopperhq.com/blog/instagram-posting-frequency-2026/
- Calendar: https://www.drikpanchang.com/diwali/diwali-puja-calendar.html?year=2026 · https://www.drikpanchang.com/festivals/karwa-chauth/karwa-chauth-date-time.html?year=2026 · https://www.drikpanchang.com/festivals/govardhan-puja/govardhan-puja-date-time.html?year=2026 · https://www.drikpanchang.com/festivals/chhath-puja/chhath-puja-date-time.html?year=2026 · https://www.drikpanchang.com/festivals/tulasi-vivah/tulasi-vivah-date-time.html?year=2026 · https://www.drikpanchang.com/shubh-dates/shubh-marriage-dates-with-muhurat.html?year=2026 · https://hindutone.com/festivals/dev-deepawali-2026-date-time-significance-celebration/ · https://www.smartpuja.com/blog/vivah-muhurat-2026-marriage-dates · https://theweddingfocus.com/blog/wedding-dates-2026/
- Exemplars: https://business.instagram.com/success/missoma/ · https://www.marieclaire.co.uk/fashion/shopping/meghan-markle-lucy-williams-missoma-594423 · https://fera.ai/blog/posts/leverage-user-generated-content-boost-sales-examples · https://kindredblack.com/blogs/journal/laura-lombardi · https://en.wikipedia.org/wiki/Sophie_Buhai · https://cfda.com/news/sophie-buhai-reimagines-art-deco-design-with-jewelry-objects-debut/ · https://retailboss.co/giant-jacquemus-handbags-in-paris-3d · https://t2online.in/goodlife/fashion-beauty/jacquemus-s-giant-sized-le-bambino-bags-on-wheels-become-the-traffic-you-d-not-mind-stopping-in/377449 · https://homegrown.co.in/homegrown-explore/bhaane-s-collection-is-nostalgia-wrapped-in-a-distinctly-indian-identity · https://global.nicobar.com/blogs/press-story/where-culture-meets-commerce · https://www.khaleejtimes.com/lifestyle/fashion/island-vibes-in-india · https://yourstory.com/ys-life/distinct-monograms-edgy-designs-outhouse-jewellery · https://www.harpersbazaar.in/women-of-the-year-awards-2025/story/bazaarwomeninfocus-suhani-parekh-is-sculpting-the-future-of-modern-jewellery-couture-one-design-at-a-time-1302689-2025-11-12 · https://confetti.design/audit/bluorng-brand-audit · https://www.impactonnet.com/more-from-impact/zeenat-aman-leads-new-tyaani-jewellery-campaign-forces-of-tyaani-11900.html · https://harpersbazaar.in/fashion/story/gursi-singh-and-amrita-khannas-lovebirds-celebrates-togetherness-with-modern-minimalist-design-1140240-2024-12-21 · https://www.platform-mag.com/fashion/the-summer-house.html · https://yourstory.com/2021/04/nykaa-acquires-online-jewellery-brand-pipa-bella/amp · https://india.entrepreneur.com/news-and-trends/shraddha-kapoor-roped-in-as-co-founder-by-demi-fine/470703
- Internal: imagegenerationnaira skill (brand-bible.md, ad-formats.md, 13 Jul 2026); /home/user/naira-scroll/creative/naira-campaign-upclose/PLAN.md (1 Oct 2026); /home/user/naira-scroll/creative/naira-ads/README.md; /home/user/naira-scroll-3790bf3e/CLAUDE.md; /home/user/naira-scroll-3790bf3e/docs/design-tokens.md
