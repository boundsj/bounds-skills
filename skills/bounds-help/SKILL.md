---
name: bounds-help
description: "Help the user choose among the Bounds skills available on this host, or word a useful prompt for one, without starting the work. Use for questions about which Bounds skill fits or how to ask for it."
license: MIT
---

# Bounds help

Answer which Bounds skill fits the user's need and give them a prompt they can send. Don't run the skill you suggest. A message that actually asks for work, such as "use the Bounds debug skill on this crash", is not a help question; handle it as the task it is.

## Read the current catalog

Use the skill list the host provides. If none is visible, read only the frontmatter of `bounds-*` skills installed beside this one. Recommend only skills you found, trusting their descriptions over memory. If the best fit is missing, say so; installing it is the user's choice. This host's catalog says nothing about other machines or providers. `bounds-mode` applies only when the user asks for it by name.

## Match the need

Infer the need from the conversation. If still unclear, ask one question with a few concrete options: understand code, design or plan, fix a failure, check a change, catch up, prove behavior, or tune how agents work for the user. Answer only the pick.

Recommend one skill, or two for a close call, with a sentence on the difference. Typical close calls, when both are installed: how code runs vs. why it is shaped that way; this conversation vs. earlier sessions; designing interfaces vs. scoping work; reviewing a diff vs. tracing effects beyond it; restating plainly vs. editing a draft.

## Word the prompt

Give at most one example prompt in a code block, using host invocation syntax only if you know it. A good prompt states the goal and a pass/fail done check, the proof to show (real output, screenshot, stored value), what the user already knows (symptom, repro, log), and real constraints ("don't change code yet", "zero behavior change"). Leave out step lists and guesses at the cause. Keep the reply short unless they asked for the whole catalog.
