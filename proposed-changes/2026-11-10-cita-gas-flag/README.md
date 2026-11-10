# Change — #20 CITA on gas applies under both tax regimes

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Decision (Noel, 10 Nov 14:05):** approved. Take the PIA flag out of the gas CITA line.
- **Status:** APPROVED — applying
- **Where:** `PPP_Upstream_Tax` › 20 "Tax - CITA (Oil & Gas)" › line 25 (now lines 25–26) — [DIFF.md](DIFF.md)

`TAX090_20` (JV CITA – Gas) = CITA rate × chargeable profit gas (`TAX080_10`) / 100, without `× SET10_10`. That matches NUIMS row
2426 `=MAX(X2423*X2411,0)`. The `< 0 → 0` floor on the next line stays. Oil (`TAX090_15`, line 22) keeps the PIA flag, as row 2425 does.

Expected RENAISSANCE 2026: JV CITA – Gas 291.29 (once chargeable profit gas = 970.96).

Rollback: apply the left side of [DIFF.md](DIFF.md).
