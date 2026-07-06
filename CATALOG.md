# ConvexOptimization Notes Catalog

This file tracks all notes in the ConvexOptimization directory with version information for manual sync management.

**Last updated:** 2026-07-07 00:08:59

> [!warning] Sync Status Note
> **Chapters 1-12**: The source materials and these notes are NOT fully synchronized. This is a legacy issue that needs manual comparison and reconciliation in the future.
>
> **Chapters 13+**: These should be kept in sync manually going forward.

## File Inventory

| File | Last Modified | Size (bytes) | SHA256 Hash |
|------|---------------|--------------|-------------|
| 2.Convexity-I.md | 2026-07-07 00:06:15 | 25866 | c2df134f53735c756108903ce76feec8ab9b52560ea2afe6fb2a9e65d8361286 |
| 3.Convexity-II.md | 2026-07-07 00:06:15 | 18434 | 4b45ba7ddf7d7bcfe4ba1043519dcfedfd547803f67a902871e47c2358c8c4a0 |
| 4.Canonical-Problem-Forms.md | 2026-07-07 00:06:15 | 12522 | 82b9e0407f3fdf512a04afd84bfcc9908acacdfffe57f8e53710ee1be16c97b7 |
| 5.Gradient-Descent.md | 2026-07-07 00:06:15 | 21313 | 9a7a12b777a10a5ab66d48c9a5dc864f4cb44aa47ef2d343f04a966f81f5355b |
| 6.Subgradient.md | 2026-07-07 00:06:15 | 16941 | a52a7204d5d09c5aa9696eabedb9b8e854b902bf1e6ca42a6dd5748eee6507c7 |
| 7.Subgradient-Methods.md | 2026-07-07 00:06:15 | 16833 | 9e5b279d53aa06f4344bbfc06af51cec84c0a5200d510e6ae5d9ddae4d37f2a4 |
| 8.Proximal-Gradient-Descent.md | 2026-07-07 00:06:15 | 26317 | 55a5491e3b4db33f9970198b6ef0ec0d96f4ba5b4a72a54123bb1d35e9ecfb54 |
| 9.Stochastic-Gradient-Descent.md | 2026-07-07 00:06:15 | 25457 | 18957194529c80b30c30d715556ca4a6f287d36d931d9ce7291a7266e4c3d0ca |
| 10-11.Duality.md | 2026-07-07 00:06:15 | 12056 | 2641219d76230bbf9c8ac8039cbb1391bb666a4142dce9429f6446d33b415afb |
| 12.Optimality-Conditions-for-Constrained-Optimization.md | 2026-07-07 00:06:15 | 45662 | 919ef85e8df5cdec6527bdf7ece960c9b87852552341f73ea54e20ef8f5e800d |
| 13.Duality-Uses-and-Correspondents.md | 2026-07-07 00:06:15 | 24300 | 5e13d05f0af42393a12c71ce887e5f60e9f95c3bff5e3e14e3e06b1f7018a41a |
| 14.Newton-Method.md | 2026-07-07 00:06:15 | 11173 | b7d92f800c0d34175760bb018cf5d627bcd77daa4d07703e486b50da51afc0f8 |
| 15.Barrier-Method.md | 2026-07-07 00:06:15 | 21577 | c23f750ad89af2a3007d602e3b04894926d76cb0ea864fa142c30bae178ee6e1 |
| 16.Primal-Dual-Interior-Point-Methods.md | 2026-07-07 00:06:15 | 18532 | fa8ca5ea9706b491f38bd678a953b7ea4b410d8174668cc271fcad4b8fe061fb |
| 17.Quasi-Newton-Methods.md | 2026-07-07 00:06:15 | 38065 | 9a49b0febb681ac1cbac3e00380b0648601503407c1e332322552fee735a8829 |
| 19.Numerical-Linear-Algebra.md | 2026-07-07 00:06:15 | 36568 | f82321a56b7e2d3573cc9aa6286e42a6da246ec1ce4517801e9e2a76525a77be |
| 20.Coordinate-Descent.md | 2026-07-07 00:06:15 | 14335 | eefcf1c977bba3306523f3b6666771b71ac246d062c2f58d5956687abdecfb78 |
| 21-22.Dual-Decomposition.md | 2026-07-07 00:06:15 | 46640 | 3187faa8e55163af04d5048906296909f2ad586a69e4aeae7cb583369a536661 |
| 23.Frank-Wolfe-Method.md | 2026-07-07 00:06:15 | 18573 | b9068a1d3cf50d83c4b6acab1e62c973a0e01047fc719a4b2740f43cbc5e337a |
| index.md | 2026-07-06 00:16:49 | 2213 | 6ae4f95872b3431e4c0ee446c1ee59dad4dcc716f988b4ed6bac36c1adc19ae9 |

## Usage Instructions

### Manual Sync Workflow
1. When adding/editing notes, update this catalog with new hash and timestamp.
2. Use this catalog to track which files have changed since last sync.
3. Compare hashes to detect content changes.

### Update Catalog
Run `npm run catalog` (i.e. `node scripts/update-catalog.mjs`). It re-inventories the top-level `*.md` files in `content/ConvexOptimization` (thus excluding `Assets` and `archive`) and rewrites the table above plus the **Last updated** stamp.
