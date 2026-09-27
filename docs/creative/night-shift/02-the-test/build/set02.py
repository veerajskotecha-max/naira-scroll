# -*- coding: utf-8 -*-
"""SET 02 — THE TEST. Five wear-test report cards. Four PASS on what the listing's Care line already says
(water, daily wear); one honest FAIL on the thing it says to keep away from: perfume. The evidence photograph
is the plate; the report form is the type; the stamp is the verdict."""
from core import *
SET=dict(slug="02-the-test",title="The Test",n=2)
S2=f"{ROOT}/s02"
TOK={"feed":dict(PLATE="700px",STAMP="150px",FORM="20px",ASIDE="33px"),"story":dict(PLATE="1120px",STAMP="180px",FORM="23px",ASIDE="40px")}
CSS="""
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#222}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.fig{position:absolute;left:var(--pad);top:calc(var(--PLATE) - 44px);font-family:'JetBrains Mono';font-size:calc(var(--MONO)*.9);letter-spacing:.14em;text-transform:uppercase;color:#F1EBE1;background:rgba(27,21,18,.72);padding:7px 12px}
.form{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + 30px);font-family:'JetBrains Mono';font-size:var(--FORM);letter-spacing:.06em;text-transform:uppercase;line-height:1.5}
.form .hd{display:flex;justify-content:space-between;border-bottom:2px solid var(--ink);padding-bottom:8px;margin-bottom:6px;font-weight:500}
.form .row{display:grid;grid-template-columns:170px 1fr;gap:0 20px;border-bottom:1px dotted rgba(27,21,18,.35);padding:9px 0;line-height:1.45}
.form .row span:first-child{color:var(--mute)}
.form .row.big span:last-child{font-family:'Jost';font-weight:600;font-size:calc(var(--FORM)*1.35);letter-spacing:.04em}
.form .row.q span:last-child{font-family:'Cormorant Garamond';font-style:italic;text-transform:none;letter-spacing:0;font-size:calc(var(--FORM)*1.25)}
.form .row.res span:last-child{font-weight:500;color:var(--ac)}
.form .row.res.fail span:last-child{color:var(--ink)}
.stamp{position:absolute;right:calc(var(--pad) - 10px);top:calc(var(--PLATE) - var(--STAMP)*0.62);width:calc(var(--STAMP)*2.1);height:var(--STAMP);border:5px solid var(--ac);color:var(--ac);display:flex;align-items:center;justify-content:center;font-family:'Velista';font-weight:500;font-size:calc(var(--STAMP)*.62);letter-spacing:.02em;transform:rotate(-9deg);background:rgba(241,235,225,.55);mix-blend-mode:multiply;text-transform:uppercase;z-index:6}
.stamp.fail{border-color:#1B1512;color:#1B1512}
.stamp small{position:absolute;bottom:6px;right:12px;font-family:'JetBrains Mono';font-size:12px;letter-spacing:.14em}
.remarks{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);line-height:1.15;margin-top:22px;max-width:40ch;text-transform:none;letter-spacing:0}
.foot .see{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-bottom:6px}
"""
def render(c,fmt):
    sk=c["sku"]; plate=f'{S2}/plate_{c["plate"]}_{fmt}.jpg'
    cls_={0:" big",2:" q",3:" res"+(" fail" if c["result"]=="FAIL" else ""),4:" q"}
    rows="".join(f'<div class="row{cls_.get(i,"")}"><span>{E(k)}</span><span>{E(v)}</span></div>' for i,(k,v) in enumerate(c["rows"]))
    stamp=f'<div class="stamp {"fail" if c["result"]=="FAIL" else ""}">{c["result"]}<small>{E(c["stampnote"])}</small></div>'
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>'
            f'{top("NAIRA PETITE · WEAR TEST REPORT",IVORY)}<div class="fig">fig. {c["n"]} · {E(c["figcap"])}</div>{stamp}'
            f'<div class="form"><div class="hd"><span>test no. {c["n"]:02d} · {E(c["date"])}</span><span></span></div>{rows}<div class="remarks">{E(c["verdict"])}</div></div>'
            f'<div class="foot"><div><div class="see">subject:</div><div class="name">{name(sk)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sk)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="T1",n=1,file="shower",plate="shower",sku="YF5215",hero=True,water=True,result="PASS",stampnote="per care line",figcap="under the shower",date="27 sep 2026",
      rows=[("condition","shower · hot water · soap"),("material","surgical stainless steel · 18k gold tone toggle"),("care line","Waterproof and tarnish free, so daily wear and water are fine."),("result","covered · wear it in"),("notes","Keep it away from perfume and harsh chemicals; wipe with a soft dry cloth.")],
      verdict="(it goes in with you. the listing says so.)",spec="6MM STEEL SPHERES · GOLD TOGGLE · 15MM HEART",cta="SHOP BRACELETS →",render=render,
      claims=[("YF5215","6mm spheres · 15mm heart")]),
 dict(id="T2",n=2,file="swim",plate="swim",sku="YF5143",hero=True,water=True,result="PASS",stampnote="per care line",figcap="pool, submerged",date="27 sep 2026",
      rows=[("condition","chlorinated pool · submerged"),("material","surgical stainless steel · 18k pvd gold tone"),("care line","Waterproof and tarnish free, so daily wear and water are fine."),("result","covered · swim in it"),("notes","Keep it away from perfume and harsh chemicals; wipe with a soft dry cloth.")],
      verdict="(water is fine. the toggle stays shut.)",spec="4MM PAPERCLIP · 50CM · TOGGLE 15MM",cta="SHOP NECKLACES →",render=render,
      claims=[("YF5143","4mm paperclip · 50cm · toggle 15mm")]),
 dict(id="T3",n=3,file="sweat",plate="sweat",sku="YF5143",hero=True,water=True,result="PASS",stampnote="per care line",figcap="after the run",date="7 sep 2026",
      rows=[("condition","run · sweat · sun"),("material","surgical stainless steel · 18k pvd gold tone"),("care line","Waterproof and tarnish free, so daily wear and water are fine."),("result","covered · daily wear"),("notes","Keep it away from perfume and harsh chemicals; wipe with a soft dry cloth.")],
      verdict="(tarnish free is the promise. sweat is daily wear.)",spec="4MM PAPERCLIP · 50CM · 12G",cta="SHOP NECKLACES →",render=render,
      claims=[("YF5143","4mm paperclip · 50cm · 12g")]),
 dict(id="T4",n=4,file="overnight",plate="overnight",sku="E20267O",hero=True,result="PASS",stampnote="per care line",figcap="06:40, slept in",date="27 sep 2026",
      rows=[("condition","worn overnight · pillow"),("material","surgical stainless steel · 18k gold tone"),("care line","Waterproof and tarnish free, so daily wear and water are fine."),("result","covered · daily wear"),("notes","Keep it away from perfume and harsh chemicals; wipe with a soft dry cloth.")],
      verdict="(she forgot to take them off. that is allowed.)",spec="25MM · BRAIDED ROPE · NO STONES",cta="SHOP EARRINGS →",render=render,
      claims=[("E20267O","25mm braided")]),
 dict(id="T5",n=5,file="perfume",plate="perfume",sku="B00681C",hero=True,result="FAIL",stampnote="per care line",figcap="atomiser, kept apart",date="27 sep 2026",
      rows=[("condition","perfume spray · direct"),("material","surgical stainless steel · rhodium plated"),("care line","Keep it away from perfume and harsh chemicals."),("result","not covered · spray first, then wear"),("notes","Waterproof and tarnish free, so daily wear and water are fine.")],
      verdict="(spray first. let it dry. then put it on. the listing's one warning.)",spec="5MM CUSHION CZ · PAVÉ HALOS · FOLD-OVER CLASP",cta="SHOP BRACELETS →",render=render,
      claims=[("B00681C","5mm cushion")]),
]
