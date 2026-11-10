# Change proposal — #20 E: CITA Gas allowable includes the gas capital allowance

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Status:** PROPOSED — needs Noel's decision (gas capital allowance in CITA Gas under both regimes?)
- **Where:** `PPP_Upstream_Tax` › 18 "Tax - Allowable Costs & Chargeable Profit CITA (Gas)" › lines 21–25 — [DIFF.md](DIFF.md)

## Root cause (from the data, Budget 2026 (Reference), NU03_JV005, read 10 Nov 15:40)

| Line | 2026 |
|---|---|
| `TAX060_25` Deductible amortised gas capex (› 14) | 313.81 |
| `TAX070_60` PIA flag (› 16 › line 24 = `SET10_10` at `000000`) | **no value** |
| `SET10_10` for NU03_JV005 | **no value** (only `SET10_05` = 1 on `000000` and `202612`) |
| `TAX080_05` Allowable cost CITA Gas | 360.83 (= sheet 563.87 − 203.03) |

› 18 › line 21 `IF RESULTLOOKUP([d/WPLn]="TAX070_60") = 0` is false for a null, so `#PARAM1` stays 0 and the gas capital
allowance is dropped.

## Proposal

Always deduct `TAX060_25` in CITA Gas. Gas profits are taxed under CITA in both regimes (PPT covers oil only), so the
gas capital allowance belongs there either way. The sheet's actual result (row 2407) deducts it too: its
`IF(O2413="PPT",0,…)` tests a blank cell.

Expected RENAISSANCE 2026: `TAX080_05` = 360.83 + 313.81 = 674.64, `TAX080_10` = 1,534.82 − 674.64 = 860.18,
CITA Gas = 30 % = 258.05. The sheet (563.87 / 970.96 / 291.29) uses its own understated gas amortisation (203.03, see D).

Related: `SET10_10` empty means the PIA flag reads as "not PIA" everywhere it is multiplied in (HT › 16, CITA Oil › 20).
That is right for RENAISSANCE (PPT) but only by accident — worth populating `SET10_10` = 0/1 per JV (Settings table).

Rollback: apply the left side of [DIFF.md](DIFF.md).
