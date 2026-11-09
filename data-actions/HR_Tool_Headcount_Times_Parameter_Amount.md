# HR_Tool_Headcount_Times_Parameter_Amount

| | |
|---|---|
| SAC id | `B9214684BFC7480EA13D2A8B55B880DA` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-10-13T07:16:53.477Z by NMUNDAY |
| Called by | [HR_Calculate_Expense_Pension_Conribution](HR_Calculate_Expense_Pension_Conribution.md) |
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
| `ParameterMeasureSelection` | PROMPT | MEMBER | CustomDimension1 | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `TargetMeasureSelection` | PROMPT | MEMBER | CustomDimension1 | SINGLE | `"Source"` |
| `ParameterCostElement` | PROMPT | MEMBER | CostElement | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `ParameterGrade` | PROMPT | MEMBER | Grade | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ParameterCurrency` | PROMPT | MEMBER | PPP_Currency | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `TargetMeasureForecast` | PROMPT | MEMBER | CustomDimension1 | SINGLE | `"Source_FC"` |
| `CurrentFY` | PROMPT | MEMBER | Date | MULTI | `[["(all)", "2027"]]` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Fill Forecast Periods and apply escallation | SCRIPT |  |
| 2 | Fill Forecast Periods and apply escallation | SCRIPT |  |
| 3 | Calculate Cost | SCRIPT | **DISABLED** |
| 4 | Calculate Cost | SCRIPT |  |

### 1. Fill Forecast Periods and apply escallation — SCRIPT

```
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(1,"YEAR",%CY%)
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %ParameterGrade%))
MEMBERSET [d/Measures] = (%ParameterMeasureSelection%)
MEMBERSET [d/CostElement] = (%ParameterCostElement%)
MEMBERSET [d/PPP_Currency] = (%ParameterCurrency%)
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Ln] = (%Parameter%)
MEMBERSET [d/Lock] = ("#")

DATA() = RESULTLOOKUP([d/Date] = "000000" /*!  Parameter  */)
```

Parameters used: CY, EntitySelection, ParameterGrade, ParameterMeasureSelection, ParameterCostElement, ParameterCurrency, Parameter

### 2. Fill Forecast Periods and apply escallation — SCRIPT

```
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Date] = NEXT(2,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %ParameterGrade%))
MEMBERSET [d/Measures] = (%ParameterMeasureSelection%)
MEMBERSET [d/CostElement] = (%ParameterCostElement%)
MEMBERSET [d/PPP_Currency] = (%ParameterCurrency%)
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Ln] = (%Parameter%)
MEMBERSET [d/Lock] = ("#")

FOREACH [d/Date].[p/YEAR] ASC

	//Forecast Years
//	DATA() =  RESULTLOOKUP([d/Date] = PreYearLast())		
//	DATA() =  RESULTLOOKUP([d/Ln] = %EscallationParam%, [d/Date] = "000000", [d/Measures] = "Qty", [d/PPP_Currency] = "#", [d/CostElement] = "#", [d/GL] = "#", [d/Grade] = "#" /*! Escallation Parameter */) / 100
	DATA() =  RESULTLOOKUP([d/Date] = PreYearLast()) * ( 1 + (
				RESULTLOOKUP([d/Ln] = %EscallationParam%, [d/Date] = "000000", [d/Measures] = "Qty", [d/PPP_Currency] = "#", [d/CostElement] = "#", [d/GL] = "#", [d/Grade] = "#" /*! Escallation Parameter */) / 100 ))

	
ENDFOR
```

Parameters used: CY, EntitySelection, ParameterGrade, ParameterMeasureSelection, ParameterCostElement, ParameterCurrency, Parameter, EscallationParam

### 3. Calculate Cost — SCRIPT

```
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %TargetGrade%))
MEMBERSET [d/GL] = (%TargetGL%)


INTEGER @ForecastPeriod = 0
FOREACH [d/Date].[p/YEAR] ASC
	
	IF [d/Date].[p/YEARDESC] = [d/PCycle].[p/Current_Year] THEN
		DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = %TargetMeasureSelection%, [d/PPP_Currency] = %ParameterCurrency%, [d/Ln] = "EX_GL", [d/Lock] = "#") = 
			RESULTLOOKUP([d/Measures] = %ParameterMeasureSelection%, [d/CostElement] = %ParameterCostElement%, [d/PPP_Currency] = %ParameterCurrency%, [d/GL] = "#", [d/Ln] = %Parameter%, [d/Lock] = "#" /*!  Parameter  */) * 
			RESULTLOOKUP([d/Measures] = "QtyInt", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Ln] = "HEADCOUNT", [d/GL] = "#" /*!  Headcount  */)
	ENDIF
	
	IF [d/Date].[p/YEARDESC] = [d/PCycle].[p/Forecast_Year_Start] THEN
		@ForecastPeriod = 1
	ENDIF
	
	IF @ForecastPeriod = 1 THEN
		DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = %TargetMeasureForecast%, [d/PPP_Currency] = %ParameterCurrency%, [d/Ln] = "EX_GL", [d/Lock] = "#") = 
			RESULTLOOKUP([d/Measures] = %ParameterMeasureSelection%, [d/CostElement] = %ParameterCostElement%, [d/PPP_Currency] = %ParameterCurrency%, [d/GL] = "#", [d/Ln] = %Parameter%, [d/Lock] = "#" /*!  Parameter  */) * 
			RESULTLOOKUP([d/Measures] = "QtyInt", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Ln] = "HEADCOUNT", [d/GL] = "#" /*!  Headcount  */)
	ENDIF
	
	IF [d/Date].[p/YEARDESC] = [d/PCycle].[p/Forecast_Year_End] THEN
		@ForecastPeriod = 0
	ENDIF
	
ENDFOR
```

Parameters used: DateSelection, EntitySelection, TargetGrade, TargetGL, TargetMeasureSelection, ParameterCurrency, ParameterMeasureSelection, ParameterCostElement, Parameter, TargetMeasureForecast

### 4. Calculate Cost — SCRIPT

```
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %TargetGrade%))
MEMBERSET [d/GL] = (%TargetGL%)

DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = %TargetMeasureSelection%, [d/PPP_Currency] = %ParameterCurrency%, [d/Ln] = "EX_GL", [d/Lock] = "#") = 
		RESULTLOOKUP([d/Measures] = %ParameterMeasureSelection%, [d/CostElement] = %ParameterCostElement%, [d/PPP_Currency] = %ParameterCurrency%, [d/GL] = "#", [d/Ln] = %Parameter%, [d/Lock] = "#" /*!  Parameter  */) * 
		RESULTLOOKUP([d/Measures] = "QtyInt", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Ln] = "HEADCOUNT", [d/GL] = "#" /*!  Headcount  */)
```

Parameters used: DateSelection, EntitySelection, TargetGrade, TargetGL, TargetMeasureSelection, ParameterCurrency, ParameterMeasureSelection, ParameterCostElement, Parameter
