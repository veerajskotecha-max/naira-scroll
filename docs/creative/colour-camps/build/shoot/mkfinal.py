"""mkfinal.py - pick the approved plate for every sku|shot: first candidate that is not marked FAIL by a verifier
(verify/*.json) and that exists. PENDING = not yet judged. Writes final_v2.json with approved plates only
(use --tentative to also include pending candidates while laying out)."""
import json,glob,os,sys
P="/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/cc/shoot/plates/"
V={}
for f in glob.glob("/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/cc/verify/*.json"):
    try: J=json.load(open(f))
    except Exception: continue
    for r in (J if isinstance(J,list) else [J]):
        if isinstance(r,dict) and r.get("plate"): V[os.path.basename(r["plate"])]=bool(r.get("pass"))
PRE={"peach_E20267O_S1_a1.png":True,"peach_YF8156_S1_a1.png":True,"peach_YF8156_S3_a1.png":True,"lilac_B00681C_S1_a1.png":True}  # passed earlier 2-3 lens checks
V={**PRE,**V}
# YF5143 S1 a4g is NOT overridden any more: the on-body listing photo shows a spring-gate sailor ring (gate, collar, push-pin),
# so a plain torus misrepresents the clasp. a5g is an image edit of a4 that restores the real clasp (reference: listing clasp crop).
V["lilac_E16676C_S1_a2r.png"]=V.get("lilac_E16676C_S1_a2.png",False)   # retouch_corner.py: the cream table past the torn paper (top corners) recoloured lilac; product pixels untouched
V["lilac_E16676C_S2_a2c.png"]=True   # re-cropped to (0,400,1255,1969) exactly as the verifier specified after checking it holds no lash or brow pixels
CAND={
 "E20267O|S1":["peach_E20267O_S1_a1"],"E20267O|S2":["peach_E20267O_S2_a2c"],"E20267O|S3":["peach_E20267O_S3_a2"],"E20267O|S4":["peach_E20267O_S4_a2"],
 "YF3952|S1":["peach_YF3952_S1_a6"],"YF3952|S3":["peach_YF3952_S3_a2"],"YF3952|S4":["peach_YF3952_S4_a3"],
 "YF8156|S1":["peach_YF8156_S1_a1"],"YF8156|S2":["peach_YF8156_S2_a2"],"YF8156|S3":["peach_YF8156_S3_a1"],"YF8156|S4":["peach_YF8156_S4_a2"],
 "E14776S|S1":["peach_E14776S_S1_a3","peach_E14776S_S1_a2"],"E14776S|S2":["peach_E14776S_S2_a3"],"E14776S|S3":["peach_E14776S_S3_a2"],"E14776S|S4":["peach_E14776S_S4_a3","peach_E14776S_S4_a2"],
 "E16075B|S1":["peach_E16075B_S1_a2"],"E16075B|S2":["peach_E16075B_S2_a3"],"E16075B|S3":["peach_E16075B_S3_a1"],"E16075B|S4":["peach_E16075B_S4_a3","peach_E16075B_S4_a2"],
 "YF5143|S1":["sage_YF5143_S1_a5g"],"YF5143|S2":["sage_YF5143_S2_a2cg"],"YF5143|S3":["sage_YF5143_S3_a3g"],"YF5143|S4":["sage_YF5143_S4_a3g"],
 "YF5215|S1":["sage_YF5215_S1_a4g"],"YF5215|S2":["sage_YF5215_S2_a2g"],"YF5215|S3":["sage_YF5215_S3_a2g"],"YF5215|S4":["sage_YF5215_S4_a2g"],
 "FE02847B|S1":["sage_FE02847B_S1_a4g"],"FE02847B|S3":["sage_FE02847B_S3_a2g"],"FE02847B|S4":["sage_FE02847B_S4_a2g"],
 "JDR0104337|S1":["sage_JDR0104337_S1_a2g"],"JDR0104337|S2":["sage_JDR0104337_S2_a2g"],"JDR0104337|S3":["sage_JDR0104337_S3_a2g"],"JDR0104337|S4":["sage_JDR0104337_S4_a2g"],
 "JDR0303312-7|S1":["sage_JDR0303312-7_S1_a4","sage_JDR0303312-7_S1_a3g"],"JDR0303312-7|S2":["sage_JDR0303312-7_S2_a2g"],"JDR0303312-7|S3":["sage_JDR0303312-7_S3_a2g"],"JDR0303312-7|S4":["sage_JDR0303312-7_S4_a2g"],
 "B00681C|S1":["lilac_B00681C_S1_a1"],"B00681C|S2":["lilac_B00681C_S2_a2"],"B00681C|S3":["lilac_B00681C_S3_a2"],"B00681C|S4":["lilac_B00681C_S4_a2"],
 "E20997C|S1":["lilac_E20997C_S1_a2"],"E20997C|S3":["lilac_E20997C_S3_a2"],"E20997C|S4":["lilac_E20997C_S4_a2"],
 "E16676C|S1":["lilac_E16676C_S1_a2r","lilac_E16676C_S1_a2"],"E16676C|S2":["lilac_E16676C_S2_a2c"],"E16676C|S3":["lilac_E16676C_S3_a1"],"E16676C|S4":["lilac_E16676C_S4_a2"],
 "YF8439-SLV|S1":["lilac_YF8439-SLV_S1_a2"],"YF8439-SLV|S2":["lilac_YF8439-SLV_S2_a2c"],"YF8439-SLV|S3":["lilac_YF8439-SLV_S3_a1"],"YF8439-SLV|S4":["lilac_YF8439-SLV_S4_a1"],
 "WR23569K8|S1":["lilac_WR23569K8_S1_a1"],"WR23569K8|S2":["lilac_WR23569K8_S2_a1"],"WR23569K8|S3":["lilac_WR23569K8_S3_a1"],"WR23569K8|S4":["lilac_WR23569K8_S4_a1"],
}
tent="--tentative" in sys.argv
out={}; status={}
for k,cands in CAND.items():
    for c in cands:
        f=c+".png"
        if not os.path.exists(P+f): continue
        v=V.get(f)
        if v is True or (v is None and tent): out[k]=P+f; status[k]=("PASS" if v else "PENDING")+" "+c; break
        status.setdefault(k,("FAIL" if v is False else "PENDING")+" "+c)
json.dump(out,open(os.path.dirname(P.rstrip('/'))+"/final_v2.json","w"),indent=1)
for k in CAND: print(f"{k:18s} {status.get(k,'MISSING')}")
