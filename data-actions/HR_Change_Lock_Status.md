# HR_Change_Lock_Status

> HR - Change Lock Status

| | |
|---|---|
| SAC id | `48526E84BFC18EDD13272260B0B1AF41` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-07-25T18:39:53.282Z by GLORD |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `GradeSelection` | PROMPT | MEMBER | Grade | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `PlanningCycle` | PROMPT | MEMBER | PCycle | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ForecastPeriod` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `Source_Lock` | PROMPT | MEMBER | Lock | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Target_Lock` | PROMPT | MEMBER | Lock | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `CurrencySelection` | PROMPT | MEMBER | PPP_Currency | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `GLSelection` | PROMPT | MEMBER | GL | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `MeasureSelection` | PROMPT | MEMBER | CustomDimension1 | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `CostElement` | PROMPT | MEMBER | CostElement | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `LineItem` | PROMPT | MEMBER | Ln | MULTI | `{"memberIds": [], "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Move to new lock status | COPY |  |
| 2 | Delete Old Status | DELETE_FACTS | **DISABLED** |

### 1. Move to new lock status — COPY

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
    {
     "paramRef": "MeasureSelection"
    }
   ],
   "hierarchyName": null
  },
  "CostElement": {
   "memberIds": [
    {
     "paramRef": "CostElement"
    }
   ],
   "hierarchyName": "default"
  },
  "PPP_Currency": {
   "memberIds": [
    {
     "paramRef": "CurrencySelection"
    }
   ],
   "hierarchyName": "H1"
  },
  "Date": {
   "memberIds": [
    {
     "paramRef": "DateSelection"
    }
   ],
   "hierarchyName": "YM"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "EntitySelection"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    {
     "paramRef": "GLSelection"
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
  "Ln": {
   "memberIds": [
    {
     "paramRef": "LineItem"
    }
   ],
   "hierarchyName": "H1"
  },
  "PCycle": {
   "memberIds": [
    {
     "paramRef": "PlanningCycle"
    }
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "aggregatedDimensions": {},
 "copyRules": [
  {
   "dimensionId": "Lock",
   "source": {
    "hierarchyName": "H1",
    "memberId": {
     "paramRef": "Source_Lock"
    }
   },
   "target": {
    "hierarchyName": "H1",
    "memberIds": [
     {
      "paramRef": "Target_Lock"
     }
    ]
   }
  }
 ],
 "writeMode": "OVERWRITE",
 "copyFactor": "1"
}
```

</details>

### 2. Delete Old Status — DELETE_FACTS

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
    {
     "paramRef": "MeasureSelection"
    }
   ],
   "hierarchyName": null
  },
  "CostElement": {
   "memberIds": [
    {
     "paramRef": "CostElement"
    }
   ],
   "hierarchyName": "default"
  },
  "PPP_Currency": {
   "memberIds": [
    {
     "paramRef": "CurrencySelection"
    }
   ],
   "hierarchyName": "H1"
  },
  "Date": {
   "memberIds": [
    {
     "paramRef": "DateSelection"
    }
   ],
   "hierarchyName": "YM"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "EntitySelection"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    {
     "paramRef": "GLSelection"
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
  "Ln": {
   "memberIds": [
    {
     "paramRef": "LineItem"
    }
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    {
     "paramRef": "Source_Lock"
    }
   ],
   "hierarchyName": "H1"
  },
  "PCycle": {
   "memberIds": [
    {
     "paramRef": "PlanningCycle"
    }
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "deleteMode": "DELETE",
 "disabled": true
}
```

</details>
