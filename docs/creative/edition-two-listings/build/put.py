# PUTs files to Higgsfield presigned upload URLs from a saved media_upload response; records name -> media_id.
import json, re, subprocess, sys, os
resp, refdir, out = sys.argv[1:4]
ids = json.load(open(out)) if os.path.exists(out) else {}
for u in json.load(open(resp))["uploads"]:
    fn = re.search(r"--data-binary @(\S+)", u["instructions"]).group(1)
    code = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT", "-H", "Content-Type: " + u["content_type"],
                           "--data-binary", "@" + os.path.join(refdir, fn), u["upload_url"]], capture_output=True, text=True).stdout
    print(fn, code)
    if code == "200": ids[fn[:-4]] = u["media_id"]
json.dump(ids, open(out, "w"), indent=1)
