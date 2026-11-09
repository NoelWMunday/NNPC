# HR_Calculate_Expense_Pension_Conribution

> HR Pension Contribution Calculation

| | |
|---|---|
| SAC id | `14613E84BFC42E89137EA36E5D8B1E33` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-08-14T15:25:43.710Z by NMUNDAY |
| Called by | [HR_Calculate_Salaries_Cost](HR_Calculate_Salaries_Cost.md) |
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
| `CurrentFY` | PROMPT | MEMBER | Date | MULTI | `[["(all)", "2027"]]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | NESTED_SEQUENCE | runs [HR_Tool_Headcount_Times_Parameter_Amount](HR_Tool_Headcount_Times_Parameter_Amount.md) |

### 1. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:B9214684BFC7480EA13D2A8B55B880DA",
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
    "displayKey": "TargetGrade"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "GradeSelection"
   }
  },
  {
   "id": {
    "displayKey": "TargetGL"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "5010034"
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
    "paramRef": "EntitySelection"
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
    "displayKey": "Parameter"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "CE04001"
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
    "displayKey": "TargetMeasureSelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "Source"
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
    "hierarchyName": "default"
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
    "displayKey": "CurrentFY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentFY"
   }
  }
 ]
}
```

</details>
