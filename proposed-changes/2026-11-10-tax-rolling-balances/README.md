# Change — #20 Tax rolling balances, prior-year HCDT, full-year cost rollup

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Decisions (Noel, 10 Nov 13:23):** (3) use the proposed rolling-balance code. (4) HCDT on prior-year Opex. Noel changed the
  Royalties cost rollup to `[d/Date] = LAST()` so the full prior year lands on December. (Q1) Closed periods hold YTD to the close
  month (e.g. `202508`), and later periods hold the rest. Users manage this. (Q2) No generic opening balances. (Q3) Tax runs for
  planning periods CY+1 onward.
- **Replaces:** [2026-11-10-tax-rolling-balances-PROPOSAL](../2026-11-10-tax-rolling-balances-PROPOSAL/README.md)
- **Status:** APPLIED 10 Nov 2026 13:33 SAST (commit `bcff8cf`) — see `DEPLOYMENTS.md`. Awaiting retest.
- **Scripts:** [DIFF.md](DIFF.md) · [manifest.json](manifest.json)

## Changes

| Data action › step | Line(s) after change | Change |
|---|---|---|
| `PPP_Upstream_Tax` › 1 "Initialise" | 8–10, 18–19 | Also deletes `BASEMEMBER([d/WPLn],"TAX")`, so every Tax result is rebuilt each run |
| `PPP_Upstream_Tax` › 5 "Tax - HCDT Fund Payable (Oil)" | `TAX015_15` | `CST05_05` at `PREVIOUS(1,"YEAR")`, i.e. prior-year full Opex Oil |
| `PPP_Upstream_Tax` › 6 "Tax - HCDT Fund Payable (Gas)" | `TAX020_15` | `CST05_10` at `PREVIOUS(1,"YEAR")` |
| `PPP_Upstream_Tax` › 13 "Tax - CA Limit Rolling Balance (Oil)" | from the `FOREACH` | `FOREACH [d/Date]`: opening `TAX055_10` = prior closing; limit test; closing = opening + addition − deduction |
| `PPP_Upstream_Tax` › 14 "Tax - CA Limit Rolling Balance (Gas)" | from the `FOREACH` | same for `TAX060_05/10/15/20` |
| `PPP_Upstream_Tax` › 16 "Tax - Hydrocarbon Tax (CPR Limit & HT Payable)" | from the `FOREACH` | same for CPR `TAX070_10/15/20/25`; HT payable lines stay after the loop |
| `PPP_Upstream_Royalties` › 14–17 "Costs - CAPEX/OPEX Oil/Gas" | `MEMBERSET [d/Lock]`, `DATA.APPEND` | Read `Lock = ("#","Hist_Open")` and write `[d/Lock] = "#"` |

### Why the Royalties Lock change

Noel's `LAST()` rollup is meant to put the full prior year on December. The loops were scoped to `Lock = "#"`, but the closed
YTD value sits on the close month with `Lock = Hist_Open` (Renaissance: Opex Oil `202508` 1,056.15). It was skipped, so
`202512` held only Sep–Dec (712.85) instead of the year (1,769.00). Including `Hist_Open` and writing to `Lock "#"` (where
every reader looks) completes the year.

## Expected, RENAISSANCE JV 2026 ($M)

| Line | Expected | Sheet | Note |
|---|---|---|---|
| `CST05_05` 2025 (on `202512`) | 1,769.00 | 1,769.00 (YEO) | |
| HCDT Oil `TAX015_05` | 53.07 | 0 | Sheet formula points at the blank column W; intended value is 3% × 1,769 = 53.07 |
| HCDT Gas `TAX020_05` | 0 | 0 | 2025 gas Opex is 0 |
| Dev Levy Gas | 36.31 | 36.31 | Now ties: no HCDT gas deduction |
| CA limit closing Oil/Gas, CPR closing | 0 every year | 0 | Limits don't bind for Renaissance, so deduction = in-year addition (Oil 342.15, Gas 203.03, CPR 1,620.06) |
| Re-run unchanged | identical | | |

## Open

- **CY+1 start:** the scripts don't restrict dates, so Tax also calculates 2025 (from `202512` data). The 2026 opening balances are
  2025's calculated closings, which are 0 for Renaissance. To start strictly at CY+1, use the planning cycle's `Year` property
  (`PCycle` `2026-2030/01` has Year 2026). That needs a syntax check in SAC first; proposed as a follow-up.
- **CITA gas:** `PPP_Upstream_Tax` › 20 "Tax - CITA (Oil & Gas)" › line 25 still multiplies by the PIA flag. The sheet's JV CITA – Gas
  (NUIMS row 2426, `=MAX(X2423*X2411,0)`) has no flag; JV CITA – Oil (row 2425) does. Awaiting Noel.

## Rollback

Apply the left side of [DIFF.md](DIFF.md).
