# NAIRA PETITE — thank-you poster, the Emerald Park pop-up (Nashik, October 2026)

| File | Use |
|---|---|
| `naira-thank-you-emerald-park-elegant-4x5.jpg` | **Elegant edition in the house colours**: 2160 × 2700, for posts, chats and groups |
| `naira-thank-you-emerald-park-elegant-status-9x16.jpg` | **Elegant edition**: 2160 × 3840, for WhatsApp Status and Stories (text kept clear of the top bar and the reply bar) |
| `naira-thank-you-emerald-park-4x5.jpg` | Emerald and gold edition, 2160 × 2700 |
| `naira-thank-you-emerald-park-status-9x16.jpg` | Emerald and gold edition, 2160 × 3840 |
| `stall-cutout-transparent.png` | The stall with the background removed (transparent PNG), for reuse |

## Photo

Chosen from four stall photos and two videos (IMG_6054, IMG_6058, both shot 22 October 2026). The low-angle table photo
won: it is the sharpest, and it holds the bracelet stand, necklace stand, trays, the "made to stay gold" gift bag
and the catalogue in one frame. In every video frame, the person at the stall is on the phone or looking down. Nashik and October 2026 come from the videos' location
and date data.

## Cut-out

The table outline was traced by hand along the tray edges, the pink box and the gift bag. The green carpet was removed by colour. The bracelet
and necklace stands come from a BiRefNet matte (rembg), including the gaps between the bars. The chair and outfit that showed through
the necklace stand's teeth were removed. Glare on the two laminated catalogue sheets was softened. The colour was
converted from Display P3 to sRGB, lightly graded, and upscaled 2× for the poster.

## Design

**Elegant edition (house colours):** cream paper (#FBF5F0) with a hairline sage frame. The logo is in its own sage
(#99B4AF) and blush (#FFBDA8). THANK YOU is set in Velista in deep sage (#5E7A70), and the Cormorant italic is in
coral (#C27560). The gift bag's coral tulips sit in the top corners. A blush arch with a sage outline stands behind
the stall, echoing the arch on the GIFT IT poster. The postmark is sage, and the catalogue fades into cream under
the footer. Built by `build/build_light.py`.

**Emerald edition:** 
Emerald ground for Emerald Park, gold-foil THANK YOU in Velista, Cormorant italic line, the NAIRA logo, the gift
bag's own coral tulips (drawn from `naira-bag/build/motifs.py`), a postmark in the style of the Lilac poster
("THE EMERALD PARK POP-UP · NASHIK · OCTOBER 2026"), a gold hairline frame, and sparkles placed on real highlights
of the gold caps. No exclamation marks.

`build/` holds the poster builder and the cut-out scripts, for reference. They read the source photo and fonts from the session
scratchpad.
