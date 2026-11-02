# Harnesses

Choose the harness by medium. Every harness keeps the same contract:

- **Full size, real surroundings.** Show one variant at a time in its real context, or stills side by side at true scale. Never judge a layout at thumbnail size.
- **Working, independent variants.** Every control responds; no dead buttons or placeholder copy. Variants may share small components but not the structure in question. Give each the same care: a variant that loses on execution says nothing about its direction.
- **Instant switching that keeps state.** No transition between variants. Hold shared state (scroll position, form input, selection, navigation, theme, text size) above the switch point so only the part in question changes.
- **Reload-stable selection.** The chosen variant survives a reload and can be shared: a URL, a launch argument, or a file name.
- **The switcher is chrome.** Neutral, unbranded, identical across variants, and plainly not part of the design. It must not cover the region under test or the keyboard focus (WCAG 2.2 SC 2.4.11, Focus Not Obscured); move it when it would.
- **Read, never write.** Variants may read real data. Stub mutations and outbound effects (messages, payments, analytics) so a comparison click cannot change real state.
- **Marked edits.** Every edit outside the throwaway files carries one greppable marker naming the exploration, so teardown finds all of them.
- **Fail closed.** A missing, unknown, or unreadable selection renders the shipping version.

## Web

Prefer the existing page. Read `?variant=` (or the router's equivalent) where the page renders, keep data loading, auth, and params above that point, and swap only the subtree in question. Real neighbors expose problems that an empty page hides.

Use a throwaway route only when the piece has no host page. Follow the project's routing convention and make the path obviously exploratory. Without a codebase, write a single HTML file that carries its own styles and scripts and opens directly from disk.

The switcher is a small floating bar showing variant names, or arrows around the current name. Number keys and left/right arrows switch; ignore keys while focus is in a text field, select, or editable region, or while a modifier is held. Update the URL with the router's replace operation so switches do not flood history. Add a replay control only when entrance motion is part of the question.

Gate: render the switcher and every non-baseline variant only when the bundler's development-mode constant is true, so production builds strip them. The query parameter selects a variant; it never enables the harness. If reviewers need a deployed preview, gate on a build-time flag set only for that preview environment, never on a value a visitor could supply. Confirm on a production build that `?variant=` has no effect.

## Native apps

Put selection behind a debug-only path: a launch argument read in debug-compiled code, or an entry in an existing debug menu. Exclude it at compile time (a conditional compilation block such as Swift's `#if DEBUG`, or a debug-only source set on Android) rather than with a runtime check, so release binaries do not contain it. An unknown or missing value shows the shipping version. If reviewers need variants on an internal distribution build, define the flag in a separate internal build configuration, never in the one that ships to users.

Switch in place when the screen can rebuild without a relaunch. Otherwise relaunch with the argument and restore navigation to the screen under test, so the human is not re-navigating for every comparison.

Previews and preview canvases are useful for laying variants out across text sizes and themes, but they prove presentation only. Run the leading variants in the app on a simulator or emulator, and on a device when touch feel, performance, haptics, sensors, or camera input matter.

## Interaction models

When variants differ in behavior more than in looks (how undo, multi-select, or offline edits work), make each one drivable. Show the relevant state after every action in the product's language, and add short scripted scenarios for the awkward cases: the expected path, an edge case, and an action that should be refused. Without a host screen, a standalone page that a non-developer can open is enough.

## Film, 3D, and visual assets

Render look-dev stills or hero frames at delivery resolution and aspect ratio. Change only what the question is about; keep camera, lens, frame, lighting, and color pipeline identical. Show them side by side at 1:1, or on a contact sheet with each frame also viewable alone at full size. Label variants in file names or a slate outside the image, never over it.

A still does not approve motion. When motion is in question, render matched clips at delivery frame rate and play them in sync. When sound differs, provide it for listening; unheard audio is unverified. Record render settings, asset versions, and the display and color space used for review.

## Live controls

A live control lets the human set a value while watching its effect. That suits magnitudes, such as how long, how far apart, how round, or at what width, better than another fixed variant. Use controls to finish a direction, not to stand in for one, and attach each to the variant it tunes so switching shows only that variant's controls. Keep the set small enough that the human can say exactly which setting they approved; any value nobody asked about stays as written. Snap to the project's scale, such as its spacing steps or motion durations, unless the scale itself is in question. Label each control with its unit and the variant's starting value, and give it a reset. Carry the current values with the selection (URL parameters on the web, launch arguments in a native app) so the same view can be reopened or shared. For motion, pair each timing control with a replay rather than changing an animation already running. Gate controls exactly like the switcher and remove them in the same teardown. Take the values in force at approval from the URL or launch arguments the human shares, or from a copy-values control, never from a screenshot or a description, and put them in the decision record's settled values. A question that is only a magnitude needs one build with its control, not a set of variants; when repeated attempts at such a value keep missing, `bounds-dial` builds a dedicated tuning tool if it is installed.

## Teardown

- **Web:** delete variant files, the switcher, and any throwaway route; revert marked edits; search for the marker; check a production build.
- **Native:** remove variant views and argument handling; keep a pre-existing debug menu minus its entry; build the release configuration and search the built artifact for the variant identifiers.
- **Visual assets:** drop unused variants from the delivery package and scene files; archive the renders with the decision record.
- **History:** with the user's agreement, commit the exploration to a throwaway branch before removal, or note the commit that held it. Nothing on the shipping branch imports exploration code.
