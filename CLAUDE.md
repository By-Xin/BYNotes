# BYNotes — project instructions

Quartz 4 notes site publishing to <https://by-xin.github.io/BYNotes/>.
`README.md` is the operating manual (publish workflow, self-hosted assets,
deploy chain); `NOTE_STYLE_SOP.md` is the authoritative style guide for note
content. Follow both exactly. The homepage repo (`By-Xin.github.io`) has its
own CLAUDE.md.

For ANY note-publishing task, `docs/publishing-runbook.md` is the mandatory
step-by-step procedure — exact commands, expected outputs, STOP gates.
Follow it literally; if a gate fails, stop and report instead of improvising.

## Publishing a note (checklist)

1. Write under `content/<Topic>/` per NOTE_STYLE_SOP.md. Filenames:
   `N.Title-Words.md`; combined lectures use ranges (`10-11.Duality.md`,
   `21-22.Dual-Decomposition.md`). New notes set theorem-like statements in
   the statement-callout family (one shared quiet box; the callout title
   carries the label; never foldable) — see SOP "Statement Callouts". Never
   retrofit statement callouts into already-published notes.
2. End-of-block markers get OPPOSITE treatment at publish: DELETE every
   `$\diamond$` (statement-end; the callout box already delimits it), KEEP
   every `$\square$` (QED). `grep -rn '\\diamond' content` must be empty —
   see SOP "End-of-Block Markers".
3. Proofread the prose: wrong characters (讲/将), missing characters, doubled
   words, English misspellings, stray edit artifacts. Never "fix" the ASCII
   punctuation, untranslated English terms, or terse phrasing — those are
   house style. See SOP "Pre-Publication Proofreading".
4. Update the topic's `index.md` (notes table / status column where present).
5. Add a "Recent Updates" entry to the aside in `content/index.md` — CI
   parses it into `recent-updates.json` for the homepage.
6. ConvexOptimization notes only: run `npm run catalog` to regenerate
   CATALOG.md.
7. Push to `main`. CI builds, deploys, then notifies the homepage repo via
   `repository_dispatch: bynotes-updated` (secret `HOMEPAGE_DISPATCH_TOKEN`;
   the step skips gracefully if the secret is absent).

## New topic = three sync points

`content/<Topic>/index.md` + the Quick Guide in `content/index.md` + the
explorer groups in `quartz.layout.ts`.

## Renaming or moving a note

Old URLs must keep working. Add a FULL-PATH alias to the note's frontmatter,
e.g. `aliases: [ConvexOptimization/21.Dual-Decomposition]`. Bare aliases
(`21.Dual-Decomposition`) emit their redirect at the SITE ROOT, not next to
the note.

## Self-hosted assets (hard policy)

Google Fonts is blocked and jsDelivr/cdnjs are unreliable in mainland China.
Fonts and KaTeX are vendored into the repo:

- After bumping `@fontsource/*` or `katex`, run `npm run vendor-assets`
  (regenerates `quartz/styles/{fonts,katex}.css` and
  `quartz/static/{fonts,katex-fonts}/`).
- Never reintroduce CDN links. The cdnjs preconnect in
  `quartz/components/Head.tsx` and the jsDelivr KaTeX links in
  `quartz/plugins/transformers/latex.ts` were removed deliberately
  (copy-tex is inlined from node_modules at build).
- Keep `fontOrigin: "local"`. Do NOT switch to `cdnCaching: false`
  build-time font downloads — Node's fetch ignores the system proxy on this
  machine, so local builds would break.

## Wide content must scroll, never clip

`.callout-content` is a CSS grid, and grid items default to `min-width: auto`,
so a `white-space: nowrap` display equation forces the track wider than the
callout and `overflow: hidden` clips it with no scrollbar. `custom.scss` fixes
this with `grid-template-columns: minmax(0, 1fr)` + `> * { min-width: 0 }` —
keep it, and give any future grid/flex wrapper the same treatment. Never
shrink or rewrap an equation to dodge a truncation.

## Known issues / quirks

- Mobile: the `.left.sidebar` top bar overflows ~85px at a 375px viewport
  (PageTitle + HomeBackLink + Search + Darkmode + ReaderMode). Known,
  unfixed.
- A cdnjs mermaid URL remains inside the bundled JS as a dormant lazy
  loader; no note uses mermaid, so it never fires. Vendor mermaid only if
  mermaid diagrams are ever added.
- Helper scripts: `npm run catalog | recent-updates | vendor-assets`.
