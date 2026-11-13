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

<!--ADREEL-->

## Not done

Nothing was changed on Shopify. The proposed corrections (copy size lines and size cards for the Soleil Petal, the V-Bar
Teardrop, the Pave Open Heart Studs and both Clover Garland pieces, plus new Soleil worn photos at true size) wait for the
owner's go-ahead, in one batch.
