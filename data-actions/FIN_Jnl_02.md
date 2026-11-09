# FIN_Jnl_02

> FIN Taxation

| | |
|---|---|
| SAC id | `7BC9D40771E66EE8795AF2AB80CB78CF` |
| Default model | PPP Financial |
| Created by | NMUNDAY |
| Last changed | 2026-10-09T11:25:26.329Z by NMUNDAY |
| Called by | [PPP_GLPost_BusPremise](PPP_GLPost_BusPremise.md) |
| Used in stories | — |

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
| 1 | Initialise | DELETE_FACTS |  |
| 2 | Initialise | DELETE_FACTS |  |
| 3 | Persist GP | SCRIPT |  |
| 4 | Persist PBT | SCRIPT |  |
| 5 | Chargeable profit | SCRIPT |  |
| 6 | Currency convertion | CONVERSION |  |
| 7 | Copy converted NGN back to the working sheet | SCRIPT |  |
| 8 | Determine tax | SCRIPT |  |

### 1. Initialise — DELETE_FACTS

<details><summary>Configuration</summary>

```json
{
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "TargetVersion"
   },
   "hierarchyName": null
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_Account": {
   "memberIds": [
    "FIN07_01_01",
    "FIN07_01_02",
    "FIN07_01_03",
    "FIN07_01_04",
    "FIN07_01_05",
    "FIN07_01_07",
    "FIN07_01_08",
    "FIN07_01_00",
    "FIN07_01_09"
   ],
   "hierarchyName": "parentId"
  }
 },
 "sourceContextFilterParamRefs": [],
 "deleteMode": "DELETE",
 "disabled": false
}
```

</details>

### 2. Initialise — DELETE_FACTS

<details><summary>Configuration</summary>

```json
{
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "TargetVersion"
   },
   "hierarchyName": null
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "FIN_010",
    "FIN_015"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "deleteMode": "DELETE",
 "disabled": false
}
```

</details>

### 3. Persist GP — SCRIPT

```
// Note: Although the IS displays in FIN as USD because CLO_GC is currency based on Entity
// the underlying data is sitting on multiple currencies for the currency dimension
// This function normalises that by rolling the values up into USD for further processing

CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = ON
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account].[h/FSV1] , "IS_REV")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)
MEMBERSET [d/Measures] = ("CLO_GC")

IF [d/Date].[p/MONTHDESC] = "Dec" THEN
	DATA.APPEND([d/PPP_Account] = "FIN07_01_00", [d/PPP_Currency] = "USD") = RESULTLOOKUP()
ENDIF
```

Parameters used: Entity, CY

### 4. Persist PBT — SCRIPT

```
// Note: Although the IS displays in FIN as USD because CLO_GC is currency based on Entity
// the underlying data is sitting on multiple currencies for the currency dimension
// This function normalises that by rolling the values up into USD for further processing

CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = ON
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account].[h/FSV1] , "IS_PBT")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_EntryNr] = "1001"
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)
MEMBERSET [d/Measures] = ("CLO_GC")

IF [d/Date].[p/MONTHDESC] = "Dec" THEN
	DATA.APPEND([d/PPP_Account] = "FIN07_01_09", [d/PPP_Currency] = "USD") = RESULTLOOKUP()
ENDIF
```

Parameters used: Entity, CY

### 5. Chargeable profit — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("FIN07_01_10","FIN07_01_11","FIN07_01_09","FIN06_02_03","FIN06_02_02")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/PPP_EntryNr] = ("1001")
MEMBERSET [d/Measures] = ("CLO_GC")
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)

DATA([d/PPP_Account] = "FIN07_01_11") = 
	RESULTLOOKUP([d/PPP_Account] = "FIN06_02_03") *
	RESULTLOOKUP([d/PPP_Account] = "FIN06_02_02") / 100

DATA([d/PPP_Account] = "FIN07_01_10") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_09") -
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_11")
```

Parameters used: Entity, CY

### 6. Currency convertion — CONVERSION

<details><summary>Configuration</summary>

```json
{
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "TargetVersion"
   },
   "hierarchyName": null
  },
  "PPP_Account": {
   "memberIds": [
    "FIN07_01_00"
   ],
   "hierarchyName": "parentId"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "conversionRules": [
  {
   "source": {
    "hierarchyName": null,
    "memberId": "CLO_GC"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "RPT_CUR_N"
   },
   "fixedDate": null,
   "delta": {
    "granularity": "MONTH",
    "shift": 0
   },
   "externalRatesType": null,
   "category": "DYNAMIC",
   "rateVersion": null
  }
 ],
 "writeMode": "OVERWRITE"
}
```

</details>

### 7. Copy converted NGN back to the working sheet — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("FIN07_01_00","FIN07_01_01")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_EntryNr] = ("1001")
MEMBERSET [d/Measures] = ("CLO_GC","RPT_CUR_N")
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)

DATA([d/Measures]="CLO_GC", [d/PPP_Account] = "FIN07_01_01") = ROUND(
	RESULTLOOKUP([d/Measures]="RPT_CUR_N", [d/PPP_Account] = "FIN07_01_00"), 0)
```

Parameters used: Entity, CY

### 8. Determine tax — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("FIN07_01_01","FIN07_01_02","FIN07_01_03","FIN07_01_04","FIN06_03_01","FIN06_03_02")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/PPP_EntryNr] = ("1001")
MEMBERSET [d/Measures] = ("CLO_GC")
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)

IF RESULTLOOKUP([d/PPP_Account] = "FIN07_01_09") < 0 THEN

	DATA([d/PPP_Account] = "FIN07_01_04") = 
		RESULTLOOKUP([d/Measures]="RPT_METRCS",[d/PPP_Account] = "FIN06_03_04",[d/PPP_Currency]="#",[d/PPP_Entity]="#",[d/PPP_EntryNr]="#") / 100

	DATA([d/PPP_Account] = "FIN07_01_05") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_04") * RESULTLOOKUP([d/PPP_Account] = "FIN07_01_00")

ELSEIF RESULTLOOKUP([d/PPP_Account] = "FIN07_01_01") > 100000000 THEN

	DATA([d/PPP_Account] = "FIN07_01_02") = 
		RESULTLOOKUP([d/Measures]="RPT_METRCS",[d/PPP_Account] = "FIN06_03_01",[d/PPP_Currency]="#",[d/PPP_Entity]="#",[d/PPP_EntryNr]="#") / 100

	DATA([d/PPP_Account] = "FIN07_01_04") = RESULTLOOKUP([d/PPP_Account] = "FIN07_01_02")

	DATA([d/PPP_Account] = "FIN07_01_05") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_04") * RESULTLOOKUP([d/PPP_Account] = "FIN07_01_09")
ELSE
	DATA([d/PPP_Account] = "FIN07_01_03") = 
		RESULTLOOKUP([d/Measures]="RPT_METRCS",[d/PPP_Account] = "FIN06_03_02",[d/PPP_Currency]="#",[d/PPP_Entity]="#",[d/PPP_EntryNr]="#") / 100
	DATA([d/PPP_Account] = "FIN07_01_04") = RESULTLOOKUP([d/PPP_Account] = "FIN07_01_03")

	DATA([d/PPP_Account] = "FIN07_01_05") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_04") * RESULTLOOKUP([d/PPP_Account] = "FIN07_01_09")
ENDIF

DATA([d/PPP_Account] = "FIN07_01_07") = 
	RESULTLOOKUP([d/PPP_Account] = "FIN07_01_11") + RESULTLOOKUP([d/PPP_Account] = "FIN07_01_05")

IF RESULTLOOKUP([d/PPP_Account] = "FIN07_01_12",[d/PPP_Currency]="#") != 0 THEN
	DATA([d/PPP_Account] = "FIN07_01_08") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_06",[d/PPP_Currency]="#")

	DATA([d/Measures]="DR_GC", [d/PPP_Account] = "5100005", [d/PPP_EntryNr] = "FIN_015") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_08")

	DATA([d/Measures]="CR_GC", [d/PPP_Account] = "CA_005", [d/PPP_EntryNr] = "FIN_015") = 
		0 - RESULTLOOKUP([d/PPP_Account] = "FIN07_01_08")
ELSE
	DATA([d/PPP_Account] = "FIN07_01_08") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_07")
	
	DATA([d/Measures]="DR_GC", [d/PPP_Account] = "5100008", [d/PPP_EntryNr] = "FIN_010") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_11")
	DATA([d/Measures]="CR_GC", [d/PPP_Account] = "CA_005", [d/PPP_EntryNr] = "FIN_010") = 
		0 - RESULTLOOKUP([d/PPP_Account] = "FIN07_01_11")
	
	DATA([d/Measures]="DR_GC", [d/PPP_Account] = "5100005", [d/PPP_EntryNr] = "FIN_015") = 
		RESULTLOOKUP([d/PPP_Account] = "FIN07_01_05")
	DATA([d/Measures]="CR_GC", [d/PPP_Account] = "CA_005", [d/PPP_EntryNr] = "FIN_015") = 
		0 - RESULTLOOKUP([d/PPP_Account] = "FIN07_01_05")	
ENDIF
```

Parameters used: Entity, CY
