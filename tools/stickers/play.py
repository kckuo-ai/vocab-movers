from common import *
import math


def football():
    d = Defs()
    ball = d.rad("#FFFFFF", "#D3DAE6", 0.38, 0.3, 0.9)
    d.items.append('<clipPath id="ballclip"><circle cx="64" cy="64" r="50"/></clipPath>')
    b = f'<circle cx="64" cy="64" r="50" fill="{ball}" {o()}/><g clip-path="url(#ballclip)">'
    # centre pentagon + five neighbours (classic ball pattern, simplified)
    def pent(cx, cy, r, rot):
        pts = [f"{cx + r * math.cos(math.radians(rot + 72 * i)):.1f},{cy + r * math.sin(math.radians(rot + 72 * i)):.1f}" for i in range(5)]
        return f'<polygon points="{" ".join(pts)}" fill="#3B3550" {o(2)}/>'
    b += pent(64, 30, 12, -90)
    for i in range(5):
        a = math.radians(-90 + 72 * i + 36)
        b += pent(64 + 48 * math.cos(a), 64 + 48 * math.sin(a), 11, -90 + 72 * i + 36 + 180)
    for i in range(5):
        a = math.radians(-90 + 72 * i)
        b += f'<path d="M{64 + 12 * math.cos(a):.1f},{30 + 12 * math.sin(a):.1f} L{64 + 22 * math.cos(a):.1f},{30 + 22 * math.sin(a) :.1f}" stroke="#3B3550" stroke-width="2"/>'
    b += '</g>'
    b += f'<ellipse cx="64" cy="78" rx="27" ry="17" fill="#FFFFFF" opacity=".92"/>'
    b += face(64, 74, 0.9, "#3B4A78", d, "open", gap=12)
    b += f'<circle cx="64" cy="64" r="50" fill="none" {o()}/>'
    b += gloss(40, 36, 12, 6, -35, .7) + sparkle(116, 18, 6) + sparkle(12, 110, 4.5)
    return svg(d, b)


def basketball():
    d = Defs()
    ball = d.rad("#FFB061", "#E2671E", 0.38, 0.3, 0.9)
    b = f'<circle cx="64" cy="64" r="50" fill="{ball}" {o()}/>'
    for p in ("M14,64 L114,64", "M64,14 L64,114", "M28,28 Q50,64 28,100", "M100,28 Q78,64 100,100"):
        b += f'<path d="{p}" fill="none" stroke="#5A2A10" stroke-width="3" stroke-linecap="round"/>'
    # face on a cream badge so it stays readable over the seams
    b += f'<ellipse cx="64" cy="78" rx="26" ry="17" fill="#FFE2C2" {o(2)}/>'
    b += face(64, 74, 0.85, "#8A3B12", d, "w", gap=12)
    b += f'<circle cx="64" cy="64" r="50" fill="none" {o()}/>'
    b += gloss(40, 36, 12, 6, -35, .6) + sparkle(116, 20, 6) + sparkle(14, 110, 4.5)
    return svg(d, b)


def palette():
    d = Defs()
    wood = d.rad("#FFE8C2", "#E2B072", 0.4, 0.3, 0.9)
    b = (f'<path d="M64,14 Q112,14 116,56 Q118,76 100,78 Q86,78 88,92 Q92,110 72,114 Q20,118 12,72 '
         f'Q8,18 64,14 Z" fill="{wood}" {o()}/>')
    b += f'<ellipse cx="96" cy="94" rx="9" ry="7" fill="#F6F0E6" {o()}/>'
    for (x, y, c) in ((40, 34, "#FF6B7A"), (66, 26, "#FFD23F"), (92, 36, "#69DB7C"), (30, 60, "#4DABF7"), (40, 88, "#B79BFF")):
        b += f'<path d="{bumps_path(x, y, 7.5, 6, 2.2)}" fill="{c}" {o(1.8)}/>' + gloss(x - 2, y - 3, 2.6, 1.6, -30, .8)
    b += face(68, 66, 0.8, "#8A5520", d, "w", gap=12)
    # brush
    b += f'<path d="M84,124 L118,88" stroke="#B76E3E" stroke-width="7" stroke-linecap="round"/><path d="M84,124 L118,88" fill="none" {o(1.6)}/>'
    b += f'<path d="M114,92 L122,84 L126,88 L118,96 Z" fill="#C0C7D4" {o(1.8)}/>'
    b += f'<path d="M122,84 Q128,74 126,70 Q118,74 122,84 Z" fill="#FF6B7A" {o(1.8)}/>'
    b += gloss(44, 22, 12, 4, -10, .6) + sparkle(14, 18, 5.5)
    return svg(d, b).replace('viewBox="-6 -6 140 140"', 'viewBox="-6 -6 144 144"')


def guitar():
    d = Defs()
    body = d.rad("#FFC27A", "#D9782E", 0.4, 0.35, 0.9)
    b = ''
    b += f'<g transform="rotate(30 64 64)">'
    b += f'<rect x="58" y="-8" width="12" height="62" rx="3" fill="#8A5520" {o()}/>'
    for y in (4, 14, 24, 34, 44):
        b += f'<path d="M58,{y} L70,{y}" stroke="#E3C08A" stroke-width="1.6"/>'
    b += f'<rect x="54" y="-18" width="20" height="14" rx="5" fill="#5E3C2E" {o()}/>'
    b += f'<path d="M64,48 Q88,46 88,70 Q88,80 82,84 Q96,92 94,108 Q90,126 64,126 Q38,126 34,108 Q32,92 46,84 Q40,80 40,70 Q40,46 64,48 Z" fill="{body}" {o()}/>'
    b += f'<circle cx="64" cy="76" r="9" fill="#5E3C2E" {o(2)}/>'
    b += f'<rect x="54" y="104" width="20" height="5" rx="2" fill="#5E3C2E" {o(1.6)}/>'
    for x in (61, 64, 67):
        b += f'<path d="M{x},-6 L{x},106" stroke="#F6F0E6" stroke-width=".9"/>'
    b += face(64, 96, 0.78, "#8A3B12", d, "w", gap=14)
    b += gloss(52, 60, 7, 4, -30, .6)
    b += '</g>'
    b += sparkle(22, 24, 6) + sparkle(112, 112, 4.5)
    # music notes
    b += f'<path d="M100,16 L100,34" {o(2.4)}/><ellipse cx="96" cy="35" rx="5" ry="4" fill="{INK}"/><path d="M100,16 Q108,18 110,26" fill="none" {o(2.4)}/>'
    return svg(d, b).replace('viewBox="-6 -6 140 140"', 'viewBox="-14 -14 156 156"')


def crown():
    d = Defs()
    gold = d.lin("#FFE680", "#F2A818")
    b = f'<path d="M14,40 L36,70 L64,24 L92,70 L114,40 L106,100 L22,100 Z" fill="{gold}" {o()}/>'
    b += f'<rect x="20" y="96" width="88" height="16" rx="5" fill="{gold}" {o()}/>'
    for x, y, c in ((14, 40, "#FF6B7A"), (64, 24, "#4DABF7"), (114, 40, "#69DB7C")):
        b += f'<circle cx="{x}" cy="{y - 4}" r="7" fill="{c}" {o(2)}/>' + gloss(x - 2, y - 7, 2.5, 1.6, -30, .85)
    for x, c in ((38, "#B79BFF"), (64, "#FF6B7A"), (90, "#4DABF7")):
        b += f'<path d="M{x},98 L{x + 5},104 L{x},110 L{x - 5},104 Z" fill="{c}" {o(1.6)}/>'
    b += face(64, 72, 0.9, "#A86A0B", d, "open", gap=13)
    b += gloss(36, 58, 4, 12, 15, .5) + sparkle(116, 14, 6) + sparkle(10, 112, 4.5) + sparkle(118, 80, 3.5)
    return svg(d, b)


def diamond():
    d = Defs()
    g1 = d.lin("#D6FAFF", "#5CC8F2")
    g2 = d.lin("#A8EEFF", "#2F9CD9")
    b = f'<path d="M30,30 L98,30 L120,56 L64,118 L8,56 Z" fill="{g2}" {o()}/>'
    b += f'<path d="M30,30 L98,30 L120,56 L8,56 Z" fill="{g1}" {o(2)}/>'
    b += f'<path d="M46,30 L36,56 L64,118 L92,56 L82,30" fill="none" stroke="#2A80B9" stroke-width="2" stroke-linejoin="round"/>'
    b += f'<path d="M36,56 L64,30 L92,56" fill="none" stroke="#2A80B9" stroke-width="2"/>'
    b += f'<path d="M30,30 L98,30 L120,56 L64,118 L8,56 Z" fill="none" {o()}/>'
    b += '<path d="M20,52 L32,34 L44,34 L34,52 Z" fill="#fff" opacity=".75"/>'
    b += face(64, 74, 0.82, "#1F5FA8", d, "w", gap=14)
    b += sparkle(112, 18, 7, "#FFFFFF") + sparkle(18, 16, 5) + sparkle(110, 100, 4.5)
    return svg(d, b)


def piano():
    d = Defs()
    case = d.lin("#9B7BFF", "#5B3FC4")
    b = f'<rect x="8" y="30" width="112" height="78" rx="14" fill="{case}" {o()}/>'
    b += f'<rect x="16" y="36" width="96" height="22" rx="7" fill="#F3EEFF" {o(2)}/>'
    b += face(64, 42, 0.62, "#6B4FD8", d, "w", gap=14)
    b += f'<rect x="16" y="62" width="96" height="38" rx="4" fill="#FFFFFF" {o(2)}/>'
    for i in range(1, 8):
        x = 16 + i * 12
        b += f'<path d="M{x},62 L{x},100" stroke="#B8C0CF" stroke-width="1.6"/>'
    for i in (1, 2, 4, 5, 6):
        x = 16 + i * 12 - 4
        b += f'<rect x="{x}" y="62" width="8" height="22" rx="2" fill="{INK}"/>'
    b += gloss(36, 38, 14, 3, -5, .25)
    # notes
    b += f'<path d="M30,4 L30,20" {o(2.4)}/><ellipse cx="26" cy="21" rx="5" ry="4" fill="{INK}"/><path d="M30,4 Q38,6 40,14" fill="none" {o(2.4)}/>'
    b += f'<path d="M92,8 L92,22 M104,6 L104,20 M92,8 L104,6" fill="none" {o(2.4)}/><ellipse cx="88" cy="23" rx="4.5" ry="3.6" fill="{INK}"/><ellipse cx="100" cy="21" rx="4.5" ry="3.6" fill="{INK}"/>'
    b += sparkle(116, 116, 5) + sparkle(62, 12, 4.5, "#FF9BD0")
    return svg(d, b).replace('viewBox="-6 -6 140 140"', 'viewBox="-6 -8 140 142"')


def skateboard():
    d = Defs()
    deck = d.lin("#FF9CC2", "#A35BEA", 0, 0, 1, 0)
    b = '<g transform="rotate(-14 64 64)">'
    b += f'<rect x="28" y="76" width="16" height="7" fill="#A0A9BA" {o(1.8)}/><rect x="84" y="76" width="16" height="7" fill="#A0A9BA" {o(1.8)}/>'
    for x in (36, 92):
        b += f'<circle cx="{x}" cy="90" r="11" fill="#FFD23F" {o()}/><circle cx="{x}" cy="90" r="4" fill="#F2A818" {o(1.6)}/>'
    b += f'<path d="M6,52 Q4,40 18,40 L110,40 Q124,40 122,52 L120,66 Q118,78 104,78 L24,78 Q10,78 8,66 Z" fill="{deck}" {o()}/>'
    b += '<path d="M16,46 L112,46" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".55"/>'
    b += sparkle(26, 64, 4, "#FFE066") + sparkle(102, 64, 4, "#FFE066")
    b += face(64, 57, 0.9, "#7A3BA8", d, "open", gap=13)
    b += '</g>'
    b += f'<path d="M6,112 L26,112 M2,120 L18,120 M14,104 L30,104" stroke="#9AA6BA" stroke-width="3" stroke-linecap="round"/>'
    b += sparkle(112, 18, 6) + sparkle(18, 20, 4.5)
    return svg(d, b)


STICKERS = {"football": football, "basketball": basketball, "palette": palette, "guitar": guitar,
            "crown": crown, "diamond": diamond, "piano": piano, "skateboard": skateboard}
