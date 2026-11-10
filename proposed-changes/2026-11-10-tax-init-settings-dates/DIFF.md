# Script diff

Left = live in SAC (`sac-export/` on `main`), right = proposed.

| Data action | Step | Lines |
|---|---|---|
| PPP_Upstream_Tax | 1. Initialise | +0 / -1 |
| PPP_Upstream_Royalties | 3. Royalties - Tranch volumes | +20 / -20 |
| PPP_Upstream_Royalties | 4. Royalties - Values (Oil) | +15 / -15 |

## PPP_Upstream_Tax — step 1. Initialise

```diff
@@ -8,3 +8,2 @@ MEMBERSET [d/Measures]="Value_WPLn"
 MEMBERSET [d/WPLn] = ("REV_32","REV_26","REV_40",
-					  BASEMEMBER([d/WPLn] ,"CST14"), 
 					  BASEMEMBER([d/WPLn] ,"REV3_05"))
```

## PPP_Upstream_Royalties — step 3. Royalties - Tranch volumes

```diff
@@ -27,11 +27,11 @@ DATA([d/WPLn] = #TRANCH1) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000"
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_010_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_015_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_020_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_025_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_030_01",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
@@ -40,11 +40,11 @@ DATA([d/WPLn] = #TRANCH2) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000"
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_010_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_015_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_020_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_025_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_030_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
@@ -53,11 +53,11 @@ DATA([d/WPLn] = #TRANCH3) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000"
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_010_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_015_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_020_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_025_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_030_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
@@ -66,11 +66,11 @@ DATA([d/WPLn] = #TRANCH4) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="000000"
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_005_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_010_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_015_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_020_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_025_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="TranchValue",[d/WPLn]="RR01_030_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))				
```

## PPP_Upstream_Royalties — step 4. Royalties - Values (Oil)

```diff
@@ -40,11 +40,11 @@ DATA([d/WPLn] = #RR_TRANCH2) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="0000
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_005_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_010_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_015_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_020_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_025_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_030_02",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
@@ -53,11 +53,11 @@ DATA([d/WPLn] = #RR_TRANCH3) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="0000
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_005_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_010_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_015_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_020_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_025_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_030_03",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))
@@ -66,11 +66,11 @@ DATA([d/WPLn] = #RR_TRANCH4) =  (RESULTLOOKUP([d/WPLn]="SET05_05",[d/Date]="0000
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_005_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_10",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_010_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_15",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_015_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_20",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_020_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_25",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_025_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central")) +
-							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="202612") * 
+							(RESULTLOOKUP([d/WPLn]="SET05_30",[d/Date]="000000") * 
 							 RESULTLOOKUP([d/Measures]="Royalty_PIA",[d/WPLn]="RR01_030_04",[d/PPP_Entity]="#",[d/Date]="000000",[d/Lock]="Central"))				
```
