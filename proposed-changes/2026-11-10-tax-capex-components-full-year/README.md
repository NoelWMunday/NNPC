# Change — #20 D (part): CAPEX components include closed periods (Hist_Open)

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Decision (Noel, 10 Nov 15:54):** "The Hist_Open you can fix."
- **Status:** APPLIED 10 Nov 2026 15:57 SAST (`f9f93a5`, Tax v18)
- **Where:** `PPP_Upstream_Tax` › 10 "Tax - CAPEX Components" (whole step) — [DIFF.md](DIFF.md), [manifest.json](manifest.json)

## Why

Step 10 ran on `Lock = "#"` only. In SAC the Renaissance capex history sits on `Lock = Hist_Open`
(read 10 Nov 15:58, `AMT_200/210`, USD, by UAP entry):

| Year | Where | Matches NUIMS col |
|---|---|---|
| 2022 | — (sheet col P is 0 on every capex row) | P |
| 2023 | `202312`, Hist_Open | Q ✓ every line |
| 2024 | `202412`, Hist_Open | R ✓ every line |
| 2025 Jan–Aug | `202508`, Hist_Open | S ✓ |
| 2025 Sep–Dec | `202512`, Lock `#` | T ✓ |
| 2026 | `202612`, Lock `#` | X ✓ |

So nothing is missing from SAC; amortisation only saw 2026 and Sep–Dec 2025.

## Change

Same pattern as the Royalties cost rollup (Royalties › 14–17): iterate the USD input leaves on both locks for the
mapped UAP entries and `DATA.APPEND` into `TAX040_*` on Lock `#`, EntryNr `#`, Currency `#`, Date `LAST()`
(December). Initialise (› 1) clears `TAX*` first, so re-runs give the same totals. The UAP → `TAX040_*` mapping is
unchanged (incl. B: gas `UAP_124` reads `AMT_210`).

## Expected RENAISSANCE 2026 (20/20/20/20/19 % on 2026, 2025, 2024, 2023, 2022)

| `TAX045_05_*` | Now | After | Sheet (buggy, §8 of findings) |
|---|---|---|---|
| Oil fac + drilling (`_10`) | 169.60 | 412.15 | 334.21 |
| Other oil (`_15`) | 21.41 | 41.90 | 7.94 |
| Gas (`_20`) | 313.81 | 492.21 | 203.03 |

TAX040 years 2023–2025 now also hold full-year totals. Exploration (`TAX040_05_05`, UAP_110/120/121/124) stays
expensed in CITA/HT — open with Noel (the sheet amortises it with the same 5-year rates).

Rollback: apply the left side of [DIFF.md](DIFF.md).
