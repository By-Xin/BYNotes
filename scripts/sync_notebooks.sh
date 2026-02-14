#!/usr/bin/env bash
set -euo pipefail

SOURCE_ROOT="${1:-/home/byxin/File/Obsidian_BY_ACA/20_StudyNotes/Lectures}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS_DIR="$ROOT_DIR/docs"
NOTEBOOKS_DIR="$DOCS_DIR/notebooks"
MKDOCS_FILE="$ROOT_DIR/mkdocs.yml"

if [[ ! -d "$SOURCE_ROOT" ]]; then
  echo "Source root does not exist: $SOURCE_ROOT" >&2
  exit 1
fi

mkdir -p "$NOTEBOOKS_DIR"

# Clean old notebooks to avoid stale pages.
find "$NOTEBOOKS_DIR" -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

shopt -s nullglob
course_dirs=("$SOURCE_ROOT"/*)
if [[ ${#course_dirs[@]} -eq 0 ]]; then
  echo "No course folders found under: $SOURCE_ROOT" >&2
  exit 1
fi

for course_dir in "${course_dirs[@]}"; do
  [[ -d "$course_dir" ]] || continue
  course_name="$(basename "$course_dir")"
  target_course_dir="$NOTEBOOKS_DIR/$course_name"
  target_lecture_dir="$target_course_dir/lectures"
  mkdir -p "$target_lecture_dir"

  # Sync only markdown lecture files, excluding large attachments and archived drafts.
  rsync -a --delete --delete-excluded \
    --exclude='archive/***' \
    --exclude='Assets/***' \
    --include='*.md' \
    --exclude='*' \
    "$course_dir/" "$target_lecture_dir/"

  find "$target_lecture_dir" -type d -empty -delete
done

python3 - "$NOTEBOOKS_DIR" <<'PY'
from pathlib import Path
import sys

notebooks_dir = Path(sys.argv[1])
for course_dir in sorted([p for p in notebooks_dir.iterdir() if p.is_dir()], key=lambda p: p.name.lower()):
    index_file = course_dir / "index.md"
    course_name = course_dir.name
    index_file.write_text(
        (
            f"# {course_name}\n\n"
            "这是该课程（Notebook）的目录页。\n\n"
            "- 左侧栏：按 lecture 跳转\n"
            "- 右侧栏：当前页面 TOC\n"
        ),
        encoding="utf-8",
    )
PY

python3 "$ROOT_DIR/scripts/normalize_math_delimiters.py" "$NOTEBOOKS_DIR"
python3 "$ROOT_DIR/scripts/normalize_math_blocks.py" "$NOTEBOOKS_DIR"
python3 "$ROOT_DIR/scripts/convert_math_blocks_to_fences.py" "$NOTEBOOKS_DIR"

python3 - "$NOTEBOOKS_DIR" "$MKDOCS_FILE" <<'PY'
from pathlib import Path
import re
import sys

notebooks_dir = Path(sys.argv[1])
mkdocs_file = Path(sys.argv[2])
start_marker = "  # AUTO_NOTEBOOK_NAV_START"
end_marker = "  # AUTO_NOTEBOOK_NAV_END"

def q(text: str) -> str:
    return "'" + text.replace("'", "''") + "'"

def display_title(md_path: Path) -> str:
    stem = md_path.stem
    text = stem.replace("_", " ")
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def natural_key(path_obj: Path):
    text = str(path_obj).lower()
    return [int(token) if token.isdigit() else token for token in re.split(r"(\d+)", text)]

lines = []
for course_dir in sorted([p for p in notebooks_dir.iterdir() if p.is_dir()], key=lambda p: p.name.lower()):
    course_name = course_dir.name
    lines.append(f"  - {q(course_name)}:")
    lines.append(f"      - {q('Notebook Home')}: {q(f'notebooks/{course_name}/index.md')}")
    lines.append(f"      - {q('Lectures')}:")

    lecture_files = sorted(
        [p for p in (course_dir / "lectures").rglob("*.md") if p.is_file()],
        key=natural_key,
    )
    if not lecture_files:
        lines.append(f"          - {q('No lecture notes yet')}: {q(f'notebooks/{course_name}/index.md')}")
        continue

    for md_file in lecture_files:
        rel_from_docs = md_file.relative_to(notebooks_dir.parent).as_posix()
        lines.append(f"          - {q(display_title(md_file))}: {q(rel_from_docs)}")

text = mkdocs_file.read_text(encoding="utf-8")
if start_marker not in text or end_marker not in text:
    raise SystemExit("mkdocs.yml is missing AUTO_NOTEBOOK_NAV markers.")

before, rest = text.split(start_marker, 1)
middle, after = rest.split(end_marker, 1)
new_text = before + start_marker + "\n" + "\n".join(lines) + "\n" + end_marker + after
mkdocs_file.write_text(new_text, encoding="utf-8")
PY

echo "Synced notebooks:"
echo "  from: $SOURCE_ROOT"
echo "  to:   $NOTEBOOKS_DIR"
