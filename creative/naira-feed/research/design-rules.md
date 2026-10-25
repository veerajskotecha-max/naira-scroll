# Design rules for Naira Instagram feed graphics

Every rule from the listed skills that applies to designing Instagram feed graphics for a premium demi-fine jewellery
brand, with its source. Compiled 25 Oct 2026.

Source keys (all read in full this session unless marked):

| Key | File |
|---|---|
| `[img-naira]` | skills/synced/…/imagegenerationnaira/SKILL.md (file is **truncated mid-sentence at line 137**: the text after the fidelity-lock section is missing) |
| `[img-naira/bible]` | …/imagegenerationnaira/references/brand-bible.md ("observed live from nairaflore.com, 13 Jul 2026") |
| `[img-naira/ads]` | …/imagegenerationnaira/references/ad-formats.md (Meta Ad Library harvest, 401 ads, 24 advertisers, 13 Jul 2026) |
| `[img-naira/tested]` | …/imagegenerationnaira/references/tested-prompts.md |
| `[img-naira/mods]` | …/imagegenerationnaira/references/modifier-banks.md |
| `[catalogue]` | …/cataloguerating/SKILL.md + references/brand_and_layout.md + rating_framework.md |
| `[banner]` | …/banner-design/SKILL.md + references/banner-sizes-and-styles.md |
| `[design]` | …/design/SKILL.md + references/social-photos-design.md |
| `[design-system]` | …/design-system/SKILL.md |
| `[impeccable]` | …/impeccable/SKILL.md + reference/craft-floor.md, new-work.md, bolder.md, typeset.md, colorize.md, delight.md |
| `[uupm]` | …/ui-ux-pro-max/SKILL.md + references/quick-reference.md, pro-rules.md (+ a local style-database search, below) |
| `[ui-styling]` | …/ui-styling/SKILL.md + references/canvas-design-system.md |
| `[emil]` | …/emil-design-eng/SKILL.md |
| `[brand]` | …/brand/SKILL.md + references/visual-identity.md, consistency-checklist.md, approval-checklist.md, logo-usage-rules.md, voice-framework.md, messaging-framework.md, color-palette-management.md, typography-specifications.md |
| `[igfinder]` | …/instagramprofilefinder/SKILL.md |
| `[frontend]` | /mnt/skills/public/frontend-design/SKILL.md |
| `[canvas]` | /mnt/skills/examples/canvas-design/SKILL.md |
| `[brand-guidelines]` | /mnt/skills/examples/brand-guidelines/SKILL.md (**Anthropic's** brand: not applicable, see §12) |
| `[sce]` | plugins/…/small-business/skills/social-content-engine/SKILL.md + reference/calendar.md, gotchas.md (+ shared/voice-profile.md) |
| `[strategy]` | …/small-business/skills/content-strategy/SKILL.md + reference/gotchas.md |
| `[brand-style]` | …/small-business/skills/brand-style/SKILL.md |
| `[canva]` | …/small-business/skills/canva-creator/SKILL.md + reference/gotchas.md |
| `[content]` | plugins/…/marketing/skills/content-creation/SKILL.md |
| `[review]` | …/marketing/skills/brand-review/SKILL.md |

Project sources (not skills, but binding on Naira output, so included and labelled):
`[tokens]` = /home/user/naira-scroll-3790bf3e/docs/design-tokens.md · `[claude-md]` = /home/user/naira-scroll-3790bf3e/CLAUDE.md ·
`[upclose]` = /home/user/naira-scroll/creative/naira-campaign-upclose/PLAN.md (1 Oct 2026) ·
`[ads21]` = /home/user/naira-scroll/creative/naira-ads/README.md · `[poster]` = /home/user/naira-scroll/creative/naira-exhibition-poster/poster.py ·
`[ref]` = research/reference-and-platform.md (this sweep).

---

## 0. Precedence (read first)

1. **The brief and the brand win over generic skill taste.** "The brief wins. Honor pinned aesthetics, eras, materials,
   fonts, and palettes even when they conflict with a saturated-pattern warning" `[impeccable]`. "Where the brief pins
   down a visual direction, follow it exactly — the brief's own words always win" `[frontend]`.
2. **A pinned world pins the world, not its softest rendition**: "the pinned world's full material range stays in play,
   and a rendition that matches what any model ships for that world failed the self-check" `[impeccable/new-work]`.
   For Naira this means: cream + Cormorant + italic is pinned, but the feed must reach into the brand's full material
   range (raw silk, brass, terracotta, khadi, jaali light, deep sage, pressed flowers, the couture house's spools and
   swatches), not just "warm cream + serif".
3. **Project truth beats creative ambition**: never invent prices, discounts, stock or product claims `[sce]`
   `[canva]` `[impeccable/new-work]` `[review]`.

### Conflicts between sources, and the resolution used

| Conflict | Sources | Resolution |
|---|---|---|
| Eyebrow / kicker above a heading is "a ban, not a default: no brief earns it back" vs Naira's own system specifies a tiny letter-spaced caps eyebrow | `[impeccable/craft-floor]`, `[frontend]` (calls tracked ALL-CAPS eyebrows a generated-design tell) vs `[img-naira/bible]`, `[catalogue]`, `[poster]`, `[upclose]` ("Jost is capped at two support lines plus at most one eyebrow") | Brand wins (precedence 1), but use it **sparingly**: at most one eyebrow per post, only when it carries information (series name, edition number, date), never as decoration on every tile |
| Middle-dot meta strings ("A · B · C") flagged as a generated-design tell | `[frontend]` vs `[catalogue]` (voice rule: use a middot instead of em-dashes), `[img-naira/bible]` ("VOLUME ONE · SPRING · MMXXVI · № 24") | Brand wins; keep middots for genuine metadata lines only, not as a stylistic tic in headlines |
| Numbered markers (01 / 02 / 03) only when the content is a sequence | `[impeccable/craft-floor]`, `[frontend]` | Agree. PTAT's [01]–[04] are legitimate because they key a legend `[ref A2 r4c1]`. Naira's edition/volume numbers are legitimate (they are a series) |
| Cormorant is on impeccable's list of "training-data default" faces | `[impeccable/new-work]` vs `[tokens]`, `[catalogue]` (Cormorant Garamond is the brand's editorial face) | Brand wins: Velista display + Cormorant italic + Jost are pinned |
| Warm cream ground + high-contrast serif + terracotta accent is the #1 "AI default" look; the terracotta near #D97757 reads as a tell | `[frontend]`, `[impeccable/new-work]` vs brand bible coral accent `#E79C82` | Keep the brand's cream and serif (pinned) but **do not lean on coral/terracotta as the accent**; let gold, sage and blush carry accents, and vary grounds (deep sage, blush field, raw silk, brass) so the grid is not a wall of cream |
| "Thin fonts preferred, light weights 200–300" | `[ui-styling/canvas-design-system]`, `[canvas]` ("Most of the time, font should be thin") vs grid legibility at 36% scale `[ref B1]` | Thin is fine at display sizes; anything that must read in the grid is ≥ 90–110 px on the 1080 canvas and Jost labels ≥ 300 weight at ≥ 34 px |
| "One CTA per banner, bottom-right, min 44 px, action verb" | `[banner]` | For organic feed posts the CTA is the caption / link sticker / product tag, not a drawn button. Naira's existing CTA style, if one is drawn, is a "solid charcoal rectangle, letter-spaced caps" `[img-naira/bible]`, **with radius 0** `[tokens]` |
| "Text under 20% for ads (Meta penalizes)" | `[banner]`, `[design]` | Meta retired the 20% rule in 2020 [prior knowledge, unverified this session]. Treat as guidance: thumbnails read better with little text |
| Instagram post 1080 x 1080 / carousel 1080 x 1350 | `[banner]`, `[design/social-photos]`, `[img-naira]` (aspects 4:5 feed, 1:1 grid) | **Out of date**: the grid is 3:4 since Jan 2025 and 3:4 uploads are native since 29 May 2025 `[ref B]`. Master at **1080 x 1440** |
| Palette hex values differ across Naira's own documents | `[tokens]` vs `[catalogue]` vs `[img-naira/bible]` vs `[poster]` | Use `[tokens]` (shipped site, extracted 4 Aug 2026) as the base; see §1 for the reconciled table |
| Price on creative | `[img-naira/ads]` ("the colour-block hero never carries a price") and `[upclose]` (no offer, code or percentage on any image) vs `[ads21]` (five of 21 ads carry a price) | Feed default: **no price, no code, no percentage on the image**. A price, if ever shown, comes from Shopify that day `[sce]` |
| Festive cues | PTAT reference (marigolds, mehndi hand, truck-art) vs `[img-naira/bible]` ("one Indian cue per frame, max; prefer material over iconographic") and `[img-naira/ads]` gap #6 ("decouple festive from red-and-gold") | Brand rule holds. One Indian cue per frame, preferably material (brass, khadi, raw silk, jaali, terracotta). If an option deliberately goes more "Indian-pop", it still uses one idiom per tile and the Naira palette |

---

## 1. Brand foundation

### 1.1 Palette (reconciled)

Base = the shipped site tokens `[tokens]`; other documents' values listed so nothing drifts.

| Role | Site token `[tokens]` | Catalogue `[catalogue]` | Image bible `[img-naira/bible]` | Exhibition poster `[poster]` |
|---|---|---|---|---|
| Ground (ivory/cream) | `--nf-ivory #FBF3EC` | Cream `#FFF8F5` | `#F4F0E8` | cream text `#F6EFE6` |
| Pressed-linen ground | `--nf-ivory-deep #F4EBE2` | cream row `#FFF3EE` | Blush wash `#FBEDE9` | |
| Ink | `--nf-ink #1A1614` | Ink `#1A1614`, Ink-60 `#6E6863` | `#1C1C1C` | |
| Sage | `--nf-sage #99B4AF`; logo sage `hsl(162 14% 61%)` ≈ `#8EA9A1`; deep `hsl(162 18% 38%)` ≈ `#4F7268` | Sage `#99B4AF`, deep sage `#7A9D97`, tint `#C8D8D4` | `#A9BCAD` | deep-sage ground `#2E4238 → #4C6A5C` |
| Blush | `--nf-blush #FFBDA8` | Blush `#FFBDA8`, light `#FFE4DA` | dusty rose `#F2CFC4` | `#F2CFC4` |
| Gold | `--nf-gold #C99A4C`, `--nf-gold-deep #B0843A`, `--nf-gold-shadow #9A7634` | | metal `#C9A55C → #E4C889` | `#E7C27A` |
| Accent (use sparingly) | | | coral `#E79C82` | |

Palette rules:
- Backgrounds live in the cream → blush band; never pure white ("marketplace code"), never grey, never black ("Cartier's
  code") `[img-naira/bible]`. Exception already used by the brand: a **deep-sage** ground for an event poster `[poster]`.
- Sage is the only cool note, secondary only `[img-naira/bible]`. Coral/apricot as a single accent, sparingly
  `[img-naira/bible]` (and see §0: avoid it as the dominant accent).
- Gold renders warm-neutral, never brassy or orange: "Orange gold is the #1 tell of cheap AI jewellery"
  `[img-naira/bible]`; "gold is the only saturated element in frame" (house constant) `[img-naira/ads]`.
- No cool/blue grade, no teal-orange grade `[img-naira/bible]`. The old off-palette teal `hsl(186 35% 28%)` is debt on the
  site; never reintroduce it `[claude-md]`.
- Sharp corners: radius stays 0 on brand surfaces `[tokens]` `[claude-md]`.
- Limited palette, 2–5 colours per composition, each with a purpose `[ui-styling/canvas-design-system]` `[canvas]`;
  60/30/10 primary/secondary/accent ratio `[brand/approval-checklist]`.
- Pick a colour strategy before picking colours: Restrained / Committed (one colour carries 30–60%) / Full palette /
  Drenched; Persuade surfaces may take the bolder strategies; "colour commits at page scale: fields that own whole
  regions, not accents scattered" `[impeccable/new-work]` `[impeccable/colorize]`. Owning a colour field is also what
  makes Missoma/Monica Vinader recognisable; "nobody [in India] owns a colour… Naira Petite's blush / cream / sage is
  already a moat" `[img-naira/ads]`.

**Measured contrast (WCAG) for the palette** (computed this session; 4.5:1 normal text, 3:1 large text
`[uupm]` `[impeccable/craft-floor]` `[brand]`):

| Foreground on ground | Ratio | Use |
|---|---|---|
| ink `#1A1614` on ivory `#FBF3EC` | 16.4 | any text |
| ink on sage `#99B4AF` | 8.1 | any text |
| ink on blush `#FFBDA8` | 11.2 | any text |
| ink on gold `#C99A4C` | 7.0 | any text |
| ink-60 `#6E6863` on ivory | 5.0 | small secondary text |
| gold-shadow `#9A7634` on ivory | 3.8 | large text only (≥ 24 px bold / ≥ 32 px regular at 1080) |
| gold-deep `#B0843A` on ivory | 3.1 | large text only |
| gold `#C99A4C` on ivory | 2.3 | **decoration only** (hairlines, dots), never text |
| sage `#99B4AF` on ivory | 2.0 | **decoration only** |
| blush `#FFBDA8` on ivory | 1.5 | **decoration only** |
| ivory on sage `#99B4AF` | 2.0 | **fails**: no white type on mid-sage |
| ivory on deep sage `#4F7268` | 4.9 | text OK |
| cream `#F6EFE6` on poster sage `#2E4238` | 9.4 | text OK |
| gold `#E7C27A` on `#2E4238` | 6.4 | text OK |
| blush `#F2CFC4` on `#2E4238` | 7.4 | text OK |
| gold `#E7C27A` on ink | 10.6 | text OK |

Note: the website wordmark is in `--nf-sage` on ivory (2.0:1); acceptable for a logo, not for words that must be read
`[inferred]`.

### 1.2 Type

- Display: **Velista** (true display face; not redistributable, "must not be re-sourced into the skill") → fallback
  Cormorant Garamond `[catalogue]` `[tokens]`. Editorial/italic voice: **Cormorant Garamond Italic**. Labels, eyebrows,
  specs: **Jost** Light 300 / Regular 400 / Medium 500 `[catalogue]` `[tokens]`.
- Headlines: large high-contrast serif caps + an italic serif lower-case counterpoint (`SOFTLY, SLOWLY,` / *worn.*)
  `[img-naira/bible]`. In practice: "one Velista line and/or one lowercase Cormorant turn" `[upclose]`; "Velista 400
  display, Jost 300 support" `[ads21]`.
- Jost caps eyebrows use wide tracking (~0.3–0.55em); Cormorant titles are title- or sentence-case, "never all-caps
  shouting" `[catalogue]`. Site tracking ladder 0.04–0.5em; label typography 0.18–0.5em `[tokens]`.
- Jost is capped at two support lines plus at most one eyebrow per creative `[upclose]`.
- Max 2 typefaces per graphic `[banner]`; one or two families, clearly distinct `[frontend]`. Naira's three roles
  (Velista / Cormorant italic / Jost) is the brand's sanctioned exception; never add a fourth.
- Avoid the generated-page tells unless the brand pins them: accenting a single word in italic/colour in every headline,
  all-caps labels everywhere, labels nobody needs `[frontend]`. Naira pins the italic counterpoint, so use it as the
  signature, not on every tile.
- Type as an active part of the design, not a neutral vehicle `[frontend]`; "typography actually part of the art"
  `[canvas]`.
- Scale steps must be obvious; display max ~6rem in UI terms; tracking floor −0.04em; balanced headings
  `[impeccable/craft-floor]`; "decisive contrast" between roles on Persuade surfaces `[impeccable/typeset]`.
- Min sizes at 1080 px: headline ≥ 48 px, sub 32, body 24, caption 18, CTA 28 `[design/social-photos]`; headline ≥ 32,
  body ≥ 16, max 7 words a line, 3 lines for ads `[banner]`. **Stricter for the 3:4 grid** (rendered at 36%): words that
  must read in the grid ≥ 90–110 px; logistics ≥ 34 px `[ref A1/B1]`.
- Use a system/fallback display face is a failure: "Source and self-host a face whose character matches" `[impeccable/craft-floor]`.
  For renders: Velista only if the licensed file is available locally; otherwise Cormorant Garamond (bundled in
  cataloguerating/assets/fonts) `[catalogue]`. Found this session: the site ships `public/fonts/Velista.ttf` and
  `Velista.woff2` in /home/user/naira-scroll-3790bf3e (and Velista.ttf in /home/user/naira-scroll), which is what Naira's
  own ad/poster builds use; Jost 400/500 and Cormorant 400 italic woff2 are in creative/naira-bag/fonts. Use them for
  internal renders; do not redistribute the Velista file `[catalogue]`.
- Tabular figures for prices/dates if numerals align in a column `[uupm]`.
- Multi-script lettering (PTAT-style) must be verified glyph by glyph by a reader of each script before posting
  `[ref A5]` (no skill covers Indic shaping; this is a project rule).

### 1.3 Motifs and marks

- Wordmark: NAIRA, high-contrast Didone/serif, wide spacing, sage; the flower displaces the I `[img-naira/bible]`
  `[claude-md]`. Show the wordmark **once** per creative; the logo flower may appear only as a ghost (~12%) elsewhere
  `[upclose]`.
- Logo on cream: the mark file is sage + blush on pure white; swap near-white to cream before placing, or the white box
  shows `[catalogue]`.
- Logo usage: clear space = height of the mark; don't stretch, recolour outside the palette, add effects or place on busy
  grounds `[brand/logo-usage-rules]`; correct brand assets only `[uupm/pro-rules]`.
- Background motifs: pressed-flower silhouettes, botanical line-art, faint architectural grid, oversized ghosted
  numerals `[img-naira/bible]`.
- Couture-house props are fair game: spool, swatch, care label, pattern key `[upclose]`.
- One consistent icon/illustration language: same stroke weight, filled vs outline discipline, drawn SVG, never emoji
  or Unicode glyphs as icons `[uupm]` `[uupm/pro-rules]` `[impeccable/craft-floor]`.

### 1.4 Voice (on-image and caption)

- Editorial, intimate, quiet. "Suggest, never sell." No exclamation marks. No emoji. **No em-dashes** (they read as
  AI-authored to this user): use a middot, comma or full stop `[catalogue]`.
- "Edition" or "Series", never "new collection". Avoid "shop now / trending / hot / must-have / drop / slay" `[catalogue]`.
  (Note PTAT's "New Collection Drop" is exactly the phrase Naira avoids.)
- Own vocabulary: hand-finished · slow-made · pressed · salt-washed · made-to-measure · atelier · edit · capsule;
  tagline "Softly, slowly, worn." `[img-naira/bible]`.
- Western-demi-fine grammar (declarative, verb-led, full stops) not Indian-discount grammar (imperative + numeral +
  exclamation) `[img-naira/ads]`.
- Captions: hook, one concrete benefit, one call to action, 3–5 hashtags; open with the value; never "Exciting news" /
  "We're thrilled to announce" `[sce]` `[content]`. Instagram: visual-first captions, storytelling hooks, line breaks,
  hashtags at the end or first comment `[content]`.
- Read the voice profile before every caption, not just the first; voice drifts in the back half of a 12–20-post set
  `[sce]` `[canva/gotchas]`. (No voice profile exists yet for Naira in the plugin's shared/voice-profile.md
  `[inferred: template only]`; build one from the owner's real posts/messages and confirm it `[sce]`.)
- Voice test: does it sound like us; would a competitor say this `[brand/voice-framework]`.

---

## 2. Canvas and platform

- **Master 1080 x 1440 (3:4)** for singles and every carousel slide; Reels 1080 x 1920 with a designed cover `[ref B1]`.
  (Skills' 1080x1080 / 1080x1350 sizes are pre-2025 `[banner]` `[design]`.)
- If a scheduler/API will publish, keep essentials out of the top and bottom 45 px (4:5 fallback) `[ref B1]`.
- Reel covers: title/face/product inside the central 1080 x 1440 and ideally 1080 x 1350; respect Reel UI zones (top
  ~270 px, bottom ~670 px, right rail) for any in-video text `[ref B]`.
- Keep the top-right ~16% x 14% of every cover clear (IG format icon) `[ref A1]`.
- Safe zones: critical content in the central 70–80% (banner) / 80% (social) `[banner]` `[design/social-photos]`;
  6% side-safe strip used by Naira ads `[ads21]`; nothing falls off the page, nothing overlaps unintentionally, every
  element inside the canvas with margin `[canvas]` `[ui-styling/canvas-design-system]`.
- Exact pixel viewport, self-contained HTML, no scrolling, 3–5 s wait for fonts/images before screenshot,
  `deviceScaleFactor` 2 for crispness `[design/social-photos]`. Naira's pipeline renders 1080x1350 at scale 4/3 →
  1440x1800 masters, JPEG q92 4:4:4 `[ads21]` (scale the same way for 1080x1440 → 1440x1920 masters).
- Test at 50% size for readability `[design/social-photos]`; better, test at **36%** (the actual grid scale) `[ref A1]`.
- Carousel: all slides one aspect (first slide sets it) `[ref B]`; slide 1 must be self-contained because it is also the
  grid tile ("Carousel slide 1 → standalone feed post: self-contained; cannot assume slides 2+") `[sce/calendar]`.
- Repurpose an approved design to story/reel-cover crops rather than regenerating; what travels is photo, treatment,
  claim; caption length and register change `[sce/calendar]`.

---

## 3. Composition and hierarchy

- One focal point, clear reading flow `[design/social-photos]`. Spend your boldness in one place; keep the rest quiet;
  "remove one accessory" `[frontend]`.
- **A small object dominates by isolation and light, not by filling the frame. Cramming the jewel large destroys scale**
  `[img-naira]` `[img-naira/tested]`. Product 35–50% of frame on colour-block heroes; 60–70% only for catalogue/DPA
  frames `[img-naira/ads]`.
- Leave a planned copy shelf: "Wide empty space in the upper left of the frame… Never bake text into the image" (into
  the AI photo; type is added in layout) `[img-naira/tested]`.
- Three-zone hierarchy: top = mark or value prop, middle = message + visual, bottom = CTA/URL `[banner/ref]`.
- Visual structure is information: outlines, numbering, eyebrows, dividers must encode something `[frontend]`.
  Refuse the hero-metric template and same-size card scaffolds `[impeccable/craft-floor]`.
- Twenty-one constructions, not one template: what holds a set together is the brand (faces, palette, one wordmark,
  safe strip), not a repeated layout `[ads21]`. Equally: derive several materially different structures before picking
  `[impeccable/new-work]`.
- The skeleton test: strip the copy; does the structure alone still say what the post is? If not, the boldness is only
  in text size `[impeccable/bolder]`.
- Whitespace groups and separates; more space above a heading than below; tight groups, generous separation
  `[uupm]` `[impeccable/craft-floor]`.
- Depth: shadows carry offset + soft blur; no zero-blur hard offset shadows unless the world is neobrutalist
  `[impeccable/craft-floor]`. Naira's own packshot shadow is a gold-umbra card shadow `[tokens]`.
- Refuse decorative glass/blur, gradient text, coloured thick side borders, sparkline/ring stand-ins
  `[impeccable/craft-floor]`. ui-ux-pro-max's generated "Liquid Glass" recommendation for a jewellery query is
  rejected (it ran this session and returned a generic dark-plus-gold kit and Liquid Glass) `[uupm]`.

---

## 4. Imagery (product and people)

From `[img-naira]` (verified across 27 generations) unless marked:
- **One product per frame, never two** in AI generation (scale collapses). Pairs only when photographed, or as "one
  declared pair" in campaigns `[upclose]`.
- Describe the product in ≤ 6 words in prompts; lock countable facts as digits; name the thing that will morph and
  forbid it ("the rope braid must stay a braid, not a smooth band") `[img-naira]` `[img-naira/tested]`.
- Two light sources: one large soft, one small hard specular, or gold renders as matte plastic.
- Build scale explicitly: referent (cardamom pod, peppercorn, rice grain, fingernail, khadi thread), honest macro depth
  of field (millimetres), a contact shadow, real grain of matter; best of all, **substrate deformation** (the piece dents
  the khadi, imprints the clay).
- Surfaces rotate so a set does not look like one shoot: blush washed linen, limewashed plaster + jaali shadow,
  travertine, raw silk, khadi, handmade deckled paper, terracotta bisque, aged brass tray `[img-naira/mods]`
  `[img-naira/tested]`. Background prompts need "absolutely never sand, tan, beige or golden" or everything drifts to
  sand `[img-naira/tested]`.
- One piece of set-dressing per frame, max (dried rose, pressed hydrangea petal, sage silk ribbon, palm-frond shadow,
  jaali shadow, folded khadi, out-of-focus brass bowl) `[img-naira/mods]`.
- Skin: warm South Asian skin, unretouched pores; **vary skin deliberately** or the model renders the same woman every
  time `[img-naira]` `[img-naira/mods]`.
- Use AI to make jewellery look **made**, not expensive: dust, dents, fingerprints, a cotton fibre in the braid
  `[img-naira/tested]`.
- Anti-brief: white cyclorama with hard drop shadow; black velvet spotlight; glossy over-saturated gold; prop clutter;
  any baked-in text, logo, watermark, price flash or badge; cool/teal-orange grade; more than one Indian iconographic cue
  `[img-naira/bible]`.
- Photography/illustration should dominate; text whispered `[canvas]` ("Analog Meditation") `[ui-styling/canvas-design-system]`.
- Generated or illustrative material must be labelled synthetic wherever a viewer could mistake it for the real thing;
  claims stay uninventable `[impeccable/new-work]`. Never present a design you have not looked at `[sce]` `[canva]`.
- State the generation cost before generating; Higgsfield/Canva batches are budgeted up front `[img-naira]` `[sce]`
  `[canva]`. (This sweep is read-only: no generation was run.)

---

## 5. Graphic devices for the "illustrated / collage / Indian-pop" direction

- Style lanes the skills name: Illustrated/Hand-drawn ("custom illustrations, artisan feel"), Collage/Mixed media
  ("cut-paper textures, photo cutouts, layered elements"), Editorial/Magazine, Nature/Organic ("botanical motifs"),
  Retro/Vintage ("serif type, halftone, muted") `[banner/ref]`; Collage is "Fashion, culture" `[design/social-photos]`.
- From the local ui-ux-pro-max style database (searched this session, query "collage scrapbook maximalism illustrated
  retro"): **Anti-Polish / Raw Aesthetic** fits ("hand-drawn elements, scanned textures, paper/pencil textures, collage,
  tape/sticker overlays, human touch"; small random rotation ±3°; texture opacity ~0.3; WCAG AA achievable).
  **Gen Z Chaos / Maximalism** is the PTAT-adjacent lane but its clashing neon palette and "Accessibility: Poor" rule it
  out for Naira `[uupm]`.
- Systematic patterns, repeated marks, layered elements that reward sustained viewing; a subtle conceptual reference
  embedded so "those who know feel it" `[canvas]` `[ui-styling/canvas-design-system]`. For Naira the niche reference is
  the couture house (pattern paper, tailor's chalk, selvedge, a measuring tape) and Nashik.
- Delight must be product-specific: "Generic whimsy is worse than neutral clarity"; "the moment is specific enough
  that a neighbouring product could not use it unchanged" `[impeccable/delight]`. Reject PTAT's generic stickers
  (smileys, rainbows) for Naira; author Naira-specific ephemera (pressed petals, swatch card, care label, wax seal, the
  box's pull tab) `[ref A5]`.
- Amplify what the system already owns; the bolder version should look more like the same brand, not less; no new
  colour/font/primitive without a named job `[impeccable/bolder]`.
- Text sparse: "90% visual, 10% essential text"; "never paragraphs" `[canvas]` `[ui-styling/canvas-design-system]`.
- Social photos: visual-first, minimal text, strong colours, lifestyle feel for Instagram `[design/social-photos]`.

---

## 6. Copy and claims on graphics (the never-list)

- **Never invent a price, discount, stock count or product claim**; read prices fresh from Shopify for any post that
  names a number; "was X, now Y" only when compare-at is genuinely higher `[sce]` `[sce/gotchas]` `[canva]`.
- **No offer, code or percentage on any image**; BUY2 lives in the caption/primary text `[upclose]`. "The colour-block
  hero never carries a price" `[img-naira/ads]`.
- **Material wording**: the listings' own words "18K gold tone & rhodium plated"; "18K gold" alone would claim gold
  content; some pieces are copper alloy, so materials are left out `[claude-md]`. (Note: the exhibition poster says
  "18k gold coated · rhodium coated" `[poster]`, and Up Close uses "gold-coated"; pick one approved phrase and use it
  everywhere: open question for the owner.)
- **No gold framing on Dhanteras/Dasara** ("buy gold") because the pieces are coated `[upclose]`.
- Sign-off **"made to stay gold."** is never shortened; in caption, never on a rhodium-only piece `[upclose]`.
- **Contested dates stay off images**: no Karwa Chauth date (sources split 28/29 Oct) `[upclose]`; no courier "order by"
  date until confirmed `[upclose]`.
- Never write scarcity ("selling fast", "only N left") `[upclose]`; the site's "Last 24 hours: N pieces sold" is a hash, not
  sales data, and must never be quoted `[claude-md]`.
- Pearl care: never claim water-safety for the two non-waterproof pearl pieces `[upclose]`.
- Copy must match the audited product truth (clasp type, stone counts, rails) `[upclose]`; only in-stock pieces (Up Close
  excluded 1–2-unit SKUs; stock guard pauses at 1) `[upclose]`; don't push a piece that is about to run out `[strategy/gotchas]`.
- One Indian cue per frame; no jokes at tailors' or aunties' expense `[upclose]` `[img-naira/bible]`.
- Logo/wordmark appears once `[upclose]`.
- Legal flags always checked: unsubstantiated superlatives ("best", "only"), comparative claims, testimonials without
  attribution, close paraphrase of others' work `[review]`. "Craft/handcrafted" claims must be true for the specific
  piece [inferred from `[review]`; the ad-formats research recommends a craft story, but sourcing in cataloguerating is
  supplier catalogues (Yiwu/1688/KAVNAR), so "handmade" is not automatically true for a Naira Petite piece: verify per
  piece before saying it].
- Don't use luxury-monogram lookalikes (IP risk) `[catalogue/rating_framework]`; don't copy another artist's work
  `[canvas]` (applies to PTAT: borrow the system, not the lockup, hand or lettering).

---

## 7. The grid as a system

- Plan the calendar first and get approval before making anything ("the single largest source of wasted work")
  `[sce]` `[canva]`.
- Cadence the team can sustain: owner plus helper 3–4 posts/week `[sce/calendar]`; Buffer 3–5/week `[ref B]`.
- Theme mix ~40% useful / 30% proof / 20% offer / 10% people; proof rows are the most under-used and best performing
  `[sce/calendar]`. Flag conflicts: same product twice the same day, promo on a holiday, a sale post after the sale
  `[sce/calendar]`.
- Seasonality must fit the niche; check before over-indexing on one spike; weigh margin and stock, not just revenue
  `[strategy/gotchas]`.
- Consistency: same style across all posts; one icon language; consistent elevation and spacing scale `[uupm]`
  `[brand/consistency-checklist]`.
- Grid quality rubric (used to vet creators, equally valid for our own grid): **visual cohesion & curation 3 pts,
  production quality 3, niche fit (jewellery visible, styling formats) 3, collab/proof signals 1**; 8+/10 to pass
  `[igfinder]`. Apply it to each option's 12-tile grid.
- Rows of three: each row mixes one dense graphic, one breathing photo/video, one mid-weight tile; colour fields big
  enough to read at 36%; event content in waves with one lockup; product never stops during an event `[ref A4]`.
- Plan pins as 0 or 3 (a full row) or design them in `[ref B2]`.

---

## 8. Motion (Reels, animated covers, any animated slide)

- Every animation needs a purpose (spatial consistency, state, explanation, feedback); "it looks cool" is not one if seen
  often `[emil]`.
- Enter with ease-out (custom curve, e.g. `cubic-bezier(0.23, 1, 0.32, 1)`); on-screen movement ease-in-out; never
  ease-in for UI; constant motion linear `[emil]`. The site's own reveal curve is `cubic-bezier(0.22, 1, 0.36, 1)`,
  0.6 s, 16 px rise `[tokens]`.
- Nothing appears from scale(0): start at ~0.95 + opacity 0 `[emil]`. Blur can mask an imperfect transition `[emil]`.
- Stagger 30–80 ms between items `[emil]`; one orchestrated moment beats scattered effects `[frontend]`
  `[impeccable/craft-floor]`.
- Match motion to the mood: elegant = slightly slower, `ease` rather than snappy `[emil]`. Naira precedent: the box turns
  at ~35 s a revolution, the wordmark flower every 10 s (owner's numbers) `[claude-md]`: quiet, slow, continuous.
- Review animations the next day / in slow motion `[emil]`. Respect reduced-motion where the medium allows `[uupm]`.

---

## 9. Process and QA

- Gather requirements (purpose, platform, content, brand, style, quantity) before designing `[banner]` `[design/social-photos]`;
  ask the questions that change the work, skip settled facts `[impeccable/new-work]`.
- Generate several concept ideas that vary composition, colour and type approach; present for approval before building
  `[design/social-photos]`. Write a short plan (4–6 named colours, type roles, layout in one-sentence prose + ASCII
  wireframes, principles), then check it against the category defaults and revise before building `[frontend]`.
- Optional but recommended: write a 4–6 paragraph design philosophy per option ("name the movement") before rendering
  `[canvas]`; record the direction as a short contract (THESIS / OWN-WORLD / STORY / FIRST VIEWPORT / FORM)
  `[impeccable/new-work]`.
- Build to full commitment; then inspect in **bounded passes**: one batched inspection, fix everything in one batch, at
  most one confirming round, stop `[impeccable]`.
- Verify every exported PNG: fonts actually loaded (no fallback), colours on brand, readable at thumbnail size, no
  overflow/clipping, safe zones respected, hierarchy clear, contrast ≥ 4.5:1 `[design/social-photos]`.
- Final refinement = refine, don't add: "If the instinct is to call a new function or draw a new shape, STOP… How can I
  make what's already here more of a piece of art?" `[canvas]`.
- Look at every output; a "success" status is not a correct design `[canva/gotchas]` `[sce]`.
- Approval checklist per asset: logo variant/clear space/min size; palette only, 60/30/10; brand fonts and hierarchy;
  imagery matches style; contrast; alt text; copy in voice, no prohibited terms, CTA clear, proofread
  `[brand/approval-checklist]`.
- Brand review pass on copy: voice/tone, terminology, messaging pillars, style rules, legal flags, with severity and
  before/after fixes `[review]`.
- Deliver for review, never publish: stage, keep the owner in control; check scheduled times are in the future
  `[sce]` `[canva]`.
- Provide alt text for every post (meaningful images) `[uupm]` `[brand/approval-checklist]`.

---

## 10. Pre-flight checklist (per post)

- [ ] 1080 x 1440 master (Reels 1080 x 1920 + cover); top-right 16% x 14% clear; ±45 px top/bottom free if API-posted
- [ ] The one thing that must read in the grid is ≥ 90–110 px on the canvas; checked at 36% scale
- [ ] Palette from §1.1 only; gold is the only saturated element; no pure white, grey, black or teal grounds (deep-sage
      exception noted)
- [ ] Every text pair ≥ 4.5:1 (≥ 3:1 if large); no ivory on mid-sage, no gold/sage/blush text on ivory
- [ ] Velista (or Cormorant) display + Cormorant italic + Jost only; ≤ 2 Jost support lines + ≤ 1 eyebrow
- [ ] Wordmark once; logo on cream fixed; radius 0
- [ ] One product per frame (or one declared pair); scale cues present; gold warm-neutral; fidelity checked against the
      real product photo
- [ ] One Indian cue max, material over iconographic
- [ ] No price/code/percentage/scarcity/date-in-dispute on the image; material wording approved; no "18K gold" alone;
      no "buy gold"
- [ ] Copy: no exclamation, no emoji, no em-dash; "edition/series", never "new collection/drop"; caption = hook +
      benefit + CTA + 3–5 hashtags; voice re-anchored
- [ ] Carousel slide 1 stands alone; all slides same aspect
- [ ] Synthetic imagery labelled where it could be mistaken for real; claims true for this piece
- [ ] Alt text written

## 11. Pre-flight checklist (per 12-tile grid)

- [ ] Rows of three each mix dense / breathing / mid-weight tiles; no row of three posters or three photos
- [ ] Colour fields legible at 36%; the grid reads as a colour rhythm, not a wall of cream
- [ ] One repeating device (lockup, frame, series number) across the set; event/festive posts told in waves
- [ ] Format mix roughly balanced (Reels / carousels / singles) and every Reel has a designed cover
- [ ] Theme mix near 40 useful / 30 proof / 20 offer / 10 people; offers only in captions
- [ ] Festive posts land before their dates (Karwa Chauth 29 Oct, Dhanteras 6 Nov, Diwali 8 Nov, Bhai Dooj 11 Nov,
      Tulsi Vivah 21 Nov) and nothing dated runs after its moment
- [ ] Pins planned as 0 or 3
- [ ] igfinder rubric self-score ≥ 8/10 (cohesion 3, production 3, niche fit 3, proof 1)

---

## 12. Read but not applicable (and why)

- `[brand-guidelines]` is **Anthropic's** brand (Poppins/Lora, `#d97757` orange, `#6a9bcc`, `#788c5d`). Do not apply
  any of it to Naira; the only transferable idea is role-based colour/font assignment with fallbacks.
- `[ui-styling]` shadcn/Tailwind component guidance: web UI only. Its canvas-fonts folder is a usable font source
  (Italiana, Gloock, Young Serif, Instrument Serif, Crimson Pro, Libre Baskerville, Poiret One, Work Sans, Jost is not
  included), but brand faces take precedence.
- `[design-system]`: token architecture (primitive → semantic → component) mirrors the site's `[tokens]`; useful only to
  keep feed colours as named roles, not raw hexes.
- `[design]` logo/CIP/icon/slides generators: out of scope.
- `[emil]` component specifics (popovers, tooltips, drag): UI only; motion principles kept in §8.
- `[uupm]` app pre-delivery checklist (touch targets, safe areas, dark mode): app UI only; contrast, no-emoji-icons,
  consistency and alt-text rules kept.
- `[canva]` / `[sce]` Canva API mechanics (100 req/min, ~5 calls per design, asset IDs for autofill, email rows
  text-only): apply only if production moves into Canva; this sweep wrote nothing to Canva.
- `[brand-style]`: captures look and output preference into a business profile; relevant only as "preview before
  saving, never ask the owner for hex codes".
- `[strategy]`: sales-data brief (QuickBooks/PayPal/Square); relevant lessons kept in §7 (seasonality fit, margin,
  stock).
