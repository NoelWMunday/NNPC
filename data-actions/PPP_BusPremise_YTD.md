# PPP_BusPremise_YTD

| | |
|---|---|
| SAC id | `49E89E00A2D82815B4792D973DB7D729` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-24T14:05:50.035Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_BusPremise](../stories/PPP_BusPremise.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `"public.Budget 2026 (Reference)"` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["NB04"]` |
| `CurrentYR` | PROMPT | MEMBER | Date | SINGLE | `["(all)", "2026"]` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | (unnamed) | DELETE_FACTS |  |
| 2 | (unnamed) | SCRIPT |  |

### 1. (unnamed) — DELETE_FACTS

<details><summary>Configuration</summary>

```json
{
 "sourceContext": {
  "Version": {
   "memberId": {
    "paramRef": "TargetVersion"
   },
   "hierarchyName": null
  },
  "PPP_Entity": {
   "memberIds": [
    {
     "paramRef": "Entity"
    }
   ],
   "hierarchyName": "H1"
  },
  "CustomDimension1": {
   "memberIds": [
    "YEO"
   ],
   "hierarchyName": null
  },
  "Date": {
   "memberIds": [
    {
     "paramRef": "CurrentYR"
    }
   ],
   "hierarchyName": "YM"
  }
 },
 "sourceContextFilterParamRefs": [],
 "deleteMode": "DELETE",
 "disabled": false
}
```

</details>

### 2. (unnamed) — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)


FOREACH [d/Date].[p/YEAR]

	IF [d/Date] = BASEMEMBER([d/Date] , %CurrentYR%) THEN
		
		DATA.APPEND(
				[d/Measures] = "YEO",
				[d/Date] = LAST([d/Date])
			   ) =
		RESULTLOOKUP(
				 [d/Measures] = "Number"
				)
		
	ENDIF
	
ENDFOR
```

Parameters used: Entity, CurrentYR
