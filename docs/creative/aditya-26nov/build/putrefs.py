# PUTs reference crops to the presigned Higgsfield upload URLs in a saved media_upload response and records
# <key> -> media id in ref_ids.json (key = filename without .jpg). Nothing printed is a signed URL.
# Usage: python3 -I putrefs.py RESPONSE.json REFS_DIR
import json, os, re, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "ref_ids.json")
ids = json.load(open(OUT)) if os.path.exists(OUT) else {}
ok = []
for u in json.load(open(sys.argv[1]))["uploads"]:
    fn = re.search(r"--data-binary @(\S+)", u["instructions"]).group(1)
    code = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT", "-H", "Content-Type: " + u["content_type"],
                           "-H", "If-None-Match: *", "--data-binary", "@" + os.path.join(sys.argv[2], fn), u["upload_url"]],
                          capture_output=True, text=True).stdout
    print(fn, code)
    if code == "200": ids[fn[:-4]] = u["media_id"]; ok.append(u["media_id"])
json.dump(ids, open(OUT, "w"), indent=1); print(json.dumps(ok))
