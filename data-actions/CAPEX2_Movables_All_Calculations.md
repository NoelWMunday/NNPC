# CAPEX2_Movables_All_Calculations

| | |
|---|---|
| SAC id | `EEECE84BFC2E1AECD8B5D8B11AA3A4A` |
| Default model | CAPEX |
| Created by | NMUNDAY |
| Last changed | 2026-10-13T11:33:39.997Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_CAPEX](../stories/PPP_CAPEX.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Plan 2027-2031 iteration 01"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `CY_MM` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |
| `Version_BP` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget 2026 (Reference)"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | NESTED_SEQUENCE | runs [CAPEX2_PriceEscalation](CAPEX2_PriceEscalation.md) |
| 2 | (unnamed) | NESTED_SEQUENCE | runs [CAPEX_QTYxPRICE](CAPEX_QTYxPRICE.md) |
| 3 | (unnamed) | NESTED_SEQUENCE | runs [CAPEX2_Base_Currencies](CAPEX2_Base_Currencies.md) |
| 4 | (unnamed) | NESTED_SEQUENCE | **DISABLED** runs [CAPEX_Y-T-D](CAPEX_Y-T-D.md) |
| 5 | (unnamed) | NESTED_SEQUENCE | runs [PPP_CAPEX_MGLEntries](PPP_CAPEX_MGLEntries.md) |

### 1. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:3190C0771E12D774F1FEC79CDE87340",
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
    "displayKey": "CY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CY_MM"
   }
  },
  {
   "id": {
    "displayKey": "Version_BP"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "Version_BP"
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
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:7BE39684BFC346212D368C5B346F90A9",
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
    "displayKey": "CY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CY_MM"
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

### 4. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:8BDE68862A313C385149F02D86577CDB",
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

### 5. (unnamed) — NESTED_SEQUENCE

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
    "paramRef": "Entity"
   }
  }
 ]
}
```

</details>
