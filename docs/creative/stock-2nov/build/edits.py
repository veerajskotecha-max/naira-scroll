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
if __name__ == "__main__":
    start = int(sys.argv[1]); keys = sys.argv[2].split(",") if len(sys.argv) > 2 else list(E); reqs, idx = [], {}
    for i, key in enumerate(keys):
        src, p, *extra = E[key]                                  # optional third item: further jobs.json keys, sent as IMAGE 2, 3...
        reqs.append({"index": start + i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
                     "medias": [{"value": J[k], "role": "image_references"} for k in [src] + (extra[0] if extra else [])]}})
        idx[start + i] = key
    json.dump(idx, open(f"{H}/idx_{start}.json", "w")); print(json.dumps(reqs, ensure_ascii=False))
