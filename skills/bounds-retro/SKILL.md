---
name: bounds-retro
description: "Examine a bounded set of accessible engineering work for repeated corrections and wasted effort, then propose evidence-backed improvements to structure, checks, tooling, or navigation."
license: MIT
---

# Bounds retro

Improve the environment the next run works in, so the user corrects less. This is not a code review or a memory system.

## Set the boundary

Use the work the user names: a session, T3 thread, delegated review, PR, or branch. Default to the current conversation, diff, and check results. For a named past session, read its own record; [sources](references/sources.md) covers host logs. State the boundary and missing evidence. Do not search unrelated histories. If compaction removed the middle of the current session, say so and suggest a retro pointed at its log.

## Find the cost

Human attention is the primary signal: user messages that correct, re-ask, repeat a constraint, or unblock; reviewer findings the implementer should have caught; early stops that left a closable gap. Then look for slow navigation, expensive or repeated tool calls, retries, misleading checks, and missing information.

When work spanned providers, models, or delegated reviewers, attribute each moment to its agent. The fix may belong in a review brief or host setting rather than the repository.

Every candidate must trace to a specific turn, command, or finding; discard untraceable advice. Separate repeated patterns from single incidents. A smooth session may have nothing worth changing.

## Choose where the fix lands

Inspect existing check commands, hooks, and CI first. Then prefer the cheapest durable mechanism:

1. Structure that removes the mistake: one owner, clear interfaces, fewer competing paths.
2. A deterministic check for a mechanical violation. Repair or wire an existing check before adding one. No guardrail at all is itself a finding.
3. Reviewer-read standards for a judgement call. Review has the least context pressure; keep standards out of always-loaded instructions.
4. A navigation pointer from an already-read file for slow discovery; wider access, such as a teed log, for missing information; a streamlined tool for expensive calls.
5. A short standing instruction only for what nothing above can carry. Keep `AGENTS.md`/`CLAUDE.md` mostly to pointers; flag no-ops and misplaced steering for removal.

## Report

Rank by cost to the user's attention, not loudness. For each: moment → cause → change and where it lands → how to validate. Keep each a short, phone-readable block; return few unless asked. Mark deletions. Say what one retro cannot judge, such as whether an older rule blocks good work. Invent no time savings.

## Act

Propose by default. Implement only when already authorized, within the identified project. Prove a new check fails on a representative mistake and accepts valid work before it blocks merges. Provider and host changes are proposals for the user. Do not edit global instructions, add hooks, install skills, publish histories, or create tracker tasks merely because they might help.
