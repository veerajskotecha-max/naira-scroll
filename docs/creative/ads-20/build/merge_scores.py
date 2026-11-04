# Folds the independent judge's rounds into scores.json: round 1 (Sets 1-2 as first built) and round 2 (all 20 after the fixes),
# each with the benchmark and Naira's recent ads re-scored as calibration. Usage: merge_scores.py judge_r1.json judge_r2.json
import json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def means(ads):
    out = {}
    for a in ads:
        out.setdefault(a["group"], []).append(a["score"])
    return {g: round(statistics.mean(v), 2) for g, v in out.items()}

def main():
    p = os.path.join(HERE, "scores.json"); sc = json.load(open(p))
    rounds = {}
    for name, f in (("round1", sys.argv[1]), ("round2", sys.argv[2])):
        j = json.load(open(f))
        rounds[name] = {"order": j["order"], "means": means(j["ads"]),
                        "ads": [{k: a[k] for k in ("id", "group", "s", "score", "best", "fix")} for a in j["ads"]],
                        "set_notes": j.get("set_notes", {}), "lessons": j.get("next_set"), "launch": j.get("launch")}
    sc["judge"] = {"_about": "An independent judge (a separate agent that saw only the images and this rubric, never these scores) "
                   "scored every ad by eye. Round 1: Sets 1-2 as first built. Round 2: all 20 after the round-1 fixes and Sets 3-4.",
                   **rounds}
    sc["sets"] = {g: v for g, v in rounds["round2"]["means"].items() if g.startswith("set")}
    json.dump(sc, open(p, "w"), indent=1, ensure_ascii=False)
    print(json.dumps({"round1": rounds["round1"]["means"], "round2": rounds["round2"]["means"]}, indent=1))

if __name__ == "__main__":
    main()
