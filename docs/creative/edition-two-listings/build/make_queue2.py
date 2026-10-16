# Writes queue2.json: a second worn frame (W2) for every product that would otherwise have only three images, plus both ear cuffs worn together.
import json, os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("build", f"{H}/build.py"); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
A = json.load(open(f"{H}/approved.json")); R = json.load(open(f"{H}/ref_ids.json"))
Q = []
for k in ["P05", "P08", "P11", "P14", "P20", "P23", "N03", "N05", "N10", "N13", "N14", "N15", "N20", "N21", "N24"]:
    ids, p = B.prompt(k, "W2")
    Q.append({"key": f"{k}_W2", "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
              "medias": [{"value": v, "role": "image_references"} for v in ids]}})
p = ("SHOT: A tight worn beauty detail, 4:5 vertical, full bleed: the ear in clean side profile, hair tucked behind it, the camera close so the ear fills about half the "
     "frame and both cuffs are large and legible.\n\n" + B.LIP + " Inside the frame: the ear, the jaw, the cheek below the nose, the neck. A cropped beauty detail, NOT a portrait.\n\n"
     "THE PRODUCT: IMAGE 1 shows exactly how these two cuffs are worn together and is the authority on their construction and placement. IMAGE 2 is our approved packshot "
     "of the green square-stone cuff and IMAGE 3 of the clear pear-stone cuff: the authority on their size, metal and stones. She wears exactly TWO ear cuffs on the same ear, "
     "both clipped onto the middle ridge of the ear (the conch): the clear PEAR-stone cuff higher, the green SQUARE-stone cuff just below it, both stones facing forward; "
     "the earlobe is bare.\n\n" + B.MODEL + "\n\nCONSTRUCTION LOCK: Each cuff is an open C of slim round polished gold wire about 1.5mm thick and about 12mm across. One carries ONE "
     "square princess-cut deep emerald-green stone in four gold claws; the other ONE pear-cut clear colourless stone in gold claws. Never hoops with hinges, never stud posts, "
     "never more than two cuffs.\n\nSCALE TEST: The ear is about 6cm tall; each stone is 5 to 7mm, smaller than a fingernail; the cuffs are small accents on the ear's "
     "middle ridge.\n\nABSENCE LIST: No eyes, no eyebrows, no forehead. No earrings in the lobe, no necklace, no other jewellery. No props. Metal: warm 18k gold tone. " + B.END)
Q.append({"key": "C12_W2", "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
          "medias": [{"value": v, "role": "image_references"} for v in [R["C_src"], A["C1_H"], A["C2_H"]]]}})
json.dump(Q, open(f"{H}/queue2.json", "w"), ensure_ascii=False, indent=0)
print(len(Q), [q["key"] for q in Q])
