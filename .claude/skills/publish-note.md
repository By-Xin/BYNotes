# Publish Note

Publish a finished markdown note into the BYNotes Quartz site, strictly
following the repository's agent-grade runbook.

## When to use

The user hands over a note file path (or says "发布" / "publish this note")
targeting the BYNotes site.

## Workflow

1. Read `docs/publishing-runbook.md` and `NOTE_STYLE_SOP.md` IN FULL before
   touching any file.
2. Execute the runbook phases 0–7 in order, literally: copy byte-identical,
   formatting pass under the fidelity contract, verification gates (build
   clean, `katex-error` = 0, census, fidelity diff), wiring (topic index +
   Recent Updates = exactly 3), review pause with the conversion report,
   then commit → push → watch deploy → verify live (200, katex-error 0,
   homepage dispatch).
3. Any gate that does not produce its EXPECTED output: STOP and report.
   Never improvise, never skip a gate, never `git add -A`.

## Hard rules (duplicated here because they are load-bearing)

- The formatting pass changes representation, never content; every diff
  hunk must be class 1 (syntax-mandatory), 2 (KaTeX-mandatory), or
  3 (flagged typo). Class-3 items are listed for the user to veto.
- Statement callouts only in NEW notes; never retrofit old ones.
- `content/index.md` Recent Updates holds EXACTLY three entries.
- `.tex` sources are out of scope (pipeline pilot pending) — ask the user.
