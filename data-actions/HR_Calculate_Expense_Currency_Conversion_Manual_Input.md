# HR_Calculate_Expense_Currency_Conversion_Manual_Input

| | |
|---|---|
| SAC id | `AA938684BFC021D16BD4866B08F5A145` |
| Default model | PPP Workforce planning |
| Created by | GLORD |
| Last changed | 2026-07-29T06:44:10.763Z by NMUNDAY |
| Called by | — |
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
| 2 | (unnamed) | SCRIPT |  |

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
    {
     "paramRef": "PlanningCycle"
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
    {
     "paramRef": "SourceCurrency"
    }
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
    "memberId": "GC"
   },
   "fixedDate": null,
   "delta": {
    "granularity": "MONTH",
    "shift": 0
   },
   "category": "DYNAMIC",
   "rateVersion": null
  },
  {
   "source": {
    "hierarchyName": null,
    "memberId": "Source_FC"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "GC"
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

### 2. (unnamed) — SCRIPT

```
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %DateSelection%))
MEMBERSET [d/PPP_Entity] = (BASEMEMBER([d/PPP_Entity].[h/H1], %EntitySelection%))
MEMBERSET [d/GL] = (BASEMEMBER([d/GL].[h/H1], %GL_Selection%))
MEMBERSET [d/Ln] = (BASEMEMBER([d/Ln].[h/H1], %LIneItem%))
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PCycle] = (BASEMEMBER([d/PCycle].[h/H1], %PlanningCycle%))

FOREACH [d/Date].[p/YEAR]
//	IF [d/Date].[p/YEAR] = [d/PCycle].[p/Current_Year] THEN
		DATA([d/Measures] = "GC_TOT", [d/PPP_Currency] = "USD", [d/Date] = LAST()) = RESULTLOOKUP([d/Measures] = "GC")
//	ENDIF
ENDFOR
```

Parameters used: DateSelection, EntitySelection, GL_Selection, LIneItem, PlanningCycle
