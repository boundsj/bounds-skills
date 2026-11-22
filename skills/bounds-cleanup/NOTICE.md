# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`792440e8a560a4a3f63748cdee70491ecd412982`:
- `poteto-mode` playbook `worktree-cleanup` and its `scripts/worktree-audit.sh`, with the
  principles that playbook cites (`principle-build-the-lever`, `principle-prove-it-works`,
  `principle-encode-lessons-in-structure`): https://github.com/cursor/plugins/tree/792440e8a560a4a3f63748cdee70491ecd412982/pstack/skills

Retains free space recorded before and after, worktree paths read from
`git worktree list` rather than typed, classification by size, merge state,
uncommitted work, and PR state, script buckets as advice rather than
permission, the user's set of active work winning over a suggestion, a pause on
uncommitted work, `git worktree remove` followed by prune, simulator and cache
reclaimers, and a reply with space reclaimed and a reason for each item held
back. Adds an agreed scope and per-category approval, categories beyond
worktrees (build output, IDE data, emulators, package caches, containers),
gates for unpushed commits, squash-merged branches, running processes, secrets,
and user data, owning-tool removal with dry runs, measured versus estimated
reporting, and user-named tools. Removes the bundled audit script, Cursor
transcript and application-state paths, subagent fan-out, and autonomous
deletion of clean merged worktrees.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt).
