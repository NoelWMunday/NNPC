# Script diff

Left = live in SAC (`sac-export/` on `main`), right = proposed.

| Data action | Step | Lines |
|---|---|---|
| PPP_Upstream_Royalties | 1. Initialise | +10 / -1 |
| PPP_Upstream_CostAlloc | 13. GL Entries | +0 / -8 |

## PPP_Upstream_Royalties — step 1. Initialise

```diff
@@ -6,5 +6,5 @@ MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
 MEMBERSET [d/PCycle] = %PCycle%
 MEMBERSET [d/Measures]="Value_WPLn"
-MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] ,"CST05" )
+MEMBERSET [d/WPLn] = (BASEMEMBER([d/WPLn] ,"CST05" ), "AMT_200", "AMT_210", "AMT_220", "AMT_230")
 MEMBERSET [d/GL] = "#"
 MEMBERSET [d/Ln] = "#"
@@ -14,4 +14,13 @@ MEMBERSET [d/Strategy] = "#"
 MEMBERSET [d/WorkProgram] = "#"
 MEMBERSET [d/Lock] = "#"
+MEMBERSET [d/PPP_Currency] = "#"
 
 DELETE()
+
+// Capex/Opex inputs are captured on PPP_Currency = USD. The Financial tab uses the UOM measure and shows "#",
+// so copy each input leaf (same PPP_EntryNr) to "#". The gas flare penalty (AMT_230 x UAP_GFP) cleared above
+// is recalculated in step 13.
+DATA([d/WPLn]="AMT_200") = RESULTLOOKUP([d/WPLn]="AMT_200", [d/PPP_Currency]="USD")
+DATA([d/WPLn]="AMT_210") = RESULTLOOKUP([d/WPLn]="AMT_210", [d/PPP_Currency]="USD")
+DATA([d/WPLn]="AMT_220") = RESULTLOOKUP([d/WPLn]="AMT_220", [d/PPP_Currency]="USD")
+DATA([d/WPLn]="AMT_230") = RESULTLOOKUP([d/WPLn]="AMT_230", [d/PPP_Currency]="USD")
```

## PPP_Upstream_CostAlloc — step 13. GL Entries

```diff
@@ -27,12 +27,4 @@ DATA([d/Measures] = "GC_CR", [d/GL] = "5010001", [d/PPP_EntryNr] = "UP_0010") =
 DATA([d/Measures] = "GC_CR", [d/GL] = "4112001", [d/PPP_EntryNr] = "UP_0010") = 
 	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_15", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
-// COS Depreciation
-//DATA([d/Measures] = "GC_CR", [d/GL] = "4202026", [d/PPP_EntryNr] = "UP_0010") = 
-//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_220", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_15", [d/PPP_Currency] = "#") +
-//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_15", [d/PPP_Currency] = "#")
-// Depletion
-//DATA([d/Measures] = "GC_CR", [d/GL] = "5230003", [d/PPP_EntryNr] = "UP_0010") = 
-//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_220", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_16", [d/PPP_Currency] = "#") +
-//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_5800_16", [d/PPP_Currency] = "#")
 // Apportioned Provision for Impairment
 DATA([d/Measures] = "GC_CR", [d/GL] = "5230006", [d/PPP_EntryNr] = "UP_0010") = 
```
