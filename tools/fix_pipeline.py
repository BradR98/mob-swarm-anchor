import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. HTML: Remove #tilt wrapper
html = html.replace('<div id="tilt"><canvas id="game"></canvas></div>', '<canvas id="game"></canvas>')

# 2. CSS: Update styles
css_replace = """
  /* Logical Game Canvas */
  #game {
    position: absolute; left: 50%; bottom: 0;
    transform-origin: 50% 100%; z-index: 1;
    background-color: transparent;
    pointer-events: none; display: block;
  }
"""
# Replace old #tilt CSS
html = re.sub(r'  /\* Tilted CSS for the physics world \*/.*?display: block; \}', css_replace.strip(), html, flags=re.DOTALL)

# 3. JS: Remove tiltEl, update canvas styling in resize
html = html.replace("const tiltEl = document.getElementById('tilt');", "")
html = html.replace("tiltEl.style.width", "canvas.style.width")
html = html.replace("tiltEl.style.height", "canvas.style.height")
html = html.replace("tiltEl.style.bottom", "canvas.style.bottom")
html = html.replace("tiltEl.style.transform = 'perspective(' + (P * k) + 'px) rotateX(' + TILT + 'deg)';", "canvas.style.transform = 'translateX(-50%) perspective(' + (P * k) + 'px) rotateX(' + TILT + 'deg)';")

# 4. Remove { alpha: false } to allow transparency
html = html.replace("canvas.getContext('2d', { alpha: false })", "canvas.getContext('2d')")

with open('index.html', 'w') as f:
    f.write(html)
