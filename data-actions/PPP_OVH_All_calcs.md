# PPP_OVH_All_calcs

> Overheads & other - All calculations

| | |
|---|---|
| SAC id | `B161368CBFC62646E8C57003ED656C2A` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-09-02T09:23:19.640Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_Overheads](../stories/PPP_Overheads.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | NESTED_SEQUENCE | runs [PPP_CurConv](PPP_CurConv.md) |
| 2 | (unnamed) | NESTED_SEQUENCE | **DISABLED** runs [PPP_GL_YTD_Dec](PPP_GL_YTD_Dec.md) |

### 1. (unnamed) — NESTED_SEQUENCE

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
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:6D49F8862A320A323A85713B3BD58453",
 "disabled": true,
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
