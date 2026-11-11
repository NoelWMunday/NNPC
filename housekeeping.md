# Housekeeping

Clean-ups to do when convenient (Noel or Claude, via the model's delete functionality or a one-off data
action). Kept deliberately until then — see "Messy data is deliberate" in `CLAUDE.md`.

| # | Item | Scope | Raised |
|---|---|---|---|
| H1 | Stale upload inputs on `PPP_Currency = "#"` from the 14 Aug load. Since 10 Nov, Royalties step 1 rebuilds `AMT_200/210/220/230` on `#` for each entity it runs (`Lock = "#"`), so what's left is entities not yet re-run and `Lock = Hist_Open` periods | `PPP_BUSPREMISE`, NU03 JVs, `Budget 2026 (Reference)`, `AMT_200/210/220/230` on `#` | Trello #19, 9 Nov |
| H2 | `CST05_*` records on `PPP_Currency = USD` written by Royalties runs before 10 Nov (never read) | `PPP_BUSPREMISE`, NU03 JVs | #19, 10 Nov |
| H3 | Metrics loaded on `PPP_Currency = USD` by mistake (e.g. SEPNU `AMT_80` 190, `AMT_85` 72.27). Metrics (`AMT_46/80/85/90/97`, `UOM_*`, `SET*`) belong on `#` (UOM measure); no data action reads the USD copies. Clear once QA has re-entered the values on `#` | `PPP_BUSPREMISE`, NU03 JVs, `Budget 2026 (Reference)` | #23, 11 Nov |
