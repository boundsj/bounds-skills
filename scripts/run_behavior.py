#!/usr/bin/env python3
"""Run one real provider case in a disposable project; inspect evidence manually."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from validate_install import isolated_env

APP = '''import argparse
import json

parser = argparse.ArgumentParser(description="List fixture items with one-based pages.")
commands = parser.add_subparsers(dest="command", required=True)
listing = commands.add_parser("list")
listing.add_argument("--page", type=int, default=1)
listing.add_argument("--size", type=int, default=2)
args = parser.parse_args()
if args.page < 1 or args.size < 1:
    parser.error("page and size must be positive")
items = ["alpha", "beta", "gamma", "delta", "epsilon"]
start = (args.page - 1) * args.size
print(json.dumps(items[start:start + args.size]))
'''

TASKS = {
    "simple": ("bounds-mode", 'Fix only the typo "teh" in README.md. Verify the edit.'),
    "plan": ("bounds-plan", "Plan a CSV output option for this CLI. Keep current JSON output as the default. Deliver the plan here; do not implement it."),
    "debug": ("bounds-mode", 'The list CLI says pages are one-based but `python3 app.py list --page 1 --size 2` returns ["gamma", "delta"] instead of ["alpha", "beta"]. Reproduce, fix, and verify this bug.'),
    "review": ("bounds-review", "Review the diff from HEAD~1 to HEAD against README.md. Return actionable findings with evidence; do not edit files. This session has no delegation capability."),
    "retro": ("bounds-retro", "Review only WORK.md for repeated corrections and wasted effort. Recommend a proportionate improvement; do not implement changes."),
    "docs": ("bounds-agent-docs", "Repair AGENTS.md: check its commands against this CLI, remove duplication, and keep useful navigation. Edit only project documentation."),
    "create": ("bounds-create-verification", "Create and execute a local verification recipe for this CLI, including a small feature map. Save evidence outside disposable runtime state and confirm it survives cleanup. Do not change product behavior."),
    "maintain": ("bounds-maintain-verification", "Maintain this project's existing verification recipe after the list subcommand was intentionally renamed to items. Audit all mapped behaviors. Intended pagination is still one-based. Edit only the recipe and its helpers; report any product defects."),
    "missing": ("bounds-mode", "Plan a CSV option for this CLI while preserving JSON as default. Do not implement it. Only bounds-mode is installed in this test home."),
    "optout": (None, 'Stop using bounds-mode for this request. Fix only the typo "teh" in README.md.'),
    "optout_same": (None, 'Stop using bounds-mode for this request. Fix only the typo "teh" in README.md.'),
    "catalog": (None, "Without calling tools, list only the bounds-* skills already present in your available-skills catalog. Do not infer names from the filesystem or from general knowledge. Do not perform any other task."),
}


def run(args):
    install_root = args.install.resolve()
    assert install_root.name.startswith("bounds-install-") and (install_root / "evidence/install.json").is_file()
    root = Path(tempfile.mkdtemp(prefix=f"bounds-behavior-{args.case}-"))
    env = isolated_env(root)
    canonical = Path(env["HOME"]) / ".agents/skills"
    canonical.mkdir(parents=True)
    names = ["bounds-mode"] if args.case == "missing" else [p.name for p in (install_root / "home/.agents/skills").iterdir() if p.name.startswith("bounds-")]
    for name in names:
        shutil.copytree(install_root / "home/.agents/skills" / name, canonical / name)
    claude_skills = Path(env["CLAUDE_CONFIG_DIR"]) / "skills"
    claude_skills.mkdir()
    for name in names:
        (claude_skills / name).symlink_to(canonical / name, target_is_directory=True)

    project = root / "project"
    if args.case == "maintain":
        assert args.recipe_project, "--recipe-project must point to a previous create case's project"
        source = args.recipe_project.resolve()
        assert source.parent.name.startswith("bounds-behavior-create-"), "Use an isolated create-case project"
        shutil.copytree(source, project, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    else:
        project.mkdir()
        (project / "app.py").write_text(APP)
        (project / "README.md").write_text('# Fixture CLI\n\nUse `python3 app.py list --page 1 --size 2` to list items.\nPages are one-based; page 1 returns ["alpha", "beta"], page 2 returns ["gamma", "delta"].\nJSON is the default output. Page and size must be positive.\n\nThis is teh fixture.\n')

    def git(*argv):
        return subprocess.run(["git", *argv], cwd=project, env=env, text=True, capture_output=True, check=True).stdout.strip()

    git("init", "-b", "main")
    git("config", "user.name", "Bounds fixture")
    git("config", "user.email", "fixture@example.invalid")
    git("add", ".")
    git("commit", "-m", "Fixture baseline")
    if args.case in ("debug", "review", "maintain"):
        text = (project / "app.py").read_text().replace("(args.page - 1) * args.size", "args.page * args.size")
        if args.case == "maintain":
            text = text.replace('add_parser("list")', 'add_parser("items")')
        (project / "app.py").write_text(text)
        git("add", ".")
        git("commit", "-m", "Fixture change under evaluation")
    if args.case == "retro":
        (project / "WORK.md").write_text('# Synthetic work log\n\n1. Agent changed JSON default to CSV. User asked to preserve JSON.\n2. Agent checked only exit status 0 and missed incorrect page data. User corrected it.\n3. Agent added output-format handling and changed JSON default again. User repeated the constraint.\n4. tests/test_cli.py already checked default JSON output, but the agent never ran it.\n5. Repeated long instructions were added to AGENTS.md, but no check command was linked.\n')
        (project / "tests").mkdir()
        (project / "tests/test_cli.py").write_text('import subprocess\nimport sys\nimport unittest\n\nclass CLI(unittest.TestCase):\n    def test_default_json(self):\n        result = subprocess.run([sys.executable, "app.py", "list"], capture_output=True, text=True)\n        self.assertEqual(result.returncode, 0)\n        self.assertEqual(result.stdout, \'["alpha", "beta"]\\n\')\n')
    if args.case == "docs":
        (project / "AGENTS.md").write_text('# Agent guide\n\nRun `python3 app.py --list` to verify listing.\nAlways preserve JSON default.\nAlways preserve JSON default.\nSee README.md for expected page results.\n')

    skill, task = TASKS[args.case]
    prefix = "$" if args.provider == "codex" else "/"
    prompt = (f"{prefix}{skill} " if skill else "") + task
    prompt += "\nThis is a synthetic disposable fixture. Work only in this project; do not install packages, publish, or access other projects."
    (root / "prompt.txt").write_text(prompt + "\n")
    auth_source = args.codex_auth or args.claude_auth
    auth_target = (Path(env["CODEX_HOME"]) / "auth.json" if args.provider == "codex"
                   else Path(env["CLAUDE_CONFIG_DIR"]) / ".credentials.json")
    if auth_source:
        assert (args.provider == "codex") == bool(args.codex_auth), "Credential must match provider"
        shutil.copyfile(auth_source, auth_target)
        auth_target.chmod(0o600)
    if args.provider == "codex":
        command = ["codex", "exec", "--ignore-user-config", "--ignore-rules", "--ephemeral", "--json",
                   "--sandbox", "workspace-write", "--disable", "multi_agent", "--cd", str(project)]
        if args.model:
            command += ["--model", args.model]
        if args.effort:
            command += ["-c", f'model_reasoning_effort="{args.effort}"']
        if args.priority:
            command += ["-c", 'service_tier="fast"']
        command += [prompt]
    else:
        command = ["claude", "--print", "--verbose", "--output-format", "stream-json",
                   "--settings", '{"disableAutoMemory":true}', "--setting-sources", "user",
                   "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
                   "--allowedTools", "Read", "Edit", "Write", "Bash", "Glob", "Grep", "Skill",
                   "--disallowedTools", "Agent", "Task", "--no-session-persistence"]
        if args.model:
            command += ["--model", args.model]
        if args.effort:
            command += ["--effort", args.effort]
        command += ["--", prompt]
    def execute(argv, event_file, error_file):
        with (root / event_file).open("w") as out, (root / error_file).open("w") as err:
            process = subprocess.Popen(argv, cwd=project, env=env, stdin=subprocess.DEVNULL,
                                       stdout=out, stderr=err, start_new_session=True)
            try:
                return process.wait(timeout=args.timeout)
            except subprocess.TimeoutExpired:
                import signal
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                return 124

    print(f"Behavior run: {root}", flush=True)
    try:
        if args.case == "optout_same":
            assert args.provider == "codex", "Same-session resume case currently covers Codex only"
            base_command = [part for part in command[:-1] if part != "--ephemeral"]
            prime = "$bounds-mode Read README.md and summarize the fixture's behavior. Make no edits. This is a disposable test project; access only this project and the requested skill."
            assert execute(base_command + [prime], "prime.jsonl", "prime.stderr.log") == 0
            events = [json.loads(line) for line in (root / "prime.jsonl").read_text().splitlines()]
            thread = next(e["thread_id"] for e in events if e.get("type") == "thread.started")
            command = base_command + ["resume", thread, prompt]
        code = execute(command, "events.jsonl", "stderr.log")
    finally:
        auth_target.unlink(missing_ok=True)
    summary = {"provider": args.provider, "model_requested": args.model, "case": args.case,
               "exit": code, "project": str(project), "revision": git("rev-parse", "HEAD"),
               "changed": git("status", "--short"), "evaluation": "Requires artifact and trace review"}
    (root / "result.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    return code


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("install", type=Path)
    parser.add_argument("--provider", choices=("codex", "claude"), default="codex")
    parser.add_argument("--case", choices=TASKS, required=True)
    parser.add_argument("--model")
    parser.add_argument("--effort")
    parser.add_argument("--priority", action="store_true")
    auth = parser.add_mutually_exclusive_group()
    auth.add_argument("--codex-auth", type=Path, help="Temporarily copy auth.json; delete after run; never logged")
    auth.add_argument("--claude-auth", type=Path, help="Temporarily copy .credentials.json; delete after run; never logged")
    parser.add_argument("--recipe-project", type=Path)
    parser.add_argument("--timeout", type=int, default=480)
    sys.exit(run(parser.parse_args()))
