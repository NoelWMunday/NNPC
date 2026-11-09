# FIN_KPI_Calculations

> KPI Calculations

| | |
|---|---|
| SAC id | `76D484037947247EF51B241BD45D3674` |
| Default model | PPP Financial |
| Created by | NMUNDAY |
| Last changed | 2026-10-08T08:49:56.090Z by NMUNDAY |
| Called by | [PPP_GLPost_BusPremise](PPP_GLPost_BusPremise.md) |
| Used in stories | [PPP_Financial](../stories/PPP_Financial.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["#"]` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |
| `Version_BusPremise` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget 2026 (Reference)"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Step 01 | SCRIPT |  |
| 2 | Step 02 | SCRIPT |  |
| 3 | Step 03 | SCRIPT |  |
| 4 | Step 04 | SCRIPT |  |
| 5 | Step 05 | SCRIPT |  |

### 1. Step 01 — SCRIPT

Roll up IS expenditure

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account].[h/FSV1] , "IS_GAE")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/Measures] = ("CLO_GC","RPT_YOY")

DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_OH") = 0

DATA.APPEND([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_OH") = RESULTLOOKUP([d/Measures]="CLO_GC")
```

Parameters used: Entity

### 2. Step 02 — SCRIPT

Roll up moveables

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account].[h/FSV1] , "FA01")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/Measures] = ("CLO_GC","RPT_YOY")

DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Moveables") = 0

DATA.APPEND([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Moveables") = RESULTLOOKUP([d/Measures]="CLO_GC")
```

Parameters used: Entity

### 3. Step 03 — SCRIPT

Roll up projects

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account].[h/FSV1] , "FA02")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/Measures] = ("CLO_GC","RPT_YOY")

DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Capex") = 0

DATA.APPEND([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Capex") = RESULTLOOKUP([d/Measures]="CLO_GC")
```

Parameters used: Entity

### 4. Step 04 — SCRIPT

Calc YOY value differences

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("FIN06_N_OH","FIN06_D_OH","FIN06_N_Moveables","FIN06_D_Moveables","FIN06_N_Capex","FIN06_D_Capex")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/Measures] = ("RPT_YOY")

DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_N_OH") = 0
DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_N_Moveables") = 0
DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_N_Capex") = 0

DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_N_OH") = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_OH") - 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_OH", [d/Date] = PREVIOUS(1,"YEAR",[d/Date]))

DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_N_Moveables") = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Moveables") - 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Moveables", [d/Date] = PREVIOUS(1,"YEAR",[d/Date]))

DATA([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_N_Capex") = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Capex") - 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Capex", [d/Date] = PREVIOUS(1,"YEAR",[d/Date]))
```

Parameters used: Entity

### 5. Step 05 — SCRIPT

Calc CAGR value difference

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("FIN06_N_OH","FIN06_D_OH","FIN06_N_Moveables","FIN06_D_Moveables","FIN06_N_Capex","FIN06_D_Capex")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/Date].[p/MONTHDESC] = "Dec"
MEMBERSET [d/Measures] = ("RPT_YOY","RPT_CAGR")

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_N_OH") = 0
DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_D_OH") = 0

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_N_Capex") = 0
DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_D_Capex") = 0

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_N_Moveables") = 0
DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_D_Moveables") = 0

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_D_OH", [d/Date] = NEXT(5,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_OH", [d/Date] = NEXT(1,"YEAR",%CY%))

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_N_OH", [d/Date] = NEXT(5,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_OH", [d/Date] = NEXT(5,"YEAR",%CY%)) - 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_OH", [d/Date] = NEXT(1,"YEAR",%CY%))

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_D_Capex", [d/Date] = NEXT(5,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Capex", [d/Date] = NEXT(1,"YEAR",%CY%))

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_N_Capex", [d/Date] = NEXT(5,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Capex", [d/Date] = NEXT(5,"YEAR",%CY%)) - 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Capex", [d/Date] = NEXT(1,"YEAR",%CY%))

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_D_Moveables", [d/Date] = NEXT(5,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Moveables", [d/Date] = NEXT(1,"YEAR",%CY%))

DATA([d/Measures]="RPT_CAGR", [d/PPP_Account] = "FIN06_N_Moveables", [d/Date] = NEXT(5,"YEAR",%CY%)) = 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Moveables", [d/Date] = NEXT(5,"YEAR",%CY%)) - 
	RESULTLOOKUP([d/Measures]="RPT_YOY", [d/PPP_Account] = "FIN06_D_Moveables", [d/Date] = NEXT(1,"YEAR",%CY%))
```

Parameters used: Entity, CY
