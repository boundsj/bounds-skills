---
name: bounds-modernize
description: "Reassess and update a stale, conflicting, duplicated, or inherited PR. Use for modernizing, rebasing, or taking over existing work while preserving contributor credit."
license: MIT
---

# Bounds modernize

Reassess the idea before updating its branch. A clean rebase does not prove that the PR still belongs.

## Establish intent and current state

Read the request, PR body, linked issues, commits, review threads, and complete diff, including later corrections or handoff records. Record URL, state, author, head repository/branch/SHA, actual base, checks, and reviews. Treat the handoff as context, not proof. Preserve unrelated local edits; use a separate worktree if needed, and do not delete this job’s worktree or branch during the job.

Fetch the remote PR head and base; record the original merge-base and observed remote head. Inspect base changes since divergence and relevant merged/open PRs. Check whether the problem is already solved, APIs or ownership changed, or the old implementation would restore removed behavior or duplicate a newer path. Age alone is not evidence.

## Give a verdict

- **MODERNIZE:** the goal and implementation still fit. Update against the current base.
- **REWORK:** the goal remains useful but needs a different implementation. Explain the smallest credible rewrite. Continue when the request authorizes that rework; otherwise present the concrete proposal for Jesse’s decision.
- **CLOSE:** the work is superseded, obsolete, or no longer worth its cost. Cite evidence and stop updating it. Closing requires Jesse’s explicit ask.

## Update the continuation

Bring branches up to date by rebasing onto the PR’s actual base by default; no merge commits from base unless Jesse asks.

Force-pushing is allowed when appropriate. Prefer `--force-with-lease=<branch>:<observed-head-sha>` after rebase. Never force-push shared/default branches without Jesse’s say-so. On lease failure, fetch and reassess.

Resolve conflicts using current intent and newer invariants. Reconsider the verdict when conflicts expose product or architecture disagreements. Changing the base or expanding scope needs authorization.

For a takeover, honor an explicit in-place, replacement, or stacked continuation. Otherwise update the existing PR when authorized; if branch access is unavailable, prepare a replacement from the original commits and link the source. Preserve Git authorship and co-author trailers, add fixes separately, and credit original contributors in the PR description. Use verified identities from commits/git config; never guess emails. If squash merging is later authorized, preserve human credit in that commit too.

Compare pre/post series with `git range-diff` and inspect the final diff for lost intent or revived obsolete behavior. Run focused repository checks and verify the original workflow. Use `bounds-review` for consequential changes and `bounds-ship` when the requested finish includes PR readiness; report unavailable skills.

Report verdict, base changes, conceptual conflicts, updates, preserved credit, proof/gaps, PR link, and remaining decisions. Merging, closing, and deleting each require Jesse’s explicit ask. Do not infer one from another.
