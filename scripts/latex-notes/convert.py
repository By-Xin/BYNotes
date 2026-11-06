#!/usr/bin/env python3
"""Strict converter for the BY XeLaTeX note template, not a general TeX engine.

Parses balanced groups/environments and retains math verbatim. Unknown body
commands fail closed. See docs/latex-publishing-sop.md for the supported profile.
"""
import argparse
from collections import Counter
from dataclasses import dataclass, field
import hashlib
import html
import json
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET


@dataclass
class Node:
    kind: str
    value: str = ""
    children: list = field(default_factory=list)
    option: str = ""
    number: str = ""
    anchor: str = ""


def uncomment(s):
    # A percent is escaped iff preceded by an odd number of backslashes.
    return re.sub(r"(?m)(?<!\\)((?:\\\\)*)%[^\n]*", r"\1", s)


class Parser:
    def __init__(self, text):
        self.s, self.i = text, 0

    def ws(self):
        while self.i < len(self.s) and self.s[self.i].isspace():
            self.i += 1

    def group(self, opening="{", closing="}", optional=False):
        self.ws()
        if self.i >= len(self.s) or self.s[self.i] != opening:
            if optional:
                return ""
            raise ValueError(f"Expected {opening}: {self.s[self.i:self.i+100]!r}")
        start = self.i = self.i + 1
        depth = 1
        while self.i < len(self.s):
            c = self.s[self.i]
            if c == "\\":
                m = re.match(r"\\(?:[A-Za-z]+|.)", self.s[self.i:])
                self.i += len(m[0])
                continue
            if c == opening:
                depth += 1
            elif c == closing:
                depth -= 1
                if depth == 0:
                    out = self.s[start:self.i]
                    self.i += 1
                    return out
            self.i += 1
        raise ValueError("Unclosed group")

    def raw_env(self, name):
        pattern = re.compile(r"\\(begin|end)\{" + re.escape(name) + r"\}")
        depth, start = 1, self.i
        for m in pattern.finditer(self.s, self.i):
            depth += 1 if m[1] == "begin" else -1
            if depth == 0:
                self.i = m.end()
                return self.s[start:m.start()]
        raise ValueError(f"Unclosed environment: {name}")

    def parse(self):
        out = []
        while self.i < len(self.s):
            c = self.s[self.i]
            if c == "{":
                out.append(Node("group", children=Parser(self.group()).parse()))
            elif c == "}":
                raise ValueError("Unexpected closing brace")
            elif c == "$":
                delim = "$$" if self.s.startswith("$$", self.i) else "$"
                self.i += len(delim)
                m = re.search(r"(?<!\\)" + re.escape(delim), self.s[self.i:])
                if not m:
                    raise ValueError("Unclosed math")
                value = self.s[self.i:self.i+m.start()]
                self.i += m.end()
                out.append(Node("display" if delim == "$$" else "math", value))
            elif c == "\\":
                m = re.match(r"\\([A-Za-z]+\*?|.)", self.s[self.i:])
                name = m[1]
                self.i += len(m[0])
                if name in ("[", "("):
                    end = r"\]" if name == "[" else r"\)"
                    i = self.s.find(end, self.i)
                    if i < 0:
                        raise ValueError("Unclosed math delimiter")
                    out.append(Node("display" if name == "[" else "math", self.s[self.i:i]))
                    self.i = i + len(end)
                elif name == "begin":
                    env = self.group()
                    opt = self.group("[", "]", True)
                    if env in ("minipage", "tabular"):
                        opt = self.group()
                    value = self.raw_env(env)
                    if env in ("tikzpicture", "equation", "equation*", "align", "align*"):
                        out.append(Node(env, value, option=opt))
                    else:
                        out.append(Node(env, children=Parser(value).parse(), option=opt))
                elif name in ("section", "subsection", "subsubsection", "textbf", "emph", "textit", "textrm", "textnormal", "underline", "footnote", "note", "caption"):
                    out.append(Node(name, children=Parser(self.group()).parse()))
                elif name in ("label", "ref", "eqref", "url"):
                    out.append(Node(name, self.group()))
                elif name == "includegraphics":
                    opt = self.group("[", "]", True)
                    out.append(Node(name, self.group(), option=opt))
                elif name == "href":
                    target = self.group()
                    out.append(Node(name, target, Parser(self.group()).parse()))
                elif name == "item":
                    out.append(Node(name, option=self.group("[", "]", True)))
                elif name in ("setlength", "renewcommand"):
                    target = self.group(); self.group()
                    allowed = {"setlength": {r"\tabcolsep", r"\parindent", r"\parskip"}, "renewcommand": {r"\arraystretch"}}
                    if target not in allowed[name]:
                        raise ValueError(f"Review required for \\{name}{{{target}}}")
                elif name == "definecolor":
                    self.group(); self.group(); self.group()
                elif name in ("vspace", "hspace", "vspace*", "hspace*", "captionsetup"):
                    self.group()
                elif name == "addlinespace":
                    self.group("[", "]", True)
                elif name in ("normalfont", "normalsize", "small", "footnotesize", "centering", "noindent", "maketitle", "newpage", "clearpage", "hfill", "toprule", "midrule", "bottomrule", "begingroup", "endgroup", "fangsong", "songti", "heiti", "kaishu"):
                    pass
                elif name in ("em", "bf", "it"):
                    # These declarations apply to the rest of the balanced group.
                    out.append(Node({"em":"emph", "it":"textit", "bf":"textbf"}[name], children=self.parse()))
                elif name in ("par", "\\"):
                    out.append(Node("row" if name == "\\" else "text", "\n\n"))
                elif name in ("%", "&", "_", "#", "$", "{", "}"):
                    out.append(Node("text", name))
                elif name in ("textemdash", "textendash", "quad", "qquad", ",", " "):
                    out.append(Node("text", {"textemdash":"—", "textendash":"–"}.get(name, " ")))
                elif name == "pagenumbering":
                    self.group()
                elif name == "setcounter":
                    target = self.group(); self.group()
                    if target != "page":
                        raise ValueError(f"Counter reset requires adapter: {target}")
                else:
                    line = self.s[:self.i].count("\n") + 1
                    raise ValueError(f"Unsupported body command \\{name} near local line {line}")
            elif c == "&":
                out.append(Node("amp")); self.i += 1
            else:
                start = self.i
                while self.i < len(self.s) and self.s[self.i] not in "{}$\\&":
                    self.i += 1
                out.append(Node("text", self.s[start:self.i].replace("~", "\u00a0")))
        return out


BLOCKS = {"defblock":"Definition", "thmblock":"Theorem", "axiomblock":"Axiom", "lemmablock":"Lemma", "propositionblock":"Proposition", "colblock":"Corollary", "exampleblock":"Example", "exerciseblock":"Exercise", "remarkblock":"Remark", "remark":"Remark"}


def walk(nodes):
    for n in nodes:
        yield n
        yield from walk(n.children)


def annotate(nodes):
    sec = sub = subsub = fig = eq = 0
    counts = Counter()
    labels = {}
    current = None
    for n in walk(nodes):
        if n.kind == "section":
            sec += 1; sub = subsub = fig = 0; counts.clear()
            n.number = str(sec); current = n
        elif n.kind == "subsection":
            sub += 1; subsub = 0
            counts = Counter({k:v for k,v in counts.items() if k == "remark"})
            n.number = f"{sec}.{sub}"; current = n
        elif n.kind == "subsubsection":
            subsub += 1; n.number = f"{sec}.{sub}.{subsub}"; current = n
        elif n.kind in BLOCKS:
            counts[n.kind] += 1
            n.number = f"{sec}.{counts[n.kind]}" if n.kind == "remark" else f"{sec}.{sub}.{counts[n.kind]}"
            current = n
        elif n.kind == "caption":
            fig += 1; n.number = f"{sec}.{fig}"; current = n
        elif n.kind == "equation":
            eq += 1; n.number = str(eq); current = n
        if n.number:
            n.anchor = f"latex-{n.kind}-{n.number.replace('.', '-')}"
        if n.kind == "label":
            if current is None or n.value in labels:
                raise ValueError(f"Unbound or duplicate label: {n.value}")
            labels[n.value] = (current.number, current.anchor)
    return labels


def read_macros(source):
    macros = {}
    for f in sorted(source.rglob("*.tex")):
        if f.name == "main.tex":
            continue
        s = uncomment(f.read_text())
        for m in re.finditer(r"\\(?:def\\([A-Za-z]+)((?:#[1-9])*)|newcommand\{\\([A-Za-z]+)\}(?:\[([1-9])\])?|DeclareMathOperator\*?\{\\([A-Za-z]+)\})", s):
            p = Parser(s); p.i = m.end()
            expansion = p.group()
            name = m[1] or m[3] or m[5]
            if m[5]:
                expansion = r"\operatorname{" + expansion + "}"
            macros["\\"+name] = expansion
    macros.update({r"\mathds":r"\mathbb{#1}", r"\abs":r"\lvert #1\rvert", r"\norm":r"\lVert #1\rVert"})
    return macros


class Renderer:
    def __init__(self, labels, asset_url, figure_sizes=None):
        self.labels, self.asset_url = labels, asset_url
        self.math, self.footnotes, self.headings = [], [[]], []
        self.footcount = self.figure_count = 0
        self.census = Counter()
        self.figure_sizes = figure_sizes or {}

    def math_html(self, value, display=False, number=""):
        i = len(self.math)
        self.math.append({"tex":value, "display":display, "number":number})
        return f"@@MATH{i}@@"

    def inline(self, nodes):
        return "".join(self.one(n) for n in nodes)

    def flow(self, nodes):
        blocks, inline = [], []
        def flush():
            v = "".join(inline).strip()
            if v:
                blocks.append("<p>"+v+"</p>")
            inline.clear()
        inline_kinds = {"text", "math", "group", "textbf", "emph", "textit", "textrm", "textnormal", "underline", "ref", "eqref", "label", "url", "href", "footnote", "note"}
        for n in nodes:
            if n.kind == "text":
                for i, v in enumerate(re.split(r"\n\s*\n", n.value)):
                    if i:
                        flush()
                    inline.append(html.escape(v))
            elif n.kind in inline_kinds:
                inline.append(self.one(n))
            else:
                flush(); blocks.append(self.one(n))
        flush()
        return "\n".join(blocks)

    def notes_html(self, notes):
        if not notes:
            return ""
        return '<aside class="latex-footnotes" aria-label="Footnotes">'+"".join(f'<div id="latex-fn-{i}"><a class="footnote-number" href="#latex-fnref-{i}">{i}</a> {body} <a href="#latex-fnref-{i}" aria-label="Return to text">↩</a></div>' for i,body in notes)+'</aside>'

    def one(self, n):
        k = n.kind
        if k == "text": return html.escape(n.value)
        if k in ("math", "display", "equation", "equation*", "align", "align*"):
            self.census["display_math" if k != "math" else "inline_math"] += 1
            tex = n.value
            if k.startswith("align"):
                tex = r"\begin{aligned}"+tex+r"\end{aligned}"
            result = self.math_html(tex, k != "math", n.number)
            return f'<div id="{n.anchor}" class="latex-equation">{result}</div>' if n.anchor else result
        if k in ("section", "subsection", "subsubsection"):
            self.census[k] += 1
            depth = {"section":2,"subsection":3,"subsubsection":4}[k]
            title = self.inline(n.children)
            self.headings.append((depth,n.number,title,n.anchor))
            return f'<h{depth} id="{n.anchor}">{n.number}. {title}</h{depth}>'
        if k == "group": return self.inline(n.children)
        if k in ("textbf", "emph", "textit", "textrm", "textnormal", "underline"):
            tag = {"textbf":"strong", "emph":"em", "textit":"em", "underline":"u"}.get(k,"span")
            return f"<{tag}>"+self.inline(n.children)+f"</{tag}>"
        if k in ("note", "footnote"):
            self.footcount += 1; i = self.footcount
            self.census["footnotes"] += 1
            content = self.flow(n.children)
            self.footnotes[-1].append((i,content))
            return f'<sup id="latex-fnref-{i}"><a href="#latex-fn-{i}" role="doc-noteref">{i}</a></sup>'
        if k in BLOCKS:
            self.census[k] += 1
            role = BLOCKS[k].lower()
            self.footnotes.append([])
            title = f"{BLOCKS[k]} {n.number}"
            if n.option:
                title += "　"+self.inline(Parser(n.option).parse())
            body = self.flow(n.children)
            notes = self.notes_html(self.footnotes.pop())
            return f'<section class="latex-block latex-{role}" id="{n.anchor}" aria-label="{BLOCKS[k]} {n.number}"><div class="latex-block-title">{title}</div>{body}{notes}</section>'
        if k in ("proof", "proof*", "solution"):
            self.census[k] += 1
            title = self.inline(Parser(n.option).parse()) if n.option else k.rstrip("*").capitalize()
            body = self.flow(n.children)
            qed = '' if k == 'proof*' else '<span class="latex-qed" aria-label="End of proof">□</span>'
            return f'<details class="latex-proof" open><summary>{title}.</summary><div class="latex-proof-body">{body}{qed}</div></details>'
        if k in ("itemize", "enumerate"):
            if n.option:
                raise ValueError("List options require a reviewed adapter")
            self.census[k] += 1
            items, current = [], None
            for child in n.children:
                if child.kind == "item":
                    if child.option:
                        raise ValueError("Custom item labels require a reviewed adapter")
                    current = []; items.append(current)
                elif current is not None:
                    current.append(child)
                elif child.kind != "text" or child.value.strip():
                    raise ValueError("Text before first list item")
            tag = "ul" if k == "itemize" else "ol"
            return f"<{tag}>"+"".join("<li>"+self.flow(i)+"</li>" for i in items)+f"</{tag}>"
        if k == "tabular":
            self.census[k] += 1
            rows, row, cell = [], [], []
            for child in n.children:
                if child.kind in ("amp", "row"):
                    row.append(self.inline(cell).strip()); cell=[]
                    if child.kind == "row":
                        rows.append(row); row=[]
                else:
                    cell.append(child)
            final_cell = self.inline(cell).strip()
            if final_cell or row:
                row.append(final_cell); rows.append(row)
            if len({len(r) for r in rows}) != 1:
                raise ValueError("Nonrectangular table")
            return '<div class="latex-table" tabindex="0">'+'<table>'+"".join('<tr>'+''.join(f'<{"th" if i==0 else "td"}>{c}</{"th" if i==0 else "td"}>' for c in row)+'</tr>' for i,row in enumerate(rows))+'</table></div>'
        if k == "figure":
            self.census[k] += 1
            return '<div class="latex-figures">'+self.flow(n.children)+'</div>'
        if k == "minipage":
            return '<figure>'+self.flow(n.children)+'</figure>'
        if k == "tikzpicture":
            self.figure_count += 1; self.census[k] += 1
            if self.figure_count not in self.figure_sizes:
                raise ValueError("Supply --assets-dir with generated SVG dimensions before conversion")
            width, height = self.figure_sizes[self.figure_count]
            return f'<a class="latex-figure-link" href="{self.asset_url}/figure-{self.figure_count}.svg"><img src="{self.asset_url}/figure-{self.figure_count}.svg" width="{width}" height="{height}" alt="Diagram {self.figure_count}" loading="lazy" /></a>'
        if k == "caption":
            return f'<figcaption id="{n.anchor}">Figure {n.number}. '+self.inline(n.children)+'</figcaption>'
        if k == "includegraphics":
            self.census[k] += 1
            name = Path(n.value).name
            if n.value != 'figures/' + name or not re.fullmatch(r'[A-Za-z0-9_-]+\.png', name):
                raise ValueError('Only reviewed local figures/*.png images are supported')
            m = re.fullmatch(r'width=(0?\.\d+|1)\\linewidth', n.option)
            if not m or not 0 < float(m[1]) <= 1 or name not in self.figure_sizes:
                raise ValueError('Missing image or unsupported image width: ' + n.value)
            width, height = self.figure_sizes[name]
            url = html.escape(self.asset_url + '/' + name, quote=True)
            percent = float(m[1]) * 100
            return f'<a class="latex-raster-figure" href="{url}" style="--figure-width:{percent:g}%"><img src="{url}" width="{width}" height="{height}" alt="Original lecture diagram" loading="lazy" /></a>'
        if k == "quote":
            self.census[k] += 1
            return '<blockquote class="latex-quote">' + self.flow(n.children) + '</blockquote>'
        if k == "center": return self.flow(n.children)
        if k == "label": return ""
        if k in ("ref", "eqref"):
            number, anchor = self.labels[n.value]
            self.census["references"] += 1
            label = f"({number})" if k=="eqref" else number
            return f'<a href="#{anchor}" class="latex-ref">{label}</a>'
        if k in ("url", "href"):
            if not re.match(r"https?://", n.value):
                raise ValueError("Only HTTP(S) external links supported")
            return f'<a href="{html.escape(n.value,quote=True)}">'+(self.inline(n.children) if k=="href" else html.escape(n.value))+'</a>'
        raise ValueError(f"Unsupported environment/node: {k}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--assets-url", default="./decision-theory")
    ap.add_argument("--assets-dir", type=Path)
    args = ap.parse_args()
    source = args.source.resolve()
    raw = source.read_text()
    preamble, body = uncomment(raw).split(r"\begin{document}",1)
    body = body.split(r"\end{document}",1)[0]
    body, end_markers = re.subn(r"(?m)^[ \t]*\$\\diamond\$[ \t]*$", "", body)
    nodes = Parser(body).parse()
    labels = annotate(nodes)
    sizes = {}
    if args.assets_dir:
        for f in args.assets_dir.glob('*.png'):
            raw_png = f.read_bytes()
            if raw_png[:8] != b'\x89PNG\r\n\x1a\n':
                raise ValueError('Invalid PNG: ' + str(f))
            sizes[f.name] = struct.unpack('>II', raw_png[16:24])
        for f in args.assets_dir.glob("figure-*.svg"):
            _, _, width, height = map(float, ET.parse(f).getroot().attrib["viewBox"].split())
            sizes[int(f.stem.split("-")[-1])] = (round(width * 4 / 3), round(height * 4 / 3))
    renderer = Renderer(labels,args.assets_url,sizes)
    renderer.census["removed_end_markers"] = end_markers
    output = renderer.flow(nodes)
    output += renderer.notes_html(renderer.footnotes[0])
    metadata = {"headings":renderer.headings,"labels":labels,"census":dict(renderer.census),"math":renderer.math,"macros":read_macros(source.parent),"source_sha256":hashlib.sha256(raw.encode()).hexdigest(),"html":output}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(metadata,ensure_ascii=False,indent=2))
    print(json.dumps(metadata["census"],ensure_ascii=False))


if __name__ == "__main__":
    main()
