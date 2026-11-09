# PPP_Copy_PCycle_CAPEX

> PPP Copy PCycle - CAPEX model

| | |
|---|---|
| SAC id | `CE6E1684BFC4A7E0A3A55D71174FE5AC` |
| Default model | CAPEX |
| Created by | NMUNDAY |
| Last changed | 2026-08-04T07:16:27.921Z by NMUNDAY |
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
   "dimensionId": "Plan_Cycle",
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
