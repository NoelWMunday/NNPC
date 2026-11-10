# Script diff

Left = live (`sac-export/` on `main`), right = proposed.

## PPP_Upstream_Tax — step 20. Tax - CITA (Oil & Gas)

```diff
@@ -23,5 +23,6 @@ DATA([d/WPLn] = "TAX090_15") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP
 IF RESULTLOOKUP([d/WPLn]="TAX090_15") < 0 THEN DATA([d/WPLn] = "TAX090_15") = 0 ENDIF
 
-DATA([d/WPLn] = "TAX090_20") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX080_10") * RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000") / 100
+// Gas CITA applies under both regimes (PPT covers oil only) - no PIA flag, as NUIMS row 2426
+DATA([d/WPLn] = "TAX090_20") = RESULTLOOKUP([d/WPLn]="TAX090_05") * RESULTLOOKUP([d/WPLn]="TAX080_10") / 100
 IF RESULTLOOKUP([d/WPLn]="TAX090_20") < 0 THEN DATA([d/WPLn] = "TAX090_20") = 0 ENDIF
 
```
