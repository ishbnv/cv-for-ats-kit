#!/usr/bin/env python3
"""
render_cv.py — deterministic one-page CV renderer (A4, PDF) from a JSON content file.

Usage:
    python3 render_cv.py content.json out.pdf [--keywords "kw1,kw2,..."] [--no-trim]

Design: single column, Carlito/Calibri-like sans (falls back to Liberation Sans, then DejaVu Sans),
blue accents (#1c4e80), bold metrics inside bullets, clickable links, plain UPPERCASE section
headings (no letter-spacing — ATS parsers break on spaced glyphs).

Behaviour:
  * auto-fit: shrinks typography from 9.3pt down to 8.3pt until the CV fits one page;
  * auto-trim (unless --no-trim): if it still overflows, removes the last bullet of the job
    with the most bullets (never below 2 per job) and retries; every removal is reported;
  * checks: keyword coverage (case-insensitive substring over the whole content), placeholders
    (⚠, [X], [N], {{ ), page count. Prints a JSON report to stdout and exits 1 on failure.

Content JSON schema (all strings; **double asterisks** = bold):
{
  "lang": "en" | "ru",
  "name": "Ivan Shabanov",
  "title": "Senior Software Engineer",                 # exact title from the vacancy
  "tail": "TypeScript / Node.js / React · ...",         # rest of the headline
  "location": "Yerevan, Armenia (GMT+4) · ...",
  "contacts": [{"label": "ivan@ishbnv.dev", "href": "mailto:ivan@ishbnv.dev"}, ...],
  "summary": "3–4 sentences, no 'I'",
  "jobs": [{"company": "...", "engagement": "via GIDFINANCE" | "", "role": "...", "dates": "...",
            "blurb": "one italic line", "bullets": ["**metric first** then method", ...]}],
  "oss": {"text": "**vk-ai-bot-platform** (MIT) — ...", "href": "https://github.com/..."} | null,
  "skills": [["Label", "comma, separated, items"], ...],
  "education": ["line 1", "line 2"],
  "labels": {"summary": "...", "experience": "...", "oss": "...", "skills": "...", "education": "..."}  # optional
}
"""
import glob
import io
import json
import os
import re
import sys
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table,
                                TableStyle, KeepTogether)

ACCENT, MUTED, TEXT, RULE = "#1c4e80", "#4d5157", "#16191d", "#c9cdd4"
LABELS = {
    "en": {"summary": "Summary", "experience": "Experience", "oss": "Open-source project",
           "skills": "Skills", "education": "Education & Languages"},
    "ru": {"summary": "О себе", "experience": "Опыт работы", "oss": "Open-source проект",
           "skills": "Навыки", "education": "Образование и языки"},
}

# ---------- fonts ----------
FONT_CANDIDATES = [
    ("Carlito", ["Carlito-Regular.ttf", "Carlito-Bold.ttf", "Carlito-Italic.ttf", "Carlito-BoldItalic.ttf"]),
    ("Calibri", ["calibri.ttf", "calibrib.ttf", "calibrii.ttf", "calibriz.ttf"]),
    ("LiberationSans", ["LiberationSans-Regular.ttf", "LiberationSans-Bold.ttf",
                        "LiberationSans-Italic.ttf", "LiberationSans-BoldItalic.ttf"]),
    ("DejaVuSans", ["DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf", "DejaVuSans-BoldOblique.ttf"]),
]
FONT_DIRS = ["/usr/share/fonts", "/usr/local/share/fonts", os.path.expanduser("~/.fonts"),
             os.path.expanduser("~/Library/Fonts"), "/Library/Fonts", "C:/Windows/Fonts", "."]


def _find(fname):
    for d in FONT_DIRS:
        hits = glob.glob(os.path.join(d, "**", fname), recursive=True)
        if hits:
            return hits[0]
    return None


def register_fonts():
    for family, files in FONT_CANDIDATES:
        paths = [_find(f) for f in files]
        if all(paths):
            names = [family, family + "-Bold", family + "-Italic", family + "-BoldItalic"]
            for n, p in zip(names, paths):
                pdfmetrics.registerFont(TTFont(n, p))
            pdfmetrics.registerFontFamily(family, normal=names[0], bold=names[1], italic=names[2], boldItalic=names[3])
            return family
    raise SystemExit("No usable TTF font family found (Carlito / Calibri / Liberation Sans / DejaVu Sans).")


# ---------- markup ----------
def md(s):
    """Escape XML, then **bold** → <b>."""
    s = escape(str(s), {'"': "&quot;"})
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)


def link(label, href):
    return f'<a href="{escape(href, {chr(34): "&quot;"})}">{escape(label)}</a>'


# ---------- story ----------
def build_story(c, font, scale):
    lang = c.get("lang", "en")
    L = dict(LABELS.get(lang, LABELS["en"]))
    L.update(c.get("labels") or {})
    fs = lambda pt: pt * scale
    lead = lambda pt: pt * scale * 1.32

    st_name = ParagraphStyle("name", fontName=font + "-Bold", fontSize=fs(20), leading=fs(20) * 1.1,
                             textColor=TEXT, spaceAfter=fs(3))
    st_head = ParagraphStyle("head", fontName=font + "-Bold", fontSize=fs(10.2), leading=lead(10.2),
                             textColor=ACCENT, spaceAfter=fs(3))
    st_meta = ParagraphStyle("meta", fontName=font, fontSize=fs(8.7), leading=lead(8.7), textColor=MUTED, spaceAfter=fs(1))
    st_h2 = ParagraphStyle("h2", fontName=font + "-Bold", fontSize=fs(8.8), leading=lead(8.8), textColor=ACCENT,
                           spaceBefore=fs(8), spaceAfter=fs(1.2))
    st_body = ParagraphStyle("body", fontName=font, fontSize=fs(9.3), leading=lead(9.3), textColor=TEXT)
    st_co = ParagraphStyle("co", parent=st_body, fontName=font + "-Bold")
    st_dates = ParagraphStyle("dates", parent=st_body, fontSize=fs(8.6), leading=lead(8.6), textColor=MUTED, alignment=TA_RIGHT)
    st_blurb = ParagraphStyle("blurb", parent=st_body, fontName=font + "-Italic", textColor=MUTED, spaceAfter=fs(2))
    st_bullet = ParagraphStyle("bullet", parent=st_body, leftIndent=fs(10), bulletIndent=fs(1),
                               bulletFontName=font + "-Bold", bulletFontSize=fs(9.3), bulletColor=ACCENT,
                               spaceAfter=fs(1.6))
    st_skill = ParagraphStyle("skill", parent=st_body, spaceAfter=fs(1.5))

    def h2(text):
        return [Paragraph(escape(text.upper()), st_h2),
                HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=0, spaceAfter=fs(3.5))]

    s = []
    s.append(Paragraph(escape(c["name"].upper()), st_name))
    headline = " · ".join([x for x in [c.get("title", ""), c.get("tail", "")] if x])
    s.append(Paragraph(escape(headline), st_head))
    s.append(Paragraph(escape(c.get("location", "")), st_meta))
    s.append(Paragraph(" &nbsp;·&nbsp; ".join(link(x["label"], x["href"]) for x in c.get("contacts", [])), st_meta))

    s += h2(L["summary"])
    s.append(Paragraph(md(c["summary"]), st_body))

    s += h2(L["experience"])
    page_w = A4[0] - 2 * 13 * mm
    for i, j in enumerate(c["jobs"]):
        co = f'<b>{escape(j["company"])}</b>'
        if j.get("engagement"):
            co += f' <font color="{MUTED}">{escape(j["engagement"])}</font>'
        co += f' — <font color="{ACCENT}"><b>{escape(j["role"])}</b></font>'
        head = Table([[Paragraph(co, st_co), Paragraph(escape(j["dates"]), st_dates)]],
                     colWidths=[page_w - 56 * mm, 56 * mm])
        head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "BOTTOM"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), fs(5) if i else 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        block = [head, Paragraph(md(j.get("blurb", "")), st_blurb)]
        block += [Paragraph(md(b), st_bullet, bulletText="•") for b in j["bullets"]]
        s.append(KeepTogether(block[:2]))
        s += block[2:]

    if c.get("oss"):
        s += h2(L["oss"])
        s.append(Paragraph(f'<a href="{escape(c["oss"]["href"])}">{md(c["oss"]["text"])}</a>', st_body))

    s += h2(L["skills"])
    for label, items in c["skills"]:
        s.append(Paragraph(f"<b>{escape(label)}:</b> {md(items)}", st_skill))

    s += h2(L["education"])
    for line in c["education"]:
        s.append(Paragraph(md(line), st_body))
    return s


def render(c, font, scale, path_or_buf):
    doc = SimpleDocTemplate(path_or_buf, pagesize=A4, leftMargin=13 * mm, rightMargin=13 * mm,
                            topMargin=10 * mm, bottomMargin=9 * mm,
                            title=f'{c["name"]} — {c.get("title", "")}', author=c["name"])
    doc.build(build_story(c, font, scale))
    return doc.page  # number of pages rendered


def all_text(c):
    parts = [c.get("title", ""), c.get("tail", ""), c.get("location", ""), c.get("summary", "")]
    for j in c["jobs"]:
        parts += [j["company"], j["role"], j.get("blurb", "")] + j["bullets"]
    if c.get("oss"):
        parts.append(c["oss"]["text"])
    parts += [f"{a}: {b}" for a, b in c["skills"]] + c["education"]
    return " ".join(parts)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    src, out = sys.argv[1], sys.argv[2]
    keywords = []
    trim = "--no-trim" not in sys.argv
    if "--keywords" in sys.argv:
        keywords = [k.strip() for k in sys.argv[sys.argv.index("--keywords") + 1].split(",") if k.strip()]

    c = json.load(open(src, encoding="utf-8"))
    font = register_fonts()
    removed = []
    scale = 1.0
    pages = 99
    while True:
        scale = 1.0
        while True:
            pages = render(c, font, scale, io.BytesIO())
            if pages == 1 or scale <= 0.89:
                break
            scale = round(scale - 0.01, 3)
        if pages == 1 or not trim:
            break
        # auto-trim: drop the last bullet of the job with the most bullets (keep >= 2)
        j = max(c["jobs"], key=lambda x: len(x["bullets"]))
        if len(j["bullets"]) <= 2:
            break
        removed.append({"job": j["company"], "bullet": j["bullets"].pop()})

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    pages = render(c, font, scale, out)
    text = re.sub(r"\s+", " ", all_text(c)).lower()
    report = {
        "file": out, "pages": pages, "font": font, "body_pt": round(9.3 * scale, 1),
        "removed_bullets": removed,
        "missing_keywords": [k for k in keywords if k.lower() not in text],
        "placeholders": re.findall(r"⚠|\[X\]|\[N\]|\{\{", all_text(c)),
        "ok": pages == 1 and not re.findall(r"⚠|\[X\]|\[N\]|\{\{", all_text(c)),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
