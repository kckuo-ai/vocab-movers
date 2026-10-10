from common import *


def unicorn():
    d = Defs()
    wh = d.rad("#FFFFFF", "#E6E0F5", 0.4, 0.3, 0.9)
    horn = d.lin("#FFF2A8", "#F5B82E")
    b = ''
    # rainbow mane: soft locks down the right side, behind the head
    for (cx, cy, rx, ry, rot, c) in ((94, 30, 16, 11, 30, "#FF8FB8"), (106, 50, 15, 11, 70, "#FFC06B"),
                                     (108, 72, 14, 10, 95, "#8EE6A4"), (102, 94, 13, 10, 120, "#86C8FF"),
                                     (88, 110, 12, 9, 150, "#B79BFF")):
        b += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{c}" transform="rotate({rot} {cx} {cy})" {o(2.2)}/>'
    b += f'<path d="M30,30 L34,8 L46,26 Z" fill="{wh}" {o()}/><path d="M78,24 L90,6 L94,28 Z" fill="{wh}" {o()}/>'
    b += '<path d="M34,26 L35.5,14 L42,24 Z" fill="#FFC1DA"/>'
    b += f'<path d="M62,16 Q100,16 100,58 Q100,82 90,98 Q80,114 62,114 Q44,114 34,98 Q24,82 24,58 Q24,16 62,16 Z" fill="{wh}" {o()}/>'
    b += '<path d="M38,94 Q62,84 86,94 Q82,112 62,112 Q42,112 38,94 Z" fill="#FFD9E8"/>'
    b += f'<circle cx="54" cy="100" r="2" fill="{INK}"/><circle cx="70" cy="100" r="2" fill="{INK}"/>'
    # horn
    b += f'<path d="M52,24 L60,0 L70,24 Z" fill="{horn}" {o()}/>'
    b += f'<path d="M54,18 L67,13 M57,9 L64,6" stroke="#D99A1E" stroke-width="2" stroke-linecap="round"/>'
    # forelock in three colours
    b += f'<path d="M40,30 Q46,16 62,22 Q56,30 54,42 Q46,32 40,30 Z" fill="#FF8FB8" {o(2)}/>'
    b += f'<path d="M58,24 Q72,14 82,26 Q72,28 68,38 Q64,28 58,24 Z" fill="#B79BFF" {o(2)}/>'
    b += eyes(46, 78, 62, 7, "#8B5CF6", d)
    b += blushes(36, 88, 78, 5.2, 3)
    b += mouth_w(62, 86, 2.4)
    b += gloss(38, 46, 8, 4, -20, .6) + sparkle(14, 30, 6, "#FF9BD0") + sparkle(16, 104, 4.5) + sparkle(118, 112, 4)
    return svg(d, f'<g transform="translate(0,9)">{b}</g>').replace('viewBox="-6 -6 140 140"', 'viewBox="-8 -2 144 144"')


def dragon():
    d = Defs()
    sk = d.rad("#9AF0A8", "#25A55F", 0.4, 0.3, 0.9)
    wing = d.lin("#C6B5FF", "#7C5CE0")
    b = ''
    b += f'<path d="M30,60 Q4,40 6,16 Q18,28 26,24 Q24,40 40,46 Z" fill="{wing}" {o()}/>'
    b += f'<path d="M98,60 Q124,40 122,16 Q110,28 102,24 Q104,40 88,46 Z" fill="{wing}" {o()}/>'
    b += f'<path d="M42,26 Q40,8 50,4 Q50,16 54,22 Z" fill="#FFE48A" {o(2)}/><path d="M86,26 Q88,8 78,4 Q78,16 74,22 Z" fill="#FFE48A" {o(2)}/>'
    b += f'<path d="M64,18 Q108,18 108,62 Q108,108 64,110 Q20,108 20,62 Q20,18 64,18 Z" fill="{sk}" {o()}/>'
    b += '<path d="M38,82 Q64,72 90,82 Q92,104 64,106 Q36,104 38,82 Z" fill="#E7FFD8"/>'
    b += f'<path d="M58,18 L64,8 L70,18" fill="#FFB347" {o(2)}/>'
    b += eyes(46, 82, 56, 7.4, "#B8640E", d)
    b += blushes(34, 94, 72, 5.2, 3)
    b += f'<circle cx="58" cy="82" r="1.8" fill="{INK}"/><circle cx="70" cy="82" r="1.8" fill="{INK}"/>'
    b += mouth_open(64, 89, 6)
    b += f'<path d="M58,89 L60,93 L62,89" fill="#fff"/>'
    b += gloss(44, 34, 11, 4.5, -20, .55) + sparkle(112, 98, 5.5) + sparkle(16, 100, 4.5)
    return svg(d, b)


def dinosaur():
    d = Defs()
    sk = d.lin("#7FE0A0", "#2E9E63", 0, 0, 1, 1)
    b = ''
    # back plates
    for x, y, r in ((22, 66, 8), (30, 50, 9), (44, 38, 10), (60, 34, 10)):
        b += f'<path d="M{x - r},{y + 4} L{x},{y - r - 2} L{x + r},{y + 4} Z" fill="#FFB347" {o(2)}/>'
    b += f'<path d="M8,96 Q2,70 22,64 Q30,44 58,40 Q66,26 90,24 Q120,24 120,52 Q120,72 98,76 Q96,92 86,104 L78,104 L78,112 L62,112 L60,104 L46,106 L44,114 L28,114 L28,104 Q14,104 8,96 Z" fill="{sk}" {o()}/>'
    b += '<path d="M64,64 Q84,66 94,78 Q90,96 80,102 Q60,100 54,84 Q54,70 64,64 Z" fill="#E4FFD0"/>'
    b += f'<path d="M86,80 Q96,84 98,92" fill="none" {o(2.4)}/>'
    b += eye(96, 44, 7.6, "#1F6B3E", d)
    b += blush(106, 58, 5, 3)
    b += f'<path d="M100,64 Q110,70 118,62" fill="none" {o(2.4)}/>'
    b += f'<circle cx="114" cy="40" r="1.8" fill="{INK}"/>'
    b += gloss(78, 34, 11, 4, -15, .55) + sparkle(20, 22, 6) + sparkle(114, 104, 4.5)
    return svg(d, b)


def rocket():
    d = Defs()
    bd = d.lin("#FFFFFF", "#D7DEEB", 0, 0, 1, 0)
    rd = d.lin("#FF6B7A", "#D7263D")
    fl = d.lin("#FFE066", "#FF7A2E")
    b = ''
    b += f'<path d="M52,100 Q56,124 64,126 Q72,124 76,100 Z" fill="{fl}" {o(2)}/>'
    b += f'<path d="M58,100 Q60,114 64,116 Q68,114 70,100 Z" fill="#FFF6B0"/>'
    b += f'<path d="M40,74 Q22,82 22,104 L42,96 Z" fill="{rd}" {o()}/><path d="M88,74 Q106,82 106,104 L86,96 Z" fill="{rd}" {o()}/>'
    b += f'<path d="M64,4 Q94,26 92,74 Q90,94 84,102 L44,102 Q38,94 36,74 Q34,26 64,4 Z" fill="{bd}" {o()}/>'
    b += f'<path d="M64,4 Q80,16 86,30 L42,30 Q48,16 64,4 Z" fill="{rd}" {o()}/>'
    b += f'<rect x="48" y="96" width="32" height="8" rx="3" fill="#8E9AAE" {o(2)}/>'
    win = d.rad("#C7F0FF", "#3E8EF7", 0.35, 0.3, 0.8)
    b += f'<circle cx="64" cy="52" r="13" fill="{win}" {o()}/>'
    b += gloss(59, 47, 5, 3, -30, .8)
    b += face(64, 80, 0.7, "#3E5AA8", d, "w", gap=12)
    b += sparkle(110, 20, 6) + sparkle(16, 40, 4.5) + sparkle(110, 60, 3.5)
    return svg(d, b).replace('viewBox="-6 -6 140 140"', 'viewBox="-6 -6 140 144"')


def ufo():
    d = Defs()
    dome = d.rad("#E6FBFF", "#7FD8F5", 0.35, 0.3, 0.9)
    sau = d.lin("#D8C7FF", "#7B5CE0")
    b = ''
    b += f'<path d="M40,84 L22,122 L106,122 L88,84 Z" fill="#FFF49A" opacity=".55"/>'
    b += f'<path d="M30,62 Q30,22 64,22 Q98,22 98,62 Z" fill="{dome}" {o()}/>'
    b += f'<ellipse cx="64" cy="48" rx="13" ry="12" fill="#8DF07A" {o(2)}/>'
    b += f'<path d="M58,37 Q54,28 50,26 M70,37 Q74,28 78,26" fill="none" {o(2)}/><circle cx="50" cy="26" r="2.8" fill="#FF7BA6" {o(1.4)}/><circle cx="78" cy="26" r="2.8" fill="#FF7BA6" {o(1.4)}/>'
    b += eyes(59, 69, 48, 3.6, "#2F7D32", d) + mouth_smile(64, 54, 2.6)
    b += gloss(44, 36, 8, 4, -30, .7)
    b += f'<ellipse cx="64" cy="70" rx="56" ry="18" fill="{sau}" {o()}/>'
    b += f'<ellipse cx="64" cy="64" rx="38" ry="7" fill="#B9A3FF" opacity=".8"/>'
    for x in (24, 44, 64, 84, 104):
        y = 74 if x in (44, 64, 84) else 70
        b += f'<circle cx="{x}" cy="{y}" r="4.2" fill="#FFE066" {o(1.8)}/>'
    b += gloss(36, 64, 10, 3, -10, .5) + sparkle(112, 22, 6) + sparkle(14, 26, 4.5)
    return svg(d, b)


def planet():
    d = Defs()
    pl = d.rad("#FFD39A", "#F07C4A", 0.38, 0.3, 0.85)
    ring = d.lin("#B9A3FF", "#6C8BFF", 0, 0, 1, 0)
    b = ''
    b += f'<path d="M8,74 Q4,58 28,52 L32,60 Q16,64 18,70 Q22,78 64,76 Q106,72 110,64 Q112,58 98,58 L100,50 Q126,52 120,66 Q114,82 64,86 Q14,90 8,74 Z" fill="{ring}" {o()}/>'
    b += f'<circle cx="64" cy="62" r="38" fill="{pl}" {o()}/>'
    b += f'<path d="M30,48 Q64,40 98,48 M28,74 Q64,82 100,74" fill="none" stroke="#F7A06B" stroke-width="5" stroke-linecap="round" opacity=".7"/>'
    b += face(64, 60, 1.05, "#A1421B", d, "open")
    # ring front part
    b += f'<path d="M26,74 Q14,72 18,66 L8,72 Q10,88 64,86 Q118,82 120,66 L110,64 Q112,70 104,72 Q90,78 64,80 Q38,80 26,74 Z" fill="{ring}" {o()}/>'
    b += gloss(48, 40, 12, 5, -30, .55) + sparkle(110, 18, 6) + sparkle(18, 22, 5, "#9EE7FF") + sparkle(112, 104, 4)
    return svg(d, b)


def rainbow():
    d = Defs()
    b = ''
    cols = ("#FF6B7A", "#FFA94D", "#FFE066", "#69DB7C", "#4DABF7", "#9775FA")
    for i, c in enumerate(cols):
        r = 52 - i * 7
        b += f'<path d="M{64 - r},86 A{r},{r} 0 0 1 {64 + r},86" fill="none" stroke="{c}" stroke-width="7.6"/>'
    b += f'<path d="M8,86 A56,56 0 0 1 120,86 L106,86 A42,42 0 0 0 22,86 Z" fill="none" {o(0)}/>'
    b += f'<path d="M8.2,86 A55.8,55.8 0 0 1 119.8,86" fill="none" {o()}/><path d="M24,86 A40,40 0 0 1 104,86" fill="none" {o()}/>'
    cl = d.rad("#FFFFFF", "#DCE8F7", 0.4, 0.3, 0.9)
    for cx in (20, 108):
        b += f'<path d="M{cx - 18},100 Q{cx - 22},86 {cx - 10},84 Q{cx - 8},72 {cx + 2},76 Q{cx + 14},70 {cx + 16},84 Q{cx + 24},88 {cx + 18},100 Z" fill="{cl}" {o()}/>'
    b += face(20, 88, 0.55, "#4D6AA8", d, "w", gap=8) + face(108, 88, 0.55, "#4D6AA8", d, "w", gap=8)
    b += sparkle(64, 18, 6) + sparkle(30, 30, 4) + sparkle(98, 30, 4)
    return svg(d, b)


def castle():
    d = Defs()
    wall = d.lin("#FFE3F1", "#F5A8CF")
    roof = d.lin("#B79BFF", "#7048E8")
    b = ''
    for x, top, w in ((14, 44, 22), (92, 44, 22)):
        b += f'<path d="M{x - 4},{top} L{x + w / 2},{top - 28} L{x + w + 4},{top} Z" fill="{roof}" {o()}/>'
        b += f'<rect x="{x}" y="{top}" width="{w}" height="{112 - top}" fill="{wall}" {o()}/>'
        b += f'<path d="M{x + w / 2},{top - 28} L{x + w / 2},{top - 38} L{x + w / 2 + 10},{top - 34} L{x + w / 2},{top - 30}" fill="#FF6B7A" {o(1.8)}/>'
        b += f'<rect x="{x + w / 2 - 4}" y="{top + 14}" width="8" height="12" rx="4" fill="#7FD3FF" {o(1.8)}/>'
    b += f'<path d="M40,30 L64,4 L88,30 Z" fill="{roof}" {o()}/>'
    b += f'<rect x="36" y="30" width="56" height="82" fill="{wall}" {o()}/>'
    b += f'<path d="M36,30 h8 v-6 h8 v6 h8 v-6 h8 v6 h8 v-6 h8 v6 h8" fill="none" {o(2)}/>'
    b += f'<path d="M52,112 L52,90 Q64,76 76,90 L76,112 Z" fill="#B76E3E" {o()}/>'
    b += f'<circle cx="72" cy="100" r="1.8" fill="{INK}"/>'
    b += f'<path d="M64,4 L64,-6 L74,-2 L64,2" fill="#FFD23F" {o(1.8)}/>'
    b += f'<path d="M56,52 Q64,44 72,52 L72,62 L56,62 Z" fill="#7FD3FF" {o(2)}/>'
    b += sparkle(64, 70, 4.2, "#FFD23F") + gloss(50, 40, 6, 3, -20, .6)
    b += sparkle(116, 16, 5) + sparkle(10, 16, 4.5)
    return svg(d, b).replace('viewBox="-6 -6 140 140"', 'viewBox="-6 -16 140 148"')


STICKERS = {"unicorn": unicorn, "dragon": dragon, "dinosaur": dinosaur, "rocket": rocket,
            "ufo": ufo, "planet": planet, "rainbow": rainbow, "castle": castle}
