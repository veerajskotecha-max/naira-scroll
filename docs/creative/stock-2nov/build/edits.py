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
if __name__ == "__main__":
    start = int(sys.argv[1]); keys = sys.argv[2].split(",") if len(sys.argv) > 2 else list(E); reqs, idx = [], {}
    for i, key in enumerate(keys):
        src, p, *extra = E[key]                                  # optional third item: further jobs.json keys, sent as IMAGE 2, 3...
        reqs.append({"index": start + i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
                     "medias": [{"value": J[k], "role": "image_references"} for k in [src] + (extra[0] if extra else [])]}})
        idx[start + i] = key
    json.dump(idx, open(f"{H}/idx_{start}.json", "w")); print(json.dumps(reqs, ensure_ascii=False))
