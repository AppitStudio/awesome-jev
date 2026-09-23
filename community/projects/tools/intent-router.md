# Intent-Router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill that compiles a vague “do something” request into a typed `IntentSpec` (probe, ask one question, or halt) before planning or routing—designed as the input layer for typed decision models such as TypeSafe Jev and Laya.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/angel291592/Intent-Router) |
| Maintainer | [angel291592](https://github.com/angel291592). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent skill package **intent-router 0.3.0** (`skills/intent-router/SKILL.md` + IntentSpec JSON Schema and fixtures). |
| Requirements | An agent host that can load Agent Skills (e.g. Claude Code / compatible skill runners). Optional repo/ticket/doc tools for probing. No TypeSafe key is required for the skill itself; downstream Jev/Laya routers use their own keys. |
| License | [MIT](https://github.com/angel291592/Intent-Router/blob/f60fefe46d6acffdea04a7a482e2aa0002bfe253/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, skill, schema, eval fixtures). Live agent/Jev runs were **not** executed on the review host. |

## When to use

Use it when a coding or ops request leaves decision-bearing unknowns (objects, approach, failure behaviour, acceptance) and you want a machine-readable contract before a router or planner acts. Prefer [JevIntent](../apps/jev-intent.md) for WeChat long-press intent labeling, or a router such as [Agent Router](agent-router.md) once the intent is already clear.

## How it works

The skill runs parse → resolve → typecheck: it probes reachable sources, asks at most one preference/irreversible question at a time with a recommended default, and emits a route/ask/halt `IntentSpec` ([`skills/intent-router/SKILL.md`](https://github.com/angel291592/Intent-Router/blob/f60fefe46d6acffdea04a7a482e2aa0002bfe253/skills/intent-router/SKILL.md), [`schema/intentspec.schema.json`](https://github.com/angel291592/Intent-Router/blob/f60fefe46d6acffdea04a7a482e2aa0002bfe253/skills/intent-router/schema/intentspec.schema.json)). It does not call TypeSafe itself; Jev/Laya are documented as the intended downstream consumers of the spec.

## Get started

```sh
git clone https://github.com/angel291592/Intent-Router.git
cd Intent-Router
git checkout f60fefe46d6acffdea04a7a482e2aa0002bfe253
# Install/load skills/intent-router per your agent host's skill docs
```

Pin for review: [commit f60fefe](https://github.com/angel291592/Intent-Router/tree/f60fefe46d6acffdea04a7a482e2aa0002bfe253).

## Examples and demos

- Schema examples under `skills/intent-router/schema/examples/`.
- Eval cases and fixtures under `evals/` (not executed on the review host).
- README demo screenshots for probe / question / spec.

## Limits and data handling

The skill may read local repo/docs/ticket surfaces you expose to the agent; it does not by itself send data to TypeSafe. Downstream routers that consume the IntentSpec may. This listing did not run live agents or Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit f60fefe](https://github.com/angel291592/Intent-Router/tree/f60fefe46d6acffdea04a7a482e2aa0002bfe253) (**0.3.0**, MIT). AI-assisted source review of README, LICENSE, skill, and schema. No live agent or TypeSafe spend.

Related: [Agent Router](agent-router.md), [VexJoy Agent](vexjoy-agent.md), [ask-jev-skill](ask-jev-skill.md).
