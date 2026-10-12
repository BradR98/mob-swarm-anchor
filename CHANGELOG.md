# Changelog

## [v18.1.1] (MS2-BUGFIX-RENDER-PIPELINE)
- Target the Logical Canvas: Stripped the `#tilt` wrapper and directly targeted the `#game` canvas.
- Apply 3D Transforms to Canvas: Shifted the `perspective` and `rotateX` CSS transformations directly onto the active `<canvas id="game">` element.
- Centering & Alignment: Applied `left: 50%; transform: translateX(-50%)` inline with the 3D transforms to perfectly center the skewed canvas inside the viewport stage.
- Remove Debug Backgrounds: Removed the hardcoded `#0b1020` and `#242a40` letterbox background fills from `mob-swarm.js`'s Canvas 2D render loop, swapping them for `clearRect()`. The game field now correctly utilizes CSS transparency.
- Input Rail Calibration: Verified that `AnchorInput` is bound to the flat `#stage` wrapper rather than the transformed `<canvas>`, bypassing `getBoundingClientRect()` distortion completely and guaranteeing 1:1 logical input tracking.


## [v18.1.0] (MS2-BUGFIX-UI-LAYERING)
- Target the HUD Container: Built a clean `#ui-overlay` DOM container over the game layer to properly hold the Level text and HP bar.
- Strip Opaque Backgrounds: Stripped out the solid maroon `roundRect` opponent base from the Canvas 2D engine that was obstructing the 3D track perspective.
- Fix Positioning & Layering (Z-Index): Placed the `#tilt` 3D perspective track under a `z-index: 1`, and anchored the new `#ui-overlay` over it with `z-index: 10` and absolute positioning.
- Pointer Events: Applied `pointer-events: none;` on the `#ui-overlay` and all its children so touch swipes pass directly down to the Anchor framework's trackpad layer without interference.
- Alignment: Anchored "LEVEL 1 / 100" and the Boss/Base HP bar cleanly to the top corners of the DOM UI using flexbox.
