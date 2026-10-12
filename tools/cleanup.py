import re

with open('src/mob-swarm.js', 'r') as f:
    content = f.read()

# Stub out DOM elements
content = re.sub(r'var hudCanvas = document\.getElementById\(\'hud\'\), hctx = hudCanvas\.getContext\(\'2d\'\);', 'var hudCanvas = { width: 360, height: 640 }; var hctx = ctxHud;', content)
content = re.sub(r'var stage = document\.getElementById\(\'stage\'\);', 'var stage = { style: {} };', content)
content = re.sub(r'var overlay = document\.getElementById\(\'overlay\'\);', 'var overlay = { classList: { add: function(){}, remove: function(){} } };', content)
content = re.sub(r'var overlayTitle = document\.getElementById\(\'overlayTitle\'\);', 'var overlayTitle = { innerText: "" };', content)
content = re.sub(r'var restartBtn = document\.getElementById\(\'restart\'\);', 'var restartBtn = { classList: { add: function(){}, remove: function(){} }, blur: function(){} };', content)
content = re.sub(r'var muteBtn = document\.getElementById\(\'mute\'\);', 'var muteBtn = { innerText: "" };', content)
content = re.sub(r'var pauseBtn = document\.getElementById\(\'pause\'\);', 'var pauseBtn = { innerText: "" };', content)
content = re.sub(r'var lvlInput = document\.getElementById\(\'lvlInput\'\), warpBtn = document\.getElementById\(\'warp\'\);', 'var lvlInput = { value: "1" }, warpBtn = {};', content)

# Remove syncMuteBtn and audio stuff
content = re.sub(r'function syncMuteBtn\(\).*?\}', 'function syncMuteBtn(){} ', content, flags=re.DOTALL)
content = re.sub(r'function initAudio\(\).*?\}', 'function initAudio(){} ', content, flags=re.DOTALL)
content = re.sub(r'function sfx.*?\).*?\}', 'function sfx(){} ', content, flags=re.DOTALL) # Need to be careful here

# Let's just stub audio calls with a regex
content = re.sub(r'function sfx[A-Z]\w*\([^)]*\)\s*\{[^}]*\}', '', content)
content = re.sub(r'sfx[A-Z]\w*\([^)]*\);?', '', content)

# Handle resize
content = re.sub(r'function resize\(\).*?\}\n', 'function resize(){} ', content, flags=re.DOTALL)

with open('src/mob-swarm.js', 'w') as f:
    f.write(content)
