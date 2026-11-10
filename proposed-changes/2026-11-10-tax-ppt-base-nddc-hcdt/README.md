# Change — #20 C: PPT base deducts NDDC and HCDT (oil)

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Decision (Noel, 10 Nov 15:28):** "Yes add the members so we can fix C."
- **Status:** APPLIED 10 Nov 2026 15:42 SAST (`d70d240`, Tax v16)
- **Model:** `PPP_BUSPREMISE` › WPLn — added 10 Nov 15:38 (Claude), parent `TAX050_20` (Default hierarchy), Calculated? = Y:
  - `TAX050_20_40` "Less: NDDC Levy Payable (Oil)" — source `TAX025_05`, written by `PPP_Upstream_Tax` › 3 "Tax - NDDC Levy Payable (Oil)" › line 24
  - `TAX050_20_45` "Less: Host Communities Development Trust (HCDT) Fund Payable - Oil" — source `TAX015_05`, written by › 5 "Tax - HCDT Fund Payable (Oil)" › line 24
  Descriptions follow the same deductions in the Dev Levy base (`TAX005_15_40` / `TAX005_15_35`, › 7 lines 26–27).
- **Scripts:** [DIFF.md](DIFF.md), [manifest.json](manifest.json)

NUIMS X2370 (Assessable profit for PPT) deducts NDDC oil (row 2316) and HCDT oil (row 2312). The three places that
add up the PPT base all gain the two lines:

| Step | Lines | |
|---|---|---|
| › 12 "Tax - Capital allowance for PPT" | 60–61 (new DATA), 70–73 (`#ASSESSABLE`) | CA limit |
| › 13 "Tax - CA Limit Rolling Balance (Oil)" | 47–50 (`#TAX050_20`) | CA-limit deduction (66.67 %) |
| › 15 "Tax - Chargeable Profit for PPT" | 28–31 (`#TAX050_20`) | `TAX065_05` |

Expected RENAISSANCE 2026: PPT base falls by NDDC 73.38 + HCDT 53.07 = 126.45. The sheet deducts NDDC only (its HCDT is 0,
column-W bug, closed by Noel), so SAC's PPT will be 85 % × 53.07 = 45.11 below the sheet, plus the amortisation (D)
differences.

Not changed: Hydrocarbon Tax allowable costs (› 16 `TAX070_40`) also omit NDDC/HCDT where NUIMS X2394 includes them.
HT is 0 under PPT; can follow once D is settled.

Rollback: apply the left side of [DIFF.md](DIFF.md). The two members are harmless if unused.
