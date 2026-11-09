# CAPEX_Y-T-D

| | |
|---|---|
| SAC id | `8BDE68862A313C385149F02D86577CDB` |
| Default model | CAPEX |
| Created by | DPARUMAUL |
| Last changed | 2026-08-24T13:35:20.157Z by NMUNDAY |
| Called by | [CAPEX2_Movables_All_Calculations](CAPEX2_Movables_All_Calculations.md), [CAPEX_Movable_Calcs](CAPEX_Movable_Calcs.md) |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": "H1"}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Movables - YTD Calc | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = "YTD_GC"
MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/MovableItems] != "#"
MEMBERSET [d/GL] = "#"

DELETE()
```

Parameters used: Entity

### 2. Movables - YTD Calc — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("YTD_GC", "GC_Amount")
MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/MovableItems] != "#"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Work_Program] = "#"
MEMBERSET [d/ProjectClass] = "#"
MEMBERSET [d/Project_Status] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/Project] = "#"
MEMBERSET [d/ImpStage] = "#"

FOREACH [d/Date].[p/YEAR]

	DATA.APPEND(
				[d/Measures] = "YTD_GC",
				[d/Date] = LAST([d/Date]),
				[d/PPP_Currency] = "USD"
			   ) =
	RESULTLOOKUP(
				 [d/Measures] = "GC_Amount"
				)

ENDFOR
```

Parameters used: Entity
