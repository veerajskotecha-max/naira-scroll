# Downloads finished job images: fetch.py KEY=URL ... into out/KEY.png and prints sizes.
import sys, subprocess, os
from PIL import Image
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
for a in sys.argv[1:]:
    k, u = a.split("=", 1); p = os.path.join(out, k + ".png")
    subprocess.run(["curl", "-sS", "-o", p, u], check=True)
    print(k, Image.open(p).size)
