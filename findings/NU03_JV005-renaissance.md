# NU03_JV005 RENAISSANCE JV — Capex / Opex baseline differences

- **Trello:** https://trello.com/c/GMpteYaU
- **Source (test data):** `2026 Upstream PPP.xlsm` › `NUIMS`, block 1.3.1, rows 54–95
- **SAC snapshot:** `sac-export/` 2026-11-09
- **Status:** analysis in progress — no SAC changes proposed yet

## 1. Source workbook replaced

`NUIMS - Testing Brief.md` (§3, §7) names `New NUIMS.xlsx` › `Enhanced PPP (2)` as the source and the
8,627-row work-program file (loaded 14 Aug) was built from it. On 9 Nov `2026 Upstream PPP.xlsm` became
the test data. **The data currently in SAC was built from the old source and the old mapping**, so the
baseline check on the card compares SAC against a different workbook. Most "posted to the wrong line"
findings should be re-tested after the v1 file (built from the new workbook) is loaded — before any
data action is changed.

The brief needs updating to name the new source.

## 2. Source totals tie

Recomputed from the workbook (US$ M, 2026, col 24):

| Line | Rows | 2026 |
|---|---|---|
| CAPEX Oil (Seismic Acq 2.25, Reprocessing 47.93, Expl Wells 42.23, Devt Well_Oil 287.18, Facilities Oil 546.75, Other Capex 31.12) | 70–79 | **957.46** |
| CAPEX Gas (Devt Well_Gas 242.31, Facilities Gas 772.85) | 80, 83 | **1,015.16** |
| OPEX Oil | 84 | **1,488.52** |
| OPEX Gas | 85 | **211.00** |

Matches the v1 upload-file comment on the card. Row 88 "NNPC Crude Oil Equity" is 0 in every year —
see §6.

## 3. What the data actions expect the upload to post

Capex and Opex inputs are never posted by a data action; they come only from the upload. The scripts
then read them by **exact `PPP_EntryNr` code**:

| Consumer | Reads |
|---|---|
| `PPP_Upstream_Tax` capital allowance (TAX040_*) and `PPP_Upstream_Royalties` | `AMT_200` × `UAP_110` (seismic acq), `UAP_120` (reprocessing), `UAP_121` + `UAP_124` (expl/appraisal wells), `UAP_130` (devt wells; also ÷5), `UAP_132 + 136 + 138 + 139` (facilities) |
| Royalties cost base CST05_15 (CAPEX Oil) | `AMT_200` × base members of `UAP_CAPEX_CST` |
| Royalties cost base CST05_20 (CAPEX Gas) | `AMT_210` × base members of `UAP_CAPEX_CST` **and** `UAP_CAPEX_OTH` |
| Royalties CST05_05 / CST05_10 (OPEX) | `AMT_220` / `AMT_230` × base members of `UAP_OPEX_CST` |
| Tax HCDT base TAX015_15 / TAX020_15 | `AMT_220` / `AMT_230` at `PPP_EntryNr = #` |
| Tax GL entries — COS Depreciation (4202026) / Depletion (5230003) | `AMT_220 + AMT_230` × `UAP_5800_15` / `UAP_5800_16` |
| Gas flare penalty | `AMT_230` × `UAP_GFP` |

So: Seismic Acquisition landing on `UAP_139` (as seen on the card) means it is treated as a facility,
not seismic, in capital allowance — the calculation is right, the input is on the wrong code.

## 4. Opex appearing three times (Host Community, COS Depreciation, Depletion)

Each of those three lines reads `AMT_220` through a different key (`#`, `UAP_5800_15`, `UAP_5800_16`).
1,488.52 appearing on all three means the loaded Opex sits on a member that all three resolve to —
most likely posted to a parent or `#` rather than to one `UAP_OPEX_*` base member. Also note the HCDT
"base" line (TAX015_15) is *meant* to show total Opex Oil; it is a basis, not a cost, so it should not
be added to the other two when totalling. **Needs the `PPP_EntryNr` hierarchy to confirm** (§7).

## 5. Possible script inconsistency (to confirm, not yet a defect)

`PPP_Upstream_Royalties` step 14 (CAPEX Oil) reads only `UAP_CAPEX_CST`; step 15 (CAPEX Gas) reads
`UAP_CAPEX_CST` **plus** `UAP_CAPEX_OTH`. If "Other Capex (not attributable to production)" (`UAP_141`)
sits under `UAP_CAPEX_OTH`, Oil excludes non-production capex and Gas includes it. Renaissance has
Other Capex on Oil only ($31.12M 2026), so it doesn't move Renaissance today, but it would for a JV
with gas-side Other Capex. Question for the build team: which is intended?

## 6. Equity participation (55.1% in SAC vs 58.7% weighted average)

The block's own equity row (88) is 0, so the 55.1% in SAC did not come from this block. To trace:
where `PART_*` / `AMT_90` is populated for NU03_JV005 (the v1 file deliberately excludes `AMT_90`).

## 7. Still needed

- `PPP_EntryNr` and `WPLn` member hierarchy (`Test data - Master data.xlsx`) — confirms §4 and §5.
- The v1 upload file — check every Renaissance row's `WPLn` × `PPP_EntryNr` against §3.
- 2025 split (Aug blank, ROY = YEO): source cols 19/20 are populated (e.g. Seismic Reprocessing
  18.464 / −11.261), so a blank August is an upload-file issue, not a source gap. Verify in v1 file.
