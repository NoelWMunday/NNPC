# Re-apply Tax v11 + v12 after the v14 revert

- **Trello:** #20 https://trello.com/c/3zpHY6z7
- **Why:** Noel's 15:18 save (v14, step 2 "Development cost" deactivated) came from a designer opened before 13:30 and
  reverted the approved v11 (`bcff8cf`, [rolling balances](../2026-11-10-tax-rolling-balances/README.md)) and v12
  (`9e9bd12`, [CITA gas flag](../2026-11-10-cita-gas-flag/README.md)) scripts.
- **Change:** steps 1, 5, 6, 13, 14, 16, 20 get back their v12 scripts exactly (files here = `a705537`). Step 2 stays deactivated.
  Applied together with [tax-open-items](../2026-11-10-tax-open-items/README.md) A and B (steps 9, 10).
- **Rollback:** the before-hashes in [manifest.json](manifest.json) are the v14 scripts (`2444a4a`).
