# Review lenses

Pick lenses from what the change touches, then work only those. Each lens says when it applies, what to check, and what evidence can settle it. Thresholds marked as standards come from the cited source. Values marked as working defaults are craft practice: a finding against one is a should fix or a nit, and a default never blocks a ship on its own.

## Picking

| The change | Usually needs |
| --- | --- |
| Copy or label edit | Worst-case content (length, translation), consistency |
| Restyle or token change | Accessibility criteria (contrast in every theme), consistency, fit and reflow |
| New control, gesture, or shortcut | Interaction across inputs, accessibility criteria, motion if it animates |
| New list, feed, table, or dashboard | States, worst-case content, fit and reflow |
| New screen or flow | Most lenses; hierarchy and subtraction matter most here |
| Animation or transition change | Motion, interaction (interrupting it), accessibility criteria (reduced motion) |
| Anything about to reach release users | Leftovers, always |

When unsure whether a lens applies, ask what a user on the least typical supported setup would hit. If nothing, skip it and say why.

## Interaction across inputs

Applies when anything a user can act on is added or changed. Check only the inputs the product supports, and say which those are.

- **Touch:** every action works without hover, and pressing gives feedback. Anything done by dragging can also be done with a single pointer and no drag, such as tapping arrow buttons (WCAG 2.5.7). Anything done with a multipoint or path-based gesture, such as a pinch or a swipe, can also be done with a single pointer and no path-based gesture, such as a tap or click (2.5.1). Both criteria exempt gestures that are essential. Controls near screen edges don't fight system gestures.
- **Pointer:** hover adds information but never holds the only route to an action. Hover effects appear only on devices that can hover; on web, gate them with the `(hover: hover)` media feature. Cursor and context-menu behavior match the platform.
- **Keyboard:** every action is reachable and operable (2.1.1) with no trap (2.1.2). When the sequence affects meaning or operation, focus moves through controls in an order that preserves both (2.4.3); in practice that usually tracks the visual reading order. The focus indicator is visible (2.4.7). A control that receives focus is never entirely covered by the product's own content, such as a sticky header, toast, or sheet (2.4.11, AA). Partial covering still passes AA; keeping the focused control fully visible is 2.4.12, which is AAA. So partial covering is never blocking: rate it should fix or nit by how much it hinders. Escape closes an overlay and focus returns to what opened it. Enter submits forms. Shortcuts that use only printable characters, with no modifier key, can be turned off, remapped, or limited to when their control has focus (2.1.4).
- **Game controller or directional focus:** every control is reachable by directional moves in a predictable order, with no dead ends. Focus is visible from viewing distance. Confirm and back behave the same everywhere. Nothing requires a pointer or simultaneous inputs without an alternative.
- **Screen reader:** each control exposes name, role, state, and value (4.1.2). Where the order of content carries meaning, the reading order exposed to assistive technology preserves that meaning (1.3.2). Images carry text alternatives or are hidden as decoration (1.1.1). Status changes such as "Saved" or result counts are announced without moving focus (4.1.3). Custom controls expose the same actions as their visual gestures. Test with the platform's reader: VoiceOver, TalkBack, Narrator, NVDA, or Orca.

Evidence: source can show a missing label or a hover-only control. Focus order, announcements, and gesture behavior need the running build with the input or assistive technology actually in use.

## Accessibility criteria

Applies to nearly every visible change. Check the published criteria for the platform under review; on the web, WCAG 2.2 level AA is the common target. Cite the criterion in each finding. A failed criterion is blocking when it stops a supported user from finishing an intended task or gives them a wrong result, and a should fix otherwise. AAA criteria and platform recommendations that go beyond a criterion never block on their own.

- **Text contrast:** 4.5:1 for normal text and 3:1 for large text (1.4.3), in every theme and in every state that recolors text. Text in inactive controls is exempt.
- **Non-text contrast (1.4.11):** the 3:1 ratio against adjacent colors covers only the visual information a person needs to identify a control or its current state, plus graphic parts needed to understand content. When a field is recognizable only by its border, that border needs 3:1; so do a checkbox's checked mark and the focus indicator. A text-only button with no border or fill needs no 3:1 boundary, because its text identifies it and 1.4.3 covers that text. Inactive controls are exempt.
- **Color alone** never carries meaning such as error, selection, or status (1.4.1).
- **Target size:** on the web, at least 24 by 24 CSS pixels unless a 2.5.8 exception applies, such as enough spacing from neighboring targets. On Apple platforms, the HIG gives a default and a minimum control size per platform: 44 and 28 points on iOS and iPadOS, 28 and 20 on macOS, 60 and 28 on visionOS. Below the default is a nit; below the minimum, should fix. Material and Android accessibility guidance give 48 by 48 dp.
- **Text size:** web text can be resized to 200% without losing content or function (1.4.4), and content reflows at a width of 320 CSS pixels without scrolling in two directions, apart from content such as data tables and maps that needs a two-dimensional layout (1.4.10). Native text follows the system text-size setting through its largest sizes: Dynamic Type, including the accessibility sizes, on iOS and iPadOS, and the largest font and display size on Android. macOS has no Dynamic Type; check whatever text sizing the app itself offers.
- **Content on hover or focus (1.4.13):** it can be dismissed without moving the pointer or focus, the pointer can move onto it without it vanishing, and it stays until the user dismisses it, moves away, or it stops being relevant.
- **Forms:** fields that need input have labels or instructions (3.3.2), tied to the field in code (1.3.1). When an input error is detected automatically, the field in error is identified and the error is described in text (3.3.1). The criterion does not say where that text appears; placing it next to the field is good practice, not a requirement.
- **Orientation** is not locked unless essential (1.3.4).
- **Flashing:** nothing flashes more than three times in any one second unless it stays below the flash thresholds (2.3.1).

Evidence: contrast can be computed from tokens and source. Text scaling, reader output, and real target sizes need rendering at the measured geometry.

## States

Applies when the change shows data, waits on anything, or needs a permission or account.

Walk each state the screen can reach: first load, refresh, empty on first run, empty after a filter or search, partial data, error, offline or slow network, permission not yet asked, permission denied, signed out or expired session, success, and disabled.

For each, check that the state exists, says what happened in plain words, and offers the next useful action: create the first item, clear the filter, retry, open settings. A loading placeholder matches the size of what it stands in for, so switching states does not shift the layout. An action already in progress cannot be started again. When a save fails, the user's input is still there.

Evidence: forcing a state in a fixture proves its presentation. Real behavior needs the real condition: throttled or dropped network, a revoked permission, an expired session, a fresh account.

## Worst-case content

Applies when the screen renders data, user text, counts, or translated copy. Check long and unbreakable strings, zero, one, and huge counts, missing optional fields, non-Latin and right-to-left text, emoji, and growth in translation: short strings can double or triple, and longer text grows about 30%. Each long string needs a deliberate truncate, wrap, or clamp choice. Values and the full method are in [worst-case data](worst-case-data.md).

## Fit and reflow

Applies whenever something visible changes size, position, or content.

- **Late arrivals:** content that loads after first paint does not push what the user is already reading. Images and embeds declare their dimensions up front, async regions hold their space, and late notices float over the page instead of being inserted above it. On the web, Cumulative Layout Shift quantifies this; web.dev treats 0.1 or lower as good.
- **Containment:** text and controls stay within their bounds. When text is cut short, the full value can still be reached by touch as well as pointer. Amounts, dates, and values people compare are never cut short.
- **System insets:** content and controls avoid notches, rounded display corners, status bars, home indicators, and the on-screen keyboard.
- **Size changes:** portrait and landscape, split view and multi-window, resized desktop windows, and folding devices. The user's state and scroll position survive each change.
- **In-place updates:** live counts, timers, and totals use tabular figures so digits don't wobble. When a status or button string swaps for a longer one, such as "Up to date" becoming "Syncing 3 of 120", size its slot for the longest version so nearby items stay where they were.

Evidence: requires rendering. Use the container width measured in the running build, then the narrowest and widest the product supports.

## Motion

Applies when anything animates, including changes to existing motion.

- **Purpose:** each animation shows cause and effect, keeps spatial context, signals a state change, or confirms input. Decoration on something used many times a day is a cost. Keyboard-driven and very frequent actions should respond at once, with little or no animation.
- **Duration and easing (working defaults):** most interface transitions run about 150–300 ms, and large surfaces such as drawers and sheets may run up to about 500 ms; exits run faster than entrances. Things entering or responding decelerate into place; an accelerating start makes the user wait at the moment they watch most closely. Elements grow from a slightly reduced size with a fade, not from zero, and popovers grow from their trigger. None of these is a standard, and none blocks a ship on its own.
- **Interruptibility:** a user can reverse or cancel mid-motion. Rapid repeat triggers retarget from the current position instead of restarting. Gesture-driven motion follows the finger and respects release velocity.
- **Reduced motion:** honors the system setting (web `prefers-reduced-motion`; Reduce Motion on Apple platforms; Remove animations on Android). Reduced means gentler, such as a fade instead of a slide, not the loss of feedback. Motion triggered by interaction can be turned off (2.3.3, AAA); motion that starts on its own, lasts more than five seconds, and runs beside other content can be paused, stopped, or hidden (2.2.2).
- **Smoothness:** on the web, animate transform and opacity rather than layout properties. Dropped frames are judged on a mid-range device, not a fast development machine.

Evidence: a still screenshot cannot show motion. Use the running build, ideally a slowed or frame-stepped recording. Frame drops and gesture feel need a device.

## Hierarchy and subtraction

Applies to new screens, flows, and redesigns.

- The primary action and the most important information are obvious at a glance; reading order matches importance.
- Take each element away in your head: a subtitle that repeats the title, a decorative image, a confirmation step for a reversible action, a status chip nobody acts on, a tooltip restating its label. If no task, warning, or state becomes harder to understand without it, it is a removal candidate.
- Button text names the result of pressing it: "Send invite" tells the user more than "Submit". Error text says what went wrong and how to recover.

Removing intentional content is a human decision: list it with the cost of keeping it. Only leftovers go straight to the fixable list.

## Consistency

Applies when the change adds or restyles components.

- Existing components are used rather than near-copies. Color, type, spacing, radius, elevation, and motion come from the project's tokens.
- The same job looks and behaves the same as elsewhere in the product: dialogs, toasts, empty states, destructive confirmations.
- Written design rules in the project are followed. Platform conventions for navigation, back behavior, and system controls are respected.

A divergence that might be deliberate goes to the human list, citing the existing pattern. Evidence: token use can be read from source; visual consistency needs side-by-side captures at the same geometry.

## Leftovers

Applies to anything about to reach users in a release. Look for anything built for development that a release user could see or reach:

- Developer tooling: inspectors, overlays, frame-rate meters, debug menus, and tuning panels.
- Stand-in content: filler copy, sample accounts, mock charts, and made-up figures or quotes on production screens.
- Test scaffolding: stress-test toggles and harness files, mocked responses, forced states, and preview-only code paths that run outside debug builds.
- Output written to the console or logs while the reviewed flows run.
- Interface code disabled by commenting it out, work-in-progress notes in visible text, and hardcoded local or staging addresses.

Severity follows the rubric in SKILL.md. A leftover is blocking when it presents invented content as real, or exposes personal data or developer-only controls that change data or access, whether on screen or in logs. A leftover that is only visible noise is a should fix.

Evidence: building or inspecting the release configuration is stronger than reading the condition that gates the code. Say which you did.
