# Script diff

Left = live in SAC (Tax v15), right = proposed.

## PPP_Upstream_Tax — step 12. Tax - Capital allowance for PPT

```diff
@@ -38,2 +38,4 @@ VARIABLEMEMBER #AMORT_CAPEX OF [d/WPLn]
 // TAX050_20_35	Less: Development Levy – Oil
+// TAX050_20_40	Less: NDDC Levy Payable (Oil)
+// TAX050_20_45	Less: HCDT Fund Payable - Oil
 
@@ -57,2 +59,4 @@ DATA([d/WPLn]="TAX050_20_30") = 0-RESULTLOOKUP([d/WPLn]="CST05_05")
 DATA([d/WPLn]="TAX050_20_35") = 0-RESULTLOOKUP([d/WPLn]="TAX005_05")
+DATA([d/WPLn]="TAX050_20_40") = 0-RESULTLOOKUP([d/WPLn]="TAX025_05")
+DATA([d/WPLn]="TAX050_20_45") = 0-RESULTLOOKUP([d/WPLn]="TAX015_05")
 
@@ -65,3 +69,5 @@ DATA([d/WPLn]=#ASSESSABLE) =
 	RESULTLOOKUP([d/WPLn]="TAX050_20_30") +
-	RESULTLOOKUP([d/WPLn]="TAX050_20_35")
+	RESULTLOOKUP([d/WPLn]="TAX050_20_35") +
+	RESULTLOOKUP([d/WPLn]="TAX050_20_40") +
+	RESULTLOOKUP([d/WPLn]="TAX050_20_45")
 
```

## PPP_Upstream_Tax — step 13. Tax - CA Limit Rolling Balance (Oil)

```diff
@@ -46,3 +46,5 @@ DATA([d/WPLn]=#TAX050_20) =
 	RESULTLOOKUP([d/WPLn]="TAX050_20_30") +
-	RESULTLOOKUP([d/WPLn]="TAX050_20_35")
+	RESULTLOOKUP([d/WPLn]="TAX050_20_35") +
+	RESULTLOOKUP([d/WPLn]="TAX050_20_40") +
+	RESULTLOOKUP([d/WPLn]="TAX050_20_45")
 
```

## PPP_Upstream_Tax — step 15. Tax - Chargeable Profit for PPT

```diff
@@ -27,3 +27,5 @@ DATA([d/WPLn] = #TAX050_20) =
 	RESULTLOOKUP([d/WPLn]="TAX050_20_30") +
-	RESULTLOOKUP([d/WPLn]="TAX050_20_35")
+	RESULTLOOKUP([d/WPLn]="TAX050_20_35") +
+	RESULTLOOKUP([d/WPLn]="TAX050_20_40") +
+	RESULTLOOKUP([d/WPLn]="TAX050_20_45")
 	
```
