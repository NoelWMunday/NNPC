# Script diff

Left = live (Tax v17), right = proposed.

## PPP_Upstream_Tax — step 10. Tax - CAPEX Components

```diff
@@ -6,5 +6,4 @@ MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
 MEMBERSET [d/PCycle] = %PCycle%
 MEMBERSET [d/Measures]="Value_WPLn"
-// MEMBERSET [d/WPLn] = BASEMEMBER([d/WPLn] , "AMT_210")
 MEMBERSET [d/GL] = "#"
 MEMBERSET [d/Ln] = "#"
@@ -13,45 +12,57 @@ MEMBERSET [d/ProductServ] = "#"
 MEMBERSET [d/Strategy] = "#"
 MEMBERSET [d/WorkProgram] = "#"
-MEMBERSET [d/Lock] = "#"
-MEMBERSET [d/PPP_EntryNr] = "#"
-MEMBERSET [d/PPP_Currency] = "#"
+// Capex inputs (USD, by UAP entry) are rolled into December of each year on Lock "#", EntryNr "#", Currency "#".
+// Closed periods (Lock Hist_Open: prior years and CY YTD) are included, so amortisation (step 11) sees full years.
+// Initialise (step 1) clears TAX*, so DATA.APPEND rebuilds the totals on every run.
+MEMBERSET [d/Lock] = ("#","Hist_Open")
+MEMBERSET [d/PPP_Currency] = ("#","USD")
+MEMBERSET [d/PPP_EntryNr] = ("#","UAP_110","UAP_120","UAP_121","UAP_124","UAP_130","UAP_132","UAP_136","UAP_138","UAP_139","UAP_101","UAP_102","UAP_134","UAP_140","UAP_141")
+MEMBERSET [d/WPLn] = ("AMT_200","AMT_210",
+	"TAX040_05_05_05","TAX040_05_05_10","TAX040_05_05_15",
+	"TAX040_05_10","TAX040_05_15","TAX040_05_20",
+	"TAX040_10_05_05","TAX040_10_05_10","TAX040_10_05_15",
+	"TAX040_10_10","TAX040_10_15","TAX040_10_20")
 
 // Oil
-DATA([d/WPLn]="TAX040_05_05_05") = RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_110", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_05_05_10") = RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_120", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_05_05_15") = RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_121", [d/PPP_Currency]="USD") + RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_124", [d/PPP_Currency]="USD")
+IF [d/PPP_Currency] = "USD" AND [d/WPLn] = "AMT_200" THEN
+	IF [d/PPP_EntryNr] = "UAP_110" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_05_05_05", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_120" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_05_05_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_121" OR [d/PPP_EntryNr] = "UAP_124" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_05_05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_130" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_05_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_132" OR [d/PPP_EntryNr] = "UAP_136" OR [d/PPP_EntryNr] = "UAP_138" OR [d/PPP_EntryNr] = "UAP_139" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_101" OR [d/PPP_EntryNr] = "UAP_102" OR [d/PPP_EntryNr] = "UAP_134" OR [d/PPP_EntryNr] = "UAP_140" OR [d/PPP_EntryNr] = "UAP_141" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_05_20", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_200")
+	ENDIF
+ENDIF
 
-DATA([d/WPLn]="TAX040_05_10") = RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_130", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_05_15") = 
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_132", [d/PPP_Currency]="USD") + 
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_136", [d/PPP_Currency]="USD") +
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_138", [d/PPP_Currency]="USD") + 
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_139", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_05_20") = 
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_101", [d/PPP_Currency]="USD") + 
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_102", [d/PPP_Currency]="USD") +
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_134", [d/PPP_Currency]="USD") + 
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_140", [d/PPP_Currency]="USD") +
-		RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_141", [d/PPP_Currency]="USD")
-		
 // Gas
-DATA([d/WPLn]="TAX040_10_05_05") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_110", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_10_05_10") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_120", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_10_05_15") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_121", [d/PPP_Currency]="USD") + RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_124", [d/PPP_Currency]="USD")
-
-DATA([d/WPLn]="TAX040_10_10") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_130", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_10_15") = 
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_132", [d/PPP_Currency]="USD") + 
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_136", [d/PPP_Currency]="USD") +
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_138", [d/PPP_Currency]="USD") + 
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_139", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_10_20") = 
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_101", [d/PPP_Currency]="USD") + 
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_102", [d/PPP_Currency]="USD") +
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_134", [d/PPP_Currency]="USD") + 
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_140", [d/PPP_Currency]="USD") +
-		RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_141", [d/PPP_Currency]="USD")
-
-
-
-
+IF [d/PPP_Currency] = "USD" AND [d/WPLn] = "AMT_210" THEN
+	IF [d/PPP_EntryNr] = "UAP_110" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_10_05_05", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_120" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_10_05_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_121" OR [d/PPP_EntryNr] = "UAP_124" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_10_05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_130" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_10_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_132" OR [d/PPP_EntryNr] = "UAP_136" OR [d/PPP_EntryNr] = "UAP_138" OR [d/PPP_EntryNr] = "UAP_139" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_10_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
+	ENDIF
+	IF [d/PPP_EntryNr] = "UAP_101" OR [d/PPP_EntryNr] = "UAP_102" OR [d/PPP_EntryNr] = "UAP_134" OR [d/PPP_EntryNr] = "UAP_140" OR [d/PPP_EntryNr] = "UAP_141" THEN
+		DATA.APPEND([d/WPLn] = "TAX040_10_20", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = RESULTLOOKUP([d/WPLn] = "AMT_210")
+	ENDIF
+ENDIF
```
