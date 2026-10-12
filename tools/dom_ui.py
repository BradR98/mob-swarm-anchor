import re

with open('index.html', 'r') as f:
    html = f.read()

ui_html = """
    <div id="ui-overlay">
      <div id="ui-level">LEVEL 1 / 100</div>
      <div id="ui-hp-wrapper">
        <div id="ui-hp-text">250 HP</div>
        <div id="ui-hp-bar-bg"><div id="ui-hp-bar-fill"></div></div>
      </div>
    </div>
"""

html = html.replace('<canvas id="hud"></canvas>', '<canvas id="hud"></canvas>\n' + ui_html)

ui_css = """
  #ui-overlay {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 10;
    pointer-events: none; display: flex; flex-direction: column; justify-content: space-between;
    box-sizing: border-box; padding: 14px;
  }
  #ui-overlay * { pointer-events: none; }
  #ui-level { font-weight: 800; font-size: 16px; color: rgba(255,255,255,0.85); text-align: left; }
  #ui-hp-wrapper { width: 100%; text-align: center; margin-top: 10px; }
  #ui-hp-text { font-weight: 700; font-size: 20px; color: #fff; margin-bottom: 6px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
  #ui-hp-bar-bg { width: 100%; height: 6px; background: rgba(0,0,0,0.35); border-radius: 3px; overflow: hidden; }
  #ui-hp-bar-fill { height: 100%; background: #7dff9a; width: 100%; transition: width 0.1s linear, background-color 0.2s; }
"""

html = html.replace('/* Flat canvas for the HUD */', ui_css + '\n  /* Flat canvas for the HUD */')

html = html.replace('#tilt { position: absolute;', '#tilt { position: absolute; z-index: 1;')

with open('index.html', 'w') as f:
    f.write(html)
