"""Step 2: join the filled judge sheet with key.csv and report per-arm results.
Usage: python analyze.py judge_sheet.csv key.csv"""
import csv, sys, statistics as st
J = {r["id"]: r for r in csv.DictReader(open(sys.argv[1], newline="", encoding="utf-8"))}
K = {r["id"]: r for r in csv.DictReader(open(sys.argv[2], newline="", encoding="utf-8"))}
names = {"1": "Person alone", "2": "Agent alone", "3": "Pair"}
print(f"{'Arm':14}{'n':>3}{'accuracy':>10}{'aud.fit':>9}{'send as-is':>12}{'median sec':>12}{'unsupported/run':>17}")
for arm in "123":
    ids = [i for i in K if K[i]["arm"] == arm and J[i]["accuracy_1to5"].strip()]
    if not ids: print(f"{names[arm]:14}{0:>3}  (no judged runs)"); continue
    acc = st.mean(float(J[i]["accuracy_1to5"]) for i in ids)
    fit = st.mean(float(J[i]["audience_fit_1to5"]) for i in ids)
    sa = sum(J[i]["send_as_is_yes_no"].strip().lower().startswith("y") for i in ids) / len(ids)
    sec = st.median(float(K[i]["secs"]) for i in ids)
    uns = st.mean(float(K[i]["unsupported"] or 0) for i in ids)
    print(f"{names[arm]:14}{len(ids):>3}{acc:>10.2f}{fit:>9.2f}{sa:>11.0%}{sec:>12.0f}{uns:>17.2f}")
