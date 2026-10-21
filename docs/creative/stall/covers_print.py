# The three catalogue covers (The Wall, Now Showing, The Naira Times) as the back-wall posters of the stall, 24 × 36 in.
# Uses the covers' own "2x3" layout (1080×1620 CSS px), zoomed 2304/1080 so the PDF comes out at exactly 24 × 36 in, with
# every photo cut at 150 ppi for that size. Crops that would be enlarged more than 1.6× go through upscale.py (Real-ESRGAN
# blended 65/35 with Lanczos) first; the CHAMAK photo is pre-upscaled in full. No bleed, no crop marks: trim size only.
# Usage: covers_print.py [wall|poster|times ...] -> <scratchpad>/stall/out/Naira-Stall-back-<n>-<name>-24x36in.{pdf,jpg}
import os, subprocess, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.normpath(f"{HERE}/../catalogue"))
import cards as C
import covers as V
import posters as P

SP = P.SP; SR_DIR = f"{SP}/sr"; WORK = f"{SP}/stall/work/covers"
ZOOM = 2304 / 1080
NAMES = [("wall", 1, "the-wall"), ("poster", 2, "now-showing"), ("times", 3, "naira-times")]

def upscale(src, dst):
    subprocess.run([f"{SP}/venv/bin/python", f"{HERE}/upscale.py", f"{SR_DIR}/realesrgan_x4.onnx", "0.65", src, dst], check=True,
                   capture_output=True)

def sr(path, rect, px, name):
    out = f"{WORK}/{name}.jpg"
    if os.path.exists(out) and Image.open(out).size == px: return out
    x0, y0, w, h = rect; im = Image.open(path).convert("RGB")
    crop = im.crop((round(x0), round(y0), round(x0 + w), round(y0 + h)))
    a, b = f"{SR_DIR}/in/{name}.jpg", f"{SR_DIR}/out/{name}-x4.jpg"
    os.makedirs(os.path.dirname(a), exist_ok=True); os.makedirs(os.path.dirname(b), exist_ok=True)
    if not os.path.exists(b): crop.save(a, quality=97, subsampling=0); upscale(a, b)
    Image.open(b).resize(px, Image.LANCZOS).save(out, quality=94, subsampling=0); return out

def main(want):
    os.makedirs(WORK, exist_ok=True); os.makedirs(P.WORK, exist_ok=True)
    hero = f"{C.SRC}/full/verdant-drop-earrings-worn.jpg"; hero4 = f"{SR_DIR}/out/verdant-drop-earrings-worn-x4.jpg"
    if not os.path.exists(hero4): upscale(hero, hero4)
    C.WORK = WORK; V.RES = 150 / 96 * ZOOM; V.UP = {hero: hero4}; V.SR = sr; V.QR = P.qr_svg
    jobs = []
    for key, n, label in NAMES:
        if want and key not in want: continue
        page = V.BUILDERS[key]("2x3") + "</body></html>"
        page = page.replace("</style></head>", f"html{{zoom:{ZOOM:.6f}}}</style></head>", 1)
        k = f"Naira-Stall-back-{n}-{label}-24x36in"; open(f"{P.WORK}/{k}.html", "w").write(page); jobs.append(k)
    env = dict(os.environ, NODE_PATH="/opt/node-tools/node_modules")
    subprocess.run(["node", f"{HERE}/render_print.cjs", P.WORK, P.OUT, *jobs], check=True, env=env)
    print(len(jobs), "back-wall posters ->", P.OUT)

if __name__ == "__main__":
    main(sys.argv[1:])
