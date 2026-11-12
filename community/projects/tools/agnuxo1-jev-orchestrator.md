# JEV Orchestrator by Agnuxo1 (bounded control plane where Jev routes and supervises multi-model work)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Windows-first Python control plane for multi-model workflows: deterministic short-circuits handle known work, one typed Jev request picks a bounded route and success criteria, generative tiers escalate only on evidence of insufficiency, and code enforces per-run limits on calls, escalation and tokens. Includes TartanIMU contract checks. Separate from the listed petercr jev-orchestrator.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Agnuxo1/TartanIMU-Cognitive-Stack) |
| Maintainer | [Agnuxo1](https://github.com/Agnuxo1). Independently curated. |
| Format | Python package and CLI (MIT; README in English and Spanish) |
| Requirements | Python 3.11+ and a TypeSafe key; keys for the generative tiers you configure. |
| License | [MIT](https://github.com/Agnuxo1/TartanIMU-Cognitive-Stack/blob/d7a661635a0f8f337437d0ac9aa026375297c52b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_orchestrator/config.py`](https://github.com/Agnuxo1/TartanIMU-Cognitive-Stack/blob/d7a661635a0f8f337437d0ac9aa026375297c52b/jev_orchestrator/config.py) at the pinned commit. |

## When to use

- Cut unnecessary model calls in a multi-model workflow with evidence-based escalation.
- Mismatch: Windows-first reference implementation; not a trained model.

## How it works

`jev_orchestrator/config.py` points the Jev client at `https://api.typesafe.ai/v1/systemone`; the orchestrator batches route selection and success criteria into one typed request and treats Jev confidence as a judgment, not a guarantee. Integration evidence: [`jev_orchestrator/config.py`](https://github.com/Agnuxo1/TartanIMU-Cognitive-Stack/blob/d7a661635a0f8f337437d0ac9aa026375297c52b/jev_orchestrator/config.py).

## Get started

Create a virtual environment and install the package in editable mode, then follow the README for credentials.

```sh
python -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev operating policy: [github.com/Agnuxo1/TartanIMU-Cognitive-Stack/blob/d7a661635a0f8f337437d0ac9aa026375297c52b/docs/JEV-POLICY.md](https://github.com/Agnuxo1/TartanIMU-Cognitive-Stack/blob/d7a661635a0f8f337437d0ac9aa026375297c52b/docs/JEV-POLICY.md)

## Limits and data handling

Task routing questions go to TypeSafe on your key; telemetry omits free-form content and redacts common secret patterns.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit d7a661635a0f](https://github.com/Agnuxo1/TartanIMU-Cognitive-Stack/tree/d7a661635a0f8f337437d0ac9aa026375297c52b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
