# CAPEX_Movable_Calcs

| | |
|---|---|
| SAC id | `929F08E2A32E615E4B743B27C3B1098` |
| Default model | CAPEX |
| Created by | DPARUMAUL |
| Last changed | 2026-07-17T08:27:12.558Z by DPARUMAUL |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | FUSD | NESTED_SEQUENCE | runs [CAPEX_CurCon](CAPEX_CurCon.md) |
| 2 | YTD | NESTED_SEQUENCE | runs [CAPEX_Y-T-D](CAPEX_Y-T-D.md) |
| 3 | GL | NESTED_SEQUENCE | runs [PPP_CAPEX_MGLEntries](PPP_CAPEX_MGLEntries.md) |

### 1. FUSD — NESTED_SEQUENCE

FUSD Calculation

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:3C8846052291A0F00AC308BB42C71038",
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

### 2. YTD — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:8BDE68862A313C385149F02D86577CDB",
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

### 3. GL — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:72EF70862A31E1E180AC185FD660962B",
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
    "memberIds": [
     "TOTAL"
    ],
    "hierarchyName": "H1"
   }
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
