# Validation

This file records release-candidate evidence and its limits. Installer validation creates fresh temporary homes for child processes, with isolated provider/config/cache directories. It never installs into the invoking user's skill homes. Logs and generated recipes remain in the temporary test projects.

## Reproduce

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
python3 scripts/validate_install.py
```

The installer script prints its temporary run directory. It invokes the real `npx --yes skills@1.7.0` CLI and checks file hashes, selective discovery, all current packages, provider lists, tag upgrades, SHA rollback, removal, and preservation of an unrelated installed sentinel. Its disposable HTTP Git remote tests refs without publishing test tags.

CI runs only package integrity and validator failure cases. Installer and provider tests are explicit local runs; CI does not install the bundle into provider homes.

Once a candidate commit is pushed, also test the GitHub path:

```sh
python3 scripts/validate_install.py --remote "https://github.com/boundsj/bounds-skills/tree/$bounds_ref"
python3 scripts/validate_codex_discovery.py /path/printed/by/validate_install
```

The optional remote pass compares all installed skill files with the checkout and runs installer check/update against the pinned source. The update assertion checks unchanged content only; it does not test provider targeting. The discovery script starts a new Codex app-server and uses its `skills/list` API; it needs no model credentials. Retained evidence is under the run directory's `evidence/` folder. Remove that specific temporary run directory when finished with its evidence.

Behavioral validation exercises representative tasks in disposable projects. The runner copies only the already-installed Bounds packages into another temporary home, creates a synthetic CLI project, and starts a fresh provider process. Model credentials are needed for actual turns. Use `--codex-auth /path/to/auth.json` for Codex or `--claude-auth /path/to/.credentials.json` for an existing Claude file credential. The runner temporarily copies only that credential file with mode 0600 and deletes the copy in `finally`; it never prints its contents or changes the source credential. Provider-managed system defaults may still start their own tools. The runner isolates writable homes, not the provider binary or system configuration.

```sh
python3 scripts/run_behavior.py /path/to/install-run --case simple --model YOUR_MODEL --effort YOUR_EFFORT --codex-auth /path/to/auth.json
python3 scripts/run_behavior.py /path/to/install-run --case create --model YOUR_MODEL --effort YOUR_EFFORT --codex-auth /path/to/auth.json
python3 scripts/run_behavior.py /path/to/install-run --case maintain --recipe-project /path/to/create-run/project --model YOUR_MODEL --effort YOUR_EFFORT --codex-auth /path/to/auth.json
python3 scripts/run_behavior.py /path/to/install-run --provider claude --case simple --claude-auth /path/to/.credentials.json
```

Other cases are `plan`, `debug`, `review`, `retro`, `recall`, `docs`, `missing`, `optout`, `optout_same`, and `catalog`. `optout_same` first invokes mode, then resumes that isolated Codex session with an opt-out; its initial turn is retained in `prime.jsonl`. The runner's exit code is provider process status, **not a behavioral pass**. Inspect the final result, commands, diff, and retained artifacts. `events.jsonl`, `prompt.txt`, and `result.json` remain in the printed temporary run directory; do not publish provider traces or authentication data. No real project or user-home skills are used as test fixtures.

## Recall addition (0.2.0)

The recall workflow was added on 2026-10-16. Research covered a bounded sample of local Codex/Claude sessions, relevant T3 messages/activity, and a development journal. Only generalized retrieval and evidence rules are distributed. Another requested host was absent from the available configured inventory; its history was not inspected. No private source links or transcripts are included here.

Package integrity, all five package tests, and Python syntax pass for the nine-skill bundle. The skill-creator quick validator passes for `bounds-recall`; it was not run against the whole bundle. The deliberate mode extension retains the compatibility limit described in the initial results below. The quick validator used an isolated Python environment with PyYAML; this is a validation dependency, not an invocation dependency.

The implementation source for these checks is `91637ad9c33d4396710acb18cd75ce4e19b8bfaf`. Isolated `skills@1.7.0` installation passes discovery, selective/full installation, complete payload hashes for both providers, provider lists, disposable tag upgrade and SHA rollback, scoped/full removal, and preservation of unrelated sentinels. A separate recall-only install to both providers also preserves exact payload hashes and installs no sibling skills. A fresh Codex CLI 0.162.1 app-server discovers all nine enabled skills with no parse errors. These checks use temporary homes; no real skill home is changed. Claude CLI is 2.1.299 on this host; a new authenticated Claude recall invocation has not been claimed from these packaging/discovery checks.

An independent Codex forward test exercised the initial skill body against the synthetic `recall` fixture: actual Git change/revert commits, Codex and Claude JSONL messages, a stale journal retelling, a later hold instruction, and an unavailable second host. It found the reverted change and current default, preserved JSON and the hold, rejected the stale journal as current evidence, and marked deployment/remote-host state unverified. It cited the supplied records and Git evidence and made no edits. The parent independently checked the fixture's actual CLI output and clean working tree. This tests a supplied-record scenario, not automatic provider catalog selection or remote integration reliability.

Opus 5.5 at xhigh reviewed implementation `91637ad`. It found one low-priority documentation overclaim: the quick-validator result applied to recall, not the entire bundle. That wording is corrected above. Its optional suggestions narrowed the trigger to prior-session context, restricted cross-project transcript search to requested projects, and strengthened the fixture: commit dates now match event dates, and the history no longer gives away the Git revert or labels the journal as stale. A second independent Codex forward test used the revised 431-word skill and stronger fixture. It discovered the actual revert from Git, checked default and explicit-size CLI behavior, preserved the later hold, reconciled the journal cutoff, reported absent laptop/deployment evidence, and left the checkout clean.

To reproduce through a fresh installed provider, use `scripts/run_behavior.py` with `--case recall` and the same provider/auth options as above. The fixture forbids real history/connector access. Inspect the answer for the later user constraint, Git reversal, stale journal, missing-host coverage, and unchanged files; provider exit status alone is insufficient. The scripted provider invocation is separate from the independent forward test described here.

## Initial eight-skill results (0.1.0)

The latest immutable package source tested on GitHub is [`eead99dee0bc7cd9b09b926720fe861db38853ab`](https://github.com/boundsj/bounds-skills/tree/eead99dee0bc7cd9b09b926720fe861db38853ab). The original full workflow matrix used [`38703034edb2c9c163263278ffe3dde05ed32d4b`](https://github.com/boundsj/bounds-skills/tree/38703034edb2c9c163263278ffe3dde05ed32d4b); the follow-up changes and targeted checks are recorded below. No release tag was published; tag upgrade and SHA rollback used a disposable local Git remote.

Completed on the Mac Mini, macOS 26.5 arm64, 2026-10-04. Installer: Node 26.0.0, npm 11.12.1, `skills@1.7.0`. Validation scripts: Python 3.14.2; Git 2.50.1 (Apple Git-155). Providers: Codex CLI 0.160.0 and Claude Code 2.1.288. Codex behavioral cases requested GPT-6 Astra, max reasoning, fast service; its fixture commands used the provider shell's Python 3.9.6. Claude used its default `claude-opus-5-5` model. The per-workflow rows below describe Codex; Claude coverage is listed explicitly.

| Check | Observed result |
| --- | --- |
| Package integrity | Eight frontmatter records, internal reference links, explicit mode policy, reachable conditional references, and both MIT notices in each installable directory pass. The original entrypoints were 254–343 words after review clarifications; the later retro update is 449 words. |
| Validator failure cases | Five unit tests pass, including rejecting missing references, sibling-skill dependencies, missing attribution and accidental implicit mode. |
| Upstream skill-creator check | Seven skills pass directly. Mode's portable fields pass; the validator's older allowlist rejects Claude's `disable-model-invocation` extension. Real Codex/Claude discovery parses that file successfully. The extension is deliberately retained. |
| Isolated installation | Selective/full installation, complete file hashes, provider lists, tag upgrade, SHA rollback, scoped Claude removal, full removal and unrelated sentinels pass. |
| GitHub distribution | Full-SHA tree URL installs all eight with identical hashes. `check` reports current; unscoped `update` against that immutable source changes no payload. This no-change check does not establish preserved provider targeting. |
| Moving-ref update limit | Independent review reproduced an upstream CLI issue: after Codex/Claude-only installation, `update --global bounds-plan --yes` for a changed tracked ref also creates a Windsurf link when that provider is detected. The supported upgrade instructions use explicit pinned re-add with agent selection. |
| Fresh Codex discovery | A new app-server's `skills/list` reports all eight enabled without parse errors, for both local and remote installs. |
| Codex explicit-mode policy | A no-tool catalog query lists the seven supporting skills and excludes mode; explicit `$bounds-mode` loads and executes in the other cases. |
| Fresh Claude discovery | New-process init reports all eight in `skills` and `slash_commands`. |
| Authenticated Claude invocation | With a temporary copy of the existing credential, `/bounds-mode` makes exactly the requested typo edit. In a separate bug case it invokes `bounds-debug` through the Skill tool, reproduces the wrong page, makes the one-line fix, and checks pages 1–4 plus invalid-page rejection. Independent artifact checks confirm results and edit scope; temporary credential copies are deleted. |
| Claude explicit-mode policy | A no-tool catalog query lists the seven supporting skills and excludes mode, while explicit `/bounds-mode` works in the authenticated cases. |
| Simple mode | Only the requested README typo changes; diff check passes. No supporting skill or reference is read. |
| Plan | Produces scope, retained JSON behavior, acceptance examples and dependencies; eight baseline checks pass; no files change. |
| Debug via mode | Reads the debugging workflow, reproduces the wrong page, fixes the offset, and passes 12 concrete CLI cases. Only product correction changes. |
| Review without delegation | Pins base/head, executes both revisions, identifies the pagination regression with file/line and impact, labels the review local, and changes no files. |
| Retro | Uses only the specified synthetic work log, distinguishes a repeated correction from a single incident, recommends wiring the existing check, and labels actual enforcement unverified. |
| Agent docs | Repairs a stale CLI command and duplicated guidance, checks output and links, changes only AGENTS.md. |
| Create verification | Generates a local recipe and four-feature map; 14 real CLI cases pass. Independent inspection confirms cleanup removed runtime state, retained readable evidence with unchanged hashes, and left product code unchanged. |
| Maintain verification | Corrects intentional command-rename drift and a stop-on-first-failure harness gap, then executes all 14 mapped cases: 8 pass, 6 fail for the separate seeded pagination defect. Reports blocked, retains original expectations, changes only verification files, and preserves evidence after cleanup. Product code stays unchanged. |
| Missing supporting skill | With only mode installed, reports `bounds-plan` absent and delivers the requested plan through local inspection; installs nothing and changes no files. |
| Fresh-turn opt-out | “Stop using bounds-mode” performs only the typo edit, with no skill body read. Same-session opt-out is checked separately below. |
| Same-session opt-out | First invokes mode for a read-only summary, then resumes that same Codex session with an opt-out. The second turn makes only the requested typo correction and does not load supporting workflows. |

An independent reviewer inspected base `722ce9ce2e5da00dc9946aa5e2553ec8599ed1b1` through package commit `38703034edb2c9c163263278ffe3dde05ed32d4b`. The moving-ref update recommendation was the sole actionable finding; the installation guide now uses the tested explicit re-add path. No skill-body or attribution findings were reported. Later documentation and harness changes receive local checks; the review is not claimed for an unseen revision.

A separate Claude Opus 5.5 review at medium effort inspected that base through `9c2072a3c13e98caeeea0c2f0a02bc351abfcede`, including all eight skills, references, attribution, docs, and validation tools. Package checks and all five tests passed; the reviewer also verified the upstream license texts at their pinned revisions. It found no blockers and three minor issues: ambiguous update-test wording, notices linked to moving `main`, and unclear reuse of delegation authorization. The follow-up clarifies the no-op test's limits, includes the source/adaptation mapping inside each installed notice, and aligns mode/review with existing user and host permissions. License texts and other workflow bodies are unchanged.

A second Claude Opus 5.5 medium review confirmed all three resolutions at `eead99dee0bc7cd9b09b926720fe861db38853ab`, with no actionable findings or merge blockers. The parent reran package checks, all five tests, isolated installation/ref changes/removal, and fresh Codex discovery. A fresh GitHub install at that SHA matched every skill file for both providers. New authenticated Claude Opus 5.5 medium fixtures exercised the changed mode/review bodies: mode made only the typo correction; review resolved both refs, executed base/head behavior, reported the seeded pagination regression as a local review, and changed no project files. Independent artifact checks confirmed edit scope and removal of temporary credential copies. These targeted reruns do not repeat the full workflow matrix or benchmark finding-priority calibration. Subsequent evidence-only edits leave the skill payload unchanged.

The `bounds-retro` revision that folds in Pocock's retro documentation was rechecked on 2026-10-05: package checks, all five tests, and isolated installation pass. Fresh `retro` cases ran on Claude Opus 5.5 (medium) and Codex GPT-6 Astra (medium) against that installed payload. Both read only `WORK.md` and ranked the repeated JSON-default correction first. Both recommended wiring the existing test over more prose, gave a validation step, stated unverified enforcement, and changed no files. An independent Codex GPT-6 Astra review found one actionable issue: an incorrect Claude project-slug rule in the session-sources reference. It also flagged the lost repeated-versus-single-incident distinction. Both are fixed; the behavioral cases predate those two text edits.

These are representative synthetic CLI cases, not a model reliability benchmark or proof for browser, mobile, performance, or production workflows. Claude's full eight-workflow matrix and same-session opt-out remain untested. Fresh installed-bundle discovery in the T3 composer, other hosts/operating systems, and a real user-home rollout remain untested. No cross-host synchronization or delegation is provided by the bundle.

## Workflow additions (0.3.0)

The added packages were proposed by Opus 5.5 at high effort from pinned public upstream sources and a generalized private research brief, then reviewed and integrated by Bounds Skills CoS. No private journal content is distributed. Each listed package passed package integrity, the five package tests, and the skill-creator quick validator for that individual skill. Supplied-artifact forward exercises are separate from fresh provider discovery/invocation and do not prove connector or other-host support.

| Skill | Supplied-artifact exercise |
| --- | --- |
| `bounds-ketchup` | A supplied thread with changed scope, a corrected overclaim, skipped native coverage, and a failed preview; retained the latest request and named what remained unverified. |
| `bounds-why` | Contradictory dated decisions and a provisional concurrency limit; separated documented reasons, inference, missing measurements, and the per-manager versus process-wide limit. |
| `bounds-blast-radius` | Ran three synthetic runtime tests to disprove that cancellation prevents late results; traced consumer and lifetime effects, separating executed evidence from the unexecuted gate-removal counterfactual. |
| `bounds-how` | Explained normal replacement, advisory cancellation, state ownership, and two-document behavior from real fixture code; kept simulated surfaces and the per-manager limit distinct from platform claims. |
| `bounds-architect` | Compared two viable document-scoped designs, rejected global latest-job state and direct provider-to-view fanout, and proposed bounded compatibility and validation steps without implementation. |
| `bounds-unslop` | Rewrote a synthetic release note while preserving the exact code block, quotations, numeric sequence, uncertainty, and worsening tail-latency result. |
| `bounds-bro` | Restated a technical decision in 161 words while retaining cancellation, ownership, untested native behavior, and the next check. |
| `bounds-help` | Used a supplied complete catalog to route rationale then execution explanation; rejected a missing historical skill name and did not execute the work. |
| `bounds-automate-me` | Drafted a project-scoped working-style skill from explicit and repeated evidence; excluded a rejected one-off preference and performed no installation or global change. |
