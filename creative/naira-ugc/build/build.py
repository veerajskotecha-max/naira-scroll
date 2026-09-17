#!/usr/bin/env python3
"""Render the UGC teardown report to PDF.

    python3 creative/naira-ugc/build/build.py

Concatenates p1..p7.html into report.html and prints it through headless
Chromium. Fonts are vendored in fonts/ so the build is offline-reproducible.
"""
import pathlib, subprocess, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / "NAIRA_UGC_Teardown_Hooks_VO-Reel_Plan.pdf"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

parts = [HERE / f"p{i}.html" for i in range(1, 8)]
report = HERE / "report.html"
report.write_text("".join(p.read_text() for p in parts))

FOOTER = ('<div style="width:100%;font-family:sans-serif;font-size:7pt;color:#8A807A;'
          'padding:0 15mm;display:flex;justify-content:space-between;">'
          '<span>NAIRA &middot; UGC teardown, hook library &amp; voiceover reel plan</span>'
          '<span class="pageNumber"></span></div>')

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME,
                          args=["--no-sandbox", "--allow-file-access-from-files"])
    pg = b.new_page()
    pg.goto(report.resolve().as_uri(), wait_until="networkidle")
    pg.wait_for_timeout(2500)          # let the vendored fonts settle
    pg.pdf(path=str(OUT), format="A4", print_background=True,
           display_header_footer=True, header_template="<div></div>",
           footer_template=FOOTER,
           margin={"top": "17mm", "bottom": "16mm", "left": "15mm", "right": "15mm"})
    b.close()
print(f"wrote {OUT}")
