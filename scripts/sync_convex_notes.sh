#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_ROOT="${1:-/home/byxin/File/Obsidian_BY_ACA/20_StudyNotes/Lectures}"

echo "sync_convex_notes.sh is deprecated. Use scripts/sync_notebooks.sh instead."
exec "$ROOT_DIR/scripts/sync_notebooks.sh" "$SOURCE_ROOT"
