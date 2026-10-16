# PUTs exported listing JPEGs to Higgsfield presigned URLs from a saved media_upload response and records
# filename -> {media_id, public url} in url_map.json (the public CloudFront URL is what Shopify pulls).
import json, re, subprocess, sys, os
resp, srcdir, out = sys.argv[1:4]
m = json.load(open(out)) if os.path.exists(out) else {}; ids = json.load(open(out + ".ids")) if os.path.exists(out + ".ids") else {}
for u in json.load(open(resp))["uploads"]:
    fn = re.search(r"--data-binary @(\S+)", u["instructions"]).group(1)
    code = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT", "-H", "Content-Type: " + u["content_type"],
                           "--data-binary", "@" + os.path.join(srcdir, fn), u["upload_url"]], capture_output=True, text=True).stdout
    print(fn, code)
    if code == "200": m[fn] = u["url"]; ids[fn] = u["media_id"]
json.dump(m, open(out, "w"), indent=1); json.dump(ids, open(out + ".ids", "w"), indent=1)
print(len(m), "urls")
