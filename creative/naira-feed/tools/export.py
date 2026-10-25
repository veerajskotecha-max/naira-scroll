# Usage: python3 export.py <slide@2x.png> ...
# From each 2160x2880 render writes: <name>.jpg (1080x1440 3:4 master, q93 4:4:4), <name>-45.jpg (1080x1350 centre crop,
# for schedulers that only take 4:5), <name>-thumb.png (391x521, the tile as it shows in the grid on a phone)
import sys
from PIL import Image
for p in sys.argv[1:]:
    im = Image.open(p).convert('RGB')
    w, h = im.size
    m = im.resize((w // 2, h // 2), Image.LANCZOS)
    base = p.replace('@2x.png', '')
    m.save(base + '.jpg', 'JPEG', quality=93, subsampling=0, optimize=True)
    W, H = m.size
    if abs(H / W - 4 / 3) < 0.01:
        m.crop((0, 45, W, H - 45)).save(base + '-45.jpg', 'JPEG', quality=93, subsampling=0, optimize=True)
    t = m.copy(); t.thumbnail((391, 521), Image.LANCZOS); t.save(base + '-thumb.png')
    print(base, m.size)
