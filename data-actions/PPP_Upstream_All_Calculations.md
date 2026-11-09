# PPP_Upstream_All_Calculations

| | |
|---|---|
| SAC id | `C056EE84BFC39D3C4C720972D2EC2980` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-09-25T12:02:28.772Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_UStream](../stories/PPP_UStream.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget 2026 (Reference)"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"#"` |
| `CAPEX_Version` | PROMPT | MEMBER | Version | SINGLE | `"public.Plan 2027-2031 iteration 01"` |
| `CAPEX_PCycle` | PROMPT | MEMBER | Plan_Cycle | SINGLE | `"#"` |
| `CAPEX_Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | NESTED_SEQUENCE | runs [PPP_Upstream_Revenue](PPP_Upstream_Revenue.md) |
| 2 | (unnamed) | NESTED_SEQUENCE | runs [PPP_Upstream_Royalties](PPP_Upstream_Royalties.md) |
| 3 | (unnamed) | NESTED_SEQUENCE | runs [PPP_Upstream_CostAlloc](PPP_Upstream_CostAlloc.md) |
| 4 | (unnamed) | NESTED_SEQUENCE | runs [PPP_Upstream_Tax](PPP_Upstream_Tax.md) |

### 1. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:E1751684BFC7BECB4638AFAF2DC6D009",
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
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:F4851684BFC29D7E2AE8285F175632F1",
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
  },
  {
   "id": {
    "displayKey": "PCycle"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "PCycle"
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
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:398D1684BFC6147FBA0CF82732D452F6",
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
    "displayKey": "PCycle_CAPEX"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CAPEX_PCycle"
   }
  },
  {
   "id": {
    "displayKey": "Version_CAPEX"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CAPEX_Version"
   }
  },
  {
   "id": {
    "displayKey": "Entity_CAPEX"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CAPEX_Entity"
   }
  }
 ]
}
```

</details>

### 4. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:AC8D1684BFC501FD9340601FF47A5050",
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
  },
  {
   "id": {
    "displayKey": "PCycle"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "PCycle"
   }
  }
 ]
}
```

</details>
