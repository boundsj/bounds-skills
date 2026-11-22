# Handoff note template

Use these sections in order. Omit a section only when it has nothing to say, and write "none" where its absence matters to the receiver (for example, no live jobs). Keep it short enough to read in one pass; link anything longer.

```markdown
# Handoff: <task in a few words>

Written: <date, time, timezone> by <host, provider, model when known>
For: <what the next session should do>

## Goal and acceptance
<the user's goal, the pass/fail checks that define done, and what is excluded>

## Decisions and constraints
- <accepted decision or constraint> (source: <user message, PR, plan>)
- <later corrections win; note revoked or narrowed permissions>

## Repository state
- Root and worktree: <path>
- Branch and HEAD: <branch> at <full SHA>; upstream <ref>, ahead <n>, behind <n>
- Status: <git status --porcelain summary>; untracked: <paths>
- Uncommitted diff: SHA-256 <hash> of the full diff below; backup patch: <path or none>
- Builds or tests at HEAD plus local edits: <known passing, known broken, or unknown>

## Verified
| Claim | Revision | Command or evidence | Result |
| --- | --- | --- | --- |

## Unverified
- <belief, assumption, or report not checked, and how to check it>

## Findings ledger
| ID | Severity | Status | Evidence | Response |
| --- | --- | --- | --- | --- |

## Live work
| Kind | Identifier | Where | Status at writing | Receiver should |
| --- | --- | --- | --- | --- |
<delegated tasks, CI runs, PR watches, deploys, dev servers, scheduled jobs>

## Next action
<one concrete first step and how to tell it worked>

## Suggested skills
- <skill>: <why the receiver needs it>

## Artifacts
- <plans, specs, PRs, commits, logs, recipes by path, URL, or SHA>

## Avoid
- <failed approaches and dead ends, each with the reason>
```

Build the uncommitted diff through a temporary index so untracked files are included and the real index is untouched; ignored files stay out. Check untracked file sizes first, and list large files instead of patching them:

```sh
index="$(mktemp -d)/index"
GIT_INDEX_FILE="$index" git add -A
GIT_INDEX_FILE="$index" git diff --cached --binary --no-ext-diff --no-textconv HEAD > <backup patch path>
shasum -a 256 <backup patch path>
```

At pickup, rebuild the diff the same way but pipe it straight to `shasum -a 256` instead of writing a file. Never write to the backup patch path again; it holds the state at handoff.

Before saving, reread the note as the receiver. Remove secrets, tokens, credentials, personal details, and raw transcript excerpts. Replace copied artifact content with a pointer. Check that every "verified" row names a revision, and move anything without one to "Unverified".
