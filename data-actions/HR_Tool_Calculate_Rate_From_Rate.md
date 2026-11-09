# HR_Tool_Calculate_Rate_From_Rate

| | |
|---|---|
| SAC id | `D2425684BFC281BD3A234BC217D66B5F` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-10-12T06:56:47.821Z by NMUNDAY |
| Called by | [HR_Calculate_All_Parameters](HR_Calculate_All_Parameters.md) |
| Used in stories | [PPP_HR](../stories/PPP_HR.md), [PPP_HR_Parameters](../stories/PPP_HR_Parameters.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `GradeSelection` | PROMPT | MEMBER | Grade | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `PlanningCycle` | PROMPT | MEMBER | PCycle | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ForecastPeriod` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `TargetLI` | PROMPT | MEMBER | Ln | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `SourceLI` | PROMPT | MEMBER | Ln | MULTI | `{"memberIds": [], "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | SCRIPT |  |

### 1. (unnamed) — SCRIPT

```
CONFIG.HIERARCHY = [d/Ln].[h/SCH]

MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Ln] = (BASEMEMBER([d/Ln].[h/SCH], %SourceLI%))
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %GradeSelection%))
MEMBERSET [d/PCycle] = (BASEMEMBER([d/PCycle].[h/H1], %PlanningCycle%))

MEMBERSET [d/Measures] = ("Rates")
MEMBERSET [d/PPP_Currency] = ("NGN")
MEMBERSET [d/CostElement] = ("#")
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/GL] = ("#")

DATA([d/Ln] = %TargetLI%) = RESULTLOOKUP()
```

Parameters used: EntitySelection, SourceLI, GradeSelection, PlanningCycle, TargetLI
