from common import *

SPRINKLE_COLS = ("#FF6B7A", "#4DABF7", "#FFE066", "#69DB7C", "#FFFFFF", "#9775FA")


def donut():
    d = Defs()
    dough = d.rad("#FFD9A0", "#D98A3D", 0.4, 0.3, 0.9)
    icing = d.rad("#FFC2DD", "#FF6FA9", 0.4, 0.3, 0.9)
    b = f'<circle cx="64" cy="66" r="50" fill="{dough}" {o()}/>'
    b += (f'<path d="M64,22 Q84,20 98,32 Q112,40 108,56 Q114,70 106,82 Q104,98 88,100 Q76,110 62,104 '
          f'Q46,110 36,100 Q20,98 22,82 Q14,70 22,56 Q18,40 32,32 Q44,20 64,22 Z" fill="{icing}" {o()}/>')
    b += f'<circle cx="64" cy="66" r="14" fill="#FFF7EC" {o()}/>'
    import random
    rnd = random.Random(7)
    for i in range(16):
        while True:
            x, y = rnd.uniform(30, 98), rnd.uniform(30, 98)
            dist = ((x - 64) ** 2 + (y - 66) ** 2) ** 0.5
            if 20 < dist < 36 and not (y > 72 and abs(x - 64) < 26):
                break
        a = rnd.uniform(0, 180)
        b += f'<rect x="{x - 4:.1f}" y="{y - 1.5:.1f}" width="8" height="3" rx="1.5" fill="{SPRINKLE_COLS[i % 6]}" stroke="{INK}" stroke-width=".9" transform="rotate({a:.0f} {x:.1f} {y:.1f})"/>'
    b += face(64, 84, 0.72, "#B0306A", d, "w", gap=13)
    b += gloss(42, 36, 12, 5, -35, .55) + sparkle(114, 20, 6) + sparkle(14, 108, 4.5)
    return svg(d, b)


def ice_cream():
    d = Defs()
    cone = d.lin("#FFD58A", "#D9902E")
    s1 = d.rad("#FFE1EE", "#FF8FBF", 0.4, 0.3, 0.9)
    s2 = d.rad("#E7FFF4", "#7FE0B6", 0.4, 0.3, 0.9)
    b = f'<path d="M36,70 L64,124 L92,70 Z" fill="{cone}" {o()}/>'
    for i in range(4):
        b += f'<path d="M{40 + i * 9},70 L{70 + i * 4},{112 - i * 10}" stroke="#B8761F" stroke-width="2" opacity=".7"/>'
        b += f'<path d="M{88 - i * 9},70 L{58 - i * 4},{112 - i * 10}" stroke="#B8761F" stroke-width="2" opacity=".7"/>'
    b += f'<path d="{bumps_path(64, 34, 22, 9, 6, 0.3)}" fill="{s2}" {o()}/>'
    b += (f'<path d="M30,72 Q24,56 36,50 Q44,40 64,42 Q84,40 92,50 Q104,56 98,72 Q92,80 84,74 Q78,82 70,76 '
          f'Q64,84 58,76 Q50,82 44,74 Q36,80 30,72 Z" fill="{s1}" {o()}/>')
    b += f'<circle cx="66" cy="10" r="8" fill="#E8344E" {o()}/><path d="M66,2 Q70,-6 78,-4" fill="none" {o(2)}/>'
    b += gloss(63, 7, 3, 2, -30, .8)
    b += face(64, 58, 0.78, "#C2417E", d, "open", gap=12)
    b += gloss(50, 26, 7, 3.5, -30, .6)
    return svg(d, f'<g transform="translate(0,4)">{b}</g>').replace('viewBox="-6 -6 140 140"', 'viewBox="-6 -10 140 146"')


def cupcake():
    d = Defs()
    cup = d.lin("#7FD3FF", "#3E8EF7")
    cream = d.rad("#FFF6FB", "#FFC2DD", 0.4, 0.3, 0.9)
    b = f'<path d="M26,66 L102,66 L92,116 L36,116 Z" fill="{cup}" {o()}/>'
    for x in (40, 52, 64, 76, 88):
        b += f'<path d="M{x},68 L{x + (x - 64) * 0.12 :.1f},114" stroke="#2F6FD0" stroke-width="2.2" opacity=".6"/>'
    b += f'<path d="M20,68 Q14,52 30,48 Q30,32 48,32 Q52,18 66,20 Q82,18 84,32 Q100,32 100,48 Q114,52 108,68 Q64,80 20,68 Z" fill="{cream}" {o()}/>'
    b += f'<path d="M34,52 Q50,58 66,50 Q82,58 96,50" fill="none" stroke="#FF9CC8" stroke-width="2.4" stroke-linecap="round"/>'
    b += f'<circle cx="66" cy="14" r="9" fill="#E8344E" {o()}/><path d="M66,5 Q70,-4 80,-2" fill="none" {o(2)}/>' + gloss(63, 11, 3, 2, -30, .8)
    import random
    rnd = random.Random(3)
    for i in range(9):
        x, y = rnd.uniform(30, 98), rnd.uniform(34, 58)
        b += f'<rect x="{x - 3.5:.1f}" y="{y - 1.3:.1f}" width="7" height="2.6" rx="1.3" fill="{SPRINKLE_COLS[i % 6]}" stroke="{INK}" stroke-width=".8" transform="rotate({rnd.uniform(0, 180):.0f} {x:.1f} {y:.1f})"/>'
    b += face(64, 86, 0.78, "#1F4FA8", d, "w", gap=14)
    b += gloss(40, 42, 8, 4, -30, .7) + sparkle(116, 30, 5.5) + sparkle(12, 96, 4.5)
    return svg(d, f'<g transform="translate(0,4)">{b}</g>').replace('viewBox="-6 -6 140 140"', 'viewBox="-6 -8 140 144"')


def watermelon():
    d = Defs()
    flesh = d.rad("#FF9AA6", "#F0435A", 0.5, 0.2, 0.9)
    b = f'<path d="M10,40 Q64,140 118,40 Z" fill="#2FA84F" {o()}/>'
    b += f'<path d="M16,40 Q64,128 112,40 Z" fill="#E9FFD6"/>'
    b += f'<path d="M22,40 Q64,118 106,40 Z" fill="{flesh}" {o(2)}/>'
    b += f'<path d="M10,40 L118,40" {o()}/>'
    for x, y in ((40, 52), (88, 52), (52, 70), (76, 70), (64, 86)):
        b += f'<ellipse cx="{x}" cy="{y}" rx="2.6" ry="4" fill="{INK}"/>'
    b += eyes(50, 78, 56, 5.8, "#9B1D2E", d)
    b += blushes(40, 88, 64, 4.6, 2.8)
    b += mouth_open(64, 64, 4.4)
    b += gloss(36, 46, 8, 3, -30, .5) + sparkle(112, 98, 6) + sparkle(16, 100, 4.5) + sparkle(64, 18, 4.5)
    return svg(d, b)


def balloon():
    d = Defs()
    bl = d.rad("#FF9AA6", "#E8344E", 0.35, 0.28, 0.85)
    b = f'<path d="M64,98 Q56,108 66,114 Q76,120 62,128" fill="none" {o(2.2)}/>'
    b += f'<path d="M64,8 Q104,8 104,50 Q104,82 70,96 L58,96 Q24,82 24,50 Q24,8 64,8 Z" fill="{bl}" {o()}/>'
    b += f'<path d="M58,96 L56,104 L72,104 L70,96 Z" fill="#E8344E" {o(2)}/>'
    b += face(64, 52, 1.05, "#8E1B2C", d, "open")
    b += f'<ellipse cx="44" cy="30" rx="8" ry="13" fill="#fff" opacity=".6" transform="rotate(25 44 30)"/>'
    b += '<circle cx="54" cy="18" r="3" fill="#fff" opacity=".7"/>'
    b += sparkle(112, 22, 6) + sparkle(16, 90, 4.5) + sparkle(110, 92, 3.5)
    return svg(d, b).replace('viewBox="-6 -6 140 140"', 'viewBox="-6 -6 140 144"')


def lollipop():
    d = Defs()
    stick = d.lin("#FFFFFF", "#D7DEEB", 0, 0, 1, 0)
    b = f'<rect x="59" y="80" width="10" height="44" rx="5" fill="{stick}" {o()}/>'
    b += f'<circle cx="64" cy="52" r="42" fill="#FFF0F6" {o()}/>'
    cols = ("#FF6B7A", "#FFC06B", "#69DB7C", "#4DABF7", "#B79BFF")
    import math
    for k in range(5):
        pts = []
        for i in range(60):
            t = i / 59
            a = math.radians(k * 72 + t * 400)
            r = 4 + t * 36
            pts.append(f"{64 + r * math.cos(a):.1f},{52 + r * math.sin(a):.1f}")
        b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{cols[k]}" stroke-width="7" stroke-linecap="round"/>'
    b += f'<circle cx="64" cy="52" r="42" fill="none" {o()}/>'
    b += f'<path d="M50,90 Q64,98 78,90 L74,100 Q64,104 54,100 Z" fill="#FFD23F" {o(2)}/>'
    b += f'<ellipse cx="44" cy="32" rx="12" ry="7" fill="#fff" opacity=".55" transform="rotate(-35 44 32)"/>'
    b += sparkle(114, 18, 6) + sparkle(14, 96, 4.5)
    return svg(d, b)


def cake():
    d = Defs()
    sponge = d.lin("#FFF4DE", "#F3CF94")
    cream = d.rad("#FFFFFF", "#F1ECF7", 0.4, 0.3, 0.9)
    plate = d.lin("#E3F2FF", "#9FC6EE")
    b = f'<ellipse cx="64" cy="112" rx="56" ry="10" fill="{plate}" {o()}/>'
    # body
    b += f'<path d="M18,58 L18,100 Q18,112 64,112 Q110,112 110,100 L110,58 Z" fill="{sponge}" {o()}/>'
    b += '<path d="M18,80 Q64,92 110,80 L110,86 Q64,98 18,86 Z" fill="#FF8FA3"/>'
    for x in (30, 50, 78, 98):
        b += f'<ellipse cx="{x}" cy="{86 if x in (50, 78) else 84}" rx="5" ry="3.4" fill="#E8344E" {o(1.4)}/>'
    # cream top with drips
    b += (f'<path d="M18,58 Q18,40 64,40 Q110,40 110,58 L110,64 Q104,72 98,64 Q92,74 84,66 Q76,76 68,66 '
          f'Q60,76 52,66 Q44,74 38,64 Q30,72 24,64 Q20,70 18,64 Z" fill="{cream}" {o()}/>')
    b += '<ellipse cx="64" cy="50" rx="40" ry="8" fill="#FFF" opacity=".7"/>'
    # strawberries + cream dollops on top
    for x, y in ((40, 46), (88, 46)):
        b += f'<path d="{bumps_path(x, y, 6, 6, 3)}" fill="#fff" {o(1.8)}/>'
    sb = d.rad("#FF8C9A", "#D7263D", 0.38, 0.3, 0.85)
    b += f'<path d="M64,14 Q80,14 78,32 Q74,46 64,48 Q54,46 50,32 Q48,14 64,14 Z" fill="{sb}" {o()}/>'
    b += f'<path d="M56,17 Q64,8 72,17 Q64,20 56,17 Z" fill="#2FA84F" {o(1.6)}/>'
    for x, y in ((58, 26), (70, 26), (64, 34), (60, 40), (68, 40)):
        b += f'<ellipse cx="{x}" cy="{y}" rx="1.1" ry="1.7" fill="#FFE48A"/>'
    b += gloss(58, 22, 2.6, 4.5, 20, .7)
    b += face(64, 99, 0.62, "#B5602A", d, "w", gap=14)
    b += gloss(34, 48, 9, 3, -10, .6) + sparkle(114, 22, 6) + sparkle(14, 26, 4.5)
    return svg(d, b)


def strawberry():
    d = Defs()
    sb = d.rad("#FF8C9A", "#D7263D", 0.38, 0.3, 0.85)
    b = f'<path d="M64,30 Q112,26 108,62 Q104,96 64,118 Q24,96 20,62 Q16,26 64,30 Z" fill="{sb}" {o()}/>'
    for x, y in ((40, 48), (88, 48), (32, 66), (96, 66), (46, 92), (82, 92), (64, 104), (64, 40), (52, 80), (76, 80)):
        b += f'<path d="M{x},{y - 2.4} Q{x + 1.6},{y} {x},{y + 2.4} Q{x - 1.6},{y} {x},{y - 2.4} Z" fill="#FFE48A"/>'
    lf = d.lin("#7FE07A", "#2FA84F")
    b += (f'<path d="M64,34 Q48,40 34,30 Q46,26 50,22 Q46,12 58,14 Q62,6 64,14 Q66,6 70,14 Q82,12 78,22 '
          f'Q82,26 94,30 Q80,40 64,34 Z" fill="{lf}" {o()}/>')
    b += f'<path d="M64,16 Q64,4 72,2" fill="none" stroke="#2FA84F" stroke-width="4" stroke-linecap="round"/>'
    b += face(64, 64, 1.0, "#8E1B2C", d, "open")
    b += gloss(42, 46, 8, 4.5, -30, .6) + sparkle(114, 22, 6) + sparkle(14, 100, 4.5)
    return svg(d, b)


STICKERS = {"donut": donut, "ice_cream": ice_cream, "cupcake": cupcake, "watermelon": watermelon,
            "balloon": balloon, "lollipop": lollipop, "cake": cake, "strawberry": strawberry}
