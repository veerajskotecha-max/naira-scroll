# Job ledger: every Higgsfield job id, which frame it shot and the attempt number. Usage: ledger.py add T01:a1:<job_id> ...
import json, sys, os
here = os.path.dirname(os.path.abspath(__file__)); path = f"{here}/jobs.json"
L = json.load(open(path)) if os.path.exists(path) else []
if sys.argv[1] == "add":
    for a in sys.argv[2:]:
        fid, att, job = a.split(":"); L.append(dict(frame=fid, attempt=att, job=job))
    json.dump(L, open(path, "w"), indent=1)
print(len(L), "jobs")
