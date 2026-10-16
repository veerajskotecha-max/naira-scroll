# Round 2: two reshoots (ruby one-piece closed oval; droplet with no water on the metal) and six new launch concepts.
import json, importlib.util
spec = importlib.util.spec_from_file_location("f1", "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/e2ads/frames.py")
F1 = importlib.util.module_from_spec(spec)
import sys, io; _o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(F1); sys.stdout = _o
P, S, A, R = F1.P, F1.S, F1.A, F1.R
F = [
 ("E2_ruby_anaar2", "N16", "On a pale ivory lime-plaster surface, half a pomegranate lies cut face up at the upper right edge of the frame, its glistening "
  "deep-red arils packed in white pith; seven loose arils have rolled out across the plaster. ONE single ruby baguette tennis bracelet, CLOSED with its box "
  "clasp shut, lies as ONE continuous unbroken oval loop in the lower middle, the loose arils around it, its stones exactly the same deep red as the seeds.",
  "Each baguette is 5 by 2.5mm; each pomegranate aril is about 9mm, a little larger than one stone; the closed bracelet is a 5.5cm oval, 5mm wide. "
  "There is exactly ONE bracelet and ONE clasp; the loop is never broken into two pieces and never has loose ends.",
  "The upper left third of the frame is calm, empty ivory plaster, softly lit, for a headline."),
 ("E2_droplet_rain2", "P07", "On a smooth pale grey slate just after rain, clear water drops of many sizes are beaded across the slate AROUND the cuff; the "
  "open cuff lies in the lower middle, perfectly dry, its polished ball end and smooth teardrop end sitting among water drops of the same shapes, so the "
  "gold ends look like two more drops. The metal itself carries NO water at all: no drops, no rings, no beads on the gold.",
  "The cuff is about 6cm across; its ball end is 9mm; the water drops on the slate range from 2 to 9mm, so the biggest drop matches the ball.",
  "The upper third of the frame is calm, empty wet slate, softly lit, for a headline."),
 ("E2_knot_gath", "N12", "On a deep red silk dupatta with a thin gold zari border, a corner of the cloth is tied in one soft, loose ceremonial knot (a gathbandhan "
  "knot) at the upper right; the gold knot bangle lies in the lower middle on the silk, its polished X knot echoing the tied cloth.",
  "The bangle is about 6cm across; its X knot is 12mm; the fabric knot is about 7cm, six times the bangle's knot.",
  "The upper left third of the frame is calm, smooth, empty red silk, softly lit, for a headline (headline will be set in cream)."),
 ("E2_duo_gangajamuni", "N14", "On a round antique Ganga-Jamuni platter, worked in alternating inlaid bands of warm brass and pale silver metal, the two-tone "
  "link necklace lies in a relaxed loop across the lower half, its gold-tone and silver-tone links repeating the platter's two metals.",
  "Each oval link is about 20mm long; the platter is 30cm across, its inlaid bands about 15mm wide, close to one link long.",
  "The upper left third of the frame is calm, plain polished metal of the platter rim or soft background, for a headline."),
 ("E2_mesh_silk", "N02", "On a pale ivory lime-plaster surface, a loose skein of raw golden tussar silk yarn lies at the upper right, its fine strands catching "
  "the light; the gold woven-mesh cuff lies in the lower middle, its fine woven mesh rhyming with the silk threads.",
  "The cuff is about 6cm across and its mesh tube 15mm wide; the silk skein is about 15cm long.",
  "The upper left third of the frame is calm, empty ivory plaster, softly lit, for a headline."),
 ("E2_meshring_chai", "P15", "On a pale ivory lime-plaster surface, an old brass tea strainer (chai channi) with a fine woven mesh bowl lies at the upper "
  "right, a few dark tea leaves caught in it, a faint ring of chai on the plaster; the gold mesh band ring stands upright in the lower middle foreground, "
  "its fine woven mesh the same weave as the strainer's.",
  "The ring is 10mm wide and 17mm across inside; the strainer bowl is 7cm across, four times the ring.",
  "The upper left third of the frame is calm, empty ivory plaster, softly lit, for a headline."),
 ("E2_roman_ghadi", "P08", "On cream handmade paper, the face of an old brass wall clock with plain black Roman numerals and slim black hands lies flat at the "
  "upper right, partly out of frame; the three-band Roman numeral ring stands upright on its edge in the lower middle foreground, its numerals echoing the "
  "clock's. The clock face carries only Roman numerals, no words, no brand.",
  "The ring is about 16mm tall and 17mm across inside; the clock face is 25cm across, each numeral on it about 2cm tall.",
  "The upper left third of the frame is calm, empty cream paper, softly lit, for a headline."),
]
Q = []
for key, k, scene, scale, space in F:
    Q.append({"key": key, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": P(k, scene, scale, space),
              "medias": [{"value": A[f"{k}_H"], "role": "image_references"}, {"value": R[S[k]["ref"]], "role": "image_references"}]}})
s = S["P14"]
choker = ("Witty editorial advertising photograph, 4:5 vertical frame, monsoon. A close crop of a young Indian woman's neck and collarbones, warm mid-brown skin "
  "with golden undertones, bare shoulders, a marigold-saffron silk camisole strap at the edge; fine fresh raindrops bead on her skin and two drops run down "
  "toward the collarbone. She wears the slim omega choker at the base of her throat, its marquise stone and the two pear drops on the fine chain falling down "
  "the centre line of her chest, the pears echoing the raindrops beside them.\n\nCROP: the frame is cut straight across at the CHIN; NO lips, NO nose, NO eyes "
  "anywhere in this picture. Inside the frame: chin edge, neck, collarbones, shoulders, upper chest.\n\n" + F1.FID +
  "CONSTRUCTION LOCK: " + s["lock"] + " " + s["neg"] + "\n\nSCALE TEST: The marquise is 10mm wide, about the width of a raindrop's run; each pear is 6mm, the "
  "size of the biggest raindrops; the drop chain is about 6cm, reaching just below the collarbones.\n\nCOPY SPACE: the upper left third of the frame is soft, "
  "plain warm cream background beside the neck, for a headline.\n\n" + F1.LIGHT + "\n\nABSENCE LIST: No text, no letters, no logo, no watermark. No eyes, no nose, "
  "no lips. No other jewellery, no earrings. No props. No border, no vignette: the photograph fills the frame edge to edge.")
Q.append({"key": "E2_choker_monsoon", "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": choker,
          "medias": [{"value": A["P14_H"], "role": "image_references"}, {"value": R[s["ref"]], "role": "image_references"}]}})
json.dump(Q, open("queue2.json", "w"), ensure_ascii=False, indent=0)
print(len(Q), [q["key"] for q in Q])
