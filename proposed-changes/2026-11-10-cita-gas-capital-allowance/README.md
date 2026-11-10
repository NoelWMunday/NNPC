# Change proposal — #20 E: CITA Gas allowable includes the gas capital allowance

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Status:** APPROVED (Noel, 10 Nov 15:42: "change the = 0 to include a check for null") — applying
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

## Change

Keep the regime test, but treat a missing flag as 0: `IF … = 0 OR … = NULL THEN` (SAC validation: no errors).
Under PPT (flag 0 or empty) the gas capital allowance `TAX060_25` is deducted in CITA Gas; with `SET10_10` = 1 (PIA) it is not.
(Alternative considered: always deduct — gas is under CITA in both regimes. Not taken; Noel kept the regime test.)

Expected RENAISSANCE 2026: `TAX080_05` = 360.83 + 313.81 = 674.64, `TAX080_10` = 1,534.82 − 674.64 = 860.18,
CITA Gas = 30 % = 258.05. The sheet (563.87 / 970.96 / 291.29) uses its own understated gas amortisation (203.03, see D).

Related: `SET10_10` empty means the PIA flag reads as "not PIA" everywhere it is multiplied in (HT › 16, CITA Oil › 20).
That is right for RENAISSANCE (PPT) but only by accident — worth populating `SET10_10` = 0/1 per JV (Settings table).

Rollback: apply the left side of [DIFF.md](DIFF.md).
