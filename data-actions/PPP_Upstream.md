# PPP_Upstream

> PPP Upstream

| | |
|---|---|
| SAC id | `991728862A3713DF799625025CE4D358` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-01T12:02:20.990Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_BusPremise_bkup](../stories/PPP_BusPremise_bkup.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["NB04"]` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Before Initialise (for debugging purposes) | SCRIPT |  |
| 2 | Initialise | SCRIPT |  |
| 3 | Annual production | SCRIPT |  |
| 4 | Initialise common entity totals | SCRIPT |  |
| 5 | Total JV Revenue step 02 | SCRIPT |  |
| 6 | Total JV Revenue step 03 | SCRIPT |  |
| 7 | Total JV Revenue step 04 | SCRIPT |  |
| 8 | Royalties - Tranch volumes | SCRIPT |  |
| 9 | Royalties - Values (Oil) | SCRIPT |  |
| 10 | PIA Royalties - Production based (Oil) | SCRIPT |  |
| 11 | PIA Royalties - Equity production based (Oil) | SCRIPT |  |
| 12 | PIA Royalties - Price based (Oil) | SCRIPT |  |
| 13 | PIA Royalties - Gas | SCRIPT |  |
| 14 | Royalties - PA Production based (Oil) | SCRIPT |  |
| 15 | Royalties - PA Price based (Oil) | SCRIPT |  |
| 16 | Royalties - PA Gas | SCRIPT |  |
| 17 | Royalties - Summary total | SCRIPT |  |
| 18 | Gas flare penalty | SCRIPT |  |
| 19 | Costs - CAPEX Oil | SCRIPT |  |
| 20 | Costs - CAPEX Gas | SCRIPT |  |
| 21 | Costs - OPEX Oil | SCRIPT |  |
| 22 | Costs - OPEX Gas | SCRIPT |  |
| 23 | Total CAPEX / OPEX Equity | SCRIPT |  |
| 24 | Total OPEX to common entity | SCRIPT |  |
| 25 | Entities share in OPEX | SCRIPT |  |
| 26 | Total costs to be apportioned - Overheads | SCRIPT |  |
| 27 | Total costs to be apportioned - Salaries | SCRIPT |  |
| 28 | Total costs to be apportioned - Depreciation | SCRIPT |  |
| 29 | Total costs to be apportioned - Impairments | SCRIPT |  |
| 30 | Total costs to be apportioned - CHOOCA | SCRIPT |  |
| 31 | Total costs to be apportioned - Finance cost | SCRIPT |  |
| 32 | Total costs to be apportioned - Tax | SCRIPT |  |
| 33 | Total costs from CAPEX model | CROSSMODELCOPY | from CAPEX |
| 34 | Total costs CAPEX from CPY to WP | SCRIPT |  |
| 35 | Cost apportionment | SCRIPT |  |
| 36 | Development cost | SCRIPT |  |
| 37 | Tax - NDDC Levy Payable (Oil) | SCRIPT |  |
| 38 | Tax - NDDC Levy Payable (Gas) | SCRIPT |  |
| 39 | Tax - HCDT Fund Payable (Oil) | SCRIPT |  |
| 40 | Tax - HCDT Fund Payable (Gas) | SCRIPT |  |
| 41 | Tax - Development Levy (Oil) | SCRIPT |  |
| 42 | Tax - Development levy (Gas) | SCRIPT |  |
| 43 | Tax - Production Allowance | SCRIPT |  |
| 44 | Tax - CAPEX Components | SCRIPT |  |
| 45 | Tax - CAPEX Amortisation | SCRIPT |  |
| 46 | Tax - Capital allowance for PPT | SCRIPT |  |
| 47 | Tax - CA Limit Rolling Balance (Oil) | SCRIPT |  |
| 48 | Tax - CA Limit Rolling Balance (Gas) | SCRIPT |  |
| 49 | Tax - Chargeable Profit for PPT | SCRIPT |  |
| 50 | Tax - Hydrocarbon Tax (CPR Limit & HT Payable) | SCRIPT |  |
| 51 | Tax - Allowable Costs & Chargeable Profit CITA (Oil) | SCRIPT |  |
| 52 | Tax - Allowable Costs & Chargeable Profit CITA (Gas) | SCRIPT |  |
| 53 | Tax - PPT Tax (Oil) | SCRIPT |  |
| 54 | Tax - CITA (Oil & Gas) | SCRIPT |  |
| 55 | GL Entries | SCRIPT |  |

### 1. Before Initialise (for debugging purposes) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_32","REV_26","REV_40", 
					  BASEMEMBER([d/WPLn] ,"CST05" ), 
					  BASEMEMBER([d/WPLn] ,"CST10"), 
					  BASEMEMBER([d/WPLn] ,"CST14"), 
					  BASEMEMBER([d/WPLn] ,"REV3_05"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA([d/WPLn]="AMT_70") = 1
```

Parameters used: Entity, PCycle

### 2. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_32","REV_26","REV_40", 
					  BASEMEMBER([d/WPLn] ,"CST05" ), 
					  BASEMEMBER([d/WPLn] ,"CST10"), 
					  BASEMEMBER([d/WPLn] ,"CST14"), 
					  BASEMEMBER([d/WPLn] ,"REV3_05"))
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

### 3. Annual production — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

// *** DEBUG AREA - CAN LEAVE THESE COMMENT LINES FOR USE WHEN DEBUGGING ***
//DATA([d/WPLn]="REV_05") = 1
//DATA([d/WPLn]="REV_05") = RESULTLOOKUP([d/WPLn]="AMT_80")
//DATA([d/WPLn]="REV_05") = RESULTLOOKUP([d/WPLn]="GA_040", [d/PPP_Entity] = "#", [d/Lock]="Central")

// Annual oil production
// from kilo barrels per day to millions barrels per year means (x 365 / 1000) so result is in "mmbbl"
DATA([d/WPLn]="REV_05") = (RESULTLOOKUP([d/WPLn]="AMT_80") * RESULTLOOKUP([d/WPLn]="GA_040", [d/PPP_Entity] = "#", [d/Lock]="Central")) / 1000

// Ave monthly oil production
DATA([d/WPLn]="AMT_81") = RESULTLOOKUP([d/WPLn]="REV_05") / RESULTLOOKUP([d/WPLn]="UOM_65")

// Ave monthly oil production per field
DATA([d/WPLn]="AMT_82") = RESULTLOOKUP([d/WPLn]="AMT_81") / RESULTLOOKUP([d/WPLn]="AMT_97")

// Oil revenue
// from mmbbl to price per barrel and revenue in single dollars means x 1 000 000 to convert to single units
DATA([d/WPLn]="REV_10") = RESULTLOOKUP([d/WPLn]="REV_05") * RESULTLOOKUP([d/WPLn]="GA_015", [d/PPP_Entity] = "#", [d/Lock]="Central") * 1000000

// Annual gas sales
DATA([d/WPLn]="REV_15") = RESULTLOOKUP([d/WPLn]="AMT_85") * RESULTLOOKUP([d/WPLn]="GA_040", [d/PPP_Entity] = "#", [d/Lock]="Central")

// Gas revenue
// Price is already per mmscf so no conversion to single dollar units necessary
DATA([d/WPLn]="REV_20") = RESULTLOOKUP([d/WPLn]="REV_15") * RESULTLOOKUP([d/WPLn]="GA_020", [d/PPP_Entity] = "#", [d/Lock]="Central") * 1000

// Total revenue
DATA([d/WPLn]="REV_25") = RESULTLOOKUP([d/WPLn]="REV_10") + RESULTLOOKUP([d/WPLn]="REV_20") 

// NNPC Share of revenue
DATA([d/WPLn]="REV_30") = RESULTLOOKUP([d/WPLn]="REV_25") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 4. Initialise common entity totals — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_32","REV_26",BASEMEMBER([d/WPLn] , "CST14"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

// Clear the entity placeholder at the common entity level i.e. not the work program entity level
// which is cleared in the initialisation step

DATA([d/WPLn]="REV_32",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="REV_26",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0

DATA([d/WPLn]="REV3_05_05",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0

DATA([d/WPLn]="CST14_05",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="CST14_10",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="CST14_15",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="CST14_20",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="CST14_25",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="CST14_30",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="CST14_35",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="CST14_40",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
```

Parameters used: PCycle

### 5. Total JV Revenue step 02 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_25","REV_32")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

// If the entity belongs to a work group (i.e. non blank) then send it's revenue to the common entity (owning entity) 
// on the WPLn identified by the property e.g. NU03_WP01 is a JV belonging to NU03 so NU03_WP01 will point
// to NU03 as the common entity and accumulate the work group total revenue on WPLn = the property on NU03_WP01 i.e. a JV total
IF [d/PPP_Entity].[p/WPGroup] != "" THEN
	DATA.APPEND([d/WPLn]=[d/PPP_Entity].[p/Ln],[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = RESULTLOOKUP([d/WPLn]="REV_25")
ENDIF
```

Parameters used: PCycle

### 6. Total JV Revenue step 03 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]= ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("REV_40","#")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL], "OTHER_INC" ), "#")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

IF [d/PPP_Entity].[p/WPGroup] != "" THEN
	DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="REV_40",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD")
ENDIF
```

Parameters used: Entity, PCycle

### 7. Total JV Revenue step 04 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Apportionment % = REV_33 BY TOTAL REVENUE

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_32","REV_33","REV_25","REV_35","REV_40")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA([d/WPLn]="REV_32") = RESULTLOOKUP([d/WPLn]="REV_32",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup])

IF RESULTLOOKUP([d/WPLn]="REV_32") > 0 THEN
	DATA([d/WPLn]="REV_33") = RESULTLOOKUP([d/WPLn]="REV_25") / RESULTLOOKUP([d/WPLn]="REV_32") * 100
	DATA([d/WPLn]="REV_35") = RESULTLOOKUP([d/WPLn]="REV_33") * RESULTLOOKUP([d/WPLn]="REV_40") / 100
ENDIF
```

Parameters used: Entity, PCycle

### 8. Royalties - Tranch volumes — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

VARIABLEMEMBER #TRANCH1 OF [d/WPLn]
VARIABLEMEMBER #TRANCH2 OF [d/WPLn]
VARIABLEMEMBER #TRANCH3 OF [d/WPLn]
VARIABLEMEMBER #TRANCH4 OF [d/WPLn]
VARIABLEMEMBER #AVEPROD OF [d/WPLn]

// Find the tranch value and royalty rate % for tranch 1 by using the ASSET TERRAIN flag (which is set to 1) to expose it
//DATA([d/Measures]="Value_WPLn",[d/WPLn]="RC05_05",[d/Date]="202612") = RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612")
//DATA([d/Measures]="Value_WPLn",[d/WPLn]="RC05_05",[d/Date]="202612") = RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_01",[d/PPP_Entity]="#",[d/Date]="202612",[d/Lock]="Central")
DATA([d/WPLn] = #TRANCH1) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_010_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_015_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_020_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_025_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_030_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))

DATA([d/WPLn] = #TRANCH2) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_010_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_015_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_020_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_025_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_030_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
							
DATA([d/WPLn] = #TRANCH3) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_010_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_015_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_020_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_025_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_030_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
														
DATA([d/WPLn] = #TRANCH4) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_010_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_015_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_020_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_025_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_030_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))				
							
DATA([d/WPLn] = #AVEPROD) = RESULTLOOKUP([d/WPLn]="AMT_82") * 1000000

IF (RESULTLOOKUP([d/WPLn] = #AVEPROD) >  RESULTLOOKUP([d/WPLn] = #TRANCH1)) THEN
	DATA([d/WPLn] = "RC05_05") = RESULTLOOKUP([d/WPLn] = #TRANCH1)
	IF ((RESULTLOOKUP([d/WPLn] = #AVEPROD) - RESULTLOOKUP([d/WPLn] = #TRANCH1)) > RESULTLOOKUP([d/WPLn] = #TRANCH2)) THEN
		DATA([d/WPLn] = "RC05_10") = RESULTLOOKUP([d/WPLn] = #TRANCH2)
		IF ((RESULTLOOKUP([d/WPLn] = #AVEPROD) - RESULTLOOKUP([d/WPLn] = #TRANCH1) - RESULTLOOKUP([d/WPLn] = #TRANCH2)) > RESULTLOOKUP([d/WPLn] = #TRANCH3)) THEN
			DATA([d/WPLn] = "RC05_15") = RESULTLOOKUP([d/WPLn] = #TRANCH3)
			DATA([d/WPLn] = "RC05_20") = RESULTLOOKUP([d/WPLn] = #AVEPROD) - RESULTLOOKUP([d/WPLn] = #TRANCH1) - RESULTLOOKUP([d/WPLn] = #TRANCH2) - RESULTLOOKUP([d/WPLn] = #TRANCH3)
		ELSE
			DATA([d/WPLn] = "RC05_15") = RESULTLOOKUP([d/WPLn] = #AVEPROD) - RESULTLOOKUP([d/WPLn] = #TRANCH1) - RESULTLOOKUP([d/WPLn] = #TRANCH2)
			DATA([d/WPLn] = "RC05_20") = 0			
		ENDIF
	ELSE
		DATA([d/WPLn] = "RC05_10") = RESULTLOOKUP([d/WPLn] = #AVEPROD) - RESULTLOOKUP([d/WPLn] = #TRANCH1)
		DATA([d/WPLn] = "RC05_15") = 0
		DATA([d/WPLn] = "RC05_20") = 0
	ENDIF
ELSE
	DATA([d/WPLn] = "RC05_05") = RESULTLOOKUP([d/WPLn] = #AVEPROD)
	DATA([d/WPLn] = "RC05_10") = 0
	DATA([d/WPLn] = "RC05_15") = 0
	DATA([d/WPLn] = "RC05_20") = 0
ENDIF
```

Parameters used: Entity, PCycle

### 9. Royalties - Values (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

VARIABLEMEMBER #RR_TRANCH1 OF [d/WPLn]
VARIABLEMEMBER #RR_TRANCH2 OF [d/WPLn]
VARIABLEMEMBER #RR_TRANCH3 OF [d/WPLn]
VARIABLEMEMBER #RR_TRANCH4 OF [d/WPLn]
VARIABLEMEMBER #OIL_PRICE OF [d/WPLn]

// Find the tranch value and royalty rate % for tranch 1 by using the ASSET TERRAIN flag (which is set to 1) to expose it
DATA([d/WPLn] = #RR_TRANCH1) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_005_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_010_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_015_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_020_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_025_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_030_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))

DATA([d/WPLn] = #RR_TRANCH2) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_005_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_010_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_015_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_020_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_025_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_030_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
							
DATA([d/WPLn] = #RR_TRANCH3) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_005_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_010_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_015_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_020_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_025_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_030_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
														
DATA([d/WPLn] = #RR_TRANCH4) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_005_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_010_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_015_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_020_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_025_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_030_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))				

// #OIL_PRICE
DATA([d/WPLn]=#OIL_PRICE) = RESULTLOOKUP([d/WPLn]="GA_015",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = "RC10_05") = RESULTLOOKUP([d/WPLn]=#RR_TRANCH1) * RESULTLOOKUP([d/WPLn]="RC05_05") * RESULTLOOKUP([d/WPLn]=#OIL_PRICE) 
DATA([d/WPLn] = "RC10_10") = RESULTLOOKUP([d/WPLn]=#RR_TRANCH2) * RESULTLOOKUP([d/WPLn]="RC05_10") * RESULTLOOKUP([d/WPLn]=#OIL_PRICE) 
DATA([d/WPLn] = "RC10_15") = RESULTLOOKUP([d/WPLn]=#RR_TRANCH3) * RESULTLOOKUP([d/WPLn]="RC05_15") * RESULTLOOKUP([d/WPLn]=#OIL_PRICE) 
DATA([d/WPLn] = "RC10_20") = RESULTLOOKUP([d/WPLn]=#RR_TRANCH4) * RESULTLOOKUP([d/WPLn]="RC05_20") * RESULTLOOKUP([d/WPLn]=#OIL_PRICE)
```

Parameters used: Entity, PCycle

### 10. PIA Royalties - Production based (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA([d/WPLn]="RC15_05") = RESULTLOOKUP([d/WPLn]="AMT_97") * 
						(RESULTLOOKUP([d/WPLn]="RC10_05") + RESULTLOOKUP([d/WPLn]="RC10_10") +
						 RESULTLOOKUP([d/WPLn]="RC10_15") + RESULTLOOKUP([d/WPLn]="RC10_20")) *
						RESULTLOOKUP([d/WPLn]="UOM_65") *
						RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")
```

Parameters used: Entity, PCycle

### 11. PIA Royalties - Equity production based (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA([d/WPLn]="RC15_10") = 	RESULTLOOKUP([d/WPLn]="RC15_05") *
							RESULTLOOKUP([d/WPLn]="AMT_90",[d/Date]="000000") / 100
```

Parameters used: Entity, PCycle

### 12. PIA Royalties - Price based (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

VARIABLEMEMBER #OILPRICE OF [d/WPLn]
VARIABLEMEMBER #OILPRICE_LT OF [d/WPLn]
VARIABLEMEMBER #OILPRICE_EQ OF [d/WPLn]
VARIABLEMEMBER #OILPRICE_GT OF [d/WPLn]
VARIABLEMEMBER #RR_LT OF [d/WPLn]
VARIABLEMEMBER #RR_EQ OF [d/WPLn]
VARIABLEMEMBER #RR_GT OF [d/WPLn]

DATA([d/WPLn] = #OILPRICE) = RESULTLOOKUP([d/WPLn]="GA_015",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #OILPRICE_LT) = RESULTLOOKUP([d/Measures]="Royalty_PriceBand",[d/WPLn]="RR03_005",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #OILPRICE_EQ) = RESULTLOOKUP([d/Measures]="Royalty_PriceBand",[d/WPLn]="RR03_010",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #OILPRICE_GT) = RESULTLOOKUP([d/Measures]="Royalty_PriceBand",[d/WPLn]="RR03_015",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #RR_LT) = RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR03_005",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central") * 100
DATA([d/WPLn] = #RR_EQ) = RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR03_010",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central") * 100
DATA([d/WPLn] = #RR_GT) = RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR03_015",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central") * 100


IF (RESULTLOOKUP([d/WPLn] = #OILPRICE) < RESULTLOOKUP([d/WPLn] = #OILPRICE_LT)) THEN
	DATA([d/WPLn]="RC20_05") = RESULTLOOKUP([d/WPLn] = #RR_LT)
ELSE
	IF (RESULTLOOKUP([d/WPLn] = #OILPRICE) < RESULTLOOKUP([d/WPLn] = #OILPRICE_EQ)) THEN
		DATA([d/WPLn]="RC20_05") = (RESULTLOOKUP([d/WPLn] = #OILPRICE) - RESULTLOOKUP([d/WPLn] = #OILPRICE_LT)) /
									RESULTLOOKUP([d/WPLn] = #OILPRICE_LT) * RESULTLOOKUP([d/WPLn] = #RR_EQ)
	ELSE
		IF (RESULTLOOKUP([d/WPLn] = #OILPRICE) < RESULTLOOKUP([d/WPLn] = #OILPRICE_GT)) THEN
			DATA([d/WPLn]="RC20_05") = RESULTLOOKUP([d/WPLn] = #RR_EQ) + 
										((RESULTLOOKUP([d/WPLn] = #OILPRICE) - RESULTLOOKUP([d/WPLn] = #OILPRICE_EQ)) / 
										RESULTLOOKUP([d/WPLn] = #OILPRICE_LT) * RESULTLOOKUP([d/WPLn] = #RR_EQ))
		ELSE
			DATA([d/WPLn]="RC20_05") = RESULTLOOKUP([d/WPLn] = #RR_GT)
		ENDIF
	ENDIF
ENDIF

DATA([d/WPLn]="RC20_10") = RESULTLOOKUP([d/WPLn] = "REV_10") * 
							RESULTLOOKUP([d/WPLn]="RC20_05") / 100 * 
							RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")
							
DATA([d/WPLn]="RC20_15") = RESULTLOOKUP([d/WPLn]="RC20_10") * RESULTLOOKUP([d/WPLn]="AMT_90",[d/Date]="000000") / 100
```

Parameters used: Entity, PCycle

### 13. PIA Royalties - Gas — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

VARIABLEMEMBER #RR_RATE OF [d/WPLn]
DATA([d/WPLn] = #RR_RATE) =  (RESULTLOOKUP([d/WPLn]="SET20_05",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_005",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_010",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_015",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_020",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_025",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_030",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_35",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_035",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
							
DATA([d/WPLn]="RC25_20") = RESULTLOOKUP([d/WPLn] = #RR_RATE) * RESULTLOOKUP([d/WPLn]="REV_20") * RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")

DATA([d/WPLn]="RC25_25") = RESULTLOOKUP([d/WPLn] = "RC25_20") * RESULTLOOKUP([d/WPLn]="AMT_90",[d/Date]="000000") / 100
```

Parameters used: Entity, PCycle

### 14. Royalties - PA Production based (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

VARIABLEMEMBER #RR_RATE OF [d/WPLn]
DATA([d/WPLn] = #RR_RATE) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_005_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_010_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_015_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_020_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_025_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_030_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))

DATA([d/WPLn]="RC30_05") = RESULTLOOKUP([d/WPLn] = #RR_RATE) * RESULTLOOKUP([d/WPLn]="REV_10") * RESULTLOOKUP([d/WPLn]="SET10_05", [d/Date] = "000000")

DATA([d/WPLn]="RC30_10") = RESULTLOOKUP([d/WPLn] = "RC30_05") * RESULTLOOKUP([d/WPLn]="AMT_90",[d/Date]="000000") / 100
```

Parameters used: Entity, PCycle

### 15. Royalties - PA Price based (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

VARIABLEMEMBER #OILPRICE OF [d/WPLn]
VARIABLEMEMBER #PRICEBAND_1 OF [d/WPLn]
VARIABLEMEMBER #PRICEBAND_2 OF [d/WPLn]
VARIABLEMEMBER #PRICEBAND_3 OF [d/WPLn]
VARIABLEMEMBER #PRICEBAND_4 OF [d/WPLn]
VARIABLEMEMBER #PRICEBAND_5 OF [d/WPLn]
VARIABLEMEMBER #RR_1 OF [d/WPLn]
VARIABLEMEMBER #RR_2 OF [d/WPLn]
VARIABLEMEMBER #RR_3 OF [d/WPLn]
VARIABLEMEMBER #RR_4 OF [d/WPLn]
VARIABLEMEMBER #RR_5 OF [d/WPLn]

DATA([d/WPLn] = #OILPRICE) = RESULTLOOKUP([d/WPLn]="GA_015",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #PRICEBAND_1) = RESULTLOOKUP([d/Measures]="Royalty_PriceBand",[d/WPLn]="RR03_020",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #PRICEBAND_2) = RESULTLOOKUP([d/Measures]="Royalty_PriceBand",[d/WPLn]="RR03_025",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #PRICEBAND_3) = RESULTLOOKUP([d/Measures]="Royalty_PriceBand",[d/WPLn]="RR03_030",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #PRICEBAND_4) = RESULTLOOKUP([d/Measures]="Royalty_PriceBand",[d/WPLn]="RR03_035",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn] = #PRICEBAND_5) = RESULTLOOKUP([d/Measures]="Royalty_PriceBand",[d/WPLn]="RR03_040",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central")

DATA([d/WPLn] = #RR_1) = RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR03_020",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central") * 100
DATA([d/WPLn] = #RR_2) = RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR03_025",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central") * 100
DATA([d/WPLn] = #RR_3) = RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR03_030",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central") * 100
DATA([d/WPLn] = #RR_4) = RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR03_035",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central") * 100
DATA([d/WPLn] = #RR_5) = RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR03_040",[d/Date]="000000",[d/PPP_Entity]="#",[d/Lock]="Central") * 100

IF (RESULTLOOKUP([d/WPLn] = #OILPRICE) < RESULTLOOKUP([d/WPLn] = #PRICEBAND_1)) THEN
	DATA([d/WPLn]="RC35_05") = RESULTLOOKUP([d/WPLn] = #RR_1)
ELSE
	IF (RESULTLOOKUP([d/WPLn] = #OILPRICE) < RESULTLOOKUP([d/WPLn] = #PRICEBAND_2)) THEN
		DATA([d/WPLn]="RC35_05") = RESULTLOOKUP([d/WPLn] = #RR_2)
	ELSE
		IF (RESULTLOOKUP([d/WPLn] = #OILPRICE) < RESULTLOOKUP([d/WPLn] = #PRICEBAND_3)) THEN
			DATA([d/WPLn]="RC35_05") = RESULTLOOKUP([d/WPLn] = #RR_3)
		ELSE
			IF (RESULTLOOKUP([d/WPLn] = #OILPRICE) < RESULTLOOKUP([d/WPLn] = #PRICEBAND_4)) THEN
				DATA([d/WPLn]="RC35_05") = RESULTLOOKUP([d/WPLn] = #RR_4)
			ELSE
				DATA([d/WPLn]="RC35_05") = RESULTLOOKUP([d/WPLn] = #RR_5)
			ENDIF
		ENDIF
	ENDIF
ENDIF

DATA([d/WPLn]="RC35_10") = RESULTLOOKUP([d/WPLn] = "REV_10") * 
						RESULTLOOKUP([d/WPLn]="RC35_05") / 100 *
						RESULTLOOKUP([d/WPLn]="SET10_05", [d/Date] = "000000")

DATA([d/WPLn]="RC35_15") = RESULTLOOKUP([d/WPLn]="RC35_10") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 16. Royalties - PA Gas — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

VARIABLEMEMBER #RR_RATE OF [d/WPLn]
DATA([d/WPLn] = #RR_RATE) =  (RESULTLOOKUP([d/WPLn]="SET20_20",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR04_020",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_25",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR04_025",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_30",[d/Date]="202612") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR04_030",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
							
							
DATA([d/WPLn]="RC40_20") = RESULTLOOKUP([d/WPLn] = #RR_RATE) * RESULTLOOKUP([d/WPLn]="REV_20")

DATA([d/WPLn]="RC40_25") = RESULTLOOKUP([d/WPLn] = "RC40_20") * 
							RESULTLOOKUP([d/WPLn]="AMT_90",[d/Date]="000000") / 100
```

Parameters used: Entity, PCycle

### 17. Royalties - Summary total — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "RC_TOT")
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

// Summary of royalty calcs
DATA([d/WPLn] = "RC_TOT_05_05_01") = RESULTLOOKUP([d/WPLn] = "RC15_05")
DATA([d/WPLn] = "RC_TOT_05_05_02") = RESULTLOOKUP([d/WPLn] = "RC20_10")
DATA([d/WPLn] = "RC_TOT_05_05_03") = RESULTLOOKUP([d/WPLn] = "RC25_20")
DATA([d/WPLn] = "RC_TOT_05_10_01") = RESULTLOOKUP([d/WPLn] = "RC30_05")
DATA([d/WPLn] = "RC_TOT_05_10_02") = RESULTLOOKUP([d/WPLn] = "RC35_10")
DATA([d/WPLn] = "RC_TOT_05_10_03") = RESULTLOOKUP([d/WPLn] = "RC40_20")

// Equity portion (not split) - just the total
DATA([d/WPLn] = "RC_TOT_10") = 
	RESULTLOOKUP([d/WPLn] = "RC15_10") +
	RESULTLOOKUP([d/WPLn] = "RC20_15") +	
	RESULTLOOKUP([d/WPLn] = "RC25_25") +
	RESULTLOOKUP([d/WPLn] = "RC30_10") +	
	RESULTLOOKUP([d/WPLn] = "RC35_15") +
	RESULTLOOKUP([d/WPLn] = "RC40_25")
```

Parameters used: Entity, PCycle

### 18. Gas flare penalty — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] =
// MEMBERSET [d/Date] =
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"


DATA([d/WPLn]="AMT_95") = RESULTLOOKUP([d/WPLn]="AMT_85") * 
							RESULTLOOKUP([d/WPLn]="GA_035",[d/PPP_Entity]="#",[d/Lock]="Central") / 100

DATA([d/WPLn]="AMT_230",[d/PPP_EntryNr]="UAP_GFP") = 
		RESULTLOOKUP([d/WPLn]="AMT_95") * 1000 *
		RESULTLOOKUP([d/WPLn]="GA_040",[d/PPP_Entity]="#",[d/Lock]="Central") *
		RESULTLOOKUP([d/WPLn]="GA_030",[d/PPP_Entity]="#",[d/Lock]="Central")
```

Parameters used: Entity, PCycle

### 19. Costs - CAPEX Oil — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("CST05_15","AMT_200")
MEMBERSET [d/PPP_EntryNr] = ("#", BASEMEMBER([d/PPP_EntryNr] , "UAP_CAPEX_CST"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"


DATA.APPEND([d/WPLn] = "CST05_15", [d/PPP_EntryNr] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_200")
```

Parameters used: Entity, PCycle

### 20. Costs - CAPEX Gas — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("CST05_20","AMT_210")
MEMBERSET [d/PPP_EntryNr] = ("#", BASEMEMBER([d/PPP_EntryNr] , "UAP_CAPEX_CST"), BASEMEMBER([d/PPP_EntryNr] , "UAP_CAPEX_OTH"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"


DATA.APPEND([d/WPLn] = "CST05_20", [d/PPP_EntryNr] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_210")
```

Parameters used: Entity, PCycle

### 21. Costs - OPEX Oil — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("CST05_05","AMT_220")
MEMBERSET [d/PPP_EntryNr] = ("#", BASEMEMBER([d/PPP_EntryNr] , "UAP_OPEX_CST"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"


DATA.APPEND([d/WPLn] = "CST05_05", [d/PPP_EntryNr] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_220")
```

Parameters used: Entity, PCycle

### 22. Costs - OPEX Gas — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("CST05_10","AMT_230")
MEMBERSET [d/PPP_EntryNr] = ("#", BASEMEMBER([d/PPP_EntryNr] , "UAP_OPEX_CST"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"


DATA.APPEND([d/WPLn] = "CST05_10", [d/PPP_EntryNr] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_230")
```

Parameters used: Entity, PCycle

### 23. Total CAPEX / OPEX Equity — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"

// Opex equity portion excludes COS Depr. and Depletion
DATA([d/WPLn]="CST10_05") = 
		(RESULTLOOKUP([d/WPLn]="CST05_05") -
		RESULTLOOKUP([d/WPLn]="AMT_220",[d/PPP_EntryNr]="UAP_5800_15") -
		RESULTLOOKUP([d/WPLn]="AMT_220",[d/PPP_EntryNr]="UAP_5800_16")) * 
		RESULTLOOKUP([d/WPLn]="AMT_90") / 100

DATA([d/WPLn]="CST10_10") = 
		(RESULTLOOKUP([d/WPLn]="CST05_10") - 
		RESULTLOOKUP([d/WPLn]="AMT_230",[d/PPP_EntryNr]="UAP_5800_15") -
		RESULTLOOKUP([d/WPLn]="AMT_230",[d/PPP_EntryNr]="UAP_5800_16")) * 
		RESULTLOOKUP([d/WPLn]="AMT_90") / 100

DATA([d/WPLn]="CST10_15") = 
		RESULTLOOKUP([d/WPLn]="CST05_15") * 
		RESULTLOOKUP([d/WPLn]="AMT_90") / 100

DATA([d/WPLn]="CST10_20") = 
		RESULTLOOKUP([d/WPLn]="CST05_20") * 
		RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 24. Total OPEX to common entity — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Note the OPEX line item for dimension WPLn is determined by the entity property
// so that it's dynamic and can be used for JV's and PSC's

MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = (BASEMEMBER([d/WPLn], "AMT_OPEX"), "REV3_05_05")
MEMBERSET [d/PPP_EntryNr] = (BASEMEMBER([d/PPP_EntryNr] , "UAP_OPEX_CST"), "#")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

// If the entity belongs to a work group (i.e. non blank) then send it's revenue to the common entity (owning entity) 
// on the WPLn identified by the property e.g. NU03_WP01 is a JV belonging to NU03 so NU03_WP01 will point
// to NU03 as the common entity and accumulate the work group total revenue on WPLn = the property on NU03_WP01 i.e. a JV total
IF [d/PPP_Entity].[p/WPGroup] != "" AND [d/WPLn] != "REV3_05_05" AND [d/PPP_EntryNr] != "#" THEN
	DATA.APPEND([d/WPLn] = [d/PPP_Entity].[p/Ln_OPEX], [d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup], [d/PPP_EntryNr] = "#") = 
		RESULTLOOKUP()
ENDIF
```

Parameters used: PCycle

### 25. Entities share in OPEX — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Apportionment %

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "REV3_05")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

// Read the total OPEX from the common entity into this entities total opex line per the properties
// At this point don't know if it's JV or PSC or other but the correct WPLn will populate
DATA([d/WPLn] = [d/PPP_Entity].[p/Ln_OPEX]) = RESULTLOOKUP([d/WPLn] = [d/PPP_Entity].[p/Ln_OPEX], [d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup])

// This calculation works out the % share of JV, PSC and any other because not knowing if it's JV, PSC etc doesn't matter
// The non-zero WPLn's will popluate and the zero WPLn just return zero
IF RESULTLOOKUP([d/WPLn] = "REV3_05_05") > 0 THEN
	DATA([d/WPLn]="REV3_10_05") = (RESULTLOOKUP([d/WPLn]="CST05_05") + RESULTLOOKUP([d/WPLn]="CST05_10")) / RESULTLOOKUP([d/WPLn] = "REV3_05_05") * 100
ENDIF
```

Parameters used: Entity, PCycle

### 26. Total costs to be apportioned - Overheads — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_05","#")
MEMBERSET [d/GL] = ("#", BASEMEMBER([d/GL] , "GEN_ADMIN"))
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_05",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD")
```

Parameters used: Entity, PCycle

### 27. Total costs to be apportioned - Salaries — SCRIPT

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

### 28. Total costs to be apportioned - Depreciation — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_15","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "DEPRECIATION")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_15",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD")
```

Parameters used: Entity, PCycle

### 29. Total costs to be apportioned - Impairments — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_20","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "PROV_IMP")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_20",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD")
```

Parameters used: Entity, PCycle

### 30. Total costs to be apportioned - CHOOCA — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_25","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "CHOOCA")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_25",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD")
```

Parameters used: Entity, PCycle

### 31. Total costs to be apportioned - Finance cost — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_30","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "OTH_0005")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_30",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD")
```

Parameters used: Entity, PCycle

### 32. Total costs to be apportioned - Tax — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("CST14_35","#")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "TAX_HIST")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="CST14_35",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD")
```

Parameters used: Entity, PCycle

### 33. Total costs from CAPEX model — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cbifmh01bklfvf7ijs46d1ano3b",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "YTD_GC",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "Value_WPLn"
      ],
      "hierarchyName": null
     }
    },
    {
     "source": {
      "memberId": "PC_YTD",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "Value_WPLn"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "USD",
      "hierarchyName": "H1"
     },
     "target": {
      "memberIds": [
       "#"
      ],
      "hierarchyName": "H1"
     }
    }
   ]
  },
  "PPP_EntryNr": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "GL": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Ln": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Lock": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Objectives": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "ProductServ": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "Strategy": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": null
   },
   "sourceDimensionId": null
  },
  "WorkProgram": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": null
   },
   "sourceDimensionId": null
  },
  "WPLn": {
   "defaultMember": {
    "memberId": "CST14_40",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "Plan_Cycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  }
 }
}
```

</details>

### 34. Total costs CAPEX from CPY to WP — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// The CAPEX model to model copy will copy the capex spend per month to the same
// entity in BUSPREMISE e.g. NU03. This effectively provides the totals in NU03
// that otherwise would be in NU03 under CAPEX dimension members.
// Those totals will be persisted on CST14_40
// This function now lets the WP (Work Program) being planned read it from the main entity
// using the work program entity's property which points to the main entity

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn")
MEMBERSET [d/WPLn] = ("CST14_40")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

DATA() = RESULTLOOKUP([d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup])
```

Parameters used: Entity, PCycle

### 35. Cost apportionment — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"

DATA([d/WPLn]="CST15_05") = RESULTLOOKUP([d/WPLn]="CST14_05") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_10") = RESULTLOOKUP([d/WPLn]="CST14_10") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_15") = RESULTLOOKUP([d/WPLn]="CST14_15") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_20") = RESULTLOOKUP([d/WPLn]="CST14_20") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_25") = RESULTLOOKUP([d/WPLn]="CST14_25") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_30") = RESULTLOOKUP([d/WPLn]="CST14_30") * RESULTLOOKUP([d/WPLn]="REV3_10_05") / 100
DATA([d/WPLn]="CST15_35") = RESULTLOOKUP([d/WPLn]="CST14_35") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
DATA([d/WPLn]="CST15_40") = RESULTLOOKUP([d/WPLn]="CST14_40") * RESULTLOOKUP([d/WPLn]="REV_33") / 100
```

Parameters used: Entity, PCycle

### 36. Development cost — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("CST20", "SET10_05")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"

// Numerator
VARIABLEMEMBER #NUMERATOR OF [d/WPLn]

// Total Appraisal & Exploration Cost – Oil
VARIABLEMEMBER #TAECO OF [d/WPLn]

// 1/5 of "Devt Well, Completion and Workover"
VARIABLEMEMBER #DRILLING OF [d/WPLn]
VARIABLEMEMBER #DRILLING_FIFTH OF [d/WPLn]

// 1/5 of "CAPEX Facilities Oil"
VARIABLEMEMBER #FACILITIES OF [d/WPLn]
VARIABLEMEMBER #FACILITIES_FIFTH OF [d/WPLn]

// 1/5 of "Devt Well, Completion and Workover"
DATA([d/WPLn] = #DRILLING) = RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_130")
DATA([d/WPLn] = #DRILLING_FIFTH) = RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_130") / 5

// 1/5 of "CAPEX Facilities Oil"
DATA([d/WPLn] = #FACILITIES) = 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_132") +
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_136") +	
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_138") +	
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_139")	
	
DATA([d/WPLn] = #FACILITIES_FIFTH) = RESULTLOOKUP([d/WPLn] = #FACILITIES) / 5

// Total Appraisal & Exploration Cost – Oil
DATA([d/WPLn] = #TAECO) = 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_110") + 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_120") + 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_121") + 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_124")


IF RESULTLOOKUP([d/WPLn] = "SET10_05", [d/Date] = "000000") = 1 THEN
	// PPT
	DATA([d/WPLn] = #NUMERATOR) =
		RESULTLOOKUP([d/WPLn] = #TAECO) + 
	
		// Drilling
		// "Devt Well, Completion and Workover" (e.g. 80% of full drilling)
		(RESULTLOOKUP([d/WPLn] = #DRILLING) *
		RESULTLOOKUP([d/WPLn] = "AMT_46") / 100) +
		// plus 1/5 of the remaining (e.g. 20%) of drilling
		(RESULTLOOKUP([d/WPLn] = #DRILLING_FIFTH) * 
		(100 - RESULTLOOKUP([d/WPLn] = "AMT_46")) / 100) +
		
		// Facilities
		(RESULTLOOKUP([d/WPLn] = #FACILITIES_FIFTH) * 
		(100 - RESULTLOOKUP([d/WPLn] = "AMT_46")) / 100)		
	
ELSE
	// PIA
	DATA([d/WPLn] = #NUMERATOR) =
		RESULTLOOKUP([d/WPLn] = #TAECO) + 
	
		// Drilling
		// plus 1/5 of the remaining (e.g. 20%) of drilling
		RESULTLOOKUP([d/WPLn] = #DRILLING_FIFTH) +
		
		// Facilities
		RESULTLOOKUP([d/WPLn] = #FACILITIES_FIFTH)	
ENDIF

DATA([d/WPLn] = "CST20") =
		RESULTLOOKUP([d/WPLn] = #NUMERATOR) /
		RESULTLOOKUP([d/WPLn] = "REV_05")
```

Parameters used: Entity, PCycle

### 37. Tax - NDDC Levy Payable (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn]="TAX025_15_05") = RESULTLOOKUP([d/WPLn]="AMT_220")
DATA([d/WPLn]="TAX025_15_10") = RESULTLOOKUP([d/WPLn]="AMT_200")

DATA([d/WPLn]="TAX025_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX025_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX025_10") * (
	RESULTLOOKUP([d/WPLn]="TAX025_15_05") +														   
	RESULTLOOKUP([d/WPLn]="TAX025_15_10")
),0) / 100
```

Parameters used: Entity, PCycle

### 38. Tax - NDDC Levy Payable (Gas) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn]="TAX030_15_05") = RESULTLOOKUP([d/WPLn]="AMT_230")
DATA([d/WPLn]="TAX030_15_10") = RESULTLOOKUP([d/WPLn]="AMT_210")

DATA([d/WPLn]="TAX030_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX030_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX025_10") * (
	RESULTLOOKUP([d/WPLn]="TAX030_15_05") +														   
	RESULTLOOKUP([d/WPLn]="TAX030_15_10")
),0) / 100
```

Parameters used: Entity, PCycle

### 39. Tax - HCDT Fund Payable (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn]="TAX015_15") = RESULTLOOKUP([d/WPLn]="AMT_220")

DATA([d/WPLn]="TAX015_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX015_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX015_15") * 
	RESULTLOOKUP([d/WPLn]="TAX015_10"
),0) / 100
```

Parameters used: Entity, PCycle

### 40. Tax - HCDT Fund Payable (Gas) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn]="TAX020_15") = RESULTLOOKUP([d/WPLn]="AMT_230")

DATA([d/WPLn]="TAX020_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX020_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX020_15") * 
	RESULTLOOKUP([d/WPLn]="TAX020_10"
),0) / 100
```

Parameters used: Entity, PCycle

### 41. Tax - Development Levy (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

// Development Levy (Oil)
DATA([d/WPLn]="TAX005_15_05") = RESULTLOOKUP([d/WPLn]="REV_10")
DATA([d/WPLn]="TAX005_15_10") = 0-RESULTLOOKUP([d/WPLn]="RC15_05") 
DATA([d/WPLn]="TAX005_15_15") = 0-RESULTLOOKUP([d/WPLn]="RC20_10") 
DATA([d/WPLn]="TAX005_15_20") = 0-RESULTLOOKUP([d/WPLn]="RC30_10") 
DATA([d/WPLn]="TAX005_15_25") = 0-RESULTLOOKUP([d/WPLn]="RC35_10") 
DATA([d/WPLn]="TAX005_15_30") = 0-RESULTLOOKUP([d/WPLn]="CST05_05") 
DATA([d/WPLn]="TAX005_15_35") = 0-RESULTLOOKUP([d/WPLn]="TAX015_05") 
DATA([d/WPLn]="TAX005_15_40") = 0-RESULTLOOKUP([d/WPLn]="TAX025_05")

DATA([d/WPLn]="TAX005_10") = RESULTLOOKUP([d/WPLn]="TL20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX005_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX005_10") * (
	RESULTLOOKUP([d/WPLn]="TAX005_15_05") +														   
	RESULTLOOKUP([d/WPLn]="TAX005_15_10") +
	RESULTLOOKUP([d/WPLn]="TAX005_15_15") +
	RESULTLOOKUP([d/WPLn]="TAX005_15_20") +
	RESULTLOOKUP([d/WPLn]="TAX005_15_25") +
	RESULTLOOKUP([d/WPLn]="TAX005_15_30") +
	RESULTLOOKUP([d/WPLn]="TAX005_15_35") +
	RESULTLOOKUP([d/WPLn]="TAX005_15_40")
),0) / 100

IF RESULTLOOKUP([d/WPLn]="TAX005_05") < 0 THEN
	DATA([d/WPLn]="TAX005_05") = 0
ENDIF
```

Parameters used: Entity, PCycle

### 42. Tax - Development levy (Gas) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn]="TAX010_15_05") = RESULTLOOKUP([d/WPLn]="REV_20")
DATA([d/WPLn]="TAX010_15_10") = 0-RESULTLOOKUP([d/WPLn]="RC25_20")
DATA([d/WPLn]="TAX010_15_15") = 0-RESULTLOOKUP([d/WPLn]="AMT_230") 
DATA([d/WPLn]="TAX010_15_20") = 0-RESULTLOOKUP([d/WPLn]="RC40_20") 
DATA([d/WPLn]="TAX010_15_25") = 0-RESULTLOOKUP([d/WPLn]="TAX030_05") 
DATA([d/WPLn]="TAX010_15_30") = 0-RESULTLOOKUP([d/WPLn]="TAX020_05") 

DATA([d/WPLn]="TAX010_10") = RESULTLOOKUP([d/WPLn]="TL20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX010_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX010_10") * (
	RESULTLOOKUP([d/WPLn]="TAX010_15_05") +														   
	RESULTLOOKUP([d/WPLn]="TAX010_15_10") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_15") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_20") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_25") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_30")
),0) / 100

IF RESULTLOOKUP([d/WPLn]="TAX010_05") < 0 THEN
	DATA([d/WPLn]="TAX010_05") = 0
ENDIF
```

Parameters used: Entity, PCycle

### 43. Tax - Production Allowance — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn]="TAX035_25") = RESULTLOOKUP([d/WPLn]="REV_05")
DATA([d/WPLn]="TAX035_10") = RESULTLOOKUP([d/WPLn]="TA20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
DATA([d/WPLn]="TAX035_15") = RESULTLOOKUP([d/WPLn]="TA20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") 
DATA([d/WPLn]="TAX035_12") = RESULTLOOKUP([d/WPLn]="GA_015",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
DATA([d/WPLn]="TAX035_17") = RESULTLOOKUP([d/WPLn]="TAX035_12") * RESULTLOOKUP([d/WPLn]="TAX035_15") / 100

IF RESULTLOOKUP([d/WPLn]="TAX035_10") < RESULTLOOKUP([d/WPLn]="TAX035_17") THEN
	DATA([d/WPLn]="TAX035_20") = RESULTLOOKUP([d/WPLn]="TAX035_10")
ELSE
	DATA([d/WPLn]="TAX035_20") = RESULTLOOKUP([d/WPLn]="TAX035_17")
ENDIF

DATA([d/WPLn]="TAX035_05") = RESULTLOOKUP([d/WPLn]="TAX035_25") * RESULTLOOKUP([d/WPLn]="TAX035_20")
```

Parameters used: Entity, PCycle

### 44. Tax - CAPEX Components — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

// Oil
DATA([d/WPLn]="TAX040_05_05_05") = RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_110")
DATA([d/WPLn]="TAX040_05_05_10") = RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_120")
DATA([d/WPLn]="TAX040_05_05_15") = RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_121") + RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_124")

DATA([d/WPLn]="TAX040_05_10") = RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_130")
DATA([d/WPLn]="TAX040_05_15") = 
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_132") + 
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_136") +
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_138") + 
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_139")
DATA([d/WPLn]="TAX040_05_20") = 
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_101") + 
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_102") +
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_134") + 
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_140") +
		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_141")
		
// Gas
DATA([d/WPLn]="TAX040_10_05_05") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_110")
DATA([d/WPLn]="TAX040_10_05_10") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_120")
DATA([d/WPLn]="TAX040_10_05_15") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_121") + RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_124")

DATA([d/WPLn]="TAX040_10_10") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_130")
DATA([d/WPLn]="TAX040_10_15") = 
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_132") + 
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_136") +
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_138") + 
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_139")
DATA([d/WPLn]="TAX040_10_20") = 
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_101") + 
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_102") +
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_134") + 
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_140") +
		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_141")
```

Parameters used: Entity, PCycle

### 45. Tax - CAPEX Amortisation — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

// Amortised costs
// TAX045_05_10	Amortised Oil Capex (Facilities+Drilling)
// TAX045_05_15	Amortised Other Oil Capex
// TAX045_05_20	Amortised Gas Capex (Facilities+Drilling)
// TAX045_05_25	Amortised Other Gas Capex

// Oil - facilities & drilling
DATA([d/WPLn]="TAX045_05_10") = 
	// Current year 1st year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_05_10") + RESULTLOOKUP([d/WPLn]="TAX040_05_15")) * 
	 RESULTLOOKUP([d/WPLn]="TA05_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +
	// Prior year 2nd year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))) * 
	 RESULTLOOKUP([d/WPLn]="TA05_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +
	// Year-3 using 3rd year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(2,"YEAR",[d/Date]))) * 
	 RESULTLOOKUP([d/WPLn]="TA05_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +		
	// Year-4 using 4th year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(3,"YEAR",[d/Date]))) * 
	 RESULTLOOKUP([d/WPLn]="TA05_20",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +	
	// Year-5 using 5th year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(4,"YEAR",[d/Date]))) * 
	 RESULTLOOKUP([d/WPLn]="TA05_25",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100)
	
// Oil - other
DATA([d/WPLn]="TAX045_05_15") = 
	// Current year 1st year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_05_20") * 
	 RESULTLOOKUP([d/WPLn]="TA05_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +
	// Prior year 2nd year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_05_20",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) * 
	 RESULTLOOKUP([d/WPLn]="TA05_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +
	// Year-3 using 3rd year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_05_20",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) * 
	 RESULTLOOKUP([d/WPLn]="TA05_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +		
	// Year-4 using 4th year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_05_20",[d/Date]=PREVIOUS(3,"YEAR",[d/Date]))  * 
	 RESULTLOOKUP([d/WPLn]="TA05_20",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +	
	// Year-5 using 5th year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_05_20",[d/Date]=PREVIOUS(4,"YEAR",[d/Date]))  * 
	 RESULTLOOKUP([d/WPLn]="TA05_25",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100)

// Gas - facilities & drilling
DATA([d/WPLn]="TAX045_05_20") = 
	// Current year 1st year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_10_10") + RESULTLOOKUP([d/WPLn]="TAX040_10_15")) * 
	 RESULTLOOKUP([d/WPLn]="TA05_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +
	// Prior year 2nd year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))) * 
	 RESULTLOOKUP([d/WPLn]="TA05_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +
	// Year-3 using 3rd year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(2,"YEAR",[d/Date]))) * 
	 RESULTLOOKUP([d/WPLn]="TA05_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +		
	// Year-4 using 4th year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(3,"YEAR",[d/Date]))) * 
	 RESULTLOOKUP([d/WPLn]="TA05_20",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +	
	// Year-5 using 5th year write off %
	((RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(4,"YEAR",[d/Date]))) * 
	 RESULTLOOKUP([d/WPLn]="TA05_25",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100)

// Gas - other
DATA([d/WPLn]="TAX045_05_25") = 
	// Current year 1st year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_10_20") * 
	 RESULTLOOKUP([d/WPLn]="TA05_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +
	// Prior year 2nd year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_10_20",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) * 
	 RESULTLOOKUP([d/WPLn]="TA05_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +
	// Year-3 using 3rd year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_10_20",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) * 
	 RESULTLOOKUP([d/WPLn]="TA05_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +		
	// Year-4 using 4th year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_10_20",[d/Date]=PREVIOUS(3,"YEAR",[d/Date]))  * 
	 RESULTLOOKUP([d/WPLn]="TA05_20",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100) +	
	// Year-5 using 5th year write off %
	(RESULTLOOKUP([d/WPLn]="TAX040_10_20",[d/Date]=PREVIOUS(4,"YEAR",[d/Date]))  * 
	 RESULTLOOKUP([d/WPLn]="TA05_25",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") / 100)
```

Parameters used: Entity, PCycle

### 46. Tax - Capital allowance for PPT — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

VARIABLEMEMBER #ASSESSABLE OF [d/WPLn]
VARIABLEMEMBER #LIMIT_PARAM OF [d/WPLn]
VARIABLEMEMBER #AMORT_CAPEX OF [d/WPLn]

// TAX050_05	Capital Allowance for PPT (result)
// TAX050_10	Investment Capital Allowance
// TAX050_10_05	In-year Investment CA Rate (%)
// TAX050_10_10	Total CAPEX – Oil
// TAX050_10_15	Total CAPEX – Gas
// TAX050_15	Capital Allowance Limit
// TAX050_15_05	Restriction on Assessible Profit (%)
// TAX050_15_10	Mark-up on In-year Investment Allowance (%)
// TAX050_20	Assessable Profit – PPT base
// TAX050_20_05	Oil Revenue
// TAX050_20_10	Less: PIA Production based royalty – Oil
// TAX050_20_15	Less: PIA Price based royalty – Oil
// TAX050_20_20	Less: PA Production based royalty – Oil
// TAX050_20_25	Less: PA Price based royalty – Oil
// TAX050_20_30	Less: Total OPEX – Oil
// TAX050_20_35	Less: Development Levy – Oil

// Amort capex
DATA([d/WPLn]=#AMORT_CAPEX) = 
	RESULTLOOKUP([d/WPLn]="TAX045_05_10") + RESULTLOOKUP([d/WPLn]="TAX045_05_15") +
	RESULTLOOKUP([d/WPLn]="TAX045_05_20") + RESULTLOOKUP([d/WPLn]="TAX045_05_25")
	
// TAX050_10	Investment Capital Allowance
DATA([d/WPLn]="TAX050_10_05") = RESULTLOOKUP([d/WPLn]="TA30_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
DATA([d/WPLn]="TAX050_10_10") = RESULTLOOKUP([d/WPLn]="CST05_15")
DATA([d/WPLn]="TAX050_10_15") = RESULTLOOKUP([d/WPLn]="CST05_20")

// TAX050_20	Assessable Profit – PPT base
DATA([d/WPLn]="TAX050_20_05") = RESULTLOOKUP([d/WPLn]="REV_10")
DATA([d/WPLn]="TAX050_20_10") = 0-RESULTLOOKUP([d/WPLn]="RC15_05")
DATA([d/WPLn]="TAX050_20_15") = 0-RESULTLOOKUP([d/WPLn]="RC20_10")
DATA([d/WPLn]="TAX050_20_20") = 0-RESULTLOOKUP([d/WPLn]="RC30_05")
DATA([d/WPLn]="TAX050_20_25") = 0-RESULTLOOKUP([d/WPLn]="RC35_10")
DATA([d/WPLn]="TAX050_20_30") = 0-RESULTLOOKUP([d/WPLn]="CST05_05")
DATA([d/WPLn]="TAX050_20_35") = 0-RESULTLOOKUP([d/WPLn]="TAX005_05")

DATA([d/WPLn]=#ASSESSABLE) = 
	RESULTLOOKUP([d/WPLn]="TAX050_20_05") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_10") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_15") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_20") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_25") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_30") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_35")

DATA([d/WPLn]="TAX050_15_05") = RESULTLOOKUP([d/WPLn]="TA30_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="202612")
DATA([d/WPLn]="TAX050_15_10") = RESULTLOOKUP([d/WPLn]="TA30_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="202612")

// Investment Capital Allowance
DATA([d/WPLn]="TAX050_10") = 
	ROUND (RESULTLOOKUP([d/WPLn]="TAX050_10_05") * 
	(RESULTLOOKUP([d/WPLn]="TAX050_10_10") + RESULTLOOKUP([d/WPLn]="TAX050_10_15")),0) / 100

// Capital allowance limit
DATA([d/WPLn]=#LIMIT_PARAM) = 
	((RESULTLOOKUP([d/WPLn]="TAX050_15_05") * RESULTLOOKUP([d/WPLn]=#ASSESSABLE)) / 100) -
	((RESULTLOOKUP([d/WPLn]="TAX050_15_10") * RESULTLOOKUP([d/WPLn]="TAX050_10")) / 100)
	
IF RESULTLOOKUP([d/WPLn]=#LIMIT_PARAM) > 0 THEN
	DATA([d/WPLn]="TAX050_15") = RESULTLOOKUP([d/WPLn]=#LIMIT_PARAM)
ELSE
	DATA([d/WPLn]="TAX050_15") = 0
ENDIF

IF RESULTLOOKUP([d/WPLn]=#AMORT_CAPEX) < RESULTLOOKUP([d/WPLn]=#LIMIT_PARAM)  THEN
	DATA([d/WPLn]="TAX050_05") = RESULTLOOKUP([d/WPLn]=#AMORT_CAPEX)
ELSE
	DATA([d/WPLn]="TAX050_05") = RESULTLOOKUP([d/WPLn]=#LIMIT_PARAM)
ENDIF
```

Parameters used: Entity, PCycle

### 47. Tax - CA Limit Rolling Balance (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

VARIABLEMEMBER #TAX050_20 OF [d/WPLn]
VARIABLEMEMBER #PARAM1 OF [d/WPLn]
VARIABLEMEMBER #PARAM2 OF [d/WPLn]

/*
TAX055_05	CA Limit – CIT sec 24(7) (%)
TAX055_10	Opening Balance CA Limit – Oil
TAX055_15	In-year addition – Oil
TAX055_20	Allowable deduction – Oil
TAX055_25	Closing Balance CA Limit – Oil
TAX055_30	Deductible Amortised Oil Capex
TAX055_35	Deductible Amortised Other Oil Capex
*/


DATA([d/WPLn]="TAX055_05") = RESULTLOOKUP([d/WPLn]="TA10_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX055_15") = RESULTLOOKUP([d/WPLn]="TAX045_05_10") + RESULTLOOKUP([d/WPLn]="TAX045_05_15")

DATA([d/WPLn]="TAX055_35") = RESULTLOOKUP([d/WPLn]="TAX045_05_15") 

DATA([d/WPLn]=#TAX050_20) =
	RESULTLOOKUP([d/WPLn]="TAX050_20_05") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_10") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_15") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_20") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_25") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_30") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_35")

IF RESULTLOOKUP([d/WPLn]=#TAX050_20) < 0 THEN
	DATA([d/WPLn]="TAX055_20") = 0
ELSE
	DATA([d/WPLn]=#PARAM1) = RESULTLOOKUP([d/WPLn]="TAX055_10") + RESULTLOOKUP([d/WPLn]="TAX055_15")
	DATA([d/WPLn]=#PARAM2) = ROUND (RESULTLOOKUP([d/WPLn]="TAX055_05") * RESULTLOOKUP([d/WPLn]= #TAX050_20) / 100, 0)
	
	IF RESULTLOOKUP([d/WPLn] = #PARAM1) < RESULTLOOKUP([d/WPLn] = #PARAM2) THEN
		DATA([d/WPLn]="TAX055_20") = RESULTLOOKUP([d/WPLn] = #PARAM1)
	ELSE
		DATA([d/WPLn]="TAX055_20") = RESULTLOOKUP([d/WPLn] = #PARAM2)
	ENDIF
ENDIF

DATA([d/WPLn]="TAX055_25") = 
	RESULTLOOKUP([d/WPLn] = "TAX055_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) +
	RESULTLOOKUP([d/WPLn] = "TAX055_15") -
	RESULTLOOKUP([d/WPLn] = "TAX055_20")

DATA([d/WPLn]="TAX055_30") = 
	RESULTLOOKUP([d/WPLn] = "TAX055_20") -
	RESULTLOOKUP([d/WPLn] = "TAX055_35")
```

Parameters used: Entity, PCycle

### 48. Tax - CA Limit Rolling Balance (Gas) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

VARIABLEMEMBER #TAX010_15 OF [d/WPLn]
VARIABLEMEMBER #PARAM1 OF [d/WPLn]
VARIABLEMEMBER #PARAM2 OF [d/WPLn]

/*
TAX060	CA Limit Balance – Gas
TAX060_05	Opening Balance CA Limit – Gas
TAX060_10	In-year addition – Gas
TAX060_15	Allowable deduction – Gas
TAX060_20	Closing Balance CA Limit – Gas
TAX060_25	Deductible Amortised Gas Capex
TAX060_30	Deductible Amortised Other Gas Capex
*/

DATA([d/WPLn]="TAX060_30") = RESULTLOOKUP([d/WPLn]="TAX045_05_25")

DATA([d/WPLn]="TAX060_10") = RESULTLOOKUP([d/WPLn]="TAX045_05_20") + RESULTLOOKUP([d/WPLn]="TAX045_05_25")

DATA([d/WPLn]=#TAX010_15) =
	RESULTLOOKUP([d/WPLn]="TAX010_15_05") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_10") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_15") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_20") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_25") +
	RESULTLOOKUP([d/WPLn]="TAX010_15_30")


IF RESULTLOOKUP([d/WPLn]=#TAX010_15) < 0 THEN
	DATA([d/WPLn]="TAX060_15") = 0
ELSE
	DATA([d/WPLn]=#PARAM1) = RESULTLOOKUP([d/WPLn]="TAX060_05") + RESULTLOOKUP([d/WPLn]="TAX060_10")
	DATA([d/WPLn]=#PARAM2) = ROUND (RESULTLOOKUP([d/WPLn]="TAX055_05") * RESULTLOOKUP([d/WPLn]= #TAX010_15) / 100, 0)
	
	IF RESULTLOOKUP([d/WPLn] = #PARAM1) < RESULTLOOKUP([d/WPLn] = #PARAM2) THEN
		DATA([d/WPLn]="TAX060_15") = RESULTLOOKUP([d/WPLn] = #PARAM1)
	ELSE
		DATA([d/WPLn]="TAX060_15") = RESULTLOOKUP([d/WPLn] = #PARAM2)
	ENDIF
ENDIF

DATA([d/WPLn]="TAX060_20") = 
	RESULTLOOKUP([d/WPLn] = "TAX060_20",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) +
	RESULTLOOKUP([d/WPLn] = "TAX060_10") -
	RESULTLOOKUP([d/WPLn] = "TAX060_15")

DATA([d/WPLn]="TAX060_25") = 
	RESULTLOOKUP([d/WPLn] = "TAX060_15") -
	RESULTLOOKUP([d/WPLn] = "TAX060_30")
```

Parameters used: Entity, PCycle

### 49. Tax - Chargeable Profit for PPT — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

VARIABLEMEMBER #TAX050_20 OF [d/WPLn]

DATA([d/WPLn] = #TAX050_20) = 
	RESULTLOOKUP([d/WPLn]="TAX050_20_05") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_10") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_15") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_20") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_25") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_30") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_35")
	
DATA([d/WPLn]="TAX065_05") = 
	RESULTLOOKUP([d/WPLn] = #TAX050_20) -
	RESULTLOOKUP([d/WPLn] = "TAX055_20")
```

Parameters used: Entity, PCycle

### 50. Tax - Hydrocarbon Tax (CPR Limit & HT Payable) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

VARIABLEMEMBER #PARAM1 OF [d/WPLn]
VARIABLEMEMBER #PARAM2 OF [d/WPLn]

DATA([d/WPLn] = "TAX070_05") = RESULTLOOKUP([d/WPLn]="TA15_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
DATA([d/WPLn] = "TAX070_55") = RESULTLOOKUP([d/WPLn]="TL15_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
DATA([d/WPLn] = "TAX070_60") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
DATA([d/WPLn] = "TAX070_30") = RESULTLOOKUP([d/WPLn]="CST05_05")

DATA([d/WPLn] = "TAX070_40") = 
	RESULTLOOKUP([d/WPLn]="RC15_05") +
	RESULTLOOKUP([d/WPLn]="RC20_10") +
	RESULTLOOKUP([d/WPLn]="TAX040_05_05") +
	RESULTLOOKUP([d/WPLn]="TAX055_30") +
	RESULTLOOKUP([d/WPLn]="RC30_05") +
	RESULTLOOKUP([d/WPLn]="RC35_10")

DATA([d/WPLn] = "TAX070_35") = RESULTLOOKUP([d/WPLn]="TAX070_30") + RESULTLOOKUP([d/WPLn]="TAX070_40")
DATA([d/WPLn] = "TAX070_15") = RESULTLOOKUP([d/WPLn]="TAX070_35")

DATA([d/WPLn] = #PARAM1) = RESULTLOOKUP([d/WPLn]="TAX070_05") * RESULTLOOKUP([d/WPLn]="REV_10") / 100
DATA([d/WPLn] = #PARAM2) = RESULTLOOKUP([d/WPLn]="TAX070_35") + RESULTLOOKUP([d/WPLn]="TAX070_10")

IF RESULTLOOKUP([d/WPLn]=#PARAM1) < RESULTLOOKUP([d/WPLn]=#PARAM2) THEN
	DATA([d/WPLn] = "TAX070_20") = RESULTLOOKUP([d/WPLn]=#PARAM1)
ELSE
	DATA([d/WPLn] = "TAX070_20") = RESULTLOOKUP([d/WPLn]=#PARAM2)
ENDIF

DATA([d/WPLn] = "TAX070_25") = RESULTLOOKUP([d/WPLn]="TAX070_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) +
	RESULTLOOKUP([d/WPLn]="TAX070_15") -
	RESULTLOOKUP([d/WPLn]="TAX070_20")

DATA([d/WPLn] = "TAX070_45") = RESULTLOOKUP([d/WPLn]="TAX070_20")

DATA([d/WPLn] = "TAX070_50") = RESULTLOOKUP([d/WPLn]="REV_10") - RESULTLOOKUP([d/WPLn]="TAX035_05") - RESULTLOOKUP([d/WPLn] = "TAX070_45")

DATA([d/WPLn] = #PARAM1) = (RESULTLOOKUP([d/WPLn]="TAX070_50") * RESULTLOOKUP([d/WPLn]="TAX070_55") / 100) * RESULTLOOKUP([d/WPLn]="TAX070_60")

IF RESULTLOOKUP([d/WPLn] = #PARAM1) > 0 THEN
	DATA([d/WPLn] = "TAX070_65") = RESULTLOOKUP([d/WPLn] = #PARAM1)
ELSE
	DATA([d/WPLn] = "TAX070_65") = 0
ENDIF

DATA([d/WPLn] = "TAX070_70") = RESULTLOOKUP([d/WPLn] = "TAX070_65") * RESULTLOOKUP([d/WPLn] = "AMT_90")
```

Parameters used: Entity, PCycle

### 51. Tax - Allowable Costs & Chargeable Profit CITA (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn] = "TAX075_05") = 
	RESULTLOOKUP([d/WPLn]="RC15_05") +
	RESULTLOOKUP([d/WPLn]="RC20_10") +
	RESULTLOOKUP([d/WPLn]="CST05_05") +
	RESULTLOOKUP([d/WPLn]="TAX005_05") +
	RESULTLOOKUP([d/WPLn]="TAX015_05") +
	RESULTLOOKUP([d/WPLn]="TAX025_05") +
	RESULTLOOKUP([d/WPLn]="TAX040_05_05") + 
	RESULTLOOKUP([d/WPLn]="TAX055_30") + 
	RESULTLOOKUP([d/WPLn]="TAX055_35") + 
	RESULTLOOKUP([d/WPLn]="RC30_05") + 
	RESULTLOOKUP([d/WPLn]="RC35_10")

DATA([d/WPLn] = "TAX075_10") = 	
	RESULTLOOKUP([d/WPLn]="REV_10") -
	RESULTLOOKUP([d/WPLn]="TAX075_05")
```

Parameters used: Entity, PCycle

### 52. Tax - Allowable Costs & Chargeable Profit CITA (Gas) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

VARIABLEMEMBER #PARAM1 OF [d/WPLn]

IF RESULTLOOKUP([d/WPLn]="TAX070_60") = 0 THEN
	DATA([d/WPLn] = #PARAM1) = RESULTLOOKUP([d/WPLn]="TAX060_25")
ELSE
	DATA([d/WPLn] = #PARAM1) = 0
ENDIF

DATA([d/WPLn] = "TAX080_05") = 
	RESULTLOOKUP([d/WPLn]=#PARAM1) +
	RESULTLOOKUP([d/WPLn]="RC25_20") +
	RESULTLOOKUP([d/WPLn]="CST05_10") +
	RESULTLOOKUP([d/WPLn]="TAX010_05") +
	RESULTLOOKUP([d/WPLn]="TAX020_05") +
	RESULTLOOKUP([d/WPLn]="TAX030_05") + 
	RESULTLOOKUP([d/WPLn]="RC40_20")

DATA([d/WPLn] = "TAX080_10") = 	
	RESULTLOOKUP([d/WPLn]="REV_20") -
	RESULTLOOKUP([d/WPLn]="TAX080_05")
```

Parameters used: Entity, PCycle

### 53. Tax - PPT Tax (Oil) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn] = "TAX085_10") = RESULTLOOKUP([d/WPLn]="TL05_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn] = "TAX085_20") = RESULTLOOKUP([d/WPLn]="TAX065_05") * RESULTLOOKUP([d/WPLn]="TAX085_10") * RESULTLOOKUP([d/WPLn]="SET10_05") / 100

IF RESULTLOOKUP([d/WPLn]="TAX085_20") < 0 THEN
	DATA([d/WPLn] = "TAX085_20") = 0
ENDIF

DATA([d/WPLn] = "TAX085_25") = RESULTLOOKUP([d/WPLn]="TAX085_20") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 54. Tax - CITA (Oil & Gas) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn] = "TAX090_05") = RESULTLOOKUP([d/WPLn]="TL05_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
DATA([d/WPLn] = "TAX090_10") = RESULTLOOKUP([d/WPLn]="SET10_10")

DATA([d/WPLn] = "TAX090_15") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX075_10") * RESULTLOOKUP([d/WPLn]="SET10_10") / 100
IF RESULTLOOKUP([d/WPLn]="TAX090_15") < 0 THEN DATA([d/WPLn] = "TAX090_15") = 0 ENDIF

DATA([d/WPLn] = "TAX090_20") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX080_10") * RESULTLOOKUP([d/WPLn]="SET10_10") / 100
IF RESULTLOOKUP([d/WPLn]="TAX090_20") < 0 THEN DATA([d/WPLn] = "TAX090_20") = 0 ENDIF

DATA([d/WPLn] = "TAX090_25") = RESULTLOOKUP([d/WPLn]="TAX090_15") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
DATA([d/WPLn] = "TAX090_30") = RESULTLOOKUP([d/WPLn]="TAX090_20") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 55. GL Entries — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CR")
// MEMBERSET [d/WPLn] = ("CST20", "SET10_05")
MEMBERSET [d/GL] = ("#")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#")
MEMBERSET [d/PPP_Currency] = "USD"

DATA([d/Measures] = "GC_CR", [d/GL] = "6011009", [d/PPP_EntryNr] = "UP_0005") = 0
DATA([d/Measures] = "GC_CR", [d/GL] = "6022022", [d/PPP_EntryNr] = "UP_0005") = 0
DATA([d/Measures] = "GC_CR", [d/GL] = "5230001", [d/PPP_EntryNr] = "UP_0005") = 0
DATA([d/Measures] = "GC_CR", [d/GL] = "4101010", [d/PPP_EntryNr] = "UP_0005") = 0
DATA([d/Measures] = "GC_CR", [d/GL] = "4600105", [d/PPP_EntryNr] = "UP_0005") = 0
DATA([d/Measures] = "GC_CR", [d/GL] = "5150009", [d/PPP_EntryNr] = "UP_0005") = 0
DATA([d/Measures] = "GC_CR", [d/GL] = "4110003", [d/PPP_EntryNr] = "UP_0005") = 0

// Revenue
DATA([d/Measures] = "GC_CR", [d/GL] = "6011008", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "REV_30", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Other Income
DATA([d/Measures] = "GC_CR", [d/GL] = "7010023", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "REV_35", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Royalty
DATA([d/Measures] = "GC_CR", [d/GL] = "5100007", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "RC_TOT_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Direct Cost
DATA([d/Measures] = "GC_CR", [d/GL] = "4101006", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_GFP", [d/PPP_Currency] = "#")
// Apportioned Overheads
DATA([d/Measures] = "GC_CR", [d/GL] = "5010036", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned Salaries
DATA([d/Measures] = "GC_CR", [d/GL] = "5010001", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned General Depreciation
DATA([d/Measures] = "GC_CR", [d/GL] = "4112001", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_15", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// COS Depreciation
DATA([d/Measures] = "GC_CR", [d/GL] = "4202026", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_220", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_15", [d/PPP_Currency] = "#") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_15", [d/PPP_Currency] = "#")
// Depletion
DATA([d/Measures] = "GC_CR", [d/GL] = "5230003", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_220", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_16", [d/PPP_Currency] = "#") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_16", [d/PPP_Currency] = "#")
// Apportioned Provision for Impairment
DATA([d/Measures] = "GC_CR", [d/GL] = "5230006", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_20", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned Corporate Overhead
DATA([d/Measures] = "GC_CR", [d/GL] = "5080044", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_25", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Finance Cost
DATA([d/Measures] = "GC_CR", [d/GL] = "FINEXP_005", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_30", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Apportioned Taxes
DATA([d/Measures] = "GC_CR", [d/GL] = "5100005", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_35", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
// Proposed Dividend 
//DATA([d/Measures] = "GC_CR", [d/GL] = "5100005", [d/PPP_EntryNr] = "UP_0005") = 
//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_", [d/GL] = "#", [d/PPP_EntryNr] = "#")
// Add: Apportioned General Depreciation
// Add: COS Depreciation
// Add:Depletion
// Add: Apportioned Provision for Impairment
// Less: Asset Projects
// Less: Apportioned Movables
// Less: Changes in Working Capital
// Net Borrowing
```

Parameters used: Entity, PCycle
