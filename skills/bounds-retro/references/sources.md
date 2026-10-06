# Reading a named session

Load this only when the user names work outside the current conversation. Read the smallest record that covers the boundary. Start with the user's own messages, because corrections show where attention went, then expand around those moments.

| Record | How to read it |
| --- | --- |
| T3 Code thread | `t3_thread_read` with the messages view for user turns, then the activity view near a correction for tool calls. Use `t3_thread_list` with subagents included to find delegated reviews; their findings show what implementation missed. |
| Claude Code session | `~/.claude/projects/<cwd-slug>/<session-id>.jsonl`. The slug is the working directory with `/` and `.` replaced by `-`. User turns have `"type":"user"`. |
| Codex session | `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`, or `~/.codex/archived_sessions/`. User messages are `response_item` records with `payload.role` of `user`; the first records are environment context. |
| Pull request | `gh pr view <n> --comments`, review threads, and `gh pr checks <n>`. |

These layouts belong to the hosts and can change. If a path or field is missing, report it and continue with what is available rather than searching broadly.

Logs can contain credentials, private links, and unrelated work. Quote only the short excerpt that establishes a moment. Never copy raw transcripts into a repository, PR, or other shared location.
