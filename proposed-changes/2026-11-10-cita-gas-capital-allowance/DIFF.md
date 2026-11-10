# Script diff

Left = live (Tax v16), right = proposed.

## PPP_Upstream_Tax — step 18. Tax - Allowable Costs & Chargeable Profit CITA (Gas)

```diff
@@ -20,3 +20,4 @@ VARIABLEMEMBER #PARAM1 OF [d/WPLn]
 
-IF RESULTLOOKUP([d/WPLn]="TAX070_60") = 0 THEN
+// TAX070_60 (SET10_10) is null when the JV has no PIA flag - treat null as 0
+IF RESULTLOOKUP([d/WPLn]="TAX070_60") = 0 OR RESULTLOOKUP([d/WPLn]="TAX070_60") = NULL THEN
 	DATA([d/WPLn] = #PARAM1) = RESULTLOOKUP([d/WPLn]="TAX060_25")
```
