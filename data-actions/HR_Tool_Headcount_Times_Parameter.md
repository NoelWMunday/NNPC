# HR_Tool_Headcount_Times_Parameter

| | |
|---|---|
| SAC id | `51F92684BFC2040AC5693C7FA2225918` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-08-13T12:35:55.228Z by NMUNDAY |
| Called by | [HR_Calculate_Expense_Health_Contribution](HR_Calculate_Expense_Health_Contribution.md) |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `TargetGrade` | PROMPT | MEMBER | Grade | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `TargetCostElement` | PROMPT | MEMBER | CostElement | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `TargetGL` | PROMPT | MEMBER | GL | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `PlanningCycle` | PROMPT | MEMBER | PCycle | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Parameter` | PROMPT | MEMBER | Ln | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `EscallationParam` | PROMPT | MEMBER | Ln | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `CurrencySelection` | PROMPT | MEMBER | PPP_Currency | SINGLE | `"NGN"` |
| `MeasureSelectionCY` | PROMPT | MEMBER | CustomDimension1 | SINGLE | `"Source"` |
| `MeasureSelectionFC` | PROMPT | MEMBER | CustomDimension1 | SINGLE | `"Source_FC"` |
| `CurrentYr` | PROMPT | MEMBER | Date | MULTI | `[["(all)", "2027"]]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | SCRIPT |  |
| 2 | (unnamed) | SCRIPT |  |

### 1. (unnamed) — SCRIPT

```
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Grade] = ("#")
MEMBERSET [d/Measures] = ("Qty")
MEMBERSET [d/CostElement] = ("#")
MEMBERSET [d/PPP_Currency] = ("#")
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Ln] = (%Parameter%)
MEMBERSET [d/Lock] = ("#")

INTEGER @FY_Activated = 0

FOREACH [d/Date].[p/YEAR] ASC

	FOREACH [d/Date].[p/CALMONTH] ASC
		IF [d/Date].[p/MONTHDESC] = "Dec" THEN
			//Current Year
			IF [d/Date] = BASEMEMBER([d/Date] , %CurrentYr%) THEN
				DATA() = RESULTLOOKUP([d/Date] = "000000" /*!  Parameter  */)
				@FY_Activated = 1
			ELSE
				IF @FY_Activated = 1 THEN
					//Forecast Years
					DATA() =  	RESULTLOOKUP([d/Date] = PreYearLast()) * ( 1 + (
							  	RESULTLOOKUP([d/Ln] = %EscallationParam%, [d/Date] = "000000" /*! Escallation Parameter */) / 100 ) )
				ENDIF
			ENDIF
			
		ENDIF
	ENDFOR
	
ENDFOR
```

Parameters used: DateSelection, EntitySelection, Parameter, CurrentYr, EscallationParam

### 2. (unnamed) — SCRIPT

```
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %TargetGrade%))
MEMBERSET [d/GL] = (%TargetGL%)

DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = %MeasureSelectionCY%, [d/PPP_Currency] = %CurrencySelection%, [d/Ln] = "EX_GL", [d/Lock] = "#") = 
			RESULTLOOKUP([d/Measures] = "Qty", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/GL] = "#", [d/Ln] = %Parameter%, [d/Grade] = "#", [d/Lock] = "#" /*!  Parameter  */) * 
			RESULTLOOKUP([d/Measures] = "QtyInt", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Ln] = "HEADCOUNT", [d/GL] = "#" /*!  Headcount  */)
```

Parameters used: DateSelection, EntitySelection, TargetGrade, TargetGL, MeasureSelectionCY, CurrencySelection, Parameter
