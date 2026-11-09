# HR_Calculate_Expense_Health_Contribution

> HR Health Contribution Expense

| | |
|---|---|
| SAC id | `92A13E84BFC61D8B3076C1154DA09AE0` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-08-13T09:47:43.103Z by NMUNDAY |
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
| `CurrentYr` | PROMPT | MEMBER | Date | MULTI | `[["(all)", "2027"]]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Health_Calc_NNPC | NESTED_SEQUENCE | runs [HR_Tool_Headcount_Times_Parameter](HR_Tool_Headcount_Times_Parameter.md) |
| 2 | Health_Calc_NRL | NESTED_SEQUENCE | runs [HR_Tool_Headcount_Times_Parameter](HR_Tool_Headcount_Times_Parameter.md) |

### 1. Health_Calc_NNPC — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:51F92684BFC2040AC5693C7FA2225918",
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
    "memberIds": [
     "Total"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "TargetGL"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "5020001"
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
     "PR_005"
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
     "PR_010"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "CurrencySelection"
   },
   "useDefaultValue": true,
   "value": null
  },
  {
   "id": {
    "displayKey": "MeasureSelectionCY"
   },
   "useDefaultValue": true,
   "value": null
  },
  {
   "id": {
    "displayKey": "CurrentYr"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentYr"
   }
  }
 ]
}
```

</details>

### 2. Health_Calc_NRL — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:51F92684BFC2040AC5693C7FA2225918",
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
    "memberIds": [
     "NRL 2a",
     "NRL 2b",
     "NRL 3a",
     "NRL 3b",
     "NRL 4a",
     "NRL 4b",
     "NRL 5a",
     "NRL 5b",
     "NRL 6a",
     "NRL 6b",
     "NRL 7a",
     "NRL 7b",
     "NRL 8a",
     "NRL 8b",
     "NRL 9a"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "TargetGL"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "5020002"
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
     "PR_040"
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
     "PR_010"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "CurrencySelection"
   },
   "useDefaultValue": true,
   "value": null
  },
  {
   "id": {
    "displayKey": "MeasureSelectionCY"
   },
   "useDefaultValue": true,
   "value": null
  },
  {
   "id": {
    "displayKey": "CurrentYr"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentYr"
   }
  }
 ]
}
```

</details>
