# Change — Tax › Initialise keeps CST14; Royalties settings read at Date 000000

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Decisions (Noel, 10 Nov 11:53):** (2) remove `CST14` from the Tax initialise step. (5) Settings are centralised on Date
  `000000`. The hard-coded `202612` dates are left over from development.
- **Status:** APPLIED 10 Nov 2026 11:59 SAST (commit `58435d4`) — see `DEPLOYMENTS.md`
- **Scripts:** [DIFF.md](DIFF.md) · [manifest.json](manifest.json)

| Data action › step | Change |
|---|---|
| `PPP_Upstream_Tax` › 1 Initialise | `BASEMEMBER([d/WPLn],"CST14")` removed from the `DELETE()` scope. `CST14` (Total costs to be apportioned) is owned by `PPP_Upstream_CostAlloc`, which clears it in its step 1 and rebuilds it. It now stays visible after a run. `REV_32/26/40` and `REV3_05` are still deleted here, as decided. |
| `PPP_Upstream_Royalties` › 3 Royalties - Tranch volumes | 20 lookups of `SET05_*` at `[d/Date]="202612"` → `"000000"` |
| `PPP_Upstream_Royalties` › 4 Royalties - Values (Oil) | 15 lookups of `SET05_*` at `[d/Date]="202612"` → `"000000"` |

Scan of all 65 data actions for hard-coded dates other than `000000`: only these 35 lookups, plus 64 in
`PPP_Upstream` (the old 54-step chain, not used by any story). Those are left alone.

## Test

Re-run Upstream (Calculations) for RENAISSANCE JV.
- Royalties should be unchanged: Renaissance takes the PA path, and its settings at `202612` and `000000` agree.
- References tab: "Total costs to be apportioned" (`CST14_*`) is now filled after the run.

## Rollback

Apply the left side of [DIFF.md](DIFF.md).
