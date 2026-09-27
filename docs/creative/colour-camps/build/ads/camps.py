# -*- coding: utf-8 -*-
"""The three colour camps: which plate each ad uses, and each product's device copy.
final.json (built from the verification verdicts) decides the plates; nothing unverified reaches an ad."""
import json, os
from ccads import *
from campcopy import COPY, ORDER

FINAL=f"{CC}/shoot/final_v2.json"
def F(): return json.load(open(FINAL)) if os.path.exists(FINAL) else {}

def cut_of(plate):
    b=os.path.basename(plate)[:-4]
    b=b.rstrip('g') if b.endswith('g') and not b.endswith('_g') else b
    for cand in (b, b.rstrip('c')):
        p=f"{CUT}/{cand}.png"
        if os.path.exists(p): return p
    return None

# per-product hero settings and device copy --------------------------------------------------------------
DEV={
 # APRICOT - fruit-stall PLU sticker, the price is the sticker
 "E20267O":dict(wmode="top",  device=dev_plu("NAIRA PETITE · APRICOT","WOVEN HOOPS · 25MM","20267")),
 "E14776S":dict(wmode="top",device=dev_plu("NAIRA PETITE · APRICOT","BRUSHED HUGGIES · 12MM","14776")),
 "YF3952": dict(wmode="top",  device=dev_plu("NAIRA PETITE · APRICOT","HEARTLINE · PAPERCLIP","3952")),
 "E16075B":dict(wmode="top",device=dev_plu("NAIRA PETITE · APRICOT","RIBBON BOWS · 15MM","16075")),
 "YF8156": dict(wmode="top",  device=dev_plu("NAIRA PETITE · APRICOT","RIBBON BEAD · 16–19CM","8156")),
 # SAGE - paint chips sampled from the photograph
 "YF5143": dict(wmode="center",device=dev_chips("NAIRA PETITE · SAGE",[("SAGE","bg"),("GOLD TONE","gold"),("SAGE LEAF","leaf")],"Nº 5143 · TOGGLE LINK")),
 "YF5215": dict(wmode="center",device=dev_chips("NAIRA PETITE · SAGE",[("SAGE","bg"),("STEEL","silver"),("GOLD HEART","gold")],"Nº 5215 · HEARTBEAD")),
 "FE02847B":dict(wmode="center",device=dev_chips("NAIRA PETITE · SAGE",[("SAGE","bg"),("GREEN CZ","emerald"),("SHELL PEARL","pearl")],"Nº 02847 · VERDANT")),
 "JDR0104337":dict(wmode="center",device=dev_chips("NAIRA PETITE · SAGE",[("SAGE","bg"),("GRANULATION","gold"),("SAGE LEAF","leaf")],"Nº 0104337 · GRANULE")),
 "JDR0303312-7":dict(wmode="center",device=dev_chips("NAIRA PETITE · SAGE",[("SAGE","bg"),("GOLD TONE","gold"),("PAVÉ CZ","cz")],"Nº 0303312 · CHEVRON")),
 # LILAC - postage stamp of the piece, cancelled by the postmark
 "B00681C":dict(wmode="center",device=dev_stamp(None,"PRISM RIVIÈRE")),
 "E20997C":dict(wmode="center",device=dev_stamp(None,"PEARL BLOSSOM")),
 "E16676C":dict(wmode="center",device=dev_stamp(None,"TRIO OVAL")),
 "YF8439-SLV":dict(wmode="center",device=dev_stamp(None,"SERPENTINE")),
 "WR23569K8":dict(wmode="center",device=dev_stamp(None,"VINTAGE HALO")),
}
TUNE={"JDR0303312-7":dict(dscale={"feed":0.86,"story":1.0},topscrim=True)}   # per-sku overrides after review

def auto_fy(cut,fmt="feed",target=0.52):
    """feed window centred so the piece sits at `target` of the card height"""
    x0,y0,x1,y1=alpha_bbox(cut); W,H=FORMATS[fmt]; s=W/PLATE_W; ph=PLATE_H*s
    cy=(y0+y1)/2*ph; top=H*target-cy          # desired top offset of the plate
    return max(0.0,min(1.0,(H/2-top)/ph))

def heroes(camp,prefix):
    FF=F(); out=[]
    for i,s in enumerate(ORDER[camp],1):
        p=FF.get(f"{s}|S1")
        if not p: continue
        cut=cut_of(p); c=COPY[s]; k=dict(DEV[s])
        if cut: k["fy"]=auto_fy(cut)
        k.update(TUNE.get(s,{}))
        out.append(hero(camp,f"{prefix}{i}",s,p,cut,c["sub"],c["spec"],c["cta"],**k))
    return out

# carousel echoes: APRICOT = mini PLU (big figure, rim text); SAGE = one chip (material, label); LILAC = postmark
ECHO={
 "E20267O":{"S2":("plu","25MM","ACROSS · ON THE LOBE"),"S3":("plu","BRAID","OF GOLD STRANDS"),"S4":("plu","PAIR","WOVEN GOLD HOOPS")},
 "E14776S":{"S2":("plu","12MM","ACROSS · 6MM BAND"),"S3":("plu","SATIN","NOT MIRROR POLISHED"),"S4":("plu","PAIR","BRUSHED HUGGIES")},
 "YF3952": {"S3":("plu","HEARTS","CZ STATIONS"),"S4":("plu","CHAIN","PAPERCLIP LINKS")},
 "E16075B":{"S2":("plu","15MM","WIDE · BOW STUDS"),"S3":("plu","BOWS","PEAR-CUT CZ"),"S4":("plu","PAIR","RIBBON BOW STUDS")},
 "YF8156": {"S2":("plu","16–19","CM · ADJUSTS"),"S3":("plu","5MM","HEART-CUT CZ"),"S4":("plu","BOW","TWO HEART CZ")},
 "YF5143": {"S2":("chip","gold","GOLD TONE"),"S3":("chip","gold","GOLD TONE"),"S4":("chip","bg","SAGE")},
 "YF5215": {"S2":("chip","bg","SAGE"),"S3":("chip","gold","GOLD HEART"),"S4":("chip","silver","STEEL")},
 "FE02847B":{"S3":("chip","emerald","GREEN CZ"),"S4":("chip","bg","SAGE")},
 "JDR0104337":{"S2":("chip","bg","SAGE"),"S3":("chip","gold","GRANULATION"),"S4":("chip","bg","SAGE")},
 "JDR0303312-7":{"S2":("chip","bg","SAGE"),"S3":("chip","cz","PAVÉ CZ"),"S4":("chip","gold","GOLD TONE")},
}
def carousel(camp,prefix):
    FF=F(); out=[]
    for i,s in enumerate(ORDER[camp],1):
        if not FF.get(f"{s}|S1"): continue
        c=COPY[s]; shots=[sh for sh in ("S2","S3","S4") if FF.get(f"{s}|{sh}")]
        n=1+len(shots)
        for j,sh in enumerate(shots,2):
            p=FF[f"{s}|{sh}"]; last=(j==n)
            cap={"S2":c["worn"],"S3":c["close"]}.get(sh,c["close"])
            echo=ECHO.get(s,{}).get(sh) if camp!="lilac" else ("pm","","")
            k=dict(echo=echo); k.update(TUNE.get(f"{s}|{sh}",{}))
            if last: out.append(car_card(camp,f"{prefix}{i}{chr(96+j)}",s,p,"",f"{j} / {n}",last=True,spec=c["spec"],cta=c["cta"],**k))
            else: out.append(car_card(camp,f"{prefix}{i}{chr(96+j)}",s,p,cap,f"{j} / {n}",**k))
    return out
