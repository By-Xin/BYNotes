# Statdiy (Quartz)

`Statdiy` has been migrated to Quartz and now publishes notes from:

- `/home/byxin/File/Obsidian_BY_ACA/20_StudyNotes/Lectures/ConvexOptimization_CMU`

## Import latest notes

```bash
cd /home/byxin/File/Statdiy
chmod +x scripts/import_convex_notes.sh scripts/make_directory_routes.sh
npm run import:convex
```

## Local preview (Quartz dev server)

```bash
cd /home/byxin/File/Statdiy
npm install
npx quartz build --serve
```

Open `http://127.0.0.1:8080`.

## Local static preview (plain server)

```bash
cd /home/byxin/File/Statdiy
npm run build:plain
python3 -m http.server 8081 -d public
```

Open `http://127.0.0.1:8081`.

## Deploy

GitHub Actions workflow is configured at:

- `.github/workflows/deploy.yml`

Push to `main` to deploy to GitHub Pages.
