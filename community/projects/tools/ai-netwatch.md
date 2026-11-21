# AI NetWatch by Sammi De Blas (Windows monitor of connections to AI cloud providers, triaged by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A local Windows dashboard (Spanish UI) that shows which processes connect to AI providers (OpenAI, Anthropic, Google, TypeSafe, OpenRouter and more): destination, SNI, protocol and timing patterns, with Jev triaging each event (confirm, refute, insufficient) to spot shadow AI, an optional local second opinion, an LLM inspector and JSON/CSV export.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PoisonXploIT/ai-netwatch) |
| Maintainer | [PoisonXploIT](https://github.com/PoisonXploIT). Independently curated. |
| Format | Python local web app (Windows) |
| Requirements | Windows, Python; Sysmon optional for full process paths; a TypeSafe key for Jev triage (stored encrypted with DPAPI). |
| License | [MIT](https://github.com/PoisonXploIT/ai-netwatch/blob/c4db20fef03395158ec9ff359b9f7163b7303a48/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_triage.py`](https://github.com/PoisonXploIT/ai-netwatch/blob/c4db20fef03395158ec9ff359b9f7163b7303a48/jev_triage.py) at the pinned commit. |

## When to use

- See which local apps talk to AI clouds and get a typed first-pass triage of suspicious traffic.
- Mismatch: macOS/Linux or network-wide monitoring; it watches the local Windows host.

## How it works

`jev_triage.py` sends aggregated connection metadata (process, destination, timing pattern) to `https://api.typesafe.ai/v1/systemone` as typed questions; the UI compares Jev's verdicts with an optional local fine-tuned model. Integration evidence: [`jev_triage.py`](https://github.com/PoisonXploIT/ai-netwatch/blob/c4db20fef03395158ec9ff359b9f7163b7303a48/jev_triage.py).

## Get started

Create the Python 3.12 environment on Windows and start the local server as the README describes (the author ships PowerShell service scripts written for his machine); Sysmon and the bytes collector are optional.

```sh
git clone https://github.com/PoisonXploIT/ai-netwatch && cd ai-netwatch
uv venv --python 3.12
uv pip install fastapi uvicorn
# start the server per the README, then open http://127.0.0.1:8790 and save your Jev key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/PoisonXploIT/ai-netwatch/blob/c4db20fef03395158ec9ff359b9f7163b7303a48/README.md](https://github.com/PoisonXploIT/ai-netwatch/blob/c4db20fef03395158ec9ff359b9f7163b7303a48/README.md)

## Limits and data handling

Connection metadata (process names, domains, timing) is sent to TypeSafe for triage. Spanish-language UI and docs.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit c4db20fef033](https://github.com/PoisonXploIT/ai-netwatch/tree/c4db20fef03395158ec9ff359b9f7163b7303a48). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
