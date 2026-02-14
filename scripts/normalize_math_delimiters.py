#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


FENCE_RE = re.compile(r"^\s*(```|~~~)")
QUOTE_PREFIX_RE = re.compile(r"^(\s*(?:>\s*)*)")


def is_fence(line: str) -> bool:
    return bool(FENCE_RE.match(line))


def quote_prefix(line: str) -> str:
    return QUOTE_PREFIX_RE.match(line).group(1)


def iter_markdown_files(root: Path):
    if root.is_file() and root.suffix.lower() == ".md":
        yield root
        return
    for md in sorted(root.rglob("*.md")):
        if md.is_file():
            yield md


def normalize_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    out: list[str] = []
    in_fence = False
    changed = False

    for line in lines:
        if is_fence(line):
            in_fence = not in_fence
            out.append(line)
            continue

        if in_fence or "$$" not in line:
            out.append(line)
            continue

        prefix = quote_prefix(line)
        content = line[len(prefix):]
        stripped = content.strip()

        # Standalone single-line display block: $$ ... $$
        m_single = re.fullmatch(r"\$\$(.+)\$\$", stripped)
        if m_single:
            expr = m_single.group(1).strip()
            if expr:
                out.append(f"{prefix}$$")
                out.append(f"{prefix}{expr}")
                out.append(f"{prefix}$$")
                changed = True
                continue

        # Single-line display block followed by sentence text:
        # $$ ... $$ tail
        m_single_tail = re.fullmatch(r"\$\$(.+)\$\$\s*(\S.*)", stripped)
        if m_single_tail:
            expr = m_single_tail.group(1).strip()
            tail = m_single_tail.group(2).strip()
            out.append(f"{prefix}$$")
            out.append(f"{prefix}{expr}")
            out.append(f"{prefix}$$")
            out.append(f"{prefix}{tail}")
            changed = True
            continue

        # Opening delimiter and content on the same line: $$...
        m_open = re.fullmatch(r"\$\$(.+)", stripped)
        if m_open and "$$" not in m_open.group(1):
            expr = m_open.group(1).rstrip()
            out.append(f"{prefix}$$")
            out.append(f"{prefix}{expr}")
            changed = True
            continue

        # Closing delimiter with trailing sentence text: ...$$ tail
        m_close_tail = re.fullmatch(r"(.+)\$\$\s*(\S.*)", stripped)
        if m_close_tail and not stripped.startswith("$$"):
            expr = m_close_tail.group(1).rstrip()
            tail = m_close_tail.group(2).strip()
            out.append(f"{prefix}{expr}")
            out.append(f"{prefix}$$")
            out.append(f"{prefix}{tail}")
            changed = True
            continue

        # Closing delimiter appended at line end: ...$$
        m_close = re.fullmatch(r"(.+)\$\$", stripped)
        if m_close and not stripped.startswith("$$"):
            expr = m_close.group(1).rstrip()
            out.append(f"{prefix}{expr}")
            out.append(f"{prefix}$$")
            changed = True
            continue

        # Inline block math inside a sentence: keep inline by using single dollars.
        m_inline = re.fullmatch(r"(.*\S)\s*\$\$(.+)\$\$\s*(\S.*)", line)
        if m_inline:
            left, expr, right = m_inline.groups()
            out.append(f"{left} ${expr.strip()}$ {right}")
            changed = True
            continue

        out.append(line)

    normalized = "\n".join(out)
    if original.endswith("\n"):
        normalized += "\n"

    if changed and normalized != original:
        path.write_text(normalized, encoding="utf-8", newline="\n")
        return True

    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize malformed $$ delimiters in markdown files.")
    parser.add_argument("path", type=Path, nargs="+", help="Markdown file or directory")
    args = parser.parse_args()

    total = 0
    changed = 0
    for target in args.path:
        for md_file in iter_markdown_files(target):
            total += 1
            if normalize_file(md_file):
                changed += 1

    print(f"delimiter-normalized: {changed}/{total} markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
