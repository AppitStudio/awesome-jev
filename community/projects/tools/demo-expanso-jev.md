# demo-expanso-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Expanso Edge × TypeSafe Jev demo suite: fingerprint routine log lines locally, ask Jev only on the remainder, route page/notify/review/archive (and related pipelines) with hold-on-failure behavior and live boards.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/expanso-io/demo-expanso-jev) |
| Maintainer | [expanso-io](https://github.com/expanso-io). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Demo repository: Expanso pipeline YAML, Python board/servers, `just` recipes, and a keyword mock Jev server. |
| Requirements | `just`, Python 3, `curl`; Expanso Edge + CLI v2+ and an Expanso Cloud network for full pipelines; TypeSafe key **or** `shared/jev-mock-server.py` with `JEV_API_URL` pointed at the mock. |
| License | [Apache-2.0](https://github.com/expanso-io/demo-expanso-jev/blob/c54e752abfa7535a96f1336a1ff2771a0f6de9d9/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation beyond listing a public Expanso demo. Not an endorsement of Expanso Cloud. Source and offline Python UI/routing tests inspected. Live Expanso Cloud deploy and live TypeSafe calls were not run. |

## When to use

Use it to learn edge pre-filter + Jev judgment patterns for logs, tickets, moderation, pod labels, and similar streams—with a board that separates bypassed vs judged vs failed traffic. Prefer thinner single-purpose tools when you only need a library call, not an Expanso pipeline. Mock Jev answers are keyword heuristics (board marks them)—not inference.

## How it works

Expanso pipelines shape and fingerprint records; known routine lines skip the model. Remaining events POST to System One (`/v1/systemone`); answers drive routing. On Jev unavailability, pipelines can **hold** rather than invent decisions. [`shared/jev-mock-server.py`](https://github.com/expanso-io/demo-expanso-jev/blob/c54e752abfa7535a96f1336a1ff2771a0f6de9d9/shared/jev-mock-server.py) emulates the wire format for zero-key demos. Pod-label demo combines simulated incidents with real cloud/K8s side effects when fully wired—read its runbook before enabling.

## Get started

```sh
git clone https://github.com/expanso-io/demo-expanso-jev.git
cd demo-expanso-jev
git checkout c54e752abfa7535a96f1336a1ff2771a0f6de9d9
# Offline board accounting tests (no Expanso Cloud / no live Jev):
python3 demos/01-log-triage/tests/ui_server_tests.py
python3 demos/11-pod-labels/test_routing.py
python3 demos/11-pod-labels/test_adapter.py
# Full demo needs Expanso Cloud credentials + just init / just up — see README
```

Optional mock: `uv run shared/jev-mock-server.py` then set `JEV_API_URL=http://127.0.0.1:8099/v1/systemone`.

## Examples and demos

- Log-triage three-act board (`just up triage`) and pod-label browser demo (`just up`) per upstream README.
- Multiple pipeline YAMLs under [`demos/`](https://github.com/expanso-io/demo-expanso-jev/tree/c54e752abfa7535a96f1336a1ff2771a0f6de9d9/demos) (sensor triage, SOC prefilter, moderation, …).
- Offline: log-triage UI server tests **72/72** passed; pod-label routing/adapter unittest suites passed on the review host.

## Limits and data handling

Full demos send selected records to TypeSafe (or the mock) and require Expanso Cloud. Author-reported “nine lines in ten” bypass rates are not measured here. Simulated pod incidents are explicit; still treat live Kubernetes patches as consequential. Do not confuse mock keyword labels with calibrated Jev probabilities.

## Review and maintenance

Reviewed on **2026-09-20** at [commit c54e752](https://github.com/expanso-io/demo-expanso-jev/tree/c54e752abfa7535a96f1336a1ff2771a0f6de9d9): Apache-2.0. AI-assisted source review of README, mock server, pipeline docs, and LICENSE. Ran `python3 demos/01-log-triage/tests/ui_server_tests.py` (**72/72**), `test_routing.py` / `test_adapter.py` (unittest OK). No Expanso Cloud deploy; no live TypeSafe calls. `log_safety_test.py` needs PyYAML (not installed on the review host).

Related: [jevlogs](jevlogs.md), [jev-corrective-rag](jev-corrective-rag.md), [jeval](jeval.md).
