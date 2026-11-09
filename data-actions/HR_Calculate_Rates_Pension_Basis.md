# HR_Calculate_Rates_Pension_Basis

> HR Pension Basis Calc

| | |
|---|---|
| SAC id | `DA913E84BFC7A56485947732A6652925` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-08-14T14:53:45.733Z by NMUNDAY |
| Called by | [HR_Calculate_All_Parameters](HR_Calculate_All_Parameters.md) |
| Used in stories | [PPP_HR](../stories/PPP_HR.md), [PPP_HR_Parameters](../stories/PPP_HR_Parameters.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Calc Pension Basis NNPC M2 to M6 | SCRIPT |  |
| 2 | Calc Pension Basis NNPC SS1 to JS1 | SCRIPT |  |

### 1. Calc Pension Basis NNPC M2 to M6 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = "N01_HCM"
MEMBERSET [d/PCycle] = "HR"
MEMBERSET [d/PPP_Currency] = ("NGN")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/CostElement] = ("#")

MEMBERSET [d/Measures] = ("Rates")
MEMBERSET [d/Grade] = ("M1","M2","M3","M4","M5","M6")
MEMBERSET [d/Ln] = ("CE01101", "CE01301", "MB_007")
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))

DATA([d/Ln] = "CE04001") = 
	(RESULTLOOKUP([d/Ln] = "CE01101") + RESULTLOOKUP([d/Ln] = "CE01301") + RESULTLOOKUP([d/Ln] = "MB_007")) * (1 +
	(RESULTLOOKUP([d/Measures] = "Qty", [d/Ln] = "PR_020", [d/CostElement] = "#", [d/Grade] = "#", [d/PPP_Currency] = "#", [d/Date] = "000000" /*! Pension % */) / 100))
```

Parameters used: DateSelection

### 2. Calc Pension Basis NNPC SS1 to JS1 — SCRIPT

```
MEMBERSET [d/PPP_Currency] = ("NGN")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PCycle] = "HR"
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = "N01_HCM"
MEMBERSET [d/Grade] = ("SS1", "SS2", "SS3", "SS4", "SS5", "SS6", "SS7", "JS1")
MEMBERSET [d/Measures] = ("Rates")
MEMBERSET [d/Ln] = ("CE01101", "CE01301")
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/CostElement] = ("#")

DATA([d/Ln] = "CE04001") = 
	(RESULTLOOKUP([d/Ln] = "CE01101") + RESULTLOOKUP([d/Ln] = "CE01301")) * (1 +
	(RESULTLOOKUP([d/Measures] = "Qty", [d/Ln] = "PR_020", [d/CostElement] = "#", [d/Grade] = "#", [d/PPP_Currency] = "#", [d/Date] = "000000" /*! Pension % */) / 100))
```

Parameters used: DateSelection
