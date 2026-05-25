#!/usr/bin/env node

import { createServer } from "node:http"
import { spawn } from "node:child_process"
import path from "node:path"
import { existsSync } from "node:fs"
import { fileURLToPath } from "node:url"
import serveHandler from "serve-handler"

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const publicDir = path.join(repoRoot, "public")
const contentIndex = path.join(publicDir, "static", "contentIndex.json")
const sitePort = Number(process.env.SITE_PORT || process.env.PORT || 8080)
const qaPort = Number(process.env.QA_PORT || 7860)

if (!existsSync(contentIndex)) {
  console.error("Missing public/static/contentIndex.json. Run `npm run build:local` first.")
  process.exit(1)
}

const qaEnv = {
  ...process.env,
  PORT: String(qaPort),
  QA_CONTENT_INDEX: process.env.QA_CONTENT_INDEX || contentIndex,
  QA_PUBLIC_BASE_URL: process.env.QA_PUBLIC_BASE_URL || `http://localhost:${sitePort}`,
  QA_ALLOWED_ORIGINS:
    process.env.QA_ALLOWED_ORIGINS || `http://localhost:${sitePort},http://127.0.0.1:${sitePort}`,
}

const qaProcess = spawn(process.execPath, ["qa-api/server.mjs"], {
  cwd: repoRoot,
  env: qaEnv,
  stdio: ["ignore", "pipe", "pipe"],
})

qaProcess.stdout.on("data", (chunk) => process.stdout.write(chunk))
qaProcess.stderr.on("data", (chunk) => process.stderr.write(chunk))

const staticServer = createServer((req, res) => {
  return serveHandler(req, res, {
    public: publicDir,
    cleanUrls: true,
    trailingSlash: false,
  })
})

staticServer.listen(sitePort, () => {
  console.log(`BYNotes static site: http://localhost:${sitePort}`)
  console.log(`BYNotes QA API:      http://localhost:${qaPort}/api/qa`)
  console.log("Press Ctrl+C to stop both servers.")
})

function shutdown() {
  staticServer.close()
  qaProcess.kill("SIGTERM")
}

process.on("SIGINT", shutdown)
process.on("SIGTERM", shutdown)

qaProcess.on("exit", (code) => {
  if (code && code !== 0) {
    console.error(`QA server exited with code ${code}`)
    process.exitCode = code
  }
  staticServer.close()
})
