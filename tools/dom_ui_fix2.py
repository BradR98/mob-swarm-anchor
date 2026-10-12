import re

with open('index.html', 'r') as f:
    html = f.read()

start = html.find('#ui-overlay {')
end = html.find('/* Flat canvas for the HUD */')

new_css = """#ui-overlay {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 10;
    pointer-events: none; box-sizing: border-box; padding: 14px;
  }
  #ui-level { position: absolute; top: 14px; left: 14px; font-weight: 800; font-size: 16px; color: rgba(255,255,255,0.85); text-align: left; }
  #ui-hp-wrapper { position: absolute; top: 14px; left: 0; width: 100%; display: flex; flex-direction: column; align-items: center; }
  #ui-hp-text { font-weight: 700; font-size: 16px; color: #fff; margin-bottom: 6px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
  #ui-hp-bar-bg { width: 140px; height: 6px; background: rgba(0,0,0,0.35); border-radius: 3px; overflow: hidden; }
  #ui-hp-bar-fill { height: 100%; background: #7dff9a; width: 100%; transition: width 0.1s linear, background-color 0.2s; }
  """

html = html[:start] + new_css + html[end:]

with open('index.html', 'w') as f:
    f.write(html)
