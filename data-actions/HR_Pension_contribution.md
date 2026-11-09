# HR_Pension_contribution

| | |
|---|---|
| SAC id | `A9FE8CBFC2FDEB3B6D64678B046BAE` |
| Default model | PPP Workforce planning |
| Created by | NMUNDAY |
| Last changed | 2026-08-14T08:35:13.147Z by NMUNDAY |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget 2026 (Reference)"` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `CurrentFY` | PROMPT | MEMBER | Date | MULTI | `[["(all)", "2027"]]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Fill Forecast Periods and apply escallation | SCRIPT | **DISABLED** |
| 2 | Calculate Cost | SCRIPT |  |

### 1. Fill Forecast Periods and apply escallation — SCRIPT

```
// Calc = (Total of all grades rates for pension contribution) * escalation factor * (total of all headcounts)

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], "Total"), BASEMEMBER([d/Grade].[h/H1], "RS_05"))
MEMBERSET [d/Measures] = "Source"
MEMBERSET [d/CostElement] = "CE04001"
MEMBERSET [d/PPP_Currency] = BASEMEMBER([d/PPP_Currency] , "Total")
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Ln] = "PR_020"
MEMBERSET [d/Lock] = ("#")

INTEGER @ForecastYearStartCount = 0

FOREACH [d/Date].[p/YEAR] ASC

	FOREACH [d/Date].[p/CALMONTH] ASC
		IF [d/Date].[p/MONTHDESC] = "Dec" THEN
			//Current Year
			IF [d/Date] = BASEMEMBER([d/Date] , %CurrentFY%) THEN
				DATA() = RESULTLOOKUP([d/Date] = "000000" /*!  Parameter  */)
				@ForecastYearStartCount = 1
			ELSEIF @ForecastYearStartCount > 0 THEN
				//Forecast Years
				DATA() =  RESULTLOOKUP([d/Date] = PreYearLast())		
				DATA() =  RESULTLOOKUP([d/Ln] = "PR_015", [d/Date] = "000000", [d/Measures] = "Qty", [d/PPP_Currency] = "#", [d/CostElement] = "#", [d/GL] = "#", [d/Grade] = "#" /*! Escallation Parameter */) / 100
				DATA() =  RESULTLOOKUP([d/Date] = PreYearLast()) * ( 1 + (
						  	RESULTLOOKUP([d/Ln] = "PR_015", [d/Date] = "000000", [d/Measures] = "Qty", [d/PPP_Currency] = "#", [d/CostElement] = "#", [d/GL] = "#", [d/Grade] = "#" /*! Escallation Parameter */) / 100 ))
			ENDIF
		ENDIF
	ENDFOR

ENDFOR
```

Parameters used: EntitySelection, CurrentFY

### 2. Calculate Cost — SCRIPT

```
//MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade], "Total"), BASEMEMBER([d/Grade], "RS_05"))
MEMBERSET [d/GL] = "5010034"

DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = "Source", [d/Ln] = "EX_GL", [d/Lock] = "#") = 
		RESULTLOOKUP([d/Measures] = "Rates", [d/CostElement] = "CE04001", [d/GL] = "#", [d/Ln] = "PR_015", [d/Lock] = "#" /*!  Parameter  */)
		
DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = "Source", [d/Ln] = "EX_GL", [d/Lock] = "#") = 
		RESULTLOOKUP([d/Measures] = "QtyInt", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Ln] = "HEADCOUNT", [d/GL] = "#" /*!  Headcount  */)
		
DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = "Source", [d/Ln] = "EX_GL", [d/Lock] = "#") = 
		RESULTLOOKUP([d/Measures] = "Rates", [d/CostElement] = "CE04001", [d/GL] = "#", [d/Ln] = "PR_015", [d/Lock] = "#" /*!  Parameter  */) * 
		RESULTLOOKUP([d/Measures] = "QtyInt", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Ln] = "HEADCOUNT", [d/GL] = "#" /*!  Headcount  */)
```

Parameters used: EntitySelection
