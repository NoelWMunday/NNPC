# Change — #19 correction: metrics stay on PPP_Currency = "#"

- **Trello:** #19 https://trello.com/c/VYeHuGjg (QA correction comment, 10 Nov 09:04)
- **Corrects:** [2026-11-09-upstream-currency-usd](../2026-11-09-upstream-currency-usd/README.md), live since
  10 Nov 08:20 (commit `c9d5952`)
- **Approach:** fix forward (Noel, 10 Nov 09:10: "ready for implementation")
- **Status:** APPROVED — applying
- **Scripts:** one file per changed step; [DIFF.md](DIFF.md) (left = live, right = proposed); [manifest.json](manifest.json)
- **Generator:** `python3 tools/propose_currency_usd.py . 9a56a3f proposed-changes/2026-11-10-upstream-metrics-on-hash`

## What was wrong

The first change treated every input as USD. Only the Capex/Opex inputs are:

| Lines | Captured in | Currency |
|---|---|---|
| `AMT_200/210/220/230` (CAPEX/OPEX Oil/Gas, by `UAP_*` entry) | WP upload, Capex/Opex input tables | `USD` |
| `AMT_46/80/85/90/97`, `UOM_*` | Metrics table (Table_1) | `#` |
| `SET*` | Settings table (Table_4) | `#` |
| `GA_*`, `RR*`, `TL*`, `TA*` | Admin (central) | `#` |

So since 08:20 the metric lookups have read USD, where there are either no values or only stale upload
values. Revenue, royalties and tax results from runs after 08:20 are unreliable until this is applied and
Upstream (Calculations) is re-run.

## The change

17 steps, 104 lines. In every changed line the only edit is removing `, [d/PPP_Currency]="USD"` from a
lookup of a metric (`AMT_46/80/85/90/97`, `UOM_*`, `SET*`). Verified by script: each proposed step equals
the live step with exactly those qualifiers removed.

Kept from the first change:
- `[d/PPP_Currency]="USD"` on lookups of `AMT_200/210/220/230` (Tax 2, 3, 4, 5, 10, 21; Royalties 21).
- Royalties 2–21 scoped to `PPP_Currency = "#"`; cost loops 14–17 read the USD leaves and append to `#`.
- Tax 21 GL entries: COS Depreciation (4202026) and Depletion (5230003) read `AMT_220/230` at
  `UAP_5800_15/16` on USD.

| Data action | Steps |
|---|---|
| `PPP_Upstream_Revenue` | 2 |
| `PPP_Upstream_Royalties` | 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 18, 21 |
| `PPP_Upstream_Tax` | 2, 16, 19, 20 |

## Retest note — Financial tab

The retest compared the Financial tab rows "CAPEX Oil / Gas, OPEX Oil / Gas". Those rows are
`AMT_200/210/220/230` (node `AMT_GL`) in a table filtered to `PPP_Currency = "#"`. No data action writes
those lines on `#` (searched all 65), so that table shows only the stale `#` records from the August load
plus the gas flare penalty (`AMT_230 × UAP_GFP`, calculated on `#`). It will not change with any data
action fix.

The data actions build the cost base on `CST05_15` / `CST05_20` / `CST05_05` / `CST05_10`
(Total CAPEX Oil / Gas, Total OPEX Oil / Gas) and the equity share on `CST10_*`. Those are the lines to
check. Options for the story (stories session):
1. Show `CST05_*` / `CST10_*` on the Financial tab, or
2. Show `AMT_GL` on `USD` (inputs) next to the `#` calculated lines.
Removing the stale `#` records (housekeeping H1) also empties the misleading rows.

## Open question (Noel)

COS Depreciation / Depletion GL block: active in `PPP_Upstream_Tax` step 21 (`PPP_EntryNr = UP_0005`),
commented out in `PPP_Upstream_CostAlloc` step 13 (`UP_0010`). Which should own these entries? Not changed here.

## Test

1. Re-run Upstream (Calculations) for RENAISSANCE JV, Budget 2026 (Reference), CAPEX_Version the same.
2. Revenue (REV_05/10/15/20/25/30) and royalties back to the pre-08:20 values (metrics unchanged).
3. 2026 `CST05_15` 957.46, `CST05_20` 1,015.16, `CST05_05` 1,488.52, `CST05_10` 211.0.
4. Re-run unchanged → identical.

## Rollback

Apply the left side of [DIFF.md](DIFF.md) (returns to `c9d5952`), or both changes' left sides to return
to the 9 Nov scripts.
