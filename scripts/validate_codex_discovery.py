#!/usr/bin/env python3
"""Ask a fresh Codex app-server for skills in an isolated validation home."""

import argparse
import json
from pathlib import Path
import queue
import subprocess
import threading

from check import NAMES
from validate_install import isolated_env


def discover(root):
    assert root.name.startswith("bounds-install-") and (root / "evidence/install.json").is_file(), "Use a validate_install.py output directory"
    env = isolated_env(root)
    cwd = root / "work"
    inbox = queue.Queue()
    error_log = root / "evidence/codex-discovery.stderr"
    with error_log.open("w") as stderr:
        process = subprocess.Popen(["codex", "app-server"], cwd=cwd, env=env, text=True,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=stderr)
        reader = threading.Thread(target=lambda: [inbox.put(line) for line in process.stdout], daemon=True)
        reader.start()

        def rpc(number, method, params):
            process.stdin.write(json.dumps({"id": number, "method": method, "params": params}) + "\n")
            process.stdin.flush()
            while True:
                message = json.loads(inbox.get(timeout=30))
                if message.get("id") == number:
                    assert "error" not in message, message
                    return message["result"]

        try:
            rpc(1, "initialize", {"clientInfo": {"name": "bounds_validation", "version": "0.1.0"}})
            result = rpc(2, "skills/list", {"cwds": [str(cwd)], "forceReload": True})
            entries = result["data"]
            found = {s["name"] for e in entries for s in e["skills"] if s["enabled"] and s["name"].startswith("bounds-")}
            assert found == NAMES, (found, result)
            assert not any(e["errors"] for e in entries), result
            (root / "evidence/codex-discovery.json").write_text(json.dumps(result, indent=2) + "\n")
            return sorted(found)
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            process.stdin.close()
            process.stdout.close()
            reader.join(timeout=5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run", type=Path)
    args = parser.parse_args()
    print(json.dumps({"status": "pass", "discovered": discover(args.run.resolve())}, indent=2))
