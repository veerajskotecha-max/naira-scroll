# Edit requests: a frame that is right in construction but wrong in one proportion is given back to Nano Banana Pro as IMAGE 1
# with one named change, so the cube, camera and light stay as they are (as ../../albyluxe-31oct/build/edits.py).
# Usage: edits.py start_index KEY,KEY,...  (keys of E; each source is a key of jobs.json) -> prints requests JSON
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__)); J = json.load(open(f"{H}/jobs.json"))
from build import END
E = {
 "A12_He": ("A12_H", "EDIT IMAGE 1, a packshot of a pair of gold huggie hoop earrings with heart drops on a cream plaster cube. Make ONE change "
   "only: each plain polished gold HOOP becomes LARGER, about TWO AND A HALF times the width of its heart drop, a round hinged hoop about 15mm "
   "across, its wire the same slim thickness, so the heart hangs well below a clearly bigger circle of gold. The heart drops keep their present "
   "size and construction exactly: each a clear heart-cut stone in a smooth closed gold bezel, point down, hanging on a small gold jump ring "
   "from the bottom of the hoop. The hoops stay plain polished gold with no stones. Keep everything else in IMAGE 1 exactly as it is: the cube, "
   "the camera, the framing, the background and the light. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END),
}
E["A08_He"] = ("A08_H_r1", "EDIT IMAGE 1, a packshot of a jewellery set on a cream plaster cube: a pair of bow-and-heart stud earrings and a fine gold "
   "chain necklace. Make ONE change only: the necklace's centre, the small polished gold heart and the three small stones beside it on the chain, is "
   "REPLACED by a PENDANT identical to each of the two earrings, exactly as IMAGE 2 shows the motif: a BOW of two clear heart-cut stones, each in a "
   "fine rim of tiny pave stones, meeting at a small polished gold knot, and below the knot ONE clear heart-cut stone in a halo of tiny pave stones, "
   "point down. The pendant, the same size as one earring, hangs by its bow from the chain at the point of the chain's soft V. Keep the two earrings "
   "exactly as they are in IMAGE 1, each with its bow and its halo heart drop, and keep the chain, the cube, the camera, the framing, the background "
   "and the light exactly as they are. No plain gold heart anywhere. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["A08_M"])
E["N02_He"] = ("N02_H", "EDIT IMAGE 1, a packshot of a gold sunburst pendant necklace on a cream plaster cube. Make ONE change only: the SIX slender "
   "polished gold petal loops are re-arranged so they radiate EVENLY ALL THE WAY AROUND the round clear centre stone, like a pinwheel or a small sun: "
   "one petal points up-left, one right, one up-right, one down-left, one straight down and one down-right, spaced about sixty degrees apart, all "
   "curving gently the same way; the fine snake chain passes BEHIND the centre stone. The centre stone, its claws, the petals' size and finish, the "
   "chain, the cube, the camera, the framing, the background and the light stay exactly as they are. Metal: warm 18k gold tone. " + END)
E["N06_He"] = ("N06_H", "EDIT IMAGE 1, a packshot of a fine gold Y necklace on a cream plaster cube. Make TWO changes only. (1) Each side of the necklace "
   "is ONE single fine gold cable chain running from the top of the cube down to the tiny flower, never two parallel strands: remove the second strand "
   "on each side. (2) The tiny flower where the two arms meet has FIVE small round clear stones as petals around a tiny polished gold bead at its "
   "centre. Keep the single fine drop chain below the flower, the small gold flower charm at its end, the cube, the camera, the framing, the "
   "background and the light exactly as they are. Metal: warm 18k gold tone. " + END)
E["N02_Hf"] = ("N02_H", "EDIT IMAGE 1, a packshot of a gold half-sunburst pendant necklace on a cream plaster cube. Make ONE change only: the pendant "
   "has exactly FIVE slender polished gold petal loops, not six: remove one petal and space the remaining five evenly in the fan below and beside the "
   "round clear stone, one pointing straight left, one down-left, one straight down, one down-right and one straight right. Nothing above the stone. "
   "The stone, its claws, the petals' size, shape and finish, the snake chain, the cube, the camera, the framing, the background and the light stay "
   "exactly as they are. Metal: warm 18k gold tone. " + END)
DESIGN7 = ("Keep its exact design as IMAGE 2 shows it: ONE round clear stone held up in gold claws at the top and SEVEN open polished gold loop "
   "petals fanned below and beside it, nothing above the stone; only its size changes. ")
E["N02_W1s"] = ("N02_W1", "EDIT IMAGE 1, a photograph of a woman wearing a gold sunburst pendant on a fine snake chain. Make ONE change only: the PENDANT is "
   "far too large; shrink it to a little over HALF its present size, so the whole pendant is about 28mm across, a little more than half the width of "
   "her lips, and its round stone about 7mm, smaller than the tip of her little finger. " + DESIGN7 + "It hangs in the same place, just below the "
   "hollow of the throat, on the same fine snake chain, which keeps its thickness. Keep everything else in IMAGE 1 exactly as it is: the model, her "
   "skin, the crop, the camisole, the hair, the background and the light. Metal: warm 18k gold tone. " + END, ["N02_Hf"])
E["N02_W2s"] = ("N02_W2", E["N02_W1s"][1], ["N02_Hf"])
E["N02_Ps"] = ("N02_P", "EDIT IMAGE 1, a photograph of a gold sunburst pendant on a fine snake chain resting in an open palm. Make ONE change only: the "
   "PENDANT is far too large; shrink it to a little over HALF its present size, so the whole pendant is about as wide as two of her fingers side by "
   "side, about 28mm, and its round stone is about half as wide as one of her fingers. " + DESIGN7 + "It rests in the same place in the centre of "
   "her palm, on the same fine snake chain, which keeps its thickness. Keep everything else in IMAGE 1 exactly as it is: the hand, the fingers, the "
   "skin, the camisole, the background and the light. Metal: warm 18k gold tone. " + END, ["N02_Hf"])
E["N03_He"] = ("N03_H", "EDIT IMAGE 1, a packshot of a gold pearl pendant necklace on a cream plaster cube. Make ONE change only: the chain must NOT "
   "wrap around the pearl. Remove the loop of box chain that curves around the LEFT side of the pearl, so the pearl's left side is bare smooth "
   "pearl. The pendant now hangs from ONE small gold bail at the top centre of the pearl, and the fine box chain runs straight up from that bail "
   "on both sides, like any pendant necklace. Keep the pearl, its size and lustre, and the crescent of small clear stones in gold collars round its "
   "right side and bottom exactly as they are, and keep the sliding bead, the cube, the camera, the framing, the background and the light exactly as "
   "they are. Metal: warm 18k gold tone. " + END)
E["N07_He"] = ("N07_H", "EDIT IMAGE 1, a packshot of a gold Asscher solitaire pendant on a curb chain over a cream plaster cube. Make TWO changes "
   "only: (1) the chain becomes a FINE, delicate gold curb chain, about one third of its present thickness, its links tiny; (2) the pendant becomes "
   "smaller and finer: a SLIM polished gold bail with a single ridge, only about half as tall as the stone, and the whole pendant, stone and bail, "
   "about two thirds of its present size. Keep the clear octagonal Asscher step-cut stone, its clipped corners, its fine claws, its clarity and "
   "sparkle, and keep the cube, the camera, the framing, the background and the light exactly as they are. Metal: warm 18k gold tone. " + END)
A13DESIGN = ("Keep its exact design as IMAGE 2 shows it: a slim rounded-rectangle huggie with ONE row of small round clear stones in tiny "
   "gold claws down its front edge and a plain polished gold top, bottom and back; only its size changes. ")
A13KEEP = ("It hangs from the same piercing in the same earlobe. Keep everything else in IMAGE 1 exactly as it is: the model, her skin, the ear, "
   "the crop, the camisole, the hair, the background and the light. Metal: warm 18k gold tone. ")
E["A13_W1s"] = ("A13_W1", "EDIT IMAGE 1, a photograph of a woman wearing a slim gold pave huggie earring. Make ONE change only: the HUGGIE is "
   "too large; shrink it to about TWO THIRDS of its present height, so it is about 18mm tall, about as long as her earlobe is tall and well "
   "under a third of the height of her whole ear. " + A13DESIGN + A13KEEP + END, ["A13_H"])
E["A13_W2s"] = ("A13_W2", "EDIT IMAGE 1, a photograph of a woman wearing a slim gold pave huggie earring. Make ONE change only: the HUGGIE is "
   "a little too large; shrink it to about FOUR FIFTHS of its present height, so it is about 18mm tall, about as long as her earlobe is tall. "
   + A13DESIGN + A13KEEP + END, ["A13_H"])
E["A13_Hs"] = ("A13_H", "EDIT IMAGE 1, a packshot of a pair of slim gold pave huggies on a cream plaster cube. Make ONE change only: each "
   "huggie's side outline becomes a ROUNDED SQUARE instead of a tall narrow rectangle: keep its height exactly as it is, and make it much deeper "
   "front to back, so its depth is about nine tenths of its height and the open window in its middle is nearly square, its four corners softly "
   "rounded. Each huggie keeps its slim 2mm band, its ONE row of about ten small round clear stones in tiny gold claws down its front edge, its "
   "plain polished gold top, bottom and back, and its hinged post in the top edge. Keep the cube, the camera, the framing, the background and the "
   "light exactly as they are. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)
E["A13_Hd"] = ("A13_Hs", "EDIT IMAGE 1, a packshot of a pair of slim gold pave huggies on a cream plaster cube. Make ONE change only: each "
   "huggie's side outline becomes EXACTLY the shape drawn in IMAGE 2: a ROUNDED SQUARE as deep front to back as it is tall, with straight sides, "
   "four softly rounded corners and a big square window in the middle, never a tall narrow rectangle. Keep each huggie's height as it is and make "
   "it as deep as it is tall. IMAGE 2 is only a flat drawing of the outline: keep the real polished gold, the slim 2mm band, the ONE row of about ten "
   "small round clear stones in tiny gold claws down the front edge, the plain gold top, bottom and back and the hinged post exactly as IMAGE 1 "
   "shows them. Keep the cube, the camera, the framing, the background and the light exactly as they are. Metal: warm 18k gold tone, never "
   "brassy, orange or greenish. " + END, ["A13_shape_ref"])
E["A13_W1qs"] = ("A13_W1q", E["A13_W1s"][1], ["A13_Hg"])      # the same shrinks, on the frames made from the approved packshot A13_Hg
E["A13_W2qs"] = ("A13_W2q", E["A13_W2s"][1], ["A13_Hg"])
E["A13_W1qh"] = ("A13_W1qs", "EDIT IMAGE 1, a photograph of a woman wearing a slim gold pave huggie earring. Make ONE change only: the HUGGIE "
   "is far too large; shrink it to about HALF of its present height, so it is about 18mm tall: its top stays at the piercing and its bottom ends "
   "only about a centimetre below the bottom of her earlobe, the whole huggie about a quarter to a third of the height of her ear. "
   + A13DESIGN + A13KEEP + END, ["A13_Hg"])
E["N05_He"] = ("N05_H", "EDIT IMAGE 1, a packshot of a gold pear solitaire pendant necklace on a cream plaster cube. Make TWO changes only: "
   "(1) the PENDANT becomes smaller: the clear pear-cut stone and its fine claws shrink to about TWO THIRDS of their present size, so the stone "
   "is only about three chain links wide; (2) the round gold BEAD bail above it becomes much smaller, a TINY polished bead only about a quarter "
   "of the stone's width, on a small jump ring. Keep the stone's pear shape, point up, its clarity and sparkle, the fine gold cable chain exactly "
   "as it is (its links keep their size), the cube, the camera, the framing, the background and the light. Metal: warm 18k gold tone. " + END)
E["N05_Pc"] = ("N05_P_comp", "EDIT IMAGE 1, a retouched photograph of a small clear pear pendant on a fine gold chain resting in an open palm. "
   "Make it ONE seamless natural photograph: (1) the fine gold cable chain continues naturally from the pendant's tiny bail, running in two thin "
   "strands across the palm and over the side of the hand out of frame, its links tiny, each about a third of the pear's width; (2) a soft, "
   "believable contact shadow under the pendant and the chain where they rest on the skin. The PENDANT itself stays EXACTLY as it is in IMAGE 1: "
   "the same small size, the same position, the same clear pear stone in its fine claws and the same tiny bail. Do NOT enlarge it or redraw it. "
   "Keep the hand, the palm lines, the fingers, the skin, the hair, the camisole, the background and the light exactly as they are. Metal: warm "
   "18k gold tone. " + END)
E["N05_Pcs"] = ("N05_Pc", "EDIT IMAGE 1, a photograph of a small clear pear pendant on a fine gold chain resting in an open palm. Make ONE "
   "change only: the PENDANT, the pear-cut stone in its fine claws and its bail, is too large; shrink it to about THREE QUARTERS of its present "
   "size, so the pear is only about a third of the width of one of her fingers and the bail a tiny loop. It stays in the same place on the same "
   "fine chain. Keep the chain, the hand, the palm lines, the fingers, the skin, the hair, the camisole, the background and the light exactly "
   "as they are. Metal: warm 18k gold tone. " + END)
E["A16_He"] = ("A16_H", "EDIT IMAGE 1, a packshot of a gold V-bar teardrop necklace on a cream plaster cube. Make TWO changes only. "
   "(1) The smooth flat herringbone chain on both sides of the V is REPLACED by a CURB CHAIN exactly like the chain in IMAGE 2, a phone photo of "
   "the real piece: small interlocking oval links twisted to lie flat, each link with bright faceted cut edges that glitter, the chain about as "
   "wide as the polished bars and softly rounded in profile, every link separate and countable; never a smooth ribbon, never a herringbone or "
   "snake chain. (2) The clear pear-cut stone becomes LARGER, about two thirds as wide as one polished bar is long, still pear-shaped with its "
   "narrow tip at the TOP and its round end at the BOTTOM in fine gold claws, and its tip is joined DIRECTLY to the point of the V by its top "
   "claw, with no ring and no link between them. Keep the two smooth polished gold tube bars and their sharp V, the cube, the camera, the "
   "framing, the background and the light exactly as they are in IMAGE 1. Ignore the hand, the plastic pouch and everything else in IMAGE 2. "
   "Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["A16_chain_ref"])
E["A16_He2"] = ("A16_He", "EDIT IMAGE 1, a packshot of a gold V-bar teardrop necklace on a curb chain on a cream plaster cube. Make ONE change "
   "only: the curb chain on both sides of the V becomes a DENSER, FLATTER curb chain exactly like the chain in IMAGE 2, a phone photo of the real "
   "piece: its links are smaller and packed tightly together, each link overlapping the next so there is almost no open space between them, "
   "every link pressed flat with bright faceted cut faces that glitter, so the chain reads as a dense flat band of sparkling links, about as wide "
   "as the polished bars and softly rounded at its edges. Keep the two smooth polished gold tube bars and their sharp V, the clear pear-cut stone "
   "in its claws at the point of the V, its size, the cube, the camera, the framing, the background and the light exactly as they are in IMAGE 1. "
   "Ignore the hand, the plastic pouch and everything else in IMAGE 2. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["A16_chain_ref"])
E["A15_He"] = ("A15_H", "EDIT IMAGE 1, a packshot of a pair of gold open heart pave studs on a cream plaster cube. Make ONE change only: both "
   "hearts stand perfectly UPRIGHT side by side, square to the camera, each with its point straight down at six o'clock and its two rounded lobes "
   "level and exactly equal, the left heart a mirror image of the right, never tilted, never turned outward, never lopsided. Keep each heart's size, "
   "its broad band with its two rows of tiny clear stones, its thin polished gold rims and fine beaded edges, its open centre and its post, and keep "
   "the cube, the camera, the framing, the background and the light exactly as they are in IMAGE 1. Metal: warm 18k gold tone, never brassy, "
   "orange or greenish. " + END)
E["A16_W1s"] = ("A16_W1", "EDIT IMAGE 1, a photograph of a woman wearing a gold V-bar teardrop necklace on a curb chain. Make ONE change only: "
   "the PENDANT becomes HALF its present size: the two smooth polished gold bars become HALF as long, each now only about a third of the width "
   "of her lips, and the clear pear-cut stone at the point of the V becomes HALF as wide and HALF as tall, now only about a fifth of the width "
   "of her lips, still in its fine gold claws with its narrow tip at the top joined to the point of the V. The curb chain keeps its present "
   "width and its dense faceted links, and simply runs a little further down to meet the shorter bars. Keep the woman, her lips, skin, hair, "
   "hand, camisole, the background, the light and the framing exactly as they are. Metal: warm 18k gold tone. " + END)
E["A16_W2s"] = ("A16_W2", "EDIT IMAGE 1, a photograph of a woman wearing a gold V-bar teardrop necklace on a curb chain. Make ONE change only: "
   "the WHOLE NECKLACE becomes about HALF its present size: the curb chain about HALF as wide, a fine dense band of small faceted links; the two "
   "smooth polished gold bars HALF as long, each now only about a third of the width of her lips; and the clear pear-cut stone at the point of "
   "the V HALF as wide and HALF as tall, now only about a fifth of the width of her lips, still in its fine gold claws with its narrow tip at "
   "the top joined to the point of the V. The necklace still sits at the base of her throat on the collarbones. Keep the woman, her lips, skin, "
   "hair, camisole, the background, the light and the framing exactly as they are. Metal: warm 18k gold tone. " + END)
E["A16_W1s2"] = ("A16_W1s", "EDIT IMAGE 1, a photograph of a woman wearing a gold V-bar teardrop necklace on a curb chain. Make ONE change "
   "only: the NECKLACE becomes smaller, about SIXTY PERCENT of its present size: the clear pear-cut stone only about a fifth of the width of her "
   "lips; each smooth polished gold bar only about a third of the width of her "
   "lips; and the curb chain a little finer, a slim dense band of small faceted links about a third of the pear's width. The pear keeps its fine "
   "gold claws, its narrow tip at the top joined to the point of the V. Keep the woman, her lips, skin, hair, hand, camisole, the background, the "
   "light and the framing exactly as they are. Metal: warm 18k gold tone. " + END)
E["A16_W2s2"] = ("A16_W2s", "EDIT IMAGE 1, a photograph of a woman wearing a gold V-bar teardrop necklace on a curb chain. Make ONE change "
   "only: the two smooth polished gold bars that form the V become SHORTER, about TWO THIRDS of their present length, each now only about one and "
   "a half times as long as the pear stone is wide, and the curb chain runs a little further down to meet them. Keep the clear pear-cut stone "
   "exactly as it is, its size and claws, at the point of the V, keep the curb chain's links as they are, and keep the woman, her lips, skin, "
   "hair, camisole, the background, the light and the framing exactly as they are. Metal: warm 18k gold tone. " + END)
E["A16_W1f"] = ("A16_W2s2", "Make a NEW photograph from IMAGE 1, a photograph of a woman wearing a gold V-bar teardrop necklace on a curb "
   "chain: the same woman, the same skin, the same long dark wavy hair, the same marigold silk camisole with narrow straps, the same warm cream "
   "background and the same soft light, but now SQUARE TO THE CAMERA, her head and shoulders facing straight on, the necklace centred at the base "
   "of her throat and lying flat on her collarbones. The frame is cut straight across just ABOVE THE UPPER LIP: NO eyes, NO eyebrows, NO forehead; "
   "inside the frame her lips, chin, neck, collarbones, shoulders and upper chest. The necklace keeps EXACTLY the size it has in IMAGE 1 against "
   "her body: the clear pear-cut stone only about a fifth of the width of her lips, each smooth polished gold bar only about a third of the width "
   "of her lips, and the curb chain a slim dense band of small faceted links. IMAGE 2 is our approved packshot of this exact necklace and the "
   "authority on its construction only: two smooth polished gold tube bars meeting in a sharp V, the clear pear-cut stone in fine gold claws "
   "hanging point up from the point of the V, and the dense flat curb chain; its size comes ONLY from IMAGE 1. No other jewellery, no hand, no "
   "props. 4:5 vertical, full bleed. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["A16_He2"])
E["A16_W1f2"] = ("A16_W1f", "EDIT IMAGE 1, a photograph of a woman wearing a gold V-bar teardrop necklace on a curb chain. Make ONE change "
   "only: the two smooth polished gold bars that form the V become SHORTER, about TWO THIRDS of their present length, each now only about one and "
   "a half times as long as the pear stone is wide, and the curb chain runs a little further down to meet them. Keep the clear pear-cut stone "
   "exactly as it is, its size and claws, at the point of the V, keep the curb chain's links as they are, and keep the woman, her lips, skin, "
   "hair, camisole, the background, the light and the framing exactly as they are. Metal: warm 18k gold tone. " + END)
E["A16_Ps"] = ("A16_P", "EDIT IMAGE 1, a photograph of a gold V-bar teardrop necklace on a curb chain resting in an open palm. Make ONE change "
   "only: the WHOLE NECKLACE becomes about HALF its present size: the curb chain about HALF as wide, a slim dense band of small faceted links only "
   "about a fifth of a fingertip's width; the two smooth polished gold bars HALF as long; and the clear pear-cut stone HALF as wide and HALF as "
   "tall, now only about two thirds of the width of one of her fingertips, still in its fine gold claws with its narrow tip at the top joined to "
   "the point of the V. The chain still runs across the palm and over the fingers. Keep the hand, the palm lines, the fingers, the skin, the "
   "background, the light and the framing exactly as they are. Metal: warm 18k gold tone. " + END)
E["A16_Ps2"] = ("A16_Ps", "EDIT IMAGE 1, a photograph of a gold V-bar teardrop necklace on a curb chain resting in an open palm. Make ONE "
   "change only: the two smooth polished gold bars that form the V become HALF as long, each now only about one and a half times as long as the "
   "pear stone is wide, and the curb chain runs a little further in to meet them. Keep the clear pear-cut stone exactly as it is, its size and "
   "its claws, at the point of the V, keep the curb chain's links as they are, and keep the hand, the palm lines, the fingers, the skin, the "
   "background, the light and the framing exactly as they are. Metal: warm 18k gold tone. " + END)
E["A16_W2q"] = ("A16_W2s2", "Make a NEW photograph from IMAGE 1, a photograph of a woman wearing a gold V-bar teardrop necklace on a curb "
   "chain: the same woman, the same skin, the same long dark wavy hair, the same marigold silk camisole with narrow straps, the same warm cream "
   "background and the same soft light, but now her head and shoulders are TURNED A QUARTER TO ONE SIDE, her jaw line in three-quarter profile, "
   "the camera a little closer, so her neck and one collarbone are seen at an angle and the necklace follows the curve of her collarbone, its "
   "polished V and the pear hanging just below the hollow of her throat. The frame is cut straight across just ABOVE THE UPPER LIP: NO eyes, NO "
   "eyebrows, NO forehead; inside the frame her lips, chin, jaw, neck, collarbones and one shoulder. The necklace keeps EXACTLY the size it has in "
   "IMAGE 1 against her body: the clear pear-cut stone only about a fifth of the width of her lips, each smooth polished gold bar only about one "
   "and a half times as long as the pear is wide, and the curb chain a slim dense band of small faceted links. IMAGE 2 is our approved packshot "
   "of this exact necklace and the authority on its construction only; its size comes ONLY from IMAGE 1. No other jewellery, no hand, no props. "
   "4:5 vertical, full bleed. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["A16_He2"])
# 3 Nov, second note on A16 ("the chain of other necklace on listing is wrong, the second image"): the stock chain, seen at 6x in
# refs/A16_chain6x.jpg, is a flat, dense, diamond-cut curb whose links show as narrow slanted rice-grain facets with no holes between
# them; the gallery drew a round-wire open curb. Each frame keeps everything but the chain.
CHAIN6 = ("a FLAT, DENSE, diamond-cut gold CURB chain exactly like the chain in IMAGE 2, a close-up phone photograph of the real chain: "
   "small links pressed flat, each link's bright flat cut face long and narrow like a grain of rice or a slim almond, every link leaning at "
   "the same slant, the links packed so TIGHTLY against each other that NO holes and NO gaps show between them anywhere, so the chain reads "
   "as a narrow flat band of slanted glittering facets with softly rounded edges. Never round-wire links, never open links with holes, never "
   "a chunky Cuban chain, never a cable, rope, box or Figaro chain, never a smooth mirror-flat herringbone or snake chain with no links to see.")
KEEP6 = "take nothing from IMAGE 2 but the chain's links. Metal: warm 18k gold tone, never brassy, orange or greenish. "
E["A16_Hc"] = ("A16_He2", "EDIT IMAGE 1, a packshot of a gold V-bar teardrop necklace on a cream plaster cube. Make ONE change only: the chain "
   "on BOTH sides of the V is REPLACED by " + CHAIN6 + " It is the same chain on the left and on the right, as wide as the polished tube bars "
   "it runs into, about 3.5mm. Keep the two smooth polished gold tube bars, their sharp V, the clear pear-cut stone and its claws, the cube, "
   "the camera, the framing, the background and the light exactly as they are in IMAGE 1; " + KEEP6 + END, ["A16_chain6x_ref"])
E["A16_Mc"] = ("A16_M", "EDIT IMAGE 1, an extreme macro of a gold V-bar teardrop necklace on a cream plaster cube. Make ONE change only: the "
   "chain on BOTH sides of the V is REPLACED by " + CHAIN6 + " It is as wide as the polished tube bars it runs into, and every link in focus "
   "shows its narrow slanted cut face. Keep the two smooth polished gold tube bars, their sharp V, the clear pear-cut stone and its claws, the "
   "plaster, the camera, the focus, the framing, the background and the light exactly as they are in IMAGE 1; " + KEEP6 + END, ["A16_chain6x_ref"])
for key, src_key, what in (("A16_W1c", "A16_W1f2", "a photograph of a woman wearing a gold V-bar teardrop necklace, square to camera"),
                           ("A16_W2c", "A16_W2q", "a photograph of a woman wearing a gold V-bar teardrop necklace, turned a quarter to the side")):
    E[key] = (src_key, f"EDIT IMAGE 1, {what}. Make ONE change only: the chain on BOTH sides of her neck is REPLACED by " + CHAIN6 +
       " It is the SAME chain on the left side and on the right side of her neck, the same slim width as the polished tube bars it runs "
       "into, so at this distance it reads as a slim, flat, close-textured line of tiny slanted glints, never as chunky links. Keep the woman, "
       "her skin, her hair, the camisole, the crop, the two polished bars, the pear stone, their size and their position, the background and "
       "the light exactly as they are in IMAGE 1; " + KEEP6 + END, ["A16_chain6x_ref"])
E["A16_Pc"] = ("A16_Ps2", "EDIT IMAGE 1, a photograph of a gold V-bar teardrop necklace resting in an open palm. Make ONE change only: the "
   "chain is REPLACED by " + CHAIN6 + " It is the same chain on both sides of the V, the same slim width as the polished tube bars it runs "
   "into. Keep the hand, the fingers, the two polished bars, the pear stone, their size and their position, the background and the light "
   "exactly as they are in IMAGE 1; " + KEEP6 + END, ["A16_chain6x_ref"])
# The CHAIN6 edits (A16_Hc, A16_W1c) still drew an open Cuban curb: the word "curb" pulls the model to round wire. Seen again at 6x, the
# stock chain's grains lean in towards each other in a chevron, as on an ear of wheat, so the second wording names a wheat (spiga) chain.
CHAIN7 = ("a dense gold WHEAT chain (a spiga chain) exactly like the chain in IMAGE 2, a close-up phone photograph of the real chain: it is "
   "built of tiny narrow links shaped like grains of rice, each with a bright flat cut face, set in a tight CHEVRON, two rows of grains leaning "
   "in towards each other along the chain like the grains on an ear of wheat; the grains are packed so tightly that NO holes and NO gaps show "
   "anywhere, and the chain reads as a slim, softly rounded cord of glittering slanted grains. Never open links with holes, never a curb or "
   "Cuban chain, never a cable, box or Figaro chain, never a smooth mirror-flat herringbone ribbon, never a snake chain.")
for k in ("A16_Hc", "A16_Mc", "A16_W1c", "A16_W2c", "A16_Pc"):
    s, p, x = E[k]; E[k[:-1] + "w"] = (s, p.replace(CHAIN6, CHAIN7).replace(", about 3.5mm.", ", about 3.5mm wide."), x)
# C2 Clover Garland Necklace (red), 3 Nov: the quarter-view worn frame came back square to camera, a twin of W1, so a true quarter turn is
# made from the approved W1 (C2_W1_a) to keep the clovers' size; the macro drew the petal stones as ovals, and the stock's are round.
E["C2_W2q"] = ("C2_W1_a", "Make a NEW photograph from IMAGE 1, a photograph of a woman wearing a red clover-link necklace: the same woman, "
   "the same skin, the same long dark wavy hair, the same marigold silk camisole with narrow straps, the same warm cream background and the same "
   "soft light, but now her head and shoulders are TURNED A QUARTER TO ONE SIDE, her jaw line in three-quarter profile, the camera a little "
   "closer, so her neck and one collarbone are seen at an angle and the necklace follows the curve of her collarbone round the side of her neck. "
   "The frame is cut straight across just ABOVE THE UPPER LIP: NO eyes, NO eyebrows, NO forehead; inside the frame her lips, chin, jaw, neck, "
   "collarbones and one shoulder. The necklace keeps EXACTLY the size it has in IMAGE 1 against her body: each clover only about a fifth of the "
   "width of her lips, a delicate line about 1cm wide. IMAGE 2 is our approved packshot of this exact necklace and the authority on its "
   "construction only: four round red stones in beaded gold cups round a tiny clear centre stone per clover, one small gold ring between "
   "clovers; its size comes ONLY from IMAGE 1. No hands, no other jewellery, no props. 4:5 vertical, full bleed. Metal: warm 18k gold tone, "
   "never brassy, orange or greenish. " + END, ["C2_H_b"])
E["C2_Me"] = ("C2_M_a", "EDIT IMAGE 1, an extreme macro of a red clover-link necklace on a cream plaster cube. Make ONE change only: every red "
   "petal stone becomes perfectly ROUND, a true circle as wide as it is long, a round faceted bright clear red stone in its own ROUND gold cup "
   "with a fine beaded rim, exactly as IMAGE 2 (a close phone photo of the real clovers) shows them; in every clover the four round cups touch "
   "each other in a two-by-two square round the tiny clear centre stone. Never oval, never pear, never marquise petals. Keep the clovers' size "
   "and positions, the gold rings between them, the plaster, the camera, the focus, the framing, the background and the light exactly as they "
   "are in IMAGE 1. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["C2_det_ref"])
# A14 Solitaire Charm Huggies, 3 Nov: the first worn frame (A14_W1_a) measures about 1.3x: against an ear of about 390 px (about 58 mm)
# the hoop is about 110 px (about 16.5 mm, not 13) and the stone about 50 px (about 7.5 mm, not 6), so the whole earring is shrunk.
E["A14_W1s"] = ("A14_W1_a", "EDIT IMAGE 1, a photograph of a woman wearing a slim gold huggie with a round stone charm. Make ONE change only: "
   "the earring is a little too large: shrink the WHOLE earring together, the slim hoop, the square tube and the round stone, to about FOUR "
   "FIFTHS of its present size, so the hoop is only about a fifth of the height of the whole ear and hugs the lobe through the same piercing, "
   "and the round stone is about half the hoop's width. Keep its construction exactly: the slim plain polished hoop, the short square gold tube "
   "threaded on its bottom, the small ring and the round clear stone in four fine claws hanging below. Keep the woman, the ear, the hair, the "
   "camisole, the crop, the background and the light exactly as they are in IMAGE 1. Metal: warm 18k gold tone, never brassy, orange or "
   "greenish. " + END)
# A14_W2_a (the close ear view) measures about 1.4x: ear about 495 px (about 58 mm), hoop about 158 px (about 18.5 mm), stone about 72 px.
E["A14_W2s"] = ("A14_W2_a", E["A14_W1s"][1].replace("a little too large", "too large").replace("about FOUR FIFTHS", "about TWO THIRDS"))
# C2_P_a (the clover necklace in the palm) measures about 1.6x: each clover is about 150 px against fingers about 140 px wide.
E["C2_Ps"] = ("C2_P_a", "EDIT IMAGE 1, a photograph of a red clover-link necklace gathered in an open palm. Make ONE change only: the necklace "
   "is far too large for the hand: shrink the WHOLE necklace to about SIXTY PERCENT of its present size, every clover and every ring together, so "
   "each clover is only about two thirds of the width of one of her fingers and about eight clovers would fit side by side across her palm; the "
   "line of clovers lies in a looser, smaller coil in the palm with more of the palm showing. Keep its construction exactly: each clover four "
   "round red stones in beaded gold cups round a tiny clear centre stone, one small gold ring between clovers. Keep the hand, the fingers, the "
   "camisole, the background and the light exactly as they are in IMAGE 1. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)
# A14: the shrink edits (A14_W1s, A14_W2s) dropped the square tube, so the two worn frames are fixed locally instead: the earring is
# removed by edit (a bare lobe, same frame), then the earring from the original frame, masked by the difference between the two, is
# pasted back scaled about its piercing to the measured size (comp.py).
BARE = ("EDIT IMAGE 1, a photograph of a woman's ear with one gold huggie earring. Make ONE change only: REMOVE the earring completely, the "
   "hoop, the square tube and the round stone, so the earlobe is bare with no jewellery at all; the skin of the lobe, the neck and the hair "
   "behind where the earring hung are continued naturally. Keep everything else in IMAGE 1 exactly as it is: the ear, its shape and position, "
   "the face, the hair, the camisole, the crop, the background and the light. " + END)
E["A14_W1bare"] = ("A14_W1_a", BARE)
E["A14_W2bare"] = ("A14_W2_a", BARE)
# C2 palm: the palm edit (C2_Ps) did not shrink, so a run of clovers from the approved packshot was laid across the empty-palm plate at
# 10 mm (comp.py run_palm -> out/C2_Pcomp.png, uploaded as C2_Pcomp_ref); one blending edit carries the line on over the palm's edges.
E["C2_Pb"] = ("C2_Pcomp_ref", "EDIT IMAGE 1, a photograph of an open palm with a short line of small red clover links lying across it. Make "
   "ONE change only: the line is part of a longer necklace, so continue it naturally from BOTH ends with more of the same clovers and small "
   "gold rings: from its top end the line runs on over the edge of the palm near the base of the thumb and drops out of sight behind the hand; "
   "from its bottom end it runs on to the lower edge of the palm and a short length hangs down below the hand. Add a soft natural contact "
   "shadow under every clover. Keep every clover already in IMAGE 1 exactly where it is and EXACTLY its size, each clover only about two "
   "thirds of the width of one of her fingers, and make the new clovers the same size: four round red stones in beaded gold cups round a tiny "
   "clear centre stone, one small gold ring between clovers. Keep the hand, the fingers, the camisole, the hair, the background and the light "
   "exactly as they are in IMAGE 1. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)
# C2_Pb_b keeps the design and the 10 mm size, but the loop hanging below the hand shows the clovers' plain gold backs.
E["C2_Pf"] = ("C2_Pb_b", "EDIT IMAGE 1, a photograph of a red clover-link necklace draped over an open palm, a loop of it hanging below the "
   "hand. Make ONE change only: the loop that hangs below the hand is turned to show the FRONT of its clovers, so every clover in it shows "
   "its four round bright red stones in beaded gold cups round a tiny clear centre stone, exactly like the clovers lying on the palm, never "
   "plain gold backs. Keep the loop's size, shape and position, every clover on the palm, the hand, the fingers, the camisole, the hair, the "
   "background and the light exactly as they are in IMAGE 1. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)
# A13 Slim Pave Huggies, 3 Nov (owner: "Check diamond setting and change it"): the pair in hand (refs/A13_set.jpg, both huggies at 2x from
# refs/A13_det.jpg) has a row of round stones down the front, each in its own raised claws so the stones stand proud and fill the band's
# face, and a second row of tiny stones down the outer side of the band; the gallery drew one row of small stones sunk in a railed channel.
SET13 = ("the STONE SETTING becomes exactly like IMAGE 2, a close phone photograph of the real pair: the stones are NOT sunk in a framed "
   "channel between polished rails; the front face of the band is filled by ONE row of round clear stones, each held up in its own small "
   "raised gold claws so the stones stand proud of the band and almost touch, with tiny gold beads between them; and a SECOND row of tiny round "
   "clear stones runs down the OUTER side of the band right beside the first, so the sparkle wraps round the edge of the band. The stones run "
   "from the hinge at the top down the front edge to the bottom corner; the bottom, the back and the inside stay plain polished gold.")
KEEP13 = (" Keep each huggie's rounded-rectangle shape, its size and its hinge, and keep {rest} exactly as they are in IMAGE 1. Metal: warm 18k "
   "gold tone, never brassy, orange or greenish. " + END)
for key, src_key, what, rest in (
    ("A13_Hs", "A13_Hg", "a packshot of a pair of slim gold rounded-rectangle huggie earrings on a cream plaster cube", "the cube, the camera, the framing, the background and the light"),
    ("A13_W1s", "A13_W1qh", "a photograph of a woman wearing a slim gold rounded-rectangle huggie earring", "the woman, the ear, the hair, the camisole, the crop, the background and the light"),
    ("A13_W2s", "A13_W2qs", "a close photograph of a woman's ear wearing a slim gold rounded-rectangle huggie earring", "the woman, the ear, the hair, the camisole, the crop, the background and the light"),
    ("A13_Ms", "A13_Mq", "an extreme macro of one slim gold rounded-rectangle huggie earring on a cream plaster cube", "the plaster, the camera, the focus, the framing, the background and the light"),
    ("A13_Ps", "A13_P", "a photograph of a pair of slim gold rounded-rectangle huggie earrings resting in an open palm", "the hand, the fingers, the background and the light")):
    E[key] = (src_key, f"EDIT IMAGE 1, {what}. Make ONE change only: " + SET13 + KEEP13.format(rest=rest), ["A13_set_ref"])
# A14 Solitaire Charm Huggies, 3 Nov afternoon (owner: "check if it is correct in detail ... check sizing properly as well always"). Against the
# pair in hand (refs/A14_det.jpg: both hoops and the loose charm at 3x, lying flat at one distance) the 3 Nov gallery drew a thin-wire hoop
# (its opening about 0.83 of the hoop's outer width against about 0.73), the square tube about 0.22 of the hoop's width against about a
# third, and the stone about 0.4 of it against about a half; the worn frames also read the hoop at 8 to 11 mm against 13 mm.
PROP14 = ("each earring's PROPORTIONS become exactly like the real pair in IMAGE 2, a close phone photograph of the pair in hand: (1) each HOOP "
   "is a chunky huggie with a THICK, wide, flat-faced polished band, about 2mm thick and 3mm wide, so its round opening is only about THREE "
   "QUARTERS of the hoop's outer width, never a thin wire; (2) the square polished gold TUBE threaded on the bottom of each hoop is a CHUNKY "
   "square bead, about a THIRD of the hoop's outer width on each side, clearly wider and taller than the band that passes through it; (3) "
   "below the tube, on ONE small round gold jump ring, the round clear brilliant-cut stone in four fine gold claws is BIG, about HALF of the "
   "hoop's outer width.")
KEEP14 = (" Keep each hoop's outer size and position and its hinge, and keep {rest} exactly as they are in IMAGE 1. Plain polished gold, no "
   "stones on the hoop. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)
for key, src_key, what, rest in (
    ("A14_Hp", "A14_H_a", "a packshot of a pair of gold huggie earrings with round stone charms on a cream plaster cube", "the cube, the camera, the framing, the background and the light"),
    ("A14_Mp", "A14_M_a", "an extreme macro of one gold huggie earring with a round stone charm on a cream plaster cube", "the plaster, the camera, the focus, the framing, the background and the light")):
    E[key] = (src_key, f"EDIT IMAGE 1, {what}. Make ONE change only: " + PROP14 + KEEP14.format(rest=rest), ["A14_det_ref"])
# A15 Pave Open Heart Studs, 3 Nov afternoon: against the ear (about 58 mm tall, about 31 mm wide) the heart reads about 22 x 21 mm in W1 and about
# 22 x 20 mm in W2 against 20 x 19 mm, so each worn frame gets a bare-lobe edit and the heart is pasted back at 0.90 and 0.92 (comp.py worn).
BARE15 = ("EDIT IMAGE 1, a photograph of a woman's ear with one gold open-heart stud earring. Make ONE change only: REMOVE the earring "
   "completely, the whole pave heart and its post, so the earlobe is bare with no jewellery at all; the skin of the lobe, the neck and the hair "
   "behind where the heart sat are continued naturally. Keep everything else in IMAGE 1 exactly as it is: the ear, its shape and position, "
   "the face, the hair, the camisole, the crop, the background and the light. " + END)
E["A15_W1bare"] = ("A15_W1", BARE15)
E["A15_W2bare"] = ("A15_W2", BARE15)
# The proportion edits thickened the band (opening about 0.74 to 0.77 of the hoop) and gave the tube about a third of the hoop's width,
# but kept the stone at about 0.42 of the hoop and drew two jump rings; the real charm has one ring and a stone about half the hoop.
STONE14 = ("Make TWO changes only: (1) the round clear stone of each charm, with its four fine gold claws, becomes LARGER, about one and a "
   "quarter times its present width, so the stone is HALF as wide as the hoop's outer diameter, as in IMAGE 2, a close phone photograph of "
   "the real pair, where the stone is about half the hoop's outer width; it stays round, brilliant-cut and clear in four claws; (2) exactly "
   "ONE small round gold jump ring hangs from the bottom of the square tube and holds the stone's setting directly, never two rings or a "
   "chain. Keep the hoops, their thick flat-faced bands, the hinges, the square tubes, {rest} exactly as they are in IMAGE 1. Metal: warm "
   "18k gold tone, never brassy, orange or greenish. " + END)
E["A14_Hs2"] = ("A14_Hp_a", "EDIT IMAGE 1, a packshot of a pair of chunky gold huggie earrings with round stone charms on a cream plaster "
   "cube. " + STONE14.format(rest="the cube, the camera, the framing, the background and the light"), ["A14_det_ref"])
E["A14_Ms2"] = ("A14_Mp_a", "EDIT IMAGE 1, an extreme macro of one chunky gold huggie earring with a round stone charm on a cream plaster "
   "cube. " + STONE14.format(rest="the plaster, the camera, the focus, the framing, the background and the light"), ["A14_det_ref"])
# Approved: packshot A14_Hs2_b, macro A14_Ms2_b. The worn frames are drawn again on the bare-lobe frames, with the earring at its true size
# (any scale left over is fixed with comp.py worn, as on 3 Nov).
WORN14 = ("EDIT IMAGE 1, {what} with a bare earlobe. Make ONE change only: she wears ONE earring through a piercing in the centre of her "
   "earlobe: exactly the earring in IMAGE 2, a packshot of the pair, with the same design and proportions: a chunky polished gold huggie hoop "
   "with a thick flat-faced band, closed and hugging the lobe, a chunky square gold tube threaded on the bottom of the hoop, and below it on "
   "one small gold jump ring a round clear stone in four fine claws, about half the hoop's width. TRUE SIZE: the hoop is about 13mm across, "
   "about a QUARTER of the height of her whole ear: its top passes through the piercing and its bottom sits a little below the lower edge of "
   "the lobe; the tube and the stone hang below it, so the whole earring is about 24mm long, about two fifths of the height of her ear; a "
   "small bright earring, never a big hoop. Keep everything else in IMAGE 1 exactly as it is: the ear, its shape and position, the face, the "
   "hair, the camisole, the crop, the background and the light. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)
E["A14_W1n"] = ("A14_W1bare_a", WORN14.format(what="a photograph of a woman"), ["A14_Hs2_b"])
E["A14_W2n"] = ("A14_W2bare_a", WORN14.format(what="a close photograph of a woman's ear"), ["A14_Hs2_b"])
# 3 Nov: the Marquise Drop Choker (Edition Two, YF7059) in silver ("Add same 10 in silver"): the five live gold photos, imported from
# Shopify as MDC_1 (on the cube, 4:5), MDC_2 (worn), MDC_4 (macro), MDC_5 (worn close) and MDC_L (laid, all 1:1), keep everything but
# the metal. ASPECT keeps each edit at its source's shape.
SILVER_MDC = ("EDIT IMAGE 1, {what}. Make ONE change only: the necklace's METAL becomes bright polished SILVER tone, a cool white "
   "rhodium metal, never gold, never yellow, never grey or dull: the ribbed round snake collar with its fine ridges, the claws holding the "
   "sideways marquise stone, the fine drop chain and the small settings of the two pear stones are ALL silver. The clear stones stay "
   "exactly as they are: the same sideways marquise and the same two small pear stones, with the same sizes, positions and sparkle. Keep "
   "EVERYTHING else in IMAGE 1 exactly identical: {keep}; the necklace's shape, size, length, ribbing and position do not change. Nothing "
   "else changes, nothing is added or removed. " + END)
KEEP_OBJ = "the surface, the camera, the framing, the focus, the background and the light"
KEEP_MODEL = "the woman, her skin, her pose, her garment, the background, the light, the framing and the camera"
E["MDC_1s"] = ("MDC_1", SILVER_MDC.format(what="a close photograph of a gold choker necklace on a cream plaster cube", keep=KEEP_OBJ.replace("surface", "cube")))
E["MDC_2s"] = ("MDC_2", SILVER_MDC.format(what="a photograph of a woman wearing a gold choker necklace", keep=KEEP_MODEL))
E["MDC_4s"] = ("MDC_4", SILVER_MDC.format(what="a macro photograph of a gold choker necklace lying on a cream surface", keep=KEEP_OBJ))
E["MDC_5s"] = ("MDC_5", SILVER_MDC.format(what="a close photograph of a woman wearing a gold choker necklace", keep=KEEP_MODEL))
E["MDC_Ls"] = ("MDC_L", SILVER_MDC.format(what="a photograph of a gold choker necklace laid on an ivory surface", keep=KEEP_OBJ))
# MDC_5s_a kept a pale gold collar beside the stone and drew the drop chain rose-copper on the warm skin, so it is redone with a firmer line.
E["MDC_5s2"] = ("MDC_5", SILVER_MDC.format(what="a close photograph of a woman wearing a gold choker necklace", keep=KEEP_MODEL).replace(
   "Nothing else changes,", "ALL of the metal is the SAME cool white silver, like platinum, with NO gold, rose, pink or copper tint anywhere: the collar on BOTH sides of the stone, the claws, the whole drop chain and the settings of both pear stones, even where the metal lies against her warm skin. Nothing else changes,"))
ASPECT = {k: "1:1" for k in ("MDC_2s", "MDC_4s", "MDC_5s", "MDC_Ls", "MDC_5s2")}

if __name__ == "__main__":
    start = int(sys.argv[1]); keys = sys.argv[2].split(",") if len(sys.argv) > 2 else list(E); reqs, idx = [], {}
    for i, key in enumerate(keys):
        src, p, *extra = E[key]                                  # optional third item: further jobs.json keys, sent as IMAGE 2, 3...
        reqs.append({"index": start + i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": ASPECT.get(key, "4:5"), "prompt": p,
                     "medias": [{"value": J[k], "role": "image_references"} for k in [src] + (extra[0] if extra else [])]}})
        idx[start + i] = key
    json.dump(idx, open(f"{H}/idx_{start}.json", "w")); print(json.dumps(reqs, ensure_ascii=False))
