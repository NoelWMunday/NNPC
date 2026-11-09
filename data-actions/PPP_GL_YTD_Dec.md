# PPP_GL_YTD_Dec

> GL_YTD_Dec

| | |
|---|---|
| SAC id | `6D49F8862A320A323A85713B3BD58453` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-09-02T09:22:31.919Z by NMUNDAY |
| Called by | [PPP_BusPremise_GL_Calcs](PPP_BusPremise_GL_Calcs.md), [PPP_OVH_All_calcs](PPP_OVH_All_calcs.md) |
| Used in stories | [PPP_Overheads](../stories/PPP_Overheads.md), [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | GL YTD Dec calc | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = "GC_CLO"
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/GL] = (BASEMEMBER([d/GL] , "Revenue"),
					BASEMEMBER([d/GL] , "OTHER_INC"),
					BASEMEMBER([d/GL] , "OTHER_DCST"), 
					BASEMEMBER([d/GL] , "COS_DPR"),
					BASEMEMBER([d/GL] , "OTHER_INC"),
					BASEMEMBER([d/GL] , "ROYALTIES"),
					BASEMEMBER([d/GL] , "CHOOCA"),
					BASEMEMBER([d/GL] , "NON_CASH"),
					BASEMEMBER([d/GL] , "GEN_ADMIN"),
					BASEMEMBER([d/GL] , "HR"),
					BASEMEMBER([d/GL] , "OTHER"),
					BASEMEMBER([d/GL] , "TAX_HIST")
				   )
MEMBERSET [d/Objectives] = "#"


DELETE()
```

Parameters used: Entity

### 2. GL YTD Dec calc — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("GC_CLO", "GC_CR")
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/GL] = (BASEMEMBER([d/GL] , "Revenue"),
					BASEMEMBER([d/GL] , "OTHER_INC"),
					BASEMEMBER([d/GL] , "OTHER_DCST"), 
					BASEMEMBER([d/GL] , "COS_DPR"),
					BASEMEMBER([d/GL] , "OTHER_INC"),
					BASEMEMBER([d/GL] , "ROYALTIES"),
					BASEMEMBER([d/GL] , "CHOOCA"),
					BASEMEMBER([d/GL] , "NON_CASH"),
					BASEMEMBER([d/GL] , "GEN_ADMIN"),
					BASEMEMBER([d/GL] , "HR"),
					BASEMEMBER([d/GL] , "OTHER"),
					BASEMEMBER([d/GL] , "TAX_HIST")
				   )
MEMBERSET [d/Objectives] = "#"

FOREACH [d/Date].[p/YEAR]

    DATA.APPEND(
        [d/Measures] = "GC_CLO", 
		[d/Date] = LAST([d/Date]),
		[d/PPP_Currency] = "USD"
    ) =
        RESULTLOOKUP(
            [d/Measures] = "GC_CR"
        )

ENDFOR
```

Parameters used: Entity
