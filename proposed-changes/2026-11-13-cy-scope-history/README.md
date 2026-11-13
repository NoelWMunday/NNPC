# Change proposal — CY scope keeps the history that later steps read

- **Trello:** #22 https://trello.com/c/j5RV7K5l, #27 https://trello.com/c/7eH24KWh
- **Follows:** Noel's CY+1…CY+5 scope (13 Nov, Royalties v45 / Tax v26), see `DEPLOYMENTS.md`
- **Status:** PROPOSED
- **Scripts:** [DIFF.md](DIFF.md), [manifest.json](manifest.json)

## Why

With every step on CY+1…CY+5, four calculations lose inputs they read from earlier years:

| Reader | Reads | Built by | Effect with CY+1…CY+5 only |
|---|---|---|---|
| Tax › 5 / 6 HCDT | `CST05_05` / `CST05_10` at `PREVIOUS(1,"YEAR")` (CY Dec) | Royalties › 14–17 (rollup of Hist_Open + Lock `#` into Dec), cleared by Royalties › 1 | CY Dec no longer rebuilt; HCDT reads whatever an earlier run left |
| Tax › 11 amortisation | `TAX040_*` at `PREVIOUS(1..4,"YEAR")` (CY-3 … CY Dec) | Tax › 10 (`DATA.APPEND`), cleared by Tax › 1 | 2022–2025 no longer rebuilt; 2026 amortisation reads stale or missing history |

Both builders use `DATA.APPEND`, so their range must match the clearing step's range, or values double up on re-runs.

## Change

| Steps | Date scope |
|---|---|
| Royalties › 1 Initialise, › 14–17 cost rollups | `PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)` — CY Jan … CY+5 Dec |
| Tax › 1 Initialise, › 10 CAPEX Components | `PREVIOUS(47,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)` — CY-3 Jan … CY+5 Dec |

All other steps stay on CY+1…CY+5. Tax results for 2022–2025 other than `TAX040_*` are cleared by Tax › 1 and not recalculated
(tax runs for CY+1 onward only). Rolling balances (Tax › 13/14/16) then open 2026 at 0, as the sheet does.

Rollback: apply the left side of [DIFF.md](DIFF.md).
