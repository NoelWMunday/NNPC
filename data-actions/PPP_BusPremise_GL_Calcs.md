# PPP_BusPremise_GL_Calcs

| | |
|---|---|
| SAC id | `5F112684BFC7507B6B9B3DFB43CA3D36` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-07-22T13:01:14.185Z by NMUNDAY |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Currency conversion | NESTED_SEQUENCE | runs [PPP_CurConv](PPP_CurConv.md) |
| 2 | Annual total | NESTED_SEQUENCE | runs [PPP_GL_YTD_Dec](PPP_GL_YTD_Dec.md) |

### 1. Currency conversion — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:527E18802BA4CE9414A6EC3227AC5B1D",
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

### 2. Annual total — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:6D49F8862A320A323A85713B3BD58453",
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
