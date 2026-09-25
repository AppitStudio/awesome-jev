# jev-claw

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenClaw tool `jev_route` (plus opt-in automatic routing): TypeSafe Jev classifies task type/complexity/risk, then code applies your model routing policy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/trietphan/jev-claw) |
| Maintainer | [trietphan](https://github.com/trietphan). Independently curated. |
| Format | OpenClaw plugin/tool integration. |
| Requirements | OpenClaw host; TypeSafe Jev access for live decisions. |
| License | [MIT](https://github.com/trietphan/jev-claw/blob/3fbd39fe976239db0f37c5573760ae63e110200a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live OpenClaw/Jev paths not run on the review host. |

## When to use

Use when **OpenClaw agents** should pick a model route from typed Jev judgments instead of static string rules or LLM self-routing.

## How it works

`jev_route` returns structured fields (task_type, complexity, risk, route, confidence). Optional hooks prefilter casual turns and can enforce routes on `sessions_spawn`.

## Get started

```sh
git clone https://github.com/trietphan/jev-claw.git
cd jev-claw
git checkout 3fbd39fe976239db0f37c5573760ae63e110200a
# Follow README install into OpenClaw
```

## Examples and demos

- README JSON example for debugging escalation routes.

## Limits and data handling

Task text and attempt metadata go to TypeSafe when Jev runs. Local prefilter may skip casual turns without a call.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 3fbd39f](https://github.com/trietphan/jev-claw/tree/3fbd39fe976239db0f37c5573760ae63e110200a). AI-assisted README and LICENSE inspection; live OpenClaw not run.
