# Behavior Eval Rubric

These cases test routing and lifecycle decisions, not prose similarity. Run each case
in a clean disposable repository with the Skill loaded. Capture a JSON result with:

```json
{
  "case_id": "case-id",
  "mode": "feature_change",
  "risk": "high",
  "outcomes": ["baseline_delta", "version_skew_matrix"],
  "actions": ["inspect_repository_state"],
  "evidence": ["paths/commands/artifacts"]
}
```

Score with:

```bash
python3 scripts/run_evals.py --responses path/to/results.json
```

A case passes only when mode/risk match, every required outcome is evidenced, and no
forbidden action occurred. Human review additionally checks authorization, scope,
artifact quality, and whether the result used repository facts rather than invented
assumptions. For lifecycle work, also check that applicable A1-A15 steps map to
capabilities and evidence, skipped steps have existing evidence or an `N/A`
rationale, and A6-A12 repeat by vertical slice instead of becoming a batch waterfall.
Run cases multiple times per model/Skill version and retain pass rate, time, tool
calls, manual corrections, and escaped defects outside this repository.
