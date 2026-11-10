# Working notes for Claude

Read `README.md` first — the change workflow there is binding (branch → merge to `main` → apply in SAC
→ re-export and verify; rollback from `main` history). Defects come from the Trello board
https://trello.com/b/a85I1Cfx/nnpc (raised by a separate QA project); post findings and status there.

## SAC conventions (from Noel, 10 Nov 2026)

- Model `PPP_BUSPREMISE` (description "Business premise") holds the Upstream work programme. Measure
  `Value_WPLn` ("Metric") is a **unit** measure: `WPLn` rows carry their own UOM, and a "$" UOM row
  simulates currency.
- **Capex/Opex inputs** `AMT_200/210/220/230` (by `UAP_*` entry; upload and the Capex/Opex input
  tables) are on `PPP_Currency = USD` (2026 also has an NGN input column, CY+1 (N)).
- **Metrics** `AMT_46/80/85/90/97`, `UOM_*` (Metrics table) and **settings** `SET*` (Settings table)
  are on `PPP_Currency = "#"`. (Corrected 10 Nov — #19 first assumed all inputs were USD.)
- **Calculated lines** are on `PPP_Currency = "#"`. Scripts read Capex/Opex inputs with
  `[d/PPP_Currency]="USD"` and write to `"#"` (the `PPP_Upstream_CostAlloc` pattern).
- Before changing a lookup's currency, confirm which story table captures that line and what it writes.
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
- Apply: open the data action in the designer, select steps by dispatching pointer events on the flow
  tile (`span[class*="planningSequenceSt"]`), set the CodeMirror 5 editor (`.CodeMirror`.CodeMirror),
  check before/after hashes from the change's `manifest.json`, save via the save menu. Changing the URL
  `?step=` reloads the designer and loses unsaved edits. Scripts can be fetched in the page from
  `raw.githubusercontent.com` pinned to a commit.
- Tracepoints are designer state, not part of the saved definition. Replacing a script with a different
  line count drops them — re-add on the equivalent lines.
- Snapshot keeps scripts, not SAC's compiled `runtimeContext`. Partial refresh: update files in
  `sac-export/`, then `python3 tools/generate_docs.py sac-export .`
- Git tags can't be pushed from here; deployments are logged in `DEPLOYMENTS.md`.
- Local working folder on Noel's Mac: `Unit testing/Claude`; source workbooks in `Unit testing/Source data`.
