# PPP_Upstream_Revenue

> PPP Upstream_Revenue

| | |
|---|---|
| SAC id | `E1751684BFC7BECB4638AFAF2DC6D009` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-11-10T06:10:49.630Z by NMUNDAY |
| Called by | [PPP_Upstream_All_Calculations](PPP_Upstream_All_Calculations.md) |
| Used in stories | [PPP_UStream](../stories/PPP_UStream.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["NB04"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Revenue calculation | SCRIPT |  |
| 3 | Initialise common entity totals | SCRIPT |  |
| 4 | Total JV Revenue step 02 | SCRIPT |  |
| 5 | Total JV Revenue step 03 | SCRIPT |  |
| 6 | Total JV Revenue step 04 | SCRIPT |  |
| 7 | GL Entries - initialise | SCRIPT |  |
| 8 | GL Entries | SCRIPT |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_32","REV_26","REV_40", BASEMEMBER([d/WPLn] ,"REV3_05"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DELETE()
```

Parameters used: Entity

### 2. Revenue calculation — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

// *** DEBUG AREA - CAN LEAVE THESE COMMENT LINES FOR USE WHEN DEBUGGING ***
//DATA([d/WPLn]="REV_05") = 1
//DATA([d/WPLn]="REV_05") = RESULTLOOKUP([d/WPLn]="AMT_80")
//DATA([d/WPLn]="REV_05") = RESULTLOOKUP([d/WPLn]="GA_040", [d/PPP_Entity] = "#", [d/Lock]="Central")

// Annual oil production
// from kilo barrels per day to millions barrels per year means (x 365 / 1000) so result is in "mmbbl"
DATA([d/WPLn]="REV_05") = (RESULTLOOKUP([d/WPLn]="AMT_80", [d/PPP_Currency]="USD") * RESULTLOOKUP([d/WPLn]="GA_040", [d/PPP_Entity] = "#", [d/Lock]="Central")) / 1000

// Ave monthly oil production
DATA([d/WPLn]="AMT_81") = RESULTLOOKUP([d/WPLn]="REV_05") / RESULTLOOKUP([d/WPLn]="UOM_65", [d/PPP_Currency]="USD")

// Ave monthly oil production per field
DATA([d/WPLn]="AMT_82") = RESULTLOOKUP([d/WPLn]="AMT_81") / RESULTLOOKUP([d/WPLn]="AMT_97", [d/PPP_Currency]="USD")

// Oil revenue
// from mmbbl to price per barrel and revenue in single dollars means x 1 000 000 to convert to single units
DATA([d/WPLn]="REV_10") = RESULTLOOKUP([d/WPLn]="REV_05") * RESULTLOOKUP([d/WPLn]="GA_015", [d/PPP_Entity] = "#", [d/Lock]="Central") * 1000000

// Annual gas sales
DATA([d/WPLn]="REV_15") = RESULTLOOKUP([d/WPLn]="AMT_85", [d/PPP_Currency]="USD") * RESULTLOOKUP([d/WPLn]="GA_040", [d/PPP_Entity] = "#", [d/Lock]="Central")

// Gas revenue
// Price is already per mmscf so no conversion to single dollar units necessary
DATA([d/WPLn]="REV_20") = RESULTLOOKUP([d/WPLn]="REV_15") * RESULTLOOKUP([d/WPLn]="GA_020", [d/PPP_Entity] = "#", [d/Lock]="Central") * 1000

// Total revenue
DATA([d/WPLn]="REV_25") = RESULTLOOKUP([d/WPLn]="REV_10") + RESULTLOOKUP([d/WPLn]="REV_20") 

// NNPC Share of revenue
DATA([d/WPLn]="REV_30") = RESULTLOOKUP([d/WPLn]="REV_25") * RESULTLOOKUP([d/WPLn]="AMT_90", [d/PPP_Currency]="USD") / 100
```

Parameters used: Entity

### 3. Initialise common entity totals — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_32","REV_26",BASEMEMBER([d/WPLn] , "CST14"))
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

// Clear the entity placeholder at the common entity level i.e. not the work program entity level
// which is cleared in the initialisation step

DATA([d/WPLn]="REV_32",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
DATA([d/WPLn]="REV_26",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = 0
```

### 4. Total JV Revenue step 02 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_25","REV_32")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

// If the entity belongs to a work group (i.e. non blank) then send it's revenue to the common entity (owning entity) 
// on the WPLn identified by the property e.g. NU03_WP01 is a JV belonging to NU03 so NU03_WP01 will point
// to NU03 as the common entity and accumulate the work group total revenue on WPLn = the property on NU03_WP01 i.e. a JV total
IF [d/PPP_Entity].[p/WPGroup] != "" THEN
	DATA.APPEND([d/WPLn]=[d/PPP_Entity].[p/Ln],[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup]) = RESULTLOOKUP([d/WPLn]="REV_25")
ENDIF
```

### 5. Total JV Revenue step 03 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures]= ("Value_WPLn","GC_CLO")
MEMBERSET [d/WPLn] = ("REV_40","#")
MEMBERSET [d/GL] = (BASEMEMBER([d/GL], "OTHER_INC" ), "#")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

IF [d/PPP_Entity].[p/WPGroup] != "" THEN
	DATA.APPEND([d/Measures]="Value_WPLn",[d/WPLn]="REV_40",[d/GL]="#",[d/PPP_Currency]="#") = 
		RESULTLOOKUP([d/Measures]="GC_CLO",[d/WPLn]="#",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup],[d/PPP_Currency]="USD")
ENDIF
```

Parameters used: Entity

### 6. Total JV Revenue step 04 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Apportionment % = REV_33 BY TOTAL REVENUE

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures]="Value_WPLn"
MEMBERSET [d/WPLn] = ("REV_32","REV_33","REV_25","REV_35","REV_40")
MEMBERSET [d/GL] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "#"
MEMBERSET [d/PPP_Currency] = "#"

DATA([d/WPLn]="REV_32") = RESULTLOOKUP([d/WPLn]="REV_32",[d/PPP_Entity]=[d/PPP_Entity].[p/WPGroup])

IF RESULTLOOKUP([d/WPLn]="REV_32") > 0 THEN
	DATA([d/WPLn]="REV_33") = RESULTLOOKUP([d/WPLn]="REV_25") / RESULTLOOKUP([d/WPLn]="REV_32") * 100
	DATA([d/WPLn]="REV_35") = RESULTLOOKUP([d/WPLn]="REV_33") * RESULTLOOKUP([d/WPLn]="REV_40") / 100
ENDIF
```

Parameters used: Entity

### 7. GL Entries - initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures] = ("GC_CR")
MEMBERSET [d/WPLn] = ("#")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("UP_0005","UP_0015")
MEMBERSET [d/PPP_Currency] = "USD"

DELETE()
```

Parameters used: Entity

### 8. GL Entries — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures] = ("Value_WPLn","GC_CR")
MEMBERSET [d/WPLn] = ("#","REV_30", "REV_35")
MEMBERSET [d/GL] = ("#","6011008","7019902")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("#",BASEMEMBER([d/PPP_EntryNr] , "UP"))
MEMBERSET [d/PPP_Currency] = "USD"


// Revenue
DATA([d/Measures] = "GC_CR", [d/GL] = "6011008", [d/PPP_EntryNr] = "UP_0005", [d/WPLn] = "#") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/GL] = "#", [d/WPLn] = "REV_30", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
	
// Other Income
DATA([d/Measures] = "GC_CR", [d/GL] = "7019902", [d/PPP_EntryNr] = "UP_0015", [d/WPLn] = "#") = 
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "REV_35", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
```

Parameters used: Entity
