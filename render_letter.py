#!/usr/bin/env python3
"""
render_letter.py — one-page cover letter (A4, PDF) from a JSON file.

Usage:
    python3 render_letter.py letter.json out.pdf

JSON schema:
{
  "name": "IVAN SHABANOV",
  "line1": "ivan@ishbnv.dev · +374 77 719 518 · linkedin.com/in/ishbnv · github.com/ishbnv · ishbnv.dev",
  "line2": "Yerevan, Armenia (GMT+4) · Remote · Full overlap with EU hours",
  "date": "3 September 2026",
  "to": ["Company — Hiring Team", "Re: Exact Role Title (Job ID …)"],
  "paragraphs": ["Dear Hiring Team,", "…", "…"],
  "closing": ["Kind regards,", "Ivan Shabanov"]
}
Auto-fit: 10.5pt → 9.5pt until the letter fits one page. Prints a JSON report; exits 1 on overflow.
"""
import io
import json
import re
import sys
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from render_cv import register_fonts  # noqa: E402


def story(l, font, pt):
    body = ParagraphStyle("b", fontName=font, fontSize=pt, leading=pt * 1.32, spaceAfter=pt * 0.7)
    small = ParagraphStyle("s", parent=body, fontSize=pt - 1.5, leading=(pt - 1.5) * 1.3, spaceAfter=0)
    name = ParagraphStyle("n", fontName=font + "-Bold", fontSize=16, leading=18, spaceAfter=2)
    bold = ParagraphStyle("bb", parent=body, fontName=font + "-Bold", spaceAfter=0)
    s = [Paragraph(escape(l["name"]), name), Paragraph(escape(l["line1"]), small), Paragraph(escape(l["line2"]), small),
         Spacer(1, 4), HRFlowable(width="100%", thickness=0.7, color="#444444"), Spacer(1, 14),
         Paragraph(escape(l["date"]), body), Spacer(1, 6),
         Paragraph(escape(l["to"][0]), bold), Paragraph(escape(l["to"][1]), body), Spacer(1, 8)]
    s += [Paragraph(escape(p), body) for p in l["paragraphs"]]
    closing = l.get("closing", ["Kind regards,", "Ivan Shabanov"])
    s += [Paragraph(escape(closing[0]), ParagraphStyle("c", parent=body, spaceAfter=3)), Paragraph(escape(closing[1]), bold)]
    return s


def render(l, font, pt, target):
    doc = SimpleDocTemplate(target, pagesize=A4, leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.75 * inch, title=f'{l["name"]} — Cover Letter', author=l["name"])
    doc.build(story(l, font, pt))
    return doc.page


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    l = json.load(open(sys.argv[1], encoding="utf-8"))
    font = register_fonts()
    pt = 10.5
    while True:
        pages = render(l, font, pt, io.BytesIO())
        if pages == 1 or pt <= 9.5:
            break
        pt = round(pt - 0.25, 2)
    out = sys.argv[2]
    __import__("os").makedirs(__import__("os").path.dirname(__import__("os").path.abspath(out)), exist_ok=True)
    pages = render(l, font, pt, out)
    words = len(" ".join(l["paragraphs"]).split())
    report = {"file": out, "pages": pages, "font": font, "body_pt": pt, "words": words,
              "em_dashes": sum(p.count("—") for p in l["paragraphs"]),
              "placeholders": re.findall(r"⚠|\[X\]|\{\{", " ".join(l["paragraphs"])), "ok": pages == 1}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
