"""Word version of the NAIRA letterhead: the A4 artwork sits behind the text on every page (header anchor, behind text),
and the margins keep typing inside the writing area."""
import copy
from pathlib import Path
from lxml import etree
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.oxml.ns import qn
import pymupdf as fitz
from PIL import Image

D = Path(__file__).resolve().parent
pdf = fitz.open(D / 'Naira-Letterhead-A4.pdf')
pm = pdf[0].get_pixmap(dpi=300); pm.save(D / 'lh_300.png')
Image.open(D / 'lh_300.png').convert('RGB').save(D / 'lh_300.jpg', 'JPEG', quality=92, subsampling=0, optimize=True)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Mm(210), Mm(297)
sec.top_margin, sec.bottom_margin, sec.left_margin, sec.right_margin = Mm(56), Mm(34), Mm(22), Mm(22)
sec.header_distance, sec.footer_distance = Mm(0), Mm(0)

normal = doc.styles['Normal']
normal.font.name = 'Georgia'; normal.font.size = Pt(11); normal.font.color.rgb = RGBColor(0x3D, 0x35, 0x30)
normal.element.rPr.rFonts.set(qn('w:eastAsia'), 'Georgia')
normal.paragraph_format.space_after = Pt(8); normal.paragraph_format.line_spacing = 1.25

hp = sec.header.paragraphs[0]
run = hp.add_run()
shape = run.add_picture(str(D / 'lh_300.jpg'), width=Mm(210), height=Mm(297))
inline = shape._inline
graphic = inline.find(qn('a:graphic'))
WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
anchor = etree.fromstring(
    f'<wp:anchor xmlns:wp="{WP}" distT="0" distB="0" distL="0" distR="0" simplePos="0" relativeHeight="0" behindDoc="1" '
    f'locked="1" layoutInCell="1" allowOverlap="1"><wp:simplePos x="0" y="0"/>'
    f'<wp:positionH relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionH>'
    f'<wp:positionV relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionV>'
    f'<wp:extent cx="{210 * 36000}" cy="{297 * 36000}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/>'
    f'<wp:docPr id="1" name="NAIRA letterhead"/><wp:cNvGraphicFramePr/></wp:anchor>')
anchor.append(copy.deepcopy(graphic))
inline.getparent().replace(inline, anchor)

doc.add_paragraph('Date:')
doc.add_paragraph('')
doc.add_paragraph('To,')
doc.add_paragraph('')
doc.add_paragraph('Dear ,')
doc.add_paragraph('')
doc.add_paragraph('Warm regards,')
doc.add_paragraph('Naira')
doc.core_properties.title = 'NAIRA letterhead'; doc.core_properties.author = 'Naira'
doc.save(D / 'Naira-Letterhead-A4-EDITABLE.docx')
print('docx saved', round((D / 'Naira-Letterhead-A4-EDITABLE.docx').stat().st_size / 1e6, 2), 'MB')
