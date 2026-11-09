# HR_Calculate_Reference_Prod_Overhead_Split

> HR - Production/Overhead Split

| | |
|---|---|
| SAC id | `C9B8C684BFC20C3314779C5D673EB7B3` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-10-19T11:25:49.924Z by NMUNDAY |
| Called by | [HR_Calculate_All](HR_Calculate_All.md) |
| Used in stories | [PPP_HR](../stories/PPP_HR.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | DELETE_FACTS |  |
| 2 | AssignCostElement_Production | SCRIPT |  |
| 3 | AssignCostElement_Overheads | SCRIPT |  |
| 4 | CostElement_Check | SCRIPT | **DISABLED** |
| 5 | CostElement_Check | SCRIPT | **DISABLED** |

### 1. Initialise — DELETE_FACTS

<details><summary>Configuration</summary>

```json
{
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "TargetVersion"
   },
   "hierarchyName": null
  },
  "CustomDimension1": {
   "memberIds": [
    "QtyInt",
    "WorkSplitAllocation"
   ],
   "hierarchyName": null
  },
  "PPP_Currency": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "CALC_05",
    "CALC_10"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "EntitySelection"
    }
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Ln": {
   "memberIds": [
    "AL"
   ],
   "hierarchyName": "H1"
  },
  "Date": {
   "memberIds": [
    [
     "(all)",
     "2020"
    ],
    [
     "(all)",
     "2021"
    ],
    [
     "(all)",
     "2022"
    ],
    [
     "(all)",
     "2023"
    ],
    [
     "(all)",
     "2024"
    ],
    [
     "(all)",
     "2025"
    ],
    [
     "(all)",
     "2026"
    ],
    [
     "(all)",
     "2027"
    ],
    [
     "(all)",
     "2028"
    ],
    [
     "(all)",
     "2029"
    ],
    [
     "(all)",
     "2030"
    ],
    [
     "(all)",
     "2031"
    ],
    [
     "(all)",
     "2032"
    ],
    [
     "(all)",
     "2033"
    ],
    [
     "(all)",
     "2034"
    ],
    [
     "(all)",
     "2035"
    ],
    [
     "(all)",
     "2036"
    ],
    [
     "(all)",
     "2037"
    ],
    [
     "(all)",
     "2038"
    ],
    [
     "(all)",
     "2039"
    ],
    [
     "(all)",
     "2040"
    ],
    [
     "(all)",
     "2041"
    ]
   ],
   "hierarchyName": "YM"
  }
 },
 "sourceContextFilterParamRefs": [],
 "deleteMode": "DELETE",
 "disabled": false
}
```

</details>

### 2. AssignCostElement_Production — SCRIPT

```
MEMBERSET [d/PPP_Currency] = ("#")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL].[h/H1], "CALC_10"))
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Ln] = ("AL_PROD")
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], "Total", "RS_05"))
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)

IF [d/Date].[p/MONTHDESC] = "Dec" THEN
	DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = "WorkSplitAllocation") = 
		RESULTLOOKUP([d/GL] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Grade] = "#", [d/CostElement] = "#", [d/Measures] = "WorkSplitAllocation", [d/Date] = "000000")
	
	DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = "QtyInt") = 1
ENDIF
```

Parameters used: EntitySelection, CY

### 3. AssignCostElement_Overheads — SCRIPT

```
MEMBERSET [d/PPP_Currency] = ("#")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL].[h/H1], "CALC_05"))
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Ln] = ("AL_OH")
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], "RS_05", "Total"))
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)

IF [d/Date].[p/MONTHDESC] = "Dec" THEN
	DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = "WorkSplitAllocation") = 
		RESULTLOOKUP([d/GL] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Grade] = "#", [d/CostElement] = "#", [d/Measures] = "WorkSplitAllocation", [d/Date] = "000000")
	
	DATA([d/CostElement] = [d/GL].[p/CostEelement], [d/Measures] = "QtyInt") = 1
ENDIF
```

Parameters used: EntitySelection, CY

### 4. CostElement_Check — SCRIPT

```
MEMBERSET [d/PPP_Currency] = ("#")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL].[h/H1], "CALC_05", "CALC_10"))
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PCycle] = (BASEMEMBER([d/PCycle].[h/H1], %PlanningCycle%))
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/CostElement] = (BASEMEMBER([d/CostElement].[h/CalcInputH], "Calculated"))
MEMBERSET [d/Measures] = ("WorkSplitAllocation")
MEMBERSET [d/Ln] = ("AL_PROD", "AL_OH")
MEMBERSET [d/Grade] = ("#")
FLOAT @PCentTot = 0
INTEGER @OverheadCount = 0
INTEGER @ProductionCount = 0
VARIABLEMEMBER #SumGL OF [d/CostElement]


FOREACH [d/CostElement], [d/Date].[p/YEAR]
	//DATA([d/CostElement]=#SumGL) = RESULTLOOKUP([d/Measures]="QtyInt")
	
	@OverheadCount = 0
	@ProductionCount = 0
	@PCentTot = 0
	
	FOREACH [d/GL]
		@PCentTot = @PCentTot + RESULTLOOKUP()
	
		IF [d/GL].[p/Prod_Overhead] = "Overhead" THEN
			//@OverheadCount = @OverheadCount + 1
			@OverheadCount = RESULTLOOKUP([d/Measures]="QtyInt") + 1
		ENDIF
		IF [d/GL].[p/Prod_Overhead] = "Production" THEN
		//	@ProductionCount = @ProductionCount + 1
			@ProductionCount = RESULTLOOKUP([d/Measures]="QtyInt") + 1
		ENDIF
	ENDFOR
	IF @OverheadCount > 0 OR @ProductionCount > 0 THEN
		FOREACH [d/GL]
			IF @OverheadCount = 0 AND @ProductionCount > 0 THEN
				DATA() = 1 / @ProductionCount
			ENDIF
			IF @OverheadCount > 0 AND @ProductionCount = 0 THEN
				DATA() = 1 / @OverheadCount
			ENDIF
		ENDFOR
	ENDIF
ENDFOR
```

Parameters used: PlanningCycle, DateSelection, EntitySelection

### 5. CostElement_Check — SCRIPT

```
MEMBERSET [d/PPP_Currency] = ("#")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL].[h/H1], "CALC_05", "CALC_10"))
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PCycle] = (BASEMEMBER([d/PCycle].[h/H1], %PlanningCycle%))
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/CostElement] = (BASEMEMBER([d/CostElement].[h/CalcInputH], "Calculated"))
MEMBERSET [d/Measures] = ("WorkSplitAllocation")
MEMBERSET [d/Ln] = ("AL_PROD", "AL_OH")
MEMBERSET [d/Grade] = ("#")
FLOAT @PCentTot = 0
INTEGER @OverheadCount = 0
INTEGER @ProductionCount = 0
FOREACH [d/CostElement]
	@OverheadCount = 0
	@ProductionCount = 0
	@PCentTot = 0
	DATA() = RESULTLOOKUP()
	FOREACH [d/GL]
		@PCentTot = @PCentTot + RESULTLOOKUP()
		DATA() = RESULTLOOKUP()
		IF [d/GL].[p/Prod_Overhead] = "Overhead" THEN
			@OverheadCount = @OverheadCount + 1
		ENDIF
		IF [d/GL].[p/Prod_Overhead] = "Production" THEN
			@ProductionCount = @ProductionCount + 1
		ENDIF
	ENDFOR
	IF @OverheadCount > 0 OR @ProductionCount > 0 THEN
		FOREACH [d/GL]
			IF @OverheadCount = 0 AND @ProductionCount > 0 THEN
				DATA() = RESULTLOOKUP()
				DATA() = 1 / @ProductionCount
			ENDIF
			IF @OverheadCount > 0 AND @ProductionCount = 0 THEN
				DATA() = RESULTLOOKUP()
				DATA() = 1 / @OverheadCount
			ENDIF
		ENDFOR
	ENDIF
ENDFOR
```

Parameters used: PlanningCycle, DateSelection, EntitySelection
