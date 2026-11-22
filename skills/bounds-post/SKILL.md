---
name: bounds-post
description: "Draft a public blog post from material the user names, such as work notes, a development log entry, a merged PR, or a lesson learned, in the user's voice, with every claim checked against its source and private details removed. Use when asked to write or outline a post from the user's own work; not for tightening an existing draft (use bounds-unslop) and never for publishing."
license: MIT
---

# Bounds post

Turn the user's own material into one public draft they edit and publish. Never publish, post, schedule, commit, or send it anywhere.

## Gather

Use only sources the user names or their instructions point to: notes, log entries, PRs, a shipped change, earlier posts for voice, and the site's conventions. Read them in full; do not search unnamed private records. Note what each source can prove. For third parties, use only sourced public statements.

Follow the user's stated voice, style, and template; otherwise write plain first person in short paragraphs, with no em dashes.

## Pick the post

Settle three things before drafting, from the material or with one short question:

- **One idea:** the single claim the post makes. Park other ideas as future posts.
- **The reader:** what they already know, so each concept is introduced before a paragraph leans on it.
- **The proof:** the concrete example that shows the idea, and the honest limit: what failed, what was not measured, or where the idea does not apply.

If the angle is open, offer two or three openings implying different claims for the user to pick; otherwise pick one and say why.

## Draft

Read [shaping](references/shaping.md) for grounding and format choices. Outline in a few lines, then write. Open on the problem or the moment, not background. Give each paragraph one job; cut any paragraph whose removal breaks nothing. Use the real command, number, or error text when it is public. End on something the reader can do or check, not a summary. If a needed example is missing, ask for one or cut the section; never invent one.

## Check every claim

List each fact, number, quote, date, and sequence of events in the draft with its source. Mark each verified, narrowed to match the source, or unverifiable, and cut or flag the unverifiable ones. Never round a number in the flattering direction or turn a tentative result into a finding. Quote only verbatim text from a source the user can share.

## Remove private details

Run [the privacy pass](references/privacy.md) over everything you return, including title options and the claims list; describe private sources there briefly instead of giving a path or link. Generalize or remove what a reasonable person would keep private; when unsure, generalize and ask. List every change so the user can restore what they choose to share. Anything the user's standing instructions mark private stays out unless they explicitly ask for it in this task.

## Return

Return the draft as Markdown, then four short lists: claims checked, privacy changes, open questions, and two or three title options. Write a file only where the user asks.
