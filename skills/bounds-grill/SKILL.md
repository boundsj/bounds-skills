---
name: bounds-grill
description: "Question the user in short rounds about a product idea, plan, or design until its decisions are explicit and nothing rests on a silent assumption, ending with a confirmed summary of what is decided and what remains. Use when the user asks to be grilled, or to stress-test whether an idea is worth building or a plan is sound; not for writing the plan, designing code, or implementing."
license: MIT
---

# Bounds grill

Question the user in rounds until every decision is explicit and nothing rests on a silent assumption. Grilling grants no authority to implement, write files, or publish.

## Mode

- **Idea:** whether a product, feature, or tool is worth building, and what to test first. Read [idea evidence](references/idea-evidence.md).
- **Plan or design:** how a chosen thing will be shaped and delivered. Read [plan tree](references/plan-tree.md).

Read the mode's reference before the first round. Infer the mode from the request; ask only when both fit.

## Prepare

Privately frame how an expert would approach this, what raw material they would start from, and what outside check would show the result is right. Let that shape the questions without narrating it.

Look up facts yourself and cite the source; only questions that depend on a pending lookup wait. Decisions, taste, and the user's own experience belong to the user.

## Rounds

The frontier is every open question whose prerequisites are settled.

1. Ask at most three numbered questions, choosing first those that unblock the most later decisions.
2. Recommend an answer to each. Word a decision so "yes" accepts it. For a question of fact or past experience, describe what a useful answer would contain; never invent the user's experience.
3. Record each answer as decided, deferred, or an open assumption, then recompute the frontier.

When several answers or failed approaches rest on one unstated belief, write it down and make it the next question.

## Stop

No fixed question cap. After about five rounds, ask whether to continue. End when the frontier is empty, the remaining questions wait on an outside test, or the user stops; say which.

In idea mode, evidence comes first. Until something shows that someone has the problem and would change what they do, don't move to later concerns. Offer the cheapest way to get that evidence, or record that the user chooses to proceed anyway, as on a personal or exploratory project.

## Close

Write the closing summary from the mode's reference, keeping user decisions, verified facts, and open assumptions distinct. Take no action until the user confirms it. Confirmation covers the summary as written, not implementation.

Name the next step where one fits:

- `bounds-plan` to turn the decisions into scope, acceptance checks, and slices.
- `bounds-architect` to settle state, interfaces, or module shape that would be costly to undo.
- `bounds-options` to compare an open visual or interaction direction as built variants.

If the named skill is absent, say so and describe the step.
