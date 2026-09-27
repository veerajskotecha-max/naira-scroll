# -*- coding: utf-8 -*-
"""COLOUR CAMPS — APRICOT. / SAGE. / LILAC.
Every hero is a full-bleed plate photographed inside the camp colour. The camp word runs huge BEHIND the jewellery
(the plate, then the word, then a background-removed cut-out of the same plate on top), so the piece sits in front of
its own colour name. Each camp owns one graphic device, drawn from its world:
  APRICOT - a fruit-stall PLU sticker (the price is the sticker)
  SAGE    - a paint-chip card whose chips are sampled from the photograph itself
  LILAC   - a perforated postage stamp carrying the piece, cancelled by a NAIRAFLORE.COM postmark
Carousels carry the same device, small, as the page number / caption holder."""
import os, re, json, math, html
import numpy as np
from PIL import Image
from core import *

CC=f"{SP}/cc"; PL=f"{CC}/shoot/plates"; CUT=f"{CC}/cutouts"
PLATE_W,PLATE_H=1536,2752

CAMP={
 "peach":dict(word="APRICOT", label="APRICOT", ink="#2F4A42", word_col="#2F4A42", dot="#C4513A", sub="#3B2A22",
              lab="#3B2A22", logo="logo_ink.png", cta_bg="#2F4A42", cta_fg="#FFF8F5", foot="#2B1D16",
              dev="#E0795A", dev_ink="#FFF8F5", band="#F3C2A6", band_ink="#2B1D16", light="#F7DCCB"),
 "sage": dict(word="SAGE", label="SAGE", ink="#1F3A31", word_col="#1F3A31", dot="#DD7F68", sub="#1F3A31",
              lab="#1F3A31", logo="logo_ink.png", cta_bg="#1F3A31", cta_fg="#F4F1EA", foot="#16291F",
              dev="#F6F3EC", dev_ink="#1F3A31", band="#A9C2B7", band_ink="#16291F", light="#D5E6DC"),
 "lilac":dict(word="LILAC", label="LILAC", ink="#3B2D52", word_col="#3B2D52", dot="#DD7F68", sub="#3B2D52",
              lab="#3B2D52", logo="logo_ink.png", cta_bg="#3B2D52", cta_fg="#FFF8F5", foot="#2A2038",
              dev="#FBF8F4", dev_ink="#3B2D52", band="#D6C3DA", band_ink="#2A2038", light="#EDE2F0"),
}

# ---------------------------------------------------------------- geometry
def plate_box(fmt,fy=0.5,path=None):
    """(left, top, width, height) of the plate drawn into the card. story = full plate width; feed = same scale, a 4:5 window."""
    W,H=FORMATS[fmt]; iw,ih=(Image.open(path).size if path else (PLATE_W,PLATE_H))
    s=W/iw; pw,ph=iw*s,ih*s
    top=-(fy*ph-H/2); top=max(min(top,0),H-ph)
    return 0,top,pw,ph

def alpha_bbox(cut):
    a=np.asarray(Image.open(cut).convert('RGBA'))[...,3]; ys,xs=np.where(a>128)
    return xs.min()/a.shape[1],ys.min()/a.shape[0],xs.max()/a.shape[1],ys.max()/a.shape[0]

def sample(path,pts):
    """hex colours sampled (median of a small patch) at fractional points of a plate"""
    im=np.asarray(Image.open(path).convert('RGB')); h,w,_=im.shape; out=[]
    for fx,fy in pts:
        x,y=int(fx*w),int(fy*h); p=im[max(0,y-6):y+7,max(0,x-6):x+7].reshape(-1,3)
        r,g,b=np.median(p,axis=0).astype(int); out.append(f"#{r:02X}{g:02X}{b:02X}")
    return out

_SC={}
def sample_class(plate,cut,cls):
    """median colour of one material in the plate, found through the cut-out mask: bg, gold, silver, leaf, emerald, pearl, cz"""
    key=(plate,cut,cls)
    if key in _SC: return _SC[key]
    from lab import rgb2lab
    im=np.asarray(Image.open(plate).convert('RGB').resize((384,688))).astype(float)/255
    if cls=="bg":
        p=im[20:90].reshape(-1,3)
    else:
        a=(np.asarray(Image.open(cut).convert('RGBA').resize((384,688)))[...,3]>200) if cut else np.ones((688,384),bool)
        L=rgb2lab(im); C=np.hypot(L[...,1],L[...,2]); h=(np.degrees(np.arctan2(L[...,2],L[...,1]))+360)%360; Lv=L[...,0]
        sel={"gold":(h>55)&(h<95)&(C>22)&(Lv>35)&(Lv<88),
             "silver":(C<9)&(Lv>38)&(Lv<86),
             "leaf":(h>95)&(h<175)&(C>8)&(C<40)&(Lv>30)&(Lv<78),
             "emerald":(h>130)&(h<210)&(C>18)&(Lv<48),
             "pearl":(Lv>80)&(C<14)&(h>40)&(h<110),
             "cz":(Lv>84)&(C<7)}[cls]&a
        p=im[sel]
        if len(p)<30: p=im[a]
    r,g,b=(np.median(p,axis=0)*255).astype(int); hx=f"#{r:02X}{g:02X}{b:02X}"; _SC[key]=hx; return hx

def img_layer(path,box,z=1,extra=""):
    l,t,w,h=box
    return f'<img class="lay" src="{path}" style="left:{l:.1f}px;top:{t:.1f}px;width:{w:.1f}px;height:{h:.1f}px;z-index:{z};{extra}">'

# ---------------------------------------------------------------- devices
def plu(price,top_txt,bot_txt,code,col,ink,w=260):
    """oval produce sticker. SVG so the curved type sits on the rim like a real PLU label."""
    h=w*0.72; rx,ry=w/2-4,h/2-4; cx,cy=w/2,h/2
    return f'''<svg width="{w}" height="{h:.0f}" viewBox="0 0 {w} {h:.0f}" style="overflow:visible">
<defs><path id="pt{code}" d="M {cx-rx*0.78:.1f},{cy+2:.1f} A {rx*0.78:.1f},{ry*0.74:.1f} 0 0,1 {cx+rx*0.78:.1f},{cy+2:.1f}"/>
<path id="pb{code}" d="M {cx-rx*0.80:.1f},{cy-4:.1f} A {rx*0.80:.1f},{ry*0.80:.1f} 0 0,0 {cx+rx*0.80:.1f},{cy-4:.1f}"/>
<linearGradient id="gl{code}" x1="0" y1="0" x2="0.6" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".34"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}"/>
<ellipse cx="{cx}" cy="{cy}" rx="{rx-9}" ry="{ry-9}" fill="none" stroke="{ink}" stroke-width="1.6" stroke-opacity=".85"/>
<text font-family="JetBrains Mono" font-size="{w*0.052:.1f}" letter-spacing="2.4" fill="{ink}"><textPath href="#pt{code}" startOffset="50%" text-anchor="middle">{E(top_txt)}</textPath></text>
<text x="{cx}" y="{cy+w*0.07:.1f}" text-anchor="middle" font-family="Jost" font-weight="600" font-size="{w*0.20:.1f}" fill="{ink}">{E(price)}</text>
<text font-family="JetBrains Mono" font-size="{w*0.046:.1f}" letter-spacing="1.8" fill="{ink}"><textPath href="#pb{code}" startOffset="50%" text-anchor="middle">{E(bot_txt)}</textPath></text>
<text x="{cx}" y="{cy+ry*0.58:.1f}" text-anchor="middle" font-family="JetBrains Mono" font-size="{w*0.040:.1f}" letter-spacing="1.5" fill="{ink}" fill-opacity=".8">PLU {E(code)}</text>
<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#gl{code})"/>
</svg>'''

def chips(title,rows,foot_txt,bg,ink,w=230):
    """paint-chip card: rows = [(hex, NAME)] sampled from the plate"""
    ch="".join(f'<div class="chip"><div class="sw" style="background:{hx}"></div><div class="cl"><b>{E(n)}</b><span>{hx}</span></div></div>' for hx,n in rows)
    return (f'<div class="chipcard" style="width:{w}px;background:{bg};color:{ink}"><div class="ct">{E(title)}</div>{ch}'
            f'<div class="cf">{E(foot_txt)}</div></div>')

def stamp(img,box,denom,line1,line2,ink,paper,w=250):
    """perforated postage stamp; its picture is a crop of the plate itself (the piece)"""
    h=int(w*1.24); pad=16; r=5.2; step=15
    l,t,rr,bb=box; iw,ih=Image.open(img).size
    cx0,cy0,cw,chh=l*iw,t*ih,(rr-l)*iw,(bb-t)*ih
    iw_,ih_=w-2*pad,h-2*pad-44
    holes=[]
    n=int(w//step); 
    for i in range(n+1):
        x=i*w/n; holes+= [(x,0),(x,h)]
    m=int(h//step)
    for j in range(m+1):
        y=j*h/m; holes+= [(0,y),(w,y)]
    hs="".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#000"/>' for x,y in holes)
    # crop box to the picture aspect
    asp=iw_/ih_
    if cw/chh>asp: nw=chh*asp; cx0+= (cw-nw)/2; cw=nw
    else: nh=cw/asp; cy0+= (chh-nh)/2; chh=nh
    uid=abs(hash((img,box)))%100000
    return f"""<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="overflow:visible">
<defs><mask id="perf{uid}"><rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>{hs}</mask></defs>
<rect x="0" y="0" width="{w}" height="{h}" fill="{paper}" mask="url(#perf{uid})"/>
<svg x="{pad}" y="{pad}" width="{iw_}" height="{ih_}" viewBox="{cx0:.1f} {cy0:.1f} {cw:.1f} {chh:.1f}" preserveAspectRatio="xMidYMid slice"><image href="{img}" x="0" y="0" width="{iw}" height="{ih}"/></svg>
<rect x="{pad}" y="{pad}" width="{iw_}" height="{ih_}" fill="none" stroke="#000" stroke-opacity=".08"/>
<text x="{pad+12}" y="{pad+34}" font-family="Jost" font-weight="600" font-size="26" fill="#fff" style="paint-order:stroke" stroke="rgba(0,0,0,.18)" stroke-width="3">{denom}</text>
<text x="{pad}" y="{h-pad-6}" font-family="Velista" font-size="30" fill="{ink}">{E(line1)}</text>
<text x="{w-pad}" y="{h-pad-8}" text-anchor="end" font-family="JetBrains Mono" font-size="10.5" letter-spacing="1.6" fill="{ink}">{E(line2)}</text>
</svg>"""

def postmark(ink,w=230,word="LILAC"):
    r=w*0.33; cx=r+4; cy=r+4
    waves="".join(f'<path d="M {cx+r*0.7:.0f},{cy-r*0.55+i*r*0.36:.0f} q 22,-12 44,0 t 44,0 t 44,0 t 44,0" fill="none" stroke="{ink}" stroke-width="3"/>' for i in range(4))
    return f'''<svg width="{w+30}" height="{2*r+8:.0f}" viewBox="0 0 {w+30} {2*r+8:.0f}" style="overflow:visible">
<defs><path id="pm{word}" d="M {cx-r*0.74:.1f},{cy:.1f} a {r*0.74:.1f},{r*0.74:.1f} 0 1,1 {r*1.48:.1f},0 a {r*0.74:.1f},{r*0.74:.1f} 0 1,1 {-r*1.48:.1f},0"/></defs>
<g opacity=".78"><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{ink}" stroke-width="3"/>
<circle cx="{cx}" cy="{cy}" r="{r*0.56:.1f}" fill="none" stroke="{ink}" stroke-width="1.6"/>
<text font-family="JetBrains Mono" font-size="{r*0.20:.1f}" letter-spacing="3" fill="{ink}"><textPath href="#pm{word}" startOffset="0">NAIRAFLORE.COM · NAIRA PETITE ·</textPath></text>
<text x="{cx}" y="{cy+r*0.12:.1f}" text-anchor="middle" font-family="Velista" font-size="{r*0.40:.1f}" fill="{ink}">{E(word)}</text>
{waves}</g></svg>'''

# ---------------------------------------------------------------- page CSS
CSS="""
.lay{position:absolute;display:block}
.word{position:absolute;left:0;right:0;text-align:center;font-family:'Velista';font-weight:500;line-height:.8;letter-spacing:-.005em;white-space:nowrap;z-index:2}
.word .dot{display:inline-block}
.subl{position:absolute;font-family:'Cormorant Garamond';font-style:italic;font-weight:500;line-height:1.12;z-index:6;max-width:17ch;text-wrap:balance}
.dev{position:absolute;z-index:7;filter:drop-shadow(0 10px 14px rgba(40,20,10,.22)) drop-shadow(0 2px 3px rgba(40,20,10,.18))}
.foot{z-index:8}
.cta.solid{background:var(--ctabg);border-color:var(--ctabg);color:var(--ctafg)}
.chipcard{padding:14px 14px 12px;border-radius:3px}
.chipcard .ct{font-family:'JetBrains Mono';font-size:12px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px;opacity:.85}
.chip{display:flex;flex-direction:column;margin-bottom:10px}
.chip .sw{height:64px;border-radius:2px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}
.chip .cl{display:flex;justify-content:space-between;align-items:baseline;margin-top:6px}
.chip .cl b{font-family:'Jost';font-weight:600;font-size:13px;letter-spacing:.1em;text-transform:uppercase}
.chip .cl span{font-family:'JetBrains Mono';font-size:11px;letter-spacing:.06em;opacity:.8}
.chipcard .cf{font-family:'JetBrains Mono';font-size:11px;letter-spacing:.14em;text-transform:uppercase;border-top:1px solid currentColor;padding-top:8px;opacity:.85}
.stamp{position:relative;background:var(--paper);
  -webkit-mask:radial-gradient(circle 6px at 6px 6px,transparent 5.5px,#000 6px) -6px -6px/15px 15px;
  mask:radial-gradient(circle 6px at 6px 6px,transparent 5.5px,#000 6px) -6px -6px/15px 15px}
.stamp .spic{position:absolute;background-repeat:no-repeat;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
.stamp .sden{position:absolute;font-family:'Jost';font-weight:600;font-size:26px;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.35);letter-spacing:.01em}
.stamp .sfoot{position:absolute;display:flex;justify-content:space-between;align-items:baseline;color:var(--sink)}
.stamp .sfoot b{font-family:'Velista';font-weight:500;font-size:30px;letter-spacing:.02em}
.stamp .sfoot span{font-family:'JetBrains Mono';font-size:10.5px;letter-spacing:.14em;text-transform:uppercase}
.pm{position:absolute;z-index:8;mix-blend-mode:multiply}
"""

# ---------------------------------------------------------------- hero
WORD_W={"feed":1000,"story":1010}
def hero_render(c,fmt):
    K=CAMP[c["camp"]]; W,H=FORMATS[fmt]; pad=52 if fmt=="feed" else 64
    plate=c["plate"]; cut=c.get("cut")
    fy=c.get("fy_"+fmt,c.get("fy",0.5))
    box=plate_box(fmt,fy,plate); l,t,pw,ph=box
    # the camp word, huge, centred on the piece
    word=K["word"]; fs=fit(word+".",WORD_W[fmt]*c.get("wscale",1.0),track=-0.005)
    mode=c.get("wmode","center")
    if cut:
        x0,y0,x1,y1=alpha_bbox(cut); cy=t+ph*((y0+y1)/2); ty=t+ph*y0
    else: cy=ty=H*0.5
    if mode=="top": wy=ty-fs*0.62+c.get("wdy_"+fmt,0)      # letters sit on the piece's top edge, lower third tucked behind it
    else: wy=cy-fs*0.40+c.get("wdy_"+fmt,0)
    wc=c.get("word_col",K["word_col"]); wop=c.get("word_op",1.0)
    word_html=(f'<div class="word" style="top:{wy:.0f}px;font-size:{fs:.0f}px;color:{wc};opacity:{wop}">{E(word)}'
               f'<span class="dot" style="color:{K["dot"]}">.</span></div>')
    sub_top=c.get("sub_top_"+fmt,(118 if fmt=="feed" else 150)); sub_fs=30 if fmt=="feed" else 38
    sub_h=sub_fs*1.12*3
    if wy<sub_top+sub_h+12:      # the word is up top: the italic line moves down, just above the name
        fb=(160 if fmt=="feed" else 196)
        sub=(f'<div class="subl" style="left:{pad}px;bottom:{fb}px;font-size:{sub_fs}px;color:{K["sub"]};max-width:22ch">{E(c["sub"])}</div>')
    else:
        sub=(f'<div class="subl" style="left:{pad}px;top:{sub_top}px;font-size:{sub_fs}px;color:{K["sub"]}">{E(c["sub"])}</div>')
    c["_wb"]=(wy+fs*0.08,wy+fs*0.78)
    dev=c["device"](c,fmt) if c.get("device") else ""
    foot=(f'<div class="foot" style="color:{K["foot"]}"><div><div class="name">{name(c["sku"])}</div><div class="spec">{E(c["spec"])}</div></div>'
          f'<div><div class="price">{price(c["sku"])}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
    scr=c.get("scrim",{})
    lr,lg,lb=[int(K["light"].lstrip('#')[i:i+2],16) for i in (0,2,4)]
    fh=(330 if fmt=="feed" else 420)
    scrim=f'<div style="position:absolute;left:0;right:0;bottom:0;height:{fh}px;z-index:4;background:linear-gradient(rgba({lr},{lg},{lb},0),rgba({lr},{lg},{lb},.62) 62%,rgba({lr},{lg},{lb},.78))"></div>'
    if c.get("topscrim"):      # darker plate tops: lift the header and the italic line with the camp's light colour
        th_=sub_top+sub_h+90
        scrim+=f'<div style="position:absolute;left:0;right:0;top:0;height:{th_:.0f}px;z-index:4;background:linear-gradient(rgba({lr},{lg},{lb},.80),rgba({lr},{lg},{lb},.58) 55%,rgba({lr},{lg},{lb},0))"></div>'
    if scr.get(fmt):
        col,hh,a=scr[fmt]; r,g,b=[int(col.lstrip('#')[i:i+2],16) for i in (0,2,4)]
        scrim+=f'<div style="position:absolute;left:0;right:0;bottom:0;height:{hh}px;z-index:4;background:linear-gradient(rgba({r},{g},{b},0),rgba({r},{g},{b},{a}))"></div>'
    return (f'<style>:root{{--ctabg:{K["cta_bg"]};--ctafg:{K["cta_fg"]}}}{CSS}</style>'
            + img_layer(plate,box,1) + word_html + (img_layer(cut,box,3) if cut else "") + scrim
            + f'<div style="position:relative;z-index:9">{top("NAIRA PETITE · "+K["label"],K["lab"],logo=K["logo"])}</div>'
            + sub + dev + foot)

def hero(camp,id,sku,plate,cut,sub,spec,cta,**k):
    d=dict(render=hero_render,camp=camp,id=id,sku=sku,skus=[sku],plate=plate,cut=cut,sub=sub,spec=spec,cta=cta,claims=[(sku,spec)],
           file=re.sub(r'[^a-z0-9]+','-',ROWS[sku]["title"].lower().replace('é','e').replace('è','e').replace('—','-')).strip('-'))
    d.update(k); return d

# device placement helpers ------------------------------------------------
def at(html_,x,y,rot=0,scale=1.0,cls="dev"):
    return f'<div class="{cls}" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({scale});transform-origin:center">{html_}</div>'

def _pos(c,fmt,dw,dh,rot):
    p=c.get("dpos",{}).get(fmt)
    if p: return p
    sc=c.get("dscale",{}).get(fmt,1.0 if fmt=="feed" else 1.1)
    best=auto_place(c,fmt,int(dw*sc)+16,int(dh*sc)+16,c.get("dside","right"),c.get("_wb"))
    x,y=best[1]+8+(dw*sc-dw)/2,best[2]+8+(dh*sc-dh)/2   # transform-origin is the centre
    return (x,y,rot,sc)

def dev_plu(top_txt,bot_txt,code,rot=-9):
    def f(c,fmt):
        K=CAMP[c["camp"]]; x,y,r,s=_pos(c,fmt,260,187,rot)
        return at(plu(price(c["sku"]),top_txt,bot_txt,code,K["dev"],K["dev_ink"]),x,y,r,s)
    return f
def dev_chips(title,spec,foot_txt,rot=5):
    """spec = [(NAME, material class)] - each chip is the real colour of that material in this photograph"""
    def f(c,fmt):
        K=CAMP[c["camp"]]; x,y,r,s=_pos(c,fmt,230,396,rot)
        rows=[(sample_class(c["plate"],c["cut"],cls),n) for n,cls in spec]
        return at(chips(title,rows,foot_txt,K["dev"],K["dev_ink"]),x,y,r,s)
    return f
def dev_stamp(crop,line2,rot=6):
    def f(c,fmt):
        K=CAMP[c["camp"]]; x,y,r,s=_pos(c,fmt,250,340,rot)
        y+=30*s
        cr=crop or c.get("stamp_crop")
        if cr is None and c.get("cut"):
            x0,y0,x1,y1=alpha_bbox(c["cut"]); pw_,ph_=x1-x0,y1-y0
            cr=(max(0,x0-pw_*0.06),max(0,y0-ph_*0.10),min(1,x1+pw_*0.06),min(1,y1+ph_*0.10))
        st=at(stamp(c.get("stamp_src",c["plate"]),cr,price(c["sku"]),"LILAC.",line2,K["dev_ink"],K["dev"]),x,y,r,s)
        pm=f'<div class="pm" style="left:{x+120*s:.0f}px;top:{y-44*s:.0f}px;transform:rotate({r-10}deg) scale({s});transform-origin:left top">{postmark(K["ink"])}</div>'
        return st+pm
    return f

# ---------------------------------------------------------------- automatic device placement
_MC={}
def card_mask(cut,box,W,H,dil=26):
    key=(cut,tuple(round(v,1) for v in box),W,H,dil)
    if key in _MC: return _MC[key]
    from PIL import ImageFilter
    l,t,pw,ph=box
    a=Image.open(cut).convert('RGBA').split()[3].resize((int(pw),int(ph)))
    canvas=Image.new('L',(W,H),0); canvas.paste(a,(int(l),int(t)))
    canvas=canvas.point(lambda v:255 if v>60 else 0).filter(ImageFilter.MaxFilter(2*(dil//2)+1))
    m=np.asarray(canvas)>0; _MC[key]=m; return m

def integral(m): return np.pad(m.astype(np.int32).cumsum(0).cumsum(1),((1,0),(1,0)))
def rect_sum(I,x,y,w,h):
    x0,y0=max(0,int(x)),max(0,int(y)); x1,y1=min(I.shape[1]-1,int(x+w)),min(I.shape[0]-1,int(y+h))
    if x1<=x0 or y1<=y0: return 0
    return I[y1,x1]-I[y0,x1]-I[y1,x0]+I[y0,x0]

def auto_place(c,fmt,dw,dh,side="right",word_band=None):
    W,H=FORMATS[fmt]; box=plate_box(fmt,c.get("fy_"+fmt,c.get("fy",0.5)),c["plate"])
    m=card_mask(c["cut"],box,W,H) if c.get("cut") else np.zeros((H,W),bool); I=integral(m)
    top_lim=112 if fmt=="feed" else 130; foot_h=250 if fmt=="feed" else 300
    best=None
    for y in range(top_lim,H-foot_h-dh+1,12):
        for x in range(40,W-40-dw+1,12):
            if x<430 and y<(250 if fmt=="feed" else 300): continue      # the italic line lives here
            ov=rect_sum(I,x,y,dw,dh)
            wb=0
            if word_band: wb=max(0,min(y+dh,word_band[1])-max(y,word_band[0]))*dw
            pref=(W-40-dw-x) if side=="right" else (x-40)
            score=ov*20+wb*0.35+pref*0.6+abs((y+dh/2)-H*0.56)*0.3
            if best is None or score<best[0]: best=(score,x,y,ov)
    return best

# ---------------------------------------------------------------- carousel cards (1080x1350)
CAR_CSS="""
.band{position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:space-between;gap:24px;padding:0 var(--pad);z-index:8}
.cap{font-family:'JetBrains Mono';font-size:17px;letter-spacing:.12em;text-transform:uppercase;line-height:1.45}
.cap b{font-family:'Jost';font-weight:600;letter-spacing:.08em;font-size:19px}
.idx{font-family:'JetBrains Mono';font-size:15px;letter-spacing:.14em;white-space:nowrap}
.bword{font-family:'Velista';font-weight:500;font-size:44px;line-height:.9;letter-spacing:.01em}
"""
def energy_pick(path,W,H,band,cands,dw,dh):
    """choose the calmest candidate rectangle (lowest edge energy) on the plate as drawn into the card"""
    from PIL import ImageFilter
    im=Image.open(path).convert('L')
    iw,ih=im.size; s=max(W/iw,(H-band)/ih); im=im.resize((int(iw*s),int(ih*s)))
    ox=(im.width-W)//2; oy=(im.height-(H-band))//2
    im=im.crop((ox,oy,ox+W,oy+H-band))
    e=np.asarray(im.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(6))).astype(float)
    best=None
    for (x,y) in cands:
        v=e[max(0,y):y+dh,max(0,x):x+dw].mean()
        if best is None or v<best[0]: best=(v,x,y)
    return best[1],best[2]

def mini_plu(big,top_txt,bot_txt,col,ink,w=190):
    h=w*0.72; rx,ry=w/2-4,h/2-4; cx,cy=w/2,h/2; uid=abs(hash((big,top_txt,bot_txt)))%100000
    return f'''<svg width="{w}" height="{h:.0f}" viewBox="0 0 {w} {h:.0f}" style="overflow:visible">
<defs><path id="mt{uid}" d="M {cx-rx*0.78:.1f},{cy+2:.1f} A {rx*0.78:.1f},{ry*0.74:.1f} 0 0,1 {cx+rx*0.78:.1f},{cy+2:.1f}"/>
<path id="mb{uid}" d="M {cx-rx*0.80:.1f},{cy-4:.1f} A {rx*0.80:.1f},{ry*0.80:.1f} 0 0,0 {cx+rx*0.80:.1f},{cy-4:.1f}"/></defs>
<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}"/>
<ellipse cx="{cx}" cy="{cy}" rx="{rx-7}" ry="{ry-7}" fill="none" stroke="{ink}" stroke-width="1.3" stroke-opacity=".85"/>
<text font-family="JetBrains Mono" font-size="{w*0.056:.1f}" letter-spacing="2" fill="{ink}"><textPath href="#mt{uid}" startOffset="50%" text-anchor="middle">{E(top_txt)}</textPath></text>
<text x="{cx}" y="{cy+w*0.075:.1f}" text-anchor="middle" font-family="Jost" font-weight="600" font-size="{w*0.21:.1f}" fill="{ink}">{E(big)}</text>
<text font-family="JetBrains Mono" font-size="{w*0.05:.1f}" letter-spacing="1.6" fill="{ink}"><textPath href="#mb{uid}" startOffset="50%" text-anchor="middle">{E(bot_txt)}</textPath></text>
</svg>'''

def one_chip(hx,nm,bg,ink,w=170):
    return (f'<div class="chipcard" style="width:{w}px;background:{bg};color:{ink};padding:10px 10px 8px">'
            f'<div class="chip" style="margin-bottom:4px"><div class="sw" style="background:{hx};height:74px"></div>'
            f'<div class="cl"><b>{E(nm)}</b><span>{hx}</span></div></div></div>')

def car_render(c,fmt):
    K=CAMP[c["camp"]]; W,H=FORMATS[fmt]; bh=c.get("band_h",150)
    last=c.get("last",False)
    # top legibility: pick logo/label colour by the plate's top brightness
    im=np.asarray(Image.open(c["plate"]).convert('L').resize((64,80))).astype(float)
    dark_top=im[:8].mean()<120
    lab_col="#FFFFFF" if dark_top else K["lab"]; logo="logo_white.png" if dark_top else K["logo"]
    scr='<div style="position:absolute;left:0;right:0;top:0;height:200px;z-index:4;background:linear-gradient(rgba(20,14,10,.38),rgba(20,14,10,0))"></div>' if dark_top else ''
    inner=(f'<div style="color:{K["band_ink"]};display:flex;align-items:center;gap:22px"><div class="bword">{E(K["word"])}<span style="color:{K["dot"]}">.</span></div>'
           f'<div class="cap">{c["caption"]}</div></div>' if not last else
           f'<div style="color:{K["band_ink"]}"><div class="name">{name(c["sku"])}</div><div class="spec">{E(c["spec"])}</div></div>'
           f'<div style="display:flex;align-items:center;gap:22px;color:{K["band_ink"]}"><div class="price">{price(c["sku"])}</div><span class="cta solid" style="margin-top:0">{E(c["cta"])}</span></div>')
    # device echo, placed on the calmest part of the plate
    dev=""
    if c.get("echo"):
        kind,a,b=c["echo"]
        if kind=="plu": html_=mini_plu(a,"NAIRA PETITE · APRICOT",b,K["dev"],K["dev_ink"]); dw,dh=190,137
        elif kind=="chip": html_=one_chip(sample_class(c["plate"],None,a),b,K["dev"],K["dev_ink"]); dw,dh=170,130
        else: html_=postmark(K["ink"],w=200,word="LILAC"); dw,dh=250,140
        cands=[(W-dw-48,112),(48,112),(W-dw-48,H-bh-dh-40),(48,H-bh-dh-40),(W-dw-48,(H-bh)//2-dh//2)]
        x,y=energy_pick(c["plate"],W,H,bh,cands,dw,dh)
        rot=-8 if kind=="plu" else (4 if kind=="chip" else -10)
        dev=at(html_,x,y,rot,1.0,cls="dev" if kind!="pm" else "pm")
    return (f'<style>:root{{--ctabg:{K["cta_bg"]};--ctafg:{K["cta_fg"]}}}{CSS}{CAR_CSS}</style>'
            f'<div class="lay" style="left:0;top:0;right:0;bottom:{bh}px;z-index:1;background-image:url({c["plate"]});background-size:cover;background-position:{c.get("bgx","50%")} {c.get("bgy","50%")}"></div>'
            + scr + f'<div style="position:relative;z-index:9">{top("NAIRA PETITE · "+K["label"],lab_col,logo=logo)}</div>'
            + dev
            + f'<div class="band" style="height:{bh}px;background:{K["band"]}">{inner}'
            + ('' if last else f'<div class="idx" style="color:{K["band_ink"]}">{c["idx"]}</div>') + '</div>')

def car_card(camp,id,sku,plate,caption,idx,**k):
    d=dict(render=car_render,camp=camp,id=id,sku=sku,skus=[sku],plate=plate,caption=caption,idx=idx,claims=[(sku,re.sub('<[^>]+>','',caption))],
           file=re.sub(r'[^a-z0-9]+','-',ROWS[sku]["title"].lower().replace('é','e').replace('è','e').replace('—','-')).strip('-'))
    d.update(k); return d
