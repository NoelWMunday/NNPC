# NNPC – SAP Analytics Cloud (PPP) development

Documentation and change control for the NNPC Upstream PPP planning content in SAP Analytics Cloud
(SAC folder: `My Files / Public / NNPC / NNPC - PPP`).

SAC has no built-in version control, so this repository is the source of record for what is
configured in SAC and for every change we propose to it.

Defects are logged on the Trello board: https://trello.com/b/a85I1Cfx/nnpc

## Layout

| Folder | Contents |
|---|---|
| `sac-export/` | Raw SAC definitions (data actions, models, stories, currency table) — the snapshot everything else is generated from |
| `data-actions/` | One page per data action: parameters, steps, full scripts, call map and index (generated) |
| `models/` | Dimensions and measures per model (generated) |
| `stories/` | Models and data actions each story uses (generated) |
| `import-mappings/` | Import jobs and the column → dimension mapping of upload files |
| `tools/` | `generate_docs.py` — rebuilds the generated folders from an export |
| `findings/` | Root-cause analysis per defect, linked to the Trello card |
| `proposed-changes/` | Change notes for anything to be applied in SAC (see workflow below) |

## Change workflow

Agreed with Noel on 10 Nov 2026. Claude makes the SAC changes once they are on `main`.

1. **Branch** – work on a branch (`fix/<trello#>-<topic>`, or keep reusing a WIP branch). The branch
   holds the proposed scripts and a change note in `proposed-changes/` (what, why, Trello card, test,
   rollback) next to the current SAC version in `sac-export/`, so both copies exist at the change point.
2. **Merge** – merge the branch into `main`.
3. **Pre-check** – re-read the affected objects from SAC. If they differ from `sac-export/` on `main`,
   someone changed SAC directly: stop, snapshot, and rework the proposal.
4. **Apply** – make the change in SAC and save. Tag `main` as `sac/<yyyy-mm-dd>-<trello#>`.
5. **Confirm** – re-export, run `tools/generate_docs.py`, commit the new snapshot to `main`. The diff
   must match the proposal's `DIFF.md`. Run the test in the change note and update the Trello card.

**Rollback:** the "SAC now" side of the change's `DIFF.md` (equally, `sac-export/` at the commit before
the merge) is the previous version. Apply it to SAC the same way, then commit the snapshot.

If SAC is changed outside this process, re-snapshot before proposing anything new.

## Data action documentation template

```markdown
# <Data action name>

- **SAC ID / path:**
- **Default model:**
- **Trello areas:** (Capex · Opex · Revenue · Royalties · Cost allocation · Other income · Tax · GL)
- **Triggered from:** (story / multi action / schedule)
- **Parameters:**

## Purpose

## Steps
| # | Type | Name | Source → Target | Filters |
|---|---|---|---|---|

## Script (step n)
```advanced-formulas
...
```

## Dependencies
- Reads:
- Writes:
- Called by / calls:

## Known issues
```

## Refreshing the snapshot

1. Export the folder from SAC (read-only; produces `nnpc_sac_export_<date>.json`).
2. `python3 tools/generate_docs.py nnpc_sac_export_<date>.json .`
3. Review `git diff` — any change not made through a PR here was made directly in SAC.
