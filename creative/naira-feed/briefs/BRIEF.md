# Naira Flore · Instagram feed brief (25 Oct 2026)

## The ask (owner's words)
"What we are lacking is a very detailed and a very creative feed. Give me two options, very curated and very
detailed, like the one I've shared [the @projecttteteatete grid], very deep graphics, very understood and
thought-through posts, so that we can actually post it on the feed. Each post thought through, done UI and
graphics. Take all the skills necessary, think deep, understand Naira's brand, use all artefacts and data.
12 posts or 9? Decide and curate."

Decision already taken: **12 posts per option** (the 3:4 profile grid shows exactly 4 rows = 12 tiles on the
owner's phone, as the reference screenshot shows; 12 = one month at 3 posts a week, one finished row per week).

## Read these first (all under /tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed)
- research/reference-ptat.png (the reference grid) and research/tiles/ (2x crops of each reference tile)
- research/reference-and-platform.md (PTAT teardown, platform specs, 2026 calendar, exemplar feeds)
- research/design-rules.md (rules distilled from every design skill; contrast-checked palette)
- research/brand-bible.md (brand, story, claims allowed/forbidden, palettes, type, motifs, never-list)
- research/data-meta.md (what sold in ads, who buys, the current Instagram grid), research/ig-current-grid-part1.jpg
- research/data-shopify.md + research/roster.json (live prices, stock, bestsellers, sets, image URLs per piece)
- research/data-drive-notion.md (sourcing truth, earlier feed sets, concept bank)
- research/artifacts-feed-social.md, artifacts-worlds-imagery.md, artifacts-ads-market.md — read the SYNTHESIS
  sections fully (owner likes/dislikes, worlds already made, copy bank, best extracted images)
- research/assets-local.md, research/assets-remote.md (+ .json) — the image library with ratings and paths
- kit/kit-preview.png, kit/tokens.css, kit/motifs/ — wordmark SVG, flower SVG, fonts, tulip vectors, paisley, box render
- cutouts/ — BiRefNet cut-outs of hero pieces' still-life photos are being produced (cutouts/index.json maps
  file -> piece + variant alt text). Any in-stock piece's still-life photo can be cut out on request.

## Facts that bind every option
- Canvas: design masters at **1080×1440 (3:4)**, everything critical inside the central 1080×1350 (45 px clear
  top and bottom) so a 4:5 export also works. Keep the top-right ~16%×14% of the first slide clear (Instagram's
  carousel/reel icon sits there). In the grid a tile shows at ~36%: words meant to be read in the grid need
  ≥ 90 px type. Reels: 1080×1920 cover; the grid crops 240 px top and bottom.
- Rollout: 12 posts, 3 a week, Tue 27 Oct → about Sun 22 Nov 2026. Posted in order P1…P12, so P12 ends top-left;
  the bottom row (P1–P3) sits directly above the current newest row (LAC / flower / BONE on oxblood and bone).
  Each week completes one row. Best order times: Sun ~12:00, Fri/Sun 18:00–21:00 IST.
- Calendar: Karwa Chauth Thu 29 Oct (never print the date), Dhanteras Fri 6 Nov (no "buy gold" framing — the
  pieces are coated), Diwali Sun 8 Nov, Govardhan Tue 10 Nov, Bhai Dooj Wed 11 Nov, Children's Day Sat 14 Nov,
  Tulsi Vivah Sat 21 Nov (wedding season opens), muhurats 21, 24–26 Nov, 2–6 and 11–12 Dec.
- Audience: women 35–54 (64% of purchases are women 35+), Maharashtra 46% (Mumbai + Nashik), then Delhi NCR,
  Bengaluru, Pune, Chennai, Hyderabad. Self-purchase and gifting. 57% cash on delivery. 69% of orders are 1 piece.
- What sells: one piece + an everyday Indian object on a warm colour field + one witty Indian line + one exact
  fact ("Anaar, pre-peeled." on the Ruby Baguette Tennis Bracelet = best ad ever). Ruby is the hero stone.
  Edition Two (16 Oct) is the season's story. Bestsellers with deep stock: Woven Gold Hoops ₹1,299 (63),
  Prism Rivière Bracelet ₹2,399 (67), Baguette Tennis Bracelet ₹1,699 (57; Crystal/Ruby/Emerald),
  Baguette Tennis Necklace ₹2,300 (70), Baguette Huggies ₹1,199 (57), Heartbead Bracelet ₹1,299 (25),
  Brushed Gold Huggies ₹999 (35), Toggle Link Chain ₹1,299 (79), Bold Nocturne trio. ALWAYS take prices and stock
  from roster.json; never feature sold-out or 1–3-left pieces; KAVNAR Edition One = pre-order only.
- Claims: "18k gold tone plated" / "rhodium plated" (or the house line "18K gold tone & rhodium plated");
  waterproof / tarnish-free / hypoallergenic ONLY on pieces tagged so in roster.json; never "gold", "real",
  "diamond", "emerald" (say green cubic zirconia), "silver" as a metal, "handmade"/"artisan"/"karigar" for the
  jewellery (sourced; the couture side IS hand-made in Nashik). No codes, percentages, MRP strikes or
  scarcity on images; offers only in captions, one code at a time (BUY2 10% / BUY3 20% / NAIRA10 — exact line:
  "Take 2 pieces for 10% off or 3 for 20% off, with codes BUY2 and BUY3 at checkout."). No fake reviews/press.
- Voice (owner's caption system): hook < 125 characters, then 1–2 short lines, then a `[ piece · material · wink ]`
  kicker. No em-dashes, no exclamation marks, no emoji, no urgency. Tags in the first comment, ≤ 5.
  Display type: Velista (CAPS only; no ₹ or · glyphs — set prices in Jost). Asides: Cormorant Garamond italic,
  lowercase. Support: Jost. Wordmark once per frame at most (kit/naira-wordmark*.svg — never redraw it).
- Owner taste (from 100+ artifacts): loves Indian everyday-object wit with restraint (anaar, elaichi, mishri,
  dabba, missed-call code, slam book, steel almirah, "Not locker gold. Tuesday gold."), lilac/purple, deck
  florals (watercolour peach tulips + sage leaves), chic minimal still life with one meaningful object, moody
  night grounds (oxblood, emerald, plum), clean plates, exact facts. Dislikes: clutter (sticker/stamp/postmark
  soup), stuck-on florals, BLACK grounds ("Cartier's code"), sand/beige/tan grounds, cool light, orange/brassy
  gold, grand copy ("Crafted for modern royalty"), discount-led art, full faces on product tiles, lyrics on
  reels, soan papdi jokes, spice/masala props, anything that reads AI-made.
- The tension to resolve, not avoid: the owner now asks for PTAT-level depth (illustrated, collaged, series,
  multi-script, Indian pop) while the brand history is quiet and premium. Maximal in idea and system; premium
  in execution. Indian festive cues are allowed when they carry wit, never as wallpaper.

## Production reality (design for what can actually be built)
Every post will be built as an HTML/CSS/SVG composition and rendered to PNG with Playwright, by designer agents,
from: real product photography (Shopify galleries, owner-approved campaign plates, BiRefNet cut-outs), the kit
(wordmark, flower, tulips, paisley, fonts, palette), flat/line illustration a designer can draw in SVG (door
frames, almirahs, thalis, envelopes, sieves, croquis lines, stitches, tape measures, paper grain, stripes,
gingham, ruled paper, pattern paper, stamps used sparingly), and at most ~8 non-jewellery AI-generated elements
for BOTH options together (Higgsfield, ~66 credits left — props, painted backgrounds, textures; give the
prompt). Never AI-generate jewellery. Reels: we can design the cover and an animated graphic edit from stills,
or specify an edit of existing footage.
