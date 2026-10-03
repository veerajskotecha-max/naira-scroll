"""NAIRA PETITE · exhibition poster for WhatsApp (Club Aquarium, Borivali · 3 & 4 October 2026).
Feed/chat 4:5 (1080 x 1350 CSS px) and Status 9:16 (1080 x 1920), both rendered at 2x."""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

P = Path(__file__).resolve().parent
SCR = P.parent
sys.path.insert(0, str(SCR / "camp" / "studio"))
import base

L = base._LOGO
px = py = 65
vw, vh = L["width"] - 2 * px, L["height"] - 2 * py
LOGO = (f"<svg viewBox='{px} {py} {vw} {vh}' class='logo' role='img' aria-label='NAIRA'>"
        f"<path d='{L['letters']}' fill='#F6EFE6' fill-rule='evenodd'/><path d='{L['flower']}' fill='{base.LOGO_BLUSH}' fill-rule='evenodd'/></svg>")

CSS = """
* { margin:0; padding:0; box-sizing:border-box }
html, body { background:#2E4238 }
.canvas { position:relative; overflow:hidden; width:1080px; color:#F6EFE6;
  background: radial-gradient(ellipse 62% 46% at 50% 47%, #4C6A5C 0%, #3A5448 42%, #2E4238 72%, #263830 100%) }
.abs { position:absolute }
.logo { position:absolute; left:50%; transform:translateX(-50%); display:block }
.kick { font-family:'JostF',sans-serif; font-weight:500; letter-spacing:.32em; text-transform:uppercase; color:#E9D9C6; white-space:nowrap }
.head { font-family:'Velista',Georgia,serif; letter-spacing:.02em; white-space:nowrap; color:#F6EFE6; line-height:1 }
.it { font-family:'CormI',Georgia,serif; font-style:italic; color:#F2CFC4; white-space:nowrap; line-height:1.1 }
.center { left:50%; transform:translateX(-50%); text-align:center }
.cut { position:absolute; left:0; width:1080px; filter: drop-shadow(0 22px 34px rgba(10,20,15,.45)) }
.date { font-family:'Velista',Georgia,serif; line-height:.92; color:#E7C27A; white-space:nowrap; letter-spacing:.01em }
.month { font-family:'Velista',Georgia,serif; line-height:1; color:#F6EFE6; white-space:nowrap; letter-spacing:.06em }
.days { font-family:'JostF',sans-serif; font-weight:500; letter-spacing:.28em; color:#E9D9C6; white-space:nowrap }
.rule { height:0; border-top:1.5px solid rgba(246,239,230,.55) }
.venue { font-family:'JostF',sans-serif; font-weight:500; letter-spacing:.16em; color:#F6EFE6; white-space:nowrap }
.place { font-family:'CormI',Georgia,serif; font-style:italic; color:#F2CFC4; white-space:nowrap }
.fade { position:absolute; left:0; width:1080px; background:linear-gradient(to bottom, rgba(38,56,48,0) 0%, rgba(38,56,48,.86) 55%, rgba(38,56,48,.94) 100%) }
.foot { font-family:'Rupee','JostF',sans-serif; font-weight:400; letter-spacing:.14em; color:#F6EFE6; white-space:nowrap }
.foot2 { font-family:'JostF',sans-serif; font-weight:300; letter-spacing:.08em; color:#E9D9C6; white-space:nowrap }
"""


def feed():
    """4:5 for chats and the feed: header on top, date and venue beside her, stall to the bottom edge."""
    return f"""
<div class='canvas' style='height:1350px'>
  <div class='abs' style='left:0;top:0;width:1080px;height:1350px'>{''}</div>
  <div style='position:absolute;top:44px;left:0;width:1080px;height:48px'>{LOGO.replace("class='logo'", "class='logo' style='height:46px'")}</div>
  <div class='abs kick center' style='top:116px;font-size:14px'>Naira Petite &nbsp;·&nbsp; exhibition &nbsp;·&nbsp; this weekend</div>
  <div class='abs head center' style='top:150px;font-size:86px'>SEE IT UP CLOSE.</div>
  <div class='abs it center' style='top:250px;font-size:36px'>come and say hello.</div>
  <img class='cut' src='cutout_trim.png' style='top:332px' alt=''>
  <div class='abs' style='left:716px;top:376px;width:330px'>
    <div class='date' style='font-size:118px'>3 &amp; 4</div>
    <div class='month' style='font-size:46px;margin-top:6px'>OCTOBER</div>
    <div class='days' style='font-size:15px;margin-top:14px'>SATURDAY &amp; SUNDAY</div>
    <div class='rule' style='width:250px;margin-top:20px'></div>
    <div class='venue' style='font-size:22px;margin-top:20px'>CLUB AQUARIUM</div>
    <div class='place' style='font-size:30px;margin-top:4px'>Borivali, Mumbai</div>
  </div>
  <div class='fade' style='top:1170px;height:180px'></div>
  <div class='abs foot center' style='top:1276px;font-size:15px'>NAIRAFLORE.COM &nbsp;·&nbsp; WHATSAPP +91 95615 57935</div>
  <div class='abs foot2 center' style='top:1306px;font-size:13px'>Demi-fine jewellery &nbsp;[ 18k gold coated · rhodium coated ]</div>
</div>"""


def story():
    """9:16 for WhatsApp Status: everything stacked and centred, clear of the top and bottom UI."""
    return f"""
<div class='canvas' style='height:1920px'>
  <div style='position:absolute;top:150px;left:0;width:1080px;height:60px'>{LOGO.replace("class='logo'", "class='logo' style='height:56px'")}</div>
  <div class='abs kick center' style='top:244px;font-size:16px'>Naira Petite &nbsp;·&nbsp; exhibition &nbsp;·&nbsp; this weekend</div>
  <div class='abs head center' style='top:290px;font-size:96px'>SEE IT UP CLOSE.</div>
  <div class='abs it center' style='top:402px;font-size:40px'>come and say hello.</div>
  <div class='abs center' style='top:500px;width:900px'>
    <div class='date' style='font-size:150px'>3 &amp; 4 <span class='month' style='font-size:64px;vertical-align:.32em'>OCTOBER</span></div>
    <div class='days' style='font-size:18px;margin-top:18px'>SATURDAY &amp; SUNDAY</div>
    <div class='rule' style='width:320px;margin:24px auto 0'></div>
    <div class='venue' style='font-size:28px;margin-top:22px'>CLUB AQUARIUM</div>
    <div class='place' style='font-size:38px;margin-top:6px'>Borivali, Mumbai</div>
  </div>
  <img class='cut' src='cutout_trim.png' style='top:880px' alt=''>
  <div class='fade' style='top:1590px;height:330px'></div>
  <div class='abs foot center' style='top:1744px;font-size:17px'>NAIRAFLORE.COM &nbsp;·&nbsp; WHATSAPP +91 95615 57935</div>
  <div class='abs foot2 center' style='top:1776px;font-size:15px'>Demi-fine jewellery &nbsp;[ 18k gold coated · rhodium coated ]</div>
</div>"""


def page(body):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{base.fonts_css()}"
            f"@font-face{{font-family:'CormI';src:url(data:font/woff2;base64,{base.b64(SCR / 'fonts' / 'cormorant-garamond-latin-300-italic.woff2')}) format('woff2');font-style:italic;font-weight:400}}"
            f"{CSS}</style></head><body>{body}</body></html>")


async def main():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        for name, body, h in (("feed", feed(), 1350), ("status", story(), 1920)):
            (P / f"poster_{name}.html").write_text(page(body))
            pg = await b.new_page(viewport={"width": 1080, "height": h}, device_scale_factor=2)
            await pg.goto((P / f"poster_{name}.html").as_uri(), wait_until="networkidle")
            await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(P / f"poster_{name}.png"), clip={"x": 0, "y": 0, "width": 1080, "height": h})
            out[name] = str(P / f"poster_{name}.png")
        await b.close()
    print(out)

asyncio.run(main())
