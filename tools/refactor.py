import re

with open('src/mob-swarm.js', 'r') as f:
    content = f.read()

# 1. Strip IIFE
content = content.replace("(function () {\n  'use strict';", "")
content = content.replace("})();", "")

# 2. Add imports
content = """
import { State } from './lib/anchor-loop.js';
import { loadState, saveState, clearState } from './lib/anchor-save.js';

export function createGame({ input, loop, rng, save, ctxGame, ctxHud }) {
""" + content

# 3. Replace DOM references
# Canvas variables
content = content.replace("var canvas = document.getElementById('game');", "var canvas = { width: 360, height: 640 };")
content = content.replace("var wctx = canvas.getContext('2d', { alpha: false });", "var wctx = ctxGame;")
content = content.replace("var tiltEl = document.getElementById('tilt');", "var tiltEl = { style: {} };")
content = content.replace("var hudCanvas = document.getElementById('hud'), hctx = hudCanvas.getContext('2d');", "var hudCanvas = { width: 360, height: 640 }, hctx = ctxHud;")
content = content.replace("var stage = document.getElementById('stage');", "var stage = { style: {} };")
content = content.replace("var overlay = document.getElementById('overlay');", "var overlay = { classList: { add: function(){}, remove: function(){}, toggle: function(){} } };")
content = content.replace("var overlayTitle = document.getElementById('overlayTitle');", "var overlayTitle = { textContent: '' };")
content = content.replace("var restartBtn = document.getElementById('restart');", "var restartBtn = { textContent: '' };")
content = content.replace("var muteBtn = document.getElementById('mute');", "var muteBtn = {};")
content = content.replace("var pauseBtn = document.getElementById('pause');", "var pauseBtn = {};")
content = content.replace("var lvlInput = document.getElementById('lvlInput'), warpBtn = document.getElementById('warp');", "var lvlInput = { value: 1 }, warpBtn = {};")

# 4. Remove resize, audio, input listeners. 
# We'll just comment out generic addEventListeners
content = re.sub(r'(window|document|hudCanvas|restartBtn|pauseBtn|warpBtn|lvlInput|muteBtn)\.addEventListener', '// addEventListener', content)

# 5. Fix `getTargetX` and `dragging` logic for input
content = content.replace("var cannonX = W / 2, targetX = W / 2;", "var cannonX = W / 2, targetX = W / 2; function getTargetX() { return input.getX(); }")
content = content.replace("cannonX += (targetX - cannonX) * Math.min(1, dt * 18);", "cannonX += (getTargetX() - cannonX) * Math.min(1, dt * 18);")
content = content.replace("if (dragging && autoFire) {", "if (input.isDown() && autoFire) {")

# 6. Fix `endGame(newState)` to talk to loop
content = content.replace("if (newState === WON) level = level >= MAX_LEVEL ? 1 : level + 1;", "if (newState === WON) level = level >= MAX_LEVEL ? 1 : level + 1;")
# Wait, let's inject a call to loop.gameOver() and loop.levelClear() inside endGame
end_game_injection = """
  function endGame(newState) {
    state = newState;
    mobCount = 0; redCount = 0; bossActive = false;
    if (newState === WON) loop.levelClear();
    else loop.gameOver();
  }
"""
content = re.sub(r'function endGame\(newState\).*?sfxLose\(\);\n  \}', end_game_injection, content, flags=re.DOTALL)

# 7. Remove the frame loop entirely
content = re.sub(r'// ---------- Main loop ----------.*', '', content, flags=re.DOTALL)

# 8. Export the update/draw API
content += """
  return {
    update: function(dt) {
      update(dt);
    },
    draw: function(alpha) {
      render();
      renderHud();
    }
  };
}
"""

with open('src/mob-swarm.js', 'w') as f:
    f.write(content)
