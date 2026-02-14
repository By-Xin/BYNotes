#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def is_fence(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def is_block_math_delim(line: str) -> bool:
    return line.strip() == "$$"


def normalize_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()

    out: list[str] = []
    in_fence = False
    i = 0
    changed = False

    while i < len(lines):
        line = lines[i]

        if is_fence(line):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue

        if in_fence or not is_block_math_delim(line):
            out.append(line)
            i += 1
            continue

        # Ensure a blank line before block math delimiter when needed.
        if out and out[-1].strip() != "":
            out.append("")
            changed = True

        out.append(line)
        i += 1

        # Copy block body until the closing $$.
        while i < len(lines):
            body_line = lines[i]
            out.append(body_line)
            i += 1
            if is_block_math_delim(body_line):
                break

        # Ensure a blank line after closing $$ when needed.
        if i < len(lines) and lines[i].strip() != "":
            out.append("")
            changed = True

    normalized = "\n".join(out)
    if original.endswith("\n"):
        normalized += "\n"

    if changed and normalized != original:
        path.write_text(normalized, encoding="utf-8", newline="\n")
        return True

    return False


def iter_markdown_files(root: Path):
    if root.is_file() and root.suffix.lower() == ".md":
        yield root
        return
    for md in sorted(root.rglob("*.md")):
        if md.is_file():
            yield md


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize display math blocks in markdown files.")
    parser.add_argument("path", type=Path, nargs="+", help="Markdown file or directory")
    args = parser.parse_args()

    total = 0
    changed = 0
    for target in args.path:
        for md_file in iter_markdown_files(target):
            total += 1
            if normalize_file(md_file):
                changed += 1

    print(f"normalized: {changed}/{total} markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
