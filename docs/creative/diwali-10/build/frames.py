# Diwali 10 (25 Oct 2026): one photograph per ad, 9:16 at 2K on Higgsfield (nano_banana_pro, 2 credits a frame), in the house recipe of
# the Edition Two plates (docs/creative/finished-ads/e2_frames.py): scene, fidelity lock, construction lock and morph clause, scale test,
# composition, light, absence list. IMAGE 1 is the listing packshot (the authority), IMAGE 2 a second photograph of the same piece.
# One product per frame; the huggies ad (08) shows one product in its four colours, as a set shows its own parts.
# Usage: frames.py [NN ...] -> prints the prompts; frames.py --queue [NN ...] -> ../build/queue.json (the batch request items)
# Each entry is the prompt of the frame that was kept (ledger.json has every attempt). 01 is its third attempt; the fourth asked for a
# life-size neck form and cropped it. 05, 06 and 10 were shot while LIGHT_NIGHT also asked for "fine hair" on skin, dropped after 03's
# first frame came back with a hairy wrist. 06 came back with a diya and poker chips on the table; both were retouched out of the plate.
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

LIGHT_DAY = ("LIGHT: soft large window light from the upper left, one soft natural shadow, plus ONE small hard specular kicker from the right, so the "
             "metal shows a crisp bright edge and a dark rolled edge on every curve and every stone carries internal sparkle and one pure-white "
             "catchlight, never flat colour. Honest macro optics: the jewellery is needle-sharp and the scene falls softly out of focus behind it. "
             "Real texture everywhere: grain, fibre, dust, believable imperfection, nothing plastic, no CGI gloss, no oversaturation.")
LIGHT_NIGHT = ("LIGHT: a Diwali evening indoors. The main light is warm, low flame light (2,000 K) from small oil lamps, soft and golden, with deep "
               "natural shadow, plus ONE small hard specular kicker so the metal shows a crisp bright edge and a dark rolled edge on every curve and "
               "every stone carries internal sparkle and one pure-white catchlight. Honest macro optics: the jewellery is needle-sharp, everything "
               "further away falls softly out of focus into round warm bokeh. Real texture: natural skin pores where there is skin, fibre, dust, "
               "nothing plastic, no CGI gloss, no oversaturation, no orange cast on the stones.")
FID = ("THE PRODUCT: IMAGE 1 is our approved product photograph and the authority on this exact piece: its construction, size, metal colour and "
       "stone colour; ignore its plaster cube, background and light. IMAGE 2 is a second photograph of the same piece, for construction detail only; "
       "ignore everything else in it. Preserve the piece exactly: do not redesign, restyle, resize or add anything. ")
COMP = ("COMPOSITION: 9:16 vertical photograph. The jewellery and its prop sit inside the middle 70% of the height; nothing important in the top 15% "
        "or the bottom 15%. {space}")
END_STILL = ("ABSENCE LIST: No text, no letters, no numbers, no logo, no watermark, no price tag anywhere in frame. No hands, no people. No second piece "
             "of jewellery. No religious symbols or idols. No border, no vignette: the photograph fills the frame edge to edge.")
END_HAND = ("ABSENCE LIST: No text, no letters, no numbers, no logo, no watermark, no price tag anywhere in frame. No face: nothing above the wrist "
            "and hand, no eyes, no lips. The hand has exactly five natural fingers with natural nails. No other jewellery on the body: no rings on "
            "other fingers, no bangles, no watch unless asked. No religious symbols or idols. No border, no vignette.")

# product: refs (IMAGE 1, IMAGE 2), construction lock and morph clause, from docs/creative/performance/build/products_g*.json
PRODUCTS = json.load(open(f"{HERE}/products.json"))

FRAMES = [
 dict(n="01", key="baguette-tennis-necklace", variant="ruby", light="day", end="still",
      scene="Witty editorial advertising still life for an Indian demi-fine jewellery brand. On a pale blush-ivory lime-plaster surface stands a "
            "small, low necklace display neck form covered in matte blush raw silk, seen from the front at the left of the frame; the ruby "
            "baguette tennis necklace sits closed around its neck exactly as it sits at the base of a woman's neck, a short choker line, the box "
            "clasp hidden at the back. At the right, on the plaster in front of the neck form, half "
            "a ripe pomegranate lies cut face up, its glistening deep-red arils packed tight in white pith, no cavity; seven loose arils have rolled "
            "across the plaster toward the neck form. The necklace stones are exactly the same deep red as the seeds, so the eye has to look twice.",
      scale="The neck form is about 12cm wide at the neck, the size of a slim neck; the necklace is 36cm long and only 6mm wide, a fine "
            "line on it; each baguette is about 5mm across the line and 2.5mm along it, about half the size of one 9mm pomegranate aril; the "
            "half pomegranate is about 9cm across. The stones stay small and fine against the arils; the line never thickens.",
      space="The upper third of the frame is calm, empty blush plaster wall, softly lit, for a headline.",
      comp_note="The neck form and the pomegranate sit side by side in the band from 35% to 80% of the height."),
 dict(n="02", key="prism-riviere-bracelet", light="day", end="hand",
      scene="Warm editorial photograph at a doorstep on Diwali morning, looking down at a gentle angle. On the pale ivory lime-plaster floor just "
            "below a low threshold step of pale old teak, a freshly drawn rangoli lies perfect and untouched, in exactly three soft pastel powder "
            "colours, aqua blue, baby pink and pale butter yellow: broad curved petals and a border of small round dots, crisp edges, a few stray "
            "grains. Resting on the teak step just above it is a woman's forearm and relaxed hand, warm wheatish Indian skin, a faint trace of pink "
            "rangoli powder on one fingertip because she has just finished drawing it; on her wrist she wears the Prism Riviere bracelet, its "
            "aqua, pink and yellow stones repeating the rangoli's three colours one level up, safe above the floor.",
      scale="Each stone is a 5mm cushion in a fine pave halo, about 7mm overall; the bracelet is 18cm long and about 7mm wide, a slim line round a "
            "5.5cm wrist; each powder dot of the rangoli is about 8mm, close to one stone; the rangoli is about 40cm across.",
      space="The upper third of the frame is calm: soft out-of-focus teak and plaster, for a headline.",
      comp_note="The wrist sits in the band from 30% to 50% of the height and the rangoli fills the band from 50% to 85%.",
      extra="The bracelet is the only jewellery; no rings, no bangles, no mehendi."),
 dict(n="03", key="baguette-tennis-bracelet", variant="crystal", light="night", end="hand",
      scene="Intimate macro photograph on Diwali night, the kind of close-up a relative makes when she zooms into a family photo. A young woman's "
            "slim, delicate, unmistakably feminine wrist, warm wheatish Indian skin, smooth, with natural pores and only fine near-invisible "
            "vellus hair, never a hairy or broad wrist, rests on the deep maroon raw-silk of her kurta sleeve folded back at the edge of the frame; she wears the clear crystal baguette tennis bracelet, which crosses the frame diagonally from lower left to middle "
            "right. Eight to ten baguettes are in razor-sharp focus, every stone in its own slim gold box setting with its four corner claws "
            "clearly visible; the bracelet rolls out of focus at both ends. Behind, far out of focus, the round warm bokeh of Diwali fairy lights "
            "and small oil lamps in a dark room.",
      scale="Each baguette is 5 by 2.5mm and the line is 6mm wide, about one tenth of the width of her slim 5.5cm wrist; the frame shows only "
            "about 7cm of wrist, so the skin pores prove the true small size of the stones. The bracelet sits flat and slightly loose on the "
            "wrist, a fine line, never chunky, never thicker than 6mm.",
      space="The upper third of the frame is calm, dark, softly glowing bokeh, for a headline in cream type."),
 dict(n="04", key="toggle-link-chain", light="day", end="still",
      scene="Witty editorial advertising still life. On a soft pale marigold-yellow lime-plaster surface sits a plain ivory card mithai box, the "
            "simple square box Indian sweet shops pack sweets in, open, its lid leaning against its far side; the box is lined with one sheet of "
            "crinkled silver foil paper, as sweet boxes are. There are NO sweets and no food at all: instead the gold toggle link chain lies coiled "
            "in the box on the silver foil in one loose spiral, its round spring-gate ring and short pave bar resting on top. The lid has only a "
            "thin printed gold border, no words, no pattern of letters, no logo.",
      scale="The box is about 14cm square and 4cm deep; each paperclip link is 4mm wide and 11mm long; the toggle ring is 15mm across, about one "
            "ninth of the box width, so the chain reads as fine and small inside the box.",
      space="The upper third of the frame is calm, empty marigold plaster, softly lit, for a headline."),
 dict(n="05", key="woven-gold-hoops", light="night", end="hand",
      scene="Warm, funny, tender photograph on Bhai Dooj evening. A man's large right hand comes in from the lower edge of the frame, palm up and "
            "open, held out as if offering a present a little awkwardly: warm medium-brown Indian skin with real palm creases, short clean nails, "
            "the rolled-back cuff of a plain white cotton kurta and a simple steel wristwatch at his wrist. In the middle of his palm lies the pair "
            "of woven gold hoops, small and delicate against his big hand, one hoop resting against the other. Behind him, far out of focus, the "
            "warm round bokeh of lit diyas in a dark room.",
      scale="Each hoop is 25mm across and 5mm thick, about a quarter of the width of his 9cm palm; both hoops together cover less than half of the "
            "palm. The hoops keep their true small size against the hand.",
      space="The upper third of the frame is calm, dark, softly glowing bokeh, for a headline in cream type.",
      extra="The watch is the only accessory and is plain steel with a plain dial and no text. Exactly five fingers, naturally relaxed."),
 dict(n="06", key="cushion-halo-ring", light="night", end="hand",
      scene="Elegant editorial photograph of Diwali card night. A woman's left hand, warm wheatish Indian skin with natural texture, holds three "
            "playing cards fanned out, seen from the BACK of the cards: plain deep-red card backs with a thin gold border line and a fine "
            "repeating gold lattice pattern, no letters, no numbers, no faces. Her fingers grip the cards from behind, toward the camera, and on "
            "her ring finger she wears the cushion halo ring, its halo turned to the camera. Below, the edge of a card table covered in deep "
            "bottle-green baize; far out of focus behind, the warm glow of a lit diya and another player's blurred cards on the table.",
      scale="The cushion halo is about 12mm across and the centre stone 8mm; each card is 63mm wide, so the halo is about a fifth of a card's width; "
            "the ring sits snug on a slim finger, never oversized.",
      space="The upper third of the frame is calm, dark, warm bokeh, for a headline in cream type.",
      extra="Only the one ring on the hand; nails natural or a soft nude polish."),
 dict(n="07", key="bold-nocturne-chain", light="day", end="still",
      scene="Warm, tender editorial still life about a mother's saree. On a pale ivory lime-plaster surface lies a folded silk saree that has clearly "
            "been loved for years: deep maroon silk with a broad antique-gold zari border woven with small paisleys, folded neatly in a soft stack "
            "with the pallu folded on top, the zari slightly softened with age. The bold gold link necklace lies on the folded pallu in one relaxed "
            "open curve, its single pave link at the front: new, polished, chunky gold on old woven gold.",
      scale="Each link is about 11.7mm wide and 20mm long; the necklace is 46cm long; the zari border is about 8cm wide, so it is about seven links "
            "wide; the folded saree is about 30cm across.",
      space="The upper third of the frame is calm, empty ivory plaster, softly lit, for a headline.",
      extra="The saree is silk with real woven texture, never printed; no other jewellery, no flowers."),
 dict(n="08", key="baguette-huggies", variant="all", light="day", end="still",
      scene="Charming editorial still life about gifting. On a pale ivory lime-plaster surface, four small raw-silk potli pouches stand in one neat "
            "row, each a different jewel colour, from left: deep ruby red, ivory white, emerald green and soft lavender, each with a thin gold "
            "drawstring, mouths open and softly folded down. In front of each potli lies ONE pair of the gold huggie earrings whose stones match "
            "that potli: the ruby pair before the red potli, the clear crystal pair before the ivory potli, the emerald pair before the green potli, "
            "the lavender amethyst pair before the lavender potli. Four pairs, eight earrings, all identical in design, only the stone colour changes.",
      scale="Each huggie is 15mm across and about 3mm thick, with 7 baguettes on its lower front; each potli is about 8cm tall, five times a huggie; "
            "every earring keeps the same small size.",
      space="The upper third of the frame is calm, empty ivory plaster above the potlis, softly lit, for a headline."),
 dict(n="09", key="verdant-eternity-band", light="day", end="hand",
      scene="Warm editorial photograph of the last minute of Diwali preparation, close on the top corner of a doorway. A fresh toran of glossy "
            "deep-green mango leaves on plain natural cotton string runs across the top of a pale ivory lime-plastered door frame. A woman's right "
            "hand, warm medium-brown Indian skin, reaches up and pulls the string's last knot tight around a small brass nail at the corner; her "
            "fingers hold the string naturally, the back of her hand toward the camera, and on her ring finger she wears the Verdant Eternity Band, "
            "its oval green stones repeating the green of the leaves just above it. Morning light, the job nearly done.",
      scale="Each mango leaf is about 15cm long and 4cm wide; her hand is life-size; the ring is about 2cm across on her finger, its green ovals 5 "
            "by 4mm each, far smaller than a leaf.",
      space="The lower half of the frame is calm, softly lit pale plaster wall, for a headline.",
      comp_note="The toran, the hand and the ring sit in the upper-middle band, from 16% to 52% of the height.",
      extra="Only the one ring; no bangles, no red thread, no flowers, no symbols on the wall or door."),
 dict(n="10", key="bold-nocturne-bracelet", light="night", end="still",
      scene="Quiet, beautiful editorial still life for Diwali, the night with no moon. A deep midnight-indigo lime-plaster surface fills the whole "
            "frame like a night sky, with fine natural plaster texture. In the upper middle of the frame, where a moon would hang, the bold gold "
            "link bracelet lies closed into one round circle, clasp fastened, its single pave link at the top catching the light, so the ring of "
            "polished gold reads like a full moon. A soft warm glow from a small flame just outside the left edge (not visible) rakes across the "
            "plaster, so the gold links glow warm amber and the pave sparkles; the rest of the frame falls into deep blue.",
      scale="Each link is about 11.7mm wide and 20mm long; the bracelet is 20cm long, so the closed circle is about 6.5cm across; the lobster "
            "clasp and the short extender tag tuck neatly inside the circle.",
      space="The lower half of the frame is calm, dark indigo plaster, for a headline in cream type.",
      comp_note="The gold circle sits centred between 24% and 44% of the height.")
]

def prompt(f):
    p = PRODUCTS[f["key"]]; v = f.get("variant")
    lock = p["lock"][v] if isinstance(p["lock"], dict) and v in p["lock"] else p["lock"]
    neg = p["neg"][v] if isinstance(p["neg"], dict) and v in p["neg"] else p["neg"]
    if v == "all":   # the four colours of one design: the ruby lock with the colour named per pair
        lock = p["lock"]["ruby"].replace("deep ruby-red ", "").replace("A PAIR", "Four PAIRS, one per colour,") + \
               " The four pairs differ ONLY in stone colour: deep ruby red, colourless clear crystal, bright emerald green, soft lavender-violet."
        neg = ("The stones stay 1 row of crosswise baguettes on the lower front half only, never round stones, never all the way round, never 2 "
               "rows; each pair keeps one single colour; the hoops stay small 15mm huggies, never large hoops, never with drops or charms.")
    lock = lock.replace("CONSTRUCTION LOCK: ", "").replace("THE PIECE: ", "").replace("The piece: ", "")
    light = LIGHT_DAY if f["light"] == "day" else LIGHT_NIGHT
    end = END_STILL if f["end"] == "still" else END_HAND
    if v == "all": end = end.replace("No second piece of jewellery.", "No jewellery other than the four pairs.")
    comp = COMP.format(space=f["space"]) + (" " + f["comp_note"] if f.get("comp_note") else "")
    fid = FID if len(refs(f)) > 1 else FID.replace("IMAGE 2 is a second photograph of the same piece, for construction detail only; "
                                                   "ignore everything else in it. ", "")
    return (f"{f['scene']}\n\n{fid}CONSTRUCTION LOCK: {lock} {neg}\n\nSCALE TEST: {f['scale']} The jewellery keeps its true small size; it "
            f"dominates by light and isolation, never by being enlarged.\n\n{comp}\n\n{light}" + (f" {f['extra']}" if f.get("extra") else "") +
            f"\n\n{end}")

def refs(f):
    p = PRODUCTS[f["key"]]; v = f.get("variant"); r = p["refs"]
    if isinstance(r, dict): r = r["ruby"][:1] + r["crystal"][:1] if v == "all" else r[v]
    return r[:2]

def main():
    args = sys.argv[1:]; q = "--queue" in args; want = [a for a in args if a != "--queue"]
    items = []
    for i, f in enumerate(FRAMES):
        if want and f["n"] not in want: continue
        pr = prompt(f)
        if not q: print(f"=== {f['n']} {f['key']} ({len(pr)} chars) refs={refs(f)}\n{pr}\n")
        items.append(dict(index=int(f["n"]), params=dict(model="nano_banana_pro", prompt=pr, aspect_ratio="9:16", resolution="2k",
                                                         medias=[dict(value=m, role="image_references") for m in refs(f)])))
    if q: json.dump(items, open(f"{HERE}/queue.json", "w"), indent=1, ensure_ascii=False); print(len(items), "items -> queue.json")

if __name__ == "__main__":
    main()
