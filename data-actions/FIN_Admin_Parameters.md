# FIN_Admin_Parameters

> FIN - Copy Admin parameters from BusPremise

| | |
|---|---|
| SAC id | `C1A1BC0771E5A68F187AB32B09251E73` |
| Default model | PPP Financial |
| Created by | NMUNDAY |
| Last changed | 2026-10-08T13:55:13.459Z by NMUNDAY |
| Called by | [PPP_GLPost_BusPremise](PPP_GLPost_BusPremise.md) |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["#"]` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |
| `Version_BusPremise` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget 2026 (Reference)"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Step 01 | CROSSMODELCOPY | from Business premise |
| 2 | Step 02 | SCRIPT |  |
| 3 | Step 03 | SCRIPT |  |
| 4 | Step 04 | SCRIPT |  |

### 1. Step 01 — CROSSMODELCOPY

Copy BusPremise assumptions into FIN

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_BusPremise"
   },
   "hierarchyName": null
  },
  "CustomDimension1": {
   "memberIds": [
    "Value_WPLn"
   ],
   "hierarchyName": null
  },
  "PPP_Currency": {
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
  "Objectives": {
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
  "ProductServ": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Strategy": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WorkProgram": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "GA_ESC_05",
    "GA_ESC_10",
    "GA_ESC_15",
    "GA_055",
    "GA_050",
    "GA_CITA_05",
    "GA_CITA_10",
    "GA_CITA_15",
    "GA_CITA_20"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "IDENTICAL_NAMES_COMPATIBLE_TYPES",
   "completionMode": "MANUAL",
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
  "PPP_Account": {
   "sourceDimensionId": "WPLn",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GA_ESC_05",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_Check_limit_OH"
      ],
      "hierarchyName": "parentId"
     }
    },
    {
     "source": {
      "memberId": "GA_ESC_10",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_Check_limit_Moveables"
      ],
      "hierarchyName": "parentId"
     }
    },
    {
     "source": {
      "memberId": "GA_ESC_15",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_Check_limit_Capex"
      ],
      "hierarchyName": "parentId"
     }
    },
    {
     "source": {
      "memberId": "GA_055",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_02_01"
      ],
      "hierarchyName": "parentId"
     }
    },
    {
     "source": {
      "memberId": "GA_050",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_02_02"
      ],
      "hierarchyName": "parentId"
     }
    },
    {
     "source": {
      "memberId": "GA_CITA_05",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_03_01"
      ],
      "hierarchyName": "parentId"
     }
    },
    {
     "source": {
      "memberId": "GA_CITA_10",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_03_02"
      ],
      "hierarchyName": "parentId"
     }
    },
    {
     "source": {
      "memberId": "GA_CITA_15",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_03_03"
      ],
      "hierarchyName": "parentId"
     }
    },
    {
     "source": {
      "memberId": "GA_CITA_20",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "FIN06_03_04"
      ],
      "hierarchyName": "parentId"
     }
    }
   ]
  },
  "PCycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_Currency": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_EntryNr": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
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
  "PPP_Entity": {
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

### 2. Step 02 — SCRIPT

Copy expense limit parameter to entity from central settings

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("FIN06_Check_limit_OH", "FIN06_Check_limit_Moveables","FIN06_Check_limit_Capex")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = ("#","USD")
MEMBERSET [d/PPP_EntryNr] = ("#","1001")
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/Measures] = ("RPT_YOY","RPT_METRCS")

DATA([d/Measures]="RPT_YOY",[d/PPP_Currency]="USD",[d/PPP_EntryNr]="1001") = 
	ROUND(RESULTLOOKUP([d/Measures]="RPT_METRCS",[d/PPP_Entity] = "#",[d/PPP_EntryNr]="#",[d/PPP_Currency]="#") / 100, 2)
```

Parameters used: Entity

### 3. Step 03 — SCRIPT

Delete assumptions prior to CY+1

```
// Deleting these periods ensures no calculation is performed for them in the next step

CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("FIN06_02_01","FIN06_02_02")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = ("USD")
MEMBERSET [d/PPP_EntryNr] = ("1001")
MEMBERSET [d/Date] = PREVIOUS(3,"YEAR",%CY%) TO %CY%
MEMBERSET [d/Measures] = ("CLO_GC")

DELETE()
```

Parameters used: Entity, CY

### 4. Step 04 — SCRIPT

Move assumptions from central area to entity from CY+1 onward

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("FIN06_02_01","FIN06_02_02")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = ("#","USD")
MEMBERSET [d/PPP_EntryNr] = ("#","1001")
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)
MEMBERSET [d/Measures] = ("CLO_GC","RPT_METRCS")

DATA([d/Measures]="CLO_GC",[d/PPP_Currency]="USD",[d/PPP_EntryNr]="1001") =
		RESULTLOOKUP([d/Measures]="RPT_METRCS",[d/PPP_Entity] = "#",[d/PPP_EntryNr]="#",[d/PPP_Currency]="#")
```

Parameters used: Entity, CY
