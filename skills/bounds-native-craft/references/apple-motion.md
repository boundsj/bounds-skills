# Apple motion

## Decide whether it moves

- Name the purpose before writing an animation: feedback, spatial continuity, a state change, or explanation. With no purpose, do not animate.
- The more often people see it, the less it should move. Interactions repeated many times a session get a near-instant response or the system default. Save expressive motion for rare moments.
- Motion is never the only carrier of information; pair it with a state change people can read, and with haptics or sound where they fit.

## Springs over curves

Use a spring for anything a finger touches or anything that can be interrupted. Springs settle from their current value and velocity, so retargeting stays continuous. A fixed-duration curve restarts.

- SwiftUI: `.spring(duration:bounce:)`, or the presets `.smooth` (no bounce), `.snappy` (a little), and `.bouncy` (more). `.spring(response:dampingFraction:)` takes the designer-facing pair; `.interpolatingSpring(mass:stiffness:damping:)` takes physical parameters.
- Default to no bounce. Apple's *Designing Fluid Interfaces* (WWDC 2018) recommends starting at 100% damping and adding a little bounce (its example uses 80%) only when the gesture carried momentum, such as a flicked card or thrown sheet. A menu that simply appeared should not overshoot.
- Working starting points, adapted from Emil Kowalski's MIT-licensed `apple-design` skill rather than published by Apple: damping 1.0 with response 0.4 s to reposition; damping 0.8 with response 0.3 s for a flicked drawer or sheet. Tune them on a device.
- Keep curves for motion nothing can interrupt, such as a linear progress fill. Do not use ease-in for entrances; it delays the moment people are watching.

## SwiftUI approaches

- Put `withAnimation` around the state change in the event handler; the callback is synchronous so the animation starts on the same frame. Use `.animation(_:value:)` to scope an implicit animation to one value. Never use the value-less form.
- Insertions and removals use `.transition` (`.opacity`, `.move(edge:)`, `.scale`, `.push(from:)`, `.blurReplace`, or `.asymmetric`). The change must happen inside an animation, and the container must persist.
- Use `contentTransition(.numericText())` for changing numbers and `symbolEffect` for symbols, sparingly.
- `phaseAnimator` and `keyframeAnimator` play scripted sequences. Keep them for moments nobody needs to interrupt.
- Remove animation from one change with `.transaction { $0.animation = nil }`.
- UIKit: `UIViewPropertyAnimator` for interruptible, scrubbable work; `UIView.animate` for fire-and-forget changes.

## Matched geometry and navigation

- `matchedGeometryEffect(id:in:)` with a `@Namespace` moves one element between two layouts in the same hierarchy. Only one view per ID may be the source at a time; swap both states inside one `withAnimation`.
- For a push or sheet that grows from its source, use `navigationTransition(.zoom(sourceID:in:))` on the destination and `matchedTransitionSource(id:in:)` on the source (iOS 18 and later). The system makes it interactive.
- Keep paths symmetric: a view leaves the way it came and grows from the control that opened it.

## Interruptible transitions

- Never disable input until an animation finishes. A second tap, drag, or Back must retarget from the on-screen value.
- Avoid chains of completion handlers that cannot be cancelled. If a step must follow, use `withAnimation(_:completionCriteria:_:completion:)` and check that the state still calls for it.

## Reduce Motion

Read `accessibilityReduceMotion` in SwiftUI or `UIAccessibility.isReduceMotionEnabled` in UIKit. The HIG's adjustments:

- Tighten springs to remove bounce.
- Let motion track gestures directly.
- Avoid animating depth changes along the z-axis.
- Replace x, y, and z movement with fades.
- Avoid animating into and out of blurs.

Keep opacity and color changes that explain state. System navigation adapts on its own; custom transitions must check the setting.

## Frame pacing

- At 120 Hz a frame has about 8 ms; at 60 Hz about 16 ms. Keep `body` cheap and animate transforms and opacity (`offset`, `scaleEffect`, `opacity`) rather than changes that relayout large hierarchies.
- `drawingGroup()` can flatten complex vector drawing. Profile first.
- Custom display-link work sets `preferredFrameRateRange`. On iPhone, rates above 60 Hz for custom animation need the `CADisableMinimumFrameDurationOnPhone` Info.plist key; check Apple's ProMotion documentation for what it covers.
- Measure hitches with Instruments (Animation Hitches, SwiftUI, Time Profiler) on a release build on a device. Simulator frame rates are not evidence.
- To review choreography, use slowed playback where the Simulator or Xcode's device tools offer it, or step through a screen recording frame by frame. That is presentation evidence only; judge feel on hardware, including an older supported device.
