# Motion

Decide whether something should move before deciding how. Often the right amount of motion is none. Use the project's existing easing and duration tokens; add new ones only as tokens.

## Whether to animate

| How often a person sees it | Decision |
| --- | --- |
| Hundreds of times a day, or triggered from the keyboard | No animation |
| Tens of times a day (hover, list navigation, frequent toggles) | None, or a barely perceptible fade |
| Occasionally (dialogs, drawers, toasts) | Standard motion |
| Rarely (first run, completion, empty states) | Room for expressive motion |

Then name the purpose: **feedback** (the press registered), **spatial continuity** (where something came from or went), **state change** (something switched), **bridging** (content would otherwise jump), or **explanation** (onboarding or marketing). No nameable purpose means no animation. Data people are reading or acting on should not move for style.

## Easing and duration

- Entering and exiting: ease-out, which starts fast and responds at once. Moving or morphing on screen: ease-in-out. Color and hover: `ease`. Progress and marquees: `linear`. Avoid ease-in for UI; it delays the moment people are watching.
- The CSS keywords are weak. Stronger curves, as tokens: `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)`, `--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1)`, and for sheets `--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1)`.

| Element | Duration |
| --- | --- |
| Press feedback | 100–160ms |
| Tooltips, small popovers | 125–200ms |
| Dropdowns, selects | 150–250ms |
| Centered dialogs | 200–300ms |
| Drawers, sheets, full-screen dialogs | Up to about 500ms |

Most UI transitions run about 150–300ms, press feedback and tooltips can be quicker, and large surfaces such as drawers, sheets, and full-screen dialogs can take up to about 500ms. Marketing and explanatory motion can run longer.

## Springs

Use springs for drags, flicks, and anything a user can grab mid-motion. They have no fixed duration and carry velocity into the next target. Default to no overshoot (bounce 0, or damping ratio 1). Add a little bounce, about 0.1 to 0.3, only when the gesture itself had momentum, such as a flicked sheet. At release, pass the pointer's velocity into the spring so dragging and settling have no seam.

## Interruptibility

- CSS transitions retarget from the current value; keyframe animations restart. Use transitions or springs for anything that can be triggered twice quickly: toggles, toasts, expanding rows.
- Start any new animation from the element's current on-screen value, not its logical target, and never block input while motion plays.

## Enter, exit, and origin

- Never enter from `scale(0)`. Start at `scale(0.95)` to `scale(0.97)` with `opacity: 0`.
- Popovers, menus, and tooltips scale from their trigger: set `transform-origin` toward the anchor. Many headless libraries expose the computed origin as a CSS variable. Centered dialogs keep a centered origin.
- Leave the way you came: a toast that rises from the bottom exits downward.
- Exits can be shorter than entrances. Where the user is deciding (hold to confirm), the deliberate phase is slow and the release is fast.
- `@starting-style` animates entry without JavaScript where supported.

## Stagger

Stagger groups by 30–80ms per item, cap the total, and never block interaction while it plays. Do not stagger lists people reload all day.

## Reduced motion

Under `prefers-reduced-motion: reduce`, replace movement, scaling, and parallax with short opacity changes. Keep feedback; remove travel. Ship this with the animation, not later. Gate hover motion behind `(hover: hover) and (pointer: fine)`.

## Removing motion

When an interface feels slow, delete animation on keyboard actions and high-frequency surfaces, scroll reveals on every section, entrance motion on data, and loops on persistent elements. Before deleting, check for:

- start states left behind, such as `opacity: 0` waiting for an animation that no longer runs;
- code waiting on `transitionend`, `animationend`, exit callbacks, or timers sized to a duration;
- focus that moved only after the animation finished;
- layout jumps the animation was hiding;
- tests that wait for animation classes.

## Reviewing motion

- Play it at 2 to 5 times its duration, or step through it in the DevTools animations panel. Check the origin, that properties stay in sync, and that crossfades do not show two overlapping objects.
- Trigger it rapidly to test interruption, and test gestures on a real touch device.
- Review again later with fresh eyes. Motion personality (crisp or playful) is the human's call.
- Report what you watched: browser, device, refresh rate if known, reduced-motion setting, and playback speed. A transition that compiled has not been seen.
