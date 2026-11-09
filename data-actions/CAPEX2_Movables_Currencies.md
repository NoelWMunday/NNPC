# CAPEX2_Movables_Currencies

| | |
|---|---|
| SAC id | `8C6ECE84BFC365BF3FEBEF706D05FEE4` |
| Default model | CAPEX |
| Created by | NMUNDAY |
| Last changed | 2026-08-06T04:23:06.095Z by NMUNDAY |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Plan 2027-2031 iteration 01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `PCycle` | PROMPT | MEMBER | Plan_Cycle | SINGLE | `"#"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | NESTED_SEQUENCE | runs [CAPEX2_Base_Currencies](CAPEX2_Base_Currencies.md) |

### 1. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:13BECE84BFC3FFB8511A87BF2A3A0AAB",
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
    "displayKey": "PCycle"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "PCycle"
   }
  },
  {
   "id": {
    "displayKey": "Entity"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "Entity"
   }
  },
  {
   "id": {
    "displayKey": "Projects"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "#"
    ],
    "hierarchyName": null
   }
  },
  {
   "id": {
    "displayKey": "Movables"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "Total"
    ],
    "hierarchyName": "H1"
   }
  }
 ]
}
```

</details>
