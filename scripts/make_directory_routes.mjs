#!/usr/bin/env node

import { mkdir, copyFile } from "node:fs/promises"
import { readdir } from "node:fs/promises"
import path from "node:path"

const root = path.resolve(process.argv[2] || "public")

async function* walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name)
    if (entry.isDirectory()) {
      yield* walk(fullPath)
    } else if (entry.isFile()) {
      yield fullPath
    }
  }
}

let count = 0

for await (const htmlPath of walk(root)) {
  if (!htmlPath.endsWith(".html")) continue

  const base = path.basename(htmlPath)
  if (base === "index.html" || base === "404.html") continue

  const relative = path.relative(root, htmlPath)
  const routeDir = path.join(root, relative.slice(0, -".html".length))
  await mkdir(routeDir, { recursive: true })
  await copyFile(htmlPath, path.join(routeDir, "index.html"))
  count += 1
}

console.log(`Directory routes created under ${root} (${count} pages)`)
