# FIN_Jnl_01

> FIN Education tax

| | |
|---|---|
| SAC id | `B591BC0771E7349F8672BF558A346AF0` |
| Default model | PPP Financial |
| Created by | NMUNDAY |
| Last changed | 2026-10-09T09:07:56.009Z by NMUNDAY |
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
| 1 | Initialise PBT | DELETE_FACTS |  |
| 2 | Persist PBT | SCRIPT |  |
| 3 | Calculate educational tax | SCRIPT |  |

### 1. Initialise PBT — DELETE_FACTS

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
    "FIN06_02_03"
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

### 2. Persist PBT — SCRIPT

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
	DATA.APPEND([d/PPP_Account] = "FIN06_02_03", [d/PPP_Currency] = "USD") = RESULTLOOKUP()
ENDIF
```

Parameters used: Entity, CY

### 3. Calculate educational tax — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Account] = ("5100008","FIN06_02_02","FIN06_02_03")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_Currency] = "USD"
MEMBERSET [d/PPP_EntryNr] = ("1001","FIN_010")
MEMBERSET [d/Measures] = ("CLO_GC","DR_GC","CR_GC")
MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) TO NEXT(5,"YEAR",%CY%)

DATA([d/Measures]="CLO_GC", [d/PPP_Account] = "FIN07_01_11", [d/PPP_EntryNr] = "1001") = 
	RESULTLOOKUP([d/Measures]="CLO_GC", [d/PPP_Account] = "FIN06_02_03", [d/PPP_EntryNr] = "1001") *
	RESULTLOOKUP([d/Measures]="CLO_GC", [d/PPP_Account] = "FIN06_02_02", [d/PPP_EntryNr] = "1001") / 100
	
/*
DATA([d/Measures]="DR_GC", [d/PPP_Account] = "5100008", [d/PPP_EntryNr] = "FIN_010") = 
	RESULTLOOKUP([d/Measures]="CLO_GC", [d/PPP_Account] = "FIN06_02_03", [d/PPP_EntryNr] = "1001") *
	RESULTLOOKUP([d/Measures]="CLO_GC", [d/PPP_Account] = "FIN06_02_02", [d/PPP_EntryNr] = "1001") / 100

DATA([d/Measures]="CR_GC", [d/PPP_Account] = "CA_005", [d/PPP_EntryNr] = "FIN_010") = 
	RESULTLOOKUP([d/Measures]="DR_GC", [d/PPP_Account] = "5100008", [d/PPP_EntryNr] = "FIN_010")
*/
```

Parameters used: Entity, CY
