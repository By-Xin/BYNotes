# Deterministic Operational Research (SJTU, 2026)

Lecture 1: Convex Geometry and Convex Optimization Foundations. Notes by
Baiying, according to lectures by Prof. Guohua Wan.

## Editable LaTeX

`main.tex` is the complete, editable XeLaTeX document. Keep `tex/` and
`figures/` beside it. Compile with TeX Live and the original Decision Theory
template's fonts:

```sh
latexmk -norc -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The PDF retains 11pt and `\linespread{1.3}`. The smaller sans-serif body and
15% tighter line-height are web CSS settings only. Statement and proof font
families on the web retain the Decision Theory profile.

## Reviewed import, 2026-11-06

- `original.md`: byte-identical snapshot of the supplied `lect1_ConvexOptimization.md`.
- `corrections.json`: 93 exact replacement operations, each with its reason,
  original source line, occurrence count and source hash. Multiple operations
  may concern the same line; apply them in order.
- `revised.md` and `corrections.patch`: the resulting minimally revised copy
  and complete diff. The Obsidian original was not edited.
- `template.tex`: reviewed Decision Theory preamble, with this note's title,
  attribution, frozen date, label-counter repair, no-QED proof variant, and
  minimum example-block page-break space. PDF font size/spacing are unchanged.
- `body.tex`: imported body, also inlined in `main.tex` for portability.
- `structure.json`: manually reviewed semantic ranges and image inventory.
- `import-audit.json`: preservation check of math order, prose and QED markers.
- `assets.json`: original image URLs, byte counts and SHA-256 checksums.

From the repository root, the one-note importer reproduces the initial TeX:

```sh
node scripts/latex-notes/import-operational-research.mjs
python3 scripts/latex-notes/test_operational_research.py
python3 scripts/latex-notes/build.py \
  --source sources/deterministic-operational-research/main.tex \
  --manifest scripts/latex-notes/deterministic-operational-research.json \
  --workdir ../latex-pilot/operational-research-next
```

**After editing `main.tex` directly, do not rerun the importer over it.** The
importer is a recorded migration, not a two-way editor. Future LaTeX revisions
should use the publishing pipeline directly. To redo the Markdown import,
review the new snapshot, rebase the correction ledger and every semantic
range, and regenerate into a separate review copy first.

See [release review](../../docs/releases/2026-11-06-deterministic-operational-research.md)
and [publishing SOP](../../docs/latex-publishing-sop.md).
