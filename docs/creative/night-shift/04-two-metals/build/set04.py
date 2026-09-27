# -*- coding: utf-8 -*-
"""SET 04 — TWO METALS. Gold and rhodium worn together, on one body part per card. The headline is split
letter by letter, warm on the left half of every glyph and cool on the right, so the type does what the
pieces do. Anchored by the Heartbead, the one piece in the catalogue that is both metals at once."""
from core import *
SET=dict(slug="04-two-metals",title="Two Metals",n=4)
S4=f"{ROOT}/s04"
TOK={"feed":dict(PLATE="760px",HEAD="150px"),"story":dict(PLATE="1180px",HEAD="176px")}
GOLD="linear-gradient(90deg,#7A5616 0%,#C9A24A 24%,#8F6A1E 49.9%,#4E535A 50.1%,#B7BCC3 74%,#5F656C 100%)"
CSS="""
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#222}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.plate .veil{position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(0deg,#F1EBE1,rgba(241,235,225,0))}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) - 24px)}
.h{font-family:'Velista';font-weight:500;line-height:.9;letter-spacing:-.005em;text-transform:uppercase;white-space:nowrap;filter:drop-shadow(0 1px 0 rgba(241,235,225,.9))}
.h span{background:GOLD;-webkit-background-clip:text;background-clip:text;color:transparent;display:inline-block}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:6px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:0 28px;margin-top:22px}
.pair .col{border-top:2px solid var(--ink);padding-top:10px}
.pair .col.g{border-color:#B98A2E}.pair .col.s{border-color:#8E939A}
.pair .lab{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.14em;text-transform:uppercase;margin-bottom:8px}
.pair .col.g .lab{color:#8A6420}.pair .col.s .lab{color:#5F646B}
.pair .nm{font-family:'Jost';font-weight:600;font-size:var(--NAME);letter-spacing:.06em;text-transform:uppercase;line-height:1.1}
.pair .sp{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase;margin-top:6px;color:var(--mute);line-height:1.4}
.pair .pr{font-family:'Jost';font-weight:600;font-size:calc(var(--PRICE)*.82);margin-top:8px}
.foot{grid-template-columns:1fr auto}
.foot .tot{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.foot .tot b{font-family:'Jost';font-weight:600;font-size:var(--PRICE);letter-spacing:.01em;color:var(--ink);display:block;margin-top:4px}
""".replace("GOLD",GOLD)
def split(text): return "".join(f'<span>{E(ch)}</span>' if ch!=" " else " " for ch in text)
def render(c,fmt):
    plate=f'{S4}/plate_{c["plate"]}_{fmt}.jpg'
    g,s=c["gold"],c["silver"]
    def col(kind,sku,spec,lab):
        return (f'<div class="col {kind}"><div class="lab">{lab}</div><div class="nm">{name(sku)}</div><div class="sp">{E(spec)}</div>'+(f'<div class="pr">{price(sku)}</div>' if not c.get("one") else "")+'</div>')
    cols=col("g",g[0],g[1],"gold · 18k gold tone")+col("s",s[0],s[1],"silver · rhodium")
    total=ROWS[g[0]]["price"]+ROWS[s[0]]["price"] if not c.get("one") else ROWS[g[0]]["price"]
    tot=f'<div class="tot">{"one piece, both metals" if c.get("one") else "the pair"}<b>{rupees(total)}</b></div>'
    W,H=FORMATS[fmt]; pad=52 if fmt=="feed" else 64; fs=fit("TWO METALS.",W-2*pad,-0.005)
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"><div class="veil"></div></div>'
            f'{top("NAIRA PETITE · TWO METALS",c.get("topcolor",IVORY))}'
            f'<div class="block"><div class="h" style="font-size:{fs:.0f}px">{split("TWO METALS.")}</div><div class="sub">{E(c["sub"])}</div><div class="pair">{cols}</div></div>'
            f'<div class="foot">{tot}<span class="cta solid">{E(c["cta"])}</span></div>')
CREATIVES=[
 dict(id="M1",file="one-bracelet",plate="bracelet",sub="(one bracelet. it never had to choose.)",one=True,
      gold=("YF5215","toggle bar and ring · 15mm heart"),silver=("YF5215","6mm mirror steel spheres"),skus=["YF5215"],hero=True,
      cta="SHOP BRACELETS →",render=render,pos="50% 40%",topcolor=INK,claims=[("YF5215","15mm heart · 6mm spheres")]),
 dict(id="M2",file="one-hand",plate="hand",sub="(one hand. index and middle.)",
      gold=("WR12518B","4 bands · 2 pavé, 2 plain · open back"),silver=("WR10170K7","8mm round brilliant · cushion halo"),skus=["WR12518B","WR10170K7"],
      cta="SHOP RINGS →",render=render,pos="50% 45%",topcolor=INK,claims=[("WR10170K7","8mm round brilliant")]),
 dict(id="M3",file="one-neck",plate="neck",sub="(one neck. the silver sits higher.)",
      gold=("YF5143","4mm paperclip · 50cm · toggle at the front"),silver=("YF8439-SLV","2mm snake chain · 10mm cushion cz · 40cm"),skus=["YF5143","YF8439-SLV"],
      cta="SHOP NECKLACES →",render=render,pos="50% 55%",topcolor=IVORY,claims=[("YF5143","4mm · 50cm"),("YF8439-SLV","2mm · 10mm · 40cm")]),
 dict(id="M4",file="one-ear",plate="ear",sub="(one ear. two piercings.)",
      gold=("E14776S","12mm huggie · brushed satin"),silver=("E20997C","9mm shell pearl · pavé bow · 18mm"),skus=["E14776S","E20997C"],
      cta="SHOP EARRINGS →",render=render,pos="50% 50%",topcolor=IVORY,claims=[("E14776S","12mm"),("E20997C","9mm · 18mm")]),
 dict(id="M5",file="one-design",plate="domes",sub="(one design. cast twice.)",
      gold=("JDR0104337","granule dome · no stones · open back"),silver=("JDR0104337-S","pavé dome · open back"),skus=["JDR0104337","JDR0104337-S"],
      cta="SHOP RINGS →",render=render,pos="50% 50%",topcolor=INK),
]
