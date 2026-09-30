"""Vector florals for the NAIRA bag and card, drawn in a local 100-unit space (1 unit = s/100 inch).
The tulip is five petals - two at the back for depth, two curling out, one tall in front with a
soft highlight - so it reads as a bloom rather than a three-lobed blob. Leaves are long tulip
blades with a vein; buds are the closed form of the same flower."""

# brand-tuned palette
CREAM = "#FBF5F0"
CORAL, CORAL_DEEP, CORAL_LIGHT, CORAL_BACK = "#F6AE96", "#EC957A", "#FBCCBA", "#E4886F"
SAGE, SAGE_DEEP, SAGE_LIGHT = "#9DB5AD", "#7F9A91", "#BBCDC6"
INK = "#3D3530"
LOGO_SAGE, LOGO_BLUSH = "#99B4AF", "#FFBDA8"


def tulip(x, y, s, rot=0, op=1.0, main=CORAL, deep=CORAL_DEEP, light=CORAL_LIGHT, back=CORAL_BACK):
    """Open tulip; base of the bloom at (x, y) inches, pointing up before rotation."""
    return f"""<g transform="translate({x},{y}) rotate({rot}) scale({s/100}) translate(0,30)" opacity="{op}">
  <path d="M-2,-36 C-24,-46 -36,-70 -27,-94 C-17,-84 -8,-70 -2,-54 Z" fill="{back}"/>
  <path d="M2,-36 C24,-46 36,-70 27,-94 C17,-84 8,-70 2,-54 Z" fill="{back}"/>
  <path d="M0,-32 C-30,-36 -46,-62 -35,-104 C-24,-94 -12,-78 -3,-58 C-4,-48 -2,-40 0,-32 Z" fill="{deep}"/>
  <path d="M0,-32 C30,-36 46,-62 35,-104 C24,-94 12,-78 3,-58 C4,-48 2,-40 0,-32 Z" fill="{light}"/>
  <path d="M0,-30 C-17,-42 -24,-74 0,-110 C24,-74 17,-42 0,-30 Z" fill="{main}"/>
  <path d="M-1,-42 C-9,-54 -11,-76 -1,-98 C5,-80 5,-60 -1,-42 Z" fill="{light}" opacity=".55"/>
</g>"""


def bud(x, y, s, rot=0, op=1.0, main=CORAL_DEEP, light=CORAL):
    """Closed tulip bud."""
    return f"""<g transform="translate({x},{y}) rotate({rot}) scale({s/100}) translate(0,30)" opacity="{op}">
  <path d="M0,-30 C-15,-42 -17,-70 0,-98 C17,-70 15,-42 0,-30 Z" fill="{main}"/>
  <path d="M-1,-40 C-8,-52 -8,-72 -1,-90 C4,-74 4,-56 -1,-40 Z" fill="{light}" opacity=".7"/>
</g>"""


def leaf(x, y, s, rot=0, fill=SAGE, op=1.0, flip=False, vein=CREAM):
    """Tulip blade from (x, y), pointing along +x before rotation."""
    fx = -1 if flip else 1
    return f"""<g transform="translate({x},{y}) rotate({rot}) scale({s*fx/100},{s/100})" opacity="{op}">
  <path d="M0,0 C18,-24 56,-36 100,-22 C78,2 38,14 0,0 Z" fill="{fill}"/>
  <path d="M3,-1 C28,-10 60,-16 93,-21" stroke="{vein}" stroke-width="1.5" fill="none" opacity=".6"/>
</g>"""


def leaf_curl(x, y, s, rot=0, fill=SAGE_DEEP, op=1.0, flip=False, vein=CREAM):
    """A longer blade that twists back on itself - the tulip leaf seen edge-on."""
    fx = -1 if flip else 1
    return f"""<g transform="translate({x},{y}) rotate({rot}) scale({s*fx/100},{s/100})" opacity="{op}">
  <path d="M0,0 C24,-30 60,-40 92,-46 C100,-40 96,-30 84,-26 C60,-14 34,4 0,0 Z" fill="{fill}"/>
  <path d="M4,-2 C30,-12 58,-24 86,-36" stroke="{vein}" stroke-width="1.4" fill="none" opacity=".5"/>
</g>"""


def stem(x1, y1, x2, y2, w=0.024, col=SAGE_DEEP, op=1.0, bend=0.12):
    return (f'<path d="M{x1},{y1} Q{(x1+x2)/2+bend},{(y1+y2)/2} {x2},{y2}" stroke="{col}" '
            f'stroke-width="{w}" fill="none" stroke-linecap="round" opacity="{op}"/>')


def dots(pts, r=0.02, col=CORAL, op=.55):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" opacity="{op}"/>' for x, y in pts)


def cluster(kind, x0, y0, w, h, k=1.0):
    """The card's four corner compositions for a face w x h in with top-left at (x0, y0).
    k scales every motif (1.0 for the 6 x 9.5 bag face; ~0.46 for the card).
    Draw order: stems, then leaves over their bases, then blooms."""
    R, B = x0 + w, y0 + h
    if kind == "tl":
        return [stem(x0 + .6*k, y0 + 1.42*k, x0 + 1.05*k, y0 + .95*k), stem(x0 + .38*k, y0 + 1.5*k, x0 + .5*k, y0 + 1.32*k),
                stem(x0 + .95*k, y0 + 1.55*k, x0 + 1.55*k, y0 + 1.42*k, bend=.05),
                leaf(x0 - .15*k, y0 + 1.4*k, 1.45*k, -36, SAGE_LIGHT), leaf_curl(x0 - .1*k, y0 + 1.62*k, 1.25*k, -10, SAGE),
                tulip(x0 + 1.05*k, y0 + .95*k, 1.2*k, 12), tulip(x0 + .5*k, y0 + 1.32*k, .88*k, -14),
                bud(x0 + 1.55*k, y0 + 1.42*k, .62*k, 26)]
    if kind == "tr":
        return [stem(R - .6*k, y0 + 1.4*k, R - .85*k, y0 + .98*k, bend=-.08), stem(R - .3*k, y0 + 1.5*k, R - .35*k, y0 + 1.25*k, bend=.03),
                leaf(R + .1*k, y0 + 1.25*k, 1.6*k, 200, SAGE), leaf_curl(R + .05*k, y0 + 1.45*k, 1.25*k, 174, SAGE_LIGHT),
                tulip(R - .85*k, y0 + .98*k, 1.0*k, -14), bud(R - .35*k, y0 + 1.25*k, .52*k, 10)]
    if kind == "br":
        return [stem(R - 1.6*k, B - .5*k, R - 1.45*k, B - 1.5*k), stem(R - 1.1*k, B - .5*k, R - .78*k, B - 1.3*k),
                stem(R - 2.05*k, B - .5*k, R - 2.0*k, B - 1.08*k), stem(R - .6*k, B - .55*k, R - .3*k, B - .95*k, bend=.04),
                leaf(R - 2.8*k, B - .35*k, 2.0*k, -7, SAGE), leaf_curl(R - 2.35*k, B - .2*k, 1.6*k, -25, SAGE_LIGHT),
                leaf(R + .15*k, B - .5*k, 1.75*k, 196, SAGE_DEEP), leaf_curl(R + .1*k, B - 1.0*k, 1.35*k, 214, SAGE),
                tulip(R - 1.45*k, B - 1.5*k, 1.15*k, 3), tulip(R - .78*k, B - 1.3*k, 1.0*k, 17),
                tulip(R - 2.0*k, B - 1.08*k, .88*k, -11), bud(R - .3*k, B - .95*k, .6*k, 30)]
    if kind == "bl":
        return [stem(x0 + .62*k, B - .5*k, x0 + .58*k, B - 1.05*k), stem(x0 + .95*k, B - .45*k, x0 + 1.1*k, B - .8*k, bend=.03),
                leaf(x0 - .12*k, B - .45*k, 1.3*k, -18, SAGE_LIGHT), leaf_curl(x0 + .1*k, B - .2*k, 1.0*k, -44, SAGE),
                tulip(x0 + .58*k, B - 1.05*k, .78*k, -6), bud(x0 + 1.1*k, B - .8*k, .48*k, 18)]
    raise ValueError(kind)
