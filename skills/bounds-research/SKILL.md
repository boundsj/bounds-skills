---
name: bounds-research
description: "Answer a bounded factual question from primary sources such as official docs, specs, source code, release notes, or installed package versions, with every claim dated, versioned, and cited. Use when a decision waits on an external fact: how an API, platform, library, or service behaves, or whether a version claim holds. Not for why or how existing project code works, or for prior sessions."
license: MIT
---

# Bounds research

Find a fact a decision waits on, from the sources that own it. Research is read-only: it grants no authority to change code, install packages, sign in, or publish. The user's instructions may name private sources, note locations, or tools to use.

## Bound the question

State the question as one answerable claim and the decision it serves: one API, one behavior, one version range. For a broad request, propose the narrow questions that settle the decision and start with the one that unblocks most. Record the versions actually in use, from lockfiles, manifests, installed headers or schemas, or version output, before reading about the latest release.

## Read primary sources

Prefer, in order: installed source, headers, or schemas; official documentation and specifications; release notes, changelogs, and migration guides; first-party repositories and issue trackers; maintainer statements. Use secondary write-ups only to find a primary source, then cite that source. Open the page; do not cite a search snippet. Search with public names and generic error text; keep private code, paths, hostnames, and project names out of queries and external probes.

Match documentation to the installed version and note deprecated, beta, or platform-limited status. When a probe is cheap and safe, such as a compile, a REPL call, or a dry-run request in a disposable location, run it and record the result.

For large reading, use one fresh-context reader with a bounded brief when delegation is available and permitted. Require cited findings. A delegated reader does the work itself and starts no further agents.

## Write history, not the present

Date every claim and pin it to a version, commit, or retrieval date: "As of version 4.2 (release notes, retrieved 2026-11-21), the client retries twice." Never write "currently" or "now" without that pin. Label each point **fact** (cited), **inference** (reasoned from cited facts), or **unknown**. Record conflicting sources with both citations and which governs the installed version. Say what you could not find and where you looked; a missing hit is not proof of absence.

Stop when the question is answered with cited evidence or no remaining source could change the decision. Do not widen into a survey.

## Report

Lead with the answer and its confidence, then the dated, cited claims, conflicts, unknowns, and the next check that would settle remaining doubt. Before returning, follow two citations yourself; replace any that lands on a summary rather than the owning source.

Answer in the conversation by default. Write a durable note only when asked, where the user or repository keeps notes, marked as a dated snapshot. Keep private sources, credentials, and internal links out of public artifacts.
