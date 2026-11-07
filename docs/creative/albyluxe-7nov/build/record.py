# Records generation job ids: record.py KEY=JOB_ID ... -> merges into jobs.json (KEY is the frame key, e.g. L01_H).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); P = f"{H}/jobs.json"
J = json.load(open(P)) if os.path.exists(P) else {}
for kv in sys.argv[1:]:
    k, v = kv.split("=", 1); J[k] = v; print(k, v)
json.dump(J, open(P, "w"), indent=1)
