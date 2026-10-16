# Side-by-side check strip: supplier crop next to each generated shot. pair.py OUT.jpg REFNAME KEY [KEY...]
import sys, os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
dst, ref, keys = sys.argv[1], sys.argv[2], sys.argv[3:]
ims = [Image.open(f"{H}/refs/{ref}.jpg").convert("RGB")] + [Image.open(f"{H}/out/{k}.png").convert("RGB") for k in keys]
h = 700; ims = [i.resize((int(i.width * h / i.height), h)) for i in ims]
s = Image.new("RGB", (sum(i.width for i in ims) + 10 * len(ims), h), "white"); x = 0
for i in ims: s.paste(i, (x, 0)); x += i.width + 10
s.save(dst, quality=88)
