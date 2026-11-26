# Downloads finished Higgsfield results: fetch.py KEY=URL ... -> out/KEY.png, and records KEY -> URL in results.json.
import json, os, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{H}/out", exist_ok=True)
R = json.load(open(f"{H}/results.json")) if os.path.exists(f"{H}/results.json") else {}
for kv in sys.argv[1:]:
    k, u = kv.split("=", 1)
    subprocess.run(["curl", "-sS", "-o", f"{H}/out/{k}.png", u], check=True); R[k] = u; print(k)
json.dump(R, open(f"{H}/results.json", "w"), indent=1)
