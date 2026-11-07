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

if __name__ == "__main__":
    start = int(sys.argv[1]); keys = sys.argv[2].split(","); reqs, idx = [], {}
    for i, key in enumerate(keys):
        src, p, *extra = E[key]
        ids = [J[src]] + [J.get(k) or R[k] for k in (extra[0] if extra else [])]
        reqs.append({"index": start + i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
                     "medias": [{"value": v, "role": "image_references"} for v in ids]}})
        idx[start + i] = key
    json.dump(idx, open(f"{H}/idx_{start}.json", "w")); print(json.dumps(reqs, ensure_ascii=False))
