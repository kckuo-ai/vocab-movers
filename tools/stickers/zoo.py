from common import *


def lion():
    d = Defs()
    mane = d.rad("#FFB347", "#D9661F", 0.5, 0.45, 0.6)
    fac = d.rad("#FFF0B8", "#F7C548", 0.4, 0.3, 0.8)
    b = f'<path d="{bumps_path(64, 66, 40, 12, 12)}" fill="{mane}" {o()}/>'
    b += f'<circle cx="40" cy="38" r="9" fill="{fac}" {o()}/><circle cx="88" cy="38" r="9" fill="{fac}" {o()}/>'
    b += '<circle cx="40" cy="38" r="4" fill="#F29E4C"/><circle cx="88" cy="38" r="4" fill="#F29E4C"/>'
    b += f'<ellipse cx="64" cy="68" rx="30" ry="28" fill="{fac}" {o()}/>'
    b += '<ellipse cx="64" cy="82" rx="14" ry="9" fill="#FFF8DE"/>'
    b += eyes(52, 76, 64, 6.4, "#8A4B16", d)
    b += blushes(44, 84, 76, 5, 3)
    b += f'<path d="M60,74 Q64,71 68,74 Q66,79 64,79 Q62,79 60,74 Z" fill="#7A3B2E" {o(1.8)}/>'
    b += mouth_w(64, 82, 2.6)
    b += gloss(50, 50, 9, 4, -20, .5) + sparkle(110, 22, 6) + sparkle(18, 104, 4.5)
    return svg(d, b)


def tiger():
    d = Defs()
    fur = d.rad("#FFC266", "#F07A1A", 0.45, 0.3, 0.85)
    b = ''
    for x in (34, 94):
        b += f'<circle cx="{x}" cy="34" r="12" fill="{fur}" {o()}/><circle cx="{x}" cy="35" r="6" fill="#FFE7D1"/>'
    b += f'<path d="M18,70 Q18,30 64,28 Q110,30 110,70 Q110,104 64,106 Q18,104 18,70 Z" fill="{fur}" {o()}/>'
    b += '<path d="M30,82 Q40,70 64,74 Q88,70 98,82 Q92,102 64,104 Q36,102 30,82 Z" fill="#FFF6EA"/>'
    # stripes
    for p in ("M56,30 Q60,38 58,46", "M64,29 L64,42", "M72,30 Q68,38 70,46",
              "M19,64 Q28,64 32,68", "M20,76 Q27,75 30,78", "M109,64 Q100,64 96,68", "M108,76 Q101,75 98,78"):
        b += f'<path d="{p}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
    b += eyes(48, 80, 62, 7, "#3F7D3A", d)
    b += blushes(38, 90, 76, 5, 3)
    b += f'<path d="M59,75 Q64,72 69,75 Q67,80 64,80 Q61,80 59,75 Z" fill="#E86A8A" {o(1.8)}/>'
    b += mouth_w(64, 84, 2.8)
    b += gloss(44, 44, 10, 4.5, -20, .5) + sparkle(112, 102, 5.5)
    return svg(d, b)


def panda():
    d = Defs()
    wh = d.rad("#FFFFFF", "#DCE2EC", 0.4, 0.3, 0.9)
    blk = d.lin("#4A4458", "#211B2B")
    b = f'<circle cx="34" cy="34" r="13" fill="{blk}" {o()}/><circle cx="94" cy="34" r="13" fill="{blk}" {o()}/>'
    b += f'<ellipse cx="64" cy="68" rx="46" ry="41" fill="{wh}" {o()}/>'
    b += f'<ellipse cx="46" cy="64" rx="13" ry="16" fill="{blk}" transform="rotate(28 46 64)"/>'
    b += f'<ellipse cx="82" cy="64" rx="13" ry="16" fill="{blk}" transform="rotate(-28 82 64)"/>'
    b += eye(47, 63, 6.5, "#6B6F86", d) + eye(81, 63, 6.5, "#6B6F86", d)
    b += blushes(34, 94, 82, 5.5, 3.2)
    b += f'<ellipse cx="64" cy="79" rx="5.5" ry="3.8" fill="{INK}"/>'
    b += mouth_w(64, 87, 2.6)
    b += gloss(44, 40, 11, 4.5, -25, .7) + sparkle(112, 76, 5) + sparkle(16, 98, 4)
    return svg(d, b)


def koala():
    d = Defs()
    fur = d.rad("#D3DAE5", "#8E9AAE", 0.45, 0.3, 0.85)
    b = ''
    for x in (24, 104):
        b += f'<circle cx="{x}" cy="46" r="20" fill="{fur}" {o()}/><circle cx="{x}" cy="48" r="11" fill="#F7D9E3"/>'
    b += f'<ellipse cx="64" cy="70" rx="40" ry="36" fill="{fur}" {o()}/>'
    b += eyes(46, 82, 64, 6, "#4D5B7A", d)
    b += blushes(38, 90, 80, 5, 3)
    nose = d.lin("#5A5468", "#2A2230")
    b += f'<ellipse cx="64" cy="76" rx="9" ry="12" fill="{nose}" {o(2)}/>'
    b += '<ellipse cx="61" cy="70" rx="3" ry="4" fill="#fff" opacity=".55"/>'
    b += mouth_smile(64, 92, 4)
    b += gloss(48, 44, 11, 4.5, -20, .55) + sparkle(110, 102, 5)
    return svg(d, b)


def fox():
    d = Defs()
    fur = d.lin("#FFA24C", "#E8641E")
    b = ''
    b += f'<path d="M24,58 L30,14 L56,40 Z" fill="{fur}" {o()}/><path d="M104,58 L98,14 L72,40 Z" fill="{fur}" {o()}/>'
    b += f'<path d="M30,48 L33,24 L46,38 Z" fill="#3B2A40"/><path d="M98,48 L95,24 L82,38 Z" fill="#3B2A40"/>'
    b += f'<path d="M18,62 Q20,36 64,34 Q108,36 110,62 Q106,84 84,98 Q72,108 64,108 Q56,108 44,98 Q22,84 18,62 Z" fill="{fur}" {o()}/>'
    b += '<path d="M20,66 Q40,64 52,76 Q58,86 64,86 Q70,86 76,76 Q88,64 108,66 Q104,84 84,98 Q72,108 64,108 Q56,108 44,98 Q24,84 20,66 Z" fill="#FFF8EE"/>'
    b += eyes(48, 80, 64, 6.8, "#B85A12", d)
    b += blushes(36, 92, 78, 5, 3)
    b += f'<ellipse cx="64" cy="88" rx="5" ry="3.6" fill="{INK}"/>'
    b += mouth_w(64, 95, 2.4)
    b += gloss(46, 46, 10, 4, -15, .5) + sparkle(112, 30, 5.5) + sparkle(14, 100, 4)
    return svg(d, b)


def hedgehog():
    d = Defs()
    sp = d.lin("#9C6B4E", "#5E3C2E")
    skin = d.rad("#FFE9CF", "#F2C08E", 0.4, 0.35, 0.9)
    b = f'<path d="{spikes_path(70, 72, 36, 50, 9, 160, 380)} Z" fill="{sp}" {o()}/>'
    b += f'<ellipse cx="70" cy="74" rx="38" ry="32" fill="{sp}"/>'
    b += f'<path d="M14,84 Q16,56 46,54 Q74,56 76,82 Q74,106 46,108 Q18,106 14,84 Z" fill="{skin}" {o()}/>'
    b += f'<circle cx="14" cy="84" r="5" fill="{INK}"/><circle cx="12.5" cy="82.5" r="1.6" fill="#fff"/>'
    b += eye(34, 78, 6.2, "#5E3C2E", d) + eye(56, 78, 6.2, "#5E3C2E", d)
    b += blushes(28, 64, 92, 4.8, 3)
    b += mouth_w(42, 95, 2.4)
    b += f'<ellipse cx="54" cy="112" rx="8" ry="4" fill="#F2C08E" {o(2)}/><ellipse cx="88" cy="110" rx="8" ry="4" fill="#F2C08E" {o(2)}/>'
    b += gloss(80, 40, 12, 4, -20, .35) + sparkle(112, 22, 6) + sparkle(22, 30, 4)
    return svg(d, b)


def frog():
    d = Defs()
    sk = d.rad("#A6EB7A", "#3FAE4A", 0.45, 0.3, 0.85)
    b = f'<circle cx="38" cy="40" r="17" fill="{sk}" {o()}/><circle cx="90" cy="40" r="17" fill="{sk}" {o()}/>'
    b += f'<path d="M14,76 Q14,46 64,46 Q114,46 114,76 Q114,108 64,108 Q14,108 14,76 Z" fill="{sk}" {o()}/>'
    b += '<path d="M26,86 Q64,104 102,86 Q96,104 64,106 Q32,104 26,86 Z" fill="#E9FFD6" opacity=".9"/>'
    b += eye(38, 40, 9.5, "#2F7D32", d) + eye(90, 40, 9.5, "#2F7D32", d)
    b += blushes(30, 98, 78, 6.5, 3.6)
    b += f'<path d="M40,74 Q64,94 88,74" fill="none" {o(2.8)}/>'
    b += f'<circle cx="58" cy="62" r="1.8" fill="{INK}"/><circle cx="70" cy="62" r="1.8" fill="{INK}"/>'
    b += gloss(36, 56, 12, 4, -15, .45) + sparkle(112, 18, 6) + sparkle(16, 112, 4.5)
    return svg(d, b)


def penguin():
    d = Defs()
    body = d.lin("#4C5C86", "#1F2744")
    belly = d.rad("#FFFFFF", "#DDE5F2", 0.45, 0.35, 0.9)
    b = f'<path d="M20,80 Q16,98 30,92" fill="{body}" {o()}/><path d="M108,80 Q112,98 98,92" fill="{body}" {o()}/>'
    b += f'<ellipse cx="46" cy="114" rx="10" ry="5" fill="#FFA62B" {o(2)}/><ellipse cx="82" cy="114" rx="10" ry="5" fill="#FFA62B" {o(2)}/>'
    b += f'<path d="M64,12 Q106,12 106,62 Q106,110 64,112 Q22,110 22,62 Q22,12 64,12 Z" fill="{body}" {o()}/>'
    b += f'<path d="M64,40 Q68,28 82,28 Q98,30 96,52 Q96,74 92,88 Q84,106 64,106 Q44,106 36,88 Q32,74 32,52 Q30,30 46,28 Q60,28 64,40 Z" fill="{belly}"/>'
    b += eyes(50, 78, 52, 6.6, "#3D5A98", d)
    b += blushes(42, 86, 66, 5, 3)
    b += f'<path d="M57,62 Q64,58 71,62 Q64,72 57,62 Z" fill="#FFA62B" {o(2)}/>'
    b += gloss(46, 24, 10, 4, -15, .4) + sparkle(114, 30, 6) + sparkle(14, 40, 4.5)
    return svg(d, b)


STICKERS = {"lion": lion, "tiger": tiger, "panda": panda, "koala": koala,
            "fox": fox, "hedgehog": hedgehog, "frog": frog, "penguin": penguin}
