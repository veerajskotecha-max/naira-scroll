# Four concept camps, ten frames each, for the in-stock Naira Petite pieces with the most units.
# Each frame is one witty idea: an everyday Indian object becomes the stand, a pun on the piece's name or its listing line,
# or the piece worn. Six-block prompts from the Naira image skill: shot, fidelity lock, scale, scene, light + grade, negatives.
# Reference 1 = the listing photo of the whole piece; reference 2 = a listing detail crop of the same piece.
import json, sys

# ---------------------------------------------------------------- shared blocks
HANDS = "five fingers, correct natural anatomy, short natural nails with a bare buffed finish"
MACRO = ("Honest macro optics: depth of field only a few millimetres deep, so the nearest part of the piece is needle-sharp "
         "and everything even slightly further away falls immediately and softly out of focus.")
SHALLOW = "Shallow depth of field, the piece in crisp focus and the background falling softly out of focus."
CONTACT = "A dark believable contact shadow directly beneath where the metal touches"
FILM = ("Natural film grain, believable imperfection, nothing clean or perfect. Witty, calm, handcrafted slow-luxury mood, "
        "the long quiet of an Indian afternoon, editorial demi-fine jewellery campaign quality.")
NOBG = ("Absolutely never a grey, white, black, sand, tan or beige backdrop, never a white seamless cyclorama, never black velvet.")
NOTEXT = "No text, no letters, no numbers, no logos, no labels, no watermarks."

def light(metal):
    return ("LIGHT: low warm late-afternoon sun from a window at the left, softened by a muslin curtain, shapes everything gently; "
            f"one small hard specular kicker from behind right draws a crisp bright edge along the {metal} and puts a single small "
            "pure-white catchlight in every stone.")

# ---------------------------------------------------------------- the four pieces
P = {}
P["toggle"] = dict(
    sku="YF5143", name="Toggle Link Chain", price="₹1,499", stock=80, metal="gold",
    fid=("Preserve the necklace from reference 1 exactly, with its clasp built exactly as in reference 2: a 4mm wide polished gold "
         "chain of open elongated paperclip links; it closes with one thick, chunky, polished round gold spring-gate ring about 15mm "
         "across: a heavy round tube that stops in two flat-cut ends at the top, bridged by a noticeably slimmer gate wire taking up "
         "about one sixth of the circle, with a small ball push-pin nub on a grooved collar a quarter turn from the gate; and a short "
         "slim straight gold bar about 9mm long with flat ends, set along its whole length with a single row of tiny clear pave stones, "
         "the bar joined to the other end of the chain by a small jump ring and threaded through the ring; warm 18k gold tone. Do not "
         "redesign, restyle, resize or add anything; the links must stay open elongated paperclip links, never cable, never curb, never "
         "rope; the ring must stay a spring-gate sailor ring with its slimmer gate and push-pin nub, never a plain closed donut ring; the "
         "bar stays short, about 0.6 times the ring's width, with no hook, no loop, no shackle and no clip under it, never a plain T-bar, "
         "never a bar with ball ends, never a lobster clasp; the only stones are on that bar; nothing hangs from the ring, no pendant, "
         "no charm. Only the background, surface and lighting change."),
    size=("CRITICAL SCALE: this is a fine everyday necklace, 50cm long; each paperclip link is about 4mm wide and 11mm long, the length "
          "of a grain of basmati rice, and the round ring is about 15mm across, the size of a fingernail"),
    wsize=("CRITICAL SCALE: this is a fine 4mm chain, about as wide as a grain of rice, and the round ring is about one and a half "
           "fingernails wide on the body, small and delicate at the base of the throat; never a statement chain, never chunky"),
    grade=("Palette: blush, warm ivory, dusty rose, a breath of peach; warm-neutral 18k gold, never brassy, orange or greenish."),
    neg="no other jewellery, no second necklace",
)
P["woven"] = dict(
    sku="E20267O", name="Woven Gold Hoops", price="₹1,499", stock=68, metal="gold braid",
    fid=("Preserve the earrings from reference 1 exactly, with the braid built exactly as in reference 2: one pair of chunky hoop "
         "earrings about 25mm across, each a thick braid of many gold strands with raised ridges, with one small flat round disc at the "
         "top of each hoop just under the latch end where the hinged wire clicks shut; the disc is solid, opaque, mirror-polished bright "
         "gold in exactly the same pale warm gold as the braid, never enamel, never a stone, never amber or caramel, never matte, never "
         "domed, never translucent; the closure is one thin hinged gold wire, with no bail, no loop, no T-bar and no ball-ended pin; no "
         "stones; pale warm yellow gold, never deep orange. Do not redesign, restyle, resize or add anything; both hoops are identical "
         "round 25mm circles, never elongated ovals; the braid must stay a thick interlaced braid of many fine gold strands, never a "
         "smooth tube, never a simple twisted rope, never chain links. Only the background, surface and lighting change."),
    size=("CRITICAL SCALE: each hoop is small, about 25mm across, the width of a thumb joint; the braid itself is about 5mm thick "
          "around an opening about 13mm across"),
    wsize=("CRITICAL SCALE: the hoop is small on the ear: about 40% of the ear's height, the width of the earlobe and a little more; "
           "never a statement hoop"),
    grade=("Palette: warm ivory linen, blush and peach silk thread, pale honey wood; warm-neutral pale yellow gold, never deep "
           "orange, never brassy."),
    neg="no other jewellery, no third earring",
)
P["heart"] = dict(
    sku="YF5215", name="Heartbead Bracelet", price="₹1,299", stock=28, metal="silver and gold",
    fid=("Preserve the bracelet from reference 1 exactly, with its clasp built exactly as in reference 2: a strand of about 23 "
         "mirror-polished silver steel beads of equal 6mm size, with one smaller silver bead at each end, joined by fine silver links, "
         "closed at the front by a gold toggle ring and a straight gold T-bar, with exactly one puffed gold heart about 15mm hanging "
         "from the ring on a small gold jump ring. Do not redesign, restyle, resize or add anything; the beads must stay bright polished "
         "stainless-steel silver like little mirrors, reflecting the pale surroundings and white light so they read light and bright, "
         "never gunmetal, never dark grey, never hematite, never black, never pearls, never matte; each bead mirrors its pale surroundings, so the strand reads bright pale silver with soft reflections of the background and one crisp white highlight per bead; exactly one gold heart, smooth, "
         "puffed and polished, never flat, never engraved, never set with stones. Only the background, surface and lighting change."),
    size=("CRITICAL SCALE: each bead is 6mm, the size of a peppercorn; the puffed heart is about 15mm, the size of a fingernail, "
          "clearly bigger than two beads side by side, about two and a half beads wide; the whole bracelet is about 18cm long, a slim strand"),
    wsize=("CRITICAL SCALE: each bead is about half the width of a fingernail and the gold heart about one fingernail wide; the "
           "bracelet is a slim strand on the wrist, never chunky"),
    grade=("Palette: blush pink, soft rose, warm ivory; the beads cool bright mirror silver, the clasp and heart warm-neutral 18k "
           "gold, never brassy."),
    neg="no other jewellery, no second bracelet, no watch",
)
P["prism"] = dict(
    sku="B00681C", name="Prism Rivière Bracelet", price="₹2,399", stock=68, metal="rhodium silver",
    fid=("Preserve the bracelet from reference 1 exactly, with its stones built exactly as in reference 2: a continuous line of square "
         "cushion-cut stones about 5mm each in the repeating order aqua blue, soft pink, pale yellow, every stone framed by its own fine "
         "pave halo of tiny clear stones, linked in rhodium silver tone with a fold-over clasp. Do not redesign, restyle, resize or add "
         "anything; the stones must stay cushion-cut pastel stones in the repeating aqua, pink, yellow order, never all one colour, "
         "never round, never other colours, and no two neighbouring stones are ever the same colour; every stone keeps its halo of two "
         "rows of very fine pave, the halo about a third as wide as the centre stone on each side; each stone is held by four short "
         "round bead claws flush at its corners, never long prongs or spikes. Only the background, surface and lighting change."),
    size=("CRITICAL SCALE: each stone is about 5mm, the size of a peppercorn, and each stone in its halo is about 8mm square; the "
          "bracelet is about 18cm long and only about 8mm wide, a slim line"),
    wsize=("CRITICAL SCALE: each stone is only about half the width of a fingernail; the bracelet is a slim line of stones on the "
           "wrist, never chunky"),
    grade=("Palette: warm ivory with pastel aqua, soft pink and pale butter yellow; cool bright rhodium silver, never grey or dull; "
           "the clear pave stays colourless and the pastel stones keep their own soft colours."),
    neg="no other jewellery, no second bracelet, no bangles, no rings",
)

CAMPS = {
 "toggle": dict(title="THE TURN", line="A chain that closes with a turn rather than a catch.",
   idea=("The listing's own first line is the brief. Everyday Indian things that close, open or move with a turn — a light "
          "switch, a spinning top, a haveli door, a kulhad of chai — take the necklace as if it always belonged to them, and the "
          "toggle is always the brightest point in the frame. Witty, warm, never loud.")),
 "woven": dict(title="HAND-WOVEN", line="Texture does the talking here.",
   idea=("The hoops are a braid, so they go back to where braids come from: the embroidery hoop, the spool, the loom, the charpai, "
          "the cane chair and a plait with a paranda. A hoop inside a hoop is the pun that carries the camp.")),
 "heart": dict(title="HEARTBEAT", line="Silver, with one small gold note.",
   idea=("Heartbead reads as heartbeat, and the listing calls the gold heart 'one small gold note'. So the bracelet becomes a pulse "
          "on ECG paper, a melody on a stave, a beat on a dholak, and a heart kept close: silver for the rhythm, gold for the beat.")),
 "prism": dict(title="COLOUR, IN A STRAIGHT LINE", line="Colour, laid out in a straight line.",
   idea=("Aqua, pink and yellow in one ruled line. The bracelet is laid through India's own pastels — Diwali rangoli powder, "
          "after-dinner mukhwas, tinted glass bottles, colour pencils, a watercolour stroke — always as the one straight line in the "
          "frame.")),
}

F = []
def add(camp, n, name, ar, ref, copy, prompt):
    F.append(dict(id=f"{camp[0].upper()}{n:02d}", camp=camp, name=name, aspect=ar, ref=ref, copy=copy,
                  prompt=" ".join(prompt.split())))

# ================================================================= TOGGLE · THE TURN
t = P["toggle"]; TL = light("gold")
def toggle_switch(ar):
    if ar == "4:5":
        comp = ("SCENE: the switch sits in the upper right third; the loop hangs down through the right half; the whole left half and "
                "the upper left of the frame are calm, empty, softly lit blush plaster with only the faint long shadow of a dried palm "
                "frond, for a headline.")
    else:
        comp = ("SCENE: vertical frame; the switch sits just above the middle; the loop hangs down into the lower half; the top third "
                "of the frame is calm, empty, softly lit blush plaster with only the faint long shadow of a dried palm frond, for a "
                "headline, and the bottom sixth is calm plaster too.")
    return f"""Witty editorial advertising still life, {ar} frame. {t['fid']} {t['size']}. The necklace hangs from a single vintage round
 light switch: a smooth ivory porcelain dome about 6cm across, four times the width of the ring, with one small ivory porcelain
 lever sticking straight out, mounted alone on a limewashed blush plaster wall. The chain is hooked over the switch lever at its
 middle and falls in a long soft loop about 22cm deep, both strands hanging straight under their own small weight, and the closed
 toggle clasp hangs at the very bottom of the loop, turned to face the camera, sharp and catching a sunbeam; the soft shadow of the
 chain falls on the wall beside it. {comp} No wires, no switchboard, no socket, no screws, no other switches. {TL} The plaster
 texture is visible at true scale, every trowel mark far finer than a link. {SHALLOW} {t['grade']} {FILM} {NOTEXT} No hands,
 {t['neg']}. {NOBG}"""
add("toggle", 1, "Toggle on", "4:5", "still", "Toggle on.", toggle_switch("4:5"))
add("toggle", 2, "Toggle on, story", "9:16", "still", "Toggle on.", toggle_switch("9:16"))
add("toggle", 3, "The lattu", "4:5", "still", "Closes with a turn.", f"""Witty editorial advertising still life, 4:5 frame, seen from a low
 three-quarter angle. {t['fid']} {t['size']}. A small Channapatna wooden spinning top, a lattu, lacquered in glossy bands of blush and
 ivory with one fine peach line, about 5cm across and 6cm tall with a short pointed tip, lies tipped on its side on a smooth blush
 plaster table; in place of its string the necklace is wound neatly twice around the top's waist, the two strands lying side by side
 in its groove, and the closed toggle clasp hangs from the last turn at the front, facing the camera, in crisp focus; the rest of the
 chain trails out across the table toward the camera in one loose curve. The top is about three and a half rings wide. {CONTACT}, and
 under the top. SCENE: the top sits in the lower right third; the upper left of the frame is calm, empty blush plaster wall softly
 out of focus, for a headline. {TL} {SHALLOW} {t['grade']} {FILM} {NOTEXT} No string, no other toys, no hands, {t['neg']}. {NOBG}""")
add("toggle", 4, "The haveli door", "9:16", "still", "Closes with a turn, not a catch.", f"""Witty editorial advertising photograph,
 vertical 9:16 frame: a close crop of an old haveli door painted dusty rose, the paint chalky, softly worn and finely cracked over
 old teak, with a few small round dark iron studs, each about 2cm across. {t['fid']} {t['size']}. The necklace hangs on the door where
 its old iron ring latch would be: the chain is hooked over one small dark iron staple fixed to the door and falls in a soft loop
 about 20cm deep, and the closed toggle clasp hangs at the bottom of the loop at the front, the 15mm ring about the same size as one
 of the door's iron stud heads; the seam between the two door leaves runs vertically beside it. Only about 40cm of the door's height
 is in frame, so the necklace reads clearly. SCENE: the staple and loop sit in the middle third; the top third of the frame is calm,
 plain dusty rose door panel for a headline; the bottom sixth is calm. Low warm sun rakes across the door from the left so every paint
 crack casts a tiny shadow, and the gold catches one hard bright highlight. {SHALLOW} {t['grade']} {FILM} {NOTEXT} No padlock, no
 keys, no door knocker, no other chains, no hands, {t['neg']}. {NOBG}""")
add("toggle", 5, "Every neck", "4:5", "still", "Made for every neck.", f"""Witty editorial advertising still life, 4:5 frame. {t['fid']}
 {t['size']}. The necklace is worn by a slender hand-thrown ceramic bud vase in warm ivory glaze, about 18cm tall, with a narrow neck
 about 3cm wide, twice the width of the ring, and soft round shoulders like collarbones: the chain sits around the vase's neck and
 its long loop drapes down over the shoulders and rests against the round belly of the vase, and the closed toggle clasp sits at the
 front centre, like a clasp turned to the front on a collarbone. A single fresh peach tulip stands in the vase, its flower head about
 5cm long. SCENE: the vase stands on a blush plaster ledge in front of a soft blush plaster wall, slightly right of centre; calm empty
 wall in the upper left for a headline. {CONTACT} on the glaze; the chain follows the curves of the vase under its own weight. {TL}
 {SHALLOW} {t['grade']} {FILM} {NOTEXT} No other flowers, no other vases, no hands, {t['neg']}. {NOBG}""")
add("toggle", 6, "Chai at five", "4:5", "still", "Your five o'clock chain.", f"""Warm editorial advertising still life, 4:5 frame,
 seen from a gentle angle above. {t['fid']} {t['size']}. A kulhad, a small unglazed hand-thrown terracotta cup about 7cm tall and 6cm
 across, full of milky masala chai with one thin curl of steam, stands on blush handloom linen; the necklace is wound twice around
 the body of the kulhad, the two strands lying side by side, and the short remaining length hangs at the front with the closed
 toggle clasp facing the camera, in crisp focus. Three green cardamom pods lie on the linen beside the cup, each about 15mm long, the
 same size as the ring. SCENE: the kulhad in the lower right third; the upper left is calm, empty blush linen softly out of focus, for
 a headline. {CONTACT}. {TL} {MACRO} {t['grade']} {FILM} {NOTEXT} No saucer, no biscuits, no spoon, no hands, {t['neg']}. {NOBG}""")
add("toggle", 7, "The turn", "4:5", "worn", "Turn it to the front.", f"""Editorial on-model advertising photograph, 4:5 frame, a close
 crop of the base of the throat and the collarbones: the top edge of the frame sits across the middle of the neck, well below the jaw,
 the head tilted slightly up and away so that absolutely no chin, jaw, lips, mouth or any part of the face is anywhere in the frame;
 a young Indian woman with fair light skin with warm ivory undertones, natural unretouched texture with visible pores and fine downy
 hair, wearing a crisp ivory linen shirt open at the collar. The fingertips of her right hand, {HANDS}, are at the base of her throat,
 turning the short pave bar through the round spring ring to close the necklace at the front, mid-gesture. {t['fid']} {t['wsize']}.
 Background: soft out-of-focus blush plaster wall, calm empty space in the upper left. Soft warm window light on the skin from the
 left; one small hard specular source gives the gold a crisp bright edge and each tiny stone a single pure-white catchlight. Shallow
 depth of field, the clasp and fingertips in crisp focus. {t['grade']} {FILM} No plastic skin, no heavy retouching. {NOTEXT} No face,
 no extra fingers, no rings, no nail polish, {t['neg']}. {NOBG}""")
add("toggle", 8, "Over a knit", "4:5", "worn", "Over a knit in winter.", f"""Editorial on-model advertising photograph, 4:5 frame, a
 collarbone crop from the middle of the neck down to the upper chest: the top edge of the frame sits across the middle of the neck,
 well below the jaw, the head tilted slightly up and away so that absolutely no chin, jaw, lips, mouth or any part of the face is
 anywhere in the frame; the necklace worn by a young Indian woman with fair porcelain-light skin with cool rosy undertones, natural
 unretouched texture with visible pores, wearing a soft warm ivory ribbed wool sweater with a round crew neck. The chain lies on top of
 the knit just below the neckband, the clasp at the centre front resting on the ribbed wool, the wool fibres at true scale, far finer
 than a link; the knit is pressed very slightly under the ring. {t['fid']} {t['wsize']}. Background: soft out-of-focus blush wall,
 calm space in the upper left. Cosy, still-warm winter morning light from the left; one small hard specular source gives the gold a
 crisp bright edge. Shallow depth of field, the clasp in crisp focus. {t['grade']} {FILM} No plastic skin, no heavy retouching.
 {NOTEXT} No face, {t['neg']}, no earrings. {NOBG}""")
add("toggle", 9, "A warm evening, story", "9:16", "worn", "Alone on a warm evening.", f"""Editorial on-model advertising photograph,
 vertical 9:16 frame, a collarbone crop: the top edge of the figure sits across the middle of the neck, well below the jaw, the head
 tilted up and away so that absolutely no chin, jaw, lips, mouth or any part of the face is anywhere in the frame; the necklace worn
 by a young Indian woman with warm deep brown skin with a soft golden glow, natural unretouched texture with visible pores, wearing a
 peach silk slip dress with fine straps; bare shoulders and collarbones in low warm evening sun, the clasp turned to the front at the
 base of the throat, catching the sun. {t['fid']} {t['wsize']}. The figure fills the lower sixty percent of the frame; the upper
 forty percent is a calm, softly out-of-focus warm blush wall for a headline, with no face and no hair crossing it. One small hard
 specular source gives the gold a crisp bright edge. Shallow depth of field. {t['grade']} {FILM} No plastic skin, no heavy retouching.
 {NOTEXT} No face, {t['neg']}, no earrings. {NOBG}""")
add("toggle", 10, "Diwali, given", "4:5", "still", "This Diwali, give the turn.", f"""Warm festive editorial advertising still life,
 4:5 frame, at dusk. {t['fid']} {t['size']}. The necklace lies coiled on a blush silk pad inside a small plain blush-pink jewellery
 drawer box about 8cm square, completely plain with no lettering, no logo, no print and no foil, its drawer pulled half open, the
 closed clasp resting on top of the coil facing the camera; beside the box, a small hand-pinched terracotta diya painted soft blush,
 about 7cm across, holds one small steady flame; three pale peach rose petals lie on pooled blush silk. The box is about five rings
 wide. SCENE: the box and diya in the lower right two thirds; the upper left is calm, warm, softly glowing blush, for a headline.
 LIGHT: the diya's small warm flame lights the scene from the right, with soft warm dusk window light from the left; one small hard
 specular glint on the gold and a single pure-white catchlight in each tiny clear stone. {SHALLOW} {t['grade']} {FILM} {NOTEXT} No
 marigolds, no other diyas, no fairy lights, no ribbon, no hands, {t['neg']}. {NOBG}""")

# ================================================================= WOVEN · HAND-WOVEN
w = P["woven"]; WL = light("gold braid")
def emb(ar):
    comp = ("the embroidery hoop sits slightly below the centre, on blush handloom linen that fills the rest of the frame; the upper "
            "part of the frame is calm, empty blush linen, for a headline" if ar == "4:5" else
            "vertical frame; the embroidery hoop sits just below the middle, on blush handloom linen that fills the rest of the frame; "
            "the top third is calm, empty blush linen for a headline and the bottom sixth is calm linen")
    return f"""Top-down witty editorial advertising photograph, {ar} frame: the camera looks straight down at 90 degrees, so circles stay
 true circles. {w['fid']} {w['size']}. The pair of earrings lies at the centre of a round wooden embroidery hoop about 15cm across, six
 earrings wide, made of two pale honey beechwood rings with a small wooden tightening screw, with warm ivory linen stretched drum-tight
 inside it; around the earrings, a half-finished hand embroidery of one small pressed-flower sprig in blush, peach and soft sage silk
 thread, each stitch about 2mm long; one blush silk thread is stitched in a loose loop around one earring, as if it is being sewn onto
 the linen, and a threaded needle about 5cm long rests on the linen beside it. SCENE: {comp}. Large soft diffused light from almost
 directly above with a gentle warm cast from the left; one small hard specular source gives the gold a crisp bright edge along every
 ridge of the braid. {CONTACT}; the stretched linen dimples very slightly under each earring. {w['grade']} {FILM} {NOTEXT} No scissors,
 no other tools, no hands, {w['neg']}. {NOBG}"""
add("woven", 1, "Hoop in a hoop", "4:5", "still", "Hoops, hand-woven.", emb("4:5"))
add("woven", 2, "Hoop in a hoop, story", "9:16", "still", "Hoops, hand-woven.", emb("9:16"))
add("woven", 3, "On the spool", "4:5", "still", "Worked like thread.", f"""Witty editorial advertising still life, 4:5 frame. {w['fid']}
 {w['size']}. One earring is slipped over a small wooden spool of blush silk thread standing upright, the spool about 3cm tall with a
 barrel about 12mm wide that passes snugly through the hoop's opening, so the earring rings the spool like a collar halfway down; the
 second earring lies flat on the linen beside the spool, its braid catching the light; a loose end of blush thread curls away across
 the linen. The spool is a little taller than the earring. SCENE: the spool and earrings in the lower right third, on warm ivory
 handloom linen; calm, empty blush background in the upper left, softly out of focus, for a headline. {CONTACT}. {WL} {MACRO}
 {w['grade']} {FILM} {NOTEXT} No needles, no scissors, no hands, {w['neg']}. {NOBG}""")
add("woven", 4, "The charpai", "4:5", "still", "Woven, like everything good.", f"""Editorial advertising still life, 4:5 frame, a
 close crop of the woven top of a charpai, a traditional Indian rope cot: soft blush hand-dyed cotton rope about 8mm thick, hand-woven
 in a tight diagonal lattice with small diamond gaps about 2cm across, every fibre and twist of the rope sharp at true scale.
 {w['fid']} {w['size']}. One earring hangs from a rope crossing by its thin latch wire; the other lies in the weave just below it; the
 rope is a little thicker than the braid of the hoop, and each earring spans about three rope widths. Only about 25cm of the woven top
 is in frame. Low warm late-afternoon sun rakes across the weave, casting long lattice shadows, and one small hard specular kicker
 gives the gold a crisp bright edge. SCENE: the earrings sit in the lower right third; the upper left is calm, sunlit weave falling
 softly out of focus, for a headline. {MACRO} {w['grade']} {FILM} {NOTEXT} No wooden frame in view, no pillows, no hands, {w['neg']}.
 {NOBG}""")
add("woven", 5, "On the loom, story", "9:16", "still", "Texture does the talking.", f"""Editorial advertising photograph, vertical 9:16
 frame, a close crop of a wooden handloom: hundreds of fine ivory cotton warp threads run straight up the frame, each finer than a hair,
 glowing softly in warm side light, and across the bottom of the frame runs a band of finished handwoven blush fabric with a fine
 border. {w['fid']} {w['size']}. One earring hangs in the middle of the frame, its thin latch wire hooked over a few warp threads, the
 braid in crisp focus; the earring spans about forty warp threads; the second earring hangs a little lower and to one side, softly out
 of focus. SCENE: the top third of the frame is calm warp threads falling softly out of focus, for a headline; the bottom sixth is the
 woven blush band. Low warm sun from the left; one small hard specular kicker gives the gold a crisp bright edge. {SHALLOW} {w['grade']}
 {FILM} {NOTEXT} No shuttle in view, no hands, no weaver, {w['neg']}. {NOBG}""")
add("woven", 6, "Two braids", "4:5", "worn", "Woven, twice.", f"""Editorial on-model advertising photograph, 4:5 frame, photographed from
 behind: the back of the head and one long, thick, glossy dark braid falling down the back, finished at its end with a blush silk
 paranda tassel, the head turned well away from the camera; the ear sits in the upper right third and the right edge of the frame falls
 just in front of the ear at the jaw hinge, so no cheek, cheekbone, temple, eyebrow, eyelash, eye, nose, lips or mouth appears anywhere,
 not even at the edge; one earring worn on the visible earlobe of a young Indian woman with fair light skin with warm golden undertones,
 natural unretouched texture with visible pores and fine downy hair at the nape; she wears a plain warm ivory cotton kurta. {w['fid']}
 {w['wsize']}; the braid of her hair is about twenty times thicker than the braid of the hoop. Background: soft out-of-focus blush
 plaster wall. Soft warm window light from the left; one small hard specular source gives the gold a crisp bright edge. Shallow depth of
 field, the earring in crisp focus. {w['grade']} {FILM} No plastic skin, no heavy retouching. {NOTEXT} No face, no necklace, no other
 jewellery. {NOBG}""")
add("woven", 7, "Skeins", "4:5", "still", "Texture does the talking here.", f"""Extreme macro advertising photograph, 4:5 frame.
 {w['fid']} The pair of earrings rests on loosely twisted skeins of silk embroidery floss in blush, peach and warm ivory, every floss
 strand finer than a hair: texture against texture, the raised ridges and shadows of the gold braid beside the soft twist of the floss.
 {w['size']}. {CONTACT}; the floss is pressed down slightly under the metal. SCENE: the earrings fill the lower two thirds; calm soft
 blush floss falls out of focus above. {MACRO} {WL} {w['grade']} {FILM} {NOTEXT} No needles, no hands, {w['neg']}. {NOBG}""")
add("woven", 8, "Cane, story", "9:16", "still", "Pattern on pattern.", f"""Witty editorial advertising photograph, vertical 9:16 frame, a
 close crop of the back of a honey-wood bentwood chair with Viennese cane webbing: hand-woven pale natural cane strands forming the
 classic open octagon pattern, each octagonal hole about 1cm across. {w['fid']} {w['size']}. The pair of earrings is hooked through the
 cane webbing by their thin latch wires, one a little above the other, each earring about two and a half octagon holes wide: pattern
 on pattern. Low warm sun from behind the chair throws the octagon pattern as a sharp soft-edged shadow onto a blush plaster wall
 behind. SCENE: only about 30cm of the chair back is in frame; the earrings sit in the middle third; the top third is calm blush wall
 with the soft cane shadow, for a headline. One small hard specular kicker gives the gold a crisp bright edge. {SHALLOW} {w['grade']}
 {FILM} {NOTEXT} No cushion, no hands, {w['neg']}. {NOBG}""")
add("woven", 9, "Work shirt", "4:5", "worn", "For a plain kurta or a work shirt.", f"""Editorial on-model advertising photograph, 4:5
 frame, photographed from behind the shoulder: the back of the head, the nape and dark hair gathered in a neat low bun fill most of
 the frame, the head turned well away from the camera; the ear sits in the right third of the frame and the right edge of the frame
 falls just in front of the ear at the jaw hinge, so no cheek, cheekbone, temple, eyebrow, eyelash, eye, nose, lips or mouth appears
 anywhere, not even at the edge; one earring worn on the earlobe of a young Indian woman with light wheatish skin with warm honey
 undertones, natural unretouched texture with visible pores and fine downy hair at the nape; the crisp collar of a warm ivory cotton
 work shirt at the bottom of the frame. {w['fid']} {w['wsize']}. Background: soft out-of-focus blush wall. Soft warm window light from
 the left; one small hard specular source gives the gold a crisp bright edge. Shallow depth of field, the earring in crisp focus.
 {w['grade']} {FILM} No plastic skin, no heavy retouching. {NOTEXT} No face, no necklace, no other jewellery. {NOBG}""")
add("woven", 10, "Diwali, given", "4:5", "still", "This Diwali, give texture.", f"""Warm festive editorial advertising still life, 4:5
 frame, seen from a gentle angle above. {w['fid']} {w['size']}. The pair of earrings sits in the half-open drawer of a small plain
 blush-pink jewellery box about 8cm square, completely plain with no lettering, no logo, no print and no foil, lined with blush silk;
 beside the box lie a small wooden spool of blush silk thread and one dried pink rosebud, on pooled blush silk. The box is about three
 earrings wide. SCENE: the box in the lower right two thirds; the upper left is calm, empty, softly glowing blush, for a headline.
 {CONTACT}. {WL} {SHALLOW} {w['grade']} {FILM} {NOTEXT} No ribbon, no card, no hands, {w['neg']}. {NOBG}""")

# ================================================================= HEART · HEARTBEAT
h = P["heart"]; HL = light("silver beads and the gold heart")
def ecg(ar):
    comp = ("the heartbeat line runs across the frame just below the centre; the top third of the frame is calm, empty grid, for a "
            "headline" if ar == "4:5" else
            "vertical frame; the heartbeat line runs across the full width of the frame just below the middle; the top forty percent "
            "of the frame is calm, empty grid for a headline and the bottom fifth is calm grid")
    return f"""Top-down witty editorial advertising photograph, {ar} frame: the camera looks straight down at 90 degrees onto a flat sheet.
 {h['fid']} {h['size']}. The bracelet is unfastened and laid flat in one line across a sheet of pale pink ECG chart paper printed only
 with a fine soft coral grid of small 1mm squares inside bolder 5mm squares, with no printed trace, no numbers and no letters; it is
 shaped into the classic heartbeat line that ends in a heart: from the left, the straight gold T-bar lies flat, then a level run of
 mirror-bright silver beads along one bold grid line, then the strand rises in one sharp tall spike about 4cm high, drops a little
 below the line and comes back, then runs level again, and at the right end lies the gold toggle ring with the puffed gold heart lying
 flat just beyond it, like the last beat. Every bead touches the next, bending only at its fine links; each bead spans just over one
 bold 5mm square of the grid. SCENE: {comp}. Large soft diffused light from almost directly above with a gentle warm cast from the
 left; one small hard specular source puts a crisp pure-white highlight on every silver bead and a bright edge on the gold. {CONTACT};
 every bead casts its own small dark shadow on the paper. {h['grade']} {FILM} {NOTEXT} No pens, no stethoscope, no hands,
 {h['neg']}. {NOBG}"""
add("heart", 1, "Pulse", "4:5", "still", "Every beat, a little gold.", ecg("4:5"))
add("heart", 2, "Pulse, story", "9:16", "still", "Every beat, a little gold.", ecg("9:16"))
add("heart", 3, "One gold note", "4:5", "still", "Silver, with one small gold note.", f"""Top-down witty editorial advertising
 photograph, 4:5 frame: the camera looks straight down at 90 degrees. {h['fid']} {h['size']}. A sheet of aged cream music manuscript
 paper printed only with blank five-line staves in soft warm brown ink, with no notes, no clefs, no letters, no numbers and no symbols;
 the bracelet is unfastened and laid along one stave like a melody: the silver beads rise and fall gently across the five lines like a
 run of notes, and at the end, a little apart on the stave, the gold toggle ring with the puffed gold heart sits like one gold note.
 Each stave is about 8mm tall, so each 6mm bead covers most of its height. One dried blush rose petal lies in the lower left corner.
 SCENE: the stave carrying the bracelet crosses the frame just below the centre; the top third is calm, empty staves, for a headline.
 Large soft diffused light from almost directly above with a warm cast from the left; one small hard specular source gives every bead a
 crisp pure-white highlight. {CONTACT}. {h['grade']} {FILM} {NOTEXT} No pens, no instruments, no hands, {h['neg']}. {NOBG}""")
add("heart", 4, "On the dholak", "4:5", "still", "Wedding season starts with a beat.", f"""Festive editorial advertising still life, 4:5
 frame, seen from a gentle angle above. {h['fid']} {h['size']}. The bracelet lies in a soft loose loop on the pale cream goatskin head of
 a dholak, an Indian barrel drum, the drum head about 18cm across, three bracelet-widths wide, its natural texture and faint mottling
 visible; the drum's wooden shell is lacquered soft blush and laced with braided cotton rope in blush and peach running in a zigzag down
 its side, with no metal rings anywhere on the drum. The gold heart lies at the front, in crisp focus. SCENE: the drum fills the lower
 right two thirds, cropped by the frame; the upper left is calm, softly out-of-focus blush wall, for a headline. {CONTACT}; the drum skin
 dimples very slightly under the beads. {HL} {SHALLOW} {h['grade']} {FILM} {NOTEXT} No sticks, no other instruments, no hands,
 {h['neg']}. {NOBG}""")
add("heart", 5, "Kathak hand, story", "9:16", "worn", "Keeps your rhythm.", f"""Editorial on-model advertising photograph, vertical 9:16
 frame: a single raised hand and forearm of a young Indian woman with fair porcelain-light skin with cool rosy undertones, natural
 texture and soft knuckle creases, held up in a soft classical Indian dance gesture: palm facing the camera, four fingers together and
 gently curved back, the thumb softly bent in, {HANDS}; a sheer blush chiffon dupatta falls from the forearm in soft folds. She wears the
 bracelet on that wrist, the gold toggle on top and the puffed gold heart hanging free from the ring. {h['fid']} {h['wsize']}. The arm
 rises from the bottom of the frame and the hand sits in the middle third; the top third is calm, soft blush wall for a headline. Soft
 warm window light from the left; one small hard specular source gives every bead a crisp pure-white highlight and the heart a bright
 edge. Shallow depth of field. {h['grade']} {FILM} No plastic skin, no heavy retouching. {NOTEXT} No face, no shoulder, no henna, no
 rings, no bangles, no ghungroo, no extra fingers, {h['neg']}. {NOBG}""")
add("heart", 6, "Hand on heart", "4:5", "worn", "Keep it close.", f"""Editorial on-model advertising photograph, 4:5 frame, a chest crop:
 the top edge of the frame sits across the collarbones, so absolutely no chin, jaw, lips, mouth or any part of the face is anywhere in
 the frame; a young Indian woman with light wheatish skin with warm honey undertones, natural unretouched texture with visible pores,
 wearing a soft blush wool knit sweater, rests her right hand flat over her heart on the left of her chest, fingers relaxed and
 together, {HANDS}; she wears the bracelet on that wrist, the gold toggle on top and the gold heart resting against the knit.
 {h['fid']} {h['wsize']}. Background: soft out-of-focus blush wall, calm space in the upper left. Soft warm window light from the left;
 one small hard specular source gives every bead a crisp pure-white highlight. Shallow depth of field, the bracelet in crisp focus.
 {h['grade']} {FILM} No plastic skin, no heavy retouching. {NOTEXT} No face, no rings, no necklace, no extra fingers, {h['neg']}.
 {NOBG}""")
add("heart", 7, "On the pulse, story", "9:16", "worn", "Right where the beat is.", f"""Editorial on-model advertising photograph,
 vertical 9:16 frame, an intimate close crop of the forearm and inner wrist of a young Indian woman with fair light skin with warm
 ivory undertones, natural texture with fine faint veins at the inner wrist and soft skin creases, the forearm resting palm-up on pale
 blush silk; she wears the bracelet with the toggle turned to the inside of the wrist, so the puffed gold heart rests exactly on the
 pulse point; the hand is relaxed at the bottom of the frame, fingers gently curled, {HANDS}. {h['fid']} {h['wsize']}. The wrist sits
 in the middle third; the top third is calm blush silk softly out of focus, for a headline. Soft warm window light from the left; one
 small hard specular source gives every bead a crisp pure-white highlight and the heart a bright edge. {MACRO} {h['grade']} {FILM} No
 plastic skin, no heavy retouching. {NOTEXT} No face, no rings, no extra fingers, {h['neg']}. {NOBG}""")
add("heart", 8, "The gold note", "4:5", "still", "Two metals, but only just.", f"""Extreme macro advertising photograph, 4:5 frame.
 {h['fid']} Fill most of the frame with the gold toggle ring and the straight gold T-bar, the puffed gold heart hanging from the ring,
 and the first few mirror-bright silver beads on each side, resting on pale blush silk charmeuse; the beads reflect the blush silk and
 a bright window like little round mirrors. {h['size']}; the silk weave is far finer than a bead. {CONTACT}. {MACRO} {HL} {h['grade']}
 {FILM} {NOTEXT} No hands, {h['neg']}. {NOBG}""")
add("heart", 9, "Silver varq", "4:5", "still", "Sweeter than mithai.", f"""Festive editorial advertising still life, 4:5 frame, seen from a
 gentle angle above. {h['fid']} {h['size']}. On a small round blush ceramic plate about 15cm across lie seven diamond-shaped pieces of
 kaju katli, each about 4cm across and about 6mm thick, the same thickness as a bead, topped with fine crinkled edible silver leaf; the
 bracelet lies in a loose curve across the sweets, its mirror-bright silver beads echoing the silver leaf, and the puffed gold heart
 rests on one piece of katli, the only warm gold in the frame. SCENE: the plate in the lower right two thirds on pale blush linen; the
 upper left is calm, softly out-of-focus blush, for a headline. {CONTACT}; the beads press very slightly into the soft katli. {HL}
 {SHALLOW} {h['grade']} {FILM} {NOTEXT} No gold leaf, no other sweets, no hands, {h['neg']}. {NOBG}""")
add("heart", 10, "Sent with love", "4:5", "still", "Sent with love.", f"""Editorial advertising still life, 4:5 frame. {h['fid']}
 {h['size']}. A small bundle of four plain blush gift-card envelopes with soft deckled edges, each about 6cm by 9cm, completely blank
 with no writing, no stamps and no printing, is held together by the bracelet wrapped once around its short side like a ribbon, the gold
 toggle closed on top and the puffed gold heart hanging over the front edge; one dried pink rosebud lies beside it. SCENE: the bundle
 lies at a slight angle in the lower right on warm ivory handmade paper with visible fibres; the upper left is calm and empty, for a
 headline. {CONTACT}. {HL} {SHALLOW} {h['grade']} {FILM} {NOTEXT} No ribbon, no wax seal, no handwriting, no hands, {h['neg']}.
 {NOBG}""")

# ================================================================= PRISM · COLOUR, IN A STRAIGHT LINE
p = P["prism"]; PL = light("rhodium silver")
def rangoli(ar):
    if ar == "4:5":
        geo = ("three soft parallel bands of fine rangoli powder run straight down the frame from top to bottom, each band about 6cm "
               "wide with soft feathered edges and visible fine grains: pastel aqua on the left, soft pink in the middle, pale butter "
               "yellow on the right, with thin gaps of bare floor between them; the bracelet is laid open and perfectly straight "
               "across all three bands at a right angle, horizontally, a little below the middle of the frame, like a ruled line "
               "through the colour; the upper third of the frame is the three bands alone, for a headline")
    else:
        geo = ("vertical frame; three soft parallel bands of fine rangoli powder run straight across the frame from side to side, "
               "stacked one above the other, each band about 6cm deep with soft feathered edges and visible fine grains: pastel aqua "
               "at the top, soft pink in the middle, pale butter yellow at the bottom, with thin gaps of bare floor between them; the "
               "bracelet is laid open and perfectly straight down through all three bands at a right angle, vertically, like a ruled "
               "line through the colour; the top fifth of the frame is bare ivory floor above the bands, for a headline")
    return f"""Top-down witty editorial advertising photograph, {ar} frame: the camera looks straight down at 90 degrees onto a smooth pale
 ivory lime-plaster floor. {p['fid']} {p['size']}. On the floor, {geo}. The powder grains are far finer than the tiny pave stones. Each
 stone keeps its own colour in the repeating aqua, pink, yellow order, whichever band it lies on. {CONTACT}; the bracelet presses a
 faint straight groove into the powder, with the lightest dusting at its very edges and the stones clean. Large soft diffused light from
 almost directly above with a warm cast from the left; one small hard specular source gives the silver a crisp bright edge and every
 stone a single pure-white catchlight. {p['grade']} {FILM} {NOTEXT} No diyas, no flowers, no hands, no fingerprints, {p['neg']}.
 {NOBG}"""
add("prism", 1, "Rangoli line", "4:5", "still", "Colour, laid out in a straight line.", rangoli("4:5"))
add("prism", 2, "Rangoli line, story", "9:16", "still", "Colour, laid out in a straight line.", rangoli("9:16"))
add("prism", 3, "Mukhwas", "4:5", "still", "Something sweet, after.", f"""Witty editorial advertising still life, 4:5 frame, seen from a
 gentle angle above. {p['fid']} {p['size']}. A small round hand-thrown ceramic bowl in warm ivory glaze, about 9cm across, is heaped with
 mukhwas, sugar-coated fennel seeds in pastel aqua, pink, pale yellow and white, each seed about 5mm long, the same size as one of the
 stones; the bracelet lies in a loose curl on top of the seeds and spills over the rim, its stones echoing the sugar colours; a few
 seeds are scattered on blush linen beside the bowl. SCENE: the bowl in the lower right two thirds; the upper left is calm, softly
 out-of-focus blush, for a headline. {CONTACT}; the bracelet settles slightly into the seeds. {PL} {MACRO} {p['grade']} {FILM}
 {NOTEXT} No spoon, no hands, {p['neg']}. {NOBG}""")
add("prism", 4, "Three bottles", "4:5", "still", "One line, three colours.", f"""Witty editorial advertising still life, 4:5 frame, a
 close crop of the necks and shoulders of three vintage glass bottles of different heights standing side by side, in softly tinted
 glass: pale aqua, blush pink and pale butter yellow, the three colours of the stones; light passes through the glass and throws soft
 coloured caustics onto a warm ivory plaster ledge. {p['fid']} {p['size']}. The bracelet is closed and rests around the neck of the
 aqua bottle, slipped down to where the neck widens into the shoulder, the loop tilted at a slight angle like a bangle resting on a
 bottle, the stones facing the camera; the loop is about 6cm across, a little wider than the aqua bottle's shoulder there. SCENE: the
 bottles fill the lower two thirds; the upper third is calm warm ivory plaster wall, for a headline. {CONTACT} where the bracelet
 touches the glass. {PL} {SHALLOW} {p['grade']} {FILM} {NOTEXT} No caps, no corks, no labels, no liquid, no flowers, no hands,
 {p['neg']}. {NOBG}""")
add("prism", 5, "Colour pencils", "4:5", "still", "Colour inside the lines.", f"""Top-down witty editorial advertising photograph,
 4:5 frame: the camera looks straight down at 90 degrees. {p['fid']} {p['size']}. Nine unbranded hexagonal wooden colour pencils with
 pastel lacquer, three aqua, three soft pink and three pale butter yellow, each about 7mm thick, lie side by side touching, sharpened
 tips all pointing up, on warm ivory cold-press paper, with a few curled pencil shavings; the bracelet is laid open and perfectly
 straight across the middle of the pencils at a right angle, each stone a little narrower than a pencil. SCENE: the pencils and
 bracelet in the lower two thirds; the upper third is calm ivory paper, for a headline. Large soft diffused light from almost directly
 above with a warm cast from the left; one small hard specular source gives the silver a crisp bright edge. {CONTACT}. {p['grade']}
 {FILM} {NOTEXT} The pencils carry no brand, no lettering and no printing. No hands, {p['neg']}. {NOBG}""")
add("prism", 6, "The prism", "4:5", "still", "Prism.", f"""Witty editorial advertising still life, 4:5 frame. {p['fid']} {p['size']}.
 A small clear glass triangular prism about 6cm long stands on a sheet of blush handmade paper, and the low sun passing through it lays
 a soft pastel spectrum across the paper in one straight band about 2cm wide; the bracelet lies open and perfectly straight inside that
 band of coloured light, its stones glowing. SCENE: the prism at the upper right edge of the frame, the band of light and the bracelet
 running diagonally across the lower middle; the upper left is calm, empty blush paper, for a headline. {CONTACT}. One small hard
 specular kicker gives the silver a crisp bright edge and every stone a single pure-white catchlight. {MACRO} {p['grade']} {FILM}
 {NOTEXT} No hands, {p['neg']}. {NOBG}""")
add("prism", 7, "With a white tee", "4:5", "worn", "Colour, without anything loud.", f"""Editorial on-model advertising photograph,
 4:5 frame, a torso crop from the shoulders to the waist: the top edge of the frame sits below the collarbones, so absolutely no chin,
 jaw, lips, mouth or any part of the face is anywhere in the frame; a young Indian woman with fair light skin with soft neutral beige
 undertones, natural unretouched texture with visible pores, wearing a crisp plain white cotton t-shirt, her left forearm resting across
 her waist, the relaxed hand with {HANDS}; she wears the bracelet on that wrist, the stones facing the camera. {p['fid']} {p['wsize']}.
 Background: soft out-of-focus blush wall. Soft warm window light from the left; one small hard specular source gives the silver a crisp
 bright edge and every stone a single pure-white catchlight. Shallow depth of field, the bracelet in crisp focus. {p['grade']} {FILM} No
 plastic skin, no heavy retouching. {NOTEXT} No print on the t-shirt. No face, no rings, no watch, no extra fingers, {p['neg']}.
 Never a grey, white or black background.""")
add("prism", 8, "Mulmul, story", "9:16", "worn", "Pastel, the Indian way.", f"""Editorial on-model advertising photograph, vertical
 9:16 frame, a close crop of a hand and wrist resting on the soft pleated folds of a pastel aqua mulmul cotton saree with a fine blush
 border; the hand belongs to a young Indian woman with light wheatish skin with warm golden undertones, natural texture and soft knuckle
 creases, {HANDS}; she wears the bracelet on that wrist, the stones facing the camera. {p['fid']} {p['wsize']}. The wrist sits in the
 middle third; the top third is calm, softly out-of-focus aqua and blush cotton, for a headline. Soft warm window light from the left;
 one small hard specular source gives the silver a crisp bright edge and every stone a single pure-white catchlight. Shallow depth of
 field. {p['grade']} {FILM} No plastic skin, no heavy retouching. {NOTEXT} No face, no rings, no bangles, no henna, no extra fingers,
 {p['neg']}. {NOBG}""")
add("prism", 9, "Waterproof", "4:5", "still", "Wear it in the rain.", f"""Extreme macro advertising photograph, 4:5 frame. {p['fid']}
 Fill most of the frame with four linked stones, aqua, pink, yellow, aqua, each in its fine pave halo of tiny clear stones, resting on
 blush silk satin and beaded with a few tiny clear water droplets, each droplet about 1 to 2mm, rounded, with a bright window highlight
 and a faint refracted image of the stone beneath it; more droplets bead on the satin around it. {p['size']}; the droplets are smaller
 than a stone. {CONTACT}. {MACRO} {PL} {p['grade']} {FILM} {NOTEXT} No splash, no puddle, no hands, {p['neg']}. {NOBG}""")
add("prism", 10, "One stroke", "4:5", "still", "Colour, laid out in a straight line.", f"""Top-down witty editorial advertising
 photograph, 4:5 frame: the camera looks straight down at 90 degrees. {p['fid']} {p['size']}. On a sheet of warm ivory cold-press
 watercolour paper with a deckled edge, one wide straight watercolour brushstroke about 3cm wide crosses the frame, blending softly from
 pastel aqua through soft pink to pale butter yellow, its edges blooming into the paper grain; the bracelet is laid open and perfectly
 straight exactly along the stroke, as if it painted it. A round watercolour brush rests on the paper near the end of the stroke. SCENE:
 the stroke and bracelet run across the lower middle of the frame; the upper third is calm empty paper, for a headline. Large soft
 diffused light from almost directly above with a warm cast from the left; one small hard specular source gives the silver a crisp
 bright edge. {CONTACT}. {p['grade']} {FILM} {NOTEXT} The brush carries no lettering. No hands, {p['neg']}. {NOBG}""")

if __name__ == "__main__":
    assert len(F) == 40, len(F)
    out = sys.argv[1] if len(sys.argv) > 1 else "frames.json"
    json.dump(dict(pieces=P, camps=CAMPS, frames=F), open(out, "w"), indent=1, ensure_ascii=False)
    for f in F: print(f["id"], f["aspect"], f["ref"], len(f["prompt"]), f["name"])
