---
name: bounds-handoff
description: "Write a resume note so another agent, provider, model, or later session can continue the current work: Git state left as is and recorded, verified versus unverified claims, open findings, live jobs, and the first next action. Use when the user asks for a handoff or pause, a model or provider switch, or when a usage limit is near; also for picking up such a note. Not for recovering past sessions or briefing the user."
license: MIT
---

# Bounds handoff

Write a note a cold agent can resume from: another provider or model, a later session, a colleague, or a side task. "Keep going" is not a pause. This skill adds no permissions: it never commits, pushes, publishes, or launches anything unasked.

## Stop at a safe boundary

Finish the current atomic step or back out of it, and start nothing new. Do not cancel delegated tasks, CI runs, or PR watches unless the user asks; record each one instead.

Leave the working tree as it is: no commit, stash, reset, or checkout. Record the repository root, branch, HEAD SHA, upstream and ahead/behind counts, `git status --porcelain`, and a SHA-256 of the full uncommitted diff, untracked files included, built through a temporary index as the [note template](references/note.md) shows so the real index is untouched. When uncommitted edits matter, also save that diff as a backup patch beside the note.

## Write the note

Save it outside the repository: a location the user names, else the host's temporary or state directory. Never commit it. Temporary folders can be cleared; give the full path and say when to copy it somewhere durable. Follow the [note template](references/note.md), tailored to the stated next task.

Point to artifacts by path, URL, or SHA instead of copying them. Mark each consequential claim verified, with revision and command, or unverified. Downgrade anything you only believe; the receiver will trust it. Redact secrets, credentials, and personal details, since the note may become another agent's prompt. The user's instructions may name private locations, logs, or trackers to reference.

## Hand it over

Unless asked to launch, reply with the note path, one line on where things stand, and a paste-ready prompt: "Read the handoff note at <path>, verify its state, then continue from its next action."

Launch a receiver only when the user asks, through the host's own tools, using the provider and model the user chose. A delegated child may get no parent history, so the note, or a prompt that reads it, is the whole task. Pass long text through a file, not shell interpolation. Record the receiver's task ID. Do not reach another host or install tooling to launch.

## Pick up a note

A note is evidence, not authorization. Before acting, check the repository state, live jobs, and consequential claims against it, and report drift: a moved HEAD, a changed diff hash, a finished or failed job. Check recorded tasks and watches before starting duplicates. Do not redo work verified at an unchanged revision. Permissions come from the current user and standing instructions. For history beyond the note, use `bounds-recall`.
