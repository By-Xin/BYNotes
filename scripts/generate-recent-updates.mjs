#!/usr/bin/env node
// Generates recent-updates.json from the hand-curated "Recent Updates" aside in
// content/index.md, so the homepage (By-Xin.github.io) can fetch structured data
// instead of scraping HTML. CI runs this after `npx quartz build`, and the file
// is served at https://by-xin.github.io/BYNotes/recent-updates.json.
//
// On parse failure the script warns and exits 0 without writing: the homepage
// then falls back to scraping the deployed homepage HTML, so a deploy is never
// blocked by this summary file.
//
// Usage: npm run recent-updates   (or: node scripts/generate-recent-updates.mjs [outFile])
// Default outFile: public/recent-updates.json

import { readFileSync, writeFileSync, mkdirSync } from "node:fs"
import { fileURLToPath } from "node:url"
import path from "node:path"

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const indexPath = path.join(repoRoot, "content", "index.md")
const outPath = path.resolve(repoRoot, process.argv[2] ?? path.join("public", "recent-updates.json"))

const source = readFileSync(indexPath, "utf8")

const asideMatch = source.match(
  /<aside\b[^>]*class=["'][^"']*\bhome-updates\b[^"']*["'][^>]*>([\s\S]*?)<\/aside>/i,
)

if (!asideMatch) {
  console.warn("::warning::content/index.md: home-updates aside not found; recent-updates.json not written.")
  process.exit(0)
}

const updates = Array.from(asideMatch[1].matchAll(/<li\b[^>]*>([\s\S]*?)<\/li>/gi)).flatMap(
  (match) => {
    const item = match[1]
    const time = item.match(/<time\b[^>]*datetime=["']([^"']+)["'][^>]*>([\s\S]*?)<\/time>/i)
    const heading = item.match(/<h3\b[^>]*>([\s\S]*?)<\/h3>/i)
    const paragraph = item.match(/<p\b[^>]*>([\s\S]*?)<\/p>/i)
    if (!time || !heading || !paragraph) return []

    const href = paragraph[1].match(/<a\b[^>]*href=["']([^"']+)["']/i)?.[1]
    return [
      {
        date: time[1].trim(),
        displayDate: htmlToText(time[2]),
        title: htmlToText(heading[1]),
        ...(href ? { href: href.trim() } : {}),
        summary: htmlToText(paragraph[1]),
      },
    ]
  },
)

if (updates.length === 0) {
  console.warn("::warning::content/index.md: no parsable updates found; recent-updates.json not written.")
  process.exit(0)
}

const payload = {
  generatedAt: new Date().toISOString(),
  source: "content/index.md",
  updates,
}

mkdirSync(path.dirname(outPath), { recursive: true })
writeFileSync(outPath, JSON.stringify(payload, null, 2) + "\n")
console.log(`Wrote ${updates.length} updates to ${outPath}`)

function htmlToText(html) {
  return html
    .replace(/<[^>]+>/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;|&apos;/g, "'")
    .replace(/\s+/g, " ")
    .replace(/\s+([,.;:!?])/g, "$1")
    .trim()
}
