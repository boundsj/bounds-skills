#!/usr/bin/env python3
"""Exercise npx skills in disposable child-process homes; never a user installer."""

import argparse
from functools import partial
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import threading
from urllib.parse import urlsplit

from check import NAMES

CLI = ["npx", "--yes", "skills@1.7.0"]


def isolated_env(root):
    # Only child processes see these homes. No host settings/auth are imported.
    env = {k: os.environ[k] for k in ("PATH", "SYSTEMROOT", "LANG", "LC_ALL") if k in os.environ}
    for key, relative in {
        "HOME": "home", "CODEX_HOME": "home/.codex", "CLAUDE_CONFIG_DIR": "home/.claude",
        "XDG_CONFIG_HOME": "home/.config", "XDG_CACHE_HOME": "home/.cache",
        "npm_config_cache": "npm-cache", "TMPDIR": "tmp",
    }.items():
        target = root / relative
        target.mkdir(parents=True, exist_ok=True)
        env[key] = str(target)
    env.update({"DISABLE_TELEMETRY": "1", "DO_NOT_TRACK": "1", "CI": "1",
                "NO_COLOR": "1", "GIT_TERMINAL_PROMPT": "0", "GIT_CONFIG_NOSYSTEM": "1"})
    return env


def digest(folder):
    return {str(p.relative_to(folder)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(folder.rglob("*")) if p.is_file()}


def installed(env, agent):
    root = (Path(env["HOME"]) / ".agents/skills" if agent == "codex"
            else Path(env["CLAUDE_CONFIG_DIR"]) / "skills")
    return root, {p.parent.name for p in root.glob("*/SKILL.md") if p.parent.name.startswith("bounds-")}


class GitHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, git_root, git_env, **kwargs):
        self.git_root = git_root
        self.git_env = git_env
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.serve_git()

    def do_POST(self):
        self.serve_git()

    def serve_git(self):
        url = urlsplit(self.path)
        env = dict(self.git_env, GIT_PROJECT_ROOT=str(self.git_root), GIT_HTTP_EXPORT_ALL="1",
                   PATH_INFO=url.path, QUERY_STRING=url.query, REQUEST_METHOD=self.command,
                   CONTENT_TYPE=self.headers.get("Content-Type", ""))
        body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        result = subprocess.run(["git", "http-backend"], input=body, capture_output=True, env=env, timeout=30)
        header, content = result.stdout.split(b"\r\n\r\n", 1)
        headers = [line.decode().split(":", 1) for line in header.split(b"\r\n")]
        status = next((int(value.strip().split()[0]) for key, value in headers if key == "Status"), 200)
        self.send_response(status)
        for key, value in headers:
            if key != "Status":
                self.send_header(key, value.strip())
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, *_args):
        pass


def validate(root, source_repo, remote=None):
    env = isolated_env(root)
    cwd = root / "work"
    cwd.mkdir()
    logs = root / "evidence"
    logs.mkdir()
    commands = []

    def run(args, at=cwd):
        result = subprocess.run(args, cwd=at, env=env, text=True, capture_output=True, timeout=180)
        index = len(commands) + 1
        (logs / f"{index:02}.log").write_text(result.stdout + result.stderr)
        commands.append({"argv": list(map(str, args)), "exit": result.returncode, "log": f"{index:02}.log"})
        assert result.returncode == 0, f"Command failed: {args}; see {logs / f'{index:02}.log'}"
        return result.stdout

    sentinels = []
    for agent in ("codex", "claude-code"):
        folder, _ = installed(env, agent)
        sentinel = folder / "existing-specialist" / "SKILL.md"
        sentinel.parent.mkdir(parents=True)
        sentinel.write_text('---\nname: existing-specialist\ndescription: "Preserve this unrelated skill."\n---\nSentinel.\n')
        sentinels.append((sentinel, sentinel.read_bytes()))

    source = str(source_repo)
    listed = run(CLI + ["add", source, "--list"])
    assert all(name in listed for name in NAMES), "Installer discovery omitted a skill"
    run(CLI + ["add", source, "--global", "--agent", "codex", "claude-code", "--skill", "bounds-mode", "bounds-plan", "--yes"])
    for agent in ("codex", "claude-code"):
        folder, names = installed(env, agent)
        assert names == {"bounds-mode", "bounds-plan"}, f"Selective install leaked skills for {agent}"
        for name in names:
            assert digest(folder / name) == digest(source_repo / "skills" / name), f"Incomplete install: {name}"
    run(CLI + ["add", source, "--global", "--agent", "codex", "claude-code", "--skill", "*", "--yes"])
    for agent in ("codex", "claude-code"):
        folder, names = installed(env, agent)
        assert names == NAMES
        for name in names:
            assert digest(folder / name) == digest(source_repo / "skills" / name), f"Changed package: {name}"
        output = run(CLI + ["list", "--global", "--agent", agent])
        assert all(name in output for name in NAMES)

    # A local HTTP Git remote exercises actual ref resolution without publishing tags.
    fixture = root / "fixture"
    fixture.mkdir()
    shutil.copytree(source_repo / "skills", fixture / "skills")
    run(["git", "init", "-b", "main"], fixture)
    run(["git", "config", "user.name", "Bounds fixture"], fixture)
    run(["git", "config", "user.email", "fixture@example.invalid"], fixture)
    marker = fixture / "skills/bounds-plan/fixture-version.txt"
    marker.write_text("one\n")
    run(["git", "add", "."], fixture)
    run(["git", "commit", "-m", "Fixture one"], fixture)
    first_sha = run(["git", "rev-parse", "HEAD"], fixture).strip()
    run(["git", "tag", "v0.1.0-test"], fixture)
    marker.write_text("two\n")
    run(["git", "add", "."], fixture)
    run(["git", "commit", "-m", "Fixture two"], fixture)
    run(["git", "tag", "v0.2.0-test"], fixture)
    run(["git", "clone", "--bare", str(fixture), str(root / "fixture.git")])
    run(["git", "--git-dir", str(root / "fixture.git"), "update-server-info"])
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(GitHandler, git_root=root, git_env=env))
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        url = f"http://127.0.0.1:{server.server_port}/fixture.git"
        for ref, expected in [("v0.1.0-test", "one\n"), ("v0.2.0-test", "two\n"), (first_sha, "one\n")]:
            run(CLI + ["add", url + "#" + ref, "--global", "--agent", "codex", "claude-code", "--skill", "bounds-plan", "--yes"])
            for agent in ("codex", "claude-code"):
                folder, _ = installed(env, agent)
                assert (folder / "bounds-plan/fixture-version.txt").read_text() == expected
    finally:
        server.shutdown()
        server.server_close()
        worker.join()

    if remote:
        run(CLI + ["add", remote, "--global", "--agent", "codex", "claude-code", "--skill", "*", "--yes"])
        for agent in ("codex", "claude-code"):
            folder, names = installed(env, agent)
            assert names == NAMES
            for name in names:
                assert digest(folder / name) == digest(source_repo / "skills" / name), f"Remote differs: {name}"
        before = digest(Path(env["HOME"]) / ".agents/skills")
        run(CLI + ["check"])
        # This immutable-source no-op checks content only, not provider targeting.
        # For upgrades, use pinned add with explicit agents; see docs/install.md.
        run(CLI + ["update", "--global", *sorted(NAMES), "--yes"])
        assert digest(Path(env["HOME"]) / ".agents/skills") == before, "Pinned update changed content"

    run(CLI + ["remove", "bounds-plan", "--global", "--agent", "claude-code", "--yes"])
    assert "bounds-plan" not in installed(env, "claude-code")[1]
    assert "bounds-plan" in installed(env, "codex")[1], "Removal affected other provider"
    run(CLI + ["remove", *sorted(NAMES), "--global", "--agent", "codex", "claude-code", "--yes"])
    for agent in ("codex", "claude-code"):
        assert not installed(env, agent)[1]
    assert all(path.read_bytes() == value for path, value in sentinels), "Existing skill changed"

    # Leave a complete local install for separate discovery/invocation tests in this temp home.
    run(CLI + ["add", source, "--global", "--agent", "codex", "claude-code", "--skill", "*", "--yes"])
    summary = {"status": "pass", "installer": "skills@1.7.0", "remote": remote,
               "checks": ["discovery", "selective install", "complete file hashes", "list by provider",
                          "tag upgrade", "SHA rollback", "provider-scoped removal", "full removal", "sentinel preservation"],
               "commands": commands}
    (logs / "install.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", help="Optional published GitHub source pinned to a full commit SHA")
    args = parser.parse_args()
    root = Path(tempfile.mkdtemp(prefix="bounds-install-"))
    print(f"Isolated run and retained evidence: {root}", flush=True)
    result = validate(root, Path(__file__).resolve().parents[1], args.remote)
    print(json.dumps({k: v for k, v in result.items() if k != "commands"}, indent=2))
