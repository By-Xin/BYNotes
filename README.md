# OptOpt README


- GitHub: https://github.com/By-Xin/BYNotes

- Live site: https://by-xin.github.io/BYNotes/

This repository publishes notes with Quartz.

## Content location

- Published notes are organized by topic under `content/<TopicName>`.
- Current topics include `content/ConvexOptimization`, `content/DeepLearning`,
  `content/OnlineLearning`, `content/ProbabilityTheory`,
  `content/StatisticalInference`, `content/StatisticalLearningAlgorithms`, and
  `content/StochasticProcess`.

## Topic naming rules

- Topic directories use concise PascalCase names under `content/`, e.g. `ConvexOptimization`, `OnlineLearning`.
- Topic landing pages may use longer display titles in `index.md`.
- The display title for `content/OnlineLearning` is `Online Learning and Online Convex Optimization`.
- The display title for `content/ProbabilityTheory` is `Probability Theory`.
- The display title for `content/StatisticalInference` is `Statistical Inference`.
- The display title for `content/StatisticalLearningAlgorithms` is `Statistical Learning Algorithms`.
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

1. Choose the target topic directory under `content/<TopicName>`, or create a new one with its own `index.md`.
2. Create a new note under that topic directory, e.g. `content/ConvexOptimization/10-11.Duality.md` or `content/OnlineLearning/1.Introduction.md`.
3. Write content following the rules above.
4. Run quick checks on the target topic directory:

```bash
rg -n "Lecture Reference|Reading Reference|Book Reference|> Ref:" content/<TopicName>
rg -n '\$\$\\begin\{aligned\}|\\end\{aligned\}\$\$' content/<TopicName>
ls -1 content/<TopicName> | rg "——"
```

5. Local preview:

```bash
npx quartz build --serve
```

6. Publish:

```bash
git add content/<TopicName> content/index.md README.md
git commit -m "Add note: 10-11 Duality"
git push origin main
```

7. Verify deployment:
- Workflow: `.github/workflows/deploy.yml`
- Site: `https://by-xin.github.io/BYNotes/`


## Local preview (Quartz)

```bash
cd /Users/xinby/BYNotes
npm install
npx quartz build --serve
```

Open `http://127.0.0.1:8080`.
