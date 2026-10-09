"""Render the simple, shape-based review deck to a portable PDF.

The PPTX remains the editable source. This renderer covers the text boxes,
filled rectangles and pictures emitted by build_presentation.py so a local
LibreOffice installation is not required for the review PDF.
"""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
from xml.sax.saxutils import escape

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


HERE = Path(__file__).resolve().parent
PPTX = HERE / "VOLLEY_Final_Review_2026-10-10.pptx"
PDF = HERE / "VOLLEY_Final_Review_2026-10-10.pdf"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("DejaVu", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
EMU_PER_PT = 12700


def pt(emu: int) -> float:
    return emu / EMU_PER_PT


def rgb(value, default="#1e3144"):
    if value is None:
        return HexColor(default)
    try:
        if value.rgb is not None:
            return HexColor("#" + str(value.rgb))
    except (AttributeError, TypeError, ValueError):
        pass
    return HexColor(default)


def fill_shape(pdf, shape, page_height):
    try:
        colour = rgb(shape.fill.fore_color)
    except (AttributeError, TypeError, ValueError):
        return
    x, y, w, h = map(pt, (shape.left, shape.top, shape.width, shape.height))
    pdf.setFillColor(colour)
    if "ROUNDED_RECTANGLE" in str(getattr(shape, "auto_shape_type", "")):
        pdf.roundRect(x, page_height - y - h, w, h, 9, fill=1, stroke=0)
    else:
        pdf.rect(x, page_height - y - h, w, h, fill=1, stroke=0)


def text_shape(pdf, shape, page_height, slide_number):
    frame = shape.text_frame
    if not frame or not shape.text.strip():
        return []
    x = pt(shape.left + frame.margin_left)
    y = pt(shape.top + frame.margin_top)
    width = max(1, pt(shape.width - frame.margin_left - frame.margin_right))
    height = max(1, pt(shape.height - frame.margin_top - frame.margin_bottom))
    parsed = []
    for p in frame.paragraphs:
        if not p.text:
            continue
        run = p.runs[0] if p.runs else None
        font = run.font if run and run.font.size else p.font
        font_size = pt(font.size) if font and font.size else 16
        font_name = "DejaVu-Bold" if font and font.bold else "DejaVu"
        color = rgb(font.color if font else None)
        align = {PP_ALIGN.CENTER: TA_CENTER, PP_ALIGN.RIGHT: TA_RIGHT}.get(p.alignment, TA_LEFT)
        parsed.append((escape(p.text), font_size, font_name, color, align, pt(p.space_after) if p.space_after else 0))
    if not parsed:
        return []

    # A few compact table cells need a small reduction because DejaVu is wider
    # than the deck's Aptos font. The reduction is recorded for visual review.
    shrink = 1.0
    rendered = []
    while shrink >= 0.72:
        rendered = []
        total = 0
        for value, size, name, colour, align, after in parsed:
            style = ParagraphStyle("slide", fontName=name, fontSize=size * shrink,
                                   leading=size * shrink * 1.17, textColor=colour,
                                   alignment=align, spaceAfter=after)
            para = Paragraph(value, style)
            _, ph = para.wrap(width, height * 3)
            rendered.append((para, ph, after))
            total += ph + after
        if total <= height + 1:
            break
        shrink -= 0.04
    overflow = total > height + 1
    if frame.vertical_anchor == MSO_ANCHOR.MIDDLE:
        y += max(0, (height - total) / 2)
    cursor = page_height - y
    for para, ph, after in rendered:
        para.drawOn(pdf, x, cursor - ph)
        cursor -= ph + after
    return [(slide_number, shape.text[:65], round(total, 1), round(height, 1))] if overflow else []


def main():
    deck = Presentation(PPTX)
    page_width, page_height = pt(deck.slide_width), pt(deck.slide_height)
    pdf = canvas.Canvas(str(PDF), pagesize=(page_width, page_height), pageCompression=1)
    overflows = []
    for number, slide in enumerate(deck.slides, 1):
        pdf.setFillColor(HexColor("#ffffff"))
        pdf.rect(0, 0, page_width, page_height, fill=1, stroke=0)
        for shape in slide.shapes:
            if shape.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE:
                fill_shape(pdf, shape, page_height)
            elif shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                x, y, w, h = map(pt, (shape.left, shape.top, shape.width, shape.height))
                pdf.drawImage(ImageReader(BytesIO(shape.image.blob)), x,
                              page_height - y - h, w, h, mask="auto")
            elif shape.has_text_frame:
                overflows.extend(text_shape(pdf, shape, page_height, number))
        pdf.showPage()
    pdf.setTitle("VOLLEY Gen5 — final B.Tech project review")
    pdf.setAuthor("Adityavardhan Mishra and Pratham Chawla")
    pdf.save()
    print(f"Wrote {PDF} ({len(deck.slides)} pages)")
    for item in overflows:
        print("TEXT OVERFLOW:", item)
    if overflows:
        raise SystemExit(f"{len(overflows)} text frames exceed their boxes")


if __name__ == "__main__":
    main()
