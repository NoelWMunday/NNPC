# CAPEX FIN Posting

| | |
|---|---|
| SAC id | `9238988E2A33A777B2833072DC4491DA` |
| Default model | PPP Financial |
| Created by | DPARUMAUL |
| Last changed | 2026-07-13T14:04:41.249Z by DPARUMAUL |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": "H1"}` |
| `PCycle` | PROMPT | MEMBER | Plan_Cycle | SINGLE | `"2026-2030/01"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | CAPEX Fin Posting | CROSSMODELCOPY | from CAPEX |
| 2 | CAPEX Contra Entry | CROSSMODELCOPY | from CAPEX |

### 1. CAPEX Fin Posting — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cbifmh01bklfvf7ijs46d1ano3b",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  },
  "Plan_Cycle": {
   "memberIds": [
    {
     "paramRef": "PCycle"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
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
      "memberId": "AMT_GL_GC",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR",
       "DR_GC"
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
  "PPP_Account": {
   "sourceDimensionId": "GL",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "defaultMember": {
    "memberId": "Capex",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PCycle": {
   "sourceDimensionId": "Plan_Cycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  }
 }
}
```

</details>

### 2. CAPEX Contra Entry — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cbifmh01bklfvf7ijs46d1ano3b",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  },
  "Plan_Cycle": {
   "memberIds": [
    {
     "paramRef": "PCycle"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
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
      "memberId": "AMT_GL_GC",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR",
       "CR_GC"
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
   "defaultMember": {
    "memberId": "Capex",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PCycle": {
   "sourceDimensionId": "Plan_Cycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "LIABILITIES",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>
