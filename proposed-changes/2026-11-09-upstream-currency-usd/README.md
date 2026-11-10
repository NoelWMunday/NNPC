# Change proposal — Upstream data actions read inputs from PPP_Currency = USD

- **Trello:** #19 https://trello.com/c/VYeHuGjg — *DEFECT: Upstream data actions read PPP_Currency = # — must read USD*
- **Decision (Noel, 9 Nov):** inputs stay on `PPP_Currency = USD`; the data actions change.
- **Status:** APPLIED 10 Nov 2026 08:20 SAST (commit `c9d5952`) — see `DEPLOYMENTS.md`. Awaiting test.
- **Scripts:** one file per changed step in the sub-folders; full before/after in [DIFF.md](DIFF.md)
- **Generator:** `tools/propose_currency_usd.py` (re-run against a fresh export if SAC changes first)

## Root cause

The work-program upload writes inputs (`AMT_*`, `UOM_*`, `SET*`) with `PPP_Currency = USD`. The Upstream
scripts scope or default every read to `PPP_Currency = "#"`, so they pick up only the stale `#` leaves from
the August load (Capex Oil 50.18 instead of 957.46, Opex Oil 4,465.56 instead of 1,488.52).

`PPP_Upstream_CostAlloc` already follows the target convention — it reads NU03 costs with
`[d/PPP_Currency]="USD"` and writes `[d/PPP_Currency]="#"`. This change applies the same convention to
the other three.

## Rules applied

| # | Rule | Where |
|---|---|---|
| R1 | Calculated lines stay on `PPP_Currency = "#"` (story, GL steps and CostAlloc expect them there) | all |
| R2 | Every `RESULTLOOKUP` of an upload input gets `[d/PPP_Currency]="USD"` | Revenue 2; Royalties 3–21; Tax 2–21 |
| R3 | Royalties steps 2–21 had no currency scope; they get `MEMBERSET [d/PPP_Currency] = "#"` | Royalties |
| R4 | Royalties cost loops iterate USD input leaves and append to `#` | Royalties 14–17 |
| R5 | Tax GL entries read COS Depreciation / Depletion inputs (`UAP_5800_15/16`) from USD | Tax 21 |

Not changed: central assumptions (`GA_*`, `RR*`, `TL*`, `TA*`, read with `PPP_Entity="#"`, `Lock="Central"`),
the gas flare penalty (`AMT_230 × UAP_GFP`, calculated by Royalties 13 on `#`), all GL-entry write scopes,
`PPP_Upstream_CostAlloc`, `PPP_Upstream_All_Calculations`.

Inputs treated as USD: `AMT_46, AMT_80, AMT_85, AMT_90, AMT_97, AMT_200, AMT_210, AMT_220, AMT_230,
UOM_*, SET*`.

### R4 — cost loop (Royalties 14, same shape in 15–17)

```
MEMBERSET [d/PPP_Currency] = ("#","USD")
...
IF [d/PPP_EntryNr] != "#" AND [d/PPP_Currency] = "USD" THEN
	DATA.APPEND([d/WPLn] = "CST05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_200")
ENDIF
```

## Decisions (Noel, 10 Nov)

1. Inputs entered in the story input table and via upload are on `PPP_Currency = USD` (story columns
   CY_YTD, CY+1 … CY+5 are restricted to USD). Treated as USD: `AMT_46/80/85/90/97/200/210/220/230`,
   `UOM_*`, `SET*`.
2. Central assumptions are on `PPP_Currency = "#"` — unchanged.
3. HCDT Gas now excludes the gas flare penalty (fines and levies are excluded by the agreed principle).
4. Stale `#` inputs stay for now (messy data is deliberate) — tracked as H1 in `housekeeping.md`.
5. Claude applies the change in SAC after the merge to `main` (see README workflow).

## Data clean-up (Trello #19 item 2) — separate, after the scripts

After this change the scripts no longer read `#` inputs, so the stale leaves stop affecting results. They
still show up in any story that does not filter on currency. Proposed one-off data action
(**not created**), run per entity on `Budget 2026 (Reference)`:

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
MEMBERSET [d/PPP_Entity]   = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/Measures]     = "Value_WPLn"
MEMBERSET [d/PPP_Currency] = "#"
MEMBERSET [d/WPLn] = ("AMT_46","AMT_80","AMT_85","AMT_90","AMT_97","AMT_200","AMT_210","AMT_220","AMT_230",
                      BASEMEMBER([d/WPLn],"Units"), BASEMEMBER([d/WPLn],"Settings"))   // confirm node IDs
DELETE()
```

No `PPP_EntryNr` restriction, so every entry number is cleared for those lines on `#`. That includes the
calculated gas flare penalty (`AMT_230 × UAP_GFP`), which is harmless because Royalties step 13 recalculates
it on the next run. Run it **after** the script change, then re-run Upstream (Calculations).

## How to apply (manual, in SAC)

1. Pre-check: the three data actions in SAC must match `sac-export/` on `main`.
2. For each file in the sub-folders, open the step named in the file and replace its script with the file
   content. Steps not listed are unchanged.
3. Validate each data action (warnings about decimal places between measures are accepted).
4. Save. Re-export, run `tools/generate_docs.py`; the resulting `git diff` on `sac-export/` should match
   [DIFF.md](DIFF.md) exactly — that is the check the change went in as reviewed.

## Test

1. Run **Upstream (Calculations)** for NU03_JV005 RENAISSANCE JV, `Budget 2026 (Reference)`, with
   `CAPEX_Version` set to the same version.
2. Financial tab, 2026: CAPEX Oil **957.46**, CAPEX Gas **1,015.16**, OPEX Oil **1,488.52**,
   OPEX Gas **211.0** (cost base lines CST05_15/20/05/10).
3. Re-run unchanged → identical results (SIT step 20).
4. Revenue and royalties should still reconcile as before; tax will move with the corrected inputs.
5. GL Entries tab: COS Depreciation (4202026) and Depletion (5230003) only show values posted to
   `UAP_5800_15/16`, not Opex.

## Rollback

Apply the "SAC now" side of [DIFF.md](DIFF.md) (= `sac-export/` before the merge).

## Apply notes (10 Nov)

- Applied by Claude through the data action designer: each step's script was replaced only after its
  current content matched `beforeSha256` in [manifest.json](manifest.json), and checked against
  `afterSha256` before saving. After saving, all three data actions were re-read from SAC and their step
  lists match `sac-export/` on `main` exactly.
- **Tracepoints:** replacing a script whose line count changes drops the step's tracepoints. Royalties step
  18 (Total CAPEX / OPEX Equity) had four; they were re-added on the shifted lines. On save SAC kept the
  two on `DATA` statements (lines 28 and 32) and dropped the two that were not on a statement (old lines
  13 and 33). GL Entries tracepoints (21, 25) were untouched.
