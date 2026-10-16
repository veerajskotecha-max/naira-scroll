# Edition One, version 2 ("bold"): the founder's references (tennis bracelets on a racket, bangles on bottle necks) show the grammar
# that stops thumbs: ONE bold everyday object wears the piece, the piece is big and sharp, hard sun, nothing else in frame.
# Lessons from round 1 verdicts, built in:
#  - never ask the piece to form a shape (the question mark bent the Aqua C out of true): the object does the joke, not the piece;
#  - pin every prop's size as a multiple of the piece ("the cup is four huggies tall"), because the model enlarges jewellery
#    against millimetre-only referents (papillon came out 1.7x against a 15cm box);
#  - hard, low, golden sun with crisp long shadows reads as a real photograph and lifts the metal.
# Writes frames_bold.json; queue.py reads it with --bold.
import json, os
from camps_e1 import P, HANDS, CONTACT, FILM, NOBG, NOTEXT, SKIN, GOLD, SILVER

HERE = os.path.dirname(os.path.abspath(__file__))
def sun(metal):
    return ("LIGHT: hard, low, warm golden-hour sun from the left, unsoftened, so every object casts one crisp, sharp-edged long shadow "
            f"across the ground; the {metal} flares with one bright hard specular highlight and every stone throws a single pure-white "
            "catchlight and tiny rainbow sparks. High, warm contrast: the lit side glows, the shadows are deep warm rose, never grey.")
def pal(extra, metal):
    return (f"Palette: a seamless blush-peach paper ground and wall, warm ivory, dusty rose{extra}; "
            f"{GOLD if metal == 'gold' else SILVER}.")
REAL = ("Shot like a real photograph on a 100mm macro lens at f/5.6: crisp across the piece and the object, the background falling "
        "away softly; true-to-life texture, real dust, believable imperfection.")
BIG = ("The piece is the hero: the sharpest, brightest thing in the frame, nothing competing with it; the camera comes close, but "
       "the piece keeps its true small size against the object, never enlarged.")

F = []
def add(camp, n, name, ar, ref, copy, prompt):
    F.append(dict(id=f"{camp}B{n}", camp=camp, n=n, name=name, aspect=ar, ref=ref, copy=copy, prompt=" ".join(prompt.split())))

d, v, b, pp, t, a, h, s, c, r = (P[k] for k in ["dome", "verdant", "bow", "papillon", "torsade", "aqua", "halo", "square", "cluster", "riviere"])

add("dome", 1, "Handle with care", "4:5", "still", "Handle with care.", f"""Witty bold advertising still life, 4:5 frame, eye level, close.
 {d['fid']} {d['size']}. A small blush porcelain espresso cup, about 6cm tall, five huggies tall, full of milky masala chai with a thin
 wisp of steam, stands on its matching saucer on blush-peach paper; the cup has NO handle of its own: instead ONE gold dome huggie is
 clipped to the side of the cup exactly where a handle would be, standing upright with its round opening facing sideways, a tiny
 doll-sized gold handle, only about a fifth of the cup's height. The joke is how small and precious the handle is. {CONTACT}. {BIG}
 SCENE: the cup fills the centre-right, the huggie-handle on the right side facing the light; calm peach space top left for a headline.
 {sun('gold')} {REAL} {pal(', milky chai', 'gold')} {FILM} {NOTEXT} No spoon, no biscuit, no second earring, no hands, {d['neg']}.
 {NOBG}""")
add("verdant", 1, "Day-night Test", "4:5", "still", "Day-night Test.", f"""Witty bold advertising still life, 4:5 frame, close.
 {v['fid']} {v['size']}. One pink leather cricket ball, the day-night Test kind, about 7cm across, seven studs wide, rests on blush-peach
 paper with its raised white stitched seam facing the camera; the pair of studs is pushed through the leather right beside the seam,
 one above the other, worn by the ball like earrings, each stud only a seventh of the ball's width. The pink leather has real scuffs and the
 seam's stitches are crisp. {CONTACT}; the ball casts a long shadow. {BIG} SCENE: the ball fills the centre-right; calm peach space top
 left for a headline. {sun('silver')} {REAL} {pal(', one candy-pink leather ball, two deep green stones', 'silver')} {FILM} {NOTEXT}
 No bat, no stumps, no grass, no hands, {v['neg']}. {NOBG}""")
add("bow", 1, "Berry cute", "4:5", "still", "Berry cute.", f"""Witty bold advertising still life, 4:5 frame, close. {b['fid']}
 {b['size']}. One ripe glossy red strawberry, about 4cm long, three bows long, lies on its side on blush-peach paper, its green leafy cap
 to the left; ONE bow stud is pinned into the strawberry just below the leafy cap, worn like a hair bow, its post hidden in the fruit,
 the bow a third of the strawberry's width; the tiny seeds of the strawberry are each far smaller than a stone. {CONTACT}. {BIG}
 SCENE: the strawberry in the centre-right; calm peach space top left for a headline. {sun('silver')} {REAL}
 {pal(', one glossy red strawberry with a green cap', 'silver')} {FILM} {NOTEXT} No other fruit, no cream, no second stud, no hands,
 {b['neg']}. {NOBG}""")
add("papillon", 1, "Garnish", "4:5", "still", "Garnish.", f"""Witty bold advertising still life, 4:5 frame, eye level, close.
 {pp['fid']} {pp['size']}. A wide coupe glass of pale pink rose sherbet stands on a peach ledge; the ring perches on the glass's rim like
 a cocktail garnish: its band hooked over the thin glass rim and the lilac butterfly sitting upright on the edge, as if it had landed to
 sip; the coupe is about 10cm wide, seven butterflies wide, and its rim is about 3mm thick. {CONTACT}. {BIG} SCENE: the rim and the ring
 fill the upper middle of the frame; calm peach wall above for a headline. {sun('gold')} {REAL}
 {pal(', pale pink sherbet, pale lilac', 'gold')} {FILM} {NOTEXT} No straw, no fruit, no real butterflies, no hands, {pp['neg']}.
 {NOBG}""")
add("torsade", 1, "Fresh batch", "4:5", "still", "Twisted, like breakfast.", f"""Witty bold advertising still life, 4:5 frame,
 close, seen from a low angle. {t['fid']} {t['size']}. Three tiny mini butter croissants, each only about 6cm long, four huggies long,
 lie on blush-peach paper in a loose row, golden and flaky; the pair of torsade huggies lies in the row with them as if fresh from the
 same oven, each huggie only a quarter of a croissant's length, their deep twisted gold ridges rhyming with the croissants' twisted layers.
 {CONTACT}; a few flakes of pastry on the paper. {BIG} SCENE: the row runs across the lower middle; calm peach space above for a
 headline. {sun('gold')} {REAL} {pal(', golden pastry', 'gold')} {FILM} {NOTEXT} No plate, no butter, no jam, no hands, {t['neg']}.
 {NOBG}""")
add("aqua", 1, "Chill", "4:5", "still", "Chill. It's pre-order.", f"""Witty bold advertising still life, 4:5 frame, eye level, close.
 {a['fid']} {a['size']}. A tall slim glass of iced pale pink lemonade, about 7cm wide, as wide as three earrings are long, frosted with fine
 condensation and fat beads of water, stands on blush-peach paper; ONE earring hangs on the glass's rim: its tall narrow C hooked over
 the rim and its pale aqua heart hanging down the outside of the glass among the condensation beads like one more icy drop. {CONTACT}.
 {BIG} SCENE: the glass rim and the earring fill the upper middle; calm peach wall at the top left for a headline. {sun('silver')}
 {REAL} {pal(', pale pink lemonade with clear ice', 'silver')} {FILM} {NOTEXT} No straw, no fruit slice, no second earring, no hands,
 {a['neg']}. {NOBG}""")
add("halo", 1, "Smash", "4:5", "still", "Smash.", f"""Witty bold advertising still life, 4:5 frame, close. {h['fid']}
 {h['size']}. One white feather badminton shuttlecock, about 7cm tall, three and a half earrings tall, stands upright on its round cork base
 on blush-peach paper; ONE earring hangs from the tip of one of its white feathers, its sunburst disc hooked at the feather's edge and
 its pearl drop hanging freely below; each feather is about as wide as the disc. {CONTACT}; the shuttlecock throws a long feathered
 shadow. {BIG} SCENE: the shuttlecock in the centre-right, the earring on the lit side; calm peach space top left for a headline.
 {sun('gold')} {REAL} {pal(', white feathers', 'gold')} {FILM} {NOTEXT} No racket, no net, no second earring, no hands, {h['neg']}.
 {NOBG}""")
add("square", 1, "Cool, squared", "4:5", "still", "Cool, squared.", f"""Top-down witty bold advertising photograph, 4:5 frame, close:
 the camera looks straight down. {s['fid']} {s['size']}. A pale blush silicone ice-cube tray, its square cells each about 3cm wide, two and a half
 huggies wide, fills the frame at a slight angle; every cell holds a clear ice cube beading with water except ONE, which holds a square
 huggie instead, sitting dry in the cell, the only gold in the frame. {CONTACT}. {BIG} SCENE: the gold cell slightly right of centre;
 the top third shows fewer cells, calmer, for a headline. {sun('gold')} {REAL} {pal(', clear ice', 'gold')} {FILM} {NOTEXT} No drink,
 no hands, no second huggie, {s['neg']}. {NOBG}""")
add("cluster", 1, "Matches your mani", "4:5", "worn", "Matches your mani.", f"""Witty bold advertising photograph, 4:5 frame, a
 close crop of one hand only against a blush-peach wall: the fingertips of a young Indian woman with light wheatish skin with warm golden
 undertones, natural skin texture, {HANDS}, her short nails painted alternately in pastel lilac, soft pink and butter yellow; she holds
 ONE cluster stud up to the camera between her thumb and index finger, its five stones facing us, the stones matching her nail colours;
 the stud is about one and a half fingernails long. Only the fingers and part of the hand are in frame; no face, no wrist jewellery. {c['fid']} Exactly six tiny pearls, never eight: none at the two ends of the arc. {c['size']}. {BIG} SCENE: the fingertips and stud in the centre-right; calm peach wall top left for a headline. {sun('silver')}
 {REAL} {pal(', pastel lilac, pink and butter-yellow nails', 'silver')} {FILM} {SKIN} {NOTEXT} No rings, no bracelet, no second stud,
 no extra fingers, {c['neg']}. {NOBG}""")
add("riviere", 1, "Sweet, and it sparkles", "4:5", "still", "Sweet, and it sparkles.", f"""Witty bold advertising still life, 4:5
 frame, close. {r['fid']} {r['size']}. A loose heap of clear crystal mishri, Indian rock sugar, lies on blush-peach paper, each crystal
 a clear faceted lump about 1cm across, about as wide as the huggie; ONE huggie sits closed on top of the heap, upright, its single row
 of ROUND brilliant-cut stones facing the camera, each stone a small round sparkling brilliant, sparkling brighter than the sugar.
 {CONTACT}. {BIG} SCENE: the heap fills the lower middle; calm peach space above for a headline. {sun('silver')} {REAL}
 {pal('', 'silver')} {FILM} {NOTEXT} No saucer, no spoon, no fennel, no hands, no second huggie, {r['neg']}. {NOBG}""")

if __name__ == "__main__":
    json.dump(dict(frames=F), open(f"{HERE}/frames_bold.json", "w"), indent=1, ensure_ascii=False)
    print(len(F), [f["id"] for f in F])
