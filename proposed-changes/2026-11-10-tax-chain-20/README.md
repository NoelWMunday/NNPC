# Change — #20 JV tax chain: cost bases, gross royalty, rate and setting dates

- **Trello:** #20 https://trello.com/c/3zpHY6z7 (QA root causes 10:55; Noel 11:18 "remaining items with dev")
- **Builds on:** Noel's direct edits 11:02–11:14 (Tax step 1 no longer deletes `CST05`; tax rates entered in Admin)
- **Status:** APPROVED — applying
- **Scripts:** [DIFF.md](DIFF.md) · [manifest.json](manifest.json) · one file per step. 10 steps of `PPP_Upstream_Tax`, 16
  lines, line counts unchanged (tracepoints unaffected).

## Changes

| Step | Was | Now | #20 item |
|---|---|---|---|
| 3 NDDC Oil | bases `AMT_220` / `AMT_200` on USD at entry `#` (only stale totals ever existed there) | `CST05_05` Total OPEX Oil / `CST05_15` Total CAPEX Oil | A |
| 4 NDDC Gas | `AMT_230` / `AMT_210` at entry `#`; payable × oil rate `TAX025_10` | `CST05_10` / `CST05_20`; × gas rate `TAX030_10` (same value today) | A |
| 5 HCDT Oil | `AMT_220` at entry `#` | `CST05_05` | A |
| 6 HCDT Gas | `AMT_230` at entry `#` | `CST05_10` (excludes gas flare penalty) | A |
| 7 Dev Levy Oil | `TAX005_15_20` = equity PA production royalty `RC30_10` | gross `RC30_05`, like PPT, HT and CITA (revenue is gross) | C |
| 8 Dev Levy Gas | `TAX010_15_15` = `AMT_230` at entry `#` | `CST05_10` | A |
| 12 CA for PPT | `TA30_10`, `TA30_15` at Date `202612` | Date `000000`, where Admin stores every rate | B (Noel) |
| 16 HT | regime flag `SET10_10` read at entity `#` / Lock Central (always empty) | the asset's own setting at Date `000000` | found |
| 19 PPT | `SET10_05` read with no date (empty for every year) → PPT always 0 | Date `000000` | D |
| 20 CITA | `SET10_10` read with no date | Date `000000` (3 lookups) | found |

Settings live at Date `000000`. The PA royalty steps read them there, and royalties tie to the sheet.

## Expected 2026 results, RENAISSANCE JV ($M)

| Line | SAC after change | Sheet | Note |
|---|---|---|---|
| NDDC Oil / Gas | 73.38 / 36.78 | 73.38 / 36.78 | |
| HCDT Oil / Gas | 44.66 / 6.33 | 0 / 0 | Sheet bug: HCDT formula points at the blank 2026-source column (findings §8) |
| Dev Levy Oil / Gas | 77.09 / 36.12 | 78.43 / 36.31 | Difference = the sheet's missing HCDT deduction. With HCDT = 0 SAC reproduces 78.43 / 36.31 exactly |
| Cost bases TAX025_15_05/10, TAX030_15_05/10 | 1,488.52 / 957.46 / 211.00 / 1,015.16 | same | |
| PPT, CA for PPT, HT lines | populated (rates now entered) | 1,864.73 / 478.83 / … | values downstream depend on the decisions below |

## Not changed — decisions needed (Noel)

1. **CITA Gas under the PPT regime.** `TAX090_20` (gas CITA) is multiplied by the PIA flag `SET10_10`, so it is 0 for a
   PPT asset. The sheet charges CITA on gas under PPT (Renaissance 291.29), which matches gas being outside PPT. Proposal:
   drop the `SET10_10` factor from the gas line only. Oil CITA stays gated (oil is under PPT).
2. **Tax › Initialise deletes other data actions' lines.** It deletes `CST14` (built by CostAlloc), `REV_32/26/40` and
   `REV3_05` (owned by Revenue › Initialise). Results aren't affected because those lines are consumed first, but after a run
   "Total costs to be apportioned" and the revenue totals are blank on the References tab. Proposal: Tax › Initialise
   deletes only what Tax writes.
3. **Tax results are never cleared, and the rolling balances aren't repeatable.** `TAX055_25`, `TAX060_20` and `TAX070_25`
   add `PREVIOUS(1)` of themselves without a `FOREACH` over Date. Each run builds on the previous run's balances, and
   values that should drop to nothing stay. Proposal: clear `TAX*` in Initialise and compute the balances in date order.
   This needs a design pass and a test against the sheet's CA-limit schedule.
4. **HCDT basis** (open since 9 Nov): SAC uses same-year Opex. The Excel intends prior-year (PIA s.240).
5. **Royalties steps 3–4 read `SET05_*` at Date `202612`** (35 lookups), while everything else uses `000000`. If the
   settings exist only at `000000`, the PIA tranche royalties read nothing. That doesn't show for Renaissance (PA path).

## Test

Run Upstream (Calculations) for RENAISSANCE JV, Budget 2026 (Reference), CAPEX_Version the same. Check the values above,
then re-run and confirm the levies are unchanged. Rolling balances may move on re-run (decision 3).

## Rollback

Apply the left side of [DIFF.md](DIFF.md).
