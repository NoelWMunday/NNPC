# Script diff

Left = live (Tax v23), right = proposed.

## PPP_Upstream_Tax — step 21. GL Entries

```diff
@@ -25,2 +25,6 @@ DATA([d/Measures] = "GC_CR", [d/GL] = "5150009", [d/PPP_EntryNr] = "UP_0005") =
 DATA([d/Measures] = "GC_CR", [d/GL] = "4110003", [d/PPP_EntryNr] = "UP_0005") = 0
+// No longer posted by Tax (11 Nov): Direct Cost (in 4500006), corporate overhead and finance cost (CostAlloc, UP_0010)
+DATA([d/Measures] = "GC_CR", [d/GL] = "4101006", [d/PPP_EntryNr] = "UP_0005") = 0
+DATA([d/Measures] = "GC_CR", [d/GL] = "5080044", [d/PPP_EntryNr] = "UP_0005") = 0
+DATA([d/Measures] = "GC_CR", [d/GL] = "FINEXP_005", [d/PPP_EntryNr] = "UP_0005") = 0
 
@@ -35,7 +39,7 @@ DATA([d/Measures] = "GC_CR", [d/GL] = "5100007", [d/PPP_EntryNr] = "UP_0005") =
 	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "RC_TOT_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
-// Direct Cost
-DATA([d/Measures] = "GC_CR", [d/GL] = "4101006", [d/PPP_EntryNr] = "UP_0005") = 
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_GFP", [d/PPP_Currency] = "#")
+// Direct Cost - removed 11 Nov: equity OPEX is posted in 4500006 below
+//DATA([d/Measures] = "GC_CR", [d/GL] = "4101006", [d/PPP_EntryNr] = "UP_0005") = 
+//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
+//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
+//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_GFP", [d/PPP_Currency] = "#")
 // Apportioned Overheads
@@ -60,8 +64,8 @@ DATA([d/Measures] = "GC_CR", [d/GL] = "5230003", [d/PPP_EntryNr] = "UP_0005") =
 //	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_20", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
-// Apportioned Corporate Overhead
-DATA([d/Measures] = "GC_CR", [d/GL] = "5080044", [d/PPP_EntryNr] = "UP_0005") = 
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_25", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
-// Finance Cost
-DATA([d/Measures] = "GC_CR", [d/GL] = "FINEXP_005", [d/PPP_EntryNr] = "UP_0005") = 
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_30", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
+// Apportioned Corporate Overhead - posted by PPP_Upstream_CostAlloc on UP_0010
+//DATA([d/Measures] = "GC_CR", [d/GL] = "5080044", [d/PPP_EntryNr] = "UP_0005") = 
+//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_25", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
+// Finance Cost - posted by PPP_Upstream_CostAlloc on UP_0010
+//DATA([d/Measures] = "GC_CR", [d/GL] = "FINEXP_005", [d/PPP_EntryNr] = "UP_0005") = 
+//	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST15_30", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
 // Apportioned Taxes
@@ -74,6 +78,7 @@ DATA([d/Measures] = "GC_CR", [d/WPLn] = "#", [d/GL] = "4500006", [d/PPP_EntryNr]
 	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_15", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_20", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_25", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")	
+	(	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_10", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
+		RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_15", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
+		RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_20", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
+		RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_25", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")) *
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_90", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") / 100
 //	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "CST10_15", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
@@ -81,18 +86,23 @@ DATA([d/Measures] = "GC_CR", [d/WPLn] = "#", [d/GL] = "4500006", [d/PPP_EntryNr]
 
-// Development levy
+// Development levy - Oil & Gas, NNPC equity share
 DATA([d/Measures] = "GC_CR", [d/GL] = "5110007", [d/PPP_EntryNr] = "UP_0005") = 
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX010_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
+	(RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX005_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX010_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")) *
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_90", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") / 100
 
-// HCDT - Oil (Account not correct)
+// HCDT - Oil (Account not correct), NNPC equity share
 DATA([d/Measures] = "GC_CR", [d/GL] = "4109025" , [d/PPP_EntryNr] = "UP_0005") = 
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX015_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX015_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") *
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_90", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") / 100
 
-// HCDT - Gas (Account not correct)
+// HCDT - Gas (Account not correct), NNPC equity share
 DATA([d/Measures] = "GC_CR", [d/GL] = "4104007", [d/PPP_EntryNr] = "UP_0005") = 
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX015_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX020_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") *
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_90", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") / 100
 
-// NDDC - Oil & Gas
+// NDDC - Oil & Gas, NNPC equity share
 DATA([d/Measures] = "GC_CR", [d/GL] = "4111006" , [d/PPP_EntryNr] = "UP_0005") = 
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX025_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
-	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX030_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")
+	(RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX025_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") +
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX030_05", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")) *
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_90", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") / 100
 
```
