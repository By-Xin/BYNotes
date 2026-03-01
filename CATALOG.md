# ConvexOptimization Notes Catalog

This file tracks all notes in the ConvexOptimization directory with version information for manual sync management.

**Last updated:** 2026-03-01 23:24:39

> [!warning] Sync Status Note
> **Chapters 1-12**: The source materials and these notes are NOT fully synchronized. This is a legacy issue that needs manual comparison and reconciliation in the future.
> 
> **Chapters 13+**: These should be kept in sync manually going forward.

## File Inventory

| File | Last Modified | Size (bytes) | SHA256 Hash |
|------|---------------|--------------|-------------|
| 02_Convexity(I).md | 2026-03-01 23:21:50 | 25186 | 99e92f35fb61bfedc7834145cfc4521aa30590ba0c13c1cd2b8870f7da82835b |
| 03_Convexity(II).md | 2026-03-01 23:21:50 | 17658 | facd39d5f70e5ed42160791c6dd093f60b4aeffef84cdae2efa4cf37de1d0f14 |
| 04_CanonicalProblems.md | 2026-03-01 23:21:50 | 12330 | a0d3aaa0457fc41a6dd7a0d02e0255a9f94da7d67e7ac90f35f75aed6e52f990 |
| 05_GradientDescent.md | 2026-03-01 23:21:50 | 20990 | 6aef2a26346a9d75aa145f14b008db23677822f32a6a83771e545deee23b9d8f |
| 06_SubGradient.md | 2026-03-01 23:21:50 | 16365 | 1ddfa57f35f6e296cb7a145159c1027caea6a865871bfd94b59fdf046e33f690 |
| 07_SubGradientMethods.md | 2026-03-01 23:21:50 | 16009 | b8e278606e604d67cfae8b566923b6dbf56ab0632d9928acdab64d46aadb0528 |
| 08_ProximalGradientDescent.md | 2026-03-01 23:21:50 | 25917 | e6ce394aa74a4e9e7004dd696dc8e56bd683fe5c25d06257779d44b95c1b1f78 |
| 09_StochasticGradientDescent.md | 2026-03-01 23:21:50 | 24917 | 2d5b87667c5e86989a4e2f97ce1bad5450b276844d32a6b8763191d5cdc78393 |
| 10-11_Duality.md | 2026-03-01 23:21:50 | 11280 | 697f0c03e170cc78b3faf6585b66e051b8f36ab54c9ddd169eaef15dca9c023f |
| 12_(KKT)OptimalityConditions_NoCvxAssump.md | 2026-03-01 23:24:39 | 44979 | d1ec90e586cbfb657c29c3323cb2723d2ea4a59c6f201cc6f91ea05631e6d0d7 |
| 13_DualityUsesAndCorrespondents.md | 2026-03-01 23:22:09 | 23033 | ee4c7b4301e7f6a2606f7e51205b0c476d1a80b2d60ab1dd330efc445007e6a9 |
| 14_NewtonMethod.md | 2026-03-01 23:22:10 | 10477 | 1d342ca452358888717f41f440f90eed61ec3820f149aba9a992c236d6e18243 |
| index.md | 2026-03-01 23:21:50 | 126 | cef65380b63f4d6bd18e5f310871d2c0e2aa2fd4206d069251ccf089700ba026 |

## Usage Instructions

### Manual Sync Workflow
1. When adding/editing notes, update this catalog with new hash and timestamp
2. Use this catalog to track which files have changed since last sync
3. Compare hashes to detect content changes

### Update Catalog
Run this command to regenerate the catalog:
```bash
cd /Users/xinby/BYNotes/content/ConvexOptimization
echo "# ConvexOptimization Notes Catalog

This file tracks all notes in the ConvexOptimization directory with version information for manual sync management.

**Last updated:** $(date '+%Y-%m-%d %H:%M:%S')

## File Inventory

| File | Last Modified | Size (bytes) | SHA256 Hash |
|------|---------------|--------------|-------------|" > ../../CATALOG.md

for file in $(find . -name "*.md" -not -path "./Assets/*" -not -path "./archive/*" | sort); do
    basename=$(basename "$file")
    timestamp=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$file")
    size=$(stat -f "%z" "$file")
    hash=$(shasum -a 256 "$file" | cut -d' ' -f1)
    echo "| $basename | $timestamp | $size | $hash |" >> ../../CATALOG.md
done

echo "
## Usage Instructions

### Manual Sync Workflow
1. When adding/editing notes, update this catalog with new hash and timestamp
2. Use this catalog to track which files have changed since last sync
3. Compare hashes to detect content changes

### Update Catalog
Run this command to regenerate the catalog:
\`\`\`bash
cd /Users/xinby/BYNotes/content/ConvexOptimization
# [regeneration script would be here]
\`\`\`" >> ../../CATALOG.md
```