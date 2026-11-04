# Toggle Link Chain: crazy hooks, checked clasps (4 Nov 2026)

The ask: high-CTR, crazy eye-catching ads for the Toggle Link Chain, planned properly, with the toggle checked in every
photo and corrected where it is wrong; then, after research into what makes ad hooks work, ten crazy variations, or
however many pass the test.

Nothing here has been uploaded to Meta or changed on Shopify.

## The product, as it is today

Toggle Link Chain, YF5143, ₹1,199 on Shopify (compare-at ₹2,900), 79 in stock. 50 cm of 4 mm open paperclip links in
gold tone; a clasp of about 15 mm worn at the front or the side: a thick spring-gate ring (gate, collared ends, a push-pin
nub at 3 o'clock) and, on the other chain end, a short pave bar with one line of tiny clear stones that passes through
the ring. One open question for the owner: the cube listing photo shows the pave piece as an oval hoop on the ring,
while the worn and velvet listing photos and the description show a straight bar. The ads draw the bar.

## What was checked (`build/audit.json`)

- **The product page.** The generated worn photo added on 21 Oct (third in the gallery) shows a plain closed ring with
  no gate or push-pin, and a curved pave hoop several stones wide instead of the bar. It should be replaced.
- **The five Toggle ads live on Meta.** Four show the wrong clasp: a plain ring (plate, fork, Story) or a hoop set with
  black and clear stones (spool). All five still say ₹1,099 (Shopify: ₹1,199), "anti-tarnish", and "codes BUY2 and BUY3
  at checkout" (the store applies the discount with no code). The hook ad (F17) is the closest.
- **19 earlier Toggle photos.** 4 pass (performance worn, colour 51, crazy3 night, colour-camps sage), 4 have small
  defects, 11 fail; most failures draw a classic T-bar or a plain ring. The live Diwali 04 ad also says ₹1,299.

## The research

Naira's own numbers first (Diwali 10 analysis): the winners above 4% CTR turn a familiar Indian thing, use "X, not Y"
craft truths, show one piece on one ground, and run better as Stories. Generic occasion lines stayed under 2.2%. On
this chain: "Paperclip, promoted." 7.3% (41 impressions), the VK Story 4.4%, "Out by noon." 1.6%.

From the web (vendor research, directional):
- [Admetrics, five static formats outperforming video in 2026](https://www.admetrics.io/post/five-static-ad-formats-outperforming-video-in-2026): the anti-ad, one core idea, the clever one, the checkerboard, the platform native.
- [Taylor Sicard, DTC ad formats 2026](https://taylorsicard.com/blog/dtc-ad-formats-2026): in 243 ads, meme/low-fi statics failed least (58.8%), native/editorial next (64.3%); comparisons against a named rival failed most (87.5%).
- Curiosity hooks work best with a moderate gap and a quick payoff; lo-fi devices (sticky notes, handwriting) are the usual pattern interrupts ([Trendtrack](https://www.trendtrack.io/blog-post/best-performing-ad-hooks), [Motion](https://motionapp.com/library/hooks/tactics/curiosity)).
- In India, discount hooks are at very high saturation ([Quickads jewelry report](https://www.quickads.ai/jewelry-report)).

## The hook tests (`build/crazy.py`): ten built, seven kept

Review board: https://claude.ai/artifact/2aan2pM7c1CDncPSb6zm9o (private to the owner until shared).

Higgsfield had 1.71 credits, so these use only the four photos that passed the clasp audit. The crazy is in the hook
and the format; five share one photo so they test the hook alone. Each is a Feed card and a Story; captions in
`captions.json`.

| Key | Hook | Format | Photo |
|---|---|---|---|
| X01 | Kabhi front. Kabhi side. | The clever one: a Bollywood title turned into a product truth | worn |
| X02 | Note to self: the clasp goes in FRONT. | Lo-fi: a sticky note and a marker arrow | worn |
| X03 | Unpopular opinion: the clasp is the best part of a necklace. | Platform-native: a plain post from Naira | sage |
| X04 | Looks expensive. Isn't. | Price reveal, said dry · **cut** (the rose read as the hero; the chain read as a bracelet) | night |
| X05 | Gem clip, promoted. | Look-alike: what India calls a paperclip | clips |
| X06 | Tap the link. | Platform-native: the hyperlink pun · **cut** (a fake hyperlink) | night |
| X07 | Anatomy of a show-off clasp | Lo-fi: marker scribbles on the product · **cut** (the marks kept landing on the metal after two rounds; 5/10) | clips |
| X08 | Goes with: | Platform-native: a checklist note | worn |
| X09 | The clasp is the point. | The checkerboard: four panels | worn, sage |
| X10 | No more 'hook laga do'. | Problem, solved, in the words people say | worn |

## The fifteen with new photos (`build/plan.json`, `build/shots.json`)

The planned set with new Higgsfield frames, judged independently (`build/judge.json`), waits for about 50 credits. The
4 Nov pilot (`T01`) drew the clasp right except for a two-stone-wide bar and about 1.5x size against the neck, and the
shot briefs were tightened for both.

## Judging (`build/judge_crazy.json`)

Three independent rounds. Final scores out of 10: X10 9, X08 8.5, X02 8, X03 7.5, X05 7.5, X01 7, X09 6. Where the judge
would spend first: X10 (Feed), X08 (Feed), X03 (Feed). X01, X02, X08 and X10 share the worn photo, and X01 and X10 are the
same picture with different words, so keep those two in separate ad sets.
