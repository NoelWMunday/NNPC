# PROPOSAL (not applied) — Tax rolling balances and prior-year HCDT

- **Trello:** #20 decisions 3 and 4 (Noel 10 Nov 11:53: "propose the changes for the rolling balances"; "HCDT prior year as per Excel")
- **Status:** PROPOSAL — for review. Nothing is applied until agreed. The script syntax still needs SAC's Validate before it goes on a branch.

## How dates are stored (this decides the design)

- `Date` is monthly (2020–2041). Annual work-programme values sit on December (`yyyy12`).
- 2025 is split: Jan–Aug on `202508` with `Lock = Hist_Open`, and Sep–Dec on `202512` with `Lock` blank.
- Every Upstream script scopes `MEMBERSET [d/Lock] = "#"`, so `202508` is never calculated. Nothing derived from
  inputs (including `CST05`) exists for 2025 Jan–Aug.
- `PREVIOUS(1,"YEAR",[d/Date])` from `202612` returns `202512`. That gives the Sep–Dec slice of 2025, not the 2025 year.

## Problems

| # | Where | Problem |
|---|---|---|
| P1 | `PPP_Upstream_Tax` › 13 CA Limit Rolling Balance (Oil), line with `TAX055_25` | Closing = `PREVIOUS(1)` closing + addition − deduction, evaluated for all years in one statement. The prior year's closing is the value stored **before** the run, so results depend on how many times the calculation has run. |
| P2 | Same, `#PARAM1 = TAX055_10 + TAX055_15` | Opening balance `TAX055_10` is never written, so the limit test ignores the amount brought forward. |
| P3 | `PPP_Upstream_Tax` › 14 CA Limit Rolling Balance (Gas) | Same as P1/P2 for `TAX060_05` (opening) and `TAX060_20` (closing). |
| P4 | `PPP_Upstream_Tax` › 16 Hydrocarbon Tax, `TAX070_25` | Same pattern for the CPR balance; opening `TAX070_10` is never written. |
| P5 | `PPP_Upstream_Tax` › 1 Initialise | No `TAX*` line is cleared, so a value that should become empty keeps its old figure. |
| P6 | `PPP_Upstream_Tax` › 5, 6 HCDT | Base is same-year Opex. Decision: prior year, as in the Excel. |

## Proposed design

1. **Initialise clears Tax's own outputs:** `TAX*` on `PPP_Currency = "#"`, `Lock = "#"`, for the run entity.
2. **Rolling balances in year order:** steps 13, 14 and 16 wrap the balance logic in `FOREACH [d/Date] … ENDFOR` and
   restrict Date to December members. Inside the loop, each year:
   ```
   FOREACH [d/Date]
       // Opening = last year's closing (2025 closing is on 202512)
       DATA([d/WPLn]="TAX055_10") = RESULTLOOKUP([d/WPLn]="TAX055_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))
       DATA([d/WPLn]="TAX055_15") = RESULTLOOKUP([d/WPLn]="TAX045_05_10") + RESULTLOOKUP([d/WPLn]="TAX045_05_15")
       ... existing limit test, now using TAX055_10 + TAX055_15 ...
       DATA([d/WPLn]="TAX055_25") = RESULTLOOKUP([d/WPLn]="TAX055_10") + RESULTLOOKUP([d/WPLn]="TAX055_15")
                                  - RESULTLOOKUP([d/WPLn]="TAX055_20")
   ENDFOR
   ```
   Same shape for Gas (`TAX060_05/10/15/20`) and CPR (`TAX070_10/15/20/25`). With Initialise clearing first, a re-run
   gives identical results (SIT step 20).
3. **HCDT prior year:** base = last year's full-year Opex (`CST05_05` / `CST05_10`). That only works once the prior year
   exists as a whole year (see questions).

## Questions before building (Noel)

1. **2025 Jan–Aug (`Lock = Hist_Open`).** Should the calculation include it? Without it, 2025 has only the Sep–Dec slice.
   Then 2026 HCDT (prior year) and the 2025 balances are wrong. Options:
   (a) scope `Lock` to `("#","Hist_Open")` for reading inputs and derived cost lines, writing results only to `Lock "#"`;
   (b) treat 2025 as a single year for tax purposes by summing `202508 + 202512` where a prior year is needed.
2. **Starting balance.** What opens the first year (2022 or 2025)? `AMT_99` "Accumulated Capital Allowance" exists as an
   input line and looks intended for this, but no script reads it.
3. **First modelled year for tax.** Should balances run from 2022 (history), or from 2026 with an opening input?

Once these are answered I'll put the scripts on a branch, validate them in SAC, and test against the sheet's CA-limit and
CPR schedules (NUIMS §4.1 rows 2340–2429).
