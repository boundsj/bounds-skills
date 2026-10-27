---
name: bounds-ship
description: "Carry an authorized change to proof, cross-provider review, green required CI, and a PR handoff. Use when asked to ship or finish through PR readiness; merge requires Jesse’s explicit instruction."
license: MIT
---

# Bounds ship

Take an authorized change to its agreed finish line. Use `bounds-mode` for task coordination, `bounds-review` for review mechanics, and `bounds-ketchup` for a requested progress briefing; discover them by name and report missing skills. This skill grants no extra permissions.

## Agree the finish

Recover the goal, acceptance checks, exclusions, and authorized external actions from the request. Resolve material gaps while continuing independent work. If deployment makes sense but the request does not say whether it is intended, ask. If deployment makes no sense here, omit it entirely. A deploy needs authorization and its own acceptance evidence.

Inspect the branch, local edits, and existing PR before changing anything. Preserve unrelated work. Use a task branch. If an existing PR could merge automatically, disable auto-merge/remove it from the queue when authorized; otherwise stop before pushing and report the blocker.

## Finish and prove

Complete the smallest coherent change and run the repository’s required checks. Observe direct evidence for the intended behavior: reproduce a fix, exercise a workflow, or inspect the running UI where applicable. Record commands/results and gaps against the exact commit; green mocks alone do not prove a user workflow.

Get one independent cross-provider review of the final commit under `bounds-review`. Discover capabilities; do not silently substitute providers/models. If unavailable, provide its review packet and report blocked review. Fix real findings within the bounded protocol. Recheck and review any changed head before claiming readiness.

## File and follow through

Reuse the branch’s PR or open one against the intended base. Lead with the problem and resulting behavior, include proof and coverage limits, and identify the verified model/harness. Check public text for private details. Use `bounds-leaving-pr-comments` for authorized replies; filing a PR does not authorize unsolicited comments.

Handle current CI and review findings. Use the host’s PR watcher when available; the owning thread watches and unwatches before handoff. Without one, report pending state and the monitoring gap. Force-push when appropriate, preferably `--force-with-lease` pinned to the observed remote head; never force-push shared/default branches without Jesse’s say-so. Reassess a failed lease.

## Handoff gate

Re-fetch and check the live head/base, required CI, completed reviews, unresolved requests, and mergeability. Readiness requires proof and cross-provider review on that head, green required CI, an up-to-date mergeable branch, and no unresolved actionable findings. Separate missing human approval from technical blockers.

Report PR URL, final SHA, evidence, review outcome, risks, and exactly what Jesse must accept. Leave it open and unmerged. Merge only on Jesse’s explicit word pinned to the reviewed SHA; revalidate the gate immediately beforehand, without protection bypasses. Never enable automatic merging without that authorization.
