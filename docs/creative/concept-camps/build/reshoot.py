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

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "over_r1.json"
    json.dump(R, open(out, "w"), indent=1, ensure_ascii=False); print(out, sorted(R))
