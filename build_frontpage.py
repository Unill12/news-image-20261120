#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news front page (1024x1024 PNG).

36 stories, all reported on Friday 20 November 2026 (overnight wires,
morning briefings and same-day reports). Nothing invented; every number
comes from the cited report; claims are attributed to whoever made them.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (252, 252, 247)
INK = (16, 16, 16)
RED = (176, 22, 22)
NAVY = (24, 38, 64)
GREY = (108, 108, 100)
LIGHT = (236, 236, 230)
RULE = (198, 198, 190)
SEA = (222, 232, 238)
LAND = (196, 205, 190)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
REG = os.path.join(FONT_DIR, "DejaVuSans.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(d, x, y, lines, fnt, fill=INK, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.22)
    for line in lines:
        d.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def story(d, x, y, w, tag, head, deck, head_size=21, deck_size=15):
    d.text((x, y), tag, font=font(BOLD, 13), fill=RED)
    y += 17
    hf = font(BOLD, head_size)
    y = block(d, x, y, wrap(d, head, hf, w)[:2], hf,
              leading=head_size + 4)
    df = font(REG, deck_size)
    y = block(d, x, y + 1, wrap(d, deck, df, w)[:2], df,
              leading=deck_size + 4)
    return y + 6


# ---- Stories -------------------------------------------------------
LEAD = ("UKRAINE  \u00b7  KYIV",
        "Four ballistic missiles hit Kyiv overnight",
        "Capital struck in the early hours as air defences engaged.")

SECOND = [
    ("MIDDLE EAST  \u00b7  SAUDI ARABIA",
     "Houthis say they struck four Saudi targets",
     "Riyadh airport, a financial centre, a petrochemical plant and "
     "an air base named; investors told to leave."),
    ("UNITED STATES  \u00b7  BASEBALL",
     "Trump pardons the late Pete Rose",
     "Posthumous pardon for tax crimes; the hits leader, banned in "
     "1989, died in 2024."),
]

COLUMNS = [
    [
        ("ITALY  \u00b7  DRONES",
         "Mystery drones shut Genoa airport",
         "Flights halted for four hours overnight after unidentified "
         "drones were seen."),
        ("GULF  \u00b7  SHIPPING",
         "Tanker ablaze after hitting a mine",
         "Vessel struck a mine east of the Strait of Hormuz; fire "
         "reported aboard."),
        ("UNITED STATES  \u00b7  CONGRESS",
         "Senate rejects Iran war-powers bid",
         "Resolution fails 51\u201348; it would have curbed strikes "
         "on Iran."),
    ],
    [
        ("GERMANY  \u00b7  UKRAINE",
         "Allies warn against a Yalta-style deal",
         "European leaders meet in Berlin; Trump phones in and says "
         "Putin wants a deal."),
        ("CLIMATE  \u00b7  COP31",
         "Climate talks close in Antalya",
         "Final day of COP31; draft runs 144 paragraphs with $120bn "
         "on the table."),
        ("INDIA  \u00b7  WEATHER",
         "Cyclone Akvan comes ashore at noon",
         "Storm crosses the Odisha\u2013Andhra coast; about 300,000 "
         "people evacuated."),
    ],
    [
        ("LEBANON  \u00b7  STRIKES",
         "Israel hits Hezbollah missile site",
         "Airstrike on a facility in eastern Lebanon, reports say."),
        ("FRANCE  \u00b7  FIRE",
         "One dead in tower-block fire",
         "Blaze in an 18-storey apartment building injures 15."),
        ("GAZA  \u00b7  AID",
         "Aid groups rate Gaza plan 4 of 26",
         "Five agencies say the 20-point peace plan is barely "
         "implemented."),
    ],
]

ALSO = [
    "UK, Norway fund two Ukrainian naval craft",
    "US, Venezuela agree to restore military ties",
    "S. Korea court clears ex-PM Han Duck-soo",
    "Fiji declares a disaster as drought bites",
    "N. Korea expands Yongbyon enrichment",
    "AI data centres need $3.9tn by 2030: IEA",
    "Congo Ebola cases pass 10,600: WHO",
    "NFL bans Rams' Puka Nacua for three games",
    "Belichick, Kraft are Hall of Fame finalists",
    "LA Sparks sale nears $750m",
    "Edwards upbeat after knee surgery",
    "Thai PM meets Putin at APEC",
    "Shelton reaches ATP Finals last four",
    "Lee Kang-in is Asia's top overseas player",
    "Foord is Asia's women's player of the year",
    "Beiranvand first keeper to win AFC award",
    "Thailand climb to 90th in FIFA rankings",
    "Indian state banks post record profit",
    "US asks top court to end Venezuelan TPS",
    "Storm Xavier alerts for Cook Islands",
    "F1 in Las Vegas with titles decided",
    "Spirit face Current in NWSL final",
    "France, Germany, UK weigh Russia talks",
    "APEC leaders' week continues",
]

# Rough equirectangular continent outlines (lon, lat).
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 68), (-95, 80), (-85, 66),
     (-75, 60), (-65, 45), (-80, 25), (-97, 16), (-105, 20), (-117, 32),
     (-125, 48), (-150, 60), (-168, 66)],
    [(-58, 64), (-45, 60), (-30, 68), (-45, 76), (-58, 74)],
    [(-80, 10), (-60, 5), (-50, 0), (-40, -5), (-35, -10), (-40, -20),
     (-48, -28), (-58, -35), (-65, -45), (-70, -55), (-75, -40),
     (-80, -20), (-80, 10)],
    [(-17, 15), (-10, 30), (0, 35), (10, 37), (20, 32), (32, 31), (35, 28),
     (43, 12), (51, 10), (48, 0), (40, -10), (35, -20), (32, -28),
     (20, -35), (15, -30), (12, -18), (9, 0), (-8, 5), (-17, 15)],
    [(-10, 36), (-9, 43), (0, 48), (-2, 50), (5, 53), (8, 57), (10, 59),
     (5, 60), (12, 65), (18, 70), (30, 70), (40, 68), (50, 70), (60, 70),
     (70, 72), (80, 73), (90, 75), (100, 76), (110, 74), (120, 72),
     (130, 72), (140, 72), (150, 70), (160, 66), (170, 66), (178, 65),
     (170, 60), (162, 56), (158, 52), (150, 60), (142, 55), (140, 45),
     (135, 43), (130, 40), (127, 38), (122, 32), (120, 28), (110, 20),
     (105, 10), (100, 8), (97, 15), (92, 20), (88, 22), (85, 19),
     (80, 15), (76, 10), (72, 20), (66, 25), (60, 25), (56, 26),
     (52, 26), (48, 29), (44, 29), (40, 31), (36, 36), (30, 36),
     (26, 38), (22, 37), (18, 40), (12, 44), (8, 44), (3, 42), (0, 38),
     (-2, 37), (-6, 36), (-9, 37), (-10, 36)],
    [(113, -22), (114, -30), (115, -35), (120, -34), (129, -32),
     (132, -32), (135, -35), (140, -38), (145, -38), (150, -37),
     (153, -32), (150, -25), (146, -19), (142, -11), (136, -12),
     (132, -11), (126, -14), (122, -17), (118, -20), (113, -22)],
    [(-5, 50), (-3, 53), (-5, 56), (-2, 58), (0, 53), (-1, 51)],
    [(130, 31), (132, 33), (135, 34), (137, 35), (139, 36), (141, 39),
     (142, 42), (144, 44), (142, 40), (140, 38), (137, 37), (134, 35),
     (131, 33)],
    [(167, -45), (170, -42), (173, -40), (176, -38), (178, -37),
     (175, -40), (172, -43), (168, -46)],
]

# (name, lon, lat, label dy in px, label dx in px)
# dy: -16 above the dot, +7 below row 1, +22 below row 2.
MAP_DOTS = [
    ("Kyiv", 30.5, 50.5, -16, 8),
    ("Genoa", 8.9, 44.4, -16, -8),
    ("Riyadh", 46.7, 24.6, 22, -12),
    ("Hormuz", 56.5, 26.5, 7, 16),
    ("Antalya", 30.7, 36.9, 7, -16),
    ("Odisha", 85.5, 20.0, 7, 0),
    ("Shenzhen", 114.1, 22.5, 7, 0),
    ("Seoul", 127.0, 37.5, -16, 0),
    ("Suva", 178.4, -17.7, -16, -6),
]
# Dots too close to a neighbour to label without a collision.
UNLABELLED_DOTS = [
    ("Beirut", 35.5, 33.9),
]


def draw_map(d, x, y, w, h):
    d.rounded_rectangle([x, y, x + w, y + h], radius=8,
                        outline=RULE, width=1, fill=SEA)
    d.text((x + 12, y + 6), "WHERE TODAY HAPPENED",
           font=font(BOLD, 15), fill=INK)
    mx0, mx1 = x + 6, x + w - 6
    my0, my1 = y + 26, y + h - 6

    def proj(lon, lat):
        px = mx0 + (lon + 180.0) / 360.0 * (mx1 - mx0)
        py = my0 + (78.0 - lat) / (78.0 + 58.0) * (my1 - my0)
        return (px, py)

    for poly in CONTINENTS:
        d.polygon([proj(lon, lat) for lon, lat in poly], fill=LAND)
    lf = font(BOLD, 11)
    for name, lon, lat, dy, dx in MAP_DOTS:
        px, py = proj(lon, lat)
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=RED,
                  outline=PAPER, width=1)
        d.text((px + dx, py + dy), name, font=lf, fill=INK, anchor="ma")
    for _name, lon, lat in UNLABELLED_DOTS:
        px, py = proj(lon, lat)
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=RED,
                  outline=PAPER, width=1)


def draw_lead_art(d, x, y, w, h):
    """Night skyline over Kyiv: dark sky, moon, rooftops, red burst."""
    d.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=NAVY)
    d.ellipse([x + w - 42, y + 10, x + w - 18, y + 34], fill=(235, 235, 220))
    import random
    rng = random.Random(20261120)
    for _ in range(14):
        sx = x + rng.randint(6, w - 6)
        sy = y + rng.randint(6, h // 2)
        d.ellipse([sx, sy, sx + 2, sy + 2], fill=(220, 220, 200))
    base = y + h
    bx = x + 8
    for bw, bh in [(34, 46), (26, 62), (40, 38), (24, 54), (36, 44)]:
        d.rectangle([bx, base - bh, bx + bw, base], fill=(10, 16, 30))
        bx += bw + 5
    cx, cy = x + 52, y + 30
    import math
    for k in range(8):
        ang = k * math.pi / 4
        r = 17 if k % 2 == 0 else 9
        ex = cx + r * math.cos(ang)
        ey = cy + r * math.sin(ang) * 0.75
        d.line([(cx, cy), (ex, ey)], fill=(255, 90, 60), width=3)
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(255, 120, 70))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 28
    cw = W - 2 * mx

    # ---- Masthead ----
    y = 12
    d.text((W // 2, y), "THE WORLD IN A DAY", font=font(BOLD, 48),
           fill=INK, anchor="ma")
    y += 52
    d.line([(mx, y), (W - mx, y)], fill=RED, width=4)
    y += 7
    d.text((W // 2, y), "FRIDAY  20  NOVEMBER  2026",
           font=font(BOLD, 26), fill=RED, anchor="ma")
    y += 30
    d.text((W // 2, y),
           "Missiles over Kyiv \u00b7 Houthi strikes on Saudi targets "
           "\u00b7 COP31 closes",
           font=font(REG, 17), fill=GREY, anchor="ma")
    y += 21
    d.line([(mx, y), (W - mx, y)], fill=INK, width=2)

    # ---- Lead story + art ----
    y += 10
    art_w, art_h = 208, 104
    art_x = W - mx - art_w
    tag, head, deck = LEAD
    d.text((mx, y), tag, font=font(BOLD, 17), fill=RED)
    y += 23
    hf = font(BOLD, 33)
    lead_w = art_x - mx - 18
    y = block(d, mx, y, wrap(d, head, hf, lead_w), hf, leading=37)
    df = font(REG, 18)
    y = block(d, mx, y + 2, wrap(d, deck, df, lead_w), df, leading=21)
    draw_lead_art(d, art_x, y - 104 + 8, art_w, art_h)
    y += 8
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=1)

    # ---- Second row: two stories ----
    y += 7
    half_w = (cw - 20) // 2
    row_bottom = y
    for i, (tag, head, deck) in enumerate(SECOND):
        sx = mx + i * (half_w + 20)
        ey = story(d, sx, y, half_w, tag, head, deck,
                   head_size=23, deck_size=16)
        row_bottom = max(row_bottom, ey)
    y = row_bottom
    d.line([(mx, y - 4), (W - mx, y - 4)], fill=RULE, width=1)

    # ---- World map ----
    y += 6
    map_h = 116
    draw_map(d, mx, y, cw, map_h)
    y += map_h + 6

    # ---- Three columns, 3 stories each ----
    col_w = (cw - 2 * 20) // 3
    col_x = [mx, mx + col_w + 20, mx + 2 * (col_w + 20)]
    bottom = y
    for cx, stories in zip(col_x, COLUMNS):
        cy = y
        for tag, head, deck in stories:
            cy = story(d, cx, cy, col_w, tag, head, deck)
            d.line([(cx, cy - 4), (cx + col_w, cy - 4)], fill=RULE, width=1)
        bottom = max(bottom, cy)
    y = bottom + 2

    # ---- Also today: numbered briefs, 3 columns x 8 rows ----
    d.text((mx, y), "ALSO TODAY", font=font(BOLD, 17), fill=RED)
    y += 20
    af = font(REG, 13)
    bf = font(BOLD, 13)
    col_aw = (cw - 2 * 16) // 3
    for i, item in enumerate(ALSO):
        ix = mx + (i // 8) * (col_aw + 16)
        iy = y + (i % 8) * 15
        num = f"{i + 1}."
        d.text((ix, iy), num, font=bf, fill=RED)
        nw = d.textlength(num + " ", font=bf)
        tw = d.textlength(item, font=af)
        if nw + tw > col_aw:
            print("TOO WIDE:", item, round(nw + tw), "vs", col_aw)
        d.text((ix + nw, iy), item, font=af, fill=INK)
    y += 8 * 15 + 6

    # ---- Footer ----
    d.line([(mx, y), (W - mx, y)], fill=INK, width=1)
    d.text((W // 2, y + 6),
           "All stories reported on Friday 20 November 2026  \u00b7  "
           "36 stories",
           font=font(REG, 14), fill=GREY, anchor="ma")
    print("layout: footer rule at", y, "of", H)
    if y + 26 > H:
        print("OVERFLOW by", y + 26 - H, "px")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
