---
name: bounds-ketchup
description: "Brief the user on what changed in the current conversation since their last substantive message: current state, evidence, blockers, decisions they own, and the next step. For earlier sessions or other threads, use recall instead."
license: MIT
---

# Bounds ketchup

Catch the user up on this conversation since the last substantive message they wrote. Assume they remember it and nothing after. Tool output, notifications, delegated results, this request, and nudges like "status?" don't count as their messages. Earlier sessions or other threads need cross-session recall; offer it rather than mining history here.

## Gather

Stay read-only: don't resume implementation, start jobs, post, or merge. Recheck what the conversation touched when a cheap read-only check exists: branch head, PR and checks, a delegated task, a running process. A finished parent turn can hide pending child work; a started process is not verified liveness. Mark what you could not recheck as unverified, with its last known time or revision.

Keep the distinctions that change the next move: implemented vs. verified, reviewed at an older revision vs. current head, merged vs. deployed vs. accepted, synthetic checks vs. real UI, device, or hosted proof. Check every number against its source.

## Reply

Phone-readable, usually under 150 words.

1. One line: how many things need the user, or that nothing does. If nothing changed and nothing waits, stop there.
2. One plain line per thing they asked for: what came of it, and whether it is done, running, failed, blocked, or unchecked. Each line must stay true read alone.
3. Action items: only decisions or access the user owns, such as a product choice, approval, irreversible step, or missing credential. Give your recommendation, why, and what happens without an answer. Include items still waiting from earlier. Never invent one.
4. At most one line on work you will continue.

Use names the user knows. Omit hashes, paths, and commands unless needed to act. Link only evidence that exists. Add a small diagram only for a relationship, such as a PR stack, and only if the host renders it.
