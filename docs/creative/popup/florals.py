# Botanical SVG elements in the Naira style (the carnation of the logo, leaf sprays, five-petal blossoms, buds), drawn as
# filled silhouettes so they read as graphic, not clip art. Each function returns an SVG group to place with a transform.
import math, random

def carnation(bloom="#B4513B", stem="#6E8E87", leaf="#99B4AE", seed=1):
    """A carnation sprig 200 wide × 420 tall, bloom at the top: ruffled cup, calyx, curved stem, two long leaves."""
    rnd = random.Random(seed); cx, cy, r = 100, 96, 66
    pts = []
    for i in range(23):                                   # ruffled top edge, left to right across the cup
        t = math.radians(198 + i * 144 / 22); rr = r * (1 if i % 2 == 0 else .8 + rnd.uniform(-.04, .04))
        pts.append((cx + rr * math.cos(t), cy + rr * math.sin(t)))
    d = f"M{cx - 30},{cy + 40} L{pts[0][0]:.1f},{pts[0][1]:.1f} "
    for i in range(1, len(pts) - 1, 2):
        d += f"Q{pts[i][0]:.1f},{pts[i][1]:.1f} {pts[i + 1][0]:.1f},{pts[i + 1][1]:.1f} "
    d += f"L{cx + 30},{cy + 40} Q{cx},{cy + 58} {cx - 30},{cy + 40}Z"
    inner = f"M{cx - 18},{cy + 30} Q{cx - 30},{cy - 22} {cx - 6},{cy - 40} M{cx + 18},{cy + 30} Q{cx + 30},{cy - 22} {cx + 8},{cy - 44} M{cx},{cy + 34} L{cx + 1},{cy - 50}"
    return (f'<g><path d="M{cx},{cy + 80} C{cx + 6},{cy + 170} {cx - 14},{cy + 250} {cx + 4},{cy + 324}" fill="none" stroke="{stem}" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M{cx - 2},{cy + 196} C{cx - 60},{cy + 150} {cx - 92},{cy + 120} {cx - 98},{cy + 74} C{cx - 70},{cy + 120} {cx - 30},{cy + 150} {cx - 2},{cy + 212}Z" fill="{leaf}"/>'
            f'<path d="M{cx + 2},{cy + 236} C{cx + 60},{cy + 196} {cx + 86},{cy + 160} {cx + 92},{cy + 116} C{cx + 66},{cy + 168} {cx + 34},{cy + 200} {cx + 2},{cy + 252}Z" fill="{leaf}" opacity=".85"/>'
            f'<path d="M{cx - 16},{cy + 42} L{cx},{cy + 92} L{cx + 16},{cy + 42}Z" fill="{stem}"/>'
            f'<path d="{d}" fill="{bloom}"/>'
            f'<path d="{inner}" fill="none" stroke="#FFF8F5" stroke-width="3" stroke-linecap="round" opacity=".55"/></g>')

def leaf_spray(n=7, color="#99B4AE", stem="#6E8E87", length=360, seed=2):
    """A curved stem with alternating almond leaves, growing up from (0,0) into negative y."""
    rnd = random.Random(seed); out = f'<path d="M0,0 C{length * .08},{-length * .4} {-length * .06},{-length * .7} {length * .05},{-length}" fill="none" stroke="{stem}" stroke-width="5" stroke-linecap="round"/>'
    for i in range(n):
        t = (i + 1) / (n + 1); y = -length * t; x = length * .05 * math.sin(t * 3)
        side = 1 if i % 2 else -1; L = 74 * (1.15 - t * .5) * rnd.uniform(.9, 1.1)
        out += (f'<path d="M0,0 C{L * .35},{-L * .22} {L * .75},{-L * .2} {L},0 C{L * .75},{L * .2} {L * .35},{L * .22} 0,0Z" fill="{color}" '
                f'transform="translate({x:.1f},{y:.1f}) rotate({-40 if side > 0 else -140} ) rotate({rnd.uniform(-8, 8):.1f})"/>')
    out += f'<path d="M{length * .05:.1f},{-length} c-12,-30 6,-46 0,-62 c-10,18 -14,40 0,62Z" fill="{color}"/>'
    return f"<g>{out}</g>"

def blossom(r=40, petal="#F0A08F", centre="#B4513B", n=5, rot=0):
    """A five-petal blossom centred on (0,0)."""
    out = ""
    for i in range(n):
        a = rot + i * 360 / n
        out += f'<ellipse cx="0" cy="{-r * .55:.1f}" rx="{r * .42:.1f}" ry="{r * .58:.1f}" fill="{petal}" transform="rotate({a:.1f})"/>'
    out += f'<circle r="{r * .24:.1f}" fill="{centre}"/>'
    for i in range(6):
        a = math.radians(i * 60 + rot); out += f'<circle cx="{r * .38 * math.cos(a):.1f}" cy="{r * .38 * math.sin(a):.1f}" r="{r * .05:.1f}" fill="{centre}"/>'
    return f"<g>{out}</g>"

def bud(color="#B4513B", stem="#6E8E87", h=120):
    return (f'<g><path d="M0,0 C4,{-h * .4} -4,{-h * .7} 0,{-h}" fill="none" stroke="{stem}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M0,{-h - 4} C-14,{-h - 14} -12,{-h - 40} 0,{-h - 50} C12,{-h - 40} 14,{-h - 14} 0,{-h - 4}Z" fill="{color}"/>'
            f'<path d="M-8,{-h + 2} L0,{-h - 14} L8,{-h + 2}Z" fill="{stem}"/></g>')

def place(svg, x, y, s=1, rot=0, op=1):
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})" opacity="{op}">{svg}</g>'

def sparkle(x, y, s, color="#B4513B"):
    return (f'<path transform="translate({x},{y}) scale({s / 50})" d="M0,-50 C5,-8 8,-5 50,0 C8,5 5,8 0,50 C-5,8 -8,5 -50,0 C-8,-5 -5,-8 0,-50Z" fill="{color}"/>')
