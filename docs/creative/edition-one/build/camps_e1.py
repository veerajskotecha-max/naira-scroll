# Edition One concept camps: eleven pre-order pieces, four frames each (three feed 4:5, one story 9:16) = 44 frames.
# Every frame is one crazy, instantly readable idea: the piece takes the place of something everyday (a mint, a pea, a doorbell,
# a cup handle, the bow on a gift), or rhymes with an Indian object (jaali, shisha, barfi, rangoli). Six-block prompts from the
# Naira image skill: shot, fidelity lock, scale, scene, light + grade, negatives.
# Reference 1 = the listing photo of the whole pair (listing-1); reference 2 = the listing macro (listing-5).
# Facts come from the listing photos (Shopify, read 15 Oct 2026). Where the listing text and photos disagree (bow and verdant
# say gold, photos show white metal; square omits its seed pearls), the photos win, as the shopper sees them.
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
HANDS = "five fingers, correct natural anatomy, short natural nails with a bare buffed finish"
MACRO = ("Honest macro optics: depth of field only a few millimetres deep, so the nearest part of the piece is needle-sharp "
         "and everything even slightly further away falls immediately and softly out of focus.")
SHALLOW = "Shallow depth of field, the piece in crisp focus and the background falling softly out of focus."
CONTACT = "A dark believable contact shadow directly beneath where the metal touches"
FILM = ("Natural film grain, believable imperfection, nothing clean or perfect. Witty, calm, handcrafted slow-luxury mood, "
        "the long quiet of an Indian afternoon, editorial demi-fine jewellery campaign quality.")
NOBG = "Absolutely never a grey, white, black, sand, tan or beige backdrop, never a white seamless cyclorama, never black velvet."
NOTEXT = "No text, no letters, no numbers, no logos, no labels, no watermarks."
SKIN = "No plastic skin, no heavy retouching."

def light(metal):
    return ("LIGHT: low warm late-afternoon sun from a window at the left, softened by a muslin curtain, shapes everything gently; "
            f"one small hard specular kicker from behind right draws a crisp bright edge along the {metal} and puts a single small "
            "pure-white catchlight in every stone.")
TOP = ("Large soft diffused light from almost directly above with a gentle warm cast from the left; one small hard specular source "
       "gives the metal a crisp bright edge and every stone a single pure-white catchlight.")
GOLD = "warm-neutral 18k gold, never brassy, orange or greenish"
SILVER = "cool bright rhodium silver, never grey or dull"
def grade(extra, metal):
    return f"Palette: blush, warm ivory, dusty rose, a breath of peach{extra}; {GOLD if metal == 'gold' else SILVER}."
UNDO = "Do not redesign, restyle, resize or add anything;"
ONLY = "Only the background, surface and lighting change."

# ---------------------------------------------------------------- the eleven pieces
P = {}
P["aqua"] = dict(title="Aqua Heart Drops", sku="WE22108C3", price=2499, metal="silver",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: white-metal half-hoop drop earrings, each an open "
       "C-shaped arc on a straight post, with a row of round clear brilliant stones in tiny claws along the outer front edge and a row of "
       "upright clear baguette stones set along the inner wall, and from the bottom tip of the arc one pale aqua-blue heart-cut stone "
       "hangs point-down in a fine silver claw setting on a small loop; bright rhodium silver tone. " + UNDO + " the arc must stay an open "
       "C, never a closed hoop, never gold; the heart must stay one pale icy aqua-blue heart, never deep blue, never sapphire, never pink, "
       "never two hearts; the only coloured stone is the heart. " + ONLY),
  size="CRITICAL SCALE: each earring is small, about 27mm long overall: the arc about 17mm tall and the heart about 9mm wide, the size of a fingernail",
  neg="no other jewellery, no third earring")
P["halo"] = dict(title="Baguette Halo Drops", sku="WE23818B", price=2200, metal="gold",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: yellow-gold drop earrings, each a flat round stud "
       "disc made of a polished gold rim around a sunburst ring of slim clear baguette stones set like rays, with one round white pearl in "
       "a gold collar at its centre, and below the disc one larger round white pearl hanging on a short gold link; exactly two pearls per "
       "earring; warm 18k gold tone. " + UNDO + " the baguettes must stay slim straight rectangular baguettes radiating like rays, never "
       "round stones, never petals; the centre stays a pearl; the drop stays one single round white pearl. " + ONLY),
  size="CRITICAL SCALE: each earring is about 26mm long: the disc about 14mm across, the size of a fingernail, and the pearl drop about 10mm, the size of a chickpea",
  neg="no other jewellery, no third earring, no loose pearls")
P["dome"] = dict(title="Bold Dome Huggies", sku="E200570", price=1649, metal="gold",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: plain mirror-polished yellow-gold dome huggie "
       "hoops, each a chunky rounded hoop that is thickest at the bottom, about 6mm deep, and tapers to a slim hinged snap closure at the "
       "top; no stones, no texture, no engraving; warm 18k gold tone. " + UNDO + " the hoop must stay a smooth domed huggie that tapers "
       "toward the hinge, never an even tube, never a thin wire hoop, never a large hoop. " + ONLY),
  size="CRITICAL SCALE: each huggie is small, about 14mm across, the size of a fingernail",
  neg="no other jewellery, no third earring")
P["papillon"] = dict(title="Lilac Papillon Ring", sku="WR11674B2", price=1899, metal="gold",
  fid=("Preserve the ring from reference 1 exactly, built exactly as in reference 2: a yellow-gold butterfly ring: one solid four-wing "
       "butterfly with its wings filled edge to edge with tiny pale lilac stones inside slim gold outlines and a plain gold bar as its "
       "body, set over a larger openwork gold butterfly outline traced with tiny round clear stones that shows around the outside of the "
       "lilac wings, on a slim plain gold band; warm 18k gold tone. " + UNDO + " exactly one lilac butterfly, its wings pale lilac-violet "
       "pavé, never enamel, never deep purple, never pink; the clear-stone outline stays an open frame larger than the wings, never "
       "filled in; the band stays slim and plain. " + ONLY),
  size="CRITICAL SCALE: the butterfly is about 18mm wide, a little wider than the finger it sits on; the band is slim, about 2mm",
  neg="no other rings, no other jewellery, no real butterflies")
P["bow"] = dict(title="Petite Bow Studs", sku="E17967C", price=1399, metal="silver",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: bright white-metal bow stud earrings, each a "
       "small bow of two scalloped, lace-edged loops and two short tails, every part outlined in tiny beaded metal and filled with tiny "
       "clear pavé stones, with one clear heart-cut stone set in claws at the knot in the middle; bright rhodium silver tone. " + UNDO +
       " the bow stays silver-white metal, never gold; the loops keep their scalloped lace edges, never smooth ribbon; the knot stays "
       "one clear heart-shaped stone. " + ONLY),
  size="CRITICAL SCALE: each bow is small, about 14mm wide, the size of a fingernail",
  neg="no other jewellery, no third earring")
P["square"] = dict(title="Petite Square Huggies", sku="WE25284B1", price=1599, metal="gold",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: mirror-polished yellow-gold square huggie hoops, "
       "each a chunky rounded tube bent into a square with softly rounded corners and a hinged snap closure, with a few tiny round white "
       "seed pearls about 2.5mm set on its outer faces; warm 18k gold tone. " + UNDO + " the hoop stays a soft-cornered square, never "
       "round, never a sharp-cornered box; the tiny pearls stay small seed pearls set on the outside of the tube. " + ONLY),
  size="CRITICAL SCALE: each huggie is small, about 15mm across, the size of a fingernail",
  neg="no other jewellery, no third earring, no loose pearls")
P["cluster"] = dict(title="Prism Cluster Studs", sku="E15838C1", price=2399, metal="silver",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: white-metal curved cluster stud earrings, each a "
       "gentle arc of five coloured stones in claw settings, in this exact order: a purple square princess stone, a pink baguette, a "
       "larger yellow emerald-cut stone at the centre, a purple square princess stone, a pink baguette, with six tiny round white pearls "
       "tucked into the gaps; bright rhodium silver tone. " + UNDO + " exactly five coloured stones in that order, purple, pink, yellow, "
       "purple, pink; the yellow stone stays the largest, at the centre; the pearls stay tiny. " + ONLY),
  size="CRITICAL SCALE: each stud is small, an arc about 20mm long, as long as a fingertip; the yellow centre stone is about 6mm tall",
  neg="no other jewellery, no third earring")
P["quatrefoil"] = dict(title="Quatrefoil Éclat Studs", sku="FE03783B", price=2449, metal="gold",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: yellow-gold quatrefoil stud earrings, each a "
       "four-pointed star outline edged with a row of tiny clear pavé stones, holding four clear pear-cut stones as petals pointing "
       "outward, each in a polished gold frame, around one round clear stone in a small gold four-point frame at the centre; warm 18k "
       "gold tone. " + UNDO + " exactly four pear-shaped petal stones pointing out to the four tips; the outline stays a pointed "
       "four-point star, never a rounded clover. " + ONLY),
  size="CRITICAL SCALE: each stud is small, about 15mm across, the size of a fingernail",
  neg="no other jewellery, no third earring")
P["riviere"] = dict(title="Rivière Huggies", sku="WE20580C", price=1999, metal="silver",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: white-metal eternity huggie hoops, each a slim "
       "hoop whose front face is set all the way round with one row of round clear brilliant stones edge to edge in shared claws, with no "
       "metal showing between neighbours, and a hinged snap closure; bright rhodium silver tone. " + UNDO + " one single row of round "
       "brilliants around the hoop, never tiny pavé, never two rows; silver-white metal, never gold. " + ONLY),
  size="CRITICAL SCALE: each huggie is small, about 15mm across, the size of a fingernail; each stone is about 2.5mm",
  neg="no other jewellery, no third earring")
P["torsade"] = dict(title="Torsade Huggies", sku="E156970", price=1799, metal="gold",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: chunky mirror-polished yellow-gold torsade "
       "huggie hoops, each a thick rounded hoop whose whole surface is twisted like a rope into deep smooth diagonal ridges, with a hinged "
       "snap closure; no stones; warm 18k gold tone. " + UNDO + " the surface stays smooth polished twisted ridges, never a braid of "
       "separate wires, never a plain smooth hoop. " + ONLY),
  size="CRITICAL SCALE: each huggie is small, about 18mm across, a little bigger than a fingernail, the hoop about 6mm thick",
  neg="no other jewellery, no third earring")
P["verdant"] = dict(title="Verdant Cushion Studs", sku="E19712C", price=2199, metal="silver",
  fid=("Preserve the earrings from reference 1 exactly, built exactly as in reference 2: white-metal halo stud earrings, each one deep "
       "emerald-green cushion-cut stone in a smooth polished bezel, ringed by a scalloped halo of round clear brilliant stones in claws; "
       "bright rhodium silver tone. " + UNDO + " the centre stays one deep green cushion-cut stone, never round, never mint or teal; the "
       "halo stays one ring of clear round stones; silver-white metal, never gold. " + ONLY),
  size="CRITICAL SCALE: each stud is small, about 12mm across, a little smaller than a fingernail",
  neg="no other jewellery, no third earring")

CAMPS = {
 "aqua": dict(name="Leave It Running", line="Aqua Heart Drops — Silver, ₹2,499",
   idea="The pale aqua heart is a drop of water, or the dot under a question. Wit in one glance."),
 "halo": dict(name="Ring Twice", line="Baguette Halo Drops, ₹2,200",
   idea="A sunburst disc with a pearl at its heart: a doorbell, a flower, the sun. The pearl drop is the dew."),
 "dome": dict(name="Not a Mint", line="Bold Dome Huggies, ₹1,649",
   idea="A plain gold dome huggie hides among everyday rings: mints, a cup handle. Spot the gold one."),
 "papillon": dict(name="The Rare One", line="Lilac Papillon Ring, ₹1,899",
   idea="A butterfly you can keep: pinned like a specimen, caught in a net, landed on a finger."),
 "bow": dict(name="Already Wrapped", line="Petite Bow Studs, ₹1,399",
   idea="The bow on the gift, the bow on the pointe shoe, the bow in the hair. Diwali gifting with a wink."),
 "square": dict(name="A Square Meal", line="Petite Square Huggies, ₹1,599",
   idea="Soft squares with seed pearls, among barfi and ice: a square that knows it's sweet."),
 "cluster": dict(name="Rangoli, to Wear", line="Prism Cluster Studs — Silver, ₹2,399",
   idea="Purple, pink and yellow in an arc: Diwali rangoli colours, nail-paint colours, worn on the ear."),
 "quatrefoil": dict(name="Mughal, in Miniature", line="Quatrefoil Éclat Studs, ₹2,449",
   idea="The quatrefoil is the jaali's own shape and the star anise's cousin. Heritage, at earring size."),
 "riviere": dict(name="Shisha, But Sparkly", line="Rivière Huggies — Silver, ₹1,999",
   idea="A ring of round brilliants beside mirror-work embroidery and rock-sugar mishri: India already sparkles."),
 "torsade": dict(name="Twisted, Like Breakfast", line="Torsade Huggies, ₹1,799",
   idea="The twist of a croissant, the twist of a silk dori: gold that rhymes with the things you love."),
 "verdant": dict(name="Two of a Kind", line="Verdant Cushion Studs — Silver, ₹2,199",
   idea="Two green stones sitting in a pea pod where the peas should be. The pair, literally."),
}

F = []
def add(camp, n, name, ar, ref, copy, prompt):
    F.append(dict(id=f"{camp}{n}", camp=camp, n=n, name=name, aspect=ar, ref=ref, copy=copy,
                  prompt=" ".join(prompt.split())))

def back_view(k, hair, top, extra=""):
    p = P[k]
    return f"""Editorial on-model advertising photograph, 4:5 frame, photographed from directly behind her, perfectly centred on the back
 of her head: {hair}; both ears show symmetrically at the left and right edges of her head, seen from behind, and each earlobe wears one
 of the pair; because the camera is straight behind her, her face is completely hidden by her own head: no cheek, cheekbone, jaw,
 eyelash, eyebrow, nose or lips anywhere in the frame, only hair, the backs of the ears, the nape, the neck, the shoulders and soft
 blush wall on both sides; a young Indian woman with light wheatish skin with warm honey undertones, natural unretouched texture with
 visible pores and fine downy hair at the nape; she wears {top}. {p['fid']} {p['size']}; on the ear it is small, the width of the
 earlobe or a little more, never a statement piece. {extra} Background: soft out-of-focus blush plaster wall. Soft warm window light
 from the left; one small hard specular source gives the metal a crisp bright edge and every stone a single pure-white catchlight.
 Shallow depth of field, both earrings in crisp focus. {grade('', p['metal'])} {FILM} {SKIN} {NOTEXT} No face, no necklace,
 {p['neg']}. {NOBG}"""

# ---------------------------------------------------------------- Aqua Heart Drops: water, and a question
a = P["aqua"]
add("aqua", 1, "Asking for a friend", "4:5", "still", "Asking for a friend.", f"""Top-down witty editorial advertising photograph,
 4:5 frame: the camera looks straight down at 90 degrees. {a['fid']} {a['size']}. ONE single earring lies flat on pale blush handmade
 cotton paper, turned so that its open C-arc curls exactly like the hook of a question mark and the aqua heart hangs just below the arc's
 lower tip exactly like the dot of a question mark: the whole earring reads as one elegant question mark, and nothing else is in the
 frame. The earring sits a little below the centre; the paper's deckled edge runs along the bottom of the frame; the upper half is calm,
 empty blush paper, for a headline. {CONTACT}; the soft paper dimples very slightly under the metal. {TOP} {grade(', with the one pale icy aqua heart as the only cool colour', 'silver')}
 {FILM} {NOTEXT} There is no drawn, printed or written question mark anywhere: the earring alone makes the shape. No second earring, no
 hands, {a['neg']}. {NOBG}""")
add("aqua", 2, "Leave it running", "4:5", "still", "Leave it running.", f"""Witty editorial advertising still life, 4:5 frame. {a['fid']}
 {a['size']}. A small vintage wall tap in soft blush enamel with a white porcelain cross handle juts out of a wall of glossy blush zellige
 tiles, each tile about 5cm square; one earring hangs from the very tip of the tap's spout by its C-arc, so the pale aqua heart hangs
 exactly where the next drop of water would fall, glinting like a drop about to let go; the spout's mouth is about 15mm across, half the
 earring's length. Below, out of focus, the rim of an ivory ceramic basin with one single real water droplet on it. SCENE: the tap and
 the earring in the right half, the earring at the centre of attention; the upper left is calm blush tile softly out of focus, for a
 headline. {light('silver')} {SHALLOW} {grade(', with the one pale icy aqua heart as the only cool colour', 'silver')} {FILM} {NOTEXT}
 No running water, no second earring, no hands, {a['neg']}. {NOBG}""")
add("aqua", 3, "Seen from behind", "4:5", "worn", "The view as you leave.", back_view("aqua",
 "dark glossy hair swept up into a soft low twisted bun at the nape", "a plain blush silk camisole with thin straps",
 "Each earring hangs below its earlobe so the pale aqua hearts catch the light like two drops."))
add("aqua", 4, "Chill", "9:16", "still", "Chill. It's pre-order.", f"""Witty editorial advertising still life, vertical 9:16 frame.
 {a['fid']} {a['size']}. A tall slim glass of pale blush rose sherbet with two clear ice cubes stands on a pale blush marble ledge, the
 glass frosted with fine condensation and a few beads of water; one earring hooks over the glass's rim by its C-arc and hangs down the
 outside of the glass, so the pale aqua heart sits among the condensation beads like one more icy drop; the glass is about 7cm wide,
 nearly three times the earring's length. SCENE: the glass in the lower half, slightly right of centre; the top third is calm, softly lit
 blush wall, for a headline. {light('silver')} {SHALLOW} {grade(', pale rose sherbet, the one pale icy aqua heart', 'silver')} {FILM}
 {NOTEXT} No straw, no fruit, no second earring, no hands, {a['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Baguette Halo Drops: doorbell, flower, sun
h = P["halo"]
add("halo", 1, "Ring twice", "4:5", "still", "Ring twice.", f"""Witty editorial advertising still life, 4:5 frame, eye level. {h['fid']}
 {h['size']}. A close crop of the edge of an old blush-painted wooden door frame beside a limewashed ivory-blush plaster wall; at doorbell
 height on the wall is a small round ivory porcelain bell plate about 4cm across, and ONE earring is set into the centre of the plate
 exactly where the bell button should be: its round sunburst disc sits flat in the middle of the plate like the button, the pearl at its
 centre like the push, and its pearl drop hangs just below the plate. There is no real doorbell button and no wire anywhere: the earring
 is the doorbell. SCENE: the plate and earring in the right third at the vertical centre; the left two thirds are calm, softly lit plaster
 and door frame, for a headline. {light('gold')} {SHALLOW} {grade('', 'gold')} {FILM} {NOTEXT} No nameplate, no house number, no
 switch, no second earring, no hands, {h['neg']}. {NOBG}""")
add("halo", 2, "Picked fresh", "4:5", "still", "Picked fresh.", f"""Witty editorial advertising still life, 4:5 frame, seen from a gentle
 angle above. {h['fid']} {h['size']}. One single fresh pale blush gerbera daisy about 9cm across lies on pale blush linen, its slim
 radiating petals echoing the earring's radiating baguettes; ONE earring sits at the very centre of the flower in place of its centre,
 the sunburst disc ringed by the petals, and its pearl drop rests on one petal like a drop of morning dew. SCENE: the flower in the lower
 right two thirds; the upper left is calm, softly out-of-focus blush linen, for a headline. {CONTACT}; the petals bend very slightly
 under the gold. {light('gold')} {MACRO} {grade(', a pale blush flower', 'gold')} {FILM} {NOTEXT} No other flowers, no leaves, no
 second earring, no hands, {h['neg']}. {NOBG}""")
add("halo", 3, "Seen from behind", "4:5", "worn", "Two pearls, either side.", back_view("halo",
 "dark glossy hair pulled back into a neat low chignon at the nape", "a plain ivory silk blouse with a soft round neckline",
 "Each pearl drop hangs freely below its earlobe."))
add("halo", 4, "Ring twice, story", "9:16", "still", "Ring twice.", f"""Witty editorial advertising still life, vertical 9:16 frame, eye
 level. {h['fid']} {h['size']}. A close crop of an old blush-painted wooden door with its frame beside a limewashed ivory-blush plaster
 wall; at doorbell height on the wall is a small round ivory porcelain bell plate about 4cm across, and ONE earring is set into the centre
 of the plate exactly where the bell button should be: its round sunburst disc sits flat in the middle like the button, the pearl at its
 centre like the push, and its pearl drop hangs just below the plate. There is no real doorbell button and no wire anywhere: the earring
 is the doorbell. SCENE: the plate and earring a little below the centre; the top third is calm, softly lit plaster, for a headline.
 {light('gold')} {SHALLOW} {grade('', 'gold')} {FILM} {NOTEXT} No nameplate, no house number, no switch, no second earring, no
 hands, {h['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Bold Dome Huggies: spot the gold one
d = P["dome"]
MINTS = ("about twenty unbranded ring-shaped mints scattered loosely across the paper, each a smooth chalky ring about 15mm across with "
         "a round hole, in pale blush pink and ivory, with no letters or marks pressed into them")
add("dome", 1, "Not a mint", "4:5", "still", "One of these is not a mint.", f"""Top-down witty editorial advertising photograph, 4:5
 frame: the camera looks straight down at 90 degrees onto pale blush cotton paper. {d['fid']} {d['size']}. On the paper lie {MINTS};
 among them lies ONE single gold dome huggie, the same size as a mint, closed, lying flat, the only gold thing in the frame and the only
 thing that shines. SCENE: the mints spread through the lower two thirds; the huggie slightly right of centre; the upper third is calm,
 empty blush paper, for a headline. {CONTACT}. {TOP} {grade('', 'gold')} {FILM} {NOTEXT} No packet, no wrapper, no second earring, no
 hands, {d['neg']}. {NOBG}""")
add("dome", 2, "Handle with care", "4:5", "still", "Handle with care.", f"""Witty editorial advertising still life, 4:5 frame, seen from
 a gentle angle above. {d['fid']} {d['size']}. A small blush porcelain espresso cup about 6cm tall, filled with steaming masala chai,
 stands on its matching saucer; the cup has no handle of its own: instead ONE gold dome huggie is fixed to the side of the cup exactly
 where the handle should be, standing upright against the porcelain like a tiny gold handle, its widest part at the bottom. SCENE: the cup
 in the lower right; the upper left is calm, softly out-of-focus blush wall, for a headline. {CONTACT}. {light('gold')} {SHALLOW}
 {grade(', milky chai', 'gold')} {FILM} {NOTEXT} No spoon, no biscuits, no second earring, no hands, {d['neg']}. {NOBG}""")
add("dome", 3, "Seen from behind", "4:5", "worn", "Small, solid, every day.", back_view("dome",
 "dark glossy hair pulled back into a sleek low bun at the nape", "a plain blush ribbed cotton tank top",
 "Each huggie hugs its earlobe closely."))
add("dome", 4, "Not a mint, story", "9:16", "still", "One of these is not a mint.", f"""Top-down witty editorial advertising photograph,
 vertical 9:16 frame: the camera looks straight down at 90 degrees onto pale blush cotton paper. {d['fid']} {d['size']}. On the paper
 lie {MINTS}; among them lies ONE single gold dome huggie, the same size as a mint, closed, lying flat, the only gold thing in the frame.
 SCENE: the mints spread through the lower half; the huggie near the centre; the top third is calm, empty blush paper, for a headline.
 {CONTACT}. {TOP} {grade('', 'gold')} {FILM} {NOTEXT} No packet, no wrapper, no second earring, no hands, {d['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Lilac Papillon Ring: the butterfly you keep
pp = P["papillon"]
add("papillon", 1, "The rare one", "4:5", "still", "The rare one.", f"""Witty editorial advertising still life, 4:5 frame, straight on.
 {pp['fid']} {pp['size']}. A small vintage wooden specimen box about 15cm wide with a glass lid propped open, lined with pale blush
 linen; where a pinned butterfly specimen would be, the ring rests at the centre of the linen, its butterfly facing the camera like the
 collection's one prize; around it the linen shows only a few tiny empty pinholes. SCENE: the box fills the lower two thirds, slightly
 right; the upper left is calm, softly out-of-focus blush wall, for a headline. {CONTACT}; the linen dimples slightly under the band.
 {light('gold')} {SHALLOW} {grade(', pale lilac', 'gold')} {FILM} {NOTEXT} No labels, no handwriting, no pins in the ring, no real
 butterflies, no hands, {pp['neg']}. {NOBG}""")
add("papillon", 2, "Caught one", "4:5", "still", "Caught one.", f"""Witty editorial advertising still life, 4:5 frame. {pp['fid']}
 {pp['size']}. A child's butterfly net with a slim pale wooden handle and a soft blush tulle net lies on pale blush linen; the ring is
 caught in the gathered blush tulle near the net's rim, the butterfly facing the camera through the fine mesh, as if it had just been
 netted; every hole of the tulle is tiny, far smaller than a stone. SCENE: the net crosses the frame diagonally; the ring in the lower
 right third; the upper left is calm blush, for a headline. {light('gold')} {MACRO} {grade(', pale lilac', 'gold')} {FILM} {NOTEXT}
 No real butterflies, no hands, {pp['neg']}. {NOBG}""")
add("papillon", 3, "It landed", "4:5", "worn", "It landed.", f"""Editorial on-model advertising photograph, 4:5 frame, a close crop of
 one raised hand only, against a soft blush plaster wall: the hand of a young Indian woman with light wheatish skin with warm golden
 undertones, natural texture and soft knuckle creases, held up gently with the fingers slightly apart and relaxed, as if a butterfly had
 just landed on it, {HANDS}; she wears the ring on her ring finger, the butterfly facing the camera. {pp['fid']} {pp['size']}. Only the
 hand and a little of the wrist are in frame; no face, no arm beyond the wrist. SCENE: the hand rises from the lower edge, slightly right;
 the upper left is calm blush wall, for a headline. Soft warm window light from the left; one small hard specular source gives the gold a
 crisp bright edge and every stone a pure-white catchlight. Shallow depth of field, the ring in crisp focus. {grade(', pale lilac', 'gold')}
 {FILM} {SKIN} {NOTEXT} No face, no other rings, no bracelet, no watch, no extra fingers, no real butterflies. {NOBG}""")
add("papillon", 4, "Lilac season", "9:16", "still", "Lilac season.", f"""Witty editorial advertising still life, vertical 9:16 frame.
 {pp['fid']} {pp['size']}. A single slim branch of pale lilac blossom lies across pale blush linen, its tiny four-petal flowers in soft
 lilac; the ring is perched on the branch among the blossoms like a butterfly visiting, its butterfly facing the camera, the blossoms each
 about the size of a stone cluster. SCENE: the branch runs diagonally through the lower half; the top third is calm blush linen, for a
 headline. {CONTACT}. {light('gold')} {MACRO} {grade(', pale lilac blossom', 'gold')} {FILM} {NOTEXT} No real butterflies, no hands,
 {pp['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Petite Bow Studs: the bow on everything
b = P["bow"]
add("bow", 1, "Already wrapped", "4:5", "still", "Already wrapped.", f"""Witty editorial advertising still life, 4:5 frame, seen from a
 gentle angle above. {b['fid']} {b['size']}. A small square gift box about 5cm wide, wrapped in pale blush paper, is tied with one narrow
 blush satin ribbon about 5mm wide crossing over its lid, but the ribbon has no bow: instead ONE bow stud sits exactly at the crossing of
 the ribbon, as the gift's bow; the second stud lies on the linen beside the box. SCENE: the box in the lower right two thirds on pale
 blush linen; the upper left is calm, softly out-of-focus blush, for a headline. {CONTACT}. {light('silver')} {SHALLOW}
 {grade('', 'silver')} {FILM} {NOTEXT} No ribbon bow, no gift tag, no other boxes, no hands, {b['neg']}. {NOBG}""")
add("bow", 2, "Pointe taken", "4:5", "still", "Pointe taken.", f"""Witty editorial advertising still life, 4:5 frame. {b['fid']}
 {b['size']}. A pair of worn blush satin ballet pointe shoes lies on pale blush wooden floorboards, their long blush satin ribbons loose and
 curling; ONE bow stud sits on the satin toe of the nearer shoe, exactly where a ribbon bow would be sewn, sparkling; the toe box is about
 6cm wide. SCENE: the shoes in the lower two thirds, the nearer toe slightly right of centre; the upper left is calm, softly out-of-focus
 blush, for a headline. {CONTACT}. {light('silver')} {SHALLOW} {grade(', blush satin', 'silver')} {FILM} {NOTEXT} No feet, no
 legs, no hands, no second stud, {b['neg']}. {NOBG}""")
add("bow", 3, "Bow, twice", "4:5", "worn", "Bow, twice.", back_view("bow",
 "dark glossy hair pulled back into a sleek low bun at the nape, tied with a soft blush satin ribbon bow about 8cm wide",
 "a plain ivory cotton top with a wide neckline",
 "The big satin bow in her hair and the two tiny sparkling bows on her ears echo each other."))
add("bow", 4, "Already wrapped, story", "9:16", "still", "Already wrapped.", f"""Witty editorial advertising still life, vertical
 9:16 frame, seen from a gentle angle above. {b['fid']} {b['size']}. A small square gift box about 5cm wide, wrapped in pale blush paper,
 is tied with one narrow blush satin ribbon about 5mm wide crossing over its lid, but the ribbon has no bow: instead ONE bow stud sits
 exactly at the crossing of the ribbon, as the gift's bow; a single small clay diya with a soft flame glows far behind, out of focus.
 SCENE: the box in the lower half; the top third is calm, softly out-of-focus blush, for a headline. {CONTACT}. {light('silver')}
 {SHALLOW} {grade(', one warm diya glow', 'silver')} {FILM} {NOTEXT} No ribbon bow, no gift tag, no other boxes, no hands, no second
 stud, {b['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Petite Square Huggies: sweet squares
s = P["square"]
BARFI = ("a small round blush ceramic plate holding nine square pieces of rose barfi, each soft pale pink square about 3cm wide and "
         "1.5cm thick, topped with fine crinkled edible silver varq and a few slivers of pistachio")
add("square", 1, "A square meal", "4:5", "still", "A square meal.", f"""Witty editorial advertising still life, 4:5 frame, seen from a
 gentle angle above. {s['fid']} {s['size']}. On pale blush linen sits {BARFI}; ONE square huggie stands upright on top of the centre
 piece of barfi like a tiny gold frame, the other lies flat beside the plate; each huggie is about half the width of a barfi square.
 SCENE: the plate in the lower right two thirds; the upper left is calm, softly out-of-focus blush, for a headline. {CONTACT}; the gold
 presses very slightly into the soft barfi. {light('gold')} {SHALLOW} {grade(', pale rose barfi', 'gold')} {FILM} {NOTEXT} No gold
 leaf, no other sweets, no hands, {s['neg']}. {NOBG}""")
add("square", 2, "Cool, squared", "4:5", "still", "Cool, squared.", f"""Top-down witty editorial advertising photograph, 4:5 frame:
 the camera looks straight down. {s['fid']} {s['size']}. A pale blush silicone ice-cube tray of fifteen square cells, each cell about 3cm
 wide, lies on pale blush linen; fourteen cells hold clear ice cubes beading with water, and ONE cell holds a square huggie instead of an
 ice cube, sitting dry in the cell, the only gold thing in the frame. SCENE: the tray fills the lower two thirds at a slight angle; the
 upper third is calm blush linen, for a headline. {CONTACT}. {TOP} {grade(', clear ice', 'gold')} {FILM} {NOTEXT} No drink, no hands,
 no second huggie, {s['neg']}. {NOBG}""")
add("square", 3, "Seen from behind", "4:5", "worn", "Squared, softly.", back_view("square",
 "dark glossy hair parted in the middle and pulled into a neat low bun at the nape", "a plain dusty-rose linen kurta with a round neck",
 "Each square huggie hugs its earlobe closely, the tiny pearls catching the light."))
add("square", 4, "A square meal, story", "9:16", "still", "A square meal.", f"""Witty editorial advertising still life, vertical 9:16
 frame, seen from a gentle angle above. {s['fid']} {s['size']}. On pale blush linen sits {BARFI}; ONE square huggie stands upright on top
 of the centre piece of barfi like a tiny gold frame, the other lies flat beside the plate; each huggie is about half the width of a barfi
 square. SCENE: the plate in the lower half; the top third is calm, softly out-of-focus blush, for a headline. {CONTACT}; the gold presses
 very slightly into the soft barfi. {light('gold')} {SHALLOW} {grade(', pale rose barfi', 'gold')} {FILM} {NOTEXT} No gold leaf, no
 other sweets, no hands, {s['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Prism Cluster Studs: rangoli colours
c = P["cluster"]
RANGOLI = ("on a smooth pale ivory-blush lime-plaster floor, a small hand-drawn Diwali rangoli: one gently curved arc of fine powder "
           "about 12cm long in three soft bands, pastel lilac, soft pink and butter yellow, its edges feathered, every grain visible and "
           "far finer than a pearl")
add("cluster", 1, "Rangoli, to wear", "4:5", "still", "Rangoli, to wear.", f"""Top-down witty editorial advertising photograph,
 4:5 frame: the camera looks straight down. {c['fid']} {c['size']}. {RANGOLI}; ONE cluster stud lies just beside the end of the arc,
 its own curve and its purple, pink and yellow stones echoing the rangoli exactly, as if the rangoli had been made from it. SCENE: the arc
 sweeps through the lower two thirds; the upper third is calm, bare floor, for a headline. {CONTACT}; the stud rests on clean floor, the
 lightest dusting of powder at its edge. {TOP} {grade(', pastel lilac, pink and butter yellow', 'silver')} {FILM} {NOTEXT} No diyas,
 no flowers, no hands, no second stud, {c['neg']}. {NOBG}""")
add("cluster", 2, "Matches your mani", "4:5", "still", "Matches your mani.", f"""Witty editorial advertising still life, 4:5 frame.
 {c['fid']} {c['size']}. Three small unbranded glass bottles of nail paint stand in a row on a pale blush ledge, one pastel lilac, one soft
 pink, one butter yellow, each about 5cm tall with a plain ivory cap; ONE cluster stud lies flat on the ledge in front of them, its
 purple, pink and yellow stones lined up with the three bottles' colours. SCENE: the bottles in the right half, softly out of focus; the
 stud in crisp focus in the lower right third; the upper left is calm blush wall, for a headline. {CONTACT}. {light('silver')} {SHALLOW}
 {grade(', pastel lilac, pink and butter yellow', 'silver')} {FILM} {NOTEXT} The bottles carry no labels, no brand, no lettering. No
 brushes, no hands, no second stud, {c['neg']}. {NOBG}""")
add("cluster", 3, "Seen from behind", "4:5", "worn", "Colour, climbing.", back_view("cluster",
 "dark glossy hair pulled up into a soft high bun", "a plain pale lilac silk camisole with thin straps",
 "Each cluster stud follows the curve of its earlobe."))
add("cluster", 4, "Rangoli, story", "9:16", "still", "Rangoli, to wear.", f"""Top-down witty editorial advertising photograph,
 vertical 9:16 frame: the camera looks straight down. {c['fid']} {c['size']}. {RANGOLI}; ONE cluster stud lies just beside the end of the
 arc, its own curve and its purple, pink and yellow stones echoing the rangoli exactly. SCENE: the arc sweeps through the lower half; the
 top third is calm, bare floor, for a headline. {CONTACT}. {TOP} {grade(', pastel lilac, pink and butter yellow', 'silver')} {FILM}
 {NOTEXT} No diyas, no flowers, no hands, no second stud, {c['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Quatrefoil Éclat Studs: heritage in miniature
q = P["quatrefoil"]
JAALI = ("a carved blush-pink sandstone jaali screen, its pattern of open quatrefoil cut-outs each about 6cm across, warm sun streaming "
         "through it and laying quatrefoil-shaped patches of light on the stone ledge below")
add("quatrefoil", 1, "Mughal, in miniature", "4:5", "still", "Mughal, in miniature.", f"""Witty editorial advertising still life,
 4:5 frame. {q['fid']} {q['size']}. {JAALI}; ONE stud sits on the ledge in the middle of one quatrefoil patch of sunlight, its four-point
 shape matching the light around it, about a quarter of the light's width. SCENE: the jaali fills the upper part softly out of focus; the
 ledge and stud in the lower third, slightly right; calm blush stone in the upper left, for a headline. {CONTACT}. {light('gold')}
 {SHALLOW} {grade(', blush sandstone', 'gold')} {FILM} {NOTEXT} No people, no hands, no second stud, {q['neg']}. {NOBG}""")
add("quatrefoil", 2, "Star of the spice box", "4:5", "still", "Star of the spice box.", f"""Witty editorial advertising still life,
 4:5 frame, seen from a gentle angle above. {q['fid']} {q['size']}. A small round blush ceramic bowl holds a loose heap of whole star
 anise, each star about 3cm across, twice the stud's width; ONE stud sits on top of the heap among the stars, its four points echoing
 theirs, the only gold and the only thing that sparkles. SCENE: the bowl in the lower right two thirds on pale blush linen; the upper left
 is calm, softly out-of-focus blush, for a headline. {CONTACT}. {light('gold')} {SHALLOW} {grade('', 'gold')} {FILM} {NOTEXT} No other
 spices, no spoon, no hands, no second stud, {q['neg']}. {NOBG}""")
add("quatrefoil", 3, "Seen from behind", "4:5", "worn", "A little heritage, either side.", back_view("quatrefoil",
 "dark glossy hair pulled back into a low braided bun at the nape", "a plain blush silk blouse with a soft round neckline",
 "Each stud sits flat on its earlobe, the four points crisp."))
add("quatrefoil", 4, "Light in fours, story", "9:16", "still", "Mughal, in miniature.", f"""Witty editorial advertising still life,
 vertical 9:16 frame. {q['fid']} {q['size']}. Low warm sun passing through a carved jaali out of frame lays a soft pattern of
 quatrefoil-shaped patches of light, each about 6cm across, on a smooth blush plaster wall and the blush stone ledge below it; ONE stud
 sits on the ledge in the middle of one quatrefoil patch of light, its four-point shape matching the light around it. SCENE: the pattern
 of light fills the upper two thirds of the wall, calm, for a headline; the ledge and stud in the lower third. {CONTACT}. {light('gold')}
 {SHALLOW} {grade(', blush sandstone', 'gold')} {FILM} {NOTEXT} No people, no hands, no second stud, {q['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Rivière Huggies: India already sparkles
r = P["riviere"]
SHISHA = ("pale blush cotton fabric embroidered in the Indian shisha mirror-work tradition: small round mirrors about 12mm across, each "
          "ringed with tight blush and ivory thread stitches, scattered in a loose pattern")
add("riviere", 1, "Shisha, but sparkly", "4:5", "still", "Shisha, but sparkly.", f"""Top-down witty editorial advertising photograph,
 4:5 frame: the camera looks straight down. {r['fid']} {r['size']}. {SHISHA}; ONE huggie lies flat among the mirrors, closed, its ring of
 round brilliants answering the round mirrors around it, the brightest sparkle in the frame; each mirror is a little smaller than the
 huggie. SCENE: the embroidery fills the frame; the huggie slightly right of centre in the lower half; the upper third is calmer, with
 only a few mirrors, for a headline. {CONTACT}. {TOP} {grade(', thread in blush and ivory', 'silver')} {FILM} {NOTEXT} No hands, no
 second huggie, {r['neg']}. {NOBG}""")
add("riviere", 2, "Sweet, and it sparkles", "4:5", "still", "Sweet, and it sparkles.", f"""Witty editorial advertising still life,
 4:5 frame, seen from a gentle angle above. {r['fid']} {r['size']}. A small blush ceramic saucer holds a heap of clear crystal mishri,
 Indian rock sugar, each crystal a clear faceted lump about 1cm across, with a few loose crystals on the pale blush linen; ONE huggie sits
 on top of the heap, closed, its round brilliants sparkling brighter than the sugar. SCENE: the saucer in the lower right two thirds; the
 upper left is calm, softly out-of-focus blush, for a headline. {CONTACT}. {light('silver')} {SHALLOW} {grade('', 'silver')} {FILM}
 {NOTEXT} No spoon, no fennel, no hands, no second huggie, {r['neg']}. {NOBG}""")
add("riviere", 3, "Seen from behind", "4:5", "worn", "A ring of light, each side.", back_view("riviere",
 "dark glossy hair pulled back into a sleek low bun at the nape", "a plain ivory silk camisole with thin straps",
 "Each huggie hugs its earlobe closely, sparkling."))
add("riviere", 4, "Shisha, story", "9:16", "still", "Shisha, but sparkly.", f"""Top-down witty editorial advertising photograph,
 vertical 9:16 frame: the camera looks straight down. {r['fid']} {r['size']}. {SHISHA}; ONE huggie lies flat among the mirrors, closed,
 its ring of round brilliants answering the round mirrors around it, the brightest sparkle in the frame. SCENE: the embroidery fills the
 frame; the huggie near the centre; the top third is calmer, with only a few mirrors, for a headline. {CONTACT}. {TOP}
 {grade(', thread in blush and ivory', 'silver')} {FILM} {NOTEXT} No hands, no second huggie, {r['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Torsade Huggies: the twist
t = P["torsade"]
CROISSANT = ("a small round blush ceramic plate with two mini butter croissants, each about 8cm long, golden and flaky with crisp "
             "spiral ridges")
add("torsade", 1, "Twisted, like breakfast", "4:5", "still", "Twisted, like breakfast.", f"""Witty editorial advertising still life,
 4:5 frame, seen from a gentle angle above. {t['fid']} {t['size']}. On pale blush linen sits {CROISSANT}; the pair of torsade huggies
 lies on the plate between the croissants, their twisted gold ridges rhyming with the croissants' spirals; each huggie is about a quarter
 of a croissant's length. SCENE: the plate in the lower right two thirds; the upper left is calm, softly out-of-focus blush, for a
 headline. {CONTACT}. {light('gold')} {SHALLOW} {grade(', a golden croissant crust', 'gold')} {FILM} {NOTEXT} No butter, no jam, no
 cutlery, no hands, {t['neg']}. {NOBG}""")
add("torsade", 2, "Tie it up", "4:5", "still", "Twist, in gold.", f"""Witty editorial advertising still life, 4:5 frame. {t['fid']}
 {t['size']}. A twisted blush silk dori cord about 5mm thick, the kind that ties the back of a blouse, lies in a loose curve on pale ivory
 silk, ending in two small blush silk tassels; the pair of torsade huggies is threaded onto the cord near the tassels, their twisted gold
 ridges echoing the twist of the silk; the cord is a little thinner than a hoop. SCENE: the cord curves through the lower two thirds; the
 upper left is calm, softly out-of-focus blush, for a headline. {CONTACT}. {light('gold')} {MACRO} {grade(', blush silk', 'gold')}
 {FILM} {NOTEXT} No hands, no blouse, {t['neg']}. {NOBG}""")
add("torsade", 3, "Seen from behind", "4:5", "worn", "The twist, either side.", back_view("torsade",
 "dark glossy hair twisted into a soft low knot at the nape", "a plain warm ivory cotton kurta with a round neck",
 "Each huggie hugs its earlobe, its twisted ridges catching the light."))
add("torsade", 4, "Twisted, story", "9:16", "still", "Twisted, like breakfast.", f"""Witty editorial advertising still life, vertical
 9:16 frame, seen from a gentle angle above. {t['fid']} {t['size']}. On pale blush linen sits {CROISSANT} and a small cup of milky chai;
 the pair of torsade huggies lies on the plate between the croissants, their twisted gold ridges rhyming with the croissants' spirals.
 SCENE: the plate in the lower half; the top third is calm, softly out-of-focus blush, for a headline. {CONTACT}. {light('gold')}
 {SHALLOW} {grade(', a golden croissant crust', 'gold')} {FILM} {NOTEXT} No butter, no jam, no cutlery, no hands, {t['neg']}. {NOBG}""")

# ---------------------------------------------------------------- Verdant Cushion Studs: two of a kind
v = P["verdant"]
POD = ("one fresh green pea pod about 9cm long, split open along its seam and lying on its back, holding a neat row of fresh round green "
       "peas, each pea about 8mm")
add("verdant", 1, "Two of a kind", "4:5", "still", "Two of a kind.", f"""Witty editorial advertising still life, 4:5 frame, seen from a
 gentle angle above. {v['fid']} {v['size']}. On a small round blush ceramic plate lies {POD}; in the middle of the row, two of the peas
 have been replaced by the pair of studs, sitting snugly in the pod among the real peas, their deep green stones and silver halos the only
 sparkle, each stud a little wider than a pea. SCENE: the plate in the lower right two thirds on pale blush linen; the upper left is calm,
 softly out-of-focus blush, for a headline. {CONTACT}. {light('silver')} {MACRO} {grade(', one fresh green pod', 'silver')} {FILM}
 {NOTEXT} No other vegetables, no hands, {v['neg']}. {NOBG}""")
add("verdant", 2, "Elaichi, but forever", "4:5", "still", "Elaichi, but forever.", f"""Witty editorial advertising still life, 4:5
 frame, seen from a gentle angle above. {v['fid']} {v['size']}. A small blush ceramic dish holds a loose heap of whole green cardamom
 pods, each pod about 15mm long, a little longer than a stud; the pair of studs sits on top of the heap, their deep green stones echoing
 the cardamom's green, the only sparkle in the frame. SCENE: the dish in the lower right two thirds on pale blush linen; the upper left is
 calm, softly out-of-focus blush, for a headline. {CONTACT}. {light('silver')} {SHALLOW} {grade(', soft cardamom green', 'silver')}
 {FILM} {NOTEXT} No other spices, no spoon, no hands, {v['neg']}. {NOBG}""")
add("verdant", 3, "Seen from behind", "4:5", "worn", "A little green, either side.", back_view("verdant",
 "dark glossy hair pulled back into a sleek low bun at the nape", "a plain blush silk blouse with a soft round neckline",
 "Each stud sits flat on its earlobe, the green stones glowing."))
add("verdant", 4, "Two of a kind, story", "9:16", "still", "Two of a kind.", f"""Witty editorial advertising still life, vertical 9:16
 frame, seen from a gentle angle above. {v['fid']} {v['size']}. On a small round blush ceramic plate lies {POD}; in the middle of the row,
 two of the peas have been replaced by the pair of studs, sitting snugly in the pod among the real peas, each stud a little wider than a
 pea. SCENE: the plate in the lower half; the top third is calm, softly out-of-focus blush, for a headline. {CONTACT}. {light('silver')}
 {MACRO} {grade(', one fresh green pod', 'silver')} {FILM} {NOTEXT} No other vegetables, no hands, {v['neg']}. {NOBG}""")

if __name__ == "__main__":
    json.dump(dict(pieces=P, camps=CAMPS, frames=F), open(f"{HERE}/frames.json", "w"), indent=1, ensure_ascii=False)
    print(len(F), "frames;", {k: sum(1 for f in F if f["camp"] == k) for k in P})
