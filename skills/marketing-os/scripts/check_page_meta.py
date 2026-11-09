#!/usr/bin/env python3
"""Offline pre-publication check of a local HTML landing page (Workflow 4D).

Errors: missing title, meta description, viewport or h1; images without alt; unlabelled form
fields; invalid JSON-LD; unresolved [NEEDS INPUT] markers.
Warnings: social tags, canonical, lang, heading order, generic button text, many exit links,
images without dimensions, lazy-loaded first image, render-blocking scripts, mistyped email or
phone fields, and hard-to-read copy.
It does not fetch URLs, measure real speed, see the rendered layout, or judge whether claims
are true. A clean result is not a prediction of conversion.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

TITLE_MAX = 60
DESCRIPTION_MAX = 160
MAX_EXIT_LINKS = 10
MAX_READING_GRADE = 9.0
MIN_WORDS_FOR_READABILITY = 100
REQUIRED_OG = ("og:title", "og:description", "og:image", "og:url")
MARKERS = ("[NEEDS INPUT", "[NEEDS HUMAN REVIEW")
NON_FIELD_INPUT_TYPES = {"hidden", "submit", "button", "image", "reset"}
GENERIC_CTA = {"submit", "click here", "learn more", "send", "go", "continue", "read more", "more", "ok"}
SKIP_TEXT_TAGS = {"script", "style", "noscript", "template", "svg"}
HEADINGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6}


class _Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang: str | None = None
        self.title = ""
        self.meta: dict[str, str] = {}
        self.canonical: str | None = None
        self.heading_levels: list[int] = []
        self.images: list[dict[str, str]] = []
        self.jsonld: list[str] = []
        self.label_for: set[str] = set()
        self.fields: list[tuple[dict[str, str], bool]] = []
        self.exit_links = 0
        self.cta_texts: list[str] = []
        self.blocking_scripts = 0
        self.text: list[str] = []
        self._in_head = False
        self._in_body = False
        self._in_title = False
        self._in_jsonld = False
        self._label_depth = 0
        self._skip_depth = 0
        self._cta_depth = 0
        self._cta_buffer: list[str] = []
        self._buffer: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag in SKIP_TEXT_TAGS:
            self._skip_depth += 1
        if tag == "html":
            self.lang = a.get("lang") or None
        elif tag == "head":
            self._in_head = True
        elif tag == "body":
            self._in_body = True
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = (a.get("property") or a.get("name") or "").lower()
            if key:
                self.meta[key] = a.get("content", "").strip()
        elif tag == "link" and "canonical" in a.get("rel", "").lower().split():
            self.canonical = a.get("href", "").strip()
        elif tag in HEADINGS:
            self.heading_levels.append(HEADINGS[tag])
        elif tag == "img":
            self.images.append(a)
        elif tag == "script":
            if a.get("type", "").lower() == "application/ld+json":
                self._in_jsonld = True
                self._buffer = []
            elif self._in_head and a.get("src") and "async" not in a and "defer" not in a and a.get("type", "").lower() != "module":
                self.blocking_scripts += 1
        elif tag == "label":
            self._label_depth += 1
            if a.get("for"):
                self.label_for.add(a["for"])
        elif tag in ("input", "select", "textarea"):
            input_type = a.get("type", "text").lower()
            if tag == "input" and input_type in NON_FIELD_INPUT_TYPES:
                if input_type == "submit" and a.get("value"):
                    self.cta_texts.append(a["value"])
                return
            labelled = self._label_depth > 0 or bool(a.get("aria-label") or a.get("aria-labelledby"))
            a["_tag"] = tag
            self.fields.append((a, labelled))
        if tag == "a":
            href = a.get("href", "").strip()
            if href and not href.startswith(("#", "tel:", "mailto:", "javascript:")):
                self.exit_links += 1
        if tag in ("a", "button"):
            self._cta_depth += 1
            if self._cta_depth == 1:
                self._cta_buffer = []

    def handle_endtag(self, tag):
        if tag in SKIP_TEXT_TAGS and self._skip_depth:
            self._skip_depth -= 1
        if tag == "head":
            self._in_head = False
        elif tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append("".join(self._buffer))
        elif tag == "label" and self._label_depth:
            self._label_depth -= 1
        if tag in ("a", "button") and self._cta_depth:
            self._cta_depth -= 1
            if self._cta_depth == 0:
                text = " ".join("".join(self._cta_buffer).split())
                if text:
                    self.cta_texts.append(text)

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif self._in_jsonld:
            self._buffer.append(data)
        elif self._in_body and not self._skip_depth:
            self.text.append(data)
            if self._cta_depth:
                self._cta_buffer.append(data)


def _syllables(word: str) -> int:
    word = word.lower()
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if word.endswith("e") and not word.endswith(("le", "ee")) and count > 1:
        count -= 1
    return max(count, 1)


def reading_grade(text: str) -> tuple[float, int]:
    """Approximate Flesch-Kincaid grade level and word count for visible text."""
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*", text)
    sentences = [s for s in re.split(r"[.!?]+|\n{2,}", text) if re.search(r"[A-Za-z]", s)]
    if not words or not sentences:
        return 0.0, len(words)
    syllables = sum(_syllables(w) for w in words)
    grade = 0.39 * (len(words) / len(sentences)) + 11.8 * (syllables / len(words)) - 15.59
    return grade, len(words)


def check(html: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    page = _Page()
    page.feed(html)

    title = page.title.strip()
    if not title:
        errors.append("Missing <title>.")
    elif len(title) > TITLE_MAX:
        warnings.append(f"Title is {len(title)} characters (search results often truncate past ~{TITLE_MAX}).")
    description = page.meta.get("description", "")
    if not description:
        errors.append("Missing meta description.")
    elif len(description) > DESCRIPTION_MAX:
        warnings.append(f"Meta description is {len(description)} characters (often truncated past ~{DESCRIPTION_MAX}).")
    if not page.canonical:
        warnings.append("No canonical link.")
    if "viewport" not in page.meta:
        errors.append("Missing viewport meta tag; the page will not render properly on phones.")
    if not page.lang:
        warnings.append("<html> has no lang attribute.")
    for tag in REQUIRED_OG:
        if not page.meta.get(tag):
            warnings.append(f"Missing Open Graph tag {tag}.")
    if not page.meta.get("twitter:card"):
        warnings.append("Missing twitter:card tag.")
    if "noindex" in page.meta.get("robots", "").lower():
        warnings.append("Page is set to noindex; confirm that is intended.")

    h1_count = page.heading_levels.count(1)
    if h1_count == 0:
        errors.append("No <h1>.")
    elif h1_count > 1:
        warnings.append(f"{h1_count} <h1> elements; use one.")
    for previous, current in zip(page.heading_levels, page.heading_levels[1:]):
        if current > previous + 1:
            warnings.append(f"Heading levels skip from h{previous} to h{current}; keep headings in order.")
            break

    without_alt = sum(1 for img in page.images if "alt" not in img)
    if without_alt:
        errors.append(f"{without_alt} of {len(page.images)} image(s) have no alt attribute.")
    without_size = sum(1 for img in page.images if not (img.get("width") and img.get("height")))
    if without_size:
        warnings.append(f"{without_size} image(s) lack width and height attributes, which causes layout shift while loading.")
    if page.images and page.images[0].get("loading", "").lower() == "lazy":
        warnings.append("The first image is lazy-loaded; the hero image should load immediately.")
    if page.blocking_scripts:
        warnings.append(f"{page.blocking_scripts} script(s) in <head> without async or defer delay rendering.")

    unlabelled = sum(1 for attrs, labelled in page.fields if not labelled and attrs.get("id") not in page.label_for)
    if unlabelled:
        errors.append(f"{unlabelled} form field(s) have no label (placeholder text is not a label).")
    for attrs, _ in page.fields:
        if attrs.get("_tag") != "input":
            continue
        ident = (attrs.get("name", "") + " " + attrs.get("id", "")).lower()
        input_type = attrs.get("type", "text").lower()
        if "email" in ident and input_type != "email":
            warnings.append("An email field does not use type=\"email\"; phones will show the wrong keyboard.")
        if re.search(r"phone|tel\b|mobile", ident) and input_type != "tel":
            warnings.append("A phone field does not use type=\"tel\"; phones will show the wrong keyboard.")

    generic = sorted({t for t in page.cta_texts if t.strip().lower().rstrip(".!→ ") in GENERIC_CTA})
    if generic:
        warnings.append(f"Generic button or link text {generic}; name the outcome instead (for example 'Get my quote').")
    if page.exit_links > MAX_EXIT_LINKS:
        warnings.append(f"{page.exit_links} links lead away from the page; a campaign page should have few exits besides its main action.")

    grade, words = reading_grade(" ".join(page.text))
    if words >= MIN_WORDS_FOR_READABILITY and grade > MAX_READING_GRADE:
        warnings.append(f"Copy reads at about grade {grade:.0f} (rough estimate); shorter sentences and plainer words are easier to act on.")

    if not page.jsonld:
        warnings.append("No JSON-LD structured data.")
    for i, block in enumerate(page.jsonld):
        try:
            json.loads(block)
        except json.JSONDecodeError as ex:
            errors.append(f"JSON-LD block {i + 1} is not valid JSON: {ex.msg}.")

    upper = html.upper()
    if any(m in upper for m in MARKERS):
        errors.append("Page contains an unresolved [NEEDS INPUT] or [NEEDS HUMAN REVIEW] marker.")
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", type=Path, help="Local HTML file")
    args = parser.parse_args(argv)
    try:
        html = args.input.read_text(encoding="utf-8")
    except OSError as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return 2
    errors, warnings = check(html)
    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARNING: {w}")
    if not errors and not warnings:
        print("PASS: metadata, structure and basic accessibility checks are clean.")
    elif not errors:
        print("PASS with warnings: review before publishing.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
