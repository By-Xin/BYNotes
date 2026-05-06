# Obsidian Style Baseline Backup

This directory stores the pre-refresh baseline for the Obsidian/Quartz note
style update started on 2026-05-06.

It contains:

- Active public Markdown notes from `content/`.
- `quartz/styles/custom.scss` before the style update.
- `quartz.config.ts`, `README.md`, and `.prettierignore` before related
  documentation changes.

It intentionally excludes:

- `content/backup/**`
- `**/archive/**`
- `**/assets/**`
- `**/Assets/**`
- generated folders such as `public/`
- dependency folders such as `node_modules/`

The backup is stored at the repository root, outside Quartz's `content/` tree,
so it is tracked by git without being published as site content.
