import re

with open('index.html', 'r') as f:
    html = f.read()

# Add imports
html = html.replace("import { createGame } from './src/mob-swarm.js';", "import { createGame } from './src/mob-swarm.js';\n  import { createAudio } from './lib/anchor-audio.js';\n  import { createControls } from './lib/anchor-ui.js';")

# Instantiate audio and ui
injection = """
  const audio = createAudio();
  
  let loop;
"""
html = html.replace("let loop;", injection)

# Wire up ui
ui_injection = """
  loop = new AnchorLoop({
"""
html = html.replace("loop = new AnchorLoop({", "const ui = createControls({ stage, loop: { togglePause: () => loop && loop.togglePause(), state: State.START }, audio });\n  loop = new AnchorLoop({")

# Make onState call sync
state_injection = """onState: (next, prev) => { 
      ui.loop.state = next;
      ui.sync();
      if (next === State.LEVEL_CLEAR) { setTimeout(() => loop.start(), 1500); } 
    }"""
html = re.sub(r'onState: \(next, prev\) => \{ if \(next === State\.LEVEL_CLEAR\) \{ setTimeout\(\(\) => loop\.start\(\), 1500\); \} \}', state_injection, html)

with open('index.html', 'w') as f:
    f.write(html)
