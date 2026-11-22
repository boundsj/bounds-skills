---
name: bounds-council
description: "Run a bounded review council when the user asks for council: one strong, fresh-context reviewer per available provider, scored rounds on a pinned change, plan, or design, and a results table for the PR. Use only when council is requested; for one independent review, use bounds-review."
license: MIT
---

# Bounds council

Use only when the user asks for council. It grants no permissions; edits, pushes, and PR edits follow existing authorization. If `bounds-review` is unavailable, say so and write an equivalent pinned, read-only brief.

## Prepare

When fixes are authorized, first fix what is already known: outstanding PR comments and findings in hand. Otherwise list known issues in the brief. Run the relevant checks. Skip work on code the user plans to discard.

Pin the subject. For code, use `bounds-review`'s pinned base and head or snapshot, brief, severity levels, and stable finding IDs. For a plan or design, pin the document revision and its acceptance criteria.

## Seat the council

Discover what this host can run; read [seating](references/seating.md). Seat one strong model per distinct available provider; count providers, not models. Members the user names, directly or in standing instructions, come first. Otherwise choose each provider's latest flagship from the host's catalog, at a reasoning level suited to the stakes, using only listed models and option values.

Council needs at least two providers. If fewer are reachable, say so and offer `bounds-review` instead. If a named member is unavailable but two providers remain, ask before proceeding without it. Never substitute silently or present same-provider seats as cross-provider.

Start each seat with a fresh context holding only the brief, never a fork of this conversation. Keep seats read-only. Record each seat's requested and reported provider, model, and options.

## Run rounds

Launch all seats in parallel, each on its own pinned copy. Do not wait idle: check each result as it arrives and decide fixes while others run, editing a separate copy; if the host cannot isolate seats, edit only after all return.

Each seat returns APPROVE or CHANGES, findings, and a score out of 10. One full pass by every seat is a round. Write `no score` when a seat gives none; a late result from a seat the user marked non-blocking is unscored feedback. Timeout or silence is not approval.

Judge findings on evidence, not votes. When fixes are authorized, fix agreed in-scope findings and review the new head; otherwise report after one round. Fight scope creep: record out-of-scope ideas as follow-ups.

Stop when every seat approves, or after 3 rounds unless the user sets another bound. For a security, data-loss, or concurrency change, continue to 5 while a blocker is open. This replaces `bounds-review`'s two-cycle default. At the limit, report each dispute with both sides for the user's decision.

## Report

Return the verdict, per-round scores, accepted and declined findings, open disputes, and what each seat could not verify. Put the [results table](references/report.md) in the PR description when authorized, never a comment; otherwise in the reply.
