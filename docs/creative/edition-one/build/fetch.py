# Download finished plates named <frame>_<attempt>.png into the scratch plates folder and write 1000px previews.
import json, sys, os, subprocess
from PIL import Image
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/e1"
os.makedirs(f"{SP}/plates", exist_ok=True); os.makedirs(f"{SP}/prev", exist_ok=True)
for a in sys.argv[1:]:          # name=url
    name, url = a.split("=", 1)
    out = f"{SP}/plates/{name}.png"
    if not os.path.exists(out):
        subprocess.run(["curl", "-sS", "-m", "180", "-o", out, url], check=True)
    im = Image.open(out); w, h = im.size
    s = 1000 / max(w, h); im.convert("RGB").resize((int(w * s), int(h * s)), Image.LANCZOS).save(f"{SP}/prev/{name}.jpg", quality=88)
    print(name, im.size)
