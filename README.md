# Statdiy README


- GitHub: https://github.com/By-Xin/BYNotes

- Live site: https://by-xin.github.io/BYNotes/

This repository publishes notes with Quartz.

## Content location

- Published notes are under `content/CvxOpt`.

## Markdown writing best practices

Follow these rules to maximize one-pass successful rendering.

1. Filename convention
- Use `NN_Topic.md` style, e.g. `10_Duality.md`.
- Use only `A-Z a-z 0-9 _ - ( )`.
- Do not use special punctuation in filenames (for example `——`).

2. Required top structure
- Start with one top-level heading: `# Title`.
- Use references in this canonical callout form:

```md
> [!info] References
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

## New note publish workflow

1. Create a new note under `content/CvxOpt`, e.g. `10_Duality.md`.
2. Write content following the rules above.
3. Run quick checks:

```bash
rg -n "Lecture Reference|Reading Reference|Book Reference|> Ref:" content/CvxOpt
rg -n '\$\$\\begin\{aligned\}|\\end\{aligned\}\$\$' content/CvxOpt
ls -1 content/CvxOpt | rg "——"
```

4. Local preview:

```bash
npx quartz build --serve
```

5. Publish:

```bash
git add content/CvxOpt README.md
git commit -m "Add note: 10_Duality"
git push origin main
```

6. Verify deployment:
- Workflow: `.github/workflows/deploy.yml`
- Site: `https://by-xin.github.io/BYNotes/`

## Optional: sync from external notes

```bash
cd /Users/xinby/BYNotes
chmod +x scripts/import_convex_notes.sh scripts/make_directory_routes.sh
npm run import:convex
```

## Local preview (Quartz)

```bash
cd /Users/xinby/BYNotes
npm install
npx quartz build --serve
```

Open `http://127.0.0.1:8080`.
