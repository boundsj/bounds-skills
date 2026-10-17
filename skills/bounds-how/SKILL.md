---
name: bounds-how
description: "Explain how existing code, a subsystem, or a change works, from entrypoint through data and state to boundaries and outcome, sized to the reader's purpose. Use for walkthroughs, onboarding, and where-does-this-live questions, not for historical rationale."
license: MIT
---

# Bounds how

Give the reader a working model they can act on. Explaining is read-only.

## Size it

Read from the conversation why they are asking: changing it, reviewing it, debugging it, or new to it. Put depth where the question is and skip what they know. If scope is unclear, state your interpretation and proceed. Trace a narrow question yourself. For a subsystem spanning services or clients, split it into a few independent angles; parallel read-only explorers help only when delegation is available and permitted, and you reconcile their findings against the code.

## Trace

Follow the real path, not names that suggest one:

- **Entrypoint:** the action, request, job, or event, and where it lands.
- **Data and state:** what flows, what is persisted or cached, and who owns each piece.
- **Boundaries:** process, network, thread, client and server, storage, and third-party crossings, with the contract at each.
- **Outcome and failure:** what the caller sees, plus error, timeout, cancellation, and retry paths.
- **Anchors:** `file:line` or a symbol for each step.

Say what you could not trace. Keep observed behavior separate from hypotheses about why it is shaped that way; label rationale a hypothesis, or offer to investigate its history.

## Explain

Answer in a sentence or two first. Name the thing in general terms, then tie it to this codebase. Walk the flow in prose with concrete actors: "the upload handler writes the manifest, then the worker reads it", not "the service delegates". Explain the problem each part solves; a list of functions is reference, not explanation.

Draw a diagram only when three or more parts interact and the host renders it: a newcomer gets a short series adding one part at a time, an expert one compact diagram. Close with a file map and gotchas when they help someone start work. Then offer the next layer instead of covering everything. Use plain words and one name per concept.
