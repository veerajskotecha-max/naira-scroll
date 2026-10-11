# Toggle Link Chain (YF5143) campaign "The Turn": 20 ad photographs.
# Six-block prompts from the Naira image skill: shot, fidelity lock, scale, scene, light + grade, negatives.
# Reference 1 = listing photo (still lifes: the plaster-cube photo; worn: the on-body photo cropped below the chin).
# Reference 2 = the clasp, cropped from the on-body listing photo. Same piece, so one product per frame still holds.
import json, sys

FID = ("Preserve the necklace from reference 1 exactly, with its clasp built exactly as in reference 2: a 4mm wide polished gold "
 "chain of open elongated paperclip links; it closes with one thick, chunky, polished round gold spring-gate ring about 15mm "
 "across: a heavy round tube that stops in two flat-cut ends at the top, bridged by a noticeably slimmer gate wire taking up "
 "about one sixth of the circle, with a small ball push-pin nub on a grooved collar a quarter turn from the gate; and a short "
 "slim straight gold bar about 9mm long with flat ends, set along its whole length with a single row of tiny clear pave stones, "
 "the bar joined to the other end of the chain by a small jump ring and threaded through the ring; warm 18k gold tone. Do not "
 "redesign, restyle, resize or add anything; the links must stay open elongated paperclip links, never cable, never curb, never "
 "rope; the ring must stay a spring-gate sailor ring with its slimmer gate and push-pin nub, never a plain closed donut ring; the "
 "bar stays short, about 0.6 times the ring's width, with no hook, no loop, no shackle and no clip under it, never a plain T-bar, "
 "never a bar with ball ends, never a lobster clasp; the only stones are on that bar; nothing hangs from the ring, no pendant, "
 "no charm. Only the background, surface and lighting change.")

SIZE = ("CRITICAL SCALE: this is a fine everyday necklace, 50cm long; each paperclip link is about 4mm wide and 11mm long, the "
 "length of a grain of basmati rice, and the round ring is about 15mm across, the size of a fingernail")

LIGHT = ("LIGHT: low warm late-afternoon sun from a window at the left, softened by a muslin curtain, shapes everything gently; "
 "one small hard specular kicker from behind right draws a crisp bright edge along the gold and puts a single small pure-white "
 "catchlight in each tiny clear stone; the clear stones stay completely colourless, never amber.")

GRADE = ("Palette: blush, warm ivory, dusty rose, a breath of peach; warm-neutral 18k gold, never brassy, orange or greenish. "
 "Natural film grain, believable imperfection, nothing clean or perfect. Calm handcrafted slow-luxury mood, the long quiet of an "
 "Indian afternoon, editorial demi-fine jewellery campaign quality.")

NEG = ("No text, no letters, no logos, no watermarks, no other jewellery, no second necklace. Absolutely never sand, tan, beige, "
 "grey, white or golden backgrounds, never black velvet, never a white seamless backdrop.")

MACRO = ("Honest macro optics: depth of field only a few millimetres deep, so the clasp is needle-sharp and everything even "
 "slightly further away falls immediately and softly out of focus.")

CONTACT = "A dark believable contact shadow directly beneath where the metal touches"

WORN = ("a collarbone crop from the middle of the neck down to the upper chest: the top edge of the frame sits across the middle of "
 "the neck, well below the jaw, the head tilted slightly up and away so that absolutely no chin, jaw, lips, mouth or any part of "
 "the face is anywhere in the frame; the necklace worn by a young Indian woman with {skin}, natural unretouched texture with "
 "visible pores and fine downy hair")
WSCALE = ("CRITICAL SCALE: this is a fine 4mm chain, about as wide as a grain of rice, and the round ring is about one and a half "
 "fingernails wide on the body, small and delicate at the base of the throat; never a statement chain, never chunky")
WNEG = ("No plastic skin, no heavy retouching. No text, no logos, no watermarks, no face, no extra fingers, no additional jewellery "
 "of any kind, no earrings, no rings, no bracelets, no second necklace.")
HANDS = "five fingers, correct natural anatomy, short natural nails with a bare buffed finish"

STILL, WREF = "still", "worn"
S = []
def add(i, name, ar, ref, text):
    S.append(dict(id=f"T{i:02d}", name=name, aspect=ar, ref=ref, prompt=" ".join(text.split())))

# ---------- still lifes ----------
add(1, "Hero on blush silk", "4:5", STILL, f"""Editorial advertising still life, 4:5 frame. {FID} {SIZE}; a single fresh peach tulip lies
 along the bottom edge of the frame, softly out of focus, its flower head about 50mm long, so the ring is about a third of the tulip
 head's length. {CONTACT}; the silk is dimpled very slightly under the ring. SCENE: the necklace lies in a soft open loop on pale
 blush silk charmeuse with gentle liquid folds, the clasp closed and turned to the front in the lower right third of the frame,
 small in the frame; wide calm empty blush silk in the upper left of the frame for a headline. {LIGHT} {MACRO} {GRADE} {NEG}""")

add(2, "Story hero, plaster and palm shadow", "9:16", STILL, f"""Editorial advertising still life, vertical 9:16 frame. {FID} {SIZE}.
 SCENE: the necklace is draped over the top edge of a small hand-plastered block about 8cm wide, in warm ivory lime plaster with
 trowel marks, standing on a blush plaster ledge in front of a soft blush plaster wall; the chain falls down the front face of the
 block and the clasp hangs closed at the front, sharp and catching the light. The block and necklace sit in the lower half of the
 frame; the upper forty percent of the frame is calm empty blush wall crossed only by the soft long shadow of a dried palm frond,
 for a headline. {CONTACT} on the plaster. {LIGHT} Shallow depth of field. {GRADE} {NEG}""")

add(3, "Clasp macro on handmade paper", "4:5", STILL, f"""Extreme macro advertising photograph, 4:5 frame. {FID} Fill the lower two
 thirds of the frame with the closed clasp, the thick round spring-gate ring with its slimmer gate and push-pin nub and the short
 pave bar threaded through it, and the first few open paperclip links, resting on blush handmade cotton-rag paper with visible
 fibres and a soft deckle edge. {SIZE}; every paper fibre is far finer than the metal, and one pressed pale pink hydrangea petal,
 about 15mm across, the same size as the ring, lies softly out of focus at the upper right. {CONTACT}, the soft paper pressed into a
 shallow dent beneath the ring. {MACRO} {LIGHT} {GRADE} No hands, no models. {NEG}""")

add(4, "Waterproof droplets", "4:5", STILL, f"""Extreme macro advertising photograph, 4:5 frame. {FID} The closed clasp and a short run
 of open paperclip links rest on dusty rose silk satin, beaded with a few tiny clear water droplets: two or three droplets sit on
 the round ring and on the links, each droplet about 1 to 2mm, rounded, with a bright window highlight and a faint refracted image
 of the gold beneath it; more droplets bead on the satin around it. {SIZE}; the droplets are smaller than the width of a link. {CONTACT}.
 {MACRO} {LIGHT} Fresh, clean, quiet. Wide calm empty dusty rose satin in the upper left. {GRADE} No hands, no models, no splash,
 no puddle. {NEG}""")

add(5, "Flat lay on handmade paper", "4:5", STILL, f"""Top-down flat lay advertising photograph, 4:5 frame: the camera looks straight
 down at 90 degrees onto a flat surface, so the round ring stays a true circle and nothing recedes in perspective. {FID} {SIZE}; the
 whole necklace lies in one soft round loop about 16cm across, the clasp closed at the bottom of the loop. A single pressed pale
 pink hydrangea petal, about 15mm, the same size as the ring, lies just beside the clasp. SCENE: one large sheet of blush handmade
 cotton-rag paper with visible fibres fills the whole frame; the loop sits in the lower half, slightly off-centre; the upper half
 of the frame is calm, empty blush paper. Large soft diffused light from almost directly above, even across the frame; one small
 hard specular source gives the gold a crisp bright edge and each stone a pure-white catchlight. {CONTACT}. {GRADE} No hands, no
 models, no other props. {NEG}""")

add(6, "Flat lay with sage ribbon", "4:5", STILL, f"""Top-down flat lay advertising photograph, 4:5 frame: the camera looks straight
 down at 90 degrees, so the round ring stays a true circle. {FID} {SIZE}; the necklace lies in a loose relaxed S along the diagonal
 of the frame, the clasp closed near the lower right. SCENE: warm ivory handloom linen with a visible slubbed weave fills the whole
 frame, laid smooth; one narrow soft sage-green silk ribbon about 10mm wide, a little wider than a link is long, curls in from the
 lower left corner and stops short of the chain, never touching it. The upper left of the frame is calm empty linen. Large soft
 diffused light from almost directly above with a gentle warm cast from the left; one small hard specular source gives the gold a
 crisp bright edge. {CONTACT}; the linen weave is visible at true scale, every thread finer than a link. {GRADE} No hands, no
 models, no other props. {NEG}""")

add(7, "Jaali afternoon", "4:5", STILL, f"""Editorial advertising still life, 4:5 frame. {FID} {SIZE}. SCENE: the necklace lies in a soft
 open curve on warm ivory raw silk with visible slubs; low late-afternoon sun falls through a carved stone jaali screen just out of
 frame, laying a crisp lattice of small eight-pointed star and diamond shapes of warm light across the silk, the shapes softening
 toward the edges of the frame; the closed clasp sits exactly inside one bright star of sunlight and glows, while the rest of the
 chain runs in and out of soft blush shadow. The necklace sits in the lower right two thirds; the upper left is calm, empty silk
 with only the faint lattice. {CONTACT}. One small hard specular kicker gives the gold a crisp bright edge and each stone a pure-white
 catchlight. {MACRO} {GRADE} {NEG}""")

add(8, "Story, palm shadow on plaster", "9:16", STILL, f"""Editorial advertising still life, vertical 9:16 frame. {FID} {SIZE}.
 SCENE: the necklace lies in a long loose S curve on a smooth blush lime-plaster tabletop that fills the whole frame, the clasp closed
 in the lower third, in crisp focus; across the upper half of the frame falls the long soft-edged shadow of a single dried palm frond
 from low warm sun, its fronds fanning across calm empty blush plaster, leaving room for a headline. {CONTACT}. {LIGHT} Shallow
 depth of field, the clasp sharp and the far chain softening. {GRADE} No hands, no models, no plants in the frame, only their shadow.
 {NEG}""")

add(9, "Pooled in a blush dish", "4:5", STILL, f"""Editorial advertising still life, 4:5 frame, seen from a gentle three-quarter
 angle above. {FID} {SIZE}; it is pooled loosely in a small shallow hand-thrown ceramic dish about 9cm across with a soft blush matte
 glaze and a raw unglazed rim, so the dish is about six rings wide; the closed clasp rests over the rim of the dish, facing the
 camera, in sharp focus; two dried rose petals in dusty pink lie on the table beside the dish. SCENE: the dish stands on warm ivory
 linen in the lower right of the frame; the upper left is calm empty blush wall softly out of focus. {CONTACT}, the chain weighing
 on the dish. {LIGHT} {MACRO} {GRADE} No hands, no models. {NEG}""")

add(10, "Gift box", "4:5", STILL, f"""Editorial advertising still life, 4:5 frame, seen from a gentle angle above. {FID} {SIZE}. SCENE:
 a small plain blush-pink jewellery drawer box about 8cm square, completely plain with no lettering, no logo, no print and no foil,
 sits on pooled blush silk; its drawer is pulled half open and the necklace is coiled inside on a blush silk pad, with the closed
 clasp resting on top of the coil, facing the camera, in sharp focus; the box is about five rings wide. The box sits in the lower
 right two thirds; the upper left is calm, empty blush silk in soft folds. {CONTACT}. {LIGHT} Shallow depth of field. {GRADE} No
 ribbon, no tissue paper, no card, no hands. {NEG}""")

add(11, "The turn, clasp open", "4:5", STILL, f"""Extreme close editorial still life, 4:5 frame. Preserve the necklace from reference
 1 and its clasp parts from reference 2 exactly. The clasp is shown open: the thick polished round gold spring-gate ring about 15mm
 across, with its slimmer gate wire at the top and a small ball push-pin nub on a grooved collar, lies flat on one end of the chain;
 the short slim straight gold bar about 9mm long, with flat ends and a single row of tiny clear pave stones along its whole length,
 lies just beside the ring, a few millimetres away, still joined to the other end of the chain by its small jump ring, about to be
 turned through the ring. The two chain ends of open elongated paperclip links, 4mm wide, curve away out of focus. Do not redesign,
 restyle or resize anything; the links must stay open paperclip links, never cable or curb; the ring must never become a plain donut,
 a hoop or a lobster clasp; the bar stays short, about 0.6 times the ring's width, never a T-bar with ball ends; the only stones are on
 the bar. Only the background, surface and lighting change. The ring is the size of a fingernail. SCENE: pale blush silk charmeuse in
 soft folds; the ring and bar sit in the lower centre; wide calm silk above. {CONTACT}, the silk dimpled under the ring. {MACRO}
 {LIGHT} {GRADE} No hands, no models. {NEG}""")

add(12, "Between the fingertips", "4:5", STILL, f"""Editorial close-up advertising photograph, 4:5 frame. {FID} A young Indian woman's
 hand with fair light skin with warm ivory undertones, natural texture with visible fingerprint ridges and soft knuckle creases, {HANDS},
 lifts the necklace by holding the round ring of the closed clasp lightly between her thumb and index fingertip; the chain falls away
 below in two soft lines out of focus. {SIZE}; the ring is only a little wider than her fingertip and the bar shorter than her
 fingernail. SCENE: soft out-of-focus blush plaster wall behind; the hand enters from the lower right, the clasp sits a little right
 of centre; the upper left of the frame is calm empty blush. {LIGHT} {MACRO} {GRADE} No face, no arm above the wrist, no extra
 fingers, no rings, no bracelets, no nail polish, no nail art. {NEG}""")

# ---------- worn (no face) ----------
def worn(i, name, ar, skin, wear, scene, extra=""):
    add(i, name, ar, WREF, f"""Editorial on-model advertising photograph, {ar} frame, {WORN.format(skin=skin)}, wearing {wear}. {FID}
 {WSCALE}. {scene} {extra} Soft warm window light on the skin from the left; one small hard specular source gives the gold a crisp
 bright edge and each tiny stone a single pure-white catchlight; the stones stay colourless. Shallow depth of field, the clasp in crisp
 focus, skin falling gently soft. {GRADE} {WNEG} Never a grey, white or black background.""")

worn(13, "Worn, linen shirt", "4:5", "fair light skin with warm ivory undertones",
     "a crisp ivory linen shirt unbuttoned to an open collar",
     "The chain lies on the collarbones with the clasp turned to the front at the centre of the throat. Background: a soft out-of-focus blush plaster wall, calm empty space in the upper left of the frame.")
worn(14, "Worn, toggle at the side", "4:5", "light wheatish skin with warm honey undertones",
     "a blush silk camisole with very thin straps",
     "The clasp is turned to the side and rests just above the left collarbone, off-centre; the chain runs smoothly round the base of the neck. Background: soft out-of-focus dusty rose wall, calm empty space in the upper right.")
worn(15, "Worn over a knit", "4:5", "fair porcelain-light skin with cool rosy undertones",
     "a soft warm ivory ribbed wool sweater with a round crew neck",
     "The chain lies on top of the knit just below the neckband, the clasp at the centre front resting on the ribbed wool, the wool fibres at true scale, far finer than a link; the knit is pressed very slightly under the ring. Background: soft out-of-focus blush wall, calm space in the upper left. Cosy winter morning light, still warm.")
worn(16, "Story, warm evening", "9:16", "warm deep brown skin with a soft golden glow",
     "a peach silk slip dress with fine straps",
     "Bare shoulders and collarbones in low warm evening sun; the clasp turned to the front at the base of the throat, catching the sun. The figure fills the lower sixty percent of the frame; the upper forty percent is a calm, softly out-of-focus warm blush wall for a headline, with no face and no hair crossing it.")
add(17, "Fastening at the nape", "4:5", WREF, f"""Editorial on-model advertising photograph, 4:5 frame, photographed from behind:
 the back of a young Indian woman's neck and shoulders, fair light skin with warm golden undertones, natural unretouched texture with
 visible pores and fine downy hair at the nape, dark hair gathered up in a low soft bun at the top of the frame, the head bowed
 slightly forward and turned away so no ear lobe, cheek, jaw or any part of the face appears. Both hands are raised to the nape,
 fastening the necklace: her fingertips hold the short pave bar as she turns it through the round ring; {HANDS}; no extra fingers.
 {FID} {WSCALE}. She wears a blush silk blouse with a low open back. Background: soft out-of-focus warm ivory wall. Soft warm window
 light from the left; one small hard specular source gives the gold a crisp edge. Shallow depth of field, the clasp and fingertips
 sharp. {GRADE} {WNEG}""")
add(18, "Held up by hand", "4:5", STILL, f"""Editorial advertising photograph, 4:5 frame. {FID} A young Indian woman's hand with light
 wheatish skin with warm honey undertones, natural texture and soft knuckle creases, {HANDS}, enters from the top of the frame and
 holds the necklace up by one point of the chain, so the necklace hangs below in a long soft U, the closed clasp hanging at the
 bottom of the U, turning slightly, in crisp focus near the centre of the lower half. {SIZE}; the ring is about as wide as one
 fingertip. SCENE: a soft out-of-focus blush plaster wall; calm empty space to the left of the chain. {LIGHT} {MACRO} {GRADE} No face,
 no arm above the wrist, no rings, no bracelets, no nail polish. {NEG}""")
worn(19, "Worn with a mulmul saree", "4:5", "fair light skin with soft neutral beige undertones",
     "a soft blush mulmul cotton saree, the pallu draped over the left shoulder and the right collarbone bare, with a plain blush blouse",
     "The chain lies on the collarbones, the clasp at the front at the centre of the throat; the fine cotton weave of the saree visible at true scale. Background: soft out-of-focus warm ivory wall with a faint jaali shadow, calm empty space in the upper right.")
worn(20, "Worn in jaali light", "4:5", "light wheatish skin with warm golden undertones",
     "an ivory linen top with a wide open boat neck",
     "The clasp is turned to the side and rests on the right collarbone. Low afternoon sun through a carved jaali screen lays a soft lattice of small star-shaped light across the skin and the linen; the clasp sits in one bright patch of sun and glows. Background: soft out-of-focus blush wall, calm space in the upper left.")

if __name__ == "__main__":
    assert len(S) == 20, len(S)
    json.dump(S, open(sys.argv[1] if len(sys.argv) > 1 else "shots.json", "w"), indent=1, ensure_ascii=False)
    for s in S: print(s["id"], s["aspect"], s["ref"], len(s["prompt"]), s["name"])
