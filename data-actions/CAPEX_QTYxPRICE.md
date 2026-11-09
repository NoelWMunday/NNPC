# CAPEX_QTYxPRICE

| | |
|---|---|
| SAC id | `7BE39684BFC346212D368C5B346F90A9` |
| Default model | CAPEX |
| Created by | NMUNDAY |
| Last changed | 2026-10-07T07:17:19.454Z by NMUNDAY |
| Called by | [CAPEX2_Movables_All_Calculations](CAPEX2_Movables_All_Calculations.md) |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Plan 2027-2031 iteration 01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": "H1"}` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Qty x Price | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/Measures] = ("M_Cost")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/MovableItems] = BASEMEMBER([d/MovableItems] , "Total")
MEMBERSET [d/PPP_Currency] = BASEMEMBER([d/PPP_Currency] , "Total")
MEMBERSEt [d/GL] = ("#")
// Lock prevents historical periods from being deleted. Histocial periods are captured
// directly as USD, no qty or price, against Hist_Open
// Only exception is CY_Dec. Here lock = "#" and no qty x price is required
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Project] = "#"
MEMBERSET [d/ImpStage] = "#"
MEMBERSET [d/ProjectClass] = "#"
MEMBERSET [d/Work_Program] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/Project_Status] = "#"
MEMBERSET [d/Start_Year] = "#"
MEMBERSET [d/End_Year] = "#"

IF [d/Date] != %CY% THEN
	DELETE()
ENDIF
```

Parameters used: Entity, CY

### 2. Qty x Price — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/Measures] = ("M_Cost")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/MovableItems] = BASEMEMBER([d/MovableItems] , "Total")
MEMBERSET [d/PPP_Currency] = BASEMEMBER([d/PPP_Currency] , "Total")
MEMBERSEt [d/GL] = ("#")
// Lock prevents historical periods from being deleted. Histocial periods are captured
// directly as USD, no qty or price, against Hist_Open
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Project] = "#"
MEMBERSET [d/ImpStage] = "#"
MEMBERSET [d/ProjectClass] = "#"
MEMBERSET [d/Work_Program] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/Project_Status] = "#"
MEMBERSET [d/Start_Year] = "#"
MEMBERSET [d/End_Year] = "#"
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"

//DATA([d/Measures]="M_Cost") = RESULTLOOKUP([d/Measures] = "QTY")
//DATA([d/Measures]="M_Cost") = RESULTLOOKUP([d/Measures]="U_Price")

IF [d/Date] != %CY% THEN
	DATA([d/Measures]="M_Cost") = 
		RESULTLOOKUP([d/Measures]="QTY") * 
		RESULTLOOKUP([d/Measures]="U_Price")
ENDIF
```

Parameters used: Entity, CY
