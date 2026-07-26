# Note Publishing Runbook — follow literally

This is the mandatory, step-by-step procedure for publishing a note to
BYNotes. It is written so that ANY agent, regardless of capability, can
execute it correctly: every phase has exact commands, the EXPECTED output,
and a STOP rule. If a check does not produce the expected output, STOP and
report to the user — do not improvise, do not skip a gate, do not "fix
forward".

Authority order: explicit user instruction > this runbook >
`NOTE_STYLE_SOP.md` (style authority) > `README.md` (background). Read
`NOTE_STYLE_SOP.md` in full before phase 2.

Scope: markdown source notes handed over by the user. Out of scope: `.tex`
sources (a pipeline design exists but its pilot has not run — ASK THE USER,
do not improvise) and the homepage repo `By-Xin.github.io` (own CLAUDE.md).

---

## Phase 0 — Preflight

```bash
cd /Users/xinby/BYNotes
git fetch origin
git status -sb | head -5
```

EXPECTED: first line exactly `## main...origin/main` (no `[behind N]`, no
`[ahead N]`), and no staged/modified files unrelated to your task.

- If `[behind N]`: run `git pull --ff-only origin main`, then re-check.
- If unrelated dirty files: STOP, report them, ask the user.
- Determine from the user's request: (a) source file path; (b) target topic
  directory; (c) whether the topic already exists under `content/`. A new
  topic requires phase 5b (three sync points).

## Phase 1 — Copy byte-identical

Target filename per SOP: course notes `N.Title-Words.md` (ranges like
`10-11.Duality.md`); only `A-Z a-z 0-9 . - ( )` characters.

```bash
cp "<SOURCE_PATH>" "content/<TOPIC>/<FILENAME>.md"
diff "<SOURCE_PATH>" "content/<TOPIC>/<FILENAME>.md" && echo IDENTICAL
```

EXPECTED: `IDENTICAL` (diff prints nothing). STOP if any diff output.

From here on, edit ONLY the copy. The source file stays untouched and
remains the fidelity baseline. NOTE: the user may still be editing the
source in Obsidian — the copy is a snapshot; if an Edit later fails to
match, re-read the copy (not the source).

## Phase 2 — Formatting pass (style: NOTE_STYLE_SOP.md)

THE FIDELITY CONTRACT (non-negotiable): this pass changes REPRESENTATION,
never CONTENT. Every diff line vs the source must fall into exactly one of:

1. Syntax-mandatory (frontmatter, label/callout syntax, heading/list/blank
   line normalization required for rendering);
2. KaTeX-mandatory (math changed only so it renders — see playbook §P2/P3;
   the mathematical expression itself must be preserved);
3. Flagged typo fix (only OBVIOUS typos; every single one must be listed in
   the conversion report for the user to veto).

Anything that fits none of these classes is FORBIDDEN without explicit user
approval: no rewording, no reordering, no invented names, no summarizing, no
"improvements". Awkward prose stays as written.

Ordered checklist (details in the SOP sections named):

1. Frontmatter (SOP "Frontmatter"). Lecture note template:

   ```yaml
   ---
   title: "Session NN - <Title>"        # or "Lecture NN - <Title>" per course
   aliases:
     - "<N>. <Title>"
     - "<Title>"
   course: "<Course Name>"
   type: "lecture-note"
   order: <N>
   status: "draft"
   tags:
     - course/<course-slug>
   ---
   ```

   Reading/paper note: `title` + `status: "draft"` + `tags: [reading/papers]`
   minimum. Quote the title if it contains `:`.
2. Delete the body `# H1` (frontmatter title renders it).
3. Speaker/date/reference blockquote at top → `> [!quote] References` callout.
4. Statement blocks — NEW notes only (SOP "Statement Callouts"): convert
   `***Theorem N* (Name)**:` flat labels and `> ***Lemma N* (Name)**`
   blockquote statements into the statement-callout family
   (`[!theorem] [!lemma] [!proposition] [!corollary] [!definition]
   [!assumption] [!claim] [!remark] [!construction]`). The TITLE carries the
   full label (`Lemma 4 (Name)`). NEVER add `+`/`-` fold suffixes to
   statement callouts. `Example` stays a text label `**Example (Name).**`.
   NEVER retrofit statement callouts into already-published notes.
5. Proofs (SOP "Proofs"): `*Proof*.` blocks → `> [!proof]+ Proof`, body
   lines prefixed `> `, end `$\square$`. Nested proofs get matching
   indentation and a named title.
6. End-of-block markers (SOP "End-of-Block Markers"). The draft uses two, and
   they get OPPOSITE treatment — do not confuse them:
   - `$\square$` (QED, ends a proof) → **KEEP every one**.
   - `$\diamond$` (ends a statement block) → **DELETE every one**. Remove the
     whole line, `>` prefix and all; if that leaves two consecutive blank
     lines, delete the spacer line above it too.

   ```bash
   grep -n '\\diamond' "content/<TOPIC>/<FILENAME>.md"
   ```

   EXPECTED: no output. STOP if a hit remains (unless it is a genuine
   `\diamond` binary operator inside an equation — those stay).
7. Algorithms (SOP "Algorithm and Pseudocode Blocks") when present.
8. Math fences: `$$` on standalone lines; never same-line with
   `\begin{aligned}` / `\end{aligned}`.
9. Figures (SOP "Figures"): remote images may remain; captions as italic
   text after the image.
10. Proofreading pass (SOP "Pre-Publication Proofreading"). Read the PROSE
    line by line and fix only these five classes: A wrong character
    (这一章**讲**考虑 → 这一章**将**考虑), B missing character (下给出 →
    下面给出), C duplicated word (缺点是在于 → 缺点在于), D English
    misspelling (excees → excess), E stray editing artifact (若即 → 若记).
    NEVER "fix" ASCII punctuation in Chinese prose, untranslated English
    terms, Chinese/Latin spacing, terse phrasing, or anything inside `$...$`
    — all of those are house style. Every fix is a class 3 change and MUST be
    listed line by line in the conversion report. A suspected MATH or FACTUAL
    error is not a proofreading fix: report it, do not change it.

Editing gotchas (these cause most failures):

- Before editing near a line, check for trailing whitespace — old_string
  must match bytes exactly:

  ```bash
  grep -nE ' +$' "content/<TOPIC>/<FILENAME>.md" | head -20
  ```

- If an Edit reports "string not found": re-read that region of the file and
  copy the exact bytes; do not retry blind.

## Phase 3 — Verification gates (ALL must pass BEFORE commit)

```bash
npx quartz build 2>&1 | tail -3
```

EXPECTED: ends with `Done processing NNN files in ...`. STOP on any error.
(`LaTeX-incompatible input ... newLineInDisplayMode` warnings are benign.)

```bash
P="public/<TOPIC>/<FILENAME-WITHOUT-.md>.html"
test -f "$P" && echo BUILT
grep -co 'katex-error' "$P"
```

EXPECTED: `BUILT`, then `0`. If not 0, extract the failing expression and
fix per playbook §P2/P3, rebuild, re-check.

Census (structure survived the conversion):

```bash
echo "callouts in source:"; grep -c '^> \[!' "content/<TOPIC>/<FILENAME>.md"
echo "callouts rendered:"; grep -o 'data-callout="[a-z]*"' "$P" | sort | uniq -c
```

EXPECTED: rendered counts per type match what you converted in phase 2.
Display-equation spot check: pick 2–3 equations from the source at random
and confirm they appear in `$P` (grep a distinctive substring).

Marker gate (SOP "End-of-Block Markers"):

```bash
grep -c 'square' "$P"; grep -co 'diamond' "$P"
```

EXPECTED: the square count matches the number of proofs you converted; the
diamond count is `0`. STOP on any diamond.

Clipped-content gate (SOP "Wide Content Must Scroll, Never Clip"). Open the
built page in the browser at desktop width AND at a 375px viewport, then run
in the console:

```js
[...document.querySelectorAll('article, article *')].filter(el => {
  const o = getComputedStyle(el).overflowX
  return (o === 'hidden' || o === 'clip') && el.scrollWidth - el.clientWidth > 2
})
```

EXPECTED: `[]` at both widths. A non-empty result means a container is hiding
content the reader cannot scroll to — most often a wide display equation
inside a callout. Fix it in `quartz/styles/custom.scss`, never by shrinking or
rewrapping the equation. STOP and report rather than editing the math.

Fidelity diff (the contract check):

```bash
diff "<SOURCE_PATH>" "content/<TOPIC>/<FILENAME>.md"
```

Walk EVERY hunk and assign it class 1/2/3 from phase 2. Any hunk that fits
no class → revert it. Then write the conversion report (template at the end
of this runbook).

## Phase 4 — Wiring

1. Topic index `content/<TOPIC>/index.md`: add a row to the Notes table
   (number, relative link, status `draft`). Remove the note from "Planned
   Notes" if listed there.
2. Homepage Recent Updates in `content/index.md`: add the new entry at the
   TOP of the `<ol>` (a `<li>` with `<time datetime="YYYY-MM-DD">`, an
   `<h3>`, and a `<p>` describing what the reader can learn, with links) and
   DELETE the oldest entry in the same edit. Then verify:

   ```bash
   grep -o '<time datetime="20[0-9-]*"' content/index.md | wc -l
   ```

   EXPECTED: exactly `3`. STOP if any other number.
3. ConvexOptimization notes only: `npm run catalog`.
4. Rebuild after wiring: `npx quartz build 2>&1 | tail -2` → must end clean.

## Phase 5b — New topic only (three sync points)

A new `content/<TOPIC>/` requires ALL THREE, in one commit:

1. `content/<TOPIC>/index.md` — course-index frontmatter + Notes table +
   Concept Map + References + Planned Notes (SOP "Course Index Template").
2. Quick Guide in `content/index.md` — add the topic link under the correct
   group section.
3. `quartz.layout.ts` — append the topic dir name to the matching group's
   `children` array in `explorerGroups`.

## Phase 6 — Review pause

Present to the user: the conversion report + anything you were unsure about.
WAIT for approval before committing — UNLESS the user already said to
publish directly in this conversation (e.g. "发布", "都准备好就提交部署吧").

## Phase 7 — Commit, deploy, verify live

Stage ONLY intended paths. NEVER `git add -A` / `git add .`; `public/` must
never be committed.

```bash
git add "content/<TOPIC>" content/index.md            # + quartz.layout.ts and CATALOG.md only if touched
git status --short
```

EXPECTED: only your intended files staged (`A`/`M` in first column); nothing
unexpected. Then:

```bash
git commit -m "Add note: <Title>"
git push origin main
RUN=$(gh run list --limit 1 --json databaseId -q '.[0].databaseId')
gh run watch "$RUN" --exit-status --interval 20 2>&1 | tail -2
gh run view "$RUN" --json conclusion -q '.conclusion'
```

EXPECTED: `success`. If failure, see playbook §P1.

Live verification (note: canonical note URLs have NO trailing slash):

```bash
curl -s -o /dev/null -w "%{http_code}\n" "https://by-xin.github.io/BYNotes/<TOPIC>/<FILENAME-WITHOUT-.md>"
curl -s "https://by-xin.github.io/BYNotes/<TOPIC>/<FILENAME-WITHOUT-.md>" | grep -co 'katex-error'
curl -s "https://by-xin.github.io/BYNotes/" | grep -oc "<distinctive words from your Recent Updates h3>"
gh run list -R By-Xin/By-Xin.github.io --limit 1
```

EXPECTED: `200`, `0`, `1`, and a `bynotes-updated` `repository_dispatch` run
(queued/in_progress/success) on the homepage repo. All four green = done.
Report the live URL to the user.

## Playbook — known failures and fixes

- **P1. Pages deploy fails "Deployment failed, try again later"** — GitHub
  transient. `gh run rerun <RUN_ID> --failed`. Do not change any code.
- **P2. KaTeX `\tag` errors** — `\tag` must sit AFTER `\end{aligned}`, never
  inside; a tag argument parses in TEXT mode, so subscripts/`$` inside need
  re-entering math: write `\tag{$\mathrm{P}_x$}`, never `\tag{P_x}` or
  `\tag{P$_x$}`.
- **P3. Finding a katex-error** — extract the exact failing expression:
  `python3 -c` over the built HTML grepping `katex-error` `title=` attribute,
  or search the page for `katex-error` and read its `title`. Fix ONLY the
  rendering syntax; the mathematical content must not change.
- **P4. Edit "string not found"** — trailing spaces or the file changed.
  `grep -nE ' +$' <file>`, re-read the exact region, retry with exact bytes.
- **P5. Live URL 404 but deploy green** — you probably added a trailing
  slash. Note pages are flat `...<slug>` (also reachable as `<slug>.html`).
- **P6. `newLineInDisplayMode` build warnings** — benign, ignore.
- **P7. Recent Updates count ≠ 3** — you forgot to delete the oldest entry
  (or deleted two). Fix before commit; this is a hard invariant.

## Conversion report template (phase 3 output, shown to user in phase 6)

```
## Conversion report — <FILENAME>
Class 1 (syntax-mandatory): frontmatter added; H1 removed; N statement
  callouts; N proof callouts; references callout; N $\diamond$ markers
  removed, N $\square$ kept.
Class 2 (KaTeX-mandatory): <each math syntax change, with line refs, or NONE>
Class 3 (typo fixes — veto any): <line N: "before" → "after" [class A-E], ...,
  or NONE>
Flagged, NOT changed (needs your call): <suspected math/factual issues, or NONE>
Out-of-contract changes: NONE            <- must literally be NONE
Gates: build ✓ · katex-error 0 ✓ · census ✓ · diamonds 0 ✓ · no clipped
  content @1280 and @375 ✓ · fidelity diff walked ✓ · Recent Updates = 3 ✓
```

## Definition of done

- [ ] Phase 0–5 executed in order, all EXPECTED outputs matched
- [ ] `$\diamond$` count is 0; every `$\square$` preserved
- [ ] Proofreading pass run; no clipped content at desktop or 375px
- [ ] Conversion report written; every diff hunk classified 1/2/3
- [ ] User approved (or had pre-authorized publishing)
- [ ] Deploy `success`; live URL 200; live katex-error 0; homepage dispatch
      fired
- [ ] Live URL reported to the user
