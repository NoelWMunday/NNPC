# Script diff

Left = live (Tax v18), right = proposed.

## PPP_Upstream_Tax — step 11. Tax - CAPEX Amortisation

```diff
@@ -20 +20 @@ MEMBERSET [d/PPP_Currency] = "#"
-// TAX045_05_10	Amortised Oil Capex (Facilities+Drilling)
+// TAX045_05_10	Amortised Oil Capex (Exploration+Drilling+Facilities)
@@ -22 +22 @@ MEMBERSET [d/PPP_Currency] = "#"
-// TAX045_05_20	Amortised Gas Capex (Facilities+Drilling)
+// TAX045_05_20	Amortised Gas Capex (Exploration+Drilling+Facilities)
@@ -25 +25 @@ MEMBERSET [d/PPP_Currency] = "#"
-// Oil - facilities & drilling
+// Oil - exploration, drilling & facilities (NUIMS row 2338 = rows 2279-2287, same 5-year rates)
@@ -28 +28 @@ DATA([d/WPLn]="TAX045_05_10") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_05_10") + RESULTLOOKUP([d/WPLn]="TAX040_05_15")) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_05_05_05") + RESULTLOOKUP([d/WPLn]="TAX040_05_05_10") + RESULTLOOKUP([d/WPLn]="TAX040_05_05_15") + RESULTLOOKUP([d/WPLn]="TAX040_05_10") + RESULTLOOKUP([d/WPLn]="TAX040_05_15")) * 
@@ -31 +31 @@ DATA([d/WPLn]="TAX045_05_10") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_05_05_05",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_05_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_05_15",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))) * 
@@ -34 +34 @@ DATA([d/WPLn]="TAX045_05_10") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(2,"YEAR",[d/Date]))) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_05_05_05",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_05_10",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_05_15",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(2,"YEAR",[d/Date]))) * 
@@ -37 +37 @@ DATA([d/WPLn]="TAX045_05_10") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(3,"YEAR",[d/Date]))) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_05_05_05",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_05_10",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_05_15",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(3,"YEAR",[d/Date]))) * 
@@ -40 +40 @@ DATA([d/WPLn]="TAX045_05_10") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(4,"YEAR",[d/Date]))) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_05_05_05",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_05_10",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_05_15",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_10",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_05_15",[d/Date]=PREVIOUS(4,"YEAR",[d/Date]))) * 
@@ -61 +61 @@ DATA([d/WPLn]="TAX045_05_15") =
-// Gas - facilities & drilling
+// Gas - exploration, drilling & facilities
@@ -64 +64 @@ DATA([d/WPLn]="TAX045_05_20") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_10_10") + RESULTLOOKUP([d/WPLn]="TAX040_10_15")) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_10_05_05") + RESULTLOOKUP([d/WPLn]="TAX040_10_05_10") + RESULTLOOKUP([d/WPLn]="TAX040_10_05_15") + RESULTLOOKUP([d/WPLn]="TAX040_10_10") + RESULTLOOKUP([d/WPLn]="TAX040_10_15")) * 
@@ -67 +67 @@ DATA([d/WPLn]="TAX045_05_20") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_10_05_05",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_05_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_05_15",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(1,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(1,"YEAR",[d/Date]))) * 
@@ -70 +70 @@ DATA([d/WPLn]="TAX045_05_20") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(2,"YEAR",[d/Date]))) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_10_05_05",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_05_10",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_05_15",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(2,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(2,"YEAR",[d/Date]))) * 
@@ -73 +73 @@ DATA([d/WPLn]="TAX045_05_20") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(3,"YEAR",[d/Date]))) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_10_05_05",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_05_10",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_05_15",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(3,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(3,"YEAR",[d/Date]))) * 
@@ -76 +76 @@ DATA([d/WPLn]="TAX045_05_20") =
-	((RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(4,"YEAR",[d/Date]))) * 
+	((RESULTLOOKUP([d/WPLn]="TAX040_10_05_05",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_05_10",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_05_15",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_10",[d/Date]=PREVIOUS(4,"YEAR",[d/Date])) + RESULTLOOKUP([d/WPLn]="TAX040_10_15",[d/Date]=PREVIOUS(4,"YEAR",[d/Date]))) * 
```

## PPP_Upstream_Tax — step 16. Tax - Hydrocarbon Tax (CPR Limit & HT Payable)

```diff
@@ -30 +29,0 @@ DATA([d/WPLn] = "TAX070_40") =
-	RESULTLOOKUP([d/WPLn]="TAX040_05_05") +
```

## PPP_Upstream_Tax — step 17. Tax - Allowable Costs & Chargeable Profit CITA (Oil)

```diff
@@ -26 +25,0 @@ DATA([d/WPLn] = "TAX075_05") =
-	RESULTLOOKUP([d/WPLn]="TAX040_05_05") + 
```
