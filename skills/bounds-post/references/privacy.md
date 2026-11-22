# Privacy pass

Treat everything in the source material as private unless the user's instructions or an already published source mark it public. Check the title, body, headings, code, command output, captions, alt text, link targets, and screenshots. Do not paste unpublished draft text into outside services, such as detectors, grammar checkers, or search, to check it.

## Remove or generalize

| Category | Examples | Default |
| --- | --- | --- |
| People | names, handles, email addresses, phone numbers, faces, colleagues, clients, family | Remove, or "a teammate", "a client". Name someone only with their public consent or their own public statement. |
| Places and machines | home or office location, hostnames, IP addresses, private network names, device names, usernames, local or absolute paths, terminal prompts | Generalize: "a home server", "the project folder", `~/project`. |
| Accounts and secrets | keys, tokens, account or team identifiers, signing details, webhook or signed URLs, environment values | Remove entirely; never placeholder a real value. |
| Work | unannounced project or product names, private repository names, internal links, tickets, private PR numbers, branch names, private commit hashes, roadmap dates, unreleased features | Generalize: "a native app", "an internal tool". Keep only what is already public. |
| Security | internal architecture, versions, or configuration that would help an attacker; unpatched issues | Remove, or describe the lesson without the exploitable detail. |
| Money and data | revenue, prices paid, balances, trading positions, customer counts, user content, health data, logs with user data | Remove, or use a clearly labeled synthetic example. |
| Agent records | raw transcripts, session or request identifiers, prompts containing private material | Summarize the lesson; do not quote private sessions. |
| Images | window titles, tabs, notifications, menu bar items, file trees, location metadata | Crop, blur, or recreate with synthetic content; strip metadata. |

## Watch for combinations

Details that are harmless alone can identify a person, place, or project together: a date with a location, a schedule that reveals absence, a niche project description with a timeline, a rare error message from a private system. Generalize one of them.

## Keep it honest

Generalizing must not change the claim. "A native app" can replace a project name; it cannot turn one test device into "many users". If removing a detail removes the proof, say so in the open questions instead of keeping the detail.

## Report

List each change as original category, location in the draft, and what replaced it, without repeating the private value itself in a form the user might paste publicly by mistake. Flag anything you could not judge.
