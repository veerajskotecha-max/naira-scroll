# "See you today" story (1080×1920) from the seated stall photo: her and the table cut out (cut_seated.py), set in a cream
# arch on a blush ground. A low bed of sage leaves and blush blossoms runs along the back edge of the trays, between her
# layer and the table layer, so it hides where the chair was. Quieter than the first version: muted florals, serif note.
# Usage: popup_seated.py -> <scratchpad>/pop2/out/naira-popup-seated.jpg
import math, os, random, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.normpath(f"{HERE}/../catalogue"))
import cards as C
import covers as V
import florals as F

SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/pop2"
W, H = 1080, 1920
INK, PAPER, CORAL, ROSE, BLUSH, SAGE, SAGE2, STEM = "#1A1614", "#FFF8F5", "#B4513B", "#D99485", "#F2C9BE", "#99B4AE", "#B9CCC6", "#6E8E87"
CUT_W, CUT_H, CUT_X0, CUT_Y0 = 879, 1160, 300, 740       # the layers are photo x 300–1179, y 740–1900
S = W / CUT_W; TOP = 600; OX = 67                         # layer scale, and where its top-left sits on the story

def line_y(x):                                            # back edge of the trays on the story, left to right
    return TOP + (612 - (x - OX) / S * (612 - 456) / 690) * S

def bed(seed=3):
    """Leaf sprays and blossoms along the tray edge, rising up to ~170 px above it."""
    rnd = random.Random(seed); out = ""
    for i in range(16):
        x = -30 + i * 62 + rnd.uniform(-14, 14); y = line_y(max(x, 0)) + 26
        out += F.place(F.leaf_spray(n=6, color=SAGE if i % 2 else SAGE2, stem=STEM, length=rnd.uniform(130, 180), seed=seed + i),
                       round(x), round(y), rnd.uniform(.62, .85), rnd.uniform(-34, 34))
    for i in range(11):
        x = 30 + i * 88 + rnd.uniform(-18, 18); y = line_y(max(x, 0)) - rnd.uniform(26, 80)
        r = rnd.uniform(15, 24); petal = [BLUSH, PAPER, ROSE][i % 3]
        out += F.place(F.blossom(r, petal, CORAL if petal != ROSE else "#9E4A38", rot=rnd.uniform(0, 70)), round(x), round(y))
    for (bx, by, sc, rot) in [(610, 0, .7, -20), (660, -10, .62, 24), (560, 10, .66, 8)]:
        out += F.place(F.leaf_spray(n=5, color=SAGE2, stem=STEM, length=150, seed=bx), bx, round(line_y(bx) + by), sc, rot)
    for (bx, by, sc, rot) in [(700, 1112, .5, -12), (735, 1100, .46, 30), (430, 1118, .5, 16), (470, 1120, .46, -24)]:
        out += F.place(F.leaf_spray(n=5, color=SAGE, stem=STEM, length=150, seed=bx + 1), bx, by, sc, rot)
    out += F.place(F.blossom(23, BLUSH, CORAL, rot=20), 694, 1036) + F.place(F.blossom(15, PAPER, CORAL, rot=50), 664, 1058)
    out += F.place(F.leaf_spray(n=5, color=SAGE2, stem=STEM, length=140, seed=77), 690, 1090, .5, -6)
    out += F.place(F.blossom(17, ROSE, "#9E4A38", rot=5), 430, 1070)
    for i in range(5):
        x = 60 + i * 200 + rnd.uniform(-30, 30); y = line_y(max(x, 0)) - 40
        out += F.place(F.bud(color=ROSE, stem=STEM, h=rnd.uniform(90, 130)), round(x), round(y), 1, rnd.uniform(-16, 16))
    return out

def carn(x, y, s, rot, **k):
    return F.place(f'<g transform="translate(-104,-420)">{F.carnation(**k)}</g>', x, y, s, rot)

def story():
    x = V.head(W, H, .12) + f'<div class="a" style="inset:0;background:linear-gradient(#FFF8F5,#FBEDE6 40%,#F5DCD2)"></div>'
    lw = 300; x += f'<img class="a" src="file://{C.BRAND}/logo_ink.png" style="left:{W / 2 - lw / 2}px;top:236px;width:{lw}px">'
    x += f'<div class="a" style="left:0;right:0;top:330px;text-align:center;font:600 20px/1 Jost;letter-spacing:.5em;color:{CORAL};margin-left:.25em">LIVE IN NASHIK</div>'
    x += f'<div class="a" style="left:0;right:0;top:372px;text-align:center;font:112px/1 Velista;color:{INK};font-variant-ligatures:none">SEE YOU TODAY</div>'
    x += f'<div class="a" style="left:0;right:0;top:494px;text-align:center;font:400 italic 40px/1 CGI;color:{INK}">at the Fashion Mantra Exhibition</div>'
    # arch behind her
    aw, ay = 640, 600; ax = (W - aw) / 2; ah = 640
    x += f'<div class="a" style="left:{ax - 14}px;top:{ay - 14}px;width:{aw + 28}px;height:{ah + 14}px;border:1.5px solid {ROSE};border-bottom:0;border-radius:{(aw + 28) / 2}px {(aw + 28) / 2}px 0 0;opacity:.7"></div>'
    x += f'<div class="a" style="left:{ax}px;top:{ay}px;width:{aw}px;height:{ah}px;border-radius:{aw / 2}px {aw / 2}px 0 0;background:radial-gradient(ellipse at 50% 35%,#FFFDFB,#FBEFE9)"></div>'
    back = (carn(ax - 30, 1150, .82, -12, bloom=ROSE, stem=STEM, leaf=SAGE, seed=3) + carn(ax + aw + 30, 1140, .78, 12, bloom=BLUSH, stem=STEM, leaf=SAGE, seed=5)
            + F.place(F.leaf_spray(seed=11, color=SAGE2, stem=STEM, length=300), ax - 70, 1120, .9, -26)
            + F.place(F.leaf_spray(seed=12, color=SAGE2, stem=STEM, length=300), ax + aw + 70, 1110, .9, 26))
    x += f'<svg class="a" style="left:0;top:0;overflow:visible" width="{W}" height="{H}">{back}</svg>'
    lay = f"left:{OX}px;top:{TOP}px;width:{CUT_W * S:.0f}px;height:{CUT_H * S:.0f}px"
    x += f'<img class="a" src="file://{SP}/person.png" style="{lay};filter:drop-shadow(0 14px 22px rgba(90,40,25,.14))">'
    x += f'<svg class="a" style="left:0;top:0;overflow:visible" width="{W}" height="{H}">{bed()}</svg>'
    x += f'<img class="a" src="file://{SP}/table.png" style="{lay}">'
    # note
    x += (f'<svg class="a" style="left:0;top:0;overflow:visible" width="{W}" height="{H}"><path d="{V.arrow(770, 672, 575, 708, -.28)}" fill="none" '
          f'stroke="{CORAL}" stroke-width="3" stroke-linecap="round"/></svg>'
          f'<div class="a" style="left:700px;top:616px;width:330px;text-align:center;font:500 italic 46px/1 CGI;color:{CORAL};transform:rotate(-4deg)">come say hi</div>')
    # scalloped card
    top = 1452; sc = ""
    for i in range(19):
        cx = i * 60; sc += f"{'M' if i == 0 else 'L'}{cx},{top + 14} A30,30 0 0 1 {cx + 60},{top + 14} "
    card = f'<path d="{sc} L1080,1920 L0,1920Z" fill="#FFF8F5"/><path d="M90,{top + 42} L990,{top + 42}" stroke="{BLUSH}" stroke-width="1.5"/>'
    front = (F.place(F.leaf_spray(seed=21, color=SAGE, stem=STEM, length=220), 30, 1470, .9, 18) + F.place(F.blossom(26, BLUSH, CORAL, rot=8), 40, 1330)
             + F.place(F.leaf_spray(seed=8, color=SAGE, stem=STEM, length=260), 70, 1560, .75, 54) + F.place(F.leaf_spray(seed=9, color=SAGE2, stem=STEM, length=260), 1010, 1560, .75, -54)
             + F.place(F.blossom(34, ROSE, "#9E4A38", rot=12), 96, 1466) + F.place(F.blossom(24, BLUSH, CORAL, rot=40), 156, 1500)
             + F.place(F.blossom(34, BLUSH, CORAL, rot=24), 984, 1464) + F.place(F.blossom(22, ROSE, "#9E4A38", rot=4), 926, 1502))
    x += f'<svg class="a" style="left:0;top:0;overflow:visible;filter:drop-shadow(0 -8px 18px rgba(90,40,25,.10))" width="{W}" height="{H}">{card}</svg>'
    x += f'<svg class="a" style="left:0;top:0;overflow:visible" width="{W}" height="{H}">{front}</svg>'
    y = 1528
    x += f'<div class="a" style="left:0;right:0;top:{y}px;text-align:center;font:700 27px/1 Jost;letter-spacing:.2em;color:{INK};margin-left:.1em">FASHION MANTRA EXHIBITION</div>'
    x += f'<div class="a" style="left:0;right:0;top:{y + 44}px;text-align:center;font:500 italic 60px/1 CGI;color:{INK}">Emerald Park, Nashik</div>'
    x += (f'<div class="a" style="left:0;right:0;top:{y + 128}px;text-align:center"><span style="display:inline-block;padding:13px 24px 12px;background:{INK};'
          f'color:{PAPER};font:600 21px/1 Jost;letter-spacing:.3em">WEDNESDAY · 21 OCT · TODAY</span></div>')
    return x + '<div class="grain"></div></body></html>'

if __name__ == "__main__":
    work, out = f"{SP}/work", f"{SP}/out"; os.makedirs(work, exist_ok=True); os.makedirs(out, exist_ok=True)
    open(f"{work}/naira-popup-seated.html", "w").write(story())
    subprocess.run(["node", f"{C.HERE}/render.cjs", work, f"naira-popup-seated:{W}:{H}"], check=True, env=dict(os.environ, NODE_PATH="/opt/node-tools/node_modules"))
    os.replace(f"{work}/naira-popup-seated.jpg", f"{out}/naira-popup-seated.jpg"); print("ok")
