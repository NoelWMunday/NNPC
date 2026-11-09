# PPP_Products & Services (Multi)

> Products & Services (Multi)

| | |
|---|---|
| SAC id | `8661B8862A334676DF95A979364567AB` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-06-26T14:01:53.602Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_ProdServices](../stories/PPP_ProdServices.md), [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | QTY x Price | NESTED_SEQUENCE | runs [PPP_PrdSrv](PPP_PrdSrv.md) |
| 2 | Currency conversion | NESTED_SEQUENCE | runs [PPP_CurConv_PrdSrv](PPP_CurConv_PrdSrv.md) |
| 3 | Determine GL codes | NESTED_SEQUENCE | runs [PPP_PrdSrv_GLEntries](PPP_PrdSrv_GLEntries.md) |
| 4 | Backward calculate historical values | NESTED_SEQUENCE | runs [PPP_PrdSrv_Historical](PPP_PrdSrv_Historical.md) |

### 1. QTY x Price — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:C53F68802BA15A7F8BBE416AC7FA910E",
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

### 2. Currency conversion — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:950F68802BA581C0A6F35C2466EF15E9",
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

### 3. Determine GL codes — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:3CC896052292306E90D1BF327E531771",
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
    "displayKey": "Entity"
   },
   "useDefaultValue": true,
   "value": null
  },
  {
   "id": {
    "displayKey": "PCycle"
   },
   "useDefaultValue": true,
   "value": null
  }
 ]
}
```

</details>

### 4. Backward calculate historical values — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:DEBA26052294CB60CEA4B06DBF678BE2",
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
