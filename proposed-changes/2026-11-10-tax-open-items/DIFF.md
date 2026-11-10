# Script diff

Left = live in SAC (`sac-export/`, Tax v12), right = proposed.

## PPP_Upstream_Tax — step 9. Tax - Production Allowance

```diff
@@ -21,3 +21,4 @@ DATA([d/WPLn]="TAX035_10") = RESULTLOOKUP([d/WPLn]="TA20_05",[d/PPP_Entity]="#",
 DATA([d/WPLn]="TAX035_15") = RESULTLOOKUP([d/WPLn]="TA20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") 
-DATA([d/WPLn]="TAX035_12") = RESULTLOOKUP([d/WPLn]="GA_015",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+// Oil price is a per-year central assumption (as in Revenue step 2 and Royalties) - no Date 000000
+DATA([d/WPLn]="TAX035_12") = RESULTLOOKUP([d/WPLn]="GA_015",[d/PPP_Entity]="#",[d/Lock]="Central")
 DATA([d/WPLn]="TAX035_17") = RESULTLOOKUP([d/WPLn]="TAX035_12") * RESULTLOOKUP([d/WPLn]="TAX035_15") / 100
```

## PPP_Upstream_Tax — step 10. Tax - CAPEX Components

```diff
@@ -39,3 +39,3 @@ DATA([d/WPLn]="TAX040_10_05_05") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryN
 DATA([d/WPLn]="TAX040_10_05_10") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_120", [d/PPP_Currency]="USD")
-DATA([d/WPLn]="TAX040_10_05_15") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_121", [d/PPP_Currency]="USD") + RESULTLOOKUP([d/WPLn]="AMT_200",[d/PPP_EntryNr]="UAP_124", [d/PPP_Currency]="USD")
+DATA([d/WPLn]="TAX040_10_05_15") = RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_121", [d/PPP_Currency]="USD") + RESULTLOOKUP([d/WPLn]="AMT_210",[d/PPP_EntryNr]="UAP_124", [d/PPP_Currency]="USD")
 
```
