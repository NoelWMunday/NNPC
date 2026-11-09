# CP_YTD

> YTD Capital Projects

| | |
|---|---|
| SAC id | `934D80862A32D3776EF13BEA7CD9AB98` |
| Default model | CAPEX |
| Created by | DPARUMAUL |
| Last changed | 2026-08-26T09:36:31.148Z by NMUNDAY |
| Called by | [CAPEX_CP_Calcs](CAPEX_CP_Calcs.md) |
| Used in stories | [PPP_CAPEX](../stories/PPP_CAPEX.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `PCycle` | PROMPT | MEMBER | Plan_Cycle | SINGLE | `"2026-2030/01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

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
MEMBERSET [d/Measures] = "PC_YTD"
MEMBERSET [d/Plan_Cycle] = %PCycle%
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/Lock] = "#"
DELETE()
```

Parameters used: PCycle, Entity

### 2. YTD Calc — SCRIPT

Year-To-Date

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("PC_YTD", "PC_FUSD")
MEMBERSET [d/Plan_Cycle] = %PCycle%
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/Lock] = "#"

FOREACH [d/Date].[p/YEAR]

	DATA.APPEND(
				[d/Measures] = "PC_YTD",
				[d/Date] = LAST([d/Date]),
				[d/PPP_Currency] = "USD"
			   ) =
	RESULTLOOKUP(
				 [d/Measures] = "PC_FUSD"
				)

ENDFOR
```

Parameters used: PCycle, Entity
