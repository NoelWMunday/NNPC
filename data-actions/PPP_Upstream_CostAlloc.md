# PPP_Upstream_CostAlloc

| | |
|---|---|
| SAC id | `398D1684BFC6147FBA0CF82732D452F6` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-11-11T11:48:47.621Z by NMUNDAY |
| Called by | [PPP_Upstream_All_Calculations](PPP_Upstream_All_Calculations.md) |
| Used in stories | [PPP_UStream](../stories/PPP_UStream.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["NB04"]` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |
| `PCycle_CAPEX` | PROMPT | MEMBER | Plan_Cycle | SINGLE | `"2026-2030/01"` |
| `Version_CAPEX` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity_CAPEX` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Total costs to be apportioned - Overheads | SCRIPT |  |
| 3 | Total costs to be apportioned - Salaries | SCRIPT |  |
| 4 | Total costs to be apportioned - Depreciation | SCRIPT |  |
| 5 | Total costs to be apportioned - Impairments | SCRIPT |  |
| 6 | Total costs to be apportioned - CHOOCA | SCRIPT |  |
| 7 | Total costs to be apportioned - Finance cost | SCRIPT |  |
| 8 | Total costs to be apportioned - Tax | SCRIPT |  |
| 9 | Total costs from CAPEX model | CROSSMODELCOPY | from CAPEX |
| 10 | Total costs CAPEX from CPY to WP | SCRIPT |  |
| 11 | Cost apportionment | SCRIPT |  |
| 12 | GL Entries - Intialise | SCRIPT |  |
| 13 | GL Entries | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] ,"CST14")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"

DELETE()
```

Parameters used: Entity, PCycle

### 2. Total costs to be apportioned - Overheads — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_05","#")
MEMBERSET [d/GL] = ("#", BASEMEMBER([d/GL] , "GEN_ADMIN"))
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","BP002")


DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_05",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CR",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD",[d/PPP_EntryNr]="BP002")
```

Parameters used: Entity, PCycle

### 3. Total costs to be apportioned - Salaries — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_10","#")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL] , "HR"), "#")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","HR_0005")

IF [d/PPP_EntryNr] = "HR_0005" AND [d/GL] != "#" THEN
	DATA.APPEND([d/Measures]="Value_WPLn", [d/WPLn]="CST14_10", [d/GL]="#", [d/PPP_Currency]="#", [d/PPP_EntryNr]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO", [d/WPLn]="#", [d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup], [d/PPP_Currency]="USD", [d/PPP_EntryNr]="HR_0005")
ENDIF
```

Parameters used: Entity, PCycle

### 4. Total costs to be apportioned - Depreciation — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_15","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "DEPRECIATION")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","BP002")

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_15",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CR",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD",[d/PPP_EntryNr]="BP002")
```

Parameters used: Entity, PCycle

### 5. Total costs to be apportioned - Impairments — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_20","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "PROV_IMP")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","BP002")

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_20",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CR",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD",[d/PPP_EntryNr]="BP002")
```

Parameters used: Entity, PCycle

### 6. Total costs to be apportioned - CHOOCA — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_25","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "CHOOCA")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","BP002")

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_25",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CR",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD",[d/PPP_EntryNr]="BP002")
```

Parameters used: Entity, PCycle

### 7. Total costs to be apportioned - Finance cost — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_30","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "OTH_0005")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","BP002")


DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_30",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CR",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD",[d/PPP_EntryNr]="BP002")
```

Parameters used: Entity, PCycle

### 8. Total costs to be apportioned - Tax — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_35","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "TAX_HIST")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","BP002")

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_35",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CR",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD",[d/PPP_EntryNr]="BP002")
```

Parameters used: Entity, PCycle

### 9. Total costs from CAPEX model — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cbifmh01bklfvf7ijs46d1ano3b",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_CAPEX"
   },
   "hierarchyName": null
  },
  "Plan_Cycle": {
   "memberIds": [
    {
     "paramRef": "PCycle_CAPEX"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity_CAPEX"
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
      "memberId": "YTD_GC",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "Value_WPLn"
      ],
      "hierarchyName": null
     }
    },
    {
     "source": {
      "memberId": "PC_YTD",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "Value_WPLn"
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
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "USD",
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
  "PPP_EntryNr": {
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
  "Ln": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Lock": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Objectives": {
   "defaultMember": {
    "memberId": "#",
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
    "memberId": "CST14_40",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "Plan_Cycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
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

### 10. Total costs CAPEX from CPY to WP — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// The CAPEX model to model copy will copy the capex spend per month to the same
// entity in BUSPREMISE e.g. NU03. This effectively provides the totals in NU03
// that otherwise would be in NU03 under CAPEX dimension members.
// Those totals will be persisted on CST14_40
// This function now lets the WP (Work Program) being planned read it from the main entity
// using the work program entity's property which points to the main entity

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn")
MEMBERSET [d/WPLn] = ("CST14_40")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA() = RESULTLOOKUP([d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup])
```

Parameters used: Entity, PCycle

### 11. Cost apportionment — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"

DATA([d/WPLn]="CST15_05") = RESULTLOOKUP([d/WPLn]="CST14_05") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_10") = RESULTLOOKUP([d/WPLn]="CST14_10") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_15") = RESULTLOOKUP([d/WPLn]="CST14_15") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_20") = RESULTLOOKUP([d/WPLn]="CST14_20") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_25") = RESULTLOOKUP([d/WPLn]="CST14_25") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_30") = RESULTLOOKUP([d/WPLn]="CST14_30") * RESULTLOOKUP([d/WPLn]="REV3_10_05")
DATA([d/WPLn]="CST15_35") = RESULTLOOKUP([d/WPLn]="CST14_35") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_40") = RESULTLOOKUP([d/WPLn]="CST14_40") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
```

Parameters used: Entity, PCycle

### 12. GL Entries - Intialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = "GC_CR"
MEMBERSET [d/WPLn] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = BASEMEMBER([d/PPP_EntryNr] ,"UP")
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/GL] = ("5010036","5010001","4112001","5230006","5080044","FINEXP_005","5100005")

DATA() = 0
```

Parameters used: Entity, PCycle

### 13. GL Entries — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CR")
// MEMBERSET [d/WPLn] = ("CST20", "SET10_05")
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#")
MEMBERSET [d/PPP_Currency] = "USD"


// Apportioned Overheads
DATA([d/Measures] = "GC_CR", [d/GL] = "5010036", [d/PPP_EntryNr] = "UP_0010") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned Salaries
DATA([d/Measures] = "GC_CR", [d/GL] = "5010001", [d/PPP_EntryNr] = "UP_0010") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned General Depreciation
DATA([d/Measures] = "GC_CR", [d/GL] = "4112001", [d/PPP_EntryNr] = "UP_0010") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_15", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned Provision for Impairment
DATA([d/Measures] = "GC_CR", [d/GL] = "5230006", [d/PPP_EntryNr] = "UP_0010") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_20", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned Corporate Overhead
DATA([d/Measures] = "GC_CR", [d/GL] = "5080044", [d/PPP_EntryNr] = "UP_0010") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_25", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned Finance Cost
DATA([d/Measures] = "GC_CR", [d/GL] = "FINEXP_005", [d/PPP_EntryNr] = "UP_0010") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_30", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned Taxes
DATA([d/Measures] = "GC_CR", [d/GL] = "5100005", [d/PPP_EntryNr] = "UP_0010") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_35", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Internal capex
//DATA([d/Measures] = "GC_CR", [d/GL] = "4112002", [d/PPP_EntryNr] = "UP_0010") = 
//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_40", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
```

Parameters used: Entity, PCycle
