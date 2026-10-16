# Writes queue.json: every remaining listing generation as {key, params}, in priority order, for the submit loop.
import json, os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("build", f"{H}/build.py"); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
A = json.load(open(f"{H}/approved.json")); R = json.load(open(f"{H}/ref_ids.json"))
Q = []
def add(key, ids, prompt):
    Q.append({"key": key, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": prompt,
              "medias": [{"value": v, "role": "image_references"} for v in ids]}})
def built(k, shot):
    ids, p = B.prompt(k, shot); add(f"{k}_{shot}", ids, p)
NEW = ["P01", "P05", "P06", "P07", "P08", "P09", "P11", "P12", "P13", "P14", "P15", "P20", "P23"]
for k in NEW: built(k, "W1")
SILVER = ("Change ONLY the metal colour: every metal surface becomes bright polished rhodium SILVER tone, cool white and mirror-bright with dark rolled edges, "
          "the same silver as the SILVER piece in IMAGE 2; never grey, never dull, no gold left anywhere, inside or out. Any stones stay clear and colourless. "
          "Nothing else changes: no new objects, the piece stays the same small size on the cube. No lettering, no watermark, no logo. Full bleed, no border.")
EDIT = "EDIT: IMAGE 1 is our approved product photograph of {d} on a cream plaster cube. Reproduce IMAGE 1 EXACTLY: {same}, the same cube, the same cream background, the same camera, framing, light, shadows and grain. "
for k, d, same, ref in [
    ("P09", "a gold convertible set of three linked rings", "the same three rings (stone-studded band, pavé band, box-chain ring) joined by the same small jump rings in the same positions", "P09_silver"),
    ("P12", "a gold domed band ring with two pavé collars, a chain swag and a pear drop", "the same dome band, the same two pavé collars, the same chain swag and pear drop in the same positions", "P12_silver"),
    ("P15", "a wide gold woven-mesh band ring standing on its edge", "the same woven mesh band with the same rolled edges, the same shape, size and position", "P15_silver")]:
    add(f"{k}_S", [A[f"{k}_H"], R[ref]], EDIT.format(d=d, same=same) + SILVER)
built("P22S", "H")
CUFF = ("SHOT: A worn beauty detail, 4:5 vertical, full bleed: the ear nearest camera in three-quarter view, hair tucked behind it, the camera close so the ear fills "
        "about a third of the frame and the cuff is clearly legible.\n\n" + B.LIP + " Inside the frame: the ear, the jaw, the cheek below the nose, the neck and the shoulder. "
        "A cropped beauty detail, NOT a portrait.\n\nTHE PRODUCT: IMAGE 1 shows how this cuff is worn and is the authority on its construction. IMAGE 2 is our approved "
        "packshot of this exact cuff: the authority on its size, metal and stone. IMAGE 3 is the authority on the model, skin, garment, hair, ground and light: match it, "
        "but she wears ONLY ONE cuff, {stone}, clipped onto the middle ridge of the ear (the conch, halfway up the ear, NOT the lobe), the stone facing forward; any other "
        "jewellery in IMAGE 3 is removed, and the earlobe is bare.\n\n" + B.MODEL + "\n\nCONSTRUCTION LOCK: {lock} {neg}\n\nSCALE TEST: {scale} The ear is about 6cm tall; "
        "the cuff is a small accent on its middle ridge, never larger than a fingernail.\n\nABSENCE LIST: No eyes, no eyebrows, no forehead. No second cuff, no earrings in "
        "the lobe, no necklace, no other jewellery. No props, no flowers. Metal: warm 18k gold tone, never brassy, orange or greenish. " + B.END)
S = json.load(open(f"{H}/skus.json"))
for k, stone in [("C1", "the square emerald-green stone cuff"), ("C2", "the clear pear stone cuff")]:
    s = S[k]; add(f"{k}_W1", [R["C_src"], A[f"{k}_H"], B.PL["ear34"]], CUFF.format(stone=stone, lock=s["lock"], neg=s["neg"], scale=s["scale"]))
for k in ["C1", "C2"] + NEW: built(k, "M")
for k in ["N04"] + [f"N{i}" for i in range(11, 25)]: built(k, "M")
json.dump(Q, open(f"{H}/queue.json", "w"), ensure_ascii=False, indent=0)
print(len(Q), [q["key"] for q in Q])
