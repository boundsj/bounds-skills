---
name: bounds-maintain-verification
description: "Refresh an existing project verification recipe and feature map after changes, distinguishing documentation drift, harness gaps, and product defects with honest live coverage."
license: MIT
---

# Bounds maintain verification

Locate the project's recipe and feature map from its instructions, docs, or local skills. If none exists, report that and use `bounds-create-verification` only if creation is authorized. If several targets are plausible, resolve from the task or ask which one matters.

Set the coverage boundary. For a changed feature, inspect and drive affected paths plus relevant neighbors. For an explicit full audit, cover every mapped feature. Check map entries against source, current commands, and recent changes; source inspection identifies candidates but is not live verification.

Follow the recipe's Launch, Doctor, Drive, Evidence, and Cleanup. Keep one owner for a shared runtime; independent source reading does not require parallel driving. Health-check before driving and after surprises. Reset invalid state when a healthy process is insufficient. Capture evidence outside disposable runtime state, clean failed attempts, and confirm artifacts survive final cleanup.

Classify discrepancies before editing:

- **Documentation drift:** commands or descriptions conflict with confirmed intended behavior. Correct the recipe/map and execute the correction.
- **Harness gap:** the product path works but available tooling cannot reach or observe it reliably. Repair within the recipe's tooling scope and re-drive, or report the limitation.
- **Product defect:** observed behavior violates requirements. Preserve the expected behavior in the map and report a reproducible finding. Do not redefine success to match a regression.

Default edits to the recipe, feature map, and their owned helpers. Product repairs require task authorization; when authorized, track and verify them separately. Retry a corrected failing step once, then report the unresolved blocker rather than looping.

Report **clean**, **changed**, or **blocked**, with per-feature executed, source-only, blocked, or untested status. “Clean” applies only to the stated coverage boundary. Partial corrections can accompany a blocked result. Include revision, commands/results, artifacts, and any untested corrections. Commit or open a PR only if requested or already authorized.
