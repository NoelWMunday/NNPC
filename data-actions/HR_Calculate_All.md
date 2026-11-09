# HR_Calculate_All

| | |
|---|---|
| SAC id | `F01B0C0771E59D10E3D508616F5352E9` |
| Default model | PPP Workforce planning |
| Created by | NMUNDAY |
| Last changed | 2026-10-14T12:32:00.805Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_HR](../stories/PPP_HR.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | SINGLE | `"#"` |
| `CY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2025", "202512"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | NESTED_SEQUENCE | runs [HR_Read_central_rates](HR_Read_central_rates.md) |
| 2 | (unnamed) | NESTED_SEQUENCE | runs [HR_Calculate_Reference_Prod_Overhead_Split](HR_Calculate_Reference_Prod_Overhead_Split.md) |
| 3 | (unnamed) | NESTED_SEQUENCE | runs [HR_Calculate_Salaries_Cost](HR_Calculate_Salaries_Cost.md) |
| 4 | (unnamed) | NESTED_SEQUENCE | runs [HR_Calculate_Expense_Currency_Conversion_CalcFields](HR_Calculate_Expense_Currency_Conversion_CalcFields.md) |

### 1. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:E0415E8CBFC039DDEBF73F1F7EC06B34",
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
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:C9B8C684BFC20C3314779C5D673EB7B3",
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
    "displayKey": "EntitySelection"
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
    "paramRef": "CY"
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
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:E081B88E2A31CF2B4CB830641D78E1BC",
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
    "displayKey": "DateSelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     [
      "(all)"
     ]
    ],
    "hierarchyName": "YM"
   }
  },
  {
   "id": {
    "displayKey": "GradeSelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "Total",
     "RS_05"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "EntitySelection"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "Entity"
   }
  },
  {
   "id": {
    "displayKey": "ReportingDate"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CY"
   }
  },
  {
   "id": {
    "displayKey": "CY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CY"
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

### 4. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:DA232E84BFC6B8B952F047BACECBBD72",
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
    "displayKey": "DateSelection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     [
      "(all)"
     ]
    ],
    "hierarchyName": "YM"
   }
  },
  {
   "id": {
    "displayKey": "EntitySelection"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "Entity"
   }
  },
  {
   "id": {
    "displayKey": "LIneItem"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "EX_GL",
     "EX_GL_MN"
    ],
    "hierarchyName": "H1"
   }
  },
  {
   "id": {
    "displayKey": "GL_Selection"
   },
   "useDefaultValue": false,
   "value": {
    "memberIds": [
     "HR"
    ],
    "hierarchyName": "H1"
   }
  }
 ]
}
```

</details>
