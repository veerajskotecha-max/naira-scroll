# Toggle 15: shared prompt blocks for the Toggle Link Chain (YF5143), six-block structure from the Naira image skill
# (shot, fidelity lock, scale, scene, light + grade, negatives). Per-shot text lives in shots.json; build(shot) joins them.
#
# References (Higgsfield media, uploaded 11 Oct 2026 for docs/creative/toggle-link):
#   still = listing-1-cube.jpg (the real necklace on a plaster cube), worn = listing-0-onbody.jpg (real, worn),
#   clasp = ref-clasp.jpg (enlarged crop of the real clasp from the worn photo).
#
# Lessons carried in from earlier Toggle shoots (concept-camps rounds 1-4, colour camps) and the 4 Nov pilot T01:
#  - The model draws the clasp right only when every part is named as a separate part: the ring's gate and collars, the
#    push-pin nub, the jump ring on each chain end, and where the bar hangs from.
#  - Left alone it makes the bar long, gives it ball ends, or leaves its end bare; it hooks the ring-side chain straight
#    round the ring's tube; and it draws the pave bar two stones wide (pilot T01). The lock forbids each one by name.
#  - It enlarges the clasp against the body (pilot T01 read about 1.5x large against the neck), so every shot gives the
#    ring a referent it must match: a fingertip, a fingernail, a paperclip, a key ring.
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA = {"still": "d7ae5d59-e64c-42e0-869a-e2cde802e598", "worn": "17737c3a-c099-48b7-8537-ca037486a406",
         "clasp": "905b250a-9517-4d23-b82b-151cc7d16cc4"}

FID = ("Preserve the necklace from reference 1 exactly, with its clasp built exactly as in reference 2: a 4mm wide polished "
 "gold chain of open elongated paperclip links; it closes with one thick, chunky, polished round gold spring-gate ring about "
 "15mm across: a heavy round tube that stops in two flat-cut collared ends at the top, bridged by a noticeably slimmer gate "
 "wire, with a small ball push-pin nub on a grooved collar at about three o'clock; the right-hand strand's last paperclip link "
 "joins the ring through a small round jump ring beside the gate, never looping directly around the ring's tube; and a short "
 "slim straight gold bar about 9mm long with flat ends, no wider than one tiny stone, set along its length with a single "
 "line of about eight tiny clear pave stones in one row, hanging from a small round jump ring on the last link of the "
 "left-hand strand and lying diagonally across the upper left of the ring exactly as in reference 2; warm 18k gold tone. "
 "Do not redesign, restyle, resize or add anything: the links stay open elongated paperclip links, never cable, curb or "
 "rope; the ring stays a spring-gate sailor ring with its slimmer gate and push-pin nub, never a plain closed donut; the bar "
 "stays short, about 0.6 times the ring's width, one stone wide, never two rows, with flat ends, no ball ends, no hook, no "
 "loop and nothing hanging under it; the only stones are on that bar; nothing hangs from the ring, no pendant, no charm; it "
 "is one single continuous necklace.")

FID_OPEN = FID.replace("lying diagonally across the upper left of the ring exactly as in reference 2",
                       "free of the ring, the necklace lying open with the ring at one end and the bar at the other")

SIZE = ("CRITICAL SCALE: this is a fine everyday necklace, 50cm long; each paperclip link is about 4mm wide and 11mm long, the "
 "length of a grain of basmati rice; the round ring is about 15mm across, no wider than a fingertip, the size of a fingernail")

LIGHT_SOFT = ("LIGHT: soft warm window light from the left shapes everything gently; one small hard specular kicker from the "
 "right draws a crisp bright line along the gold and puts a single pin-point white catchlight in each tiny clear stone; the "
 "clear stones stay completely colourless, never amber.")

GRADE = ("Palette: warm-neutral 18k gold, never brassy, orange or greenish. Natural film grain, believable imperfection, "
 "nothing clean or perfect; editorial demi-fine jewellery campaign quality.")

NEG = ("No text, no letters, no numbers, no logos, no watermarks, no other jewellery, no earrings, no rings, no bracelets, no "
 "second necklace.")

NEG_FACE = "No face: no eyes, no nose, no lips, no mouth, no chin, no jawline in frame."


def build(s):
    fid = FID_OPEN if s.get("open") else FID
    parts = [s["shot"], fid, SIZE + "; " + s["scale"], "SCENE: " + s["scene"], s.get("light", LIGHT_SOFT),
             s.get("optics", ""), s.get("grade", GRADE), NEG, NEG_FACE if s.get("body") else "", s.get("neg", "")]
    return " ".join(p.strip() for p in parts if p.strip())


def request(s):
    refs = [MEDIA[s.get("ref", "still")], MEDIA["clasp"]] + [m for m in s.get("extra_refs", [])]
    return {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": s.get("aspect", "9:16"), "prompt": build(s),
            "medias": [{"value": v, "role": "image_references"} for v in refs]}


if __name__ == "__main__":
    shots = json.load(open(os.path.join(HERE, "shots.json")))["shots"]
    want = set(sys.argv[1:])
    for s in shots:
        if not want or s["id"] in want:
            print(json.dumps({"id": s["id"], "params": request(s)}, ensure_ascii=False))
