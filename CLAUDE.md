# Working notes for Claude

Read `README.md` first — the change workflow there is binding (branch → merge to `main` → apply in SAC
→ re-export and verify; rollback from `main` history). Defects come from the Trello board
https://trello.com/b/a85I1Cfx/nnpc (raised by a separate QA project); post findings and status there.

## SAC conventions (from Noel, 10 Nov 2026)

- Model `PPP_BUSPREMISE` (description "Business premise") holds the Upstream work programme. Measure
  `Value_WPLn` ("Metric") is a **unit** measure: `WPLn` rows carry their own UOM, and a "$" UOM row
  simulates currency.
- **Inputs** (upload and story input columns CY_YTD, CY+1 … CY+5) are on `PPP_Currency = USD`
  (2026 also has an NGN input column, CY+1 (N)).
- **Calculated lines** are on `PPP_Currency = "#"`. Scripts read inputs with `[d/PPP_Currency]="USD"` and
  write to `"#"` (the `PPP_Upstream_CostAlloc` pattern).
- **Central assumptions** (`GA_*`, `RR*`, `TL*`, `TA*`) are on `PPP_Entity="#"`, `Lock="Central"`,
  `PPP_Currency="#"`.
- **Messy data is deliberate.** Stale or irrelevant records are left in the model so scripts are proven
  to scope tightly. Never rely on data being clean; scope every read. Clean-up is a separate housekeeping
  task (`housekeeping.md`).
- Data action parameter *Target Version* is empty by design (set at runtime). Validation warnings about
  decimal places between measures are accepted.
- Test data source: `2026 Upstream PPP.xlsm` (replaces `New NUIMS.xlsx`). Do not assume the workbook is
  right — trace formulas to inputs; NU03 overhead allocations and JV direct capex are mixed in places.

## Mechanics

- Export: read-only `objectmgr` `readObject` calls from the logged-in SAC tab (Claude in Chrome);
  members via `fpa/member` `query`. Then `python3 tools/generate_docs.py <export.json> .`
- Local working folder on Noel's Mac: `Unit testing/Claude`; source workbooks in `Unit testing/Source data`.
