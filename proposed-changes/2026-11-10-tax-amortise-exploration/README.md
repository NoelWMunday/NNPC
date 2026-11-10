# Change — #20 D (part): exploration capex is amortised, not expensed

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Decision (Noel, 10 Nov 16:01):** "Our business rules come from what excel does." Users capture annual exploration
  spend (`AMT_200` at UAP_110/120/121/124); the sheet amortises it.
- **Status:** APPLIED 10 Nov 2026 16:04 SAST (`72aea87`, Tax v19)
- **Scripts:** [DIFF.md](DIFF.md), [manifest.json](manifest.json)

## What the sheet does

NUIMS row 2338 "Oil Capex" = rows 2279–2287 (seismic acquisition, processing, reprocessing, exploration wells,
appraisal wells, development wells, completion, workover, facilities), amortised in row 2350 at rows 2343–2347:
20/20/20/20/19 % over 5 years. Row 2337 "Expensed Exploration & Appraisal well cost" is blank (nothing expensed).

## Change

| Where | Change |
|---|---|
| `PPP_Upstream_Tax` › 11 "Tax - CAPEX Amortisation" › lines 28–41 | Oil amortisation base adds `TAX040_05_05_05/10/15` (exploration) to `TAX040_05_10/15`, for every year term |
| › 11 › lines 64–77 | Gas base adds `TAX040_10_05_05/10/15` the same way (gas exploration was not used anywhere before; nil for Renaissance; the sheet has no gas exploration rows) |
| › 16 "Tax - Hydrocarbon Tax" › line 30 | stop expensing `TAX040_05_05` in HT allowable costs (it now arrives via `TAX055_30`) |
| › 17 "Tax - Allowable Costs & Chargeable Profit CITA (Oil)" › line 26 | stop expensing `TAX040_05_05` in CITA Oil allowable costs (via `TAX055_30`) |

## Expected RENAISSANCE 2026 ($M)

`TAX045_05_10` Oil = 20 % × (926.34 + 315.07 + 620.90 + 490.62) + 19 % × 0 = **470.59** (was 412.15 expected after v18).
Other 41.90 and Gas 492.21 unchanged. Exploration no longer expensed in 2026 (92.41 = 2.25 + 47.93 + 42.23).

Rollback: apply the left side of [DIFF.md](DIFF.md).
