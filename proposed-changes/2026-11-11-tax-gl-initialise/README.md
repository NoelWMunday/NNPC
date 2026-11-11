# Change — #24: Tax "GL Entries - Initialise" step + gas flare penalty at equity

- **Trello:** #24 https://trello.com/c/ycGHaDR6
- **Decisions (Noel, 11 Nov 17:29):**
  - "yes at the step — we have it in the other files and we need it here too" (clear all GC_CR on UP_0005).
  - Non-productive cost at the NNPC equity share; "for now just the one line" (gas flare penalty).
- **Status:** APPLIED 11 Nov 2026 17:35 SAST (`0cabc34`, Tax v25)
- **Scripts:** [DIFF.md](DIFF.md), [manifest.json](manifest.json)

## Structure

| Step | Before (v24) | After |
|---|---|---|
| 21 | GL Entries | **GL Entries - Initialise** (same step id, new name and script) |
| 22 | — | **GL Entries** (new step `38173194…`, duplicated from 21 in the designer; the v24 GL script with the changes below) |

A blank new step failed validation ("hierarchy name of the %Entity% parameter is not defined"); a duplicated step validates. So the old step keeps its id and becomes the initialise step, and the duplicate is GL Entries.

## Changes

- **GL Entries - Initialise:** `DELETE()` on `GC_CR`, `PPP_EntryNr = UP_0005`, all GL accounts, USD, for the entity. Same pattern as
  `PPP_Upstream_Revenue` › 7 "GL Entries - initialise". Every run now starts from an empty UP_0005, so dropped postings
  cannot linger. GL Entries re-posts all UP_0005 lines, including revenue (6011008) and royalty (5100007), which Revenue
  and Royalties also post earlier in the chain.
- **GL Entries:** the 11 `= 0` lines are removed (covered by the initialise step). 4500006 adds the gas flare penalty
  `AMT_230` / `UAP_GFP` × `AMT_90` / 100.

## Effect

- `PPP_Upstream_Royalties` › 22 posts development cost to 5090002 on UP_0005 before Tax runs. The initialise step clears
  it. Where development cost is posted is open with Noel (item 1, 11 Nov): it would then move into Tax GL Entries.
- Expected RENAISSANCE 2026: 4500006 = 1,488.95 + 488.35 × 55.06 % (268.89) = 1,757.84; profit before apportionment
  425.63 − 268.89 = 156.74.

Rollback: restore step 21's name and script from the left side of [DIFF.md](DIFF.md), delete step 22.
