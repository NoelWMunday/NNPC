# HR_Calculate_Expense_Currency_Conversion_CalcFields

| | |
|---|---|
| SAC id | `DA232E84BFC6B8B952F047BACECBBD72` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-08-13T13:26:34.052Z by NMUNDAY |
| Called by | [HR_Calculate_All](HR_Calculate_All.md) |
| Used in stories | [PPP_HR](../stories/PPP_HR.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `DateSelection` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `PlanningCycle` | PROMPT | MEMBER | PCycle | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `EntitySelection` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `ForecastPeriod` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `LIneItem` | PROMPT | MEMBER | Ln | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `GL_Selection` | PROMPT | MEMBER | GL | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `SourceCurrency` | PROMPT | MEMBER | PPP_Currency | MULTI | `{"memberIds": [], "hierarchyName": "H1"}` |
| `TargetMeasure` | PROMPT | MEMBER | CustomDimension1 | SINGLE | `"GC"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | CONVERSION |  |
| 2 | (unnamed) | COPY |  |
| 3 | Delete | DELETE_FACTS |  |

### 1. (unnamed) — CONVERSION

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
  "GL": {
   "memberIds": [
    {
     "paramRef": "GL_Selection"
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
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Ln": {
   "memberIds": [
    {
     "paramRef": "LIneItem"
    }
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
  "PPP_Currency": {
   "memberIds": [
    "Total"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "conversionRules": [
  {
   "source": {
    "hierarchyName": null,
    "memberId": "Source"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "GC_TOT"
   },
   "fixedDate": null,
   "delta": {
    "granularity": "MONTH",
    "shift": 0
   },
   "category": "DYNAMIC",
   "rateVersion": null
  }
 ],
 "writeMode": "OVERWRITE"
}
```

</details>

### 2. (unnamed) — COPY

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
    "GC_TOT"
   ],
   "hierarchyName": null
  },
  "PPP_Currency": {
   "memberIds": [
    "NGN"
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
  "Grade": {
   "memberIds": [
    "Total",
    "RS_05"
   ],
   "hierarchyName": "H1"
  },
  "Ln": {
   "memberIds": [
    {
     "paramRef": "LIneItem"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    {
     "paramRef": "GL_Selection"
    }
   ],
   "hierarchyName": "H1"
  },
  "PCycle": {
   "memberIds": [
    "#"
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
   "dimensionId": "PPP_Currency",
   "source": {
    "hierarchyName": "H1",
    "memberId": "NGN"
   },
   "target": {
    "hierarchyName": "H1",
    "memberIds": [
     "USD"
    ]
   }
  }
 ],
 "writeMode": "APPEND",
 "copyFactor": "1"
}
```

</details>

### 3. Delete — DELETE_FACTS

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
    "GC_TOT"
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
  "PPP_Currency": {
   "memberIds": [
    "NGN"
   ],
   "hierarchyName": "H1"
  },
  "Ln": {
   "memberIds": [
    {
     "paramRef": "LIneItem"
    }
   ],
   "hierarchyName": "H1"
  },
  "Grade": {
   "memberIds": [
    "Total",
    "RS_05"
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
  "GL": {
   "memberIds": [
    {
     "paramRef": "GL_Selection"
    }
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "deleteMode": "DELETE",
 "disabled": false
}
```

</details>
