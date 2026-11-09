# CAPEX_CP_Calcs

| | |
|---|---|
| SAC id | `8AC1F08E2A366833AC511E80FFC49AA6` |
| Default model | CAPEX |
| Created by | DPARUMAUL |
| Last changed | 2026-08-06T02:44:24.995Z by NMUNDAY |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | FUSD | NESTED_SEQUENCE | runs [CAPEX_CP_CurrConv](CAPEX_CP_CurrConv.md) |
| 2 | YTD | NESTED_SEQUENCE | runs [CP_YTD](CP_YTD.md) |

### 1. FUSD — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:E8AD28862A3261484EFBE29868C267BE",
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
    "memberIds": [
     "2026-2030/01"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "Entity"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "TOTAL"
    ],
    "hierarchyName": "H1"
   }
  }
 ]
}
```

</details>

### 2. YTD — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:934D80862A32D3776EF13BEA7CD9AB98",
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
   "useDefaultValue": true,
   "value": null
  },
  {
   "id": {
    "displayKey": "Entity"
   },
   "useDefaultValue": true,
   "value": null
  }
 ]
}
```

</details>
