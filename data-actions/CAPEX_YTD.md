# CAPEX_YTD

| | |
|---|---|
| SAC id | `A9B408862A328079364BB8A69E2F0CAB` |
| Default model | CAPEX |
| Created by | DPARUMAUL |
| Last changed | 2026-07-06T12:07:59.153Z by NMUNDAY |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `PCycle` | PROMPT | MEMBER | Plan_Cycle | SINGLE | `"2026-2030/01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | SINGLE | `"NB01"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | YTD Calc | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON
MEMBERSET [d/Measures] = "YTD_GC"
MEMBERSET [d/Plan_Cycle] = %PCycle%
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/GL] = "#"

DELETE()
```

Parameters used: PCycle, Entity

### 2. YTD Calc — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("YTD_GC", "GC_Amount")
MEMBERSET [d/Plan_Cycle] = %PCycle%
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/GL] = "#"
MEMBERSET [d/GL_Code] = "#"
MEMBERSET [d/Lock] = "#"
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

Parameters used: PCycle, Entity
