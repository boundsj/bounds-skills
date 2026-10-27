# Pinned, bounded review

For committed work, record base ref, resolved base SHA, merge-base when used, head SHA, diff command, requirements source, and checks already run. Review only the agreed change and enough surrounding code to assess its effects.

For local edits, capture `git diff --binary HEAD` and the relevant untracked files without staging or altering the user's tree. Store a manifest of included paths and content hashes beside the snapshot. Exclude secrets, ignored runtime state, and unrelated files. If a stable snapshot cannot be made, label the review as a moving working-tree inspection and recheck before a final verdict.

## Delegation

Discover the session's native or app-owned capabilities. Inherit the user's provider/model settings unless they specify otherwise; never guess model slugs, launch another host, or install tooling to manufacture independence. For a required cross-provider review, select a provider distinct from the implementer. Verify returned provider/model/options; no silent model swaps. If the requested selection cannot run, report the mismatch. No delegation tool means a local review with an explicit coverage limit, not independent approval.

Give a reviewer a bounded read-only brief:

```text
Review only. Do not edit, commit, push, publish comments, or start subagents.
Intent and acceptance: <brief plus accessible source>
Scope: <repository, base SHA, head SHA, exact diff command>
Local snapshot, if any: <path and identity>
Relevant conventions: <paths>
Evidence already available: <commands/results with revision>
Constraints and exclusions: <scope and access limits>
Return APPROVE or CHANGES for this head, with stable finding IDs, severity,
file/line, trigger, consequence, evidence, and verification limits.
blocker: broken intended case or critical safety failure.
should: concrete in-scope defect. nit: optional improvement.
Distinguish preferences and uncertainty; say what you could not verify.
```

Keep the task identifier and obtain its result through that host's supported tools. For a new review round, provide the original brief, new head, prior findings, responses, and unresolved objections. Follow the host's task lifecycle; a backing conversation is not automatically a reusable delegated task.

Reproduce or inspect each finding before accepting it. After relevant changes, old results remain evidence for the old revision. Refresh the affected checks and review; record what was not rerun. Do not loop for cosmetic consensus or claim a second opinion from a self-review.

## Findings and completion

Keep a ledger of ID, severity, evidence, response, and status: open, fixed pending verification, resolved, disputed, or declined with reason. Carry IDs across rounds; do not renumber recurring findings. Evaluate severity yourself: a rare but severe safety failure is not automatically a nit. Resolve or decline findings on evidence, not consensus. Record actual provider/model/options and usage only when exposed.

Do not edit the scoped change while its reviewer runs. Keep its task ID. A timeout, error, silence, or exhausted budget never counts as approval. Inspect task status before retrying; cancel and verify a failed/stuck task has stopped before starting its replacement. Do not duplicate active reviews. Follow host lifecycle and waiting tools.

When fixes are authorized, use at most two fix/review cycles unless the user sets another bound. Later briefs include the original acceptance contract, new head, delta, ledger, responses, and unresolved objections. Focus on changed code and open IDs. Approval covers only the reviewed revision; explicitly identify unreviewed changes. At the limit, report both sides of disputes and unresolved blockers for the user’s decision.

## No-reviewer packet

If no independent reviewer can start, return a paste-ready packet using the brief above: intent/acceptance, accessible requirements and conventions, pinned base/head or snapshot identity, exact diff command, relevant artifacts, executed checks with revision/results, exclusions, ledger, and requested reviewer selection. Include the startup failure or missing capability and label independence unfulfilled. Do not call a self-review independent approval.
