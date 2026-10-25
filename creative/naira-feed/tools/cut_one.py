# Usage: python3 cut_one.py <handle> <img-index> [<img-index> ...]  -> cutouts/<handle>/x<idx>.png + -trim.png, appended to index.json
import json, sys, io, urllib.request, os
import onnxruntime as ort
_SO = ort.SessionOptions
class _Lean(_SO):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self.enable_cpu_mem_arena = False; self.enable_mem_pattern = False
ort.SessionOptions = _Lean
from PIL import Image
from rembg import remove, new_session
W = '/tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed'
h = sys.argv[1]; ids = [int(x) for x in sys.argv[2:]]
p = {q['handle']: q for q in json.load(open(f'{W}/research/roster.json'))}[h]
idx_path = f'{W}/cutouts/index.json'; index = json.load(open(idx_path))
s = new_session('birefnet-general'); os.makedirs(f'{W}/cutouts/{h}', exist_ok=True)
for i in ids:
    m = p['image_meta'][i]; url = m['url'] + ('&' if '?' in m['url'] else '?') + 'width=1400'
    im = Image.open(io.BytesIO(urllib.request.urlopen(url, timeout=60).read())).convert('RGB'); im.thumbnail((1400, 1400))
    out = remove(im, session=s, post_process_mask=True); key = f'{h}/x{i:02d}'
    out.save(f'{W}/cutouts/{key}.png')
    bb = out.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
    if bb: out.crop((max(bb[0]-12,0), max(bb[1]-12,0), min(bb[2]+12,out.width), min(bb[3]+12,out.height))).save(f'{W}/cutouts/{key}-trim.png')
    index[key] = {'handle': h, 'name': p['name'], 'src': m['url'], 'alt': m.get('alt'), 'size': im.size}
    json.dump(index, open(idx_path, 'w'), indent=1); print('ok', key, im.size, flush=True)
