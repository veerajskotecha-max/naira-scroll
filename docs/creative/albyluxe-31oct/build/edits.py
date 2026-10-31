# Edit requests for the final round (31 Oct): a packshot that is right in construction but wrong in size or drape is given back to
# Nano Banana Pro as IMAGE 1 with one named change, so the cube, camera and light stay as they are. Usage: edits.py start_index.
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__)); J = json.load(open(f"{H}/jobs.json"))
from build import END
E = {
 "B04_H": ("B04_H", "EDIT IMAGE 1, a packshot of a red pave heart pendant on a cream plaster cube. Make ONE change only: the HEART PENDANT becomes "
   "HALF its present size, half as wide and half as tall, about one tenth of the frame's width, a small dainty heart about 8mm across, "
   "smaller than a fingernail. It still hangs at the point of the chain's V by its small rose-gold bail. Its construction stays exactly as in "
   "IMAGE 1: ONE puffed heart covered all over in tiny red pave stones deepening from bright red to dark red at its edges, ONE round clear stone in a "
   "polished rose-gold collar at its centre. Keep everything else in IMAGE 1 exactly as it is: the fine rose-gold cable chain and its V, the cube, "
   "the camera, the framing, the background and the light; the heart's soft contact shadow on the plaster shrinks with it. Metal: soft rose-gold "
   "tone, a pinkish gold, never copper-orange, never yellow gold. " + END),
 "A16_H": ("A16_H", "EDIT IMAGE 1, a packshot of a gold herringbone necklace with a clear pear-cut stone on a cream plaster cube. Make THREE changes "
   "only. (1) The herringbone CHAIN becomes NARROW: about HALF its present width, a fine flat 2mm herringbone that reads as a thin bright gold line, "
   "still stiff and flat, lying in a smooth V. (2) The clear pear-cut stone is TURNED so it hangs POINT UP like a falling drop of water: its narrow "
   "pointed tip at the TOP, joined to the tiny bail, and its round full end at the BOTTOM; it stays clear, faceted and sparkling in fine gold claws, "
   "about 8x12mm, never a pearl. (3) Next to the stone the chain is only about one fifth of the stone's width. Keep everything else in IMAGE 1 exactly "
   "as it is: the cube, the camera, the framing, the background and the light. Metal: warm 18k gold tone, never brassy, orange or greenish. " + END),
}
if __name__ == "__main__":
    start = int(sys.argv[1]); reqs, idx = [], {}
    for i, (key, (src, p)) in enumerate(E.items()):
        reqs.append({"index": start + i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
                     "medias": [{"value": J[src], "role": "image_references"}]}})
        idx[start + i] = f"{key}e"
    json.dump(idx, open(f"{H}/idx_{start}.json", "w")); print(json.dumps(reqs, ensure_ascii=False))
