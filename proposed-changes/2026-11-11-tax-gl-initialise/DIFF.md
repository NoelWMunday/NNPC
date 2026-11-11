# Script diff

Tax v24 step 21 "GL Entries" (left) → new step 22 "GL Entries" (right). Step 21 becomes "GL Entries - Initialise" (new script, below).

## Step 22. GL Entries

```diff
@@ -18,13 +18,3 @@ MEMBERSET [d/PPP_Currency] = "USD"
 
-DATA([d/Measures] = "GC_CR", [d/GL] = "6011009", [d/PPP_EntryNr] = "UP_0005") = 0
-DATA([d/Measures] = "GC_CR", [d/GL] = "6022022", [d/PPP_EntryNr] = "UP_0005") = 0
-DATA([d/Measures] = "GC_CR", [d/GL] = "5230001", [d/PPP_EntryNr] = "UP_0005") = 0
-DATA([d/Measures] = "GC_CR", [d/GL] = "4101010", [d/PPP_EntryNr] = "UP_0005") = 0
-DATA([d/Measures] = "GC_CR", [d/GL] = "4600105", [d/PPP_EntryNr] = "UP_0005") = 0
-DATA([d/Measures] = "GC_CR", [d/GL] = "5150009", [d/PPP_EntryNr] = "UP_0005") = 0
-DATA([d/Measures] = "GC_CR", [d/GL] = "4110003", [d/PPP_EntryNr] = "UP_0005") = 0
-// No longer posted by Tax (11 Nov): Direct Cost (in 4500006), corporate overhead and finance cost (CostAlloc, UP_0010)
-DATA([d/Measures] = "GC_CR", [d/GL] = "4101006", [d/PPP_EntryNr] = "UP_0005") = 0
-DATA([d/Measures] = "GC_CR", [d/GL] = "5080044", [d/PPP_EntryNr] = "UP_0005") = 0
-DATA([d/Measures] = "GC_CR", [d/GL] = "FINEXP_005", [d/PPP_EntryNr] = "UP_0005") = 0
+// Old postings on UP_0005 are cleared by the previous step "GL Entries - Initialise"
 
@@ -82,2 +72,5 @@ DATA([d/Measures] = "GC_CR", [d/WPLn] = "#", [d/GL] = "4500006", [d/PPP_EntryNr]
 		RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "TAX045_05_25", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#")) *
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_90", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") / 100 +
+	// Non-productive cost: gas flare penalty (calculated by Royalties step 13), NNPC equity share
+	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_230", [d/GL] = "#", [d/PPP_EntryNr] = "UAP_GFP", [d/PPP_Currency] = "#") *
 	RESULTLOOKUP([d/Measures] = "Value_WPLn", [d/WPLn] = "AMT_90", [d/GL] = "#", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") / 100
```

## Step 21. GL Entries - Initialise

```
CONFIG.TIME_HIERARCHY = CALENDARYEAR
CONFIG.FLIPPING_SIGN_ACCORDING_ACCTYPE = OFF
CONFIG.GENERATE_UNBOOKED_DATA = ON

// Clears every GL posting (GC_CR) on UP_0005 for the entity, so postings dropped from GL Entries
// do not stay in the model. Same pattern as PPP_Upstream_Revenue step 7 "GL Entries - initialise".
// GL Entries (next step) re-posts all UP_0005 lines, incl. revenue and royalty.
MEMBERSET [d/PPP_Entity] = BASEMEMBER([d/PPP_Entity] , %Entity%)
MEMBERSET [d/PCycle] = %PCycle%
MEMBERSET [d/Measures] = ("GC_CR")
MEMBERSET [d/WPLn] = ("#")
MEMBERSET [d/Ln] = "#"
MEMBERSET [d/Objectives] = "#"
MEMBERSET [d/ProductServ] = "#"
MEMBERSET [d/Strategy] = "#"
MEMBERSET [d/WorkProgram] = "#"
MEMBERSET [d/Lock] = "#"
MEMBERSET [d/PPP_EntryNr] = ("UP_0005")
MEMBERSET [d/PPP_Currency] = "USD"

DELETE()

```
