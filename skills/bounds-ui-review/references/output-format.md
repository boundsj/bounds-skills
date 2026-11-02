# Output format

Lead with the verdict. Keep every list heading and write "None." when a list is empty, so the reader knows it was considered. Give findings stable IDs and keep them across rounds; never renumber a finding that recurs.

## Verdict

- **Ship:** no open blocking or should-fix items; remaining device checks confirm expectations rather than chase a suspicion; open decisions do not block release.
- **Ship after fixes:** the design holds, and the named fixes are needed first.
- **Rethink:** the approach fails its job in a way fixes will not repair. Examples: the core task is unreachable by keyboard or screen reader by design, the hierarchy works against the screen's purpose, or the states the product needs have nowhere to go. Rethink is a recommendation; the direction is the user's call.

A verdict covers only what the approval scope says. Ship from source reading is not ship from a device.

## Template

```markdown
**Verdict: <ship | ship after fixes | rethink>.** <One or two sentences: the reason and the item that matters most.>

### Reviewed
- Change: <PR, branch, commit, or build number>; screens and flows: <list>
- Observed on: <device model and OS | simulator or emulator and OS | browser, engine, and version | source only>
- Geometry, measured in the running build: <viewport or window size, container widths, scale factor, safe-area insets, orientation>
- Theme, text size, input: <light or dark, text size setting, touch, pointer, keyboard, controller, screen reader>
- Data: <real account | staging | fixture or demo, presentation only | worst-case toggle>
- Lenses applied: <list>. Skipped: <lens: reason>
- Standards: <bounds-web-craft | bounds-native-craft | WCAG 2.2 AA | Apple HIG | Material 3 | project design rules at path>

### Fixable in source
| ID | Severity | Location | What breaks, for whom, when | Fix | Evidence |
| --- | --- | --- | --- | --- | --- |

### Check on real hardware or services
| ID | Check to run | Passes when |
| --- | --- | --- |

### Your call
| ID | Decision | Options and consequences | Recommendation |
| --- | --- | --- | --- |

### Held up
- <What was tried and handled well, so nobody "fixes" it>

### Approval scope
- Covers: <screens, flows, states, and settings reviewed>
- On evidence: <device, simulator, browser, fixture, or source, per area>
- Does not cover: <code correctness, other screens or platforms, release build, real network, untested settings, unheard audio, unfelt haptics>

Fixes are not applied. Name the IDs to fix.
```

## Filled example

A settings screen that lists connected accounts, reviewed in a browser.

**Verdict: ship after fixes.** The layout holds with normal data, but long emails push the remove button off the row on narrow screens, and that button has no accessible name.

### Reviewed
- Change: commit `4e1b9c0`; Settings, Connected accounts list and remove flow
- Observed on: Chromium-based browser on desktop; responsive mode is not a phone
- Geometry, measured: list container 352 CSS px at a 390 CSS px viewport; 1180 CSS px at desktop width; device pixel ratio 2
- Theme, text size, input: light and dark; 100% and 200% zoom; pointer and keyboard; no screen reader run
- Data: fixture data (presentation only) and the worst-case toggle
- Lenses applied: interaction, accessibility criteria, worst-case content, fit and reflow, states, leftovers. Skipped: motion (nothing animates), hierarchy (existing layout unchanged)
- Standards: WCAG 2.2 AA; project components in `src/ui/`

### Fixable in source
| ID | Severity | Location | What breaks, for whom, when | Fix | Evidence |
| --- | --- | --- | --- | --- | --- |
| UI-1 | Blocking | `src/settings/AccountRow.tsx:41` | Icon-only remove button has no accessible name; screen reader users hear only "button" and cannot tell which account it removes | Label it with the action and the account, such as "Remove sam+receipts-2026@example.org" | Source |
| UI-2 | Blocking | `src/settings/AccountRow.tsx:18` | A long email cannot shrink or break; at the measured 352 px container the remove button leaves the row and cannot be clicked | Let the text column shrink and break long addresses; keep the button's size fixed | Browser, worst-case toggle |
| UI-3 | Nit | `src/settings/AccountList.tsx:9` | Heading reads "1 accounts" | Use the project's plural helper | Browser, fixture |

### Check on real hardware or services
| ID | Check to run | Passes when |
| --- | --- | --- |
| D-1 | On a phone with the screen reader on and the largest text size, open Connected accounts and move through one row | Each row reads the account name, the email, then "Remove <email>, button"; nothing clips |
| D-2 | On a real network, remove an account, then drop the connection during the request | An inline error offers retry; the row stays and is not shown as removed |

### Your call
| ID | Decision | Options and consequences | Recommendation |
| --- | --- | --- | --- |
| H-1 | Long emails: wrap or truncate in the middle? | Wrap: the full address is always visible, row heights vary. Middle truncation: rows stay even, the full address appears only on the detail screen. | Wrap; the email is what identifies the account |

### Held up
- The empty state exists and offers "Connect an account".
- Focus returns to the list after the remove dialog closes.
- Contrast passes in both themes for text, the remove icon, and the focus indicator.

### Approval scope
- Covers: the Connected accounts list, its empty and error states, and the remove flow at the listed widths and zoom levels.
- On evidence: browser at measured geometry with fixture and worst-case data; source for labels.
- Does not cover: real phones, screen reader output, real network failure, other settings screens, code correctness of the remove request.

Fixes are not applied. Name the IDs to fix.

## Stress-test addendum

Add after the verdict when a stress test was run:

```markdown
### Stress-test harness
- Toggle: <where it is and how to switch>; states: <normal, worst case, empty, one, many>
- Gate: <debug-only mechanism>; release build checked: <how, or "not checked">
- Values used: <field: value, for the values that broke something>
- Not tried: <catalog rows skipped and why>
- Files added: <paths>. Existing files edited: <paths and what changed>
- Keep the harness? <Default is removal. Say "keep" to retain it, debug-only, as regression data> | <Removed: the files above are deleted and the edits reverted> | <Kept at your request, debug-only>
```

## After authorized fixes

Report each fixed ID with the change made and the recheck: same screens, same evidence pin, every toggle state including normal data. Mark observations from before the fix as belonging to the earlier revision, and list anything not rechecked.
