# PPP_PrdSrv

> Products and Services

| | |
|---|---|
| SAC id | `C53F68802BA15A7F8BBE416AC7FA910E` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-09-01T11:42:17.851Z by NMUNDAY |
| Called by | [PPP_ProdServ_All_calcs](PPP_ProdServ_All_calcs.md), [PPP_Products & Services (Multi)](PPP_Products_Services_Multi.md) |
| Used in stories | [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Revenue and Costs | SCRIPT |  |

### 1. Revenue and Costs — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("AMT_Rev","AMT_COGS","QTY","Price","COS")
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Lock] = "#"

//-----------------------------------------------------------------------------------
//Calculation and Data Writing
//-----------------------------------------------------------------------------------

DATA([d/Measures]="AMT_Rev") = RESULTLOOKUP([d/Measures]="QTY") * RESULTLOOKUP([d/Measures]="Price" )
DATA([d/Measures]="AMT_COGS") = RESULTLOOKUP([d/Measures]="QTY") * RESULTLOOKUP([d/Measures]="COS" )
```

Parameters used: PCycle, Entity
