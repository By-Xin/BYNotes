#!/usr/bin/env bash
set -euo pipefail

SRC="/home/byxin/File/Obsidian_BY_ACA/20_StudyNotes/Lectures/ConvexOptimization_CMU"
DST="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/content/CvxOpt"

mkdir -p "$DST"

# Import only markdown files (keep folder structure, drop non-markdown assets).
rsync -a --delete --prune-empty-dirs \
  --exclude 'Assets/***' \
  --exclude 'archive/***' \
  --include '*/' \
  --include '*.md' \
  --exclude '*' \
  "$SRC/" "$DST/"

cat > "$DST/index.md" << 'EOF'
---
title: Convex Optimization - CMU - Fall18
---

# Convex Optimization - CMU - Fall18

Course notes imported from Obsidian.
EOF

cat > "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/content/index.md" << 'EOF'
---
title: Statdiy
---

# Statdiy

- [Convex Optimization CMU](./CvxOpt)
EOF

echo "Imported markdown files to: $DST"
