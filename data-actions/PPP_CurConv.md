# PPP_CurConv

> PPP Currency conversion

| | |
|---|---|
| SAC id | `527E18802BA4CE9414A6EC3227AC5B1D` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-10-13T08:10:02.939Z by NMUNDAY |
| Called by | [PPP_BusPremise_GL_Calcs](PPP_BusPremise_GL_Calcs.md), [PPP_OVH_All_calcs](PPP_OVH_All_calcs.md) |
| Used in stories | [PPP_Overheads](../stories/PPP_Overheads.md), [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | DELETE_FACTS |  |
| 2 | Currency Conversion | CONVERSION |  |

### 1. (unnamed) — DELETE_FACTS

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
    "BP002"
   ],
   "hierarchyName": "H1"
  },
  "CustomDimension1": {
   "memberIds": [
    "GC_CR"
   ],
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "Revenue",
    "OTHER_INC",
    "COS_DPR",
    "OTHER_DCST",
    "ROYALTIES",
    "CHOOCA",
    "TAX_HIST",
    "NON_CASH",
    "GEN_ADMIN",
    "HR",
    "OTHER",
    "COGS"
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    "#",
    "Hist_Open"
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

### 2. Currency Conversion — CONVERSION

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
  "GL": {
   "memberIds": [
    "OTHER_INC",
    "OTHER_DCST",
    "COS_DPR",
    "ROYALTIES",
    "CHOOCA",
    "TAX_HIST",
    "NON_CASH",
    "GEN_ADMIN",
    "HR",
    "OTHER",
    "Revenue",
    "COGS"
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
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "BP002"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "conversionRules": [
  {
   "source": {
    "hierarchyName": null,
    "memberId": "CR"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "GC_CR"
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
