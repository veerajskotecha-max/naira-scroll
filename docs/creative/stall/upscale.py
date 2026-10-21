# 4× upscale for print with Real-ESRGAN x4plus (ONNX, fixed 64-px tiles), tiled with feathered overlap, then blended
# with a plain Lanczos 4× so the network sharpens edges without repainting texture (stones, pavé, skin stay as shot).
# Usage: <venv>/bin/python upscale.py <model.onnx> <blend 0..1, share of the network> <in.jpg> <out.jpg> [...pairs]
import sys
import numpy as np, onnxruntime as ort
from PIL import Image

T, O, S = 64, 12, 4                                  # tile, overlap, scale

def run(sess, img):
    a = np.asarray(img, dtype=np.float32) / 255.0; h, w, _ = a.shape
    pad = np.pad(a, ((O, O + T), (O, O + T), (0, 0)), mode="reflect")
    out = np.zeros(((h + 2 * O + T) * S, (w + 2 * O + T) * S, 3), np.float32); wt = np.zeros(out.shape[:2], np.float32)
    ramp = np.minimum(np.arange(T * S) + 1, np.arange(T * S)[::-1] + 1).astype(np.float32)
    win = np.minimum(np.outer(ramp, ramp), (O * S) ** 2) / (O * S) ** 2 + 1e-4
    name = sess.get_inputs()[0].name; step = T - 2 * O
    for y in range(0, h + 2 * O, step):
        for x in range(0, w + 2 * O, step):
            t = pad[y:y + T, x:x + T]
            if t.shape[0] < T or t.shape[1] < T: continue
            r = sess.run(None, {name: t.transpose(2, 0, 1)[None]})[0][0].transpose(1, 2, 0)
            out[y * S:(y + T) * S, x * S:(x + T) * S] += r * win[..., None]; wt[y * S:(y + T) * S, x * S:(x + T) * S] += win
    out = out / wt[..., None]
    out = out[O * S:(O + h) * S, O * S:(O + w) * S]
    return Image.fromarray((np.clip(out, 0, 1) * 255 + .5).astype(np.uint8))

if __name__ == "__main__":
    sess = ort.InferenceSession(sys.argv[1], providers=["CPUExecutionProvider"]); k = float(sys.argv[2])
    args = sys.argv[3:]
    for i in range(0, len(args), 2):
        im = Image.open(args[i]).convert("RGB")
        net = run(sess, im); lz = im.resize(net.size, Image.LANCZOS)
        Image.blend(lz, net, k).save(args[i + 1], quality=95, subsampling=0); print(args[i + 1], net.size)
