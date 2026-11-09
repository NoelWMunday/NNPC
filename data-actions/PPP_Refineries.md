# PPP_Refineries

| | |
|---|---|
| SAC id | `EBBB20862A31E79D22EC6D0B72831DAA` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-26T08:38:46.136Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md), [PPP_Refinerie](../stories/PPP_Refinerie.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Read central parameters 01 | SCRIPT |  |
| 3 | Read central parameters 02 | SCRIPT |  |
| 4 | Crude intake in Bbl | SCRIPT |  |
| 5 | Volume MT | SCRIPT |  |
| 6 | Sales Volume & F'USD | SCRIPT |  |
| 7 | Sales Volume & F'USD Crude oil | SCRIPT |  |
| 8 | Sales Volume & F'USD Crude oil | SCRIPT |  |
| 9 | (unnamed) | NESTED_SEQUENCE | runs [PPP_Refinerie_GL_Postings](PPP_Refinerie_GL_Postings.md) |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("Vol_MT","Vol_Annual_Products","AMT_Rev","AMT_COGS","DCapacity","CF01","CF02","CIT01","CIT02","AMT_Rev_GC","AMT_COGS_GC")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/Lock] = "#"

DELETE()
```

Parameters used: Entity

### 2. Read central parameters 01 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("DCapacity")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_Currency] = "#"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/ProductServ] = "Operational parameters"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

IF RESULTLOOKUP([d/Measures] = "CUtil") > 0 THEN
	DATA([d/Lock]="#") = RESULTLOOKUP([d/Lock]="Central", [d/Date] = "000000")
ENDIF
```

Parameters used: Entity

### 3. Read central parameters 02 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("CF01","CF02")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_Currency] = "#"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

IF RESULTLOOKUP([d/Measures] = "CUtil", [d/ProductServ] = "Operational parameters") > 0 THEN
	DATA([d/Lock]="#") = RESULTLOOKUP([d/Lock]="Central", [d/PPP_Entity] = "#", [d/Date] = "000000")
ENDIF
```

Parameters used: Entity

### 4. Crude intake in Bbl — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("CIT01","CIT02")
MEMBERSET [d/ProductServ] = "Operational parameters"
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_Currency] = "#"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

// Crude intake ... per barrel and per MT
DATA([d/Measures]="CIT01") = RESULTLOOKUP([d/Measures]="DCapacity") * RESULTLOOKUP([d/Measures]="CUtil") * RESULTLOOKUP([d/Measures]="OSDays")
DATA([d/Measures]="CIT02") = RESULTLOOKUP([d/Measures]="CIT01") / RESULTLOOKUP([d/Measures]="CF01")
```

Parameters used: Entity

### 5. Volume MT — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("Vol_MT")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_Currency] = "#"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

DATA([d/Measures]="Vol_MT") = 
	RESULTLOOKUP([d/Measures]="CIT02", [d/ProductServ] = "Operational parameters") * 
	RESULTLOOKUP([d/Measures]="YPattern")
```

Parameters used: Entity

### 6. Sales Volume & F'USD — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("Vol_Annual_Products","AMT_Rev","AMT_COGS")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/ProductServ] != ("Crude Oil","Crude Pipeline Tariff","LPG")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

DATA([d/Measures]="Vol_Annual_Products",[d/PPP_Currency]="NGN") = 
	RESULTLOOKUP([d/Measures]="Vol_MT",[d/PPP_Currency]="#") * 
	RESULTLOOKUP([d/Measures]="CF02",[d/PPP_Currency]="#")
	
DATA([d/Measures]="AMT_Rev") = 
	RESULTLOOKUP([d/Measures]="Vol_Annual_Products") * 
	RESULTLOOKUP([d/Measures]="Price")
	
DATA([d/Measures]="AMT_COGS") = 
	RESULTLOOKUP([d/Measures]="Vol_Annual_Products") * 
	RESULTLOOKUP([d/Measures]="COS")
```

Parameters used: Entity

### 7. Sales Volume & F'USD Crude oil — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("Vol_Annual_Products","AMT_Rev","AMT_COGS")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/ProductServ] = ("Crude Oil","Crude Pipeline Tariff")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

DATA([d/Measures]="Vol_Annual_Products",[d/PPP_Currency]="USD") = RESULTLOOKUP([d/Measures]="CIT01",[d/ProductServ]="Operational parameters",[d/PPP_Currency]="#")
DATA([d/Measures]="AMT_Rev") = RESULTLOOKUP([d/Measures]="Vol_Annual_Products") * RESULTLOOKUP([d/Measures]="Price")
DATA([d/Measures]="AMT_COGS") = RESULTLOOKUP([d/Measures]="Vol_Annual_Products") * RESULTLOOKUP([d/Measures]="COS")
```

Parameters used: Entity

### 8. Sales Volume & F'USD Crude oil — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("Vol_Annual_Products","AMT_Rev","AMT_COGS")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/ProductServ] = "LPG"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

DATA([d/Measures]="Vol_Annual_Products",[d/PPP_Currency]="NGN") = RESULTLOOKUP([d/Measures]="Vol_MT",[d/PPP_Currency]="#")
DATA([d/Measures]="AMT_Rev") = RESULTLOOKUP([d/Measures]="Vol_Annual_Products") * RESULTLOOKUP([d/Measures]="Price")
DATA([d/Measures]="AMT_COGS") = RESULTLOOKUP([d/Measures]="Vol_Annual_Products") * RESULTLOOKUP([d/Measures]="COS")
```

Parameters used: Entity

### 9. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:C86E9E84BFC2396880E8708183529705",
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
    "displayKey": "Entity"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "Entity"
   }
  }
 ]
}
```

</details>
