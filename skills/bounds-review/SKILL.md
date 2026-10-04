---
name: bounds-review
description: "Review a pinned diff or change for correctness, requirement compliance, and maintainability, separating actionable findings from preferences and unverified assumptions."
license: MIT
---

# Bounds review

Resolve the requested base and head to commit SHAs before reviewing. For a branch or PR, record the merge-base and review `git diff <merge-base-sha> <head-sha>`; if the user requested a literal endpoint comparison, use that instead. Validate refs and note an empty diff. Infer the base from the PR or repository when clear; ask only if the choice changes the review materially.

For uncommitted work, capture the staged and unstaged diff plus relevant untracked files as a fixed snapshot outside the change. Record its identity and HEAD; do not pretend HEAD includes local edits. Read [review protocol](references/protocol.md) for snapshot details or delegated review.

Find the applicable request/spec and project conventions. If requirements are unavailable, state that limitation and still review the code. Check:

- **Correctness:** failing inputs, state transitions, error paths, compatibility, and tests that could miss a real defect.
- **Requirements:** missing behavior, unintended scope, and retained behavior at risk.
- **Maintainability:** concrete costs in the changed paths, judged against the project's conventions. Preferences are optional observations.

Use one independent reviewer for consequential changes when delegation is available and permitted by existing user and host instructions. Reuse authorization already granted; do not ask for it again. Add another only for consequential uncertainty or disputed findings. Discover capabilities and follow the linked protocol. Otherwise do a local review and label it accurately.

For each actionable finding, give priority, file/line, trigger, consequence, evidence, and a focused correction. Distinguish executed checks, source-based reasoning, and assumptions. Evaluate findings on their evidence rather than reviewer agreement. State “no actionable findings” when appropriate, with coverage limits.

A review request returns findings; it does not authorize edits or publishing comments. When fixes are authorized, rerun affected checks and review the changed head. Bound the process to two fix/review cycles unless the user specifies otherwise; report unresolved issues at the limit.
