import os
import re

book_dir = r"C:\Users\RAKICT\Documents\The_Algorithm_of_Belief"

# Read all chapter files in order
chapter_files = sorted([f for f in os.listdir(book_dir) if f.startswith("Chapter_") and f.endswith(".md")])

chapters_content = []
for cf in chapter_files:
    with open(os.path.join(book_dir, cf), 'r', encoding='utf-8') as f:
        chapters_content.append(f.read())

# Convert markdown to simple HTML
def md_to_html(md):
    html = md
    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    # Horizontal rules
    html = re.sub(r'^---+$', r'<hr>', html, flags=re.MULTILINE)
    # Footnotes
    html = re.sub(r'(\d+)', r'<sup>\1</sup>', html)  # This is too aggressive, skip
    # Paragraphs
    lines = html.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('<h') and not stripped.startswith('<hr') and not stripped.startswith('<sup'):
            if not stripped.startswith('<'):
                result.append(f'<p>{stripped}</p>')
            else:
                result.append(stripped)
        else:
            result.append(stripped)
    return '\n'.join(result)

full_html = '\n\n'.join([md_to_html(ch) for ch in chapters_content])

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Algorithm of Belief: Finding God in Innovation</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Cinzel+Decorative:wght@400;700;900&family=IM+Fell+English:ital@0;1&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap');

  :root {{
    --bg-dark: #0a0505;
    --bg-page: #f5f0e8;
    --text-dark: #1a1a1a;
    --accent-red: #8b1a1a;
    --accent-gold: #c8a882;
    --accent-crimson: #6b0f0f;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    background: var(--bg-dark);
    font-family: 'EB Garamond', 'Georgia', serif;
    color: var(--text-dark);
  }}

  /* COVER PAGE */
  .cover {{
    width: 100%;
    min-height: 100vh;
    position: relative;
    overflow: hidden;
    background: radial-gradient(ellipse at 50% 30%, #1a0a0a 0%, #0a0505 40%, #050202 70%, #000000 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    page-break-after: always;
  }}

  .cover::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse at center, transparent 30%, rgba(0,0,0,0.7) 100%);
    z-index: 10;
    pointer-events: none;
  }}

  .cover-cross {{
    position: relative;
    width: 200px;
    height: 300px;
    margin-bottom: 40px;
    z-index: 5;
  }}

  .cover-cross-v {{
    position: absolute;
    width: 8px;
    height: 300px;
    background: linear-gradient(180deg, rgba(180,30,30,0.1) 0%, rgba(220,50,50,0.9) 40%, rgba(255,60,60,1) 50%, rgba(220,50,50,0.9) 60%, rgba(180,30,30,0.1) 100%);
    left: 50%;
    transform: translateX(-50%);
    box-shadow: 0 0 20px rgba(255,0,0,0.5), 0 0 60px rgba(200,0,0,0.3), 0 0 100px rgba(150,0,0,0.2);
  }}

  .cover-cross-h {{
    position: absolute;
    width: 200px;
    height: 8px;
    background: linear-gradient(90deg, rgba(180,30,30,0.1) 0%, rgba(220,50,50,0.9) 40%, rgba(255,60,60,1) 50%, rgba(220,50,50,0.9) 60%, rgba(180,30,30,0.1) 100%);
    top: 30%;
    box-shadow: 0 0 20px rgba(255,0,0,0.5), 0 0 60px rgba(200,0,0,0.3);
  }}

  .cover-node {{
    position: absolute;
    width: 10px;
    height: 10px;
    background: #ff3333;
    border-radius: 50%;
    box-shadow: 0 0 10px #ff0000, 0 0 25px rgba(255,0,0,0.5);
  }}

  .cover-title {{
    text-align: center;
    z-index: 15;
    position: relative;
  }}

  .cover-title .the {{
    font-family: 'IM Fell English', serif;
    font-style: italic;
    font-size: 18px;
    color: rgba(200,160,120,0.7);
    letter-spacing: 10px;
    text-transform: uppercase;
  }}

  .cover-title .algorithm {{
    font-family: 'Cinzel Decorative', serif;
    font-weight: 900;
    font-size: 48px;
    color: #c8a882;
    letter-spacing: 6px;
    text-transform: uppercase;
    text-shadow: 0 0 30px rgba(200,50,50,0.4), 0 3px 6px rgba(0,0,0,0.9);
  }}

  .cover-title .of {{
    font-family: 'IM Fell English', serif;
    font-style: italic;
    font-size: 20px;
    color: rgba(200,160,120,0.6);
    letter-spacing: 14px;
  }}

  .cover-title .belief {{
    font-family: 'Cinzel Decorative', serif;
    font-weight: 900;
    font-size: 64px;
    color: #d4b896;
    letter-spacing: 8px;
    text-transform: uppercase;
    text-shadow: 0 0 40px rgba(200,50,50,0.5), 0 0 80px rgba(150,30,30,0.3), 0 4px 8px rgba(0,0,0,0.9);
  }}

  .cover-subtitle {{
    text-align: center;
    margin-top: 30px;
    z-index: 15;
    position: relative;
  }}

  .cover-subtitle .finding {{
    font-family: 'Cinzel', serif;
    font-size: 18px;
    color: rgba(220,180,140,0.7);
    letter-spacing: 8px;
    text-transform: uppercase;
  }}

  .cover-subtitle .god {{
    font-family: 'Cinzel', serif;
    font-weight: 700;
    font-size: 28px;
    color: #c8a882;
    letter-spacing: 10px;
    text-transform: uppercase;
    text-shadow: 0 0 25px rgba(200,50,50,0.3);
  }}

  .cover-subtitle .innovation {{
    font-family: 'Cinzel', serif;
    font-size: 18px;
    color: rgba(220,180,140,0.7);
    letter-spacing: 8px;
    text-transform: uppercase;
  }}

  /* BOOK CONTENT */
  .book-content {{
    background: var(--bg-page);
    max-width: 800px;
    margin: 0 auto;
    padding: 60px 80px;
    box-shadow: 0 0 100px rgba(0,0,0,0.5);
    min-height: 100vh;
  }}

  .book-content h1 {{
    font-family: 'Cinzel', serif;
    font-weight: 900;
    font-size: 28px;
    color: var(--accent-crimson);
    text-align: center;
    margin: 60px 0 30px;
    letter-spacing: 3px;
    text-transform: uppercase;
    border-bottom: 2px solid var(--accent-red);
    padding-bottom: 15px;
  }}

  .book-content h2 {{
    font-family: 'Cinzel', serif;
    font-weight: 700;
    font-size: 22px;
    color: var(--accent-crimson);
    margin: 45px 0 20px;
    letter-spacing: 2px;
  }}

  .book-content h3 {{
    font-family: 'Cinzel', serif;
    font-weight: 400;
    font-size: 18px;
    color: var(--accent-red);
    margin: 35px 0 15px;
    letter-spacing: 1px;
  }}

  .book-content p {{
    font-size: 17px;
    line-height: 1.85;
    margin-bottom: 18px;
    text-align: justify;
    hyphens: auto;
    color: #2a2a2a;
  }}

  .book-content strong {{
    font-weight: 600;
    color: #1a1a1a;
  }}

  .book-content em {{
    font-style: italic;
  }}

  .book-content hr {{
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent-red), transparent);
    margin: 40px 0;
  }}

  .book-content sup {{
    font-size: 0.7em;
    color: var(--accent-red);
    vertical-align: super;
  }}

  /* TABLE OF CONTENTS */
  .toc {{
    page-break-after: always;
    padding: 40px 0;
  }}

  .toc h2 {{
    font-family: 'Cinzel Decorative', serif;
    font-size: 24px;
    text-align: center;
    color: var(--accent-crimson);
    margin-bottom: 40px;
    letter-spacing: 4px;
  }}

  .toc ul {{
    list-style: none;
    padding: 0;
  }}

  .toc li {{
    font-family: 'Cinzel', serif;
    font-size: 16px;
    padding: 12px 0;
    border-bottom: 1px dotted rgba(139,26,26,0.3);
    color: #333;
  }}

  .toc li span {{
    color: var(--accent-red);
    font-weight: 600;
  }}

  /* PRINT STYLES */
  @media print {{
    body {{ background: white; }}
    .cover {{ page-break-after: always; }}
    .book-content {{ box-shadow: none; padding: 40px; max-width: 100%; }}
    .book-content h1 {{ page-break-before: always; }}
  }}
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
  <div class="cover-cross">
    <div class="cover-cross-v"></div>
    <div class="cover-cross-h"></div>
    <div class="cover-node" style="top: -5px; left: 50%; transform: translateX(-50%);"></div>
    <div class="cover-node" style="top: 30%; left: -5px; transform: translateY(-50%);"></div>
    <div class="cover-node" style="top: 30%; right: -5px; transform: translateY(-50%);"></div>
    <div class="cover-node" style="bottom: -5px; left: 50%; transform: translateX(-50%);"></div>
  </div>
  
  <div class="cover-title">
    <div class="the">The</div>
    <div class="algorithm">Algorithm</div>
    <div class="of">of</div>
    <div class="belief">Belief</div>
  </div>
  
  <div class="cover-subtitle">
    <div class="finding">Finding</div>
    <div class="god">God</div>
    <div class="innovation">in Innovation</div>
  </div>
</div>

<!-- BOOK CONTENT -->
<div class="book-content">

<!-- TABLE OF CONTENTS -->
<div class="toc">
  <h2>Contents</h2>
  <ul>
    <li><span>Chapter 1</span> — The Convergence of Blockchain and AI</li>
    <li><span>Chapter 2</span> — Exploring the Philosophical Foundations</li>
    <li><span>Chapter 3</span> — Blockchain and AI in the Context of Philosophical Traditions</li>
    <li><span>Chapter 4</span> — Blockchain and AI in Contemporary Philosophical Theories</li>
    <li><span>Chapter 5</span> — Blockchain and AI in Real-World Applications</li>
    <li><span>Chapter 6</span> — Challenges, Solutions, and Ethical Considerations</li>
    <li><span>Chapter 7</span> — The Road Ahead: Future Prospects</li>
  </ul>
</div>

{full_html}

</div>

</body>
</html>'''

output_path = os.path.join(book_dir, "The_Algorithm_of_Belief_Complete.html")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"HTML book generated: {output_path}")
print(f"File size: {os.path.getsize(output_path) / 1024:.1f} KB")
