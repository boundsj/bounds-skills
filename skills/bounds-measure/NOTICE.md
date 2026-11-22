# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`792440e8a560a4a3f63748cdee70491ecd412982`:
- `benchmark-checklist` and `principle-explain-the-number`: https://github.com/cursor/plugins/tree/792440e8a560a4a3f63748cdee70491ecd412982/pstack/skills
- The harness-vetting parts of the `hillclimb` and `eval` playbooks in `poteto-mode`: https://github.com/cursor/plugins/tree/792440e8a560a4a3f63748cdee70491ecd412982/pstack/skills/poteto-mode/playbooks

Retains the claim written before running, the seven questions (limiter, tuning,
limits, errors, repeatability, relevance, and whether the work happened),
alternating runs with median and range, the one-run ballpark exception, the
verdict-first report with an inconclusive rule, one primary number in a PR, a
harness proven sensitive and frozen with error and work counts, and the eval
blinding and transcript-over-self-report rules.

Adds a denominator check, sections for evals, backtests and studies, disk
space, and usage telemetry, estimate-versus-measurement labeling, and a
statement that measuring grants no authority to change or publish. Removes the
hillclimb improvement loop, decision log, fixed model choices, the arena
dependency, Cursor transcript paths, sibling-skill and playbook references,
and explicit-only metadata.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt).
