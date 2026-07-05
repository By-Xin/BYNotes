#!/usr/bin/env node
// Regenerates the File Inventory table in CATALOG.md for content/ConvexOptimization.
// Only top-level *.md files are inventoried (Assets/ and archive/ subdirectories
// are therefore excluded automatically).
//
// Usage: npm run catalog   (or: node scripts/update-catalog.mjs)

import { createHash } from "node:crypto"
import { readFileSync, writeFileSync, readdirSync, statSync } from "node:fs"
import { fileURLToPath } from "node:url"
import path from "node:path"

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const notesDir = path.join(repoRoot, "content", "ConvexOptimization")
const catalogPath = path.join(repoRoot, "CATALOG.md")

// index.md sorts last; numbered notes sort by leading lecture number.
function noteOrder(name) {
  if (name === "index.md") return 1e9
  const m = name.match(/^(\d+)/)
  return m ? Number(m[1]) : 1e8
}

const files = readdirSync(notesDir)
  .filter((name) => name.endsWith(".md"))
  .sort((a, b) => noteOrder(a) - noteOrder(b) || a.localeCompare(b))

function fmtDate(d) {
  const p = (n) => String(n).padStart(2, "0")
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}:${p(d.getSeconds())}`
}

const rows = files.map((name) => {
  const full = path.join(notesDir, name)
  const buf = readFileSync(full)
  const hash = createHash("sha256").update(buf).digest("hex")
  return `| ${name} | ${fmtDate(statSync(full).mtime)} | ${buf.length} | ${hash} |`
})

const table = [
  "| File | Last Modified | Size (bytes) | SHA256 Hash |",
  "|------|---------------|--------------|-------------|",
  ...rows,
].join("\n")

let catalog = readFileSync(catalogPath, "utf8")

catalog = catalog.replace(/^\*\*Last updated:\*\* .*$/m, `**Last updated:** ${fmtDate(new Date())}`)

const sectionRe = /(## File Inventory\n\n)[\s\S]*?(\n\n## )/
if (!sectionRe.test(catalog)) {
  console.error("CATALOG.md: could not locate the File Inventory section; aborting.")
  process.exit(1)
}
catalog = catalog.replace(sectionRe, `$1${table}$2`)

writeFileSync(catalogPath, catalog)
console.log(`CATALOG.md updated: ${files.length} files inventoried.`)
