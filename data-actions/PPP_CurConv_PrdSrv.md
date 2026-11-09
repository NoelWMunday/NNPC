# PPP_CurConv_PrdSrv

> PPP Currency conversion - Products and Services

| | |
|---|---|
| SAC id | `950F68802BA581C0A6F35C2466EF15E9` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-11T17:20:25.405Z by NMUNDAY |
| Called by | [PPP_ProdServ_All_calcs](PPP_ProdServ_All_calcs.md), [PPP_Products & Services (Multi)](PPP_Products_Services_Multi.md), [PPP_Refinerie_GL_Postings](PPP_Refinerie_GL_Postings.md) |
| Used in stories | [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Currency Conversion | CONVERSION |  |

### 1. Currency Conversion — CONVERSION

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
    "#"
   ],
   "hierarchyName": "H1"
  },
  "ProductServ": {
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
  },
  "PCycle": {
   "memberIds": [
    "#"
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
    "memberId": "AMT_Rev"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "AMT_Rev_GC"
   },
   "fixedDate": null,
   "delta": {
    "granularity": "MONTH",
    "shift": 0
   },
   "category": "DYNAMIC",
   "rateVersion": null
  },
  {
   "source": {
    "hierarchyName": null,
    "memberId": "AMT_COGS"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "AMT_COGS_GC"
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
