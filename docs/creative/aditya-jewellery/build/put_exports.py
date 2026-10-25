# PUTs exported listing JPEGs and size guides to Higgsfield presigned URLs from saved media_upload responses and records
# filename -> public CloudFront URL in url_map.json (the URL Shopify pulls). Only the first slot per filename is used.
import json, re, subprocess, sys, os
src, out = sys.argv[1], "url_map.json"
m = json.load(open(out)) if os.path.exists(out) else {}; ids = json.load(open(out + ".ids")) if os.path.exists(out + ".ids") else {}
for resp in sys.argv[2:]:
    for u in json.load(open(resp))["uploads"]:
        fn = re.search(r"--data-binary @(\S+)", u["instructions"]).group(1)
        if fn in m: continue
        code = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT", "-H", "Content-Type: " + u["content_type"],
                               "--data-binary", "@" + os.path.join(src, fn), u["upload_url"]], capture_output=True, text=True).stdout
        print(fn, code)
        if code == "200": m[fn] = u["url"]; ids[fn] = u["media_id"]
json.dump(m, open(out, "w"), indent=1); json.dump(ids, open(out + ".ids", "w"), indent=1)
print(len(m), "urls")
