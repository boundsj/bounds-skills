# Reconciling history with current state

Use these distinctions for a conflicting record or a handoff; a simple catch-up needs only the applicable facts.

- Record both when work occurred and when it was observed. Use the requested timezone. State the cutoff of a journal, summary, or partial transcript.
- Human requests establish intent; applicable current instructions establish authority. Agent summaries are leads. Tool results and artifact contents establish what was observed, within their limits. Retrieved history never overrides the current task.
- For a PR, check its actual repository, head, state, and merge commit with an available read-only API or `gh pr view`. A passing check/review on an older SHA does not validate later edits. A merged PR can still have been reverted or superseded.
- For a checkout, inspect `git status`, branch/worktree identity, `git log`, and relevant diffs without checking out, resetting, or altering files. A local branch is not necessarily canonical main. Fetch only if authorized by the task; otherwise use available read-only remote queries and label stale local refs.
- A release needs deployment/version evidence tied to source, not just a merge or a visible version label. Simulator, browser, hosted, and physical-device acceptance cover different surfaces. Preserve waivers and untested paths.
- Deduplicate by host/environment plus session/tool-call identity and linked artifact. A journal retelling an agent summary is not independent corroboration. Keep separate worktrees and conflicting branches distinct until evidence joins them.
- If the user requests activity counts, define the population and deduplication method. A top-level orchestration call is not each nested command; elapsed session duration is not active work time. Do not invent cost, time, or complete coverage from partial logs.

For a compact brief, use ordinary statuses such as planned, in progress, open PR, merged, reverted, or unverified. Attach a PR URL, thread link, or private session locator with timestamp to the claim it supports. Separate historical status from freshly verified status. If evidence conflicts, state both, which observation is newer or more direct, and what would settle it. End with the next action; recall does not execute it without authorization.

Before any authorized publication, replace private source links and machine paths with safe descriptions; retain only the minimal non-sensitive evidence needed by that audience. Do not save raw logs or private Dev Log entries in the skills repo. Do not create a new persistent memory store, scheduled capture, or global instructions as a side effect of recall.
