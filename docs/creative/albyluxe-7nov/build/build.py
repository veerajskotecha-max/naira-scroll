# Albyluxe pieces, 7 Nov 2026 (the owner's 16 photos): a copy of ../../stock-2nov/build/build.py, the house recipe. IMAGE 1 is either the
# owner's phone photo of the piece ("src": "phone") or the supplier's own product photo on albyluxe.com ("src": "shop"); either way it is
# the only authority on what the piece is. The P (palm) shot is made locally from the approved packshot (comp.py palm), not generated. Adds two shots: P, the piece resting in the model's open palm
# (a size proof the owner asked for), and MN, the set's necklace macro. A spec's "detname" names what its IMAGE 2 shows when that is
# not a closer view of the same piece (the set: IMAGE 1 the earrings, IMAGE 2 the necklace).
# Usage: build.py SKU:SHOT,SKU:SHOT,... start_index -> prints requests JSON (and writes idx_<start>.json).
import json, re, sys, os
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
# 12 Nov: the old ending named creases, fold lines and aged paper to forbid them, and two worn frames in a row came out as old folded prints
# (naming a thing primes it): it now describes the clean picture it wants instead.
END = ("No lettering, no watermark, no logo, no tag, no size sticker anywhere in frame. The picture runs edge to edge as a crisp, clean, "
       "modern digital studio photograph, shot today on a high-resolution digital camera.")
NOUN = {"earring": "pair of earrings", "earcuff": "ear cuff", "bangle": "rigid bangle", "cuff": "open cuff bracelet", "set": "set (the necklace and its pair of earrings)"}
METAL = {"gold": "warm 18k gold tone, never brassy, orange or greenish", "silver": "bright rhodium silver tone, never grey or dull, never gold",
         "two-tone": "polished gold tone and bright silver tone exactly where IMAGE 1 shows them",
         "tri-tone": "rose-gold tone, bright silver tone and warm gold tone exactly where IMAGE 1 shows them",
         "rose": "soft rose-gold tone, a pinkish gold, never copper-orange, never yellow gold, never silver",
         "palegold": "a pale, light yellow gold tone, soft and lemony as on the stock, never deep orange 18k, never brassy, never greenish, never rose, never silver"}

def refs(s, plate, hero=None, worn=False):
    if worn and hero and s.get("wref") == "hero":                # the supplier photo kept leaking its backdrop into worn frames
        return ([hero, PL[plate]], "IMAGE 1 is our approved packshot of this exact piece and the ONLY authority on what it is: copy its construction, "
                "proportions, metal colour and stone colour EXACTLY; ignore its cube and its background. IMAGE 1 is a close view, "
                "so the piece's SIZE in this picture comes ONLY from the SCALE TEST below.", 2)
    ids = [R[s["ref"]]]
    names = (("IMAGE 1 is a phone photograph of the actual piece and the ONLY authority on what it is: " if s.get("src") == "phone" else
              "IMAGE 1 is the supplier's own product photograph of this exact piece and the ONLY authority on its design: ")
             + "copy its construction, its metal colour and its stone colour EXACTLY" + (s.get("colour_note", "")) + "; "
             + (re.sub(r"\s*IMAGE 2 [^.]*\.", "", s["note"]) if hero else s["note"]))     # with the packshot as IMAGE 2, the note's own IMAGE 2 line goes
    if hero:
        ids.append(hero); names += (" IMAGE 2 is our approved packshot of this exact piece: the authority on its size, proportions, metal colour and finish;"
                                    " the piece in this picture must match it exactly.")
    elif s.get("det"):
        ids.append(R[s["det"]]); names += s.get("detname", " IMAGE 2 is a close detail of the same piece.")
    return ids + [PL[plate]], names, len(ids) + 1

def prompt(k, shot):
    s = S[k]; kind = s["kind"]; m = METAL[s["metal"]]; hero = A.get(s["mhero"] if shot == "M" and s.get("mhero") else f"{k}_H") if shot != "H" else None
    if shot in ("H", "E"):
        ids, rn, n = refs(s, "block")
        what = (f"ONE {s.get('noun') or NOUN.get(kind, kind)} only, {s['place']}" if shot == "H" else
                f"ONLY the PAIR OF EARRINGS from this set (the necklace is NOT in this picture), {s['eplace']}")
        p = (f"SHOT: Straight-on e-commerce packshot, 4:5. {what}, on a cream plaster cube. "
             f"Camera close, a little above the cube's top face, looking down at about thirty degrees. Macro-sharp on the metal.\n\n"
             f"THE PRODUCT: {rn} IMAGE {n} is here ONLY for the plinth, the camera distance, the background and the light: copy its cube and its framing exactly and ignore everything else about it.\n\n"
             f"CONSTRUCTION LOCK: {s['lock']} {s['neg']}\n\nSCALE TEST: {s['scale']} The piece keeps its true small size against the cube, never enlarged.\n\n"
             f"GROUND: The cream plaster cube fills the lower half of the frame, large and close; flat faces, softly rounded corners, fine plaster grain. "
             f"Warm cream seamless behind with a gentle gradient falloff, never sand, tan, beige or golden. {LIGHT}\n\n"
             f"ABSENCE LIST: No hand, no fingers, no model, no fabric, no props, no flowers, no box. "
            f"{'No jewellery other than this necklace and its two earrings.' if kind == 'set' and shot == 'H' else 'No second piece of jewellery.'} Metal: {m}. {END}")
    elif shot in ("M", "MN"):
        ids, rn, n = refs(s, "macro", hero, worn=True)      # worn=True only matters for wref "hero" pieces
        p = (f"SHOT: Extreme macro, 4:5, of {s['nmacro' if shot == 'MN' else 'macro']}, resting on the top face of a cream plaster cube. Camera very close; the piece fills about two thirds of the frame; "
             f"razor-sharp on the stones and the metal edges, the rest falling softly out of focus.\n\n"
             f"THE PRODUCT: {rn} IMAGE {n} is the authority for the plaster, the background and the light only.\n\n"
             f"CONSTRUCTION LOCK: {s['lock']} {s['neg']}\n\nSCALE TEST: {s['scale']}\n\nLIGHT: {LIGHT}\n\n"
             f"ABSENCE LIST: No hand, no ear, no model, no fabric, no props. No second piece of jewellery."
             f"{' Only ONE earring is in this picture: its partner from the pair is NOT in frame, no second post, no second stone.' if kind in ('earring', 'set') and shot == 'M' else ''}{' Only the necklace is in this picture, no earrings.' if shot == 'MN' else ''}"
             f" Metal: {m}. {END}")
    else:
        if shot == "P":
            plate = "ring"
            sh = (f"SHOT: A size photograph, 4:5 vertical, full bleed: {s['palm']}. The model's hand is turned PALM UP and held nearly LEVEL in front "
                  "of the warm cream background, as if offering the piece, fingers together and gently curved, never raised upright like a wave or a "
                  "stop sign; the camera close and a little above, looking down into the palm, so the piece rests in it naturally and "
                  "is legible and is seen at its TRUE small size against the palm and the fingers.")
            crop = "Inside the frame: the open palm, the fingers and the wrist only. No face, no neck, no camisole."
            where = "resting in her open palm, NOT worn"
        elif kind in ("bracelet", "bangle", "cuff"):
            plate = "wrist"   # 12 Nov: no longer asks for the piece "large" (the cuff's stones came out twice their size)
            # 13 Nov: no more "camera close" for worn frames: the whole hand and wrist stay in frame, so the piece is drawn in proportion to them
            sh = (f"SHOT: A worn photograph: the model's forearm lying across her body, the wrist forward and square to camera, the whole hand and the forearm in frame, the {kind} a small accent at its true size against the wrist. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  f"SHOT: A worn photograph: the hand raised and resting flat against the opposite shoulder, the BACK of the wrist square to camera, the whole hand and the forearm in frame, the {kind} {'sitting loosely around' if kind in ('bangle', 'cuff') else 'lying on'} the wrist at its true small size against it. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: chin, neck, collarbones, shoulder, forearm and hand."
            where = "worn on ONE wrist" + (f", {s['wear']}" if s.get("wear") else "")
        elif kind == "ring":
            plate = "ring"   # 12 Nov: W2 no longer asks for the ring "large" (rings came out up to twice their size)
            # 13 Nov: the whole hand stays in frame, so the ring is drawn in proportion to it (close framing made rings up to twice their size)
            sh = ("SHOT: A worn photograph: the model's hand raised and resting lightly on her collarbone, the WHOLE hand in frame, all its fingers and the wrist, the ring a small accent on one finger in true proportion to the hand. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  "SHOT: Worn ring frame, 4:5: the BACK OF ONE HAND held up flat and square to camera in front of the collarbone, fingers together and relaxed, "
                   "the whole hand and the wrist in frame, so the ring on the ring finger is seen at its true small size against the hand.")
            crop = LIP + " Inside the frame: hand, fingers, wrist, collarbone and shoulder."
            where = s.get("where", "worn on the ring finger only")
        elif kind == "earcuff":
            plate = "earclose"
            sh = ("SHOT: A tight beauty close-up of the ear in profile, hair tucked behind it, the ear cuff on the middle of the outer rim large and legible. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  "SHOT: A three-quarter profile portrait, the ear nearest camera sharp and centred, hair tucked behind it, the ear cuff legible on the outer rim. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: the ear, the jaw, the cheek below the nose, the neck and the shoulder. A cropped beauty detail, NOT a portrait."
            where = "worn on the middle of the outer rim of the ear, no piercing, nothing in the earlobe"
        elif kind == "set" and shot == "W1":
            plate = "ear34"
            sh = ("SHOT: A three-quarter profile portrait, the ear nearest camera sharp, hair tucked behind it, the earring legible on the lobe and the "
                  "necklace's pendant legible in the hollow of the throat. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: the ear, the jaw, the cheek below the nose, the neck, the collarbones and the shoulder. A cropped beauty detail, NOT a portrait."
            where = "the necklace around the neck and one matching earring in each earlobe"
        elif kind in ("earring", "set"):
            plate = "ear34" if shot == "W1" else "earclose"
            sh = ("SHOT: A three-quarter profile portrait, the ear nearest camera sharp and centred, hair tucked behind it, the earring legible in frame. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  "SHOT: A tight beauty close-up of the ear and the jaw line, the camera brought close so every stone on the earring is countable. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: the ear, the jaw, the cheek below the nose, the neck, the collarbone and the shoulder. A cropped beauty detail, NOT a portrait."
            where = "worn in the earlobe: EXACTLY ONE earring in this ear, through a single piercing, never two earrings stacked on the same ear"
        else:
            plate = "ear34"
            sh = ("SHOT: A worn photograph, square to camera: the necklace at the base of the throat lying flat on the collarbones, centred. 4:5 vertical, full bleed."
                  if shot == "W1" else
                  "SHOT: A worn photograph, the head and shoulders turned a quarter to the side, the necklace following the collarbone, close enough that its links or stones are countable. 4:5 vertical, full bleed.")
            crop = LIP + " Inside the frame: chin, neck, collarbones, shoulders and upper chest."
            where = "worn around the neck"
        ids, rn, n = refs(s, plate, hero, worn=True)
        p = (f"{sh}\n\n{crop}\n\nTHE PRODUCT: {rn} IMAGE {n} is the authority on the model, skin, garment, hair, ground and light: match it exactly, "
             f"but she wears ONLY the piece from IMAGE 1, {where}; any other jewellery in IMAGE {n} is removed.\n\n{MODEL}\n\n"
             f"CONSTRUCTION LOCK: {s['lock']} {s['neg']}\n\nSCALE TEST: {(s.get('pscale', '') + ' ' + s['scale']) if shot == 'P' else (s.get('wscale') or s['scale'])} The jewellery keeps its true small size against the body; it is read by bringing the camera closer, never by making the piece bigger.\n\n"
             f"ABSENCE LIST: No eyes, no eyebrows, no forehead. No second piece of jewellery, no watch, no other rings, no other earrings, no necklace unless it is the product. "
             f"No nail polish colour. No props, no flowers. Metal: {m}. {END}")
    if s.get("stoneless"):                 # a plain metal piece: drop the house lines about stones, so none are invented
        p = (p.replace(", its metal colour and its stone colour EXACTLY", " and its metal colour EXACTLY")
              .replace(", metal colour and stone colour EXACTLY", " and metal colour EXACTLY")
              .replace(", and every stone shows internal sparkle and a hard white point, never flat colour.", ", never flat colour.")
              .replace("razor-sharp on the stones and the metal edges", "razor-sharp on the metal edges and the twist"))
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
