# Size check from the owner's videos (13 Nov 2026)

## The ask

After the 13 Nov ship, the owner wrote: "Drive video and both video had the solitaire size and other sizes pls verify each
size pls in depth!" The two videos on the store's Drive are:

- `IMG_7514.MOV` (12 Nov, 49.5 s, 1440 × 1920 after rotation): the stainless steel stock in its bags and on its cards, handled
  on a desk with a keyboard. This is the stock the 2 Nov listings (`../stock-2nov/`) were made from.
- `289DBD98-FBAC-4521-9D8F-9558C792C520.mp4` (2 Nov, 30 s, the "Ads reels" folder): the ad reel with the Woven Gold Hoops,
  Brushed Gold Huggies, Toggle Link Chain and Cushion Halo Ring, worn.

Both are shared by link, so they were downloaded straight from Drive (the Drive connector stops at 10 MB). Neither video is
committed: they are 100 MB together, and the frames that matter are in `page/img/`.

## Method

- Frames at 6 per second (`ffmpeg -vf fps=6`), each scored for sharpness (variance of the Laplacian); measurements use the
  sharpest frames.
- **Keyboard.** At 38 to 41 s the V-Bar Teardrop's bag lies on the keyboard. Key centres 19.05 mm apart (O to K to M on one
  side, the arrow keys on the other) give about 9.0 px per mm (8.7 to 9.6 across the frame).
- **Fingers.** Elsewhere the scale comes from the owner's fingers lying on the same bag as the piece: index fingertip about
  17.5 mm, thumb about 21 mm. Widths are read by `tools/fw.py`, which samples a line across the finger and keeps the run of
  skin-coloured pixels around the centre, so they are not eyeballed; each line was checked on its debug image. In 4.2 s the
  thumb (229 to 246 px) and the index finger (about 195 px) give the expected 1.2 ratio.
- Pieces are measured as boxes or lines in pixel coordinates on gridded crops (`tools/zoom.py`), then divided by the frame's
  scale. Every value is a range, good to about 10 to 15 percent. Where the only finger is not in the piece's plane, the
  verdict is "can't tell".
- `tools/ev.py` draws the evidence crops in `page/img/` (it ran in the session scratchpad, next to the extracted frames).

## Results (stock video)

| Piece | Status | Listing says | Video shows | Frames | Verdict |
|---|---|---|---|---|---|
| Soleil Petal Pendant (SPP) | live | 25 mm across; stone 7 mm | 15 to 20 mm; stone 5 to 6 mm | 4.2, 5.2, 6.0 s | listing too big |
| V-Bar Teardrop Necklace (HTN) | live | bars 15 mm; pear 10 × 13 mm; chain 3.5 mm | bars 16 to 19 mm; pear 10 to 11 × 14 to 16 mm; chain 3.5 to 4 mm | 38.5 to 40.5 s (keyboard) | a little bigger |
| Pave Open Heart Studs (POHS) | live | 20 × 19 mm | 22 to 24 mm across | 10.8, 15.2 s | a little bigger |
| Clover Garland Necklace (CLGN-RD) and Bracelet (CLG) | live | clovers 10 mm; stones 3.5 mm | clovers 7 to 10 mm (most 8 to 9); stones about 3 mm | 23.0, 23.8, 24.7, 28.5 s | a little smaller |
| Heart Solitaire Huggies (HSH) | live | hoop 15 mm; heart 6.5 mm | hoop 15.5 to 18 mm; heart with bezel 7 to 8.5 mm | 12.8 s | close |
| Petite Pear Solitaire Necklace (PPSN) | live | pear 6 × 8 mm | 5.5 to 6.5 × 7 to 8 mm | 8.8 s | matches |
| Asscher Solitaire Pendant (ASP) | draft | 9 mm | 8.5 to 9 mm with claws | 4.2 s | matches |
| Cushion Bezel Pendant (CBP) | draft | bezel 8 mm; stone 6 mm | bezel 7 to 7.5 mm; stone 5.5 to 6 mm | 0.0 s | matches |
| Bow and Heart Gift Set (BHGS) | live | earrings 14 mm long; drop heart 9 mm | 12 to 19 mm long | 32.7 s | can't tell (finger above the card) |

- **Soleil Petal.** In one frame (4.2 s), at one scale, the flower is about twice the Asscher stone and its centre stone about
  0.6 of it; the Asscher stone is about 9 mm against the thumb in the same frame. The 2 Nov estimate (27 to 30 mm) came from
  a close-up with the flower held in front of the fingers, which makes it look bigger. The two worn photos on the listing were
  drawn on 2 Nov at about 31 mm on the neck, well over one and a half times the real size.
- In the stock video but matched to no listing: a three-stone drop earring on a "STAINLESS STEEL" card (18 to 20 s), a flat
  chain and tennis chain set marked 695 (41 to 45 s), and curb and marquise chains set with stones (35 to 36 s, 46 s).

## Results (ad reel)

A background agent measured the reel at 30 fps (frame n is n/30 s). The reel has no keyboard and few fingers on the pieces, so
the scale comes from a thumbnail (taken as 10.5 to 13 mm), an earlobe (18 to 20 mm), the fingers (15 to 18.5 mm) or the
chain's own 4 mm links. These are looser than the stock video's numbers.

| Piece | Status | Listing says | Reel shows | Frames | Verdict |
|---|---|---|---|---|---|
| Toggle Link Chain (YF5143) | live | "Closure: Gold toggle bar and ring clasp, approximately 15mm"; links 4 mm | ring about 22 to 23 mm across (5.4 to 5.8 link widths); 18.5 to 26 mm against the fingers; bar about 13 to 15 mm; links 3 to 4.8 mm | n420 to n439 (14.0 to 14.6 s) | ring bigger than listed; not changed |
| Cushion Halo Ring (WR20902K8) | live | stone 8 mm; halo 12 mm | halo 12.1 to 14.9 mm in the box, 10.3 to 12.1 mm worn; stone 0.70 of the halo (listing 0.67) | n650 (21.67 s), n461 to n465 | matches |
| Woven Gold Hoops (E20267O) | live | 25 mm across | 22.9 to 29.5 mm in the box (depth corrected); 22.3 to 25.6 mm worn | n713 (23.77 s), n461 | matches |
| Brushed Gold Huggies (E14776S) | live | 14 × 9.8 mm | 13.1 to 14.5 mm tall, 10.4 to 11.5 mm wide | n410 (13.67 s), n406 | matches |

- **Toggle ring.** In the reel it looks oval (167 to 178 by 115 to 130 px). The agent read it as an oval ring, but the store's
  close-up (`../concept-camps/build/refs/toggle/ref-clasp.jpg`) shows it round (408 × 413 px), so the oval is its tilt and the
  long side is its width.
  - Against the chain's links (30.8 px, listed 4 mm), the ring is about 22 to 23 mm.
  - The bar is about 0.6 of the ring (237 to 242 px against 410 in the close-up), about 13 to 15 mm, so the listing's 15 mm fits
    the bar, not the ring.
  - `tools/toggle.py` draws `page/img/toggle-link-chain.jpg`.
  - **Changed on 13 Nov**, after the owner chose "Fix all of it" (`ship/toggle_13nov.py`, `ship/toggle_13nov.graphql`,
    `ship/toggle_13nov.json`). One `productUpdate` sent the description and SEO only:
    - the clasp now reads as a ring of about 22mm across and a bar of about 15mm;
    - "non tarnish", "anti-tarnish" and "Waterproof and tarnish free" are out (Finish: Polished gold tone; Plating: PVD 18k
      gold tone coating; the store's usual care line);
    - the SEO title and description name the Toggle Link Chain instead of "Ivory Clasp Chain".
  - Checked afterwards: no userErrors, still ACTIVE at ₹999 (₹1,429) with 78 in stock and its 7 media; the returned text is
    the text sent.
  - **Tags left as they are:** Hypoallergenic, Tarnish Free and Waterproof. They are store-wide (96, 98 and 99 products; 81 of
    the 174 live products carry Waterproof) and may drive badges or filters, so removing them is the owner's call.
- **Huggies.** The size card marks the height (14 mm) and the band's front (9.8 mm). The listing's "approximately 6mm deep" is a
  third measure the card doesn't show and the reel can't reach.
- **Prices.** The reel's price card (5 to 8.3 s) shows:
  - Woven Gold Hoops ₹1,199 (struck ₹2,769) against ₹1,049 (₹1,749) on the store;
  - Brushed Gold Huggies ₹799 (₹1,799) against ₹699 (₹999);
  - Toggle Link Chain ₹1,199 (₹2,900) against ₹999 (₹1,429);
  - Cushion Halo Ring ₹1,099 (₹2,200) against ₹999 (₹1,669).

  If the reel still runs as an ad, its prices are out of date. No ad was touched.
- The agent's evidence images for the three that match are `page/img/cushion-halo-ring.jpg`, `woven-gold-hoops.jpg` and
  `brushed-gold-huggies.jpg`. Its frames and script stayed in the session scratchpad.

## Shipped, 13 Nov

The owner: "And make changes and ship to the drafts urgently once in depth verification done". All five pieces were live, and
the owner chose to keep them live; one Shopify mutation changed their sizes only (`../stock-2nov/build/fix_13nov.py`, recorded
in `../stock-2nov/README.md`):

- **Soleil Petal Pendant:** about 18 mm across with a 5.5 mm stone. New size card. The two oversized worn photos are off the
  listing. Two new tries on 13 Nov still drew the pendant at about 32 to 34 mm, so there is no worn photo for now.
- **V-Bar Teardrop Necklace:** bars about 17 mm, pear about 10 × 14 mm (the stone without its claws). New size card.
- **Pave Open Heart Studs:** about 23 mm across and 22 mm tall. New size card.
- **Clover Garland Necklace and Bracelet:** clovers about 8.5 mm, stones about 3 mm. New card for the necklace.
- **Toggle Link Chain**, a second mutation (above): the clasp ring about 22mm and the bar about 15mm, the waterproof and
  tarnish wording out of the description, and the SEO under its own name.

The page (https://claude.ai/artifact/Mot3ynaP8aPMBtmfbRHHf3, version 3) shows the same.

## Still open

- A worn photo of the Soleil Petal Pendant at its true size (2 credits a try).
- The tags Waterproof, Tarnish Free and Hypoallergenic, store-wide (about 96 to 99 products).
- One ruler photo of a Bow and Heart earring.
- The reel's prices, if it still runs as an ad.
