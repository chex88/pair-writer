"""Step 1: turn the exported runs.csv into a blind judge sheet.
Usage: python blind_pack.py runs.csv
Outputs judge_sheet.csv (give this to the judge) and key.csv (keep this; maps ids to arms)."""
import csv, random, sys
rows = list(csv.DictReader(open(sys.argv[1], newline="", encoding="utf-8")))
random.seed(7); random.shuffle(rows)
with open("judge_sheet.csv", "w", newline="", encoding="utf-8") as j, open("key.csv", "w", newline="", encoding="utf-8") as k:
    jw = csv.writer(j); kw = csv.writer(k)
    jw.writerow(["id", "label", "audience", "tone", "message", "accuracy_1to5", "audience_fit_1to5", "send_as_is_yes_no"])
    kw.writerow(["id", "label", "arm", "secs", "rounds", "unsupported", "accepted"])
    for i, r in enumerate(rows, 1):
        jw.writerow([i, r["label"], r["audience"], r["tone"], r["message"], "", "", ""])
        kw.writerow([i, r["label"], r["arm"], r["secs"], r["rounds"], r["unsupported"], r["accepted"]])
print(f"{len(rows)} runs written. Give judge_sheet.csv to the judge.")
