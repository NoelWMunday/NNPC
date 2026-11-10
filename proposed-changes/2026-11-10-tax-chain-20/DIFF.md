# Script diff — #20

Left = live in SAC (`sac-export/` on `main`), right = proposed. Line counts unchanged in every step.

| Data action | Step | Lines changed |
|---|---|---|
| PPP_Upstream_Tax | 3. Tax - NDDC Levy Payable (Oil) | 2 |
| PPP_Upstream_Tax | 4. Tax - NDDC Levy Payable (Gas) | 3 |
| PPP_Upstream_Tax | 5. Tax - HCDT Fund Payable (Oil) | 1 |
| PPP_Upstream_Tax | 6. Tax - HCDT Fund Payable (Gas) | 1 |
| PPP_Upstream_Tax | 7. Tax - Development Levy (Oil) | 1 |
| PPP_Upstream_Tax | 8. Tax - Development levy (Gas) | 1 |
| PPP_Upstream_Tax | 12. Tax - Capital allowance for PPT | 2 |
| PPP_Upstream_Tax | 16. Tax - Hydrocarbon Tax (CPR Limit & HT Payable) | 1 |
| PPP_Upstream_Tax | 19. Tax - PPT Tax (Oil) | 1 |
| PPP_Upstream_Tax | 20. Tax - CITA (Oil & Gas) | 3 |

## PPP_Upstream_Tax — step 3. Tax - NDDC Levy Payable (Oil)

```diff
@@ -18,4 +18,4 @@ MEMBERSET [d/PPP_Currency] = "#"
 
-DATA([d/WPLn]="TAX025_15_05") = RESULTLOOKUP([d/WPLn]="AMT_220", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX025_15_10") = RESULTLOOKUP([d/WPLn]="AMT_200", [d/PPP_Currency]="USD")
+DATA([d/WPLn]="TAX025_15_05") = RESULTLOOKUP([d/WPLn]="CST05_05")
+DATA([d/WPLn]="TAX025_15_10") = RESULTLOOKUP([d/WPLn]="CST05_15")
 
```

## PPP_Upstream_Tax — step 4. Tax - NDDC Levy Payable (Gas)

```diff
@@ -18,4 +18,4 @@ MEMBERSET [d/PPP_Currency] = "#"
 
-DATA([d/WPLn]="TAX030_15_05") = RESULTLOOKUP([d/WPLn]="AMT_230", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX030_15_10") = RESULTLOOKUP([d/WPLn]="AMT_210", [d/PPP_Currency]="USD")
+DATA([d/WPLn]="TAX030_15_05") = RESULTLOOKUP([d/WPLn]="CST05_10")
+DATA([d/WPLn]="TAX030_15_10") = RESULTLOOKUP([d/WPLn]="CST05_20")
 
@@ -23,3 +23,3 @@ DATA([d/WPLn]="TAX030_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",
 
-DATA([d/WPLn]="TAX030_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX025_10") * (
+DATA([d/WPLn]="TAX030_05") = ROUND( RESULTLOOKUP([d/WPLn]="TAX030_10") * (
 	RESULTLOOKUP([d/WPLn]="TAX030_15_05") +														   
```

## PPP_Upstream_Tax — step 5. Tax - HCDT Fund Payable (Oil)

```diff
@@ -18,3 +18,3 @@ MEMBERSET [d/PPP_Currency] = "#"
 
-DATA([d/WPLn]="TAX015_15") = RESULTLOOKUP([d/WPLn]="AMT_220", [d/PPP_Currency]="USD")
+DATA([d/WPLn]="TAX015_15") = RESULTLOOKUP([d/WPLn]="CST05_05")
 
```

## PPP_Upstream_Tax — step 6. Tax - HCDT Fund Payable (Gas)

```diff
@@ -18,3 +18,3 @@ MEMBERSET [d/PPP_Currency] = "#"
 
-DATA([d/WPLn]="TAX020_15") = RESULTLOOKUP([d/WPLn]="AMT_230", [d/PPP_Currency]="USD")
+DATA([d/WPLn]="TAX020_15") = RESULTLOOKUP([d/WPLn]="CST05_10")
 
```

## PPP_Upstream_Tax — step 7. Tax - Development Levy (Oil)

```diff
@@ -22,3 +22,3 @@ DATA([d/WPLn]="TAX005_15_10") = 0-RESULTLOOKUP([d/WPLn]="RC15_05")
 DATA([d/WPLn]="TAX005_15_15") = 0-RESULTLOOKUP([d/WPLn]="RC20_10") 
-DATA([d/WPLn]="TAX005_15_20") = 0-RESULTLOOKUP([d/WPLn]="RC30_10") 
+DATA([d/WPLn]="TAX005_15_20") = 0-RESULTLOOKUP([d/WPLn]="RC30_05") 
 DATA([d/WPLn]="TAX005_15_25") = 0-RESULTLOOKUP([d/WPLn]="RC35_10") 
```

## PPP_Upstream_Tax — step 8. Tax - Development levy (Gas)

```diff
@@ -20,3 +20,3 @@ DATA([d/WPLn]="TAX010_15_05") = RESULTLOOKUP([d/WPLn]="REV_20")
 DATA([d/WPLn]="TAX010_15_10") = 0-RESULTLOOKUP([d/WPLn]="RC25_20")
-DATA([d/WPLn]="TAX010_15_15") = 0-RESULTLOOKUP([d/WPLn]="AMT_230", [d/PPP_Currency]="USD") 
+DATA([d/WPLn]="TAX010_15_15") = 0-RESULTLOOKUP([d/WPLn]="CST05_10") 
 DATA([d/WPLn]="TAX010_15_20") = 0-RESULTLOOKUP([d/WPLn]="RC40_20") 
```

## PPP_Upstream_Tax — step 12. Tax - Capital allowance for PPT

```diff
@@ -67,4 +67,4 @@ DATA([d/WPLn]=#ASSESSABLE) =
 
-DATA([d/WPLn]="TAX050_15_05") = RESULTLOOKUP([d/WPLn]="TA30_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="202612")
-DATA([d/WPLn]="TAX050_15_10") = RESULTLOOKUP([d/WPLn]="TA30_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="202612")
+DATA([d/WPLn]="TAX050_15_05") = RESULTLOOKUP([d/WPLn]="TA30_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+DATA([d/WPLn]="TAX050_15_10") = RESULTLOOKUP([d/WPLn]="TA30_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
 
```

## PPP_Upstream_Tax — step 16. Tax - Hydrocarbon Tax (CPR Limit & HT Payable)

```diff
@@ -23,3 +23,3 @@ DATA([d/WPLn] = "TAX070_05") = RESULTLOOKUP([d/WPLn]="TA15_05",[d/PPP_Entity]="#
 DATA([d/WPLn] = "TAX070_55") = RESULTLOOKUP([d/WPLn]="TL15_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
-DATA([d/WPLn] = "TAX070_60") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+DATA([d/WPLn] = "TAX070_60") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")
 DATA([d/WPLn] = "TAX070_30") = RESULTLOOKUP([d/WPLn]="CST05_05")
```

## PPP_Upstream_Tax — step 19. Tax - PPT Tax (Oil)

```diff
@@ -20,3 +20,3 @@ DATA([d/WPLn] = "TAX085_10") = RESULTLOOKUP([d/WPLn]="TL05_05",[d/PPP_Entity]="#
 
-DATA([d/WPLn] = "TAX085_20") = RESULTLOOKUP([d/WPLn]="TAX065_05") * RESULTLOOKUP([d/WPLn]="TAX085_10") * RESULTLOOKUP([d/WPLn]="SET10_05") / 100
+DATA([d/WPLn] = "TAX085_20") = RESULTLOOKUP([d/WPLn]="TAX065_05") * RESULTLOOKUP([d/WPLn]="TAX085_10") * RESULTLOOKUP([d/WPLn]="SET10_05",[d/Date]="000000") / 100
 
```

## PPP_Upstream_Tax — step 20. Tax - CITA (Oil & Gas)

```diff
@@ -19,8 +19,8 @@ MEMBERSET [d/PPP_Currency] = "#"
 DATA([d/WPLn] = "TAX090_05") = RESULTLOOKUP([d/WPLn]="TL05_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
-DATA([d/WPLn] = "TAX090_10") = RESULTLOOKUP([d/WPLn]="SET10_10")
+DATA([d/WPLn] = "TAX090_10") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")
 
-DATA([d/WPLn] = "TAX090_15") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX075_10") * RESULTLOOKUP([d/WPLn]="SET10_10") / 100
+DATA([d/WPLn] = "TAX090_15") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX075_10") * RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000") / 100
 IF RESULTLOOKUP([d/WPLn]="TAX090_15") < 0 THEN DATA([d/WPLn] = "TAX090_15") = 0 ENDIF
 
-DATA([d/WPLn] = "TAX090_20") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX080_10") * RESULTLOOKUP([d/WPLn]="SET10_10") / 100
+DATA([d/WPLn] = "TAX090_20") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX080_10") * RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000") / 100
 IF RESULTLOOKUP([d/WPLn]="TAX090_20") < 0 THEN DATA([d/WPLn] = "TAX090_20") = 0 ENDIF
```
