#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${1:-public}"

if [[ ! -d "$ROOT_DIR" ]]; then
  echo "Directory not found: $ROOT_DIR" >&2
  exit 1
fi

# Duplicate foo.html to foo/index.html so plain static servers can resolve extensionless links.
while IFS= read -r -d '' html; do
  rel="${html#$ROOT_DIR/}"
  base="$(basename "$rel")"

  if [[ "$base" == "index.html" || "$base" == "404.html" ]]; then
    continue
  fi

  dir_rel="${rel%.html}"
  out_dir="$ROOT_DIR/$dir_rel"
  mkdir -p "$out_dir"
  cp -f "$html" "$out_dir/index.html"
done < <(find "$ROOT_DIR" -type f -name "*.html" -print0)

echo "Directory routes created under: $ROOT_DIR"
