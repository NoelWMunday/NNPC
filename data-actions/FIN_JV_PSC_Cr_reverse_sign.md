# FIN_JV_PSC_Cr_reverse sign

> JV's and PSC's Posting - Cr reverse sign

| | |
|---|---|
| SAC id | `D7AB684BFC3986817571680A7E00627` |
| Default model | PPP Financial |
| Created by | NMUNDAY |
| Last changed | 2026-07-26T13:36:07.979Z by NMUNDAY |
| Called by | — |
| Used in stories | — |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["NB04"]` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Reverse sign | SCRIPT |  |

### 1. Reverse sign — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = "CR_GC"
MEMBERSET [d/PPP_Account] = BASEMEMBER([d/PPP_Account] , "TO")
MEMBERSET [d/PPP_EntryNr] = "UP_0005"

DATA() = 0 - RESULTLOOKUP()
```

Parameters used: Entity, PCycle
