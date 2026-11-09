# PPP_GLPost_BusPremise

> GLPostings from BusPremise

| | |
|---|---|
| SAC id | `E2716605229298231EC8A987439CC522` |
| Default model | PPP Financial |
| Created by | NMUNDAY |
| Last changed | 2026-10-09T10:06:52.201Z by NMUNDAY |
| Called by | [PPP_FIN_GLPostings (Multi)](PPP_FIN_GLPostings_Multi.md) |
| Used in stories | [PPP_Financial](../stories/PPP_Financial.md), [PPP_Financial_Test](../stories/PPP_Financial_Test.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `Entity_FIN` | PROMPT | MEMBER | PPP_Entity | MULTI | `{"memberIds": [], "hierarchyName": null}` |
| `Version_FIN` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Entity_CAPEX` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `Version_BusPremise` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `Version_CAPEX` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget"` |
| `CurrentFY` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2026", "202612"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Initialisation | SCRIPT |  |
| 2 | Revenue - GL Posting from Bus Premise | CROSSMODELCOPY | from Business premise |
| 3 | Revenue - GL Posting from Bus Premise (Contra) | CROSSMODELCOPY | from Business premise |
| 4 | Expenses - GL Posting from Bus Premise | CROSSMODELCOPY | from Business premise |
| 5 | Expenses - GL Posting from Bus Premise (Contra) | CROSSMODELCOPY | from Business premise |
| 6 | HR Expenses - GL Posting from Bus Premise | CROSSMODELCOPY | from Business premise |
| 7 | Expenses - GL Posting from Bus Premise (Contra) | CROSSMODELCOPY | from Business premise |
| 8 | JV's and PSC's - Cr | CROSSMODELCOPY | from Business premise |
| 9 | JV's and PSC's - Cr  (Contra) | CROSSMODELCOPY | from Business premise |
| 10 | JV's and PSC's - Cr  (Inter-cpy Contra) | CROSSMODELCOPY | from Business premise |
| 11 | JV's and PSC's - Dr | CROSSMODELCOPY | from Business premise |
| 12 | JV's and PSC's - Dr  (Contra) | CROSSMODELCOPY | from Business premise |
| 13 | JV's and PSC's - Dr  (Inter-cpy Contra) | CROSSMODELCOPY | from Business premise |
| 14 | CAPEX Projects | CROSSMODELCOPY | from CAPEX |
| 15 | CAPEX Projects (Contra) | CROSSMODELCOPY | from CAPEX |
| 16 | CAPEX Movables | CROSSMODELCOPY | from CAPEX |
| 17 | CAPEX Movables (Contra) | CROSSMODELCOPY | from CAPEX |
| 18 | Reverse CR sign | SCRIPT |  |
| 19 | (unnamed) | NESTED_SEQUENCE | runs [PPP_FIN_GL_cross-cast](PPP_FIN_GL_cross-cast.md) |
| 20 | Copy global parameters to FIN | NESTED_SEQUENCE | runs [FIN_Admin_Parameters](FIN_Admin_Parameters.md) |
| 21 | FIN Calculate educational tax  | NESTED_SEQUENCE | **DISABLED** runs [FIN_Jnl_01](FIN_Jnl_01.md) |
| 22 | Taxation | NESTED_SEQUENCE | runs [FIN_Jnl_02](FIN_Jnl_02.md) |
| 23 | (unnamed) | NESTED_SEQUENCE | runs [PPP_FIN_GL_cross-cast](PPP_FIN_GL_cross-cast.md) |
| 24 | KPI Calculations | NESTED_SEQUENCE | runs [FIN_KPI_Calculations](FIN_KPI_Calculations.md) |

### 1. Initialisation — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Be careful that the default model in a model-to-model copy data action is the target
// so that an initialisation step like this clears the destination and not the source

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity_FIN%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/PPP_EntryNr] = (BASEMEMBER([d/PPP_EntryNr] , "UP"),"BP002","BP003","#","Capex","Projects","HR_0005","HR_0010")
MEMBERSET [d/Measures] = ("DR","CR","DR_GC","CR_GC")


DELETE()
```

Parameters used: Entity_FIN

### 2. Revenue - GL Posting from Bus Premise — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_BusPremise"
   },
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "Revenue",
    "OTHER_INC"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "BP002",
    "HR_0005",
    "BP003"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CLO",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    },
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "targetHierarchy": "YM",
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Account": {
   "sourceDimensionId": "GL",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "DEFAULT",
   "completionDefaultMember": {
    "memberId": "EQ_005",
    "hierarchyName": "parentId"
   },
   "memberMappings": []
  },
  "PCycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 3. Revenue - GL Posting from Bus Premise (Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_BusPremise"
   },
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "Revenue",
    "OTHER_INC"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "BP002",
    "HR_0005",
    "BP003"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    },
    {
     "source": {
      "memberId": "GC_CLO",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "PCycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "targetHierarchy": "YM",
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "CA_010",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 4. Expenses - GL Posting from Bus Premise — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_BusPremise"
   },
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "COGS",
    "OTHER_DCST",
    "COS_DPR",
    "ROYALTIES",
    "CHOOCA",
    "TAX_HIST",
    "NON_CASH",
    "GEN_ADMIN",
    "HR",
    "OTHER"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "BP002",
    "BP003"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    },
    {
     "source": {
      "memberId": "GC_CLO",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "sourceDimensionId": "GL",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "DEFAULT",
   "completionDefaultMember": {
    "memberId": "EQ_005",
    "hierarchyName": "parentId"
   },
   "memberMappings": []
  },
  "PCycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 5. Expenses - GL Posting from Bus Premise (Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_BusPremise"
   },
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "COGS",
    "OTHER_DCST",
    "COS_DPR",
    "ROYALTIES",
    "CHOOCA",
    "TAX_HIST",
    "NON_CASH",
    "GEN_ADMIN",
    "HR",
    "OTHER"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "BP002",
    "BP003"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    },
    {
     "source": {
      "memberId": "GC_CLO",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "CL_005",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  },
  "PCycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 6. HR Expenses - GL Posting from Bus Premise — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_BusPremise"
   },
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "HR"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CLO",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "sourceDimensionId": "GL",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "DEFAULT",
   "completionDefaultMember": {
    "memberId": "EQ_005",
    "hierarchyName": "parentId"
   },
   "memberMappings": []
  },
  "PCycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 7. Expenses - GL Posting from Bus Premise (Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_BusPremise"
   },
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "HR"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CLO",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "CL_005",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  },
  "PCycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 8. JV's and PSC's - Cr — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "Revenue",
    "OTHER_INC"
   ],
   "hierarchyName": "H1"
  },
  "Objectives": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "UP"
   ],
   "hierarchyName": "H1"
  },
  "ProductServ": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Strategy": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WorkProgram": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "PCycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "sourceDimensionId": "GL",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "DEFAULT",
   "completionDefaultMember": {
    "memberId": "CL_005",
    "hierarchyName": "parentId"
   },
   "memberMappings": []
  }
 }
}
```

</details>

### 9. JV's and PSC's - Cr  (Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "Revenue",
    "OTHER_INC"
   ],
   "hierarchyName": "H1"
  },
  "Objectives": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "UP_0005"
   ],
   "hierarchyName": "H1"
  },
  "ProductServ": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Strategy": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WorkProgram": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "PCycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "CA_010",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 10. JV's and PSC's - Cr  (Inter-cpy Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "Revenue",
    "OTHER_INC"
   ],
   "hierarchyName": "H1"
  },
  "Objectives": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "UP_0010",
    "UP_0015"
   ],
   "hierarchyName": "H1"
  },
  "ProductServ": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Strategy": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WorkProgram": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "PCycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "LTL_015",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 11. JV's and PSC's - Dr — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "COGS",
    "OTHER_DCST",
    "COS_DPR",
    "ROYALTIES",
    "CHOOCA",
    "TAX_HIST",
    "NON_CASH",
    "GEN_ADMIN",
    "HR",
    "OTHER"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "UP"
   ],
   "hierarchyName": "H1"
  },
  "Objectives": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "ProductServ": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Strategy": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WorkProgram": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "PCycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "sourceDimensionId": "GL",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "DEFAULT",
   "completionDefaultMember": {
    "memberId": "EQ_005",
    "hierarchyName": "parentId"
   },
   "memberMappings": []
  }
 }
}
```

</details>

### 12. JV's and PSC's - Dr  (Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "COGS",
    "OTHER_DCST",
    "COS_DPR",
    "ROYALTIES",
    "CHOOCA",
    "TAX_HIST",
    "NON_CASH",
    "GEN_ADMIN",
    "HR",
    "OTHER"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "UP_0005"
   ],
   "hierarchyName": "H1"
  },
  "Objectives": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "ProductServ": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Strategy": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WorkProgram": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "PCycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "CL_005",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 13. JV's and PSC's - Dr  (Inter-cpy Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cuv5rh01bkl1726m85cg2id8u2c",
 "sourceContext": {
  "Version": {
   "memberId": "public.Budget",
   "hierarchyName": null
  },
  "PCycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "COGS",
    "OTHER_DCST",
    "COS_DPR",
    "ROYALTIES",
    "CHOOCA",
    "TAX_HIST",
    "NON_CASH",
    "GEN_ADMIN",
    "HR",
    "OTHER"
   ],
   "hierarchyName": "H1"
  },
  "PPP_EntryNr": {
   "memberIds": [
    "UP_0010",
    "UP_0015"
   ],
   "hierarchyName": "H1"
  },
  "Objectives": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "ProductServ": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "Strategy": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WorkProgram": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "WPLn": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "GC_CR",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "sourceDimensionId": "PPP_EntryNr",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "PCycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "LTL_015",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  }
 }
}
```

</details>

### 14. CAPEX Projects — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cbifmh01bklfvf7ijs46d1ano3b",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_CAPEX"
   },
   "hierarchyName": null
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity_CAPEX"
    }
   ],
   "hierarchyName": "H1"
  },
  "Plan_Cycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "CustomDimension1": {
   "memberIds": [
    "PC_FUSD"
   ],
   "hierarchyName": null
  },
  "PPP_Currency": {
   "memberIds": [
    "USD"
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "PC_FUSD",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "FA02_AUC",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  },
  "PPP_EntryNr": {
   "defaultMember": {
    "memberId": "Projects",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PCycle": {
   "defaultMember": {
    "memberId": "#",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  }
 }
}
```

</details>

### 15. CAPEX Projects (Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cbifmh01bklfvf7ijs46d1ano3b",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_CAPEX"
   },
   "hierarchyName": null
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity_CAPEX"
    }
   ],
   "hierarchyName": "H1"
  },
  "Plan_Cycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "CustomDimension1": {
   "memberIds": [
    "PC_FUSD"
   ],
   "hierarchyName": null
  },
  "PPP_Currency": {
   "memberIds": [
    "USD"
   ],
   "hierarchyName": "H1"
  },
  "Lock": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "Plan_Cycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "defaultMember": {
    "memberId": "Projects",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "CL_005",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  },
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "PC_FUSD",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  }
 }
}
```

</details>

### 16. CAPEX Movables — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cbifmh01bklfvf7ijs46d1ano3b",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_CAPEX"
   },
   "hierarchyName": null
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity_CAPEX"
    }
   ],
   "hierarchyName": "H1"
  },
  "Plan_Cycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "MovableItems": {
   "memberIds": [
    "Total"
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "GL"
   ],
   "hierarchyName": "H1"
  },
  "CustomDimension1": {
   "memberIds": [
    "AMT_GL_GC"
   ],
   "hierarchyName": null
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "AMT_GL_GC",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "DR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  },
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Account": {
   "sourceDimensionId": "GL",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "DEFAULT",
   "completionDefaultMember": {
    "memberId": "EQ_005",
    "hierarchyName": "parentId"
   },
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "defaultMember": {
    "memberId": "Capex",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PCycle": {
   "sourceDimensionId": "Plan_Cycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  }
 }
}
```

</details>

### 17. CAPEX Movables (Contra) — CROSSMODELCOPY

<details><summary>Configuration</summary>

```json
{
 "sourceCubeId": "Cbifmh01bklfvf7ijs46d1ano3b",
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "Version_CAPEX"
   },
   "hierarchyName": null
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity_CAPEX"
    }
   ],
   "hierarchyName": "H1"
  },
  "Plan_Cycle": {
   "memberIds": [
    "#"
   ],
   "hierarchyName": "H1"
  },
  "MovableItems": {
   "memberIds": [
    "Total"
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "GL"
   ],
   "hierarchyName": "H1"
  },
  "CustomDimension1": {
   "memberIds": [
    "AMT_GL_GC"
   ],
   "hierarchyName": null
  }
 },
 "sourceContextFilterParamRefs": [],
 "writeMode": "OVERWRITE",
 "mappings": {
  "Date": {
   "sourceDimensionId": "Date",
   "autoMappingStrategy": "START_DATE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [],
   "autoMappingOptions": {
    "sourceProperty": "DATE",
    "targetProperty": "DATE"
   }
  },
  "PPP_Currency": {
   "sourceDimensionId": "PPP_Currency",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_Entity": {
   "sourceDimensionId": "PPP_Entity",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PCycle": {
   "sourceDimensionId": "Plan_Cycle",
   "autoMappingStrategy": "IDENTICAL_NAMES",
   "completionMode": "MANUAL",
   "completionDefaultMember": null,
   "memberMappings": []
  },
  "PPP_EntryNr": {
   "defaultMember": {
    "memberId": "Capex",
    "hierarchyName": "H1"
   },
   "sourceDimensionId": null
  },
  "PPP_Account": {
   "defaultMember": {
    "memberId": "CL_005",
    "hierarchyName": "parentId"
   },
   "sourceDimensionId": null
  },
  "CustomDimension1": {
   "sourceDimensionId": "CustomDimension1",
   "autoMappingStrategy": "NONE",
   "completionMode": "IGNORE",
   "completionDefaultMember": null,
   "memberMappings": [
    {
     "source": {
      "memberId": "AMT_GL_GC",
      "hierarchyName": null
     },
     "target": {
      "memberIds": [
       "CR_GC"
      ],
      "hierarchyName": null
     }
    }
   ]
  }
 }
}
```

</details>

### 18. Reverse CR sign — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity_FIN%)
MEMBERSET [d/PCycle] = "#"
MEMBERSET [d/Measures] = ("CR","CR_GC")
MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account] , "GL")
MEMBERSET [d/PPP_EntryNr] = (BASEMEMBER([d/PPP_EntryNr] , "UP"),"BP002","BP003","Capex","Projects","HR_0005","HR_0010")

IF [d/Version] = %Version_FIN% THEN
	DATA() = 0 - RESULTLOOKUP()
ENDIF
```

Parameters used: Entity_FIN, Version_FIN

### 19. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:4339660522912877CF641BF760FFA59F",
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
    "paramRef": "Entity_FIN"
   }
  },
  {
   "id": {
    "displayKey": "CurrentFY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentFY"
   }
  }
 ]
}
```

</details>

### 20. Copy global parameters to FIN — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:C1A1BC0771E5A68F187AB32B09251E73",
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
    "paramRef": "Entity_FIN"
   }
  },
  {
   "id": {
    "displayKey": "CY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentFY"
   }
  },
  {
   "id": {
    "displayKey": "Version_BusPremise"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "Version_BusPremise"
   }
  }
 ]
}
```

</details>

### 21. FIN Calculate educational tax  — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:B591BC0771E7349F8672BF558A346AF0",
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
    "paramRef": "Entity_FIN"
   }
  },
  {
   "id": {
    "displayKey": "CY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentFY"
   }
  }
 ]
}
```

</details>

### 22. Taxation — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:7BC9D40771E66EE8795AF2AB80CB78CF",
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
    "paramRef": "Entity_FIN"
   }
  },
  {
   "id": {
    "displayKey": "CY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentFY"
   }
  }
 ]
}
```

</details>

### 23. (unnamed) — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:4339660522912877CF641BF760FFA59F",
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
    "paramRef": "Entity_FIN"
   }
  },
  {
   "id": {
    "displayKey": "CurrentFY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentFY"
   }
  }
 ]
}
```

</details>

### 24. KPI Calculations — NESTED_SEQUENCE

<details><summary>Configuration</summary>

```json
{
 "nestedSequenceId": "PLANNINGSEQUENCE:t.B:76D484037947247EF51B241BD45D3674",
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
    "paramRef": "Entity_FIN"
   }
  },
  {
   "id": {
    "displayKey": "CY"
   },
   "useDefaultValue": false,
   "value": {
    "paramRef": "CurrentFY"
   }
  }
 ]
}
```

</details>
