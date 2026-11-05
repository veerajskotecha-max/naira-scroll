"""Ad 9 · Two peas in a pod — the Verdant Eternity Band, twice, in an open pea pod (visual idiom). Sister rings for the
wedding, with the Buy 2 maths on the card. Generated from the product photo; the story extends the flat pink paper."""
from kit import *

IMG = T / 'img'
PH = IMG / 'n10.png'                         # 1856 x 2304
SC = 1080 / 1856
TOP_PINK, BOT_PINK = '#FD7BBE', '#EB70A2'
pair = 2 * LIVE['verdant-eternity-band']['price']; deal = round(pair * 0.9)
CSS = f"""
.card{{background:linear-gradient({TOP_PINK}, {BOT_PINK})}}
.ph{{position:absolute;left:0;width:1080px;background-size:cover;background-position:center}}
.ph.fade{{-webkit-mask-image:linear-gradient(transparent 0, #000 60px, #000 calc(100% - 60px), transparent 100%)}}
.hd{{position:absolute;left:64px;color:#3B0D1F}}
.hd .eb{{font-size:19px;opacity:.85}}
.hd h1{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:100px;line-height:.95;margin-top:14px;letter-spacing:.01em;color:#FFFFFF;text-shadow:0 2px 14px rgba(120,10,50,.18)}}
.hd p{{font-size:38px;line-height:1.12;margin-top:16px;color:#3B0D1F}}
.ft{{position:absolute;color:#3B0D1F}}
.ft .row{{display:flex;align-items:baseline;gap:14px}}
.ft .price{{font-family:'RupeeV','Velista',serif;font-size:66px;line-height:1;color:#FFFFFF}}
.ft .each{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:22px;letter-spacing:.06em}}
.ft .deal{{display:inline-block;margin-top:14px;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:17px;letter-spacing:.14em;text-transform:uppercase;background:#3B0D1F;color:#FFFFFF;padding:12px 14px}}
.ft .deal s{{opacity:.6;text-decoration-thickness:2px}}
"""


def body(story):
    if story:
        top = 300
        return ''.join([
            f"<div class='ph' style='top:0;height:1920px;background-image:url({uri(IMG / 'a9_story.jpg')})'></div>",
            tab('rings', y='top:300px', radius='29px', invert=True),
            f"<div class='hd safe' style='top:340px;width:600px'><div class='eb eyebrow'>RINGS · VERDANT ETERNITY BAND</div>"
            f"<h1>TWO PEAS<br>IN A POD.</h1><p class='serif-i'>One for you,<br>one for your sister.</p></div>",
            f"<div class='ft safe' style='left:560px;top:1392px;width:460px'><div class='row'><span class='price'>₹1,099</span><span class='each'>EACH</span></div>"
            f"<span class='deal'>Two for <s>{inr(pair)}</s> {inr(deal)} · BUY2</span></div>",
            f"<div class='safe' style='position:absolute;left:64px;top:1470px'>{logo(86, '#3B0D1F', '#FFFFFF')}</div>",
        ])
    return ''.join([
        f"<div class='ph' style='top:0;height:1350px;background-image:url({uri(PH)})'></div>",
        tab('rings', y='top:0', invert=True),
        f"<div class='hd safe' style='top:70px;width:600px'><div class='eb eyebrow'>RINGS · VERDANT ETERNITY BAND</div>"
        f"<h1>TWO PEAS<br>IN A POD.</h1><p class='serif-i'>One for you, one for your sister.</p></div>",
        f"<div class='ft safe' style='left:64px;top:1150px;width:600px'><div class='row'><span class='price'>₹1,099</span><span class='each'>EACH</span></div>"
        f"<span class='deal'>Two for <s>{inr(pair)}</s> {inr(deal)} · code BUY2</span></div>",
        f"<div style='position:absolute;right:64px;bottom:50px'>{logo(86, '#3B0D1F', '#FFFFFF')}</div>",
    ])


render([('A09_two-peas_feed', doc(*FEED, CSS, body(False)), FEED), ('A09_two-peas_story', doc(*STORY, CSS, body(True)), STORY)])
print('pair', pair, 'deal', deal)
