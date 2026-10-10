"""Shared drawing helpers for the treasure-chest stickers (img/t_*.svg).

Style: glossy, softly graded fills with a white highlight (desktop-icon look)
plus Japanese manga / kawaii details: big eyes with two catch-lights, blush
with hatching, sparkles, and a dark rounded outline. Every sticker gets a
white die-cut border and a soft drop shadow through one SVG filter.
"""

INK = "#2A2230"
SW = 2.6  # outline width
EYE_SCALE = 1.25  # manga-size eyes


def o(width=SW, color=INK):
    """Outline attributes."""
    return f'stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"'


class Defs:
    """Collects <defs> entries (gradients) with ids that are unique per file."""

    def __init__(self):
        self.items = []
        self.n = 0

    def lin(self, c1, c2, x1=0, y1=0, x2=0, y2=1):
        self.n += 1
        gid = f"g{self.n}"
        self.items.append(
            f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')
        return f"url(#{gid})"

    def rad(self, c1, c2, cx=0.35, cy=0.3, r=0.85):
        self.n += 1
        gid = f"g{self.n}"
        self.items.append(
            f'<radialGradient id="{gid}" cx="{cx}" cy="{cy}" r="{r}">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></radialGradient>')
        return f"url(#{gid})"


STICKER_FILTER = (
    '<filter id="stk" x="-25%" y="-25%" width="150%" height="150%" color-interpolation-filters="sRGB">'
    '<feMorphology in="SourceAlpha" operator="dilate" radius="4.2" result="d"/>'
    '<feFlood flood-color="#FFFFFF"/><feComposite in2="d" operator="in" result="w"/>'
    '<feGaussianBlur in="d" stdDeviation="2.2" result="b"/><feOffset in="b" dy="2.6" result="ob"/>'
    '<feFlood flood-color="#2A2230" flood-opacity=".28"/><feComposite in2="ob" operator="in" result="sh"/>'
    '<feMerge><feMergeNode in="sh"/><feMergeNode in="w"/><feMergeNode in="SourceGraphic"/></feMerge>'
    '</filter>')


def svg(defs, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 -6 140 140" width="128" height="128">'
            f'<defs>{STICKER_FILTER}{"".join(defs.items)}</defs>'
            f'<g filter="url(#stk)">{body}</g></svg>')


# ---------- face parts ----------

def eye(cx, cy, r, iris="#5B3A8C", d=None, look=0.0):
    """Manga eye: dark oval, coloured iris at the bottom, two catch-lights."""
    iris_fill = d.lin(iris, "#1E1530") if d else iris
    r *= EYE_SCALE
    rx, ry = r * 0.78, r
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx:.2f}" ry="{ry:.2f}" fill="{INK}"/>'
            f'<ellipse cx="{cx + look:.2f}" cy="{cy + r * 0.28:.2f}" rx="{rx * 0.72:.2f}" ry="{ry * 0.58:.2f}" fill="{iris_fill}" opacity=".95"/>'
            f'<ellipse cx="{cx - rx * 0.32 + look:.2f}" cy="{cy - ry * 0.38:.2f}" rx="{rx * 0.42:.2f}" ry="{ry * 0.36:.2f}" fill="#fff"/>'
            f'<circle cx="{cx + rx * 0.38 + look:.2f}" cy="{cy + ry * 0.42:.2f}" r="{r * 0.17:.2f}" fill="#fff"/>')


def eyes(x1, x2, cy, r, iris="#5B3A8C", d=None, look=0.0):
    return eye(x1, cy, r, iris, d, look) + eye(x2, cy, r, iris, d, look)


def happy_eye(cx, cy, w):
    """Closed, smiling ^ eye."""
    return f'<path d="M{cx - w},{cy + w * 0.35} Q{cx},{cy - w * 0.75} {cx + w},{cy + w * 0.35}" fill="none" {o(2.8)}/>'


def blush(cx, cy, rx=6, ry=3.6):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#FF7BA6" opacity=".45"/>'
            f'<path d="M{cx - rx * 0.55},{cy + 1.4} l2,-3 M{cx - 0.6},{cy + 1.4} l2,-3 M{cx + rx * 0.45},{cy + 1.4} l2,-3" '
            f'stroke="#E2557F" stroke-width="1.1" stroke-linecap="round" opacity=".7"/>')


def blushes(x1, x2, cy, rx=6, ry=3.6):
    return blush(x1, cy, rx, ry) + blush(x2, cy, rx, ry)


def mouth_w(cx, cy, s=4.0):
    """Cat-like ω mouth."""
    return (f'<path d="M{cx - 2 * s},{cy - s * 0.3} Q{cx - s},{cy + s * 1.1} {cx},{cy - s * 0.2} '
            f'Q{cx + s},{cy + s * 1.1} {cx + 2 * s},{cy - s * 0.3}" fill="none" {o(2.3)}/>')


def mouth_smile(cx, cy, w=5.0):
    return f'<path d="M{cx - w},{cy} Q{cx},{cy + w * 0.9} {cx + w},{cy}" fill="none" {o(2.4)}/>'


def mouth_open(cx, cy, w=6.0, tongue=True):
    t = (f'<path d="M{cx - w * 0.55},{cy + w * 0.62} Q{cx},{cy + w * 0.2} {cx + w * 0.55},{cy + w * 0.62} '
         f'Q{cx},{cy + w * 1.05} {cx - w * 0.55},{cy + w * 0.62} Z" fill="#FF6F91"/>') if tongue else ""
    return (f'<path d="M{cx - w},{cy} Q{cx},{cy + w * 1.5} {cx + w},{cy} Z" fill="#7A2340" {o(2.2)}/>' + t)


def face(cx, cy, s=1.0, iris="#5B3A8C", d=None, mouth="w", blush_on=True, gap=None):
    """A complete kawaii face centred at (cx, cy); s scales it."""
    g = (gap or 11) * s
    out = eyes(cx - g, cx + g, cy, 6.2 * s, iris, d)
    if blush_on:
        out += blushes(cx - g - 4 * s, cx + g + 4 * s, cy + 8.5 * s, 5.2 * s, 3.1 * s)
    my = cy + 8 * s
    if mouth == "w":
        out += mouth_w(cx, my, 2.6 * s)
    elif mouth == "open":
        out += mouth_open(cx, my - 1 * s, 4.6 * s)
    else:
        out += mouth_smile(cx, my, 4 * s)
    return out


# ---------- decoration ----------

def gloss(cx, cy, rx, ry, rot=-25, op=0.55):
    """Soft white highlight, desktop-icon style."""
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fff" opacity="{op}" '
            f'transform="rotate({rot} {cx} {cy})"/>')


def sparkle(cx, cy, s=6.0, color="#FFD23F"):
    """Four-point manga sparkle."""
    k = s * 0.22
    return (f'<path d="M{cx},{cy - s} Q{cx + k},{cy - k} {cx + s},{cy} Q{cx + k},{cy + k} {cx},{cy + s} '
            f'Q{cx - k},{cy + k} {cx - s},{cy} Q{cx - k},{cy - k} {cx},{cy - s} Z" fill="{color}" {o(1.4)}/>')


def bumps_path(cx, cy, r, n, bump, phase=0.0):
    """Closed scalloped circle (lion mane, clouds, frosting)."""
    import math
    pts = []
    for i in range(n):
        a0 = phase + 2 * math.pi * i / n
        a1 = phase + 2 * math.pi * (i + 1) / n
        am = (a0 + a1) / 2
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        qx, qy = cx + (r + bump) * math.cos(am) * 1.0, cy + (r + bump) * math.sin(am)
        if i == 0:
            pts.append(f"M{x0:.2f},{y0:.2f}")
        pts.append(f"Q{qx:.2f},{qy:.2f} {x1:.2f},{y1:.2f}")
    return " ".join(pts) + " Z"


def spikes_path(cx, cy, r_in, r_out, n, a_from, a_to):
    """Zig-zag arc (hedgehog spines, dino plates) from angle a_from to a_to (degrees)."""
    import math
    pts = []
    for i in range(2 * n + 1):
        a = math.radians(a_from + (a_to - a_from) * i / (2 * n))
        r = r_out if i % 2 else r_in
        pts.append(f"{cx + r * math.cos(a):.2f},{cy + r * math.sin(a):.2f}")
    return "M" + " L".join(pts)
