import re

with open('CHANGELOG.md', 'r') as f:
    cl = f.read()

entry = """## [v18.1.1] (MS2-BUGFIX-RENDER-PIPELINE)
- Target the Logical Canvas: Stripped the `#tilt` wrapper and directly targeted the `#game` canvas.
- Apply 3D Transforms to Canvas: Shifted the `perspective` and `rotateX` CSS transformations directly onto the active `<canvas id="game">` element.
- Centering & Alignment: Applied `left: 50%; transform: translateX(-50%)` inline with the 3D transforms to perfectly center the skewed canvas inside the viewport stage.
- Remove Debug Backgrounds: Removed the hardcoded `#0b1020` and `#242a40` letterbox background fills from `mob-swarm.js`'s Canvas 2D render loop, swapping them for `clearRect()`. The game field now correctly utilizes CSS transparency.
- Input Rail Calibration: Verified that `AnchorInput` is bound to the flat `#stage` wrapper rather than the transformed `<canvas>`, bypassing `getBoundingClientRect()` distortion completely and guaranteeing 1:1 logical input tracking.

"""

cl = cl.replace('# Changelog\n', '# Changelog\n\n' + entry)

with open('CHANGELOG.md', 'w') as f:
    f.write(cl)
