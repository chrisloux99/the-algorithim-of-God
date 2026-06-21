import os
import re

book_dir = r"C:\Users\RAKICT\Documents\The_Algorithm_of_Belief"

chapter_files = sorted([f for f in os.listdir(book_dir) if f.startswith("Chapter_") and f.endswith(".md")])

chapters_content = []
for cf in chapter_files:
    with open(os.path.join(book_dir, cf), 'r', encoding='utf-8') as f:
        chapters_content.append(f.read())

def md_to_html(md):
    html = md
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'^---+$', r'<hr>', html, flags=re.MULTILINE)
    
    lines = html.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            result.append('')
            continue
        if stripped.startswith('<h1') or stripped.startswith('<h2') or stripped.startswith('<h3') or stripped.startswith('<hr') or stripped.startswith('<p>'):
            result.append(stripped)
        elif stripped.startswith('<sup>'):
            result.append(stripped)
        elif stripped.startswith('<strong>') or stripped.startswith('<em>'):
            result.append(f'<p>{stripped}</p>')
        elif stripped.startswith('<'):
            result.append(stripped)
        else:
            result.append(f'<p>{stripped}</p>')
    return '\n'.join(result)

full_html = '\n\n'.join([md_to_html(ch) for ch in chapters_content])

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Algorithm of Belief — Finding God in Innovation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Cinzel:wght@400;500;600;700;800;900&family=Cinzel+Decorative:wght@400;700;900&display=swap" rel="stylesheet">
<style>
  :root {{
    --ink: #1c1914;
    --ink-light: #3d3630;
    --ink-muted: #6b5f54;
    --paper: #faf7f2;
    --paper-dark: #f0ebe2;
    --cream: #f5f0e6;
    --red-dark: #5c0a0a;
    --red: #7a1212;
    --red-light: #9e2020;
    --gold: #8b7355;
    --gold-light: #b09a78;
    --rule: #c4b8a8;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  html {{
    font-size: 18px;
    scroll-behavior: smooth;
  }}

  body {{
    background: #0d0a08;
    font-family: 'EB Garamond', 'Georgia', 'Times New Roman', serif;
    color: var(--ink);
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }}

  /* ==================== COVER ==================== */
  .cover {{
    width: 100%;
    min-height: 100vh;
    background: radial-gradient(ellipse at 50% 40%, #1a0c0c 0%, #0d0505 50%, #060202 80%, #000 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    overflow: hidden;
    page-break-after: always;
  }}

  .cover::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 45%, rgba(120,15,15,0.08) 0%, transparent 60%);
    z-index: 1;
  }}

  .cover-inner {{
    position: relative;
    z-index: 5;
    text-align: center;
    padding: 60px 40px;
  }}

  /* Cross */
  .cross-wrap {{
    position: relative;
    width: 160px;
    height: 260px;
    margin: 0 auto 50px;
  }}

  .cross-v {{
    position: absolute;
    left: 50%;
    top: 0;
    width: 6px;
    height: 100%;
    transform: translateX(-50%);
    background: linear-gradient(180deg, rgba(140,20,20,0) 0%, rgba(160,30,30,0.4) 15%, rgba(180,40,40,0.85) 35%, rgba(200,50,50,1) 50%, rgba(180,40,40,0.85) 65%, rgba(160,30,30,0.4) 85%, rgba(140,20,20,0) 100%);
    border-radius: 3px;
  }}

  .cross-v::after {{
    content: '';
    position: absolute;
    inset: 0;
    background: inherit;
    filter: blur(20px);
    opacity: 0.6;
  }}

  .cross-h {{
    position: absolute;
    top: 32%;
    left: 50%;
    width: 140px;
    height: 6px;
    transform: translate(-50%, -50%);
    background: linear-gradient(90deg, rgba(140,20,20,0) 0%, rgba(160,30,30,0.4) 15%, rgba(180,40,40,0.85) 35%, rgba(200,50,50,1) 50%, rgba(180,40,40,0.85) 65%, rgba(160,30,30,0.4) 85%, rgba(140,20,20,0) 100%);
    border-radius: 3px;
  }}

  .cross-h::after {{
    content: '';
    position: absolute;
    inset: 0;
    background: inherit;
    filter: blur(20px);
    opacity: 0.6;
  }}

  /* Neural nodes on cross */
  .nd {{
    position: absolute;
    border-radius: 50%;
    z-index: 2;
  }}
  .nd-1 {{ width: 8px; height: 8px; background: rgba(220,50,50,0.9); box-shadow: 0 0 12px rgba(255,30,30,0.7), 0 0 30px rgba(255,20,20,0.3); left: 50%; top: 8%; transform: translateX(-50%); }}
  .nd-2 {{ width: 6px; height: 6px; background: rgba(200,40,40,0.7); box-shadow: 0 0 8px rgba(255,20,20,0.5); left: 50%; top: 22%; transform: translateX(-50%); }}
  .nd-3 {{ width: 6px; height: 6px; background: rgba(200,40,40,0.7); box-shadow: 0 0 8px rgba(255,20,20,0.5); left: 50%; top: 78%; transform: translateX(-50%); }}
  .nd-4 {{ width: 8px; height: 8px; background: rgba(220,50,50,0.9); box-shadow: 0 0 12px rgba(255,30,30,0.7), 0 0 30px rgba(255,20,20,0.3); left: 50%; top: 92%; transform: translateX(-50%); }}
  .nd-5 {{ width: 7px; height: 7px; background: rgba(210,45,45,0.8); box-shadow: 0 0 10px rgba(255,25,25,0.6); left: 12%; top: 32%; transform: translateY(-50%); }}
  .nd-6 {{ width: 6px; height: 6px; background: rgba(200,40,40,0.7); box-shadow: 0 0 8px rgba(255,20,20,0.5); left: 30%; top: 32%; transform: translateY(-50%); }}
  .nd-7 {{ width: 6px; height: 6px; background: rgba(200,40,40,0.7); box-shadow: 0 0 8px rgba(255,20,20,0.5); right: 30%; top: 32%; transform: translateY(-50%); }}
  .nd-8 {{ width: 7px; height: 7px; background: rgba(210,45,45,0.8); box-shadow: 0 0 10px rgba(255,25,25,0.6); right: 12%; top: 32%; transform: translateY(-50%); }}

  /* Neural lines radiating */
  .neural-lines {{
    position: absolute;
    inset: -80px;
    z-index: 0;
    pointer-events: none;
  }}

  .neural-lines svg {{
    width: 100%;
    height: 100%;
  }}

  .cover-title {{
    position: relative;
    z-index: 5;
  }}

  .cover-the {{
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 0.85rem;
    color: rgba(176,154,120,0.6);
    letter-spacing: 0.5em;
    text-transform: uppercase;
    margin-bottom: 8px;
  }}

  .cover-algorithm {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: 2.6rem;
    color: #c4a87a;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-bottom: 2px;
  }}

  .cover-of {{
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 0.9rem;
    color: rgba(176,154,120,0.5);
    letter-spacing: 0.8em;
    margin-bottom: 2px;
  }}

  .cover-belief {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: 3.8rem;
    color: #d4bc94;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    text-shadow: 0 0 50px rgba(160,30,30,0.25), 0 2px 4px rgba(0,0,0,0.6);
  }}

  .cover-rule {{
    width: 80px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 35px auto;
  }}

  .cover-sub {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: rgba(196,168,122,0.7);
    letter-spacing: 0.35em;
    text-transform: uppercase;
    line-height: 2;
  }}

  .cover-sub span {{
    display: block;
  }}

  .cover-sub .god {{
    font-size: 1.6rem;
    color: #c4a87a;
    letter-spacing: 0.5em;
    text-shadow: 0 0 30px rgba(160,30,30,0.2);
  }}

  /* Blood drips */
  .drip {{
    position: absolute;
    top: 0;
    width: 2px;
    background: linear-gradient(180deg, rgba(120,15,15,0.7), rgba(80,10,10,0.3), transparent);
    z-index: 2;
    border-radius: 0 0 1px 1px;
  }}

  /* ==================== BOOK CONTENT ==================== */
  .book {{
    background: var(--paper);
    max-width: 720px;
    margin: 0 auto;
    padding: 0;
    position: relative;
  }}

  .page {{
    padding: 80px 90px 80px 100px;
    min-height: 100vh;
  }}

  /* Title page */
  .title-page {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    border-bottom: 1px solid var(--rule);
    page-break-after: always;
  }}

  .title-page h1 {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: 2.8rem;
    color: var(--red-dark);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 8px;
    border: none;
    padding: 0;
  }}

  .title-page .tp-of {{
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 1.1rem;
    color: var(--ink-muted);
    letter-spacing: 0.5em;
    margin-bottom: 8px;
  }}

  .title-page .tp-belief {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: 3.5rem;
    color: var(--red-dark);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 40px;
    border: none;
    padding: 0;
  }}

  .title-page .tp-subtitle {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: var(--ink-muted);
    letter-spacing: 0.3em;
    text-transform: uppercase;
    line-height: 2.2;
  }}

  .title-page .tp-subtitle .god {{
    font-size: 1.3rem;
    color: var(--red);
    letter-spacing: 0.4em;
  }}

  /* Table of contents */
  .toc-page {{
    page-break-after: always;
    padding: 80px 90px;
  }}

  .toc-page h2 {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 600;
    font-size: 1.6rem;
    color: var(--red-dark);
    text-align: center;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-bottom: 50px;
    border: none;
    padding: 0;
  }}

  .toc-list {{
    list-style: none;
    max-width: 500px;
    margin: 0 auto;
  }}

  .toc-list li {{
    font-family: 'EB Garamond', serif;
    font-size: 1.05rem;
    color: var(--ink-light);
    padding: 14px 0;
    border-bottom: 1px solid rgba(196,184,168,0.5);
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }}

  .toc-list .ch-num {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 600;
    color: var(--red);
    letter-spacing: 0.1em;
    margin-right: 12px;
    min-width: 80px;
  }}

  .toc-list .ch-dots {{
    flex: 1;
    border-bottom: 1px dotted var(--rule);
    margin: 0 12px;
    align-self: flex-end;
    margin-bottom: 4px;
  }}

  /* Chapters */
  .chapter {{
    page-break-before: always;
    padding-top: 60px;
  }}

  .chapter:first-of-type {{
    page-break-before: auto;
  }}

  .chapter-num {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: 0.85rem;
    color: var(--gold);
    letter-spacing: 0.4em;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 12px;
  }}

  .book h1 {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 600;
    font-size: 1.9rem;
    color: var(--red-dark);
    text-align: center;
    letter-spacing: 0.08em;
    margin-bottom: 45px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--rule);
    line-height: 1.4;
  }}

  .book h2 {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 600;
    font-size: 1.4rem;
    color: var(--red);
    margin: 50px 0 22px;
    letter-spacing: 0.05em;
    line-height: 1.4;
    border-bottom: 1px solid rgba(196,184,168,0.4);
    padding-bottom: 10px;
  }}

  .book h3 {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 600;
    font-size: 1.15rem;
    color: var(--red-light);
    margin: 40px 0 16px;
    letter-spacing: 0.03em;
    font-style: italic;
  }}

  .book p {{
    font-family: 'EB Garamond', serif;
    font-size: 1.05rem;
    line-height: 1.85;
    margin-bottom: 0;
    text-indent: 1.8em;
    text-align: justify;
    hyphens: auto;
    color: var(--ink);
  }}

  .book p:first-of-type,
  .book h1 + p,
  .book h2 + p,
  .book h3 + p,
  .book hr + p {{
    text-indent: 0;
  }}

  .book p + p {{
    text-indent: 1.8em;
  }}

  .book strong {{
    font-weight: 600;
    color: var(--ink);
  }}

  .book em {{
    font-style: italic;
  }}

  .book hr {{
    border: none;
    text-align: center;
    margin: 50px 0;
    page-break-after: avoid;
  }}

  .book hr::before {{
    content: '* * *';
    font-family: 'EB Garamond', serif;
    font-size: 1.2rem;
    color: var(--gold-light);
    letter-spacing: 0.5em;
  }}

  /* Drop cap for first paragraph of chapter */
  .chapter > p:first-of-type::first-letter,
  .book h1 + p:first-of-type::first-letter {{
    float: left;
    font-family: 'Cormorant Garamond', serif;
    font-weight: 700;
    font-size: 4.2em;
    line-height: 0.8;
    padding-right: 10px;
    padding-top: 6px;
    color: var(--red-dark);
  }}

  /* Footnotes section */
  .footnotes {{
    margin-top: 60px;
    padding-top: 30px;
    border-top: 1px solid var(--rule);
  }}

  .footnotes p {{
    font-size: 0.82rem;
    line-height: 1.6;
    text-indent: 0;
    color: var(--ink-muted);
    margin-bottom: 4px;
  }}

  .footnotes p + p {{
    text-indent: 0;
  }}

  /* ==================== RESPONSIVE ==================== */
  @media (max-width: 800px) {{
    .page, .toc-page {{
      padding: 40px 30px;
    }}
    .cover-algorithm {{ font-size: 2rem; }}
    .cover-belief {{ font-size: 2.8rem; }}
    .book h1 {{ font-size: 1.5rem; }}
    .book h2 {{ font-size: 1.2rem; }}
    .book p {{ font-size: 1rem; text-indent: 1.4em; }}
  }}

  /* ==================== PRINT ==================== */
  @media print {{
    body {{ background: white; }}
    .cover {{ page-break-after: always; min-height: 100vh; }}
    .book {{ box-shadow: none; max-width: 100%; }}
    .page {{ padding: 60px 80px; }}
    .chapter {{ page-break-before: always; }}
  }}
</style>
</head>
<body>

<!-- ==================== COVER ==================== -->
<div class="cover">
  <div class="drip" style="left: 18%; height: 55px;"></div>
  <div class="drip" style="left: 38%; height: 38px;"></div>
  <div class="drip" style="left: 58%; height: 65px;"></div>
  <div class="drip" style="left: 76%; height: 30px;"></div>
  <div class="drip" style="left: 90%; height: 48px;"></div>

  <div class="cover-inner">
    <div class="cross-wrap">
      <div class="cross-v"></div>
      <div class="cross-h"></div>
      <div class="nd nd-1"></div>
      <div class="nd nd-2"></div>
      <div class="nd nd-3"></div>
      <div class="nd nd-4"></div>
      <div class="nd nd-5"></div>
      <div class="nd nd-6"></div>
      <div class="nd nd-7"></div>
      <div class="nd nd-8"></div>
      
      <div class="neural-lines">
        <svg viewBox="0 0 320 420" xmlns="http://www.w3.org/2000/svg">
          <g stroke="rgba(160,30,30,0.12)" stroke-width="0.5" fill="none">
            <line x1="160" y1="40" x2="60" y2="100"/>
            <line x1="60" y1="100" x2="30" y2="70"/>
            <line x1="60" y1="100" x2="100" y2="60"/>
            <line x1="30" y1="70" x2="20" y2="130"/>
            <line x1="100" y1="60" x2="130" y2="90"/>
            <line x1="130" y1="90" x2="160" y2="130"/>
            
            <line x1="160" y1="40" x2="260" y2="100"/>
            <line x1="260" y1="100" x2="290" y2="70"/>
            <line x1="260" y1="100" x2="220" y2="60"/>
            <line x1="290" y1="70" x2="300" y2="130"/>
            <line x1="220" y1="60" x2="190" y2="90"/>
            
            <line x1="160" y1="380" x2="70" y2="320"/>
            <line x1="70" y1="320" x2="40" y2="350"/>
            <line x1="70" y1="320" x2="110" y2="290"/>
            
            <line x1="160" y1="380" x2="250" y2="320"/>
            <line x1="250" y1="320" x2="280" y2="350"/>
            <line x1="250" y1="320" x2="210" y2="290"/>
            
            <line x1="160" y1="130" x2="80" y2="174"/>
            <line x1="160" y1="130" x2="240" y2="174"/>
            <line x1="80" y1="266" x2="160" y2="310"/>
            <line x1="240" y1="266" x2="160" y2="310"/>
          </g>
          <g>
            <circle cx="60" cy="100" r="2" fill="rgba(200,40,40,0.5)"/>
            <circle cx="30" cy="70" r="1.5" fill="rgba(180,30,30,0.3)"/>
            <circle cx="100" cy="60" r="1.5" fill="rgba(180,30,30,0.3)"/>
            <circle cx="260" cy="100" r="2" fill="rgba(200,40,40,0.5)"/>
            <circle cx="290" cy="70" r="1.5" fill="rgba(180,30,30,0.3)"/>
            <circle cx="220" cy="60" r="1.5" fill="rgba(180,30,30,0.3)"/>
            <circle cx="70" cy="320" r="2" fill="rgba(200,40,40,0.5)"/>
            <circle cx="250" cy="320" r="2" fill="rgba(200,40,40,0.5)"/>
            <circle cx="160" cy="130" r="3" fill="rgba(210,45,45,0.7)"/>
            <circle cx="80" cy="174" r="2.5" fill="rgba(200,40,40,0.6)"/>
            <circle cx="240" cy="174" r="2.5" fill="rgba(200,40,40,0.6)"/>
            <circle cx="160" cy="310" r="2.5" fill="rgba(200,40,40,0.6)"/>
          </g>
        </svg>
      </div>
    </div>

    <div class="cover-title">
      <div class="cover-the">The</div>
      <div class="cover-algorithm">Algorithm</div>
      <div class="cover-of">of</div>
      <div class="cover-belief">Belief</div>
    </div>

    <div class="cover-rule"></div>

    <div class="cover-sub">
      <span>Finding</span>
      <span class="god">God</span>
      <span>in Innovation</span>
    </div>
  </div>
</div>

<!-- ==================== BOOK ==================== -->
<div class="book">

  <!-- Title Page -->
  <div class="page title-page">
    <h1>The Algorithm</h1>
    <div class="tp-of">of</div>
    <div class="tp-belief">Belief</div>
    <div class="tp-subtitle">
      Finding<br>
      <span class="god">God</span><br>
      in Innovation
    </div>
  </div>

  <!-- Table of Contents -->
  <div class="toc-page">
    <h2>Contents</h2>
    <ul class="toc-list">
      <li>
        <span class="ch-num">Chapter 1</span>
        <span>The Convergence of Blockchain and AI</span>
      </li>
      <li>
        <span class="ch-num">Chapter 2</span>
        <span>Exploring the Philosophical Foundations</span>
      </li>
      <li>
        <span class="ch-num">Chapter 3</span>
        <span>Blockchain and AI in Philosophical Traditions</span>
      </li>
      <li>
        <span class="ch-num">Chapter 4</span>
        <span>Blockchain and AI in Contemporary Theories</span>
      </li>
      <li>
        <span class="ch-num">Chapter 5</span>
        <span>Blockchain and AI in Real-World Applications</span>
      </li>
      <li>
        <span class="ch-num">Chapter 6</span>
        <span>Challenges, Solutions, and Ethics</span>
      </li>
      <li>
        <span class="ch-num">Chapter 7</span>
        <span>The Road Ahead: Future Prospects</span>
      </li>
    </ul>
  </div>

  <!-- Main Content -->
  <div class="page">
    {full_html}
  </div>

</div>

</body>
</html>'''

output_path = os.path.join(book_dir, "The_Algorithm_of_Belief_Pro.html")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = os.path.getsize(output_path) / 1024
print(f"Professional HTML book generated: {output_path}")
print(f"File size: {size_kb:.1f} KB")
