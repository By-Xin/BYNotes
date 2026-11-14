# LaTeX web reading typography — 2026-11-14

The author reported both imported articles as oversized, sparse, visually
inconsistent and uncomfortable to read, and explicitly requested sans-serif
statement/proof bodies with italics only for actual emphasis.

Reference: ordinary Subgradient Methods note, measured in the same preview:
15px Source Sans Pro/system sans-serif, 25.2px paragraph line-height (1.68),
570px article width at the desktop viewport. Existing custom.scss confirms
that the 15px base is shared by ordinary Markdown notes.

Both Decision Theory and Convex Geometry now use:

- 15px body with consistent 24px line-height (1.6) in prose, lists, blocks and
  proofs, including mobile. The old profile mixed 1.5725/1.428 paragraph rules.
- Site sans-serif body fonts throughout; site sans-serif heading font for
  headings and block titles. Removed the Termes/Song/Kai/Pagella font switches
  and blanket italic in statement/proof labels. Explicit source em remains.
- Paragraph spacing 0.6em (9px), tighter list paragraphs, 0.7rem/0.9rem box
  padding, 1rem between boxes, reduced heading/edition/figure/table whitespace.
  Article title 32px desktop / 25.6px mobile; headings retain a clear hierarchy.
- Compact inline math using KaTeX's normal textstyle; the renderer no longer
  injects displaystyle into every inline expression. Explicit source style
  commands and all display equations are preserved. Inline wrappers use 1.2
  line-height with compensating paint padding/margins to protect math accents
  and descenders while maintaining compact text lines.
- Existing semantic colors, proof toggles, footnotes, table/figure links and
  overflow scrolling retained.

Before editing the renderer, reproduced both published Markdown files exactly
from their source-hash-matched converted.json snapshots. Re-rendered those same
inputs afterward. All prose outside KaTeX is byte-identical after parsing;
all 1,186 + 1,409 formula annotations match, removing only the old automatic
inline displaystyle prefix. All structure, QED and proof counts are retained.
Decision Theory has 19 Proofs/19 QEDs; Convex Geometry has 17 Proofs/15 QEDs.
No TeX, PDF, source ZIP, mathematical claim or other note was edited.

Validation: full Quartz build, 19 existing Python tests and one new Node
regression for compact inline math plus preserved explicit styles. Visual and
computed-style checks cover both articles, desktop/mobile, light/dark, proof
controls and long formula overflow. Historical fonts/licenses remain in the
repository; the current stylesheet no longer loads the unused TeX font families.
