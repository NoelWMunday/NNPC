# HR_Tool_Fill_Forecast_Ref_Amounts

| | |
|---|---|
| SAC id | `71D20684BFC2357B15D57C62C99840F3` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-10-19T11:04:04.598Z by NMUNDAY |
| Called by | [HR_Calculate_All_Parameters](HR_Calculate_All_Parameters.md) |
| Used in stories | [PPP_HR](../stories/PPP_HR.md), [PPP_HR_Parameters](../stories/PPP_HR_Parameters.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `TargetGrade` | PROMPT | MEMBER | Grade | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `TargetCostElement` | PROMPT | MEMBER | CostElement | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `TargetGL` | PROMPT | MEMBER | GL | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `Parameter` | PROMPT | MEMBER | Ln | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `EscallationParam` | PROMPT | MEMBER | Ln | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `ParameterMeasureSelection` | PROMPT | MEMBER | CustomDimension1 | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `TargetMeasureSelection` | PROMPT | MEMBER | CustomDimension1 | SINGLE | `"Source"` |
| `ParameterCostElement` | PROMPT | MEMBER | CostElement | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ParameterGrade` | PROMPT | MEMBER | Grade | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ParameterCurrency` | PROMPT | MEMBER | PPP_Currency | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `CurrentYear` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2027"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Fill Forecast Periods and apply escallation | SCRIPT |  |
| 2 | Fill Forecast Periods and apply escallation | SCRIPT |  |

### 1. Fill Forecast Periods and apply escallation — SCRIPT

First planning year (CY+1)

```
MEMBERSET [d/PCycle] = "HR" 
MEMBERSET [d/Date] = BASEMEMBER([d/Date],%CurrentYear%)
MEMBERSET [d/PPP_Entity] = "N01_HCM"
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %ParameterGrade%))
MEMBERSET [d/Measures] = (%ParameterMeasureSelection%)
MEMBERSET [d/CostElement] = (BASEMEMBER([d/CostElement].[h/CalcInputH], %ParameterCostElement%))
MEMBERSET [d/PPP_Currency] = (%ParameterCurrency%)
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Ln] = (BASEMEMBER([d/Ln].[h/H1], %Parameter%))

DATA() = RESULTLOOKUP([d/Date] = "000000" /*!  Parameter  */)
```

Parameters used: CurrentYear, ParameterGrade, ParameterMeasureSelection, ParameterCostElement, ParameterCurrency, Parameter

### 2. Fill Forecast Periods and apply escallation — SCRIPT

Years after CY+1

```
// Current year that is passed as a variable is actually CY+1

MEMBERSET [d/PCycle] = "HR" 
MEMBERSET [d/PPP_Entity] = "N01_HCM"
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %ParameterGrade%))
MEMBERSET [d/Measures] = (%ParameterMeasureSelection%)
MEMBERSET [d/CostElement] = (BASEMEMBER([d/CostElement].[h/CalcInputH], %ParameterCostElement%))
MEMBERSET [d/PPP_Currency] = (%ParameterCurrency%)
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Ln] = (BASEMEMBER([d/Ln].[h/H1], %Parameter%))

INTEGER @ForecastYearStartCount = 0

FOREACH [d/Date].[p/YEAR] ASC

	IF [d/Date] = BASEMEMBER([d/Date] , %CurrentYear%) THEN

		@ForecastYearStartCount = 2

	ELSEIF @ForecastYearStartCount > 1 AND @ForecastYearStartCount < 7 THEN
			IF [d/Date].[p/MONTHDESC] = "Dec" THEN
				
				@ForecastYearStartCount = @ForecastYearStartCount + 1
				
				//Forecast Years
				DATA() = RESULTLOOKUP([d/Date] = PREYEARLAST()) * (1 + (
				RESULTLOOKUP([d/Ln] = %EscallationParam%, [d/Date] = "000000", [d/Measures] = "Qty", [d/PPP_Currency] = "#", [d/CostElement] = "#", [d/GL] = "#", [d/Grade] = "#" /*! Escallation Parameter */) / 100
																		)
																   )
			ENDIF
	ENDIF
ENDFOR
```

Parameters used: ParameterGrade, ParameterMeasureSelection, ParameterCostElement, ParameterCurrency, Parameter, CurrentYear, EscallationParam
