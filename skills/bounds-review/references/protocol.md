# Pinned, bounded review

For committed work, record base ref, resolved base SHA, merge-base when used, head SHA, diff command, requirements source, and checks already run. Review only the agreed change and enough surrounding code to assess its effects.

For local edits, capture `git diff --binary HEAD` and the relevant untracked files without staging or altering the user's tree. Store a manifest of included paths and content hashes beside the snapshot. Exclude secrets, ignored runtime state, and unrelated files. If a stable snapshot cannot be made, label the review as a moving working-tree inspection and recheck before a final verdict.

## Delegation

Discover the session's native or app-owned capabilities. Inherit the user's provider/model settings unless they specify otherwise; never guess model slugs, launch another host, or install tooling to manufacture independence. No delegation tool means a local review with an explicit coverage limit.

Give a reviewer a bounded read-only brief:

```text
Review this change for actionable defects; do not edit or publish anything.
Intent and acceptance: <brief plus accessible source>
Scope: <repository, base SHA, head SHA, exact diff command>
Local snapshot, if any: <path and identity>
Relevant conventions: <paths>
Evidence already available: <commands/results with revision>
Constraints and exclusions: <scope and access limits>
Return prioritized findings with file/line, trigger, consequence, and evidence.
Distinguish preferences and uncertainty; say what you could not verify.
```

Keep the task identifier and obtain its result through that host's supported tools. For a new review round, provide the original brief, new head, prior findings, responses, and unresolved objections. Follow the host's task lifecycle; a backing conversation is not automatically a reusable delegated task.

Reproduce or inspect each finding before accepting it. After relevant changes, old results remain evidence for the old revision. Refresh the affected checks and review; record what was not rerun. Do not loop for cosmetic consensus or claim a second opinion from a self-review.
