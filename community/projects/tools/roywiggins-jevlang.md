# jevlang (RoyWiggins)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python codec preprocessor: if/while/match conditions decided by TypeSafe Jev (including English conditions); upstream LICENSE file missing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RoyWiggins/jevlang) |
| Maintainer | [RoyWiggins](https://github.com/RoyWiggins). Independently curated. |
| Format | Python source codec / preprocessor runtime. |
| Requirements | Python; TypeSafe/Jev backend credentials per upstream; optional JEVLANG_LOCAL_PYTHON=1 for local Python conditionals. |
| License | Upstream LICENSE file not found at the reviewed tip; do not treat as Open source. Access/redistribution terms unspecified. TypeSafe usage may incur charges when live. |
| Disclosure | No LICENSE file at reviewed tip; do not claim Open source. Access terms unspecified upstream. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Distinct from TimMikeladze/JevLang. |

## When to use

Use for experimental **Jev-decided control flow** in Python (including English conditions). Prefer TimMikeladze/JevLang for typed policy engines with a clear MIT license.

## How it works

Registers a coding codec that rewrites block headers into runtime `cond` calls; the session packs locals/source context and asks Jev (or local Python in Luddite mode).

## Get started

```sh
git clone https://github.com/RoyWiggins/jevlang.git
cd jevlang
git checkout c2b0934567cad420fe69df054be7521f1a74e046
# pip install -e . per README; #coding: jevlang — no LICENSE file at review tip
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit c2b0934](https://github.com/RoyWiggins/jevlang/tree/c2b0934567cad420fe69df054be7521f1a74e046). AI-assisted README and license inspection; install/live paths not executed.
