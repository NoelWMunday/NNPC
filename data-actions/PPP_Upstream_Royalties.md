# PPP_Upstream_Royalties

> PPP Upstream - Royalties

| | |
|---|---|
| SAC id | `F4851684BFC29D7E2AE8285F175632F1` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-26T09:51:38.081Z by NMUNDAY |
| Called by | [PPP_Upstream_All_Calculations](PPP_Upstream_All_Calculations.md) |
| Used in stories | [PPP_UStream](../stories/PPP_UStream.md) |

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
| 2 | Initialise common entity totals | SCRIPT |  |
| 3 | Royalties - Tranch volumes | SCRIPT |  |
| 4 | Royalties - Values (Oil) | SCRIPT |  |
| 5 | PIA Royalties - Production based (Oil) | SCRIPT |  |
| 6 | PIA Royalties - Equity production based (Oil) | SCRIPT |  |
| 7 | PIA Royalties - Price based (Oil) | SCRIPT |  |
| 8 | PIA Royalties - Gas | SCRIPT |  |
| 9 | Royalties - PA Production based (Oil) | SCRIPT |  |
| 10 | Royalties - PA Price based (Oil) | SCRIPT |  |
| 11 | Royalties - PA Gas | SCRIPT |  |
| 12 | Royalties - Summary total | SCRIPT |  |
| 13 | Gas flare penalty | SCRIPT |  |
| 14 | Costs - CAPEX Oil | SCRIPT |  |
| 15 | Costs - CAPEX Gas | SCRIPT |  |
| 16 | Costs - OPEX Oil | SCRIPT |  |
| 17 | Costs - OPEX Gas | SCRIPT |  |
| 18 | Total CAPEX / OPEX Equity | SCRIPT |  |
| 19 | Total OPEX to common entity | SCRIPT |  |
| 20 | Entities share in OPEX | SCRIPT |  |
| 21 | Development cost | SCRIPT |  |
| 22 | GL Entries | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] ,"CST05" )
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

### 2. Initialise common entity totals — SCRIPT

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

### 3. Royalties - Tranch volumes — SCRIPT

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
DATA([d/WPLn] = #TRANCH1) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
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

DATA([d/WPLn] = #TRANCH2) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
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
							
DATA([d/WPLn] = #TRANCH3) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
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
														
DATA([d/WPLn] = #TRANCH4) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
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

### 4. Royalties - Values (Oil) — SCRIPT

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
DATA([d/WPLn] = #RR_TRANCH1) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_005_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_010_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_015_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_020_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_025_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_030_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))

DATA([d/WPLn] = #RR_TRANCH2) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
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
							
DATA([d/WPLn] = #RR_TRANCH3) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
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
														
DATA([d/WPLn] = #RR_TRANCH4) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000") * 
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

### 5. PIA Royalties - Production based (Oil) — SCRIPT

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

### 6. PIA Royalties - Equity production based (Oil) — SCRIPT

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
							RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 7. PIA Royalties - Price based (Oil) — SCRIPT

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
							
DATA([d/WPLn]="RC20_15") = RESULTLOOKUP([d/WPLn]="RC20_10") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 8. PIA Royalties - Gas — SCRIPT

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
							(RESULTLOOKUP([d/WPLn]="SET20_10",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_010",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_15",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_015",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_20",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_020",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_25",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_025",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_30",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_030",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_35",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR04_035",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
							
DATA([d/WPLn]="RC25_20") = RESULTLOOKUP([d/WPLn] = #RR_RATE) * RESULTLOOKUP([d/WPLn]="REV_20") * RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")

DATA([d/WPLn]="RC25_25") = RESULTLOOKUP([d/WPLn] = "RC25_20") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 9. Royalties - PA Production based (Oil) — SCRIPT

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
							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_010_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_015_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_020_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_025_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR01_030_00",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))


DATA([d/WPLn]="RC30_05") = RESULTLOOKUP([d/WPLn] = #RR_RATE) * RESULTLOOKUP([d/WPLn]="REV_10") * RESULTLOOKUP([d/WPLn]="SET10_05", [d/Date] = "000000")

DATA([d/WPLn]="RC30_10") = RESULTLOOKUP([d/WPLn] = "RC30_05") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 10. Royalties - PA Price based (Oil) — SCRIPT

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

### 11. Royalties - PA Gas — SCRIPT

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
DATA([d/WPLn] = #RR_RATE) =  (RESULTLOOKUP([d/WPLn]="SET20_20",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR04_020",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_25",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR04_025",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
							(RESULTLOOKUP([d/WPLn]="SET20_30",[d/Date]="000000") * 
							 RESULTLOOKUP([d/Measures]="Royalty_PA",[d/WPLn]="RR04_030",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
							
							
DATA([d/WPLn]="RC40_20") = RESULTLOOKUP([d/WPLn] = #RR_RATE) * RESULTLOOKUP([d/WPLn]="REV_20")

DATA([d/WPLn]="RC40_25") = RESULTLOOKUP([d/WPLn] = "RC40_20") * 
							RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 12. Royalties - Summary total — SCRIPT

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

### 13. Gas flare penalty — SCRIPT

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

### 14. Costs - CAPEX Oil — SCRIPT

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

IF [d/PPP_EntryNr] != "#" THEN
	DATA.APPEND([d/WPLn] = "CST05_15", [d/PPP_EntryNr] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_200")
ENDIF
```

Parameters used: Entity, PCycle

### 15. Costs - CAPEX Gas — SCRIPT

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

IF [d/PPP_EntryNr] != "#" THEN
	DATA.APPEND([d/WPLn] = "CST05_20", [d/PPP_EntryNr] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_210")
ENDIF
```

Parameters used: Entity, PCycle

### 16. Costs - OPEX Oil — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// This is only productive opex costs

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

IF [d/PPP_EntryNr] != "#" THEN
	DATA.APPEND([d/WPLn] = "CST05_05", [d/PPP_EntryNr] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_220")
ENDIF
```

Parameters used: Entity, PCycle

### 17. Costs - OPEX Gas — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// This is only productive opex costs

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

IF [d/PPP_EntryNr] != "#" THEN
	DATA.APPEND([d/WPLn] = "CST05_10", [d/PPP_EntryNr] = "#") = RESULTLOOKUP([d/WPLn] = "AMT_230")
ENDIF
```

Parameters used: Entity, PCycle

### 18. Total CAPEX / OPEX Equity — SCRIPT

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


DATA([d/WPLn]="CST10_05") = 
		RESULTLOOKUP([d/WPLn]="CST05_05")  * 
		RESULTLOOKUP([d/WPLn]="AMT_90") / 100

DATA([d/WPLn]="CST10_10") = 
		RESULTLOOKUP([d/WPLn]="CST05_10") * 
		RESULTLOOKUP([d/WPLn]="AMT_90") / 100

DATA([d/WPLn]="CST10_15") = 
		RESULTLOOKUP([d/WPLn]="CST05_15") * 
		RESULTLOOKUP([d/WPLn]="AMT_90") / 100

DATA([d/WPLn]="CST10_20") = 
		RESULTLOOKUP([d/WPLn]="CST05_20") * 
		RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 19. Total OPEX to common entity — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Note the OPEX line item for dimension WPLn is determined by the entity property
// so that it's dynamic and can be used for JV's and PSC's. For NU03 the JV's point to 
// REV3_05_05 on the central node. This JV running will append it's opex to the node so 
// the node aggregates all JV opex.

// Then on the apportionment calc the JV will read the total back from the node to this id
// so it can reflect the total it used in it's own books. Aggregating the JV's should = the node
// but including the node as well should give x2 JV opex costs

// Also note the JV's OPEX excludes non-production costs like gas flare penalty so the node UAP_OPEX_CST
// excludes any non-production costs against both WPLn oil and gas

// The JV has OPEX of it's own used to calculate it's % share of all JV OPEX and
// the % is applied to the JV HO / node to apportion the nodes OPEX to the JV

MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV3_05_05","CST05_05","CST05_10")
MEMBERSET [d/PPP_EntryNr] = "#"
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

// Note: There is no entity scope so the entity selection parameter is not limiting this function otherwise running it for a 
// single JV will produce an incorrect result. However, the alternative (this approach), runs over all entities and simply
// checks if they have an OPEX central entity node allocated WPLn and if so updates that node because on initialisation it would
// have been reset to zero and now need updating. This then runs over all JV's, PSC's and other WP's of a central entity.
// Every entity running this data action will recalculate the central entities total (all central entities)

IF [d/PPP_Entity].[p/Ln_OPEX] != "#" THEN
	// For central node
	DATA.APPEND([d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup], [d/WPLn] = [d/PPP_Entity].[p/Ln_OPEX]) = 
		RESULTLOOKUP([d/WPLn] = "CST05_05") + 
		RESULTLOOKUP([d/WPLn] = "CST05_10")
	
	// For entity itself
	DATA([d/WPLn] = [d/PPP_Entity].[p/Ln_OPEX]) = 
		RESULTLOOKUP([d/WPLn] = "CST05_05") + 
		RESULTLOOKUP([d/WPLn] = "CST05_10")	
ENDIF
```

Parameters used: PCycle

### 20. Entities share in OPEX — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

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

VARIABLEMEMBER #ALLJVS OF [d/WPLn]
// Read the total OPEX from the common entity into this entities total opex line per the properties
// At this point don't know if it's JV or PSC or other but the correct WPLn will populate
DATA([d/WPLn] = #ALLJVS) = RESULTLOOKUP([d/WPLn] = [d/PPP_Entity].[p/Ln_OPEX], [d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup])

// This calculation works out the % share of JV, PSC and any other because not knowing if it's JV, PSC etc doesn't matter
// The non-zero WPLn's will popluate and the zero WPLn just return zero
IF RESULTLOOKUP([d/WPLn] = "REV3_05_05") > 0 THEN
	DATA([d/WPLn]="REV3_10_05") = (RESULTLOOKUP([d/WPLn]="CST05_05") + RESULTLOOKUP([d/WPLn]="CST05_10")) / RESULTLOOKUP([d/WPLn] = #ALLJVS)
	DATA([d/WPLn]="REV_34") = 0
ENDIF
```

Parameters used: Entity, PCycle

### 21. Development cost — SCRIPT

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

### 22. GL Entries — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CR")
MEMBERSET [d/WPLn] = ("RC_TOT_10", "#")
MEMBERSET [d/GL] = ("#","5100007","4500006")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#","UP_0005")
MEMBERSET [d/PPP_Currency] = ("#","USD")


// Royalty
DATA([d/Measures] = "GC_CR", [d/WPLn] = "#", [d/GL] = "5100007", [d/PPP_EntryNr] = "UP_0005", [d/PPP_Currency] = "USD") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "RC_TOT_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")

// Costs - Entities own costs, NNPC's share of
DATA([d/Measures] = "GC_CR", [d/WPLn] = "#", [d/GL] = "4500006", [d/PPP_EntryNr] = "UP_0005", [d/PPP_Currency] = "USD") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_15", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_20", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
```

Parameters used: Entity, PCycle
