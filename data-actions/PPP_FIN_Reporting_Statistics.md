# PPP_FIN_Reporting_Statistics

| | |
|---|---|
| SAC id | `E4E0D68CBFC4433BC39632393EB16CA6` |
| Default model | PPP Financial |
| Created by | GLORD |
| Last changed | 2026-08-11T15:07:26.576Z by GLORD |
| Called by | — |
| Used in stories | [PPP_Financial_Test](../stories/PPP_Financial_Test.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `SourceVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `SourceDate` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `TargetDate` | PROMPT | MEMBER | Date | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `SourcePlanningCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"#"` |
| `TargetPlanningCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"#"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Oil Price | CROSSMODELCOPY | from Business premise |
| 2 | (unnamed) | SCRIPT |  |
| 3 | (unnamed) | CONVERSION |  |

### 1. Oil Price — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "SourceVersion"
   },
   "hierarchyName": null
  },
  "PPP_Currency": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Strategy": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": null
  },
  "PPP_EntryNr": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Ln": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    "Central"
   ],
   "hierarchyName": "H1"
  },
  "ProductServ": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WorkProgram": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": null
  },
  "Objectives": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "GA_015"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "CustomDimension1": {
   "memberIds": [
    "Value_WPLn"
   ],
   "hierarchyName": null
  },
  "Date": {
   "memberIds": [
    {
     "paramRef": "SourceDate"
    }
   ],
   "hierarchyName": "YM"
  },
  "PCycle": {
   "memberIds": [
    {
     "paramRef": "SourcePlanningCycle"
    }
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "Value_WPLn",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "RPT_METRCS"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "PCycle",
   "autoMappingStrategy": "NONE",
   "completionMode": "DEFAULT",
   "completionDefaultMember": {
    "memberId": {
     "paramRef": "TargetPlanningCycle"
    },
    "hierarchyName": "H1"
   },
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "CRUDE_OIL_PRICE",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 2. (unnamed) — SCRIPT

```
MEMBERSET [d/Measures] = ("RPT_GC")
MEMBERSET [d/PPP_Currency] = ("USD")
MEMBERSET [d/PPP_Account] = ("EXCHANGE_RATE_DOLLAR_N")
MEMBERSET [d/PCycle] = (%TargetPlanningCycle%)
MEMBERSET [d/PPP_Entity] = ("#")
MEMBERSET [d/PPP_EntryNr] = ("#")
MEMBERSET [d/Date] = (BASEMEMBER([d/Date].[h/YM], %TargetDate%))
DATA() = 1
```

Parameters used: TargetPlanningCycle, TargetDate

### 3. (unnamed) — CONVERSION

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
  "Date": {
   "memberIds": [
    {
     "paramRef": "TargetDate"
    }
   ],
   "hierarchyName": "YQM"
  },
  "PPP_Account": {
   "memberIds": [
    "EXCHANGE_RATE_DOLLAR_N"
   ],
   "hierarchyName": "parentId"
  },
  "PPP_Currency": {
   "memberIds": [
    "USD"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PCycle": {
   "memberIds": [
    {
     "paramRef": "TargetPlanningCycle"
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
    "memberId": "RPT_GC"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "RPT_CUR_N"
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
