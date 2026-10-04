#!/usr/bin/env python3
"""Check distributable structure and references without installing dependencies."""

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


NAMES = {
    "bounds-mode", "bounds-plan", "bounds-debug", "bounds-review", "bounds-retro",
    "bounds-agent-docs", "bounds-create-verification", "bounds-maintain-verification",
}


def frontmatter(path):
    """Read this repository's deliberately flat YAML subset, not arbitrary YAML."""
    text = path.read_text()
    assert text.startswith("---\n"), f"{path}: missing frontmatter"
    header, body = text[4:].split("\n---\n", 1)
    values = {}
    for line in header.splitlines():
        key, value = line.split(":", 1)
        assert key not in values, f"{path}: duplicate key {key}"
        value = value.strip()
        values[key] = json.loads(value) if value.startswith('"') or value in ("true", "false") else value
    return values, body


def check(root):
    skills = root / "skills"
    actual = {p.parent.name for p in skills.glob("*/SKILL.md")}
    assert actual == NAMES, f"Skill set mismatch: {actual ^ NAMES}"
    notices = [(root / "licenses" / name).read_text() for name in (
        "Matt-Pocock-MIT.txt", "Lauren-Tan-MIT.txt")]
    stats = {}
    for name in sorted(NAMES):
        folder = skills / name
        metadata, body = frontmatter(folder / "SKILL.md")
        allowed = {"name", "description", "license", "disable-model-invocation"}
        assert set(metadata) <= allowed, f"{name}: unsupported metadata"
        assert metadata["name"] == name
        assert isinstance(metadata["description"], str) and 20 < len(metadata["description"]) <= 1024
        assert metadata["license"] == "MIT"
        assert bool(metadata.get("disable-model-invocation")) == (name == "bounds-mode")
        if name == "bounds-mode":
            assert (folder / "agents/openai.yaml").read_text().strip() == (
                "policy:\n  allow_implicit_invocation: false")
        else:
            assert not (folder / "agents/openai.yaml").exists(), f"{name}: unexpected override"
        license_text = (folder / "LICENSE.txt").read_text()
        assert all(notice in license_text for notice in notices), f"{name}: missing upstream notice"
        assert (folder / "NOTICE.md").is_file()
        assert not re.search(r"\[TODO:|\bTBD\b", body), f"{name}: unfinished scaffold"
        count = len(body.split())
        assert count <= 450, f"{name}: {count} words; move conditional detail to references"
        stats[name] = count

    linked = set()
    for path in root.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            assert resolved.exists(), f"{path.relative_to(root)}: broken link {target}"
            if path.is_relative_to(skills):
                folder = skills / path.relative_to(skills).parts[0]
                assert resolved.is_relative_to(folder.resolve()), f"{path}: link escapes skill: {target}"
            linked.add(resolved)
    for ref in skills.glob("*/references/*.md"):
        assert ref.resolve() in linked, f"Unreachable reference: {ref}"
    return stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps({"status": "pass", "entrypoint_words": check(args.root.resolve())}, indent=2))
