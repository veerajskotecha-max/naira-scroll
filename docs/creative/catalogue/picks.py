# Picks by eye from the contact sheets: product number -> (on-model image, close-up image). None for the on-model
# image means the store has no photo of the piece worn; those products use their product shot instead.
import json, sys
P = {1:(5,6),2:(3,1),3:(4,6),4:(2,3),5:(2,3),6:(2,4),7:(2,4),8:(2,4),9:(7,2),10:(2,3),
     11:(2,3),12:(2,4),13:(2,3),14:(2,4),15:(3,2),16:(4,6),17:(3,7),18:(1,2),19:(2,3),20:(2,5),
     21:(None,2),22:(2,4),23:(2,6),24:(2,4),25:(2,3),26:(2,3),27:(2,3),28:(2,4),29:(4,5),30:(2,4),
     31:(2,3),32:(2,3),33:(2,3),34:(2,6),35:(2,3),36:(4,1),37:(2,5),38:(1,2),39:(2,3),40:(4,2),
     41:(2,3),42:(2,5),43:(3,1),44:(2,4),45:(2,5),46:(None,7),47:(2,5),48:(2,5),49:(5,1),50:(2,3),
     51:(2,5),52:(4,7),53:(4,3),54:(None,2),55:(None,1),56:(1,2),57:(2,5),58:(2,3),59:(1,2),60:(3,4),
     61:(2,4),62:(2,3),63:(1,2),64:(None,5),65:(2,3),66:(3,4),67:(1,3),68:(4,5),69:(2,3),70:(2,3),
     71:(3,2),72:(2,4),73:(None,5),74:(2,1),75:(None,1),76:(3,1),77:(2,3),78:(2,4),79:(None,2),80:(2,3),
     81:(4,3),82:(2,3),83:(None,1),84:(2,4),85:(2,5),86:(3,2),87:(2,3),88:(2,4),89:(3,2),90:(2,3),91:(2,3)}
idx = {r["n"]: r for r in json.load(open(sys.argv[1]))}
out = [dict(n=n, handle=idx[n]["handle"], title=idx[n]["title"], type=idx[n]["type"], worn=w, close=c) for n, (w, c) in sorted(P.items())]
json.dump(out, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
print(len(out), "products;", sum(1 for o in out if o["worn"]), "with an on-model photo")
