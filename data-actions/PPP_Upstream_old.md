# PPP_Upstream_old

> PPP Upstream (old)

| | |
|---|---|
| SAC id | `B82A684BFC16177B8576BA2C7860896` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-01T11:59:19.848Z by NMUNDAY |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["NB04"]` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Generic testing step | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("CST14_10")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DELETE()
```

Parameters used: Entity, PCycle

### 2. Generic testing step — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_10","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "HR")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","HR_0005")

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_10",[d/GL]="#",[d/PPP_Currency]="#",[d/PPP_EntryNr]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD",[d/PPP_EntryNr]="HR_0005")
```

Parameters used: Entity, PCycle
