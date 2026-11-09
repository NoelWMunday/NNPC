# PPP_FIN_GLPostings (Multi)

| | |
|---|---|
| SAC id | `D1612E84BFC3F305DC043E546B4B0D5A` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-07-22T14:03:06.303Z by NMUNDAY |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | GL Postings | NESTED_SEQUENCE | runs [PPP_GLPost_BusPremise](PPP_GLPost_BusPremise.md) |

### 1. GL Postings — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:E2716605229298231EC8A987439CC522",
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
