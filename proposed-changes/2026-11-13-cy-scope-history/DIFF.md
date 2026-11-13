# Script diff

Left = live (Royalties v45, Tax v26), right = proposed.

## PPP_Upstream_Royalties — step 1. Initialise

```diff
@@ -17 +17,2 @@ MEMBERSET [d/PPP_Currency] = "#"
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY and CY+1..CY+5: CY December holds the prior-year cost base (HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Royalties — step 14. Costs - CAPEX Oil

```diff
@@ -19 +19,2 @@ MEMBERSET [d/Lock] = ("#","Hist_Open")
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY and CY+1..CY+5: CY December holds the prior-year cost base (HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Royalties — step 15. Costs - CAPEX Gas

```diff
@@ -19 +19,2 @@ MEMBERSET [d/Lock] = ("#","Hist_Open")
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY and CY+1..CY+5: CY December holds the prior-year cost base (HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Royalties — step 16. Costs - OPEX Oil

```diff
@@ -21 +21,2 @@ MEMBERSET [d/Lock] = ("#","Hist_Open")
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY and CY+1..CY+5: CY December holds the prior-year cost base (HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Royalties — step 17. Costs - OPEX Gas

```diff
@@ -21 +21,2 @@ MEMBERSET [d/Lock] = ("#","Hist_Open")
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY and CY+1..CY+5: CY December holds the prior-year cost base (HCDT reads PREVIOUS(1,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(11,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Tax — step 1. Initialise

```diff
@@ -18 +18,2 @@ MEMBERSET [d/Lock] = "#"
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY-3..CY+5: CAPEX components need the 4 prior years for amortisation (step 11 reads PREVIOUS(1..4,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(47,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```

## PPP_Upstream_Tax — step 10. Tax - CAPEX Components

```diff
@@ -25 +25,2 @@ MEMBERSET [d/WPLn] = ("AMT_200","AMT_210",
-MEMBERSET [d/Date] = NEXT(1,"YEAR",%CY%) to NEXT(5,"YEAR",%CY%)
+// CY-3..CY+5: CAPEX components need the 4 prior years for amortisation (step 11 reads PREVIOUS(1..4,"YEAR"))
+MEMBERSET [d/Date] = PREVIOUS(47,"MONTH",%CY%) TO NEXT(5,"YEAR",%CY%)
```
