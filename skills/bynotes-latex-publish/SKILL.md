---
name: bynotes-latex-publish
description: 将用户的 LaTeX 学术笔记转换为 BYNotes/Quartz 网页与 PDF，保留原稿风格、公式、证明和 TikZ 图，并验证本地预览。适用于发布或更新已有 LaTeX note；不用于普通 Markdown 清理、解题或论文改写。
---

# BYNotes LaTeX Publishing

Use the existing BYNotes repository and its source-preserving LaTeX profile.
The tested local checkout is `/Users/byxin/Documents/academic-page/BYNotes`;
locate the user's actual checkout if it moved rather than creating a new site.

Read `docs/latex-publishing-sop.md` in the repository, then the relevant
sections of `NOTE_STYLE_SOP.md`. For promotion/deployment, also read
`docs/publishing-runbook.md`. These files and `scripts/latex-notes/` are the
maintained implementation; avoid duplicating their instructions in this skill.

## Workflow

- Inspect the main source and included preamble/macros. Check whether it uses
  the supported BY XeLaTeX template; do not present the adapter as universal.
- Preserve the author's source. Use a fresh external work directory and
  manifest. Start with `scripts/latex-notes/build.py --help`; the
  `decision-theory.json` manifest is a working example, not mandatory metadata.
- Generate the complete document, PDF, vector figures, Quartz preview and
  standalone reading edition. Keep the source style opt-in via `latex-note`.
- Run the parser tests and `audit.py`, then visually compare PDF and web.
  Inspect all diagrams, references, footnotes, desktop/mobile overflow and
  proof toggles. Source counts and passing KaTeX alone are insufficient.
- Unknown constructs or changed numbering need an explicit adapter and
  verification. Fix the cause; never silently discard content or approximate
  a diagram with a different mathematical meaning.
- Report template changes separately from suspected source mathematics.
  Corrections to mathematical claims require the user's intended scope.
  If explicitly authorized, use a per-note, source-hash-bound correction
  ledger and apply it before both PDF and web generation. Keep before/after,
  reasons and a separate patch; verify the changed calculation/direction.
  Rebase the ledger when the author edits the source. Permission for this
  Decision Theory release is not blanket permission for future notes.
- Deliver a persistent local reading file/PDF and concise verification
  evidence. Stop test servers after QA. Promote or deploy only within the
  current request's authorization, following the existing publishing runbook.

## Important lessons from the pilot

- Custom block labels require `\refstepcounter`; separating the type name
  from numeric counter representation keeps prose references correct.
  Adapt only the build copy and preserve its diff.
- For TikZ SVG use the dvisvgm PGF driver and XDV. A successful conversion
  with ignored PDF specials can still omit geometry, so inspect the images.
- Web fonts are local subsets. Add new glyphs from the union of published
  sources, retaining licenses. Avoid a network font dependency for readers.
- The parser intentionally supports a limited profile. The SOP identifies
  known adapters and unsupported constructs. Expand from real source needs,
  not speculative universal TeX support.
