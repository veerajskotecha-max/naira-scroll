# 25 Oct sizing fix: requests for the worn photos that read too big, and the ear cuff on-ear reshoot.
# For each oversized piece two variants: "c" blends a hand composite (the piece cut out, scaled to its listed size and pasted
# back, made by scratchpad tools/shrink.py) and "e" is a plain shrink edit of the approved photo with the packshot as IMAGE 2.
# Usage: fix_requests.py COMPOSITE_IDS_JSON START -> writes req_fix_a.json (first 12) and req_fix_b.json, and idx_START.json.
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(f"{H}/skus.json")); A = json.load(open(f"{H}/approved.json")); R = json.load(open(f"{H}/ref_ids.json"))
C = json.load(open(sys.argv[1])); start = int(sys.argv[2])
END = "No lettering, no watermark, no logo, no border, no vignette: the image fills the whole frame edge to edge."
PIECES = {  # key: (noun, garment-or-body, extra clean-up note, shrink request, target against the body)
 "J01": ("clover pendant", "camisole", "",
         "about 40% of its current size", "the upper clover about 8.5mm, the width of her little fingernail, and the whole drop about 17mm, about a third of the width of her mouth"),
 "J02": ("clover drop earring", "hair", "The earlobe around the stud and the neck and hair behind the drop must look natural and untouched.",
         "well under half of its current size", "the whole earring about 19mm long, about a third of the height of her ear, the clover on the lobe smaller than the lobe itself"),
 "J03": ("clover on the bracelet", "camisole", "The two thin straight gold strokes where the chain meets the clover are placeholders: redraw each as the same fine gold cable chain as the rest of the bracelet, so the chain runs on continuously into the clover.",
         "less than half of its current size", "the clover about 9mm across, about a sixth of the width of her wrist, the chain as fine as before"),
 "J05": ("twin heart pendant", "camisole", "The two thin straight gold strokes where the chain meets the hearts are placeholders: redraw each as the same fine gold cable chain as the rest of the necklace, so the chain runs on continuously into the hearts.",
         "less than half of its current size", "the two hearts together about 8.5mm across, the width of a fingernail, about a sixth of the width of her mouth"),
 "J07": ("bow pendant", "camisole", "The two thin straight gold strokes where the chain meets the bow are placeholders: redraw each as the same fine gold cable chain as the rest of the necklace, so the chain runs on continuously into the bow.",
         "about 40% of its current size", "the bow about 10mm wide and the whole pendant about 15mm tall, less than a third of the width of her mouth"),
 "J08": ("blossom on the bracelet", "camisole", "The two thin straight gold strokes where the chain meets the blossom are placeholders: redraw each as the same fine gold cable chain as the rest of the bracelet, so the chain runs on continuously into the blossom.",
         "half of its current size", "the blossom about 8.5mm across, about a sixth of the width of her wrist, the chain as fine as before"),
 "J16": ("three-stone pear drop", "camisole", "",
         "about 40% of its current size", "the whole three-stone drop about 12mm long, a quarter of the width of her mouth"),
 "J17": ("pear drop hoop earring", "hair", "The earlobe and the hair behind the drop must look natural and untouched.",
         "half of its current size", "the whole earring about 21mm long, about a third of the height of her ear, the huggie hoop no bigger than her earlobe"),
}
def blend(k):
    n, g, extra, _, _ = PIECES[k]
    return (f"EDIT IMAGE 1. IMAGE 1 is a finished jewellery photograph that has been retouched: the {n} was made smaller and the skin where the larger "
            f"{n} used to sit was patched by hand. Your job is the final clean-up only. Keep EVERYTHING exactly as it is in IMAGE 1: the woman, her skin "
            f"tone, the light, the {g}, the framing and the crop, and above all the {n} itself: its exact size, its exact position, its shape and every "
            f"stone stay EXACTLY as they are in IMAGE 1. Do not enlarge it, do not move it, do not redesign it. Change ONE thing only: make the patched "
            f"area around the {n} look completely untouched, real skin with its pores and fine texture running on smoothly, no smudge, no blur, no ghost "
            f"outline, no light or dark blotch, and the {n} casting its own small soft shadow where it touches the skin. {extra} {END}")
def shrink(k):
    n, g, _, ask, tgt = PIECES[k]
    return (f"EDIT IMAGE 1. Keep EVERYTHING in IMAGE 1 exactly the same: the woman, her skin, the light, the {g}, the framing and the crop. Change ONE "
            f"thing only: the {n} is far too big for the real piece, so redraw it much smaller, at {ask}: {tgt}. It stays in the same place, with "
            f"exactly the same design as in IMAGE 2, our packshot of this exact piece: {S[k]['lock']} The skin around it stays natural and untouched, "
            f"and it casts a small soft shadow. {END}")
LIP = "CROP: The frame is cut straight across just ABOVE THE UPPER LIP. NO eyes, NO eyebrows, NO forehead anywhere in this picture."
MODEL = ("THE PLATE: A young Indian woman, late twenties, warm mid-brown skin with golden undertones. Long dark brown hair in loose natural waves, "
         "tucked behind the ear. Bare shoulders, marigold-saffron silk camisole with narrow spaghetti straps. Warm cream seamless with a gentle gradient "
         "falloff, never sand, tan, beige or golden. Soft large key from camera-left, one soft shadow, plus ONE small hard specular kicker from the right "
         "so the gold shows a bright moving highlight and a dark rolled edge on every curve.")
s = S["J11"]
PLACE = ("PLACEMENT, THE MOST IMPORTANT INSTRUCTION: the cuff is clipped onto the curled outer rim of the ear (the helix) at the BACK EDGE of the ear, "
         "exactly HALFWAY between the top of the ear and the bottom of the earlobe, level with the ear canal. The thin cartilage rim slides into the "
         "cuff's open slot, so the cuff hugs the rim: part of it sits on the front of the rim facing the camera and it wraps round the edge to the "
         "back of the ear. The cuff stays UPRIGHT exactly as it stands on the cube in IMAGE 2: its wavy loops run straight UP AND DOWN, parallel to the "
         "edge of the rim, side by side. The earlobe is completely bare: nothing on, around or through it. Never in the bowl of the ear, never across "
         "the ear, never on or near the lobe, never at the top of the ear.")
SCALE = ("SCALE TEST: the cuff is small: about 12mm tall and 15mm across, about one fifth of the height of her ear, so the ear is five times taller "
         "than the cuff. It covers only a short stretch of the rim; the rim above it and below it is bare skin. The jewellery keeps its true small "
         "size against the body; it is read by bringing the camera closer, never by making the piece bigger.")
def cuff(variant):
    sh = ("SHOT: A tight beauty close-up of one ear in clean side profile, the ear square to the camera and sharp from the top of the rim to the "
          "bottom of the lobe, hair tucked behind it. 4:5 vertical, full bleed." if variant == 1 else
          "SHOT: A close beauty photograph of the side of the head, the camera level with the ear and slightly behind the jaw, the whole ear sharp "
          "and centred, hair swept back behind it, the cuff clearly gripping the back edge of the rim. 4:5 vertical, full bleed.")
    return (f"{sh}\n\n{LIP} Inside the frame: the whole ear, the jaw, the cheek below the nose, the neck and a little shoulder. A cropped beauty "
            f"detail, NOT a portrait.\n\nTHE PRODUCT: IMAGE 1 is the supplier photograph and the ONLY authority on what this piece is: copy its "
            f"construction and its metal colour EXACTLY; {s['note']} IMAGE 2 is our approved packshot of this exact piece: the authority on its "
            f"size, proportions, metal colour and finish. IMAGE 3 is the authority on the model, skin, garment, hair, ground and light: match it, "
            f"but she wears ONLY this ear cuff and no other jewellery.\n\n{PLACE}\n\n{MODEL}\n\nCONSTRUCTION LOCK: {s['lock']} {s['neg']}\n\n"
            f"{SCALE}\n\nABSENCE LIST: No eyes, no eyebrows, no forehead. No earring in the lobe, no second cuff, no necklace, no rings. No props. "
            f"Metal: warm 18k gold tone, never brassy, orange or greenish. {END}")
CUFF_EDIT = ("EDIT IMAGE 1. Keep EVERYTHING exactly the same: the woman, her ear, skin, hair, light, framing and crop. Change ONE thing only: the "
             "gold ear cuff. Move it UP the outer rim to the middle of the ear, level with the ear canal, and make it smaller, about one fifth of "
             "the height of the ear. Turn it so its wavy loops run straight UP AND DOWN along the edge of the rim, exactly as the cuff stands "
             "upright on the cube in IMAGE 2; it still hugs the rim, wrapping from the front of the rim round to the back. The lower rim and the "
             f"earlobe where it was become bare, natural skin. The cuff keeps the design of IMAGE 2: {s['lock']} {END}")
reqs, idx = [], {}
def add(key, prompt, medias):
    i = start + len(reqs)
    reqs.append({"index": i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": prompt,
                                        "medias": [{"value": v, "role": "image_references"} for v in medias]}})
    idx[i] = key
add("J11_W1s", cuff(1), [R["J11_full"], A["J11_H"], "e1e967bf-2b40-48fd-9eb0-245d7ffb85ce"])
add("J11_W1t", cuff(2), [R["J11_full"], A["J11_H"], "e1e967bf-2b40-48fd-9eb0-245d7ffb85ce"])
add("J11_W1u", CUFF_EDIT, ["97acff44-a633-4f3a-b9a7-86689d9d30e2", A["J11_H"]])
for k in PIECES:
    add(f"{k}_W1c", blend(k), [C[f"{k}_c"]])
    add(f"{k}_W1s", shrink(k), [A[f"{k}_W1"], A[f"{k}_H"]])
json.dump(reqs[:12], open(f"{H}/req_fix_a.json", "w"), ensure_ascii=False)
json.dump(reqs[12:], open(f"{H}/req_fix_b.json", "w"), ensure_ascii=False)
json.dump(idx, open(f"{H}/idx_{start}.json", "w"))
print(len(reqs), "requests", sum(len(r["params"]["prompt"]) for r in reqs), "chars"); print(idx)
