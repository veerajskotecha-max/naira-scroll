# Edition Two launch ad frames (plus two Diwali Prism frames): one product per frame beside a same-size Indian referent.
# IMAGE 1 = the approved listing packshot (fidelity), IMAGE 2 = supplier photo (construction). Writes queue.json for the submit loop.
import json, os
L = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/listing"
S = json.load(open(f"{L}/skus.json")); A = json.load(open(f"{L}/approved.json")); R = json.load(open(f"{L}/ref_ids.json"))
LIGHT = ("LIGHT: soft large window light from the upper left, one soft natural shadow, plus ONE small hard specular kicker from the right, so the metal shows a crisp "
         "bright edge and a dark rolled edge on every curve and every stone carries internal sparkle and one pure-white catchlight, never flat colour. "
         "Honest macro optics: the jewellery is needle-sharp and the scene falls softly out of focus behind it. Real texture everywhere: grain, fibre, dust, "
         "believable imperfection, nothing plastic.")
END = ("ABSENCE LIST: No text, no letters, no logo, no watermark, no price tag anywhere in frame. No hands, no people. No second piece of jewellery. "
       "No border, no vignette: the photograph fills the frame edge to edge.")
FID = ("THE PRODUCT: IMAGE 1 is our approved product photograph and the authority on this exact piece: its construction, size, metal colour and stone colour; "
       "ignore its plaster cube, background and light. IMAGE 2 is the supplier photograph of the same piece, for construction detail only; ignore everything "
       "else in it. Preserve the piece exactly: do not redesign, restyle, resize or add anything. ")
def P(k, scene, scale, space, extra=""):
    s = S[k]
    return (f"Witty editorial advertising still life, 4:5 vertical frame, for an Indian demi-fine jewellery brand. {scene}\n\n{FID}"
            f"CONSTRUCTION LOCK: {s['lock']} {s['neg']}\n\nSCALE TEST: {scale} The jewellery keeps its true small size against the referent; it dominates "
            f"by light and isolation, never by being enlarged.\n\nCOPY SPACE: {space}\n\n{LIGHT} {extra}\n\n{END}")
F = [
 ("E2_ruby_anaar", "N16", "On a pale ivory lime-plaster surface, half a pomegranate lies cut face up at the upper right edge of the frame, its glistening "
  "deep-red arils packed in white pith; nine loose arils have rolled out across the plaster. The ruby baguette tennis bracelet lies in a relaxed open curve "
  "in the lower middle, threading between the loose arils, its stones exactly the same deep red as the seeds, so the eye has to look twice.",
  "Each baguette is 5 by 2.5mm; each pomegranate aril is about 9mm, a little larger than one stone; the bracelet is 17cm long and 5mm wide.",
  "The upper left third of the frame is calm, empty ivory plaster, softly lit, for a headline."),
 ("E2_emerald_elaichi", "N17", "On a pale ivory lime-plaster surface, a small heap of plump green cardamom pods sits at the upper right, two pods split open "
  "to show their dark seeds, a few loose pods scattered toward the centre. The emerald baguette tennis bracelet lies in a relaxed open curve in the lower "
  "middle, its stones the same fresh green as the pods.",
  "Each baguette is 5 by 2.5mm; each cardamom pod is about 9mm long, nearly two stones long; the bracelet is 17cm long and 5mm wide.",
  "The upper left third of the frame is calm, empty ivory plaster, softly lit, for a headline."),
 ("E2_crystal_mishri", "N06", "On a pale sand-coloured handwoven linen cloth, a small heap of mishri, clear irregular rock-sugar crystals of 5 to 12mm, "
  "glints at the upper right in a tiny brass katori bowl, a few crystals spilled out onto the linen. The clear baguette tennis bracelet lies in a relaxed "
  "open curve in the lower middle, its crisp step-cut stones answering the rough sugar crystals.",
  "Each baguette is about 4mm wide; each sugar crystal is 5 to 12mm, one to three stones across; the katori is about 7cm; the bracelet is 17cm long.",
  "The upper left third of the frame is calm, empty linen, softly lit, for a headline."),
 ("E2_studs_mogra", "P06", "On pale sage handwoven linen, a loose scatter of fresh white mogra (Arabian jasmine) buds and two half-open blossoms runs "
  "diagonally from the upper right; the pair of flower studs lies among the buds in the lower middle, stones up, so the clear petals read as one more "
  "small white flower. A faint dew on the petals.",
  "Each stud is about 13mm tall; each jasmine bud is 10 to 14mm, about the same size as a stud, so they look like part of the same bunch.",
  "The upper left third of the frame is calm, empty sage linen, softly lit, for a headline."),
 ("E2_mint_nimbu", "N13", "On a pale grey kota-stone surface, a tall clear glass of nimbu pani with a thin lime wheel and a sprig of mint stands at the upper "
  "right, cold condensation beading on the glass, a halved green lime beside it. The pair of drop earrings lies flat in the foreground lower middle, "
  "their pale lime-green pear stones echoing the lime.",
  "Each earring is about 22mm long; the pale green pear stone is 9mm, about the size of one segment of the lime's cut face; the glass is 14cm tall.",
  "The upper left third of the frame is calm, empty pale stone and soft background, for a headline.",
  "The glass and lime are softly out of focus; the earrings are needle-sharp."),
 ("E2_tubogas_churi", "P01", "On a pale ivory plaster shelf, a tall stack of thin ribbed gold glass bangles (churis) lies on its side as a short cylinder "
  "at the right, softly out of focus, its fine ridges rhyming with the ring. The wide tubogas dome ring stands upright on its edge in the lower middle "
  "foreground, sharp, its ridges catching the light.",
  "The ring is about 17mm across inside and 10mm wide; each bangle is 65mm across, nearly four times the ring, so the ring reads as a tiny bangle stack "
  "for one finger.",
  "The upper left third of the frame is calm, empty plaster, softly lit, for a headline."),
 ("E2_watch_haath", "P13", "On cream handmade paper, an old two-tone steel-and-gold wristwatch with a plain ivory dial (no lettering, no logo, no numerals) "
  "lies open at the upper right, its bracelet of three rows of polished links curving across the paper; the wide watch-link ring stands upright on its "
  "edge in the lower middle, its three rows of links clearly the same family as the strap.",
  "The ring is 11mm wide and 17mm across inside; the watch strap is about 18mm wide, a little wider than the ring; the watch case is 35mm.",
  "The upper left third of the frame is calm, empty cream paper, softly lit, for a headline."),
 ("E2_droplet_rain", "P07", "On a smooth pale grey slate just after rain, clear water drops of many sizes are beaded across the surface; the open cuff lies "
  "in the lower middle, its polished ball end and teardrop end sitting among real water drops of the same shapes, two small drops resting on the gold "
  "itself, each drop with its own tiny reflection.",
  "The cuff is about 6cm across; its ball end is 9mm; the water drops range from 2 to 9mm, so the biggest drop matches the ball.",
  "The upper third of the frame is calm, empty wet slate, softly lit, for a headline."),
]
PRISM = ("Preserve the bracelet from reference 1 exactly, with its stones built exactly as in reference 2: a continuous line of square cushion-cut stones about 5mm each "
 "in the repeating order aqua blue, soft pink, pale yellow, every stone framed by its own fine pave halo of tiny clear stones, linked in rhodium silver tone with a "
 "fold-over clasp. Do not redesign, restyle, resize or add anything; the stones must stay cushion-cut pastel stones in the repeating aqua, pink, yellow order, never "
 "all one colour, never round, never other colours, and no two neighbouring stones are ever the same colour; every stone keeps its halo of two rows of very fine pave, "
 "the halo about a third as wide as the centre stone on each side; each stone is held by four short round bead claws flush at its corners, never long prongs or "
 "spikes. Only the background, surface and lighting change. CRITICAL SCALE: each stone is about 5mm, the size of a peppercorn, and each stone in its halo is about "
 "8mm square; the bracelet is about 18cm long and only about 8mm wide, a slim line.")
PF = [
 ("P11_diya", "Witty editorial advertising still life, 4:5 vertical frame, Diwali evening. On a pale ivory lime-plaster floor, three small hand-thrown terracotta "
  "diyas, each about 7cm across, burn with small steady flames in a gentle arc at the upper right. The bracelet lies open in a soft curve around their "
  "front, and every pastel stone holds a tiny warm reflection of the flames. " + PRISM + " The diyas are about nine times the width of the bracelet's line. "
  "COPY SPACE: the upper left third is calm, softly glowing empty plaster for a headline. LIGHT: the warm diya flames as the key, a soft cool fill from the left "
  "so the aqua and pink keep their colour, one small hard kicker on the silver. " + END),
 ("P12_saree", "Witty editorial advertising still life, 4:5 vertical frame. Three neatly folded silk sarees are stacked at the right of the frame, aqua on "
  "the bottom, soft pink in the middle, pale butter yellow on top, their zari borders a thin line of muted gold; the bracelet lies straight across the top "
  "fold of the stack and runs off onto the pale ivory plaster in front, its aqua, pink and yellow stones matching the three silks. " + PRISM +
  " Each folded saree is about 4cm thick, five times the bracelet's width. COPY SPACE: the upper left third is calm, empty ivory plaster for a headline. "
  "LIGHT: soft window light from the left, one soft shadow, one small hard kicker giving every stone a white catchlight. " + END),
]
Q = []
for key, k, scene, scale, space, *extra in F:
    Q.append({"key": key, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": P(k, scene, scale, space, *(extra or [""])),
              "medias": [{"value": A[f"{k}_H"], "role": "image_references"}, {"value": R[S[k]["ref"]], "role": "image_references"}]}})
for key, p in PF:
    Q.append({"key": key, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": "4:5", "prompt": p,
              "medias": [{"value": "d7b3663a-9f07-4fc9-b8ca-d1c0110edcaa", "role": "image_references"}, {"value": "e7ef630a-57fb-47f7-8a6e-24b056372a66", "role": "image_references"}]}})
json.dump(Q, open("queue.json", "w"), ensure_ascii=False, indent=0)
print(len(Q)); print(Q[0]["params"]["prompt"]); print([m["value"][:8] for m in Q[0]["params"]["medias"]])
