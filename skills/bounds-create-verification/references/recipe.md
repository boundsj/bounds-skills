# Project-local recipe shape

Use this as an authoring outline, not content to paste with blanks. Keep the result as small as the project allows. If writing a local skill, include valid `name` and `description` frontmatter for the actual provider.

## Launch

State the repository working directory, exact build/setup and launch commands, prerequisites, and readiness check. Use per-run data/profile paths and an available port where needed. Record owned process IDs or handles. If an existing shared instance is the only option, describe its ownership and avoid conflicting drivers or destructive data.

## Doctor

Provide the read-only command or inspection that establishes the expected build and usable state. Check the instance being driven, not just any process on a port. Run before the first Drive and after a failed or surprising action. Reset or relaunch an owned instance if healthy infrastructure masks invalid UI state.

## Drive

Use real commands, routes, accessible UI names, or device selectors from the project. Name inputs and expected output or side effects. Cover persistence or error behavior when it matters. A test double is useful only with its boundary and proof limitation stated. For a dry-run, observe what it actually writes or sends before relying on it as isolation.

## Evidence

Save a concise record: date, host/platform, relevant tool versions, base/head or current revision and dirty files, commands with exit status, observed assertions, feature coverage, and artifacts. Redact sensitive data before capture or sharing. Keep screenshots/logs outside runtime directories that Cleanup removes; keep private artifacts out of version control.

## Cleanup

Stop only processes started by this run and remove only its disposable fixtures. Avoid broad process-name kills and global resets. Run cleanup on failure as well as success, then check that evidence is still readable.

## Feature map

One table is enough until details justify per-feature files:

| Feature / user entrypoint | Prerequisites | Drive and expected observation | Status / evidence |
| --- | --- | --- | --- |
| Name a real behavior | Required state | Exact action and independent expectation | Executed at revision, source-only, blocked, or untested |

Keep run results distinct from the maintained recipe. “Blocked” includes the attempted route and missing prerequisite. An untested feature must not inherit another feature's passing status. When commands, routes, or prerequisites change, update the recipe and rerun affected paths.
