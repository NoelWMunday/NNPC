"""Generate repository documentation from a SAC folder export.

Usage: python3 tools/generate_docs.py <export.json> <repo-root>

The export is produced read-only from the SAC browser session (see README).
Writes:
  sac-export/<object-type>/<name>.json   raw definitions (source of record)
  data-actions/<name>.md                 one page per data action
  data-actions/README.md                 index + call map
  models/<name>.md                       dimensions and measures
  stories/<name>.md                      pages, models and data actions referenced
"""
import json
import os
import re
import sys
from collections import defaultdict

SKIP_STEP_KEYS = {"id", "name", "description", "stepType", "scriptContent", "runtimeContext",
                  "isNameSet", "isDescriptionSet", "isConvertedOnce", "isTextScriptChanged",
                  "panelType", "isVisualPanel", "memberFilter", "scriptReferences"}


def safe(name):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


def unjson(v):
    """SAC stores some step properties as JSON strings; expand them for readability."""
    if isinstance(v, str) and v[:1] in "[{":
        try:
            return unjson(json.loads(v))
        except ValueError:
            return v
    if isinstance(v, dict):
        return {k: unjson(x) for k, x in v.items()}
    if isinstance(v, list):
        return [unjson(x) for x in v]
    return v


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def param_line(p):
    val = p.get("value")
    if isinstance(val, dict):
        val = val.get("memberId") or val.get("memberIds") or val
    dim = p.get("dimensionId") or ""
    return (f"| `{p.get('displayKey')}` | {p.get('inputType', '')} | {p.get('type', '')} "
            f"| {dim} | {p.get('cardinality', '')} | `{json.dumps(val) if val is not None else ''}` |")


def main(src, root):
    b = json.load(open(src, encoding="utf-8"))
    das = b["dataActions"]
    models = b["models"]
    model_name = {cid: (m["data"].get("description") or cid) for cid, m in models.items()}
    inv_by_id = {i["id"]: i for i in b["inventory"]}
    seq_name = {d["id"]: n for n, d in das.items()}

    # ---- raw export -------------------------------------------------------
    for n, d in das.items():
        write(f"{root}/sac-export/data-actions/{safe(n)}.json", json.dumps(d, indent=1, ensure_ascii=False))
    for cid, m in models.items():
        write(f"{root}/sac-export/models/{safe(model_name[cid])}.json", json.dumps(m, indent=1, ensure_ascii=False))
    for n, s in b["stories"].items():
        write(f"{root}/sac-export/stories/{safe(n)}.json", json.dumps(s, ensure_ascii=False))
    write(f"{root}/sac-export/currency/CURRENCY.json", json.dumps(b["currencyTable"], indent=1, ensure_ascii=False))
    write(f"{root}/sac-export/inventory.json", json.dumps(
        {k: b[k] for k in ("exportedAt", "tenant", "folder", "folderId", "inventory")}, indent=1))

    # ---- call graph -------------------------------------------------------
    calls = defaultdict(list)
    called_by = defaultdict(list)
    for n, d in das.items():
        for s in d["steps"]:
            if s["stepType"] == "NESTED_SEQUENCE":
                tid = s.get("nestedSequenceId", "").split(":")[-1]
                t = seq_name.get(tid, tid)
                calls[n].append(t)
                called_by[t].append(n)

    # stories -> data actions / models (by id reference anywhere in the story JSON)
    story_refs = {}
    for sn, s in b["stories"].items():
        txt = json.dumps(s)
        story_refs[sn] = {
            "das": sorted({n for n, d in das.items() if d["id"] in txt}),
            "models": sorted({model_name[c] for c in models if c in txt}),
        }
    da_in_stories = defaultdict(list)
    for sn, r in story_refs.items():
        for n in r["das"]:
            da_in_stories[n].append(sn)

    # ---- data action pages ------------------------------------------------
    for n, d in das.items():
        L = [f"# {n}", ""]
        if d.get("description") and d["description"] != n:
            L += [f"> {d['description']}", ""]
        L += ["| | |", "|---|---|",
              f"| SAC id | `{d['id']}` |",
              f"| Default model | {model_name.get(d.get('defaultCubeId'), d.get('defaultCubeId') or '—')} |",
              f"| Created by | {d.get('createdBy', '')} |",
              f"| Last changed | {d.get('modified', '')} by {d.get('changedBy', '')} |",
              f"| Called by | {', '.join(f'[{c}]({safe(c)}.md)' for c in sorted(set(called_by.get(n, [])))) or '—'} |",
              f"| Used in stories | {', '.join(f'[{s}](../stories/{safe(s)}.md)' for s in sorted(da_in_stories.get(n, []))) or '—'} |",
              ""]
        if d.get("parameters"):
            L += ["## Parameters", "", "| Key | Input | Type | Dimension | Cardinality | Default |",
                  "|---|---|---|---|---|---|"]
            L += [param_line(p) for p in d["parameters"]]
            L.append("")
        L += ["## Steps", "", "| # | Step | Type | Notes |", "|---|---|---|---|"]
        for i, s in enumerate(d["steps"], 1):
            note = ""
            if s["stepType"] == "NESTED_SEQUENCE":
                t = seq_name.get(s.get("nestedSequenceId", "").split(":")[-1], "?")
                note = f"runs [{t}]({safe(t)}.md)"
            elif s.get("sourceCubeId"):
                note = f"from {model_name.get(s['sourceCubeId'], s['sourceCubeId'])}"
            if s.get("disabled"):
                note = ("**DISABLED** " + note).strip()
            L.append(f"| {i} | {s.get('name') or '(unnamed)'} | {s['stepType']} | {note} |")
        L.append("")
        for i, s in enumerate(d["steps"], 1):
            L += [f"### {i}. {s.get('name') or '(unnamed)'} — {s['stepType']}", ""]
            if s.get("description") and s["description"] != s.get("name"):
                L += [s["description"], ""]
            if s.get("scriptContent"):
                L += ["```", s["scriptContent"].rstrip(), "```", ""]
            cfg = {k: unjson(v) for k, v in s.items() if k not in SKIP_STEP_KEYS}
            if s["stepType"] == "SCRIPT":
                used = (s.get("scriptReferences") or {})
                if used.get("usedParameters"):
                    L += [f"Parameters used: {', '.join(used['usedParameters'])}", ""]
            elif cfg:
                L += ["<details><summary>Configuration</summary>", "", "```json",
                      json.dumps(cfg, indent=1, ensure_ascii=False), "```", "", "</details>", ""]
        write(f"{root}/data-actions/{safe(n)}.md", "\n".join(L))

    # ---- data action index + call map -------------------------------------
    roots = sorted(n for n in das if calls.get(n) and not called_by.get(n))
    groups = defaultdict(list)
    for n in sorted(das, key=str.lower):
        groups[n.split("_")[0] if not n.startswith("PPP_") else "PPP_" + n.split("_")[1]].append(n)
    L = ["# Data actions", "",
         f"Exported {b['exportedAt'][:10]} from `{b['folder']}`. {len(das)} data actions. "
         "Generated by `tools/generate_docs.py` — do not edit by hand; edit SAC, re-export, regenerate.", "",
         "## Call map", "", "Multi-step chains (data action → embedded data actions).", "", "```mermaid", "flowchart LR"]
    ids = {n: f"n{i}" for i, n in enumerate(sorted(das))}
    for p in sorted(calls):
        for c in dict.fromkeys(calls[p]):
            if c in ids:
                L.append(f'  {ids[p]}["{p}"] --> {ids[c]}["{c}"]')
    L += ["```", "", "## Index", "",
          "| Data action | Description | Model | Steps | Called by | Stories | Last changed |",
          "|---|---|---|---|---|---|---|"]
    for n in sorted(das, key=str.lower):
        d = das[n]
        types = defaultdict(int)
        for s in d["steps"]:
            types[s["stepType"]] += 1
        L.append(f"| [{n}]({safe(n)}.md) | {d.get('description') or ''} | "
                 f"{model_name.get(d.get('defaultCubeId'), '')} | "
                 f"{', '.join(f'{v}×{k.lower()}' for k, v in types.items())} | "
                 f"{', '.join(sorted(set(called_by.get(n, [])))) or '—'} | "
                 f"{', '.join(sorted(da_in_stories.get(n, []))) or '—'} | {(d.get('modified') or '')[:10]} |")
    orphans = sorted(n for n in das if not called_by.get(n) and not da_in_stories.get(n))
    L += ["", "## Not referenced", "",
          "Not called by another data action and not found in any story in this folder "
          "(may still be used from elsewhere, e.g. a calendar task):", ""]
    L += [f"- [{n}]({safe(n)}.md)" for n in orphans]
    write(f"{root}/data-actions/README.md", "\n".join(L) + "\n")

    # ---- models -----------------------------------------------------------
    ML = ["# Models", "", "| Model | Id | Dimensions |", "|---|---|---|"]
    for cid, m in models.items():
        md = m["data"]
        nm = model_name[cid]
        ML.append(f"| [{nm}]({safe(nm)}.md) | `{cid}` | {len(md.get('dimensions', []))} |")
        L = [f"# {nm}", "", f"SAC id `{cid}`", "",
             f"Default currency: {md.get('defaultCurrency')} · Data locking: {md.get('dataLockingEnabled')}", "",
             "## Dimensions", "", "| Dimension | Description | Type | Hierarchies |", "|---|---|---|---|"]
        for dm in md.get("dimensions", []):
            hs = [h.get("name") or h.get("id") for h in (dm.get("hierarchies") or []) if isinstance(h, dict)]
            L.append(f"| `{dm.get('name')}` | {dm.get('description', '')} | {dm.get('type', '')} | {', '.join(map(str, hs))} |")
        if md.get("measures"):
            L += ["", "## Measures", "", "| Measure | Description | Aggregation | Decimals |", "|---|---|---|---|"]
            for ms in md["measures"]:
                L.append(f"| `{ms.get('name') or ms.get('id')}` | {ms.get('description', '')} | "
                         f"{ms.get('aggregation', '')} | {ms.get('decimalPlaces', '')} |")
        users = sorted(n for n, d in das.items() if d.get("defaultCubeId") == cid)
        L += ["", "## Data actions with this default model", ""] + [f"- [{n}](../data-actions/{safe(n)}.md)" for n in users]
        write(f"{root}/models/{safe(nm)}.md", "\n".join(L) + "\n")
    write(f"{root}/models/README.md", "\n".join(ML) + "\n")

    # ---- stories ----------------------------------------------------------
    SL = ["# Stories", "", "| Story | Description | Models | Data actions | Last changed |", "|---|---|---|---|---|"]
    for sn, s in sorted(b["stories"].items(), key=lambda x: x[0].lower()):
        meta = next((i for i in b["inventory"] if i["name"] == sn and i["type"] == "STORY"), {})
        pages = []
        try:
            for e in s["data"]["contentOptimized"]["entities"]:
                for p in ((e.get("data") or {}).get("pages") or []):
                    pages.append(p.get("title") or p.get("name") or p.get("id"))
        except (KeyError, TypeError):
            pass
        r = story_refs[sn]
        SL.append(f"| [{sn}]({safe(sn)}.md) | {meta.get('description', '')} | {', '.join(r['models'])} | "
                  f"{len(r['das'])} | {(meta.get('modifiedTime') or '')[:10]} |")
        L = [f"# {sn}", "", f"> {meta.get('description', '')}", "",
             f"Last changed {(meta.get('modifiedTime') or '')[:10]} by {meta.get('modifiedBy', '')}", "",
             "## Models", ""] + [f"- [{m}](../models/{safe(m)}.md)" for m in r["models"]]
        if pages:
            L += ["", "## Pages", ""] + [f"- {p}" for p in pages]
        L += ["", "## Data actions referenced", ""] + [f"- [{n}](../data-actions/{safe(n)}.md)" for n in r["das"]]
        write(f"{root}/stories/{safe(sn)}.md", "\n".join(L) + "\n")
    write(f"{root}/stories/README.md", "\n".join(SL) + "\n")

    print(f"{len(das)} data actions, {len(models)} models, {len(b['stories'])} stories")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
