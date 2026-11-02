# visionOS

Values come from Apple's Human Interface Guidelines (HIG). A simulator shows layout; comfort, targeting, and fatigue are judged only on a device.

## Choose the container

- **Window** for familiar, UI-centric tasks. It defaults to 1280×720 pt, about two meters away. Keep its glass background; removing it hurts legibility.
- **Volume** (`windowStyle(.volumetric)`) for bounded 3D content viewed from any angle. Content beyond its bounds is clipped; size it with `defaultSize(width:height:depth:in:)`.
- **Immersive space** (`ImmersiveSpace`) only for moments that benefit from it. A Full Space hides other apps. Styles are `mixed` (blends with passthrough), `progressive` (Digital Crown adjusts, by default across 120° to 360°), and `full` (replaces passthrough).
- Prefer launching in the Shared Space or `mixed` style. Let people choose when to go deeper, with an exit control that says whether it returns to a window or quits. Never require the Digital Crown to leave.
- `progressive` and `full` establish a boundary about 1.5 m from the starting head position. Do not require walking; bring objects to people.

## Windows and ornaments

- Shape a window's initial size to its content. Set minimum and maximum sizes so layouts never collide or sprawl, and keep content horizontally centered when large.
- Avoid opening extra windows by default. Keep depth inside windows shallow; real 3D belongs in a volume.
- Toolbars and tab bars become ornaments automatically; place items with toolbar placements such as `.bottomOrnament`. Use `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)` only for custom ones.
- Keep ornaments few, no wider than their window, and visible unless people are absorbed in media. A volume should prefer one extra ornament, not on the toolbar's edge.

## Glass, color, and materials

- visionOS has no separate Dark Mode; glass adapts to what is behind it. Prefer translucency to opaque fills. Use `glassBackgroundEffect()` when custom content needs glass backing.
- Use the vibrant label hierarchy: primary for text, secondary for supporting text, tertiary only for inactive items.
- Use color sparingly on glass, and prefer it on bold text and large areas. Keep brightness balanced in immersive scenes.

## Targets and hover

- Meet the platform minimum per the HIG: buttons need a 60×60 pt hit region. The HIG's control sizes are 60×60 pt by default and 28×28 pt at minimum; go smaller than the default only for dense secondary controls. Space them so centers are at least 60 pt apart, or leave 16 pt around each.
- Prefer rounded shapes; eyes drift toward corners. Give a compound control one containing shape the system can highlight.
- System controls highlight when looked at. Custom SwiftUI views add `hoverEffect()`, shaped with `contentShape(.hoverEffect, _:)`.
- RealityKit entities need `InputTargetComponent` and `CollisionComponent` to receive input, and `HoverEffectComponent` to highlight.
- Gaze stays private: apps learn where someone looked only when they tap, and custom hover effects render outside the app's process. Never design logic that depends on gaze.
- Avoid revealing content next to what people are looking at; the movement pulls their eyes away from it. Hover can still add information, such as a tooltip below a button, after a slightly longer delay. Custom hover effects can appear with no delay (the default), a short delay, or a longer one.

## Depth and z-offset

- Use depth for hierarchy: a sheet comes forward as its window recedes. Spend it on large, important elements; refocusing between depths tires people.
- Do not lift text off its background.
- `offset(z:)` and `frame(depth:)` place SwiftUI content in depth. Keep offsets small and purposeful.
- Points are angular. Windows default to dynamic scale, so they read the same size at any distance. Volumes default to fixed scale, which suits objects that must match real-world size. For interactive volume content the HIG generally favors dynamic scale, set with `defaultWorldScaling(.dynamic)` in visionOS 2 and later.

## Ergonomics and placement

- Apps open in front of people. Keep important content centered and anchored in space, never locked to the head.
- Place content for sustained reading at least a meter away.
- Design for a seated, still person. Direct touch with raised arms tires quickly; keep it occasional.
- Avoid motion in the periphery, sustained oscillation (especially near 0.2 Hz), and rotating the world. Fade an object out and back in rather than flying it across the room. Large moving objects get more translucency or lower contrast.

## Eye and hand input

- Indirect input (look, then pinch) is the default for UI. Direct touch suits close objects and occasional use. Support both where possible.
- `SpatialTapGesture`, `DragGesture`, and the other standard gestures work on views and, through targeted gestures, on entities.
- Custom gestures must be discoverable, distinct, and never the only path. For gestures that need several fingers or both hands, consider also offering one that takes less movement. Do not conflict with the system's hand gesture for overlays.

## Evidence

Also record seated or standing, immersion style, window placement, and session length.
