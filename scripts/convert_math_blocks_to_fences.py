#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


FENCE_RE = re.compile(r"^\s*(```|~~~)")
BLOCK_MATH_RE = re.compile(r"^(\s*(?:>\s*)*)\$\$\s*$")


def is_fence(line: str) -> bool:
    return bool(FENCE_RE.match(line))


def iter_markdown_files(root: Path):
    if root.is_file() and root.suffix.lower() == ".md":
        yield root
        return
    for md in sorted(root.rglob("*.md")):
        if md.is_file():
            yield md


def normalize_content_prefix(content_line: str, prefix: str) -> str:
    # If the line repeats the same markdown prefix (indent / blockquote marker),
    # drop one prefix level inside the math fence to keep formula text clean.
    if prefix and content_line.startswith(prefix):
        return content_line[len(prefix):]
    return content_line


def convert_file(path: Path) -> bool:
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

        if in_fence:
            out.append(line)
            i += 1
            continue

        m = BLOCK_MATH_RE.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        prefix = m.group(1)
        i += 1
        block_lines: list[str] = []
        closed = False

        while i < len(lines):
            current = lines[i]
            if BLOCK_MATH_RE.match(current):
                closed = True
                i += 1
                break
            block_lines.append(normalize_content_prefix(current, prefix))
            i += 1

        if not closed:
            # Unmatched $$, keep original content untouched.
            out.append(line)
            out.extend(block_lines)
            break

        out.append(f"{prefix}```math")
        out.extend(block_lines)
        out.append(f"{prefix}```")
        changed = True

    converted = "\n".join(out)
    if original.endswith("\n"):
        converted += "\n"

    if changed and converted != original:
        path.write_text(converted, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert $$ display math blocks to ```math fences.")
    parser.add_argument("path", type=Path, nargs="+", help="Markdown file or directory")
    args = parser.parse_args()

    total = 0
    changed = 0
    for target in args.path:
        for md_file in iter_markdown_files(target):
            total += 1
            if convert_file(md_file):
                changed += 1

    print(f"fence-converted: {changed}/{total} markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
