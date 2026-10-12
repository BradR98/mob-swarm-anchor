import re

with open('src/mob-swarm.js', 'r') as f:
    content = f.read()

# Replace canvas lookups with the passed contexts
content = re.sub(r'var canvas = document\.getElementById\(\'game\'\);', 'var canvas = { width: 360, height: 640 }; // Stub for sizing', content)
content = re.sub(r'var wctx = canvas\.getContext.*?;\s*// world canvas \(tilted\)', 'var wctx = ctxGame;', content)
content = re.sub(r'var hudCanvas = document\.getElementById\(\'hud\'\);', 'var hudCanvas = { width: 360, height: 640 }; // Stub for sizing', content)
content = re.sub(r'var hudCtx = hudCanvas\.getContext.*?;\s*// flat UI canvas', 'var hudCtx = ctxHud;', content)
content = re.sub(r'var tiltEl = document\.getElementById\(\'tilt\'\);', 'var tiltEl = { style: {} };', content)

# Fix DOM listeners that weren't caught
content = re.sub(r'window\.addEventListener\(.*?\}\);', '', content, flags=re.DOTALL)
content = re.sub(r'document\.addEventListener\(.*?\}\);', '', content, flags=re.DOTALL)
content = re.sub(r'pauseBtn\.addEventListener\(.*?\);', '', content, flags=re.DOTALL)
content = re.sub(r'restartBtn\.addEventListener\(.*?\);', '', content, flags=re.DOTALL)
content = re.sub(r'warpBtn\.addEventListener\(.*?\);', '', content, flags=re.DOTALL)
content = re.sub(r'muteBtn\.addEventListener\(.*?\);', '', content, flags=re.DOTALL)
content = re.sub(r'\w+\.addEventListener\(.*?\);', '', content) # generic catch all for btn listeners

# Ensure input logic works
content = re.sub(r'var dragging = false;', 'var dragging = false; function getTargetX() { return input.getX(); }', content)
content = re.sub(r'function getTargetX\(\) \{ return input\.getX\(\); \}\n.*?var dragging = false;', 'var dragging = false;', content, flags=re.DOTALL) # remove double injection

with open('src/mob-swarm.js', 'w') as f:
    f.write(content)
