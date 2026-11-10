# PPP_Upstream_Tax

> PPP Upstream - Taxation

| | |
|---|---|
| SAC id | `AC8D1684BFC501FD9340601FF47A5050` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-11-10T13:57:11.433Z by NMUNDAY |
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
| 2 | Development cost | SCRIPT | **DISABLED** |
| 3 | Tax - NDDC Levy Payable (Oil) | SCRIPT |  |
| 4 | Tax - NDDC Levy Payable (Gas) | SCRIPT |  |
| 5 | Tax - HCDT Fund Payable (Oil) | SCRIPT |  |
| 6 | Tax - HCDT Fund Payable (Gas) | SCRIPT |  |
| 7 | Tax - Development Levy (Oil) | SCRIPT |  |
| 8 | Tax - Development levy (Gas) | SCRIPT |  |
| 9 | Tax - Production Allowance | SCRIPT |  |
| 10 | Tax - CAPEX Components | SCRIPT |  |
| 11 | Tax - CAPEX Amortisation | SCRIPT |  |
| 12 | Tax - Capital allowance for PPT | SCRIPT |  |
| 13 | Tax - CA Limit Rolling Balance (Oil) | SCRIPT |  |
| 14 | Tax - CA Limit Rolling Balance (Gas) | SCRIPT |  |
| 15 | Tax - Chargeable Profit for PPT | SCRIPT |  |
| 16 | Tax - Hydrocarbon Tax (CPR Limit & HT Payable) | SCRIPT |  |
| 17 | Tax - Allowable Costs & Chargeable Profit CITA (Oil) | SCRIPT |  |
| 18 | Tax - Allowable Costs & Chargeable Profit CITA (Gas) | SCRIPT |  |
| 19 | Tax - PPT Tax (Oil) | SCRIPT |  |
| 20 | Tax - CITA (Oil & Gas) | SCRIPT |  |
| 21 | GL Entries | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_32","REV_26","REV_40",
					  BASEMEMBER([d/WPLn] ,"REV3_05"),
					  BASEMEMBER([d/WPLn] ,"TAX"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"

// TAX* are cleared so the rolling balances (steps 13, 14, 16) restart from this run
DELETE()
```

Parameters used: Entity, PCycle

### 2. Development cost — SCRIPT

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
DATA([d/WPLn] = #DRILLING) = RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_130", [d/PPP_Currency]="USD")
DATA([d/WPLn] = #DRILLING_FIFTH) = RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_130", [d/PPP_Currency]="USD") / 5

// 1/5 of "CAPEX Facilities Oil"
DATA([d/WPLn] = #FACILITIES) = 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_132", [d/PPP_Currency]="USD") +
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_136", [d/PPP_Currency]="USD") +	
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_138", [d/PPP_Currency]="USD") +	
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_139", [d/PPP_Currency]="USD")	
	
DATA([d/WPLn] = #FACILITIES_FIFTH) = RESULTLOOKUP([d/WPLn] = #FACILITIES) / 5

// Total Appraisal & Exploration Cost – Oil
DATA([d/WPLn] = #TAECO) = 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_110", [d/PPP_Currency]="USD") + 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_120", [d/PPP_Currency]="USD") + 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_121", [d/PPP_Currency]="USD") + 
	RESULTLOOKUP([d/WPLn] = "AMT_200", [d/PPP_EntryNr] = "UAP_124", [d/PPP_Currency]="USD")


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

### 3. Tax - NDDC Levy Payable (Oil) — SCRIPT

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

DATA([d/WPLn]="TAX025_15_05") = RESULTLOOKUP([d/WPLn]="CST05_05")
DATA([d/WPLn]="TAX025_15_10") = RESULTLOOKUP([d/WPLn]="CST05_15")

DATA([d/WPLn]="TAX025_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX025_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX025_10") * (
	RESULTLOOKUP([d/WPLn]="TAX025_15_05") +														   
	RESULTLOOKUP([d/WPLn]="TAX025_15_10")
),0) / 100
```

Parameters used: Entity, PCycle

### 4. Tax - NDDC Levy Payable (Gas) — SCRIPT

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

DATA([d/WPLn]="TAX030_15_05") = RESULTLOOKUP([d/WPLn]="CST05_10")
DATA([d/WPLn]="TAX030_15_10") = RESULTLOOKUP([d/WPLn]="CST05_20")

DATA([d/WPLn]="TAX030_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX030_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX030_10") * (
	RESULTLOOKUP([d/WPLn]="TAX030_15_05") +														   
	RESULTLOOKUP([d/WPLn]="TAX030_15_10")
),0) / 100
```

Parameters used: Entity, PCycle

### 5. Tax - HCDT Fund Payable (Oil) — SCRIPT

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

// HCDT basis = prior year operating expenditure (PIA s.240); CST05 holds the full year on December (Royalties LAST() rollup)
DATA([d/WPLn]="TAX015_15") = RESULTLOOKUP([d/WPLn]="CST05_05",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))

DATA([d/WPLn]="TAX015_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX015_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX015_15") * 
	RESULTLOOKUP([d/WPLn]="TAX015_10"
),0) / 100
```

Parameters used: Entity, PCycle

### 6. Tax - HCDT Fund Payable (Gas) — SCRIPT

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

// HCDT basis = prior year operating expenditure (PIA s.240); CST05 holds the full year on December (Royalties LAST() rollup)
DATA([d/WPLn]="TAX020_15") = RESULTLOOKUP([d/WPLn]="CST05_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))

DATA([d/WPLn]="TAX020_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

DATA([d/WPLn]="TAX020_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX020_15") * 
	RESULTLOOKUP([d/WPLn]="TAX020_10"
),0) / 100
```

Parameters used: Entity, PCycle

### 7. Tax - Development Levy (Oil) — SCRIPT

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
DATA([d/WPLn]="TAX005_15_20") = 0-RESULTLOOKUP([d/WPLn]="RC30_05") 
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

### 8. Tax - Development levy (Gas) — SCRIPT

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
DATA([d/WPLn]="TAX010_15_15") = 0-RESULTLOOKUP([d/WPLn]="CST05_10") 
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

### 9. Tax - Production Allowance — SCRIPT

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
// Oil price is a per-year central assumption (as in Revenue step 2 and Royalties) - no Date 000000
DATA([d/WPLn]="TAX035_12") = RESULTLOOKUP([d/WPLn]="GA_015",[d/PPP_Entity]="#",[d/Lock]="Central")
DATA([d/WPLn]="TAX035_17") = RESULTLOOKUP([d/WPLn]="TAX035_12") * RESULTLOOKUP([d/WPLn]="TAX035_15") / 100

IF RESULTLOOKUP([d/WPLn]="TAX035_10") < RESULTLOOKUP([d/WPLn]="TAX035_17") THEN
	DATA([d/WPLn]="TAX035_20") = RESULTLOOKUP([d/WPLn]="TAX035_10")
ELSE
	DATA([d/WPLn]="TAX035_20") = RESULTLOOKUP([d/WPLn]="TAX035_17")
ENDIF

DATA([d/WPLn]="TAX035_05") = RESULTLOOKUP([d/WPLn]="TAX035_25") * RESULTLOOKUP([d/WPLn]="TAX035_20")
```

Parameters used: Entity, PCycle

### 10. Tax - CAPEX Components — SCRIPT

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
// Capex inputs (USD, by UAP entry) are rolled into December of each year on Lock "#", EntryNr "#", Currency "#".
// Closed periods (Lock Hist_Open: prior years and CY YTD) are included, so amortisation (step 11) sees full years.
// Initialise (step 1) clears TAX*, so DATA.APPEND rebuilds the totals on every run.
MEMBERSET [d/Lock] = ("#","Hist_Open")
MEMBERSET [d/PPP_Currency] = ("#","USD")
MEMBERSET [d/PPP_EntryNr] = ("#","UAP_110","UAP_120","UAP_121","UAP_124","UAP_130","UAP_132","UAP_136","UAP_138","UAP_139","UAP_101","UAP_102","UAP_134","UAP_140","UAP_141")
MEMBERSET [d/WPLn] = ("AMT_200","AMT_210",
	"TAX040_05_05_05","TAX040_05_05_10","TAX040_05_05_15",
	"TAX040_05_10","TAX040_05_15","TAX040_05_20",
	"TAX040_10_05_05","TAX040_10_05_10","TAX040_10_05_15",
	"TAX040_10_10","TAX040_10_15","TAX040_10_20")

// Oil
IF [d/PPP_Currency] = "USD" AND [d/WPLn] = "AMT_200" THEN
	IF [d/PPP_EntryNr] = "UAP_110" THEN
		DATA.APPEND([d/WPLn] = "TAX040_05_05_05", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_120" THEN
		DATA.APPEND([d/WPLn] = "TAX040_05_05_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_121" OR [d/PPP_EntryNr] = "UAP_124" THEN
		DATA.APPEND([d/WPLn] = "TAX040_05_05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_130" THEN
		DATA.APPEND([d/WPLn] = "TAX040_05_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_132" OR [d/PPP_EntryNr] = "UAP_136" OR [d/PPP_EntryNr] = "UAP_138" OR [d/PPP_EntryNr] = "UAP_139" THEN
		DATA.APPEND([d/WPLn] = "TAX040_05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_101" OR [d/PPP_EntryNr] = "UAP_102" OR [d/PPP_EntryNr] = "UAP_134" OR [d/PPP_EntryNr] = "UAP_140" OR [d/PPP_EntryNr] = "UAP_141" THEN
		DATA.APPEND([d/WPLn] = "TAX040_05_20", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
	ENDIF
ENDIF

// Gas
IF [d/PPP_Currency] = "USD" AND [d/WPLn] = "AMT_210" THEN
	IF [d/PPP_EntryNr] = "UAP_110" THEN
		DATA.APPEND([d/WPLn] = "TAX040_10_05_05", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_120" THEN
		DATA.APPEND([d/WPLn] = "TAX040_10_05_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_121" OR [d/PPP_EntryNr] = "UAP_124" THEN
		DATA.APPEND([d/WPLn] = "TAX040_10_05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_130" THEN
		DATA.APPEND([d/WPLn] = "TAX040_10_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_132" OR [d/PPP_EntryNr] = "UAP_136" OR [d/PPP_EntryNr] = "UAP_138" OR [d/PPP_EntryNr] = "UAP_139" THEN
		DATA.APPEND([d/WPLn] = "TAX040_10_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
	ENDIF
	IF [d/PPP_EntryNr] = "UAP_101" OR [d/PPP_EntryNr] = "UAP_102" OR [d/PPP_EntryNr] = "UAP_134" OR [d/PPP_EntryNr] = "UAP_140" OR [d/PPP_EntryNr] = "UAP_141" THEN
		DATA.APPEND([d/WPLn] = "TAX040_10_20", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
	ENDIF
ENDIF
```

Parameters used: Entity, PCycle

### 11. Tax - CAPEX Amortisation — SCRIPT

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

### 12. Tax - Capital allowance for PPT — SCRIPT

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
// TAX050_20_40	Less: NDDC Levy Payable (Oil)
// TAX050_20_45	Less: HCDT Fund Payable - Oil

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
DATA([d/WPLn]="TAX050_20_40") = 0-RESULTLOOKUP([d/WPLn]="TAX025_05")
DATA([d/WPLn]="TAX050_20_45") = 0-RESULTLOOKUP([d/WPLn]="TAX015_05")

DATA([d/WPLn]=#ASSESSABLE) = 
	RESULTLOOKUP([d/WPLn]="TAX050_20_05") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_10") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_15") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_20") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_25") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_30") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_35") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_40") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_45")

DATA([d/WPLn]="TAX050_15_05") = RESULTLOOKUP([d/WPLn]="TA30_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
DATA([d/WPLn]="TAX050_15_10") = RESULTLOOKUP([d/WPLn]="TA30_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")

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

### 13. Tax - CA Limit Rolling Balance (Oil) — SCRIPT

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
	RESULTLOOKUP([d/WPLn]="TAX050_20_35") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_40") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_45")

// Rolling balance: years are processed in date order, so each opening is the prior year's closing from
// this run (Initialise clears TAX* first). Re-running gives the same result.
FOREACH [d/Date]

	DATA([d/WPLn]="TAX055_10") = RESULTLOOKUP([d/WPLn] = "TAX055_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))

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
		RESULTLOOKUP([d/WPLn] = "TAX055_10") +
		RESULTLOOKUP([d/WPLn] = "TAX055_15") -
		RESULTLOOKUP([d/WPLn] = "TAX055_20")

	DATA([d/WPLn]="TAX055_30") = 
		RESULTLOOKUP([d/WPLn] = "TAX055_20") -
		RESULTLOOKUP([d/WPLn] = "TAX055_35")

ENDFOR
```

Parameters used: Entity, PCycle

### 14. Tax - CA Limit Rolling Balance (Gas) — SCRIPT

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


// Rolling balance: years are processed in date order, so each opening is the prior year's closing from
// this run (Initialise clears TAX* first). Re-running gives the same result.
FOREACH [d/Date]

	DATA([d/WPLn]="TAX060_05") = RESULTLOOKUP([d/WPLn] = "TAX060_20",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))

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
		RESULTLOOKUP([d/WPLn] = "TAX060_05") +
		RESULTLOOKUP([d/WPLn] = "TAX060_10") -
		RESULTLOOKUP([d/WPLn] = "TAX060_15")

	DATA([d/WPLn]="TAX060_25") = 
		RESULTLOOKUP([d/WPLn] = "TAX060_15") -
		RESULTLOOKUP([d/WPLn] = "TAX060_30")

ENDFOR
```

Parameters used: Entity, PCycle

### 15. Tax - Chargeable Profit for PPT — SCRIPT

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
	RESULTLOOKUP([d/WPLn]="TAX050_20_35") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_40") +
	RESULTLOOKUP([d/WPLn]="TAX050_20_45")
	
DATA([d/WPLn]="TAX065_05") = 
	RESULTLOOKUP([d/WPLn] = #TAX050_20) -
	RESULTLOOKUP([d/WPLn] = "TAX055_20")
```

Parameters used: Entity, PCycle

### 16. Tax - Hydrocarbon Tax (CPR Limit & HT Payable) — SCRIPT

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
DATA([d/WPLn] = "TAX070_60") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")
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

// Rolling balance: years are processed in date order, so each opening is the prior year's closing from
// this run (Initialise clears TAX* first). Re-running gives the same result.
FOREACH [d/Date]

	DATA([d/WPLn] = "TAX070_10") = RESULTLOOKUP([d/WPLn]="TAX070_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))

	DATA([d/WPLn] = #PARAM1) = RESULTLOOKUP([d/WPLn]="TAX070_05") * RESULTLOOKUP([d/WPLn]="REV_10") / 100
	DATA([d/WPLn] = #PARAM2) = RESULTLOOKUP([d/WPLn]="TAX070_35") + RESULTLOOKUP([d/WPLn]="TAX070_10")

	IF RESULTLOOKUP([d/WPLn]=#PARAM1) < RESULTLOOKUP([d/WPLn]=#PARAM2) THEN
		DATA([d/WPLn] = "TAX070_20") = RESULTLOOKUP([d/WPLn]=#PARAM1)
	ELSE
		DATA([d/WPLn] = "TAX070_20") = RESULTLOOKUP([d/WPLn]=#PARAM2)
	ENDIF

	DATA([d/WPLn] = "TAX070_25") = RESULTLOOKUP([d/WPLn]="TAX070_10") +
		RESULTLOOKUP([d/WPLn]="TAX070_15") -
		RESULTLOOKUP([d/WPLn]="TAX070_20")

ENDFOR

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

### 17. Tax - Allowable Costs & Chargeable Profit CITA (Oil) — SCRIPT

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

### 18. Tax - Allowable Costs & Chargeable Profit CITA (Gas) — SCRIPT

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

// TAX070_60 (SET10_10) is null when the JV has no PIA flag - treat null as 0
IF RESULTLOOKUP([d/WPLn]="TAX070_60") = 0 OR RESULTLOOKUP([d/WPLn]="TAX070_60") = NULL THEN
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

### 19. Tax - PPT Tax (Oil) — SCRIPT

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

DATA([d/WPLn] = "TAX085_20") = RESULTLOOKUP([d/WPLn]="TAX065_05") * RESULTLOOKUP([d/WPLn]="TAX085_10") * RESULTLOOKUP([d/WPLn]="SET10_05",[d/Date]="000000") / 100

IF RESULTLOOKUP([d/WPLn]="TAX085_20") < 0 THEN
	DATA([d/WPLn] = "TAX085_20") = 0
ENDIF

DATA([d/WPLn] = "TAX085_25") = RESULTLOOKUP([d/WPLn]="TAX085_20") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 20. Tax - CITA (Oil & Gas) — SCRIPT

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
DATA([d/WPLn] = "TAX090_10") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")

DATA([d/WPLn] = "TAX090_15") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX075_10") * RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000") / 100
IF RESULTLOOKUP([d/WPLn]="TAX090_15") < 0 THEN DATA([d/WPLn] = "TAX090_15") = 0 ENDIF

// Gas CITA applies under both regimes (PPT covers oil only) - no PIA flag, as NUIMS row 2426
DATA([d/WPLn] = "TAX090_20") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX080_10") / 100
IF RESULTLOOKUP([d/WPLn]="TAX090_20") < 0 THEN DATA([d/WPLn] = "TAX090_20") = 0 ENDIF

DATA([d/WPLn] = "TAX090_25") = RESULTLOOKUP([d/WPLn]="TAX090_15") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
DATA([d/WPLn] = "TAX090_30") = RESULTLOOKUP([d/WPLn]="TAX090_20") * RESULTLOOKUP([d/WPLn]="AMT_90") / 100
```

Parameters used: Entity, PCycle

### 21. GL Entries — SCRIPT

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
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_220", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_15", [d/PPP_Currency]="USD") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_15", [d/PPP_Currency]="USD")
// Depletion
DATA([d/Measures] = "GC_CR", [d/GL] = "5230003", [d/PPP_EntryNr] = "UP_0005") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_220", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_16", [d/PPP_Currency]="USD") +
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_16", [d/PPP_Currency]="USD")
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
