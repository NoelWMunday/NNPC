# Script diff

Left = live in SAC (`sac-export/` on `main`), right = proposed.

| Data action | Step | Lines |
|---|---|---|
| PPP_Upstream_Tax | 1. Initialise | +3 / -1 |
| PPP_Upstream_Tax | 5. Tax - HCDT Fund Payable (Oil) | +2 / -1 |
| PPP_Upstream_Tax | 6. Tax - HCDT Fund Payable (Gas) | +2 / -1 |
| PPP_Upstream_Tax | 13. Tax - CA Limit Rolling Balance (Oil) | +25 / -17 |
| PPP_Upstream_Tax | 14. Tax - CA Limit Rolling Balance (Gas) | +25 / -17 |
| PPP_Upstream_Tax | 16. Tax - Hydrocarbon Tax (CPR Limit & HT Payable) | +18 / -10 |
| PPP_Upstream_Royalties | 14. Costs - CAPEX Oil | +3 / -2 |
| PPP_Upstream_Royalties | 15. Costs - CAPEX Gas | +3 / -2 |
| PPP_Upstream_Royalties | 16. Costs - OPEX Oil | +3 / -2 |
| PPP_Upstream_Royalties | 17. Costs - OPEX Gas | +3 / -2 |

## PPP_Upstream_Tax — step 1. Initialise

```diff
@@ -7,5 +7,6 @@ MEMBERSET [d/PCycle] = %PCycle%
 MEMBERSET [d/Measures]="Value_WPLn"
 MEMBERSET [d/WPLn] = ("REV_32","REV_26","REV_40",
-					  BASEMEMBER([d/WPLn] ,"REV3_05"))
+					  BASEMEMBER([d/WPLn] ,"REV3_05"),
+					  BASEMEMBER([d/WPLn] ,"TAX"))
 MEMBERSET [d/GL] = "#"
 MEMBERSET [d/Ln] = "#"
@@ -16,3 +17,4 @@ MEMBERSET [d/WorkProgram] = "#"
 MEMBERSET [d/Lock] = "#"
 
+// TAX* are cleared so the rolling balances (steps 13, 14, 16) restart from this run
 DELETE()
```

## PPP_Upstream_Tax — step 5. Tax - HCDT Fund Payable (Oil)

```diff
@@ -17,5 +17,6 @@ MEMBERSET [d/PPP_EntryNr] = "#"
 MEMBERSET [d/PPP_Currency] = "#"
 
-DATA([d/WPLn]="TAX015_15") = RESULTLOOKUP([d/WPLn]="CST05_05")
+// HCDT basis = prior year operating expenditure (PIA s.240); CST05 holds the full year on December (Royalties LAST() rollup)
+DATA([d/WPLn]="TAX015_15") = RESULTLOOKUP([d/WPLn]="CST05_05",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))
 
 DATA([d/WPLn]="TAX015_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
```

## PPP_Upstream_Tax — step 6. Tax - HCDT Fund Payable (Gas)

```diff
@@ -17,5 +17,6 @@ MEMBERSET [d/PPP_EntryNr] = "#"
 MEMBERSET [d/PPP_Currency] = "#"
 
-DATA([d/WPLn]="TAX020_15") = RESULTLOOKUP([d/WPLn]="CST05_10")
+// HCDT basis = prior year operating expenditure (PIA s.240); CST05 holds the full year on December (Royalties LAST() rollup)
+DATA([d/WPLn]="TAX020_15") = RESULTLOOKUP([d/WPLn]="CST05_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))
 
 DATA([d/WPLn]="TAX020_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
```

## PPP_Upstream_Tax — step 13. Tax - CA Limit Rolling Balance (Oil)

```diff
@@ -47,25 +47,33 @@ DATA([d/WPLn]=#TAX050_20) =
 	RESULTLOOKUP([d/WPLn]="TAX050_20_35")
 
-IF RESULTLOOKUP([d/WPLn]=#TAX050_20) < 0 THEN
-	DATA([d/WPLn]="TAX055_20") = 0
-ELSE
-	DATA([d/WPLn]=#PARAM1) = RESULTLOOKUP([d/WPLn]="TAX055_10") + RESULTLOOKUP([d/WPLn]="TAX055_15")
-	DATA([d/WPLn]=#PARAM2) = ROUND (RESULTLOOKUP([d/WPLn]="TAX055_05") * RESULTLOOKUP([d/WPLn]= #TAX050_20) / 100, 0)
-	
-	IF RESULTLOOKUP([d/WPLn] = #PARAM1) < RESULTLOOKUP([d/WPLn] = #PARAM2) THEN
-		DATA([d/WPLn]="TAX055_20") = RESULTLOOKUP([d/WPLn] = #PARAM1)
+// Rolling balance: years are processed in date order, so each opening is the prior year's closing from
+// this run (Initialise clears TAX* first). Re-running gives the same result.
+FOREACH [d/Date]
+
+	DATA([d/WPLn]="TAX055_10") = RESULTLOOKUP([d/WPLn] = "TAX055_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))
+
+	IF RESULTLOOKUP([d/WPLn]=#TAX050_20) < 0 THEN
+		DATA([d/WPLn]="TAX055_20") = 0
 	ELSE
-		DATA([d/WPLn]="TAX055_20") = RESULTLOOKUP([d/WPLn] = #PARAM2)
+		DATA([d/WPLn]=#PARAM1) = RESULTLOOKUP([d/WPLn]="TAX055_10") + RESULTLOOKUP([d/WPLn]="TAX055_15")
+		DATA([d/WPLn]=#PARAM2) = ROUND (RESULTLOOKUP([d/WPLn]="TAX055_05") * RESULTLOOKUP([d/WPLn]= #TAX050_20) / 100, 0)
+	
+		IF RESULTLOOKUP([d/WPLn] = #PARAM1) < RESULTLOOKUP([d/WPLn] = #PARAM2) THEN
+			DATA([d/WPLn]="TAX055_20") = RESULTLOOKUP([d/WPLn] = #PARAM1)
+		ELSE
+			DATA([d/WPLn]="TAX055_20") = RESULTLOOKUP([d/WPLn] = #PARAM2)
+		ENDIF
 	ENDIF
-ENDIF
 
-DATA([d/WPLn]="TAX055_25") = 
-	RESULTLOOKUP([d/WPLn] = "TAX055_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) +
-	RESULTLOOKUP([d/WPLn] = "TAX055_15") -
-	RESULTLOOKUP([d/WPLn] = "TAX055_20")
+	DATA([d/WPLn]="TAX055_25") = 
+		RESULTLOOKUP([d/WPLn] = "TAX055_10") +
+		RESULTLOOKUP([d/WPLn] = "TAX055_15") -
+		RESULTLOOKUP([d/WPLn] = "TAX055_20")
+
+	DATA([d/WPLn]="TAX055_30") = 
+		RESULTLOOKUP([d/WPLn] = "TAX055_20") -
+		RESULTLOOKUP([d/WPLn] = "TAX055_35")
 
-DATA([d/WPLn]="TAX055_30") = 
-	RESULTLOOKUP([d/WPLn] = "TAX055_20") -
-	RESULTLOOKUP([d/WPLn] = "TAX055_35")
+ENDFOR
 
 	
```

## PPP_Upstream_Tax — step 14. Tax - CA Limit Rolling Balance (Gas)

```diff
@@ -44,25 +44,33 @@ DATA([d/WPLn]=#TAX010_15) =
 
 
-IF RESULTLOOKUP([d/WPLn]=#TAX010_15) < 0 THEN
-	DATA([d/WPLn]="TAX060_15") = 0
-ELSE
-	DATA([d/WPLn]=#PARAM1) = RESULTLOOKUP([d/WPLn]="TAX060_05") + RESULTLOOKUP([d/WPLn]="TAX060_10")
-	DATA([d/WPLn]=#PARAM2) = ROUND (RESULTLOOKUP([d/WPLn]="TAX055_05") * RESULTLOOKUP([d/WPLn]= #TAX010_15) / 100, 0)
-	
-	IF RESULTLOOKUP([d/WPLn] = #PARAM1) < RESULTLOOKUP([d/WPLn] = #PARAM2) THEN
-		DATA([d/WPLn]="TAX060_15") = RESULTLOOKUP([d/WPLn] = #PARAM1)
+// Rolling balance: years are processed in date order, so each opening is the prior year's closing from
+// this run (Initialise clears TAX* first). Re-running gives the same result.
+FOREACH [d/Date]
+
+	DATA([d/WPLn]="TAX060_05") = RESULTLOOKUP([d/WPLn] = "TAX060_20",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))
+
+	IF RESULTLOOKUP([d/WPLn]=#TAX010_15) < 0 THEN
+		DATA([d/WPLn]="TAX060_15") = 0
 	ELSE
-		DATA([d/WPLn]="TAX060_15") = RESULTLOOKUP([d/WPLn] = #PARAM2)
+		DATA([d/WPLn]=#PARAM1) = RESULTLOOKUP([d/WPLn]="TAX060_05") + RESULTLOOKUP([d/WPLn]="TAX060_10")
+		DATA([d/WPLn]=#PARAM2) = ROUND (RESULTLOOKUP([d/WPLn]="TAX055_05") * RESULTLOOKUP([d/WPLn]= #TAX010_15) / 100, 0)
+	
+		IF RESULTLOOKUP([d/WPLn] = #PARAM1) < RESULTLOOKUP([d/WPLn] = #PARAM2) THEN
+			DATA([d/WPLn]="TAX060_15") = RESULTLOOKUP([d/WPLn] = #PARAM1)
+		ELSE
+			DATA([d/WPLn]="TAX060_15") = RESULTLOOKUP([d/WPLn] = #PARAM2)
+		ENDIF
 	ENDIF
-ENDIF
 
-DATA([d/WPLn]="TAX060_20") = 
-	RESULTLOOKUP([d/WPLn] = "TAX060_20",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) +
-	RESULTLOOKUP([d/WPLn] = "TAX060_10") -
-	RESULTLOOKUP([d/WPLn] = "TAX060_15")
+	DATA([d/WPLn]="TAX060_20") = 
+		RESULTLOOKUP([d/WPLn] = "TAX060_05") +
+		RESULTLOOKUP([d/WPLn] = "TAX060_10") -
+		RESULTLOOKUP([d/WPLn] = "TAX060_15")
+
+	DATA([d/WPLn]="TAX060_25") = 
+		RESULTLOOKUP([d/WPLn] = "TAX060_15") -
+		RESULTLOOKUP([d/WPLn] = "TAX060_30")
 
-DATA([d/WPLn]="TAX060_25") = 
-	RESULTLOOKUP([d/WPLn] = "TAX060_15") -
-	RESULTLOOKUP([d/WPLn] = "TAX060_30")
+ENDFOR
 
 	
```

## PPP_Upstream_Tax — step 16. Tax - Hydrocarbon Tax (CPR Limit & HT Payable)

```diff
@@ -36,16 +36,24 @@ DATA([d/WPLn] = "TAX070_35") = RESULTLOOKUP([d/WPLn]="TAX070_30") + RESULTLOOKUP
 DATA([d/WPLn] = "TAX070_15") = RESULTLOOKUP([d/WPLn]="TAX070_35")
 
-DATA([d/WPLn] = #PARAM1) = RESULTLOOKUP([d/WPLn]="TAX070_05") * RESULTLOOKUP([d/WPLn]="REV_10") / 100
-DATA([d/WPLn] = #PARAM2) = RESULTLOOKUP([d/WPLn]="TAX070_35") + RESULTLOOKUP([d/WPLn]="TAX070_10")
+// Rolling balance: years are processed in date order, so each opening is the prior year's closing from
+// this run (Initialise clears TAX* first). Re-running gives the same result.
+FOREACH [d/Date]
 
-IF RESULTLOOKUP([d/WPLn]=#PARAM1) < RESULTLOOKUP([d/WPLn]=#PARAM2) THEN
-	DATA([d/WPLn] = "TAX070_20") = RESULTLOOKUP([d/WPLn]=#PARAM1)
-ELSE
-	DATA([d/WPLn] = "TAX070_20") = RESULTLOOKUP([d/WPLn]=#PARAM2)
-ENDIF
+	DATA([d/WPLn] = "TAX070_10") = RESULTLOOKUP([d/WPLn]="TAX070_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))
+
+	DATA([d/WPLn] = #PARAM1) = RESULTLOOKUP([d/WPLn]="TAX070_05") * RESULTLOOKUP([d/WPLn]="REV_10") / 100
+	DATA([d/WPLn] = #PARAM2) = RESULTLOOKUP([d/WPLn]="TAX070_35") + RESULTLOOKUP([d/WPLn]="TAX070_10")
+
+	IF RESULTLOOKUP([d/WPLn]=#PARAM1) < RESULTLOOKUP([d/WPLn]=#PARAM2) THEN
+		DATA([d/WPLn] = "TAX070_20") = RESULTLOOKUP([d/WPLn]=#PARAM1)
+	ELSE
+		DATA([d/WPLn] = "TAX070_20") = RESULTLOOKUP([d/WPLn]=#PARAM2)
+	ENDIF
+
+	DATA([d/WPLn] = "TAX070_25") = RESULTLOOKUP([d/WPLn]="TAX070_10") +
+		RESULTLOOKUP([d/WPLn]="TAX070_15") -
+		RESULTLOOKUP([d/WPLn]="TAX070_20")
 
-DATA([d/WPLn] = "TAX070_25") = RESULTLOOKUP([d/WPLn]="TAX070_25",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) +
-	RESULTLOOKUP([d/WPLn]="TAX070_15") -
-	RESULTLOOKUP([d/WPLn]="TAX070_20")
+ENDFOR
 
 DATA([d/WPLn] = "TAX070_45") = RESULTLOOKUP([d/WPLn]="TAX070_20")
```

## PPP_Upstream_Royalties — step 14. Costs - CAPEX Oil

```diff
@@ -15,8 +15,9 @@ MEMBERSET [d/ProductServ] = "#"
 MEMBERSET [d/Strategy] = "#"
 MEMBERSET [d/WorkProgram] = "#"
-MEMBERSET [d/Lock] = "#"
+// Closed periods (Lock Hist_Open) are included so December holds the full year; results go to Lock "#"
+MEMBERSET [d/Lock] = ("#","Hist_Open")
 
 IF [d/PPP_EntryNr] != "#" AND [d/PPP_Currency] = "USD" THEN
-	DATA.APPEND([d/WPLn] = "CST05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Date] = LAST()) = 
+	DATA.APPEND([d/WPLn] = "CST05_15", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = 
 		RESULTLOOKUP([d/WPLn] = "AMT_200")
 ENDIF
```

## PPP_Upstream_Royalties — step 15. Costs - CAPEX Gas

```diff
@@ -15,8 +15,9 @@ MEMBERSET [d/ProductServ] = "#"
 MEMBERSET [d/Strategy] = "#"
 MEMBERSET [d/WorkProgram] = "#"
-MEMBERSET [d/Lock] = "#"
+// Closed periods (Lock Hist_Open) are included so December holds the full year; results go to Lock "#"
+MEMBERSET [d/Lock] = ("#","Hist_Open")
 
 IF [d/PPP_EntryNr] != "#" AND [d/PPP_Currency] = "USD" THEN
-	DATA.APPEND([d/WPLn] = "CST05_20", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Date] = LAST()) = 
+	DATA.APPEND([d/WPLn] = "CST05_20", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = 
 		RESULTLOOKUP([d/WPLn] = "AMT_210")
 ENDIF
```

## PPP_Upstream_Royalties — step 16. Costs - OPEX Oil

```diff
@@ -17,8 +17,9 @@ MEMBERSET [d/ProductServ] = "#"
 MEMBERSET [d/Strategy] = "#"
 MEMBERSET [d/WorkProgram] = "#"
-MEMBERSET [d/Lock] = "#"
+// Closed periods (Lock Hist_Open) are included so December holds the full year; results go to Lock "#"
+MEMBERSET [d/Lock] = ("#","Hist_Open")
 
 IF [d/PPP_EntryNr] != "#" AND [d/PPP_Currency] = "USD" THEN
-	DATA.APPEND([d/WPLn] = "CST05_05", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Date] = LAST()) = 
+	DATA.APPEND([d/WPLn] = "CST05_05", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = 
 		RESULTLOOKUP([d/WPLn] = "AMT_220")
 ENDIF
```

## PPP_Upstream_Royalties — step 17. Costs - OPEX Gas

```diff
@@ -17,8 +17,9 @@ MEMBERSET [d/ProductServ] = "#"
 MEMBERSET [d/Strategy] = "#"
 MEMBERSET [d/WorkProgram] = "#"
-MEMBERSET [d/Lock] = "#"
+// Closed periods (Lock Hist_Open) are included so December holds the full year; results go to Lock "#"
+MEMBERSET [d/Lock] = ("#","Hist_Open")
 
 IF [d/PPP_EntryNr] != "#" AND [d/PPP_Currency] = "USD" THEN
-	DATA.APPEND([d/WPLn] = "CST05_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Date] = LAST()) = 
+	DATA.APPEND([d/WPLn] = "CST05_10", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#", [d/Lock] = "#", [d/Date] = LAST()) = 
 		RESULTLOOKUP([d/WPLn] = "AMT_230")
 ENDIF
```
