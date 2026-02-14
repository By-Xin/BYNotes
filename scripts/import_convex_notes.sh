#!/usr/bin/env bash
set -euo pipefail

SRC="/home/byxin/File/Obsidian_BY_ACA/20_StudyNotes/Lectures/ConvexOptimization_CMU"
DST="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/content/notebooks/ConvexOptimization_CMU"

mkdir -p "$DST"

# Import only markdown files (keep folder structure, drop non-markdown assets).
rsync -a --delete --prune-empty-dirs \
  --include '*/' \
  --include '*.md' \
  --exclude '*' \
  "$SRC/" "$DST/"

cat > "$DST/index.md" << 'EOF'
---
title: ConvexOptimization_CMU
---

# ConvexOptimization_CMU

Course notes imported from Obsidian.
EOF

cat > "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/content/index.md" << 'EOF'
---
title: Statdiy
---

# Statdiy

- [Convex Optimization CMU](./notebooks/ConvexOptimization_CMU)
EOF

echo "Imported markdown files to: $DST"
