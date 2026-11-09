# CAPEX2_PriceEscalation

| | |
|---|---|
| SAC id | `3190C0771E12D774F1FEC79CDE87340` |
| Default model | CAPEX |
| Created by | NMUNDAY |
| Last changed | 2026-10-06T16:01:49.295Z by NMUNDAY |
| Called by | [CAPEX2_Movables_All_Calculations](CAPEX2_Movables_All_Calculations.md) |
| Used in stories | [PPP_CAPEX](../stories/PPP_CAPEX.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Plan 2027-2031 iteration 01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": "H1"}` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |
| `Version_BP` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget 2026 (Reference)"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | CPI | CROSSMODELCOPY | from Business premise |
| 2 | Price escalation calculation | SCRIPT |  |

### 1. CPI — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_BP"
   },
   "hierarchyName": null
  },
  "CustomDimension1": {
   "memberIds": [
    "Value_WPLn"
   ],
   "hierarchyName": null
  },
  "PPP_EntryNr": {
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
  "GL": {
   "memberIds": [
    "#"
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
  "PPP_Currency": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "GA_ESC_03"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
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
       "M_Cost"
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
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceHierarchy": "H1"
   }
  },
  "Lock": {
   "sourceDimensionId": "Lock",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "Central",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "#"
      ],
      "hierarchyName": "H1"
     }
    }
   ]
  },
  "ProjectClass": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "End_Year": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "ImpStage": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "MovableItems": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Project": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": null
   },
   "sourceDimensionId": null
  },
  "Start_Year": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Project_Status": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Work_Program": {
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
  "Plan_Cycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "GL": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_Currency": {
   "defaultMember": {
    "memberId": "USD",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 2. Price escalation calculation — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/Measures] = ("U_Price")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/MovableItems] = BASEMEMBER([d/MovableItems] , "Total")
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSEt [d/GL] = ("#")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Project] = "#"
MEMBERSET [d/ImpStage] = "#"
MEMBERSET [d/ProjectClass] = "#"
MEMBERSET [d/Work_Program] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/Project_Status] = "#"
MEMBERSET [d/Start_Year] = "#"
MEMBERSET [d/End_Year] = "#"
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"


DATA([d/Date]=NEXT(2,"YEAR",%CY%)) =
	RESULTLOOKUP([d/Date]=NEXT(1,"YEAR",%CY%)) * (1 + (
	RESULTLOOKUP([d/Measures]="M_Cost",[d/Date]=NEXT(2,"YEAR",%CY%),[d/PPP_Entity]="#",[d/MovableItems]="#") / 100))

DATA([d/Date]=NEXT(3,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Date]=NEXT(2,"YEAR",%CY%)) * (1 + (
	RESULTLOOKUP([d/Measures]="M_Cost",[d/Date]=NEXT(3,"YEAR",%CY%),[d/PPP_Entity]="#",[d/MovableItems]="#") / 100))
	
DATA([d/Date]=NEXT(4,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Date]=NEXT(3,"YEAR",%CY%)) * (1 + (
	RESULTLOOKUP([d/Measures]="M_Cost",[d/Date]=NEXT(4,"YEAR",%CY%),[d/PPP_Entity]="#",[d/MovableItems]="#") / 100))
	
DATA([d/Date]=NEXT(5,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Date]=NEXT(4,"YEAR",%CY%)) * (1 + (
	RESULTLOOKUP([d/Measures]="M_Cost",[d/Date]=NEXT(5,"YEAR",%CY%),[d/PPP_Entity]="#",[d/MovableItems]="#") / 100))
```

Parameters used: Entity, CY
