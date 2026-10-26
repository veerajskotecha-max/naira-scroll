"""Shared pieces for the catalogue builds: the NAIRA logo vector, brand colours, rupee formatting and embedded fonts."""
import base64, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # scratchpad/lookbook
REPO = Path("/home/user/naira-scroll")
FONTS = ROOT / "fonts"
_LOGO = json.load(open(REPO / "creative/naira-bag/build/assets/naira-logo-vector.json"))
LOGO_SAGE, LOGO_BLUSH = "#99B4AF", "#FFBDA8"


def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def inr(n):
    return "₹" + f"{int(round(n)):,}"


def fonts_css():
    def face(fam, file, fmt, weight=400, style="normal", rng=None):
        r = f"unicode-range:{rng};" if rng else ""
        return (f"@font-face{{font-family:'{fam}';src:url(data:font/{fmt};base64,{b64(FONTS / file)}) format('{'truetype' if fmt == 'ttf' else fmt}');"
                f"font-weight:{weight};font-style:{style};font-display:block;{r}}}")
    return "".join([
        face("Velista", "Velista.ttf", "ttf"),
        face("JostF", "Jost-300.woff2", "woff2", 300), face("JostF", "Jost-400.woff2", "woff2", 400), face("JostF", "Jost-500.woff2", "woff2", 500),
        face("CormI", "CormorantGaramond-300i.woff2", "woff2", 400, "italic"),
        face("Rupee", "Poppins-400-deva.woff2", "woff2", 300, rng="U+20B9"), face("Rupee", "Poppins-400-deva.woff2", "woff2", 400, rng="U+20B9"),
        face("Rupee", "Poppins-500-deva.woff2", "woff2", 500, rng="U+20B9"),
        face("Rupee", "Poppins-400-deva.woff2", "woff2", 400, "italic", rng="U+20B9"),
    ])
