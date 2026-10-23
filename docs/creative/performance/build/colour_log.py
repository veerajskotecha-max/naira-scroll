# Writes the shot log in ../COLOUR50.md (between the <!-- log --> markers) from colour50.json, so the plan and the record agree.
# colour_log.py --set crazy3 writes ../CRAZY3.md from crazy3.json instead.
import json, os, re
import sys
SET = sys.argv[2] if sys.argv[1:2] == ["--set"] else "colour"
JSON, MD = {"colour": ("colour50.json", "COLOUR50.md"), "crazy3": ("crazy3.json", "CRAZY3.md")}[SET]
HERE = os.path.dirname(os.path.abspath(__file__)); DOC = os.path.join(os.path.dirname(HERE), MD)
L = json.load(open(f"{HERE}/{JSON}"))
rows = [f"| # | Product | {'Object' if SET == 'crazy3' else 'Ingredient'} | Ground | Line | Score | Tries |", "|---|---|---|---|---|---|---|"]
for e in L:
    name = e["title"] + (f" ({e['variant']})" if e.get("variant") else "")
    rows.append(f"| {e['n']} | {name} | {e['ingredient']} | {e['ground']} | {e['line']} | {e['score']} | {len(e['jobs'])} |")
scores = [e["score"] for e in L]
head = (f"{len(L)} shots kept, average score {sum(scores) / len(scores):.2f}, {sum(len(e['jobs']) for e in L)} frames rendered. "
        f"Each shot's notes, kept job and rhyme are in `build/{JSON}`; plates in `plates/{SET}/`, Feed and Story ads in `ads/{SET}/`.")
block = "<!-- log -->\n" + head + "\n\n" + "\n".join(rows) + "\n<!-- /log -->"
doc = open(DOC).read()
doc = re.sub(r"<!-- log -->.*?<!-- /log -->", block, doc, flags=re.S) if "<!-- log -->" in doc else doc.rstrip() + "\n\n## Shot log\n\n" + block + "\n"
open(DOC, "w").write(doc); print(len(L), "rows")
