# Deployments to SAC

What is live in SAC, and which commit it came from. Newest first. (Git tags can't be pushed from the
working environment, so this log replaces them.)

To roll back an entry: apply the "SAC before" side of its `DIFF.md` (equally, `sac-export/` at the
commit before the merge), then commit a new snapshot and add a line here.

| Date (SAST) | Trello | Change | Commit applied | SAC objects → version | Verified |
|---|---|---|---|---|---|
| 2026-11-10 09:14–09:18 | [#19](https://trello.com/c/VYeHuGjg) | Correction: metric and settings lookups back to `PPP_Currency = "#"`; only `AMT_200/210/220/230` read USD ([proposal](proposed-changes/2026-11-10-upstream-metrics-on-hash/README.md)) | `c59bdfe` | `PPP_Upstream_Tax` v7 (4 steps) · `PPP_Upstream_Royalties` v36 (12 steps) · `PPP_Upstream_Revenue` v18 (1 step) | Live step lists hash-identical to `sac-export/`; tracepoints unchanged |
| 2026-11-10 08:10–08:20 | [#19](https://trello.com/c/VYeHuGjg) | Upstream data actions read inputs from `PPP_Currency = USD` ([proposal](proposed-changes/2026-11-09-upstream-currency-usd/README.md)) | `c9d5952` | `PPP_Upstream_Revenue` v17 (1 step) · `PPP_Upstream_Royalties` v35 (20 steps) · `PPP_Upstream_Tax` v6 (11 steps) | Live step lists hash-identical to `sac-export/`; SAC validation: no errors |
