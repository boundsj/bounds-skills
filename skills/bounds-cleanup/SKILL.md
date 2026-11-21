---
name: bounds-cleanup
description: "Reclaim disk space without losing work: measure what uses space, propose deletions by category with gates for uncommitted, unpushed, in-use, and open-PR work, delete only what the user approves, and report measured space freed. Use when the user asks to free disk space or clean up worktrees, build output, simulators, or caches."
license: MIT
---

# Bounds cleanup

Free disk space without losing work. Measuring is read-only; each deletion category needs the user's approval. The user's instructions may name their own cleanup tool, script, or protected folders: inspect a named tool before running it and prefer it where it fits.

## Measure first

Record free space on each affected volume, and agree the scope: volumes, folders, repositories. Size the largest items per category with read-only commands, within scope. Read [reclaimers](references/reclaimers.md) for per-tool measuring and removal commands.

- **Git worktrees:** paths from `git worktree list --porcelain`, never hand-typed.
- **Build output:** project build folders, compiler caches, test artifacts.
- **IDE data:** derived data, indexes, device support files.
- **Simulators and emulators:** test clones, unavailable devices, old runtimes.
- **Package and tool caches:** package managers and toolchains.
- **Containers and VMs:** images, volumes, build cache.

Tools disagree on sizes; say how each number was measured.

## Gate each candidate

Hold back, with a reason, anything that:

- has uncommitted or untracked work, ignored files that are not build output (such as `.env` files or local databases), or commits on no remote, including a detached HEAD's; show what would be lost;
- backs an open PR or a branch still in use; ancestry checks miss squash merges, so check PR state;
- is the main worktree, this session's own, or in use by a process, editor, dev server, or another agent session;
- holds secrets, credentials, or user data, or sits outside the agreed scope;
- is kept on purpose, such as a pinned toolchain, an offline cache, or a worktree marked `locked`.

Script buckets are advice, not permission; the user's list of active work overrides them.

## Propose, then delete

Present each category with estimated space, item count, risk, rebuild cost, and the exact commands. Wait for the user's OK; approval for one category does not cover another. Ask again when something new appears.

Use the owning tool's removal command: `git worktree remove` then `git worktree prune`, the platform simulator tool, the package manager's cache command, the container tool's prune. Prefer its dry-run first. Use `rm` only for leftovers inside an approved path, never on a path built from unchecked variables. Keep branch refs unless their deletion was approved. Removing a detached worktree deletes its HEAD reflog, so first create a branch for any local commits, with the user's OK.

## Report

Give free space before and after, measured space freed against the estimate, what was removed per category, what was held back and why, and rebuild costs the user will pay. If freed space has not appeared yet, such as space held by snapshots, say so rather than claim an unmeasured number.
