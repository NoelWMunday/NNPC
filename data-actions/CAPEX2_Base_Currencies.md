# CAPEX2_Base_Currencies

> PPP CAPEX - Base level currency conversions

| | |
|---|---|
| SAC id | `13BECE84BFC3FFB8511A87BF2A3A0AAB` |
| Default model | CAPEX |
| Created by | NMUNDAY |
| Last changed | 2026-10-07T07:19:26.428Z by NMUNDAY |
| Called by | [CAPEX2_Movables_All_Calculations](CAPEX2_Movables_All_Calculations.md), [CAPEX2_Movables_Currencies](CAPEX2_Movables_Currencies.md) |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Plan 2027-2031 iteration 01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["ND06"]` |
| `Projects` | PROMPT | MEMBER | Project | MULTI | `["#"]` |
| `Movables` | PROMPT | MEMBER | MovableItems | MULTI | `["#"]` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialise movables | SCRIPT |  |
| 2 | Initialise projects | SCRIPT |  |
| 3 | Currency_Con | CONVERSION |  |

### 1. Initialise movables — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/Measures] = "GC_Amount"
MEMBERSET [d/MovableItems] = BASEMEMBER([d/MovableItems] , %Movables%)
MEMBERSEt [d/GL] = ("#")
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

Parameters used: Entity, Movables

### 2. Initialise projects — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)
MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/Project] = %Projects%
MEMBERSET [d/Measures] = "PC_GC"
MEMBERSET [d/Lock] = ("#")

MEMBERSET [d/MovableItems] = "#"
MEMBERSEt [d/GL] = ("#")
MEMBERSET [d/Work_Program] = "#"

DELETE()
```

Parameters used: Entity, Projects

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
    "#"
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
    "#",
    "Hist_Open"
   ],
   "hierarchyName": "H1"
  },
  "Project": {
   "memberIds": [
    {
     "paramRef": "Projects"
    }
   ],
   "hierarchyName": null
  },
  "MovableItems": {
   "memberIds": [
    {
     "paramRef": "Movables"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_Currency": {
   "memberIds": [
    "Total"
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Work_Program": {
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
  },
  {
   "source": {
    "hierarchyName": null,
    "memberId": "PC"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "PC_GC"
   },
   "fixedDate": null,
   "delta": {
    "granularity": "MONTH",
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
