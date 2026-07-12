# BYNotes

- GitHub: https://github.com/By-Xin/BYNotes

- Live site: https://by-xin.github.io/BYNotes/

This repository publishes notes with Quartz.

## Content location

- Published notes are organized by topic under `content/<TopicName>`.
- The authoritative topic list lives in `content/index.md` (homepage Quick Guide)
  and `quartz.layout.ts` (sidebar explorer groups). This README intentionally
  does not duplicate it.

## Topic naming rules

- Topic directories use concise PascalCase names under `content/`, e.g. `ConvexOptimization`, `OnlineLearning`.
- Topic landing pages may use longer display titles via `title:` frontmatter in their `index.md`.
- Do not maintain per-topic `CATALOG.md` files unless explicitly requested.

## Markdown writing best practices

For the current repository-wide note style guide, see
[`NOTE_STYLE_SOP.md`](./NOTE_STYLE_SOP.md). That SOP is authoritative for the
Obsidian/Quartz note refresh. Follow these rules to maximize one-pass successful
rendering.

1. Filename convention
- For course notes, use readable blog-style slugs: `N.Title-Words.md`, e.g. `5.Gradient-Descent.md`.
- For combined chapters, keep the numeric range before the dot, e.g. `10-11.Duality.md`.
- Use hyphens between words in filenames; avoid camelCase and underscores for title words.
- Use only `A-Z a-z 0-9 . - ( )`.
- Do not use special punctuation in filenames (for example `——`).

2. Required top structure
- Start with one top-level heading: `# Title`.
- Use references in this canonical callout form:

```md
> [!quote] References
> - Lecture: ...
> - Reading: ...
```

- Do not force fixed keys.
- Keep only source types that actually exist:
- If only lecture exists, keep only `Lecture`.
- If only reading exists, keep only `Reading`.
- If a note has no references, omit the whole block.

3. Math writing (Quartz/KaTeX-safe)
- Inline math: `$...$`.
- Block math must place `$$` on standalone lines:

```md
$$
\begin{aligned}
...
\end{aligned}
$$
```

- Avoid `$$\begin{aligned}` or `\end{aligned}$$` on the same line.

4. Structure and indentation
- Keep heading levels ordered: `#` -> `##` -> `###`.
- Use spaces (not tabs) for list indentation.
- Keep one blank line between major blocks (heading, paragraph, math, callout).

5. Title display behavior
- By default, Quartz displays filename as page title.
- If display title must differ from filename, add frontmatter:

```md
---
title: Display Title
---
```

- If the `title` value contains `:`, wrap it in quotes, e.g. `title: "A: B"`.

## New note publish workflow

> Agents: the mandatory detailed procedure (exact commands, expected
> outputs, verification gates, failure playbook) is
> [`docs/publishing-runbook.md`](./docs/publishing-runbook.md). The steps
> below are the human-readable summary.

1. Choose the target topic directory under `content/<TopicName>`, or create a new one with its own `index.md`. A new topic must also be added to the homepage Quick Guide (`content/index.md`) and the sidebar groups (`quartz.layout.ts`).
2. Create a new note under that topic directory, e.g. `content/ConvexOptimization/10-11.Duality.md` or `content/OnlineLearning/1.Introduction.md`.
3. Write content following the rules above.
4. Add an entry to the "Recent Updates" aside in `content/index.md`. CI turns this aside into `recent-updates.json`, which the homepage (By-Xin.github.io) consumes.
5. If the note is under `content/ConvexOptimization`, refresh the catalog:

```bash
npm run catalog
```

6. Run quick checks on the target topic directory:

```bash
rg -n "Lecture Reference|Reading Reference|Book Reference|> Ref:" content/<TopicName>
rg -n '\$\$\\begin\{aligned\}|\\end\{aligned\}\$\$' content/<TopicName>
ls -1 content/<TopicName> | rg "——"
```

7. Local preview:

```bash
npx quartz build --serve
```

8. Publish:

```bash
git add content/<TopicName> content/index.md CATALOG.md
git commit -m "Add note: 10-11 Duality"
git push origin main
```

9. Verify deployment:
- Workflow: `.github/workflows/deploy.yml` — builds the site, generates `recent-updates.json` (`scripts/generate-recent-updates.mjs`), deploys to GitHub Pages, then notifies the homepage repo `By-Xin/By-Xin.github.io` via `repository_dispatch` (`bynotes-updated`) so its Recent Updates section rebuilds immediately.
- The dispatch step needs a `HOMEPAGE_DISPATCH_TOKEN` repository secret (a fine-grained PAT with Contents read/write on `By-Xin.github.io`). Without the secret the step is skipped gracefully and the homepage falls back to its weekly scheduled rebuild.
- Site: https://by-xin.github.io/BYNotes/

## Self-hosted fonts and KaTeX

- Site fonts (Schibsted Grotesk / Source Sans Pro / IBM Plex Mono) and KaTeX
  CSS + fonts are vendored into the repo — the published site makes no requests
  to Google Fonts or jsDelivr (blocked/unreliable in mainland China).
- After bumping `@fontsource/*` or `katex`, regenerate with:

```bash
npm run vendor-assets
```

This rewrites `quartz/styles/fonts.css`, `quartz/styles/katex.css`,
`quartz/static/fonts/`, and `quartz/static/katex-fonts/`.

## Local preview (Quartz)

```bash
cd BYNotes
npm install
npx quartz build --serve
```

Open `http://127.0.0.1:8080`.
