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

## 4. Opex appearing three times (Host Community, COS Depreciation, Depletion) — confirmed data issue

From the `PPP_EntryNr` hierarchy (SAC, 9 Nov):

| Code | Description | Parent |
|---|---|---|
| `UAP_5800_14` | Host Community | `UAP_OPEX_CST` |
| `UAP_5800_15` | COS Depreciation | `UAP_OPEX_CST` |
| `UAP_5800_16` | Depletion | `UAP_OPEX_CST` |

All three are **base members of `UAP_OPEX_CST`**, so 1,488.52 on each means the loaded file posted the
OPEX Oil row to all three entry numbers. Consequences, all from the data not the scripts:

- Royalties cost base CST05_05 sums every `UAP_OPEX_CST` base member → Opex Oil 3× (4,465.56).
- Tax GL entries post `UAP_5800_15` as COS Depreciation (GL 4202026) and `UAP_5800_16` as Depletion
  (GL 5230003) → Opex re-labelled as depreciation and depletion.

Fix: post OPEX to a single Opex entry (not 5800_14/15/16). Depreciation and depletion are their own
inputs and the source block has none.

## 5. Capex entry numbers — what the codes mean

| Code | Description | Parent | Read by Tax capital allowance as |
|---|---|---|---|
| `UAP_110` | Acquisition | CAPEX_CST | seismic/exploration |
| `UAP_120` | Exploration – non drilling | CAPEX_CST | seismic/exploration |
| `UAP_121` | Exploration & Appraisal drilling | CAPEX_CST | exploration wells |
| `UAP_124` | Exploration safety loss | CAPEX_CST | exploration wells |
| `UAP_130` | Production Well Oil | CAPEX_CST | development drilling (÷5) |
| `UAP_131` | Production Well Gas | CAPEX_CST | — (gas via AMT_210 total) |
| `UAP_132` / `136` | Capital Construction Oil | CAPEX_CST | facilities |
| `UAP_133` / `137` | Capital Construction Gas | CAPEX_CST | — |
| `UAP_138` | IPP Infrastructure | CAPEX_CST | facilities |
| `UAP_139` | Terminals | CAPEX_CST | facilities |
| `UAP_141` | Land and Building | CAPEX_CST | — |
| `UAP_140` | Movable Asset | **CAPEX_OTH** (non-production) | — |

`UAP_CAPEX_OTH` holds only `UAP_140`. On the card, Devt Well_Gas went to Gas `UAP_140 Movable` —
i.e. gas development wells were loaded as non-production movable assets.

Suggested mapping for the new workbook (**for Noel to confirm**, not applied):

| Source row | Oil (`AMT_200`) | Gas (`AMT_210`) |
|---|---|---|
| Seismic Acquisition (70) | `UAP_110` | |
| Seismic Processing / Reprocessing (71–72) | `UAP_120` | |
| Exploration / Appraisal Wells (73–74) | `UAP_121` | |
| Devt / Comptn / W-Over Well Oil (75–77) | `UAP_130` | |
| CAPEX Facilities Oil (78) | `UAP_132` (or 139 if terminals) | |
| Other Capex – not attributable to production (79) | `UAP_140`? | |
| Devt / Comptn / W-Over Well Gas (80–82) | | `UAP_131` |
| CAPEX Facilities Gas (83) | | `UAP_133` |
| OPEX Oil / Gas (84–85) | one `UAP_OPEX_CST` base, e.g. `UAP_4110` | same |

"Other Capex (not attributable to production)" by its name belongs in `UAP_CAPEX_OTH` (`UAP_140`), but
the Royalties Oil cost base (step 14) reads only `UAP_CAPEX_CST`, while the Gas base (step 15) also
reads `UAP_CAPEX_OTH`. Whether non-production capex should be in the royalty/cost-oil base needs one
rule applied to both.

## 6. Equity participation (55.1% in SAC vs 58.7% weighted average)

The block's own equity row (88) is 0, so the 55.1% in SAC did not come from this block. To trace:
where `PART_*` / `AMT_90` is populated for NU03_JV005 (the v1 file deliberately excludes `AMT_90`).

## 8. Errors in the source workbook (Renaissance calc block, `NUIMS` rows 2195–2436)

Columns: P–R = 2022–2024, S = 2025 Jan–Aug, T = 2025 Sep–Dec, U = 2025 YEO, **V/W = "2026 SOURCE"
(N'M / $'M, blank for this block)**, X–AB = 2026–2030. Several formulas use "the column to the left"
as *previous year*; inserting V/W (and S/T) broke them.

| Row | Line | Formula (2026, col X) | Problem | Effect on 2026 |
|---|---|---|---|---|
| 2312 | HCDT Fund Payable – Oil (3% of **prior-year** Opex) | `=W2311*$G2310` | Should be `U2311` (2025 YEO). 2025 YEO col U uses `T2311` (Sep–Dec only) instead of 2024 (R). | 2026 HCDT = 0 instead of 3% × 1,769 = 53.07 |
| 2324 | HCDT Fund Payable – Gas | `=W2323*$G2322` | Same | 0 |
| 2350 | Amortised Oil Capex (20/20/20/20/19 over 5 yrs) | `X*Y1 + W*Y2 + V*Y3 + S*Y4 + R*Y5` | Should be X, U, R, Q, P. Uses blank 2026-source cols and 2025 Jan–Aug only. Col Y (2027) still points at W/V/S. | 334.21 (understated) |
| 2351 | Amortised Other Capex | rates `$G2344…$G2348` | Rate rows shifted by one; G2348 is blank. Col Z reverts to G2343… | inconsistent by year |
| 2352 | Amortised Gas Capex | rates `$G2345…$G2349` | Shifted by two; G2348/G2349 blank | inconsistent by year |
| 90 / 2216 | No. of producing fields | input = 0 | PIA production-based royalty multiplies by field count | PIA oil royalty = 0 (not used while regime = PPT) |
| 88 / 2430 | NNPC Crude Oil Equity | input = 0 | NNPC share of profit oil = 0 | see §6 |

The Renaissance Capex/Opex inputs (rows 70–85) are typed values — there is no formula trail inside the
workbook back to a project list or to an NU03 allocation, so the split between JV direct capex and any
NU03 overhead allocation cannot be derived from this sheet. **Open with Noel:** which line(s) carry the
NU03 allocation and where its source is.

### Question this raises for SAC

`PPP_Upstream_Tax` step 5/6 computes HCDT on **same-year** Opex (`TAX015_15 = AMT_220`). The Excel intent
(and PIA s.240) is 3% of the **preceding** year's operating expenditure. If prior-year is the rule,
SAC needs a `PREVIOUS(1)` / prior-year lookup; if same-year is the agreed simplification, it should be
recorded as a deliberate difference. The amortisation schedule should be checked against the same
prior-year logic.

## 7. Still needed

- `PPP_EntryNr` and `WPLn` member hierarchy (`Test data - Master data.xlsx`) — confirms §4 and §5.
- The v1 upload file — check every Renaissance row's `WPLn` × `PPP_EntryNr` against §3.
- 2025 split (Aug blank, ROY = YEO): source cols 19/20 are populated (e.g. Seismic Reprocessing
  18.464 / −11.261), so a blank August is an upload-file issue, not a source gap. Verify in v1 file.
