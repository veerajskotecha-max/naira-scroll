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

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "over_r1.json"
    json.dump(R, open(out, "w"), indent=1, ensure_ascii=False); print(out, sorted(R))
