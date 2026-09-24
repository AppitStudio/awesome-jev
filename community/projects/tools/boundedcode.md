# BoundedCode

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Coding agent stack for **8 GB GPUs**: local OpenCode generation, a **required** TypeSafe Jev decision plane for narrow judgments, and a Go supervisor that only accepts verified candidates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/akynte/boundedcode) |
| Maintainer | [akynte](https://github.com/akynte). Independently curated. |
| Format | Go supervisor + OpenCode integration (pre-1.0). |
| Requirements | Linux x86-64 + CUDA 8 GB GPU / 64 GB RAM per upstream docs; TypeSafe Jev for decisions; OpenCode 2 UI. |
| License | [Apache-2.0](https://github.com/akynte/boundedcode/blob/663a6c6eed933134450ebdfdda4a747cd819ed29/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live GPU/OpenCode/Jev not run. Pre-1.0—upstream cautions effectiveness is not yet broadly established. |

## When to use

Use it when you want **local code generation** with hosted typed decisions and deterministic acceptance. Prefer lighter Jev gates (hooks/Actions) when you do not need a full supervised agent stack.

## How it works

OpenCode investigates/edits locally; narrow judgments leave the machine for TypeSafe Jev; only the Go supervisor accepts work from verification results and scope. See upstream trust-boundary docs.

## Get started

```sh
git clone https://github.com/akynte/boundedcode.git
cd boundedcode
git checkout 663a6c6eed933134450ebdfdda4a747cd819ed29
# Follow docs/how-to/install.md for GPU/OpenCode/Jev setup (not executed here)
```

## Examples and demos

- README architecture table; `docs/`, `examples/`, `evals/` (not executed).

## Limits and data handling

Judgment payloads leave the machine for TypeSafe; generation stays local per upstream. Not a fully offline system. Historical evals may include false acceptances—treat checks as evidence, not proof.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 663a6c6](https://github.com/akynte/boundedcode/tree/663a6c6eed933134450ebdfdda4a747cd819ed29). AI-assisted README + docs skim. No GPU/TypeSafe spend.

Related: [Agent Router](agent-router.md), [Canny](canny.md).
