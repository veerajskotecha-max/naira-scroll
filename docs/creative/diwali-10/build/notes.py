# Diwali 10 (25 Oct 2026): the thinking behind the ten ads, in one place. page.py renders it twice: as README.md and as the review page.
# WINNERS are every Naira ad above 4% CTR (all) with 250+ impressions, read from Meta on 25 Oct 2026 (lifetime). The March–May 2026 ads
# sold lehengas, a different business, and are left out; so are ads under 250 impressions (one shows 50% on 2 impressions).
# Each ad's critique quotes are from the independent review of draft one (scores out of 10).

WINNERS = [  # statics, by CTR; feed = the same picture as a Feed ad, where it ran
 dict(id="molten", line="Poured, not made.", product="Molten Bloom Hoops", place="Story", ctr=7.25, octr=6.69, imp=538, sales=1, roas=1.90,
      img="molten_story.jpg", feed=dict(ctr=6.14, octr=5.12, imp=293),
      why="A craft truth in three words, one gold piece alone on cobalt."),
 dict(id="edible", line="Almost edible.", product="Prism Rivière Bracelet", place="Story", ctr=6.21, octr=5.92, imp=338,
      img="demifine_s7.jpg", feed=dict(ctr=5.61, octr=4.67, imp=1907),
      why="Pastel stones in a bowl of sugared gummies, corrected underneath: “cubic zirconia, not candy.”"),
 dict(id="rangoli_line", line="Rangoli, in a line.", product="Prism Rivière Bracelet", place="Story", ctr=6.10, octr=5.45, imp=771,
      img="rangoli_line_story.jpg", why="The bracelet across three stripes of rangoli colour: a real Indian thing, named and turned."),
 dict(id="rolling", line="It has been rolling for miles.", product="Woven Gold Hoops", place="Story", ctr=6.08, octr=4.73, imp=1332, sales=1,
      roas=0.85, img="hoops_w2.jpg", feed=dict(ctr=5.62, octr=4.65, imp=623),
      why="The braid up close, with a line about how it is made."),
 dict(id="kesar", line="Worth its weight in kesar.", product="Baguette Eternity Band, Ruby", place="Feed", ctr=5.85, octr=4.75, imp=547,
      img="kesar_feed.jpg", why="Saffron threads beside ruby stones: a familiar Indian luxury in the same red, and an idiom turned. Running now."),
 dict(id="woven", line="Woven, not cast.", product="Woven Gold Hoops", place="Story", ctr=5.81, octr=5.37, imp=689, sales=1, roas=1.46,
      img="s1_hoops_story.jpg", why="A craft truth in the shape “X, not Y”, on oxblood."),
 dict(id="anaar", line="No words on the picture", caption="Anaar, pre-peeled.", product="Baguette Tennis Bracelet, Ruby", place="Story",
      ctr=5.49, octr=4.91, imp=7264, sales=15, roas=3.63, img="anaar_story.jpg",
      why="The best seller: ruby baguettes beside a halved pomegranate in the same red. The line lived in the caption."),
 dict(id="rangoli_wear", line="Rangoli you can wear.", product="Prism Cluster Studs, Silver", place="Feed", ctr=5.21, octr=4.28, imp=537,
      img="rangoli_studs_feed.jpg", why="Rangoli powders in the stones’ colours. Running now."),
 dict(id="catalogue", line="Edition Two carousel, 31 pieces", product="The new pieces on models", place="Feed carousel", ctr=5.14,
      octr=4.38, imp=20158, sales=13, roas=2.86, img=None, why="The second-best seller: the whole range, worn. A range sells baskets."),
 dict(id="verdant", line="Up. For once.", product="Verdant Drop Earrings", place="Feed", ctr=4.29, octr=4.29, imp=326,
      img="l6_verdant_feed.jpg", why="Green stones alone on a pale lilac ground, with a two-word line."),
]
REELS = [
 dict(id="reel_where", line="“Where is this from?”", who="Ananaya, wearing a halo ring and a pearl lariat", ctr=11.47, octr=2.36, imp=15091,
      sales=1, roas=1.13),
 dict(id="reel_riya2", line="Riya collab reel, second run", who="Riya", ctr=6.48, octr=2.02, imp=4349, sales=0, roas=None),
 dict(id="reel_riya", line="Riya collab reel", who="Riya", ctr=5.59, octr=1.87, imp=49013, sales=6, roas=0.71),
 dict(id="reel_sonal", line="“Doing all the work”", who="Sonal", ctr=4.39, octr=1.18, imp=12837, sales=1, roas=0.55),
]
PATTERNS = [
 ("A familiar Indian thing in the stone’s colour", "Anaar arils and kesar threads for ruby, rangoli powder and sugared gummies for the "
  "Prism pastels. The eye has to look twice to tell the jewel from the thing."),
 ("A line that names that thing and turns it", "“Worth its weight in kesar.”, “Rangoli, in a line.”, “Rangoli you can wear.”, and the best "
  "seller’s caption, “Anaar, pre-peeled.” A real noun, then a twist."),
 ("A craft truth as “X, not Y”", "“Poured, not made.” (7.25%), “Woven, not cast.” (5.81%), “cubic zirconia, not candy.” (6.21%). Three of "
  "the top six statics."),
 ("One piece, one ground, a lot of air", "Every static winner shows one product on one colour: cobalt, oxblood, blush, pastel stripes."),
 ("Stories beat Feed", "Each time a winning picture ran both ways, the Story did better: 7.25% against 6.14%, 6.21% against 5.61%, "
  "6.08% against 5.62%."),
 ("The best seller had no words on it", "Fifteen sales at 3.6× came from a Story with nothing written on the picture. The picture sells; "
  "the line earns the stop. So every ad here also ships a Story with no text, to test against the one with the line."),
]
FAILED = [
 ("Reels click, statics sell", "The four reels above 4% (4.4% to 11.5% CTR) sent only 1.2% to 2.4% of viewers to the shop and returned "
  "0.55× to 1.13×. People tapped the profile and the sound, not the product. This set is all statics."),
 ("Generic occasion lines", "“RSVP: yes.”, “Black tie.”, “Plans tonight?” and “Make an entrance.” all stayed under 2.2% CTR. They could "
  "sell anything, so they sell nothing: the founder’s “timepass”."),
]
BRAND = [
 "Naira is Indian demi-fine: gold-tone and silver-tone pieces set with cubic zirconia, ₹1,099 to ₹2,399, for urban Indian women who buy for "
 "themselves and for the women around them. It talks like a sharp friend, not a showroom: short, exact, warm, a little wry. It names real "
 "things (anaar, kesar, a toran, Mummy’s saree) instead of reaching for adjectives, and it never shouts: no exclamation marks, no "
 "“stunning”, no “elevate”.",
 "It never pretends to be gold or diamond, and never sells itself as the thing you wear so the family gold can stay at home. At Diwali its "
 "place is not the puja or the gold rate. It is the moments around them: the doorstep, the family photo, card night, the borrowed saree, "
 "the gifts for the cousins. So the campaign is called “Diwali, as it happens”: ten true moments from the five days, one piece in each, in "
 "roughly the order they happen.",
]
VOICE = [
 ("Says", "a real Indian noun, then a turn; under seven words; Cormorant italic on the picture, the product truth in the caption"),
 ("Never says", "real, diamond, waterproof, tarnish-free; “stunning”, “elevate”, “must-have”; anything that could sell any product"),
 ("Never shows", "food you would eat, powders, broken things, religious objects, a prop that needs explaining"),
]

# per ad: the Diwali truth and where it holds, the picture, why the line works, the winners it is built on, the lines it beat, what it
# changed for the next ad, the shoot, open flags. Shoot facts match ledger.json.
ADS = {
 "01": dict(
  truth="In Delhi, Mumbai and Pune anaar is also the fountain firework lit on Diwali night, so the word already sounds like the festival. "
        "And Naira’s best seller is a ruby bracelet beside a halved pomegranate, captioned “Anaar, pre-peeled.”",
  where="The fruit reads everywhere. The firework is a bonus in the North and West: Ahmedabad says kothi, Kolkata tubri, the South flower pot.",
  picture="The necklace closed on a small blush neck form, so it reads as a necklace at a glance. Half a pomegranate is cut face up beside "
          "it, with seven arils rolled toward the neck. The stones are the arils’ exact red, so the eye checks twice. The fruit is cut, not "
          "broken, by the founder’s prop rule.",
  turn="Pomegranate seeds sit packed in rows; a tennis necklace is red stones in a row. “Pre-strung” says the fruit came ready to wear: one "
       "jump, and it answers the winner’s “pre-peeled” for anyone who saw that ad.",
  built=["anaar"], built_note="Same fruit, same red, same caption shape, moved from the bracelet to the necklace.",
  killed=[("Anaar, the quiet kind.", "Draft one, 6 from the critic. Two jumps (fruit, then firework), and the anaar is already the gentle "
           "cracker, so “quiet” barely turns. Beside a no-noise sign-off it starts to sound like an anti-cracker sermon."),
          ("Anaar. Worn, not lit.", "The critic’s line. A good shape, but it only works if you call the firework anaar, and half the "
           "country doesn’t."),
          ("The anaar you hold close.", "A mood, not a turn.")],
  next="The first two frames drew the necklace as a small closed loop lying flat, and it read as the winner’s bracelet. A necklace needs a "
       "neck. From here every piece is shown where it is worn or handed over (a wrist, a palm, a box, a hand at the door) unless its shape "
       "is the point, as in 10.",
  shoot="4 tries, 8 credits. Kept try 3; try 4 asked for a life-size neck form and ran it out of the frame.",
  flags=["The stones read about 1.5× large next to the arils, and four tries did not fix it."]),
 "02": dict(
  truth="Every doorstep rangoli gets stepped on before the night is out: a guest, a child, the delivery boy. Kolam, muggu, alpana: it "
        "happens in every language.",
  where="Pan-Indian.",
  picture="Her wrist rests on the teak threshold just above a fresh rangoli in aqua, pink and butter yellow, the bracelet’s three stone "
          "colours. A trace of pink powder on one fingertip says she drew it a minute ago. The bracelet is the rangoli one step up, out of "
          "reach of feet.",
  turn="“At wrist height” puts the rangoli where it is safe. The line points at the gap between the floor and the wrist, and the picture "
       "shows that gap.",
  built=["rangoli_line", "rangoli_wear"], built_note="The rangoli is the account’s surest colour rhyme for the Prism stones. This is its "
       "third rangoli ad, so it needed a new truth, not a new rangoli.",
  killed=[("The one rangoli nobody steps on.", "Draft one, 7 from the critic. The picture contradicted it: laid on the floor, the bracelet "
           "sat exactly where feet go."),
          ("The rangoli that leaves the house.", "True, but it only says a bracelet is portable.")],
  next="The picture has to act out the line literally. Read every frame as a stranger would: if the line says nobody steps on it, nothing "
       "can lie where feet go. The same check later moved 09 from a ring hanging on a toran to her hand tying it.",
  shoot="2 tries, 4 credits. Try 1 was the floor version.", flags=[]),
 "03": dict(
  truth="Every Diwali photo goes to the family WhatsApp group, and the aunties zoom in, on the jewellery first.",
  where="Pan-Indian. The family group is the real Diwali audience.",
  picture="A night macro of her wrist: eight to ten baguettes razor sharp, every claw visible, the bracelet rolling out of focus at both "
          "ends, fairy-light bokeh behind. The frame is the zoom.",
  turn="It names who is looking, and so turns a product close-up into a moment: she has already passed the inspection.",
  built=["woven", "rolling"], built_note="Both put the making in front of the eye. Here the macro is the proof and the line gives a reason "
       "to look that close.",
  killed=[], kept="Draft one survived: the critic gave it 9 and said to lead the set with it. One warning: never push it to “They won’t "
       "know”, which is a fake-diamond wink and would make Naira the imitation counter.",
  next="A macro is a promise: any flaw at that size and the comments become the aunties. The first frame came back with a broad, hairy wrist "
       "that read as a man’s, because the night light asked for “fine hair” on skin. That cue came out for the reshoot, and the last hand in "
       "the set (09) was cast as carefully as the piece: her hand, her skin, what she is doing.",
  shoot="2 tries, 4 credits.", flags=[], extra="Worth a six-second pinch-zoom Reel later (the critic’s idea, not made)."),
 "04": dict(
  truth="Diwali boxes travel. The same mithai box goes from house to house, and sometimes back to the house that sent it.",
  where="Pan-Indian.",
  picture="A plain ivory mithai box, its lid leaning on its side, lined with crinkled silver foil, and no sweets: the chain lies coiled where "
          "the barfi would be, the toggle ring on top, marigold plaster behind. The box says gift, and there is no food in the frame.",
  turn="It names what everyone does with Diwali boxes and says this one stops here, because it was opened and kept. “Opened” carries the "
       "delight, “not passed on” the joke, in the account’s best line shape: “X, not Y”.",
  built=["molten", "woven", "edible"], built_note="Three of the top six statics turn on “X, not Y”. The box does for gifting what kesar and "
       "anaar do for colour: a thing everyone knows, standing in for the jewel.",
  killed=[("Not the soan papdi.", "Draft one, 6 from the critic. A meme brand pages have run for years, so timepass by the founder’s "
           "definition, and it measures a ₹1,299 chain against a ₹200 re-gift."),
          ("The chain stops here.", "A pun on chain. It gets a groan."),
          ("Nobody re-gifts this one.", "True, but a statement with nothing to see.")],
  next="A true line that everyone has already seen is still timepass. From here every line was checked against Naira’s own past shoots and "
       "the season’s memes. That check is what moved 06 off its poker pun.",
  shoot="1 try, 2 credits.", flags=[]),
 "05": dict(
  truth="On Bhai Dooj the brother gives a gift, usually cash in an envelope, and the sister has been dropping hints for weeks.",
  where="North, West and Bengal (Bhai Dooj, Bhau-beej, Bhai Phonta). Weaker in the South.",
  picture="A man’s big open palm, steel watch and rolled white kurta cuff, holding out the small pair of hoops a little awkwardly, with diya "
          "bokeh behind. His hand is the scale: the hoops look small and fine against it.",
  turn="“Took the hint” is what every sister wants to say. “For once.” is the eye-roll: affection, not complaint.",
  built=["woven", "rolling", "verdant"], built_note="The Woven Gold Hoops are the account’s most proven static, with a sale from each of "
       "their two winners. Same piece, new reason to buy it. “For once.” borrows the cadence of “Up. For once.”",
  killed=[("Bhai took the hint.", "Draft one, 8 from the critic. Right, but it needed the wry tag."),
          ("The hint, ready to forward.", "Says the mechanic out loud."),
          ("Bhai, skip the envelope.", "Dropped before draft one: the red shagun envelope was already shot as “Shagun, upgraded.”")],
  next="The buyer is not the person seeing the ad, so its job is to be forwarded. The primary text ends “Forward this to your brother. "
       "Consider it the hint.”, and the ad stops on 6 Nov so he can still order in time for Bhai Dooj. From here the gifting ads (07, 08) "
       "were written knowing who pays.",
  shoot="1 try, 2 credits.", flags=["The primary text needs your last order date for delivery before Bhai Dooj."]),
 "06": dict(
  truth="Diwali week is card night: teen patti at someone’s house, on a bedsheet or a green baize table.",
  where="Strong in Delhi, Mumbai, Ahmedabad and Marwari Kolkata; weak in South Indian homes.",
  picture="Her hand holds three fanned cards with their backs to the camera (deep red with a gold lattice, no numbers, no faces), the halo "
          "ring on her ring finger, green baize below.",
  turn="At a card table everyone watches your hand, meaning your cards. Here they are watching your actual hand.",
  built=["reel_where"], built_note="Naira’s highest CTR (11.47%) was a reel about being asked where your jewellery is from, and it "
       "showed a halo ring. As a reel it sent only 2.36% to the shop. This puts the same moment, being noticed, in a static.",
  killed=[("Best hand at the table.", "Draft one, 6 from the critic: a poker pun that could run in Las Vegas."),
          ("Best hand at teen patti.", "Fixes the place, keeps the pun."),
          ("Nobody's watching your cards.", "The best alternate. Worth testing against the kept line.")],
  next="The critic flagged the diya behind the cards (a puja lamp in a betting scene) and Meta’s gambling review, and the model had added "
       "poker chips. The chips were painted out and the lamp turned into soft bokeh: no chips, no cash, no card faces. From here each prop "
       "was read for what it means in an Indian home, not only for how it looks. That read is what killed the locker key in 07.",
  shoot="1 try, 2 credits, two retouches.", flags=["Meta can hold card pictures for gambling review. If it does, drop this ad rather than "
       "edit it."], alt="Nobody's watching your cards."),
 "07": dict(
  truth="On Diwali, many daughters wear their mother’s saree. The saree is borrowed; the necklace is hers.",
  where="Pan-Indian. One word changes by region: Amma in the South, Ma in Kolkata.",
  picture="A maroon silk saree with an antique zari border, folded, clearly loved for years. The bold gold chain lies across the pallu with "
          "its one pavé link at the front: new polished gold on old woven gold.",
  turn="Two short sentences, two owners. “Mummy’s” is the warmth; “My” is the purchase. It sells to her without saying “treat yourself”.",
  built=["woven"], built_note="“Woven, not cast.” set woven gold against cast gold on a deep red ground. Here woven zari meets polished "
       "links on maroon silk: the same contrast, now with a story.",
  killed=[("The locker can stay shut.", "Draft one, 6 from the critic, and the set’s biggest brand risk. It cast Naira as what you wear so "
           "the family gold stays safe, which is the imitation counter’s pitch, and in the week India buys gold for the Lakshmi puja, "
           "“keep it shut” also argues with the ritual. Its frame was shot (2 credits) and dropped."),
          ("Stop checking your neck.", "Still about the locker gold."),
          ("Mummy's saree. My earrings.", "The critic’s version. Same truth, but the chain needed a new idea after the locker, and a "
           "chain can lie along a zari border the way earrings can’t.")],
  next="Naira is never instead of the family gold; it is hers. That became the test for the last three: 08 is a gift nobody can compare, "
       "09 hands the evening back to her, and in 10 she wears the only moon.",
  shoot="2 frames, 4 credits (the locker frame was dropped).", flags=[],
  regional="“Amma’s saree. My necklace.” runs in Bengaluru, Chennai and Hyderabad, and “Ma’s saree. My necklace.” in Kolkata. Same "
           "photograph, Feed and Story."),
 "08": dict(
  truth="When you gift the sisters-in-law or the cousins, everyone must get the same thing, or someone compares.",
  where="Pan-Indian.",
  picture="Four raw-silk potlis in a row, ruby, ivory, emerald and lavender, each with its matching pair of huggies in front. One design, "
          "four colours, eight earrings.",
  turn="It names the exact fear, who got the better one, and closes it: same design, so nobody can win. It is what you would say out loud "
       "while handing them over.",
  built=["catalogue"], built_note="The catalogue carousel was the second-best seller because a range sells baskets. Four colours in one "
       "frame is a small catalogue, and with BUY2 and BUY3 four pairs is a basket by design.",
  killed=[("Family diplomacy, in four colours.", "Draft one, 8 from the critic. “Diplomacy” is an idea, not a thing."),
          ("Four bhabhis. No comparisons.", "Assumes four sisters-in-law and narrows the buyer."),
          ("Equal, not identical.", "Clever, but it needs a second read.")],
  next="Name the thing people say out loud, not the idea behind it. That sharpened 09 (“Your turn.” is what someone says at the door) and "
       "10 (a real moon instead of “light”).",
  shoot="1 try, 2 credits.", flags=["Ruby is 12 of the 57 pairs. If it sells out first, the picture still shows it."]),
 "09": dict(
  truth="Diwali prep is the house first: clean, paint, toran, lights, rangoli. The woman who does it gets ready last.",
  where="Pan-Indian, and the most moving truth in the set.",
  picture="Her hand ties the last knot of a fresh mango-leaf toran onto a brass nail at the top of the door frame. The ring’s oval green "
          "stones repeat the leaves just above them.",
  turn="“Toran’s up.” closes the house’s job; “Your turn.” opens hers. The evening hands itself back to her.",
  built=["kesar", "anaar", "verdant"], built_note="The colour rhyme again (kesar and anaar for ruby), here mango-leaf green for the green "
       "stones, as the green drops ran alone on a pale ground.",
  killed=[("The door's done. Your turn.", "Draft one, 8 from the critic. The line was right and the picture wrong: a ring dangling on toran "
           "string is a display, not a moment, and hanging stock on an auspicious toran is borderline.")],
  next="When the line is about her, she has to be in the picture doing the thing. The last ad has no person in it, so the piece itself has "
       "to become the picture.",
  shoot="2 jobs, 2 credits (the first failed on Higgsfield’s side and was not charged).", flags=[]),
 "10": dict(
  truth="Diwali falls on amavasya, the one night with no moon, and the whole country lights the dark itself.",
  where="Pan-Indian.",
  picture="The chunky gold bracelet is closed into a circle high on midnight-indigo plaster, where a moon would hang, its pavé link catching "
          "a flame from outside the frame.",
  turn="On the one night with no moon, hers is the only one out. It flatters the wearer without saying so, and the picture is the line.",
  built=["molten"], built_note="The account’s best static is one gold piece alone on a deep blue ground, the gold doing all the work.",
  killed=[("No moon tonight. Bring your own light.", "Draft one, 5 from the critic: a fact nobody feels, a poster quote, and seven words in "
           "tone-on-tone italic that nobody reads mid-scroll."),
          ("No moon tonight. Over to you.", "Weaker than giving the picture its moon."),
          ("Amavasya, lit by hand.", "Needs a hand in the frame.")],
  next="The set ends on the night itself. For the next campaign: when the piece can become the picture (a circle into a moon), the line only "
       "has to point at it.",
  shoot="1 try, 2 credits. Four-point star glints that looked like CGI were removed from the dark ground; the pavé was left untouched.",
  flags=[]),
}
SCORES = {"01": 8.5, "02": 9.0, "03": 8.8, "04": 9.2, "05": 9.0, "06": 8.8, "07": 9.2, "08": 9.3, "09": 9.0, "10": 9.0}

CRITIQUE = [  # draft one, the critic's score and reason, the line that runs
 ("01", "Anaar, the quiet kind.", 6, "Two jumps, and the fruit was broken", "Anaar, pre-strung."),
 ("02", "The one rangoli nobody steps on.", 7, "The picture puts it where feet go", "Rangoli, at wrist height."),
 ("03", "The aunties will zoom in.", 9, "Instant; lead with it", "Kept"),
 ("04", "Not the soan papdi.", 6, "A meme, so timepass", "Opened, not passed on."),
 ("05", "Bhai took the hint.", 8, "Warm; run it before Dhanteras", "Bhai took the hint. For once."),
 ("06", "Best hand at the table.", 6, "A poker pun; a diya in a betting scene", "All eyes on your hand."),
 ("07", "The locker can stay shut.", 6, "Casts Naira as the stand-in for gold", "Mummy's saree. My necklace."),
 ("08", "Family diplomacy, in four colours.", 8, "An idea, not a thing", "Nobody got the better pair."),
 ("09", "The door's done. Your turn.", 8, "Right line, wrong picture", "Toran's up. Your turn."),
 ("10", "No moon tonight. Bring your own light.", 5, "A poster quote", "The only moon out tonight."),
]
CRITIC = ("Your winners name a real thing and turn it: anaar, kesar, rangoli, poured, woven. The weak lines lean on an idiom or an idea "
          "instead. That is where “Black tie” lived.")
KILLED = [  # ideas dropped before draft one, and why
 ("“Outlasts the phuljhadi.” A crystal bracelet beside a sparkler", "Already shot in October as “The phuljhadi that lasts.”"),
 ("“Bhai, skip the envelope.” Hoops on a red shagun envelope", "Already shot as “Shagun, upgraded.”"),
 ("“Dhanteras steel, technically.” Families buy steel on Dhanteras, and the pieces are surgical steel",
  "Many believe iron or steel should not be bought on Dhanteras, so the joke can read as inauspicious."),
 ("Fairy lights that tangle, beside a tennis bracelet that never does", "Too close to the approved “A ladi that never fuses.”"),
 ("“Dhanteras, minus the gold rate.”", "A price joke, off the brand’s no-discount lane."),
]
PLAN = dict(
 adsets=[("Diwali night", ["01", "02", "03", "06", "09", "10"], "the moments she wears it"),
         ("Gifting", ["04", "05", "07", "08"], "the moments she gives it, gets it or is lent it")],
 audience="Women 18–65 in the nine metros, Feed and Stories, as in the October tests.",
 budget="₹1,000 a day for each ad set from 29 Oct to 10 Nov, about ₹26,000 in all. At the ₹350–800 CPMs the account paid in October, that "
        "gives every file at least 1,000 impressions.",
 ab="Run the Story with the line and the Story with no text side by side. After about 1,000 impressions each, keep the one with the "
    "better outbound CTR.",
 kill="Pause any file under 2% CTR after 1,000 impressions and move its budget to the two best.",
 stock=[("01", "Baguette Tennis Necklace, Ruby", 20), ("03", "Baguette Tennis Bracelet, Crystal", 29), ("08", "Baguette Huggies, Ruby", 12)],
)
QUESTIONS = [
 ("“Devyani”", "I read “Devyani this camp later” as “Diwali ni camp”, the Diwali campaign, to run later. If you meant a creator or model "
  "called Devyani, send her photos and I will plan the ten around her."),
 ("Bhai Dooj order date", "Ad 05 stops on 6 Nov so brothers can order in time. What is the last order date that still arrives before Bhai "
  "Dooj? I will add it to its primary text."),
 ("Regional saree ads", "Meta sets places per ad set, so running Amma’s (Bengaluru, Chennai, Hyderabad) and Ma’s (Kolkata) means two more "
  "small ad sets. Run them, or run Mummy’s everywhere?"),
 ("The necklace picture", "In 01 the stones read about 1.5× large next to the arils after four tries. Keep it, or drop 01 and give its "
  "budget to 03?"),
 ("Card night", "If Meta holds 06 for gambling review, drop it?"),
]
