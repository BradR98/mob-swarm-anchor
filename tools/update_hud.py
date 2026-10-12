import re

with open('src/mob-swarm.js', 'r') as f:
    js = f.read()

# We need to replace the entire body of renderHud(). 
# Let's find it.
start = js.find('function renderHud() {')
end = js.find('  return {\n    update: function(dt)')

new_render_hud = """
  var uiLevel = document.getElementById('ui-level');
  var uiHpText = document.getElementById('ui-hp-text');
  var uiHpFill = document.getElementById('ui-hp-bar-fill');
  var uiHpBg = document.getElementById('ui-hp-bar-bg');

  function renderHud() {
    ctx = hctx;
    ctx.clearRect(0, 0, W, H);
    var BY = baseScreenBottom - BASE_H; if (BY < HUD_TOP - 22) BY = HUD_TOP - 22;

    // Update DOM UI
    if (uiLevel) {
      uiLevel.innerText = 'LEVEL ' + level + ' / ' + MAX_LEVEL + (isBossLevel ? ' [BOSS]' : '');
    }
    if (uiHpText && uiHpFill) {
      var showHP = isBossLevel ? bossHP : baseHP, showMax = isBossLevel ? bossMaxHP : baseMaxHP;
      uiHpText.innerText = (isBossLevel ? 'BOSS ' + fmt(bossActive ? bossHP : bossMaxHP) : fmt(baseHP) + ' HP');
      uiHpFill.style.width = (((bossActive || !isBossLevel ? showHP : showMax) / showMax) * 100) + '%';
      uiHpFill.style.backgroundColor = isBossLevel ? '#ff9a3c' : '#7dff9a';
    }

    // Powerup text
    if (powerLeft > 0) {
      ctx.fillStyle = '#ffd36a'; ctx.font = '800 13px system-ui, sans-serif'; ctx.textAlign = 'right';
      ctx.fillText(Armory[powerName].name.toUpperCase() + ' ' + powerLeft.toFixed(1) + 's', W - 14, 26);
      ctx.textAlign = 'left';
    }

    // Screen flash when the cannon is hit
    if (cannonFlash > 0) {
      ctx.fillStyle = 'rgba(255,40,60,' + (cannonFlash * 0.28).toFixed(3) + ')';
      ctx.fillRect(0, 0, W, H);
    }
  }

"""

js = js[:start] + new_render_hud + js[end:]

with open('src/mob-swarm.js', 'w') as f:
    f.write(js)
