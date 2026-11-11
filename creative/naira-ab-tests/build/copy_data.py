"""Copy, buttons, links and test plan for the 14 angle tests. Every product fact is from the live Shopify product pages (11 Nov 2026)."""

UTM = 'utm_source=meta&utm_medium=paid&utm_campaign={camp}&utm_content={id}'
TRUST = 'Free insured shipping · Cash on delivery'

SETS = [
    dict(
        key='P', name='Prism Rivière · the Sweet On You photo', piece='Prism Rivière Bracelet', price='₹2,399', stock=49,
        chip='BRACELETS', token='rani', fmt='Feed 4:5 · 1080 × 1350', placement='Instagram Feed only, as the original ran',
        photo='Library image 2ebe51f1, 9 Aug 2026: the pastel bracelet half-buried in sugared jelly sweets',
        url='https://www.nairaflore.com/products/prism-riviere-bracelet', camp='ab-prism-sugar-nov26',
        original=dict(name='A6 · Sweet On You · bracelets', when='from 29 Aug · Feed only · women 20–55 · metros',
                      stats=[('₹4,917', 'spent'), ('2.59%', 'link CTR'), ('₹42', 'per link click'), ('117', 'link clicks'), ('8 / 109', 'add-to-carts / page views'), ('1', 'sale, ₹2,849')]),
        ads=[
            dict(id='P1', slug='treat-yourself', angle='Self-treat', hook='TREAT · yourself.', cta='Shop now',
                 why='Most demi-fine is bought for yourself. "Treat" turns the sweets into permission to buy.',
                 primary='A treat that lasts. Aqua, soft pink and pale yellow cushion-cut stones of about 5mm, each in its own pavé halo, linked in one flat line. PVD rhodium on surgical steel, so it is waterproof and tarnish-free. The Prism Rivière Bracelet, ₹2,399. Free insured shipping and cash on delivery across India.',
                 headline='Prism Rivière Bracelet · ₹2,399'),
            dict(id='P2', slug='zero-sugar-label', angle='Proof as parody', hook='ZERO SUGAR. · all sparkle.', cta='Learn more',
                 why='Proof in a format everyone already reads. Every line on the label is a real spec from the product page.',
                 primary='Zero sugar, all sparkle. Per serving: one 18cm row of cushion-cut stones in aqua, soft pink and pale yellow, a pavé halo around every stone, PVD rhodium on surgical steel. Waterproof, tarnish-free, fits wrists of 15 to 19cm. The Prism Rivière Bracelet, ₹2,399.',
                 headline='Prism Rivière Bracelet · ₹2,399'),
            dict(id='P3', slug='one-of-these', angle='Spot the bracelet', hook="ONE OF THESE · isn't a sweet.", cta='Shop now',
                 why='A small puzzle makes people look twice at the stones, which is the whole point of this photo.',
                 primary='Look again. The stones are cushion-cut, about 5mm, in the same aqua, pink and pale yellow as the sweets, and every one sits in its own pavé halo. The difference is that this one is waterproof and tarnish-free. The Prism Rivière Bracelet, ₹2,399, with free insured shipping and cash on delivery.',
                 headline='Prism Rivière Bracelet · ₹2,399'),
            dict(id='P4', slug='sugar-coating-vs-pvd', angle='Plating, explained', hook="SUGAR COATING · wears off. PVD doesn't.", cta='Learn more',
                 why='Answers the "plated jewellery fades" doubt with the product page\'s own PVD explanation.',
                 primary="Sugar coating wears off. PVD doesn't. Regular plating is a soft layer that wears off over time. PVD is bonded to the metal in a vacuum, so it is far harder, stands up to sweat and keeps its colour much longer. The Prism Rivière Bracelet: PVD rhodium on surgical steel, waterproof and tarnish-free. ₹2,399.",
                 headline='Prism Rivière Bracelet · ₹2,399'),
            dict(id='P5', slug='gift-tag', angle='Gifting', hook="FOR THE ONE · you're sweet on.", cta='Order now',
                 why='Wedding season, then Christmas gifting. The tag does the asking; the box line removes the wrapping worry.',
                 primary="For the one you're sweet on. A flat line of pastel cushion-cut stones, each in a pavé halo, on PVD rhodium that stays bright through daily wear and water. It arrives in a Naira Petite box, ready to give. The Prism Rivière Bracelet, ₹2,399. Free insured shipping and cash on delivery across India.",
                 headline='Prism Rivière Bracelet · ₹2,399'),
            dict(id='P6', slug='sweeter-by-10', angle='Offer', hook='SWEETER · by 10%.', cta='Get offer',
                 why='Tests whether a discount beats a story on the photo that already won. NAIRA10 is live, no minimum, no end date.',
                 primary='Sweeter by 10%. Code NAIRA10 takes 10% off any order, no minimum. The Prism Rivière Bracelet: pastel cushion-cut stones in pavé halos, PVD rhodium on surgical steel, waterproof and tarnish-free. ₹2,399 before the code, with free insured shipping and cash on delivery.',
                 headline='10% off with code NAIRA10'),
            dict(id='P7', slug='pov-sweets', angle='Native caption', hook='pov: you came for the sweets · and left with the bracelet', cta='Buy now',
                 why='Caption-style text reads like a post before it reads like an ad, which buys the first second.',
                 primary='pov: you came for the sweets and left with the bracelet. Pastel stones in pavé halos, PVD rhodium on surgical steel, waterproof and tarnish-free. The Prism Rivière Bracelet, ₹2,399. Free insured shipping and cash on delivery across India.',
                 headline='Prism Rivière Bracelet · ₹2,399'),
        ]),
    dict(
        key='W', name='Woven Gold Hoops · the red Woven photo', piece='Woven Gold Hoops', price='₹1,199', stock=49,
        chip='EARRINGS', token='haldi', fmt='Story 9:16 · 1080 × 1920', placement='Instagram Stories only, as the original runs',
        photo='Library image 141d0fbd, 6 Aug 2026: the braided hoops on an oxblood lacquer dome beaded with water',
        url='https://www.nairaflore.com/products/woven-gold-hoops', camp='ab-woven-red-nov26',
        original=dict(name="W1 · Woven Gold Hoops 'Woven, not cast' (red) · Story 9:16", when='live since 3 Nov · IG Stories only · women 18–65 · all India',
                      stats=[('₹1,097', 'spent'), ('2.35%', 'link CTR'), ('₹34', 'per link click'), ('32', 'link clicks'), ('10 / 38', 'add-to-carts / page views'), ('1.52', 'ROAS, 1 sale')]),
        ads=[
            dict(id='W1', slug='waterproof-haldi', angle='Waterproof, for the wedding', hook='WATERPROOF. · only the haldi washes off.', cta='Shop now',
                 why='The water on the dome is the proof and the haldi is the reason. Built for the wedding season.',
                 primary='Waterproof. Only the haldi washes off. 25mm hoops of braided gold-tone rope, 18k gold PVD on surgical steel, so the colour holds through every function and every wash. The Woven Gold Hoops, ₹1,199. Free insured shipping and cash on delivery across India.',
                 headline='Woven Gold Hoops · ₹1,199'),
            dict(id='W2', slug='price-not-a-typo', angle='Price shock', hook='₹1,199 · not a typo.', cta='Buy now',
                 why='Price-led stop. The hoops sit in front of the number, so price and product land in the same glance.',
                 primary='₹1,199. Not a typo. Chunky 25mm hoops of braided gold-tone rope, 18k gold PVD on surgical steel, waterproof and tarnish-free, sold as a pair. Free insured shipping and cash on delivery across India.',
                 headline='Woven Gold Hoops · ₹1,199'),
            dict(id='W3', slug='look-closer', angle='Craft, shown', hook='LOOK CLOSER. · every strand is there.', cta='Learn more',
                 why='Keeps the original craft idea but shows the braid instead of making the unverified "not cast" claim.',
                 primary='Look closer. Each hoop is a thick braided rope of gold-tone strands, so the surface reads as ridge and shadow, never a flat tube. 25mm across, 18k gold PVD on surgical steel, waterproof and tarnish-free. The Woven Gold Hoops, ₹1,199.',
                 headline='Woven Gold Hoops · ₹1,199'),
            dict(id='W4', slug='every-function', angle='One pair, every function', hook='ONE PAIR. · every function.', cta='Order now',
                 why='Answers "will I wear it enough" in the season of six outfits.',
                 primary='One pair, every function. Roka to reception, 25mm braided hoops that carry a lehenga, a plain kurta or a work shirt. 18k gold PVD on surgical steel and waterproof, so the haldi washes off and the gold stays. The Woven Gold Hoops, ₹1,199. Free insured shipping and cash on delivery.',
                 headline='Woven Gold Hoops · ₹1,199'),
            dict(id='W5', slug='take-10-off', angle='Offer', hook='TAKE 10% OFF. · keep all the gold.', cta='Get offer',
                 why='Tests whether a discount beats a story on the photo that already wins.',
                 primary='Take 10% off and keep all the gold. Code NAIRA10 works on any order, no minimum. The Woven Gold Hoops: 25mm of braided gold-tone rope, 18k gold PVD on surgical steel, waterproof and tarnish-free. ₹1,199 before the code.',
                 headline='10% off with code NAIRA10'),
            dict(id='W6', slug='fine-print', angle='Spec sheet', hook='THE FINE PRINT. · all good news.', cta='Shop now',
                 why='For the careful buyer. Every numbered line is from the product page, set like a technical drawing.',
                 primary='The fine print, all of it good news. 25mm across. A braided rope of gold-tone strands. 18k gold PVD on surgical stainless steel. Waterproof, tarnish-free, hypoallergenic. Sold as one pair. The Woven Gold Hoops, ₹1,199, with free insured shipping and cash on delivery.',
                 headline='Woven Gold Hoops · ₹1,199'),
            dict(id='W7', slug='pov-real-gold', angle='Native caption', hook='pov: someone asks if · your hoops are real gold', cta='Shop now',
                 why='The "is it real?" moment, answered honestly in caption style.',
                 primary="pov: someone asks if your hoops are real gold. They're 18k gold PVD on surgical steel, waterproof and tarnish-free, and they cost ₹1,199. Tell them or don't. The Woven Gold Hoops, with free insured shipping and cash on delivery.",
                 headline='Woven Gold Hoops · ₹1,199'),
        ]),
]

CTA_GUIDE = [
    ('Shop now', 'P1 · P3 · W1 · W6 · W7', 'The default for a first look at a product. Use it whenever the ad is still telling a story.'),
    ('Learn more', 'P2 · P4 · W3', 'For the explaining angles. It lowers the commitment, so clicks often rise; the add-to-cart check catches it if buyers do not follow.'),
    ('Buy now', 'P7 · W2', 'For angles where the decision happens in the ad itself, like a price shock.'),
    ('Order now', 'P5 · W4', 'For gifting and wedding dates. It reads like placing an order for a day, and suits cash-on-delivery shoppers.'),
    ('Get offer', 'P6 · W5', 'Only on the code angles, so the button repeats the promise on the image.'),
]


def link(s, ad):
    return s['url'] + '?' + UTM.format(camp=s['camp'], id=ad['id'])


def files(s, ad):
    tag = 'prism-sugar' if s['key'] == 'P' else 'woven-red'
    kind = 'feed' if s['key'] == 'P' else 'story'
    return f"{ad['id']}_{tag}_{ad['slug']}_{kind}.jpg"


def ad_name(s, ad):
    return f"AB · {'Prism sugar' if s['key'] == 'P' else 'Woven red'} · {ad['id']} {ad['angle']} · {'Feed 4:5' if s['key'] == 'P' else 'Story 9:16'} · {ad['cta']}"
