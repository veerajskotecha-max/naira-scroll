# Writes the shot log in ../COLOUR50.md (between the <!-- log --> markers) from colour50.json, so the plan and the record agree.
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); DOC = os.path.join(os.path.dirname(HERE), "COLOUR50.md")
L = json.load(open(f"{HERE}/colour50.json"))
rows = ["| # | Product | Ingredient | Ground | Line | Score | Tries |", "|---|---|---|---|---|---|---|"]
for e in L:
    name = e["title"] + (f" ({e['variant']})" if e.get("variant") else "")
    rows.append(f"| {e['n']} | {name} | {e['ingredient']} | {e['ground']} | {e['line']} | {e['score']} | {len(e['jobs'])} |")
scores = [e["score"] for e in L]
head = (f"{len(L)} shots kept, average score {sum(scores) / len(scores):.2f}, {sum(len(e['jobs']) for e in L)} frames rendered. "
        "Each shot's notes, kept job and rhyme are in `build/colour50.json`; plates in `plates/colour/`, Feed and Story ads in `ads/colour/`.")
block = "<!-- log -->\n" + head + "\n\n" + "\n".join(rows) + "\n<!-- /log -->"
doc = open(DOC).read()
doc = re.sub(r"<!-- log -->.*?<!-- /log -->", block, doc, flags=re.S) if "<!-- log -->" in doc else doc.rstrip() + "\n\n## Shot log\n\n" + block + "\n"
open(DOC, "w").write(doc); print(len(L), "rows")
