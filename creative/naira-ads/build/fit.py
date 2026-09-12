#!/usr/bin/env python3
"""
Measure every display line in Velista at its real size against the width its architecture
actually gives it. Eyeballing a contact sheet catches a line that overflows by 30%; it does not
catch one that overflows by 4%, and a 4% overflow is a clipped final letter, which reads as a
production error rather than as a bleed.
"""
import json, pathlib, sys
from PIL import ImageFont

ROOT = pathlib.Path(__file__).parent
FONT = str(ROOT / "fonts" / "Velista-400.ttf")
W = 1080
GUT = 6.0
_f = {}


def wid(txt, px):
    if px not in _f:
        _f[px] = ImageFont.truetype(FONT, int(px))
    b = _f[px].getbbox(txt)
    return b[2] - b[0]


def avail(s):
    """The width each architecture leaves the display line, in px."""
    lay = s["layout"]
    full = (100 - 2 * GUT) / 100 * W
    if lay == "specimen":
        return s.get("footw", 60) / 100 * W
    if lay == "angled":
        return s.get("tw", 70) / 100 * W
    if lay == "ticker":
        return 48 / 100 * W
    if lay == "zoom":
        return s.get("tw", 56) / 100 * W
    if lay == "margin":
        return (s["col"] - GUT - 5) / 100 * W
    if lay == "side":
        return (s["col"] - GUT - 6) / 100 * W
    if lay == "archw":
        return 64 / 100 * W
    if lay == "card":
        return (s["card"][2] - 12) / 100 * W
    if lay == "overprint":
        return (100 - 2 * abs(s["x"])) / 100 * W if s["x"] < 0 else (100 - s["x"] - 2) / 100 * W
    if lay == "vertical":
        return 1e9                      # the constraint is height, checked separately
    return full


def run(path):
    specs = json.loads(pathlib.Path(path).read_text())
    bad = 0
    print(f"{'id':<5}{'layout':<11}{'size':>5}{'widest':>8}{'avail':>7}   line")
    for s in specs:
        lines = s.get("lines", [])
        px = s.get("size") or s.get("sub", 60)
        if s["layout"] == "numeral":
            px = s.get("sub", 60)
        a = avail(s)
        if not lines:
            continue
        ws = [wid(l, px) for l in lines]
        i = ws.index(max(ws))
        over = max(ws) > a
        if s["layout"] == "vertical":
            # a climbing line is bounded by the canvas height minus the two margins it must clear
            a = (100 - s["y"] - 12) / 100 * 1350
            over = max(ws) > a
        if over:
            bad += 1
        print(f"{s['id']:<5}{s['layout']:<11}{px:>5}{max(ws):>8}{int(a):>7}   {lines[i]}"
              + ("   << OVERFLOW" if over else ""))
        # rag: line 1 widest, last narrowest - only meaningful for a real multi-line setting
        if len(ws) > 2 and (ws[0] != max(ws) or ws[-1] != min(ws)):
            print(f"     rag: {ws}   << line 1 must be widest, last narrowest")
    print(f"\n{len(specs)-bad}/{len(specs)} fit")


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else ROOT / "ads.json")
