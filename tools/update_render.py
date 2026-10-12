import re

with open('src/mob-swarm.js', 'r') as f:
    js = f.read()

# Replace background drawing with clearRect
bg_code = """    // Background
    ctx.fillStyle = '#0b1020';
    ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = '#242a40';                          // letterbox: unused screen space is grayed out
    ctx.fillRect(10, BASE_BOTTOM, W - 20, TRACK_Y - BASE_BOTTOM);
"""
new_bg_code = """    // Clear for transparency
    ctx.clearRect(0, 0, W, H);
"""

js = js.replace(bg_code, new_bg_code)

with open('src/mob-swarm.js', 'w') as f:
    f.write(js)
