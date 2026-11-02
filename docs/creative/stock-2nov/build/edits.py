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
if __name__ == "__main__":
    start = int(sys.argv[1]); keys = sys.argv[2].split(",") if len(sys.argv) > 2 else list(E); reqs, idx = [], {}
    for i, key in enumerate(keys):
        src, p, *extra = E[key]                                  # optional third item: further jobs.json keys, sent as IMAGE 2, 3...
        reqs.append({"index": start + i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
                     "medias": [{"value": J[k], "role": "image_references"} for k in [src] + (extra[0] if extra else [])]}})
        idx[start + i] = key
    json.dump(idx, open(f"{H}/idx_{start}.json", "w")); print(json.dumps(reqs, ensure_ascii=False))
