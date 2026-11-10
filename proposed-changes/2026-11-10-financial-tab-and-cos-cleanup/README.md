# Change — #19: Capex/Opex shown on "#" for the Financial tab; remove dead COS/Depletion block

- **Trello:** #19 https://trello.com/c/VYeHuGjg
- **Decisions (Noel, 10 Nov 09:30):**
  1. COS Depreciation / Depletion GL entries are owned by `PPP_Upstream_Tax` step 21. Delete the commented-out
     copy in `PPP_Upstream_CostAlloc` step 13.
  2. The Financial tab shows `PPP_Currency = "#"` by design. It uses the UOM measure `Value_WPLn` to show mixed
     units (%, $, kbopd …) in one table, so it can't filter on a currency. Real currency (USD) only appears once
     the GL entries are posted and shown on the GL Entries tab.
- **Status:** APPROVED — applying
- **Scripts:** one file per step; [DIFF.md](DIFF.md) (left = live, right = proposed); [manifest.json](manifest.json)

## Why

The Financial tab rows CAPEX Oil / Gas and OPEX Oil / Gas are `AMT_200/210/220/230` on `#`. Inputs for those
lines are captured on USD, and no data action wrote them to `#`. The tab therefore showed only stale `#`
records from the August load (CAPEX Oil 50.18 instead of 957.46), plus the gas flare penalty.

## The change

**`PPP_Upstream_Royalties` step 1 "Initialise"** (runs first in Royalties, before anything reads these lines):
- Scope now includes `AMT_200/210/220/230` and is limited to `PPP_Currency = "#"`. `DELETE()` therefore clears the
  calculated `#` copy of those lines as well as the `CST05` cost base. The USD inputs are outside the scope and
  can't be deleted.
- Then each USD input leaf is copied to `#` with the same `PPP_EntryNr`, so the Financial tab can drill by entry.
- The gas flare penalty (`AMT_230 × UAP_GFP`, on `#`) is cleared too, and step 13 recalculates it in the same run.
- Side effect: `CST05` is now only cleared on `#`. Since #19, Royalties only writes `CST05` on `#`. Any `CST05`
  left on USD by a run before 10 Nov is never read (all readers are scoped to `#`). It's added to housekeeping.
- Stale `#` records of `AMT_200/210/220/230` are removed for the entity on every run, because they are this step's
  target. They are no longer listed under housekeeping H1.

**`PPP_Upstream_CostAlloc` step 13 "GL Entries"**: delete the 8 commented lines for COS Depreciation (4202026)
and Depletion (5230003). Comments only, so behaviour doesn't change. The commented "Internal capex" block is kept.

## Known limit (unchanged by this change)

Every Upstream script is scoped to `Lock = "#"`. Inputs for periods up to 202508 are loaded with
`Lock = Hist_Open`, so the engine (including this copy) doesn't calculate those periods. To be raised separately.

## Test

1. Run Upstream (Calculations) for RENAISSANCE JV, Budget 2026 (Reference), CAPEX_Version the same.
2. Financial tab 2026: CAPEX Oil 957.46, CAPEX Gas 1,015.16, OPEX Oil 1,488.52, OPEX Gas 211.0 + gas flare penalty.
3. Drill by entry number: values sit on the uploaded `UAP_*` entries, and nothing remains on `UAP_5800_14/15/16`
   unless it was uploaded there.
4. Re-run unchanged → identical.

## Rollback

Apply the left side of [DIFF.md](DIFF.md). The `#` copies stay until cleared.
