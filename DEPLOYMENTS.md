# Deployments to SAC

What is live in SAC, and which commit it came from. Newest first. (Git tags can't be pushed from the
working environment, so this log replaces them.)

To roll back an entry: apply the "SAC before" side of its `DIFF.md` (equally, `sac-export/` at the
commit before the merge), then commit a new snapshot and add a line here.

| Date (SAST) | Trello | Change | Commit applied | SAC objects → version | Verified |
|---|---|---|---|---|---|
| 2026-11-10 13:13 | [#20](https://trello.com/c/3zpHY6z7) | **Direct SAC edit by Noel** (snapshotted after the fact): Royalties › 14–17 cost loops append to `[d/Date] = LAST()` so all periods of a year roll into December | — | `PPP_Upstream_Royalties` v40 | Reconstructed steps hash-identical to live |
| 2026-11-10 11:57–11:59 | [#20](https://trello.com/c/3zpHY6z7) | Tax › 1 Initialise no longer deletes `CST14`; Royalties › 3, 4 read `SET05_*` at Date `000000` (35 lookups) ([note](proposed-changes/2026-11-10-tax-init-settings-dates/README.md)) | `58435d4` | `PPP_Upstream_Tax` v10 (1 step) · `PPP_Upstream_Royalties` v39 (2 steps) | Live step lists hash-identical to `sac-export/` |
| 2026-11-10 11:26 | [#20](https://trello.com/c/3zpHY6z7) | JV tax chain: cost bases from `CST05`, gross PA royalty in Dev Levy Oil, CA-for-PPT rates and regime flags at Date `000000` ([proposal](proposed-changes/2026-11-10-tax-chain-20/README.md)) | `9e8e855` | `PPP_Upstream_Tax` v9 (10 steps) | Live step list hash-identical to `sac-export/`; SAC validation: no errors |
| 2026-11-10 11:02–11:14 | [#20](https://trello.com/c/3zpHY6z7) | **Direct SAC edits by Noel** (outside the workflow; snapshotted after the fact): Tax step 1 no longer deletes `CST05`; Royalties step 1 USD→`#` copy lines commented out | — | `PPP_Upstream_Tax` v8 · `PPP_Upstream_Royalties` v38 | Reconstructed scripts hash-identical to live |
| 2026-11-10 09:34–09:36 | [#19](https://trello.com/c/VYeHuGjg) | Capex/Opex inputs copied to `#` for the Financial tab (Royalties step 1); dead COS/Depletion comments removed (CostAlloc step 13) ([proposal](proposed-changes/2026-11-10-financial-tab-and-cos-cleanup/README.md)) | `14dae49` | `PPP_Upstream_Royalties` v37 (1 step) · `PPP_Upstream_CostAlloc` v29 (1 step) | Live step lists hash-identical to `sac-export/`; SAC validation: no errors |
| 2026-11-10 09:14–09:18 | [#19](https://trello.com/c/VYeHuGjg) | Correction: metric and settings lookups back to `PPP_Currency = "#"`; only `AMT_200/210/220/230` read USD ([proposal](proposed-changes/2026-11-10-upstream-metrics-on-hash/README.md)) | `c59bdfe` | `PPP_Upstream_Tax` v7 (4 steps) · `PPP_Upstream_Royalties` v36 (12 steps) · `PPP_Upstream_Revenue` v18 (1 step) | Live step lists hash-identical to `sac-export/`; tracepoints unchanged |
| 2026-11-10 08:10–08:20 | [#19](https://trello.com/c/VYeHuGjg) | Upstream data actions read inputs from `PPP_Currency = USD` ([proposal](proposed-changes/2026-11-09-upstream-currency-usd/README.md)) | `c9d5952` | `PPP_Upstream_Revenue` v17 (1 step) · `PPP_Upstream_Royalties` v35 (20 steps) · `PPP_Upstream_Tax` v6 (11 steps) | Live step lists hash-identical to `sac-export/`; SAC validation: no errors |
