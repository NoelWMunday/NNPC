# HR_Calculate_Rates_Fuel

| | |
|---|---|
| SAC id | `D81A5E84BFC73D898D5688B4BA0ABA79` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-10-19T09:46:51.615Z by NMUNDAY |
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
| `CY_plus_1` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2026", "202612"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Calculate_Fuel | SCRIPT |  |
| 2 | Calculate_Diesel | SCRIPT |  |

### 1. Calculate_Fuel — SCRIPT

```
CONFIG.HIERARCHY = [d/Ln].[h/SCH]
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Date] = BASEMEMBER([d/Date] , %CY_plus_1%)
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %GradeSelection%))
MEMBERSET [d/PPP_Currency] = ("NGN")
MEMBERSET [d/Ln] = ("MB_025")
MEMBERSET [d/PCycle] = "HR"
MEMBERSET [d/CostElement] = ("#")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/GL] = ("#")


DATA([d/Measures] = "Rates") = 
	RESULTLOOKUP([d/Measures] = "Qty", [d/PPP_Currency] = "#") * 
	RESULTLOOKUP([d/Measures] = "Price") * 
	RESULTLOOKUP([d/Measures] = "Weeks", [d/PPP_Currency] = "#") * 
	RESULTLOOKUP([d/Measures] = "NoCars", [d/PPP_Currency] = "#")
```

Parameters used: EntitySelection, CY_plus_1, GradeSelection

### 2. Calculate_Diesel — SCRIPT

```
CONFIG.HIERARCHY = [d/Ln].[h/SCH]
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Date] = BASEMEMBER([d/Date] , %CY_plus_1%)
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %GradeSelection%))
MEMBERSET [d/PPP_Currency] = ("NGN")
MEMBERSET [d/Ln] = ("MB_020")
MEMBERSET [d/PCycle] = "HR"
MEMBERSET [d/CostElement] = ("#")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/GL] = ("#")

DATA([d/Measures] = "Rates") = 
	RESULTLOOKUP([d/Measures] = "Qty", [d/PPP_Currency] = "#") * 
	RESULTLOOKUP([d/Measures] = "Price") * 
	RESULTLOOKUP([d/Measures] = "Weeks", [d/PPP_Currency] = "#")
```

Parameters used: EntitySelection, CY_plus_1, GradeSelection
