# Script diff

Left = live (Tax v15), right = proposed.

## PPP_Upstream_Tax — step 18. Tax - Allowable Costs & Chargeable Profit CITA (Gas)

```diff
@@ -20,7 +20,5 @@ VARIABLEMEMBER #PARAM1 OF [d/WPLn]
 
-IF RESULTLOOKUP([d/WPLn]="TAX070_60") = 0 THEN
-	DATA([d/WPLn] = #PARAM1) = RESULTLOOKUP([d/WPLn]="TAX060_25")
-ELSE
-	DATA([d/WPLn] = #PARAM1) = 0
-ENDIF
+// Gas capital allowance is a CITA deduction under both regimes (PPT covers oil only).
+// Was gated on TAX070_60 = 0, which fails when SET10_10 has no value (null) - e.g. RENAISSANCE.
+DATA([d/WPLn] = #PARAM1) = RESULTLOOKUP([d/WPLn]="TAX060_25")
 
```
