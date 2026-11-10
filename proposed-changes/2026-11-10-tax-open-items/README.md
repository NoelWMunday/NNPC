# Change proposal — #20 open items after the 14:10 retest

- **Trello:** #20 https://trello.com/c/3zpHY6z7 (QA retest 10 Nov ~14:10; Noel 14:45 "remaining open with dev")
- **Status:** A and B APPLIED 10 Nov 15:33 SAST (`de0839c`, Tax v15). C APPLIED 15:42 (Tax v16, [note](../2026-11-10-tax-ppt-base-nddc-hcdt/README.md)); D with Noel; E APPLIED 15:44 (Tax v17, [note](../2026-11-10-cita-gas-capital-allowance/README.md)
- **Scripts:** [DIFF.md](DIFF.md) (left = live Tax v12, right = proposed); [manifest.json](manifest.json)
- **Workbook:** `2026 Upstream PPP.xlsm` › NUIMS, RENAISSANCE block rows 2195–2436 (X = 2026, U = 2025 YEO,
  S/T = 2025 Jan–Aug / Sep–Dec, P/Q/R = 2022–2024)

## A. Production Allowance = 0 — oil price read on Date 000000 (ready)

`PPP_Upstream_Tax` › 9 "Tax - Production Allowance" › line 22 reads `GA_015` (oil price) with
`[d/Date]="000000"`. The oil price is a per-year assumption: Revenue › 2 › line 35 and Royalties › 4 / 7 / 10
read `GA_015` without a date and get values. On `000000` there is none, so `TAX035_12` is empty,
`TAX035_17` = 0, the MIN picks 0 and `TAX035_05` = 0.

Fix: drop `[d/Date]="000000"` on that lookup only. `TA20_05` / `TA20_10` (fixed $2.50, 20 %) stay on `000000`.

Expected 2026: price 60.26 → 20 % = 12.05; MIN(2.50, 12.05) = 2.50 × 89.42 MMbbl = **223.56** (NUIMS row 2333).

## B. Gas CAPEX component reads oil capex (ready)

`PPP_Upstream_Tax` › 10 "Tax - CAPEX Components" › line 40: `TAX040_10_05_15` (gas) adds
`AMT_200` (oil) at `UAP_124`; every other gas line reads `AMT_210`. Changed to `AMT_210`. No effect on
Renaissance today (nothing on `UAP_124`), but it would double-count oil capex into gas for any JV that has it.

## C. PPT base misses NDDC and HCDT (needs two WPLn members)

NUIMS X2370 (Assessable profit for PPT) = revenue − royalties − OPEX oil − Education tax/Dev Levy oil (2308)
− **NDDC oil (2316)** − **HCDT oil (2312)**.

`PPP_Upstream_Tax` › 12 "Tax - Capital allowance for PPT" › lines 51–66 (and the same sum in
› 15 "Tax - Chargeable Profit for PPT" › lines 21–28) deduct royalties, `CST05_05` and `TAX005_05` only.
`TAX050_20` has children `_05 … _35`; there is no member for NDDC or HCDT.

Proposed: add `TAX050_20_40` "Less: NDDC Levy – Oil" (= −`TAX025_05`) and `TAX050_20_45`
"Less: HCDT Fund – Oil" (= −`TAX015_05`) under `TAX050_20`, and include both in steps 12 and 15.
Hydrocarbon Tax allowable costs (› 16 › `TAX070_40`) also omit NDDC and HCDT where NUIMS X2394 includes them; HT
is 0 under PPT, so that can follow with the same members.

Expected 2026: PPT base falls by 73.38 (NDDC) + 53.07 (HCDT). The sheet only deducts 73.38 because its HCDT is 0
(column-W bug, closed by Noel), so SAC will sit 53.07 × 85 % below the sheet's PPT. **Decision:** OK to add the members
(model change)?

## D. Capex amortisation — SAC sees only Sep–Dec 2025 and no 2022–2024

SAC's 2026 values reconcile exactly:

| Line | SAC | = 20 % × 2026 | + 20 % × 2025 | Sheet |
|---|---|---|---|---|
| Oil fac + drilling (`TAX045_05_10`) | 169.60 | 833.93 | 14.06 (T, Sep–Dec only) | 334.21 |
| Other oil (`TAX045_05_15`) | 21.41 | 31.12 | 75.94 (T) | 7.94 |
| Gas (`TAX045_05_20`) | 313.81 | 1,015.16 | 553.89 (T) | 203.03 |

Causes:
1. **Closed periods skipped.** `PPP_Upstream_Tax` › 10 runs on `Lock = "#"`, so 2025 `TAX040` holds Sep–Dec only;
   Jan–Aug sits on `202508`, `Lock = Hist_Open` (oil 28.22 + 108.17, gas 364.88). Same problem as the Royalties
   cost rollup fixed at 13:33. Fix: build `TAX040` from both locks into December (the `LAST()` rollup pattern).
2. **No 2022–2024 capex** behind the 3rd–5th-year rates. The sheet has them (cols P–R). **Question:** are prior
   years loaded in SAC, or should a closing tax written-down value per JV be an input (e.g. on Date `000000`)?
3. **Exploration.** SAC expenses exploration (`TAX040_05_05`, `UAP_110/120/121/124`) in CITA / HT
   (› 17 › line 26, › 16 `TAX070_40`) and amortises only development + facilities. The sheet amortises all oil
   capex rows 2279–2287 incl. seismic and exploration wells (its "Expensed Exploration" row 2337 is blank).
   **Decision:** keep SAC's split, or amortise exploration?
4. The sheet itself is wrong here (`findings/NU03_JV005-renaissance.md` §8): X2350 uses W, V, S, R
   (blank 2026-source columns) instead of U, R, Q, P, and rows 2351–2352 use shifted rates. By principle
   (20/20/20/20/19 % on 2026, 2025, 2024, 2023, 2022):

   | | incl. exploration (sheet basis) | excl. exploration (SAC basis) |
   |---|---|---|
   | Oil | 470.59 | 412.15 |
   | Other | 41.90 | 41.90 |
   | Gas | 492.21 | 492.21 |

   With full-year 2025 but no 2022–2024: oil 196.88, other 23.22, gas 386.79.

## E. CITA Gas allowable misses the gas capital allowance (needs data)

NUIMS X2407 = `IF(O2413="PPT",0,X2391)` + gas royalties + OPEX gas + Dev Levy gas + HCDT gas + NDDC gas.
`O2413` is blank (the regime is in `G2413`), so the sheet always deducts amortised gas (203.03) → 563.87.
SAC 360.83 = 563.87 − 203.03, i.e. `#PARAM1` in `PPP_Upstream_Tax` › 18 "Allowable Costs & Chargeable Profit CITA
(Gas)" › lines 21–25 contributes 0. It takes `TAX060_25` (deductible amortised gas, › 14) when `TAX070_60` = 0.

Need from the data foundation (RENAISSANCE, 2026): `TAX060_05/10/15/20/25/30`, `TAX070_60`, `TAX055_05`,
`TAX010_15_05 … _30` to see whether `TAX060_25` is 0 or the flag is set.

Principle question: under PPT, gas is taxed under CITA, so the gas capital allowance belongs in CITA Gas. The sheet's
intended formula (`IF regime = "PPT" → 0`) would drop it under PPT; its actual result keeps it. SAC's condition
(`TAX070_60 = 0` → include) includes it under PPT. **Decision:** include the gas capital allowance in CITA Gas under both
regimes?

## Rollback

Apply the left side of [DIFF.md](DIFF.md).
