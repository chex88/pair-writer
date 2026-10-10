# Pair Writer: Collaborative Intelligence capstone (C7)

Task: a Captavis colleague writes sales and marketing messages. Three arms on the same briefs: person alone, agent alone, person plus agent.

Live tool: https://claude.ai/artifact/Hsd9TaEjaWA6sqWr5XDKEh

## Files
- `pair-writer/index.html`: the tool (single page). Logs every run and exports `runs.csv`.
- `workflow.json`: the loop as a specification.
- `prompts/arm2_agent_alone.md`: the agent-alone prompt.
- `eval/blind_pack.py`: strips arm labels and shuffles messages for a blind judge.
- `eval/analyze.py`: per-arm accuracy, audience fit, send-as-is rate, time, unsupported claims.

## Run the evaluation
1. Export `runs.csv` from the tool.
2. `python eval/blind_pack.py runs.csv`
3. Judge fills `judge_sheet.csv` without seeing arms.
4. `python eval/analyze.py judge_sheet.csv key.csv`

## Design decisions
- Only a score and one tag cross from person to agent (the brief found free-text advice made pairs worse).
- Audience and tone are required inputs (naming the audience was the biggest measured lever).
- Every factual claim in a draft must trace to a listed fact or is flagged UNSUPPORTED.
- The tool measures the pair and the system, never a person for any consequential decision.

## Status and limitations
Pilot only: one builder as the user, six briefs, 18 runs, no independent judge. The pair arm in the first round did not run a revision, so no pair result is claimed. See the case study for the full account and the design changes made afterwards. Raw run logs are not included because they contain recipient names and links from real emails.
