# PPP_CAPEX_MGLEntries

> Movables GL Entries

| | |
|---|---|
| SAC id | `72EF70862A31E1E180AC185FD660962B` |
| Default model | CAPEX |
| Created by | DPARUMAUL |
| Last changed | 2026-10-07T07:21:03.285Z by NMUNDAY |
| Called by | [CAPEX2_Movables_All_Calculations](CAPEX2_Movables_All_Calculations.md), [CAPEX_Movable_Calcs](CAPEX_Movable_Calcs.md) |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Plan 2027-2031 iteration 01"` |
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

MEMBERSET [d/Measures] = ("AMT_GL_GC")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] ,%Entity% )
MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/MovableItems] != "#"
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "GL")
MEMBERSET [d/PPP_Currency] = ("USD")

DELETE()
```

Parameters used: Entity

### 2. GL Entries — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("AMT_GL_GC")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] ,%Entity% )
MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/MovableItems] != "#"
MEMBERSET [d/Lock] = ("#", "Hist_Open")

MEMBERSET [d/Work_Program]= "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/ProjectClass] = "#"
MEMBERSET [d/Start_Year] = "#"
MEMBERSET [d/End_Year] = "#"
MEMBERSET [d/Project] = "#"
MEMBERSET [d/Project_Status] = "#"
MEMBERSET [d/ImpStage] = "#"


// Use these rows for debugging
DATA.APPEND([d/Measures] = "AMT_GL_GC",[d/GL]=[d/MovableItems].[p/GL],[d/PPP_Currency]="USD") = RESULTLOOKUP([d/Measures]="GC_Amount", [d/GL]="#")
// DATA([d/Measures] = "AMT_GL_GC", [d/GL]=[d/MovableItems].[p/GL], [d/PPP_Currency]="USD") = 1

//DATA([d/Measures] = "GC_CR", [d/GL]=[d/ProductServ].[p/GL_COGS], [d/PPP_Currency]="USD") = 1

// DATA.APPEND([d/Measures] = "AMT_GL_GC", [d/GL]=[d/MovableItems].[p/GL], [d/PPP_Currency]="USD") = RESULTLOOKUP([d/Measures]="GC_Amount", [d/GL]="#")
```

Parameters used: Entity
