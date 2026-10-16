# Edition One: version 3 plan (ready for the next Higgsfield top-up)

Written 16 Oct 2026, after the hero round, the bold v2 round and the ad-performance research (`build/AD_PERFORMANCE.md`).

## What the account's own data says

Naira's Meta account: 108 jewellery ads, ₹1,59,164 of spend, corrected for nine friends-and-family orders.

- **Concept statics beat plain statics:**

  | | ROAS |
  |---|---|
  | Concept statics | 1.44× |
  | Plain statics | 0.57× |
  | Plain, all | 0.90× |

  Concept also won outbound click-through in 10 of 10 side-by-side ad sets. The lead rests on one image, "Almost edible." (the Prism bracelet in gummy sweets, 10 of the 16 concept sales), and the data is thin. Treat it as direction, not law.
- **What won:**
  - visual puns where the piece is the punchline, readable in the thumbnail;
  - food and candy, and measuring tools ("The Width", a hoop in a brass calliper);
  - light pastel grounds;
  - the 4:5 Instagram Feed;
  - pieces over ₹2,000.
- **What didn't:**
  - puns carried only in the words;
  - dark plinths;
  - Reels for statics;
  - halved fruit (apricot);
  - copy-only cards.
- **Copy formula that won:** a two-word headline, a plain-spoken correction and a real number. For example: "Almost edible. *Cubic zirconia, not candy.*" and "25 millimetres across."

## How we shoot

- **The grammar:** one bold everyday object wears the piece, the camera is close, the sun is hard and low, and the ground is blush-peach.
- **Never ask the piece to make a shape.** The question mark bent the Aqua C out of true.
- **Compensate the scale bias.** The generator draws jewellery about 1.5–1.7× the ratio asked for against a prop. Ask for about 0.6× the true ratio. For example, ask for a stud that is "a tenth of the cricket ball's width" to get the true ~1/6.
- **Verify every plate** against the listing photos with `BRIEF.md`. Run only plates scoring 8.5+.
- **Feed 4:5 first;** Stories only for the proven winners.

## Frames to shoot, by priority (₹2,000+ pieces first)

| Piece | ₹ | Have (verified 8.5+) | Next frames |
|---|---|---|---|
| Aqua Heart Drops | 2,499 | — | Chill (lemonade glass) if it passes; **Almost edible** among pastel hard candies; Leave it running (tap) |
| Quatrefoil Éclat Studs | 2,449 | jaali-light crop (pending) | **Kaju katli** (the stud on a diamond katli with silver varq); quatrefoil **cookie cutter** in blush dough; star anise |
| Prism Cluster Studs | 2,399 | — | **Almost edible** at 2K (the 1K lite test reads instantly); Matches your mani; rangoli with six pearls |
| Baguette Halo Drops | 2,200 | — | **Almost a snack**: the pearl drop among makhana (white puffs, pearl-sized); doorbell with a flat plate; shuttlecock at true size |
| Verdant Cushion Studs | 2,199 | Two of a kind (peas) 8.6 | Day-night Test (pink ball) recalibrated; **pistachios** ("Pista, but forever") |
| Rivière Huggies | 1,999 | — | Mishri at true size; **The Width** (brass calliper) |
| Lilac Papillon Ring | 1,899 | — | Garnish (coupe rim) recalibrated; Caught one (net) |
| Torsade Huggies | 1,799 | — | Croissants recalibrated; The Width |
| Bold Dome Huggies | 1,649 | Not a mint 8.5 | Handle with care (cup) if it passes; The Width |
| Petite Square Huggies | 1,599 | — | Cool, squared (ice tray) if it passes; barfi recalibrated |
| Petite Bow Studs | 1,399 | — | Berry cute (strawberry) if it passes; gift box recalibrated |

Hoops under ₹2,000 can't pay back alone at ₹1,500–3,000 per sale. Shoot them as a **bundle** (two pairs in one frame, priced as a set) or as gift-set frames for Diwali.

## Ready to fire: the bold v2 fixes (from the reviewers, 16 Oct)

The bold v2 set drew the pieces 1.75–2.4× the ratio asked for, more than the usual 1.5–1.7×. So each fix below asks for a smaller ratio than plain compensation would. Each one lands within ±30% of true size across the overshoot seen. Full wording is in `build/verify/bold_*.json` (`fix`).

| Frame | Ask for | Also change |
|---|---|---|
| Candy test, Cluster ("Almost edible.") | the stud about two-thirds of one sweet's width | Shoot at 2K, the first frame to shoot. Exactly six pearls as in listing-1, none at the tips. The scene is already tested: the last 0.15 credits went on Z Image (text only, no product) for the same bowl. Pastel sugared jellies of about 2 cm in a clear bowl, hard low sun from the left and blush top left all hold, so keep that scene wording. |
| Handle with care, Dome | the huggie at one eighth of the cup's height | Delete "five huggies tall" and "where a handle would be". Anchor the hoop just below the rim. |
| Day-night Test, Verdant | each stud at one tenth of the ball's width, about four seam stitches long | Bezel bright rhodium white. Sunlit top third. |
| Berry cute, Bow | the bow at one fifth of the strawberry's length | Delete "a third of its width". |
| Garnish, Papillon | the butterfly at one ninth of the coupe's width | All four wings flat in one plane. Show the coupe's near half and stem. |
| Fresh batch, Torsade | each huggie at one fifth of a mini croissant's length | Tightly rolled minis in one row. The huggies at the same depth. |
| Chill, Aqua | the earring at one quarter of the glass's width | Frame the top third of the glass. If the C still runs long, use one fifth. |
| Smash, Halo | the earring at 0.23 of the shuttlecock's height | Shuttlecock upright on its cork. The post through a feather. |
| Matches your mani, Cluster | the stud no longer than the index fingernail | Lock the asymmetric stone order, unmirrored. |
| Sweet, and it sparkles, Rivière | the huggie the same size as one sugar crystal | Camera closer, so the hoop is about 20% of the frame width. |
| W09, Woven | shoot straight from behind, as W06 take 3 | Never ask for a "150° turned" head: it shows the face. |

## No credits needed: composites

When the credits ran out (0.07 left, under the 0.15 the cheapest model costs), the scene test paid for with the last 0.15 became the set. That test is the candy bowl with no product in it. `finished-ads/comp_prism.py` and `comp_cluster.py` cut the real piece out of its own listing photo and set it into that scene by hand:

- **True scale.** The Prism closed loop is about 65 mm across against sweets of about 2.5 cm. The Cluster arc is about 20 mm.
- **The scene's light.** The sun is low behind the sweets, about 43° up. Every shadow falls toward the camera and to the right, as the sweets' shadows do.
- **Shadows and occlusion.** Coloured light passes through the stones into their shadows. A sweet's shadow darkens any links it crosses, and the sweets nearer the camera are redrawn over the piece.
- **The piece itself is not redrawn.** Stone count, order and metal are exactly the listing photo's.

It works only where the scene has no generated product to remove. Every failed Prism frame has the generated bracelet baked into a textured ground, such as pencils, watercolour or a rainbow beam, so those can't be rescued this way. The candy scene is also too low for a 9:16 Story: the loop would sit in the reply-bar zone. The next 2K shoots should include one or two empty scenes, the set without the piece, so more composites can follow at no cost.

## Cost

- Each 2K image costs 2 credits; reshoots run about 40%.
- The table above is about 30 frames, roughly 85 credits including reshoots.
- The four concept camps need about 30–40 credits more to fill their gaps.

## Open questions for the founder

- **Prism Cluster Studs:** the listing macro shows 8 tiny pearls; the description and the other photos show 6. Which is right?
- **Petite Bow Studs and Verdant Cushion Studs:** the listing text says gold; every photo shows white metal.
- **Petite Square Huggies:** the description doesn't mention the seed pearls that appear in every photo.
