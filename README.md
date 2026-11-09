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

SAC is never changed directly from this repository. Every change follows these steps:

1. **Snapshot** – the current SAC configuration is exported into the relevant folder on `main`.
2. **Propose** – a branch and pull request containing the before/after script and a change note
   in `proposed-changes/` (what, why, Trello card, test to run, rollback).
3. **Agree** – the PR is reviewed and approved.
4. **Apply** – the change is applied manually in SAC by the agreed person.
5. **Confirm** – the snapshot on `main` is updated to match SAC, the PR is merged and the Trello card
   moves to *Ready for testing*.

If SAC is changed outside this process, re-snapshot it before proposing anything new.

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
