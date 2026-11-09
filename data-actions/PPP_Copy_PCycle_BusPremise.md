# PPP_Copy_PCycle_BusPremise

> PPP Copy PCycle - Business Premise model

| | |
|---|---|
| SAC id | `D6461684BFC480D2DFECFA20A7133BE6` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-04T07:12:53.810Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_Admin](../stories/PPP_Admin.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Planning cycle - Business premise | COPY |  |

### 1. Planning cycle - Business premise — COPY

<details><summary>Configuration</summary>

```json
{
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "TargetVersion"
   },
   "hierarchyName": null
  }
 },
 "sourceContextFilterParamRefs": [],
 "aggregatedDimensions": {},
 "copyRules": [
  {
   "dimensionId": "PCycle",
   "source": {
    "hierarchyName": "H1",
    "memberId": "2026-2030/01"
   },
   "target": {
    "hierarchyName": "H1",
    "memberIds": [
     "#"
    ]
   }
  }
 ],
 "writeMode": "OVERWRITE",
 "copyFactor": "1"
}
```

</details>
