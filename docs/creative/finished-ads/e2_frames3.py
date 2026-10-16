# Round 3 (last credits): four more launch concepts and one Diwali Prism frame.
import json, importlib.util, sys, io
spec = importlib.util.spec_from_file_location("f1", "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/e2ads/frames.py")
F1 = importlib.util.module_from_spec(spec); _o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(F1); sys.stdout = _o
P, S, A, R = F1.P, F1.S, F1.A, F1.R
F = [
 ("E2_huggie_jamun", "N23_A", "N23", "On a pale ivory lime-plaster surface, a small heap of ripe glossy jamun fruit, deep purple-black with a dusty bloom, sits at the upper "
  "right, one jamun bitten open to show its violet flesh, a purple juice stain on the plaster. The pair of gold huggie hoops lies in the lower middle, their row of "
  "soft AMETHYST-LILAC baguette stones (not red: the stones in IMAGE 1 are amethyst-lilac) answering the fruit's violet.",
  "Each huggie is about 18mm across; each jamun is about 20mm long, close to one hoop; each baguette is 4mm.",
  "The upper left third of the frame is calm, empty ivory plaster, softly lit, for a headline."),
 ("E2_coil_jalebi", "N04_H", "N04", "On a pale ivory lime-plaster surface, one hot golden jalebi, glossy with syrup, its spiral coils catching the light, lies on a small "
  "brass plate at the upper right. The gold triple-coil wrap bangle stands upright in the lower middle, its three stacked ribbed turns rhyming with the jalebi's spiral.",
  "The bangle is about 6cm across and 14mm tall; the jalebi is about 8cm across, a little bigger than the bangle.",
  "The upper left third of the frame is calm, empty ivory plaster, softly lit, for a headline."),
 ("E2_star_dhruv", "N09_H", "N09", "On deep indigo handmade paper speckled with tiny silver-white flecks like a night sky, the slim mirror-polished SILVER bangle with "
  "alternating engraved north stars and round clear stones lies in a relaxed oval in the lower middle; one brighter fleck above it at the upper right glows like a pole star.",
  "The bangle is about 6cm across and 6mm wide; each engraved star is about 5mm; the paper flecks are 1 to 2mm.",
  "The upper left third of the frame is calm, empty indigo paper for a headline (it will be set in cream)."),
 ("E2_tennis_phuljhadi", "P05_H", "P05", "Diwali night. On a dark slate surface, a lit phuljhadi sparkler held in a small brass stand at the upper right throws a soft burst "
  "of golden sparks, blurred; the fine gold tennis bracelet lies in a gentle curve in the lower middle, sharp, every small round stone throwing back a pinpoint of the "
  "sparkler's light.",
  "Each stone is 2.5mm, the size of a mustard seed; the bracelet line is under 3mm wide; the sparkler wire is about 25cm long.",
  "The upper left third of the frame is calm, dark, softly glowing background for a headline (it will be set in cream).",),
]
Q = []
for key, hero, k, scene, scale, space in F:
    Q.append({"key": key, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": P(k, scene, scale, space),
              "medias": [{"value": A[hero], "role": "image_references"}, {"value": R[S[k]["ref"]], "role": "image_references"}]}})
prism = ("Witty editorial advertising still life, 4:5 vertical frame, Diwali evening. Three small handmade paper akash kandil lanterns, star-shaped, one aqua, one soft "
  "pink, one pale butter yellow, glow softly from within at the upper right, slightly out of focus; below them on a pale ivory lime-plaster floor the bracelet lies "
  "open in a gentle curve, each pastel stone carrying the glow of the lantern of its own colour. " + F1.PRISM + " Each lantern is about 20cm across, far larger than "
  "the bracelet. COPY SPACE: the upper left third is calm, softly lit empty plaster wall for a headline. LIGHT: the lanterns' soft coloured glow, a soft warm fill from "
  "the left, one small hard kicker giving the silver a crisp edge and every stone a white catchlight. " + F1.END)
Q.append({"key": "P13_kandil", "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": prism,
          "medias": [{"value": "d7b3663a-9f07-4fc9-b8ca-d1c0110edcaa", "role": "image_references"}, {"value": "e7ef630a-57fb-47f7-8a6e-24b056372a66", "role": "image_references"}]}})
json.dump(Q, open("queue4.json", "w"), ensure_ascii=False, indent=0)
print(len(Q), [q["key"] for q in Q], [[m["value"][:8] for m in q["params"]["medias"]] for q in Q])
