#!/usr/bin/env python3
"""Rewrite the list of translations in the README and in every translation.

To add a translation, add it to LANGUAGES below and run:

    python3 translations/update-links.py

Every file must already contain a list of translations within its first 60
lines, so copy that list from another translation into a new one first. Nothing
is written if any of the files cannot be updated.
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


def updated(path, prefix):
    """Return the content of the file with its list of translations rewritten."""
    lines = path.read_text(encoding="utf-8").split("\n")
    found = [i for i, line in enumerate(lines[:60]) if LINK.match(line)]
    if not found or found != list(range(found[0], found[-1] + 1)):
        raise SystemExit(
            f"{path}: could not find the list of translations, "
            "copy it from another translation first"
        )
    links = [f"* [English]({prefix}README.md)"]
    links += [
        f"* [{label}]({prefix}translations/README-{code}.md)"
        for label, code in LANGUAGES
    ]
    lines[found[0] : found[-1] + 1] = links
    return "\n".join(lines)


for _, code in LANGUAGES:
    if not (ROOT / "translations" / f"README-{code}.md").exists():
        raise SystemExit(f"translations/README-{code}.md does not exist")

files = {ROOT / "README.md": ""}
for translation in sorted((ROOT / "translations").glob("README-*.md")):
    files[translation] = "../"

# Work out all the new contents first, so that nothing is written on an error.
contents = {path: updated(path, prefix) for path, prefix in files.items()}
for path, content in contents.items():
    path.write_text(content, encoding="utf-8")
