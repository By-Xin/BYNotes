#!/usr/bin/env python3
"""Regenerate web font subsets from the UNION of all published LaTeX sources.

Requires fonttools[woff] and the source fonts from TeX Live. Keep licenses in
quartz/static/latex-fonts when distributing the result.
"""
import argparse
from pathlib import Path
import string
import subprocess
from fontTools import subset
from fontTools.ttLib import TTFont

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("sources", nargs="+", type=Path)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
corpus = string.printable + "—·↗目录"
for source in args.sources:
    paths = source.rglob("*.tex") if source.is_dir() else [source]
    corpus += "".join(path.read_text() for path in paths)
args.output.mkdir(parents=True, exist_ok=True)
fonts = [
    ("texgyretermes-regular.otf", "termes-regular", "BYNotes Termes", "Regular"),
    ("texgyretermes-italic.otf", "termes-italic", "BYNotes Termes", "Italic"),
    ("texgyretermes-bold.otf", "termes-bold", "BYNotes Termes", "Bold"),
    ("texgyrepagella-bold.otf", "pagella-bold", "BYNotes Pagella", "Bold"),
    ("FandolSong-Regular.otf", "song", "BYNotes Song", "Regular"),
    ("FandolKai-Regular.otf", "kai", "BYNotes Kai", "Regular"),
]
for original, output, family, style in fonts:
    path = subprocess.check_output(["kpsewhich", original], text=True).strip()
    if not path:
        raise SystemExit(f"Font missing from TeX Live: {original}")
    font = TTFont(path)
    options = subset.Options()
    options.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14, 16, 17]
    sub = subset.Subsetter(options=options)
    sub.populate(text=corpus)
    sub.subset(font)
    ps_name = family.replace(" ", "") + "-" + style
    replacements = {1:family, 2:style, 3:ps_name, 4:family + " " + style, 6:ps_name, 16:family, 17:style}
    for record in list(font["name"].names):
        if record.nameID in replacements:
            font["name"].setName(replacements[record.nameID], record.nameID, record.platformID, record.platEncID, record.langID)
    if "CFF " in font:
        cff = font["CFF "].cff
        cff.fontNames = [ps_name]
        cff.topDictIndex[0].FamilyName = family
        cff.topDictIndex[0].FullName = family + " " + style
    font.flavor = "woff2"
    destination = args.output / (output + ".woff2")
    font.save(destination)
    print(f"{destination.name}: {destination.stat().st_size} bytes")
