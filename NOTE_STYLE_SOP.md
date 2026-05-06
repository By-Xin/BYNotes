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
title: "2. Convexity I"
aliases:
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

For lecture notes, keep the numeric lecture prefix or range in `title`, e.g.
`"10-11. Duality"`. Put unnumbered titles in `aliases`, not in `title`.

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

Use these status values only:

- `draft`: readable but not fully polished.
- `polished`: reviewed after the current SOP was applied.
- `stub`: planned or incomplete note.
- `suspended`: intentionally paused work.

## Course Index Template

Course landing pages should behave as dashboards, not just folders.

```md
# Course Title

Short description of the course or topic collection.

## Notes

| # | Note | Status |
|---|------|--------|
| 1 | [Introduction](./1.Introduction.md) | draft |

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

## Article Template

```md
---
...
---

# Title

> [!quote] References
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

> [!proof] Proof
> ...
> $\square$
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

- `[!proof]`
- `[!quote] References`

Existing callouts in a note, such as `[!note]`, `[!warning]`, or `[!danger]`,
may remain. Convert `[!example]` blocks to `**Example (Name).**` labels during
a formatting pass. Do not introduce new non-reference/non-proof callouts.

Every callout must have an explicit title that identifies the block role. Use a
type prefix when the callout is not self-evident from the title:

```md
> [!quote] References
> ...

> [!proof] Proof
> ...

> [!note] Note: Boundary behavior
> ...

> [!danger] Danger: Common mistake
> ...
```

When converting legacy markers such as `***Definition* (...)**`, preserve the
block text and order. Only normalize the label syntax.

## Proofs

- Formal proofs should use `[!proof] Proof`.
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
- Do not collapse proofs by default.
- Short inline explanations may remain as prose only when they are not labeled
  as proofs.

Top-level proof:

```md
**Theorem (Weak Duality).** ...

> [!proof] Proof
> ...
> $\square$
```

Nested proof for a bullet claim:

```md
- **Claim.** Norms are convex.

  > [!proof] Proof of the claim
  > By triangle inequality and homogeneity, ...
  > $\square$
```

Nested proof for a sub-bullet claim:

```md
- For $\ell_p$ norms:
  - **Claim.** The dual norm is $\ell_q$.

    > [!proof] Proof of the $\ell_p/\ell_q$ duality claim
    > By Holder's inequality, ...
    > $\square$
```

## Headings

- Use exactly one `#` heading per article, matching the page title.
- Use ordered heading levels: `#`, `##`, `###`.
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
- By default, site CSS centers Markdown images and constrains them to a
  comfortable reading width. Do not add width controls unless a specific figure
  needs to be smaller or larger than the default.
- If a figure needs manual sizing, use explicit HTML width or a future shared
  figure class rather than ad hoc surrounding layout.
- Put captions immediately after figures as italic text:

```md
![Alt text](./image.png)

*Figure: Description.*
```

- Remote images may remain during formatting passes. Localizing them is a
  separate asset-cleanup task.

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
5. Normalize proof blocks and proof endings.
6. Normalize figure syntax, captions, and links.
7. Add or clean `Related Notes` only when useful.
8. Run a Quartz build.
9. Pause for preview and reviewer approval.
10. Commit the single-article change only after approval.

The commit should be narrow enough that one article can be reviewed or reverted
without affecting unrelated notes.

## Pilot Order

Use `content/ConvexOptimization/10-11.Duality.md` as the first pilot article.
It is representative enough to test definitions, lemmas, examples, proofs,
references, and images before applying the SOP to longer notes.
