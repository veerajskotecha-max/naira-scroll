# Aditya jewellery copy of aditya-bracelets/build/build.py: IMAGE 1 wording per piece (skus.json "note"), and an ear cuff kind. Builds Nano Banana Pro listing requests (live Naira listing recipe: plaster-cube packshot, two worn frames on the
# saffron-camisole model plate, macro). A "bangle" is shot like a bracelet but named a rigid bangle (J10, 25 Oct). Usage: build.py SKU:SHOT,SKU:SHOT,... start_index -> prints requests JSON.
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(f"{H}/skus.json")); R = json.load(open(f"{H}/ref_ids.json")); A = json.load(open(f"{H}/approved.json"))
PL = {"block": "8cf120d5-4319-4aee-a284-5f0edc11a513", "macro": "d9cf3baf-ed10-4f13-ba70-81a8f3ead91f",
      "wrist": "0c899647-3a71-476d-8141-5b9e0b42cc4e", "ring": "d19c010a-c90b-4584-b05d-48d6423770d4",
      "ear34": "fd78da3e-a92d-423c-ad14-760305cc8f08", "earclose": "e1e967bf-2b40-48fd-9eb0-245d7ffb85ce"}
LIGHT = ("Soft large key from camera-left, one soft shadow, plus ONE small hard specular kicker from the right, so the metal shows a bright "
         "moving highlight and a dark rolled edge on every curve, and every stone shows internal sparkle and a hard white point, never flat colour.")
MODEL = ("THE PLATE: A young Indian woman, late twenties, warm mid-brown skin with golden undertones. Long dark brown hair in loose natural waves. "
         "Bare shoulders, marigold-saffron silk camisole with narrow spaghetti straps. Nails short, bare, pale nude, no polish colour. "
         "Warm cream seamless with a gentle gradient falloff, never sand, tan, beige or golden. Soft large key from camera-left, one soft shadow.")
LIP = "CROP: The frame is cut straight across just ABOVE THE UPPER LIP. NO eyes, NO eyebrows, NO forehead anywhere in this picture."
END = ("No lettering, no watermark, no logo, no tag, no size sticker anywhere in frame. No border, no frame, no paper edge, no vignette: "
       "the image fills the whole frame edge to edge.")
NOUN = {"earring": "pair of earrings", "earcuff": "ear cuff", "bangle": "rigid bangle"}
METAL = {"gold": "warm 18k gold tone, never brassy, orange or greenish", "silver": "bright rhodium silver tone, never grey or dull, never gold",
         "two-tone": "polished gold tone and bright silver tone exactly where IMAGE 1 shows them",
         "tri-tone": "rose-gold tone, bright silver tone and warm gold tone exactly where IMAGE 1 shows them"}

def refs(s, plate, hero=None):
    ids = [R[s["ref"]]]
    names = ("IMAGE 1 is the supplier photograph and the ONLY authority on what this piece is: copy its construction, its metal colour and its stone colour EXACTLY; "
             + s["note"])
    if hero:
        ids.append(hero); names += (" IMAGE 2 is our approved packshot of this exact piece: the authority on its size, proportions, metal colour and finish;"
                                    " the piece in this picture must match it exactly.")
    elif s.get("det"):
        ids.append(R[s["det"]]); names += " IMAGE 2 is a close detail of the same piece."
    return ids + [PL[plate]], names, len(ids) + 1

def prompt(k, shot):
    s = S[k]; kind = s["kind"]; m = METAL[s["metal"]]; hero = A.get(f"{k}_H") if shot != "H" else None
    if shot == "H":
        ids, rn, n = refs(s, "block")
        p = (f"SHOT: Straight-on e-commerce packshot, 4:5. ONE {NOUN.get(kind, kind)} only, {s['place']}, on a cream plaster cube. "
             f"Camera close, a little above the cube's top face, looking down at about thirty degrees. Macro-sharp on the metal.\n\n"
             f"THE PRODUCT: {rn} IMAGE {n} is here ONLY for the plinth, the camera distance, the background and the light: copy its cube and its framing exactly and ignore everything else about it.\n\n"
             f"CONSTRUCTION LOCK: {s['lock']} {s['neg']}\n\nSCALE TEST: {s['scale']} The piece keeps its true small size against the cube, never enlarged.\n\n"
             f"GROUND: The cream plaster cube fills the lower half of the frame, large and close; flat faces, softly rounded corners, fine plaster grain. "
             f"Warm cream seamless behind with a gentle gradient falloff, never sand, tan, beige or golden. {LIGHT}\n\n"
             f"ABSENCE LIST: No hand, no fingers, no model, no fabric, no props, no flowers, no box. No second piece of jewellery. Metal: {m}. {END}")
    elif shot == "M":
        ids, rn, n = refs(s, "macro", hero)
        p = (f"SHOT: Extreme macro, 4:5, of {s['macro']}, resting on the top face of a cream plaster cube. Camera very close; the piece fills about two thirds of the frame; "
             f"razor-sharp on the stones and the metal edges, the rest falling softly out of focus.\n\n"
             f"THE PRODUCT: {rn} IMAGE {n} is the authority for the plaster, the background and the light only.\n\n"
             f"CONSTRUCTION LOCK: {s['lock']} {s['neg']}\n\nSCALE TEST: {s['scale']}\n\nLIGHT: {LIGHT}\n\n"
             f"ABSENCE LIST: No hand, no ear, no model, no fabric, no props. No second piece of jewellery. Metal: {m}. {END}")
    else:
        if kind in ("bracelet", "bangle"):
            plate = "wrist"
            sh = (f"SHOT: A worn photograph: the model's forearm lying across her body, the wrist forward and square to camera, the {kind} large and legible in frame. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  f"SHOT: A CLOSE worn photograph: the hand raised and resting flat against the opposite shoulder, the BACK of the wrist square to camera, the {kind} LARGE in frame and {'sitting loosely around' if kind == 'bangle' else 'lying on'} the wrist. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: chin, neck, collarbones, shoulder, forearm and hand."
            where = "worn on ONE wrist"
        elif kind == "ring":
            plate = "ring"
            sh = ("SHOT: A worn photograph: the model's hand raised and resting lightly on her collarbone, the ring finger forward, the camera close enough that the ring is clearly legible. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  "SHOT: Worn ring frame, 4:5: the BACK OF ONE HAND held up flat and square to camera in front of the collarbone, fingers together and relaxed, the ring on the ring finger large and legible.")
            crop = LIP + " Inside the frame: hand, fingers, wrist, collarbone and shoulder."
            where = "worn on the ring finger only"
        elif kind == "earcuff":
            plate = "earclose"
            sh = ("SHOT: A tight beauty close-up of the ear in profile, hair tucked behind it, the ear cuff on the middle of the outer rim large and legible. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  "SHOT: A three-quarter profile portrait, the ear nearest camera sharp and centred, hair tucked behind it, the ear cuff legible on the outer rim. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: the ear, the jaw, the cheek below the nose, the neck and the shoulder. A cropped beauty detail, NOT a portrait."
            where = "worn on the middle of the outer rim of the ear, no piercing, nothing in the earlobe"
        elif kind == "earring":
            plate = "ear34" if shot == "W1" else "earclose"
            sh = ("SHOT: A three-quarter profile portrait, the ear nearest camera sharp and centred, hair tucked behind it, the earring legible in frame. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  "SHOT: A tight beauty close-up of the ear and the jaw line, the camera brought close so every stone on the earring is countable. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: the ear, the jaw, the cheek below the nose, the neck, the collarbone and the shoulder. A cropped beauty detail, NOT a portrait."
            where = "worn in the earlobe"
        else:
            plate = "ear34"
            sh = ("SHOT: A worn photograph, square to camera: the necklace at the base of the throat lying flat on the collarbones, centred. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  "SHOT: A worn photograph, the head and shoulders turned a quarter to the side, the necklace following the collarbone, close enough that its links or stones are countable. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: chin, neck, collarbones, shoulders and upper chest."
            where = "worn around the neck"
        ids, rn, n = refs(s, plate, hero)
        p = (f"{sh}\n\n{crop}\n\nTHE PRODUCT: {rn} IMAGE {n} is the authority on the model, skin, garment, hair, ground and light: match it exactly, "
             f"but she wears ONLY the piece from IMAGE 1, {where}; any other jewellery in IMAGE {n} is removed.\n\n{MODEL}\n\n"
             f"CONSTRUCTION LOCK: {s['lock']} {s['neg']}\n\nSCALE TEST: {s.get('wscale') or s['scale']} The jewellery keeps its true small size against the body; it is read by bringing the camera closer, never by making the piece bigger.\n\n"
             f"ABSENCE LIST: No eyes, no eyebrows, no forehead. No second piece of jewellery, no watch, no other rings, no other earrings, no necklace unless it is the product. "
             f"No nail polish colour. No props, no flowers. Metal: {m}. {END}")
    return ids, p

if __name__ == "__main__":
    items = [x.split(":") for x in sys.argv[1].split(",")]; start = int(sys.argv[2])
    reqs = []; idx = {}
    for i, (k, shot) in enumerate(items):
        ids, p = prompt(k, shot)
        reqs.append({"index": start + i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
                     "medias": [{"value": v, "role": "image_references"} for v in ids]}})
        idx[start + i] = f"{k}_{shot}"
    json.dump(idx, open(f"{H}/idx_{start}.json", "w"))
    print(json.dumps(reqs, ensure_ascii=False))
