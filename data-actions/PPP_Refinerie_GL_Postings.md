# PPP_Refinerie_GL_Postings

| | |
|---|---|
| SAC id | `C86E9E84BFC2396880E8708183529705` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-26T08:38:23.821Z by NMUNDAY |
| Called by | [PPP_Refineries](PPP_Refineries.md) |
| Used in stories | [PPP_Refinerie](../stories/PPP_Refinerie.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Plan 2027-2031 iteration 01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Currency conversion | NESTED_SEQUENCE | runs [PPP_CurConv_PrdSrv](PPP_CurConv_PrdSrv.md) |
| 2 | Initialise GLs | SCRIPT |  |
| 3 | Post refineries GLs | SCRIPT |  |

### 1. Currency conversion — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:950F68802BA581C0A6F35C2466EF15E9",
 "parameterValues": [
  {
   "id": {
    "displayKey": "TargetVersion"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "TargetVersion"
   }
  },
  {
   "id": {
    "displayKey": "Entity"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "TOTAL"
    ],
    "hierarchyName": "H1"
   }
  }
 ]
}
```

</details>

### 2. Initialise GLs — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("GC_CLO")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] ,%Entity% )
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/ProductServ] = BASEMEMBER([d/ProductServ] , "Total")
MEMBERSET [d/GL] = BASEMEMBER([d/GL] , "GL")
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/PPP_Currency] = BASEMEMBER([d/PPP_Currency] ,"Total")
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("BP003","#")

DELETE()
```

Parameters used: Entity

### 3. Post refineries GLs — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("GC_CLO")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] ,%Entity% )
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/ProductServ] = BASEMEMBER([d/ProductServ] , "Total")
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/PPP_Currency] = ("USD","NGN")
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = "BP003"

// Use these rows for debugging
//DATA([d/Measures] = "GC_CLO", [d/GL]=[d/ProductServ].[p/GL_Revenue], [d/PPP_Currency]="USD") = 1
//DATA([d/Measures] = "GC_CLO", [d/GL]=[d/ProductServ].[p/GL_COGS], [d/PPP_Currency]="USD") = 1

// Note: The .APPEND is for aggregating USD results from multiple source currencies. Although the converted GC values being aggregated are in USD based
// on the entity currency property the data still reflects the GC on the source currency base line item so multiple lines must aggregate into the final total
DATA.APPEND([d/Measures] = "GC_CLO", [d/GL]=[d/ProductServ].[p/GL_Revenue], [d/PPP_Currency]="USD") = 
	RESULTLOOKUP([d/Measures]="AMT_Rev_GC", [d/GL]="#", [d/PPP_EntryNr] = "#") 
DATA.APPEND([d/Measures] = "GC_CLO", [d/GL]=[d/ProductServ].[p/GL_COGS], [d/PPP_Currency]="USD") = 
	RESULTLOOKUP([d/Measures]="AMT_COGS_GC", [d/GL]="#", [d/PPP_EntryNr] = "#")
```

Parameters used: Entity
