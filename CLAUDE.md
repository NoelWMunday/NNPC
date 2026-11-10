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
- **Story display:** tabs built on the UOM measure (e.g. Financial) show mixed units, so they read `#`. Any
  input shown there must be copied to `#` by a data action (Royalties step 1 copies `AMT_200/210/220/230`).
  Real USD appears once GL entries are posted (GL Entries tab).
- COS Depreciation / Depletion GL entries are owned by `PPP_Upstream_Tax` step 21.
- Before changing a lookup's currency, confirm which story table captures that line and what it writes.
- **Central assumptions** (`GA_*`, `RR*`, `TL*`, `TA*`) are on `PPP_Entity="#"`, `Lock="Central"`,
  `PPP_Currency="#"`.
- **Messy data is deliberate.** Stale or irrelevant records are left in the model so scripts are proven
  to scope tightly. Never rely on data being clean; scope every read. Clean-up is a separate housekeeping
  task (`housekeeping.md`).
- Data action parameter *Target Version* is empty by design (set at runtime). Validation warnings about
  decimal places between measures are accepted.
- **Business rules come from what the Excel does** (Noel, 10 Nov) — e.g. exploration capex is amortised because the
  sheet amortises it. Cell-reference bugs in the sheet are not rules (see `findings/`).
- Not every `SET*` applies to every JV; null is a valid value. Scripts must treat a missing setting as 0/off.
- Test data source: `2026 Upstream PPP.xlsm` (replaces `New NUIMS.xlsx`). Do not assume the workbook is
  right — trace formulas to inputs; NU03 overhead allocations and JV direct capex are mixed in places.

## Referencing (Noel, 10 Nov)

Always point to code as **data action › step number + step name › line number**, with a link to the repo file, e.g.
`PPP_Upstream_Tax` › 20 "Tax - CITA (Oil & Gas)" › line 25
([data-actions/PPP_Upstream_Tax.md](data-actions/PPP_Upstream_Tax.md)). Line numbers are those shown in the SAC script editor.

## Settings and rates

All settings (`SET*`) and central rates are on Date `000000`. Hard-coded period dates (e.g. `202612`) are development
leftovers and are defects. `PPP_Upstream` (old chain, unused) still has 64 of them.

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
- Reading model data: from a story tab, capture one of the story's INA requests (`/sap/bc/ina/service/v2/GetResponse`),
  clone it, replace the WPLn / Entity / Lock / Currency / Date filters, set `ReadMode = "Booked"` on WPLn and Date, and
  POST it with the same headers. Read-only.
- SAC Validate only refreshes on a real click (not a JS `.click()`); check the panel by screenshot.
- Saving a data action from a designer opened before someone else's save overwrites their changes (v14 reverted
  v11/v12 on 10 Nov). Reload the designer and check the live version before every apply.
- `RESULTLOOKUP(x) = 0` is false when x has no value. Test `= 0 OR = NULL` where a flag may be unset.
- Git tags can't be pushed from here; deployments are logged in `DEPLOYMENTS.md`.
- Local working folder on Noel's Mac: `Unit testing/Claude`; source workbooks in `Unit testing/Source data`.
