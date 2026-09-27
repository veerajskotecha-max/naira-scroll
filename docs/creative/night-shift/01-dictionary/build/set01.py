# -*- coding: utf-8 -*-
"""SET 01 — THE DICTIONARY. Five craft words the customer meets on a listing and nobody defines. Dictionary-page
typography over a macro plate of the piece that demonstrates the word. Claims the unclaimed craft vocabulary lane."""
from core import *
SET=dict(slug="01-dictionary",title="The Dictionary",n=1)
S1=f"{ROOT}/s01"
TOK={"feed":dict(HEAD="168px",DEF="30px",PLATE="620px",STRIP="104px"),"story":dict(HEAD="186px",DEF="35px",PLATE="940px",STRIP="124px")}
CSS="""
.top{top:calc((var(--STRIP) - 24px)/2)}
.plate{position:absolute;left:0;right:0;top:var(--STRIP);height:var(--PLATE);overflow:hidden;background:#E9E2D6}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.entry{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--STRIP) + var(--PLATE) + 30px)}
.rh{display:flex;justify-content:space-between;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.12em;text-transform:uppercase;color:var(--mute);border-bottom:1px solid var(--ink);padding-bottom:10px}
.hw{display:flex;align-items:baseline;gap:24px;margin-top:16px}
.hw .w{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.9;letter-spacing:-.01em}
.hw .pr{font-family:'JetBrains Mono';font-size:calc(var(--MONO)*1.3);letter-spacing:.08em;color:var(--mute)}
.hw .pos{font-family:'Cormorant Garamond';font-style:italic;font-size:calc(var(--DEF)*1.05);color:var(--mute)}
.sense{display:grid;grid-template-columns:auto 1fr;gap:0 16px;margin-top:18px;max-width:64ch}
.sense b{font-family:'Jost';font-weight:600;font-size:var(--DEF)}
.sense p{font-family:'Jost';font-weight:400;font-size:var(--DEF);line-height:1.3;text-wrap:pretty}
.ety{font-family:'Cormorant Garamond';font-style:italic;font-size:calc(var(--DEF)*1.02);line-height:1.25;margin-top:12px;max-width:60ch;text-wrap:pretty}
.foot .see{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-bottom:8px}
"""
def render(c,fmt):
    W,H=FORMATS[fmt]; sk=c["sku"]
    plate=f'{S1}/plate_{c["plate"]}_{fmt}.jpg'
    return (f'{top(c["guide"],INK)}'
            f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>'
            f'<div class="entry"><div class="rh"><span>The Naira dictionary</span><span>entry {c["n"]:02d} of 05</span></div>'
            f'<div class="hw"><span class="w">{E(c["word"])}</span><span class="pr">{E(c["pron"])}</span><span class="pos">{E(c["pos"])}</span></div>'
            f'<div class="sense"><b>1.</b><p>{E(c["def"])}</p></div>'
            f'<div class="ety">{E(c["ety"])}</div></div>'
            f'<div class="foot"><div><div class="see">see:</div><div class="name">{name(sk)}</div><div class="spec">{E(c["seehow"])}</div></div>'
            f'<div><div class="price">{price(sk)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="E1",n=1,file="pave",word="pavé",pron="pa·VAY",pos="n.",plate="pave",sku="B00681C",guide="pavé · pear",
      def_="Stones set so close together that the metal beneath them disappears, and the surface reads as light rather than gold.",
      ety="From the French pavé, “paved”.",seehow="each stone in its own pavé halo",cta="SHOP BRACELETS →",render=render,
      claims=[("B00681C","5mm cushion CZ in pavé halos")]),
 dict(id="E2",n=2,file="baguette",word="baguette",pron="ba·GET",pos="n.",plate="baguette",sku="WE14387B",guide="baguette · bail",
      def_="A long rectangular step cut, set edge to edge in a channel so the row reads as one bar of light.",
      ety="From the French for “little rod”, the same word as the bread.",seehow="channel set the whole way round · 20mm",cta="SHOP EARRINGS →",render=render,
      claims=[("WE14387B","channel set the whole way round · 20mm")]),
 dict(id="E3",n=3,file="huggie",word="huggie",pron="HUG·ee",pos="n.",plate="huggie",sku="E14776S",guide="hoop · huggie",
      def_="A small hinged hoop that snaps shut flush against the lobe, so named because it hugs it.",
      ety="Informal; the jeweller’s word, not the dictionary’s.",seehow="12mm · brushed satin · no stones",cta="SHOP EARRINGS →",render=render,
      claims=[("E14776S","12mm brushed satin")]),
 dict(id="E4",n=4,file="toggle",word="toggle",pron="TOG·ul",pos="n.",plate="toggle",sku="YF5143",guide="tennis · toggle",
      def_="A clasp that closes with a turn instead of a catch: a straight bar passed through a ring and pulled flat against it.",
      ety="Worn at the front, on purpose. The closure is the design.",seehow="bar and ring · about 15mm · 50cm chain",cta="SHOP NECKLACES →",render=render,hero=True,
      claims=[("YF5143","bar and ring about 15mm · 50cm chain · 4mm")]),
 dict(id="E5",n=5,file="baroque",word="baroque",pron="ba·ROKE",pos="adj.",plate="baroque",sku="YF3925",guide="band · baroque",
      def_="Of a pearl: irregular in shape, not round, no two alike.",
      ety="The word belonged to the pearl before it belonged to art: Portuguese barroco, “a misshapen pearl”.",seehow="flat baroque shell pearls · gold toggle",cta="SHOP BRACELETS →",render=render),
]
for c in CREATIVES: c["def"]=c.pop("def_")
