#!/usr/bin/env node
import fs from "node:fs"
import path from "node:path"
import katex from "katex"

const [input, outFile, manifest] = process.argv.slice(2)
if (!input || !outFile || !manifest)
  throw new Error("Usage: node render.mjs converted.json output.md manifest.json")
const meta = JSON.parse(fs.readFileSync(manifest, "utf8"))
const escapeHtml = (value) =>
  String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
const data = JSON.parse(fs.readFileSync(input, "utf8"))
let body = data.html
data.math.forEach((m, i) => {
  const tex = (m.display ? "" : "\\displaystyle ") + m.tex + (m.number ? `\\tag{${m.number}}` : "")
  const rendered = katex.renderToString(tex, {
    displayMode: m.display,
    throwOnError: true,
    strict: "ignore",
    trust: false,
    output: "htmlAndMathml",
    macros: { ...data.macros },
  })
  body = body.replace(
    `@@MATH${i}@@`,
    m.display ? rendered : `<span class="latex-inline-math">${rendered}</span>`,
  )
})
// Native Markdown headings let Quartz build its TOC and section links.
for (const [depth, number, title, anchor] of data.headings) {
  if (/<|@@/.test(title)) throw new Error("Math/markup in headings needs a reviewed adapter")
  body = body.replace(
    `<h${depth} id="${anchor}">${number}. ${title}</h${depth}>`,
    `\n\n<span id="${anchor}"></span>\n\n${"#".repeat(depth)} ${number}. ${title}\n\n`,
  )
}
// A raw HTML block must not contain blank lines; otherwise Markdown can consume
// the interior as unrelated blocks. Paragraphs already carry explicit <p> tags.
body = body
  .split(/(\n\n(?:<span id="latex-|#{2,4} )[^\n]*\n\n)/)
  .map((s) => (s.startsWith("\n\n") ? s : s.replace(/\n\s*\n/g, "\n")))
  .join("")
const frontmatter = `---
title: ${JSON.stringify(meta.title)}
type: lecture-note
status: draft
cssclasses: [latex-note]
lang: zh-CN
date: ${JSON.stringify(meta.date)}
tags: ${JSON.stringify(meta.tags)}
---

<!-- Generated from LaTeX. Edit the source, not this file. Source SHA256: ${data.source_sha256} -->

<div class="latex-byline">${escapeHtml(meta.byline)}</div>

<nav class="latex-editions" aria-label="Reading formats"><span>LECTURE NOTES</span><a href="./${meta.asset_slug}/${meta.slug}.pdf">Download PDF ↗</a></nav>

`
fs.mkdirSync(path.dirname(outFile), { recursive: true })
fs.writeFileSync(outFile, frontmatter + body + "\n")
fs.writeFileSync(
  path.join(path.dirname(input), "verification.json"),
  JSON.stringify(
    {
      source_sha256: data.source_sha256,
      author_source_sha256: data.author_source_sha256 ?? data.source_sha256,
      corrections_count: data.corrections_count ?? 0,
      counts: data.census,
      math_rendered: data.math.length,
      katex_errors: 0,
      labels: data.labels,
      style_adaptations: [
        "mathds mapped to mathbb for the indicator glyph",
        "Inline math uses displaystyle, matching the source",
      ],
    },
    null,
    2,
  ),
)
console.log(`Rendered ${data.math.length} math expressions to ${outFile}`)
