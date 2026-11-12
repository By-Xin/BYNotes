# Convex Geometry presentation revision — 2026-11-12

Authorized changes: correct the lecture title, nest proof sketches in Proof
and Proof inside the statement being proved, use Definition selectively, and
repair the right-hand TOC that stopped before the final section.

- Article/PDF title: Convex Geometry and Convex Optimization Foundations.
  Deterministic Operational Research (SJTU, 2026) remains the course index.
  Existing page and download URLs remain valid.
- Removed six broad Definition wrappers: general optimization model, LP and
  standard form, general convex optimization problem, conic optimization
  overview, basic topologies overview, H/V representations overview. Their
  complete text remains as ordinary prose in its original position. Concrete
  mathematical terms retain 31 definition environments.
- Merged each sketch with its corresponding detailed proof into one Proof.
  All 17 Proof toggles now occur inside the theorem/proposition/example they
  establish. Three sketch passages remain within those Proofs. Fifteen original
  QED markers retained; the two proofs without an original marker remain so.
- The TOC list now shrinks to the available sidebar space. Restored its flex
  layout against the desktop visibility utility, fixed the header height, and
  gave the list min-height:0. Actual wheel scrolling reaches 5.7, with the final
  link entirely within the list viewport (scrollTop 997.5, maximum 998).
- No mathematical corrections in this revision. Original/revised Markdown
  and the previous correction ledger are unchanged. Import audit retains all
  1,409 math expressions in order, all 18 image occurrences and source prose.
  The TeX/HTML audit passes; no KaTeX errors or broken local anchors/images.
- Nineteen parser/correction/structure tests pass, including a regression that
  every Proof has a statement ancestor. Desktop 1280px and mobile 375px have
  no visibly clipped article content; proof toggling and TOC scrolling tested.
- PDF rebuilt with unchanged 11pt/1.3 template typography: 42 pages, no text
  outside page bounds. Visually checked title, ordinary introductory text,
  merged Weierstrass proof, projection proof and ending. Poppler's local CJK
  mapping was incomplete, so final visual checks used PyMuPDF instead.
- Full-site integration retains exactly three Recent Updates and the original
  course grouping. Generated Markdown, PDF and LaTeX ZIP updated together.

The published TeX is still the editable authoring document. The note-specific
importer records this reviewed migration; do not rerun over future manual edits.
