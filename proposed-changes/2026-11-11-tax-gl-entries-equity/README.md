# Change — #24: Tax GL Entries reproduce profit (equity basis)

- **Trello:** #24 https://trello.com/c/ycGHaDR6 (QA retest 11 Nov 16:15, items 1–6)
- **Decision (Noel, 11 Nov 16:13):** "Yes please fix and work with QA."
- **Status:** APPROVED — applying
- **Where:** `PPP_Upstream_Tax` › 21 "GL Entries" — [DIFF.md](DIFF.md), [manifest.json](manifest.json)

| QA item | Change (line numbers in the new script) |
|---|---|
| 1. 4101006 Direct Cost still posted; dropped postings stay in the model | Direct Cost commented out (40–44) — it duplicated equity OPEX in 4500006. Zero lines added for 4101006, 5080044, FINEXP_005 on UP_0005 (26–29), same pattern as the existing zero lines 19–25 |
| 2. 4500006 amortisation gross | `TAX045_05_10/15/20/25` × `AMT_90` / 100 (79–83) |
| 3. CHOOCA / Finance cost double-posted on UP_0005 | commented out (65–70); CostAlloc posts them on UP_0010 |
| 4. HCDT Gas read the oil member | reads `TAX020_05` (98–100) |
| 5. Levies gross | NDDC, HCDT Oil/Gas, Dev levy × `AMT_90` / 100 (87–106) |
| 6. Dev levy gas only | `TAX005_05` + `TAX010_05` (87–90) |

Not changed:
- **Gas flare penalty** (`AMT_230`/`UAP_GFP`, 488.35 gross in 2026) is not added to 4500006: QA's expected profit 425.63 reconciles
  exactly without it (below). It was only in the removed Direct Cost line. Open with QA/Noel.
- **Item 7** (Royalties › 22 posts `CST20` to 5090002): `CST20` = development-cost numerator ÷ `REV_05` (Royalties › 21), i.e. $/bbl.
  Posting it puts 1.03 on the GL. Needs Noel's decision (post the numerator, or drop the posting).
- A general "clear all GC_CR on UP_0005" needs a separate initialise step (a GL step's scope is GL = "#"); proposed, not done.

## Expected RENAISSANCE 2026 ($M, AMT_90 = 55.06 %)

| GL | Amount |
|---|---|
| 6011008 Revenue (`REV_30`) | 3,812.12 |
| 5100007 Royalty (`RC_TOT_10`) | −709.84 |
| 4500006 Equity OPEX 935.76 + amortisation 1,004.71 × 55.06 % = 553.19 | 1,488.95 |
| 5110007 Dev levy (76.84 + 36.31) × 55.06 % | 62.30 |
| 4109025 HCDT Oil 53.07 × 55.06 % | 29.22 |
| 4104007 HCDT Gas | 0 |
| 4111006 NDDC (73.38 + 36.78) × 55.06 % | 60.65 |
| 5100006 PPT (`TAX085_25`) | 922.91 |
| 5100005 CITA (`TAX090_25` + `TAX090_30`) | 112.62 |
| **Profit before apportionment** | **425.63** (= QA's expected) |
| UP_0010 apportioned (CostAlloc) | 298.18 |
| **Profit after apportionment** | **127.45** |

Rollback: apply the left side of [DIFF.md](DIFF.md).
