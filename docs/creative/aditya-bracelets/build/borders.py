# Measures white "paper edge" strips the model sometimes paints along a frame's sides; export.py crops them away.
import numpy as np, sys, json
from PIL import Image
def border(path, maxw=60):
    a = np.asarray(Image.open(path).convert("RGB")).astype(float)
    mx, mn = a.max(-1), a.min(-1); white = (mx > 222) & ((mx - mn) < 30)
    def run(cols):
        w = 0
        for i, col in enumerate(cols):
            if col.mean() > 0.45: w = i + 1
            elif i > w + 6: break
        return w
    L = run([white[:, i] for i in range(maxw)]); R = run([white[:, -1 - i] for i in range(maxw)])
    T = run([white[i, :] for i in range(maxw)]); B = run([white[-1 - i, :] for i in range(maxw)])
    return {"L": L, "R": R, "T": T, "B": B}
if __name__ == "__main__":
    out = {}
    for k in sys.argv[1:]:
        out[k] = border(f"out/{k}.png"); print(k, out[k])
