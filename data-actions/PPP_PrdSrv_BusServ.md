# PPP_PrdSrv_BusServ

> Products & Services - Business services calcs

| | |
|---|---|
| SAC id | `CB0B1E84BFC1472D256296FA1D8E02B7` |
| Default model | Business premise |
| Created by | NMUNDAY |
| Last changed | 2026-08-26T09:24:29.557Z by NMUNDAY |
| Called by | — |
| Used in stories | [PPP_ProdServices_bkup](../stories/PPP_ProdServices_bkup.md) |

## Parameters

| Key | Input | Type | Dimension | Cardinality | Default |
|---|---|---|---|---|---|
| `TargetVersion` | PROMPT | MEMBER | Version | SINGLE | `{"memberId": null, "hierarchyName": null}` |
| `Entity` | PROMPT | MEMBER | PPP_Entity | MULTI | `["TOTAL"]` |
| `PCycle` | PROMPT | MEMBER | PCycle | SINGLE | `"2026-2030/01"` |

## Steps

| # | Step | Type | Notes |
|---|---|---|---|
| 1 | Taxation - Education | SCRIPT |  |
| 2 | Taxation - Cpy (Convert to NGN) | CONVERSION |  |
| 3 | Taxation - Company | SCRIPT |  |

### 1. Taxation - Education — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/PPP_EntryNr] = "BP002"
MEMBERSET [d/PPP_Currency] = ("NGN","USD")
MEMBERSET [d/Measures] = "GC_CR"
// MEMBERSET [d/GL] = "5100008"
MEMBERSET [d/Lock] = "#"
// MEMBERSET [d/ProductServ] = "#"
// MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

VARIABLEMEMBER #TAX_RATE OF [d/WPLn]
VARIABLEMEMBER #INCOME OF [d/WPLn]
VARIABLEMEMBER #EXPENSES OF [d/WPLn]
VARIABLEMEMBER #TAXABLE OF [d/WPLn]
VARIABLEMEMBER #TAXABLE_AFTER_ED OF [d/WPLn]
VARIABLEMEMBER #TAX_ED OF [d/WPLn]

DATA([d/ProductServ] = "#", [d/Ln] = "#", [d/PPP_Currency] = "USD", [d/WPLn] = #TAXABLE) = 0

DATA([d/ProductServ] = "#", [d/Ln] = "#", [d/PPP_Currency] = "USD", [d/WPLn] = #TAX_RATE, [d/GL] = "#") =
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "GA_050", [d/PPP_Entity] = "#", [d/Lock] = "Central", [d/PPP_Currency] = "#", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/ProductServ] = "#", [d/Ln] = "#")

IF [d/GL] = BASEMEMBER([d/GL] , "Revenue") THEN
	DATA.APPEND([d/WPLn] = #INCOME, [d/GL] = "5100008", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#") = 
		RESULTLOOKUP()
ENDIF

IF [d/GL] = BASEMEMBER([d/GL] , "COGS") THEN
	DATA.APPEND([d/WPLn] = #EXPENSES, [d/GL] = "5100008", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#") = 
		RESULTLOOKUP()
ENDIF

DATA([d/WPLn] = #TAXABLE, [d/GL] = "5100008", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#") = 
	RESULTLOOKUP([d/WPLn] = #INCOME) - RESULTLOOKUP([d/WPLn] = #EXPENSES)

DATA([d/GL] = "5100008", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#") = 
	RESULTLOOKUP([d/WPLn] = #TAXABLE) * 
	RESULTLOOKUP([d/WPLn] = #TAX_RATE, [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#", [d/GL] = "#") / 100

// Send gross sales in $ to a holding account to determine the tax rate which is calculated in the next
// few steps
DATA([d/GL] = "5100005", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#") = RESULTLOOKUP([d/WPLn] = #INCOME)

DATA([d/WPLn] = #TAX_ED, [d/GL] = "5100008", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#") = 
	RESULTLOOKUP([d/GL] = "5100008", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#")
	
DATA([d/WPLn] = #TAXABLE_AFTER_ED, [d/GL] = "5100008", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#") = 
	RESULTLOOKUP([d/WPLn] = #TAXABLE) - RESULTLOOKUP([d/WPLn] = #TAX_ED)

DATA([d/Measures] = "DR", [d/GL] = "5100008", [d/PPP_Currency] = "USD", [d/ProductServ] = "#", [d/Ln] = "#") = RESULTLOOKUP([d/WPLn] = #TAXABLE_AFTER_ED)
```

Parameters used: Entity, PCycle

### 2. Taxation - Cpy (Convert to NGN) — CONVERSION

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
  "PCycle": {
   "memberIds": [
    {
     "paramRef": "PCycle"
    }
   ],
   "hierarchyName": "H1"
  },
  "GL": {
   "memberIds": [
    "5100005"
   ],
   "hierarchyName": "H1"
  }
 },
 "sourceContextFilterParamRefs": [],
 "conversionRules": [
  {
   "source": {
    "hierarchyName": null,
    "memberId": "GC_CR"
   },
   "target": {
    "hierarchyName": null,
    "memberId": "DR"
   },
   "fixedDate": null,
   "delta": {
    "granularity": "MONTH",
    "shift": 0
   },
   "category": "DYNAMIC",
   "rateVersion": null
  }
 ],
 "writeMode": "OVERWRITE"
}
```

</details>

### 3. Taxation - Company — SCRIPT

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// In SAC the amount may show against a currency of USD but still actually be the NGN amount because
// if i currency convert from multiple source currencies into a USD measure the USD measure retains the 
// currency dimension source ID of the transaction currency. So here we grab the gross revenue from the 
// group currency GL's in USD and convert back to NGN for the company tax. The tax measure is in NGN but the
// line item currency ID will show USD. 

MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/PPP_EntryNr] = "BP002"
MEMBERSET [d/PPP_Currency] = ("USD")
MEMBERSET [d/Measures] = "DR"
MEMBERSET [d/GL] = "5100005"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/WPLn] = "#"

VARIABLEMEMBER #TAX_RATE OF [d/WPLn]
VARIABLEMEMBER #TAX_RATE_MIN OF [d/WPLn]
VARIABLEMEMBER #GROSS_INCOME OF [d/WPLn]

DATA([d/WPLn] = #GROSS_INCOME) = RESULTLOOKUP()
// Debug purposes
DATA([d/GL] = "5100011") = RESULTLOOKUP([d/WPLn] = #GROSS_INCOME)

DATA([d/WPLn] = #TAX_RATE_MIN) =
	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "GA_CITA_20", [d/PPP_Entity] = "#", [d/Lock] = "Central", [d/PPP_Currency] = "#", [d/GL] = "#", [d/PPP_EntryNr] = "#")

// Debug purposes
// DATA([d/GL] = "5100011") = RESULTLOOKUP([d/WPLn] = #TAX_RATE_MIN)
	
IF RESULTLOOKUP([d/WPLn] = #GROSS_INCOME) > 100000000 THEN
	DATA([d/WPLn] = #TAX_RATE) = 
		RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "GA_CITA_05", [d/PPP_Entity] = "#", [d/Lock] = "Central", [d/PPP_Currency] = "#", [d/GL] = "#", [d/PPP_EntryNr] = "#")
ELSE
	IF RESULTLOOKUP([d/WPLn] = #GROSS_INCOME) > 25000000 THEN
		DATA([d/WPLn] = #TAX_RATE) = 
			RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "GA_CITA_10", [d/PPP_Entity] = "#", [d/Lock] = "Central", [d/PPP_Currency] = "#", [d/GL] = "#", [d/PPP_EntryNr] = "#")
	ELSE
		DATA([d/WPLn] = #TAX_RATE) = 
			RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "GA_CITA_15", [d/PPP_Entity] = "#", [d/Lock] = "Central", [d/PPP_Currency] = "#", [d/GL] = "#", [d/PPP_EntryNr] = "#")
	ENDIF
ENDIF

IF RESULTLOOKUP([d/WPLn] = #TAX_RATE_MIN) > RESULTLOOKUP([d/WPLn] = #TAX_RATE) THEN
	DATA([d/WPLn] = #TAX_RATE) = RESULTLOOKUP([d/WPLn] = #TAX_RATE_MIN)
ENDIF

// Debug purposes
DATA([d/GL] = "5100011") = RESULTLOOKUP([d/WPLn] = #TAX_RATE)

DATA([d/Measures] = "GC_CR", [d/GL] = "5100005") = RESULTLOOKUP([d/GL] = "5100008") * RESULTLOOKUP([d/WPLn] = #TAX_RATE) / 100
```

Parameters used: Entity, PCycle
