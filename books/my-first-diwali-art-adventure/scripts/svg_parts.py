"""Reusable SVG motifs for the Diwali kids activity book."""

NAVY = "#1B3A6B"
ORANGE = "#F28C28"
YELLOW = "#F5C518"
PINK = "#F07AB0"
GREEN = "#4CAF50"
RED = "#E53935"
BROWN = "#8D6E63"
INK = "#1A1A1A"
GUIDE = "#BDBDBD"
GOLD = "#E8B923"


def logo(width=120):
    h = int(width * 0.85)
    return f'''<svg class="logo" width="{width}" height="{h}" viewBox="0 0 160 130" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lgBook" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FF6B9D"/>
      <stop offset="50%" stop-color="#FFB347"/>
      <stop offset="100%" stop-color="#6EC6FF"/>
    </linearGradient>
  </defs>
  <circle cx="28" cy="22" r="5" fill="{YELLOW}"/>
  <circle cx="132" cy="18" r="4" fill="{PINK}"/>
  <path d="M20 70 Q20 40 50 40 L110 40 Q140 40 140 70 L140 95 Q140 105 80 105 Q20 105 20 95 Z" fill="url(#lgBook)" stroke="{INK}" stroke-width="3"/>
  <path d="M80 40 L80 105" stroke="{INK}" stroke-width="2.5"/>
  <!-- kids peeking -->
  <circle cx="58" cy="48" r="14" fill="#FFD7A8" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="102" cy="48" r="14" fill="#FFD7A8" stroke="{INK}" stroke-width="2.5"/>
  <path d="M48 42 Q58 34 68 42" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M92 42 Q102 34 112 42" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M52 50 Q55 53 58 50" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
  <path d="M96 50 Q99 53 102 50" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
  <circle cx="63" cy="54" r="2.2" fill="{PINK}"/>
  <circle cx="97" cy="54" r="2.2" fill="{PINK}"/>
  <path d="M54 58 Q58 62 62 58" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round"/>
  <path d="M98 58 Q102 62 106 58" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round"/>
  <!-- crayons -->
  <rect x="12" y="78" width="8" height="28" rx="2" fill="{RED}" stroke="{INK}" stroke-width="1.5" transform="rotate(-18 16 92)"/>
  <rect x="140" y="76" width="8" height="28" rx="2" fill="{GREEN}" stroke="{INK}" stroke-width="1.5" transform="rotate(16 144 90)"/>
  <rect x="28" y="100" width="8" height="24" rx="2" fill="{YELLOW}" stroke="{INK}" stroke-width="1.5" transform="rotate(-8 32 112)"/>
  <text x="80" y="124" text-anchor="middle" font-family="Nunito, sans-serif" font-size="18" font-weight="800">
    <tspan fill="#FF6B9D">P</tspan><tspan fill="#FFB347">e</tspan><tspan fill="#6EC6FF">h</tspan><tspan fill="#7ED957">l</tspan><tspan fill="#FF6B9D">a</tspan>
    <tspan fill="#FFB347"> </tspan>
    <tspan fill="#6EC6FF">P</tspan><tspan fill="#FF6B9D">a</tspan><tspan fill="#FFB347">g</tspan><tspan fill="#7ED957">e</tspan>
  </text>
</svg>'''


def marigold(cx, cy, r=18, fill=ORANGE):
    petals = ""
    for i in range(10):
        a = i * 36
        petals += f'<ellipse cx="{cx}" cy="{cy - r * 0.55}" rx="{r * 0.28}" ry="{r * 0.55}" fill="{fill}" stroke="{INK}" stroke-width="1.5" transform="rotate({a} {cx} {cy})"/>'
    return f'''<g>
  {petals}
  <circle cx="{cx}" cy="{cy}" r="{r * 0.35}" fill="{YELLOW}" stroke="{INK}" stroke-width="1.5"/>
</g>'''


def sparkle(cx, cy, s=10, fill=YELLOW):
    return f'''<path d="M{cx} {cy - s} L{cx + s * 0.22} {cy - s * 0.22} L{cx + s} {cy} L{cx + s * 0.22} {cy + s * 0.22} L{cx} {cy + s} L{cx - s * 0.22} {cy + s * 0.22} L{cx - s} {cy} L{cx - s * 0.22} {cy - s * 0.22} Z" fill="{fill}" stroke="{INK}" stroke-width="1"/>'''


def confetti(cx, cy, r=4, fill=PINK):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'


def leaf(cx, cy, rot=0, fill=GREEN):
    return f'''<g transform="rotate({rot} {cx} {cy})">
  <ellipse cx="{cx}" cy="{cy}" rx="8" ry="16" fill="{fill}" stroke="{INK}" stroke-width="1.8"/>
  <path d="M{cx} {cy - 12} L{cx} {cy + 12}" stroke="{INK}" stroke-width="1.2"/>
</g>'''


def footer_deco():
    return f'''
  {sparkle(0, 0, 7)}
  {confetti(18, 0, 3.5, ORANGE)}
'''


def page_footer(n):
    return f'''<div class="footer">
  <svg class="foot-deco" viewBox="-12 -12 24 24">{sparkle(0, 0, 8)}</svg>
  <svg class="foot-deco" viewBox="-6 -6 12 12">{confetti(0, 0, 4, ORANGE)}</svg>
  <div class="page-num">{n}</div>
  <svg class="foot-deco" viewBox="-6 -6 12 12">{confetti(0, 0, 4, YELLOW)}</svg>
  <svg class="foot-deco" viewBox="-12 -12 24 24">{sparkle(0, 0, 8)}</svg>
</div>'''


def header(title, instruction, rule_class=""):
    return f'''<div class="header">
  <div>
    <div class="series">My First Diwali Art Adventure</div>
    <h1 class="title">{title}</h1>
    <p class="instruction">{instruction}</p>
  </div>
  {logo(118)}
</div>
<hr class="rule {rule_class}"/>'''


def scatter_decor(extra=""):
    """Common festive scatter for activity pages."""
    bits = [
        marigold(60, 80, 16),
        marigold(520, 90, 14),
        marigold(70, 420, 15),
        marigold(510, 400, 16),
        sparkle(140, 60, 9),
        sparkle(460, 70, 8),
        sparkle(120, 460, 8),
        sparkle(480, 450, 9),
        confetti(180, 50, 4, PINK),
        confetti(400, 55, 4, ORANGE),
        confetti(90, 200, 3.5, PINK),
        confetti(500, 220, 3.5, ORANGE),
        confetti(150, 380, 4, ORANGE),
        confetti(430, 390, 4, PINK),
        leaf(100, 140, -25),
        leaf(490, 150, 30),
    ]
    return "\n".join(bits) + extra
