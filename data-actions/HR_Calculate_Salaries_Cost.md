# HR_Calculate_Salaries_Cost

| | |
|---|---|
| SAC id | `E081B88E2A31CF2B4CB830641D78E1BC` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-10-19T11:09:31.691Z by NMUNDAY |
| Called by | [HR_Calculate_All](HR_Calculate_All.md) |
| Used in stories | [PPP_HR](../stories/PPP_HR.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `GradeSelection` | PROMPT | MEMBER | Grade | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `PlanningCycle` | PROMPT | MEMBER | PCycle | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ForecastPeriod` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ReportingDate` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2026", "202612"]` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | SINGLE | `{"memberId": null, "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Populate Cost Element for Parmeters | SCRIPT |  |
| 3 | Calculate_Costs | SCRIPT |  |
| 4 | Allocate costs | SCRIPT |  |
| 5 | Allocate costs - clear source | SCRIPT |  |
| 6 | (unnamed) | ALLOCATION | **DISABLED** |
| 7 | Copy Allocationto Expense GL Line Item | COPY | **DISABLED** |
| 8 | (unnamed) | NESTED_SEQUENCE | runs [HR_Calculate_Expense_Pension_Conribution](HR_Calculate_Expense_Pension_Conribution.md) |
| 9 | (unnamed) | NESTED_SEQUENCE | runs [HR_Calculate_Expense_Health_Contribution](HR_Calculate_Expense_Health_Contribution.md) |
| 10 | Calculate_ITF/NSITF Contribution | SCRIPT |  |
| 11 | Calculate_ITF/NSITF Contribution | SCRIPT |  |

### 1. Initialise — SCRIPT

```
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/CostElement] = (BASEMEMBER([d/CostElement].[h/CalcInputH], "Calc_PO_Split"))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %GradeSelection%))
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(1,"YEAR",%CY%)

DATA([d/Measures] = "Source", [d/GL] = "#", [d/Ln] = "EX_GL", [d/PPP_Currency] = "NGN", [d/Lock] = "#") = 0
DATA([d/Measures] = "Source_FC", [d/GL] = "#", [d/Ln] = "EX_GL", [d/PPP_Currency] = "NGN", [d/Lock] = "#") = 0
```

Parameters used: EntitySelection, GradeSelection, CY

### 2. Populate Cost Element for Parmeters — SCRIPT

```
MEMBERSET [d/Measures] = ("Rates")
MEMBERSET [d/Ln] = (BASEMEMBER([d/Ln].[h/H1], "SC"))
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %GradeSelection%))
MEMBERSET [d/PPP_Currency] = ("NGN")
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/PCycle] = "#"

DATA([d/Ln] = "SC_001", [d/CostElement] = [d/Ln].[p/CostElement]) = RESULTLOOKUP([d/CostElement] = "#")
```

Parameters used: GradeSelection, EntitySelection

### 3. Calculate_Costs — SCRIPT

```
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%) 
MEMBERSET [d/CostElement] = (BASEMEMBER([d/CostElement].[h/CalcInputH], "Calc_PO_Split"))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], %GradeSelection%))

DATA([d/Measures] = "Source", [d/GL] = "#", [d/Ln] = "EX_GL", [d/PPP_Currency] = "NGN", [d/Lock] = "#") = 
	RESULTLOOKUP([d/GL] = "#", [d/PPP_Currency] = "NGN", [d/Lock] = "#", [d/Measures] = "Rates", [d/Ln] = "SC_001" /*!  Salary Scale  */) * 
	RESULTLOOKUP([d/Measures] = "QtyInt", [d/GL] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Ln] = "HEADCOUNT", [d/CostElement] = "#" /*!  Headcount  */)
```

Parameters used: CY, EntitySelection, GradeSelection

### 4. Allocate costs — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = "Source"
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Grade] = BASEMEMBER([d/Grade] , "Total", "RS_05")
MEMBERSET [d/CostElement] = (BASEMEMBER([d/CostElement].[h/CalcInputH], "Calc_PO_Split"))

MEMBERSET [d/PPP_Currency] = "NGN"
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/Ln] = "EX_GL"
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)  

IF [d/GL] != "#" THEN
	
	DATA() = 	
		(RESULTLOOKUP([d/Measures] = "WorkSplitAllocation", [d/PPP_Currency] = "#", [d/Ln] = "AL_PROD") *
		RESULTLOOKUP([d/GL] = "#")) +

		(RESULTLOOKUP([d/Measures] = "WorkSplitAllocation", [d/PPP_Currency] = "#", [d/Ln] = "AL_OH") *
		RESULTLOOKUP([d/GL] = "#"))
	
ENDIF
```

Parameters used: EntitySelection, CY

### 5. Allocate costs - clear source — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = "Source"
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Grade] = BASEMEMBER([d/Grade] , "Total", "RS_05")
MEMBERSET [d/CostElement] = (BASEMEMBER([d/CostElement].[h/CalcInputH], "Calc_PO_Split"))

MEMBERSET [d/PPP_Currency] = "NGN"
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/Ln] = "EX_GL"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)  

DELETE()
```

Parameters used: EntitySelection, CY

### 6. (unnamed) — ALLOCATION

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
  "PPP_Currency": {
   "memberIds": [
    "NGN"
   ],
   "hierarchyName": "H1"
  },
  "CostElement": {
   "memberIds": [
    "Calc_PO_Split"
   ],
   "hierarchyName": "CalcInputH"
  },
  "CustomDimension1": {
   "memberIds": [
    "Source"
   ],
   "hierarchyName": null
  },
  "Ln": {
   "memberIds": [
    "EX_GL"
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
  "Grade": {
   "memberIds": [
    {
     "paramRef": "GradeSelection"
    }
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "keepSource": true,
 "overwriteTarget": true,
 "referenceDimensions": [
  {
   "id": "Date",
   "hierarchyName": "YM"
  },
  {
   "id": "PPP_Entity",
   "hierarchyName": "H1"
  },
  {
   "id": "Grade",
   "hierarchyName": "H1"
  },
  {
   "id": "CostElement",
   "hierarchyName": "default"
  },
  {
   "id": "PCycle",
   "hierarchyName": "H1"
  },
  {
   "id": "Lock",
   "hierarchyName": "H1"
  },
  {
   "id": "Ln",
   "hierarchyName": "H1"
  }
 ],
 "iterations": 1,
 "disabled": true,
 "sourceDimensions": [
  {
   "id": "GL",
   "hierarchyName": "H1"
  }
 ],
 "driverDimensions": [
  {
   "id": "CustomDimension1",
   "hierarchyName": null
  }
 ],
 "targetDimensions": [
  {
   "id": "GL",
   "hierarchyName": "H1"
  }
 ],
 "allocationRules": [
  {
   "source": [
    {
     "memberId": "#"
    }
   ],
   "driver": [
    {
     "memberId": "WorkSplitAllocation"
    }
   ],
   "target": [
    {
     "memberIds": [
      "CALC_05",
      "CALC_10"
     ]
    }
   ]
  }
 ],
 "targetBookingAccount": {
  "memberId": null,
  "hierarchyName": null
 }
}
```

</details>

### 7. Copy Allocationto Expense GL Line Item — COPY

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
    "Source",
    "Source_FC"
   ],
   "hierarchyName": null
  },
  "Date": {
   "memberIds": [
    {
     "paramRef": "DateSelection"
    }
   ],
   "hierarchyName": "YM"
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Ln": {
   "memberIds": [
    "EX_PA"
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
  "Grade": {
   "memberIds": [
    {
     "paramRef": "GradeSelection"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_Currency": {
   "memberIds": [
    "NGN"
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "aggregatedDimensions": {},
 "copyRules": [
  {
   "dimensionId": "Ln",
   "source": {
    "hierarchyName": "H1",
    "memberId": "EX_PA"
   },
   "target": {
    "hierarchyName": "H1",
    "memberIds": [
     "EX_GL"
    ]
   }
  }
 ],
 "writeMode": "OVERWRITE",
 "disabled": true,
 "copyFactor": "1"
}
```

</details>

### 8. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:14613E84BFC42E89137EA36E5D8B1E33",
 "parameterValues": [
  {
   "id": {
    "displayKey": "TargetVersion"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "TargetVersion"
   }
  },
  {
   "id": {
    "displayKey": "DateSelection"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "DateSelection"
   }
  },
  {
   "id": {
    "displayKey": "GradeSelection"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "GradeSelection"
   }
  },
  {
   "id": {
    "displayKey": "EntitySelection"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "EntitySelection"
   }
  },
  {
   "id": {
    "displayKey": "CurrentFY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "ReportingDate"
   }
  }
 ]
}
```

</details>

### 9. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:92A13E84BFC61D8B3076C1154DA09AE0",
 "parameterValues": [
  {
   "id": {
    "displayKey": "TargetVersion"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "TargetVersion"
   }
  },
  {
   "id": {
    "displayKey": "DateSelection"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "DateSelection"
   }
  },
  {
   "id": {
    "displayKey": "EntitySelection"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "EntitySelection"
   }
  },
  {
   "id": {
    "displayKey": "CurrentYr"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "ReportingDate"
   }
  }
 ]
}
```

</details>

### 10. Calculate_ITF/NSITF Contribution — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/GL] = "5060006"
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
MEMBERSET [d/PPP_Entity] = %Entity%
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/CostElement] = "CE06001"

DELETE()
```

Parameters used: CY, Entity

### 11. Calculate_ITF/NSITF Contribution — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("Source")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL].[h/H1], "CALC_05", "CALC_10", "MI_05", "MI_10"))
MEMBERSET [d/PPP_Currency] = BASEMEMBER([d/PPP_Currency] , "Total")
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/PPP_Entity] = %Entity%
MEMBERSET [d/Ln] = ("EX_GL","EX_GL_MN")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], "Total"), BASEMEMBER([d/Grade].[h/H1], "RS_05"))

VARIABLEMEMBER #TOTAL OF [d/GL]
VARIABLEMEMBER #QTY OF [d/GL]

DATA([d/Measures] = "Qty", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Date] = "000000", [d/GL] = #QTY, [d/Grade] = "#", [d/Ln] = "#", [d/Lock] = "#") = 
	RESULTLOOKUP([d/Measures] = "Qty", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Date] = "000000", [d/GL] = "#", [d/Grade] = "#", [d/Ln] = "PR_025", [d/Lock] = "#" /*!  ITF  */) + 
	RESULTLOOKUP([d/Measures] = "Qty", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Date] = "000000", [d/GL] = "#", [d/Grade] = "#", [d/Ln] = "PR_030", [d/Lock] = "#" /*!  NSITF  */)
	
DATA([d/GL] = #TOTAL, [d/Ln] = "EX_GL", [d/CostElement] = "CE06001") = 0
DATA.APPEND([d/GL] = #TOTAL, [d/Ln] = "EX_GL", [d/CostElement] = "CE06001") = RESULTLOOKUP()

DATA([d/GL] = "5060006", [d/Ln] = "EX_GL", [d/CostElement] = "CE06001") = 
	RESULTLOOKUP([d/Measures] = "Qty", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Date] = "000000", [d/GL] = #QTY, [d/Grade] = "#", [d/Ln] = "#", [d/Lock] = "#") / 100 *
	RESULTLOOKUP([d/GL] = #TOTAL, [d/Ln] = "EX_GL", [d/CostElement] = "CE06001")
```

Parameters used: Entity
