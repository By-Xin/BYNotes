# Statdiy Notes Blog

使用 `MkDocs + Material` 把 Obsidian 课程笔记发布成 OneNote 风格站点。

## 1. 初始化环境

```bash
cd /home/byxin/File/Statdiy
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

如果 `python3 -m venv` 报错缺少 `ensurepip`，先安装：

```bash
sudo apt install python3.12-venv
```

## 2. 同步所有 Course Notebook

```bash
bash scripts/sync_notebooks.sh
```

默认会同步：

- `/home/byxin/File/Obsidian_BY_ACA/20_StudyNotes/Lectures`

同步规则：

- 仅同步 Markdown 笔记（`*.md`）
- 不同步 `Assets/`
- 不同步 `archive/`
- 自动标准化数学公式块（修复`$$...$$`渲染问题）
- 自动按 Course 生成顶部导航（Notebook Tabs）
- 自动按 Lecture 生成左侧导航

同步后目标目录为：

- `docs/notebooks/<CourseName>/lectures/`

兼容入口（等价于上面的命令）：

```bash
bash scripts/sync_convex_notes.sh
```

## 3. 本地预览

```bash
python3 -m mkdocs serve
```

浏览器打开：`http://127.0.0.1:8000`

## 4. 构建静态文件

```bash
python3 -m mkdocs build
```

构建输出目录：`site/`

## 5. 发布到 GitHub Pages

1. 在 GitHub 创建仓库（例如 `Statdiy`）。
2. 修改 `mkdocs.yml` 里的 `repo_url`、`repo_name`。
3. 推送代码到 `main` 分支。
4. 在仓库 `Settings -> Pages` 中选择 `Build and deployment: GitHub Actions`。
5. push 之前请先在本地执行一次 `bash scripts/sync_notebooks.sh`，确保最新笔记已同步到 `docs/`。
6. push 之后会自动触发 `.github/workflows/deploy.yml` 发布站点。

## 6. 后续更新笔记

每次笔记有更新，执行：

```bash
bash scripts/sync_notebooks.sh
git add .
git commit -m "update notes"
git push
```
