#!/usr/bin/env python3
"""Check distributable structure and references without installing dependencies."""

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


TSTACK_NAMES = {"bounds-ship", "bounds-modernize", "bounds-review", "bounds-leaving-pr-comments", "bounds-council"}
EMIL_NAMES = {"bounds-options", "bounds-dial", "bounds-ui-review", "bounds-web-craft", "bounds-native-craft"}

NAMES = {
    "bounds-ship", "bounds-modernize", "bounds-leaving-pr-comments",
    "bounds-mode", "bounds-plan", "bounds-debug", "bounds-review", "bounds-retro",
    "bounds-agent-docs", "bounds-create-verification", "bounds-maintain-verification", "bounds-recall",
    "bounds-ketchup",
    "bounds-why",
    "bounds-blast-radius",
    "bounds-how",
    "bounds-architect",
    "bounds-unslop",
    "bounds-bro",
    "bounds-help",
    "bounds-automate-me",
    "bounds-grill",
    "bounds-options",
    "bounds-dial",
    "bounds-ui-review",
    "bounds-web-craft",
    "bounds-native-craft",
    "bounds-council",
    "bounds-handoff",
    "bounds-measure",
}


PRIVATE_PATTERNS = (
    (re.compile(r"(?:(?<![\w.])|(?<=/mnt/[a-z]))/(?:Users|home)/(?!\d+\b)[A-Za-z0-9._-]+"), "absolute home path"),
    (re.compile(r"\b[A-Za-z]:\\{1,2}Users\\{1,2}", re.I), "Windows home path"),
    (re.compile(r"\b[\w-]+(?:\.[\w-]+)*\.ts\.net\b"), "tailnet hostname"),
    (re.compile(r"(?<![.\w-])[A-Za-z0-9-]+\.local\b(?!\.\w)"), "local network hostname"),
    (re.compile(r"\b(?:192\.168|10\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])|100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7]))\.\d{1,3}\.\d{1,3}\b"), "private IP address"),
    (re.compile(r"\bf[cd][0-9a-f]{2}(?::[0-9a-f]{0,4}){2,7}", re.I), "private IPv6 address"),
)
EMAIL = re.compile(r"(?<![\w.%+-])(?!git@|noreply@|no-reply@)[A-Za-z0-9._%+-]+@((?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,})")
EXAMPLE_DOMAIN = re.compile(r"(?:^|\.)(?:example\.(?:com|org|net)|[a-z0-9-]+\.(?:example|test|invalid|localhost))$")


def private_details(text):
    """Name generic private-detail patterns; a stored list of real names would itself leak them."""
    found = [label for pattern, label in PRIVATE_PATTERNS if pattern.search(text)]
    if any(not EXAMPLE_DOMAIN.search(domain.lower()) for domain in EMAIL.findall(text)):
        found.append("email address")
    return found


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
    theo_notice = (root / "licenses/Theo-Browne-MIT.txt").read_text()
    emil_notice = (root / "licenses/Emil-Kowalski-MIT.txt").read_text()
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
        if name in TSTACK_NAMES:
            assert theo_notice in license_text, f"{name}: missing tstack upstream notice"
        if name in EMIL_NAMES:
            assert emil_notice in license_text, f"{name}: missing Emil Kowalski upstream notice"
        assert (folder / "NOTICE.md").is_file()
        for path in folder.rglob("*"):
            if path.is_file() and path.name != ".DS_Store":
                try:
                    text = path.read_text()
                except UnicodeDecodeError:
                    raise AssertionError(f"{path.relative_to(root)}: not UTF-8 text; the privacy scan cannot read it")
                leaks = private_details(text)
                assert not leaks, f"{path.relative_to(root)}: private detail ({', '.join(leaks)})"
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
