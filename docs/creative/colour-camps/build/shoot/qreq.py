import json,sys
Q=json.load(open(sys.argv[1])); a,b=int(sys.argv[2]),int(sys.argv[3])
print(json.dumps([{"index":i,"params":{"model":"nano_banana_pro","aspect_ratio":q['aspect'],"resolution":"2k","medias":[{"value":q['media'],"role":"image_references"}],"prompt":q['prompt']}} for i,q in enumerate(Q) if a<=i<b],ensure_ascii=False))
