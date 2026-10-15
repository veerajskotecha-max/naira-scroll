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

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "over_r1.json"
    json.dump(R, open(out, "w"), indent=1, ensure_ascii=False); print(out, sorted(R))
