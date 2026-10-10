from common import *


def octopus():
    d = Defs()
    sk = d.rad("#FFB3D9", "#E0559C", 0.4, 0.3, 0.85)
    b = ''
    # tentacles
    for x0, x1, x2, curl in ((30, 18, 14, -1), (48, 40, 36, -1), (64, 64, 64, 1), (80, 88, 92, 1), (98, 110, 114, 1)):
        b += (f'<path d="M{x0 - 6},74 Q{x1 - 6},100 {x2},112 Q{x2 + 6 * curl},118 {x2 + 9 * curl},110 '
              f'Q{x1 + 6},98 {x0 + 6},74 Z" fill="{sk}" {o()}/>')
    b += f'<path d="M18,64 Q18,14 64,14 Q110,14 110,64 Q110,86 64,86 Q18,86 18,64 Z" fill="{sk}" {o()}/>'
    for cx, cy in ((26, 30), (100, 40), (90, 22)):
        b += f'<circle cx="{cx}" cy="{cy}" r="3.4" fill="#FFE1F0" opacity=".9"/>'
    b += face(64, 54, 1.15, "#9B2C6B", d, "open")
    b += gloss(44, 28, 12, 5, -25, .6) + sparkle(14, 18, 5.5)
    return svg(d, b)


def dolphin():
    d = Defs()
    sk = d.lin("#7FD3FF", "#2F86D9", 0, 0, 1, 1)
    b = ''
    b += f'<path d="M28,30 Q14,14 10,28 Q20,32 22,42 Z" fill="{sk}" {o()}/>'  # tail fluke
    b += f'<path d="M22,36 Q48,22 78,30 Q108,40 114,72 Q116,88 100,92 L92,92 Q74,80 54,72 Q32,60 22,36 Z" fill="{sk}" {o()}/>'
    b += '<path d="M60,74 Q80,82 92,92 L100,92 Q112,90 112,80 Q92,84 60,74 Z" fill="#E8F7FF"/>'
    b += f'<path d="M66,30 Q70,12 84,14 Q78,24 80,34 Z" fill="{sk}" {o()}/>'
    b += f'<path d="M66,74 Q60,88 70,94 Q74,84 78,80 Z" fill="{sk}" {o()}/>'
    b += eye(92, 58, 7, "#1F5FA8", d) + blush(98, 72, 5, 3)
    b += f'<path d="M100,84 Q106,86 112,82" fill="none" {o(2.2)}/>'
    # water splash
    w = d.lin("#B9ECFF", "#4FB3F0")
    b += f'<path d="M12,110 Q24,96 36,110 Q48,96 60,110 Q72,96 84,110 Q96,96 108,110 Q114,118 64,118 Q14,118 12,110 Z" fill="{w}" {o()}/>'
    b += '<circle cx="40" cy="92" r="3.5" fill="#B9ECFF" stroke="#2A2230" stroke-width="1.6"/><circle cx="30" cy="84" r="2.5" fill="#B9ECFF" stroke="#2A2230" stroke-width="1.4"/>'
    b += gloss(60, 36, 14, 4, -10, .55) + sparkle(110, 18, 6)
    return svg(d, b)


def turtle():
    d = Defs()
    sh = d.rad("#9BE07A", "#2F8F46", 0.4, 0.3, 0.85)
    sk = d.lin("#D7F59A", "#9DCB5A")
    b = ''
    for cx, cy in ((34, 100), (94, 100)):
        b += f'<ellipse cx="{cx}" cy="{cy}" rx="11" ry="8" fill="{sk}" {o()}/>'
    b += f'<circle cx="64" cy="32" r="22" fill="{sk}" {o()}/>'
    b += face(64, 30, 0.95, "#3B6B1E", d, "smile")
    b += f'<path d="M16,90 Q16,46 64,46 Q112,46 112,90 Q112,98 64,98 Q16,98 16,90 Z" fill="{sh}" {o()}/>'
    b += f'<path d="M64,56 L78,64 L78,80 L64,88 L50,80 L50,64 Z" fill="#B8EC8E" opacity=".75" {o(2)}/>'
    for p in ("M50,64 L34,58", "M78,64 L94,58", "M50,80 L30,88", "M78,80 L98,88", "M64,88 L64,97"):
        b += f'<path d="{p}" fill="none" {o(2)}/>'
    b += f'<path d="M14,92 Q64,106 114,92" fill="none" {o()}/>'
    b += gloss(40, 58, 12, 4.5, -25, .55) + sparkle(110, 22, 6) + sparkle(16, 30, 4.5)
    return svg(d, b)


def butterfly():
    d = Defs()
    w1 = d.lin("#FFC1E3", "#C05BEA", 0, 0, 1, 1)
    w2 = d.lin("#9EE7FF", "#7B6CF6", 0, 0, 1, 1)
    b = ''
    b += f'<path d="M62,58 Q40,10 16,22 Q2,34 18,58 Q30,68 62,62 Z" fill="{w1}" {o()}/>'
    b += f'<path d="M66,58 Q88,10 112,22 Q126,34 110,58 Q98,68 66,62 Z" fill="{w1}" {o()}/>'
    b += f'<path d="M62,66 Q34,66 24,86 Q22,106 40,104 Q58,98 62,74 Z" fill="{w2}" {o()}/>'
    b += f'<path d="M66,66 Q94,66 104,86 Q106,106 88,104 Q70,98 66,74 Z" fill="{w2}" {o()}/>'
    for cx, cy, r in ((30, 36, 6), (98, 36, 6), (40, 88, 4.5), (88, 88, 4.5)):
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFF3A8" {o(1.6)}/>'
    b += f'<path d="M58,28 Q52,12 44,10" fill="none" {o(2.2)}/><path d="M70,28 Q76,12 84,10" fill="none" {o(2.2)}/>'
    b += f'<circle cx="44" cy="10" r="3" fill="#FF7BA6" {o(1.6)}/><circle cx="84" cy="10" r="3" fill="#FF7BA6" {o(1.6)}/>'
    body = d.lin("#7A5AA8", "#3E2A66")
    b += f'<ellipse cx="64" cy="76" rx="6" ry="26" fill="{body}" {o()}/>'
    b += f'<circle cx="64" cy="40" r="15" fill="{d.rad("#FFE9F5", "#F3B8D9")}" {o()}/>'
    b += face(64, 38, 0.62, "#7A3BA8", d, "w", gap=12)
    b += gloss(30, 28, 9, 3.5, -30, .6) + gloss(98, 28, 9, 3.5, 30, .6)
    return svg(d, b)


def parrot():
    d = Defs()
    red = d.rad("#FF7A6B", "#D7263D", 0.4, 0.3, 0.85)
    b = ''
    b += f'<path d="M58,96 Q50,118 62,124 Q66,112 70,100 Z" fill="#3E8EF7" {o()}/>'
    b += f'<path d="M70,96 Q78,120 90,120 Q86,108 80,96 Z" fill="#FFD23F" {o()}/>'
    b += f'<path d="M64,14 Q100,14 100,52 Q102,86 80,100 Q64,108 48,100 Q28,88 28,56 Q28,14 64,14 Z" fill="{red}" {o()}/>'
    b += f'<path d="M28,62 Q16,78 26,100 Q40,96 46,82 Z" fill="#2FBF71" {o()}/>'
    b += f'<path d="M100,62 Q112,78 102,100 Q88,96 82,82 Z" fill="#2FBF71" {o()}/>'
    b += f'<path d="M30,82 Q22,92 28,98 M98,82 Q106,92 100,98" fill="none" stroke="#3E8EF7" stroke-width="5" stroke-linecap="round"/>'
    b += '<ellipse cx="46" cy="50" rx="12" ry="11" fill="#FFF6EA"/><ellipse cx="82" cy="50" rx="12" ry="11" fill="#FFF6EA"/>'
    b += eyes(47, 81, 50, 6.2, "#A3361F", d)
    beak = d.lin("#FFE48A", "#F2A33A")
    b += f'<path d="M54,64 Q64,58 74,64 Q76,76 64,86 Q56,78 54,64 Z" fill="{beak}" {o()}/>'
    b += f'<path d="M58,72 Q64,76 70,72" fill="none" {o(1.8)}/>'
    b += blushes(36, 92, 66, 5, 3)
    b += f'<path d="M56,16 Q58,4 66,6 Q64,10 64,16" fill="{red}" {o(2)}/>'
    b += gloss(48, 26, 11, 4, -20, .55) + sparkle(112, 24, 6) + sparkle(14, 26, 4.5)
    return svg(d, b)


def whale():
    d = Defs()
    sk = d.rad("#7FB6FF", "#3557C9", 0.4, 0.3, 0.9)
    b = ''
    # water spout
    b += f'<path d="M58,30 Q56,18 46,14 M64,30 L64,10 M70,30 Q72,18 82,14" fill="none" stroke="#5CC8FF" stroke-width="5" stroke-linecap="round"/>'
    b += '<circle cx="44" cy="12" r="4" fill="#9EE3FF" stroke="#2A2230" stroke-width="1.6"/><circle cx="84" cy="12" r="4" fill="#9EE3FF" stroke="#2A2230" stroke-width="1.6"/><circle cx="64" cy="7" r="4.5" fill="#9EE3FF" stroke="#2A2230" stroke-width="1.6"/>'
    b += f'<path d="M100,78 Q120,58 122,74 Q114,80 118,92 Q110,92 100,88 Z" fill="{sk}" {o()}/>'
    b += f'<path d="M10,76 Q10,34 58,32 Q104,32 106,74 Q106,106 58,106 Q10,106 10,76 Z" fill="{sk}" {o()}/>'
    b += '<path d="M16,86 Q58,104 100,86 Q96,104 58,104 Q20,104 16,86 Z" fill="#E6F1FF"/>'
    for x in (40, 52, 64, 76):
        b += f'<path d="M{x},90 L{x - 2},100" stroke="#B8CCF2" stroke-width="2" stroke-linecap="round"/>'
    b += face(54, 66, 1.05, "#2643A3", d, "w")
    b += gloss(36, 46, 13, 5, -20, .55) + sparkle(112, 30, 6) + sparkle(16, 22, 4.5)
    return svg(d, b)


def shark():
    d = Defs()
    sk = d.lin("#A9C6E8", "#5D7FA8")
    b = ''
    b += f'<path d="M52,36 Q60,6 76,10 Q70,22 72,38 Z" fill="{sk}" {o()}/>'
    b += f'<path d="M104,64 Q124,40 124,58 Q118,70 124,84 Q118,92 104,78 Z" fill="{sk}" {o()}/>'
    b += f'<path d="M8,70 Q12,34 58,34 Q100,34 108,70 Q100,104 58,104 Q14,104 8,70 Z" fill="{sk}" {o()}/>'
    b += '<path d="M14,78 Q56,72 102,78 Q96,102 58,102 Q22,102 14,78 Z" fill="#F4F8FF"/>'
    b += f'<path d="M50,88 Q42,100 54,104 Q56,96 60,92 Z" fill="{sk}" {o(2)}/>'
    b += eyes(36, 62, 62, 5.8, "#2E4E78", d)
    b += blushes(28, 70, 74, 4.6, 2.8)
    b += f'<path d="M38,80 Q49,92 60,80 Z" fill="#7A2340" {o(2)}/>'
    b += '<path d="M42,80 L44.5,84 L47,80 M52,80 L54.5,84 L57,80" fill="#fff"/>'
    b += gloss(40, 44, 14, 4.5, -10, .55) + sparkle(18, 22, 5.5) + sparkle(112, 106, 4.5)
    return svg(d, b)


def owl():
    d = Defs()
    fe = d.rad("#C99A6E", "#7A5236", 0.45, 0.3, 0.85)
    b = ''
    b += f'<path d="M24,40 L22,12 L44,28 Z" fill="{fe}" {o()}/><path d="M104,40 L106,12 L84,28 Z" fill="{fe}" {o()}/>'
    b += f'<path d="M64,18 Q112,18 110,70 Q108,114 64,114 Q20,114 18,70 Q16,18 64,18 Z" fill="{fe}" {o()}/>'
    b += '<path d="M42,86 Q64,74 86,86 Q84,110 64,110 Q44,110 42,86 Z" fill="#F4DDBF"/>'
    for x, y in ((54, 92), (64, 96), (74, 92), (59, 102), (69, 102)):
        b += f'<path d="M{x - 3},{y} Q{x},{y + 3} {x + 3},{y}" fill="none" stroke="#B88A60" stroke-width="1.8" stroke-linecap="round"/>'
    disc = d.rad("#FFF3E0", "#F1D2A8")
    b += f'<circle cx="44" cy="56" r="18" fill="{disc}" {o(2)}/><circle cx="84" cy="56" r="18" fill="{disc}" {o(2)}/>'
    b += eye(44, 56, 9, "#D98A1F", d) + eye(84, 56, 9, "#D98A1F", d)
    b += f'<path d="M58,70 L70,70 L64,82 Z" fill="#FFB43B" {o(2)}/>'
    b += blushes(28, 100, 74, 4.6, 2.8)
    b += f'<path d="M18,72 Q8,90 22,100 M110,72 Q120,90 106,100" fill="none" {o()}/>'
    b += gloss(52, 28, 11, 4, -15, .45) + sparkle(114, 104, 5.5) + sparkle(12, 26, 4.5)
    return svg(d, b)


STICKERS = {"octopus": octopus, "dolphin": dolphin, "turtle": turtle, "butterfly": butterfly,
            "parrot": parrot, "whale": whale, "shark": shark, "owl": owl}
