# Changelog

## [v18.1.0] (MS2-BUGFIX-UI-LAYERING)
- Target the HUD Container: Built a clean `#ui-overlay` DOM container over the game layer to properly hold the Level text and HP bar.
- Strip Opaque Backgrounds: Stripped out the solid maroon `roundRect` opponent base from the Canvas 2D engine that was obstructing the 3D track perspective.
- Fix Positioning & Layering (Z-Index): Placed the `#tilt` 3D perspective track under a `z-index: 1`, and anchored the new `#ui-overlay` over it with `z-index: 10` and absolute positioning.
- Pointer Events: Applied `pointer-events: none;` on the `#ui-overlay` and all its children so touch swipes pass directly down to the Anchor framework's trackpad layer without interference.
- Alignment: Anchored "LEVEL 1 / 100" and the Boss/Base HP bar cleanly to the top corners of the DOM UI using flexbox.
