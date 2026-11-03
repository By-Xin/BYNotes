# LaTeX notes → BYNotes SOP

Validated pilot: **Advanced Microeconomics — Decision Theory**, 2026-11-03.
Production release: 2026-11-04, with explicitly authorized minimal corrections;
see [release review](releases/2026-11-04-decision-theory.md).
This is a working template-specific publishing path, not a general LaTeX converter.
The author keeps editing LaTeX; HTML and PDF are generated editions.

## Authority and scope

Explicit user instructions take priority. The fidelity contract in
`NOTE_STYLE_SOP.md` still applies. This document supplies the LaTeX-specific
exceptions to Markdown formatting, and replaces phases 1–3 of
`docs/publishing-runbook.md` for supported `.tex` input. The runbook's topic,
homepage, recent-updates, release, and deployment checks still apply when
actually promoting a note into the site.

The pilot is a local preview. Successful generation does not by itself publish
or commit anything. Follow the scope authorized in the current conversation.

Supported profile: the author's XeLaTeX/ctex template with `defblock`,
`thmblock`, `axiomblock`, `lemmablock`, `propositionblock`, `exampleblock`,
subsection counters, section-numbered figures, and inline `\displaystyle`.
The entry file is currently named `main.tex`. Sections and prose must be in
that file; preamble/macro inputs can be separate. Tested: nested proofs,
footnotes, ordinary lists, rectangular tables, equation/display math,
references, and TikZ inside figures. Bibliography commands, body `\input`,
custom list labels, novel environments, and different counter schemes need
an explicit adapter and a new validation pass. Do not silently drop them.

## Preserve the authoring source

- Work from a byte-identical snapshot, with SHA-256 for all copied inputs.
- Never edit the Obsidian original as a side effect of publishing.
- Do not translate, condense or rearrange arguments. Correct mathematics only
  within the user's explicit authorization for the current note.
- When authorized, record minimal corrections in a source-hash-bound JSON
  ledger (`id`, exact before/after, reason, source line, occurrence count),
  named by the manifest's `corrections` field. Apply it to `edition-source/`
  before both PDF and HTML generation. Preserve `source/` byte-for-byte,
  `content-corrections.patch`, and the independent template-only patch.
  Stop on a changed source hash or ambiguous context; review/rebase the ledger
  rather than silently dropping corrections. Never treat one note's permission
  as blanket permission for mathematical edits to future notes.
- Record suspected mathematical errors separately. Mechanical template fixes
  belong in a build copy and an inspectable patch.
- The legacy template used `\stepcounter` in custom blocks; labels could pick
  up the preceding section rather than the block. The build adapter changes
  this to `\refstepcounter`, separates type names from numeric counter values,
  and keeps the displayed block title. PDF and web label values must agree.
- Freeze `\today` in the build copy to the manifest date; preserve the source.

## Run a fresh preview

Dependencies: Node/npm dependencies installed for BYNotes, Python 3.9+,
TeX Live with XeLaTeX, latexmk and dvisvgm. The build uses subprocess argument
arrays and an empty work directory outside the source. TeX is run without
shell-escape. Inputs are assumed to be the author's trusted local source.

From the BYNotes repository root:

```bash
python3 scripts/latex-notes/build.py \
  --source /Users/byxin/Documents/Obsidian_BY_ACA/AM/main.tex \
  --manifest scripts/latex-notes/decision-theory.json \
  --workdir ../latex-pilot/decision-theory-next
python3 scripts/latex-notes/test_convert.py
python3 scripts/latex-notes/test_corrections.py
python3 scripts/latex-notes/audit.py ../latex-pilot/decision-theory-next
```

For another note, copy and edit the manifest: title, attribution/byline, topic,
topic title, page slug, asset directory, date, and tags. Preserve the source's
attribution. The script accepts simple ASCII path segments; expand that
validation deliberately if a different naming convention is required.

The work directory contains:

- `source/`, `inputs.json`: fidelity baseline and hashes.
- `edition-source/`, `corrections.json`, `content-corrections.patch`: the
  explicitly reviewed content corrections, applied identically to both editions.
- `pdf-build/`, `publishing-copy.patch`: adapted build and exact template diff.
- `content/<topic>/<slug>.md`: generated Quartz entry, not an editing source.
- `content/<topic>/<asset_slug>/`: PDF and outlined SVG diagrams.
- `public/`: complete isolated Quartz site.
- `public/preview.html`: standalone reading edition; double-click to open.
  Fonts/CSS are embedded; keep its neighboring topic directory for PDF/SVG.
- `verification.json`, `audit.json`, build logs: evidence, not a substitute
  for visual review.

To inspect the actual Quartz layout, serve `public/` on loopback and open
`/<topic>/<slug>.html`. Stop the owned test server after QA. The standalone
reading edition remains usable without a server. To share it as a bundle,
retain the directory structure (for example zip the entire `public/`).

`BYNOTES_OFFLINE_PREVIEW=1` disables only social-card generation, which can
fetch remote fonts despite locally hosted reading fonts. Normal production
builds keep social cards enabled.

## Rendering decisions

- Use the opt-in `cssclasses: [latex-note]` profile. Existing notes keep their
  existing styles. This profile intentionally preserves the source's blue
  definitions, pink statements, grey examples, Termes/Song body text,
  Pagella headings, and italic Latin/Kai Chinese in statement bodies.
- Preserve the full document and its numbering. Native Markdown headings
  feed Quartz's TOC; stable `latex-*` anchors serve LaTeX references.
- Proofs remain inside their original parent blocks and are expanded native
  `<details>` elements. The end-of-proof square remains visible.
- Footnotes get globally unique web numbers, backlinks, and are placed at
  their containing block's end, or document end for ordinary body footnotes.
  This adapts page/minipage footnotes without dropping content.
- Remove only a standalone line containing `$\diamond$` as an end marker,
  per the existing SOP. Preserve mathematical diamonds in running text.
- Keep TeX math content; KaTeX must throw on unsupported input. `\mathds`
  currently maps to `\mathbb` (indicator glyph shape can differ). Web math
  uses KaTeX fonts rather than claiming pixel-identical TeX typography.
- TikZ uses XeLaTeX's XDV path with `pgfsys-dvisvgm.def`, then dvisvgm with
  outlined glyphs. Do not use the default PDF-special driver for SVG: it can
  exit successfully while losing lines/arrows. Verify every diagram visually.
  The pilot's explicit TikZ bounding rectangles omit exterior vertex labels;
  SVG export adds a 32pt margin so they remain visible. Inspect new diagrams
  for adequate bounds. Image dimensions reserve layout space before lazy load.
- Long formulas/tables scroll in their own containers. Never solve overflow
  by clipping or shrinking the whole document. Mobile figures stack.

## Fonts

Reading fonts and licenses live in `quartz/static/latex-fonts/`. The supplied
subsets cover this pilot. For additional notes, regenerate from the **union**
of all LaTeX note sources, so new glyphs are added without removing old ones:

```bash
# In a Python environment with fonttools[woff] installed:
python3 scripts/latex-notes/fonts.py /path/to/first/source /path/to/second/source \
  --output quartz/static/latex-fonts
```

`kpsewhich` must be on PATH. The script uses local TeX Live originals, subsets
and renames them to BYNotes families, and writes WOFF2. Retain the included
license and attribution files. Browser fallback fonts are a fallback, not a
replacement for checking the new note's glyph coverage.

## Acceptance checks

1. Conversion exits without unsupported constructs; all math renders.
2. Audit matches source counts for blocks, proofs, lists, tables, figures and
   footnotes; long literal prose fragments remain; all PDF/web labels agree;
   no duplicate IDs, missing images, broken anchors or math placeholders.
3. Inspect build warnings. Undefined references and overfull content require
   resolution; document harmless package notices separately.
4. Compare source/build PDF and HTML at the beginning, middle and end. Inspect
   every figure, representative tables, nested proof, footnote/backlink,
   numbered equations and custom notation. Counts alone do not prove fidelity.
5. Check desktop and 375px mobile, light and dark. No visible content may be
   clipped. Test actual overflow scrolling, proof toggle and reference jumps.
   KaTeX's intentionally hidden MathML is an accessibility layer, not clipping.
6. Open the standalone edition and test its native TOC/proofs and relative
   PDF/SVG paths. A short-lived server URL is not the persistent deliverable.
7. Report adjustments and remaining limitations honestly. A rendering pass is
   not an audit of the mathematical claims.

Only then promote generated Markdown/assets into the real `content/`, update
the topic index/catalog/sidebar/homepage as required by the publishing
runbook, and perform the full-site build/release checks. Do not manually edit
generated HTML to repair content: fix the adapter or authorized source copy,
then regenerate.
