#!/usr/bin/env python3
"""
Pixel QA across twenty-one different architectures.

Measuring contrast from a declared type box only works when every creative has one. These do not:
a line reverses out of a band, sits on paper, crosses a photograph, or is clipped inside a figure.
So each creative is rendered twice - once normally, once with every glyph made transparent - and
the two are differenced. Grounds, rules, borders and chips are identical in both passes, so the
difference is exactly the marks and the pixels immediately under them.

Two earlier versions of this script were wrong in instructive ways and both said the work was
failing when it was not:

  1. It hid elements with visibility:hidden, which also removed a CTA chip's own ink ground. The
     diff then compared cream type against the cream tray behind the chip and reported 1:1.
  2. It tested each pixel on its own. An antialiased glyph edge is a blend of ink and paper, and a
     half-covered pixel measures about 2:1 against the paper by arithmetic alone - no matter how
     black the type is. Every creative "failed" at roughly the share of its glyph area that is edge.

Contrast is a property of two COLOURS, not of a blend, so marks are grouped into blocks, and each
block is measured once: its nominal ink (the colour of its most-covered pixels) against the ground
those pixels actually sit on.
"""
import json, pathlib, sys
import numpy as np
from PIL import Image

W, H = 1440, 1800
GUT = 0.06
CELL = 12          # coarse grid for grouping marks into blocks
GROW = 2           # cells of dilation: joins letters into lines and lines into a block


def _lin(c):
    c = np.asarray(c, dtype=float) / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def lum(a):
    a = _lin(a)
    return 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]


def ratio(a, b):
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def blocks(mask):
    """Label connected groups of marks on a coarse, dilated grid. Pure numpy + a flood fill;
    the grid is 120x150 cells, so a Python loop over it costs nothing."""
    gh, gw = mask.shape[0] // CELL, mask.shape[1] // CELL
    g = mask[:gh * CELL, :gw * CELL].reshape(gh, CELL, gw, CELL).any(axis=(1, 3))
    d = g.copy()
    for _ in range(GROW):                       # dilate
        d[1:] |= d[:-1].copy(); d[:-1] |= d[1:].copy()
        d[:, 1:] |= d[:, :-1].copy(); d[:, :-1] |= d[:, 1:].copy()
    lab = np.zeros((gh, gw), dtype=int)
    cur = 0
    for y0 in range(gh):
        for x0 in range(gw):
            if not d[y0, x0] or lab[y0, x0]:
                continue
            cur += 1
            stack = [(y0, x0)]
            lab[y0, x0] = cur
            while stack:
                y, x = stack.pop()
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < gh and 0 <= nx < gw and d[ny, nx] and not lab[ny, nx]:
                        lab[ny, nx] = cur
                        stack.append((ny, nx))
    full = np.repeat(np.repeat(lab, CELL, axis=0), CELL, axis=1)
    out = np.zeros(mask.shape, dtype=int)
    out[:full.shape[0], :full.shape[1]] = full
    return out * mask, cur


def run(specs, live, bare, verbose=False):
    print(f"{'id':<6}{'blocks':>7}{'worst':>7}{'gutL':>7}{'gutR':>7}{'top':>6}{'bot':>6}  flags")
    bad = 0
    for s in specs:
        f1, f2 = pathlib.Path(live) / f"{s['id']}.png", pathlib.Path(bare) / f"{s['id']}.png"
        if not (f1.exists() and f2.exists()):
            print(f"{s['id']:<6}  MISSING"); bad += 1; continue
        a = np.asarray(Image.open(f1).convert("RGB"), dtype=float)
        b = np.asarray(Image.open(f2).convert("RGB"), dtype=float)
        la_all, lb_all = lum(a), lum(b)
        d = np.abs(la_all - lb_all)
        mask = d >= 0.035                       # any mark at all, edges included
        lab, n = blocks(mask)

        worst, worstid = 99.0, None
        rows = []
        for k in range(1, n + 1):
            m = lab == k
            if m.sum() < 400:                   # a rule, a dot, a stray - not a run of type
                continue
            # split by polarity before measuring: a CTA chip's cream letters and the ink caption
            # 26px above it can fall in one block, and averaging the two gives mid-grey against
            # mid-grey - a 1.5:1 reading for two runs that are each about 15:1.
            for pol in (1, -1):
                sub = m & (((lb_all - la_all) * pol) > 0)
                if sub.sum() < 300:
                    continue
                core = sub & (d >= 0.88 * d[sub].max())   # most-covered pixels: the nominal ink
                if core.sum() < 60:
                    continue
                fg, bg = lum(a[core].mean(0)), lum(b[core].mean(0))
                r = ratio(fg, bg)
                ys, xs = np.where(sub)
                rows.append((r, k, xs.min() / W, ys.min() / H, int(sub.sum())))
                if r < worst:
                    worst, worstid = r, k
        ys, xs = np.where(mask)
        gl, gr = xs.min() / W, 1 - xs.max() / W
        tp, bt = ys.min() / H, 1 - ys.max() / H
        bleed = s.get("bleed", [])
        flags = []
        if worst < 4.5:
            flags.append(f"CONTRAST {worst:.1f}:1")
        if gl < GUT - 1e-3 and "L" not in bleed: flags.append("GUTTER-L")
        if gr < GUT - 1e-3 and "R" not in bleed: flags.append("GUTTER-R")
        if tp < 0.035 and "T" not in bleed: flags.append("TOP")
        if bt < 0.035 and "B" not in bleed: flags.append("BOTTOM")
        if flags:
            bad += 1
        print(f"{s['id']:<6}{len(rows):>7}{worst:>7.1f}{gl:>7.3f}{gr:>7.3f}{tp:>6.3f}{bt:>6.3f}  "
              + (", ".join(flags) if flags else "ok"))
        if verbose or flags:
            for r, k, x, y, px in sorted(rows)[:4]:
                print(f"        block at ({x:.2f},{y:.2f})  {px:>6}px  {r:5.1f}:1")
    print(f"\n{len(specs)-bad}/{len(specs)} clean")


if __name__ == "__main__":
    specs = json.loads(pathlib.Path(sys.argv[1]).read_text())
    run(specs, sys.argv[2], sys.argv[3], "-v" in sys.argv)
