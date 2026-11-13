# Change proposal — CY scope: keep the history later steps read; December-only tax

- **Trello:** #22 https://trello.com/c/j5RV7K5l, #27 https://trello.com/c/7eH24KWh
- **Follows:** Noel's CY+1…CY+5 scope (13 Nov; Royalties v45, Tax v26 — see `DEPLOYMENTS.md`)
- **Status:** PROPOSED
- **Scripts:** [DIFF.md](DIFF.md), [manifest.json](manifest.json) — 19 steps

## 1. History the scope cuts off

| Reader | Reads | Built by (cleared by) | With CY+1…CY+5 only |
|---|---|---|---|
| Tax › 5 / 6 HCDT | `CST05_05` / `CST05_10` at `PREVIOUS(1,"YEAR")` = CY Dec | Royalties › 14–17 rollups (Royalties › 1) | CY Dec is no longer rebuilt; HCDT reads whatever an earlier run left |
| Tax › 11 amortisation | `TAX040_*` at `PREVIOUS(1..4,"YEAR")` = CY-3 … CY Dec | Tax › 10 (Tax › 1) | 2022–2025 no longer rebuilt; 2026 amortisation reads stale or missing history |

Both builders use `DATA.APPEND`, so their range must equal their clearing step's range (else values double on re-run).

| Steps | Date scope |
|---|---|
| Royalties › 1, › 14–17 | `PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)` (CY Jan … CY+5 Dec) |
| Tax › 1, › 10 | `PREVIOUS(47,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)` (CY-3 Jan … CY+5 Dec) |

Everything else stays on CY+1…CY+5. Tax › 1 now also clears 2022–2025 tax results; only `TAX040_*` is rebuilt for those years.

## 2. Non-December tax records (#27)

`NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)` is a month range (202612 … 203012). Tax has 18 statements that copy a rate
from Date `000000` (e.g. › 9 `TAX035_10 = TA20_05`); with `GENERATE_UNBOOKED_DATA = ON` each writes the rate into every month in
scope — the 16 × 11 non-December records per year QA found (the two `SET10_10` lines are empty for RENAISSANCE).
A December-only `MEMBERSET` cannot be combined with a year range in SAC (tested: a list of `NEXT()` and a second
`MEMBERSET` on `[p/MONTHDESC]` are both rejected), so each of the 18 statements gets the tenant's existing guard:

```
IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX035_10") = RESULTLOOKUP(... [d/Date]="000000") ENDIF
```

Steps: Tax › 3, 4, 5, 6, 7, 8, 9, 12, 13, 16, 19, 20. All other tax lines multiply these rates or read December values, so
they stay December-only.

## 3. Clean-up of existing records (separate, needs approval)

RENAISSANCE today (`#` currency/entry, Lock `#`, read 13 Nov):

| Years | Records |
|---|---|
| 2020–2021 | `TAX*` 32 December + 352 other months |
| 2022–2025 | `TAX*` December + 704 other months; `REV*` / `RC*` / `CST*` calculated lines; `AMT*` / `UOM*` inputs |
| 2026–2030 | `TAX*` 880 non-December records |

After this change and one run, Tax › 1 clears 2022–2030 (all months) and the run rebuilds what is needed. Left behind:
`TAX*` 2020–2021, and `REV*` / `RC*` / `CST*` calculated lines for years up to CY (except `CST05_*` CY December), and GL postings
before CY+1. Proposed: a one-off data action **PPP_Upstream_Housekeeping** (parameters Entity, CY) that deletes those
calculated lines outside the window. Inputs (`AMT*`, `UOM*`, `SET*`, Hist_Open) are not touched.

Rollback (scripts): apply the left side of [DIFF.md](DIFF.md).
