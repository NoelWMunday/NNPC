# PPP_PrdSrv_Historical

> Products and Services - Historical calcs

| | |
|---|---|
| SAC id | `DEBA26052294CB60CEA4B06DBF678BE2` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-26T09:25:10.276Z by NMUNDAY |
| Called by | [PPP_Products & Services (Multi)](PPP_Products_Services_Multi.md) |
| Used in stories | [PPP_ProdServices](../stories/PPP_ProdServices.md), [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md), [PPP_Refinerie](../stories/PPP_Refinerie.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Transpose historical GL to Prod/Serv | SCRIPT |  |
| 3 | Revenue and Costs | SCRIPT |  |

### 1. Initialise — SCRIPT

```
// For the entity that is planning the pricing for history is shown on the screen at that entities level
// just for reference purposes. It is not functional. The pricing which is functionally used is read directly
// from the central pricing entity.

// So using historical GL data and captured historical quantities we can calculate ave historical pricing for the
// entity and save it on the entity at the same granularity as the current/future just for reference purposes.

// The historical pricing is not written back to the central pricing entity because it's an average just for the
// planning entity. At the central level it would mean a calculation of all entity averages and this is not a bus req.

CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("AMT_Rev_GC","AMT_COGS_GC","Price","COS")
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/ProductServ] = BASEMEMBER([d/ProductServ] , "Total")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Lock] = "Hist_Open"

//-----------------------------------------------------------------------------------
//Calculation and Data Writing
//-----------------------------------------------------------------------------------

DELETE()
```

Parameters used: PCycle, Entity

### 2. Transpose historical GL to Prod/Serv — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("AMT_Rev_GC","AMT_COGS_GC","GC_CR")
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/ProductServ] = BASEMEMBER([d/ProductServ] , "Total")
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Lock] = "Hist_Open"

//-----------------------------------------------------------------------------------
//Calculation and Data Writing
//-----------------------------------------------------------------------------------
IF [d/GL] = [d/ProductServ].[p/GL_Revenue] THEN
	DATA.APPEND([d/Measures]="AMT_Rev_GC", [d/GL]="#", [d/PPP_Currency] = [d/ProductServ].[p/Cur]) = RESULTLOOKUP([d/Measures] = "GC_CR") 
ENDIF

IF [d/GL] = [d/ProductServ].[p/GL_COGS] THEN
	DATA.APPEND([d/Measures]="AMT_COGS_GC", [d/GL]="#", [d/PPP_Currency] = [d/ProductServ].[p/Cur]) = RESULTLOOKUP([d/Measures] = "GC_CR")
ENDIF
```

Parameters used: PCycle, Entity

### 3. Revenue and Costs — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("AMT_Rev_GC","AMT_COGS_GC","QTY","Price","COS")
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/ProductServ] = BASEMEMBER([d/ProductServ] , "Total")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Lock] = "Hist_Open"

//-----------------------------------------------------------------------------------
//Calculation and Data Writing
//-----------------------------------------------------------------------------------

DATA([d/Measures]="Price") = ROUND(RESULTLOOKUP([d/Measures] = "AMT_Rev_GC" ) / RESULTLOOKUP([d/Measures]="QTY"),2)
DATA([d/Measures]="COS") = ROUND(RESULTLOOKUP([d/Measures] = "AMT_COGS_GC") / RESULTLOOKUP([d/Measures]="QTY"),2)
```

Parameters used: PCycle, Entity
