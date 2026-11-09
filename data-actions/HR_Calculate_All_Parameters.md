# HR_Calculate_All_Parameters

| | |
|---|---|
| SAC id | `896A3C0771E22997F7E74FCF84B78D9B` |
| Default model | PPP Workforce planning |
| Created by | NMUNDAY |
| Last changed | 2026-10-19T10:09:26.937Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_HR_Parameters](../stories/PPP_HR_Parameters.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `GradeSelection` | PROMPT | MEMBER | Grade | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `PlanningCycle` | PROMPT | MEMBER | PCycle | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ForecastPeriod` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `CY_Plus_1` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2026", "202612"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | NESTED_SEQUENCE | runs [HR_Calculate_Rates_Fuel](HR_Calculate_Rates_Fuel.md) |
| 2 | (unnamed) | NESTED_SEQUENCE | runs [HR_Tool_Calculate_Rate_From_Rate](HR_Tool_Calculate_Rate_From_Rate.md) |
| 3 | (unnamed) | NESTED_SEQUENCE | runs [HR_Calculate_Rates_Pension_Basis](HR_Calculate_Rates_Pension_Basis.md) |
| 4 | (unnamed) | NESTED_SEQUENCE | runs [HR_Tool_Calculate_Rate_From_Rate](HR_Tool_Calculate_Rate_From_Rate.md) |
| 5 | (unnamed) | NESTED_SEQUENCE | runs [HR_Tool_Fill_Forecast_Ref_Amounts](HR_Tool_Fill_Forecast_Ref_Amounts.md) |
| 6 | Calculate_ITF/NSITF Contribution | SCRIPT | **DISABLED** |

### 1. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:D81A5E84BFC73D898D5688B4BA0ABA79",
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
    "displayKey": "GradeSelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "M2",
     "M3",
     "M4",
     "M5",
     "M6"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "EntitySelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "N01_HCM"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "CY_plus_1"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CY_Plus_1"
   }
  }
 ]
}
```

</details>

### 2. (unnamed) — NESTED_SEQUENCE

Monetisation of Mangement housing

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:D2425684BFC281BD3A234BC217D66B5F",
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
    "displayKey": "GradeSelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "Total",
     "RS_05"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "PlanningCycle"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "HR"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "EntitySelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "N01_HCM"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "TargetLI"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "CE01306"
    ],
    "hierarchyName": "SCH"
   }
  },
  {
   "id": {
    "displayKey": "SourceLI"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "MB_005",
     "MB_007",
     "MB_010",
     "MB_015",
     "MB_020",
     "MB_025"
    ],
    "hierarchyName": "SCH"
   }
  }
 ]
}
```

</details>

### 3. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:DA913E84BFC7A56485947732A6652925",
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
    "memberIds": [
     [
      "(all)"
     ]
    ],
    "hierarchyName": "YM"
   }
  }
 ]
}
```

</details>

### 4. (unnamed) — NESTED_SEQUENCE

Annual bonus

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:D2425684BFC281BD3A234BC217D66B5F",
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
    "displayKey": "GradeSelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "Total",
     "RS_05"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "PlanningCycle"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "HR"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "EntitySelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "N01_HCM"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "TargetLI"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "CE01205"
    ],
    "hierarchyName": "SCH"
   }
  },
  {
   "id": {
    "displayKey": "SourceLI"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "CE01101"
    ],
    "hierarchyName": "SCH"
   }
  }
 ]
}
```

</details>

### 5. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:71D20684BFC2357B15D57C62C99840F3",
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
    "displayKey": "EntitySelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "N01_HCM"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "Parameter"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "SC"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "EscallationParam"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "PR_015"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "ParameterMeasureSelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "Rates"
    ],
    "hierarchyName": null
   }
  },
  {
   "id": {
    "displayKey": "ParameterCostElement"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "#"
    ],
    "hierarchyName": "CalcInputH"
   }
  },
  {
   "id": {
    "displayKey": "ParameterGrade"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "Total",
     "RS_05"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "ParameterCurrency"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "NGN"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "CurrentYear"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CY_Plus_1"
   }
  }
 ]
}
```

</details>

### 6. Calculate_ITF/NSITF Contribution — SCRIPT

```
MEMBERSET [d/Measures] = ("Source")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL].[h/H1], "CALC_05", "CALC_10", "MI_05", "MI_10"))
MEMBERSET [d/PPP_Currency] = BASEMEMBER([d/PPP_Currency] , "Total")
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/Ln] = ("EX_GL","EX_GL_MN")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Grade] = (BASEMEMBER([d/Grade].[h/H1], "Total"), BASEMEMBER([d/Grade].[h/H1], "RS_05"))

DATA([d/GL] = "5060006", [d/Ln] = "EX_GL", [d/CostElement] = "CE06001") = 
	((RESULTLOOKUP([d/Measures] = "Qty", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Date] = "000000", [d/GL] = "#", [d/Grade] = "#", [d/Ln] = "PR_025", [d/Lock] = "#" /*!  ITF  */) + 
	 RESULTLOOKUP([d/Measures] = "Qty", [d/CostElement] = "#", [d/PPP_Currency] = "#", [d/Date] = "000000", [d/GL] = "#", [d/Grade] = "#", [d/Ln] = "PR_030", [d/Lock] = "#" /*!  NSITF  */) ) / 100 ) * 
	 RESULTLOOKUP()
```

Parameters used: DateSelection, EntitySelection
