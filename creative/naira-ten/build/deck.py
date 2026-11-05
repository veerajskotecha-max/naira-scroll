"""The Naira Ten: copy, links, techniques and plan for the ten concept ads. Facts are from the live nairaflore.com listings
and the Shopify stock sheet on 4 November 2026."""
import json, sys
from pathlib import Path
from kit import LIVE, STOCK, LINK, UTM, OFFER, COLL, OUT, T, inr

OFFER_LONG = ("Buy 2 pieces for 10% off or 3 for 20% off with codes BUY2 and BUY3 at checkout. "
              "Free insured shipping and cash on delivery across India.")
ADS = [
    dict(id='A01', slug='i-do', coll='rings', layer='Desire', piece='cushion-halo-ring',
         hook='I do. Say it with a ring that adjusts.',
         technique='Typographic swap', lineage='The product rewrites the word, as in KFC "FCK" (Mother London, Cannes Gold Lion 2018) and McDonald\'s "Follow the Arches" (Cossette, Cannes Outdoor Grand Prix 2018).',
         edit='The ring, generated upright from the product photo and cut out, is set as the O of Velista at the exact height of the letter. The letters cast the same contact shadow as the ring, on sindoor-red paper grain.',
         headline='Cushion Halo Ring · ₹1,099',
         primary='I do. Say it with a ring that adjusts. An 8mm clear stone in four claws inside a 12mm cushion pavé halo, rhodium PVD on surgical steel, open at the back so it fits US 5 to 9. No ring size, no guessing. The Cushion Halo Ring, ₹1,099.\n' + OFFER_LONG,
         why='Engagement season, and fit is the first doubt when buying a ring online. The judge called this ring the most convincing hand of the Naira Twenty (8.05); this card gives it a headline nobody scrolls past.'),
    dict(id='A02', slug='repeat-the-hoops', coll='earrings', layer='Desire', piece='woven-gold-hoops',
         hook='Repeat the hoops. Not the outfit.',
         technique='Pop-art repetition', lineage='Warhol\'s screenprint grid, the language of Absolut Warhol (1985): one image repeated until the repetition is the point.',
         edit='One library portrait screenprinted nine times in the colours of the wedding\'s functions, with a black key layer and deliberate misregistration. The Woven Gold Hoops are masked out and left as the only photograph in every panel.',
         headline='Woven Gold Hoops · ₹1,199',
         primary='Roka, sagai, mehendi, haldi, sangeet, cocktail, pheras, vidaai, reception. Nine outfits, one pair of hoops. The Woven Gold Hoops are 25mm of braided gold rope, 18k gold PVD on surgical steel and waterproof, so the gold holds its colour through every function. ₹1,199.\n' + OFFER_LONG,
         why='Haldi yellow was the strongest thumb-stop of the judged round (8.07) and the hoops are the account\'s most-bought single piece. Repeating the hoops, not the outfit, is the honest reason to buy one good pair for a nine-function week.'),
    dict(id='A03', slug='periodic-table', coll='all', layer='Inform', piece=None,
         hook='The Periodic Table of Naira. Every piece is made of Au or Rh.',
         technique='Information design, colour-coded', lineage='The catalogue grid, the account\'s best format, set as the periodic table: collections as element groups, and the two real elements every piece is coated in.',
         edit='Ten shop photographs cropped as element tiles, each with a symbol, number and price; columns in the collection colours (Haldi, Sindoor, Neelam, Rani). Au and Rh are rendered as brushed-metal tiles with their real atomic numbers and weights.',
         headline='121 pieces in stock · from ₹599',
         primary='Every piece is made of Au or Rh: 18k gold or rhodium, bonded to surgical steel by PVD, so it does not wear off like plating. Ten pieces from four collections, from the ₹799 Brushed Gold Huggies to the ₹2,399 Prism Rivière Bracelet. 121 pieces in stock, from ₹599.\n' + OFFER_LONG,
         why='Catalogue grids and carousels at current prices are the only format in the account with a cost per purchase under ₹520 (ROAS 2.6 to 2.7). This one is the same proven format, made into something people screenshot.'),
    dict(id='A04', slug='anatomy', coll='earrings', layer='Inform', piece='verdant-circlet-studs',
         hook='Anatomy of a compliment.',
         technique='Craft proof as engineering drawing', lineage='The brand brief\'s first territory: nobody in the category argues craft. A cyanotype technical drawing with numbered callouts, a dimension line and a title block.',
         edit='The stud, generated front-on from the product photo and cut out, is drawn on a blueprint grid with construction lines, five callouts taken from the listing, a 16.8mm dimension line and a title block where the price sits like a part number.',
         headline='Verdant Circlet Studs · ₹1,099',
         primary='Anatomy of a compliment. 01 18k gold PVD on surgical steel. 02 A 10mm cushion-cut green CZ. 03 An open circlet of clear stones. 04 A 6mm shell pearl inside the circle. 05 Gold star points. 16.8mm tall, waterproof. The Verdant Circlet Studs, ₹1,099.\n' + OFFER_LONG,
         why='The deepest-stocked piece in the warehouse (80 pairs). Detail callouts answer "what am I actually getting" before the click, which is the question a ₹1,099 stud has to answer.'),
    dict(id='A05', slug='dance-floor', coll='bracelets', layer='Desire', piece='prism-riviere-bracelet',
         hook='The dance floor is 18 cm long.',
         technique='Miniature world', lineage='Tabletop miniature photography (the Tatsuya Tanaka school): ordinary objects become sets for tiny people.',
         edit='Generated from the product photo: a 1:87 sangeet of hand-painted figurines dancing on the stones, a dhol player on the clasp, fairy lights strung between toothpicks, on rani-pink paper. The copy sits on a darkened floor of the same pink.',
         headline='Prism Rivière Bracelet · ₹2,399',
         primary='The dance floor is 18cm long. Aqua, pink and yellow cushion-cut stones, each 5mm and each in its own pavé halo, linked in one line and closed with a fold-over clasp that keeps it flat while you dance. Rhodium PVD on surgical steel. The Prism Rivière Bracelet, ₹2,399.\n' + OFFER_LONG,
         why='Prism and rainbow pieces carry the highest CTR of any static in the account (3.1 to 3.2%), and the sangeet line scored 8.18 with the judge. 63 in stock.'),
    dict(id='A06', slug='pick-your-shade', coll='necklaces', layer='Desire', piece='baguette-tennis-necklace',
         hook='Pick your shade.',
         technique='Paint-chip swatches', lineage='The colour-swatch vernacular: the product sold as a palette, one price for every shade.',
         edit='Three library shots of the same model in ruby, crystal and emerald, set as paint chips with a colour band, a shade code and a label, dropped at slight angles with real shadows on neelam blue.',
         headline='Baguette Tennis Necklace · ₹2,099',
         primary='Pick your shade. The Baguette Tennis Necklace comes in ruby, crystal and emerald, the same ₹2,099 for each: a 36cm line of crosswise baguettes, each held at its corners by gold claws, so it sits close at the base of the neck. 18k gold PVD on surgical steel.\n' + OFFER_LONG,
         why='All three shades are in stock (ruby 20, crystal 29, emerald 20). Showing the choice on one card turns "do I like it" into "which one", which is a better question to leave a shopper with.'),
    dict(id='A07', slug='fifty-cm', coll='necklaces', layer='Inform', piece='toggle-link-chain', carousel=True,
         hook='This is 50 cm.',
         technique='Seamless panorama carousel', lineage='The brand brief\'s "actual size" territory: 42% of shoppers judge size from the image alone. One photograph runs across three cards, so the swipe measures the chain.',
         edit='One generated flat-lay of the unclasped chain on linen, split across three 4:5 cards, with a drawn tailor\'s tape from 0 at the T-bar to 50 at the ring. The story runs the same tape vertically.',
         headline='Toggle Link Chain · 50cm · ₹1,199',
         primary='This is 50cm. Laid flat next to a tailor\'s tape, T-bar to ring: long flat paperclip links 4mm wide and a 15mm toggle you can wear at the front or turned to the side. 18k gold PVD on surgical steel. The Toggle Link Chain, ₹1,199.\n' + OFFER_LONG,
         why='The deepest-stocked necklace (79 units). Length is the commonest necklace return reason; a ruler answers it before the order.'),
    dict(id='A08', slug='hugs-and-kisses', coll='bracelets', layer='Desire', piece='kiss-knot-bangle',
         hook='Hugs and kisses, on one wrist.',
         technique='Visual pun on a found object', lineage='The brand library\'s chalk board, finished: the bangle is the O (a hug) and its knot is the X (a kiss), so O wins the diagonal straight through it.',
         edit='Hand-drawn chalk added over the library photograph: the winning line, and "hug" and "kiss" in Kalam with arrows, through a chalk-grain filter so they match the board. The story floats the slate on a blurred copy of itself.',
         headline='Kiss Knot Bangle · ₹1,199',
         primary='Hugs and kisses, on one wrist. The Kiss Knot Bangle is a flexible ribbed coil whose two ends cross under one polished X, so it reads as both. It slips over the hand. In gold or silver, 18k gold or rhodium PVD on surgical steel. ₹1,199.\n' + OFFER_LONG,
         why='A gifting line that does not need a discount to work. 36 in stock (gold 17, silver 19).'),
    dict(id='A09', slug='two-peas', coll='rings', layer='Convert', piece='verdant-eternity-band',
         hook='Two peas in a pod.',
         technique='Visual idiom', lineage='An idiom staged literally, in the saturated still-life style the account\'s best Stories use: pea green on hot pink.',
         edit='Generated from the product photo: two bands around peas in an open pod. For the story, a loose pea was painted out and the paper extended up and down with its own grain.',
         headline='Two rings · ₹1,978 with BUY2',
         primary='Two peas in a pod. One Verdant Eternity Band for you, one for your sister: oval green stones in scalloped pavé all the way round, rhodium PVD, open at the back so each fits US 5 to 9. ₹1,099 each, or two for ₹1,978 with code BUY2. Free insured shipping and cash on delivery across India.',
         why='Sisters and bridesmaids buy in pairs at weddings. The card does the Buy 2 maths (₹2,198 to ₹1,978) so the offer is a number, not a code. 58 in stock.'),
    dict(id='A10', slug='the-799-pair', coll='earrings', layer='Convert', piece='brushed-gold-huggies',
         hook='₹799. The pair.',
         technique='Knockout type, price as material', lineage='Price as the design, as in Penny "Price Packs" (Serviceplan, Cannes Print & Publishing Grand Prix 2025). Here the price is cut out of the product\'s own brushed surface.',
         edit='"₹799" set in Rozha One and filled with a macro of the real huggie\'s satin-brushed band, with a soft specular sweep and a fine edge highlight; the library cut-out of the pair sits below on a warm black ground.',
         headline='Brushed Gold Huggies · ₹799 the pair',
         primary='₹799, the pair. The Brushed Gold Huggies are 14 by 9.8mm with a wide 6mm band in a satin-brushed finish, so they read chunky without the weight. 18k gold PVD on surgical steel, waterproof.\n' + OFFER_LONG,
         why='"The ₹799 pair" was the judge\'s clearest entry-price hook (8.20). It is the lowest-priced hero in stock (32 pairs), so it carries the price argument for the whole range.'),
]
PLAN = dict(
    name='Naira · The Ten · Shop All + collections · ₹1,000/day · Nov 2026',
    objective='Sales (OUTCOME_SALES), conversion event Purchase, website',
    launch='10:10 IST on launch day. If The Guest List is already running, start The Ten after its day-7 review, or run it as a second campaign at the same budget.',
    budget='₹1,000 per day, campaign budget (CBO)',
    adsets=[
        dict(name='Cold · all India · women 22 to 45 · Advantage+ audience', budget='₹700/day (minimum ₹600)', ads=['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08']),
        dict(name='Warm · site visitors 30d, Instagram engagers 60d, add to cart 14d, purchasers excluded', budget='₹300/day, frequency cap 2 per 7 days', ads=['A09', 'A10', 'A03', 'A07']),
    ],
    kpis=['Link CTR at or above 2.5%', 'Cost per link click at or below ₹20', 'Cost per purchase at or below ₹600', 'Purchase ROAS at or above 2.0'],
    rules=['Judge nothing before 1,500 impressions or 48 hours.', 'Link CTR under 1.2% at 1,500 impressions: switch the ad off.',
           '₹1,500 spent with no purchase: switch it off and move the budget to the best ad in its layer.',
           'Day 7: keep the five best by cost per purchase.', 'Every Monday: check hero stock; any hero under 15 units is swapped for the next piece in its collection.'],
)


def build():
    out = []
    for a in ADS:
        p = LIVE[a['piece']] if a['piece'] else None
        files = sorted(f.name for f in OUT.glob(f"{a['id']}_*.jpg") if 'pano' not in f.name)
        out.append(dict(a, collection=COLL[a['coll']]['label'], colour=COLL[a['coll']]['hex'], colour_name=COLL[a['coll']]['name'],
                        link=LINK[a['coll']] + '?' + UTM.format(id=a['id']), description='Free insured shipping · Cash on delivery', cta='SHOP_NOW',
                        piece_title=p['title'] if p else None, price=p['price'] if p else None, stock=STOCK.get(a['piece']) if p else None, files=files))
    json.dump(dict(plan=PLAN, offer=OFFER, ads=out), open(OUT / 'deck.json', 'w'), indent=1, ensure_ascii=False)
    return out


if __name__ == '__main__':
    d = build()
    for a in d: print(a['id'], a['collection'], a['piece_title'], a['price'], a['stock'], len(a['files']), 'files', len(a['primary']), 'chars')
