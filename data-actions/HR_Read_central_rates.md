# HR_Read_central_rates

| | |
|---|---|
| SAC id | `E0415E8CBFC039DDEBF73F1F7EC06B34` |
| Default model | PPP Workforce planning |
| Created by | NMUNDAY |
| Last changed | 2026-08-12T16:04:30.338Z by NMUNDAY |
| Called by | [HR_Calculate_All](HR_Calculate_All.md) |
| Used in stories | [PPP_HR](../stories/PPP_HR.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | SINGLE | `{"memberId": null, "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | COPY |  |

### 1. (unnamed) — COPY

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
  "Ln": {
   "memberIds": [
    "TOTAL",
    "PB",
    "SS"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "aggregatedDimensions": {},
 "copyRules": [
  {
   "dimensionId": "PPP_Entity",
   "source": {
    "hierarchyName": "H1",
    "memberId": "N01_HCM"
   },
   "target": {
    "hierarchyName": "H1",
    "memberIds": [
     {
      "paramRef": "Entity"
     }
    ]
   }
  },
  {
   "dimensionId": "PCycle",
   "source": {
    "hierarchyName": "H1",
    "memberId": "HR"
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
