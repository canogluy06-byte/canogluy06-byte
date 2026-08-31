# -*- coding: utf-8 -*-
"""
GitHub profil varliklari uretici.

Tek kaynak -> iki tema (koyu/acik). Dis font/servis/istek YOK.

DAYANIKLILIK KURALI: hicbir icerigin GORUNURLUGU animasyona bagli degildir.
Taban durum = nihai durum. Animasyonlar CSS ile ve `animation-fill-mode: both`
kullanilarak eklenir; animasyon calismazsa (reduced-motion, eski render,
statik onizleme) her sey tam ve dogru gorunur.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

DARK = dict(
    bg0="#06080D", bg1="#0A0E16", bg2="#0E131D", rule="#1C2434",
    txt0="#EDF1F7", txt1="#9AA8BC", txt2="#6C7A8E",
    vio="#7C5CFF", amb="#F5A524", grn="#2FD97B",
    gridOp="0.055", glowVio="0.16", glowAmb="0.09", stroke="#1C2434", dotEmpty="#232C3D",
)
LIGHT = dict(
    bg0="#FFFFFF", bg1="#F7F9FC", bg2="#EDF1F7", rule="#DBE2EC",
    txt0="#0A0F1A", txt1="#46536580".replace("80",""), txt2="#66748A",
    vio="#5B3BE0", amb="#B87400", grn="#0E9F6E",
    gridOp="0.05", glowVio="0.07", glowAmb="0.05", stroke="#DBE2EC", dotEmpty="#CFD8E4",
)

SANS = "Segoe UI, -apple-system, BlinkMacSystemFont, Helvetica Neue, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, Menlo, monospace"

# Ortak CSS.
#
# `animation-fill-mode: both` KULLANILMAZ: gecikme suresince ogeyi `from`
# durumunda (opacity 0) tutar, animasyon hic ilerlemezse icerik kalici olarak
# gorunmez kalir. Bunun yerine `forwards` kullanilir -- gecikme boyunca ogenin
# normal (gorunur) stili gecerlidir. Boylece animasyon calismasa da her sey
# eksiksiz gorunur; animasyon yalnizca hareket katar.
CSS = """
    .rev  { animation: rev .5s cubic-bezier(.2,.7,.3,1) forwards; }
    .draw { animation: draw 1.2s cubic-bezier(.2,.7,.2,1) forwards .2s; }
    .blink{ animation: blink 2.4s ease-in-out infinite; }
    .sweep{ animation: sweep 11s linear infinite; }
    @keyframes rev   { from { opacity:.001; transform:translateY(7px) }
                       to   { opacity:1;    transform:none } }
    @keyframes draw  { from { width:0 } to { width:var(--w) } }
    @keyframes blink { 0%,100% { opacity:1 } 50% { opacity:.25 } }
    @keyframes sweep { from { transform:translateX(-520px) } to { transform:translateX(1200px) } }
    @media (prefers-reduced-motion: reduce) {
      .rev,.draw,.blink,.sweep { animation: none }
    }
"""


def defs(t):
    return f'''
    <style>{CSS}</style>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['vio']}"/><stop offset="55%" stop-color="{t['vio']}"/>
      <stop offset="100%" stop-color="{t['amb']}"/>
    </linearGradient>
    <linearGradient id="sw" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['vio']}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{t['vio']}" stop-opacity="0.26"/>
      <stop offset="100%" stop-color="{t['vio']}" stop-opacity="0"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{t['vio']}" stroke-opacity="{t['gridOp']}" stroke-width="1"/>
    </pattern>
    <linearGradient id="gf" x1="0" y1="0" x2="1" y2="0.35">
      <stop offset="0%" stop-color="#fff" stop-opacity="0.9"/>
      <stop offset="62%" stop-color="#fff" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="gm"><rect width="100%" height="100%" fill="url(#gf)"/></mask>
    <radialGradient id="gV"><stop offset="0%" stop-color="{t['vio']}" stop-opacity="{t['glowVio']}"/>
      <stop offset="100%" stop-color="{t['vio']}" stop-opacity="0"/></radialGradient>
    <radialGradient id="gA"><stop offset="0%" stop-color="{t['amb']}" stop-opacity="{t['glowAmb']}"/>
      <stop offset="100%" stop-color="{t['amb']}" stop-opacity="0"/></radialGradient>'''


# ═════════════════════════════════ HERO ═════════════════════════════════
def hero(t):
    W, H = 1200, 330
    METRICS = [("ÜRETİMDEKİ SİSTEM", "9"), ("GÜNLÜK İSTEMCİ", "~10"), ("REST UÇ NOKTASI", "20")]
    rows = ""
    for i, (lab, val) in enumerate(METRICS):
        y = 84 + i * 42
        rows += f'''
      <g class="rev" style="animation-delay:{0.5 + i*0.1:.2f}s">
        <text x="22" y="{y}" font-family="{SANS}" font-size="11" fill="{t['txt2']}" letter-spacing="1.4">{lab}</text>
        <text x="242" y="{y + 1}" font-family="{MONO}" font-size="19" font-weight="600"
              fill="{t['txt0']}" text-anchor="end">{val}</text>
        <line x1="22" y1="{y + 14}" x2="242" y2="{y + 14}" stroke="{t['rule']}" stroke-width="1"/>
      </g>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     role="img" aria-label="Yunus Emre Canoğlu — Kurumsal iş yazılımı, backend ve masaüstü sistemleri">
  <defs>{defs(t)}<clipPath id="fr"><rect width="{W}" height="{H}" rx="12"/></clipPath></defs>
  <g clip-path="url(#fr)">
    <rect width="{W}" height="{H}" fill="{t['bg0']}"/>
    <rect width="{W}" height="{H}" fill="url(#grid)" mask="url(#gm)"/>
    <ellipse cx="110" cy="20" rx="520" ry="330" fill="url(#gV)"/>
    <ellipse cx="1130" cy="330" rx="430" ry="270" fill="url(#gA)"/>
    <rect class="sweep" x="0" y="0" width="520" height="{H}" fill="url(#sw)"/>
    <rect x="0" y="0" width="{W}" height="2.5" fill="url(#edge)"/>

    <text class="rev" x="76" y="74" font-family="{MONO}" font-size="11.5" fill="{t['txt2']}"
          letter-spacing="3.4">YAZILIM MÜHENDİSLİĞİ &#160;·&#160; ANKARA, TÜRKİYE</text>

    <text class="rev" style="animation-delay:.08s" x="74" y="144" font-family="{SANS}"
          font-size="52" font-weight="700" fill="{t['txt0']}" letter-spacing="-0.3">YUNUS EMRE CANOĞLU</text>

    <rect class="draw" style="--w:286px" x="76" y="164" width="286" height="2.5" rx="1.25" fill="url(#edge)"/>

    <text class="rev" style="animation-delay:.16s" x="76" y="204" font-family="{SANS}" font-size="18"
          font-weight="600" fill="{t['txt1']}" letter-spacing="1.6">Kurumsal iş yazılımı &#160;·&#160; Backend, masaüstü ve saha sistemleri</text>

    <text class="rev" style="animation-delay:.24s" x="76" y="248" font-family="{MONO}" font-size="14" letter-spacing="0.3">
      <tspan fill="{t['vio']}">.NET 10</tspan><tspan fill="{t['txt2']}">  /  </tspan><tspan
       fill="{t['txt1']}">Clean Architecture</tspan><tspan fill="{t['txt2']}">  /  </tspan><tspan
       fill="{t['amb']}">PostgreSQL</tspan><tspan fill="{t['txt2']}">  /  </tspan><tspan
       fill="{t['txt1']}">PHP 8</tspan><tspan fill="{t['txt2']}">  /  </tspan><tspan fill="{t['vio']}">Unity</tspan>
    </text>

    <g transform="translate(76,286)"><g class="rev" style="animation-delay:.32s">
      <circle class="blink" cx="5" cy="-4" r="4.5" fill="{t['grn']}"/>
      <text x="20" y="0" font-family="{MONO}" font-size="12" fill="{t['txt2']}" letter-spacing="1.5">
        SAHADA ÇALIŞAN SİSTEMLER &#160;—&#160; PROTOTİP DEĞİL</text>
    </g></g>

    <g transform="translate(872,60)"><g class="rev" style="animation-delay:.4s">
      <rect x="0" y="0" width="264" height="212" rx="10" fill="{t['bg1']}" stroke="{t['stroke']}" stroke-width="1"/>
      <rect x="0" y="0" width="264" height="2" rx="1" fill="url(#edge)" opacity="0.9"/>
      <text x="22" y="38" font-family="{MONO}" font-size="10.5" fill="{t['txt2']}" letter-spacing="2.4">ÖLÇÜMLER</text>
      <line x1="22" y1="52" x2="242" y2="52" stroke="{t['rule']}" stroke-width="1"/>
      {rows}
    </g></g>

    <rect x="0" y="{H-2}" width="{W}" height="2" fill="url(#edge)" opacity="0.45"/>
  </g>
</svg>
'''


# ═══════════════════════════ YETKİNLİK MATRİSİ ═══════════════════════════
CAPS = [
    ("Backend &amp; REST API",          [1, 1, 0, 1, 0, 0]),
    ("Katmanlı mimari (Clean Arch.)",   [1, 0, 1, 0, 0, 0]),
    ("Kimlik doğrulama &amp; yetki",    [1, 1, 0, 1, 0, 0]),
    ("İlişkisel veri &amp; şema",       [1, 1, 1, 0, 0, 0]),
    ("Masaüstü arayüz (custom paint)",  [1, 0, 1, 0, 0, 1]),
    ("Web frontend",                    [1, 1, 0, 1, 0, 0]),
    ("PWA / mobil paketleme",           [1, 1, 0, 0, 0, 0]),
    ("Dosya tabanlı depolama",          [0, 0, 0, 1, 1, 1]),
    ("Dağıtım &amp; operasyon",         [1, 1, 1, 1, 0, 0]),
]
SYSTEMS_H = ["ERP", "CİVARİ", "FİNANS", "BLOG", "UNITY", "STOK"]


def matrix(t):
    W, top, rowH, colX0, gap = 1200, 108, 40, 700, 80
    H = top + len(CAPS) * rowH + 46

    head = "".join(
        f'<text x="{colX0+i*gap}" y="{top-26}" '
        f'font-family="{MONO}" font-size="10.5" fill="{t["txt2"]}" letter-spacing="1.3" '
        f'text-anchor="middle">{s}</text>' for i, s in enumerate(SYSTEMS_H))

    body = ""
    for r, (lab, marks) in enumerate(CAPS):
        y, cy = top + r * rowH, top + r * rowH + rowH / 2
        if r % 2 == 0:
            body += f'<rect x="40" y="{y}" width="{W-80}" height="{rowH}" fill="{t["bg1"]}" opacity="0.55"/>'
        body += (f'<text x="64" y="{cy+5}" '
                 f'font-family="{SANS}" font-size="14.5" fill="{t["txt1"]}">{lab}</text>')
        for i, m in enumerate(marks):
            x = colX0 + i * gap
            if m:
                body += (f'<circle cx="{x}" cy="{cy}" r="11" fill="none" stroke="{t["vio"]}" '
                         f'stroke-width="1" opacity="0.2"/>'
                         f'<circle cx="{x}" cy="{cy}" r="6" fill="{t["vio"]}"/>')
            else:
                body += f'<circle cx="{x}" cy="{cy}" r="3" fill="none" stroke="{t["dotEmpty"]}" stroke-width="1.4"/>'
        body += (f'<line x1="40" y1="{y+rowH}" x2="{W-40}" y2="{y+rowH}" stroke="{t["rule"]}" '
                 f'stroke-width="1" opacity="0.5"/>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     role="img" aria-label="Yetkinlik ve sistem matrisi">
  <defs>{defs(t)}<clipPath id="fr"><rect width="{W}" height="{H}" rx="12"/></clipPath></defs>
  <g clip-path="url(#fr)">
    <rect width="{W}" height="{H}" fill="{t['bg0']}"/>
    <rect width="{W}" height="{H}" fill="url(#grid)" mask="url(#gm)"/>
    <rect x="0" y="0" width="{W}" height="2.5" fill="url(#edge)"/>
    <text class="rev" x="64" y="54" font-family="{SANS}" font-size="19" font-weight="700" fill="{t['txt0']}">Yetkinlik × Sistem</text>
    <text class="rev" style="animation-delay:.06s" x="64" y="78" font-family="{MONO}" font-size="11"
          fill="{t['txt2']}" letter-spacing="1.1">DOLU DAİRE = O SİSTEMDE FİİLEN UYGULANDI</text>
    {head}
    <line x1="40" y1="{top-14}" x2="{W-40}" y2="{top-14}" stroke="{t['rule']}" stroke-width="1"/>
    {body}
  </g>
</svg>
'''


# ═════════════════════════════ SİSTEM MİMARİSİ ═════════════════════════════
def systems(t):
    W, H = 1200, 500

    def box(x, y, w, h, title, sub, accent, delay, dashed=False):
        dash = ' stroke-dasharray="4 3"' if dashed else ''
        ty = y + (26 if sub else h / 2 + 5)
        s = (f'<g>'
             f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{t["bg1"]}" '
             f'stroke="{accent}" stroke-width="1.2"{dash}/>'
             f'<text x="{x+w/2}" y="{ty}" font-family="{SANS}" font-size="14.5" font-weight="600" '
             f'fill="{t["txt0"]}" text-anchor="middle">{title}</text>')
        if sub:
            s += (f'<text x="{x+w/2}" y="{y+45}" font-family="{MONO}" font-size="10.5" '
                  f'fill="{t["txt2"]}" text-anchor="middle">{sub}</text>')
        return s + '</g>'

    def arr(x1, y1, x2, y2, delay, dashed=False):
        dash = ' stroke-dasharray="5 4"' if dashed else ''
        return (f'<path d="M{x1} {y1} L{x2} {y2}" '
                f'stroke="{t["vio"]}" stroke-width="1.4" fill="none" opacity="0.5" '
                f'marker-end="url(#ah)"{dash}/>')

    clients = [("WinForms", "masaüstü", 244), ("PWA", "mobil", 500), ("Tarayıcı", "web", 756)]
    parts = "".join(box(x, 112, 200, 64, n, s, t["amb"], 0.15 + i * 0.1)
                    for i, (n, s, x) in enumerate(clients))
    parts += "".join(arr(x + 100, 176, 600, 226, 0.45 + i * 0.08)
                     for i, (_, _, x) in enumerate(clients))

    layers = [("ASP.NET Core API", "20 REST controller", 232, t["vio"]),
              ("Application", "DTO · use-case sözleşmeleri", 312, t["stroke"]),
              ("Domain", "20 entity · sıfır bağımlılık", 392, t["vio"])]
    parts += "".join(box(360, y, 480, 52, n, s, a, 0.7 + i * 0.12)
                     for i, (n, s, y, a) in enumerate(layers))
    parts += arr(600, 284, 600, 310, 0.85) + arr(600, 364, 600, 390, 0.95)
    parts += box(898, 312, 212, 52, "Infrastructure", "EF Core · JWT · BCrypt", t["stroke"], 1.05, True)
    parts += arr(896, 338, 844, 338, 1.15, True)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     role="img" aria-label="Sistem mimarisi: tek API, üç istemci">
  <defs>{defs(t)}
    <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="{t['vio']}" opacity="0.6"/>
    </marker>
    <clipPath id="fr"><rect width="{W}" height="{H}" rx="12"/></clipPath>
  </defs>
  <g clip-path="url(#fr)">
    <rect width="{W}" height="{H}" fill="{t['bg0']}"/>
    <rect width="{W}" height="{H}" fill="url(#grid)" mask="url(#gm)"/>
    <ellipse cx="600" cy="500" rx="620" ry="230" fill="url(#gV)"/>
    <rect x="0" y="0" width="{W}" height="2.5" fill="url(#edge)"/>

    <text class="rev" x="64" y="54" font-family="{SANS}" font-size="19" font-weight="700" fill="{t['txt0']}">Tek API, üç istemci</text>
    <text class="rev" style="animation-delay:.06s" x="64" y="78" font-family="{MONO}" font-size="11"
          fill="{t['txt2']}" letter-spacing="1.1">BAĞIMLILIKLAR İÇERİ DOĞRU AKAR — İŞ KURALI TEK YERDE DURUR</text>

    <text x="64" y="150" font-family="{MONO}" font-size="10.5" fill="{t['txt2']}" letter-spacing="2">İSTEMCİ</text>
    <text x="64" y="264" font-family="{MONO}" font-size="10.5" fill="{t['txt2']}" letter-spacing="2">SUNUCU</text>
    {parts}
    {arr(600, 444, 600, 466, 1.2)}
    <text x="600" y="486" font-family="{MONO}" font-size="11.5"
          fill="{t['amb']}" text-anchor="middle" letter-spacing="1.6">PostgreSQL</text>
  </g>
</svg>
'''


if __name__ == "__main__":
    for name, fn in (("hero", hero), ("matrix", matrix), ("systems", systems)):
        for sfx, tok in (("dark", DARK), ("light", LIGHT)):
            p = os.path.join(OUT, f"profile-{name}-{sfx}.svg")
            open(p, "w", encoding="utf-8", newline="\n").write(fn(tok))
            print(f"  profile-{name}-{sfx}.svg  {os.path.getsize(p)//1024} KB")
    print("\n6 varlik uretildi — taban durum gorunur, animasyon yalnizca ekler")
