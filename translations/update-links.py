#!/usr/bin/env python3
"""Rewrite the list of translations in the README and in every translation.

To add a translation, add it to LANGUAGES below and run:

    python3 translations/update-links.py
"""
import re
from pathlib import Path

# (label, code): the file of a translation is translations/README-<code>.md
LANGUAGES = [
    ("German", "de"),
    ("Español", "es"),
    ("Français", "fr"),
    ("Italiano", "it"),
    ("Português do Brasil", "pt_BR"),
    ("中文版", "cn"),
    ("日本語", "ja"),
    ("한국어", "ko"),
    ("Turkish", "tr"),
    ("Greek", "gr"),
    ("Magyar", "hu"),
    ("Polish", "pl"),
    ("Русский", "ru"),
    ("Tiếng Việt", "vn"),
    ("Bahasa Indonesia", "id"),
    ("فارسی", "fa"),
    ("עברית", "he"),
]

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"^\s*[*-] \[[^\]]+\]\([^)]*README[^)]*\.md\)\s*$")


def update(path, prefix):
    lines = path.read_text(encoding="utf-8").split("\n")
    found = [i for i, line in enumerate(lines[:60]) if LINK.match(line)]
    if not found or found != list(range(found[0], found[-1] + 1)):
        raise SystemExit(f"{path}: could not find the list of translations")
    links = [f"* [English]({prefix}README.md)"]
    links += [
        f"* [{label}]({prefix}translations/README-{code}.md)"
        for label, code in LANGUAGES
    ]
    lines[found[0] : found[-1] + 1] = links
    path.write_text("\n".join(lines), encoding="utf-8")


for _, code in LANGUAGES:
    if not (ROOT / "translations" / f"README-{code}.md").exists():
        raise SystemExit(f"translations/README-{code}.md does not exist")

update(ROOT / "README.md", "")
for translation in sorted((ROOT / "translations").glob("README-*.md")):
    update(translation, "../")
