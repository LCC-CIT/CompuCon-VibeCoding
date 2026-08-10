#!/usr/bin/env python3
"""Add or refresh the ``## Contents`` section of each Markdown file.

Scans a file for headings at levels two through four (``##``, ``###``, ``####``) and
lists them under a ``## Contents`` heading near the top, as linked entries using the
GitHub-style anchors that GitHub Pages / kramdown renders. Only the title of a file
should be ``#``; the script warns about any other ``#`` headings but never rewrites
them.

It is idempotent — run it again after adding, removing, or renaming headings and it
updates the existing Contents section in place instead of adding a second one. It
never edits anything outside the Contents section, so hand-written prose and code
blocks are preserved byte-for-byte.

Usage:
    python add_toc.py [FILE ...]

With no arguments it processes every ``*.md`` file under ``docs/`` plus the repo
``README.md``. ``CLAUDE.md`` and anything under ``.claude/`` are skipped on purpose.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs"


def discover_default_files() -> list[pathlib.Path]:
    files = sorted(DOCS.rglob("*.md")) if DOCS.is_dir() else []
    files.append(ROOT / "README.md")
    return files


def heading_info(line: str) -> tuple[int, str] | None:
    """Return (level, text) for a ``##``, ``###``, or ``####`` heading, else None."""
    m = re.match(r"^(#{2,4}) (.+)$", line)
    if m:
        return (len(m.group(1)), m.group(2).strip())
    return None


def slugify(text: str) -> str:
    """GitHub-style heading anchor: lowercase, strip punctuation, spaces -> hyphens."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s.strip("-")


def add_toc(text: str) -> tuple[str, str, list[str]]:
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.splitlines()

    headings = []        # (level, text, anchor, line_index)
    all_slugs = []       # slug of every heading (incl. the # title), in document order
    contents_index = None
    hash_headings_seen = 0
    in_fence = False
    warnings: list[str] = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if line.startswith("# "):
            hash_headings_seen += 1
            if hash_headings_seen > 1:
                warnings.append(
                    f"line {i + 1}: '# {line[2:].strip()}' — only the title "
                    "should be '#'. Demote it to '##'."
                )
            all_slugs.append(slugify(line[2:].strip()))
            continue

        h = heading_info(line)
        if h is None:
            continue
        level, htext = h
        if level == 2 and htext == "Contents":
            if contents_index is None:
                contents_index = i
            continue

        slug = slugify(htext)
        all_slugs.append(slug)
        n = all_slugs.count(slug) - 1
        anchor = slug if n == 0 else f"{slug}-{n}"
        headings.append((level, htext, anchor, i))

    if not headings:
        return text, "no ## or deeper headings to index", warnings

    first_real_index = min(h[3] for h in headings)
    if contents_index is not None and contents_index > first_real_index:
        # A "Contents" heading deeper in the document is content, not ours.
        contents_index = None

    # Render the fresh section, nesting each entry under the heading that most
    # recently precedes it at a shallower level — ### under ##, #### under ###,
    # and so on. A heading that opens a file (no shallower parent) is top level.
    section = ["## Contents", ""]
    stack: list[int] = []
    for level, htext, anchor, _ in headings:
        while stack and stack[-1] >= level:
            stack.pop()
        section.append(f"{'  ' * len(stack)}- [{htext}](#{anchor})")
        stack.append(level)
    section.append("")

    if contents_index is not None:
        # Replace in place: the managed block is the heading, blank lines, and
        # bullet items only — anything else after it is left alone.
        end = contents_index + 1
        while end < len(lines):
            ln = lines[end]
            if ln.strip() == "" or re.match(r"^\s*[-*] ", ln):
                end += 1
            else:
                break
        start, action = contents_index, "updated"
    else:
        start = first_real_index
        end = first_real_index
        action = "added"

    new_lines = lines[:start] + section + lines[end:]
    if new_lines == lines:
        return text, f"Contents up to date ({len(headings)} entries)", warnings

    out = newline.join(new_lines)
    if not out.endswith(newline):
        out += newline
    return out, f"{action} Contents ({len(headings)} entries)", warnings


def process(path: pathlib.Path) -> int:
    if not path.is_file():
        print(f"SKIP  {path} (not found)")
        return 0

    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")

    out, status, warnings = add_toc(text)
    for w in warnings:
        print(f"WARN  {path}: {w}")

    if out != text:
        encoded = out.encode("utf-8")
        if bom:
            encoded = b"\xef\xbb\xbf" + encoded
        path.write_bytes(encoded)
    print(f"{path}: {status}")
    return 0


def main(argv: list[str]) -> int:
    if argv:
        files = [pathlib.Path(a) for a in argv]
    else:
        files = discover_default_files()

    failures = 0
    for path in files:
        try:
            failures += process(path)
        except OSError as e:
            print(f"ERROR {path}: {e}")
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
