"""Generate the proposed Upstream scripts for Trello #19 (inputs on PPP_Currency = USD).

Usage: python3 tools/propose_currency_usd.py <repo-root> <base-git-ref> <out-folder>

Targets are computed from the scripts as they were at <base-git-ref> (the 9 Nov snapshot: 9a56a3f).
Each target is compared with the current `sac-export/` (what is live). Steps that differ are written to
<out-folder> with manifest.json (before/after SHA-256) and DIFF.md.

Rules:
  R1  Calculations and metrics stay on PPP_Currency = "#".
  R2  Every RESULTLOOKUP of a Capex/Opex input (AMT_200/210/220/230) reads PPP_Currency = "USD".
  R3  Royalties steps 2-21 get MEMBERSET [d/PPP_Currency] = "#" (they had none).
  R4  Royalties cost loops (steps 14-17) iterate the USD input leaves and append to "#".
Central assumptions (GA_*, RR*, TL*, TA*) and calculated lines are not touched.
"""
import json
import os
import re
import sys

# Only the Capex/Opex inputs are on USD (Noel, 10 Nov). Metrics (AMT_46/80/85/90/97, UOM_*, SET*) are
# captured on "#" by the Metrics and Settings tables.
INPUTS = re.compile(r'^AMT_(200|210|220|230)$')
DAS = ["PPP_Upstream_Revenue", "PPP_Upstream_Royalties", "PPP_Upstream_Tax"]
COST_LOOPS = {14: ("CST05_15", "AMT_200"), 15: ("CST05_20", "AMT_210"),
              16: ("CST05_05", "AMT_220"), 17: ("CST05_10", "AMT_230")}


def fix_lookup(m):
    args = m.group(1)
    w = re.search(r'\[d/WPLn\]\s*=\s*"([^"]+)"', args)
    if not w or not INPUTS.match(w.group(1)):
        return m.group(0)
    if re.search(r'\[d/PPP_EntryNr\]\s*=\s*"UAP_GFP"', args):
        return m.group(0)  # gas flare penalty is calculated (Royalties step 13), stays on "#"
    if "[d/PPP_Currency]" in args:
        args = re.sub(r'\[d/PPP_Currency\]\s*=\s*"[^"]*"', '[d/PPP_Currency]="USD"', args)
    else:
        args = args.rstrip() + ', [d/PPP_Currency]="USD"'
    return f"RESULTLOOKUP({args})"


def transform(da, idx, script):
    out = []
    for line in script.split("\n"):
        if line.lstrip().startswith("//"):
            out.append(line)
            continue
        out.append(re.sub(r'RESULTLOOKUP\(([^()]*)\)', fix_lookup, line))
    s = "\n".join(out)

    if da == "PPP_Upstream_Royalties" and 2 <= idx <= 21 and "MEMBERSET [d/PPP_Currency]" not in s:
        s = re.sub(r'(MEMBERSET \[d/Measures\][^\n]*\n)',
                   r'\1MEMBERSET [d/PPP_Currency] = "#"\n', s, count=1)

    if da == "PPP_Upstream_Royalties" and idx in COST_LOOPS:
        target, src = COST_LOOPS[idx]
        s = s.replace('MEMBERSET [d/PPP_Currency] = "#"\n', 'MEMBERSET [d/PPP_Currency] = ("#","USD")\n', 1)
        s = re.sub(
            r'IF \[d/PPP_EntryNr\] != "#" THEN\s*\n\s*DATA\.APPEND\(\[d/WPLn\] = "' + target +
            r'", \[d/PPP_EntryNr\] = "#"\) = RESULTLOOKUP\(\[d/WPLn\] = "' + src + r'"[^)]*\)',
            f'IF [d/PPP_EntryNr] != "#" AND [d/PPP_Currency] = "USD" THEN\n'
            f'\tDATA.APPEND([d/WPLn] = "{target}", [d/PPP_EntryNr] = "#", [d/PPP_Currency] = "#") = '
            f'RESULTLOOKUP([d/WPLn] = "{src}")', s)
    return s


def main(root, base_ref, out):
    import hashlib
    import subprocess
    import tempfile
    sha = lambda t: hashlib.sha256(t.encode()).hexdigest()
    os.makedirs(out, exist_ok=True)
    manifest, rows, body = [], [], []
    tmp = tempfile.mkdtemp()
    for da in DAS:
        orig = json.loads(subprocess.run(["git", "-C", root, "show", f"{base_ref}:sac-export/data-actions/{da}.json"],
                                         capture_output=True, text=True, check=True).stdout)
        live = json.load(open(f"{root}/sac-export/data-actions/{da}.json", encoding="utf-8"))
        for i, (o, l) in enumerate(zip(orig["steps"], live["steps"]), 1):
            assert o["id"] == l["id"]
            if not o.get("scriptContent"):
                continue
            after, before = transform(da, i, o["scriptContent"]), l["scriptContent"]
            if after == before:
                continue
            name = re.sub(r"[^A-Za-z0-9]+", "_", l["name"]).strip("_")
            path = f"{out}/{da}/step{i:02d}_{name}.advformula"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(after)
            bf = f"{tmp}/before"
            open(bf, "w", encoding="utf-8").write(before)
            d = subprocess.run(["git", "diff", "--no-index", "-U1", "--no-color", bf, path],
                               capture_output=True, text=True).stdout.splitlines()[4:]
            d = [x for x in d if not x.startswith("\\ No newline")]
            rows.append(f"| {da} | {i}. {l['name']} | {sum(1 for x in d if x.startswith('+'))} |")
            body += ["", f"## {da} — step {i}. {l['name']}", "", "```diff", *d, "```"]
            manifest.append({"dataAction": da, "step": i, "stepId": l["id"], "name": l["name"],
                             "file": os.path.relpath(path, root), "beforeSha256": sha(before), "afterSha256": sha(after)})
    json.dump(manifest, open(f"{out}/manifest.json", "w"), indent=1)
    open(f"{out}/DIFF.md", "w", encoding="utf-8").write("\n".join(
        ["# Script diff", "", f"Generated by `tools/propose_currency_usd.py` (base `{base_ref}`). "
         "Left = live in SAC (`sac-export/`), right = proposed.", "",
         "| Data action | Step | Lines changed |", "|---|---|---|", *rows, *body]) + "\n")
    print(f"{len(manifest)} steps, {sum(int(r.split('|')[-2]) for r in rows)} lines")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
