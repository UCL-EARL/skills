#!/usr/bin/env python3
"""Validate repository-level branding, governance, paths, and local links."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_HOMEPAGE = "https://github.com/UCL-ERL/skills"
REQUIRED_PATHS = (
    ".github/CODEOWNERS",
    "agent-instructions/README.md",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "CONTRIBUTORS.md",
    "GOVERNANCE.md",
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "docs/catalog.md",
)
TEXT_SUFFIXES = {".cff", ".json", ".md", ".py", ".txt", ".yml", ".yaml"}
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_ASSET_RE = re.compile(r"(?:src|srcset)=\"([^\"]+)\"")
PRIVATE_PATH_RE = re.compile(r"(?:/Users/[^/\s]+|/home/[^/\s]+|[A-Za-z]:\\Users\\[^\\\s]+)")


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / item.decode() for item in result.stdout.split(b"\0") if item]


def local_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]

    if not target or target.startswith("#"):
        return None
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, flags=re.IGNORECASE):
        return None
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    if catalog.get("homepage") != EXPECTED_HOMEPAGE:
        errors.append(f"catalog.homepage must be {EXPECTED_HOMEPAGE}")

    instruction_root = ROOT / "agent-instructions"
    instruction_index = (instruction_root / "README.md").read_text(encoding="utf-8")
    instruction_profiles = sorted(
        path for path in instruction_root.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    if not instruction_profiles:
        errors.append("agent-instructions must contain at least one profile")

    for profile in instruction_profiles:
        targets = [
            profile / filename
            for filename in ("AGENTS.md", "CODEX.md")
            if (profile / filename).is_file()
        ]
        if len(targets) != 1:
            errors.append(
                f"instruction profile {profile.name} must contain exactly one AGENTS.md or CODEX.md"
            )
            continue

        index_target = f"./{profile.name}/{targets[0].name}"
        if index_target not in instruction_index:
            errors.append(f"instruction profile missing from index: {index_target}")

    legacy_markers = ("UCL-" + "RAI", "github.com/UCL-" + "RAI")
    legacy_brand_pattern = re.compile(
        r"\bE" + r"ARL\b|Embodied Autonomy|UCL-E" + r"ARL|earl-lab",
        flags=re.IGNORECASE,
    )
    for path in tracked_files():
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path == Path(__file__).resolve():
            continue

        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")

        for marker in legacy_markers:
            if marker.casefold() in text.casefold():
                errors.append(f"legacy branding in {relative}: {marker}")

        legacy_brand = legacy_brand_pattern.search(text)
        if legacy_brand:
            errors.append(f"legacy branding in {relative}: {legacy_brand.group(0)}")

        private_path = PRIVATE_PATH_RE.search(text)
        if private_path:
            errors.append(f"private absolute path in {relative}: {private_path.group(0)}")

        if path.suffix.lower() != ".md":
            continue

        raw_targets = MARKDOWN_LINK_RE.findall(text) + HTML_ASSET_RE.findall(text)
        for raw_target in raw_targets:
            target = local_target(raw_target)
            if target is None:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repository in {relative}: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"missing local link target in {relative}: {raw_target}")

    if errors:
        for error in sorted(set(errors)):
            print(f"error: {error}")
        return 1

    print("repository ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
