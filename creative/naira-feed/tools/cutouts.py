# Cut out every still-life (plinth) photo of the hero pieces with BiRefNet, so the designs can
# collage real product photography. Writes cutouts/<handle>/<idx>.png (full) and <idx>-trim.png (bbox-cropped),
# plus cutouts/index.json mapping each file to its source URL and alt text (alt names the stone/metal variant).
import json, os, sys, io, urllib.request
from PIL import Image
import onnxruntime as ort
_SO = ort.SessionOptions
class _Lean(_SO):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.enable_cpu_mem_arena = False
        self.enable_mem_pattern = False
ort.SessionOptions = _Lean
from rembg import remove, new_session
W = '/tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed'
handles = sys.argv[1].split(',')
roster = {p['handle']: p for p in json.load(open(f'{W}/research/roster.json'))}
idx_path = f'{W}/cutouts/index.json'
index = json.load(open(idx_path)) if os.path.exists(idx_path) else {}
s = new_session('birefnet-general')
for h in handles:
    p = roster.get(h)
    if not p: print('missing', h, flush=True); continue
    metas = [m for m in p.get('image_meta', []) if m.get('kind') in ('still_life', 'packshot', 'flatlay', 'still-life')]
    if not metas: metas = p.get('image_meta', [])[:1]
    os.makedirs(f'{W}/cutouts/{h}', exist_ok=True)
    for i, m in enumerate(metas):
        key = f'{h}/{i:02d}'
        if key in index: continue
        url = m['url'] + ('&' if '?' in m['url'] else '?') + 'width=1400'
        try:
            data = urllib.request.urlopen(url, timeout=60).read()
            im = Image.open(io.BytesIO(data)).convert('RGB')
            im.thumbnail((1400, 1400), Image.LANCZOS)
            out = remove(im, session=s, post_process_mask=True)
            out.save(f'{W}/cutouts/{key}.png')
            bb = out.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
            if bb:
                pad = 12; bb = (max(bb[0]-pad,0), max(bb[1]-pad,0), min(bb[2]+pad,out.width), min(bb[3]+pad,out.height))
                out.crop(bb).save(f'{W}/cutouts/{key}-trim.png')
            index[key] = {'handle': h, 'name': p['name'], 'src': m['url'], 'alt': m.get('alt'), 'size': im.size}
            json.dump(index, open(idx_path, 'w'), indent=1)
            print('ok', key, im.size, flush=True)
        except Exception as e:
            print('fail', key, e, flush=True)
