---
name: bounds-leaving-pr-comments
description: "Write attributed GitHub comments on Jesse’s behalf when posting is authorized: PR comments, inline reviews, replies, and issue comments. Does not itself authorize posting."
license: MIT
---

# Bounds leaving PR comments

Use this format for agent-authored GitHub comments posted on Jesse’s behalf. Posting still needs authorization from the request or an explicitly invoked workflow; preparing a comment does not authorize sending it.

Prefix the comment with:

```md
> [!NOTE]
> 🤖 **{model} writing on behalf of Jesse Bounds**

The actual reply starts here.
```

Replace `{model}` with the verified public model name that wrote the comment. If unavailable, use the harness name and do not guess. Keep attribution in the note and the reply outside it. Do not add a second attribution, signature footer, heading, or horizontal rule.

Use Jesse’s verified identity. If an email is needed for the task, read `git config user.name` and `git config user.email` in the relevant repository and verify that they identify Jesse. If absent or conflicting, leave `<Jesse’s verified email>` in the prepared draft and ask before any action requiring it. Do not hardcode or publish Jesse’s email merely to attribute a comment.

Apply the note to top-level PR comments, inline review comments, replies to bots or humans, issue comments, and explanations preceding thread resolution or feedback dismissal. Do not add it to PR descriptions, commit messages, or text Jesse explicitly asks to post verbatim without attribution.

Lead with the conclusion. Cite relevant code, observed behavior, checks, or a reproduction. Keep the reply concise, distinguish fact from judgment, and omit filler, canned thanks, and status narration. Give a written evidence-based reason when declining a finding; do not change code just to satisfy a bot.

Inspect the full draft, quoted text, and attachments for private details or secrets. Preview the Markdown and preserve the blank line after the note. After posting, verify the returned comment/review URL. Resolve a review thread only after its authorized response posts successfully. Report posting failures accurately; do not claim a reply or resolution that did not happen.
