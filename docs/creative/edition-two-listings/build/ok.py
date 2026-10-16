# Approves shots: ok.py KEY [KEY...] copies their job IDs from jobs.json into approved.json (KEY or KEY=JOBID).
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__)); J = json.load(open(f"{H}/jobs.json")); A = json.load(open(f"{H}/approved.json"))
for a in sys.argv[1:]:
    k, v = a.split("=") if "=" in a else (a, J[a]); A[k] = v
json.dump(A, open(f"{H}/approved.json", "w"), indent=1); print(len(A))
