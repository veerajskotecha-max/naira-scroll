# Reshoot prompts: each is the frame's original prompt with targeted replacements taken from the verifier's fix.
# Writes over_<round>.json {frame id: prompt}; queue.py reads it as overrides.
import json, sys
D = json.load(open("frames.json")); idx = {f["id"]: f["prompt"] for f in D["frames"]}
R = {}
def fix(fid, pairs, extra=""):
    p = idx[fid]
    for a, b in pairs:
        assert a in p, (fid, a[:60]); p = p.replace(a, b)
    R[fid] = (p + (" " + extra if extra else "")).strip()

# ---- round 1 (woven) ------------------------------------------------------------------------------------------------
fix("W03", [
  ("One earring is slipped over a small wooden spool of blush silk thread standing upright, the spool about 3cm tall with a barrel about 12mm wide that passes snugly through the hoop's opening, so the earring rings the spool like a collar halfway down;",
   "One earring is clipped around a slim wooden thread bobbin of blush silk thread standing upright, the bobbin about 3cm tall with a barrel about 10mm wide and end flanges barely wider than the barrel, so the hoop, opened at its hinge and closed again, rings the bobbin like a collar halfway down;"),
  ("on warm ivory handloom linen; calm, empty blush background in the upper left",
   "on pale blush-pink handloom linen, clearly pink, never oatmeal, natural, undyed, sand or tan; a calm, empty dusty-rose wall in the upper left"),
  ("Palette: warm ivory linen, blush and peach silk thread, pale honey wood;", "Palette: blush linen, dusty rose, peach silk thread, pale honey wood;")],
  "The shadows stay blush, never tan; the gold hoops are the brightest thing in the frame.")
fix("W04", [
  ("soft blush hand-dyed cotton rope about 8mm thick, hand-woven in a tight diagonal lattice with small diamond gaps about 2cm across,",
   "single soft blush hand-dyed cotton ropes, each one rope about 8mm thick, as thick as a pencil, never bundles of thin cords, hand-woven over and under in a diagonal lattice with small diamond gaps about 2cm across,"),
  ("the rope is a little thicker than the braid of the hoop, and each earring spans about three rope widths. Only about 25cm of the woven top is in frame.",
   "each rope is visibly about one and a half times thicker than the braid of the hoop; each earring spans only about three rope widths, and its 13mm opening is narrower than two ropes side by side. Only about 15cm of the woven top is in frame, so the earrings stay small.")])
fix("W05", [
  ("hundreds of fine ivory cotton warp threads run straight up the frame, each finer than a hair, glowing softly in warm side light,",
   "hundreds of fine pale blush-pink cotton warp threads run straight up the frame, each finer than a hair, in soft, cool-warm daylight in front of a softly blurred blush plaster wall, never golden, honey, beige or tan,"),
  ("Low warm sun from the left;", "Soft daylight from the left, not golden;")],
  "Behind the earrings the warp and wall stay blush and slightly deeper than the gold, so the hoops are the brightest, most saturated thing in the frame.")

# ---- round 2 (woven) ------------------------------------------------------------------------------------------------
BEHIND = ("the camera is directly behind her, the head turned about 150 degrees away from the camera, so her whole face, profile, "
          "brow, eyelashes, cheekbone, cheek and jaw are hidden behind her own head and neck; we see only the back of her head, her hair, "
          "the back of her right ear, her nape and neck; beyond the hoop on the right there is only hair, neck and soft blush wall, with "
          "clear air between the hoop and the edge of the frame")
fix("W06", [
  ("photographed from behind: the back of the head and one long, thick, glossy dark braid falling down the back, finished at its end with a blush silk paranda tassel, the head turned well away from the camera; the ear sits in the upper right third and the right edge of the frame falls just in front of the ear at the jaw hinge, so no cheek, cheekbone, temple, eyebrow, eyelash, eye, nose, lips or mouth appears anywhere, not even at the edge;",
   "photographed from behind: the back of the head and one long, thick, glossy dark braid falling down the back, finished at its end with a blush silk paranda tassel; " + BEHIND + "; the ear and hoop sit in the right-centre third of the frame, so no cheek, cheekbone, temple, eyebrow, eyelash, eye, nose, lips, jaw or mouth appears anywhere, not even at the edge;"),
  ("Shallow depth of field, the earring in crisp focus.", "The hoop hangs turned slightly to three-quarters so the flat disc under the latch reads as a round, bright, mirror-polished gold disc. Shallow depth of field, the earring in crisp focus.")])
fix("W09", [
  ("photographed from behind the shoulder: the back of the head, the nape and dark hair gathered in a neat low bun fill most of the frame, the head turned well away from the camera; the ear sits in the right third of the frame and the right edge of the frame falls just in front of the ear at the jaw hinge, so no cheek, cheekbone, temple, eyebrow, eyelash, eye, nose, lips or mouth appears anywhere, not even at the edge;",
   "photographed from behind: the back of the head, the nape and dark hair gathered in a neat low bun fill most of the frame; " + BEHIND + "; the ear and hoop sit in the right-centre third of the frame, the hoop hanging over the neck, so no cheek, cheekbone, temple, eyebrow, eyelash, eye, nose, lips, jaw or mouth appears anywhere, not even at the edge;")])
fix("W07", [
  ("The pair of earrings rests on loosely twisted skeins of silk embroidery floss in blush, peach and warm ivory,",
   "The pair of earrings rests on loosely twisted skeins of silk embroidery floss in blush, dusty rose and pale ivory pastels, never apricot or terracotta, on blush silk,"),
  ("SCENE: the earrings fill the lower two thirds; calm soft blush floss falls out of focus above.",
   "The front hoop is turned about 35 degrees so the flat round disc under its latch faces the camera and catches the hard kicker, reading as bright mirror-polished pale gold, exactly like the braid's highlights. SCENE: the earrings fill the lower two thirds; the top quarter is calm, soft blush blur for a headline; no oatmeal or grey anywhere.")])
fix("W10", [
  ("The pair of earrings sits in the half-open drawer of a small plain blush-pink jewellery box about 8cm square, completely plain with no lettering, no logo, no print and no foil, lined with blush silk; beside the box lie a small wooden spool of blush silk thread and one dried pink rosebud, on pooled blush silk. The box is about three earrings wide.",
   "The pair of earrings sits in the half-open drawer of a small plain blush-pink jewellery box about 8cm square, completely plain with no lettering, no logo, no print and no foil, lined with blush silk; the drawer is fully three hoops wide, each hoop only about a third of the drawer's width; outside the box, on the silk beside it, lie a small wooden spool of blush silk thread about 3cm long, a little longer than a hoop, and one dried pink rosebud. Far behind, softly out of focus, glows one small warm diya flame for Diwali."),
  ("the upper left is calm, empty, softly glowing blush, for a headline.", "the upper left is calm, empty, softly glowing blush, never ivory, for a headline.")])

# ---- round 3 (toggle) -----------------------------------------------------------------------------------------------
CLASP_OLD = ("and a short slim straight gold bar about 9mm long with flat ends, set along its whole length with a single row of tiny clear pave stones, "
             "the bar joined to the other end of the chain by a small jump ring and threaded through the ring; warm 18k gold tone.")
CLASP_NEW = ("and a short slim straight gold bar about 9mm long with flat ends, set with ONE single row of about nine tiny clear stones. The two "
             "chain ends stay separate: one end joins the ring by a small smooth round jump ring around the ring's tube right beside the gate; the "
             "other end ends in a small smooth round jump ring through the end of the bar. The bar is short, about 0.6 of the ring's outer width, "
             "and when the clasp is closed it lies diagonally across the front of the ring's upper left with its free end over the opening, never "
             "hanging below the ring and never in line with the chain. No textured, granulated or lumpy connectors anywhere; warm 18k gold tone. "
             "The necklace is 50cm long, about 45 paperclip links in all.")
def tfix(fid, pairs, extra=""):
    fix(fid, [(CLASP_OLD, CLASP_NEW)] + pairs, extra)
SW_OLD = "falls in a long soft loop about 22cm deep, both strands hanging straight under their own small weight,"
SW_NEW = "falls in one long soft loop about 24cm deep, four switch-widths below the lever, about 22 links down each side, both strands hanging straight under their own small weight,"
tfix("T01", [(SW_OLD, SW_NEW),
  ("with only the faint long shadow of a dried palm frond, for a headline.", "with only the faint long shadow of a dried palm frond, the frond itself out of frame, for a headline.")])
tfix("T02", [(SW_OLD, SW_NEW),
  ("with only the faint long shadow of a dried palm frond, for a headline,", "with only the faint long shadow of a dried palm frond, the frond itself out of frame, for a headline,")],
  "The ring is about a quarter of the switch's width.")
tfix("T04", [
  ("with a few small round dark iron studs, each about 2cm across.", "with a few round dark iron studs, each stud head about 2cm across."),
  ("and falls in a soft loop about 20cm deep, and the closed toggle clasp hangs at the bottom of the loop at the front, the 15mm ring about the same size as one of the door's iron stud heads;",
   "and falls in one soft loop about 24cm deep, about twelve stud-widths below the staple, with about 22 links down each side, and the closed toggle clasp hangs at the bottom of the loop at the front; the 15mm ring is clearly smaller than a stud head, about three-quarters of its width, and each paperclip link is about half a stud long;"),
  ("Only about 40cm of the door's height is in frame, so the necklace reads clearly.", "About 55cm of the door's height is in frame, so the whole loop sits in the middle of the frame.")])
tfix("T05", [
  ("the chain sits around the vase's neck and its long loop drapes down over the shoulders and rests against the round belly of the vase, and the closed toggle clasp sits at the front centre, like a clasp turned to the front on a collarbone.",
   "one single strand goes once around the vase's neck; both sides fall over the shoulders and meet in ONE long loop resting on the belly, the closed toggle at the front centre like a clasp turned to the front on a collarbone; only one strand of chain anywhere in the frame, never doubled, never wrapped twice, never layered.")])

# ---- round 4 (heart) ------------------------------------------------------------------------------------------------
HEART_OLD = "the puffed heart is about 15mm, the size of a fingernail, clearly bigger than two beads side by side, about two and a half beads wide;"
HEART_NEW = "the puffed heart is about twice a bead's width, about one fingernail wide;"
WRIST_OLD = "CRITICAL SCALE: each bead is about half the width of a fingernail and the gold heart about one fingernail wide; the bracelet is a slim strand on the wrist, never chunky."
WRIST_NEW = ("CRITICAL SCALE: a fine, delicate strand: each bead about half the width of her fingernail and about one tenth of the width of "
             "her wrist; the gold heart about one fingernail wide, about twice a bead's width and about one fifth of the wrist's width; about "
             "ten beads plus the clasp show across the front of the wrist; an average adult wrist with naturally proportioned fingers; never "
             "chunky, never bold.")
fix("H05", [(WRIST_OLD, WRIST_NEW), ("palm facing the camera, four fingers together", "palm turned toward the camera, four fingers together")])
fix("H10", [
  ("A small bundle of four plain blush gift-card envelopes with soft deckled edges, each about 6cm by 9cm, completely blank with no writing, no stamps and no printing, is held together by the bracelet wrapped once around its short side like a ribbon, the gold toggle closed on top and the puffed gold heart hanging over the front edge; one dried pink rosebud lies beside it.",
   "A small bundle of four plain blush gift envelopes, each about 6cm by 9cm with a visible pointed flap and soft deckled edges, completely blank with no writing, no stamps and no printing, is tied with the bracelet wrapped once around the bundle's short side like a ribbon, passing under the bundle and back over the top, the gold toggle closed on top and the puffed gold heart hanging over the front edge; one dried pink rosebud lies beside it."),
  ("the bundle lies at a slight angle in the lower right on warm ivory handmade paper with visible fibres; the upper left is calm and empty, for a headline.",
   "the bundle lies at a slight angle in the lower right on pale blush handmade paper with visible fibres, pale ivory-pink, never cream, beige, sand or tan, in front of a soft blush plaster wall; the upper left is calm and empty, for a headline."),
  (HEART_OLD, HEART_NEW)])

# ---- round 5 (woven worn frames: new framings that keep the face out by construction) ------------------------------------
W6_OLD = idx["W06"].split(" Preserve the earrings from reference 1 exactly")[0]
W6_NEW = ("Editorial on-model advertising photograph, 4:5 frame, photographed from directly behind her, perfectly centred on the back of her head: "
          "sleek dark hair parted in the middle and woven into one long, thick, glossy braid that falls straight down the centre of her back, "
          "finished with a blush silk paranda tassel; both ears show symmetrically at the left and right edges of her head, seen from behind, "
          "and each earlobe wears one of the pair of hoops; because the camera is straight behind her, her face is completely hidden by her own "
          "head: no cheek, cheekbone, jaw, eyelash, eyebrow, nose or lips anywhere in the frame, only hair, the backs of the ears, the nape, the "
          "neck, the shoulders and soft blush wall on both sides; a young Indian woman with fair light skin with warm golden undertones, natural "
          "unretouched texture with visible pores and fine downy hair at the nape; she wears a plain warm ivory cotton kurta.")
fix("W06", [(W6_OLD, W6_NEW), ("Shallow depth of field, the earring in crisp focus.", "Shallow depth of field, both hoops in crisp focus.")])
W9_OLD = idx["W09"].split(" Preserve the earrings from reference 1 exactly")[0]
W9_NEW = ("Editorial on-model advertising photograph, 4:5 frame, a close crop of her right ear seen from slightly behind: her long loose dark "
          "hair is tucked behind this ear above it, and a soft curtain of the same loose hair falls forward in front of the ear, completely "
          "covering her cheek, jaw and the whole of her face, so only hair is visible on the face side; in frame are the ear, the earlobe "
          "wearing one hoop, the hairline, a little of the neck, and a bare shoulder above the plain wide neckline of an ivory cotton top; no "
          "cheek, cheekbone, jaw, eyelash, eyebrow, nose or lips anywhere, not even at the edge; a young Indian woman with light wheatish skin "
          "with warm honey undertones, natural unretouched texture with visible pores and fine downy hair.")
fix("W09", [(W9_OLD, W9_NEW)])

# ---- round 6 (heart + toggle) -----------------------------------------------------------------------------------------
GRID_OLD = "Every bead touches the next, bending only at its fine links; each bead spans just over one bold 5mm square of the grid."
GRID_NEW = ("Every bead touches the next, bending only at its fine links. Scale against the grid: each bold 5mm square holds exactly 5 by 5 "
            "small 1mm squares; each 6mm bead spans six small squares, a little more than one bold square; the puffed heart is about two "
            "and a half bold squares wide; the T-bar is about four bold squares long; laid open, the whole strand runs about 36 bold squares. "
            "The paper is blank grid with no printed trace at all: the bracelet is the only line on it.")
fix("H02", [(GRID_OLD, GRID_NEW), (HEART_OLD, HEART_NEW)])
fix("H03", [
  ("the bracelet is unfastened and laid along one stave like a melody: the silver beads rise and fall gently across the five lines like a run of notes, and at the end, a little apart on the stave, the gold toggle ring with the puffed gold heart sits like one gold note. Each stave is about 8mm tall, so each 6mm bead covers most of its height.",
   "the bracelet is ONE single strand with exactly two ends, unfastened: the straight gold T-bar on one end and the gold ring with the heart on the other, fine silver links between the beads, no loose wire ends, never two strands; it is laid in one gentle wave along a single stave like a melody, the silver beads rising and falling across the five lines like a run of notes, and at the end, a little apart on the stave, the gold toggle ring with the puffed gold heart sits like one gold note. Each stave is about 8mm tall: each 6mm bead covers about three quarters of a stave's height, and the heart is about one and a half staves tall."),
  ("A sheet of aged cream music manuscript paper", "A sheet of pale blush-tinted music manuscript paper"),
  (HEART_OLD, HEART_NEW)])
fix("H04", [
  ("on the pale cream goatskin head of a dholak, an Indian barrel drum, the drum head about 18cm across, three bracelet-widths wide, its natural texture and faint mottling visible;",
   "on the pale ivory goatskin head of a dholak, an Indian barrel drum, the drum head about 18cm across, three bracelet-widths wide, clean, with only faint natural mottling and no brown stains;"),
  ("SCENE: the drum fills the lower right two thirds, cropped by the frame; the upper left is calm, softly out-of-focus blush wall, for a headline.",
   "The toggle is fastened: the T-bar's centre loop passes through the ring. SCENE: the camera is close, so the bracelet's loop fills about 40% of the frame's width; the drum fills the lower right two thirds, cropped by the frame; the upper left is a calm, light, clean blush plaster wall, softly out of focus, never taupe or muddy, for a headline. A pale reflector makes every bead mirror bright light."),
  (HEART_OLD, HEART_NEW)])
fix("H06", [
  ("a chest crop: the top edge of the frame sits across the collarbones, so absolutely no chin, jaw, lips, mouth or any part of the face is anywhere in the frame;",
   "a chest crop: the top edge of the frame sits across the sweater's round neckline, about 3cm below the collarbones, so the neck, chin, jaw, lips and the whole face are far above and outside the frame;"),
  (WRIST_OLD, "CRITICAL SCALE: a fine, delicate strand: each bead a little over half the width of her fingernail; the heart about one and a half fingernails wide; never chunky."),
  ("the gold toggle on top and the gold heart resting against the knit.", "the gold toggle on top, fastened, the T-bar's centre loop passing through the ring, and the gold heart resting against the knit.")])
fix("H07", [
  ("the hand is relaxed at the bottom of the frame, fingers gently curled,", "the hand is relaxed, its gently curled fingers leaving the frame at the lower left,"),
  ("so the puffed gold heart rests exactly on the pulse point;", "so the puffed gold heart rests exactly on the pulse point, a little toward the thumb side;"),
  ("The wrist sits in the middle third; the top third is calm blush silk softly out of focus, for a headline.",
   "The wrist sits in the middle third; the top third is empty blush silk softly out of focus, with no hand or fingers in it, for a headline. A pale reflector makes every bead mirror bright light so they read bright silver.")])
NECK_OLD = "the top edge of the frame sits across the middle of the neck, well below the jaw, the head tilted slightly up and away so that absolutely no chin, jaw, lips, mouth or any part of the face is anywhere in the frame;"
fix("T08", [(CLASP_OLD, CLASP_NEW), (NECK_OLD,
   "the top edge of the frame is only about 5cm above the collarbones, while the chin is about 10cm above them, so the chin, jaw, lips and the whole face are far above and outside the frame, the head tilted up and away;"),
  ("CRITICAL SCALE: this is a fine 4mm chain, about as wide as a grain of rice, and the round ring is about one and a half fingernails wide on the body, small and delicate at the base of the throat; never a statement chain, never chunky.",
   "CRITICAL SCALE: a fine 4mm chain; the 15mm ring is about one sixth of the width of her neck and only about one and a half times the length of one 11mm link, small and delicate at the base of the throat; never a statement ring, never chunky.")])
T9_OLD = idx["T09"].split(" Preserve the necklace from reference 1 exactly")[0]
T9_NEW = ("Editorial on-model advertising photograph, vertical 9:16 frame, in low warm evening sun: the bare right shoulder, collarbone and "
          "the side of the neck of a young Indian woman with warm deep brown skin with a soft golden glow, natural unretouched texture with "
          "fine pores, wearing a peach silk slip dress with fine straps; she stands in the lower right of the frame, turned three-quarters "
          "away, and her neck rises out of the frame's top-right corner, so her head, chin, jaw, lips and ears are entirely outside the frame; "
          "the necklace lies on her collarbones with the clasp turned to the side so it rests on the right collarbone, facing the camera, "
          "large and clear in the frame, catching the sun; the upper left forty percent of the frame is calm, softly out-of-focus warm blush "
          "wall for a headline, with no hair crossing it.")
fix("T09", [(CLASP_OLD, CLASP_NEW), (T9_OLD, T9_NEW),
  ("The figure fills the lower sixty percent of the frame; the upper forty percent is a calm, softly out-of-focus warm blush wall for a headline, with no face and no hair crossing it.",
   "The clasp shows clean flat-cut collars, a slim gate wire and one row of separate tiny stones.")])

# ---- round 7 (prism: whole-bracelet views drew too few, too-big stones) --------------------------------------------------
P_SCALE_W_OLD = "CRITICAL SCALE: each stone is only about half the width of a fingernail; the bracelet is a slim line of stones on the wrist, never chunky."
P_SCALE_W_NEW = ("CRITICAL SCALE: each stone is only about half the width of a fingernail and about a third of a fingertip; the wrist is about "
                 "seven stone-units wide; a slim 8mm line of about twenty small stones, never chunky.")
fix("P02", [
  ("the bracelet is laid open and perfectly straight down through all three bands at a right angle, vertically, like a ruled line through the colour; the top fifth of the frame is bare ivory floor above the bands, for a headline",
   "the bracelet runs perfectly straight down the frame a little right of centre, crossing all three bands at a right angle like a ruled line through the colour, entering at the top edge of the frame and leaving at the bottom edge, so neither end nor the clasp is in the frame; the left half of the top fifth is bare ivory floor, for a headline")])
fix("P03", [
  ("is heaped with mukhwas, sugar-coated fennel seeds in pastel aqua, pink, pale yellow and white, each seed about 5mm long, the same size as one of the stones;",
   "holds a low, loose layer of mukhwas, slim sugar-coated fennel seeds in pastel aqua, pink, pale yellow and white, each seed about 5mm long and 1.5mm thick, fewer and slimmer than the stones;"),
  ("the bracelet lies in a loose curl on top of the seeds and spills over the rim, its stones echoing the sugar colours; a few seeds are scattered on blush linen beside the bowl.",
   "the bracelet lies in a loose curl on top of the seeds and spills over the rim, its stones and bright silver the brightest things in the frame; a few seeds are scattered on pale blush linen beside the bowl."),
  ("the upper left is calm, softly out-of-focus blush, for a headline.", "the upper left is calm, light, softly out-of-focus pale blush with no brown shadow, high-key, for a headline.")])
fix("P04", [
  ("The bracelet is closed and rests around the neck of the aqua bottle, slipped down to where the neck widens into the shoulder, the loop tilted at a slight angle like a bangle resting on a bottle, the stones facing the camera; the loop is about 6cm across, a little wider than the aqua bottle's shoulder there.",
   "The bracelet is a slim 18cm bracelet of about twenty small stones, closed, resting around the neck of the narrow-shouldered aqua bottle, slipped down to where the neck widens, the loop tilted at a slight angle like a bangle resting on a bottle, loose and delicate, the stones facing the camera; the loop is about 6cm across, so about seven or eight stone units span the loop's width; each stone the size of a peppercorn."),
  ("the upper third is calm warm ivory plaster wall, for a headline.", "the upper third is a calm pale ivory-blush plaster wall, never tan or beige, for a headline.")])
fix("P05", [
  ("Nine unbranded hexagonal wooden colour pencils with pastel lacquer, three aqua, three soft pink and three pale butter yellow, each about 7mm thick, lie side by side touching, sharpened tips all pointing up, on warm ivory cold-press paper, with a few curled pencil shavings; the bracelet is laid open and perfectly straight across the middle of the pencils at a right angle, each stone a little narrower than a pencil.",
   "Eighteen unbranded hexagonal wooden colour pencils with pastel lacquer in repeating aqua, soft pink and pale butter yellow, each about 7mm thick, lie side by side touching across the whole width of the frame, sharpened tips all pointing up, on pale ivory cold-press paper, with a few curled pencil shavings; the bracelet is laid perfectly straight across all of them at a right angle and runs off both side edges of the frame, so neither end shows; each stone is about two-thirds the width of one pencil and each stone in its halo about one pencil wide, so the line crosses about one stone per pencil; the stones repeat aqua, pink, yellow, never two of the same colour side by side.")])
fix("P06", [
  ("the bracelet lies open and perfectly straight inside that band of coloured light, its stones glowing.",
   "the bracelet lies perfectly straight inside that band of coloured light, running along it and out of the frame's left and lower edges, so neither end shows, its stones glowing; the prism is about seven stone-units long."),
  ("the low sun passing through it lays a soft pastel spectrum", "soft low sun passing through it lays a soft pastel spectrum")])
fix("P07", [(P_SCALE_W_OLD, P_SCALE_W_NEW),
  ("a torso crop from the shoulders to the waist: the top edge of the frame sits below the collarbones,",
   "a closer crop of the forearm and hand resting across the waist of a plain white cotton t-shirt: the top edge of the frame sits at the middle of the chest, far below the collarbones,")])
fix("P08", [(P_SCALE_W_OLD, P_SCALE_W_NEW)])
fix("P10", [
  ("the bracelet is laid open and perfectly straight exactly along the stroke, as if it painted it.",
   "the bracelet is laid perfectly straight exactly along the stroke, as if it painted it, and runs off both side edges of the paper and the frame, so neither end shows; each stone in its halo is about the width of the brush's metal ferrule.")])

# ---- round 8 (woven scale: draw the cords the model draws, and give the cane a real 1cm opening) ---------------------------
def refix(fid, pairs, extra=""):
    # like fix(), but starts from this frame's latest reshoot prompt instead of its original
    p = R[fid]
    for a, b in pairs:
        assert a in p, (fid, a[:60]); p = p.replace(a, b)
    R[fid] = (p + (" " + extra if extra else "")).strip()
refix("W04", [
  ("single soft blush hand-dyed cotton ropes, each one rope about 8mm thick, as thick as a pencil, never bundles of thin cords, hand-woven over and under in a diagonal lattice with small diamond gaps about 2cm across,",
   "soft blush hand-dyed cotton cords, each cord about 3mm thick, laid three side by side in flat bands about 9mm wide, hand-woven over and under in a diagonal lattice with small diamond gaps about 2cm across,"),
  ("each rope is visibly about one and a half times thicker than the braid of the hoop; each earring spans only about three rope widths, and its 13mm opening is narrower than two ropes side by side.",
   "each cord is a little thinner than the braid of the hoop; each earring spans about eight cords, about three bands of the weave, and its 13mm opening is about one and a half bands wide."),
  ("the upper left is calm, sunlit weave falling softly out of focus, for a headline.",
   "the upper left is calm blush weave falling softly out of focus, rosy, never beige or tan, for a headline."),
  ("Palette: warm ivory linen, blush and peach silk thread, pale honey wood;", "Palette: blush and dusty-rose cotton cord, soft peach, warm ivory light;")],
  "The braid's end cap at the hinge stays matte and finely stippled, never a second polished disc; each hoop has exactly one polished flat disc, under the latch; each latch wire is a smooth gentle arc.")
fix("W08", [
  ("a close crop of the back of a honey-wood bentwood chair with Viennese cane webbing: hand-woven pale natural cane strands forming the classic open octagon pattern, each octagonal hole about 1cm across.",
   "a close crop of the back of a bentwood chair painted soft blush, with Viennese cane webbing in pale bleached ivory cane: hand-woven cane strands about 2mm wide forming the classic open octagon pattern, each octagonal opening about 1cm across, only a little smaller than the hoop's 13mm centre hole."),
  ("The pair of earrings is hooked through the cane webbing by their thin latch wires, one a little above the other, each earring about two and a half octagon holes wide: pattern on pattern.",
   "The pair of earrings hangs from the cane webbing, each thin latch wire threaded behind one cane strand so the hoop visibly hangs from it, one a little above the other; each earring spans only about one and a half octagons of the pattern; the cane strands are visibly about three times wider than one wire of the hoop's braid; the blush bentwood frame bar at the edge of the frame is about as wide as a whole hoop: pattern on pattern."),
  ("Low warm sun from behind the chair throws the octagon pattern as a sharp soft-edged shadow onto a blush plaster wall behind.",
   "Low warm sun from behind the chair throws the octagon pattern as a soft-edged shadow onto a sunlit blush plaster wall behind, which stays light, never deep brown shade."),
  ("SCENE: only about 30cm of the chair back is in frame;", "SCENE: only about 12cm of the chair back is in frame;"),
  ("Palette: warm ivory linen, blush and peach silk thread, pale honey wood;", "Palette: blush, warm ivory, dusty rose, a breath of peach; bleached ivory cane, never honey, straw or tan;")])

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "over_r1.json"
    json.dump(R, open(out, "w"), indent=1, ensure_ascii=False); print(out, sorted(R))
