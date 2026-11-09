# CAPEX_CP_CurrConv

> CP Currency Conversion

| | |
|---|---|
| SAC id | `E8AD28862A3261484EFBE29868C267BE` |
| Default model | CAPEX |
| Created by | DPARUMAUL |
| Last changed | 2026-10-07T08:49:25.958Z by NMUNDAY |
| Called by | [CAPEX_CP_Calcs](CAPEX_CP_Calcs.md) |
| Used in stories | [PPP_CAPEX](../stories/PPP_CAPEX.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Pc_GC | CONVERSION |  |
| 2 | Initialise | SCRIPT |  |
| 3 | FUSD_Calc | SCRIPT |  |
| 4 | Delete intermediate GC values | DELETE_FACTS | **DISABLED** |

### 1. Pc_GC — CONVERSION

Project Cost to GC

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
  }
 },
 "sourceContextFilterParamRefs": [],
 "conversionRules": [
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

### 2. Initialise — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("PC_FUSD")
MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)

DELETE()
```

Parameters used: Entity

### 3. FUSD_Calc — SCRIPT

Functional USD Calculation

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/Measures] = ("PC_GC","PC_FUSD")
MEMBERSET [d/Plan_Cycle] = "#"
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity], %Entity%)

DATA.APPEND([d/Measures] = "PC_FUSD",[d/PPP_Currency] = "USD",[d/Date] = LAST(),[d/Lock]="#") =
	RESULTLOOKUP( [d/Measures] = "PC_GC")
```

Parameters used: Entity

### 4. Delete intermediate GC values — DELETE_FACTS

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
  "CustomDimension1": {
   "memberIds": [
    "PC_GC"
   ],
   "hierarchyName": null
  },
  "ImpStage": {
   "memberIds": [
    "Total"
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
  }
 },
 "sourceContextFilterParamRefs": [],
 "deleteMode": "DELETE",
 "disabled": true
}
```

</details>
