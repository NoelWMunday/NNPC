# Script diff

Left = live (Royalties v45, Tax v26), right = proposed.

## PPP_Upstream_Royalties — step 1. Initialise

```diff
@@ -17 +17,2 @@ MEMBERSET [d/PPP_Currency] = "#"
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY Jan .. CY+5 Dec: CY December holds the prior-year cost base (Tax HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Royalties — step 14. Costs - CAPEX Oil

```diff
@@ -19 +19,2 @@ MEMBERSET [d/Lock] = ("#","Hist_Open")
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY Jan .. CY+5 Dec: CY December holds the prior-year cost base (Tax HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Royalties — step 15. Costs - CAPEX Gas

```diff
@@ -19 +19,2 @@ MEMBERSET [d/Lock] = ("#","Hist_Open")
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY Jan .. CY+5 Dec: CY December holds the prior-year cost base (Tax HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Royalties — step 16. Costs - OPEX Oil

```diff
@@ -21 +21,2 @@ MEMBERSET [d/Lock] = ("#","Hist_Open")
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY Jan .. CY+5 Dec: CY December holds the prior-year cost base (Tax HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Royalties — step 17. Costs - OPEX Gas

```diff
@@ -21 +21,2 @@ MEMBERSET [d/Lock] = ("#","Hist_Open")
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY Jan .. CY+5 Dec: CY December holds the prior-year cost base (Tax HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Tax — step 1. Initialise

```diff
@@ -18 +18,2 @@ MEMBERSET [d/Lock] = "#"
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY-3 Jan .. CY+5 Dec: CAPEX history for amortisation (step 11 reads PREVIOUS(1..4,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(47,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Tax — step 3. Tax - NDDC Levy Payable (Oil)

```diff
@@ -23 +23 @@ DATA([d/WPLn]="TAX025_15_10") = RESULTLOOKUP([d/WPLn]="CST05_15")
-DATA([d/WPLn]="TAX025_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX025_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 4. Tax - NDDC Levy Payable (Gas)

```diff
@@ -23 +23 @@ DATA([d/WPLn]="TAX030_15_10") = RESULTLOOKUP([d/WPLn]="CST05_20")
-DATA([d/WPLn]="TAX030_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX030_10") = RESULTLOOKUP([d/WPLn]="TL20_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 5. Tax - HCDT Fund Payable (Oil)

```diff
@@ -23 +23 @@ DATA([d/WPLn]="TAX015_15") = RESULTLOOKUP([d/WPLn]="CST05_05",[d/Date]=PREVIOUS(
-DATA([d/WPLn]="TAX015_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX015_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 6. Tax - HCDT Fund Payable (Gas)

```diff
@@ -23 +23 @@ DATA([d/WPLn]="TAX020_15") = RESULTLOOKUP([d/WPLn]="CST05_10",[d/Date]=PREVIOUS(
-DATA([d/WPLn]="TAX020_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX020_10") = RESULTLOOKUP([d/WPLn]="TL20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 7. Tax - Development Levy (Oil)

```diff
@@ -30 +30 @@ DATA([d/WPLn]="TAX005_15_40") = 0-RESULTLOOKUP([d/WPLn]="TAX025_05")
-DATA([d/WPLn]="TAX005_10") = RESULTLOOKUP([d/WPLn]="TL20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX005_10") = RESULTLOOKUP([d/WPLn]="TL20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 8. Tax - Development levy (Gas)

```diff
@@ -27 +27 @@ DATA([d/WPLn]="TAX010_15_30") = 0-RESULTLOOKUP([d/WPLn]="TAX020_05")
-DATA([d/WPLn]="TAX010_10") = RESULTLOOKUP([d/WPLn]="TL20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX010_10") = RESULTLOOKUP([d/WPLn]="TL20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 9. Tax - Production Allowance

```diff
@@ -21,2 +21,2 @@ DATA([d/WPLn]="TAX035_25") = RESULTLOOKUP([d/WPLn]="REV_05")
-DATA([d/WPLn]="TAX035_10") = RESULTLOOKUP([d/WPLn]="TA20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
-DATA([d/WPLn]="TAX035_15") = RESULTLOOKUP([d/WPLn]="TA20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") 
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX035_10") = RESULTLOOKUP([d/WPLn]="TA20_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX035_15") = RESULTLOOKUP([d/WPLn]="TA20_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 10. Tax - CAPEX Components

```diff
@@ -25 +25,2 @@ MEMBERSET [d/WPLn] = ("AMT_200","AMT_210",
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY-3 Jan .. CY+5 Dec: CAPEX history for amortisation (step 11 reads PREVIOUS(1..4,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(47,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Tax — step 12. Tax - Capital allowance for PPT

```diff
@@ -49 +49 @@ DATA([d/WPLn]=#AMORT_CAPEX) =
-DATA([d/WPLn]="TAX050_10_05") = RESULTLOOKUP([d/WPLn]="TA30_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX050_10_05") = RESULTLOOKUP([d/WPLn]="TA30_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
@@ -75,2 +75,2 @@ DATA([d/WPLn]=#ASSESSABLE) =
-DATA([d/WPLn]="TAX050_15_05") = RESULTLOOKUP([d/WPLn]="TA30_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
-DATA([d/WPLn]="TAX050_15_10") = RESULTLOOKUP([d/WPLn]="TA30_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX050_15_05") = RESULTLOOKUP([d/WPLn]="TA30_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX050_15_10") = RESULTLOOKUP([d/WPLn]="TA30_15",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 13. Tax - CA Limit Rolling Balance (Oil)

```diff
@@ -35 +35 @@ TAX055_35	Deductible Amortised Other Oil Capex
-DATA([d/WPLn]="TAX055_05") = RESULTLOOKUP([d/WPLn]="TA10_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn]="TAX055_05") = RESULTLOOKUP([d/WPLn]="TA10_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 16. Tax - Hydrocarbon Tax (CPR Limit & HT Payable)

```diff
@@ -23,3 +23,3 @@ VARIABLEMEMBER #PARAM2 OF [d/WPLn]
-DATA([d/WPLn] = "TAX070_05") = RESULTLOOKUP([d/WPLn]="TA15_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
-DATA([d/WPLn] = "TAX070_55") = RESULTLOOKUP([d/WPLn]="TL15_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
-DATA([d/WPLn] = "TAX070_60") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn] = "TAX070_05") = RESULTLOOKUP([d/WPLn]="TA15_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn] = "TAX070_55") = RESULTLOOKUP([d/WPLn]="TL15_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn] = "TAX070_60") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 19. Tax - PPT Tax (Oil)

```diff
@@ -20 +20 @@ MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
-DATA([d/WPLn] = "TAX085_10") = RESULTLOOKUP([d/WPLn]="TL05_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn] = "TAX085_10") = RESULTLOOKUP([d/WPLn]="TL05_05",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
```

## PPP_Upstream_Tax — step 20. Tax - CITA (Oil & Gas)

```diff
@@ -20,2 +20,2 @@ MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
-DATA([d/WPLn] = "TAX090_05") = RESULTLOOKUP([d/WPLn]="TL05_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000")
-DATA([d/WPLn] = "TAX090_10") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000")
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn] = "TAX090_05") = RESULTLOOKUP([d/WPLn]="TL05_10",[d/PPP_Entity]="#",[d/Lock]="Central",[d/Date]="000000") ENDIF
+IF [d/Date].[p/MONTHDESC] = "Dec" THEN DATA([d/WPLn] = "TAX090_10") = RESULTLOOKUP([d/WPLn]="SET10_10",[d/Date]="000000") ENDIF
```
