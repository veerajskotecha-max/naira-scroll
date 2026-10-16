# One command from verdicts to deliverables: picks the keepers of the four concept camps and Edition One, builds every PDF, renders
# the finished ads (finished-ads/ads.json) and their PDF, then builds the contact sheet page (every frame, its verdict, the finished
# ads, the keepers, the credit ledger and the PDFs) into <scratchpad>/sheet.
# Usage: assemble.py
import os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
E1 = os.path.normpath(os.path.join(HERE, "..", "..", "edition-one", "build"))
FA = os.path.normpath(os.path.join(HERE, "..", "..", "finished-ads"))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
def run(*a):
    r = subprocess.run([sys.executable, *a], capture_output=True, text=True)
    print(r.stdout.strip()[-1500:]); r.stderr.strip() and print(r.stderr.strip()[-800:])
    if r.returncode: sys.exit(r.returncode)

run(f"{HERE}/select.py", f"{SPB}/c4/final.json")
run(f"{E1}/select_e1.py", f"{SPB}/e1/final_e1.json")
shutil.rmtree(f"{SPB}/c4/pdf_out", ignore_errors=True); shutil.rmtree(f"{SPB}/e1/pdf_out", ignore_errors=True)
run(f"{HERE}/pdfs.py", f"{SPB}/c4/final.json", f"{SPB}/c4/pdf_out")
run(f"{E1}/pdfs_e1.py", f"{SPB}/e1/final_e1.json", f"{SPB}/e1/pdf_out")
shutil.rmtree(f"{SPB}/ads/pdf_out", ignore_errors=True)
run(f"{FA}/build_ads.py")
run(f"{FA}/ads_pdf.py", f"{SPB}/ads/pdf_out")
run(f"{HERE}/build_sheet.py")
