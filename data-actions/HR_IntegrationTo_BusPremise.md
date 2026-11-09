# HR_IntegrationTo_BusPremise

> HR Integration to BusPremise

| | |
|---|---|
| SAC id | `7784FE84BFC1657AB21446094CCA17D3` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-10-06T10:49:49.900Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_Overheads](../stories/PPP_Overheads.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `Version_HR` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity_BP` | PROMPT | MEMBER | PPP_Entity | MULTI | `["#"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | DELETE_FACTS |  |
| 2 | HR to Business premise | CROSSMODELCOPY | from PPP Workforce planning |
| 3 | Rounding | SCRIPT |  |
| 4 | Delete tmp area | DELETE_FACTS |  |

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
    "GC_CLO_HR",
    "GC_CLO"
   ],
   "hierarchyName": null
  },
  "PPP_EntryNr": {
   "memberIds": [
    "HR"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity_BP"
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

### 2. HR to Business premise — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Crj0f13ha6urrkncndbh3nljj6t",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_HR"
   },
   "hierarchyName": null
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
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
  "GL": {
   "memberIds": [
    "HR",
    "TOTAL"
   ],
   "hierarchyName": "H1"
  },
  "CustomDimension1": {
   "memberIds": [
    "GC_TOT"
   ],
   "hierarchyName": null
  },
  "PPP_Currency": {
   "memberIds": [
    "USD"
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
      "memberId": "GC_TOT",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "GC_CLO_HR"
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
  "GL": {
   "sourceDimensionId": "GL",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "OTH_005",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "4900005"
      ],
      "hierarchyName": "H1"
     }
    },
    {
     "source": {
      "memberId": "OTH_015",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "4900001"
      ],
      "hierarchyName": "H1"
     }
    },
    {
     "source": {
      "memberId": "OTH_010",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "4900016"
      ],
      "hierarchyName": "H1"
     }
    },
    {
     "source": {
      "memberId": "OTH_020",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "4900007"
      ],
      "hierarchyName": "H1"
     }
    },
    {
     "source": {
      "memberId": "OTH_025",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "5010016"
      ],
      "hierarchyName": "H1"
     }
    },
    {
     "source": {
      "memberId": "OTH_030",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "4900010"
      ],
      "hierarchyName": "H1"
     }
    },
    {
     "source": {
      "memberId": "OTH_035",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "4700000"
      ],
      "hierarchyName": "H1"
     }
    },
    {
     "source": {
      "memberId": "OTH_040",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "4900006"
      ],
      "hierarchyName": "H1"
     }
    },
    {
     "source": {
      "memberId": "PEN_005",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "5010034"
      ],
      "hierarchyName": "H1"
     }
    }
   ]
  },
  "Lock": {
   "sourceDimensionId": "Lock",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "Objectives": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Ln": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_EntryNr": {
   "defaultMember": {
    "memberId": "HR_0005",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "ProductServ": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "WPLn": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PCycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Strategy": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "WorkProgram": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 3. Rounding — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity_BP%)
MEMBERSET [d/PPP_EntryNr] = BASEMEMBER([d/PPP_EntryNr] , "HR")

DATA([d/Measures]="GC_CLO") = round(RESULTLOOKUP([d/Measures]="GC_CLO_HR"),0)
```

Parameters used: Entity_BP

### 4. Delete tmp area — DELETE_FACTS

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
    "GC_CLO_HR"
   ],
   "hierarchyName": null
  },
  "PPP_EntryNr": {
   "memberIds": [
    "HR"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity_BP"
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
