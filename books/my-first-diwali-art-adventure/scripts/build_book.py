#!/usr/bin/env python3
"""Build My First Diwali Art Adventure — print-ready HTML + PDF."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUT_HTML = ROOT / "book.html"
OUT_PDF = Path("/workspace/docs/pdf/My-First-Diwali-Art-Adventure.pdf")
PAGES_DIR = ROOT / "pages"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg_parts import (  # noqa: E402
    BROWN,
    GREEN,
    GUIDE,
    INK,
    ORANGE,
    PINK,
    RED,
    YELLOW,
    confetti,
    header,
    leaf,
    logo,
    marigold,
    page_footer,
    scatter_decor,
    sparkle,
)


def wrap_page(body: str, cover: bool = False) -> str:
    cls = "page cover" if cover else "page"
    return f'<section class="{cls}">{body}</section>\n'


def cover_page() -> str:
    art = f'''<svg class="cover-art" viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg">
  {marigold(80, 80, 22)}
  {marigold(520, 70, 20)}
  {marigold(90, 340, 18)}
  {marigold(510, 350, 19)}
  {sparkle(160, 50, 12)}
  {sparkle(440, 45, 11)}
  {sparkle(300, 30, 10)}
  {confetti(200, 70, 5, PINK)}
  {confetti(400, 80, 5, ORANGE)}
  <!-- big cute diya -->
  <ellipse cx="300" cy="280" rx="140" ry="55" fill="{RED}" stroke="{INK}" stroke-width="4"/>
  <path d="M180 260 Q300 230 420 260" fill="none" stroke="{YELLOW}" stroke-width="6"/>
  <circle cx="240" cy="285" r="8" fill="{YELLOW}" stroke="{INK}" stroke-width="2"/>
  <circle cx="300" cy="292" r="8" fill="{YELLOW}" stroke="{INK}" stroke-width="2"/>
  <circle cx="360" cy="285" r="8" fill="{YELLOW}" stroke="{INK}" stroke-width="2"/>
  <!-- kawaii face -->
  <path d="M270 275 Q278 282 286 275" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M314 275 Q322 282 330 275" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <circle cx="262" cy="285" r="5" fill="{PINK}"/>
  <circle cx="338" cy="285" r="5" fill="{PINK}"/>
  <path d="M292 295 Q300 302 308 295" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>
  <!-- flame -->
  <ellipse cx="300" cy="175" rx="36" ry="70" fill="{YELLOW}" stroke="{INK}" stroke-width="3.5"/>
  <ellipse cx="300" cy="185" rx="22" ry="45" fill="{ORANGE}" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="300" cy="195" rx="10" ry="22" fill="{RED}"/>
  {sparkle(240, 120, 10)}
  {sparkle(360, 115, 9)}
  <!-- kids peeking beside diya -->
  <circle cx="150" cy="210" r="24" fill="#FFD7A8" stroke="{INK}" stroke-width="3"/>
  <path d="M130 200 Q150 185 170 200" fill="#5D4037" stroke="{INK}" stroke-width="2"/>
  <path d="M140 208 Q150 202 160 208" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M142 218 Q150 224 158 218" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
  <circle cx="140" cy="220" r="3.5" fill="{PINK}"/>
  <circle cx="160" cy="220" r="3.5" fill="{PINK}"/>
  <path d="M120 245 Q150 275 180 245" fill="#6EC6FF" stroke="{INK}" stroke-width="3"/>
  <circle cx="450" cy="210" r="24" fill="#FFD7A8" stroke="{INK}" stroke-width="3"/>
  <path d="M430 200 Q450 185 470 200" fill="#5D4037" stroke="{INK}" stroke-width="2"/>
  <path d="M440 208 Q450 202 460 208" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M442 218 Q450 224 458 218" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
  <circle cx="440" cy="220" r="3.5" fill="{PINK}"/>
  <circle cx="460" cy="220" r="3.5" fill="{PINK}"/>
  <path d="M420 245 Q450 275 480 245" fill="{PINK}" stroke="{INK}" stroke-width="3"/>
</svg>'''
    return wrap_page(
        f'''
  {logo(160)}
  <h1>My First Diwali<br/>Art Adventure</h1>
  <p class="tagline">Color, trace, connect &amp; create — a festive workbook for little artists</p>
  <div class="ages">Ages 3–6</div>
  {art}
  <div class="bottom-meta">Pehla Page · Festival of Lights Activity Book</div>
''',
        cover=True,
    )


def page_join_dots() -> str:
    # Diya outline via numbered dots 1-12
    dots = [
        (300, 90),   # 1 flame tip
        (340, 140),  # 2
        (355, 200),  # 3
        (400, 250),  # 4 right rim
        (390, 320),  # 5
        (340, 360),  # 6
        (300, 375),  # 7 bottom
        (260, 360),  # 8
        (210, 320),  # 9
        (200, 250),  # 10 left rim
        (245, 200),  # 11
        (260, 140),  # 12
    ]
    dots_svg = ""
    guide = f'<path d="M{" L".join(f"{x},{y}" for x,y in dots)} Z" fill="none" stroke="{GUIDE}" stroke-width="2.5"/>'
    for i, (x, y) in enumerate(dots, 1):
        dots_svg += f'''<circle cx="{x}" cy="{y}" r="5" fill="{INK}"/>
        <text x="{x + 12}" y="{y - 8}" font-family="Nunito,sans-serif" font-size="16" font-weight="800" fill="#1B3A6B">{i}</text>'''
    predrawn = f'''
  <!-- pre-drawn bowl details -->
  <path d="M220 270 Q300 255 380 270" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M230 285 Q250 300 270 285 Q290 300 310 285 Q330 300 350 285 Q370 300 380 285" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="250" cy="305" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="300" cy="312" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="350" cy="305" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="300" cy="330" r="18" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="300" cy="330" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M300 312 L300 348 M282 330 L318 330 M288 318 L312 342 M312 318 L288 342" stroke="{INK}" stroke-width="1.8"/>
  <path d="M285 175 Q300 145 315 175 Q300 195 285 175" fill="none" stroke="{GUIDE}" stroke-width="2"/>
'''
    body = f'''
{header("Join the Diya Dots", "Connect the dots from 1 to 12. Then color the diya.")}
<div class="stage">
<svg class="main" viewBox="0 0 600 500" xmlns="http://www.w3.org/2000/svg">
  {scatter_decor()}
  {guide}
  {predrawn}
  {dots_svg}
</svg>
</div>
{page_footer(1)}
'''
    return wrap_page(body)


def page_copy_kandil() -> str:
    def grid(x0, y0, size=200, cells=4, content=""):
        step = size / cells
        lines = ""
        for i in range(cells + 1):
            lines += f'<line x1="{x0}" y1="{y0 + i * step}" x2="{x0 + size}" y2="{y0 + i * step}" stroke="{INK}" stroke-width="1.5"/>'
            lines += f'<line x1="{x0 + i * step}" y1="{y0}" x2="{x0 + i * step}" y2="{y0 + size}" stroke="{INK}" stroke-width="1.5"/>'
        return f'<rect x="{x0}" y="{y0}" width="{size}" height="{size}" fill="#fff" stroke="{INK}" stroke-width="3"/>{lines}{content}'

    # Colored kandil in left grid
    kandil = f'''
  <g transform="translate(70,70)">
    <rect x="85" y="10" width="30" height="18" rx="3" fill="{BROWN}" stroke="{INK}" stroke-width="2"/>
    <path d="M100 0 L100 10" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
    <polygon points="40,40 160,40 180,100 20,100" fill="{ORANGE}" stroke="{INK}" stroke-width="2.5"/>
    <polygon points="55,50 145,50 155,90 45,90" fill="{PINK}" stroke="{INK}" stroke-width="2"/>
    <polygon points="80,55 120,55 100,95" fill="{YELLOW}" stroke="{INK}" stroke-width="2"/>
    <circle cx="100" cy="72" r="8" fill="{RED}" stroke="{INK}" stroke-width="1.5"/>
    <path d="M45 100 L35 160 M70 100 L65 165 M100 100 L100 170 M130 100 L135 165 M155 100 L165 160"
          stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
    <circle cx="35" cy="165" r="5" fill="{YELLOW}" stroke="{INK}" stroke-width="1.5"/>
    <circle cx="65" cy="170" r="5" fill="#5BA4E6" stroke="{INK}" stroke-width="1.5"/>
    <circle cx="100" cy="175" r="5" fill="{PINK}" stroke="{INK}" stroke-width="1.5"/>
    <circle cx="135" cy="170" r="5" fill="{YELLOW}" stroke="{INK}" stroke-width="1.5"/>
    <circle cx="165" cy="165" r="5" fill="#5BA4E6" stroke="{INK}" stroke-width="1.5"/>
  </g>
'''
    body = f'''
{header("Copy the Kandil", "Look carefully and copy the picture in the empty box.")}
<div class="stage">
<svg class="main" viewBox="0 0 600 480" xmlns="http://www.w3.org/2000/svg">
  {scatter_decor()}
  <text x="170" y="48" text-anchor="middle" font-family="Nunito,sans-serif" font-size="14" font-weight="800" fill="#2F5A9A">Look</text>
  <text x="430" y="48" text-anchor="middle" font-family="Nunito,sans-serif" font-size="14" font-weight="800" fill="#2F5A9A">Draw</text>
  {grid(70, 60, 200, 4, kandil)}
  {grid(330, 60, 200, 4, "")}
</svg>
</div>
{page_footer(2)}
'''
    return wrap_page(body)


def page_dot_rangoli() -> str:
    circles = ""
    # Central ring of dots for marker coloring
    import math
    for i in range(8):
        a = i * (math.pi * 2 / 8)
        x = 300 + math.cos(a) * 55
        y = 250 + math.sin(a) * 55
        circles += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'
    for i in range(8):
        a = i * (math.pi * 2 / 8) + math.pi / 8
        x = 300 + math.cos(a) * 110
        y = 250 + math.sin(a) * 110
        circles += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'
    for i in range(12):
        a = i * (math.pi * 2 / 12)
        x = 300 + math.cos(a) * 155
        y = 250 + math.sin(a) * 155
        circles += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'

    petals = ""
    for i in range(8):
        a = i * 45
        petals += f'''<path d="M300 250 Q{300 + 90:.0f} {250 - 40:.0f} 300 {250 - 140}" fill="none" stroke="{INK}" stroke-width="3"
          transform="rotate({a} 300 250)"/>'''

    body = f'''
{header("Dot-Color the Rangoli", "Use dot markers or crayons to fill the circles.")}
<div class="stage">
<svg class="main" viewBox="0 0 600 500" xmlns="http://www.w3.org/2000/svg">
  {scatter_decor()}
  <circle cx="300" cy="250" r="40" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <circle cx="300" cy="250" r="18" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="300" cy="250" r="175" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <circle cx="300" cy="250" r="130" fill="none" stroke="{INK}" stroke-width="2.5"/>
  {petals}
  {circles}
  <circle cx="300" cy="250" r="8" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
</svg>
</div>
{page_footer(3)}
'''
    return wrap_page(body)


def page_symmetry_gift() -> str:
    left = f'''
  <!-- left half gift -->
  <path d="M300 120 Q240 100 210 130 Q200 150 220 160 L220 180 L300 180 Z" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <rect x="200" y="180" width="100" height="40" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <rect x="190" y="220" width="110" height="160" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <path d="M200 250 Q230 265 260 250 Q280 265 300 250" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="220" cy="270" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="255" cy="275" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="285" cy="270" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <line x1="200" y1="300" x2="300" y2="300" stroke="{INK}" stroke-width="2.5"/>
  <path d="M210 330 Q225 350 240 330 Q255 350 270 330 Q285 350 295 330" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <line x1="300" y1="100" x2="300" y2="400" stroke="{ORANGE}" stroke-width="2.5" stroke-dasharray="8 6"/>
'''
    body = f'''
{header("Finish the Gift Box", "Complete the missing half. Then color it.")}
<div class="stage">
<svg class="main" viewBox="0 0 600 500" xmlns="http://www.w3.org/2000/svg">
  {scatter_decor()}
  {left}
</svg>
</div>
{page_footer(4)}
'''
    return wrap_page(body)


def page_festive_home() -> str:
    house = f'''
  <!-- house -->
  <path d="M120 220 L300 80 L480 220" fill="none" stroke="{INK}" stroke-width="4"/>
  <rect x="140" y="220" width="320" height="200" fill="none" stroke="{INK}" stroke-width="4"/>
  <!-- roof garland -->
  <path d="M130 215 Q180 195 230 215 Q280 195 330 215 Q380 195 430 215 Q460 205 470 215" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="180" cy="205" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="230" cy="212" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="280" cy="205" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="330" cy="212" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="380" cy="205" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="430" cy="212" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <!-- windows -->
  <rect x="175" y="250" width="70" height="55" rx="4" fill="none" stroke="{INK}" stroke-width="3"/>
  <rect x="355" y="250" width="70" height="55" rx="4" fill="none" stroke="{INK}" stroke-width="3"/>
  <line x1="210" y1="250" x2="210" y2="305" stroke="{INK}" stroke-width="2"/>
  <line x1="175" y1="277" x2="245" y2="277" stroke="{INK}" stroke-width="2"/>
  <line x1="390" y1="250" x2="390" y2="305" stroke="{INK}" stroke-width="2"/>
  <line x1="355" y1="277" x2="425" y2="277" stroke="{INK}" stroke-width="2"/>
  <!-- door -->
  <rect x="265" y="310" width="70" height="110" rx="4" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <circle cx="320" cy="370" r="4" fill="{INK}"/>
  <!-- lanterns -->
  <path d="M150 220 L150 250" stroke="{INK}" stroke-width="2"/>
  <polygon points="150,250 130,280 150,310 170,280" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M450 220 L450 250" stroke="{INK}" stroke-width="2"/>
  <polygon points="450,250 430,280 450,310 470,280" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <!-- pots -->
  <path d="M160 400 L150 440 L190 440 L180 400 Z" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="170" cy="395" rx="22" ry="10" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M420 400 L410 440 L450 440 L440 400 Z" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="430" cy="395" rx="22" ry="10" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <!-- rangoli -->
  <circle cx="300" cy="455" r="35" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="300" cy="455" r="15" fill="none" stroke="{INK}" stroke-width="2"/>
  <!-- diyas on steps -->
  <ellipse cx="220" cy="430" rx="18" ry="8" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M220 410 Q225 395 230 410 Q225 418 220 410" fill="none" stroke="{INK}" stroke-width="2"/>
  <ellipse cx="380" cy="430" rx="18" ry="8" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M380 410 Q385 395 390 410 Q385 418 380 410" fill="none" stroke="{INK}" stroke-width="2"/>
  {sparkle(200, 120, 8)}
  {sparkle(400, 110, 8)}
  {confetti(250, 140, 4, PINK)}
  {confetti(360, 130, 4, ORANGE)}
'''
    body = f'''
{header("My Festive Diwali Home", "Color the picture and add your own festive decorations.")}
<div class="stage" style="height:200mm">
  <div class="prompt" style="top:8mm;left:8mm">Add more stars!</div>
  <div class="prompt blue" style="top:8mm;right:8mm;left:auto">Draw some dots!</div>
  <div class="prompt pink" style="bottom:22mm;left:10mm">Add more diyas!</div>
<svg class="main" viewBox="0 0 600 500" xmlns="http://www.w3.org/2000/svg">
  {house}
</svg>
</div>
{page_footer(5)}
'''
    return wrap_page(body)


def page_learn_draw() -> str:
    steps = [
        (1, f'<ellipse cx="90" cy="70" rx="70" ry="28" fill="none" stroke="{INK}" stroke-width="3"/>'),
        (2, f'''<ellipse cx="90" cy="70" rx="70" ry="28" fill="none" stroke="{INK}" stroke-width="3"/>
          <path d="M30 70 Q50 85 70 70 Q90 85 110 70 Q130 85 150 70" fill="none" stroke="{INK}" stroke-width="2.5"/>
          <circle cx="60" cy="88" r="4" fill="none" stroke="{INK}" stroke-width="2"/>
          <circle cx="90" cy="92" r="4" fill="none" stroke="{INK}" stroke-width="2"/>
          <circle cx="120" cy="88" r="4" fill="none" stroke="{INK}" stroke-width="2"/>'''),
        (3, f'''<ellipse cx="90" cy="85" rx="70" ry="28" fill="none" stroke="{INK}" stroke-width="3"/>
          <path d="M30 85 Q50 100 70 85 Q90 100 110 85 Q130 100 150 85" fill="none" stroke="{INK}" stroke-width="2.5"/>
          <path d="M90 20 Q110 50 90 85 Q70 50 90 20" fill="none" stroke="{INK}" stroke-width="3"/>
          <path d="M70 45 L65 35 M110 45 L115 35 M90 28 L90 18" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'''),
        (4, f'''<ellipse cx="90" cy="95" rx="70" ry="28" fill="{RED}" stroke="{INK}" stroke-width="3"/>
          <path d="M30 90 Q90 75 150 90" fill="none" stroke="{YELLOW}" stroke-width="5"/>
          <circle cx="60" cy="100" r="5" fill="{YELLOW}" stroke="{INK}" stroke-width="1.5"/>
          <circle cx="90" cy="105" r="5" fill="{YELLOW}" stroke="{INK}" stroke-width="1.5"/>
          <circle cx="120" cy="100" r="5" fill="{YELLOW}" stroke="{INK}" stroke-width="1.5"/>
          <path d="M75 92 Q82 98 89 92" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M95 92 Q102 98 109 92" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>
          <circle cx="70" cy="102" r="3.5" fill="{PINK}"/>
          <circle cx="110" cy="102" r="3.5" fill="{PINK}"/>
          <path d="M86 108 Q90 112 94 108" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
          <ellipse cx="90" cy="40" rx="22" ry="38" fill="{YELLOW}" stroke="{INK}" stroke-width="2.5"/>
          <ellipse cx="90" cy="48" rx="12" ry="22" fill="{ORANGE}" stroke="{INK}" stroke-width="2"/>
          <ellipse cx="90" cy="55" rx="5" ry="10" fill="{RED}"/>
          {sparkle(50, 30, 7)}
          {sparkle(130, 28, 6)}
          {marigold(40, 70, 10)}
          {marigold(145, 75, 9)}'''),
    ]
    boxes = ""
    for n, svg in steps:
        boxes += f'''<div class="step-box">
  <div class="step-label">Step {n}</div>
  <svg viewBox="0 0 180 140" width="100%" height="100%">{svg}</svg>
</div>'''
    body = f'''
{header("Learn to Draw a Cute Diya", "Follow the steps to draw your own diya.")}
<div class="steps">{boxes}</div>
<div class="practice-box">
  <div class="step-label" style="background:{PINK}">Your turn!</div>
  <svg width="100%" height="100%" viewBox="0 0 500 180">
    {marigold(30, 30, 12)}
    {sparkle(470, 30, 8)}
    {confetti(450, 150, 4, ORANGE)}
    {marigold(470, 150, 11)}
  </svg>
</div>
{page_footer(6)}
'''
    return wrap_page(body)


def page_festival_fun() -> str:
    scene = f'''
  <!-- doorway -->
  <rect x="80" y="80" width="440" height="320" rx="8" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M80 120 Q150 95 220 120 Q290 95 360 120 Q430 95 520 120" fill="none" stroke="{INK}" stroke-width="3"/>
  <!-- toran flowers -->
  {marigold(150, 110, 12)}
  {marigold(250, 105, 11)}
  {marigold(350, 110, 12)}
  {marigold(450, 105, 11)}
  {leaf(200, 115, -20)}
  {leaf(300, 112, 15)}
  {leaf(400, 115, -10)}
  <!-- boy on stool hanging lantern -->
  <rect x="140" y="340" width="50" height="30" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="165" cy="250" r="22" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M145 280 Q165 310 185 280" fill="none" stroke="{INK}" stroke-width="3"/>
  <line x1="165" y1="310" x2="165" y2="340" stroke="{INK}" stroke-width="3"/>
  <line x1="165" y1="290" x2="200" y2="220" stroke="{INK}" stroke-width="3"/>
  <polygon points="210,200 190,230 210,260 230,230" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M210 180 L210 200" stroke="{INK}" stroke-width="2"/>
  <!-- girl with rangoli -->
  <circle cx="400" cy="300" r="22" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M375 330 Q400 360 425 330" fill="none" stroke="{INK}" stroke-width="3"/>
  <ellipse cx="400" cy="390" rx="55" ry="20" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="400" cy="390" r="25" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <!-- diyas around -->
  <ellipse cx="280" cy="400" rx="20" ry="9" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M280 380 Q288 365 296 380 Q288 388 280 380" fill="none" stroke="{INK}" stroke-width="2"/>
  <ellipse cx="480" cy="400" rx="20" ry="9" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M480 380 Q488 365 496 380 Q488 388 480 380" fill="none" stroke="{INK}" stroke-width="2"/>
  <ellipse cx="120" cy="400" rx="20" ry="9" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M120 380 Q128 365 136 380 Q128 388 120 380" fill="none" stroke="{INK}" stroke-width="2"/>
'''
    body = f'''
{header("Festival Fun at Home", "Color the picture.")}
<div class="stage">
<svg class="main" viewBox="0 0 600 480" xmlns="http://www.w3.org/2000/svg">
  {scene}
</svg>
</div>
{page_footer(7)}
'''
    return wrap_page(body)


def page_trace_lanterns() -> str:
    def dashed_lantern(cx, style):
        dash = 'stroke-dasharray="6 5"'
        if style == 1:
            return f'''
  <line x1="{cx}" y1="40" x2="{cx}" y2="100" stroke="{INK}" stroke-width="2.5" {dash}/>
  <ellipse cx="{cx}" cy="160" rx="40" ry="55" fill="none" stroke="{INK}" stroke-width="3" {dash}/>
  <line x1="{cx - 40}" y1="160" x2="{cx + 40}" y2="160" stroke="{INK}" stroke-width="2" {dash}/>
  <line x1="{cx}" y1="105" x2="{cx}" y2="215" stroke="{INK}" stroke-width="2" {dash}/>
  <path d="M{cx} 215 L{cx - 8} 250 M{cx} 215 L{cx} 255 M{cx} 215 L{cx + 8} 250" stroke="{INK}" stroke-width="2.5" {dash} stroke-linecap="round"/>
'''
        if style == 2:
            return f'''
  <line x1="{cx}" y1="40" x2="{cx}" y2="95" stroke="{INK}" stroke-width="2.5" {dash}/>
  <polygon points="{cx},100 {cx - 45},160 {cx},220 {cx + 45},160" fill="none" stroke="{INK}" stroke-width="3" {dash}/>
  <polygon points="{cx},130 {cx - 20},160 {cx},190 {cx + 20},160" fill="none" stroke="{INK}" stroke-width="2" {dash}/>
  <path d="M{cx} 220 L{cx - 8} 255 M{cx} 220 L{cx} 260 M{cx} 220 L{cx + 8} 255" stroke="{INK}" stroke-width="2.5" {dash}/>
'''
        if style == 3:
            return f'''
  <line x1="{cx}" y1="40" x2="{cx}" y2="90" stroke="{INK}" stroke-width="2.5" {dash}/>
  <rect x="{cx - 28}" y="95" width="56" height="100" rx="6" fill="none" stroke="{INK}" stroke-width="3" {dash}/>
  <line x1="{cx - 28}" y1="120" x2="{cx + 28}" y2="120" stroke="{INK}" stroke-width="2" {dash}/>
  <line x1="{cx - 28}" y1="145" x2="{cx + 28}" y2="145" stroke="{INK}" stroke-width="2" {dash}/>
  <line x1="{cx - 28}" y1="170" x2="{cx + 28}" y2="170" stroke="{INK}" stroke-width="2" {dash}/>
  <path d="M{cx} 195 L{cx - 8} 235 M{cx} 195 L{cx} 240 M{cx} 195 L{cx + 8} 235" stroke="{INK}" stroke-width="2.5" {dash}/>
'''
        return f'''
  <line x1="{cx}" y1="40" x2="{cx}" y2="95" stroke="{INK}" stroke-width="2.5" {dash}/>
  <ellipse cx="{cx}" cy="155" rx="38" ry="50" fill="none" stroke="{INK}" stroke-width="3" {dash}/>
  <path d="M{cx - 38} 145 Q{cx - 20} 135 {cx} 145 Q{cx + 20} 155 {cx + 38} 145" fill="none" stroke="{INK}" stroke-width="2.5" {dash}/>
  <path d="M{cx} 205 L{cx - 8} 245 M{cx} 205 L{cx} 250 M{cx} 205 L{cx + 8} 245" stroke="{INK}" stroke-width="2.5" {dash}/>
'''

    body = f'''
{header("Trace the Hanging Lanterns", "Trace the dotted lines. Then color the lanterns.")}
<div class="stage">
<svg class="main" viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg">
  {marigold(50, 80, 14)}
  {marigold(550, 90, 13)}
  {marigold(60, 320, 12)}
  {marigold(540, 300, 14)}
  {sparkle(100, 200, 8)}
  {sparkle(500, 180, 8)}
  {confetti(120, 100, 4, PINK)}
  {confetti(480, 120, 4, ORANGE)}
  {leaf(80, 250, -20)}
  {leaf(520, 240, 25)}
  {dashed_lantern(120, 1)}
  {dashed_lantern(250, 2)}
  {dashed_lantern(380, 3)}
  {dashed_lantern(500, 4)}
</svg>
</div>
{page_footer(8)}
'''
    return wrap_page(body)


def page_color_by_number() -> str:
    diya = f'''
  <!-- lotus petals outer = 5 -->
  <path d="M300 360 Q220 340 200 280 Q260 300 300 320 Z" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M300 360 Q380 340 400 280 Q340 300 300 320 Z" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M220 380 Q180 340 190 290 Q240 320 270 350 Z" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M380 380 Q420 340 410 290 Q360 320 330 350 Z" fill="none" stroke="{INK}" stroke-width="3"/>
  <text x="230" y="330" font-family="Nunito,sans-serif" font-size="18" font-weight="800" fill="{GUIDE}">5</text>
  <text x="360" y="330" font-family="Nunito,sans-serif" font-size="18" font-weight="800" fill="{GUIDE}">5</text>
  <text x="210" y="360" font-family="Nunito,sans-serif" font-size="18" font-weight="800" fill="{GUIDE}">5</text>
  <text x="380" y="360" font-family="Nunito,sans-serif" font-size="18" font-weight="800" fill="{GUIDE}">5</text>
  <!-- upper petals = 4 -->
  <path d="M300 300 Q240 250 250 200 Q290 240 300 260 Z" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M300 300 Q360 250 350 200 Q310 240 300 260 Z" fill="none" stroke="{INK}" stroke-width="3"/>
  <text x="255" y="245" font-family="Nunito,sans-serif" font-size="18" font-weight="800" fill="{GUIDE}">4</text>
  <text x="335" y="245" font-family="Nunito,sans-serif" font-size="18" font-weight="800" fill="{GUIDE}">4</text>
  <!-- bowl = 3 -->
  <ellipse cx="300" cy="200" rx="70" ry="35" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <path d="M240 195 Q270 210 300 195 Q330 210 360 195" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="270" cy="215" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="300" cy="220" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="330" cy="215" r="5" fill="none" stroke="{INK}" stroke-width="2"/>
  <text x="292" y="205" font-family="Nunito,sans-serif" font-size="20" font-weight="800" fill="{GUIDE}">3</text>
  <!-- flame outer 1, inner 2 -->
  <path d="M300 80 Q340 140 300 195 Q260 140 300 80" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <path d="M300 110 Q320 145 300 180 Q280 145 300 110" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <text x="292" y="130" font-family="Nunito,sans-serif" font-size="18" font-weight="800" fill="{GUIDE}">1</text>
  <text x="292" y="160" font-family="Nunito,sans-serif" font-size="16" font-weight="800" fill="{GUIDE}">2</text>
'''
    legend = f'''
<div class="legend">
  <div class="legend-item"><div class="legend-swatch"><span style="background:{YELLOW}"></span></div>1 = Yellow</div>
  <div class="legend-item"><div class="legend-swatch"><span style="background:{ORANGE}"></span></div>2 = Orange</div>
  <div class="legend-item"><div class="legend-swatch"><span style="background:{BROWN}"></span></div>3 = Brown</div>
  <div class="legend-item"><div class="legend-swatch"><span style="background:{PINK}"></span></div>4 = Pink</div>
  <div class="legend-item"><div class="legend-swatch"><span style="background:{GREEN}"></span></div>5 = Green</div>
</div>
'''
    body = f'''
{header("Lotus Diya Color by Number", "Color each part using the matching numbers.", "yellow")}
<div class="stage" style="height:185mm">
<svg class="main" viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg">
  {scatter_decor()}
  {diya}
</svg>
{legend}
</div>
{page_footer(9)}
'''
    return wrap_page(body)


def page_sweet_plate() -> str:
    def plate(scale_group, colored=False):
        if colored:
            return f'''<g transform="{scale_group}">
  <ellipse cx="200" cy="120" rx="150" ry="70" fill="{YELLOW}" stroke="{INK}" stroke-width="3"/>
  <ellipse cx="200" cy="120" rx="130" ry="55" fill="#FFE082" stroke="{INK}" stroke-width="2"/>
  <circle cx="80" cy="120" r="5" fill="{RED}"/>
  <circle cx="320" cy="120" r="5" fill="{RED}"/>
  <circle cx="200" cy="60" r="5" fill="{RED}"/>
  <circle cx="200" cy="180" r="5" fill="{RED}"/>
  <!-- laddoos -->
  <circle cx="150" cy="115" r="28" fill="{ORANGE}" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="200" cy="100" r="28" fill="{ORANGE}" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="250" cy="115" r="28" fill="{ORANGE}" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="145" cy="108" r="2" fill="#fff"/><circle cx="155" cy="118" r="2" fill="#fff"/>
  <circle cx="195" cy="95" r="2" fill="#fff"/><circle cx="208" cy="105" r="2" fill="#fff"/>
  <circle cx="245" cy="108" r="2" fill="#fff"/><circle cx="255" cy="118" r="2" fill="#fff"/>
  {leaf(120, 95, -40)}
  {leaf(280, 95, 40)}
  <!-- diya -->
  <ellipse cx="200" cy="145" rx="35" ry="14" fill="{RED}" stroke="{INK}" stroke-width="2"/>
  <path d="M175 142 Q200 132 225 142" fill="none" stroke="{YELLOW}" stroke-width="3"/>
  <path d="M200 115 Q215 130 200 145 Q185 130 200 115" fill="{YELLOW}" stroke="{INK}" stroke-width="2"/>
  <path d="M200 125 Q208 135 200 142 Q192 135 200 125" fill="{ORANGE}"/>
</g>'''
        return f'''<g transform="{scale_group}">
  <ellipse cx="200" cy="140" rx="170" ry="85" fill="none" stroke="{INK}" stroke-width="4"/>
  <ellipse cx="200" cy="140" rx="145" ry="65" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="55" cy="140" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="345" cy="140" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="200" cy="65" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="200" cy="215" r="6" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="140" cy="130" r="32" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="200" cy="110" r="32" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="260" cy="130" r="32" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="135" cy="122" r="2.5" fill="{INK}"/><circle cx="148" cy="135" r="2.5" fill="{INK}"/>
  <circle cx="195" cy="105" r="2.5" fill="{INK}"/><circle cx="210" cy="118" r="2.5" fill="{INK}"/>
  <circle cx="255" cy="122" r="2.5" fill="{INK}"/><circle cx="268" cy="135" r="2.5" fill="{INK}"/>
  <ellipse cx="115" cy="100" rx="12" ry="22" fill="none" stroke="{INK}" stroke-width="2.5" transform="rotate(-40 115 100)"/>
  <ellipse cx="285" cy="100" rx="12" ry="22" fill="none" stroke="{INK}" stroke-width="2.5" transform="rotate(40 285 100)"/>
  <ellipse cx="200" cy="165" rx="40" ry="16" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M170 160 Q200 148 230 160" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M200 128 Q218 148 200 165 Q182 148 200 128" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>'''

    body = f'''
{header("Color the Sweet Plate as Shown", "Look at the small picture. Color the big picture to match.")}
<div class="stage">
<svg class="main" viewBox="0 0 600 520" xmlns="http://www.w3.org/2000/svg">
  {marigold(40, 40, 12)}
  {sparkle(560, 40, 8)}
  {confetti(80, 200, 4, PINK)}
  {confetti(520, 180, 4, ORANGE)}
  {marigold(50, 480, 12)}
  {marigold(550, 470, 11)}
  {plate("translate(100,10) scale(0.7)", colored=True)}
  {plate("translate(100,230)", colored=False)}
</svg>
</div>
{page_footer(10)}
'''
    return wrap_page(body)


def page_count_diyas() -> str:
    diyas = ""
    positions = [(100, 160), (220, 140), (340, 165), (460, 145), (160, 280), (300, 300), (440, 275)]
    for i, (x, y) in enumerate(positions):
        diyas += f'''
  <ellipse cx="{x}" cy="{y}" rx="32" ry="14" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M{x} {y - 45} Q{x + 18} {y - 20} {x} {y} Q{x - 18} {y - 20} {x} {y - 45}" fill="none" stroke="{INK}" stroke-width="2.5"/>
'''
    body = f'''
{header("Count the Glowing Diyas", "Count the diyas. Write the number in the box. Then color them!")}
<div class="stage">
<svg class="main" viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg">
  {scatter_decor()}
  {diyas}
  <rect x="220" y="360" width="160" height="50" rx="10" fill="none" stroke="{ORANGE}" stroke-width="3"/>
  <text x="300" y="392" text-anchor="middle" font-family="Nunito,sans-serif" font-size="18" font-weight="700" fill="#2F5A9A">I count ____ diyas</text>
</svg>
</div>
{page_footer(11)}
'''
    return wrap_page(body)


def page_maze() -> str:
    body = f'''
{header("Maze to the Diwali Party", "Help the child find the way to the glowing diya.")}
<div class="stage">
<svg class="main" viewBox="0 0 600 480" xmlns="http://www.w3.org/2000/svg">
  {marigold(40, 40, 12)}
  {marigold(560, 40, 12)}
  {sparkle(300, 30, 8)}
  <!-- start child -->
  <circle cx="70" cy="80" r="18" fill="#FFD7A8" stroke="{INK}" stroke-width="2.5"/>
  <path d="M55 105 Q70 125 85 105" fill="#6EC6FF" stroke="{INK}" stroke-width="2.5"/>
  <text x="70" y="145" text-anchor="middle" font-family="Nunito,sans-serif" font-size="12" font-weight="800" fill="#2F5A9A">START</text>
  <!-- maze walls -->
  <rect x="40" y="160" width="520" height="260" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M40 220 H180 V280 H100 V360 H220 V300 H300 V220 H400 V300 H480 V220 H560
           M120 160 V220 M260 160 V200 M340 160 V240 M460 160 V200
           M180 360 V420 M300 340 V420 M420 360 V420 M520 300 V360"
        fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="square"/>
  <!-- goal diya -->
  <ellipse cx="520" cy="390" rx="28" ry="12" fill="{RED}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M520 350 Q535 370 520 390 Q505 370 520 350" fill="{YELLOW}" stroke="{INK}" stroke-width="2"/>
  <text x="520" y="430" text-anchor="middle" font-family="Nunito,sans-serif" font-size="12" font-weight="800" fill="#2F5A9A">PARTY!</text>
</svg>
</div>
{page_footer(12)}
'''
    return wrap_page(body)


def page_certificate() -> str:
    body = f'''
<div style="text-align:center;padding-top:20mm">
  {logo(140)}
  <h1 class="title" style="margin:10mm auto 4mm;font-size:34px;max-width:none">You Did It!</h1>
  <p class="instruction" style="max-width:none;margin:0 auto">Certificate of Creative Celebration</p>
  <hr class="rule" style="width:60%;margin:8mm auto"/>
  <svg viewBox="0 0 500 280" width="160mm" style="margin:4mm auto;display:block">
    {marigold(40, 40, 16)}
    {marigold(460, 40, 16)}
    {sparkle(250, 30, 12)}
    <rect x="60" y="70" width="380" height="160" rx="16" fill="none" stroke="{ORANGE}" stroke-width="4"/>
    <text x="250" y="120" text-anchor="middle" font-family="Nunito,sans-serif" font-size="16" fill="#2F5A9A">This certifies that</text>
    <line x1="120" y1="160" x2="380" y2="160" stroke="{INK}" stroke-width="2"/>
    <text x="250" y="155" text-anchor="middle" font-family="Nunito,sans-serif" font-size="14" fill="{GUIDE}">Name</text>
    <text x="250" y="200" text-anchor="middle" font-family="Nunito,sans-serif" font-size="15" fill="#1B3A6B" font-weight="700">completed My First Diwali Art Adventure!</text>
    {confetti(100, 90, 4, PINK)}
    {confetti(400, 90, 4, ORANGE)}
  </svg>
  <p style="margin-top:8mm;font-weight:700;color:#1B3A6B">Happy Diwali from Pehla Page</p>
</div>
{page_footer(13)}
'''
    return wrap_page(body)


def build_html() -> str:
    pages = [
        cover_page(),
        page_join_dots(),
        page_copy_kandil(),
        page_dot_rangoli(),
        page_symmetry_gift(),
        page_festive_home(),
        page_learn_draw(),
        page_festival_fun(),
        page_trace_lanterns(),
        page_color_by_number(),
        page_sweet_plate(),
        page_count_diyas(),
        page_maze(),
        page_certificate(),
    ]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>My First Diwali Art Adventure — Pehla Page</title>
  <link rel="stylesheet" href="assets/book.css"/>
</head>
<body>
{"".join(pages)}
</body>
</html>
'''


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    if pdf_path.exists():
        pdf_path.unlink()
    url = html_path.resolve().as_uri()
    cmd = [
        "google-chrome",
        "--headless=new",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        "--no-margins",
        "--virtual-time-budget=8000",
        "--run-all-compositor-stages-before-draw",
        url,
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Chrome sometimes hangs after writing the PDF; wait for file then stop.
    import time

    deadline = time.time() + 45
    while time.time() < deadline:
        if pdf_path.exists() and pdf_path.stat().st_size > 50_000:
            time.sleep(1.5)
            proc.kill()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
            print(f"Wrote {pdf_path} ({pdf_path.stat().st_size // 1024} KB)")
            return
        if proc.poll() is not None:
            break
        time.sleep(0.4)
    stdout, stderr = proc.communicate(timeout=10)
    if not pdf_path.exists():
        raise RuntimeError(f"PDF not created.\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}")
    print(f"Wrote {pdf_path} ({pdf_path.stat().st_size // 1024} KB)")


def main() -> None:
    html = build_html()
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT_HTML}")
    # also write individual preview pages list
    PAGES_DIR.mkdir(exist_ok=True)
    render_pdf(OUT_HTML, OUT_PDF)


if __name__ == "__main__":
    main()
