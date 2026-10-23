# Crazy ads phase 3: chic, minimal, elegant (23 Oct 2026)

The brief: "Loved these, chic, minimal and elegant. Make it for 20 products, 2-3 ads like this, 40 more, step by step." The
two shots in question are round three's 07 and 57: the Crystal tennis bracelet on a blank ivory wedding invitation with a
sprig of baby's breath, and the same bracelet beside an ivory satin evening clutch on aubergine. Both are now marked Keep on
the handoff page.

## What made those two work

- **One object from the moment the piece is worn**: the invitation to the wedding, the bag for the evening. Nothing to decode.
- **One quiet accent at most**: a sprig of baby's breath, and only on the day frame.
- **A tonal, matte plaster ground**: pale and airy by day (dove grey), deep and moody by night (aubergine).
- **The jewel is the only sparkle** and lies at true size, with room around it.
- **Ivory, gold and one deep tone**: no loud colour, no food, no pun props.

## The format of phase 3

Every product gets a **day** ad and a **night** ad, the way the bracelet got the invitation and the clutch: 20 products by
stock on 23 Oct, 40 ads. Same files as before: a text-free 9:16 Story and a 4:5 Feed with the wordmark, one line and the name
and price in the shot's ink. Each frame is shot one at a time and checked at zoom against the listing photos.

| # | Product | Day: object and ground | Night: object and ground | Lines (day / night) |
|---|---|---|---|---|
| 01 · 02 | Toggle Link Chain | tortoiseshell sunglasses, folded · pale sand | one long-stem red rose · charcoal | Out by noon. / Date night. |
| 03 · 04 | Prism Rivière Bracelet | three blank notecards in aqua, blush and butter · cloud grey | a mother-of-pearl box clutch · midnight navy | Note to self: all three. / Colour after dark. |
| 05 · 06 | Woven Gold Hoops | a folded ivory linen shirt, its collar and mother-of-pearl buttons · oat | a black silk fan, half open · oxblood | Effortless, on purpose. / Make an entrance. |
| 07 · 08 | Verdant Eternity Band | one white calla lily · pale sage | an emerald satin clutch · bottle green | Always in bloom. / Dinner in green. |
| 09 · 10 | Cushion Halo Ring | a blank place card with a gold edge and baby's breath · dove grey | a silver candlestick, lit ivory taper · plum | Plus one. / Ask by candlelight. |
| 11 · 12 | Bold Nocturne Chain | a structured cream top-handle bag · pale stone | one black satin stiletto · charcoal | Meeting at ten. / Out late. |
| 13 · 14 | Bold Nocturne Bracelet | two linen-bound books with a ribbon marker · sand | a black silk bow tie · near-black | Well read. / Black tie. |
| 15 · 16 | Halo Curve Ring | a tortoiseshell claw clip · latte | a lit amber glass votive · chocolate | Hair up, ring on. / Golden hour, extended. |
| 17 · 18 | Marquise Layering Set | a fresh mogra (jasmine) gajra · blush | a faceted crystal perfume bottle · midnight | Shaadi season. / Layered for tonight. |
| 19 · 20 | Ribbon Bead Bracelet | blush satin ballet flats with bows · blush | a black gift box tied with a satin bow · mauve | On pointe. / Gift-wrapped. |
| 21 · 22 | Brushed Gold Huggies | a tan leather notebook and brass pen · stone | a black cashmere turtleneck collar · near-black | Nine to five. / The classic. |
| 23 · 24 | Rivière Eternal Bracelet | a folded cream pashmina · ivory | a black satin opera glove · black | Winter white. / Old Hollywood. |
| 25 · 26 | Baguette Tennis Necklace · Crystal | the loved invitation and baby's breath · dove grey | the loved ivory satin clutch · aubergine | Dress code: sparkle. / Ready by eight. |
| 27 · 28 | Lilac Papillon Ring | a sprig of lilac · pale lavender | one deep violet anemone · ink blue | Spring, all year. / Night garden. |
| 29 · 30 | Aqua Heart Drops · Silver | a blue hydrangea head · pale sky | a small mirrored disco ball · deep teal | Something blue. / Heart of the party. |
| 31 · 32 | Prism Cluster Studs · Silver | sweet peas in pink, violet and lemon · cream | a gold lipstick case, open · rosewood | Sweet on colour. / Last look. |
| 33 · 34 | Molten Panel Bracelet | a gold-rimmed espresso cup on its saucer · sand | a black silk saree with a gold zari border · charcoal | Brunch, in gold. / Liquid gold. |
| 35 · 36 | Torsade Pearl Cuff | a pearl-white satin headband · blush | a black satin hair bow · near-black | Classic, with a twist. / Black bow, white pearls. |
| 37 · 38 | Baguette Halo Drops | one white gardenia · ivory | a lit brass diya · maroon | Pearl and petal. / Diwali, dressed up. |
| 39 · 40 | Verdant Cushion Studs · Silver | a sprig of eucalyptus · pale mint | a green glass perfume bottle · forest green | Fresh green. / Emerald hour. |

Lines are drafts and are settled shot by shot. Changed so far: 05 has a linen shirt in place of the silk scarf (a silk knot read as a
necktie in round three, and the shirt's buttons give the hoops a true size); 06's line is Make an entrance., since Fan favourite.
claims a popularity we have not measured; 12 has a black satin stiletto in place of leather gloves, which fit few Indian evenings out; 17 has a mogra gajra in place of a lace fan, since 06 already has a fan; 28 is on ink blue in place of aubergine, which 26 already has; 30 has a mirrored disco ball in place of a silver mesh clutch, since the set already has four clutches; 32 is on deep rosewood in place of plum, which 10 already has; 33 and 34 have a gold-rimmed espresso cup and a black silk saree with a zari border in place of two more clutches.

## True scale

The model draws small pieces too large next to a prop: the hoops came out 1.5x and 1.9x, the emerald band 1.6x to 2.6x in five
tries, whatever the prompt said about millimetres. So every kept frame is measured against its prop (buttons, kiss-lock balls, a
fan's sticks, a lily's spadix) and, where the piece is too large, set back at true size in post; the notes of each shot say by
how much. On a plain plaster ground the piece is lifted out by colour and the plaster rebuilt under it (`build/retouch/shrink.py`);
where it touches anything else, the model first removes the piece from its own frame to give a clean plate, and the piece is set
back on it (`build/retouch/replate.py`). Both scripts read the raw downloads in the session scratchpad.

## Budget

40 frames at 2 credits, plus about 8 reshoots: about 95 credits. 28 credits were left after round three, enough for the first
six products (01-12). The rest needs a top-up of about 70 credits.

## Files

`build/crazy3.json` (the shot log), `plates/crazy3/` (text-free plates), `ads/crazy3/` (Feed and Story). The finished set joins
the handoff page as its own section, marked for Keep or Drop.

## Shot log

<!-- log -->
34 shots kept, average score 9.08, 64 frames rendered. Each shot's notes, kept job and rhyme are in `build/crazy3.json`; plates in `plates/crazy3/`, Feed and Story ads in `ads/crazy3/`.

| # | Product | Object | Ground | Line | Score | Tries |
|---|---|---|---|---|---|---|
| 01 | Toggle Link Chain | classic tortoiseshell sunglasses, folded | pale warm sand lime plaster | Out by noon. | 9.2 | 1 |
| 02 | Toggle Link Chain | one long-stem deep red rose | deep charcoal-black lime plaster | Date night. | 9.3 | 2 |
| 03 | Prism Rivière Bracelet | three blank deckle-edged notecards in aqua, blush and butter | pale cloud-grey lime plaster | Note to self: all three. | 9.1 | 1 |
| 04 | Prism Rivière Bracelet | a mother-of-pearl box clutch | deep midnight-navy lime plaster | Colour after dark. | 9.3 | 1 |
| 05 | Woven Gold Hoops | a folded ivory linen shirt, its open collar and mother-of-pearl buttons | pale warm oat lime plaster | Effortless, on purpose. | 9.2 | 1 |
| 06 | Woven Gold Hoops | a black silk folding fan, half open | deep oxblood lime plaster | Make an entrance. | 9.0 | 1 |
| 07 | Verdant Eternity Band | the flower head of one white calla lily | pale soft sage lime plaster | Always in bloom. | 8.9 | 3 |
| 08 | Verdant Eternity Band | an emerald-green satin evening clutch with a silver kiss-lock frame | deep bottle-green lime plaster | Dinner in green. | 9.0 | 4 |
| 09 | Cushion Halo Ring | a blank place card with a thin gold edge and a sprig of baby's breath | pale dove-grey lime plaster | Plus one. | 9.3 | 2 |
| 10 | Cushion Halo Ring | a small silver chamberstick with a lit ivory candle | deep plum lime plaster | Ask by candlelight. | 9.1 | 2 |
| 11 | Bold Nocturne Chain | a structured cream leather top-handle bag | pale warm stone lime plaster | Meeting at ten. | 9.0 | 2 |
| 12 | Bold Nocturne Chain | one black satin pointed-toe stiletto | deep charcoal lime plaster | Out late. | 9.0 | 1 |
| 13 | Bold Nocturne Bracelet | two plain linen-bound books with a dusty-rose ribbon marker | pale warm sand lime plaster | Well read. | 9.1 | 2 |
| 14 | Bold Nocturne Bracelet | a pre-tied black silk bow tie | deep near-black charcoal lime plaster | Black tie. | 9.0 | 2 |
| 15 | Halo Curve Ring | a tortoiseshell acetate claw hair clip | soft latte lime plaster | Hair up, ring on. | 8.9 | 2 |
| 16 | Halo Curve Ring | a small amber glass votive with a lit tealight | deep chocolate lime plaster | Golden hour, extended. | 9.1 | 2 |
| 17 | Marquise Layering Set | a fresh mogra (jasmine) gajra | pale soft blush lime plaster | Shaadi season. | 9.2 | 1 |
| 18 | Marquise Layering Set | a faceted crystal perfume bottle with a gold cap | deep midnight-blue lime plaster | Layered for tonight. | 9.1 | 1 |
| 19 | Ribbon Bead Bracelet | a blush satin ballet flat with a bow | pale soft blush lime plaster | On pointe. | 9.0 | 2 |
| 20 | Ribbon Bead Bracelet | a small black gift box tied with a satin bow | deep mauve lime plaster | Gift-wrapped. | 8.9 | 2 |
| 21 | Brushed Gold Huggies | a closed tan leather notebook with a slim brass pen | pale warm stone lime plaster | Nine to five. | 9.0 | 2 |
| 22 | Brushed Gold Huggies | the folded ribbed collar of a black knit | deep near-black charcoal lime plaster | The classic. | 9.0 | 2 |
| 23 | Rivière Eternal Bracelet | a softly folded cream pashmina with a twisted fringe | pale warm ivory lime plaster | Winter white. | 9.0 | 2 |
| 24 | Rivière Eternal Bracelet | a long black satin opera glove | deep black lime plaster | Old Hollywood. | 9.0 | 2 |
| 25 | Baguette Tennis Necklace (Crystal) | a blank ivory wedding invitation with a gold-foil border and a sprig of baby's breath | pale dove-grey lime plaster | Dress code: sparkle. | 9.2 | 2 |
| 26 | Baguette Tennis Necklace (Crystal) | a small ivory duchess-satin clutch with a gold kiss-lock frame | deep aubergine-plum lime plaster | Ready by eight. | 9.1 | 2 |
| 27 | Lilac Papillon Ring | a fresh sprig of pale lilac blossom | pale lavender-grey lime plaster | Spring, all year. | 9.1 | 2 |
| 28 | Lilac Papillon Ring | one deep violet anemone | deep ink-blue lime plaster | Night garden. | 9.1 | 2 |
| 29 | Aqua Heart Drops (Silver) | a fresh blue hydrangea head | pale sky-blue lime plaster | Something blue. | 9.0 | 2 |
| 30 | Aqua Heart Drops (Silver) | a small mirrored disco ball | deep teal lime plaster | Heart of the party. | 9.1 | 2 |
| 31 | Prism Cluster Studs (Silver) | three sweet pea flowers in pink, violet and pale lemon | pale warm cream lime plaster | Sweet on colour. | 9.1 | 3 |
| 32 | Prism Cluster Studs (Silver) | an open gold lipstick case with its cap | deep rosewood lime plaster | Last look. | 9.0 | 2 |
| 33 | Molten Panel Bracelet | a small white espresso cup on its saucer, both with a thin gold rim | pale warm sand lime plaster | Brunch, in gold. | 9.1 | 2 |
| 34 | Molten Panel Bracelet | a folded black silk saree with a woven gold zari border | deep charcoal lime plaster | Liquid gold. | 9.1 | 2 |
<!-- /log -->
