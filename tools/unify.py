import re
p='src/mob-swarm.js'
js=open(p).read()

# signature: single canvas
js=js.replace("export function createGame({ input, loop, rng, save, ctxGame, ctxHud }) {","export function createGame({ input, loop, rng, save, ctxGame }) {")
js=js.replace("var hudCanvas = { width: 360, height: 640 }, hctx = ctxHud;   // flat overlay: HUD, base bar, trackpad, flash","var hudCanvas = { width: 360, height: 640 };   // legacy stub (no flat canvas any more)")
js=js.replace("    hctx.setTransform(hudCanvas.width / W, 0, 0, hudCanvas.height / H, 0, 0);\n","")

# base bar drawn on the single world canvas (before cannon section: insert after danger line block)
marker="    // Black holes (rotating swirl)"
base="""    // Opponent base: drawn on the unified canvas at the far end of the track (tilts with the world)
    var heatMix = baseHeat * (0.5 + 0.5 * Math.sin(clock * 55));
    var shake = Math.sin(clock * 90) * baseHeat * 2;
    ctx.fillStyle = 'rgb(' + ((216 + 39 * heatMix) | 0) + ',' + ((58 + 80 * heatMix) | 0) + ',' + ((74 + 64 * heatMix) | 0) + ')';
    roundRect(10 + shake, BASE_Y, W - 20, BASE_H, 14);
    ctx.fill();

"""
assert marker in js
js=js.replace(marker, base+marker,1)

# renderHud -> DOM only
s=js.index("  function renderHud() {")
e=js.index("  return {\n    update: function(dt)")
new="""  var uiPower = document.getElementById('ui-power');
  var uiFlash = document.getElementById('ui-flash');
  function renderHud() {
    if (uiLevel) uiLevel.innerText = 'LEVEL ' + level + ' / ' + MAX_LEVEL + (isBossLevel ? ' [BOSS]' : '');
    if (uiHpText && uiHpFill) {
      var showHP = isBossLevel ? bossHP : baseHP, showMax = isBossLevel ? bossMaxHP : baseMaxHP;
      uiHpText.innerText = (isBossLevel ? 'BOSS ' + fmt(bossActive ? bossHP : bossMaxHP) : fmt(baseHP) + ' HP');
      uiHpFill.style.width = (((bossActive || !isBossLevel ? showHP : showMax) / showMax) * 100) + '%';
      uiHpFill.style.backgroundColor = isBossLevel ? '#ff9a3c' : '#7dff9a';
    }
    if (uiPower) uiPower.innerText = powerLeft > 0 ? Armory[powerName].name.toUpperCase() + ' ' + powerLeft.toFixed(1) + 's' : '';
    if (uiFlash) uiFlash.style.opacity = cannonFlash > 0 ? (cannonFlash * 0.28).toFixed(3) : '0';
  }

"""
js=js[:s]+new+js[e:]
open(p,'w').write(js)

h=open('index.html').read()
h=h.replace('    <canvas id="hud"></canvas>\n','')
h=h.replace('<div id="ui-overlay">','<div id="ui-overlay">\n      <div id="ui-flash"></div>\n      <div id="ui-power"></div>')
h=re.sub(r"  /\* Flat canvas for the HUD \*/\n  #hud \{[^}]*\}\n","  #ui-flash { position: absolute; inset: 0; background: rgb(255,40,60); opacity: 0; }\n  #ui-power { position: absolute; top: 40px; right: 14px; font-weight: 800; font-size: 13px; color: #ffd36a; }\n",h)
h=h.replace("  const hudCanvas = document.getElementById('hud');\n","")
h=h.replace("    hudCanvas.width = Math.floor(cw * dpr); hudCanvas.height = Math.floor(ch * dpr);\n","    ctxGame.setTransform(canvas.width / W, 0, 0, canvas.height / wh, 0, -WORLD_TOP * canvas.height / wh);\n")
h=h.replace("  const dim = resize();\n  window.addEventListener('resize', () => resize());\n\n  // Set up contexts\n  const ctxGame = canvas.getContext('2d');\n  const ctxHud = hudCanvas.getContext('2d');\n","  const ctxGame = canvas.getContext('2d');\n  const dim = resize();\n  window.addEventListener('resize', () => resize());\n")
h=re.sub(r"  // Transform contexts just once.*?\n  ctxHud\.setTransform[^\n]*\n","",h,flags=re.S)
h=h.replace("    ctxGame, \n    ctxHud \n","    ctxGame\n")
open('index.html','w').write(h)
