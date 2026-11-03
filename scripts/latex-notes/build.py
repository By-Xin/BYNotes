#!/usr/bin/env python3
"""Build an isolated BYNotes LaTeX pilot. Never writes into the source or content/."""
import argparse
import base64
from datetime import date
import difflib
import hashlib
import html
import json
import mimetypes
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

from convert import uncomment
from corrections import apply_corrections

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def run(argv, cwd, log, env):
    with log.open("w") as stream:
        proc = subprocess.run(argv, cwd=cwd, env=env, stdout=stream, stderr=subprocess.STDOUT)
    if proc.returncode:
        raise RuntimeError(f"Command failed: {argv[0]}; see {log}\n{log.read_text()[-2500:]}")


def publishing_copy(raw, publish_date):
    """Repair the legacy template's label counters only in the build copy."""
    preamble, body = raw.split(r"\begin{document}", 1)
    for kind in ("lemma", "proposition", "corollary", "theorem", "axiom", "definition", "example", "exercise", "remark"):
        counter = "subsection" + kind
        expected = rf"\newcounter{{{counter}}}[subsection]"
        if expected not in preamble:
            raise ValueError(f"Template changed: missing {expected}. Review the counter adapter.")
        old = rf"\renewcommand{{\the{counter}}}{{{kind.capitalize()}~\thesubsection.\arabic{{{counter}}}}}"
        new = rf"\renewcommand{{\the{counter}}}{{\thesubsection.\arabic{{{counter}}}}}"
        if old in preamble:
            preamble = preamble.replace(old, new)
            preamble = "\n".join(line if r"\renewcommand" in line else line.replace(rf"\the{counter}", rf"{kind.capitalize()}~\the{counter}") for line in preamble.split("\n"))
        elif new not in preamble:
            raise ValueError(f"Unsupported numbering scheme: {counter}")
        preamble = preamble.replace(rf"\stepcounter{{{counter}}}", rf"\refstepcounter{{{counter}}}")
    if r"\numberwithin{figure}{section}" not in preamble or r"\everymath{\displaystyle}" not in preamble:
        raise ValueError("Template profile needs section-numbered figures and displaystyle inline math")
    formatted = publish_date.strftime("%B") + f" {publish_date.day}, {publish_date.year}"
    preamble = preamble.replace(r"\date{\today}", "\\date{" + formatted + "}")
    return preamble + r"\begin{document}" + body


def portable(public, page, meta):
    """Native HTML reading edition: no server, JavaScript, or external font fetch."""
    document = page.read_text()
    article = re.search(r'<article[^>]*>(.*?)</article>', document, re.S)[1]
    # Source assets use paths relative to the original topic page.
    article = article.replace(f'./{meta["asset_slug"]}/', f'./{meta["topic"]}/{meta["asset_slug"]}/')
    css = (public / "index.css").read_text()
    def embed(match):
        url = match[1].strip("\"'")
        if url.startswith("data:"):
            return match[0]
        if "://" in url:
            raise ValueError(f"Portable CSS must not fetch remote assets: {url}")
        path = public / url.lstrip("/")
        if not path.is_file():
            raise ValueError(f"Missing CSS asset: {path}")
        mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
        return f'url("data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}")'
    css = re.sub(r"url\(([^)]+)\)", embed, css)
    links = []
    for level, anchor, text in re.findall(r'<h([234]) id="([^"]+)"[^>]*>(.*?)</h\1>', article, re.S):
        text = re.sub(r'<a\b.*?</a>', '', text, flags=re.S)
        links.append(f'<li class="depth-{level}"><a href="#{anchor}">{text}</a></li>')
    title = html.escape(meta["title"])
    extra = 'body{margin:0;padding:32px 20px;background:var(--light);overflow-x:hidden}.reading-page{max-width:860px;margin:auto}.reading-page>header{display:block;padding-bottom:1rem;border-bottom:1px solid var(--lightgray)}.reading-page>header p{font-size:.9rem;color:var(--gray)}.reading-toc{margin:1rem 0 2rem}.reading-toc summary{cursor:pointer}.reading-toc .depth-3{margin-left:1.2rem}.reading-toc li{margin:.3rem 0}.reading-toc ul{list-style:none;padding:0}@media(max-width:600px){body{padding:20px 16px}}'
    output = f'<!doctype html><html lang="zh-CN" saved-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{css}\n{extra}</style></head><body><main class="reading-page"><header><h1 class="article-title">{title}</h1><p>BYNotes · {meta["date"]}</p><details class="reading-toc"><summary>Contents / 目录</summary><ul>{"".join(links)}</ul></details></header><article class="latex-note">{article}</article></main></body></html>'
    (public / "preview.html").write_text(output)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True, help="Main .tex using the reviewed BY template")
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--workdir", type=Path, required=True, help="New or empty directory")
    args = ap.parse_args()
    source, work = args.source.resolve(), args.workdir.resolve()
    meta = json.loads(args.manifest.read_text())
    for key in ("topic", "slug", "asset_slug"):
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", meta[key]):
            raise ValueError(f"Unsafe or unsupported path segment: {key}")
    if source.name != "main.tex":
        raise ValueError("This profile currently expects main.tex")
    if work == source.parent or source.parent in work.parents:
        raise ValueError("Work directory must be outside the source tree")
    if work.exists() and any(work.iterdir()):
        raise ValueError("Choose a new/empty work directory; existing runs are retained for comparison")
    env = dict(os.environ)
    env["PATH"] = "/Library/TeX/texbin:" + env.get("PATH", "")
    env["BYNOTES_OFFLINE_PREVIEW"] = "1"
    for tool in ("latexmk", "xelatex", "dvisvgm", "node"):
        if not shutil.which(tool, path=env["PATH"]):
            raise ValueError(f"Missing dependency: {tool}")
    snapshot = work / "source"
    snapshot.mkdir(parents=True)
    inputs = {}
    for path in source.parent.rglob("*"):
        relative = path.relative_to(source.parent)
        if path.is_symlink() or any(p.startswith(".") or p in {"build", "node_modules"} for p in relative.parts):
            continue
        if path.is_file() and path.suffix in {".tex", ".bib", ".sty", ".cls", ".png", ".jpg", ".pdf", ".svg"}:
            target = snapshot / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            inputs[str(relative)] = hashlib.sha256(path.read_bytes()).hexdigest()
    (work / "inputs.json").write_text(json.dumps(inputs, indent=2))
    (work / "manifest.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2))
    raw = (snapshot / "main.tex").read_text()
    edition = work / "edition-source"
    shutil.copytree(snapshot, edition)
    corrected = raw
    correction_count = 0
    if meta.get("corrections"):
        ledger = json.loads((args.manifest.resolve().parent / meta["corrections"]).read_text())
        corrected = apply_corrections(raw, ledger)
        correction_count = len(ledger["changes"])
        (work / "corrections.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2))
    (edition / "main.tex").write_text(corrected)
    (work / "content-corrections.patch").write_text("".join(difflib.unified_diff(raw.splitlines(True), corrected.splitlines(True), fromfile="source/main.tex", tofile="edition-source/main.tex")))
    adapted = publishing_copy(corrected, date.fromisoformat(meta["date"]))
    compile_dir = work / "pdf-build"
    shutil.copytree(snapshot, compile_dir)
    (compile_dir / "main.tex").write_text(adapted)
    (work / "publishing-copy.patch").write_text("".join(difflib.unified_diff(corrected.splitlines(True), adapted.splitlines(True), fromfile="edition-source/main.tex", tofile="pdf-build/main.tex")))
    run(["latexmk", "-norc", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", "-outdir=build", "main.tex"], compile_dir, work / "pdf-build.log", env)
    content = work / "content"
    assets = content / meta["topic"] / meta["asset_slug"]
    assets.mkdir(parents=True)
    shutil.copy2(compile_dir / "build/main.pdf", assets / (meta["slug"] + ".pdf"))
    clean = uncomment(adapted)
    preamble, body = clean.split(r"\begin{document}", 1)
    figures = re.findall(r"\\begin\{figure\}(.*?)\\end\{figure\}", body, re.S)
    picture_count = body.count(r"\begin{tikzpicture}")
    if picture_count:
        if sum(f.count(r"\begin{tikzpicture}") for f in figures) != picture_count:
            raise ValueError("Every TikZ picture must be inside a figure in this profile")
        preamble = preamble.replace(r"\usepackage[most]{tcolorbox}", "\\def\\pgfsysdriver{pgfsys-dvisvgm.def}\n\\usepackage[most]{tcolorbox}")
        fig_source = preamble + "\n\\usepackage[active,tightpage]{preview}\n\\PreviewEnvironment{tikzpicture}\n\\begin{document}\n" + "\n".join(r"\begin{figure}" + f + r"\end{figure}" for f in figures) + "\n\\end{document}\n"
        (compile_dir / "figures-svg.tex").write_text(fig_source)
        run(["xelatex", "-no-pdf", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build", "figures-svg.tex"], compile_dir, work / "figures-build.log", env)
        # The template's explicit TikZ bounding boxes omit exterior vertex
        # labels. PDF paints outside those boxes; SVG needs a visible margin.
        run(["dvisvgm", f"--page=1-{picture_count}", "--no-fonts", "--bbox=32", "--output=figure-%p.svg", "build/figures-svg.xdv"], compile_dir, work / "figures-svg.log", env)
        for i in range(1, picture_count + 1):
            shutil.copy2(compile_dir / f"figure-{i}.svg", assets)
    run([sys.executable, str(HERE / "convert.py"), str(edition / "main.tex"), "--output", str(work / "converted.json"), "--assets-url", "./" + meta["asset_slug"], "--assets-dir", str(assets)], REPO, work / "convert.log", env)
    converted = json.loads((work / "converted.json").read_text())
    converted.update(author_source_sha256=inputs["main.tex"], corrections_count=correction_count)
    (work / "converted.json").write_text(json.dumps(converted, ensure_ascii=False, indent=2))
    note = content / meta["topic"] / (meta["slug"] + ".md")
    run(["node", str(HERE / "render.mjs"), str(work / "converted.json"), str(note), str(work / "manifest.json")], REPO, work / "render.log", env)
    (content / "index.md").write_text(f'---\ntitle: BYNotes — LaTeX Preview\n---\n\n[[{meta["topic"]}/{meta["slug"]}|{meta["title"]}]]\n')
    (content / meta["topic"] / "index.md").write_text(f'---\ntitle: {json.dumps(meta["topic_title"], ensure_ascii=False)}\n---\n\n[[{meta["slug"]}|{meta["title"]}]]\n')
    run(["node", "quartz/bootstrap-cli.mjs", "build", "-d", str(content), "-o", str(work / "public")], REPO, work / "quartz-build.log", env)
    portable(work / "public", work / "public" / meta["topic"] / (meta["slug"] + ".html"), meta)
    run([sys.executable, str(HERE / "audit.py"), str(work)], REPO, work / "audit.log", env)
    # Verify that compilation and copying left all author inputs unchanged.
    for relative, digest in inputs.items():
        if hashlib.sha256((source.parent / relative).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Source changed during the build: {relative}; rerun from a stable snapshot")
    print(f'Built: {work / "public/preview.html"}')
    print(f'PDF: {assets / (meta["slug"] + ".pdf")}')
    print("Source hashes unchanged. Review verification.json, publishing-copy.patch and browser layout before promotion.")


if __name__ == "__main__":
    main()
