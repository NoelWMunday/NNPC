# PPP_ProdServ_All_calcs

| | |
|---|---|
| SAC id | `4A293E8CBFC2AEE8F88037B05EE384A6` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-09-01T11:47:59.383Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_ProdServices](../stories/PPP_ProdServices.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | NESTED_SEQUENCE | runs [PPP_PrdSrv](PPP_PrdSrv.md) |
| 2 | (unnamed) | NESTED_SEQUENCE | runs [PPP_CurConv_PrdSrv](PPP_CurConv_PrdSrv.md) |
| 3 | (unnamed) | NESTED_SEQUENCE | runs [PPP_PrdSrv_GLEntries](PPP_PrdSrv_GLEntries.md) |

### 1. (unnamed) — NESTED_SEQUENCE

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
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "#"
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
    "paramRef": "Entity"
   }
  }
 ]
}
```

</details>

### 2. (unnamed) — NESTED_SEQUENCE

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
    "displayKey": "Entity"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "Entity"
   }
  }
 ]
}
```

</details>

### 3. (unnamed) — NESTED_SEQUENCE

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
   "useDefaultValue": false,
   "value": {
    "paramRef": "Entity"
   }
  }
 ]
}
```

</details>
