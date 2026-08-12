#!/usr/bin/env python3
"""Find new apps under ``docs/gallery/`` and link them into ``docs/gallery.html``.

The gallery folder is two levels deep: ``docs/gallery/<Section>/<Camper-Name>/...``,
where ``<Section>`` is ``MiddleSchool``, ``HighSchool``, or ``Instructor``. This script
walks that tree, works out which file is the "entry point" for each camper's app (their
``index.html`` if they have one, otherwise every ``.html``/``.py`` file directly in their
folder counts as its own app), and checks each one against the links already in
``gallery.html``. Anything not already linked gets a new card appended to the matching
section, inside the ``<!-- gallery:<Section>:start -->`` / ``:end`` markers.

It does not try to write a good description or pick a perfect icon — it pulls a title
and description where it reasonably can (an HTML ``<title>``/meta description, or a
Python module docstring) and otherwise leaves a placeholder. **Read the printed summary
and fix up any TODO markers by hand** — this script only saves you from writing the
boilerplate and forgetting to link something in, not from writing good copy.

It is idempotent — run it again after adding new files and it only adds cards for
apps it hasn't seen before; existing cards are left untouched.

Usage:
    python update_gallery.py [--dry-run]
"""

from __future__ import annotations

import itertools
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs"
GALLERY_DIR = DOCS / "gallery"
GALLERY_HTML = DOCS / "gallery.html"

# Folder name under docs/gallery/ -> the gallery:<Section> marker name used in gallery.html.
SECTIONS = ["MiddleSchool", "HighSchool", "Instructor"]

ICONS = ["🧩", "🎮", "✨", "🚀", "🎯", "🎨", "🧠", "🔧", "🌟", "🕹️"]
COLORS = ["gthumb-cy", "gthumb-am", "gthumb-vi", "gthumb-gr"]


def find_entries(person_dir: pathlib.Path) -> list[pathlib.Path]:
    """Return the file(s) that count as this person's app(s).

    A folder with an ``index.html`` is treated as one app (everything else in the
    folder — JS, CSS, images — is a companion asset). Otherwise every ``.html`` and
    ``.py`` file directly in the folder is its own separate app.
    """
    index = person_dir / "index.html"
    if index.is_file():
        return [index]
    entries = [
        p for p in sorted(person_dir.iterdir())
        if p.is_file() and p.suffix.lower() in (".html", ".py")
    ]
    return entries


def href_for(entry: pathlib.Path) -> str:
    rel = entry.relative_to(DOCS).as_posix()
    return rel  # already "gallery/Section/Camper-Name/file"


def title_from_html(text: str) -> str | None:
    m = re.search(r"<title>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
    if not m:
        return None
    title = re.sub(r"\s+", " ", m.group(1)).strip()
    # Titles like "Which Animal Are You? — A Big Five Personality Quiz" carry a
    # subtitle after an em/en dash; the card only has room for the short part.
    for dash in (" — ", " – ", " - "):
        if dash in title:
            return title.split(dash, 1)[0].strip()
    return title


def description_from_html(text: str) -> str | None:
    m = re.search(
        r'<meta\s+name="description"\s+content="([^"]*)"', text, re.IGNORECASE
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    return None


def title_from_filename(path: pathlib.Path) -> str:
    words = re.sub(r"[_-]+", " ", path.stem)
    words = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", words)  # camelCase -> camel Case
    return words.title().strip()


def docstring_from_py(text: str) -> str | None:
    m = re.match(r'\s*("""|\'\'\')(.*?)(\1)', text, re.DOTALL)
    if not m:
        return None
    first_line = m.group(2).strip().splitlines()[0].strip()
    return first_line or None


def describe_entry(entry: pathlib.Path) -> tuple[str, str, bool]:
    """Return (title, description, is_placeholder_description)."""
    text = entry.read_text(encoding="utf-8", errors="replace")
    if entry.suffix.lower() == ".html":
        title = title_from_html(text) or title_from_filename(entry)
        desc = description_from_html(text)
        if desc:
            return title, desc, False
        return title, "TODO: describe what this app does.", True
    else:  # .py
        title = title_from_filename(entry)
        doc = docstring_from_py(text)
        if doc:
            return title, doc, False
        return title, "TODO: describe what this app does. Python — download to run.", True


def camper_byline(section: str, person_dir_name: str) -> str:
    name = person_dir_name.replace("-", " ").strip()
    if section == "Instructor":
        return f"{name}, Instructor"
    return name


def build_card(section: str, person_dir_name: str, entry: pathlib.Path, icon_cycle) -> str:
    title, desc, is_placeholder = describe_entry(entry)
    href = href_for(entry)
    icon, color = next(icon_cycle)
    by = camper_byline(section, person_dir_name)
    if entry.suffix.lower() == ".py" and "download to run" not in desc:
        desc = f"{desc} Python — download to run."
    card = (
        f'<a class="gcard" href="{href}">\n'
        f'          <div class="gcard-thumb icon {color}">{icon}</div>\n'
        f'          <div class="gcard-body">\n'
        f'            <h3>{title}</h3>\n'
        f'            <p>{desc}</p>\n'
        f'            <span class="gcard-by">by {by}</span>\n'
        f'          </div>\n'
        f'        </a>'
    )
    return card, is_placeholder


def discover_new(existing_hrefs: set[str]) -> dict[str, list[tuple[str, pathlib.Path]]]:
    """Return {section: [(person_dir_name, entry_path), ...]} for unlinked apps."""
    found: dict[str, list[tuple[str, pathlib.Path]]] = {s: [] for s in SECTIONS}
    if not GALLERY_DIR.is_dir():
        return found

    for section in SECTIONS:
        section_dir = GALLERY_DIR / section
        if not section_dir.is_dir():
            continue
        for person_dir in sorted(p for p in section_dir.iterdir() if p.is_dir()):
            for entry in find_entries(person_dir):
                if href_for(entry) not in existing_hrefs:
                    found[section].append((person_dir.name, entry))
    return found


def insert_cards(html: str, section: str, new_cards: list[str]) -> str:
    """Rebuild the whole marker block from scratch: existing cards (pulled back out
    of the current block) plus the new ones, in the same canonical layout. Rebuilding
    instead of splicing avoids fiddly whitespace bookkeeping.
    """
    start = f"<!-- gallery:{section}:start -->"
    end = f"<!-- gallery:{section}:end -->"
    pattern = re.compile(re.escape(start) + r"(.*?)" + re.escape(end), re.DOTALL)
    m = pattern.search(html)
    if not m:
        raise ValueError(f"Couldn't find {start} / {end} markers in gallery.html")

    block = m.group(1)
    existing_cards = re.findall(r'<a class="gcard".*?</a>', block, re.DOTALL)
    all_cards = existing_cards + new_cards

    cards_html = "\n\n".join("        " + c for c in all_cards)
    new_block = (
        "\n      <div class=\"gallery\">\n\n"
        + cards_html
        + "\n\n      </div>\n      "
    )

    new_full = start + new_block + end
    return html[: m.start()] + new_full + html[m.end() :]


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv

    if not GALLERY_HTML.is_file():
        print(f"ERROR: {GALLERY_HTML} not found")
        return 1

    html = GALLERY_HTML.read_text(encoding="utf-8")
    existing_hrefs = set(re.findall(r'href="(gallery/[^"]+)"', html))

    found = discover_new(existing_hrefs)
    total_new = sum(len(v) for v in found.values())

    if total_new == 0:
        print("No new gallery files found — nothing to link.")
        return 0

    icon_cycle = itertools.cycle(itertools.product(ICONS, COLORS))
    placeholders: list[str] = []

    for section, items in found.items():
        if not items:
            continue
        cards = []
        for person_dir_name, entry in items:
            card, is_placeholder = build_card(section, person_dir_name, entry, icon_cycle)
            cards.append(card.rstrip("\n"))
            href = href_for(entry)
            flag = " (TODO: needs a real description)" if is_placeholder else ""
            print(f"ADD   [{section}] {href}{flag}")
            if is_placeholder:
                placeholders.append(href)
        html = insert_cards(html, section, cards)

    if dry_run:
        print(f"\n(dry run — {total_new} new card(s) not written)")
        return 0

    GALLERY_HTML.write_text(html, encoding="utf-8")
    print(f"\nLinked {total_new} new app(s) in {GALLERY_HTML}.")
    if placeholders:
        print(
            "Some entries got a placeholder description and a generic icon — "
            "open gallery.html and clean these up by hand:"
        )
        for href in placeholders:
            print(f"  - {href}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
