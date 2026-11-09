# PPP_PrdSrv_GLEntries

> Product & Services GL entries

| | |
|---|---|
| SAC id | `3CC896052292306E90D1BF327E531771` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-09-01T12:21:28.438Z by NMUNDAY |
| Called by | [PPP_ProdServ_All_calcs](PPP_ProdServ_All_calcs.md), [PPP_Products & Services (Multi)](PPP_Products_Services_Multi.md) |
| Used in stories | [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialisation | SCRIPT |  |
| 2 | GL Entries | SCRIPT |  |

### 1. Initialisation — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("GC_CLO")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] ,%Entity% )
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/ProductServ] = BASEMEMBER([d/ProductServ] , "Total")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "GL")
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/PPP_Currency] = ("USD","NGN")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/PPP_EntryNr] = ("BP002","#")

DELETE()
```

Parameters used: Entity

### 2. GL Entries — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("GC_CLO")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] ,%Entity% )
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/ProductServ] = BASEMEMBER([d/ProductServ] , "Total")
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
// MEMBERSET [d/PPP_Currency] = ("USD","NGN")
MEMBERSET [d/PPP_EntryNr] = "BP002"

// Use these rows for debugging
//DATA([d/Measures] = "GC_CLO", [d/GL]=[d/ProductServ].[p/GL_Revenue], [d/PPP_Currency]="USD") = 1
//DATA([d/Measures] = "GC_CLO", [d/GL]=[d/ProductServ].[p/GL_COGS], [d/PPP_Currency]="USD") = 1

// Note: The .APPEND is for aggregating USD results from multiple source currencies. Although the converted GC values being aggregated are in USD based
// on the entity currency property the data still reflects the GC on the source currency base line item so multiple lines must aggregate into the final total
DATA.APPEND([d/Measures] = "GC_CLO", [d/GL]=[d/ProductServ].[p/GL_Revenue], [d/Lock] = "#") = RESULTLOOKUP([d/Measures]="AMT_Rev_GC", [d/GL]="#", [d/PPP_EntryNr] = "#") 
DATA.APPEND([d/Measures] = "GC_CLO", [d/GL]=[d/ProductServ].[p/GL_COGS], [d/Lock] = "#") = RESULTLOOKUP([d/Measures]="AMT_COGS_GC", [d/GL]="#", [d/PPP_EntryNr] = "#")
```

Parameters used: Entity
