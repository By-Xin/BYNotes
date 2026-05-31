# Note Style SOP

This SOP is the source of truth for future Obsidian/Quartz note cleanup in this
repository. It is intentionally conservative: preserve mathematical content and
change formatting only unless a content edit is explicitly approved.

## Scope

- Applies to public notes under `content/`.
- Excludes `content/backup/**`, `**/archive/**`, `**/assets/**`, and
  `**/Assets/**`.
- Do not split articles, reorder mathematical arguments, rename concepts, or
  rewrite prose for style during a formatting pass.
- Do not use bulk regex/script rewrites for article formatting. Read each note
  manually, identify the role of each block, then make scoped edits.
- Allowed changes: frontmatter, heading normalization, semantic label
  formatting, proof formatting, references blocks, links, image markup,
  captions, and course index organization.

## Frontmatter

Lecture notes should use this shape:

```yaml
---
title: "Lecture 02 - Convexity I"
aliases:
  - "2. Convexity I"
  - "Convexity I"
  - "Convexity-I"
course: "Convex Optimization"
type: "lecture-note"
order: 2
status: "draft"
tags:
  - course/convex-optimization
---
```

For lecture notes, use the `Lecture NN - Title` title format so lecture
numbers do not visually collide with manually numbered section headings. Use
zero-padded single lecture numbers, e.g. `"Lecture 02 - Convexity I"`, and
ranges without padding expansion, e.g. `"Lecture 10-11 - Duality"`. Keep the
old dotted lecture title and unnumbered title in `aliases`.

For ordered topic notes that are not lectures, use zero-padded numeric titles
with the same short-hyphen separator, e.g. `"04 - Modern CNNs"`. Do not prefix
these titles with `Topic 04`, and avoid middle-dot separators in display
titles.

Course indexes should use this shape:

```yaml
---
title: "Convex Optimization"
type: "course-index"
status: "active"
tags:
  - course/convex-optimization
---
```

Do not repeat the page title as a body `#` heading. Quartz renders the page
title from frontmatter.

Use these status values only:

- `draft`: readable but not fully polished.
- `polished`: reviewed after the current SOP was applied.
- `stub`: planned or incomplete note.
- `suspended`: intentionally paused work.

## Course Index Template

Course landing pages should behave as dashboards, not just folders.

```md
Short description of the course or topic collection.

## Notes

| #   | Note                                | Status |
| --- | ----------------------------------- | ------ |
| 1   | [Introduction](./1.Introduction.md) | draft  |

## Concept Map

- Main topic
- Related topic

## References

- Source or text

## Planned Notes

- Planned item
```

Use relative Markdown links in course indexes for Quartz reliability. Obsidian
wikilinks may remain inside article bodies.

## Homepage Recent Updates

The homepage `Recent Updates` section in `content/index.md` is a manually
curated reader-facing summary of recently published note content.

- Keep exactly three entries, newest first.
- Before every homepage commit, count the `<li>` entries in this section. If a
  new entry would create a fourth item, remove the oldest entry in the same
  edit so the published homepage never shows more than three.
- Use the note publish/update date, a topic title, and a short content summary.
- Link to the most relevant course/module pages and notes.
- Describe what the reader can learn from the notes; do not copy git commit
  subjects, hashes, or changelog-style repository maintenance text.
- Organization-only changes should appear here only when they create a clearer
  study path for existing notes.

## Paper Reading Notebooks

Paper reading content uses a separate Explorer group, not a subfolder under an
existing course area.

- Keep `PAPER READING` as a top-level Explorer group in `quartz.layout.ts`,
  parallel to groups such as `STAT FOUNDATIONS AND MORE`, `OPTIMIZATION`, and
  `MACHINE LEARNING AND AI`.
- Create each reading notebook as a root folder under `content/`, with an
  `index.md` landing page. Example: `content/OptimizationReadings/index.md`
  with display title `Optimization Readings`.
- Create each notebook section as a child folder with its own `index.md`.
  Example:
  `content/OptimizationReadings/DecisionFocusedLearning/index.md` with display
  title `Decision-Focused Learning`.
- Put individual paper notes inside the relevant section folder.
- Include the publication venue or publisher and year in each paper note title,
  e.g.
  `End-to-End Decision-Based Cardinality-Constrained Portfolio Optimization (EJOR, Elsevier, 2025)`.
- For a lean seed note, use only the useful essentials: citation, abstract, and
  local reading assets such as slides or PDFs. Add deeper method notes only when
  the user asks for that level of reading.
- Summarize or paraphrase abstracts unless the abstract text is explicitly
  provided for verbatim use.
- Store mirrored reading assets next to the note in a local asset folder such
  as `slides/`, and link them with relative paths, e.g.
  `[Open the mirrored PDF](slides/example.pdf)` and `![[slides/example.pdf]]`.
- Preserve old URLs with `aliases` when moving or renaming paper notes.
- Update the homepage `PAPER READING` Quick Guide when adding a new notebook.
- Add a `Recent Updates` entry only when the paper reading change creates a new
  notebook, section, or useful reader-facing path, and still keep exactly three
  homepage updates.
- Run `node quartz\bootstrap-cli.mjs build` and verify the generated `public/`
  output contains the expected group, notebook, section, and paper title text.

## Article Template

```md
---

...
---

> [!quote] References
>
> - Lecture: ...
> - Reading: ...

## Roadmap

Short outline if it helps the reader.

## Section

Main content.

## Related Notes

- [Related note](./Related-Note.md)
```

Omit `References`, `Roadmap`, or `Related Notes` when they do not add value.

## Semantic Labels

Do not convert definitions, theorems, lemmas, propositions, corollaries, claims,
or examples into callouts. Use compact text labels instead:

```md
**Definition (Convex function).** A function $f$ is convex if ...

**Theorem (Supporting hyperplane theorem).** ...

**Claim (Sublevel set characterization).** ...

**Example (Random walk on $\mathbb{Z}$).** ...

> [!proof]+ Proof
> ...
> $\square$

> [!proof]+ Solution
> ...
```

Use this label taxonomy:

- `**Definition (Name).**`
- `**Theorem (Name).**`
- `**Lemma (Name).**`
- `**Proposition (Name).**`
- `**Corollary (Name).**`
- `**Claim (Name).**`
- `**Example (Name).**`

Approved globally introduced callouts:

- `[!proof]` / `[!proof]+`
- `[!quote] References`
- `[!note] Note: ...`

Existing callouts in a note, such as `[!note]`, `[!warning]`, or `[!danger]`,
may remain. Convert explicit `**Note (...)**` or `> **Note.**` blocks to
`[!note] Note: ...` callouts. Convert `[!example]` blocks to
`**Example (Name).**` labels during a formatting pass. Do not introduce new
non-reference/non-proof/non-note callouts.

Every callout must have an explicit title that identifies the block role. Use a
type prefix when the callout is not self-evident from the title:

```md
> [!quote] References
> ...

> [!proof]+ Proof
> ...

> [!proof]+ Solution
> ...

> [!note] Note: Boundary behavior
> ...

> [!danger] Danger: Common mistake
> ...
```

When converting legacy markers such as `***Definition* (...)**`, preserve the
block text and order. Only normalize the label syntax.

## Proofs

- Formal proofs should use `[!proof]+ Proof` by default. The `+` makes the
  proof collapsible while keeping it expanded on first render.
- If the source text explicitly labels a block as `Proof`, convert it to a
  proof callout. Do not leave `*Proof*`, `**Proof.**`, or `- Proof` markers in
  polished notes.
- Align proof callout indentation with the statement being proved.
  - For a top-level theorem, lemma, proposition, or definition-level claim, use
    a top-level proof callout.
  - For a proof of a bullet or sub-bullet claim, nest the proof callout under
    that bullet with matching indentation, and name the target in the title.
- End formal proofs with `$\square$`.
- Keep proof text in the original order.
- Do not use default-collapsed proof callouts (`[!proof]-`) unless the user
  explicitly asks for collapsed proofs or the article intentionally hides a long
  appendix-style proof.
- Short inline explanations may remain as prose only when they are not labeled
  as proofs.

## Solutions

- Formal solution blocks should use the proof callout template with a Solution
  title: `[!proof]+ Solution`. The `+` makes the solution collapsible while
  keeping it expanded on first render, and the `proof` type keeps the visual
  style aligned with proof blocks.
- If the source text explicitly labels a block as `Solution`, convert that
  whole worked-solution block into a solution callout.
- Align solution callout indentation with the problem or example being solved.
- Keep solution steps, equations, and order unchanged.
- Do not add `$\square$` to solution blocks unless the source already uses it.

Top-level proof:

```md
**Theorem (Weak Duality).** ...

> [!proof]+ Proof
> ...
> $\square$
```

Nested proof for a bullet claim:

```md
- **Claim.** Norms are convex.

  > [!proof]+ Proof of the claim
  > By triangle inequality and homogeneity, ...
  > $\square$
```

Nested proof for a sub-bullet claim:

```md
- For $\ell_p$ norms:
  - **Claim.** The dual norm is $\ell_q$.

    > [!proof]+ Proof of the $\ell_p/\ell_q$ duality claim
    > By Holder's inequality, ...
    > $\square$
```

## Headings

- Do not include a body `#` heading in public notes. Quartz already renders the
  page title from frontmatter, so repeating it in the article body creates a
  duplicate visual title.
- Public note bodies should start with references, roadmap text, or `##`
  sections.
- Use ordered heading levels after the page title: `##`, `###`, and, only when
  needed for local subtopics, `####`.
- Use the lecture-title separator system in frontmatter titles, e.g.
  `title: "Lecture 08 - Topic"`.
- Add visible section numbers manually to article section headings. Do not rely
  on renderer-generated numbering. Use `## 1. Section`, `### 1.1 Subsection`,
  `### 1.2 Subsection`, then `## 2. Section`, etc.
- Do not bold an entire heading unless the bold text is mathematically
  meaningful.
- Prefer concise, descriptive heading text.

## Math

- Inline math: `$...$`.
- Display math must use standalone fences:

```md
$$
\begin{aligned}
...
\end{aligned}
$$
```

- Do not place `$$` on the same line as `\begin{aligned}` or `\end{aligned}`.
- Do not alter equations during formatting passes.

## Figures

- Prefer Markdown image syntax.
- Use raw HTML only when width or layout control is necessary.
- Raw HTML images must be centered explicitly, e.g. `style="display: block;
width: 50%; margin: 1.25rem auto;"`.
- By default, site CSS centers Markdown images and constrains them to a
  comfortable reading width. Do not add width controls unless a specific figure
  needs to be smaller or larger than the default.
- If a figure needs manual sizing, use explicit HTML width or a future shared
  figure class rather than ad hoc surrounding layout.
- Put captions immediately after figures as italic text:

```md
![Alt text](./image.png)

_Figure: Description._
```

- Remote images may remain during formatting passes. Localizing them is a
  separate asset-cleanup task.

## Notebook-Style Code Cells

Use notebook-style cells for small Python examples whose value comes from seeing
both the code and its result inline, such as matrix calculations, random
sampling, toy model outputs, or short numerical checks.

Author notebook cells with fenced code metadata. Do not hand-write visible
`In [1]` or `Out [1]` labels in Markdown; Quartz renders those labels from the
metadata.

````md
```python nb-in=1
import numpy as np

x = np.arange(5)
x.mean()
```

```text nb-out=1
2.0
```
````

Use these cell metadata forms:

- `nb-in=N` for Python input cells.
- `nb-out=N` for normal text output.
- `nb-error=N` for traceback or error output.

The execution number `N` should match between an input cell and its related
output cell. Renumber cells locally within the note or example section. If a
cell is intentionally unexecuted, omit the number, e.g. `nb-in`, so the renderer
can show an empty prompt.

Keep notebook-style examples compact:

- Use them for explanatory examples inside ordinary notes, not for long
  experiments or training logs.
- Prefer 1-3 nearby input/output pairs inside a standard article section.
- If an example becomes long enough to dominate the article, move it to a
  dedicated note and link to it from the main explanation.
- Keep code output static. Do not add client-side Python execution to ordinary
  notes.

Represent output by type:

- Plain stdout or scalar results: use `text nb-out=N`.
- Tracebacks: use `traceback nb-error=N`.
- Tables: prefer Markdown tables or HTML tables after the relevant input cell
  when the output is naturally tabular.
- Plots and arrays rendered as figures: save the image locally and use normal
  figure syntax after the relevant input cell, following the [[#Figures]] rules.

During formatting passes:

- Convert legacy hand-written `**In [N].**` / `**Out [N].**` labels to notebook
  cell metadata when the surrounding blocks clearly form a code/result pair.
- Do not invent outputs that are not present in the source note.
- Do not run or rewrite code unless the task explicitly asks for execution or
  correction.
- Preserve the original code and output text unless a content edit is approved.
- After adding or changing notebook cells, run a Quartz build and preview the
  affected page to confirm the prompts, wrapping, code highlighting, and mobile
  layout are readable.

## Links

- Course indexes should use relative Markdown links.
- Article bodies may use Obsidian wikilinks where they improve authoring.
- Planned future links should appear under `Planned Notes`.
- Keep aliases in frontmatter when renaming or normalizing display titles.

## Visual Style

Quartz visual polish lives in `quartz/styles/custom.scss`.

- Keep styling restrained and readable.
- Proof callouts should be visually quiet.
- Do not add visual boxes around definitions, theorems, lemmas, propositions,
  or corollaries.
- Avoid broad theme rewrites during article cleanup.

## Per-Article Workflow

For each note:

1. Confirm the article path and backup baseline.
2. Normalize frontmatter.
3. Normalize the top-level title and references block.
4. Normalize semantic labels without adding definition/theorem/example callouts.
5. Normalize proof and solution blocks.
6. Normalize notebook-style code cells when code/result pairs are present.
7. Normalize figure syntax, captions, and links.
8. Add or clean `Related Notes` only when useful.
9. Run a Quartz build.
10. Pause for preview and reviewer approval.
11. Commit the single-article change only after approval.

The commit should be narrow enough that one article can be reviewed or reverted
without affecting unrelated notes.

## Pilot Order

Use `content/ConvexOptimization/10-11.Duality.md` as the first pilot article.
It is representative enough to test definitions, lemmas, examples, proofs,
references, and images before applying the SOP to longer notes.
