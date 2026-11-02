# Apple interaction

Sizes come from Apple's Human Interface Guidelines (HIG). Momentum projection and velocity handoff follow Apple's *Designing Fluid Interfaces* (WWDC 2018). The rubber-band function is a common approximation, not an Apple-published formula, adapted from Emil Kowalski's MIT-licensed `apple-design` skill.

## Targets

Meet the platform minimum per the HIG. Its Buttons guidance gives a hit region of at least 44×44 pt on iOS and iPadOS, and 60×60 pt on visionOS. Its accessibility guidance lists control sizes per platform:

| Platform | Default control size | Minimum control size |
| --- | --- | --- |
| iOS, iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |
| visionOS | 60×60 pt | 28×28 pt |

- Treat the default size as the target. Go smaller only for dense secondary controls, and never below the minimum.
- Leave about 12 pt around bezeled controls and 24 pt around the visible edges of borderless ones.
- Grow the hit area, not the artwork: pad the control and set `contentShape`, or set a minimum frame. Hit areas must not overlap.

## Press response

- Show the pressed state on touch-down and commit on touch-up inside, so dragging off cancels. `Button` does this; a custom look belongs in a `ButtonStyle` using `isPressed`.
- Do not build buttons from `onTapGesture`. It loses press state, the button trait, and keyboard activation.

## Gestures and direct manipulation

- Use standard gestures for standard actions. Add custom gestures only for frequent, specialized work, and keep a visible button, menu item, or shortcut for the same action.
- Track the finger 1:1 from where it grabbed, not from the view's center. Hold transient drag state in `@GestureState` so it resets on cancel.
- `DragGesture` starts after 10 pt by default. Lower that only where no scroll view competes.
- Do not claim screen edges the system uses for Back, Home, or system overlays. `defersSystemGestures(on:)` is for games and immersive content.
- Pay the double-tap recognition delay only where double-tap exists.

## Interruption and velocity handoff

- Never lock input during an animation. A moving element must be catchable mid-flight, continuing from its on-screen position.
- SwiftUI springs replace each other with velocity preserved; in UIKit, `UIViewPropertyAnimator` can pause, scrub, and reverse.
- On release, carry the finger's velocity into the settle animation. Read it from `DragGesture.Value.velocity` or `UIPanGestureRecognizer.velocity(in:)`. APIs that want relative velocity, such as `UISpringTimingParameters(dampingRatio:initialVelocity:)`, expect `velocity / (target - current)`. Check each API's units.
- Decide commit or cancel from velocity direction and projected landing point, not release position. A quick flick should be enough.

## Momentum projection and rubber-banding

Project where a flick would come to rest, then snap to the nearest valid target from there:

```swift
func project(_ velocity: CGFloat, decelerationRate: CGFloat = 0.998) -> CGFloat {
    (velocity / 1000) * decelerationRate / (1 - decelerationRate)
}
```

0.998 matches `UIScrollView.DecelerationRate.normal`; 0.99 is `.fast`. Prefer a scroll view's own snapping (`scrollTargetBehavior`, paging) when the content scrolls anyway.

Past a boundary, resist progressively instead of stopping hard, then spring back on release:

```swift
func rubberBand(_ overshoot: CGFloat, dimension: CGFloat, constant: CGFloat = 0.55) -> CGFloat {
    (overshoot * dimension * constant) / (dimension + constant * abs(overshoot))
}
```

## Haptics

- Use system patterns for their documented meanings: notification (success, warning, error) for outcomes, impact (light through heavy, rigid, soft) for snaps and collisions, selection for stepping values.
- In SwiftUI use `sensoryFeedback(_:trigger:)`; in UIKit use the feedback generators, calling `prepare()` before latency-sensitive moments.
- Fire on the causal frame, match the visual's intensity, and keep to one per action. Never fire per frame or as the only feedback.
- On iOS only supported iPhone hardware plays haptics; a simulator plays none. Mac Force Touch trackpads offer alignment, level-change, and generic feedback.

## iPad pointer and keyboard

- System controls get pointer effects. For custom views, use `hoverEffect(.highlight)` for controls in a group and `.lift` for standalone ones. Shape the effect with `contentShape(.hoverEffect, _:)`, and keep adjacent bar hit regions contiguous.
- Give frequent commands `keyboardShortcut` and declare them through `commands` so they are discoverable. Avoid overriding system-defined shortcuts, and in general do not repurpose standard ones.
- Modifier keys must mean the same thing whether a drag starts by touch or pointer.

## Focus

- Drive text-field focus with `@FocusState`: advance on Return and dismiss the keyboard when the task ends. When a focused item disappears, move focus somewhere sensible.
- On iPadOS and macOS, Full Keyboard Access already reaches controls, so add focus support only for content elements such as list items, text fields, and search fields. `focusable()` alone does not make a custom control operable: give it `Button` semantics, or the right accessibility traits and actions.
- On macOS, a custom keyboard-driven control adds `focusable()` together with `onKeyPress` or `onMoveCommand`. For a button-like view, `focusable(interactions: .activate)` follows the convention of taking focus only when keyboard navigation is on.

## macOS conventions

- Expose every command in the menu bar with standard shortcuts, and preferences in a `Settings` scene.
- Context menus (`contextMenu`) and hover reveals (`onHover`) duplicate visible paths; they are never the only way to an action.
- Every function must work from keyboard and pointer alone.
