# CAPEX_CurCon

> PPP Currency Conversion - CAPEX

| | |
|---|---|
| SAC id | `3C8846052291A0F00AC308BB42C71038` |
| Default model | CAPEX |
| Created by | DPARUMAUL |
| Last changed | 2026-08-06T02:38:51.072Z by NMUNDAY |
| Called by | [CAPEX_Movable_Calcs](CAPEX_Movable_Calcs.md) |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `PCycle` | PROMPT | MEMBER | Plan_Cycle | SINGLE | `"2026-2030/01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["NB01"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise | SCRIPT |  |
| 2 | Moveable_Calc | SCRIPT |  |
| 3 | Currency_Con | CONVERSION |  |

### 1. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/Plan_Cycle] = %PCycle%
MEMBERSET [d/Measures] = "M_Cost"
MEMBERSET [d/MovableItems] = BASEMEMBER([d/MovableItems] , "Total")
MEMBERSET [d/PPP_Currency] = BASEMEMBER([d/PPP_Currency] , "Total")
MEMBERSEt [d/GL] = ("#")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Project] = "#"
MEMBERSET [d/ImpStage] = "#"
MEMBERSET [d/ProjectClass] = "#"
MEMBERSET [d/Work_Program] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/Project_Status] = "#"
MEMBERSET [d/Start_Year] = "#"
MEMBERSET [d/End_Year] = "#"


DELETE()
```

Parameters used: Entity, PCycle

### 2. Moveable_Calc — SCRIPT

Calculation

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Plan_Cycle] = %PCycle%
MEMBERSET [d/Measures] = ("QTY","M_Cost","U_Price")
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/MovableItems] = BASEMEMBER([d/MovableItems] , "Total")
MEMBERSET [d/PPP_Currency] = BASEMEMBER([d/PPP_Currency] , "Total")
MEMBERSEt [d/GL] = ("#")
MEMBERSET [d/Lock] = ("#")
MEMBERSET [d/Project] = "#"
MEMBERSET [d/ImpStage] = "#"
MEMBERSET [d/ProjectClass] = "#"
MEMBERSET [d/Work_Program] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/Project_Status] = "#"
MEMBERSET [d/Start_Year] = "#"
MEMBERSET [d/End_Year] = "#"

// For debug purposes
//DATA([d/Measures]="M_Cost", [d/MovableItems] = "MIX96785", [d/PPP_Currency] = "USD") = 1
//DATA([d/Measures]="M_Cost", [d/MovableItems] = "MIX96785", [d/PPP_Currency] = "NGN") = 1

DATA([d/Measures]="M_Cost") = RESULTLOOKUP([d/Measures] = "QTY")

DATA([d/Measures]="M_Cost") = RESULTLOOKUP([d/Measures]="U_Price")

DATA([d/Measures]="M_Cost") = 
	RESULTLOOKUP([d/Measures]="QTY") * 
	RESULTLOOKUP([d/Measures]="U_Price")
```

Parameters used: PCycle, Entity

### 3. Currency_Con — CONVERSION

Conversion

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
  "Plan_Cycle": {
   "memberIds": [
    {
     "paramRef": "PCycle"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "conversionRules": [
  {
   "source": {
    "hierarchyName": null,
    "memberId": "M_Cost"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "GC_Amount"
   },
   "fixedDate": null,
   "delta": {
    "granularity": "YEAR",
    "shift": 0
   },
   "category": "DYNAMIC",
   "rateVersion": null
  }
 ],
 "writeMode": "OVERWRITE"
}
```

</details>
