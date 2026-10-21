# Naira pop-up stories (1080×1920, WhatsApp status and Instagram Stories): Fashion Mantra Exhibition, Emerald Park, Nashik,
# Wednesday 21 October 2026. Three options, all within the Story safe zone (y 230–1680):
#   1 "The Arch"       a cream invitation: the Marquise Drop Choker shot in an arch, a coral TODAY seal, the details set like a card
#   2 "Come Say Hi"    the real stall photo as a taped polaroid on blush, marker note pointing at the table
#   3 "Admit All"      a cinema ticket to the pop-up over the wall of on-model pieces, marker TODAY!!
# Usage: popup.py  -> <scratchpad>/pop/out/naira-popup-<name>.jpg
import os, subprocess, sys
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "catalogue")))
import cards as C
import covers as V

HERE = os.path.dirname(os.path.abspath(__file__))
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/pop"
WORK, OUT = f"{SP}/work", f"{SP}/out"
STALL = f"{SP}/work/stall_clean.jpg"          # the stall photo with the hanging cable painted out
W, H = 1080, 1920
INK, PAPER, CORAL, PILL, MARK = "#1A1614", "#FFF8F5", "#B4513B", "#F0A08F", "#E2412B"
DAY, DATE, SHOW, VENUE = "Wednesday", "21 October", "Fashion Mantra", "Emerald Park, Nashik"

def stall_crop(aspect, size, name):
    from PIL import Image
    im = Image.open(STALL); w, h = im.size
    x0, x1 = 470, 1960; cw = x1 - x0; ch = cw / aspect; y0 = max(0, min(560 - ch * .26, h - ch))
    return C.cut(STALL, (x0, y0, cw, ch), size, name)[0]

def arch():
    x = V.head(W, H, .18) + f'<div class="a" style="inset:0;background:{PAPER}"></div>'
    x += f'<div class="a" style="inset:40px;border:1.5px solid rgba(26,22,20,.55)"></div><div class="a" style="inset:52px;border:.75px solid rgba(26,22,20,.35)"></div>'
    x += f'<img class="a" src="file://{C.BRAND}/logo_ink.png" style="left:{W / 2 - 220}px;top:236px;width:440px">'
    x += (f'<div class="a" style="left:0;right:0;top:356px;text-align:center;font:600 21px/1 Jost;letter-spacing:.62em;color:{CORAL};'
          f'margin-left:.31em">THE POP-UP</div>')
    p = V.photo("marquise-drop-choker", "worn", 1, (1520, 1520), fill=.62, ycen=.5, smin=.75, name="arch-photo", focus=False)
    ax, ay, aw, ah = 170, 420, 740, 760
    x += f'<div class="a" style="left:{ax - 16}px;top:{ay - 16}px;width:{aw + 32}px;height:{ah + 16}px;border:2px solid {PILL};border-bottom:0;border-radius:{(aw + 32) / 2}px {(aw + 32) / 2}px 0 0"></div>'
    x += (f'<div class="a" style="left:{ax}px;top:{ay}px;width:{aw}px;height:{ah}px;border-radius:{aw / 2}px {aw / 2}px 0 0;overflow:hidden;'
          f'box-shadow:0 30px 60px rgba(60,30,15,.22)"><img src="file://{p}" style="width:{aw}px;height:{ah}px;object-fit:cover"></div>')
    sx, sy, R = 880, 500, 118
    x += (f'<svg class="a" style="left:0;top:0;overflow:visible" width="{W}" height="{H}"><g transform="rotate(10 {sx} {sy})" style="filter:drop-shadow(0 14px 24px rgba(60,25,10,.35))">'
          f'<polygon points="{V.scallop(sx, sy, R, 22, .07)}" fill="{PILL}"/><circle cx="{sx}" cy="{sy}" r="{R - 18}" fill="none" stroke="{INK}" stroke-width="1.5" stroke-dasharray="2 6"/></g></svg>')
    x += (f'<div class="a" style="left:{sx - R}px;top:{sy - R}px;width:{2 * R}px;height:{2 * R}px;transform:rotate(10deg);display:flex;flex-direction:column;'
          f'align-items:center;justify-content:center;color:{INK}"><div style="font:50px/1 Velista">TODAY</div>'
          f'<div style="font:600 20px/1 Jost;letter-spacing:.24em;margin-top:8px;margin-left:.24em">21 · 10</div></div>')
    y = 1222
    x += f'<div class="a" style="left:0;right:0;top:{y}px;text-align:center;font:104px/1 Velista;color:{INK};font-variant-ligatures:none">FASHION MANTRA</div>'
    x += (f'<div class="a" style="left:0;right:0;top:{y + 116}px;text-align:center;font:600 22px/1 Jost;letter-spacing:.6em;color:{INK};margin-left:.3em">EXHIBITION</div>')
    x += (f'<svg class="a" style="left:{W / 2 - 150}px;top:{y + 162}px" width="300" height="20"><g stroke="{CORAL}" stroke-width="1.5" fill="{CORAL}">'
          f'<line x1="0" y1="10" x2="128" y2="10"/><line x1="172" y1="10" x2="300" y2="10"/><path d="M150,2 L158,10 L150,18 L142,10Z"/></g></svg>')
    x += f'<div class="a" style="left:0;right:0;top:{y + 196}px;text-align:center;font:500 italic 62px/1 CGI;color:{INK}">{DAY}, {DATE}</div>'
    x += f'<div class="a" style="left:0;right:0;top:{y + 282}px;text-align:center;font:500 30px/1 Jost;letter-spacing:.24em;color:{INK};text-transform:uppercase">{VENUE}</div>'
    x += f'<div class="a" style="left:0;right:0;top:{y + 344}px;text-align:center;font:500 italic 42px/1 CGI;color:{CORAL}">Come try every piece on.</div>'
    x += f'<div class="a" style="left:0;right:0;top:{y + 418}px;text-align:center;font:600 17px/1 Jost;letter-spacing:.34em;color:rgba(26,22,20,.6);margin-left:.17em">NAIRAFLORE.COM</div>'
    return x + '<div class="grain"></div>'

def say_hi():
    x = V.head(W, H, .2) + f'<div class="a" style="inset:0;background:#F6DCD2"></div>'
    x += f'<div class="a" style="inset:0;background:radial-gradient(ellipse at 50% 42%,rgba(255,248,245,.7),rgba(240,160,143,.35))"></div>'
    x += f'<img class="a" src="file://{C.BRAND}/logo_ink.png" style="left:{W / 2 - 180}px;top:236px;width:360px">'
    x += f'<div class="a" style="left:0;right:0;top:350px;text-align:center;font:600 24px/1 Jost;letter-spacing:.5em;color:{CORAL};margin-left:.25em">LIVE IN NASHIK</div>'
    x += f'<div class="a" style="left:0;right:0;top:396px;text-align:center;font:160px/.92 Velista;color:{INK}">SEE YOU<br>TODAY</div>'
    pw, ph = 800, 560
    p = stall_crop(pw / ph, (2 * pw, 2 * ph), "stall-polaroid")
    px, py, rot = (W - pw - 52) / 2, 732, -3
    x += (f'<div class="a" style="left:{px}px;top:{py}px;width:{pw + 52}px;padding:26px 26px 0;background:#FFFDF9;transform:rotate({rot}deg);'
          f'box-shadow:0 34px 60px rgba(70,25,15,.32),0 2px 6px rgba(70,25,15,.15)"><img src="file://{p}" style="width:{pw}px;height:{ph}px">'
          f'<div style="height:104px;display:flex;align-items:center;justify-content:center;font:42px/1 Marker;color:{INK}">the Naira table ♡</div></div>')
    x += V.tape(px - 34, py - 30, 210, 56, -28, 4) + V.tape(px + pw - 120, py - 40, 210, 56, 24, 9)
    svg = f'<svg class="a" style="left:0;top:0;overflow:visible" width="{W}" height="{H}"><g fill="none" stroke="{MARK}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">'
    svg += f'<path d="{V.arrow(720, 862, 560, 925, .25)}"/></g></svg>'
    x += svg + f'<div class="a" style="left:640px;top:792px;width:300px;text-align:center;font:44px/1 Marker;color:{MARK};transform:rotate(-6deg);text-shadow:0 2px 0 #FFFDF9">come say hi!</div>'
    y = 1492
    x += f'<div class="a" style="left:0;right:0;top:{y}px;text-align:center;font:700 29px/1 Jost;letter-spacing:.2em;color:{INK};margin-left:.1em">FASHION MANTRA EXHIBITION</div>'
    x += f'<div class="a" style="left:0;right:0;top:{y + 48}px;text-align:center;font:500 italic 58px/1 CGI;color:{INK}">{VENUE}</div>'
    x += (f'<div class="a" style="left:0;right:0;top:{y + 128}px;text-align:center"><span style="display:inline-block;padding:14px 26px 13px;background:{INK};'
          f'color:{PAPER};font:600 22px/1 Jost;letter-spacing:.3em">{DAY.upper()} · 21 OCT · TODAY</span></div>')
    return x + '<div class="grain"></div>'

def admit():
    x = V.head(W, H, .16) + f'<div class="a" style="inset:0;background:{PAPER}"></div>'
    cols, gap = 6, 4; tw = (W - gap * (cols + 1)) / cols
    tiles = [r for r in sorted(V.rows.values(), key=lambda r: r["n"]) if r["worn"]]
    import random; random.Random(11).shuffle(tiles)
    for i in range(cols * 11):
        r = tiles[i % len(tiles)]; c, rr = i % cols, i // cols
        tp = V.photo(r["handle"], "worn", 1, (300, 300), ycen=.5, name=f"tile-{r['handle']}")
        x += f'<img class="a" src="file://{tp}" style="left:{gap + c * (tw + gap):.1f}px;top:{gap + rr * (tw + gap):.1f}px;width:{tw:.1f}px;height:{tw:.1f}px">'
    x += '<div class="a" style="inset:0;background:radial-gradient(ellipse at 50% 50%,rgba(26,22,20,.55),rgba(26,22,20,.25) 60%,rgba(26,22,20,.12))"></div>'
    # top band
    x += (f'<div class="a" style="left:0;right:0;top:236px;height:84px;background:{INK};display:flex;align-items:center;justify-content:center;gap:26px">'
          f'<img src="file://{C.BRAND}/logo_white.png" style="width:220px"><span style="font:600 22px/1 Jost;letter-spacing:.42em;color:{PILL}">LIVE IN NASHIK</span></div>')
    # ticket
    tx, ty, tw2, th2 = 110, 520, 860, 860
    notch = "radial-gradient(circle at 0 60%,transparent 34px,#000 35px) left/51% 100% no-repeat,radial-gradient(circle at 100% 60%,transparent 34px,#000 35px) right/51% 100% no-repeat"
    x += (f'<div class="a" style="left:{tx}px;top:{ty}px;width:{tw2}px;height:{th2}px;transform:rotate(-4deg);filter:drop-shadow(0 34px 50px rgba(0,0,0,.5))">'
          f'<div style="position:absolute;inset:0;background:{PAPER};-webkit-mask:{notch};mask:{notch}"></div>'
          f'<div style="position:absolute;inset:22px;border:2px solid {INK};-webkit-mask:{notch};mask:{notch}"></div>'
          f'<div style="position:absolute;left:60px;right:60px;top:{th2 * .6 - 1}px;border-top:3px dashed rgba(26,22,20,.45)"></div>'
          f'<div style="position:absolute;left:0;right:0;top:66px;text-align:center;color:{INK}">'
          f'<div style="font:700 24px/1 Jost;letter-spacing:.56em;color:{CORAL};margin-left:.28em">ADMIT ALL</div>'
          f'<img src="file://{C.BRAND}/logo_ink.png" style="width:400px;margin:30px auto 0">'
          f'<div style="font:150px/1 Velista;margin-top:24px">POP-UP</div>'
          f'<div style="font:500 italic 40px/1 CGI;margin-top:14px">Seat: anywhere. Dress code: shiny.</div></div>'
          f'<div style="position:absolute;left:0;right:0;top:{th2 * .6 + 34}px;text-align:center;color:{INK}">'
          f'<div style="font:700 26px/1 Jost;letter-spacing:.18em">FASHION MANTRA EXHIBITION</div>'
          f'<div style="font:500 italic 56px/1 CGI;margin-top:18px">{VENUE}</div>'
          f'<div style="font:600 22px/1 Jost;letter-spacing:.28em;margin-top:22px">{DAY.upper()} · 21 OCTOBER 2026</div></div></div>')
    x += V.tape(tx - 20, ty + 10, 200, 54, -36, 5) + V.tape(tx + tw2 - 170, ty - 40, 200, 54, 30, 8)
    # marker TODAY!!
    x += (f'<div class="a" style="left:0;right:0;top:1440px;text-align:center;font:150px/1 Marker;color:{MARK};transform:rotate(-5deg);'
          f'text-shadow:0 4px 0 {PAPER},0 0 18px rgba(255,248,245,.85)">TODAY!!</div>')
    x += (f'<svg class="a" style="left:0;top:0;overflow:visible" width="{W}" height="{H}"><g fill="none" stroke="{MARK}" stroke-width="8" stroke-linecap="round">'
          f'<path d="M250,1628 C430,1600 650,1600 850,1585" style="filter:drop-shadow(0 2px 0 {PAPER})"/></g></svg>')
    return x + '<div class="grain"></div>'

DESIGNS = {"arch": arch, "say-hi": say_hi, "admit": admit}

def main(names):
    os.makedirs(WORK, exist_ok=True); os.makedirs(OUT, exist_ok=True); C.WORK = WORK; jobs = []
    for n in names:
        k = f"naira-popup-{n}"; open(f"{WORK}/{k}.html", "w").write(DESIGNS[n]() + "</body></html>"); jobs.append(f"{k}:{W}:{H}")
    subprocess.run(["node", f"{C.HERE}/render.cjs", WORK, *jobs], check=True, env=dict(os.environ, NODE_PATH="/opt/node-tools/node_modules"))
    for j in jobs:
        k = j.split(":")[0]; os.replace(f"{WORK}/{k}.jpg", f"{OUT}/{k}.jpg")
    print(len(jobs), "stories ->", OUT)

if __name__ == "__main__":
    main(sys.argv[1:] or list(DESIGNS))
