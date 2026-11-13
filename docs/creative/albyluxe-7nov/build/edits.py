# Edit requests: a frame that is right in construction but wrong in one detail is given back to Nano Banana Pro as IMAGE 1 with the
# change named, so the cube, camera and light stay as they are (as ../../stock-2nov/build/edits.py).
# Usage: edits.py start_index KEY,KEY,...  -> prints requests JSON (and writes idx_<start>.json). Each source is a key of jobs.json;
# an optional third item lists further references (jobs.json keys or ref_ids.json names), sent as IMAGE 2, 3...
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__)); J = json.load(open(f"{H}/jobs.json")); R = json.load(open(f"{H}/ref_ids.json"))
sys.path.insert(0, H); from build import END     # -I leaves the script folder off sys.path
E = {}
E["L04_He"] = ("L04_H", "EDIT IMAGE 1, a packshot of a pair of lilac butterfly stud earrings on a cream plaster cube. Make TWO changes only, on "
   "BOTH studs. (1) The UPPER-RIGHT stone of each butterfly becomes a SMALLER, SLIMMER MARQUISE: about three quarters the length and two thirds "
   "the width of the upper-left marquise, still pointing from the centre bead out toward the upper right, still in its fine gold claws, so the "
   "two upper wings are clearly unequal, as IMAGE 2 shows. (2) All the stones become a PALER, softer lilac: a pale lavender with a hint of pink "
   "and bright white sparkle, as IMAGE 2 shows, never deep purple. Keep everything else exactly as it is: the upper-left marquise, the two "
   "larger lower pears with their points toward the centre, the tiny gold bead at each centre, the posts, the cube, the camera, the framing, "
   "the background and the light. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["L04_det"])

# L04_He changed one stud's colour and not the stone sizes, so the second try asks for the size change alone, with no second image
# (the owner's photo pulled one stud pinker); the paler lilac is made locally afterwards, the same on both studs (l04fix.py tone).
E["L04_Hg"] = ("L04_H", "EDIT IMAGE 1, a packshot of a pair of lilac butterfly stud earrings on a cream plaster cube. Make ONE change only, "
   "the SAME on BOTH studs: the stone at the UPPER RIGHT of each butterfly becomes clearly SMALLER and SLIMMER than the stone at the upper "
   "left. Its outer tip moves in toward the centre, so it is only about THREE QUARTERS as long as the upper-left marquise and about two thirds "
   "as wide; it is still a marquise in fine gold claws, pointing from the centre bead out toward the upper right. The other three stones on each "
   "stud keep their size exactly: the upper-left marquise and the two larger lower pears. Both studs stay identical to each other, and every "
   "stone keeps exactly its present lilac colour. Keep everything else in IMAGE 1 exactly as it is: the gold bead at each centre, the posts, "
   "the cube, the camera, the framing, the background and the light. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)

# 13 Nov: the owner says the L03 band is thicker than drawn (their video shows a broad, heavy band with the clusters on thick gold blocks).
# The 7 Nov packshot has the four stones right, so the band alone is changed on it.
E["L03_He"] = ("L03_H", "EDIT IMAGE 1, a packshot of an open cluster ring on a cream plaster cube. Make ONE change only: the gold BAND becomes "
   "BROAD and HEAVY, about 5 to 6mm wide and about 2mm thick, a solid wide band like a cigar band, as IMAGE 2 (the owner's photo of the ring "
   "worn on a finger) shows, with each open end squared off into a thick gold block under its cluster. Keep everything else in IMAGE 1 exactly "
   "as it is: the four clear stones (one small round and one pear on one end, two pears with their points turned outward on the other), their "
   "claws, their positions and their sizes, the row of tiny gold beads, the cube, the camera, the framing, the background and the light. "
   "Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["L03_full"])

# Teardrop Pear Hoops (L11) in silver: the four approved gold frames with the metal changed, as SILVER_MDC in ../../stock-2nov/build/edits.py,
# with the firmer line that the 3 Nov redo needed (no gold, rose or copper tint anywhere, even against the skin).
SILVER_TPH = ("EDIT IMAGE 1, {what}. Make ONE change only: the hoop's METAL becomes bright polished SILVER tone, a cool white rhodium "
   "metal like platinum, never gold, never yellow, never grey or dull: the chunky tapered hoop, its hinge and the claws holding the pear "
   "stone are ALL the SAME cool white silver, with NO gold, rose, pink or copper tint anywhere, even where the metal lies against warm skin. "
   "The clear pear stone stays exactly as it is, with the same size, position and sparkle. Keep EVERYTHING else in IMAGE 1 exactly "
   "identical: {keep}; the hoop's shape, size and position do not change. Nothing else changes, nothing is added or removed. " + END)
KEEP_OBJ = "the cube, the camera, the framing, the focus, the background and the light"
KEEP_MODEL = "the woman, her skin, her ear, her pose, her hair, her garment, the background, the light, the framing and the camera"
E["L11_Hs"] = ("L11_H", SILVER_TPH.format(what="a packshot of a pair of gold teardrop hoop earrings, each with a clear pear stone, on a cream plaster cube", keep=KEEP_OBJ))
E["L11_W1s"] = ("L11_W1", SILVER_TPH.format(what="a photograph of a woman wearing a gold teardrop hoop earring with a clear pear stone", keep=KEEP_MODEL))
E["L11_W2s"] = ("L11_W2", SILVER_TPH.format(what="a close photograph of a woman wearing a gold teardrop hoop earring with a clear pear stone", keep=KEEP_MODEL))
E["L11_Ms"] = ("L11_M", SILVER_TPH.format(what="a macro photograph of a gold teardrop hoop earring with a clear pear stone on a cream plaster cube", keep=KEEP_OBJ))

# Charm Chain Duo Ring (L16): the worn frame W1 has the rings right (a finger between them, as the supplier's photo) but SIX charms, emerald-cut,
# pear, pear, emerald-cut, pear, emerald-cut from the upper ring; removing the third (a pear) leaves the supplier's five in order.
E["L16_W1e"] = ("L16_W1", "EDIT IMAGE 1, a close photograph of a woman's hand wearing two slim gold rings joined by a fine gold chain hung with small "
   "clear charms in gold bezels. Make ONE change only: REMOVE the THIRD charm counting from the upper ring along the chain (a clear PEAR charm, the "
   "lower of the two pears that hang one under the other on the left), together with its tiny jump ring, so the chain carries exactly FIVE charms: "
   "an emerald-cut, a pear, an emerald-cut, a pear and an emerald-cut. Where it hung, the fine chain and the skin of the back of the hand continue "
   "naturally. Keep EVERYTHING else in IMAGE 1 exactly identical: the two rings, the chain's path, the other five charms, the hand, the skin, the "
   "pose, the garment, the background, the light, the framing and the camera. Metal: warm 18k gold tone. " + END)

# Marquise Molten Bar Ring (L02): the redo W2b lays the marquise and the bar straight ACROSS the finger as the owner's photo, but draws the ring
# about 1.8x too large (the bar reads about 37 mm against the finger, the marquise about 19 mm), so it is shrunk with its design and angle kept.
E["L02_W2s"] = ("L02_W2b", "EDIT IMAGE 1, a photograph of a woman holding the back of her hand up in front of her chin, wearing an open gold ring with "
   "a clear marquise stone and a polished molten gold bar lying across her finger. Make ONE change only: the RING is far too large; shrink it to a "
   "little over HALF its present size, so the marquise is only about two thirds as long as the finger is wide (about 10mm) and the molten bar is "
   "only a little longer than the finger is wide (about 22mm), its two rounded ends overhanging the sides of that ONE finger only slightly. Keep its "
   "exact design and angle, as IMAGE 2 shows the ring: the clear marquise in four fine claws and the smooth molten gold bar side by side, both lying "
   "straight ACROSS the finger, on the same finger in the same place, on a slim plain band. Keep everything else in IMAGE 1 exactly as it is: the "
   "woman, her hand, her fingers, her skin, the camisole, the crop, the background and the light. Metal: warm 18k gold tone. " + END, ["L02_H"])

# L02_W2s shrank the ring only part of the way (the marquise still reads about 16 mm against the finger, the bar about 26 mm), so once more.
E["L02_W2t"] = ("L02_W2s", "EDIT IMAGE 1, a photograph of a woman holding the back of her hand up in front of her chin, wearing an open gold ring "
   "with a clear marquise stone and a polished molten gold bar lying across her finger. Make ONE change only: the RING is still too large; shrink "
   "it to about TWO THIRDS of its present size, so the marquise is clearly SHORTER than the finger is wide (about 10mm, two thirds of the "
   "finger's width) and the molten bar is only a little longer than the finger is wide. Keep its exact design and angle: the clear marquise and "
   "the molten bar side by side, both lying straight ACROSS the finger, on the same finger in the same place. Keep everything else in IMAGE 1 "
   "exactly as it is: the woman, her hand, her fingers, her skin, the camisole, the crop, the background and the light. Metal: warm 18k gold tone. " + END)

# 12 Nov corrections (../corrections.md). Each is ONE change on an approved frame, so its cube, camera and light stay.
# Blush Octagon Studs (L05): the packshot drew a square with small clipped corners; the owner's stone is a REGULAR octagon (IMAGE 2: her photo).
E["L05_He"] = ("L05_H", "EDIT IMAGE 1, a packshot of a pair of blush pink octagon stud earrings on a cream plaster cube. Make ONE change only, the "
   "SAME on BOTH studs: each stone's outline becomes a REGULAR OCTAGON with all EIGHT sides the SAME length: the four short diagonal corner sides "
   "grow until they are as long as the four straight sides, so the stone reads almost round, like the outline of the stone in IMAGE 2, never a "
   "square with small clipped corners. The slim gold setting follows the new outline, with its fine claws at the corners. Keep everything else in "
   "IMAGE 1 exactly as it is: the stone's colour and sparkle, its size across, the posts, the cube, the camera, the framing, the background and "
   "the light. Use IMAGE 2 ONLY for the stone's outline. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END, ["L05_det"])
# Duet Emerald-Cut Cuff (L09): the pink step-cut was a long narrow rectangle; the supplier's is only a little longer than wide and as wide as the square.
E["L09_He"] = ("L09_H", "EDIT IMAGE 1, a packshot of an open gold cuff bangle with a clear square stone at one end and a pink emerald-cut stone at "
   "the other, on a cream plaster cube. Make ONE change only: the PINK emerald-cut stone and its gold box become WIDER, so the pink stone is only "
   "slightly longer than it is wide (about 5 by 6 mm) and as wide as the clear square stone at the other end, with its step-cut facets kept; its "
   "box grows with it and keeps its four claws. Keep everything else in IMAGE 1 exactly as it is: the clear square stone and its box, the wire, "
   "the cube, the camera, the framing, the background and the light. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)
# Baguette Heart Studs (L12): the two small stones at the lower corners of each heart are SQUARE on the supplier's piece, drawn round.
E["L12_He"] = ("L12_H", "EDIT IMAGE 1, a packshot of a pair of gold heart stud earrings, each set with clear baguette stones, on a cream plaster "
   "cube. Make ONE change only, the SAME on BOTH studs: the two small ROUND stones at the lower left and lower right of each heart become small "
   "clear SQUARE step-cut stones, each in its own square gold collet, as wide as the baguettes beside them, with no claws. Keep everything else in "
   "IMAGE 1 exactly as it is: the eight baguettes, the rim, the tiny gold beads, the posts, the cube, the camera, the framing, the background and "
   "the light. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END)
# Two-Tone Heart Snake Chain (L07): the macro drew a round chain of coarse scales; the piece (IMAGE 2, the packshot) has a flat, finely ribbed ribbon.
E["L07_Mc"] = ("L07_Mb", "EDIT IMAGE 1, a macro photograph of three heart beads (polished silver, gold covered in tiny clear stones, polished "
   "silver) threaded on a silver chain, on a cream plaster cube. Make ONE change only: the CHAIN becomes a FLAT, smooth, bright silver ribbon "
   "snake chain about a third of a heart's width, with very fine ribbing across it, exactly like the chain in IMAGE 2, never round, never coarse "
   "rounded scales. Keep everything else in IMAGE 1 exactly as it is: the three hearts, their colours and stones, the cube, the camera, the "
   "framing, the focus, the background and the light. Metal: bright rhodium silver tone and warm gold tone exactly where IMAGE 1 shows them. " + END, ["L07_H"])
# Teardrop Pear Hoops (L11) Silver: gold was left on the pear's claws in the silver macro and close worn frame.
CLAWS_TPH = ("EDIT IMAGE 1, {what}. Make ONE change only: the three small CLAWS holding the clear pear stone, and the little setting under it, "
   "become the SAME cool bright silver as the hoop: no gold, champagne, bronze or warm tint on them anywhere. Keep EVERYTHING else in IMAGE 1 "
   "exactly identical: {keep}, the hoop and the pear stone. Nothing else changes. " + END)
E["L11_Msc"] = ("L11_Ms", CLAWS_TPH.format(what="a macro photograph of a silver teardrop hoop earring with a clear pear stone on a cream plaster cube", keep=KEEP_OBJ))
E["L11_W2sc"] = ("L11_W2s", CLAWS_TPH.format(what="a close photograph of a woman wearing a silver teardrop hoop earring with a clear pear stone", keep=KEEP_MODEL))
# 12 Nov: the silver worn frame now comes from the remade W1 (L11_W1y, the hoop at its true size against the ear).
E["L11_W1ys"] = ("L11_W1y", SILVER_TPH.format(what="a photograph of a woman wearing a gold teardrop hoop earring with a clear pear stone", keep=KEEP_MODEL))
# Interlocked Baguette Trio Ring (L10): the 7 Nov packshot has the gold square channel and the wide flush-set band right but the SILVER band plain;
# on the supplier's sheet the silver band carries a channel of green baguettes between silver rails.
E["L10_He"] = ("L10_H", "EDIT IMAGE 1, a packshot of a stacked ring of three bands (a slim gold band with a channel of small green square stones, a "
   "plain silver band, and a wide gold band with round green stones set flush) on a cream plaster cube. Make ONE change only: the middle SILVER band "
   "gets a channel of small rectangular BAGUETTE-cut deep emerald-green stones, set end to end all along its visible face between two thin bright "
   "silver rails, like the channel of square stones on the gold band beside it but with longer, narrower stones. Keep everything else in IMAGE 1 "
   "exactly as it is: the gold square-stone band, the wide gold band and its round stones, the band widths, the cube, the camera, the framing, the "
   "background and the light. Metal: polished gold tone and bright silver tone exactly where IMAGE 1 shows them. " + END)

if __name__ == "__main__":
    start = int(sys.argv[1]); keys = sys.argv[2].split(","); reqs, idx = [], {}
    for i, key in enumerate(keys):
        src, p, *extra = E[key]
        ids = [J[src]] + [J.get(k) or R[k] for k in (extra[0] if extra else [])]
        reqs.append({"index": start + i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
                     "medias": [{"value": v, "role": "image_references"} for v in ids]}})
        idx[start + i] = key
    json.dump(idx, open(f"{H}/idx_{start}.json", "w")); print(json.dumps(reqs, ensure_ascii=False))
