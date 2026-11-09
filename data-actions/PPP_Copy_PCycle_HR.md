# PPP_Copy_PCycle_HR

> PPP Copy PCycle - HR model

| | |
|---|---|
| SAC id | `F6761684BFC1665F421B12BA110A3983` |
| Default model | PPP Workforce planning |
| Created by | NMUNDAY |
| Last changed | 2026-08-04T07:17:05.757Z by NMUNDAY |
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
