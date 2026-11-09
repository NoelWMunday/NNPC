# PPP_FIN_GL_cross-cast

> Financial model GL cross-cast

| | |
|---|---|
| SAC id | `4339660522912877CF641BF760FFA59F` |
| Default model | PPP Financial |
| Created by | NMUNDAY |
| Last changed | 2026-10-15T11:50:11.062Z by NMUNDAY |
| Called by | [PPP_GLPost_BusPremise](PPP_GLPost_BusPremise.md) |
| Used in stories | [PPP_Financial](../stories/PPP_Financial.md), [PPP_Financial_Test](../stories/PPP_Financial_Test.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `CurrentFY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2026", "202612"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Debug 01 | SCRIPT | **DISABLED** |
| 2 | Debug 02 | SCRIPT | **DISABLED** |
| 3 | Initialise OPE | SCRIPT |  |
| 4 | Initialise CLO & MOV | SCRIPT |  |
| 5 | Initialise RI / RE | SCRIPT |  |
| 6 | Movements | SCRIPT |  |
| 7 | Cross-cast (first year - no carry forward) | SCRIPT |  |
| 8 | Cross-cast (Subsequent years) | SCRIPT |  |
| 9 | Retained income | SCRIPT |  |
| 10 | Cross-cast (First period) | SCRIPT |  |
| 11 | Cross-cast | SCRIPT |  |

### 1. Debug 01 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Debugging step to determine time periods

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = ("1001")
MEMBERSET [d/PPP_Account] = "CA_005"
MEMBERSET [d/Date] = PREVIOUS(46,"MONTH",%CurrentFY%) TO PREVIOUS(3,"YEAR",%CurrentFY%)
MEMBERSET [d/Measures] = ("OPE_GC")
MEMBERSET [d/PPP_Currency] = "USD"

DATA() = 1
```

Parameters used: Entity, CurrentFY

### 2. Debug 02 — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Debugging step to determine time periods

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = ("1001")
MEMBERSET [d/PPP_Account] = "CA_005"
MEMBERSET [d/Date] = PREVIOUS(35,"MONTH",%CurrentFY%) TO NEXT(5,"YEAR",%CurrentFY%)
MEMBERSET [d/Measures] = ("OPE_GC")
MEMBERSET [d/PPP_Currency] = "USD"

DATA() = 1
```

Parameters used: Entity, CurrentFY

### 3. Initialise OPE — SCRIPT

Initialise

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// This function recalculates the entire TB so all balances are deleted and 
// recalculated i.e. on entry = 1001 and the retained income is recalculated so also
// entry FIN_005 used exclusively for that purpose. Nobody should upload or use these 
// numbers for anything else.

// Opening balances are deleted for all periods except the very first month where the 
// opening TB is captured

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = ("1001","FIN_005")
MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account] , "GL")
MEMBERSET [d/Date] = PREVIOUS(46,"MONTH",%CurrentFY%) TO NEXT(5,"YEAR",%CurrentFY%)
MEMBERSET [d/Measures] = ("OPE","OPE_GC")

DELETE()
```

Parameters used: Entity, CurrentFY

### 4. Initialise CLO & MOV — SCRIPT

Initialise

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// This function recalculates the entire TB so all balances are deleted and 
// recalculated i.e. on entry = 1001 and the retained income is recalculated so also
// entry FIN_005 used exclusively for that purpose. Nobody should upload or use these 
// numbers for anything else.

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = ("1001","FIN_005")
MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account] , "GL")
MEMBERSET [d/Date] = PREVIOUS(5,"YEAR",%CurrentFY%) TO NEXT(5,"YEAR",%CurrentFY%)
MEMBERSET [d/Measures] = ("MOV","CLO","MOV_GC","CLO_GC")

DELETE()
```

Parameters used: Entity, CurrentFY

### 5. Initialise RI / RE — SCRIPT

Initialise

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Clearing the retained earnings means also clearing the CR entry where all
// other accounts the postings residing on DR and CR in source and group currency
// should never be touched

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = ("1001","FIN_005")
MEMBERSET [d/PPP_Account] = "RI_005"
MEMBERSET [d/Date] = PREVIOUS(5,"YEAR",%CurrentFY%) TO NEXT(5,"YEAR",%CurrentFY%)
MEMBERSET [d/Measures] = ("CR","CR_GC")

DELETE()
```

Parameters used: Entity, CurrentFY

### 6. Movements — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = ON
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = BASEMEMBER([d/PPP_EntryNr] , "Total")
MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account] , "GL")
MEMBERSET [d/Date] = PREVIOUS(5,"YEAR",%CurrentFY%) TO NEXT(5,"YEAR",%CurrentFY%)

IF [d/PPP_EntryNr] != "1001" THEN
	DATA.APPEND([d/Measures] = "MOV", [d/PPP_EntryNr]="1001") = 
		RESULTLOOKUP([d/Measures] = "DR") + 
		RESULTLOOKUP([d/Measures] = "CR")
	
	DATA.APPEND([d/Measures] = "MOV_GC", [d/PPP_EntryNr]="1001") = 
		RESULTLOOKUP([d/Measures] = "DR_GC") + 
		RESULTLOOKUP([d/Measures] = "CR_GC")
ENDIF
```

Parameters used: Entity, CurrentFY

### 7. Cross-cast (first year - no carry forward) — SCRIPT

```
// By not touching OPE in the first year and first month the user can upload the opening position
// into this measure

CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = ("1001")
MEMBERSET [d/PPP_Currency] = ("NGN","USD")
MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account] , "GL")
// First year (e.g. CY = 202512 so range 202112 to 202212)
MEMBERSET [d/Date] = PREVIOUS(47,"MONTH",%CurrentFY%) TO PREVIOUS(3,"YEAR",%CurrentFY%)

FOREACH [d/Date]

	IF ([d/Date].[p/MONTHDESC] != "Jan") THEN
		DATA.APPEND([d/Measures] = "OPE") = RESULTLOOKUP([d/Measures] = "CLO",[d/Date]=PREVIOUS(1,"MONTH",[d/Date]))
		DATA.APPEND([d/Measures] = "OPE_GC") = RESULTLOOKUP([d/Measures] = "CLO_GC",[d/Date]=PREVIOUS(1,"MONTH",[d/Date]))
	ENDIF

	DATA.APPEND([d/Measures] = "CLO") = RESULTLOOKUP([d/Measures] = "OPE") + RESULTLOOKUP([d/Measures] = "MOV")
	DATA.APPEND([d/Measures] = "CLO_GC") = RESULTLOOKUP([d/Measures] = "OPE_GC") + RESULTLOOKUP([d/Measures] = "MOV_GC")

ENDFOR
```

Parameters used: Entity, CurrentFY

### 8. Cross-cast (Subsequent years) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = ("1001")
MEMBERSET [d/PPP_Currency] = ("NGN","USD")
MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account] , "GL")
// Subsequent years
MEMBERSET [d/Date] = PREVIOUS(35,"MONTH",%CurrentFY%) TO NEXT(5,"YEAR",%CurrentFY%)

FOREACH [d/Date] 
	IF ([d/Date].[p/MONTHDESC] = "Jan") AND ([d/PPP_Account].[p/accType] = ("LEQ","AST")) THEN
		DATA.APPEND([d/Measures] = "OPE") = RESULTLOOKUP([d/Measures] = "CLO", [d/Date]=PREVIOUS(1,"MONTH",[d/Date]))
		DATA.APPEND([d/Measures] = "OPE_GC") = RESULTLOOKUP([d/Measures] = "CLO_GC", [d/Date]=PREVIOUS(1,"MONTH",[d/Date]))
//		DATA([d/Measures] = "OPE") = 1
	ENDIF

	IF ([d/Date].[p/MONTHDESC] != "Jan") THEN
		DATA.APPEND([d/Measures] = "OPE") = RESULTLOOKUP([d/Measures] = "CLO",[d/Date]=PREVIOUS(1,"MONTH",[d/Date]))
		DATA.APPEND([d/Measures] = "OPE_GC") = RESULTLOOKUP([d/Measures] = "CLO_GC",[d/Date]=PREVIOUS(1,"MONTH",[d/Date]))
//		DATA([d/Measures] = "OPE") = 1
	ENDIF

	DATA.APPEND([d/Measures] = "CLO") = RESULTLOOKUP([d/Measures] = "OPE") + RESULTLOOKUP([d/Measures] = "MOV")
	DATA.APPEND([d/Measures] = "CLO_GC") = RESULTLOOKUP([d/Measures] = "OPE_GC") + RESULTLOOKUP([d/Measures] = "MOV_GC")
//	DATA([d/Measures] = "CLO") = 1

ENDFOR
```

Parameters used: Entity, CurrentFY

### 9. Retained income — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = ON
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = ("1001","FIN_005")
MEMBERSET [d/PPP_Currency] = ("NGN","USD")
MEMBERSET [d/PPP_Account] = (BASEMEMBER([d/PPP_Account] , "INCOME_STMT"), "RI_005")
MEMBERSET [d/Measures] = ("CR", "CR_GC", "MOV","MOV_GC", "CLO", "CLO_GC")
MEMBERSET [d/Date] = PREVIOUS(5,"YEAR",%CurrentFY%) TO NEXT(5,"YEAR",%CurrentFY%)

IF [d/PPP_Account] = BASEMEMBER([d/PPP_Account] , "INCOME_STMT" ) AND [d/Date].[p/MONTHDESC] = "Dec" THEN
	DATA.APPEND([d/Measures] = "CR", [d/PPP_Account] = "RI_005", [d/PPP_EntryNr] = "FIN_005", [d/Date] = NEXT(1,"MONTH",[d/Date])) = 
		RESULTLOOKUP([d/Measures] = "CLO", [d/PPP_EntryNr] = "1001")
	DATA.APPEND([d/Measures] = "CR_GC", [d/PPP_Account] = "RI_005", [d/PPP_EntryNr] = "FIN_005", [d/Date] = NEXT(1,"MONTH",[d/Date])) = 
		RESULTLOOKUP([d/Measures] = "CLO_GC", [d/PPP_EntryNr] = "1001")

	DATA.APPEND([d/Measures] = "MOV", [d/PPP_Account] = "RI_005", [d/PPP_EntryNr] = "1001", [d/Date] = NEXT(1,"MONTH",[d/Date])) = 
		RESULTLOOKUP([d/Measures] = "CLO", [d/PPP_EntryNr] = "1001")
	DATA.APPEND([d/Measures] = "MOV_GC", [d/PPP_Account] = "RI_005", [d/PPP_EntryNr] = "1001", [d/Date] = NEXT(1,"MONTH",[d/Date])) = 
		RESULTLOOKUP([d/Measures] = "CLO_GC", [d/PPP_EntryNr] = "1001")	
ENDIF
```

Parameters used: Entity, CurrentFY

### 10. Cross-cast (First period) — SCRIPT

Cross-cast

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/PPP_Currency] = ("NGN","USD")
MEMBERSET [d/PPP_Account] = "RI_005"
MEMBERSET [d/Date] = PREVIOUS(47,"MONTH",%CurrentFY%) TO PREVIOUS(47,"MONTH",%CurrentFY%)

FOREACH [d/Date]
	DATA([d/Measures] = "CLO") = RESULTLOOKUP([d/Measures] = "OPE") + RESULTLOOKUP([d/Measures] = "MOV")
	DATA([d/Measures] = "CLO_GC") = RESULTLOOKUP([d/Measures] = "OPE_GC") + RESULTLOOKUP([d/Measures] = "MOV_GC")
ENDFOR
```

Parameters used: Entity, CurrentFY

### 11. Cross-cast — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/PPP_Currency] = ("NGN","USD")
MEMBERSET [d/PPP_Account] = "RI_005"
MEMBERSET [d/Date] = PREVIOUS(46,"MONTH",%CurrentFY%) TO NEXT(5,"YEAR",%CurrentFY%)

FOREACH [d/Date]
	DATA([d/Measures] = "OPE") = RESULTLOOKUP([d/Measures] = "CLO", [d/Date]=PREVIOUS(1,"MONTH",[d/Date]))
	DATA([d/Measures] = "OPE_GC") = RESULTLOOKUP([d/Measures] = "CLO_GC", [d/Date]=PREVIOUS(1,"MONTH",[d/Date]))

	DATA([d/Measures] = "CLO") = RESULTLOOKUP([d/Measures] = "OPE") + RESULTLOOKUP([d/Measures] = "MOV")
	DATA([d/Measures] = "CLO_GC") = RESULTLOOKUP([d/Measures] = "OPE_GC") + RESULTLOOKUP([d/Measures] = "MOV_GC")
ENDFOR
```

Parameters used: Entity, CurrentFY
