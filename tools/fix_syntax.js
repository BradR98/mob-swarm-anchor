const fs = require('fs');
let code = fs.readFileSync('src/mob-swarm.js', 'utf8');

// Replace these blocks with empty lines
code = code.replace(/\/\/ addEventListener\('click', function \(\) \{\n\s*initAudio\(\);\n\s*muted = !muted;\n\s*try \{ localStorage\.setItem\('mobswarm_muted', muted \? '1' : '0'\); \} catch \(_\) \{\}\n\s*syncMuteBtn\(\);\n\s*\}\);/g, '');

code = code.replace(/\/\/ addEventListener\('pointerdown', function \(e\) \{\n\s*initAudio\(\);\n\s*dragging = true;\n\s*targetX = pointerToLogicalX\(e\);\n\s*try \{ hudCanvas\.setPointerCapture\(e\.pointerId\); \} catch \(_\) \{\}\n\s*e\.preventDefault\(\);\n\s*\}\);/g, '');

code = code.replace(/\/\/ addEventListener\('pointermove', function \(e\) \{\n\s*if \(dragging \|\| e\.pointerType === 'mouse'\) targetX = pointerToLogicalX\(e\);\n\s*e\.preventDefault\(\);\n\s*\}\);/g, '');

code = code.replace(/\['pointerdown', 'touchmove', 'keydown'\].forEach\(function \(ev\) \{ \/\/ addEventListener\(ev, function \(e\) \{ e\.stopPropagation\(\); \}\); \}\);/g, '');

fs.writeFileSync('src/mob-swarm.js', code);
