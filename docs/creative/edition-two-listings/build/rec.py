# Records submitted jobs: rec.py KEY=JOBID ... into jobs.json
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__)); p = f"{H}/jobs.json"; j = json.load(open(p))
for a in sys.argv[1:]: k, v = a.split("="); j[k] = v
json.dump(j, open(p, "w"), indent=1); print(len(j))
