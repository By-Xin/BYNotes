#!/usr/bin/env python3
"""Cross-check source structure, retained prose, PDF labels, and output links."""
import argparse
from collections import Counter
from html.parser import HTMLParser
import html
import json
from pathlib import Path
import re
from convert import BLOCKS, Parser, walk, uncomment
from corrections import apply_corrections


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.images = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and (a.get("href") or "").startswith("#") and a["href"] != "#":
            self.refs.append(a["href"][1:])
        if tag == "img":
            self.images.append(a["src"])


def normalized(s):
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def audit(work):
    data = json.loads((work / "converted.json").read_text())
    meta = json.loads((work / "manifest.json").read_text())
    original = (work / "source/main.tex").read_text()
    edition_path = work / "edition-source/main.tex"
    edition = edition_path.read_text() if edition_path.exists() else original
    expected_edition = apply_corrections(original, json.loads((work / "corrections.json").read_text())) if (work / "corrections.json").exists() else original
    if edition != expected_edition:
        raise ValueError("Edition differs from the reviewed correction ledger")
    raw = uncomment(edition)
    body = raw.split(r"\begin{document}", 1)[1].split(r"\end{document}", 1)[0]
    expected = Counter(re.findall(r"\\begin\{([^}]+)\}", body))
    structural = set(BLOCKS) | {"proof", "solution", "figure", "tikzpicture", "tabular", "enumerate", "itemize"}
    errors = []
    for kind in structural:
        if expected[kind] != data["census"].get(kind, 0):
            errors.append(f"Structure mismatch: {kind}")
    footnotes = len(re.findall(r"\\(?:footnote|note)\{", body))
    if footnotes != data["census"].get("footnotes", 0):
        errors.append("Footnote count mismatch")
    plain = normalized(re.sub(r"<[^>]+>", "", data["html"]))
    chunks = [normalized(n.value) for n in walk(Parser(body).parse()) if n.kind == "text" and len(normalized(n.value)) >= 15]
    missing = [s for s in chunks if s not in plain]
    errors.extend("Missing prose: " + s[:90] for s in missing)
    aux = (work / "pdf-build/build/main.aux").read_text()
    pdf_labels = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]+)\}", aux))
    for label, (number, anchor) in data["labels"].items():
        if pdf_labels.get(label) != number:
            errors.append(f"PDF/web label differs: {label}: {pdf_labels.get(label)} vs {number}")
    page_path = work / "public" / meta["topic"] / (meta["slug"] + ".html")
    page = Page()
    page.feed(page_path.read_text())
    duplicates = [key for key, count in Counter(page.ids).items() if count > 1]
    errors.extend("Duplicate ID: " + key for key in duplicates)
    errors.extend("Broken anchor: " + key for key in page.refs if key not in page.ids)
    for url in page.images:
        if not (page_path.parent / url).is_file():
            errors.append("Missing image: " + url)
    if "katex-error" in page_path.read_text() or "@@MATH" in page_path.read_text():
        errors.append("Unrendered math")
    report = {"passed": not errors, "structure_counts": {k:expected[k] for k in sorted(structural) if expected[k]}, "prose_chunks_checked":len(chunks), "footnotes":footnotes, "pdf_web_labels_matched":len(data["labels"]), "anchor_links_checked":len(page.refs), "images":len(page.images), "errors":errors, "limitations":"Structural and retained-prose checks; not a mathematical correctness audit or a substitute for visual comparison."}
    (work / "audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("workdir", type=Path)
    audit(parser.parse_args().workdir.resolve())
