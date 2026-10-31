# Exports the approved frames of the two pieces listed on 30 Oct 2026 at the live listing size (1288x1600 JPEG), after the
# house 1.5% inset crop (as ../../aditya-bracelets/build/export.py):
#   ../exports/clover-garland-bracelet-01..12.jpg: Sky Blue, Pink, White, each hero, worn, worn close, macro;
#   ../../tennis-necklace/exports/riviere-classique-necklace-01..08.jpg: Silver, then Gold, each hero, worn, worn turned, macro.
# Usage: python3 -I export.py [clover|necklace]
import os, sys
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, "../../tennis-necklace/build/out")
CLOVER = [f"{H}/out/{k}{c}.png" for c in ("", "_pink", "_white") for k in ("C1_H_b", "C1_W1c", "C1_W2", "C1_M")]
NECKLACE = [f"{T}/{k}.png" for k in ("T1_H_c", "T1_W1r", "T1_W2r", "T1_M", "T1g_H", "T1g_W1", "T1g_W2", "T1g_M")]
JOBS = {"clover": (CLOVER, f"{H}/../exports/clover-garland-bracelet"),
        "necklace": (NECKLACE, f"{H}/../../tennis-necklace/exports/riviere-classique-necklace")}

def export(src, dst, inset=0.015):
    im = Image.open(src).convert("RGB"); w, h = im.size; dx, dy = round(w * inset), round(h * inset)
    im.crop((dx, dy, w - dx, h - dy)).resize((1288, 1600), Image.LANCZOS).save(dst, quality=92, optimize=True, progressive=True)

if __name__ == "__main__":
    for name in sys.argv[1:] or JOBS:
        frames, stem = JOBS[name]
        for i, src in enumerate(frames, 1):
            export(src, f"{stem}-{i:02d}.jpg")
        print(name, len(frames), "exported")
