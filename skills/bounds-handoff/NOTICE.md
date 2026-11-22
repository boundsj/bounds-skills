# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Matt Pocock's MIT-licensed skills, revision
`abeeaf95660ba9e8b7c753eb38f441ca707a8823`:
- `handoff` (`skills/productivity/handoff`) with its documentation (`docs/productivity/handoff.md`),
  and `claude-handoff` (`skills/in-progress/claude-handoff`): https://github.com/mattpocock/skills/tree/abeeaf95660ba9e8b7c753eb38f441ca707a8823

Selected source: Lauren Tan's MIT-licensed pstack, revision
`792440e8a560a4a3f63748cdee70491ecd412982`:
- `poteto-mode` playbooks `pause-safely` and `session-pickup`: https://github.com/cursor/plugins/tree/792440e8a560a4a3f63748cdee70491ecd412982/pstack/skills/poteto-mode/playbooks

Retains a note written outside the workspace for the stated next task,
references to artifacts instead of copies, redaction, suggested skills, a safe
stop that starts nothing new, file-based launch text instead of shell
interpolation, downgrading unverified beliefs, and a receiver that resumes from
the trail instead of redoing it while checking inherited claims. Adds leaving
the working tree untouched with a recorded HEAD, status, and diff hash plus an
optional backup patch; verified versus unverified claims with revision and
command; the findings ledger; live delegated work, CI, and watches recorded so
the receiver checks them instead of starting duplicates; host-native launch
only on request; and drift checks at pickup. Removes the `wip:` commit,
cancelling nested subagents, the fixed CLI launch command, Cursor transcript
paths, and explicit-only metadata.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt).
