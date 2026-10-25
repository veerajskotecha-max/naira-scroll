# Usage: python3 cut_file.py <src image> <out key, e.g. heartbead-bracelet/full>  -> cutouts/<key>.png + -trim.png
import sys, os, json
import onnxruntime as ort
_SO = ort.SessionOptions
class _Lean(_SO):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self.enable_cpu_mem_arena = False; self.enable_mem_pattern = False
ort.SessionOptions = _Lean
from PIL import Image
from rembg import remove, new_session
W = '/tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed'
s = new_session('birefnet-general')
pairs = sys.argv[1:]
idx = json.load(open(f'{W}/cutouts/index.json'))
for src, key in zip(pairs[::2], pairs[1::2]):
    im = Image.open(src).convert('RGB'); im.thumbnail((1600, 1600))
    out = remove(im, session=s, post_process_mask=True)
    os.makedirs(os.path.dirname(f'{W}/cutouts/{key}'), exist_ok=True)
    out.save(f'{W}/cutouts/{key}.png')
    bb = out.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
    out.crop((max(bb[0]-12,0), max(bb[1]-12,0), min(bb[2]+12,out.width), min(bb[3]+12,out.height))).save(f'{W}/cutouts/{key}-trim.png')
    idx[key] = {'handle': key.split('/')[0], 'name': key, 'src': src, 'alt': 'cut from local file', 'size': im.size}
    json.dump(idx, open(f'{W}/cutouts/index.json', 'w'), indent=1); print('ok', key, im.size, flush=True)
