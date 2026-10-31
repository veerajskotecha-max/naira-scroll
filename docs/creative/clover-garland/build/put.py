# PUTs files to the presigned Higgsfield upload URLs in a saved media_upload response and records filename -> public
# CloudFront URL in url_map.json (the URLs Shopify pulls) and filename -> media id in url_map.json.ids. Nothing printed is a
# signed URL. Usage: python3 -I put.py RESPONSE.json DIR [DIR ...]  (each filename is looked for in the DIRs in turn)
import json, os, re, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "url_map.json")
m = json.load(open(OUT)) if os.path.exists(OUT) else {}; ids = json.load(open(OUT + ".ids")) if os.path.exists(OUT + ".ids") else {}
resp, dirs = sys.argv[1], sys.argv[2:]
done = []
for u in json.load(open(resp))["uploads"]:
    fn = re.search(r"--data-binary @(\S+)", u["instructions"]).group(1)
    path = next(os.path.join(d, fn) for d in dirs if os.path.exists(os.path.join(d, fn)))
    code = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT", "-H", "Content-Type: " + u["content_type"],
                           "-H", "If-None-Match: *", "--data-binary", "@" + path, u["upload_url"]], capture_output=True, text=True).stdout
    print(fn, code)
    if code == "200": m[fn] = u["url"]; ids[fn] = u["media_id"]; done.append(u["media_id"])
json.dump(m, open(OUT, "w"), indent=1); json.dump(ids, open(OUT + ".ids", "w"), indent=1)
print(json.dumps(done))
